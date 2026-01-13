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



# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', isRequired=True, description='Files' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'findPrint.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Add line number to all print commands in python, then undo',
	'categories': [
						'programming',
						'tool',
						'help',
						'troubleshoot',
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
						'p findPrint -f line.py ',
						''
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

from shutil import copyfile

fileBackup = _.regImp( __.appReg, 'fileBackup' )
# fileBackup.switch( 'Silent' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )


def processFile( filename ):

	_.pr()
	_.pr('processing:', filename)
	fileBackup.switch( 'Input', filename )
	fileBackup.switch( 'Flag', 'pre findPrint' )
	recoveryFile = fileBackup.do( 'action' )

	file = _.getText( filename )

	newFile = []
	rows = []
	for i,line in enumerate(file):
		line = line.replace( '\n', '' )
		tmp = line.replace( '\t', ' ' )
		tmp = _str.replaceDuplicate( tmp, ' ' )
		tmp = _str.cleanBE( tmp, ' ' )
		shouldRun = False
		if tmp.startswith('_.pr('):
			shouldRun = True

		if shouldRun:
			newFile.append( line.replace( '_.pr(', '_.pr('+str(i+1)+',' ) )
		else:
			newFile.append(line)



	_.saveText( newFile, filename )



	if _.switches.isActive('Files'):

		keep=input('Keep changes? ')
		if 'n' in keep.lower():
			try:
				copyfile(recoveryFile, os.path.abspath(filename))
				_.colorThis( 'Undo successful', 'green' )
			except Exception as e:
				_.colorThis( 'Undo fail', 'red' )
				_.pr( recoveryFile )
				_.pr( os.path.abspath(filename) )



def action():
	pass
	global data

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			processFile(row)



########################################################################################
if __name__ == '__main__':
	action()