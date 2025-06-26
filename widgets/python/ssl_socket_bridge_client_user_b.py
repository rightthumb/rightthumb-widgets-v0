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

#client.py
#!/usr/bin/python



#client.py
#!/usr/bin/python

import os
 
import socket
import ssl
import sys

import _rightThumb._md5 as _md5
import _rightThumb._vars as _v

# hostname = 'localhost'
# hostname = 'ncc-1701-d.rightthumb.com'
# port = 8443
# # PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )





# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' , _v.keys+_v.slash+'self_private_NCC-1701-D.pem' )

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_address = ( hostname , int(port) )
# s.bind(server_address)
# s.listen(5)
# sock = context.wrap_socket(s, server_side=True)




# hostname = 'localhost'
hostname = 'ncc-1701-d.rightthumb.com'
# port = 8443
port = 80
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock = context.wrap_socket(s, server_hostname=hostname)
# Build a connection
sock.connect((hostname, port))
loggedIn = False

print( 'user:', sys.argv[2] )

# Bind the socket to the address given on the command line

# print(sys.stderr, 'starting up on %s port %s' % sock.getsockname())





class Process:

	def __init__( self ):
		self.history = []
		self.queue = {}
		self.buffer = {}
		self.loggedIn = False

	def login( self ):
		self.loggedIn = True
		# if statement
		# schedule send
		pass

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

	def send( self, data ):
		pass

	def save( self ):
		# save history
		pass

	def execute( self ):
		# execute command
			# import keyboard
			# in thread
		pass

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

def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result


def saveTable2( rows, theFile, printThis=False, sort_keys=False, indentCode=True ):
	# print('*******************',theFile)

	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
	else:
		dataDump = json.dumps(rows)

	# dataDump = json.dumps(rows, indent=4, sort_keys=sort_keys)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)

def getTable2( theFile,     isDic=None, isList=None ):
	import simplejson as json
	if os.path.isfile(theFile) == True:
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		if isDic is None and isList is None:
			return []
		if isDic:
			return {}
		if isList:
			return []

authCache_File = _v.myTables+_v.slash+'ssl_socket_bridge_authorization_cache.json'

authCache = getTable2( authCache_File, isDic=True )
# saveTable2( authCache, authCache_File )

active = True

loggedIn = False



while active:

	# print(sys.stderr, 'waiting for a connection')
	print('\twaiting for a connection')
	try:
		# print(sys.stderr, 'client connected:', client_address)
		# print('client connected:', client_address)
		result = ''
		i = 0
		while True:

			
			if not loggedIn:
				loggedIn = True
				data = {
							'user': sys.argv[2],
							'groups': ['users'],
							'password': 'qwyFAz5-mQ3_uPrbSn4kwJpefi1xJbXG60vrsypVO-A=',
							'machine': '{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}',
							'flag': '2BR2D2C3P04LIFE_LOGIN',
				}
				if data['user'] == 'dad':
					data['password'] = 'sDu5hnoJs9QWeC-KzFhbx1y7QQBcUhgpceNPf71spFg='
				if data['user'] == 'dennis':
					data['password'] = '2yT9tM06WBQBs0xcm-boxzhm5N7oC2PNWFztCgJNNJk='

				result = formatData(str(data))


				sock.send(result)

			data = ''
			try:
				dataIn = sock.recv(16)
				data = str(dataIn,'iso-8859-1')
			except Exception as e:
				pass
			print( data )
			if data == 'hello':
				sock.send( dataIn )
			if data == 'exit':
				active = False
				sock.close()

				# raise
				sys.exit()

			# result = ''
			# result += str(data,'iso-8859-1')

			# if data:
			#     result = _md5.md5( str(data,'iso-8859-1') )
			#     try:
			#         result = str(result,'utf-8')
			#     except Exception as e:
			#         try:
			#             result = str(result,'iso-8859-1')
			#         except Exception as e:
			#             result = result.encode('utf-8')
			#     sock.sendall(result)
			# else:

			#     # works

			#     print( 'Payload:', result )


			#     break
	finally:
		# print('the end')
		pass
# sock.close()


