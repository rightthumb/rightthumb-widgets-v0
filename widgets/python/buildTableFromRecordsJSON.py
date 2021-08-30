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
# 	profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
# 	_blowfish.encrypt( infilepath, outfilepath, key )
# 	_blowfish.decrypt( infilepath, outfilepath, key )
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
# 	_file_folder.switch( 'Save,Clean' )
# 	_file_folder.switch( 'Compair,Clean' )
# 	_file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
# 	_fileNameDate.imp.newName( filename )
# 	_fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
	# folderReport = _filePathPatterns.action()
# txtBackup = _.regImp( __.appReg, 'txtBackup' )
# 	txtBackup.switch( 'Input', filename )
# 	txtBackup.switch( 'Flag', 'pre replaceText' )
# 	recoveryFile = txtBackup.do( 'action' )
##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register( 'Timestamp', '-timestamp', description='Add timestamp from modification epoch' )
	_.switches.register( 'Label', '-label', isRequired=True, description='New table name' )
	_.switches.register( 'Folder', '-folder' )
	_.switches.register( 'UniqueKey', '-key' )

	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True description='' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False


_.appInfo[focus()] = {
	'file': 'buildTableFromRecordsJSON.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Build table from individual json files',
	'categories': [
						'tool',
						'convert',
						'build',
						'table',
						'records',
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
						'p buildTableFromRecordsJSON -timestamp + netblock_* -label netblockCache.json -key ip',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





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
	# _.switches.trigger('Input',_.formatColumns)
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
# _.showLine(item)
# 	if os.path.isdir(row):
# 	if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START

def process( row ):
	global data
	try:
		record = _.getTable2( row )
	except Exception as e:
		record = False

	if not type(record) == dict:
		return False
	if not len( record.keys() ):
		return False

	if _.switches.isActive('Timestamp'):
		record['timestamp'] = os.path.getmtime( row )
	data.append( record )


def uniqueKey():
	global data
	global spent

	newData = []
	if not len( data ):
		return False
	else:
		if 'timestamp' in data[0].keys():
			data = _.tables.returnSorted( 'data', 'd.timestamp', data )
	uniqueKey = _.switches.values('UniqueKey')[0]
	allKeys = []
	for record in data:
		for key in record.keys():
			if not key in allKeys:
				allKeys.append( key )
	for record in data:
		if not record[uniqueKey] in spent:
			for key in allKeys:
				if not key in record.keys():
					record[key] = ''
			newData.append( record )
	data = newData


def action():
	global data
	load()

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		# _.pipeCleaner()
		# _.printVar(_.appData)
		total = len(_.appData[__.appReg]['pipe'])
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			print( str(i) + ' of ' + str(total), end='\r', flush=True )
			if _.showLine( row ):
				process( row )
		pass
		if _.switches.isActive('UniqueKey'):
			uniqueKey()
		print( '                                                                       ', end='\r', flush=True )
		# print( 'Done' )
		_.saveTable( data, _.switches.values('Label')[0] )


def load():
	if _.switches.isActive('Folder'):
		folder = _.switches.values('Folder')[0]
	else:
		folder = os.getcwd()

	_.setPipeData( os.listdir(folder) , focus() )
	


data = []
spent = []
########################################################################################
if __name__ == '__main__':
	action()





