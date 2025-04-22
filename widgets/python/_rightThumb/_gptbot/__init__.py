#!/usr/bin/python3

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##


##################################################
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')
##################################################

# app_navigator: switches
def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i', group='Group Name' )
		##  -->    p SwitchGroupsExamples   <--
	# #e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

_._default_settings_()

# __.setting('pipe-cleaner',False)
# __.setting('pipe-cleaner', {'first': False})

# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()

	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	# _.switches.trigger( 'Files', _.isFileSimple )                 # No File Registration          (Fn Alias Resolves To: def isFile)
	
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> caseUnspecific
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)
		#     or
		# results = [rel for rel in [subject for subject in _.isData(r=0) if _.showLine(subject)]]


	#n)--> fields
		# data = []
		# for k in code.db: data.append({'name': k+'  ' })
		# _.fields.asset( 'data', data )
		# for k in code.db:
		# 	_.pr(   _.fields.value( 'data', 'name', k+':' )+'  '+str(len(code.db[k]))   )

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start





import os, json, re, subprocess
from openai import OpenAI # type: ignore
import shutil


class GPT4oBot:
	def __init__(self, memory_file='memory.json', sprint_task_limit=3, os_interaction=False, app=None, hasFiles=False, getDistro=False):
		self.memory_file = memory_file
		self.sprint_task_limit = sprint_task_limit
		self.os_interaction = os_interaction
		self.app = app
		self.hasFiles = hasFiles
		self.getDistro = getDistro

		self.api_key = _v.fig['openai']
		self.client = OpenAI(api_key=self.api_key)

		self.mem = self.load_memory()

		if self.getDistro:
			self.distro = self.get_distro_name()
			print(f"🖥️ Detected distro: {self.distro}")

	def get_distro_name(self):
		try:
			import distro # type: ignore
			return distro.id()
		except Exception as e:
			return f"unknown ({e})"

	def load_memory(self):
		if not os.path.exists(self.memory_file):
			return {"goal": "", "sprints": [], "history": []}
		with open(self.memory_file) as f:
			return json.load(f)

	def save_memory(self):
		with open(self.memory_file, "w") as f:
			json.dump(self.mem, f, indent=4)

	def prompt(self, text):
		print("\n🤖 GPT Prompting...\n====================\n")
		print(text.strip())
		print("\n====================")
		res = self.client.chat.completions.create(
			model="gpt-4o",
			messages=[{"role": "user", "content": text}],
			max_tokens=4096,  # Or 8192 if using a higher-capacity tier
			temperature=0.7,
		)

		response = res.choices[0].message.content.strip()
		print("\n✅ GPT Response:\n--------------------\n")
		print(response)
		print("\n--------------------\n")

		if self.os_interaction:
			self.extract_and_execute_code_blocks(response)

		return response

	def extract_and_execute_code_blocks(self, text):
		code_blocks = re.findall(r"```(.*?)\n(.*?)```", text, re.DOTALL)
		for lang, code in code_blocks:
			code = code.strip()
			lang = lang.strip().lower()
			# files = self.extract_files(text, lang, code)
			files = self.extract_files(text)
			if files:
				for filename in files:
					file_code = files[filename]
					print(f"\n💾 Saving: {filename}\n")
					folder = os.path.dirname(filename)
					if folder and not os.path.exists(folder):
						os.makedirs(folder)
					with open(filename, 'w') as f:
						f.write(file_code)
					if self.hasFiles and lang == "py":
						print(f"🚀 Running: {filename}")
						if shutil.which("python3.11"):
							subprocess.run(["python3.11", filename])
						else:
							subprocess.run(["python3", filename])

					if self.hasFiles and lang == "py":
						print(f"🚀 Running: {filename}")
						subprocess.run(["python3", filename])
					if lang == "sh" and self.app == "rust":
						if 'cargo build' in code:
							self.rust_build_loop()

	def extract_files(self, text):
		files = {}
		current_filename = None
		inside_code_block = False
		code_lines = []

		lines = text.splitlines()
		for line in lines:
			stripped = line.strip()

			# Detect start of new file block
			if stripped.startswith("### filename:"):
				if current_filename and code_lines:
					files[current_filename] = "\n".join(code_lines).strip()
					code_lines = []

				current_filename = stripped[len("### filename:"):].strip()
				inside_code_block = False  # Reset in case previous block didn't close properly

			elif stripped.startswith("```") and current_filename:
				# Toggle inside_code_block
				inside_code_block = not inside_code_block
				if not inside_code_block:
					# End of code block – save current file
					files[current_filename] = "\n".join(code_lines).strip()
					current_filename = None
					code_lines = []

			elif inside_code_block and current_filename:
				code_lines.append(line)

		# Handle case where last file isn't followed by closing ```
		if current_filename and code_lines and current_filename not in files:
			files[current_filename] = "\n".join(code_lines).strip()

		return files


	def rust_build_loop(self):
		print("\n🔁 Running Rust build loop...")
		for cmd in ["cargo clean", "cargo update"]:
			subprocess.run(cmd.split(), capture_output=True)
		while True:
			result = subprocess.run(["cargo", "build", "--release"], capture_output=True, text=True)
			if result.returncode == 0:
				print("✅ Rust build succeeded!")
				break
			else:
				print("❌ Build error detected, sending to GPT for fix...")
				fix_prompt = f"Rust build error:\n\n{result.stderr}\n\nRefactor the code to fix this. Provide updated file blocks with ### filename: name.rs and ```rust``` blocks."
				fix_response = self.prompt(fix_prompt)
				if 'no fix' in fix_response.lower():
					break

	def init_goal(self, goal=None):
		GOAL = goal
		while '  ' in GOAL: GOAL = GOAL.replace('  ', ' ')
		if 'create' in goal.lower():
			self.hasFiles = True
			if 'rust' in goal.lower():
				self.app = 'rust'
		if self.mem["goal"]:
			return self.mem["goal"]
		if goal:
			self.mem["goal"] = goal
		else:
			goal = input("Enter a project goal or leave blank for GPT to create one: ").strip()
			if not goal:
				goal = self.prompt("Give me a creative software project idea.")
			self.mem["goal"] = goal
		self.save_memory()
		return self.mem["goal"]

	def create_sprint(self):
		if any(s["status"] == "active" for s in self.mem["sprints"]):
			return
		

		history = "\n".join([h["summary"] for h in self.mem["history"][-3:]])
		prompt = f"""
You are assisting with the software project: {self.mem['goal']}

Recent progress summary:
{history}

Create a new sprint. Use this format:
SPRINT: [Sprint Title]
- Task 1
- Task 2
- Task 3


Each task should represent meaningful progress toward the project goal.
Avoid overly generic tasks. Be specific and actionable.
"""

		response = self.prompt(prompt)
		lines = response.strip().splitlines()
		if self.hasFiles:
			lines.append("- Ensure all relevant files are saved and up-to-date.")
		title = lines[0].replace("SPRINT:", "").strip()
		tasks = [line.strip("- ").strip() for line in lines[1:] if line.strip()]
		sprint = {"title": title, "status": "active", "tasks": [{"task": t, "status": "pending"} for t in tasks]}
		self.mem["sprints"].append(sprint)
		self.save_memory()

	def run_next_task(self):
		file_instruction = ''
		if self.hasFiles:
			file_instruction = """
- If the task includes files, follow the formatting rules below.
			
If you include any code that should be saved to disk:
- Start with a line formatted exactly like this: ### filename: [relative/path/to/file.extension]
- Follow it with a triple backtick code block using the correct language identifier (e.g., ```python, ```html, ```sh)
   - e.g., src/main.rs for Rust projects (this prompt is not language specific and used for all languages)
- Only include the files that should actually be written or updated
- Do not explain the code outside of the file block unless necessary for task context
- Include entire file contents when filename is provided (important)
- Include files with names for all files referenced in code
- html files should be html javascript files should be javascript etc

"""
			file_instruction = """
📝 File Output Instructions:

If the task includes code that should be saved:

1. Begin each file with a line exactly like this:
   ### filename: relative/path/to/file.extension

2. Immediately follow it with a properly tagged code block using the correct language:
   - HTML:       ```html
   - JavaScript: ```javascript
   - CSS:        ```css
   - Python:     ```python
   - Shell:      ```sh
   - Rust:       ```rust

3. Do not use ```text or omit the language — always use the matching language tag based on the file extension.

4. Include **entire file contents**, not snippets.

5. Only include files that need to be saved or updated.

6. If your code references other files, include those too using the same format.

7. Do not embed unrelated explanation inside the code block. If absolutely necessary, keep commentary outside and minimal.

❗ Avoid saving JavaScript or CSS in .html files unless explicitly required. Each file must match its purpose and extension.
"""

			file_instruction = """
📝 File Output Instructions:

If this task includes code that should be saved:

1. Start each file block with:
   ### filename: relative/path/to/file.extension

2. Immediately follow it with a properly tagged code block using the correct language:
   - HTML:       ```html
   - JavaScript: ```javascript
   - CSS:        ```css
   - Python:     ```python
   - Shell:      ```sh
   - Rust:       ```rust

3. Always match the language to the file type. Never use ```text or omit the language tag.

4. Include the **full contents** of each file. Do not send only partial code or diffs.

5. IMPORTANT: Save a **single file** when possible. Consolidate logic where appropriate.
   - The fewer files you save, the more reliable and efficient the process.
   - Only split into multiple files when absolutely necessary (e.g., separate HTML, JS, and CSS files when modularity matters).

6. Do not include unrelated explanation inside the code blocks. If needed, keep commentary minimal and outside the block.

7. If code references other files (like linked JS or CSS), include them too using the same format.

🚫 Do not embed JavaScript or CSS inside HTML unless the file is intended to be self-contained. Use `.js` and `.css` files for modular structure unless otherwise specified.
"""



		active_sprint = next((s for s in self.mem["sprints"] if s["status"] == "active"), None)
		if not active_sprint:
			self.create_sprint()
			self.mem = self.load_memory()
			active_sprint = next((s for s in self.mem["sprints"] if s["status"] == "active"), None)

		pending = [t for t in active_sprint["tasks"] if t["status"] == "pending"]
		if not pending:
			active_sprint["status"] = "done"
			self.save_memory()
			return None, f"Sprint '{active_sprint['title']}' completed."

		task = pending[0]["task"]
		history = "\n".join([h["summary"] for h in self.mem["history"][-3:]])
		prompt = f"""
PROJECT: {self.mem['goal']}
SPRINT: {active_sprint['title']}
TASK: {task}

RECENT HISTORY:
{history}

Instructions:
- Complete the above task.
- If the task reveals new requirements or follow-up tasks, briefly mention them at the end.

{file_instruction}
"""

		result = self.prompt(prompt)

		print(f"\n🚀 Completed Task: {task}\n")
		pending[0]["status"] = "done"
		self.mem["history"].append({"task": task, "summary": result})
		self.save_memory()

		return task, result

	def status(self):
		return {
			"goal": self.mem["goal"],
			"active_sprint": next((s for s in self.mem["sprints"] if s["status"] == "active"), None),
			"history": self.mem["history"][-3:]
		}



















### Example Usage Script (not part of package): run_bot.py
# from gptbot import GPT4oBot

# bot = GPT4oBot()

# project_goal = "Build a Telegram bot that sends daily motivational quotes."
# bot.init_goal(goal=project_goal)

# while True:
#     task, result = bot.run_next_task()
#     if not task:
#         print(result)
#         break
#     print(f"\n✅ Completed: {task}\n{result}\n")
#     input("Press Enter to continue...")



def action():
	pass

	# load(); global c3po;

	# Threads = _.Threads(t=10, onDone=None)
	# def Done(result): pass  # other onFn have no args
	# Threads.queue(fn,  ak=None, timeout=None, onStart=None, onDone=Done, onKill=None, onTimeout=None, label=None)  # ak = args, kwargs

	#n)--> iterate
	# for subject in _.isData(r=0): _.pr(subject)
	# for subject in _.myData(): _.pr(subject)
	

# def load():
# 	global c3po
# 	c3po = _.getTable( 'table' )
# 	#n)--> print table
# 	_.pt(c3po)


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__)

