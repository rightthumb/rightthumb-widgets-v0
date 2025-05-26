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
	_.switches.register( 'Folder', '-folder' )
	_.switches.register( 'Recursive', '-r,-recursive')
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'Test', '-t,-test' )

	

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'char-scan.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'scan for valid print chars in text files',
	'categories': [
						'char',
						'scan',
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
						'p char-scan -r ',
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
	_.switches.trigger( 'Folder', _.myFolderLocations )
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
	try:
		files = os.listdir( folder )
	except Exception as e:
		return None
	for file in files:
		path = folder +os.sep+ file
		if os.path.isdir(path):
			if _.switches.isActive('Recursive'):
				getFolder(path)
		elif os.path.isfile(path):
			if _.showLine(path):
				process(path)

def process(path):
	global data
	# _.pr(path)
	try:
		m = _mime.isText( path )
	except Exception as e:
		return None
	_.pr( m,  path)
	theFile = ''
	shouldScan = False
	# return None
	try:
		if m:
			shouldScan = True
			theFile = _.getText( path, raw=True, clean=2 )
	except Exception as e:
		return None
	if shouldScan:
		for char in theFile:
			if not char in data:
				data.append(char)

	


def action():
	# should be   Single-Task   OR   Imply-Architecture-Functions   OR   CLASSES!!
	load()
	global data

	if _.switches.isActive('Print'):
		_.pr(  ' '.join(data)  )
		return None
	if _.switches.isActive('Test'):

		for file in _.switches.values('Test'):
			head = " ".join(['{:02X}'.format(byte) for byte in     open( file , 'rb' ).read(500)    ])
		what = 'text'
		for hx in head.split(' '):
			x = ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])
			if not x in data:
				what = 'bin'
				break
		_.pr(what)        
			
		return None

	if _.switches.isActive('Folder'):
		folder = _.switches.values('Folder')[0]
	else:
		folder = os.getcwd()
	getFolder( folder )

	_.saveTableDB( data, 'text-file-chars.list', indentCode=False )
	_.pr( 'Saved: text-file-chars.list' )


def load():
	global data
	data = _.getTableDB( 'text-file-chars.list' )

import _rightThumb._mimetype as _mime


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







