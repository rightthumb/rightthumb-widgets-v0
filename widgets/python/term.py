import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
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
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


# on event stuff
# what is possible
if False:

	import _rightThumb._bookmarks as _bm
	import subprocess
	import os
	import sys
	import signal
	import shutil
	import socket
	import random
	import readline
	import atexit
	import time
	from prompt_toolkit import prompt # type: ignore
	from prompt_toolkit.styles import Style # type: ignore
	from prompt_toolkit.formatted_text import FormattedText  # type: ignore
	from datetime import datetime
	import re
	from prompt_toolkit.completion import Completer, Completion  # type: ignore
	from prompt_toolkit.buffer import Buffer  # type: ignore




	if os.name != 'nt':
		import readline
		import atexit
	class TerminalProxy:

		def __init__(self):
			self.isActive = True
			self.emoji = random.choice(['🐞', '🌭', '🦴', '🧠', '⚡', '🛠️', '🔥'])
			self.user = os.getenv("USERNAME") or os.getenv("USER") or "user"
			self.host = self.get_hostname()
			self.emoji = "🐞"
			self.events = OnEventLogger(self)
			self.shell = self.detect_shell()
			self.aliases=_.getTable('file-open-aliases.hash')
			self.clean_history_file()
			from prompt_toolkit.history import FileHistory  # type: ignore

			history_path = os.path.expanduser(self.ptermHistory())

			# print(self.ptermHistory())
			# sys.exit(0)

			# Ensure history file exists before using FileHistory
			if not os.path.exists(self.ptermHistory()):
				with open(self.ptermHistory(), 'w', encoding='utf-8') as f:
					pass  # create empty history file

			# Now initialize history
			self.history = FileHistory(self.ptermHistory())





			# self.style = Style.from_dict({
			# 	'prompt': '#ff0066 bold',
			# 	'user_input': 'ansicyan'
			# })

			self.style = Style.from_dict({
				'prompt': '#b4009e bold',     # Accurate color from your screenshot
				'user_input': 'ansicyan'      # Still a nice complement
			})

			if not 'aliases' in self.aliases: self.aliases['aliases'] = {}
			os.environ['pterm'] = 'true'
			if os.name != 'nt':
				self.history_file = os.path.expanduser("~/.pterm_history")
				self.setup_history()
				signal.signal(signal.SIGTSTP, signal.SIG_IGN)
				if hasattr(signal, 'SIGTTIN'):
					signal.signal(signal.SIGTTIN, signal.SIG_IGN)
				if hasattr(signal, 'SIGTTOU'):
					signal.signal(signal.SIGTTOU, signal.SIG_IGN)
			signal.signal(signal.SIGINT, self.sigint_handler)


		def get_history_commands(self):
			history_path = os.path.expanduser(self.ptermHistory())
			commands = []

			# Read and clean the raw history content
			with open(history_path, 'r', encoding='utf-8') as f:
				file_content = f.read()
			file_content = clean_history_file_content(file_content)

			# Parse the cleaned lines
			session = None
			timestamp = None
			for line in file_content.splitlines():
				if line.startswith('#'):
					match = re.match(r'# (.*?) \| session:(.*)', line)
					if match:
						timestamp, session = match.groups()
				elif line.startswith('+'):
					commands.append({
						'command': line[1:].strip(),
						'session': session,
						'time': timestamp
					})
			return commands


		def clean_history_file(path):
			try:
				with open(path, 'r', encoding='utf-8') as f:
					content = f.read()
				# Remove carriage returns and ANSI
				content = content.replace('\r', '')
				content = clean_history_file_content(content)
				with open(path, 'w', encoding='utf-8') as f:
					f.write(content)
			except Exception as e:
				print(f"[pterm] ⚠️ Failed to clean history file: {e}")


		def clean_history_file_content(raw: str):
			# Normalize line endings (just in case)
			raw = raw.replace(chr(10), '\n')

			# Remove ANSI escape codes (colors, cursor moves, etc.)
			ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
			raw = ansi_escape.sub('', raw)

			return raw




		def add_to_history(self, command: str):
			if not command.strip():
				return

			try:
				if hasattr(self.history, 'append_string'):
					self.history.append_string(command.strip())

					# Include metadata with SESSION_ID or fallback to __.startTime
					session_id = os.environ.get('SESSION_ID', getattr(__, 'startTime', 'unknown'))
					entry = f"# {datetime.now().isoformat()} | session:{session_id}\n+{command.strip()}\n"

					with open(self.ptermHistory(), 'a', encoding='utf-8') as f:
						f.write(entry)

			except Exception as e:
				print(f"[pterm] ⚠️ Failed to add to history: {e}")



		def setup_history(self):
			try:
				readline.read_history_file(self.history_file)
			except FileNotFoundError:
				pass
			atexit.register(readline.write_history_file, self.history_file)

		def get_hostname(self):
			if os.name == "nt":
				return os.environ.get("COMPUTERNAME", "PC")
			else:
				try:
					with open("/etc/hostname") as f:
						return f.read().strip()
				except:
					return socket.gethostname()

		def pterm(self):
			if os.name == 'nt':
				home = os.getenv('USERPROFILE') or os.path.expanduser('~')
				return home.rstrip('\\') + '\\' + '.pterm'
			else:
				home = os.getenv('HOME') or os.path.expanduser('~')
				return home.rstrip('/') + '/' + '.pterm'

		def ptermHistory(self):
			if os.name == 'nt':
				home = os.getenv('USERPROFILE') or os.path.expanduser('~')
				return home.rstrip('\\') + '\\' + '.pterm_history'
			else:
				home = os.getenv('HOME') or os.path.expanduser('~')
				return home.rstrip('/') + '/' + '.pterm_history'


		def detect_shell(self):
			if os.name == "nt":
				return "cmd.exe"
			else:
				return os.environ.get("SHELL", "/bin/bash")

		def sigint_handler(self, sig, frame):
			os.environ.pop('pterm', None)
			if hasattr(self, 'shell_proc') and self.shell_proc:
				self.shell_proc.terminate()
			print("\n[Exiting terminal proxy]")
			sys.exit(0)


		def get_fancy_prompt(self):
			cwd = os.getcwd()
			home = os.path.expanduser('~')
			if cwd.startswith(home):
				cwd = cwd.replace(home, '~', 1)

			return FormattedText([
				('class:prompt', f"┌──({self.user}{self.emoji}{self.host})-[ {cwd} ]\n"),
				('class:prompt', "└─ ")
			])



		def change_directory(self, path):
			try:
				os.chdir(os.path.expandvars(os.path.expanduser(path)))
			except Exception as e:
				print(f"cd: {e}")

		def inject(self, command):
			if command.strip() == 'c':
				self.wasC = True
			else:
				self.wasC = False
			self.add_to_history(command)
			if command == 'exit': self.isActive = False
			if '.fi' in command or '.fo' in command or '.url' in command:
				parts = command.split()
				new = []
				for i, part in enumerate(parts):
					if not i:
						new.append(part)
						continue
					if part.endswith('.url'):
						part = part[:-len('.url')]
						path=_.url2file(part)
						if path and os.path.exists(path):
							part = path
					if part.endswith('.url.fo'):
						part = part[:-len('.url.fo')]
						path=_.url2file(part)
						path = __.path(path,pop=True)
						if path and os.path.exists(path):
							part = path
					elif part.endswith('.fi'):
						if part[:-3] in self.aliases['aliases']:
							part = self.aliases['aliases'][part[:-3]]
					elif part.endswith('.fo'):
						path = _bm.Bookmarks( part[:-3] ).get()
						if path and os.path.exists(path):
							part = path
					new.append(part)
				command = ' '.join(new)
			if os.name != 'nt':
				blocked = ['clear', 'reset', 'stty', 'tput', 'less', 'more']
				if any(command.strip().startswith(b) for b in blocked):
					return f'echo "[pterm] ⛔ blocked: {command.strip()}"'
			command += ' && pwd > ' + self.pterm()
			return command

		def run_command(self, command):
			command = self.inject(command)
			try:
				env = os.environ.copy()
				if os.name == 'nt':
					subprocess.run(['cmd.exe', '/c', command], shell=False, env=env)
					self.last_dir = _.getText(self.pterm(), raw=True, clean=2).strip()
					os.chdir(self.last_dir)
					print()
					
				else:
					bash_cmd = f'bash -i -c "{command}"'
					subprocess.run(bash_cmd, shell=True, env=env)
					self.last_dir = _.getText(self.pterm(), raw=True, clean=2).strip()
					os.chdir(self.last_dir)
					print()
					
			except Exception as e:
				print(f"[Error] {e}")

		def brand(self):
			return self.get_fancy_prompt()



		def correct_command(self, command):
			try:
				if hasattr(_, 'spellFix') and callable(_.spellFix):
					corrected = _.spellFix(command)
					if corrected != command:
						print(f"[pterm] 🧠 Corrected: {command} ➜ {corrected}")
						return corrected
			except Exception as e:
				print(f"[pterm] ⚠️ SpellFix failed: {e}")
			return command


		# def start(self):
		# 	os.system('cls' if os.name == 'nt' else 'clear')
		# 	__.touch = time.time()
		# 	self.show_brand_next = True  # show prompt at startup

		# 	# ✅ Ensure event bindings are initialized
		# 	if not hasattr(self, 'events'):
		# 		from OnEventLogger import OnEventLogger  # or define above if inline
		# 		self.events = OnEventLogger(self)

		# 	while self.isActive:
		# 		__.touch = time.time()
		# 		try:
		# 			# Show branding prompt (top bar, but no prompt text)
		# 			if self.show_brand_next:
		# 				prompt_text = self.brand()
		# 			else:
		# 				prompt_text = [('class:prompt', '└─ ')]

		# 			# ✅ Use prompt_toolkit with history + on-event tracking

		# 			buf = self.get_prompt_buffer()

		# 			command = prompt(
		# 				prompt_text,
		# 				style=self.style,
		# 				history=self.history,
		# 				key_bindings=self.events.get_bindings(),
		# 				buffer=buf
		# 			).strip()

		# 			# ✅ Expand shorthand here
		# 			command = self.expand_shorthand(command)


		# 			# ✅ Call your AI/pattern-correction here
		# 			command = self.correct_command(command)


					


		# 			if not command:
		# 				continue

		# 			if command.startswith("cd "):
		# 				self.change_directory(command[3:].strip())
		# 			else:
		# 				self.run_command(command)

		# 			self.show_brand_next = self.wasC  # Show branding again only if user typed `c`

		# 		except EOFError:
		# 			break
		# 		except Exception as e:
		# 			print(f"[Error] {e}")

		# 	self.isActive = False
		# 	_.isExit(__file__)  # ✅ Log terminal exit or session end








		def start(self):
			os.system('cls' if os.name == 'nt' else 'clear')
			__.touch = time.time()
			self.show_brand_next = True  # show prompt at startup

			# ✅ Ensure event bindings are initialized
			if not hasattr(self, 'events'):
				from OnEventLogger import OnEventLogger  # or define above if inline
				self.events = OnEventLogger(self)

			while self.isActive:
				__.touch = time.time()
				try:
					# Show branding prompt (top bar, but no prompt text)
					if self.show_brand_next:
						prompt_text = self.brand()
					else:
						prompt_text = [('class:prompt', '└─ ')]

					# ✅ Use prompt_toolkit with history + on-event tracking
					command = prompt(
						prompt_text,
						style=self.style,
						history=self.history,
						key_bindings=self.events.get_bindings()  # <--- ALL KEY EVENTS HOOKED HERE
					).replace('\r', '').strip()  # <-- Strip ^M characters from input

					# ✅ Process full input pipeline: expand shorthand + correct
					command = self.process_input(command)

					if not command:
						continue

					if command.startswith("cd "):
						self.change_directory(command[3:].strip())
					else:
						self.run_command(command)

					self.show_brand_next = self.wasC  # Show branding again only if user typed `c`

				except EOFError:
					break
				except Exception as e:
					print(f"[Error] {e}")

			self.isActive = False
			_.isExit(__file__)  # ✅ Log terminal exit or session end

		def expand_shorthand(self, command):
			# 🔧 Customize this map to your CLI shortcuts
			shortcuts = {
				'lsc': 'ls --color=auto',
				'gs': 'git status',
				'gcm': 'git commit -m ""',
				'c.': 'clear && echo "📂 $(pwd)"',
				'pyc': 'python3 -m compileall .',
			}
			if command in shortcuts:
				expanded = shortcuts[command]
				print(f"[pterm] ⏩ Expanded: {command} ➜ {expanded}")
				return expanded
			return command

		def process_input(self, command):
			command = self.expand_shorthand(command)
			command = self.correct_command(command)
			return command
















		def get_prompt_buffer(self):
			from prompt_toolkit.document import Document

			def on_text_changed(buf):
				# Optional: log text live here
				pass

			return Buffer(
				multiline=False,
				on_text_changed=on_text_changed
			)










	class MyCompleter(Completer):
		def get_completions(self, document, complete_event):
			text = document.text_before_cursor

			# Suggest commands or paths, for example:
			if text.startswith('ec'):
				yield Completion('echo', start_position=-len(text))
			if text.startswith('pyt'):
				yield Completion('python', start_position=-len(text))



	from prompt_toolkit.key_binding import KeyBindings
	from prompt_toolkit.keys import Keys


	from prompt_toolkit.key_binding import KeyBindings
	from prompt_toolkit.keys import Keys

	class OnEventLogger:
		def __init__(self, terminal):
			self.terminal = terminal
			self.kb = KeyBindings()
			self.bind_all_keys()

		def log(self, key_name, event):
			buffer = event.app.current_buffer
			cursor = buffer.cursor_position
			full_text = buffer.text
			before = buffer.document.text_before_cursor
			after = buffer.document.text_after_cursor

			# if hasattr(_, 'ord'):
			# 	_.ord(f"[onEvent] {key_name} | text: '{full_text}' | cursor: {cursor} | before: '{before}' | after: '{after}'")
			# else:
			# 	print(f"[onEvent] {key_name} | text: '{full_text}' | cursor: {cursor} | before: '{before}' | after: '{after}'")

		def bind_all_keys(self):


			@self.kb.add(Keys.Any)
			def _(event):
				# Minimal logging only
				key = event.key_sequence[0].key
				self.log(f'Key({key})', event)

			# # # Logs every keypress, cursor state, and buffer contents — useful for debugging
			# # @self.kb.add(Keys.Any)
			# # def _(event):
			# # 	buffer = event.app.current_buffer
			# # 	text = buffer.text
			# # 	cursor = buffer.cursor_position
			# # 	before = buffer.document.text_before_cursor
			# # 	after = buffer.document.text_after_cursor

			# # 	# Example: programmatically move the cursor
			# # 	# buffer.cursor_position += 1  # move right
			# # 	# buffer.cursor_position = len(buffer.text)  # jump to end

			# # 	# Currently does nothing
			# # 	pass

			# # Arrow up: normally cycles through history; currently overridden to do nothing
			# @self.kb.add('up')
			# def _(event):
			# 	self.log('ArrowUp', event)
			# 	pass

			# # Arrow down: normally cycles forward in history; currently overridden to do nothing
			# @self.kb.add('down')
			# def _(event):
			# 	self.log('ArrowDown', event)
			# 	pass

			# # Tab key: can be used for autocompletion; currently overridden to do nothing
			# @self.kb.add('tab')
			# def _(event):
			# 	self.log('Tab', event)
			# 	pass

			# # Enter key: normally submits input
			# @self.kb.add('enter')
			# def _(event):
			# 	self.log('Enter', event)
			# 	pass  # <-- do nothing for now

			# # Ctrl+C: normally interrupts, cancels input, or exits; currently overridden
			# @self.kb.add('c-c')
			# def _(event):
			# 	self.log('Ctrl+C', event)
			# 	pass  # <-- no exit, just log

			# # Backspace: normally deletes character before cursor
			# @self.kb.add('backspace')
			# def _(event):
			# 	self.log('Backspace', event)
			# 	pass  # <-- no deletion, just log

			# # Escape: often used to clear input or exit modes
			# @self.kb.add('escape')
			# def _(event):
			# 	self.log('Escape', event)
			# 	pass  # <-- no clear or exit

			# # Ctrl+L: normally clears the screen
			# @self.kb.add('c-l')
			# def _(event):
			# 	self.log('Ctrl+L', event)
			# 	pass  # <-- no screen clearing

			# # Catch-all again to log remaining keys except 'enter' separately
			# @self.kb.add(Keys.Any)
			# def _(event):
			# 	key = event.key_sequence[0].key
			# 	if key != 'c-m':  # 'c-m' is enter
			# 		self.log(f'Key({key})', event)
			# 	pass

		def get_bindings(self):
			return self.kb














	# class OnEventLogger:
	# 	def __init__(self, terminal):
	# 		self.terminal = terminal
	# 		self.kb = KeyBindings()
	# 		self.bind_all_keys()

	# 	def log(self, key_name, event):
	# 		buffer = event.app.current_buffer
	# 		cursor = buffer.cursor_position
	# 		full_text = buffer.text
	# 		before = buffer.document.text_before_cursor
	# 		after = buffer.document.text_after_cursor

	# 		if hasattr(_, 'ord'):
	# 			_.ord(f"[onEvent] {key_name} | text: '{full_text}' | cursor: {cursor} | before: '{before}' | after: '{after}'")
	# 		else:
	# 			print(f"[onEvent] {key_name} | text: '{full_text}' | cursor: {cursor} | before: '{before}' | after: '{after}'")

	# 	def bind_all_keys(self):

	# 		# @self.kb.add(Keys.Any)
	# 		# def _(event):
	# 		# 	buffer = event.app.current_buffer
	# 		# 	print("Cursor is at:", buffer.cursor_position)
	# 		# 	print("Text before cursor:", buffer.document.text_before_cursor)
	# 		# 	print("Text after cursor:", buffer.document.text_after_cursor)

	# 		@self.kb.add(Keys.Any)
	# 		def _(event):
	# 			buffer = event.app.current_buffer

	# 			text = buffer.text
	# 			cursor = buffer.cursor_position

	# 			# Optional: get split text
	# 			before = buffer.document.text_before_cursor
	# 			after = buffer.document.text_after_cursor

	# 			# print(f"[onEvent] Prompt: '{text}'")
	# 			# print(f"[onEvent] Cursor at index: {cursor}")
	# 			# print(f"[onEvent] Before: '{before}' | After: '{after}'")

	# 			## programmatically move the cursor
				
	# 			# current cursor position = buffer.cursor_position
				
	# 			# buffer.cursor_position += 1  # move right
	# 			# buffer.cursor_position = len(buffer.text)  # jump to end

	# 		@self.kb.add('up')
	# 		def _(event):
	# 			self.log('ArrowUp', event)
	# 			buffer = event.app.current_buffer
	# 			buffer.history_backward(count=1)

	# 		@self.kb.add('down')
	# 		def _(event):
	# 			self.log('ArrowDown', event)
	# 			buffer = event.app.current_buffer
	# 			buffer.history_forward(count=1)

	# 		@self.kb.add('tab')
	# 		def _(event):
	# 			############## event.prevent_default()

	# 			self.log('Tab', event)
	# 			buffer = event.app.current_buffer
	# 			buffer.insert_text('\t')

	# 			######################## buffer.document = Document('new command text')   ### replace entire prompt


	# 		@self.kb.add('tab')
	# 		def _(event):
	# 			# event.prevent_default()  # ❌ Not needed — just override behavior
	# 			buffer = event.app.current_buffer
	# 			# buffer.insert_text('[Your suggestion]')
	# 			pass  # <-- explicitly do nothing or add your logic here


	# 		@self.kb.add('enter')
	# 		def _(event):
	# 			self.log('Enter', event)
	# 			buffer = event.app.current_buffer
	# 			event.app.exit(result=buffer.text)

	# 		@self.kb.add('c-c')
	# 		def _(event):
	# 			self.log('Ctrl+C', event)
	# 			event.app.exit(exception=KeyboardInterrupt, style='class:aborting')

	# 		@self.kb.add('backspace')
	# 		def _(event):
	# 			self.log('Backspace', event)

	# 		# @self.kb.add('escape')
	# 		# def _(event):
	# 		# 	self.log('Escape', event)

	# 		@self.kb.add('escape')
	# 		def _(event):
	# 			# event.prevent_default()  # ❌ Not needed
	# 			buffer = event.app.current_buffer
	# 			buffer.text = ''


	# 		@self.kb.add('c-l')
	# 		def _(event):
	# 			self.log('Ctrl+L', event)
	# 			os.system('cls' if os.name == 'nt' else 'clear')

	# 		@self.kb.add(Keys.Any)
	# 		def _(event):
	# 			# ✅ FIX: Get the key from key_sequence properly
	# 			key = event.key_sequence[0].key
	# 			if key != 'c-m':  # enter gets logged separately
	# 				self.log(f'Key({key})', event)

	# 	def log(self, key_name, event):
	# 		current_text = event.app.current_buffer.text
	# 		# if hasattr(_, 'ord'):
	# 		# 	_.ord(f"[onEvent] {key_name} | text: {current_text}")
	# 		# else:
	# 		# 	print(f"[onEvent] {key_name} | text: {current_text}")

	# 	def get_bindings(self):
	# 		return self.kb


'''
scrape files out of shell script installers 

{
  "time": "2025-04-21T10:39:55Z",
  "session": "SESSION_ID_2983",
  "files": [
	"/etc/nginx/nginx.conf",
	"/var/www/html/index.html",
	"/usr/local/bin/nginx"
  ],
  "urls": [
	"https://nginx.org/en/linux_packages.html"
  ],
  "triggered_by": "nginx-install.sh"
}

'''


'''
will not let you curl cpanel.net/latest if perl is not installed

{
  "url": "https://cpanel.net/latest",
  "steps": [
	{"cmd": "yum install perl", "status": "pending"},
	{"cmd": "curl -o latest ...", "status": "pending"},
	{"cmd": "sh latest", "status": "pending"},
  ],
  "confirmed": False
}

'''



# store pipe data, prompt_toolkit
# pipe_data_variable = event.app.current_buffer.text
'''
@self.kb.add('c-p')  # Ctrl+P to save virtual pipe data
def _(event):
	pipe_data_variable = event.app.current_buffer.text
	_.vpipe['session_id'] = pipe_data_variable  # Save to your global pipe store
	print(f"[pipe] Captured: {pipe_data_variable}")

in python app 	
'''



# ideas for virtual pipes across devices with registration and hashtags 
# _.pushVirtualPipe(app='app.py', data=pipe, session='SESSION_ID', tags=['config', 'whm', 'edit'])



'''
##Documentation
#KeyBindings

## 🔑 What does `'c-l'` mean?

This is shorthand for:

```
c = Control
l = lowercase letter L
```

So:
```python
@kb.add('c-l')
```
Means: **trigger when the user presses Ctrl + L**.

---

## ✅ Supported Key Syntax

| Syntax      | Meaning                     | Example Use         |
|-------------|-----------------------------|---------------------|
| `'c-x'`     | Ctrl + x                    | `'c-b'` → Ctrl+B    |
| `'a-x'`     | Alt + x                     | `'a-z'` → Alt+Z     |
| `'s-x'`     | Shift + x (on some systems) | `'s-tab'`           |
| `'tab'`     | Tab key                     | `'tab'`             |
| `'enter'`   | Enter/Return key            | `'enter'`           |
| `'escape'`  | Escape key                  | `'escape'`          |
| `'up'`      | Arrow up                    | `'down'`, `'right'` |
| `'f1'`–`'f12'` | Function keys             | `'f5'`, `'f10'`     |

---

## 🧪 Example: Capture Ctrl+B

```python
@self.kb.add('c-b')
def _(event):
	self.log('Ctrl+B', event)
	print("📦 You pressed Ctrl+B!")
```

---

## 🎛 Multiple Keys (Sequential Bindings)

If you want something like **`Ctrl+X` followed by `Ctrl+F`**, you can do this:

```python
@self.kb.add('c-x', 'c-f')
def _(event):
	print("🔥 Ctrl+X then Ctrl+F detected!")
```

Yes, you can stack key sequences with commas like a combo.

---

## 🧠 See What Keys Are Available

If you're unsure of the name for a key, run this minimal test:
```python
from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings

kb = KeyBindings()

@kb.add('<any>')
def _(event):
	print(f"You pressed: {event.key}")

prompt('> ', key_bindings=kb)
```

---

## 🛠 Need to match `Shift+something`?

Most terminals don't distinguish `Shift+A` vs `a` directly, but they do for things like `Shift+Tab`:

```python
@self.kb.add('s-tab')
def _(event):
	print("⇧ Shift+Tab was pressed")
```

---

## Summary

| Key Combo        | Binding String |
|------------------|----------------|
| Ctrl+L           | `'c-l'`        |
| Ctrl+B           | `'c-b'`        |
| Alt+Z            | `'a-z'`        |
| Shift+Tab        | `'s-tab'`      |
| Ctrl+X → Ctrl+F  | `'c-x', 'c-f'` |


#KeyBindings-end
'''





























# pre on events


import _rightThumb._bookmarks as _bm
import subprocess
import os
import sys
import signal
import shutil
import socket
import random
import readline
import atexit
import time
from prompt_toolkit import prompt # type: ignore
from prompt_toolkit.styles import Style # type: ignore
from prompt_toolkit.formatted_text import FormattedText  # type: ignore
from datetime import datetime
import re





if os.name != 'nt':
	import readline
	import atexit












# class TerminalProxy:

# 	def __init__(self):
# 		self.isActive = True
# 		self.emoji = random.choice(['🐞', '🌭', '🦴', '🧠', '⚡', '🛠️', '🔥'])
# 		self.user = os.getenv("USERNAME") or os.getenv("USER") or "user"
# 		self.host = self.get_hostname()
# 		self.emoji = "🐞"
# 		self.shell = self.detect_shell()
# 		self.aliases=_.getTable('file-open-aliases.hash')
# 		self.clean_history_file()
# 		from prompt_toolkit.history import FileHistory  # type: ignore

# 		history_path = os.path.expanduser(self.ptermHistory())

# 		# print(self.ptermHistory())
# 		# sys.exit(0)

# 		# Ensure history file exists before using FileHistory
# 		if not os.path.exists(self.ptermHistory()):
# 			with open(self.ptermHistory(), 'w', encoding='utf-8') as f:
# 				pass  # create empty history file

# 		# Now initialize history
# 		self.history = FileHistory(self.ptermHistory())





# 		# self.style = Style.from_dict({
# 		# 	'prompt': '#ff0066 bold',
# 		# 	'user_input': 'ansicyan'
# 		# })

# 		self.style = Style.from_dict({
# 			'prompt': '#b4009e bold',     # Accurate color from your screenshot
# 			'user_input': 'ansicyan'      # Still a nice complement
# 		})

# 		if not 'aliases' in self.aliases: self.aliases['aliases'] = {}
# 		os.environ['pterm'] = 'true'
# 		if os.name != 'nt':
# 			self.history_file = os.path.expanduser("~/.pterm_history")
# 			self.setup_history()
# 			signal.signal(signal.SIGTSTP, signal.SIG_IGN)
# 			if hasattr(signal, 'SIGTTIN'):
# 				signal.signal(signal.SIGTTIN, signal.SIG_IGN)
# 			if hasattr(signal, 'SIGTTOU'):
# 				signal.signal(signal.SIGTTOU, signal.SIG_IGN)
# 		signal.signal(signal.SIGINT, self.sigint_handler)








from prompt_toolkit.history import FileHistory, InMemoryHistory

class TerminalProxy:
	def __init__(self):
		self.isActive = True
		self.emoji = "🐞"
		self.user = os.getenv("USERNAME") or os.getenv("USER") or "user"
		self.host = self.get_hostname()
		self.shell = self.detect_shell()
		self.aliases = _.getTable('file-open-aliases.hash')
		self._cached_commands = None

		self.history_file = self.ptermHistory()
		self.meta_history_file = self.ptermHistory() + '.meta'

		self.ensure_file(self.history_file)
		self.ensure_file(self.meta_history_file)
		self.rotate_history_file(self.history_file)

		self.history = FileHistory(self.history_file)

		self.style = Style.from_dict({
			'prompt': '#b4009e bold',
			'user_input': 'ansicyan'
		})

		os.environ['pterm'] = 'true'
		if os.name != 'nt':
			self.setup_history()
			signal.signal(signal.SIGTSTP, signal.SIG_IGN)
			if hasattr(signal, 'SIGTTIN'):
				signal.signal(signal.SIGTTIN, signal.SIG_IGN)
			if hasattr(signal, 'SIGTTOU'):
				signal.signal(signal.SIGTTOU, signal.SIG_IGN)
		signal.signal(signal.SIGINT, self.sigint_handler)






	def ensure_file(self, path):
		if not os.path.exists(path):
			with open(path, 'w', encoding='utf-8') as f:
				pass



	def rotate_history_file(self, path, max_lines=1000):
		try:
			with open(path, 'r', encoding='utf-8') as f:
				lines = f.readlines()
			if len(lines) > max_lines:
				with open(path, 'w', encoding='utf-8') as f:
					f.writelines(lines[-max_lines:])
		except Exception as e:
			print(f"[pterm] ⚠️ Failed to rotate history: {e}")



	def get_history_commands(self, force_refresh=False):
		SESSION_RE = re.compile(r'# (.*?) \| session:(.*)')
		ANSI_RE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
		if self._cached_commands and not force_refresh:
			return self._cached_commands

		commands = []
		try:
			with open(self.meta_history_file, 'r', encoding='utf-8') as f:
				raw = ANSI_RE.sub('', f.read().replace('\r', '').replace(chr(10), '\n'))

			session = None
			timestamp = None
			for line in raw.splitlines():
				if line.startswith('#'):
					match = SESSION_RE.match(line)
					if match:
						timestamp, session = match.groups()
				elif line.startswith('+'):
					commands.append({
						'command': line[1:].strip(),
						'session': session,
						'time': timestamp
					})

			self._cached_commands = commands
		except Exception as e:
			print(f"[pterm] ⚠️ Failed to load history: {e}")
			self._cached_commands = []

		return self._cached_commands



	# def get_history_commands(self):
	# 	history_path = os.path.expanduser(self.ptermHistory())
	# 	commands = []

	# 	# Read and clean the raw history content
	# 	with open(history_path, 'r', encoding='utf-8') as f:
	# 		file_content = f.read()
	# 	file_content = clean_history_file_content(file_content)

	# 	# Parse the cleaned lines
	# 	session = None
	# 	timestamp = None
	# 	for line in file_content.splitlines():
	# 		if line.startswith('#'):
	# 			match = re.match(r'# (.*?) \| session:(.*)', line)
	# 			if match:
	# 				timestamp, session = match.groups()
	# 		elif line.startswith('+'):
	# 			commands.append({
	# 				'command': line[1:].strip(),
	# 				'session': session,
	# 				'time': timestamp
	# 			})
	# 	return commands


	def clean_history_file(path):
		try:
			with open(path, 'r', encoding='utf-8') as f:
				content = f.read()
			# Remove carriage returns and ANSI
			content = content.replace('\r', '')
			content = clean_history_file_content(content)
			with open(path, 'w', encoding='utf-8') as f:
				f.write(content)
		except Exception as e:
			print(f"[pterm] ⚠️ Failed to clean history file: {e}")


	def clean_history_file_content(raw: str):
		# Normalize line endings (just in case)
		raw = raw.replace(chr(10), '\n')

		# Remove ANSI escape codes (colors, cursor moves, etc.)
		ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
		raw = ansi_escape.sub('', raw)

		return raw

	def add_to_history(self, command: str):
		if not command.strip():
			return

		# Clean up any trailing carriage returns or prompt artifacts
		cleaned = command.strip().replace('\r', '').replace('\x1b', '')

		try:
			if hasattr(self.history, 'append_string'):
				self.history.append_string(cleaned)

			session_id = os.environ.get('SESSION_ID', getattr(__, 'startTime', 'unknown'))
			entry = f"# {datetime.now().isoformat()} | session:{session_id}\n+{cleaned}\n"

			with open(self.meta_history_file, 'a', encoding='utf-8') as f:
				f.write(entry)

		except Exception as e:
			print(f"[pterm] ⚠️ Failed to add to history: {e}")



	# def add_to_history(self, command: str):
	# 	if not command.strip():
	# 		return
	# 	try:
	# 		if hasattr(self.history, 'append_string'):
	# 			self.history.append_string(command.strip())

	# 		session_id = os.environ.get('SESSION_ID', getattr(__, 'startTime', 'unknown'))
	# 		entry = f"# {datetime.now().isoformat()} | session:{session_id}\n+{command.strip()}\n"

	# 		with open(self.meta_history_file, 'a', encoding='utf-8') as f:
	# 			f.write(entry)

	# 	except Exception as e:
	# 		print(f"[pterm] ⚠️ Failed to add to history: {e}")




	# def add_to_history(self, command: str):
	# 	if not command.strip():
	# 		return

	# 	try:
	# 		if hasattr(self.history, 'append_string'):
	# 			self.history.append_string(command.strip())

	# 			# Include metadata with SESSION_ID or fallback to __.startTime
	# 			session_id = os.environ.get('SESSION_ID', getattr(__, 'startTime', 'unknown'))
	# 			entry = f"# {datetime.now().isoformat()} | session:{session_id}\n+{command.strip()}\n"

	# 			with open(self.ptermHistory(), 'a', encoding='utf-8') as f:
	# 				f.write(entry)

	# 	except Exception as e:
	# 		print(f"[pterm] ⚠️ Failed to add to history: {e}")



	def setup_history(self):
		try:
			readline.read_history_file(self.history_file)
		except FileNotFoundError:
			pass
		atexit.register(readline.write_history_file, self.history_file)

	def get_hostname(self):
		if os.name == "nt":
			return os.environ.get("COMPUTERNAME", "PC")
		else:
			try:
				with open("/etc/hostname") as f:
					return f.read().strip()
			except:
				return socket.gethostname()

	def pterm(self):
		if os.name == 'nt':
			home = os.getenv('USERPROFILE') or os.path.expanduser('~')
			return home.rstrip('\\') + '\\' + '.pterm'
		else:
			home = os.getenv('HOME') or os.path.expanduser('~')
			return home.rstrip('/') + '/' + '.pterm'

	def ptermHistory(self):
		if os.name == 'nt':
			home = os.getenv('USERPROFILE') or os.path.expanduser('~')
			return home.rstrip('\\') + '\\' + '.pterm_history'
		else:
			home = os.getenv('HOME') or os.path.expanduser('~')
			return home.rstrip('/') + '/' + '.pterm_history'


	def detect_shell(self):
		if os.name == "nt":
			return "cmd.exe"
		else:
			return os.environ.get("SHELL", "/bin/bash")

	def sigint_handler(self, sig, frame):
		os.environ.pop('pterm', None)
		if hasattr(self, 'shell_proc') and self.shell_proc:
			self.shell_proc.terminate()
		print("\n[Exiting terminal proxy]")
		sys.exit(0)

	# def get_fancy_prompt(self):
	# 	cwd = os.getcwd()
	# 	home = os.path.expanduser('~')
	# 	if cwd.startswith(home):
	# 		cwd = cwd.replace(home, '~', 1)
	# 	line1 = f"\033[95m┌──({self.user}{self.emoji}{self.host})-[ {cwd} ]\033[0m"
	# 	line2 = f"\033[95m└─ \033[0m"
	# 	return f"{line1}\n{line2}"

	def get_fancy_prompt(self):
		cwd = os.getcwd()
		home = os.path.expanduser('~')
		if cwd.startswith(home):
			cwd = cwd.replace(home, '~', 1)

		return FormattedText([
			('class:prompt', f"┌──({self.user}{self.emoji}{self.host})-[ {cwd} ]\n"),
			('class:prompt', "└─ ")
		])



	def change_directory(self, path):
		try:
			os.chdir(os.path.expandvars(os.path.expanduser(path)))
		except Exception as e:
			print(f"cd: {e}")

	def inject(self, command):
		if command.strip() == 'c':
			self.wasC = True
		else:
			self.wasC = False
		self.add_to_history(command)
		if command == 'exit': self.isActive = False
		if '.fi' in command or '.fo' in command or '.url' in command:
			parts = command.split()
			new = []
			for i, part in enumerate(parts):
				if not i:
					new.append(part)
					continue
				if part.endswith('.url'):
					part = part[:-len('.url')]
					path=_.url2file(part)
					if path and os.path.exists(path):
						part = path
				if part.endswith('.url.fo'):
					part = part[:-len('.url.fo')]
					path=_.url2file(part)
					path = __.path(path,pop=True)
					if path and os.path.exists(path):
						part = path
				elif part.endswith('.fi'):
					if part[:-3] in self.aliases['aliases']:
						part = self.aliases['aliases'][part[:-3]]
				elif part.endswith('.fo'):
					try:
						path = _bm.Bookmarks( part[:-3] ).get()
						if path and os.path.exists(path):
							part = path
					except: pass
				new.append(part)
			command = ' '.join(new)
		if os.name != 'nt':
			blocked = ['clear', 'reset', 'stty', 'tput', 'less', 'more']
			if any(command.strip().startswith(b) for b in blocked):
				return f'echo "[pterm] ⛔ blocked: {command.strip()}"'
		command += ' && pwd > ' + self.pterm()
		return command

	def run_command(self, command):
		command = self.inject(command)
		try:
			env = os.environ.copy()
			if os.name == 'nt':
				subprocess.run(['cmd.exe', '/c', command], shell=False, env=env)
				self.last_dir = _.getText(self.pterm(), raw=True, clean=2).strip()
				os.chdir(self.last_dir)
				print()
				
			else:
				bash_cmd = f'bash -i -c "{command}"'
				subprocess.run(bash_cmd, shell=True, env=env)
				self.last_dir = _.getText(self.pterm(), raw=True, clean=2).strip()
				os.chdir(self.last_dir)
				print()
				
		except Exception as e:
			print(f"[Error] {e}")

	def brand(self):
		return self.get_fancy_prompt()


	# def start(self):
	# 	os.system('cls' if os.name == 'nt' else 'clear')
	# 	# print("🧪 Terminal proxy started. Ctrl+C to exit.\n")
	# 	__.touch = time.time()
	# 	self.show_brand_next = True  # show prompt at startup
	# 	while self.isActive:
	# 		__.touch = time.time()
	# 		try:
	# 			if self.show_brand_next:
	# 				self.brand()
	# 			if os.name == 'nt':
	# 				if self.show_brand_next:
	# 					command = input('').strip()
	# 				else:
	# 					# command = input('└─ ').strip()
	# 					command = prompt([('class:prompt', '└─ ')], style=self.style, history=self.history)


	# 					# command = prompt([('class:prompt', '└─ ')], style=self.style)
						

	# 			else:
	# 				command = input().strip()  # prompt already printed
	# 			if not command:
	# 				continue
	# 			if command.startswith("cd "):
	# 				self.change_directory(command[3:].strip())
	# 			else:
	# 				self.run_command(command)
	# 			self.show_brand_next = self.wasC  # trigger prompt only if 'c' was typed
	# 		except EOFError:
	# 			break
	# 		except Exception as e:
	# 			print(f"[Error] {e}")

	def start(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		__.touch = time.time()
		self.show_brand_next = True  # show prompt at startup

		while self.isActive:
			__.touch = time.time()
			try:
				# Show branding prompt (top bar, but no prompt text)
				if self.show_brand_next:
					prompt_text = self.brand()
				else:
					prompt_text = [('class:prompt', '└─ ')]

				# Use prompt_toolkit for history support and consistent UI
				# command = prompt(prompt_text, style=self.style, history=self.history).strip()

				try:
					command = prompt(prompt_text, style=self.style, history=self.history).strip()
				except KeyboardInterrupt:
					print("\n[Ctrl+C detected — exiting]")
					_.isExit(__file__)
					break

				command = prompt(prompt_text, style=self.style, history=self.history).strip()
				command = command.replace('\r', '').replace('\x1b', '')  # just in case

				if not command:
					continue

				if command.startswith("cd "):
					self.change_directory(command[3:].strip())
				else:
					self.run_command(command)

				self.show_brand_next = self.wasC  # Show branding again only if user typed c

			except EOFError:
				break
			except Exception as e:
				print(f"[Error] {e}")

		self.isActive = False











def action():
	TerminalProxy().start()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)