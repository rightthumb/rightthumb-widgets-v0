import os

# s.de = string_de
# s.en = string_en

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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

def appSwitches():
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'vault.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Vault',
	'categories': [
						'vault',
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
						'p thisApp -file file.txt',
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
					# {},
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
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

def cleanString(data):
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	return data

def cleanStringA(data):
	data = _str.cleanBE(data,_v.default_powershell)
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,'\r')
	data = _str.cleanEnd(data,' ')
	data = _str.cleanEnd(data,'\t')
	data = _str.cleanEnd(data,' ')
	data = _str.cleanEnd(data,'\t')

	# data = _str.cleanBE(data,'\t')
	# data = _str.cleanBE(data,' ')
	return data

def login( label, appReg=None ):
	auto = _v.vaultPath()
	if appReg is None:
		appReg = __.appReg
	location = appReg+'.'+label

	

	vaultPass = False
	if not os.path.isfile(auto):
		vaultPass = True
		_.pr()
		_.colorThis( 'Vault:', 'yellow' )
		password = getpass.getpass()
		_.pr()

		_.saveText( _blowfish.encrypt(password), auto )
	gateKey = _blowfish.decrypt( _.getText(auto,raw=True,clean=2) )
	vault = _.getTable( 'vault.index' )
	
	if location in vault:
		password = _blowfish.decrypt( vault[location], gateKey )
	else:
		if vaultPass:
			_.colorThis( label, 'yellow' )
		password = getpass.getpass()
		vault[location] = _blowfish.encrypt( password, gateKey )
		_.saveTable( vault, 'vault.index' )

	return password

def key(password=None):
	auto = _v.vaultPath()
	if os.path.isfile(auto):
		pass
	else:
		auto = _v.vaultPath(1)
		vaultPass = True
		if password is None:
			_.pr()
			_.colorThis( 'Vault:', 'yellow' )
			password = getpass.getpass()
			_.pr()

			_.saveText( _blowfish.encrypt(password,456), auto )
			_blowfish.myEn('1998',password)
	enPass = open(auto, 'r').read()
	gateKey = _blowfish.decrypt( enPass,456)
	# gateKey = _blowfish.decryptU( enPass,456)
	return gateKey

def string( data ):
	password = key()
	return _blowfish.decrypt( data, password )

def action():
	pass

s = _.dot()
f = _.dot()

def string_de( what ):
	return cleanString( _blowfish.decrypt( cleanString(what), key() ) )

def string_en( what ):
	return cleanString( _blowfish.encrypt( cleanString(what), key() ) )

s.de = string_de
s.en = string_en









_cryptFile = None
def secureFiles_Decrypt( path, pw='' ):
	global _dir
	global _cryptFile
	if _cryptFile is None:
		import _rightThumb._dir as _dir
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
		_cryptFile.switch( 'Password', pw )
	else:
		_cryptFile.switch( 'Password', key() )

	_cryptFile.switch( 'Decrypt' )
	_cryptFile.switch( 'Encrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.do( 'action' )
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)

def secureFiles_Encrypt( path, pw='' ):
	global _dir
	global _cryptFile
	if _cryptFile is None:
		import _rightThumb._dir as _dir
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
		_cryptFile.switch( 'Password', pw )
	else:
		_cryptFile.switch( 'Password', key() )
	_cryptFile.switch( 'Encrypt' )
	_cryptFile.switch( 'Decrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.do( 'action' )
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)

def secureFiles_crypt_toggle( path ):
	if _.isCrypt(path):
		secureFiles_Decrypt(path)
	else:
		secureFiles_Encrypt(path)

f.en = secureFiles_Encrypt
f.de = secureFiles_Decrypt
f.t = secureFiles_crypt_toggle






# auto = _v.vault_path

# _vault = _.regImp( __.appReg, '_rightThumb._vault' )
# _vault.imp.login(app)
# _vault.imp.key()
# _vault.imp.string('string')

# import _rightThumb._vault as _vault
# _vault.login(app)
# _vault.key()
# _vault.string('string')

import getpass
import _rightThumb._encryptString as _blowfish
# import _rightThumb._md5 as _md5
# import _rightThumb._dir as _dir


########################################################################################
if __name__ == '__main__':
	action()







