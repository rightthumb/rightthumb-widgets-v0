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

# server.py
import time
from threading import Thread


import socket
import ssl
import sys

import _rightThumb._md5 as _md5
import _rightThumb._vars as _v

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' , _v.keys+_v.slash+'self_private_NCC-1701-D.pem' )

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
socket.bind(('', 5555))
socket.listen(5)
ssock = context.wrap_socket(socket, server_side=True)




buf = ''
i = 0

def handler(client, i):
	global buf
	print( 'Hello!', client, i )
	if i == 0:  # client A, who sends data to server
		while True:
			req = client.recv(1000)
			buf = str(req).strip()  # removes end of line 
			print( 'Received from Client A: %s' % buf )
	elif i == 1:  # client B, who receives data sent to server by client A
		while True:
			if buf != '':
				client.send(buf)
				buf = ''
			time.sleep(0.1)

while True:  # very simple concurrency: accept new clients and create a Thread for each one
	client, address = ssock.accept()
	print( "{} connected".format(address) )
	Thread(target=handler, args=(client, i)).start()
	i += 1

# https://stackoverflow.com/questions/53479668/how-to-make-2-clients-connect-each-other-directly-after-having-both-connected-a


