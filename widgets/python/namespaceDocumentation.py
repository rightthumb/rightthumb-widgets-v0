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
import _rightThumb._dir as _dir
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
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
	# folderReport = _filePathPatterns.action()

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
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


_.appInfo[focus()] = {
	'file': 'namespaceDocumentation.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage namespace documentation',
	'categories': [
						'python',
						'namespace',
						'documentation',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						'p countListItemsInFiles ?',
						'p countListItemsInFilesReport',
	],
	'examples': [
						'p namespaceDocumentation',
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
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START

def defaultRecordRoot():
	return {
				'label': '',
				'description': '',
				'myApp': False,
				'records': [],
				'tags': [],
	}

def defaultRecordPath():
	return {
				'label': '',
				'path': '',
				'description': '',
				'records': [],
				'tags': [],
	}

def defaultRecordFunction_Variable():
	return {
				'label': '',
				'path': '',
				'description': '',
				'type': 'function,variable',
				'hasReturn': True,
				'hasArgument': True,
				'potential': [{ 'data_type': '', 'value': '', 'usage': [{ 'determined': '', 'path': 'this,appName', 'type': 'function || if', 'category': 'display,option' }] }],
				'tags': [],
	}

def nextRecord( name ):
	global documentation
	# global spaceID

	if not len(documentation):
		processName( name )
	else:

		fieldBase = "['THIS']"
		commandBase = 'documentation'

		buildCommand = commandBase
		space = name.split('.')
		spaceID = 0
		found = False
		for record in documentation:
			if record['label'] == space[spaceID]:
				found = True
				locateRecord( record['records'], space, spaceID )
		if not found:
			documentation.append( addRecord( 'root', space[spaceID] ) )
			_.saveData( documentation, 'namespace_records' )
			nextRecord( name )
			


def acquireID( name ):
	global documentation
	return buildIDS( documentation, name )

def buildIDS( records, name, spaceID=False ):
	if type(spaceID) == bool:
		spaceID = 0
	else:
		spaceID +=1
	space = name.split('.')
	thisName = space[spaceID]
	if spaceID == (len(space)-1):
		isLast = True
	else:
		isLast = False
	
	for i,record in enumerate(records):
		if record['label'] == thisName:
			if isLast:
				return i
			else:
				return buildIDS( record['records'], name, spaceID )



	# documentation[acquireID('os')]['records'][acquireID('os.path')]['records'][acquireID('os.path.isfile')] 

def theAppend( name ):
	global documentation
	# name = os.path.isfile
	commandBase = 'documentation'
	one = "[acquireID('THIS')]['records']"
	two = '.append( data )'

	buildCommand = commandBase
	space = name.split('.')

	for i,x in enumerate(space):
		buildCommand += one.replace( 'THIS', pathGen( name, i ) )
		if i == (len(space)-1):
			buildCommand += two

	# documentation[acquireID('os')]['records'][acquireID('os.path')]['records'].append( data )
	return buildCommand

def pathGen( name, spaceID ):
	result = []
	for i,space in enumerate(name.split('.')):
		if i <= spaceID:
			result.append( space )
	return '.'.join( result )


def addRecord( what, name ):
	if what == 'root':
		template = defaultRecordRoot()
		template['label'] = name
	if what == 'path':
		template = defaultRecordPath()
		template['path'] = name
		x = name.split('.')
		template['label'] = x[len(x)-1]
	if what == 'item':
		template = defaultRecordFunction_Variable()
		template['path'] = name
		x = name.split('.')
		template['label'] = x[len(x)-1]


	_.saveData( template, 'namespaceDocumentation_temp' )
	tempFile = _v.myTables + _v.slash+'namespaceDocumentation_temp.json'
	createEpoch = _dir.fileInfo( tempFile )['date_modified_raw']
	checkEpoch = createEpoch
	do = 'n "' + tempFile + '"'
	os.system('"' + do + '"')
	while createEpoch == checkEpoch:
		time.sleep( 30 )
		checkEpoch = _dir.fileInfo( tempFile )['date_modified_raw']
	return _.getData( 'namespaceDocumentation_temp' )

def locateRecord( records, space, spaceID ):
	# global spaceID
	spaceID+=1
	if spaceID == (len(space)-1):
		isLast = True
	else:
		isLast = False
	for record in records:
		pass

def processName( name ):
	pass

def action():
	global namespace
	global documentation
	load()

	test = theAppend( 'os.path.isfile' )
	_.pr( test )
	sys.exit()

	if not len( documentation ):
		nextRecord( namespace[0] )
	else:
		for name in namespace:
			nextRecord( name )




def load():
	global namespace
	global documentation
	namespace = _.getData( 'namespace_tree' )
	documentation = _.getData( 'namespace_records' )


# documentation[acquireID('os')]['records'][acquireID('os.path')]['records'][acquireID('os.path.isfile')]['records'].append( data )
# 127

namespace = []
documentation = []
spaceID = 0
########################################################################################
if __name__ == '__main__':
	action()






