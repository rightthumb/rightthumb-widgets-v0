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

import os
import sys
import time
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str





##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register( 'Domain', '-domain,-site', 'ncc-1701-d.rightthumb.com' )
	_.switches.register( 'IP_Addresses', '-ip,-ips', '127.0.0.1   192.168.1.10   47.199.204.180' )

	# _.switches.register( 'Key', '-key' )
	_.switches.register( 'FileLabel', '-label', 'ncc 1701 d' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'genKeySelfSigned.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate ssl keys that are self signed',
	'categories': [
						'ssl',
						'key',
						'security',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'?',
						'p genKeySelfSigned -domain ncc-1701-d.rightthumb.com -ips 127.0.0.1   192.168.1.10   47.199.204.180 -label ncc 1701 d',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],

	}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
				'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
				'table': {'sent': [], 'received': [] }, 
	},
	}

# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START






from datetime import datetime, timedelta
import ipaddress

def generate_selfsigned_cert(hostname, ip_addresses=None, key=None):
	"""Generates self signed certificate for a hostname, and optional IP addresses."""
	from cryptography import x509
	from cryptography.x509.oid import NameOID
	from cryptography.hazmat.primitives import hashes
	from cryptography.hazmat.backends import default_backend
	from cryptography.hazmat.primitives import serialization
	from cryptography.hazmat.primitives.asymmetric import rsa
	
	# Generate our key
	if key is None:
		key = rsa.generate_private_key(
			public_exponent=65537,
			key_size=2048,
			backend=default_backend(),
		)
	
	name = x509.Name([
		x509.NameAttribute(NameOID.COMMON_NAME, hostname)
	])
 
	# best practice seem to be to include the hostname in the SAN, which *SHOULD* mean COMMON_NAME is ignored.    
	alt_names = [x509.DNSName(hostname)]
	
	# allow addressing by IP, for when you don't have real DNS (common in most testing scenarios 
	if ip_addresses:
		for addr in ip_addresses:
			# openssl wants DNSnames for ips...
			alt_names.append(x509.DNSName(addr))
			# ... whereas golang's crypto/tls is stricter, and needs IPAddresses
			# note: older versions of cryptography do not understand ip_address objects
			alt_names.append(x509.IPAddress(ipaddress.ip_address(addr)))
	
	san = x509.SubjectAlternativeName(alt_names)
	
	# path_len=0 means this cert can only sign itself, not other certs.
	basic_contraints = x509.BasicConstraints(ca=True, path_length=0)
	now = datetime.utcnow()
	cert = (
		x509.CertificateBuilder()
		.subject_name(name)
		.issuer_name(name)
		.public_key(key.public_key())
		.serial_number(1000)
		.not_valid_before(now)
		.not_valid_after(now + timedelta(days=10*365))
		.add_extension(basic_contraints, False)
		.add_extension(san, False)
		.sign(key, hashes.SHA256(), default_backend())
	)
	cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
	key_pem = key.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.TraditionalOpenSSL,
		encryption_algorithm=serialization.NoEncryption(),
	)

	return cert_pem, key_pem









def action():

	domain = 'rightthumb.com'
	ipaddresses = ['50.63.114.1']

	domain = 'tools.rightthumb.com'
	ipaddresses = ['107.180.50.181']

	domain = 'ncc-1701-d.rightthumb.com'
	ipaddresses = ['47.199.204.180']
	ipaddresses = ['127.0.0.1','192.168.1.10', '47.199.204.180']
	
	label = 'test'
	# domain = 'localhost'
	# ipaddresses = ['127.0.0.1']
 
	key = None
	if _.switches.isActive('Domain'):
		domain = _.switches.values('Domain')[0]

	if _.switches.isActive('IP_Addresses'):
		ipaddresses = _.switches.values('IP_Addresses')
	
	if _.switches.isActive('FileLabel'):
		label = '-'.join( _.switches.values('FileLabel') )
	label = label.upper()

	if _.switches.isActive('Key'):
		# key = _.getText( _.switches.values('Key')[0], clean=2, raw=1 )
		with open(  _.switches.values('Key')[0]  , mode='rb') as file: # b is important -> binary
			key = file.read()


	_.pr( 'Domain:', domain )
	_.pr( 'IP Addresses:', ipaddresses )
	_.pr( 'Label:', label )

	cert = generate_selfsigned_cert( hostname=domain, ip_addresses=ipaddresses, key=key )
	# _.pr()
	# _.pr( 'cert_pem:' )
	# _.pr()
	# _.pr( str(  cert[0]  ,'iso-8859-1') )
	# _.pr()
	# _.pr( 'key_pem:' )
	# _.pr()
	# _.pr( str(  cert[1]  ,'iso-8859-1') )

	# if _.switches.isActive('Save'):
	_.saveText(  str(  cert[0]  ,'iso-8859-1'), _v.keys+_v.slash+'self_public_'+label+'.crt'  )
	_.saveText(  str(  cert[1]  ,'iso-8859-1'), _v.keys+_v.slash+'self_private_'+label+'.pem'  )
	_.pr( 'Saved' )

# https://gist.github.com/bloodearnest/9017111a313777b9cce5
########################################################################################
if __name__ == '__main__':
	action()









# Copyright 2018 Simon Davy






