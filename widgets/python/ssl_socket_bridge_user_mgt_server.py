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

hostname = 'ncc-1701-d.rightthumb.com'
# port = 8443
port = 80

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain( _v.keys+_v.slash+'self_public_NCC-1701-D.pem' , _v.keys+_v.slash+'self_private_NCC-1701-D.pem' )



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ( hostname , int(port) )
s.bind(server_address)
s.listen(5)
sock = context.wrap_socket(s, server_side=True)



class Users:

	def __init__( self ):
		self.users = {}
	
	def login( self, user ):
		pass
	
	def logout( self, user ):
		pass

	def hello( self, user ):
		# if user == 'ALL':
		pass

	def status( self, dic ):
		# use, users, group, groups, all
		pass

	def activeUsers( self ):
		pass

	def activeAdmins( self ):
		pass

	def active( self, user ):
		# while users.active( account['user'] )
		pass


class Data:

	def __init__( self ):
		self.history = []
		self.queue = {}
		self.buffer = {}

	def process( self ):
		# on recv
		pass

	def send_recv( self ):
		# in if statement
		pass

	def query( self ):
		# group,system user,logs
		pass

	def registerExpectations( self ):
		# ex: hello waiting for response
		# send command wait for md5 - send md5 sent to confirmed
		pass

	def send( self, data, to ):
		pass

	def save( self ):
		# save history
		pass


# class Databases:

#     def __init__( self ):
#         self.databases = {}

#     def create( self, db ):
#         pass

#     def insert( self, db, sql ):
#         pass

#     def query( self, sql ):
#         pass

#     def buildSQL( self, dic ):
#         pass








history = []
buf = ''
dataBuffer = {}
bufferQueue = {} #################################################################
users = []
i = 0

def handler( client, i, qID=None, account=None, test=None ):
	global dataBuffer
	global users
	print( 'account:', str(account) )
	while account is None:
		dataIn = client.recv(1000)
		data = str(dataIn,'iso-8859-1')
		# print(data)
		if '2BR2D2C3P04LIFE_LOGIN' in data:
			account = eval(data)
			dataBuffer[  account['user']  ] = None

			print( 'Login:\t', account['user'] )

			# for key in account.keys():
			#     print()
			#     print( key+':' )
			#     print( '\t', account[key] )

			if 'users' in account['groups']:
				users.append({ 'epoch': time.time(), 'sent': 0, 'record': account, 'flag': '2BR2D2C3P04LIFE_ANNOUNCE_USER' })

			# if 'administrators' in account['groups']:

			break

	if 'administrators' in account['groups']:
		print( 'Administrator Login' )
		while True:



			dataIn = client.recv(1000)
			data = str(dataIn,'iso-8859-1')
			if '2BR2D2C3P04LIFE_INSTRUCTIONS' in data:
				instructions = eval(data)
				if not instructions['send'] is None:
					dataBuffer[  instructions['user']  ] = instructions['send']
					print( 'INSTRUCTIONS:\t', instructions['user'], instructions['send'] )

	elif 'system' in account['groups'] and account['user'] == 'logs':
		# print( 'Log Client Connected' )

		while True:

			for i,user in enumerate(users):
				if not user['sent']:
					users[i]['sent'] = 1
					result = str(users[i])

					try:
						result = str(result,'utf-8')
					except Exception as e:
						try:
							result = str(result,'iso-8859-1')
						except Exception as e:
							result = result.encode('utf-8')

					client.send(result)

	elif 'users' in account['groups']:
		# print( 'User Login:', account['user'] )
		while True:
			if not dataBuffer[  account['user']  ] is None:
				print( account['user'], 'Data for me' )
				result = dataBuffer[  account['user']  ]
				try:
					result = str(result,'utf-8')
				except Exception as e:
					try:
						result = str(result,'iso-8859-1')
					except Exception as e:
						result = result.encode('utf-8')
				if len(str(result,'iso-8859-1')):
					client.send(result)
				dataBuffer[  account['user']  ] = None
			time.sleep(0.1)

while True:  # very simple concurrency: accept new clients and create a Thread for each one
	client, address = sock.accept()
	print( "{} connected".format(address) )
	Thread(target=handler, args=(client, i)).start()
	i += 1

# https://stackoverflow.com/questions/53479668/how-to-make-2-clients-connect-each-other-directly-after-having-both-connected-a


