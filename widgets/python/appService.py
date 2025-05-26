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
import _pickle as cPickle
import bz2


import math
import _rightThumb._nID as _nID
_nID.mini.safe = True
import _rightThumb._md5 as _md5

import base64
from Crypto.Cipher import Blowfish

# import getpass_ak

# from Tkinter import Entry, Tk
from tkinter import * 

import platform

from ftplib import FTP

import shutil

from struct import pack


"""
class Ask():
	def __init__(self):
		self.result = None
		return self.run()
		# self.root = Tkinter.Tk()
		# button = Tkinter.Button(self.root, text = 'root quit', command=self.quit)
		# button.pack()
		# self.root.mainloop()
	def run(self):
		self.root = Tk()   
		self.password = StringVar() #Password variable
		self.enter_password = Entry(self.root, textvariable=self.password, show='*').pack()
		self.submit = Button(self.root, text='submit',command=self.submit).pack()
		self.root.mainloop()
		return self.result

	def submit(self):
		self.result = self.password.get()
		self.root.destroy
		return self.result
"""


def ask( label=None ):
	global xyz
	xyz = None
	def show():
		global xyz
		xyz = password.get()
		_.colorThis( [ '\t\t code:', label ], 'green' )

	app = Tk()   
	password = StringVar() #Password variable
	passEntry = Entry(app, textvariable=password, show='*').pack()
	submit = Button(app, text='Show Console',command=show).pack()
	app.mainloop() 
	return xyz

def password2():
	global thePassword
	if not thePassword is None:
		return thePassword
	global maxPassword
	global defaultNumber
	global xyz

	



	if defaultNumber is None:
		n = int( ask('n') )
		xyz = None
		defaultNumber = n

	else:
		n = defaultNumber


	a = ask('a')
	xyz = None
	b = ask('b')
	xyz = None
	print()

	p = str(n)+b+a

	_nID.mini.password( p )
	x = _nID.mini.gen( n )

	md5 = _md5.md5(x)

	while not len(md5) >= maxPassword:
		md5 += _md5.md5(md5)

	word = ''
	for i,x in enumerate(md5):
		if i < maxPassword:
			word += x
	thePassword = word
	return word



def compressed_pickle( data, path ):
	with bz2.BZ2File( path , 'w' ) as f:
		cPickle.dump( data, f )


def decompress_pickle(file):
	data = bz2.BZ2File( file, 'rb' )
	data = cPickle.load( data )
	return data



def encrypt( data ):
	global password
	key = password

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
	global password
	key = password
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


def switchV( switch ):
	global switches
	
	isPipe = False
	sw = {}

	for swX in switches.keys():
		for x in switches[swX].split(','):
			if x == '|' and switch == swX:
				isPipe = True
			elif not x == '|':
				sw[x] = swX
	result = {}
	active = None
	for x in sys.argv:
		if x in sw:
			active = sw[x]
			result[ sw[x] ] = []
		elif not active is None:
			result[active].append( x )

	if isPipe and not switch in result:
		if not sys.stdin.isatty():
			pipe = sys.stdin.readlines()
			if pipe:
				result[switch] = pipe



	if switch in result:
		return result[switch]
	else:
		return []


def switchA( switch ):
	global switches

	isPipe = False    
	sw = {}


	for swX in switches.keys():
		for x in switches[swX].split(','):
			if x == '|' and switch == swX:
				isPipe = True
			elif not x == '|':
				sw[x] = swX
	result = {}
	active = None
	for x in sys.argv:
		if x in sw:
			active = sw[x]
			result[ sw[x] ] = []
		elif not active is None:
			result[active].append( x )

	if isPipe and not switch in result:
		if not sys.stdin.isatty():
			pipe = sys.stdin.readlines()
			if pipe:
				result[switch] = pipe

	if switch in result:
		return True
	else:
		return False


def slash():
	global theSLASH
	if not theSLASH is None:
		return theSLASH
	if platform.system() == 'Windows':
		theSLASH = _v.slash
		return _v.slash
	else:
		theSLASH = '/'
		return '/'
	

def processAPPS():
	for row in switchV('APPS'):
		print(row)
		clean = []
		for x in row:
			if x in ':\\/0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-.':
				clean.append(x)
		row = ''.join(clean)
		if row:
			print('HERE')
			app = row.replace('.py','')
			if slash() in row:
				parts  = row.split(slash())
				parts.reverse()
				app = parts[0].replace('.py','')




			print( 'Processing:', app, row )


			spec = importlib.util.spec_from_file_location(app, row)
			imp = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(imp)
			# print( _v.python['crypt']['en'] )
			file = _v.python['crypt']['en'] + app + '.en'
			# compressed_pickle( imp, file )
			# compressed_pickle( encrypt(file), file )
			# dill.dump( imp, 'test.txt' )
			# dill.dump( 'test.txt', imp )
			dmp = dill.dumps(imp)
			# print( dmp )
			test = dill.loads( dmp )
			test.action()
			# imp.fieldSet( switchName, switchField, switchValue, theFocus=False )
			# imp.fieldSet( 'Ago', 'active', True )
			# imp.fieldSet( 'Ago', 'value', '1d' )
			# imp.fieldSet( 'Ago', 'values', ['1d'] )
			# imp.action()


def action():
	load()
	# print( switchA('Files') )
	# print( switchV('Files') )
	# sys.exit()
	global password

	# print( sys.argv )
	if switchA('APPS'):
		processAPPS()



def load():
	global switches
	global password
	password = '{FBEA7897-3186-471C-86A5-D465AD4BDAEC}'
	switches = {
					'APPS': '-A,-APP,-APPS,|',
					'LOAD': '-L,-LOAD',
	}


switches = None
password = None
theSLASH = None
# import importlib
import importlib.util
import _rightThumb._vars as _v

import dill

########################################################################################
if __name__ == '__main__':
	action()






