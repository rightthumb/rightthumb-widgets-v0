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

import os
import sys
import time
# import platform
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
	_.switches.register( 'Make', '-make', ';sp', isRequired=True )
	_.switches.register( 'Increment', '-inc', '0000' )
	_.switches.register( 'Iterations', '-it,-iter,-iterate,-iterations', '5 r' )
	


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = ['Make']
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'lineM.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'similar to "line -make" but does not replace any text',
	'categories': [
						'make',
						'line',
						'code',
						'tool',
						'generate',
						'gen',
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
						'type  %tmpf0% | p lineM -make "{},"',
						'',
						'echo null | p lineM -make "Win10Pro-(n).iso" -inc -it 10',
						'',
						'echo null | p lineM -make "p link -src Win10Pro.iso -dst Win10Pro-(n).iso" -inc -it 10 | p execute',
						'',
						'echo null | p lineM -make " this is (n) test>>file.txt" -inc 00 -it 20 | p execute',
						'echo null | p lineM -make "echo this is (n) test>>file.txt" -inc 0000 -it 1000 r > %tmpf0%',
						'',
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
	__.myFileLocations_SKIP_VALIDATION = False
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START

if _.switches.isActive('Increment'):
	mm = 4
	if len(_.switches.value('Increment')):
		mm = len(_.switches.value('Increment'))
	_.fields.register( 'cnt', 'val', 7, m=mm )



def action():
	make = ' '.join( _.switches.values('Make') )
	ii = 1
	for i,row in enumerate(_.isData(r=1)):
		if len(row):
			it = 1
			ix = 0
			if _.switches.isActive('Iterations'):
				it = int(_.switches.values('Iterations')[0])
				irt = it
			while not it == ix:
				m = make.replace( '{}', row )
				if _.switches.isActive('Increment'):
					if len(_.switches.values('Iterations')) > 1 and _.switches.values('Iterations')[1] == 'r':
						test = _.fields.padZeros( 'cnt', 'val', irt )
					else:
						test = _.fields.padZeros( 'cnt', 'val', ii )
					m = m.replace( '(n)', test )
					ii+=1
					irt-=1
				_.pr( m )
				ix+=1

########################################################################################
if __name__ == '__main__':
	action()