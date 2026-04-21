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

# hostname = 'localhost'
hostname = 'ncc-1701-d.rightthumb.com'
port = 8443
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations( _v.keys+_v.slash+'self_public.pem' )

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
		with context.wrap_socket(sock, server_hostname=hostname) as ssock:
			# print(ssock.version())
			# for x in dir(ssock):
			#     print(x)
			shouldExit = False
			s = ssock
			# Build a connection
			s.connect((hostname, port))
			print()
			print()
			print()
			# Read the message from keyboard
			m = input( 'Enter your message: - ' );
			while len(m) < 1:
				m = input( 'Empty, Enter a message: - ' );
			#m = input("Eneter your message:\n");# evaluate the string
			if m.lower() == 'exit':
				shouldExit = True
			result = m
			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			# Send the message to server
			expecting = _md5.md5( str(result,'iso-8859-1') )
			s.send( result );
			#s.sendall('Hello, world')
			
			# Receive the feedback from server
			data = s.recv(1024)
			s.close()
			
			print( 'validation:', str(data,'iso-8859-1') )
			
			serverReturn = str(data,'iso-8859-1')

			if expecting == serverReturn:
				print( 'Data Validation Pass' )
			else:
				print( 'Data Validation Fail' )

			if shouldExit:
				print( 'Exit command received' )
				sys.exit()
			#print 'Received:\n', repr(data)


# accept
# bind
# cipher
# close
# compression
# connect
# connect_ex
# context
# detach
# do_handshake
# do_handshake_on_connect
# dup
# family
# fileno
# get_channel_binding
# get_inheritable
# getpeercert
# getpeername
# getsockname
# getsockopt
# gettimeout
# ioctl
# listen
# makefile
# pending
# proto
# read
# recv
# recv_into
# recvfrom
# recvfrom_into
# recvmsg
# recvmsg_into
# selected_alpn_protocol
# selected_npn_protocol
# send
# sendall
# sendfile
# sendmsg
# sendto
# server_hostname
# server_side
# session
# session_reused
# set_inheritable
# setblocking
# setsockopt
# settimeout
# share
# shared_ciphers
# shutdown
# suppress_ragged_eofs
# timeout
# type
# unwrap
# version
# write



