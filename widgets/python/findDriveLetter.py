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
	pass
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'ID', '-id' )
	_.switches.register( 'Scan', '-scan,-all,-list' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'findDriveID.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Find drive ID by searching label or descriptors',
	'categories': [
						'drive',
						'search',
						'drive id',
						'drive search',
						'registration',
						'search registration',
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
						'p findDriveID + 3t backup',
						'p findDriveID -id + {D644A899-89BB-9748-8339-3FC5F75B8A16}',
						'',
						'theDriveID + my 256GB btn Sandisk BLK',
						'',
						'theDriveID + 3t backup',
						'  theDrive %theDrive%',
						'  echo %theDrive%',
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

def driveScan( driveID ):
	letters = 'CDEFGHIJKLMNOPQRSTUVWXYZ'
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for letter in letters:
		test = letter+':\\drive.id.sys'
		# _.pr(letter)
		if os.path.isfile( test ) and driveID in _.getText( test, raw=True ):
			return letter
	# _.pr('Error')
	return 'Error'
def action():
	global data
	load()

	for i,record in enumerate(data):
		data[i]['scan_results'] = 'Not Connected'
	

	records = []
	if not _.switches.isActive('ID'):

		for record in data:
			if _.showLine( record['name'] ):
				records.append( record )

		if not len(records):
			for record in data:
				if _.showLine( record['descriptors'] ):
					records.append( record )

		if len(records) == 0:
			_.pr( '0' )
			return None


		
		if not _.switches.isActive('Scan') and len(records) == 1:
			scan = driveScan( records[0]['id'] )
			_.pr( scan )
		else:
			_.fields.asset( 'data', records )
			# _.pr(records[0].keys())
			for record in records:
				scan = driveScan( record['id'] )
				if scan == 'Error':
					color = 'red'
				else:
					color = 'green'
				# _.pr( record.keys() )
				part = '\t'
				part += _.colorThis( [  _.fields.value( 'data', 'name', record['name'].replace('-',' ').replace('_',' '), right=1 )  ], color, p=0 )
				part += '   '

				# _.pr(scan)
				if scan == 'Error':
					part += _.colorThis( [  _.fields.value( 'data', 'scan_results', 'Not Connected' )  ], color, p=0 )
				else:
					part += _.colorThis( [  _.fields.value( 'data', 'scan_results', scan+':'+_v.slash )  ], color, p=0 )

				part += '   '
				part += _.colorThis( [  _.fields.value( 'data', 'id', record['id'], right=1 )  ], color, p=0 )
				_.pr( part )

	elif _.switches.isActive('ID'):
		_.fields.asset( 'data', data )
		for record in data:
			if _.showLine( record['id'] ):
				driveScan( records['id'] )



def load():
	global data
	machineID = _v.getMachineID()
	file_drives = 'indexTable_drives-' + machineID + '.json'
	data = _.getTable( file_drives )


data = []


########################################################################################
if __name__ == '__main__':
	action()