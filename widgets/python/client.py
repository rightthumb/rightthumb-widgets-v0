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

import socket
import sys

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._md5 as _md5

from Crypto.Cipher import Blowfish
import base64

import uuid
import os

# import pyicu as icu
# import icu

# import magic

# import cchardet


_.switches.register('IP', '-ip','192.168.1.10')
_.switches.register('Port', '-port','10000')
_.switches.register('Message', '-message','this is a test message')
_.switches.register('Table', '-table','tableName.json')
_.switches.register('File', '-file','file.zip')
_.switches.register('Decrypt', '-decrypt')
_.switches.register('Auto', '-auto')
_.switches.register('Secure', '-secure,-unhackable','password')

_.appInfo=    {
	'file': 'client.py',
	'description': 'Get data that is pushed',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -auto')
_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -table table.json')
_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -decrypt')
_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -table table.json -decrypt')
_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -file out.zip -decrypt')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p client -ip 192.168.1.10 -port 10000 -auto')

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
auto = {}
salt = []

# def convert_encoding(data, new_coding = 'UTF-8'):
# def convert_encoding(data, new_coding = 'iso-8859-1'):
#   if not type(data) == str:
#       data = str(data,'iso-8859-1')
#   # data = data.encode().decode()
#   print(cchardet.detect(data))
#   encoding = cchardet.detect(data)['encoding']
#   if new_coding.upper() != encoding.upper():
#     data = data.decode(encoding, data).encode(new_coding)

#   return data
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
	global auto
	keyInput = ''
	if _.switches.isActive('Auto') and not _.switches.value('Auto'):
		theFile = ''
		if _.switches.isActive('Table'):
			theFile = _.switches.value('Table')

		if _.switches.isActive('File'):
			theFile = _.switches.value('File')
		# keyInput = str(encryptionKey) + str(theFile) + str(auto['encryptionKey'])
		keyInput = str(encryptionKey) + str(auto['encryptionKey'])
		md5 = _md5.md5(keyInput)
		encryptionKeyNew = _md5.md52GUID(md5,True)
	elif _.switches.isActive('Auto') and _.switches.value('Auto'):
		keyInput = encryptionKey + seasoning()
		# print(keyInput)
		md5 = _md5.md5(keyInput)
		encryptionKeyNew = _md5.md52GUID(md5,True)
		# encryptionKeyNew = encryptionKey
	else:
		encryptionKeyNew = encryptionKey
	# print(keyInput)
	# print(encryptionKeyNew)
	return encryptionKeyNew

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

salt.append({'start': 75, 'count': 8, 'value': ''})
salt.append({'start': 12, 'count': 8, 'value': ''})
salt.append({'start': 15, 'count': 8, 'value': ''})
salt.append({'start': 45, 'count': 8, 'value': ''})

salt.append({'start': 175, 'count': 8, 'value': ''})
salt.append({'start': 111, 'count': 8, 'value': ''})
salt.append({'start': 115, 'count': 8, 'value': ''})
salt.append({'start': 130, 'count': 8, 'value': ''})


salt.append({'start': 203, 'count': 16, 'value': ''})
salt.append({'start': 210, 'count': 16, 'value': ''})
salt.append({'start': 215, 'count': 16, 'value': ''})
salt.append({'start': 225, 'count': 16, 'value': ''})
loop = False
errorCount = 0
def unhack():
	global loop
	global errorCount
	
	# _.switches.printStatus()
	if _.switches.isActive('Secure'):
		pu_File = _.switches.value('File')
		pu_Secure = _.switches.value('Secure')
		# print(pu_Secure)
		# print(pu_Secure)
		# print(pu_Secure)
		# pu_IP = _.switches.value('IP')
		# pu_Port = _.switches.value('Port')
		# if _.switches.isActive('Decrypt'):
		#     pu_Decrypt = True
		# else:
		#     pu_Decrypt = False
		if _.switches.isActive('Auto'):
			pu_Auto = True
		else:
			pu_Auto = False
		import unhackable
		_.switches.process()
		# print('pre:',,_.switches.value('Secure'))
		_.switches.fieldSet('File','active',True)
		_.switches.fieldSet('File','value',pu_File)

		_.switches.fieldSet('Password','active',True)
		_.switches.fieldSet('Password','value',str(pu_Secure))
		unhackable.baseKey = pu_Secure
		unhackable.imported = True
		try:
			unhackable.file()
			errorCount = 0
		except Exception as e:
			errorCount += 1
			print('Error:',errorCount)
			# unhack()


		if pu_Auto:
			loop = True
			_.switches.process()
		# print('Error:',errorCount)
		if errorCount > 0:
			unhack()

def action():
	global auto
	global salt
	global loop
	shouldAsk = True
	encryptionKeyOriginal = encryptionKey
	# print()
	# print()
	def isEven(x):
		if x & 1:
		return False
		else:
		return True


	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the address given on the command line
	server_address = (_.switches.value('IP'), int(_.switches.value('Port')))
	sock.bind(server_address)
	# print(sys.stderr, 'starting up on %s port %s' % sock.getsockname())
	print('starting up on %s port %s' % sock.getsockname())
	sock.listen(1)


	if _.switches.isActive('Auto'):
		_.switches.fieldSet('Auto','value',True)


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
				if _.switches.isActive('Table'):
					if isEven(i):
						_.updateLine('-')
					else:
						_.updateLine('|')
				else:
					pass
					# print('received "%s"' % data)
				# print(sys.stderr, 'received "%s"' % data)
				

				# result += str(data,'utf-8')
				# data2 = str(data)
				# result += data2.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf8')
				# result += convert_encoding(data)
				result += str(data,'iso-8859-1')

				if data:
					# pass
					connection.sendall(data)
				else:
					# print(result)
					# print('done')
					# print(_.switches.isActive('Auto'),_.switches.value('Auto'),type(_.switches.isActive('Auto')),type(_.switches.value('Auto')))
					# print(result)
					###########################################################################
					###########################################################################
					if _.switches.isActive('Auto') == True and _.switches.value('Auto') == True:
						# print('activated')
						

						string = result
						i = len(salt)
						while i > 0:
							i -= 1
							exData = extractCode(string,salt[i]['start'],salt[i]['count'])
							salt[i]['value'] = exData['code']
							string = exData['payload']
						result = string
						# print('seasoning:',seasoning())

						shouldAsk = False
						clientFile = 'client_auto.json'
						crypt_obj = Blowfish.new(newKey(), Blowfish.MODE_ECB)

						# sys.exit()
						# print(seasoning())
						# print(newKey())
						# sys.exit()



						# print('"{}"'.format(string))
						# decoded = base64.b64decode(string)
						# print(result)

						decoded = base64.b64decode(result)

						decrypt = crypt_obj.decrypt(decoded)
						# print(str(decoded,'iso-8859-1'))
						# resultNew = str(decrypt,'iso-8859-1')
						resultNew = str(decrypt,'iso-8859-1')
						# sys.exit()



						
						# print(resultNew)
						# print(resultNew)
						# resultNew = str(decrypt,'iso-8859-1')
						# print(resultNew)
						# print(resultNew)
						# thisID = genUUID()
						# textFilePath = _v.myTemp + '\\' + clientFile
						# textFilePath2 = _v.myTemp + '\\' + thisID
						# print(textFilePath)
						# print(textFilePath2)
						# print(len(resultNew))
						# print(type(resultNew))
						# _.saveText(str(resultNew),textFilePath)
						# pause = input('pause')
						# newString = ''
						# for rn in resultNew:
						#     print(str(rn,'iso-8859-1'))
						#     newString += str(rn,'iso-8859-1')
						# _.saveText(newString,textFilePath2)
						# result = _str.replaceAll(result,'\n\n','\n')
						# _.saveText(result,thisID)
						# os.system('base64 -d -n ' + textFilePath2 + ' ' + textFilePath)
						# os.remove(textFilePath2)
						import ast
						# auto = ast.literal_eval(auto2)
						# auto = eval(resultNew)
						# auto2 = _.getTable(textFilePath,False,True)
						# auto = eval(str(auto2))
						try:
							auto2 = ast.literal_eval(resultNew)
							auto2[0] = auto2[0].replace('false','False')
							auto2[0] = auto2[0].replace('true','True')
							auto = eval(str(auto2[0]))
						except Exception as e:
							print('Error')
							sys.exit()
						# print(auto)
						# print(type(auto))
						# print(len(auto))
						# print(auto[0])
						# print(type(auto[0]))
						# print(type(auto[0]['encryptionKey']))
						# _.switches.printStatus()
						# print(auto)
						# print(auto['isTable'],type(auto['isTable']))
						# print(0,_.switches.isActive('Table'))
						
						
						# _.switches.fieldSet('Auto','active',False)
						# _.switches.fieldSet('Auto','value',False)

						if auto['isMessage']:
							_.switches.fieldSet('Message','active',True)
							# print('isMessage True')
						else:
							_.switches.fieldSet('Message','active',False)
							# print('isMessage False')

						if auto['isTable']:
							_.switches.fieldSet('Table','active',True)
							_.switches.fieldSet('Table','value',str(auto['theFile']))
							# print('isTable True')
						else:
							_.switches.fieldSet('Table','active',False)
							_.switches.fieldSet('Table','value',None)
							# print('isTable False')

						if auto['isFile']:
							_.switches.fieldSet('File','active',True)
							_.switches.fieldSet('File','value',str(auto['theFile']))
							# print('isFile True')
						else:
							_.switches.fieldSet('File','active',False)
							_.switches.fieldSet('File','value',None)
							# print('isFile False')

						if auto['isEncrypted']:
							_.switches.fieldSet('Decrypt','active',True)
							# print('isEncrypted True')
						else:
							_.switches.fieldSet('Decrypt','active',False)
							# print('isEncrypted False')

						if auto['isUnhackable']:
							_.switches.fieldSet('Secure','active',True)
							_.switches.fieldSet('Secure','value',str(auto['secureKey']))
							# print('isTable True')
						else:
							_.switches.fieldSet('Secure','active',False)
							_.switches.fieldSet('Secure','value',None)
						# print(_.switches.value('Secure'))
						# print(0,_.switches.isActive('Table'))
						# _.switches.printStatus()
						
						# print('works')
						# sys.exit()
					elif _.switches.isActive('Table'):
						if _.switches.isActive('Decrypt'):
							# plaintext = 'test'
							crypt_obj = Blowfish.new(newKey(), Blowfish.MODE_ECB)
							# ciphertext = crypt_obj.encrypt(pad_string(plaintext))
							decoded = base64.b64decode(result)
							decrypt = crypt_obj.decrypt(decoded)
							result = decrypt
						print()
						# result = str(result,'utf-8')
						# result = result.decode('iso-8859-1','ignore')
						try:
							result = str(result,'utf-8')
						except Exception as e:
							result = result.encode('utf-8')
						# print('File Received')
						_.saveText(result,_.switches.value('Table'))
						unhack()
						print('File Saved')
						# print(4)
						# sys.exit()
					elif _.switches.isActive('File'):
						# print('File Received')
						if _.switches.isActive('Decrypt'):
							# plaintext = 'test'
							crypt_obj = Blowfish.new(newKey(), Blowfish.MODE_ECB)
							# ciphertext = crypt_obj.encrypt(pad_string(plaintext))
							decoded = base64.b64decode(result)
							decrypt = crypt_obj.decrypt(decoded)
							result = decrypt
						print()
						# result = str(result,'utf-8')
						# result = result.decode('iso-8859-1','ignore')
						try:
							result = str(result,'utf-8')
						except Exception as e:
							try:
								result = str(result,'iso-8859-1')
							except Exception as e:
								result = result.encode('utf-8')
						if _.switches.isActive('Decrypt'):
							thisID = genUUID()
							result = _str.replaceAll(result,'\n\n','\n')
							_.saveText(result,thisID)
							os.system('base64 -d -n ' + thisID + ' ' + _.switches.value('File'))
							os.remove(thisID)

							# print(1)
						else:
							# print(2)
							_.saveText(result,_.switches.value('File'))
							# print(3)
						unhack()
						print('File Saved')


						# sys.exit()
						# if _.switches.isActive('Decrypt'):
						#     # plaintext = 'test'
						#     crypt_obj = Blowfish.new('{3DDED2AD-AFA6-58A3-3D7C-55D93A9AE84E}', Blowfish.MODE_ECB)
						#     # ciphertext = crypt_obj.encrypt(pad_string(plaintext))
						#     decoded = base64.b64decode(result)
						#     decrypt = crypt_obj.decrypt(decoded)
						#     result = decrypt
						# result = _str.removeAll(result,' ')
						# decoded = base64.b64decode(result)
						# result = decoded
						# with open(_.switches.value('File'), 'wb') as file:
						#     file.write(result)
					elif _.switches.isActive('Message'):
						print()
						print()
						print(result)
						print()
						print()
						if _.switches.isActive('Decrypt'):
							# plaintext = 'test'
							crypt_obj = Blowfish.new(newKey(), Blowfish.MODE_ECB)
							# ciphertext = crypt_obj.encrypt(pad_string(plaintext))
							# encoded = base64.b64encode(ciphertext)
							decoded = base64.b64decode(result)
							decrypt = crypt_obj.decrypt(decoded)
							print()
							print()
							print("Decrypted: " + str(decrypt,'iso-8859-1'))
							print()
							print()
					if _.switches.isActive('Auto') and _.switches.value('Auto'):
						_.switches.fieldSet('Auto','value',False)
					elif _.switches.isActive('Auto') and not _.switches.value('Auto'):
						_.switches.fieldSet('Auto','value',True)
						if not loop:
							sys.exit()
						pass
					# elif shouldAsk and False:
					#     _.switches.fieldSet('Auto','value',True)
					else:
						wait = input('Wait? (y)')
						if wait == 'n':
							sys.exit()
					# else:
					#     shouldAsk = True
					# sys.exit()
					break
		finally:
			# print('the end')
			connection.close()



########################################################################################
if __name__ == '__main__':
	action()





