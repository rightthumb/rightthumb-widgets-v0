try:
	from nltk.stem import PorterStemmer  # type: ignore
	stemmer = PorterStemmer()
except:
	stemmer = None

def get_stems(text):
	if stemmer is None:
		return text
	words = text.split()
	stems = [stemmer.stem(word) for word in words]
	return " ".join(stems)

def query_log_jsonl(log_file_path, query_sql="SELECT * FROM read_json_auto(?)"):
	conn = duckdb.connect()
	try:
		result = conn.execute(query_sql, [log_file_path]).fetchall()
		return result
	except Exception as e:
		print(f"❌ Query error: {e}")
		return []
	finally:
		conn.close()

import os
import json
import re
import subprocess
import shutil
import duckdb
import importlib.util
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import sys
import requests
import time
import threading
from datetime import datetime
from bs4 import BeautifulSoup

# start folders
if os.name == 'nt':
	BASE_DIR = os.path.join(os.environ['USERPROFILE'], 'bots')
else:
	BASE_DIR = '/opt/bots'

# Define paths
LOCK_PATH = os.path.join(BASE_DIR, 'library.lock')
LIBRARY_DB = os.path.join(BASE_DIR, 'library.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')
PERMANENT_BK = os.path.join(BASE_DIR, 'library_bk.db')
FAIL_DIR = os.path.join(BASE_DIR, 'fail')
NEXT_ID_FILE = os.path.join(BASE_DIR, 'nextID.txt')
THREAD_INDEX_FILE = os.path.join(BASE_DIR, 'thread_index.json')

# Ensure all necessary directories exist
required_dirs = [
	BASE_DIR,
	os.path.dirname(LOCK_PATH),
	os.path.dirname(LIBRARY_DB),
	BACKUP_DIR,
	os.path.dirname(PERMANENT_BK),
	FAIL_DIR,
	os.path.dirname(NEXT_ID_FILE),
	os.path.dirname(THREAD_INDEX_FILE)
]

for directory in required_dirs:
	if not os.path.exists(directory):
		os.makedirs(directory, exist_ok=True)
# end folders

class ThreadManager:
	def __init__(self, max_threads=190):
		self.queue = []
		self.index = 0
		self.max_threads = max_threads
		self.threads = []
		self.save_interval = 30
		threading.Thread(target=self.background_saver, daemon=True).start()

	def queue_task(self, func, args=()):
		self.queue.append({"func": func, "args": args})

	def run(self):
		while self.index < len(self.queue):
			active_threads = [t for t in self.threads if t.is_alive()]
			if len(active_threads) < self.max_threads:
				item = self.queue[self.index]
				t = threading.Thread(target=item["func"], args=item["args"])
				t.start()
				self.threads.append(t)
				self.index += 1
			else:
				time.sleep(0.5)

	def background_saver(self):
		while True:
			with open(THREAD_INDEX_FILE, "w") as f:
				json.dump({"index": self.index}, f)
			time.sleep(self.save_interval)

	def recover(self):
		try:
			with open(THREAD_INDEX_FILE) as f:
				data = json.load(f)
				self.index = data.get("index", 0)
		except:
			self.index = 0

class LibraryLock:
	def __init__(self, project_id):
		self.project_id = project_id

	def wait(self):
		while os.path.exists(LOCK_PATH):
			if time.time() - os.path.getmtime(LOCK_PATH) > 60:
				os.remove(LOCK_PATH)
				break
			time.sleep(2)

	def acquire(self):
		self.wait()
		with open(LOCK_PATH, "w") as f:
			f.write(json.dumps({"project": self.project_id, "ts": time.time()}))

	def release(self):
		if os.path.exists(LOCK_PATH):
			os.remove(LOCK_PATH)

import threading

def query_log_jsonl(log_file_path, query_sql="SELECT * FROM read_json_auto(?)"):
	conn = duckdb.connect()
	try:
		result = conn.execute(query_sql, [log_file_path]).fetchall()
		return result
	except Exception as e:
		print(f"❌ Query error: {e}")
		return []
	finally:
		conn.close()

class AIBot:
	def __init__(self, model_id="HuggingFaceH4/zephyr-7b-beta", recover_only=False, project_path=None, max_threads=190):
		self.project_root = BASE_DIR
		os.makedirs(self.project_root, exist_ok=True)
		os.makedirs(FAIL_DIR, exist_ok=True)

		if project_path:
			self.project_path = project_path
			self.project_id = os.path.basename(project_path)
		else:
			self.project_id = self.next_project_id()
			self.project_path = os.path.join(self.project_root, str(self.project_id))
			os.makedirs(self.project_path, exist_ok=True)
			self.update_next_id()

		self.db_path = os.path.join(self.project_path, "project.duckdb")
		self.resources_db_path = os.path.join(self.project_path, "resources.db")
		self.personal_library_path = os.path.join(self.project_path, "library.db")
		os.makedirs(os.path.join(self.project_path, "results"), exist_ok=True)

		self.lock = LibraryLock(self.project_id)
		self.lock.acquire()
		self.safe_backup_library()
		if recover_only:
			self.lock.release()
			print("Recovery mode completed.")
			exit(0)

		self.library = duckdb.connect(LIBRARY_DB)
		self.init_library(self.library)

		self.personal_library = duckdb.connect(self.personal_library_path)
		self.init_library(self.personal_library)

		self.lock.release()

		self.model_id = model_id
		self.tokenizer = AutoTokenizer.from_pretrained(model_id)
		self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

		self.db = duckdb.connect(self.db_path)
		self.init_project_db()

		self.resources_db = duckdb.connect(self.resources_db_path)
		self.init_resources_db()

		self.thread_manager = ThreadManager(max_threads=max_threads)

	def update_next_id(self):
		with open(NEXT_ID_FILE, "w") as f:
			f.write(str(int(self.project_id) + 1))

	def safe_backup_library(self):
		if not os.path.exists(BACKUP_DIR):
			os.makedirs(BACKUP_DIR)
		if os.path.exists(LIBRARY_DB):
			backup_file = os.path.join(BACKUP_DIR, f"library_{self.project_id}.db")
			shutil.copy2(LIBRARY_DB, backup_file)
			if not os.path.exists(PERMANENT_BK):
				shutil.copy2(LIBRARY_DB, PERMANENT_BK)
			try:
				conn = duckdb.connect(LIBRARY_DB)
				for table in ["os_tasks", "python_tasks", "logistics", "prompt_archive"]:
					conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
				conn.close()
			except Exception as e:
				print(f"Corruption detected: {e}")
				self.recover_library()

	def recover_library(self):
		backups = sorted([os.path.join(BACKUP_DIR, f) for f in os.listdir(BACKUP_DIR) if f.endswith(".db")], key=os.path.getmtime, reverse=True)
		for backup in backups:
			try:
				conn = duckdb.connect(backup)
				conn.execute("SELECT COUNT(*) FROM os_tasks").fetchone()
				conn.close()
				shutil.copy2(backup, LIBRARY_DB)
				print(f"Recovered library.db from {backup}")
				return
			except:
				continue
		print("❌ Failed to recover library.db, no valid backups found.")

	def init_library(self, db):
		db.execute("""
			CREATE TABLE IF NOT EXISTS os_tasks (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				context TEXT, command TEXT, result TEXT,
				tags TEXT, origin TEXT, rank INTEGER DEFAULT 50,
				created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			);
		""")
		db.execute("""
			CREATE TABLE IF NOT EXISTS python_tasks (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				context TEXT, code TEXT, result TEXT,
				tags TEXT, origin TEXT, rank INTEGER DEFAULT 50,
				created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			);
		""")
		db.execute("""
			CREATE TABLE IF NOT EXISTS logistics (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				purpose TEXT, description TEXT, details TEXT,
				rank INTEGER DEFAULT 50,
				created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			);
		""")
		db.execute("""
			CREATE TABLE IF NOT EXISTS prompt_archive (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				role TEXT, context TEXT, prompt TEXT, model TEXT,
				tags TEXT, rank INTEGER DEFAULT 50,
				created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			);
		""")

	def init_project_db(self):
		self.db.execute("""
			CREATE TABLE IF NOT EXISTS log (
				task_id INTEGER,
				step TEXT,
				result TEXT
			);
		""")

	def init_resources_db(self):
		self.resources_db.execute("""
			CREATE TABLE IF NOT EXISTS resources (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				db_name TEXT,
				table_name TEXT,
				fields TEXT,
				description TEXT,
				created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			);
		""")

	def search_resources(self, keyword):
		query = f"""
			SELECT db_name, table_name, fields, description
			FROM resources
			WHERE
				db_name ILIKE '%{keyword}%'
				OR table_name ILIKE '%{keyword}%'
				OR fields ILIKE '%{keyword}%'
				OR description ILIKE '%{keyword}%'
			ORDER BY created DESC
		"""
		return self.resources_db.execute(query).fetchall()

	def create_or_update_resource(self, db, table, record, tag_path="", description=""):
		db_path = os.path.join(self.project_path, db)
		conn = duckdb.connect(db_path)

		tables = conn.execute("SHOW TABLES").fetchall()
		tables = [t[0].lower() for t in tables]

		if table.lower() not in tables:
			fields_sql = ", ".join([f"{k} TEXT" for k in record.keys()])
			conn.execute(f"CREATE TABLE {table} ({fields_sql});")
			self.resources_db.execute("""
				INSERT INTO resources (db_name, table_name, fields, description)
				VALUES (?, ?, ?, ?)
			""", (db, table, ", ".join(record.keys()), tag_path + " - " + description))
		else:
			existing_cols = conn.execute(f"DESCRIBE {table}").fetchall()
			existing_cols = [col[0] for col in existing_cols]
			for field in record.keys():
				if field not in existing_cols:
					conn.execute(f"ALTER TABLE {table} ADD COLUMN {field} TEXT;")

		conn.close()
		self.resources_db.commit()

	def run_sprint(self, tasks):
		for i, task in enumerate(tasks, 1):
			print(f"🔹 Running Task {i}/{len(tasks)}: {task}")
			try:
				self.run_task(task)
			except Exception as e:
				print(f"❌ Error in task {i}: {e}")

	def log_event(self, event_type, message, data=None):
		log_file = os.path.join(self.project_path, "log.jsonl")
		event = {
			"timestamp": datetime.utcnow().isoformat(),
			"epoch": int(time.time()),
			"event": event_type,
			"message": message,
			"data": data
		}
		try:
			with open(log_file, "a", encoding="utf-8") as f:
				f.write(json.dumps(event) + "\n")
			print(f"✅ Logged: {event_type} - {message[:60]}...")
		except Exception as e:
			print(f"❌ Logging failed: {e}")

	def run_task(self, task_text):
		self.plan_resources_for_task(task_text)

		instruction = f"""
You are a smart assistant working on the following task:
\"\"\"
{task_text}
\"\"\"

Please complete the task carefully. If code, return code blocks. If description, return plain text.
"""
		inputs = self.tokenizer(instruction, return_tensors="pt")
		inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
		outputs = self.model.generate(**inputs, max_new_tokens=1500)
		response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

		output_file = os.path.join(self.project_path, "results", f"task_{int(time.time())}.txt")
		with open(output_file, "w", encoding="utf-8") as f:
			f.write(response)

		print(f"✅ Task completed and saved: {task_text[:60]}...")

	def plan_resources_for_task(self, task_text):
		instruction = f"""
You are assisting a project bot. Analyze the following task and suggest any needed database resources.
If any are needed, output in this exact JSON format:

[
	{{
		"db": "database_name.db",
		"table": "table_name",
		"record": {{
			"field1": "",
			"field2": "",
			"field3": ""
		}},
		"tag_path": "folder/path/to/resource",
		"description": "Brief description of what this table stores."
	}}
]

TASK:
{task_text}

ONLY output valid JSON.
If no database or table is needed, output an empty list: []
"""
		inputs = self.tokenizer(instruction, return_tensors="pt")
		inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
		outputs = self.model.generate(**inputs, max_new_tokens=1500)
		response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

		# Attempt to isolate JSON if model returns extra text
		try:
			start_idx = response.index('[')
			end_idx = response.rindex(']') + 1
			json_text = response[start_idx:end_idx]
			proposals = json.loads(json_text)
		except Exception as e:
			print(f"❌ Failed to parse resource plan: {e}")
			return

		# Process proposals
		for proposal in proposals:
			self.create_or_update_resource(
				db=proposal["db"],
				table=proposal["table"],
				record=proposal["record"],
				tag_path=proposal["tag_path"],
				description=proposal["description"]
			)

		

if __name__ == "__main__":
	recover_only = "--recover-only" in sys.argv
	project_path = None
	goal = None

	found = False
	for i, arg in enumerate(sys.argv):
		if arg == "--project-path" and i + 1 < len(sys.argv):
			found = True
			project_path = sys.argv[i + 1]
		if arg == "--goal" and i + 1 < len(sys.argv):
			found = True
			goal = sys.argv[i + 1]

	if not found:
		print("""
Usage:
  python3 bot.py --recover-only                  # Recover only, no project execution
  python3 bot.py --project-path /path/to/project  # Use specific project path
  python3 bot.py --goal "Create a file organizer"  # Start and run a project with a goal
  python3 bot.py                                  # Start normally and create next project ID
""")
		sys.exit(0)

	try:
		bot = AIBot(recover_only=recover_only, project_path=project_path)
		if goal and not recover_only:
			print(f"🚀 Creating project with goal: {goal}")
			bot.create_project(goal)
			tasks = bot.split_goal_into_tasks(goal)
			if tasks:
				bot.run_sprint(tasks)
		if not recover_only:
			bot.thread_manager.run()
			print("✅ Bot and Thread Manager running.")
	except KeyboardInterrupt:
		print("\n❌ Ctrl+C detected. Exiting gracefully...")
		sys.exit(0)
