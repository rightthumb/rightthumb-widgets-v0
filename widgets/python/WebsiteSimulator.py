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
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
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



# import os
# import shutil
# import random
# import string
# import http.server
# import socketserver
# import threading
# import time
# from urllib.parse import quote

# import sys
# import platform
# if platform.system() == "Windows":
# 	import msvcrt
# import os
# import shutil
# import random
# import string
# import http.server
# import socketserver
# import threading
# import time
# from urllib.parse import quote

# LIPSUM_WORDS = [
# 	"lorem", "ipsum", "dolor", "amet", "consectetur", "adipiscing", "elit", "sed", "do", "eiusmod",
# 	"tempor", "incididunt", "labore", "dolore", "magna", "aliqua", "ut", "enim", "ad", "minim"
# ]

# LIPSUM_BODY = (
# 	"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt "
# 	"ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
# 	"laboris nisi ut aliquip ex ea commodo consequat."
# )

# DEFAULT_CSS = """
# body {
# 	font-family: Arial, sans-serif;
# 	background-color: #f4f4f4;
# 	margin: 0;
# 	padding: 0;
# }
# .sidebar {
# 	background-color: #333;
# 	color: #fff;
# 	width: 220px;
# 	height: 100vh;
# 	position: fixed;
# 	top: 0;
# 	left: 0;
# 	padding: 20px;
# }
# .sidebar a {
# 	color: #fff;
# 	text-decoration: none;
# 	display: block;
# 	margin: 10px 0;
# }
# .content {
# 	margin-left: 240px;
# 	padding: 20px;
# }
# """

# PAGE_TEMPLATE = """
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>{title}</title>
# 	<link rel="stylesheet" href="/assets/default.css">
# 	{extra_css}
# 	{extra_js}
# </head>
# <body>
# 	<div class="sidebar">
# 		<h3>Menu</h3>
# 		{menu}
# 	</div>
# 	<div class="content">
# 		[content]
# 	</div>
# </body>
# </html>
# """


# class WebsiteSimulator:
# 	def __init__(self, root_dir="__WebsiteSimulator__", port=0):
# 		self.root_dir = root_dir
# 		self.assets_dir = os.path.join(self.root_dir, "assets")
# 		self.port = port
# 		self.httpd = None
# 		self.original_dir = os.getcwd()
# 		self.page_words = random.sample(LIPSUM_WORDS, 20)

# 	def setup_structure(self):




# 		if os.path.exists(self.root_dir):
# 			shutil.rmtree(self.root_dir)
# 		os.makedirs(self.assets_dir, exist_ok=True)

# 		with open(os.path.join(self.assets_dir, "default.css"), "w") as f:
# 			f.write(DEFAULT_CSS)

# 		self.extra_css_files = []
# 		for i in range(3):
# 			fname = f"style{i+1}.css"
# 			self.extra_css_files.append(fname)
# 			with open(os.path.join(self.assets_dir, fname), "w") as f:
# 				f.write(f"/* {fname} */\nbody {{ background-color: #{''.join(random.choices('ABCDEF0123456789', k=6))}; }}")

# 		self.extra_js_files = []
# 		for word in self.page_words[:3]:
# 			js_file = f"{word}.js"
# 			self.extra_js_files.append(js_file)
# 			with open(os.path.join(self.assets_dir, js_file), "w") as f:
# 				f.write(f"// {js_file}\nconsole.log('{js_file} loaded');")

# 		self.pages = []

# 		# Add homepage
# 		home_word = "welcome"
# 		home_path = os.path.join(self.root_dir, "index.html")
# 		home_url = "/index.html"
# 		self.pages.insert(0, (home_word, home_path, home_url))

# 		for i, word in enumerate(self.page_words):
# 			depth = random.randint(1, 3)
# 			folders = [random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) for _ in range(depth)]
# 			is_homepage = i == 0
# 			filename = "index.html" if is_homepage else f"{word}.html"
# 			path = os.path.join(self.root_dir, *folders, filename)
# 			url_path = "/" + "/".join(folders + ([filename]))
# 			self.pages.append((word, path, url_path))

# 		menu_html = "\n".join([f'<a href="{url}">{word.title()}</a>' for word, _, url in self.pages])

# 		for word, path, url in self.pages:
# 			self.create_page(word, path, menu_html)

# 	def create_page(self, word, path, menu_html):
# 		os.makedirs(os.path.dirname(path), exist_ok=True)
# 		body_words = LIPSUM_BODY.split()
# 		random.shuffle(body_words)
# 		randomized_body = ' '.join(body_words)
# 		content = f"<h2>{word.title()}</h2>\n<p>{randomized_body}</p>"

# 		extra_css = "\n".join([f'<link rel="stylesheet" href="/assets/{f}">' for f in self.extra_css_files])
# 		extra_js = "\n".join([f'<script src="/assets/{f}"></script>' for f in self.extra_js_files])
# 		html = PAGE_TEMPLATE.format(title=word.title(), extra_css=extra_css, extra_js=extra_js, menu=menu_html)
# 		html = html.replace("[content]", content)
# 		with open(path, "w", encoding="utf-8") as f:
# 			f.write(html)

# 	def listen_for_ctrl_bracket(self):
# 		import platform
# 		if platform.system() == "Windows":
# 			import msvcrt
# 			while True:
# 				if msvcrt.kbhit():
# 					key = msvcrt.getch()
# 					if key == b'\x1b':
# 						print("\n[⛔] Ctrl + [ detected — stopping server.")
# 						self.stop_server()
# 						break
# 				time.sleep(0.1)
# 		else:
# 			while True:
# 				key = input()
# 				if key == '\x1b':
# 					print("\n[⛔] Ctrl + [ detected — stopping server.")
# 					self.stop_server()
# 					break

# 	def start_server(self):
# 		import platform
# 		if platform.system() == "Windows":
# 			import msvcrt

# 		os.chdir(self.root_dir)
# 		Handler = http.server.SimpleHTTPRequestHandler

# 		class ReusableTCPServer(socketserver.TCPServer):
# 			allow_reuse_address = True

# 		try:
# 			self.httpd = ReusableTCPServer(("127.0.0.1", 0), Handler)
# 			self.port = self.httpd.server_address[1]
# 		except Exception as e:
# 			print(f"[✘] Failed to bind to random port: {e}")
# 			os.chdir(self.original_dir)
# 			return

# 		_copy = _.regImp(__.appReg, '-copy')
# 		_copy.imp.copy(f"http://localhost:{self.port}/", p=0)
# 		print("Copied the URL")

# 		print(f"Starting server at http://localhost:{self.port}/")
# 		print("Press Ctrl+[ to stop and trigger cleanup")

# 		threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
# 		threading.Thread(target=self.listen_for_ctrl_bracket, daemon=True).start()

# 		try:
# 			while self.httpd:
# 				time.sleep(1)
# 		except KeyboardInterrupt:
# 			self.stop_server()

# 	def stop_server(self):
# 		if self.httpd:
# 			self.httpd.shutdown()
# 			self.httpd.server_close()
# 			self.httpd = None
# 		os.chdir(self.original_dir)
# 		print("\nServer stopped. Auto-deleting '__WebsiteSimulator__'...")
# 		try:
# 			shutil.rmtree(self.root_dir)
# 			print("✅ Deleted '__WebsiteSimulator__'")
# 		except Exception as e:
# 			print(f"⚠️ Failed to delete: {e}")


# # Run it
# simulator = WebsiteSimulator()
# simulator.setup_structure()
# simulator.start_server()




import os
import shutil
import random
import string
import http.server
import socketserver
import threading
import time

LIPSUM_WORDS = [
    "lorem", "ipsum", "dolor", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "labore", "dolore",
    "magna", "aliqua", "ut", "enim", "ad", "minim"
]

LIPSUM_BODY = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
    "laboris nisi ut aliquip ex ea commodo consequat."
)

DEFAULT_CSS = """
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}
.sidebar {
    background-color: #333;
    color: #fff;
    width: 220px;
    height: 100vh;
    position: fixed;
    top: 0;
    left: 0;
    padding: 20px;
}
.sidebar a {
    color: #fff;
    text-decoration: none;
    display: block;
    margin: 10px 0;
}
.content {
    margin-left: 240px;
    padding: 20px;
}
"""

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="/assets/default.css">
    {extra_css}
    {extra_js}
</head>
<body>
    <div class="sidebar">
        <h3>Menu</h3>
        {menu}
    </div>
    <div class="content">
        [content]
    </div>
</body>
</html>
"""


class WebsiteSimulator:
    def __init__(self, root_dir="__WebsiteSimulator__", port=0):
        self.root_dir = root_dir
        self.assets_dir = os.path.join(self.root_dir, "assets")
        self.port = port
        self.httpd = None
        self.original_dir = os.getcwd()
        self.page_words = random.sample(LIPSUM_WORDS, 20)

    def setup_structure(self):
        if os.path.exists(self.root_dir):
            shutil.rmtree(self.root_dir)
        os.makedirs(self.assets_dir, exist_ok=True)

        with open(os.path.join(self.assets_dir, "default.css"), "w") as f:
            f.write(DEFAULT_CSS)

        self.extra_css_files = []
        for i in range(3):
            fname = f"style{i+1}.css"
            self.extra_css_files.append(fname)
            with open(os.path.join(self.assets_dir, fname), "w") as f:
                f.write(f"/* {fname} */\nbody {{ background-color: #{''.join(random.choices('ABCDEF0123456789', k=6))}; }}")

        self.extra_js_files = []
        for word in self.page_words[:3]:
            js_file = f"{word}.js"
            self.extra_js_files.append(js_file)
            with open(os.path.join(self.assets_dir, js_file), "w") as f:
                f.write(f"// {js_file}\nconsole.log('{js_file} loaded');")

        self.pages = []

        # Add homepage
        home_word = "home"
        home_path = os.path.join(self.root_dir, "index.html")
        home_url = "/index.html"
        self.pages.append((home_word, home_path, home_url))

        # Add other pages
        for i, word in enumerate(self.page_words):
            depth = random.randint(1, 3)
            folders = [random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) for _ in range(depth)]
            filename = f"{word}.html"
            path = os.path.join(self.root_dir, *folders, filename)
            url_path = "/" + "/".join(folders + [filename])
            self.pages.append((word, path, url_path))

        menu_html = "\n".join([f'<a href="{url}">{word.title()}</a>' for word, _, url in self.pages])

        for word, path, url in self.pages:
            print(f"✓ Generating: {path}")
            self.create_page(word, path, menu_html)

    def create_page(self, word, path, menu_html):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        words = LIPSUM_BODY.split()
        random.shuffle(words)
        randomized_body = ' '.join(words)
        content = f"<h2>{word.title()}</h2>\n<p>{randomized_body}</p>"
        extra_css = "\n".join([f'<link rel="stylesheet" href="/assets/{f}">' for f in self.extra_css_files])
        extra_js = "\n".join([f'<script src="/assets/{f}"></script>' for f in self.extra_js_files])
        html = PAGE_TEMPLATE.format(title=word.title(), extra_css=extra_css, extra_js=extra_js, menu=menu_html)
        html = html.replace("[content]", content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

    def listen_for_ctrl_bracket(self):
        import platform
        if platform.system() == "Windows":
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b'\x1b':
                        print("\n[⛔] Ctrl + [ detected — stopping server.")
                        self.stop_server()
                        break
                time.sleep(0.1)
        else:
            while True:
                key = input()
                if key == '\x1b':
                    print("\n[⛔] Ctrl + [ detected — stopping server.")
                    self.stop_server()
                    break

    def start_server(self):
        import platform
        if platform.system() == "Windows":
            import msvcrt

        os.chdir(self.root_dir)
        Handler = http.server.SimpleHTTPRequestHandler

        class ReusableTCPServer(socketserver.TCPServer):
            allow_reuse_address = True

        try:
            self.httpd = ReusableTCPServer(("127.0.0.1", 0), Handler)
            self.port = self.httpd.server_address[1]
        except Exception as e:
            print(f"[✘] Failed to bind to random port: {e}")
            os.chdir(self.original_dir)
            return

        _copy = _.regImp(__.appReg, '-copy')
        _copy.imp.copy(f"http://localhost:{self.port}/", p=0)
        print("Copied the URL")

        print(f"Starting server at http://localhost:{self.port}/")
        print("Press Ctrl+[ to stop and trigger cleanup")

        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        threading.Thread(target=self.listen_for_ctrl_bracket, daemon=True).start()

        try:
            while self.httpd:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_server()

    def stop_server(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None
        os.chdir(self.original_dir)
        print("\nServer stopped. Auto-deleting '__WebsiteSimulator__'...")
        try:
            shutil.rmtree(self.root_dir)
            print("✅ Deleted '__WebsiteSimulator__'")
        except Exception as e:
            print(f"⚠️ Failed to delete: {e}")


# Run it
simulator = WebsiteSimulator()
simulator.setup_structure()
simulator.start_server()






def action():
	pass
	# load(); global c3po;

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

