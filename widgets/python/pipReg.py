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

def appSwitches():
	_.switches.register( 'Module', '-mod,-module', 'torrent_parser' )
	_.switches.register( 'Version', '-v,-version', ' Python version: 2, 3 (assumes 3 if blank) ' )
	_.switches.register( 'Path', '-path,-folder', 'D:\\techApps\\Python_Installers\\3\\PKG_Name'+_v.slash )
	_.switches.register( 'Command', '-cmd,-command', 'pip install PKG_Name --upgrade ,  pip install PKG_Name.whl' )
	_.switches.register( 'View', '-view', 'E' )


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'pipReg.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Python module Registration for USB install management (reduce folder sync)',
	'categories': [
						'log',
						'pip',
						'pip log',
						'registration',
						'python module',
						'module',
						'import',
						'python',
						'documentation',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						'p pipReg -view %theUSB%',
						'',
						'p pipReg -view %techDrive%',
						'p USB_python_modules_synchronized -drive %techDrive%',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p pipReg -pip torrent_parser',
						'',
						'p pipReg -mod PKG_Name -path %techDrive%:\\techApps\\Python_Installers\\3\\PKG_Name\\  -command %py% setup.py install ',
						'',
						'p pipReg -mod PKG_Name -path %techDrive%:\\techApps\\Python_Installers\\3\\  -command %pip% install PKG_Name.whl ',
						'',
						'',
						'p pipReg -view',
						'p pipReg -view %theUSB%',
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
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START

_USB_UPDATE_LOG = _.regImp( __.appReg, 'USB_python_modules_synchronized' )
_USB_UPDATE_LOG.switch( 'Clean' )

def action():
	global data
	load()
	if not _.switches.isActive('View'):
		if data is None:
			data = []
		record = {
					'epoch': time.time(),
					'module': '',
					'version': '3',
					'path': '',
					'command': '',
		}
		if _.switches.isActive('Module'):
			record['module'] = '_'.join( _.switches.values('Module') )

		if _.switches.isActive('Version'):
			record['version'] = '.'.join( _.switches.values('Version') )

		if _.switches.isActive('Path'):
			record['path'] = ' '.join( _.switches.values('Path') )

		if _.switches.isActive('Command'):
			record['command'] = ' '.join( _.switches.values('Command') )
		_.printVar( record )
		_.pr()
		keep = input( 'Keep? ' )
		_.pr()
		if not 'n' in keep.lower():
			data.append( record )
			_.saveTable2( data, _v.updates+_v.slash+'python_module_installation_log.json' )
			_.colorThis( [ 'Saved' ], 'green' )
		else:
			_.colorThis( [ 'Not Saved' ], 'red' )

	else:
		if not len( _.switches.value('View') ):
			_.pr()
			_.switches.fieldSet( 'Long', 'active', True )
			_.tables.register( 'log', data )
			_.tables.fieldProfileSet( 'log', 'epoch', 'trigger', _.resolveEpochTest )
			_.tables.print( 'log', 'epoch,module,version,command,path' )
		else:
			_USB_UPDATE_LOG.switch( 'Drive', _.switches.value('View') )
			log = _USB_UPDATE_LOG.do( 'action' )
			view = []
			try:
				for record in data:
					if record['epoch'] < log['last']:
						view.append( record )
						# _.printVar( record )
			except Exception as e:
				view = data
			_.pr()
			_.switches.fieldSet( 'Long', 'active', True )
			_.tables.register( 'log', view )
			_.tables.fieldProfileSet( 'log', 'epoch', 'trigger', _.resolveEpochTest )
			_.tables.print( 'log', 'epoch,module,version,command,path' )
			# _.printVar( log )
			



def load():
	global data
	data = _.getTable2( _v.updates+_v.slash+'python_module_installation_log.json' )


data = []
########################################################################################
if __name__ == '__main__':
	action()







