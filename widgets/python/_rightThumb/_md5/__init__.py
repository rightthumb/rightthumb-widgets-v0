# md5

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# import _rightThumb._md5 as _md5
import os
import sys
import hashlib


def md5File(fname):
	# return ''
	if os.path.isfile(fname):
		# print(fname)
		hashData = hashlib.md5()
		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hashData.update(chunk)
		return hashData.hexdigest()
	else:
		print('Error: md5 no file')
		sys.exit()

def sha256File(fname):
	# return ''
	if os.path.isfile(fname):
		# print(fname)
		hashData = hashlib.sha256()
		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hashData.update(chunk)
		return hashData.hexdigest()
	else:
		print('Error: md5 no file')
		sys.exit()


def file( fname, h='md5' ):
	# return ''
	if os.path.isfile(fname):
		hashes = [
					'md5',
					'sha1',
					'sha224',
					'sha256',
					'sha384',
					'sha512',
					'sha3_224',
					'sha3_256',
					'sha3_384',
					'sha3_512',
		]
		if not h in hashes:
			print( 'Error: hash type not valid' )
			print( '\t Try:', ' , '.join( hashes ) )
			sys.exit()
		if h == 'md5':
			hashData = hashlib.md5()
		if h == 'sha1':
			hashData = hashlib.sha1()
		if h == 'sha224':
			hashData = hashlib.sha224()
		if h == 'sha256':
			hashData = hashlib.sha256()
		if h == 'sha384':
			hashData = hashlib.sha384()
		if h == 'sha3_224':
			hashData = hashlib.sha3_224()
		if h == 'sha3_256':
			hashData = hashlib.sha3_256()
		if h == 'sha3_384':
			hashData = hashlib.sha3_384()
		if h == 'sha3_512':
			hashData = hashlib.sha3_512()
		if h == 'sha512':
			hashData = hashlib.sha512()


		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hashData.update(chunk)
		return hashData.hexdigest()
	else:
		print('Error: not a file')
		sys.exit()


def string( chunk, h='md5' ):
	chunk=str(chunk)
	hashes = [
				'md5',
				'sha1',
				'sha224',
				'sha256',
				'sha384',
				'sha512',
				'sha3_224',
				'sha3_256',
				'sha3_384',
				'sha3_512',
	]
	if not h in hashes:
		print( 'Error: hash type not valid' )
		print( '\t Try:', ' , '.join( hashes ) )
		sys.exit()
	if h == 'md5':
		hashData = hashlib.md5()
	if h == 'sha1':
		hashData = hashlib.sha1()
	if h == 'sha224':
		hashData = hashlib.sha224()
	if h == 'sha256':
		hashData = hashlib.sha256()
	if h == 'sha384':
		hashData = hashlib.sha384()
	if h == 'sha3_224':
		hashData = hashlib.sha3_224()
	if h == 'sha3_256':
		hashData = hashlib.sha3_256()
	if h == 'sha3_384':
		hashData = hashlib.sha3_384()
	if h == 'sha3_512':
		hashData = hashlib.sha3_512()
	if h == 'sha512':
		hashData = hashlib.sha512()

	pass
	hashData.update(bytes(chunk, 'utf-8'))
	return hashData.hexdigest()



def bin( data, h='md5' ):
	
	hashes = [
				'md5',
				'sha1',
				'sha224',
				'sha256',
				'sha384',
				'sha512',
				'sha3_224',
				'sha3_256',
				'sha3_384',
				'sha3_512',
	]
	if not h in hashes:
		print( 'Error: hash type not valid' )
		print( '\t Try:', ' , '.join( hashes ) )
		sys.exit()
	if h == 'md5':
		hashData = hashlib.md5()
	if h == 'sha1':
		hashData = hashlib.sha1()
	if h == 'sha224':
		hashData = hashlib.sha224()
	if h == 'sha256':
		hashData = hashlib.sha256()
	if h == 'sha384':
		hashData = hashlib.sha384()
	if h == 'sha3_224':
		hashData = hashlib.sha3_224()
	if h == 'sha3_256':
		hashData = hashlib.sha3_256()
	if h == 'sha3_384':
		hashData = hashlib.sha3_384()
	if h == 'sha3_512':
		hashData = hashlib.sha3_512()
	if h == 'sha512':
		hashData = hashlib.sha512()

	pass
	hashData.update(data)
	return hashData.hexdigest()


# md5
# sha1
# sha224
# sha256
# sha384
# sha3_224
# sha3_256
# sha3_384
# sha3_512
# sha512
# shake_128
# shake_256



def md5Bin( data ):
	hashData = hashlib.md5()
	hashData.update(data)
	return hashData.hexdigest()

def md5(chunk):
	# try:
	#     pass
	#     chunk = line.encode('UTF-8').decode('latin-1')
	# except Exception as e:
	#     pass
	hashData = hashlib.md5()
	hashData.update(bytes(chunk, 'utf-8'))
	return hashData.hexdigest()
			
def md52GUID(string,brackets=True):
	string = string.upper()
	result = ''
	result += str(string[0:8])
	result += str('-')
	result += str(string[8:12])
	result += str('-')
	result += str(string[12:16])
	result += str('-')
	result += str(string[16:20])
	result += str('-')
	result += str(string[20:32])
	if brackets == True:
		result = '{' + result + '}'
	return result

# set machineID={%machineID:~0,8%-%machineID:~8,4%-%machineID:~12,4%-%machineID:~16,4%-%machineID:~20,12%}

