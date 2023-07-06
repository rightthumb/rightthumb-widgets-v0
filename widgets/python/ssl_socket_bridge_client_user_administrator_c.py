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
#     index = _textIndex.do( 'action' )

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

def appSwitches():
	pass


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ssl_socket_bridge_client_user_administrator_c.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'ssl bridge client admin',
	'categories': [
						'ssl',
						'bridge',
						'client',
						'admin',
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



######################################################################################## ########################################################################################
########################################################################################################################
from cryptography.fernet import Fernet

def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)


def load_key():
	return open("key.key", "rb").read()


def encrypt(fin, fout, key):
	f = Fernet(key)
	with open(fin, "rb") as file:
		# read all file data
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)

	# write the encrypted file
	with open(fout, "wb") as file:
		file.write(encrypted_data)

def decrypt(fin, fout, key):
	f = Fernet(key)
	with open(fin, "rb") as file:
		# read the encrypted data
		encrypted_data = file.read()
	# decrypt data
	decrypted_data = f.decrypt(encrypted_data)
	# write the original file
	with open(fout, "wb") as file:
		file.write(decrypted_data)

def decrypt2(fin, fout, key):
	f = Fernet(key)
	# with open(fin, "rb") as file:
	#     # read the encrypted data
	#     encrypted_data = file.read()
	# # decrypt data
	decrypted_data = f.decrypt(fin)
	# write the original file
	with open(fout, "wb") as file:
		file.write(decrypted_data)

########################################################################################################################
import base64
from Crypto.Cipher import Blowfish


import hashlib
def md5(chunk):
	hash_md5 = hashlib.md5()
	hash_md5.update(bytes(chunk, 'utf-8'))
	return hash_md5.hexdigest()


def pad_string( string ):
	INPUT_SIZE = 8
	new_str = string
	pad_chars = INPUT_SIZE - (len(string) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
	return new_str

def decryptB( data, password=False ):
	crypt_obj = Blowfish.new(md5(password), Blowfish.MODE_ECB)
	decoded = base64.b64decode(data)
	decrypt = crypt_obj.decrypt(decoded)
	result = str(decrypt,'iso-8859-1')
	return result


def encryptB( data, password=False ):
	crypt_obj = Blowfish.new(md5(password), Blowfish.MODE_ECB)
	try:
		ciphertext = crypt_obj.encrypt(pad_string(str(data)))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(pad_string(str(data)) + space)
				works = True
			except Exception as e:
				pass
			space += ' '
			if i == 10:
				works = True
			i += 1

	result = base64.b64encode(ciphertext)
	thePayload = str(result,'iso-8859-1')

	return thePayload



def formatData( result ):
	result = str(result)
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result

import getpass

# password = getpass.getpass()
# _.pr(password)
######################################################################################## ########################################################################################
import socket
import ssl
import sys

import _rightThumb._md5 as _md5
import _rightThumb._vars as _v



def recvall(sock):
	BUFF_SIZE = 4096 # 4 KiB
	data = b''
	while True:
		part = sock.recv(BUFF_SIZE)
		data += part
		if len(part) < BUFF_SIZE:
			# either 0 or end of data
			break
	return data



class Socket_Manager:

	def __init__( self ):
		self.run_establish_connection = False

	def establish( self ):
		if not self.run_establish_connection:
			self.run_establish_connection = True
			hostname = 'ncc-1701-d.rightthumb.com'
			port = 80
			# port = 8443
			global encryptedData
			context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
			# context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )
			context.load_verify_locations( encryptedData['path'] )
			ssock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
			ssock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
			_.saveText( encryptedData['file'], encryptedData['path'] )
			if os.path.isfile( encryptedData['path'] ):
				os.remove( encryptedData['path'] )
			self.socket = context.wrap_socket( ssock, server_hostname=hostname )
			self.socket.connect((hostname, port))



			self.loggedIn = False
			self.active = True
			self.credentials = {
					'user': 'administrator',
					'groups': ['administrators'],
					'password': '3mDOhQLMMRA-QTZhlN1hJpHOq2aZbAEvOClnpJwxDEA=',
					'machine': _v.getMachineID(),
					'flag': '2BR2D2C3P04LIFE_LOGIN'
		}
"""
		{
										'user': 'logs',
										'groups': ['system'],
										'flag': '2BR2D2C3P04LIFE_LOGIN'
		}
"""

			self.expecting = None
			self.waitingMsg = '\twaiting for a connection'


	def formatData( self, result ):
		result = str(result)
		try:
			result = str(result,'utf-8')
		except Exception as e:
			try:
				result = str(result,'iso-8859-1')
			except Exception as e:
				result = result.encode('utf-8')
		return result


	def waitingNotice( self ):
		_.pr( self.waitingMsg )


	def recvall( self ):
		BUFF_SIZE = 4096 # 4 KiB
		data = b''
		while True:
			part = self.socket.recv(BUFF_SIZE)
			data += part
			if len(part) < BUFF_SIZE:
				# either 0 or end of data
				break
		return str(data,'iso-8859-1')

	def send( self, data, expecting=False ):
		self.expecting = expecting
		data = self.formatData( data )
		self.socket.send( data )


	def receive( self ):

		data = self.recvall()



		if data == 'hello':
			self.send( dataIn )
		elif data == 'exit':

			self.active = False
			self.socket.close()

			# raise
			sys.exit()


		elif '2BR2D2C3P04LIFE' in data:
			records = eval(data)

			_.printVar( records )



	def manage( self ):
		self.establish()
		while self.active:
			self.waitingNotice()
			
			try:
				i = 0
				while self.active:

					
					if not self.loggedIn:
						self.loggedIn = True

						self.send( self.credentials, expecting={'type':'listen'} )
						

					pass
					self.receive()



			finally:
				
				pass



def action():
	global thisSocket
	load()

	thisSocket.manage()



def load():
	global thisSocket
	global encryptedData
	thisSocket = Socket_Manager()
	encryptedFile = 'gAAAAABeQaWH4QKoXmOVovz9svaeL8xxF_fNxhk7ycfgXio1IPO3WSOrLb7aCyicE5v89YsMwy5yCql6_B5BTbQQ4nYMX3UbB4BDe4mQe9Q07Jt21OhlJUky_fO6S4AXWV4HBvtn7QpYkJpKV4hrA-Mz-rVap34KTgwVxPlJk3ZRP6xN85Nm5aG8HsJ8PZjXDPjKcDmEkVA7v7YOos6tGZpytXAyrj6B0ACAe5U3yJpmSNYV99D_m6yd5Fpg-xnkC5Ku4lSTYV6CjlaWlx0cwFQqEhvCfdeMuCi4qXePtFFR1I-_mh0deCTDK431FJmKHyT5pigjjBFn2zImoWvyNeFEA1HpV0Yr8CpeHLnfVE5KpEyoa43RD3QsWwj9r2Qho0g3v_kk4NtVI0-BEjfpbkxtb2I6i0osxA78Rjp91AU-dDcx2VCqcwyaRDPkeHjJUoljd9dwkKBsdzeC7ohTe0YMzvVgaXERltUwBUJUE9S4ORKtegTmOOSCQjCjUDRBP-iQUJo8gp_7yzf1p0ewhuIfd_BHHzM8O9q8_LU2ix14EoSSYfxhP-4JxXeG2cx4oAxvXkGBheo_j_u82vBqC0MPtrFuY-yDOvDggIo4Vr_fRQ4V8xbo714fnnkj7dmbngAF_BiOjNxH5S-TQu20RwsmIeHNYP7HGqL2tkjiYv0bXs72L6L2bAqeGUIHhiDvXxiN33rVwycBm0Jl55L8Uj0EZHWSw9XjYLqR4E38Kzfwpjm6dc_3m78yHSAW-wizww2Pb3LHjZXInMh6XF5wY1qkhM1xQVtiLKQyPKPvke4xoIdHnXGFnr-rVQnGoqR668HHzd6zgtlrAuuSLMBZfZHeobqL-Zo_blT3j2iTDaGnMyJjgJl_blG0q0hauIyRIMBLkMnT46-PM_isKfPPCdytZ9mBJRrmBbSjM4ZGAgBuosabjuUKPJUfPV56KbMBU-fGUQGMBiFinWCEgVCXu71fah2zxg9berw194mUxdSlnPfTxa0axdy7SIIIaaOZ23OGNwcRrOhlE2dPd1R0o8suEGLLbhkGehHBjTWUidVj7VoZOrOzmV0NVYR1U0rEbtLeNQtpVjzND-cJaOTl8jfbQi8EFZ7uAtufZY-CkFcSpFzoYF_jwc5pnlSqhOW3G0qQSapmlhnHZuaZlSI1mxA5XYxoDXRmwFqGA5Yx1DnAb4VIJh6imCg6slfbvPHDZSaBmwq0SeIz_b_ld0bkZNJb9U5RnuYGMAM-1Hall0bF4byTpmENHaBS7x_iH0XJLGcf6V0d7PwbwqdA5ntYlpVoVua3DEWbXevrWac2VmpHPIq3KP8zvZXFg-AxY5tMoIdBen8AFuWCwnoUIs2pX3giWzOyJW9XSlS0adMyH68a0Olugn3zAmpVji0UlnIgpqOFBoTcV9j37reHd09yIgoNKeYBYq7T4m3RaxjhYFrveQo3OqnlGuoTNNoxb5BBnfIdjRCmafJs6SBHJlkyGCSJBafGMUrxaPEGaWl9ifdjQ-lyG6OcarkEmSL2QFTr5UrLPQ3n9j1rWr_PWo_n3H0xp2W_QzjAdmN1aXYrGmmG0V9W8Pm1M8TFbyNja5UAlgBOp3GN16uTk_Y9XhePPJBZuNNuQWZv42sFhDZ1aa4s-R9Ak5yHeDTl_dtXl7dOgmzAImhulGzp'
	encryptedData['file'] = encryptedFile
	enKey = formatData( encryptedData['enKey'] )
	password = getpass.getpass()
	key = formatData(decryptB( enKey, password ))
	# key = formatData(decryptB( enKey, input(' Password ') ))
	key = str(key,'iso-8859-1').replace( ' ', '' )
	key = formatData(key)
	# _.pr( 'decrypted key:', key )
	# decrypt2(fin=formatData(encryptedFile), fout=encryptedData['path'], key=key)
	# sys.exit()
	try:
		decrypt2(fin=formatData(encryptedFile), fout=encryptedData['path'], key=key)
	except Exception as e:
		_.pr()
		_.colorThis( [   'Bad Password'   ], 'red' )
		sys.exit()

encryptedData = { 'path': _v.keys+_v.slash+_.longID(4)+'.pem', 'file': '', 'enKey': 'zgEU5amYMg601oJeCjrLbdgR1+Xt2KBXMc43tKt0Ye2nHynBIugEH9ht6ssCnZCv' }
# _.pr(encryptedData)
thisSocket = None



######################################################################################## ########################################################################################
######################################################################################## ########################################################################################
######################################################################################## ########################################################################################
######################################################################################## ########################################################################################
# """


#client.py
#!/usr/bin/python
 
import socket
import ssl
import sys

import time
from threading import Thread


import _rightThumb._md5 as _md5
import _rightThumb._vars as _v

# hostname = 'localhost'
hostname = 'ncc-1701-d.rightthumb.com'
# port = 8443
port = 80
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
def establish():
	context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
	context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )

	# Create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock = context.wrap_socket(s, server_hostname=hostname)
	# Build a connection
	sock.connect((hostname, port))
	return sock

sock = establish()

loggedIn = False
first = True
# def handler( sock, i=0, qID=None, account=None, test=None ):
#     while True:
#         pass
#         # dataIn = sock.recv(1000)
#         # data = str(dataIn,'iso-8859-1')
#         # _.pr(data)
# Thread(target=handler, args=('sock')).start()
# Thread(target=handler, args=(client, i)).start()

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result


active = True
while active:
	# _.pr('loop')
	_.pr()
	# try:
	#     sock.connect((hostname, port))
	# except Exception as e:
	#     pass
	if not loggedIn:
		loggedIn = True
		data = {
					'user': 'administrator',
					'groups': ['administrators'],
					'flag': '2BR2D2C3P04LIFE_LOGIN'
		}

		result = formatData(str(data))

		expecting = _md5.md5( str(result,'iso-8859-1') )
		sock.send(result)
		# data = sock.recv(1024)
		# validation = str(data,'iso-8859-1')
		# _.pr( 'validation', validation )
		# if expecting == validation:
		#     _.pr( 'validation pass' )
		# else:
		#     _.pr( 'validation fail' )
		# sock.close()
		# try:
		#     sock.connect((hostname, port))
		# except Exception as e:
		#     pass
	# Read the message from keyboard

	u = input( 'Subject: - ' );
	while len(u) < 1:
		u = input( 'Empty, Subject: - ' );



	if active:
		m = input( 'Command: - ' );
		while len(m) < 1:
			m = input( 'Empty, Command: - ' );



	if active:

		data = {
					'user': u,
					'send': m,
					'flag': '2BR2D2C3P04LIFE_INSTRUCTIONS'
		}

		if data['user'] == 'self' and data['send'] == 'exit':
			active = False
			sock.close()
			# sys.exit()
		if active:
			result = str(data)
			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			sock.send( result )

			if data['user'] == 'server' and data['send'] == 'kill':
				active = False

				dataIn = sock.recv(16)
				data = str(dataIn,'iso-8859-1')

				if 'sendclose' == data:
					sock.close()
					sock = establish()


				try:
					sock.close()
				except Exception as e:
					pass



# """



########################################################################################
if __name__ == '__main__':
	action()







