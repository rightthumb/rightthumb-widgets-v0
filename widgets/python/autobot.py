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
import sys
import requests
import time
import threading
from datetime import datetime
from bs4 import BeautifulSoup
import openai

# Load your OpenAI key securely
OPENAI_KEY_PATH = os.path.expanduser("~/.rt/.config.hash")
if os.path.exists(OPENAI_KEY_PATH):
	with open(OPENAI_KEY_PATH) as f:
		config = json.load(f)
	openai.api_key = config.get('openai')

# start folders
if os.name == 'nt':
	BASE_DIR = os.path.join(os.environ['USERPROFILE'], 'bots')
else:
	BASE_DIR = '/opt/bots'

LOCK_PATH = os.path.join(BASE_DIR, 'library.lock')
LIBRARY_DB = os.path.join(BASE_DIR, 'library.db')
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')
PERMANENT_BK = os.path.join(BASE_DIR, 'library_bk.db')
FAIL_DIR = os.path.join(BASE_DIR, 'fail')
NEXT_ID_FILE = os.path.join(BASE_DIR, 'nextID.txt')
THREAD_INDEX_FILE = os.path.join(BASE_DIR, 'thread_index.json')

required_dirs = [
	BASE_DIR,
	BACKUP_DIR,
	FAIL_DIR
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
	def __init__(self, model="gpt-4o", recover_only=False, project_path=None, max_threads=190):
		self.model = model
		self.project_root = BASE_DIR
		self.fail_dir = FAIL_DIR

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

		self.db = duckdb.connect(self.db_path)
		self.init_project_db()

		self.resources_db = duckdb.connect(self.resources_db_path)
		self.init_resources_db()

		self.thread_manager = ThreadManager(max_threads=max_threads)

	def next_project_id(self):
		if os.path.exists(NEXT_ID_FILE):
			with open(NEXT_ID_FILE) as f:
				return int(f.read().strip())
		else:
			return 1

	def update_next_id(self):
		with open(NEXT_ID_FILE, "w") as f:
			f.write(str(int(self.project_id) + 1))

	def safe_backup_library(self):
		if os.path.exists(LIBRARY_DB):
			backup_file = os.path.join(BACKUP_DIR, f"library_{self.project_id}.db")
			shutil.copy2(LIBRARY_DB, backup_file)
			if not os.path.exists(PERMANENT_BK):
				shutil.copy2(LIBRARY_DB, PERMANENT_BK)

	def init_library(self, db):
		db.execute("""CREATE TABLE IF NOT EXISTS os_tasks (id INTEGER, context TEXT, command TEXT, result TEXT, tags TEXT, origin TEXT, rank INTEGER, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
		db.execute("""CREATE TABLE IF NOT EXISTS python_tasks (id INTEGER, context TEXT, code TEXT, result TEXT, tags TEXT, origin TEXT, rank INTEGER, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
		db.execute("""CREATE TABLE IF NOT EXISTS logistics (id INTEGER, purpose TEXT, description TEXT, details TEXT, rank INTEGER, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
		db.execute("""CREATE TABLE IF NOT EXISTS prompt_archive (id INTEGER, role TEXT, context TEXT, prompt TEXT, model TEXT, tags TEXT, rank INTEGER, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")

	def init_project_db(self):
		self.db.execute("""CREATE TABLE IF NOT EXISTS log (task_id INTEGER, step TEXT, result TEXT);""")

	def init_resources_db(self):
		self.resources_db.execute("""CREATE TABLE IF NOT EXISTS resources (id INTEGER, db_name TEXT, table_name TEXT, fields TEXT, description TEXT, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")

	def chatgpt(self, instruction):
		response = openai.ChatCompletion.create(
			model=self.model,
			messages=[
				{"role": "system", "content": "You are a helpful assistant."},
				{"role": "user", "content": instruction}
			],
			temperature=0,
			max_tokens=3000
		)
		return response['choices'][0]['message']['content']

	def plan_resources_for_task(self, task_text):
		instruction = f"""
Analyze the following task and suggest needed database resources in JSON:

[
	{{
		"db": "database_name.db",
		"table": "table_name",
		"record": {{"field1": "", "field2": "", "field3": ""}},
		"tag_path": "folder/path/to/resource",
		"description": "Brief description."
	}}
]

TASK:
{task_text}

If no database needed, output []
"""
		try:
			response = self.chatgpt(instruction)
			start_idx = response.index('[')
			end_idx = response.rindex(']') + 1
			proposals = json.loads(response[start_idx:end_idx])
			for proposal in proposals:
				self.create_or_update_resource(
					db=proposal["db"],
					table=proposal["table"],
					record=proposal["record"],
					tag_path=proposal["tag_path"],
					description=proposal["description"]
				)
		except Exception as e:
			print(f"❌ Resource planning failed: {e}")

	def create_or_update_resource(self, db, table, record, tag_path="", description=""):
		db_path = os.path.join(self.project_path, db)
		conn = duckdb.connect(db_path)
		tables = conn.execute("SHOW TABLES").fetchall()
		tables = [t[0].lower() for t in tables]

		if table.lower() not in tables:
			fields_sql = ", ".join([f"{k} TEXT" for k in record.keys()])
			conn.execute(f"CREATE TABLE {table} ({fields_sql});")
			self.resources_db.execute("INSERT INTO resources (db_name, table_name, fields, description) VALUES (?, ?, ?, ?)",
				(db, table, ", ".join(record.keys()), tag_path + " - " + description))
		else:
			existing_cols = conn.execute(f"DESCRIBE {table}").fetchall()
			existing_cols = [col[0] for col in existing_cols]
			for field in record.keys():
				if field not in existing_cols:
					conn.execute(f"ALTER TABLE {table} ADD COLUMN {field} TEXT;")
		conn.close()
		self.resources_db.commit()

	def run_task(self, task_text):
		self.plan_resources_for_task(task_text)
		instruction = f"""
You are helping with this task:
\"\"\"
{task_text}
\"\"\"
If code, return code blocks. Otherwise, describe the result.
"""
		response = self.chatgpt(instruction)
		output_file = os.path.join(self.project_path, "results", f"task_{int(time.time())}.txt")
		with open(output_file, "w", encoding="utf-8") as f:
			f.write(response)
		print(f"✅ Task completed and saved: {task_text[:60]}...")

	def run_sprint(self, tasks):
		for i, task in enumerate(tasks, 1):
			print(f"🔹 Running Task {i}/{len(tasks)}: {task}")
			try:
				self.run_task(task)
			except Exception as e:
				print(f"❌ Error in task {i}: {e}")

if __name__ == "__main__":
	recover_only = "--recover-only" in sys.argv
	project_path = None
	goal = None

	for i, arg in enumerate(sys.argv):
		if arg == "--project-path" and i + 1 < len(sys.argv):
			project_path = sys.argv[i + 1]
		if arg == "--goal" and i + 1 < len(sys.argv):
			goal = sys.argv[i + 1]

	if not any(["--project-path" in arg or "--goal" in arg for arg in sys.argv]):
		print("""
Usage:
  python3 bot.py --recover-only
  python3 bot.py --project-path /path/to/project
  python3 bot.py --goal "Create a file organizer"
""")
		sys.exit(0)

	try:
		bot = AIBot(recover_only=recover_only, project_path=project_path)
		if goal and not recover_only:
			print(f"🚀 Creating project with goal: {goal}")
			# Implement your own create_project and split_goal_into_tasks if needed
		if not recover_only:
			bot.thread_manager.run()
			print("✅ Bot and Thread Manager running.")
	except KeyboardInterrupt:
		print("\n❌ Ctrl+C detected. Exiting gracefully...")
		sys.exit(0)
