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


# _nd = _.regImp( __.appReg, 'fileNameDate' )
#   _nd.pipe( [databaseFile] )
#   _nd.do( 'action' )

# _textIndex = _.regImp( __.appReg, 'words' )
	# _textIndex.switch( 'Alpha' )
	# _textIndex.switch( 'Unique' )
	# _textIndex.switch( 'MinLength', 2 )
	# _textIndex.switch( 'Stemming' )
	# _textIndex.switch( 'PartsOfSpeech' )
	# _textIndex.switch( 'Clean' )
	# _textIndex.pipe( data )
#   index = _textIndex.do( 'action' )

# _bm = _.regImp( __.appReg, 'bookmarks' )
	# index = _bm.imp.index()
# _dirList = _.regImp( __.appReg, 'dirList' )
#   _dirList.switch( 'Files' )
#   _dirList.switch( 'Recursion' )
#   _dirList.switch( 'Binary' )
#   _dirList.switch( 'Path','D:\\Apps' )
#   files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#   profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#   _blowfish.encrypt( infilepath, outfilepath, key )
#   _blowfish.decrypt( infilepath, outfilepath, key )
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
#   _file_folder.switch( 'Save,Clean' )
#   _file_folder.switch( 'Compair,Clean' )
#   _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#   _fileNameDate.imp.newName( filename )
#   _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#   fileBackup.switch( 'Input', filename )
#   fileBackup.switch( 'Flag', 'pre replaceText' )
#   recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#   _folderContent.switch( 'Silent' )
#   _folderContent.switch( 'Folder', _v.myAppsBatch )
#   _folderContent.switch( 'NoExtension' )

#   _folderContent.switch( 'Recursive' )

#   _folderContent.switch( 'Text' )
#   _folderContent.switch( 'Binary' )
#   _folderContent.switch( 'Label', 'App: ' )
#   _folderContent.switch( 'Prefix', ';t' )
#   files = _folderContent.do( 'action' )['files']
#   folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#   _tickets.switch( 'ReturnFiles' )
#   records = _tickets.do( 'records' )
##################################################
# from lxml import html
# import requests
# import cssselect
# import sqlite3
##################################################


def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'Hijack_This_Log.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Hijack_This_Log analyzer',
	'categories': [
						'Hijack Hijack',
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
						'p thisApp -file file.txt',
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
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	
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
	global whitelist
	global log
	load()

	for row in log:
		# row = row.encode('utf-8')
		# row = str(row,'iso-8859-1')
		bad = True
		for check in whitelist:
			check = _str.cleanBE( check, ' ' )
			dic={}
			dic['a']=check
			dic['b']=row
			# _.pr(dic)

			# sys.exit()
			# _.pr(row)

			if check.lower() in row.lower():
				# _.pr(row)
				bad = False

		# if not len(row):
		#   bad = False
		if bad:
		_.pr( row.replace('\n','') )


def load():
	global whitelist
	global log
	# whitelist = _.getText( _v.dbTables+os.sep+'HijackThis_Whitelist.txt', raw=True, clean=2 ).lower().replace('\r','')
	# _.pr(whitelist)
	# sys.exit()
	whitelist = _.getText( _v.dbTables+os.sep+'HijackThis_Whitelist.txt', raw=True, clean=2 ).lower().replace('\r','').split('\n')
	log = _.getText( _.switches.values('Files')[0] , raw=True, clean=2 ).replace('\r','').split('\n')



whitelist = []
log = []
########################################################################################
if __name__ == '__main__':
	action()