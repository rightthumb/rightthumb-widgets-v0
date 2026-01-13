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

import sys
import os

import _pickle as cPickle
import bz2
import math
import base64
from Crypto.Cipher import Blowfish
from tkinter import * 
import platform
import shutil
from struct import pack
import hashlib


xyz = None
maxPassword = 30

def md5Gen(chunk):
	hashData = hashlib.md5()
	hashData.update(bytes(chunk, 'utf-8'))
	return hashData.hexdigest()

def ask( label=None ):
	global xyz
	xyz = None
	def show():
		global xyz
		xyz = password.get()
		print( '\t\t code:', label )

	app = Tk()   
	password = StringVar() #Password variable
	passEntry = Entry(app, textvariable=password, show='*').pack()
	submit = Button(app, text='Show Console',command=show).pack()
	app.mainloop() 
	return xyz

def password():
	global maxPassword
	global xyz
	a = ask('a')
	xyz = None
	b = ask('b')
	xyz = None
	c = ask('c')
	xyz = None


	md5 = md5Gen( b+c+a )

	while not len(md5) >= maxPassword:
		md5 += md5Gen(md5)

	word = ''
	for i,x in enumerate(md5):
		if i < maxPassword:
			word += x
	return word
	


def compressed_pickle( data, path ):
	with bz2.BZ2File( path , 'w' ) as f:
		cPickle.dump( data, f )


def decompress_pickle(file):
	data = bz2.BZ2File( file, 'rb' )
	data = cPickle.load( data )
	return data



	

def encrypt( data ):
	key = password()

	def pad_string( string ):
		INPUT_SIZE = 8
		new_str = string
		pad_chars = INPUT_SIZE - (len(string) % INPUT_SIZE)

		if pad_chars != 0:
			for x in range(pad_chars):
				new_str += " "
			

		return new_str

	crypt_obj = Blowfish.new( key, Blowfish.MODE_ECB )
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

	# result = base64.b64encode(ciphertext)
	# thePayload = str(result,'iso-8859-1')

	return ciphertext


def decrypt( data ):
	key = password()
	crypt_obj = Blowfish.new(key, Blowfish.MODE_ECB)
	# decoded = base64.b64decode(data)
	# decrypt = crypt_obj.decrypt(decoded)
	decrypt = crypt_obj.decrypt(data)
	result = str(decrypt,'iso-8859-1')
	return result

def encrypt2( fileIN, fileOUT ):
	import pyAesCrypt
	from os import stat, remove
	key = password()

	# encryption/decryption buffer size - 64K
	bufferSize = 64 * 1024

	# encrypt
	with open(fileIN, "rb") as fIn:
		with open(fileOUT, "wb") as fOut:
			pyAesCrypt.encryptStream(fIn, fOut, key, bufferSize)

def decrypt2( fileIN, fileOUT ):
	import pyAesCrypt
	from os import stat
	key = password()
	# get encrypted file size
	encFileSize = stat(fileIN).st_size
	bufferSize = 64 * 1024
	# decrypt
	with open(fileIN, "rb") as fIn:
		try:
			with open(fileOUT, "wb") as fOut:
				# decrypt file stream
				pyAesCrypt.decryptStream(fIn, fOut, key, bufferSize, encFileSize)
		except ValueError:
			try:
				os.remove(fileOUT)
			except Exception as e:
				pass
			# remove output file on error

########################################################################################

def getText( theFile ):
	f = open(theFile, 'r', encoding='utf-8')
	lines = f.readlines()
	f.close()
	txt = ''.join( lines )
	return txt

def saveText( data, theFile ):
	with open(theFile, 'wb') as file:
		file.write(data.encode('ascii'))

	# f = open(theFile,'w', encoding='utf-8')
	# f.write(data)
	# f.close()

def action():
	arg = list( sys.argv )
	i = 0
	try:
		crypt = arg[i+1].lower()
	except Exception as e:
		crypt = '?'
	try:
		file = arg[i+2]
		save = arg[i+3]
	except Exception as e:
		crypt = '?'

	if crypt == '?':
		print( '' )
		print( '\tExample:' )
		print( '\t\tpython3 appServerHelper.py de appServer.unix appServer.unix.py' )
		print( '\t\tpython3 appServerHelper.py en appServer.unix.py appServer.unix' )
		print( '' )
		print( '\t\t'+"%"+'py'+"%"+' appServerHelper.py de appServer.win appServer.win.py' )
		print( '\t\t'+"%"+'py'+"%"+' appServerHelper.py en appServer.win.py appServer.win' )
		print( '' )
		print( arg )

	if crypt == 'en':
		# compressed_pickle( encrypt( getText( file ) ), save )
		encrypt2( file, save )

	if crypt == 'de':
		decrypt2( file, save )
		# saveText( decrypt( decompress_pickle( file ) ), save )
		print( '' )
		print( '\tNext Command:' )
		if 'win' in file:
			print( "\t\t%"+'py'+"%"+' appServer.win.py -crypt de  -restore  -location server -f batch bookmarks tables javascript sublime.txt windows' )
		elif 'unix' in file:
			print( '\t\tpython3 appServer.unix.py -crypt de  -restore  -location server -f bash bookmarks tables javascript sublime.txt unix' )





########################################################################################
if __name__ == '__main__':
	action()