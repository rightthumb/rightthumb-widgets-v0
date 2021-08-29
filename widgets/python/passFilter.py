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

##################################################


def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','.bash_history', isPipe='data', description='Files' )
	_.switches.register( 'Save', '-save', '.bash_history' )


	


_.autoBackupData = False
__.isRequired_Pipe = True
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'passFilter.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'terminal history filter and cleaner ( USED IN x.bat )',
	'categories': [
						'terminal',
						'history',
						'tool',
						'exit',
						'x',
						'filter',
						'cleaner',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						'x.bat',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'type "%fileTempData%" | p passFilter >> "%file%"',
						''
	],
	'columns': [
				       # { 'name': 'name', 'abbreviation': 'n' },
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
# __.appRegPipe
########################################################################################
# START

def process( row ):
	if '-password' in row or '-pass' in row.lower() or '-pw' in row.lower() or 'crypt' in row.lower():
		parts = row.split(' ')
		isNext = False
		newRow = []
		for part in parts:
			if isNext:
				if part.startswith('-') or part.startswith('+'):
					isNext = False
				if isNext:
					part = '******'

			if '-pass' in part.lower() or '-pw' in part.lower() or '-en' in part.lower() or '-de' in part.lower():
				isNext = True

			newRow.append( part )
		row = ' '.join( newRow )
	return row


def action():
	theFile = []
	for i,row in enumerate( _.isData(r=1) ):
		newRow = process( row )
		theFile.append(newRow)
		print( newRow )

	if _.switches.isActive('Save'):
		# _.saveText( '\n'.join(theFile) , _.switches.values('Save') )
		_.saveText( theFile , _.switches.values('Save')[0] )

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	# 	_.pipeCleaner(0)
	# 	# _.printVar( _.appData )
	# 	for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
	# 		print( process( row ) )



########################################################################################
if __name__ == '__main__':
	action()




