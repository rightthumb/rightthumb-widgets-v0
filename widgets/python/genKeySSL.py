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

##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
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

##################################################


def appSwitches():
		_.switches.register( 'Description', '-description' )
		_.switches.register( 'FileLabel', '-file,-label' )


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
		'file': 'genKeySSL.py',
		'liveAppName': __.thisApp( __file__ ),
		'description': 'Generate SSL keys public.crt private.pem',
		'categories': [
												'ssl',
						'key',
						'public',
						'private',
						'tool',
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
												'p genKeySSL -file vnc  -description secure vnc connection',
												''
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START



#!/usr/bin/python

import OpenSSL

def GenerateSelfSignedCert(common_name, validity, serial_no):
	# Create private and public key
	key = OpenSSL.crypto.PKey()
	key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)
	# Create self-signed certificate
	cert = OpenSSL.crypto.X509()
	if common_name:
		cert.get_subject().CN = common_name
	cert.set_serial_number(serial_no)
	cert.gmtime_adj_notBefore(0)
	cert.gmtime_adj_notAfter(validity)
	cert.set_issuer(cert.get_subject())
	cert.set_pubkey(key)
	cert.sign(key, "SHA1")
	return (cert, key)

def WriteCertFile(cert, key, filename):
	key_pem = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
	cert_pem = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
	# cert_fd.write(cert_pem)
	# cert_fd.write(key_pem)

	cert_fd = open( 'ssl_public_'+ filename +'.crt', "w")
	cert_fd.write(  str(  cert_pem  ,'iso-8859-1')  )
	cert_fd.close()

	cert_fd = open( 'ssl_private_'+ filename +'.pem', "w")
	cert_fd.write(  str(  key_pem  ,'iso-8859-1')  )
	cert_fd.close()

def TestFrankenCert():
	validity = 24*60*365
	(cert1, key1) = GenerateSelfSignedCert("My Certificate No 1", validity, 12345)
	(cert2, key2) = GenerateSelfSignedCert("My Certificate No 2", validity, 67890)

	WriteCertFile(cert1, key1, "TEST")
	# WriteCertFile(cert2, key2, "two")
	# WriteCertFile(cert1, key2, "cross")

	try:
		ctx = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
		ctx.use_privatekey(key2)
		ctx.use_certificate(cert1)
		ctx.check_privatekey()
	except OpenSSL.SSL.Error as e:
		_.pr()
		_.pr( "SSL test success" )
		# _.pr( "SSL test success : %s" % e )
		return

	_.pr()
	_.pr( "SSL test fail" )

# if __name__ == "__main__":
#     TestFrankenCert()



def action():
  
	validity = 24*60*365
	serial_no = _.genSerial( 'ssl_key' )

	description = 'Socket Project'
	label = 'socket'

	if _.switches.isActive('Description'):
		description = ' '.join(  _.switches.values( 'Description' )  )

	if _.switches.isActive('FileLabel'):
		label = _.switches.values( 'FileLabel' )[0]

	_.pr(  )
	_.pr( 'Description:', description )
	_.pr( 'Label:', label.upper() )

	(cert1, key1) = GenerateSelfSignedCert( description , validity, serial_no )

	WriteCertFile( cert1, key1, label.upper() )


# https://github.com/pyca/pyopenssl/issues/178
########################################################################################
if __name__ == '__main__':
  action()







