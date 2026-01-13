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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	### EXAMPLE: START
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isRequired=True, description='Files' )
	_.switches.register( 'Size', '-size' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'Delete', '-delete' )
	_.switches.register( 'Clean', '--c' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


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
						'p backupFootprint -file %scrap%',
						'p backupFootprint -file %scrap% %tmpf% %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9%',
						'p backupFootprint -file %tmpf% %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9% --c -print -size 2mb | p dirX -c s n -s s',
						'',
						'p backupFootprint -file %scrap%  --c -print | p dirX -c s n -s s -long',
						'',
						'p backupFootprint -file %tmpf% %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9% -size 2mb -delete',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START

import _rightThumb._dir as _dir

def process( subject ):
	global total_bytes
	global remove
	global size
	global log
	global i

	isClean = _.switches.isActive('Clean')

	for record in log:
		if record['file'] == subject:
			theBytes = _dir.info( record['backup'] )['bytes']
			shouldAdd = True
			if not size is None:
				if theBytes < size:
					shouldAdd = False

			if shouldAdd:
				total_bytes += theBytes
				i+=1
				remove.append( record['backup'] )
				if not isClean:
					_.updateLine( 'Calculating backup footprint '+_.addComma(i), clear=True )

def action():
	global total_bytes
	global remove
	global log
	global i
	load()

	isClean = _.switches.isActive('Clean')
	
	for subject in _.switches.values('Files'):
		process( subject )


	if not isClean:
		_.updateLine( '', clear=True )
	if isClean and _.switches.isActive('Print'):
		pass
	else:
		_.colorThis( [ _dir.formatSize( total_bytes ), 'found',i,'backups' ], 'yellow' )


	if _.switches.isActive('Print'):
		for x in remove:
			_.pr( x )

	if _.switches.isActive('Delete'):

		fileBackup = _.regImp( __.appReg, 'fileBackup' )
		# fileBackup.switch( 'Silent' )
		fileBackup.switch( 'isRunOnce' )
		fileBackup.switch( 'DoNotSchedule' )
		fileBackup.switch( 'Flag', 'bkFtprnt' )
		fileBackup.switch( 'Input', _v.myTables+_v.slash+'fileBackup.json' )
		recoveryFile = fileBackup.do( 'action' )
		ii=0
		ie = 0
		newLog = []
		errors = []
		for record in log:
			shouldKeep = True
			tried = False
			if record['backup'] in remove:
				shouldKeep = False
				tried = True
				try:
					os.remove( record['backup'] )
				except Exception as e:
					pass
				if os.path.isfile( record['backup'] ):
					shouldKeep = True
			if shouldKeep:
				newLog.append( record )
				if tried:
					errors.append(record['backup'])
					ie+=1

			else:
				ii+=1

		_.colorThis( [ ii, 'files deleted' ], 'yellow' )
		if ie:
			for x in errors:
				_.pr( '\t', x )
			_.colorThis( [ ie, 'file errors' ], 'red' )
		_.saveTable( newLog, 'fileBackup.json' )
				


def load():
	global size
	global log
	log = _.tables.returnSorted( 'data', 'a.timestamp', _.getTable('fileBackup.json') )

	if _.switches.isActive( 'Size' ):
		size = _dir.unFormatSize( _.switches.value( 'Size' ) )


remove = []
log = []
total_bytes = 0
i=0
size = None


# - p backupFootprint -file %tmpf% %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9% --c -size 2mb
# 4.07 GB found 25 backups

########################################################################################
if __name__ == '__main__':
	action()