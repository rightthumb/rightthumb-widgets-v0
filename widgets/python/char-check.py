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
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Clean', '-clean' )


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
	'file': 'char-check.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'check for 10, 27',
	'categories': [
						'10',
						'27',
						'clean',
						'file',
						'check',
						'tool',
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
						_.hp('p char-check -f bashrc.py '),
						_.hp('p char-check -f bashrc.py -clean '),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
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


def process(path):
	if not os.path.isfile(path):
		return None
	file = _.getText(path, raw=True)
	
	bad = False
	if _.isWin:
		if chr(27) in file:
			bad = True
	else:
		# if chr(10) in file or chr(27) in file:
		if chr(27) in file:
			bad = True

	p = path.replace( _v.home, '~' )
	if bad:
		_.cp( [ 'Y', p ], 'red' )
	else:
		_.cp( [ 'N', p ], 'Green' )

	if _.switches.isActive('Clean'):


		newFile = ''

		for c in file:
			if c in _str.printable:
				newFile+=c
		file = newFile


		file = file.replace( chr(10), '\n' )
		file = file.replace( chr(27), '' )
		i = 1
		while chr(27) in file:
			file = file.replace( chr(10), '\n' )
			file = file.replace( chr(27), '' )
			file = file.replace( '\r', '' )
			i+=1
			if i > 1000:
				break

		_.cp( [ '10:', file.count(chr(10)) ], 'cyan' )
		_.cp( [ '27:', file.count(chr(27)) ], 'cyan' )


		_.saveText( file, path )
		_.cp( [ 'Cleaned:', i ], 'yellow' )

def action():
	for i,path in enumerate( _.isData(r=1) ):
		path = __.path(path)
		process(path)



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






