import os

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
import _rightThumb._md5 as _md5

import socket
import ssl


##################################################


def appSwitches():
	pass
	# _.switches.register( 'Input', '-i' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'cloud_server.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
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
						'p cloud_server -file file.txt',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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






def encryptVar( data, key ):
	f = Fernet(key)
	return f.encrypt(data)


def decryptVar( data, key ):
	f = Fernet(key)
	return f.decrypt(data)

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











class Users:

	def __init__( self ):
		self.users = {}
	
	def login( self, user ):
		pass
	
	def logout( self, user ):
		pass

	def hello( self, user ):
		# if user == 'ALL':
		pass

	def status( self, dic ):
		# use, users, group, groups, all
		pass

	def activeUsers( self ):
		pass

	def activeAdmins( self ):
		pass

	def active( self, user ):
		# while users.active( account['user'] )
		pass


class Data:

	def __init__( self ):
		self.history = []
		self.queue = {}
		self.buffer = {}

	def process( self ):
		# on recv
		pass

	def send_recv( self ):
		# in if statement
		pass

	def query( self ):
		# group,system user,logs
		pass

	def registerExpectations( self ):
		# ex: hello waiting for response
		# send command wait for md5 - send md5 sent to confirmed
		pass

	def send( self, data, to ):
		pass

	def save( self ):
		# save history
		pass


# class Databases:

#     def __init__( self ):
#         self.databases = {}

#     def create( self, db ):
#         pass

#     def insert( self, db, sql ):
#         pass

#     def query( self, sql ):
#         pass

#     def buildSQL( self, dic ):
#         pass





import random




def handler( client, i, qID=None, account=None ):
	# _.pr( 'client:', type(client) )
	# sys.exit()
	global dataBuffer

	global users

	global history
	global buf
	global bufferQueue

	global killswitch
	global alive

	global logoutComplete

	global database

	global thePassword


	if alive:
		# _.pr( 'account:', str(account) )
		while alive and account is None:
			dataIn = client.recv(1000)
			data = str(dataIn,'iso-8859-1')
			# _.pr(data)
			if '2BR2D2C3P04LIFE_LOGIN' in data:
				account = eval(data)
				del account['flag']
				users[account['user']] = account
				users[account['user']]['status'] = 1
				users[account['user']]['epoch'] = time.time()
				users[account['user']]['logout'] = None

				salt = {
							'flag': '2BR2D2C3P04LIFE_SALT',
							'auth': _.genUUID(),
							'code': random.randint(1,10)
				}

				# client.send( formatData( salt ) )

				users[account['user']]['authorized'] = False
				
				recordFound = False
				authorized = False
				for userRecord in database:
					if userRecord['user'] == account['user']:
						_.colorThis( [ 'Login:\t', account['user'] ], 'yellow' )
						# _.pr( 'record found' )
						recordFound = True
						# _.pr( 'en:', userRecord['password'] )
						# _.pr( 'pass:', formatData(account['password']) )
						# _.pr( 'base:', thePassword )
						try:
							decryptedPassword = decryptVar( formatData(userRecord['password']), formatData(account['password']) )
							decryptedPasswordDecoded = str(decryptedPassword,'iso-8859-1')
						except Exception as e:
							decryptedPassword = '{098DCA7077F5}'

						# _.pr( 'decrypted', decryptedPasswordDecoded )
						if decryptedPasswordDecoded == users[account['user']]['machine']:
							authorized = True
							users[account['user']]['authorized'] = True

							# _.colorThis( [ 'Good Password' ], 'green' )
						else:
							users[account['user']]['authorized'] = False
							# _.colorThis( [ 'Bad Password' ], 'red' )
				if not recordFound:
					_.colorThis( [ 'record NOT found:', account['user'] ], 'red' )
					write_key()
					key = load_key()
					_.pr( 'new key:', _.colorThis( [ key ], 'green', p=0 ) )
					
					newRecord = {
										'user': account['user'],
										'password': encryptVar( formatData(users[account['user']]['machine']), key ),
					}
					# _.pr( newRecord )
					database.append(newRecord)
					_.saveTable( database, 'ssl_socket_bridge_user_mgt_server.json' )




				dataBuffer[  account['user']  ] = None
				del users[account['user']]['password']
				
				
				if authorized:
					authColor = 'green'
				else:
					authColor = 'red'
				_.pr( 'authorized:', _.colorThis( authorized, authColor, p=0 ) )

				if account['user'] == 'logs':
					dataBuffer[  account['user']  ] = { 'data': users, 'flag': '2BR2D2C3P04LIFE_USERS' }

				break

		if 'administrators' in account['groups']:
			_.pr( 'Administrator Login' )

			while users[account['user']]['status']:

				dataIn = client.recv(1000)
				data = str(dataIn,'iso-8859-1')

				if '2BR2D2C3P04LIFE_INSTRUCTIONS' in data:
					instructions = eval(data)
					_.printVar( instructions )
					if not instructions['send'] is None:
						_.pr( 'INSTRUCTIONS:\t', instructions['user'], instructions['send'] )
						time.sleep(.5)

						

						history.append({ 'epoch': time.time(), 'user': instructions['user'], 'send': instructions['send'] })

						# if instructions['send'] == 'exit':
						#     time.sleep(2)
						#     users[instructions['user']]['status'] = 0
						#     users[instructions['user']]['logout'] = time.time()

						if instructions['user'] == 'request':
							
							if instructions['send'] == 'users':
								dataBuffer[  'logs'  ] = { 'data': users, 'flag': '2BR2D2C3P04LIFE_USERS' }

							if instructions['send'] == 'history':
								dataBuffer[  'logs'  ] = { 'data': history, 'flag': '2BR2D2C3P04LIFE_HISTORY' }


						elif not instructions['user'] == 'server':
							dataBuffer[  instructions['user']  ] = instructions['send']
						else:
							if instructions['send'] == 'kill':
								_.pr( 'server kill' )
								killswitch = True
								
								_.threads.autoLoaded = True
								_.pr( 'Kill', account['user'], qID )
								users[account['user']]['status'] = 0
								users[account['user']]['logout'] = time.time()
								# shutdown()


								wait = True

								while wait:
									_.pr( 'waiting for connections to close' )
									cnt = 0
									for usr in active.keys():
										if active[usr] == True and not usr == 'administrator':
											cnt+=1
									if not cnt:
										wait = False
									time.sleep(2)
								logoutComplete = 1
								client.send(  formatData('sendclose')  )
								alive = False
								client.close()
								_.threads.kill( qID )
								sys.exit()

		elif 'system' in account['groups'] and account['user'] == 'logs':
			# _.pr( 'Log Client Connected' )

			while users[account['user']]['status']:

				if killswitch:
					users[account['user']]['status'] = 0
					users[account['user']]['logout'] = time.time()
					client.send(  formatData('exit')  )
					_.pr( 'Kill', account['user'], qID )
					client.close()
					_.threads.kill( qID )

					

				if not dataBuffer[  account['user']  ] is None:
					_.pr( account['user'], 'Data for me' )
					result = dataBuffer[  account['user']  ]
					if result == 'exit':
						users[account['user']]['status'] = 0
						users[account['user']]['logout'] = time.time()
					result = formatData( result )
					if len(str(result,'iso-8859-1')):
						client.send(result)
						_.pr( 'sent' )
					dataBuffer[  account['user']  ] = None
				time.sleep(0.1)




		elif 'users' in account['groups']:
			# _.pr( 'User Login:', account['user'] )
			while users[account['user']]['status']:

				if killswitch:
					users[account['user']]['status'] = 0
					users[account['user']]['logout'] = time.time()
					client.send(  formatData('exit')  )
					_.pr( 'Kill', account['user'], qID )
					client.close()
					_.threads.kill( qID )

					

				if not dataBuffer[  account['user']  ] is None:
					_.pr( account['user'], 'Data for me' )
					result = dataBuffer[  account['user']  ]
					if result == 'exit':
						users[account['user']]['status'] = 0
						users[account['user']]['logout'] = time.time()
					result = formatData( result )
					if len(str(result,'iso-8859-1')):
						client.send(result)
						_.pr( 'sent' )
					dataBuffer[  account['user']  ] = None
				time.sleep(0.1)



def action():

	global history
	global buf
	global dataBuffer
	global bufferQueue

	global killswitch
	global alive

	global logoutComplete

	global database

	database = _.getTable( 'ssl_socket_bridge_user_mgt_server.json' )

	hostname = 'ncc-1701-d.rightthumb.com'
	# port = 8443
	port = 80

	context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	context.load_cert_chain( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' , _v.keys+_v.slash+'self_private_NCC-1701-D.pem' )



	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_address = ( hostname , int(port) )
	s.bind(server_address)
	s.listen(5)
	sock = context.wrap_socket(s, server_side=True)


	_.threads.autoLoaded = False
	_.threads.maxThreadsSafe = 250
	_.threads.report = False
	_.threads.auditPrint = False
	_.threads.register( 'sessions', logout )


	i = 0
	while alive:
		try:
			# sock.settimeout(5.0)
			client, address = sock.accept()
			_.pr( "{} connected".format(address) )

			_.threads.add( 'sessions', handler, [{'client':client,'i':i}], kwargs=True )
			i += 1
		finally:
			pass

		if not alive:
			try:
				sock.shutdown(socket.SHUT_RDWR)
			except Exception as e:
				pass
			try:
				sock.close()
			except Exception as e:
				pass
			_.pr('sleep')
			while logoutComplete == 0:
				time.sleep(.5)
			time.sleep(5)
			_.pr('killAll')
			_.threads.killAll()
			while not logoutComplete == 2:
				time.sleep(.5)
			time.sleep(8)
			_.pr('end')
			sys.exit()
			raise


def logout():
	global logoutComplete
	logoutComplete = 2
	_.pr( 'Logout' )




database = []

logoutComplete = 0
history = []
buf = ''
dataBuffer = {}
bufferQueue = {} #####
active = {}
killswitch = False
alive = True
users = {}
from threading import Thread
thePassword = '{EA3B13CF-199A-4D6D-84C6-7B99E86F17CC}'



"""
BASED ON 
			ssl_socket_bridge_user_mgt_server_b

epyi cloud_server -file bridge
epyi cloud_server -file client
epyi cloud_server -file admin


"""




########################################################################################
if __name__ == '__main__':
	action()






