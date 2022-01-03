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

def openFile(path):
	print(path)
	global filesOpened
	if not path in filesOpened:
		filesOpened.append(path)

		_file_open.switch('App',_v.meta['code_editor'])
		_file_open.switch('Files',path)
		_file_open.action()

def processFile(path):
	global ask
	global filesOpened_cnt
	global markdown
	global sep
	global base

	if not os.path.isfile(path) or not path.endswith('.md'):
		return None

	

	if base is None:
		base=''

	if _.switches.isActive('GUI-Edit'):
		
		if filesOpened_cnt == 0:
			filesOpened_cnt+=1
			openFile(path)


		elif filesOpened_cnt < 2 and ask is None:
			print()
			ask=input(' open all ?:  ')
			print()
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
			processFile(path)

	if _.switches.isActive('Recursive'):
		_.switches.fieldSet( 'Folder', 'active', True )

	if _.switches.isActive( 'Folder' ):
		if len( _.switches.value('Folder') ):
			folder = _.switches.values( 'Folder' )[0]
		else:
			folder = os.getcwd()

		getFolder(folder)

	else:
		base = os.getcwd()
		_.pipeCleaner(0)
		for i,row in enumerate(_.isData(r=1)):
			processFile(row)

	if _.switches.isActive('GUI-Edit'):
		delim='\n\n-----\n\n'
	else:
		delim=''

	_.saveText( html.replace( 'MARKDOWN_HERE', delim.join(markdown) ), save )
	webbrowser.open(save, new=2)

import webbrowser
_file_open = _.regImp( __.appReg, 'file-open' )

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




