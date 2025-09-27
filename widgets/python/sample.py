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

	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, description='Files' )
	
	_.switches.register( 'Length', '-length' )

	_.switches.register( 'Top', '-top' )
	_.switches.register( 'Tail', '-tail' )
	_.switches.register( 'Sample', '-sample' )


_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'filePart.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Return part of file',
	'categories': [
						'peek',
						'file',
						'sample',
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
						'p thisApp -file file.txt',
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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



def action():
	
	if _.switches.isActive('Length'):
		_.pr( len( _.isData(required=True) ) )

	if _.switches.isActive('Top'):
		end = int( _.switches.value('Top') )
		for i,row in enumerate(_.isData(required=True)):
			if i <= end:
				_.pr(row)

	if _.switches.isActive('Sample'):
		start = int( _.switches.values('Sample')[0] )
		try:
			end = int( _.switches.values('Sample')[1] )
		except Exception as e:
			end = len(_.isData(required=True))
		for i,row in enumerate(_.isData(required=True)):
			if i >= start:
				if i <= end:
					_.pr(row)

	if _.switches.isActive('Tail'):
		end = int( _.switches.value('Tail') )
		results = []
		data = _.isData(required=True)
		data.reverse()
		for i,row in enumerate(data):
			if i <= end:
				results.append(row)
		results.reverse()
		for x in results:
			_.pr(x)

########################################################################################
if __name__ == '__main__':
	action()







