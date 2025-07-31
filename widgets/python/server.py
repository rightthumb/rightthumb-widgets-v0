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

# import os
# import simplejson as json
# import shutil
# https://gist.github.com/MarkNenadov/861037
import socket
import sys

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._md5 as _md5

from Crypto.Cipher import Blowfish
import base64

import time
import uuid
import os

from random import randint



_.switches.register('IP', '-ip','192.168.1.10')
_.switches.register('Port', '-port','10000')
_.switches.register('Message', '-message','this is a test message')
_.switches.register('Table', '-table','tableName.json')
_.switches.register('File', '-file','file.zip')
_.switches.register('Encrypt', '-encrypt')
_.switches.register('Auto', '-auto')
_.switches.register('Secure', '-secure,-unhackable','password')

_.appInfo=    {
	'file': 'server.py',
	'description': 'Push data to a client',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -table countries_from_adobe_web_form.json')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -message this is a test message')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -message this is a test message -encrypt')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -table countries_from_adobe_web_form.json -encrypt')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -file table.zip -encrypt')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -auto -encrypt -file 0000_test.txt ')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p server -ip 192.168.1.10 -port 10000 -auto -encrypt -file file.json -secure 777')
if __name__ == '__main__':
	_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
encryptionKey = '{3DDED2AD-AFA6-58A3-3D7C-55D93A9AE84E}'
encryptionKeyBase = ''
salt = []

def genUUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	return string

def pad_string(string):
	INPUT_SIZE = 8
	new_str = string
	pad_chars = INPUT_SIZE - (len(string) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		

	return new_str

def newKey():
	global encryptionKey
	global encryptionKeyBase
	# print(_.switches.value('Auto'),type(_.switches.value('Auto')))
	keyInput = ''
	if _.switches.isActive('Auto'):
		if len(encryptionKeyBase) == 0:
			encryptionKeyBase = genUUID()
		theFile = ''
		if _.switches.isActive('Table'):
			theFile = _.switches.value('Table')

		if _.switches.isActive('File'):
			theFile = _.switches.value('File')
		# keyInput = str(encryptionKey) + str(theFile) + str(encryptionKeyBase)
		keyInput = str(encryptionKey) + str(encryptionKeyBase)
		md5 = _md5.md5(keyInput)
	if _.switches.isActive('Auto') and _.switches.value('Auto'):
		encryptionKeyNew = _md5.md52GUID(md5,True)
	elif _.switches.isActive('Auto') and not _.switches.value('Auto'):
		keyInput = encryptionKey + seasoning()
		md5 = _md5.md5(keyInput)
		encryptionKeyNew = _md5.md52GUID(md5,True)


		# encryptionKeyNew = encryptionKey
	else:
		encryptionKeyNew = encryptionKey
	# print(keyInput)
	# print(encryptionKeyNew)
	return encryptionKeyNew

def encryptMessage(thePayload):
	crypt_obj = Blowfish.new(newKey(), Blowfish.MODE_ECB)
	try:
		ciphertext = crypt_obj.encrypt(pad_string(str(thePayload)))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(pad_string(str(thePayload)) + space)
				works = True
			except Exception as e:
				pass
			space += ' '
			if i == 10:
				works = True
			i += 1

	# try:
	result = base64.b64encode(ciphertext)
	thePayload = str(result,'iso-8859-1')
	# except Exception as e:
	#     pass

	return thePayload

def send(thePayload):
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port on the server given by the caller
	# print(sys.argv[2])
	server_address = (_.switches.value('IP'), int(_.switches.value('Port')))
	# print(sys.stderr, 'connecting to %s port %s' % server_address)
	print('\tconnecting to %s port %s' % server_address)
	sock.connect(server_address)

	try:
		# message = str(thePayload,'iso-8859-1')
		message = thePayload.encode( )
		try:
			pass
		except Exception as e:
			message = bytes(thePayload)
		
		# print(sys.stderr, 'sending "%s"' % message)
		# print('sending "%s"' % message)
		sock.sendall(message)

		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			# print(sys.stderr, 'received "%s"' % data)
			# print('received "%s"' % str(data,'utf-8'))
			# ********************************************************************
			# print('received "%s"' % str(data))

	finally:
		sock.close()

def injectCode(string,st,code):
	newString = str(string[0:st])
	newString += str(code)
	newString += str(string[st:])
	return newString

def extractCode(string,st,cnt):
	newString = str(string[0:st])
	tmp = str(string[st:])
	# print(len(tmp))
	code = ''
	i = 0
	while i < cnt:
		code += tmp[0:1]
		tmp = tmp[1:]
		i += 1

	# print(len(tmp))
	newString += str(tmp)
	return {'code': code, 'payload': newString}

def genKeyPart(cnt):
	b64 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/+'
	result = ''
	i = 0
	while i < cnt:
		result += str(b64[randint(0, len(b64)-1)])
		i += 1
	return result

def seasoning():
	global salt
	result = ''
	for slt in salt:
		result += str(slt['value'])
	return result
salt.append({'start': 75, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 12, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 15, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 45, 'count': 8, 'value': genKeyPart(8)})

salt.append({'start': 175, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 111, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 115, 'count': 8, 'value': genKeyPart(8)})
salt.append({'start': 130, 'count': 8, 'value': genKeyPart(8)})


salt.append({'start': 203, 'count': 16, 'value': genKeyPart(16)})
salt.append({'start': 210, 'count': 16, 'value': genKeyPart(16)})
salt.append({'start': 215, 'count': 16, 'value': genKeyPart(16)})
salt.append({'start': 225, 'count': 16, 'value': genKeyPart(16)})

def action():
	global salt
	global encryptionKeyBase
	global passGet
	# countries_from_adobe_web_form.json
	if _.switches.isActive('Auto'):
		theKey = ''
		theFile = ''
		if _.switches.isActive('Table'):
			theFile = _.switches.value('Table')

		if _.switches.isActive('File'):
			theFile = _.switches.value('File')

		if _.switches.isActive('Encrypt'):
			encryptionKeyBase = genUUID()
			theKey = encryptionKeyBase
		# print(_.switches.value('Secure'))
		if passGet == False:
			securePass = _.switches.value('Secure')
		else:
			securePass = passGet
		auto = {
		
		'isTable': _.switches.isActive('Table'),
		'isFile': _.switches.isActive('File'),
		'isMessage': _.switches.isActive('Message'),
		
		'theFile': theFile,

		'isEncrypted': _.switches.isActive('Encrypt'),
		'encryptionKey': theKey,
		'isUnhackable': _.switches.isActive('Secure'),

		'secureKey': securePass,

		'exitAfter': True,
		
		}

		serverFile = 'server_auto.json'
		thisID = genUUID()
		textFilePath = _v.myTemp + _v.slash + serverFile
		textFilePath2 = _v.myTemp + _v.slash + thisID
		_.saveTable(auto,serverFile,False,False,False)
		os.system('base64 -e ' + textFilePath + ' ' + textFilePath2)
		test = _.getTable(serverFile,False,False)
		theData = _.getText(textFilePath)
		os.remove(textFilePath2)
		theData = _str.replaceAll(theData,'\n\n','\n')
		theData = str(theData)
		# print(theData)
		_.switches.fieldSet('Auto','value',False)
		# print(theData)
		autoPayload = encryptMessage(theData)
		# print(autoPayload)
		# print(autoPayload)

		# print('"{}"'.format(autoPayload))

		for slt in salt:
			autoPayload = injectCode(autoPayload,slt['start'],slt['value'])
		

		# print(seasoning())
		# print(newKey())
		send(autoPayload)
		# sys.exit()
		time.sleep(1)
		_.switches.fieldSet('Auto','value',True)

	thePayload = ''
	if _.switches.isActive('Message'):
		thePayload = _.ci2(_.switches.value('Message'))
	elif _.switches.isActive('Table'):
		tablePath = _v.myTables + _v.slash + _.ci2(_.switches.value('Table'))
		theTable = _.getText(tablePath)
		# print(len(theTable))
		# sys.exit()
		for line in theTable:
			thePayload += line
	elif _.switches.isActive('File'):
		thisID = genUUID()
		os.system('base64 -e ' + _.switches.value('File') + ' ' + thisID)
		theTable = _.getText(thisID)
		for line in theTable:
			thePayload += line
		os.remove(thisID)
		# with open(_.switches.value('File'), 'rb') as file:
		#     encoded_string = base64.b64encode(file.read())
		# thePayload = str(encoded_string,'utf-8')
	else:
		thePayload = 'Test message'

	if _.switches.isActive('Encrypt'):
		# print(thePayload)
		# sys.exit()
		thePayload = encryptMessage(thePayload)




	try:
		send(thePayload)
	except Exception as e:
		print('Error Sending')



passGet = False
########################################################################################
if __name__ == '__main__':
	action()






