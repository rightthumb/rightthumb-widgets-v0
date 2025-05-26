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



# hostname = "localhost"
# hostname = "192.168.1.10"
# hostname = "127.0.0.1"
hostname = 'ncc-1701-d.rightthumb.com'
# port = 8443
port = 80
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
try:
	import _rightThumb._vars as _v
	context.load_verify_locations( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' )
except Exception as e:
	context.load_verify_locations( "self_public_NCC-1701-D.pem" )
	

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock = context.wrap_socket(s, server_hostname=hostname)
# Build a connection
sock.connect((hostname, port))

loggedIn = False

while True:
	if not loggedIn:
		loggedIn = True
		data = {
					"user": "administrator_phone",
					"groups": ["administrators"],
					'password': 'ilSRR1g2zPIDO_1Rta4XNTW4-Wc4DFiIdF62JcZTECw=',
					'machine': '{D18C6188-B114-4BD3-9075-F5F5B1546ED9}',
					"flag": "2BR2D2C3P04LIFE_LOGIN"
		}

		result = str(data)
		try:
			result = str(result,"utf-8")
		except Exception as e:
			try:
				result = str(result,"iso-8859-1")
			except Exception as e:
				result = result.encode("utf-8")
		sock.send(result)



	u = input( "Send to user: - " );
	while len(u) < 1:
		u = input( "Empty, Send to user: - " );
	if u.lower() == "exit":
		sock.exit()
	m = input( "Enter your message: - " );
	while len(m) < 1:
		m = input( "Empty, Enter a message: - " );
	if m.lower() == "exit":
		sock.exit()

	data = {
				"user": u,
				"send": m,
				"flag": "2BR2D2C3P04LIFE_INSTRUCTIONS"
	}


	result = str(data)
	try:
		result = str(result,"utf-8")
	except Exception as e:
		try:
			result = str(result,"iso-8859-1")
		except Exception as e:
			result = result.encode("utf-8")
	sock.send( result );


