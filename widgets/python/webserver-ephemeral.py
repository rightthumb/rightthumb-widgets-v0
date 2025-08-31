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
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	_.switches.register( 'SSL', '-ssl' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] },
		},
	}


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

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

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start
import os
import sys
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import webbrowser
import simplejson


def generate_html_list(recursive=False):
	# Helper function to generate HTML for a directory
	def generate_directory_html(path, recursive):
		html_str = "<ul>\n"
		
		for name in os.listdir(path):
			full_path = os.path.join(path, name)
			relative_path = os.path.relpath(full_path, current_folder)
			if os.path.isdir(full_path):
				if recursive:
					html_str += f"    <li>{name}{generate_directory_html(full_path, recursive)}</li>\n"
			else:
				if os.name == 'nt':
					relative_path1 = relative_path.split(os.sep)[-1]
					relative_path2 = relative_path.replace('\\', '\\\\')
				html_str += f"    <li><a href='#' onclick=\"window.sds.app.process('{relative_path2}')\">{relative_path1}</a></li>\n"
		
		html_str += "</ul>"
		return html_str

	# Get the current working directory
	current_folder = os.getcwd()

	# Start generating HTML from the current working directory
	html_str = generate_directory_html(current_folder, recursive)

	return html_str



def generate_html_list0(recursive=False):
	# Helper function to list files
	def list_files(path, recursive):
		files = []
		for root, _, filenames in os.walk(path):
			for filename in filenames:
				files.append(os.path.join(root, filename))
			if not recursive:
				break
		return files
	
	# Get the current working directory
	current_folder = os.getcwd()

	# List all files
	files = list_files(current_folder, recursive)
	
	# Start the HTML unordered list
	html_str = "<ul>\n"
	
	# Loop through all files and append the list items to the HTML string
	for file in files:
		relative_path = os.path.relpath(file, current_folder)
		relative_path2 = os.path.relpath(file, current_folder)
		if _.isWin:
			relative_path2=relative_path2.replace('\\','\\\\')
		html_str += f"    <li><a href='#' onclick=\"window.sds.app.process('{relative_path2}')\">{relative_path}</a></li>\n"
	
	# Close the HTML unordered list tag
	html_str += "</ul>"
	
	return html_str

# Use the function to generate an HTML list and print it
html_list = generate_html_list(recursive=True)

class Server(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def load_page(self, path, url, field="config"):
		content = _.getText(path)
		data = {field: content}
		response = requests.post(url, data=data)
		return response.text

	def do_GET(self):
		data = self.parse_GET()
		for k, v in data.items(): data[k] = [str(item) for item in v]

		content='get'
		content=simplejson.dumps(data)

		self.respond_OK( """
<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<!--
<!DOCTYPE html>
-->
<html lang="en">

<head>
	<title>ephemeral server</title>
	<meta charset="utf-8">
	<!-- <base href="https://www.w3schools.com/" target="_blank"> -->
	<!-- <META http-equiv="refresh" content="1;URL=/?"> -->
	<!-- <script src="script.js"></script> -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<!-- <link rel="stylesheet" href="https://s2.webigami.com/systemglobal/w/C166/apps/boilerplate/webigami.css"> -->
</head>

<body>
	"""+generate_html_list(1)+"""
	<script type="text/javascript">


		window.sds = typeof window.sds !== 'undefined' ? window.sds : {} ;
		window.sds.v = typeof window.sds.v !== 'undefined' ? window.sds.v : {} ;
		window.sds.app = {
			placeholder: 0,
			process: function(path) {
				$.post(
						'https://local.sds.sh/', {
							'path': path
						},
						function(data) {
							console.log(data);
						}
				);
				// window.sds.app.process();
			}, //==============================================
		};
	</script>
</body>

</html>


		""" )
		# self.respond_OK( f"""
		# <html>
		# <head>
		# 	<title>Simple Web Server</title>

		# </head>
		# <body>
		# 	<h1>Welcome to My Web Server</h1>
		# 	<div id="content">{content}</div>
		# 	<a href="./?shutdown=1">shutdown</a>
		# </body>
		# </html>
		# """ )
		if 'shutdown' in data: sys.exit()

	def do_POST(self):
		if not _.switches.isActive('Clean'): _.pr("Post")

		data = self.parse_POST()

		for k, v in data.items(): data[k] = [str(item) for item in v]

		content='post'
		content=simplejson.dumps(data)
		self.respond_OK( f"""
		<html>
		<head>
			<title>Simple Web Server</title>
		</head>
		<body>
			<h1>Welcome to My Web Server</h1>
			<div id="content">{content}</div>
			<a href="./?shutdown=1">shutdown</a>
		</body>
		</html>
		""" )
		if 'shutdown' in data: sys.exit()

	def parse_GET(self):
		get_vars = parse_qs(self.path[2:])
		return get_vars


	def parse_POST(self):
		ctype, pdict = parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
					self.rfile.read(length), 
					keep_blank_values=1)
		else:
			postvars = {}

	
		return postvars

	def respond_OK(self, msg):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(bytes(msg, "utf-8"))


def action():
	try:
		host = "localhost"
		host = "pc.local.sds.sh"
		port = random.randint(8000, 8999)
		server = HTTPServer((host, port), Server)
		if _.switches.isActive('SSL'):
			server.socket = ssl.wrap_socket(server.socket, certfile='C:\\Users\\Scott\\.rt\\profile\\certs\\certificate.pem', keyfile='C:\\Users\\Scott\\.rt\\profile\\certs\\private_key.key', server_side=True)
		url = f"https://{host}:{port}/"
		print(url)
		print(url+'?shutdown=true')
		webbrowser.open(url, new=2)
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			pass
	except KeyboardInterrupt:
		print("Server shutting down.")
import ssl

# https://orchards.softwaredevelopment.solutions/ephemeral/

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

 
