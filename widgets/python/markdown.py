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
import os, sys, time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register('GUI-Edit', '-edit')
	_.switches.register('Folder', '-folder')
	_.switches.register('Recursive', '-r,-recursive')
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'markdown.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'markdown .md files to html webpage',
	'categories': [
						'.md',
						'markdown',
						'html',
						'webpage',
						'convert',
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
						_.hp('p markdown -f readme.md '),
						_.hp('p markdown -r '),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START
########################################################################################  ########################################################################################
# webserver start


import os,sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from cgi import parse_header, parse_multipart
from urllib.parse import parse_qs
import random
host = "localhost"
port = random.randint(8000,8999)

hello_msg = "Server running..."

def get_title_clean(data):
	data = data.replace('\r','')
	data = _str.cleanBE( data, ' ' )
	data = _str.cleanBE( data, '\t' )
	data = _str.cleanBE( data, '\r' )
	return data

def get_title(data):
	data = get_title_clean(data)
	data = get_title_clean(data)
	data = get_title_clean(data)
	data = get_title_clean(data)
	data = data.split('\n')[0]
	data = data.replace('#','')
	data = get_title_clean(data)
	data = get_title_clean(data)
	data = _str.replaceDuplicate(data,' ')
	return data

class Server(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self.respond_OK(hello_msg)

	def do_POST(self):
		_.pr("Post")

		data = self.parse_POST()

		# _.pr(data)
		# _.pr(type(data))
		# _.pr(str(data[b'butt'][0]))
		shutdown=str( data[b'shutdown'][0] ,'iso-8859-1')

		if shutdown=='yes':
			result='file not saved'
			path=str( data[b'path'][0] ,'iso-8859-1')
			fileBackup.switch( 'isPreOpen', delete=True )
			# fileBackup.switch( 'isPreOpen' )
			fileBackup.switch( 'Input', path )
			fileBackup.action()
		else:

			global filesOpened
			if len(filesOpened) > 1:
				path = __.path(filesOpened[0])
				parts=path.split(os.sep)
				parts.reverse()
				parts.pop(0)
				parts.reverse()
				folder = os.sep.join(parts)
				fn=''
				for ch in get_title(file):
					if ch in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_[]()':
						fn+=ch
				fn = fn.replace(' ','-')
				xXx = folder+os.sep+fn+'.md'
				if os.path.isfile(xXx):
					xXx = folder+os.sep+fn+'-'+_.miniUUID().replace('{','').replace('}','')+'.md'
				path = xXx


			result='file saved'
			file=str( data[b'file'][0] ,'iso-8859-1').replace('\r','')
			path=str( data[b'path'][0] ,'iso-8859-1')
			html=str( data[b'html'][0] ,'iso-8859-1')
			if len(html) > 4:
				result='files saved'
				HTML = '''<!DOCTYPE html>
<html lang="en">

<head>
	<title>THE_TITLE</title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<link href='https://eyeformeta.com/apps/showdown/style.css' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Old+Standard+TT:400,400italic,700' rel='stylesheet' type='text/css'>
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.2/css/foundation.min.css">
	<link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
	<!-- <META http-equiv="refresh" content="1;URL=/?"> -->
	<style type="text/css">
		#markdown-html {
			width: 80%;
			margin-left: auto;
			margin-right: auto;
		}
	</style>

</head>

<body>
	<div id="markdown-html">CODE_HERE</div>
</body>

</html>'''

				HTML = HTML.replace('THE_TITLE',get_title(file))
				HTML = HTML.replace('CODE_HERE',html)
				webbrowser.open(path[:-2]+'htm', new=2)
				_.saveText( HTML,path[:-2]+'htm' )


			_.saveText( file,path )
			_.cp(['saved:',path],'green')
			pass
			fileBackup.switch( 'isPreOpen', delete=True )
			# fileBackup.switch( 'isPreOpen' )
			fileBackup.switch( 'Input', path )
			fileBackup.action()

		self.respond_OK('''
<!DOCTYPE html>
<html lang="en">

<head>
	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,700,600' rel='stylesheet' type='text/css'>
	<title>saved</title>
	<meta charset="utf-8">
	<!-- <META http-equiv="refresh" content="1;URL=/?"> -->
	<style type="text/css">
body {
	background-image: url('https://eyeformeta.com/img/bk/dragon-bk.png');
	background-repeat: no-repeat;
	background-attachment: fixed;  
	background-size: cover;
	color: #fff;
	font-family: 'Open Sans', 'Myriad Pro', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Geneva, Verdana, sans-serif;
	background-position: center;
	font-size: 400%;
}

.boxH
{
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* content of this box will be centered vertically */
.boxV
{
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}
	</style>
</head>

<body>
		<div>
		</div>
		<div class="boxH">
		<div class="boxV">
			<div class="boxM">
			THE_RESULT
			</div>
		</div>
		</div>
</body>

</html>

			'''.replace('THE_RESULT',result))

		sys.exit()


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

def START_WEBSERVER():
	webServer = HTTPServer((host, port), Server)
	_.pr("Server started http://%s:%s" % (host, port))

	try:
		webServer.serve_forever()
	except KeyboardInterrupt:
		pass

	webServer.server_close()
	_.pr("Server stopped.")

# webserver end
########################################################################################  ########################################################################################
def getFolder(folder):
	global base
	if base is None:
		base = folder
	dirList = os.listdir(folder)
	# i = 0

	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(path):
			processFile(path)

		if os.path.isdir(path):
			if _.switches.isActive( 'Recursive' ):
				try:
					getFolder(path)
				except Exception as e:
					pass

markdown = []

filesOpened = []
filesOpened_cnt = 0
ask=None
THE_PATH=''

def openFile(path):
	global THE_PATH
	THE_PATH = __.path(path)
	_.pr(path)

	global filesOpened
	if not path in filesOpened:
		filesOpened.append(path)

		# _file_open.switch('App',_v.meta['code_editor'])
		# _file_open.switch('Files',path)
		# _file_open.action()


def process(table):
	for i,path in enumerate( table ):
		run = True
		if _.switches.isActive('Widgets'):
			run = False
			if path.lower().startswith(_v.w.lower()):
				run = True
		if not os.path.isfile(path):
			run=False
		if run:
			_.pr()
			fileBackup.switch( 'Input', path )
			fileBackup.switch( 'isPreOpen' )
			fb = fileBackup.action()
			_.pr(path)
			_.pr(fb)

def build_tables():
	if not len(v.crypt):
		process(  _.getTable('crypt-docs.list')  )
		process(  _.getTable('secure-crypt-local.meta')  )

v = _.dot()
v.crypt = []

def processFile(path):
	global ask
	global filesOpened_cnt
	global markdown
	global sep
	global base

	# fileBackup.switch( 'isPreOpen', delete=True )
	fileBackup.switch( 'isPreOpen' )
	fileBackup.switch( 'Input', path )
	fileBackup.action()

	if not os.path.isfile(path) or not path.lower().endswith('.md'):
		return None

	pass

	

	if base is None:
		base=''

	if _.switches.isActive('GUI-Edit'):
		
		if filesOpened_cnt == 0:
			filesOpened_cnt+=1
			openFile(path)


		elif filesOpened_cnt < 2 and ask is None:
			_.pr()
			ask=input(' open all ?:  ')
			_.pr()
			if not 'n' in ask.lower():
				filesOpened_cnt+=1
				openFile(path)
		elif filesOpened_cnt > 1:
			openFile(path)

	if not os.path.isfile(path) or not path.endswith('.md'):
		return None

	markdown.append( sep.replace('FILE_PATH',path.replace(base+os.sep,'')) + _.getText( path, raw=True ) )
base=None
def action():
	_.switches.fieldSet( 'GUI-Edit', 'active', True )
	global markdown
	global sep
	sep='''
-----
```md
	FILE:  FILE_PATH
```

-----
'''
	sep='\n\n\n-----\n\n-----\n\n\n'

	if _.switches.isActive('GUI-Edit'):
		sep=''

	if _.switches.isActive('GUI-Edit'):
		html = _.getText( _v.w +os.sep+ 'widgets' +os.sep+ 'html' +os.sep+ 'markdown' +os.sep+ 'showdown.min-2.0.0.js-PYTHON-EDIT.htm', raw=True )
	else:
		html = _.getText( _v.w +os.sep+ 'widgets' +os.sep+ 'html' +os.sep+ 'markdown' +os.sep+ 'showdown.min-2.0.0.js-PYTHON.htm', raw=True )

	save = _v.stmp +os.sep+ 'markdown.htm'

	if _.switches.isActive('Files'):
		base = os.getcwd()
		for path in _.switches.values('Files'):
			if os.path.isdir(path):
				getFolder(path)
			else:
				try:
					processFile(path)
				except Exception as e:
					pass

	if _.switches.isActive('Recursive'):
		_.switches.fieldSet( 'Folder', 'active', True )

	if _.switches.isActive( 'Folder' ):
		if len( _.switches.value('Folder') ):
			folder = _.switches.values( 'Folder' )[0]
		else:
			folder = os.getcwd()

		getFolder(folder)

	# else:
	#   base = os.getcwd()
	#   _.pipeCleaner(0)
	#   for i,row in enumerate(_.isData(r=1)):
	#       processFile(row)

	if _.switches.isActive('GUI-Edit'):
		delim='\n\n-----\n\n'
	else:
		delim=''
	global THE_PATH
	global port
	_.saveText( html.replace( 'MARKDOWN_HERE', delim.join(markdown) ).replace( 'PATH_HERE', THE_PATH ).replace( '8080', str(port) ), save )
	webbrowser.open(save, new=2)
	START_WEBSERVER()

import webbrowser
_file_open = _.regImp( __.appReg, 'file-open' )


fileBackup = _.regImp( focus(), 'fileBackup' )
fileBackup.switch( 'Silent' )
fileBackup.switch( 'Flag', 'imdb' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )
fileBackup.switch( 'isPreOpen', delete=True )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





