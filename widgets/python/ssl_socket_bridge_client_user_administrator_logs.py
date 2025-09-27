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

# print( 'user:', sys.argv[2] )

# Bind the socket to the address given on the command line

# print(sys.stderr, 'starting up on %s port %s' % sock.getsockname())

loggedIn = False
while True:

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
							'user': 'logs',
							'groups': ['system'],
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

				sock.send(result)



			data = sock.recv(16)
			print(str(data,'iso-8859-1'))



	finally:
		# print('the end')
		pass
sock.close()


