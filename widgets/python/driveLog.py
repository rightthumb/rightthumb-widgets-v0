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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-input','file.txt')
	# _.switches.register('Files', '-f,-file,-files','file.txt')
	_.switches.register('Fields', '-f,-fields','n d')
	_.switches.register('Delim', '-delim')

	

_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT'
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
						'p driveLog + 8 -f p',
						'',
						'p driveLog + archive',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

_.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo[focus()]['columns'].append({'name': 'type', 'abbreviation': 't'})
_.appInfo[focus()]['columns'].append({'name': 'priority', 'abbreviation': 'p'})
_.appInfo[focus()]['columns'].append({'name': 'descriptors', 'abbreviation': 'd'})
_.appInfo[focus()]['columns'].append({'name': 'owner', 'abbreviation': 'o'})

_.appInfo[focus()]['columns'].append({'name': 'id', 'abbreviation': 'id'})
_.appInfo[focus()]['columns'].append({'name': 'serial', 'abbreviation': 'sn'})
_.appInfo[focus()]['columns'].append({'name': 'drive', 'abbreviation': 'drv'})
_.appInfo[focus()]['columns'].append({'name': 'machineID', 'abbreviation': 'm'})
_.appInfo[focus()]['columns'].append({'name': 'initiated', 'abbreviation': 'created'})
_.appInfo[focus()]['columns'].append({'name': 'initiated', 'abbreviation': 'date'})
_.appInfo[focus()]['columns'].append({'name': 'timestamp', 'abbreviation': 'time'})
_.appInfo[focus()]['columns'].append({'name': 'timestamp', 'abbreviation': 'modified'})
_.appInfo[focus()]['columns'].append({'name': 'volumesizeused', 'abbreviation': 'u'})
_.appInfo[focus()]['columns'].append({'name': 'volumesizeused', 'abbreviation': 'used'})
_.appInfo[focus()]['columns'].append({'name': 'volumesizefree', 'abbreviation': 'f'})
_.appInfo[focus()]['columns'].append({'name': 'volumesizefree', 'abbreviation': 'free'})
_.appInfo[focus()]['columns'].append({'name': 'volumesize', 'abbreviation': 'size'})
_.appInfo[focus()]['columns'].append({'name': 'volumesize', 'abbreviation': 's'})





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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	_.switches.trigger('Fields',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
#     if os.path.isdir(row):
#     if os.path.isfile(row):
########################################################################################
# START

def action():
	global data
	load()

	# if not type( _.appData[__.appReg]['pipe'] ) == bool:
	#     _.pipeCleaner()
	#     # _.printVar(_.appData)
	#     for i,row in enumerate(_.appData[__.appReg]['pipe']):
	#         pass



def load():
	global data
	file_drives = 'indexTable_drives-' + _v.getMachineID() + '.json'
	data = _.getTable( file_drives )
	records = []
	for record in data:
		show=False

		if _.switches.isActive( 'Fields' ):
			for search in _.switches.values( 'Fields' ):
				if _.showLine( str(record[search]) ):
					show=True

		else:
			if _.showLine( record['type'] ):
				show=True
			if _.showLine( str(record['priority']) ):
				show=True
			if _.showLine( record['descriptors'] ):
				show=True
			if _.showLine( record['name'] ):
				show=True
			if _.showLine( str(record['owner']) ):
				show=True
			if _.showLine( str(record['id']) ):
				show=True

		if show:
			record['size'] = record['volumesize']
			record['used'] = record['volumesizeused']
			record['free'] = record['volumesizefree']
			records.append( record )

	pass
	if not _.switches.isActive( 'Delim' ):
		_.tables.register( 'data', records )
		_.tables.fieldProfileSet( 'data', 'timestamp', 'trigger', _.resolveEpochTest )
		
		if not _.switches.isActive( 'Column' ):
			_.tables.print( 'data', 'owner,name,type,descriptors,priority,size,used,free,timestamp' )
		else:
			_.tables.print( 'data', _.switches.value( 'Column' ) )
	else:
		pass






	# {
	#     "serial": null,
	#     "name": "Papa's_74GB_archive_023_WD_SATA",
	#     "type": "archive",
	#     "priority": 8,
	#     "drive": "F:\\",
	#     "id": "{C1CB0F3E-AA5E-47BE-9A7B-8BBE69FE46E9}",
	#     "machineID": "{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}",
	#     "pc": "MSI",
	#     "initiated": 1569087967.6843686,
	#     "timestamp": 1569087999.3618705,
	#     "volumesizeused": "7.71GB",
	#     "volumesizefree": "66.82GB",
	#     "volumesize": "74.53GB",
	#     "drivesize": 137438953472.0,
	#     "descriptors": "023,WD,SATA",
	#     "owner": "Papa"
	# }



	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['liveAppName'], 'project': 'app_instance' }

	# if _.switches.isActive('Files'):
	#     tmpFiles = []
	#     hasFiles = False
	#     justNames = False
	#     if justNames:
	#         _.setPipeData( _.switches.values('Files'), focus() )
	#     else:
	#         for file in _.switches.values('Files'):
	#             if os.path.isfile( file ):
	#                 hasFiles = True
	#                 for row in _.getText( file, raw=True, clean=2 ).split('\n'):
	#                     tmpFiles.append( row )
	#     if hasFiles:
	#         _.setPipeData( tmpFiles, focus() )
	#     if not hasFiles:
	#         if type( _.appData[__.appReg]['pipe'] ) == bool:
	#             _.appData[__.appReg]['pipe'] = []
	#             for row in _.switches.value('Files').split( ',' ):
	#                 _.appData[__.appReg]['pipe'].append( row )

data = []
########################################################################################
if __name__ == '__main__':
	action()





