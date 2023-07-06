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

# _bm = _.regImp( __.appReg, 'bookmarks' )
	# index = _bm.imp.index()
# _dirList = _.regImp( __.appReg, 'dirList' )
#     _dirList.switch( 'Files' )
#     _dirList.switch( 'Recursion' )
#     _dirList.switch( 'Binary' )
#     _dirList.switch( 'Path','D:\\Apps' )
#     files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
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
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#     fileBackup.switch( 'Input', filename )
#     fileBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )
##################################################
# from lxml import html
# import requests
# import cssselect
# import sqlite3
##################################################


def appSwitches():
	pass
	_.switches.register( 'Folder', '-folder' )
	_.switches.register( 'Undo', '-u,-undo' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'file_folder_name_clean.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Renames Files and folders to cleaner format',
	'categories': [
						'tool',
						'files',
						'file',
						'folders',
						'folder',
						'rename',
						'name',
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
						'p file_folder_name_clean ',
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
# __.appRegPipe
########################################################################################
# START

def clean( name ):

	name = name.replace('\n',' ')
	name = name.replace('\r',' ')
	name = name.replace('\t',' ')

	name = _str.replaceDuplicate( name, ' ' )
	name = _str.cleanBE( name, ' ' )

	name = _str.replaceDuplicate( name, '.' )

	name = name.replace( ' ', '_' )

	name = _str.replaceDuplicate( name, '-' )
	name = _str.replaceDuplicate( name, '_' )
	name = _str.cleanEnd( name, '.' )
	name = _str.cleanEnd( name, '-' )
	name = _str.cleanEnd( name, '_' )

	return name


def process( old_name ):
	global data
	global undo
	
	if not _.showLine( old_name ):
		return None

	if not os.path.isfile( old_name ) and not os.path.isdir( old_name ):
		return None

	p = os.path.abspath( old_name ).split(_v.slash)
	p.reverse()
	file = p.pop(0)
	p.reverse()


	if '.' in file and os.path.isfile( old_name ):
		e = file.split( '.' )

		e.reverse()
		ext = e.pop(0)
		e.reverse()

		ext = ext.lower()

		file = '.'.join( e )
	else:
		ext = ''

	folder = _v.slash.join( p )
	new_name = clean( file )

	if not file == new_name:
		
	
		# _.pr( folder, '\t', file, '\t', new_name )

		# sys.exit()
		# _dir.fileInfo
		if len( ext ):
			name_old = folder + _v.slash + file + '.' + ext
			name_new = folder + _v.slash + new_name + '.' + ext

		else:
			name_old = folder + _v.slash + file
			name_new = folder + _v.slash + new_name
		record = { 'old': file , 'new': new_name, 'ext': ext.upper(), 'path': name_old }
		data.append( record )
		# _.pr(  '\t', file, '\t', new_name )
		undo[name_new] = record
		os.rename( name_old, name_new )

def unprocess( old_name ):
	global data
	global undo

	if not _.showLine( old_name ):
		return None

	pass

	if not os.path.isfile( old_name ) and not os.path.isdir( old_name ):
		return None

	name_old = os.path.abspath( old_name )
	try:
		# name_new = undo[name_old]
		name_new = undo[name_old]['path']
		record = undo[name_old]
		del undo[name_old]
	except Exception as e:
		name_new = ''

	if len(name_new):
		data.append( record )

		# _.pr(  '\t', name_old, '\t', name_new )
		os.rename( name_old, name_new )


def action():
	global data
	global undo
	load()

	# _.colorThis( [ 'Needs undo' ], 'red' )
	# pause=input('Notice:  ')

	# if len(pause):
	#     _.colorThis( [ 'Exit requested' ], 'yellow' )
	#     sys.exit()



	if _.switches.isActive('Undo'):
		# _.printVar( undo )
		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner(0)
			# _.printVar( _.appData )
			for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
				try:
					unprocess( row )
				except Exception as e:
					pass

		if data:
			_.saveTable( undo, 'file_folder_name_clean.json', p=0 )

			_.tables.register( 'data', data )
			_.tables.print( 'data', 'ext,old,new' )
		sys.exit()


	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			try:
				process( row )
			except Exception as e:
				pass
		if data:
			_.saveTable( undo, 'file_folder_name_clean.json', p=0 )
			_.tables.register( 'data', data )
			_.tables.print( 'data', 'ext,old,new' )



def load():
	global undo

	_.switches.fieldSet( 'Long', 'active', True )
	_.switches.fieldSet( 'GroupBy', 'active', True )
	_.switches.fieldSet( 'GroupBy', 'value', 'ext' )

	undo = _.getTable( 'file_folder_name_clean.json' )
	if not len(undo):
		undo = {}

	if type( _.appData[__.appReg]['pipe'] ) == bool:

		_.appData[__.appReg]['pipe'] = []
		folder = os.getcwd()

		if _.switches.isActive('Folder'):
			folder = _.switches.values('Folder')[0]

		_.appData[__.appReg]['pipe'] = os.listdir(folder)


undo = {}
data = []
########################################################################################
if __name__ == '__main__':
	action()







