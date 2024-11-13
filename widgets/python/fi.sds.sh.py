import os
import requests
import getpass
import hashlib
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import _rightThumb._construct as __; appDBA = __.clearFocus(__name__, __file__); __.appReg = appDBA; import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet = _.l.vars(focus(), __name__, __file__, appDBA); _.load(); _v = __.imp('_rightThumb._vars');

def sw():
	_.switches.register('API-Ask', '-ask')
	_.switches.register('API', '-api')
	_.switches.register('Encrypt', '-en')
	_.switches.register('Decrypt', '-de')
	_.switches.register('Upload', '-u,-up')
	_.switches.register('Download', '-d,-dl')
	_.switches.register('Password', '-password')
	_.switches.register('File', '-f,-fi,-file')
	_.switches.register('isCrypt', '-isCrypt')
	_.switches.register('Log', '-log')
	_.switches.register('Do-Not-Log', '-nolog')
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'fi.sds.sh.py',
	'description': 'Upload Download Encrypt Decrypt Files',
	'categories': [
		'Files',
		'Upload',
		'Download',
		'Encrypt',
		'Decrypt',
		'fi.sds.sh',
	],
	'examples': [
		_.hp('p fi.sds.sh -f fi.txt -en -u test_folder'),
		_.hp('p fi.sds.sh -f fi.txt -d -de test_folder'),
		_.hp('p fi.sds.sh -f fi.txt -en -u test_folder -ask'),
		_.linePrint(label='simple', p=0),
		'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp(__file__), _.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return {'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()]}

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe', True); _.l.sw.register(triggers, sw);

########################################################################################
#n)--> start

HEADER_IDENTIFIER = b"SDS"

def derive_key(password):
	return hashlib.md5(password.encode('utf-8')).digest()

def encrypt_file(file_path, password):
	if isCrypt(file_path):
		_.pr('File is already encrypted.', c='red')
		return False
	key = derive_key(password)
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)
	with open(file_path, 'rb') as file:
		file_data = file.read()
	iv = cipher.iv
	encrypted_data = cipher.encrypt(pad(file_data, Blowfish.block_size))
	with open(file_path, 'wb') as file:
		file.write(HEADER_IDENTIFIER + iv + encrypted_data)
	return True
def decrypt_file(file_path, password):
	key = derive_key(password)
	with open(file_path, 'rb') as file:
		header = file.read(len(HEADER_IDENTIFIER))
		if header != HEADER_IDENTIFIER:
			_.pr('File is already decrypted.', c='red')
			return False
		iv = file.read(Blowfish.block_size)
		encrypted_data = file.read()
	cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
	decrypted_data = unpad(cipher.decrypt(encrypted_data), Blowfish.block_size)
	with open(file_path, 'wb') as file:
		file.write(decrypted_data)
	return True

def upload_file(file_path, api_key, folder=None):
	if not _.switches.isActive('Do-Not-Log'):
		_vault = _.regImp( __.appReg, '_rightThumb._vault' )
		en = isCrypt(file_path)
		global the_password
		rec = { 'file': file_path, 'api': _vault.imp.s.en(api_key), 'folder': folder, 'en': en, 'password': _vault.imp.s.en(the_password) }
		_.pr('\tLog:',rec,c='cyan')
		log = _.getTable('fi.sds.sh.json')
		log.append(rec)
		_.saveTable(log, 'fi.sds.sh.json',p=0)
	url = 'https://fi.sds.sh/upload.php'
	data = {'api_key': api_key}
	if folder:
		data['folder'] = folder
	with open(file_path, 'rb') as file:
		files = {'file': file}
		response = requests.post(url, files=files, data=data)
	return response

def download_file(file_name, api_key, folder=None):
	url = 'https://fi.sds.sh/download.php'
	params = {'file_name': file_name, 'api_key': api_key}
	if folder:
		params['folder'] = folder
	response = requests.get(url, params=params)
	if response.status_code == 200:
		with open(file_name, 'wb') as file:
			file.write(response.content)
	return response

the_password = None

def fig(key):
	if key in _v.fig:
		return _v.fig[key]
	else:
		dic = {
			'fi.sds.sh': 'no_api_key',
			'fi.sds.sh-pw': 'ba7cfca5',
		}
		return dic[key]

def secret(isActive=True, value=None):
	password = None
	if isActive and value is None:
		password = getpass.getpass(_.pr('Password: ',c='cyan',p=0)+' ')
	if isActive:
		if password is None:
			password = value
		if password.lower() == 'f':
			password = fig('fi.sds.sh-pw')
		elif password.lower().startswith('fi') and password.lower().endswith('pw') and len(password) <= 6:
			password = fig('fi.sds.sh-pw')
		elif password.lower() == 'fig':
			password = fig('fi.sds.sh-pw')
		elif password.lower() == 'api':
			password = fig('fi.sds.sh')
		elif password.lower() == 'v':
			_vault = _.regImp(__.appReg, '_rightThumb._vault')
			password = _vault.imp.key()
		elif password.lower() == 'vault':
			_vault = _.regImp(__.appReg, '_rightThumb._vault')
			password = _vault.imp.key()
		elif not password.strip():
			_vault = _.regImp(__.appReg, '_rightThumb._vault')
			password = _vault.imp.key()
	else:
		_vault = _.regImp(__.appReg, '_rightThumb._vault')
		password = _vault.imp.key()
	global the_password
	the_password = password
	return password

def IS(path, check=1):
	header = open(path, 'rb').read(len(HEADER_IDENTIFIER))
	if isinstance(check, str):
		return header.startswith(check.encode())
	elif isinstance(check, list):
		return any(header.startswith(c.encode()) for c in check)
	return False

def isCrypt(path):
	return IS(path, HEADER_IDENTIFIER.decode())

def action():

	if _.switches.isActive('Upload') and not _.switches.isActive('File'):
		_.pr('  Please specify a file with -f or -f.',c='red')
		return False
	if _.switches.isActive('Upload') and _.switches.isActive('File') and not os.path.isfile(_.switches.value('File')):
		_.pr('  File does not exist',c='red')
		return False
	
	if _.switches.isActive('Log'):
		log = _.getTable('fi.sds.sh.json')
		_vault = _.regImp( __.appReg, '_rightThumb._vault' )
		for rec in log:
			path = 'uploads/'+_vault.imp.s.de( rec['api'] ) + '/' + rec['folder'] + '/' + rec['file']
			path = path.replace( '\\', '/' )
			while '//' in path:
				path = path.replace('//', '/')
			print()
			_.pr( '  '+path,c='cyan' )

			if not 'password' in rec:
				pw = ''
			elif 'password' in rec:
				recPW = _vault.imp.s.de( rec['password'] )
				if recPW == fig('fi.sds.sh-pw'): pw = 'f'
				elif recPW == fig('fi.sds.sh'): pw = 'api'
				elif recPW == _vault.imp.key(): pw = ''
				else: pw = recPW
			if not pw:
				cmdPW = ' '
			else:
				cmdPW = ' -password '+ pw+ ' '

			if _vault.imp.s.de( rec['api'] ) == fig('fi.sds.sh'):
				api = ' '
			else:
				api = ' -api '+ _vault.imp.s.de( rec['api'] )+ ' '

			if rec['en']:
				en = ' -de '
			else:
				en = ' '
			if rec['folder'] == 'default':
				fo = ' '
			else:
				fo = rec['folder']+' '
			cmd = 'p fi.sds.sh -f '+ rec['file']+en+ ' -dl ' + fo+api+cmdPW
			while '  ' in cmd:
				cmd = cmd.replace('  ', ' ')
			_.pr( '    '+cmd.strip(), c='green' )

	if _.switches.isActive('isCrypt') and _.switches.isActive('File'):
		for file in _.switches.values('File'):
			if isCrypt(file):
				_.pr(f"{file} is encrypted.",c='Background.red')
			else:
				_.pr(f"{file} is not encrypted.",c='Background.green')
	folder = 'default'
	if _.switches.values('Upload'):
		folder = _.switches.value('Upload')
	if _.switches.values('Download'):
		folder = _.switches.value('Download')

	
	if _.switches.isActive('API'):
		api_key = _.switches.value('API')
	elif _.switches.isActive('API-Ask'):
		api_key = getpass.getpass('Enter your API key: ')
	else:
		api_key = fig('fi.sds.sh')

	password = secret(_.switches.isActive('Password'), _.switches.value('Password'))

	if _.switches.isActive('Password') and not len(_.switches.value('Password')):
		password = getpass.getpass('Enter your password: ')
	elif _.switches.isActive('Password'):
		password = _.switches.value('Password')[0]
	else:
		_vault = _.regImp(__.appReg, '_rightThumb._vault')
		password = _vault.imp.key()

	if _.switches.isActive('Encrypt'):
		file_path = _.switches.values('File')[0]
		en = encrypt_file(file_path, password)
		if en:
			_.pr(f"File encrypted and saved as {file_path}.",c='green')
	if _.switches.isActive('Upload'):
		file_path = _.switches.values('File')[0]
		response = upload_file(file_path, api_key, folder)
		_.pr(f"Upload response: {response.text}",c='green')

	decrypt_file_flag = _.switches.isActive('Decrypt')
	if _.switches.isActive('Download'):
		file_name = _.switches.values('File')[0]
		response = download_file(file_name, api_key, folder)
		if response.status_code == 200:
			_.pr(f"File downloaded and saved as {file_name}.",c='green')
			if not decrypt_file_flag and isCrypt(file_name):
				ask = input(_.pr('Decrypt? (y/n) ',c='yellow',p=0)+' ')
				if ask.lower() == 'y':
					decrypt_file_flag = True
					if not _.switches.isActive('Password'):
						password = secret()
		else:
			_.pr(f"Download failed with status code {response.status_code}.",c='red')
	if decrypt_file_flag:
		file_path = _.switches.values('File')[0]
		de = decrypt_file(file_path, password)
		if de:
			_.pr(f"File decrypted and saved as {file_path}.",c='Background.yellow')

########################################################################################
if __name__ == '__main__':
	try:
		action()
	except Exception as e:
		_.pr(e, c='red')
	_.isExit(__file__)
