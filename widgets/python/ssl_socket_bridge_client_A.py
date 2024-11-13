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
hostname = 'ncc-1701-d.rightthumb.com'
port = 8443
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )





context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' , _v.keys+_v.slash+'self_private_NCC-1701-D.pem' )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ( hostname , int(port) )
s.bind(server_address)
s.listen(5)
sock = context.wrap_socket(s, server_side=True)






# Bind the socket to the address given on the command line

# print(sys.stderr, 'starting up on %s port %s' % sock.getsockname())
print('starting up on %s port %s' % sock.getsockname())
sock.listen(1)


while True:

	# print(sys.stderr, 'waiting for a connection')
	print('\twaiting for a connection')
	connection, client_address = sock.accept()
	try:
		# print(sys.stderr, 'client connected:', client_address)
		print('client connected:', client_address)
		result = ''
		i = 0
		while True:
			i += 1
			data = connection.recv(16)

			result += str(data,'iso-8859-1')

			if data:
				# possibly change to md5 of data
				connection.sendall(data)
			else:

				# works

				print( 'Payload:', result )


				break
	finally:
		# print('the end')
		connection.close()


