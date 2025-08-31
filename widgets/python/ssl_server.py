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

import socket
import ssl
import sys

import _rightThumb._md5 as _md5
import _rightThumb._vars as _v

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain( _v.keys+_v.slash+'self_public.pem' , _v.keys+_v.slash+'self_private.pem' )

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
	sock.bind(('127.0.0.1', 8443))
	# sock.bind(('192.168.1.10', 8443))
	sock.listen(5)
	with context.wrap_socket(sock, server_side=True) as ssock:
		# conn, addr = ssock.accept()


		while True:

			# print(sys.stderr, 'waiting for a connection')
			print()
			print()
			print()
			print('\twaiting for a connection')
			connection, client_address = ssock.accept()
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
						# connection.sendall(data)
						validation = _md5.md5( str(data,'iso-8859-1') )
						try:
							validation = str(validation,'utf-8')
						except Exception as e:
							try:
								validation = str(validation,'iso-8859-1')
							except Exception as e:
								validation = validation.encode('utf-8')

						print( 'validation:', str(validation,'iso-8859-1') )
						connection.sendall( validation )
					else:

						# works

						print( 'Payload:', result )

						if result.lower() == 'exit':
							print( 'Exit command received' )
							sys.exit()


						break
			finally:
				# print('the end')
				connection.close()


