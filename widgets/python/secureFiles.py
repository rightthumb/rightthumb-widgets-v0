#!/usr/bin/python3
import os
import sys
import time
# import platform
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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Folders', '-fd,-folder,-folders','$HOME/secure' )
	_.switches.register( 'Encrypt', '-en,-encrypt' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'noBackup', '-nobk,-nobackup' )
	_.switches.register( 'Backup', '-bk,-backup' )
	_.switches.register( 'Resolve', '-res,-resolve' )
	_.switches.register( 'Delete', '-del,-delete', 'search' )
	_.switches.register( 'Extensions', '-ext', 'pem crt' )
	_.switches.register( 'Recursive', '-r' )

	_.switches.register( 'DoNotSync', '-nosync' )
	_.switches.register( 'Sync', '-sync' )
	_.switches.register( 'Size', '-size' )
	
	_.switches.register( 'Lock', '-lock' )
	_.switches.register( 'ScanFolders', '-scan' )

	_.switches.register( 'Compressed', '-zip' )



_.autoBackupData = False
__.releaseAcquiredData = False
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'secureFiles.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage secure files and their settings',
	'categories': [
						'files',
						'secure',
						'crypt',
						'encryption',
						'tool',
						'manage',
						'settings',
						'security',
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
						'p secureFiles -folder $HOME/secure',
						'p secureFiles -folder %userprofile%\\Documents\\secure',
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
	'notes': [
				       { 'test': 'one' },
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
	__.myFileLocations_SKIP_VALIDATION = False
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START












_cryptFile = None
def secureFiles_Decrypt( path, pw ):
	global _cryptFile
	if _cryptFile is None:
		try:
			_cryptFile = _.regImp( __.appReg, 'cryptFile' )
			_cryptFile.switch( 'NoExt' )
			# if _.switches.isActive('Clean'):
			_cryptFile.switch( 'Clean' )
			_cryptFile.imp.appDBA = _cryptFile.focus
		except Exception as e:
			_.colorThis( 'Error: missing pyAesCrypt', 'red' )


	_.cp( 'crypt.de', 'Background.light_blue' )
	_cryptFile.switch( 'Password', delete=True )
	if len(pw):
		# print(_blowfish.decrypt( pw, _vault.key() ))
		_cryptFile.switch( 'Password', _blowfish.decrypt( pw, _vault.key() ) )
	_cryptFile.switch( 'Decrypt' )
	_cryptFile.switch( 'Encrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.do( 'action' )
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)

def secureFiles_Encrypt( path, pw ):
	global _cryptFile
	if _cryptFile is None:
		try:
			_cryptFile = _.regImp( __.appReg, 'cryptFile' )
			_cryptFile.switch( 'NoExt' )
			# if _.switches.isActive('Clean'):
			_cryptFile.switch( 'Clean' )
			_cryptFile.imp.appDBA = _cryptFile.focus
		except Exception as e:
			_.colorThis( 'Error: missing pyAesCrypt', 'red' )


	if _.isCrypt(path):
		return None
	
	_.cp( 'crypt.en', 'Background.light_blue' )
	_cryptFile.switch( 'Password', delete=True )
	if len(pw):
		_cryptFile.switch( 'Password', _blowfish.decrypt( pw, _vault.key() ) )
	_cryptFile.switch( 'Encrypt' )
	_cryptFile.switch( 'Decrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.do( 'action' )
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)

def secureSubFolderTest( path ):
	global settings
	if _.isWin:
		path = path.lower()
	if not settings['folders']:
		return ''

	if _v.sanitizeFolder(_v.popFile(path)) in settings['folders']:
		f = _v.sanitizeFolder(_v.popFile(path))
		secure_record = settings['folders'][ f ]
		if secure_record['Extensions']:
			for xt in secure_record['Extensions']:
				if path.lower().endswith('.'+xt.lower()):
					return f
		else:
			return f
	for f in settings['folders']:
		if settings['folders'][f]['Recursive']:

			ff = _v.resolveFolderIDs(f)
			if _.isWin:
				ff = ff.lower()
			if not ff.endswith(_v.slash):
				ff += _v.slash
			if path.startswith( ff ):
				if secure_record['Extensions']:
					for xt in secure_record['Extensions']:
						if path.lower().endswith('.'+xt.lower()):
							return f
				else:
					return f
				
	return ''



def secureFiles( path, unlock=None, lock=None ):

	if unlock is None and lock is None:
		unlock = False
		lock = True
	elif not unlock is None:
		if unlock:
			lock = False
			unlock = True
		else:
			lock = True
			unlock = False
	elif not lock is None:
		if lock:
			lock = True
			unlock = False
		else:
			lock = False
			unlock = True

	global settings
	# _.printVarSimple(settings)
	# sys.exit()
	
	secure_folder = secureSubFolderTest( path )

	if secure_folder or _v.sanitizeFolder(path) in settings['files']:
		_.cp( [ 'SECURE FILE:', path ], 'Background.red' )
		
		if _v.sanitizeFolder(path) in settings['files']:
			secure_record = settings['files'][ _v.sanitizeFolder(path) ]
		elif secure_folder in settings['folders']:
			secure_record = settings['files'][ secure_folder ]
		

		if secure_record['noBackup'] and not secure_record['Encrypt']:
			return True

		elif secure_record['noBackup'] and secure_record['Encrypt']:
			if unlock and _.isCrypt(path):
				secureFiles_Decrypt( path, secure_record['Password'] )
			return True
		
		elif secure_record['noBackup']:
			return True

		elif secure_record['Backup'] and  secure_record['Encrypt']:
			if not _.isCrypt(path):
				pass
			else:
				secureFiles_Decrypt( path, secure_record['Password'] )

		elif secure_record['Encrypt'] and unlock:
			if _.isCrypt(path):
				secureFiles_Decrypt( path, secure_record['Password'] )

		


		
		if secure_record['Encrypt']:
			if not unlock and not _.isCrypt(path):
				secureFiles_Encrypt( path, secure_record['Password'] )

			elif unlock and _.isCrypt(path):
				secureFiles_Decrypt( path, secure_record['Password'] )









def getFolder( folder, ext=[], recursive=False, record={} ):
	__.v.secure.folders[folder] = record
	# print( 'getFolder:', folder )
	try:
		dirList = os.listdir( folder )
	except Exception as e:
		return None

	for file in dirList:
		path = __.path(folder +_v.slash+ file)
		# print(path)
		if os.path.isdir( path ):
			if recursive:
				getFolder( path, ext, recursive, record )
		if os.path.isfile( path ):
			if not ext:
				_.v.files.append(path)
			else:
				for xt in ext:
					if path.lower().endswith( '.'+xt ):
						_.v.files.append(path)


def scanFolders(sync=False, meta=False):
	global settings
	try:
		settings['folders']
	except Exception as e:
		load()

	__.v.secure.folders = {}
	__.v.secure.files = {}
	__.v.secure.nosync = {}
	__.v.secure.sync = {}
	__.v.secure.crypt = {}

	__.v.secure.hash = {}

	loco = {}
	for f in settings['folders']:
		record = settings['folders'][f]
		_.v.files = []
		if record['Recursive']:
			# print('................................................')
			record['priority'] = 0
			recursive = True
		else:
			record['priority'] = 1
			recursive = False
		getFolder( _v.resolveFolderIDs(f), record['Extensions'], recursive=recursive, record=record )
		for path in _.v.files:
			if os.path.isfile(path):
				# print(path)
				processFiles( path, record, sync )
				# __.v.secure.files[ p ] = record




	for f in settings['files']:
		record = settings['files'][f]
		record['priority'] = 2
		p = __.path( _v.resolveFolderIDs(f) )
		if os.path.isfile(p):
			processFiles( p, record, sync )
			# __.v.secure.files[ p ] = record
		

	# local = {}
	# for f in loco:
	# 	if os.path.isfile( _v.resolveFolderIDs(f) ):
	# 		p = __.path(os.path.abspath( _v.resolveFolderIDs(f) ))
	# 		local[p] = loco[f]
		
	_.saveTable( __.v.secure.crypt, 'secure-crypt-local.settings', p=0 )
	_.saveTable( __.v.secure.files, 'secure-files-local.settings', p=0 )
	if sync:
		_.saveTable( __.v.secure.sync, 'secure-sync-local.settings', p=0 )
		_.saveTable( __.v.secure.nosync, 'secure-nosync-local.settings', p=0 )



	if meta:
		genMeta()
		_.saveTable( __.v.secure.files, 'secure-crypt-local.meta', p=0 )
	return __.v.secure.files

def processFiles( path, record, sync ):
	# print( 'processFiles:', path )
	if record['Encrypt']:
		__.v.secure.crypt[ path ] = record
	if record['noBackup'] or record['Backup']:
		__.v.secure.backup[ path ] = record

	if record['Encrypt'] or record['noBackup'] or record['Backup']:
		__.v.secure.files[ path ] = record
		


	if sync:
		item = False
		if record['NoSync']:
			if record['Size']:
				if record['Size'][0] == 'l' and _dir.info(path)['bytes'] <= record['Size'][1]:
					item = True
				elif record['Size'][0] == 'g' and _dir.info(path)['bytes'] >= record['Size'][1]:
					item = True
			elif not record['Size']:
				item = True
		elif record['Sync']:
			if record['Size']:
				if record['Size'][0] == 'l' and _dir.info(path)['bytes'] <= record['Size'][1]:
					item = True
				elif record['Size'][0] == 'g' and _dir.info(path)['bytes'] >= record['Size'][1]:
					item = True
			elif not record['Size']:
				item = True

		if item:
			if record['NoSync']:
				shouldAdd = True

				if path in __.v.secure.sync:
					if __.v.secure.sync[path]['priority'] > record['priority']:
						shouldAdd = False
					else:
						del __.v.secure.sync[path]


				if shouldAdd:
					__.v.secure.nosync[path] = record
			elif record['Sync']:
				shouldAdd = True

				if path in __.v.secure.nosync:
					if __.v.secure.nosync[path]['priority'] >= record['priority']:
						shouldAdd = False
					else:
						del __.v.secure.nosync[path]



				if shouldAdd:
					__.v.secure.sync[path] = record




def genMeta():
	__.v.secure.meta = {}

	




























def process( subject ):
	global settings

	# Encrypt Password noBackup Backup
	pw = _.switches.value('Password')
	if len(pw):
		pw = _blowfish.encrypt( pw, _vault.key() )
	config = {
					'Encrypt': _.switches.isActive('Encrypt'),
					'Password': pw,
					'noBackup': _.switches.isActive('noBackup'),
					'Backup': _.switches.isActive('Backup'),
					'NoSync': _.switches.isActive('DoNotSync'),
					'Sync': _.switches.isActive('Sync'),
					'Size': [],
	}

	if _.switches.isActive('Size'):
		config['Size'] = [ _.switches.values('Size')[0].lower(), _.unFormatSize( _.switches.values('Size')[1] ) ]
		if 'l' in config['Size'][0]:
			config['Size'][0] = 'l'
		elif 'g' in config['Size'][0]:
			config['Size'][0] = 'g'
	if _.switches.isActive('Folders'):
		config['Recursive'] = _.switches.isActive('Recursive')
		config['Extensions'] = _.switches.values('Extensions')
		for i,xt in enumerate(config['Extensions']):
			
			# config['Extensions'][i] = _str.cleanFirst(  xt.lower()  , '.' ).replace(' ','')
			if xt.startswith('.'):
				config['Extensions'][i] = xt[1:].lower()
			else:
				config['Extensions'][i] = xt.lower()
 
	# if not _.switches.isActive('Encrypt') and not _.switches.isActive('Password') and not _.switches.isActive('noBackup') and not _.switches.isActive('Backup'):
	if len( _.switches.active() ) < 2:
		_.colorThis( [ 'Error: expected additional settings' ], 'red' )
		sys.exit()



	san = None

	if os.path.isfile(subject):
		subject = os.path.abspath(subject)
		ff = _.fileFolder(subject)
		# san = _v.sanitizeFolder( ff['folder'] )
		san = _v.sanitizeFolder( subject )
		if not type(san) == str:
			san = None
		elif type(san) == str:
			settings['files'][ san ] = config

		# print( 'file   subject:', subject, ff, '\n', san )

	elif os.path.isdir(subject):
		subject = os.path.abspath(subject)
		san = _v.sanitizeFolder( subject )

		if san.endswith(_v.slash):
			san = san[:len(san) - 1]


		if not type(san) == str:
			san = None
		elif type(san) == str:
			settings['folders'][ san ] = config


		# print( 'folder subject:', subject, '\n', san )
	elif _.switches.isActive('Resolve'):
			print()
			print( subject )
			print( _v.resolveFolderIDs(subject) )
			print()
	else:
		_.colorThis( [ 'Error:', subject ], 'red' )
		sys.exit()

	if not _.switches.isActive('Resolve')                and                not san is None:
		_.saveTableDB(   settings,   'secure-files.settings'   )

# def remove():

def scanLock( lock=False ):
	scanFolders(sync=True, meta=True)
	if lock:
		for f in __.v.secure.files:
			print()
			# _.cp( f, 'cyan' )
			secureFiles( f, lock=True )
def action():
	load()

	# _.printVarSimple( _.switches.active() )
	# sys.exit()

	# s = "123456"
	# print(s[2:])
	# sys.exit()
	global appDBA
	global settings


	if _.switches.isActive('Delete'):

		if _.switches.isActive('Folders'):
			if not len(_.switches.value('Folders')):
				_.switches.fieldSet( 'Folders', 'value', os.getcwd() )
				_.switches.fieldSet( 'Folders', 'values', [os.getcwd()] )

			for i,row in enumerate(_.switches.values('Folders')):
				f = _v.sanitizeFolder(  row )
				if f in settings['folders']:
					del settings['folders'][f]
		if _.switches.isActive('Files'):
			for i,row in enumerate(_.switches.values('Files')):
				f = _v.sanitizeFolder(  row )
				if f in settings['files']:
					del settings['files'][f]

		if type(_.appData[appDBA]['pipe']) == list:
			for i,row in enumerate( _.appData[appDBA]['pipe'] ):
				row = __.path(row)
				if os.path.isfile(row):
					f = _v.sanitizeFolder(  row )
					if f in settings['files']:
						del settings['files'][f]
				elif os.path.isdir(row):
					f = _v.sanitizeFolder(  row )
					if f in settings['folders']:
						del settings['folders'][f]

		_.saveTableDB(   settings,   'secure-files.settings'   )
		scanLock( lock=_.switches.isActive('Lock') )
		return None

	if _.switches.isActive('ScanFolders') or _.switches.isActive('Lock'):
		scanLock( lock=_.switches.isActive('Lock') )
		return None


	if _.switches.isActive('Folders'):
		if not len(_.switches.value('Folders')):
			_.switches.fieldSet( 'Folders', 'value', os.getcwd() )
			_.switches.fieldSet( 'Folders', 'values', [os.getcwd()] )

		for i,row in enumerate(_.switches.values('Folders')):
			process(row)
	if _.switches.isActive('Files'):
		for i,row in enumerate(_.switches.values('Files')):
			process(row)

	if type(_.appData[appDBA]['pipe']) == list:
		for i,row in enumerate( _.appData[appDBA]['pipe'] ):
			process(row)


	scanLock()
	return None

	# for i,row in enumerate(_.isData(r=1)):
	# 	print(row)

__.v.secure = _.dot()

def load():
	global settings
	settings   = _.getTableDB( 'secure-files.settings' )
	if settings == {}:
		settings = {
						'folders': {},
						'files': {},
		}

	# print(settings)
	# sys.exit()
settings = {}

import _rightThumb._vault as _vault
import _rightThumb._encryptString as _blowfish
import _rightThumb._dir as _dir
focus()


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()



