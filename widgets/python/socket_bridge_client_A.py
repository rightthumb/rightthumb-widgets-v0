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
 
ip = '127.0.0.1'
port = 5555


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ( ip , int(port) )
sock.bind(server_address)
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

