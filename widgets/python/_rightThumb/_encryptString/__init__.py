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

errors=False
errors=True
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

if errors and hasErrors:
	sys.exit()

def genPassword( password=False ):
	return newKey( password )

def newKey( password ):
	# min 150

	if not type(password) == bool:
		result = _v.cryptoKeyPad + str(password)
	else:
		if password:
			# 187 chars
			result = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID())
		else:
			result = _v.myCrypto()

	return _md5.md5( result )


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
def decrypt( data, password=False ):
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	decoded = base64.b64decode(data)
	decrypt = crypt_obj.decrypt(decoded)
	result = str(decrypt,'iso-8859-1')
	return result
	return _str.do('e',result,' ')


def encrypt( data, password=False ):
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	try:
		ciphertext = crypt_obj.encrypt(pad_string(str(data)))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(pad_string(str(data)) + space)
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
# 	data = open(  path , 'rb'  ).read()
# 	encoded = base64.encodebytes(data)
# 	crypt_obj = Blowfish.new( md5(password) , Blowfish.MODE_ECB)

# 	try:
# 		ciphertext = crypt_obj.encrypt(pad_string(str(encoded)))
# 	except Exception as e:
# 		works = False
# 		space = ' '
# 		i = 0
# 		while works == False:
# 			try:
# 				ciphertext = crypt_obj.encrypt(pad_string(str(encoded)) + space)
# 				works = True
# 			except Exception as e:
# 				pass
# 			space += ' '
# 			if i == 10:
# 				works = True
# 			i += 1

# 	encoded = base64.encodebytes(ciphertext)
# 	for x in dir(base64):
# 		if 'code' in x:
# 			print(x)
# 	# thePayload = str(result,'iso-8859-1')
# 	save( encoded, savePath )
# 	return None




# def save( data, path ):
# 	with open(  path   ,  'wb'  ) as fh:
# 		fh.write( data )
# 		# fh.write(base64.decodebytes(encoded))


# def decryptBin( password, path, savePath ):
# 	data = open(  path , 'rb'  ).read()

# 	decoded = base64.decodebytes(data)
# 	# decoded = base64.b64decode(data)

# 	what = decoded
# 	crypt_obj = Blowfish.new( md5(password)  , Blowfish.MODE_ECB)
# 	decrypt = crypt_obj.decrypt(what)

# 	# decoded = base64.b64decode(decrypt)
# 	decoded = base64.decodebytes(decrypt)

# 	what = decoded
# 	save( what, savePath )
# 	return None

p=genPassword

