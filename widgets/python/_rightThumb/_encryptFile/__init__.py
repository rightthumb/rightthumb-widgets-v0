# from ctypes import pythonapi

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# PyObject_GetBuffer = pythonapi.PyObject_GetBuffer


import os
import base64

try:
	from Crypto.Cipher import Blowfish
except Exception as e:
	pass
	# raise e

import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._md5 as _md5
import uuid

# from struct import pack



# import os
from Crypto.Cipher import _Blowfish
from struct import pack


# def encrypt(infilepath, outfilepath, password=False):
#     """ Encrypt the specified file with the specified
#        key and output to the chosen output file."""

#     key = genPassword( password )
#     size = os.path.getsize(infilepath)
#     infile = open(infilepath, 'rb')
#     outfile = open(outfilepath, 'wb')
#     data = infile.read()
#     infile.close()

#     if size % 8 > 0:  # Add padding if size if not divisible by 8
#         extra = 8-(size % 8)
#         padding = [0]*extra
#         padding = pack('b'*extra, *padding)
#         data += padding

#     revdata = reversebytes(data)
#     encrypted_data = encryptbytes(revdata, key)
#     finaldata = reversebytes(encrypted_data)
#     outfile.write(finaldata)
#     outfile.close()


# def encryptbytes(data, key):

#     cipher = _Blowfish.new(key, _Blowfish.MODE_ECB)
#     return cipher.encrypt(data)


# def decrypt(infilepath, outfilepath, password):
#     key = genPassword( password )
#     infile = open(infilepath, 'rb')
#     outfile = open(outfilepath, 'wb')
#     data = infile.read()
#     infile.close()

#     revdata = reversebytes(data)
#     decrypted_data = decryptbytes(revdata, key)
#     finaldata = reversebytes(decrypted_data)

#     end = len(finaldata) - 1
#     while str(finaldata[end]).encode('hex') == '00':
#         end -= 1

#     finaldata = finaldata[0:end]

#     outfile.write(finaldata)
#     outfile.close()


# def decryptbytes(data, key):

#     cipher = _Blowfish.new(key, _Blowfish.MODE_ECB)
#     return cipher.decrypt(data)


# def reversebytes(data):
#     return bytes(data)
#     # """ Takes data and reverses byte order to fit
#     # blowfish-compat format. For example, using
#     # reversebytes('12345678') will return 43218765."""
#  #    data_size = 0
#  #    for n in data:
#  #        data_size += 1

#  #    reversedbytes = bytearray()
#  #    i = 0
#  #    for x in range(0, roundUp( data_size/4 ) ):
#  #        try:
#  #            a = (data[i:i+4])
#  #            i += 4
#  #            z = 0

#  #            n0 = a[z]
#  #            n1 = a[z+1]
#  #            n2 = a[z+2]
#  #            n3 = a[z+3]
#  #            reversedbytes.append(n3)
#  #            reversedbytes.append(n2)
#  #            reversedbytes.append(n1)
#  #            reversedbytes.append(n0)
#  #        except Exception as e:
#  #            pass
#  #    # for row in dir(reversedbytes):
#  #    #     print( row )
#  #    # sys.exit()
#  #    # return reversedbytes.hex()
#  #    return memoryview(reversedbytes)
#  #    # return buffer(reversedbytes)


### with open(fname, "rb") as f:
###     for chunk in iter(lambda: f.read(4096), b""):
###         hash_md5.update(chunk)
### return hash_md5.hexdigest()

		
# def roundUp( number ):
#     temp = str( number )
#     if '.' in temp:
#         tempX = int( temp.split('.')[0] ) + 1
#         number = tempX
#     return number

# '''
# ############# USES #############
# infilepath = 'input.txt'
# outfilepath = 'output.txt'
# key = "mykey" 
# encrypt(infilepath, outfilepath, key)
# decrypt(infilepath, outfilepath, key)
# '''


###################################################################################




def genUUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	return string

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


def decrypt2( filenameIn, filenameOut, password ):
	
	# from Crypto.Cipher import Blowfish
	
	crypt_obj = Blowfish.new( password, Blowfish.MODE_ECB )
	# ciphertext = crypt_obj.encrypt(pad_string(plaintext))
	theFile = getFile( filenameIn )
	data = crypt_obj.decrypt(theFile)

	saveFile( filenameOut, data )


def decrypt( filenameIn, filenameOut, password=False ):
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)
	# ciphertext = crypt_obj.encrypt(pad_string(plaintext))
	theFile = getText( filenameIn, raw=True )
	decoded = base64.b64decode(theFile)
	decrypt = crypt_obj.decrypt(decoded)
	result = decrypt
	# print()
	# result = str(result,'utf-8')
	# result = result.decode('iso-8859-1','ignore')
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	thisID = genUUID()
	# result = _str.replaceAll(result,'\n\n','\n')
	saveText(result,thisID)
	os.system('base64 -d -n ' + thisID + ' ' + filenameOut)
	os.remove(thisID)


def encrypt( filenameIn, filenameOut, password=False ):
	crypt_obj = Blowfish.new(newKey(password), Blowfish.MODE_ECB)


	thisID = genUUID()
	# result = _str.replaceAll(result,'\n\n','\n')
	
	os.system('base64 -e ' + filenameIn + ' ' + thisID)
	theFile = getText( thisID, raw=True, clean=2 )
	os.remove(thisID)

	try:
		ciphertext = crypt_obj.encrypt(pad_string(theFile))
	except Exception as e:
		works = False
		space = ' '
		i = 0
		while works == False:
			try:
				ciphertext = crypt_obj.encrypt(pad_string(theFile) + space)
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
	saveText( thePayload, filenameOut )
	# except Exception as e:
	#     pass

	return thePayload

def getFile( theFile ):
	f=open( theFile, 'rb' )
	resultA=f.read()
	resultB=list(resultA)
	f.close()
	return resultA

def saveFile( theFile, data ):
	f=open( theFile, 'wb' )
	f.write(data)
	f.close()

def getText( theFile, raw=False, clean=False ):
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( '\\n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines

def saveText( rows, theFile, errors=True ):
	# print(type(rows))
	try:
		if type(rows) == bytes:
			rows = str(rows,'utf-8')
		f = open(theFile,'w', encoding='utf-8')
		# if type(rows) == str:

		# print(type(rows))
		# f.write(str(rows))
		# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
		# f.write(rows)
		# f.write(rows.encode("iso-8859-1", "replace"))

		# print(type(rows))
		if type(rows) == str:
			# print(rows)
			f.write(rows)
		else:
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						f.write(str(row) + '\n')
				else:
					f.write(str(row) + '\n')
		f.close()
	except Exception as e:
		if type(rows) == list:
			result = ''
			for i,row in enumerate(rows):
				# f.write(str(row) + os.linesep)
				if i == 0:
					if len(str(row)) > 0:
						result += str(row) + '\n'
				else:
					result += str(row) + '\n'

			rows = result
		open(theFile, 'wb').write(rows)
		if errors:
			print( 'Auto correction when saving text' )

