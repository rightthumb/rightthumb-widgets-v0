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
import socket, time
from threading import Thread
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 5555))
socket.listen(5)
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
	client, address = socket.accept()
	print( "{} connected".format(address) )
	Thread(target=handler, args=(client, i)).start()
	i += 1

# https://stackoverflow.com/questions/53479668/how-to-make-2-clients-connect-each-other-directly-after-having-both-connected-a

