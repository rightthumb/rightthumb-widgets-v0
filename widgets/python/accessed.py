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
	_.switches.register( 'Epoch', '-epoch' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Folders', '-folder,-folders','folder', description='Folders' )
	_.switches.register( 'Oldest', '-o,-old,-oldest', '5' )
	_.switches.register( 'Newest', '-n,-new,-newest', '20' )
	_.switches.register( 'Path', '-p,-path' )
	_.switches.register( 'NoDate', '-nd,-nodate,-nodates' )
	_.switches.register( 'NoFile', '-nf,-nofile,-nofiles' )
	_.switches.register( 'SearchPath', '-sp,-searchpath' )



	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.isRequired_or_List = ['Pipe','Files','Folders']

_.appInfo[focus()] = {
	'file': 'accessed.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'When was a file (or files) last accessed',
	'categories': [
						'accessed',
						'access',
						'file',
						'meta',
						'metadata',
						'meta data',
						'date',
						'use',
						'usage',
						'used',
						'pipe',
						'file',
						'files',
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
						'p file --c | p accessed -epoch | sort | p resolveIDs',
						'p files --c | p accessed -epoch | sort | p resolveIDs',
						'',
						'p files --c | p accessed -n 20 -p',
						'',
						'p files --c | p accessed -n 20 -p -nd',
						'p files --c | p accessed -newest 20 -path -nodate',
						'p files --c | p accessed -newest 20 -path -nodates',
						'',
						'p files --c | p accessed -o 20 -nf',
						'p files --c | p accessed -oldest 20 -nofiles',
						'',
						'p accessed -f 3T_drive.txt testSSL.bat',
						'',
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
# data = _.tables.returnSorted( 'data', 'd.epoch', data )
# __.appRegPipe
########################################################################################
# START

def action():
	records = []
	hasMultiple = False
	if _.switches.isActive('Epoch'):
		keepEpoch = True
	else:
		keepEpoch = False

	if _.switches.isActive('Files'):

		if len(_.switches.values('Files')) > 1:
			hasMultiple = True

		for file in _.switches.values('Files'):
			if os.path.isfile( file ):
				epoch = os.path.getatime(file)
				date = _.friendlyDate( epoch )
				fx = file.split(_v.slash)
				fx.reverse()
				if _.switches.isActive('SearchPath'):
					search = os.path.abspath(file)
				else:
					search = fx[0]
				if _.showLine( search ):
					records.append({ 'epoch': epoch, 'date': date, 'file': fx[0], 'path': os.path.abspath(file) })

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		hasMultiple = True
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,file in enumerate( _.appData[__.appReg]['pipe'] ):
			if os.path.isfile( file ):
				epoch = os.path.getatime(file)
				date = _.friendlyDate( epoch )
				fx = file.split(_v.slash)
				fx.reverse()
				if _.switches.isActive('SearchPath'):
					search = os.path.abspath(file)
				else:
					search = fx[0]
				if _.showLine( search ):
					records.append({ 'epoch': epoch, 'date': date, 'file': fx[0], 'path': os.path.abspath(file) })



	if len(records):
		howMany = None
		if _.switches.isActive('Sort') or _.switches.isActive('Oldest') or _.switches.isActive('Newest'):


			val = None
			if _.switches.isActive('Oldest'):
				val = _.switches.value('Oldest')

			if _.switches.isActive('Newest'):
				val = _.switches.value('Newest')

			if not val is None and len(val):
				howMany = int(val)

			records = _.tables.returnSorted( 'data', 'd:epoch', records )
			if _.switches.isActive('Oldest'):
				records.reverse()
		spent = 0
		fileField = None
		dateField = None
		hasTab = False
		if hasMultiple:
			fileField = 'file'
		if _.switches.isActive('Path'):
			fileField = 'path'

		if keepEpoch:
			dateField = 'epoch'
		else:
			dateField = 'date'

		if _.switches.isActive('NoDate'):
			dateField = None

		if _.switches.isActive('NoFile'):
			fileField = None

		if not fileField is None and not dateField is None:
			hasTab = True


		for i,record in enumerate(records):
			shouldPrint = True
			if not howMany is None:
				if spent >= howMany:
					shouldPrint = False

			if shouldPrint:
				spent += 1

				r = ''
				if not dateField is None:
					r += str(record[dateField])

				if hasTab:
					r += '\t'

				if not fileField is None:
					r += str(record[fileField])

				_.pr( r )
				# if keepEpoch and hasMultiple:
				#     _.pr(  record['epoch'], record['file']  )
				# if keepEpoch and not hasMultiple:
				#     _.pr(  record['epoch']  )
				# if not keepEpoch and hasMultiple:
				#     _.pr(  record['date'], record['file']  )
				# if not keepEpoch and not hasMultiple:
				#     _.pr(  record['date']  )


########################################################################################
if __name__ == '__main__':
	action()







