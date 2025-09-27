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
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock = context.wrap_socket(s, server_hostname=hostname)
# Build a connection
sock.connect((hostname, port))
loggedIn = False
first = True
def handler( sock, i=0, qID=None, account=None, test=None ):
	while True:
		pass
		# dataIn = sock.recv(1000)
		# data = str(dataIn,'iso-8859-1')
		# print(data)
Thread(target=handler, args=('sock')).start()
# Thread(target=handler, args=(client, i)).start()
done = False
while not done:
	print('loop')
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

		result = str(data)
		try:
			result = str(result,'utf-8')
		except Exception as e:
			try:
				result = str(result,'iso-8859-1')
			except Exception as e:
				result = result.encode('utf-8')
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

	u = input( 'Send to user: - ' );
	while len(u) < 1:
		u = input( 'Empty, Send to user: - ' );


	if u.lower() == 'exit':
		done = True
		sock.close()
		# sys.exit()

	if not done:
		m = input( 'Enter your message: - ' );
		while len(m) < 1:
			m = input( 'Empty, Enter a message: - ' );


		if m.lower() == 'exit':
			done = True
			sock.close()
			# sys.exit()


	if not done:

		data = {
					'user': u,
					'send': m,
					'flag': '2BR2D2C3P04LIFE_INSTRUCTIONS'
		}


		result = str(data)
		try:
			result = str(result,'utf-8')
		except Exception as e:
			try:
				result = str(result,'iso-8859-1')
			except Exception as e:
				result = result.encode('utf-8')
		sock.send( result )

print('end')
try:
	sock.close()
except Exception as e:
	pass
try:
	sock.close()
except Exception as e:
	pass
try:
	sys.exit(0)
except Exception as e:
	pass
import os
try:
	os._exit()
except Exception as e:
	pass
try:
	sys.exit()
except Exception as e:
	pass


print('end')


