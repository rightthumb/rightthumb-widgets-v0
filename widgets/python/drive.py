#!/usr/bin/python3
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
	_.switches.register('Scan', '-scan')
	_.switches.register('Index', '-i,-index','usb, C:\\ D:'+_v.slash)
	_.switches.register('History', '-h,-history')
	_.switches.register('Path', '-p,-path')


_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'drive.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'Manages drives and indexes',
	'categories': [
						'index',
						'drive',
						'admin',
						'manage',
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
						'p drive -scan',
						'p drive -index usb',
						'p drive -index usb internal',
						'p drive -index C:\\Users\\Scott\\Desktop Desktop',
						'p drive -index C:\\ D:'+_v.slash,
						'p drive -index cloud',
						'',
	],
	'columns': [
				       # { 'name': 'name', 'abbreviation': 'n' },
				       # { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
						{ 'name': 'name', 'abbreviation': 'n' },
						{ 'name': 'initiated', 'abbreviation': 'i' },
						{ 'name': 'type', 'abbreviation': 't' },
						{ 'name': 'priority', 'abbreviation': 'p' },
						{ 'name': 'drive', 'abbreviation': 'dldr' },
						{ 'name': 'machineID', 'abbreviation': 'm' },
						{ 'name': 'timestamp', 'abbreviation': 'tstimedate' },
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

	# print( _drive.Scan().file_drives )
	i=0
	while i < 100:
		i+=1
		print( 'Uncle Scotty, I just love being with you.' )


import _rightThumb._drive as _drive
# from _rightThumb._date import _date
# import _rightThumb._date as _date



########################################################################################
if __name__ == '__main__':
	action()




