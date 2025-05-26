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
import platform
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
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-input','file.txt')
	# _.switches.register('Files', '-f,-file,-files','file.txt')
	

_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'folderEmailPrep.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Renames files that cannot be emailed',
	'categories': [
						'filename',
						'file',
						'rename',
						'email',
						'tool',
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
						'p folderEmailPrep',
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
#     if os.path.isdir(row):
#     if os.path.isfile(row):
########################################################################################
# START

def buildUndoFile():
	global data
	undo_file = []
	undo_file.append('@echo off')
	for record in data:
		undo_file.append('rename "' + record['id'] + '" "' + record['file'] + '"' )
	
	undo_file.append('echo.>'+'"' + __.postInstall['execute'] + '"')
	undo_file.append('if exist "' + __.postInstall['file'] + '" ( copy /Y "' + __.postInstall['file'] + '" "' + __.postInstall['execute'] + '" )')
	undo_file.append('CALL "' + __.postInstall['execute'] + '"')
	# undo_file.append('if exist "' + __.postInstall['execute'] + '" call "' + __.postInstall['execute'] + '"')
	undo_file.append('if exist "' + __.postInstall['execute'] + '" del "' + __.postInstall['execute'] + '"')
	undo_file.append('if exist %0 del %0')
	if platform.system() == 'Windows':
		undo_file.append('cls')
	else:
		undo_file.append('clear')
	undo_file.append('echo Done')
	_.saveText( undo_file, '_rebuild_files' )


def renameFiles():
	global data

	for record in data:
		os.rename( record['file'], record['id'] )

def isFlagged( test ):
	global flagged

	test = test.lower()

	for record in flagged:
		if test.endswith( record['ext'] ):
			return True

	return False


def undo():
	undoFile = _.getText( '_rebuild_files' )
	if not len( undoFile ):
		undoFile = _.getText( '_rebuild_files.bat' )
	for line in undoFile:
		if line.startswith( 'rename' ):
			info = line.split( '"' )
			if os.path.isfile( info[1] ):
				os.rename( info[1], info[3] )
	if os.path.isfile( '_rebuild_files' ):
		os.remove( '_rebuild_files' )
	if os.path.isfile( '_rebuild_files.bat' ):
		os.remove( '_rebuild_files.bat' )


def action():
	global data
	load()

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		# _.pipeCleaner()
		# _.printVar(_.appData)
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if '_rebuild_files' in row:
				undo()
				sys.exit()
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if os.path.isfile( row ) and isFlagged( row ):
				data.append({ 'file': row, 'id': _.genUUID() })
				
		buildUndoFile()
		renameFiles()



def load():
	global flagged
	flagged = _.getTable( 'bad_email_attachments.json' )
	_.setPipeData( os.listdir(os.getcwd()), focus() )

data = []
flagged = []
__.postInstall = { 'file': '2b_R2D2.txt', 'execute': 'postInstall.bat' }

########################################################################################
if __name__ == '__main__':
	action()






