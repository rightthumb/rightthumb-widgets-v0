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
		# _.pr(_blowfish.decrypt( pw, _vault.key() ))
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
	# _.pr( 'getFolder:', folder )
	try:
		dirList = os.listdir( folder )
	except Exception as e:
		return None

	for file in dirList:
		path = __.path(folder +_v.slash+ file)
		# _.pr(path)
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
	__.v.secure.nosync = {}
	__.v.secure.sync = {}
	if meta:
		__.v.secure.files = _.getTable('secure-crypt-local.meta')
	else:
		__.v.secure.files = _.getTable('secure-files-local.settings')
	__.v.secure.crypt = _.getTable('secure-crypt-local.settings')

	__.v.secure.hash = {}

	loco = {}
	for f in settings['folders']:
		record = settings['folders'][f]
		_.v.files = []
		if record['Recursive']:
			# _.pr('................................................')
			record['priority'] = 0
			recursive = True
		else:
			record['priority'] = 1
			recursive = False
		getFolder( _v.resolveFolderIDs(f), record['Extensions'], recursive=recursive, record=record )
		for path in _.v.files:
			if os.path.isfile(path):
				# _.pr(path)
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
	#     if os.path.isfile( _v.resolveFolderIDs(f) ):
	#         p = __.path(os.path.abspath( _v.resolveFolderIDs(f) ))
	#         local[p] = loco[f]
		
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
	# _.pr( 'processFiles:', path )
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

	

























# _docs_list = _.getTable('crypt-docs.list')
def process( subject ):
	global settings
	global _docs_list
	_path=__.path(subject)
	check_decrypt_docs_database(_path)
	# if _path in _docs_list:
	#     _decrypt_docs = _.regImp( __.appReg, 'decrypt-docs' )
	#     _decrypt_docs.imp.run( _path )
	#     _docs_list.pop(  _docs_list.index(_path)  )
	#     _.saveTable( _docs_list, 'crypt-docs.list' )


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

		# _.pr( 'file   subject:', subject, ff, '\n', san )

	elif os.path.isdir(subject):
		subject = os.path.abspath(subject)
		san = _v.sanitizeFolder( subject )

		if san.endswith(_v.slash):
			san = san[:len(san) - 1]


		if not type(san) == str:
			san = None
		elif type(san) == str:
			settings['folders'][ san ] = config


		# _.pr( 'folder subject:', subject, '\n', san )
	elif _.switches.isActive('Resolve'):
			_.pr()
			_.pr( subject )
			_.pr( _v.resolveFolderIDs(subject) )
			_.pr()
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
			_.pr()
			# _.cp( f, 'cyan' )
			secureFiles( f, lock=True )

def check_decrypt_docs_database(path):
	table = _.getTable('crypt-docs.list')
	new = []
	found=False
	for fi in table:
		if not fi == path: new.append(fi)
		else: found=True

	if found:
		_.cp('in decrypt-docs database','yellow')
		appReg=__.appReg
		_bk=_.regImp( __.appReg, 'fileBackup' ); __.appReg=appReg; _bk.switch( 'isPreOpen' ); _bk.switch( 'Silent' );
		_bk.switch( 'Input', path ); bkfi = _bk.action();
		__.appReg=appReg
		_.saveTable(new,'crypt-docs.list',p=0)

def action():
	load()

	# _.printVarSimple( _.switches.active() )
	# sys.exit()

	# s = "123456"
	# _.pr(s[2:])
	# sys.exit()
	global appDBA
	global settings
	global spent
	global removed
	spent={}
	removed={}
	# secure-crypt-local.meta
	# secure-files-local.settings
	# secure-crypt-local.settings

	settings2   = _.getTable('secure-crypt-local.meta')
	settings3   = _.getTable('secure-files-local.settings')
	settings4   = _.getTable('secure-crypt-local.settings')


	if _.switches.isActive('Delete'):
		appReg=__.appReg
		_bk=_.regImp( __.appReg, 'fileBackup' ); __.appReg=appReg; _bk.switch( 'isPreOpen' );
		__.appReg=appReg
		def pre_delete_decryption(_path_):
			global spent
			global removed
			removed[_path_]=1
			if os.path.isdir(_path_):
				_.fo(folder=_path_,r=True,script=pre_delete_decryption)
			else:
				if not _path_ in spent:
					spent[_path_] = 1
					__.appReg=appReg
					_bk.switch( 'Input', _path_ ); bkfi = _bk.action();
					__.appReg=appReg
					_.cp( ['decrypted and removed from secureFiles database',_path_] ,'red');

			# _.cp('in secureFiles database','yellow'); pre_delete_decryption(_path_);
		if _.switches.isActive('Folders'):
			if not len(_.switches.value('Folders')):
				_.switches.fieldSet( 'Folders', 'value', os.getcwd() )
				_.switches.fieldSet( 'Folders', 'values', [os.getcwd()] )

			for i,row in enumerate(_.switches.values('Folders')):
				row=__.path(row)
				f = _v.sanitizeFolder(  row )
				if f in settings['folders']:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings['folders'][f]
				if row in settings2:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings2[row]

				if row in settings3:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings3[row]

				if row in settings4:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings4[row]


		if _.switches.isActive('Files'):
			for i,row in enumerate(_.switches.values('Files')):
				row=__.path(row)
				f = _v.sanitizeFolder(  row )
				if row in settings['files']:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings['files'][row]
				if f in settings['files']:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings['files'][f]
				if row in settings2:
					_.pr(line=True,c='red')
					del settings2[row]
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);


				if row in settings3:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings3[row]



				if row in settings4:
					_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
					del settings4[row]



		if type(_.appData[appDBA]['pipe']) == list:
			for i,row in enumerate( _.appData[appDBA]['pipe'] ):
				row = __.path(row)
				f = _v.sanitizeFolder(  row )
				if os.path.isfile(row):
					if row in settings['files']:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings['files'][row]
					if f in settings['files']:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings['files'][f]
				elif os.path.isdir(row):
					if row in settings['folders']:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings['folders'][row]
					if f in settings['folders']:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings['folders'][f]
				if os.path.isfile(row):
					if row in settings2:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings2[row]
				elif os.path.isdir(row):
					if row in settings2:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings2[row]



				if os.path.isfile(row):
					if row in settings3:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings3[row]
				elif os.path.isdir(row):
					if row in settings3:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings3[row]



				if os.path.isfile(row):
					if row in settings4:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings4[row]
				elif os.path.isdir(row):
					if row in settings4:
						_.cp('in secureFiles database','yellow'); pre_delete_decryption(row);
						del settings4[row]




		if removed:
			print('removed')
			_.saveTableDB(   settings,   'secure-files.settings'  ,p=1 )
			_.saveTable(   settings2,   'secure-crypt-local.meta'   )
			_.saveTable(   settings3,   'secure-files-local.settings'   )
			_.saveTable(   settings4,   'secure-crypt-local.settings'   )
			__.isExit()

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
	#     _.pr(row)

__.v.secure = _.dot()

def load():
	global settings
	settings   = _.getTableDB( 'secure-files.settings' )



	if settings == {}:
		settings = {
						'folders': {},
						'files': {},
		}

	# _.pr(settings)
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


# wsl hang here processFiles( path, record, sync )
#     due to very old ttt secure-files.settings 
#       stuck scanning large root folders




