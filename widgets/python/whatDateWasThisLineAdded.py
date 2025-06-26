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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isRequired=True, description='Files' )
	_.switches.register( 'Clean', '--c' )


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'whatDateWasThisLineAdded.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Find when a line was added to a file',
	'categories': [
						'date',
						'time',
						'help',
						'research',
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
						'p whatDateWasThisLineAdded -file %scrap% + "https://www.myfloridacounty.com/ori/index.do?x=61&y=28"',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START



def action():
	global log
	load()

	subject = _.switches.value('Files')
	records = []
	isClean = _.switches.isActive( 'Clean' )
	if not isClean:
		_.updateLine( 'Locating backups', clear=True )
	for record in log:
		if record['file'] == subject:
			records.append( record )


	i = 0
	total = len(records)
	for record in records:
		i+=1
		if not isClean:
			_.updateLine( 'Checking file '+_.addComma(i)+' of '+_.addComma(total)+' files', clear=True )
		for line in _.getText( record['backup'] ):
			if _.showLine( line ):
				if not isClean:
					_.updateLine( '', clear=True )
					_.colorThis( [ 'Found:\n' ], 'green' )
					_.colorThis( [ '\t\t', _.friendlyDate( record['timestamp'] ) ], 'green' )
					_.colorThis( [ '\n\non file', _.addComma(i), 'of', _.addComma(len(records)), 'files' ], 'yellow' )
				elif isClean:
					_.colorThis( [ _.friendlyDate( record['timestamp'] ) ], 'green' )
				sys.exit()

	"""
	{
		"id": "{05A05E79-56FA-86EC-69F5-9913529FA9AC}",
		"timestamp": 1551215270.9417222,
		"file": "D:\\tech\\programs\\python\\src\\windows\\txtRecover.py",
		"backup": "D:\\tech\\hosts\\MSI\\backup\\txt\\1551215270.9417222-2019_02_26-16_03_41-txtRecover.py",
		"mime": "text",
		"status": 1,
		"version": "0.0.0.1",
		"v": 0,
		"v1": 0,
		"v2": 0,
		"v3": 1,
		"flag": ""
	}
	"""


def load():
	global log
	log = _.tables.returnSorted( 'data', 'a.timestamp', _.getTable('fileBackup.json') )


log = []



########################################################################################
if __name__ == '__main__':
	action()






