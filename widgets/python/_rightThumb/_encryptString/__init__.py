import sys

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##




# import sys
# print(f"Using Python interpreter: {sys.executable}")
# import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
# print(f"Installed packages: {installed_packages_list}")

# sys.exit()

# from Crypto.Cipher import Blowfish







errors=True
errors=False
hasErrors=False
try:
	import base64
except Exception as e:
	hasErrors=True
	if errors: print(e);
	pass
try:
	from Crypto.Cipher import Blowfish
except Exception as e:
	hasErrors=True
	if errors: print(e);
	pass
try:
	import _rightThumb._vars as _v
except Exception as e:
	hasErrors=True
	if errors: print(e);
	pass
try:
	import _rightThumb._md5 as _md5
except Exception as e:
	hasErrors=True
	if errors: print(e);
	pass
try:
	import _rightThumb._string as _str
except Exception as e:
	hasErrors=True
	if errors: print(e);
	pass


# print(5552424)
if errors and hasErrors: sys.exit()



def genPassword( password=False ):
	return newKey( password )

def newKey( password ):
	# min 150
	if password == 456:
		result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID2())
		return _md5.md5( result ).encode('utf-8')

	if not type(password) == bool:
		result = _v.cryptoKeyPad + str(password)
	else:
		if password:
			# 187 chars
			result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID())
		else:
			result = _v.myCrypto()

	return _md5.md5( result ).encode('utf-8')

# def newKey( password ):
#     # min 150
# 	if password == 456:
# 		result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID2())
#     	return _md5.md5( result ).encode('utf-8')

#     if not type(password) == bool:
#         result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID2())
#     else:
#         if password:
#             # 187 chars
#             result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID())
#         else:
#             result = _v.myCrypto()

#     return _md5.md5( result ).encode('utf-8')



def pad_string( string ):
	INPUT_SIZE = 8
	new_str = string
	pad_chars = INPUT_SIZE - (len(string) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		

	return new_str



def decryptClean( data, password=False ):
	result = decrypt( data, password )
	# return result
	# return _str.cleanBE( result, ' ' )
	return _str.do('e',result,' ')

def myDecrypt():
	password   = decrypt(open(_v.vaultPath(), 'r').read(),456)
	# print(password)
	if myDe(password).strip() == '1998':
		return True
	else:
		return False



# Function to encrypt a string
def myPad(key, block_size):
	# Pad the key to make sure it is at least the minimum size and at most 56 bytes
	if len(key) < block_size:
		key += b'0' * (block_size - len(key))
	elif len(key) > 56:
		key = key[:56]
	return key

def myEn(plaintext, password):
	password = password.strip()
	from Crypto.Cipher import Blowfish
	from Crypto.Util.Padding import pad
	import base64

	# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
	key = myPad(password.encode(), 4)
	
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)
	iv = cipher.iv
	padded_text = pad(plaintext.encode(), Blowfish.block_size)
	encrypted = cipher.encrypt(padded_text)
	# Combine IV with the encrypted text and encode in base64
	encrypted_text = base64.b64encode(iv + encrypted).decode('utf-8')
	
	with open(_v.myDecrypt, 'w') as file:
		file.write(encrypted_text)
	# print(myDe(password))
	return encrypted_text



# Function to decrypt a string
def myDe(password):
	# print(password)
	password = password.strip()
	from Crypto.Cipher import Blowfish
	from Crypto.Util.Padding import unpad
	import base64

	encrypted_text = open(_v.myDecrypt, 'r').read()

	try:
		encrypted_data = base64.b64decode(encrypted_text)
		iv = encrypted_data[:Blowfish.block_size]
		encrypted_message = encrypted_data[Blowfish.block_size:]

		# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
		key = myPad(password.encode(), 4)

		# print(f"IV: {iv}")
		# print(f"Encrypted message: {encrypted_message}")
		# print(f"Key: {key}")
		
		cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
		decrypted_padded = cipher.decrypt(encrypted_message)
		decrypted = unpad(decrypted_padded, Blowfish.block_size).decode('utf-8')
		# print("Decryption successful")
		# print(decrypted)
		return decrypted
	except (ValueError, KeyError) as e:
		print(f'Decryption error: {e}')
		return "Decryption failed. Incorrect padding or invalid key."

def myEn2(plaintext, password):
	password = password.strip()
	from Crypto.Cipher import Blowfish
	from Crypto.Util.Padding import pad
	import base64

	# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
	key = myPad(password.encode(), 4)
	
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)
	iv = cipher.iv
	padded_text = pad(plaintext.encode(), Blowfish.block_size)
	encrypted = cipher.encrypt(padded_text)
	# Combine IV with the encrypted text and encode in base64
	encrypted_text = base64.b64encode(iv + encrypted).decode('utf-8')
	
	# with open(_v.myDecrypt, 'w') as file:
		# file.write(encrypted_text)
	
	return encrypted_text

def myDe2(text,password):
	password = password.strip()
	from Crypto.Cipher import Blowfish
	from Crypto.Util.Padding import unpad
	import base64

	encrypted_text = text

	try:
		encrypted_data = base64.b64decode(encrypted_text)
		iv = encrypted_data[:Blowfish.block_size]
		encrypted_message = encrypted_data[Blowfish.block_size:]

		# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
		key = myPad(password.encode(), 4)

		# print(f"IV: {iv}")
		# print(f"Encrypted message: {encrypted_message}")
		# print(f"Key: {key}")
		
		cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
		decrypted_padded = cipher.decrypt(encrypted_message)
		decrypted = unpad(decrypted_padded, Blowfish.block_size).decode('utf-8')
		# print("Decryption successful")
		# print(decrypted)
		return decrypted
	except (ValueError, KeyError) as e:
		print(f'Decryption error: {e}')
		return "Decryption failed. Incorrect padding or invalid key."
	
def decrypt( data, password=False ):
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	decoded = base64.b64decode(data)
	decrypt = crypt_obj.decrypt(decoded)
	result = str(decrypt,'iso-8859-1')
	return result
	return _str.do('e',result,' ')



def decryptU(data, password=False):
	from Crypto.Cipher import Blowfish
	from Crypto.Util.Padding import unpad
	import base64
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	decoded = base64.b64decode(data)
	decrypted = crypt_obj.decrypt(decoded)

	try:
		unpadded = unpad(decrypted, Blowfish.block_size)
	except ValueError as e:
		raise Exception(f"Decryption error: {e}")

	return unpadded.decode('utf-8', errors='ignore')


def encrypt( data, password=False ):
	data=str(data)
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	try:
		ciphertext = crypt_obj.encrypt(pad_string(data).encode('utf-8'))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(str(pad_string(data) + space).encode('utf-8'))
				works = True
			except Exception as e:
				pass
			space += ' '
			if i == 10:
				works = True
			i += 1

	result = base64.b64encode(ciphertext)
	thePayload = str(result,'iso-8859-1')

	return thePayload




def decrypt2( data, password=False ):
	crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)
	decoded = base64.b64decode(data)
	decrypt = crypt_obj.decrypt(decoded)
	result = str(decrypt,'iso-8859-1')
	return result

def encrypt2( data, password=False ):
	data=str(data)
	crypt_obj = Blowfish.new(password, Blowfish.MODE_ECB)
	try:
		ciphertext = crypt_obj.encrypt(pad_string(data).encode('utf-8'))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(str(pad_string(data) + space).encode('utf-8'))
				works = True
			except Exception as e:
				pass
			space += ' '
			if i == 10:
				works = True
			i += 1

	result = base64.b64encode(ciphertext)
	thePayload = str(result,'iso-8859-1')

	return thePayload




import hashlib
def md5(chunk):
	hash_md5 = hashlib.md5()
	hash_md5.update(bytes(chunk, 'utf-8'))
	return hash_md5.hexdigest()


def md5File(fname):
	import os, sys
	if os.path.isfile(fname):
		hash_md5 = hashlib.md5()
		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()
	else:
		print('MD5 Error: file not found')
		sys.exit()


# def encryptFile( password, path, savePath ):
#     data = open(  path , 'rb'  ).read()
#     encoded = base64.encodebytes(data)
#     crypt_obj = Blowfish.new( md5(password) , Blowfish.MODE_ECB)

#     try:
#         ciphertext = crypt_obj.encrypt(pad_string(str(encoded)))
#     except Exception as e:
#         works = False
#         space = ' '
#         i = 0
#         while works == False:
#             try:
#                 ciphertext = crypt_obj.encrypt(pad_string(str(encoded)) + space)
#                 works = True
#             except Exception as e:
#                 pass
#             space += ' '
#             if i == 10:
#                 works = True
#             i += 1

#     encoded = base64.encodebytes(ciphertext)
#     for x in dir(base64):
#         if 'code' in x:
#             print(x)
#     # thePayload = str(result,'iso-8859-1')
#     save( encoded, savePath )
#     return None




# def save( data, path ):
#     with open(  path   ,  'wb'  ) as fh:
#         fh.write( data )
#         # fh.write(base64.decodebytes(encoded))


# def decryptBin( password, path, savePath ):
#     data = open(  path , 'rb'  ).read()

#     decoded = base64.decodebytes(data)
#     # decoded = base64.b64decode(data)

#     what = decoded
#     crypt_obj = Blowfish.new( md5(password)  , Blowfish.MODE_ECB)
#     decrypt = crypt_obj.decrypt(what)

#     # decoded = base64.b64decode(decrypt)
#     decoded = base64.decodebytes(decrypt)

#     what = decoded
#     save( what, savePath )
#     return None

p=genPassword

