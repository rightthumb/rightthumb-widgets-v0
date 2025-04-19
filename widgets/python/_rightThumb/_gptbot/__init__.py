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




import os, json
from openai import OpenAI

class GPT4oBot_v0:
    def __init__(self, memory_file='memory.json', sprint_task_limit=3):
        self.memory_file = memory_file
        self.sprint_task_limit = sprint_task_limit

        self.api_key = _v.fig['openai']  # Uses your framework config
        self.client = OpenAI(api_key=self.api_key)

        self.mem = self.load_memory()

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
        )
        response = res.choices[0].message.content.strip()
        print("\n✅ GPT Response:\n--------------------\n")
        print(response)
        print("\n--------------------\n")
        return response

    def init_goal(self, goal=None):
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
You are working on the project: {self.mem['goal']}
Recent progress:
{history}

Define a new sprint with a name and {self.sprint_task_limit} key tasks.
Respond in this format:
SPRINT: [Sprint Title]
- Task 1
- Task 2
- Task 3
"""
        response = self.prompt(prompt)
        lines = response.strip().splitlines()
        title = lines[0].replace("SPRINT:", "").strip()
        tasks = [line.strip("- ").strip() for line in lines[1:] if line.strip()]
        sprint = {"title": title, "status": "active", "tasks": [{"task": t, "status": "pending"} for t in tasks]}
        self.mem["sprints"].append(sprint)
        self.save_memory()

    def run_next_task(self):
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

Complete this task. If relevant, describe new insights or needs for future sprints.
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



### FILE: gptbot/__init__.py
from .bot import GPT4oBot


### FILE: gptbot/bot.py
import os, json, re, subprocess
from openai import OpenAI
from _rightThumb import _v

class GPT4oBot:
    def __init__(self, memory_file='memory.json', sprint_task_limit=3, os_interaction=False, app=None):
        self.memory_file = memory_file
        self.sprint_task_limit = sprint_task_limit
        self.os_interaction = os_interaction
        self.app = app

        self.api_key = _v.fig['openai']
        self.client = OpenAI(api_key=self.api_key)

        self.mem = self.load_memory()

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
            filename = self.extract_filename(text, lang, code)
            if filename:
                print(f"\n💾 Saving: {filename}\n")
                with open(filename, 'w') as f:
                    f.write(code)
                if lang == "sh" and self.app == "rust":
                    if 'cargo build' in code:
                        self.rust_build_loop()

    def extract_filename(self, text, lang, code):
        match = re.search(rf"#+\s*filename[:\s]+(.+?\.(?:{lang}|rs|py|js|html|css|sh))", text, re.IGNORECASE)
        return match.group(1).strip() if match else None

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
You are working on the project: {self.mem['goal']}
Recent progress:
{history}

Define a new sprint with a name and {self.sprint_task_limit} key tasks.
Respond in this format:
SPRINT: [Sprint Title]
- Task 1
- Task 2
- Task 3
"""
        response = self.prompt(prompt)
        lines = response.strip().splitlines()
        title = lines[0].replace("SPRINT:", "").strip()
        tasks = [line.strip("- ").strip() for line in lines[1:] if line.strip()]
        sprint = {"title": title, "status": "active", "tasks": [{"task": t, "status": "pending"} for t in tasks]}
        self.mem["sprints"].append(sprint)
        self.save_memory()

    def run_next_task(self):
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

Complete this task. If relevant, describe new insights or needs for future sprints.
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

