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

import _rightThumb._md5 as _md5
import _rightThumb._vars as _v

# hostname = 'localhost'
hostname = 'ncc-1701-d.rightthumb.com'
port = 8443
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s = context.wrap_socket(s, server_hostname=hostname)
# Build a connection
s.connect((hostname, port))

# Read the message from keyboard
m = input( 'Enter your message:\n\n - ' );
while len(m) < 1:
	m = input( 'Empty, Enter a message:\n\n - ' );
#m = input("Eneter your message:\n");# evaluate the string

result = m
try:
	result = str(result,'utf-8')
except Exception as e:
	try:
		result = str(result,'iso-8859-1')
	except Exception as e:
		result = result.encode('utf-8')
# Send the message to server
s.send( result );
#s.sendall('Hello, world')

# Receive the feedback from server
data = s.recv(1024)
s.close()

print( 'Received from server:\n', data )
#print 'Received:\n', repr(data)


