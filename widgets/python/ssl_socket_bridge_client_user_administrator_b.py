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
#         # print(data)
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
	# print('loop')
	print()
	# try:
	#     sock.connect((hostname, port))
	# except Exception as e:
	#     pass
	if not loggedIn:
		loggedIn = True
		data = {
					'user': 'administrator',
					'groups': ['administrators'],
					'password': '3mDOhQLMMRA-QTZhlN1hJpHOq2aZbAEvOClnpJwxDEA=',
					'machine': '{B1669E09-DB5B-E77C-7B53-65EE04FBF88E}',
					'flag': '2BR2D2C3P04LIFE_LOGIN',
		}

		result = formatData(str(data))

		expecting = _md5.md5( str(result,'iso-8859-1') )
		sock.send(result)
		# data = sock.recv(1024)
		# validation = str(data,'iso-8859-1')
		# print( 'validation', validation )
		# if expecting == validation:
		#     print( 'validation pass' )
		# else:
		#     print( 'validation fail' )
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



