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

def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Crypt', '-crypt', 'en,de', isRequired=True )
	_.switches.register( 'RestoreOriginalPath', '-original,-restore' )
	_.switches.register( 'Location', '-location', 'local,server,srv' )
	_.switches.register( 'Binary', '-binary' )
	_.switches.register( 'Alias', '-alias', 'src' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'appServer.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'encrypt and compress python files as pickle.pbz2 encrypted with blowfish not converted to BASE64    ALSO    reverse',
	'categories': [
						'utility',
						'tool',
						'src',
						'source',
						'source protect',
						'src security',
						'code security',
						'code',
						'protect code',
						'cPickle',
						'pickle',
						'encrypt',
						'crypt',
						'compress',
						'decrypt',
						'blowfish',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						'b pysw',
						'p appServer -crypt en -f *.py',
						'',
						'b pysu',
						'p appServer -crypt en -f *.py',
						'',
						'b pycu',
						'p appServer -crypt en -f *.pyc',
						'',
						'p appServer -crypt de -f *.py',
						'',
						'p appServer -crypt de -location server -f dirX.pyc',
						'',
						'b py',
						'p appServer -crypt en -f pass.py dirX.py',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
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
	__.myFileLocations_SKIP_VALIDATION = True
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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
# START


import _rightThumb._mimetype as _mime

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

def password():
	global thePassword
	if not thePassword is None:
		return thePassword
	global maxPassword
	global defaultNumber
	global xyz

	


	if defaultNumber is None:
		_.colorThis(  [  '\n', '\tlynx "https://rephrecruiting.com/projects/lynx/number/?id=2b"', '\n'  ], 'purple'  )
		n = int( ask('n') )
		xyz = None
		defaultNumber = n

	else:
		n = defaultNumber


	a = ask('a')
	xyz = None
	b = ask('b')
	xyz = None
	_.pr()

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


def process( path, alias=None ):
	_.colorThis( [ '\n\n', path ], 'cyan' )

	mime = ''
	if _.switches.values('Crypt')[0].lower() == 'en' and os.path.isdir( path ):
		dirType = 'folder'
		ZIP_FOLDER_TEMP = _v.python['crypt']['en'] + _v.slash + _.genUUID() + '.folder'
		shutil.make_archive( ZIP_FOLDER_TEMP, 'zip', path )
		ZIP_FOLDER_TEMP += '.zip'
		mime = 'binary'
		# sys.exit()
	else:
		dirType = 'file'
		if _.switches.isActive('Binary'):
			mime = 'binary'
		else:
			try:
				if os.path.isfile(path):
					mime = _mime.what( path ).lower()
			except Exception as e:
				pass
	mime = mime.lower()

	global index
	if index == []:
		index = {}
	if index == {}:
		index = { 'windows': {}, 'unix': {}, 'crypt': {}, 'file': {}, 'records': [], 'unc': {'windows': {}, 'unix': {}}, 'aliases': {} }

	if not 'aliases' in index.keys():
		index['aliases'] = {}
	if not 'unc' in index.keys():
		index['unc'] = {'windows': {}, 'unix': {}}
		
	


	if os.path.isfile(path) or os.path.isdir(path):
		try:
			path = os.path.abspath(path)
		except Exception as e:
			pass
		filename = _.fileFolder( path, py=True )['file']

	unc = {
			'unix': _v.autoUNC( path, o='unix' ),
			'windows': _v.autoUNC( path, o='win' ),
	}

	if _v.appsFolder in path:
		base = 'apps'
		base_path = _v.appsFolder
	elif _v.techFolder in path:
		base = 'tech'
		base_path = _v.techFolder
	elif path.startswith( _v.techDrive ):
		base = 'drive'
		base_path = _v.techDrive
	else:
		base = 'other'
		base_path = '{7BE83231-EA06-4C4F-BA76-1A0094CD5510}{40436CCA-106C-420B-B938-5DC6DEAB7799}'

	if platform.system() == 'Windows':
		thisOS = 'windows'
		windows = path.replace( base_path, '' )
		unix = windows.replace( _v.slashes['windows'], _v.slashes['unix'] )
		selection = windows

	elif not platform.system() == 'Windows':
		thisOS = 'unix'
		unix = path.replace( base_path, '' )
		windows = unix.replace( _v.slashes['unix'], _v.slashes['windows'] )
		selection = unix


	if _.switches.values('Crypt')[0].lower() == 'en':
		addRecord = False
		if selection in index[thisOS].keys():
			record = index['records'][  index[thisOS][selection]  ]
			crypt = record['crypt']
		else:
			theID = len( index['records'] )
			guid = _.genUUID( project='crypt', label=filename )
			crypt = guid + '.crypt'

			if platform.system() == 'Windows':

				encrypt_win = _v.python['crypt']['en'] + _v.slash + crypt
				encrypt_win = encrypt_win.replace( _v.techFolder, '' )
				encrypt_unix = encrypt_win.replace( _v.slashes['windows'], _v.slashes['unix'] )

				decrypt_win = _v.python['crypt']['de'] + _v.slash + filename
				decrypt_win = decrypt_win.replace( _v.techFolder, '' )
				decrypt_unix = decrypt_win.replace( _v.slashes['windows'], _v.slashes['unix'] )

			elif not platform.system() == 'Windows':

				encrypt_unix = _v.python['crypt']['en'] + _v.slash + crypt
				encrypt_unix = encrypt_unix.replace( _v.techFolder, '' )
				encrypt_win = encrypt_unix.replace( _v.slashes['windows'], _v.slashes['unix'] )

				decrypt_unix = _v.python['crypt']['de'] + _v.slash + filename
				decrypt_unix = decrypt_unix.replace( _v.techFolder, '' )
				decrypt_win = decrypt_unix.replace( _v.slashes['windows'], _v.slashes['unix'] )

			addRecord = True



			record = {
						'id': theID,
						'file': filename,
						'guid': guid,

						'crypt': crypt,

						'windows': {
										'encrypt': encrypt_win,
										'decrypt': decrypt_win,
										'path': windows,
										'unc': unc['windows'],
						},

						'unix': {
										'encrypt': encrypt_unix,
										'decrypt': decrypt_unix,
										'path': unix,
										'unc': unc['unix'],
						},

						'path': path,
						'base': base,

						'dir': dirType,
						'mime': mime,
			}
			
		if not alias is None:
			index['aliases'][alias] = record['id']
		index['file'][filename] = record['id']
		if filename.lower().endswith('.py') or filename.lower().endswith('.pyc'):
			index['file'][thisOS+filename] = record['id']
		index['windows'][windows] = record['id']
		index['unix'][unix] = record['id']
		index['crypt'][crypt] = record['id']
		if addRecord:
			index['records'].append( record )

		
		if dirType == 'folder':

			encrypt2( ZIP_FOLDER_TEMP, _v.techFolder + record[thisOS]['encrypt'] )
			os.remove(ZIP_FOLDER_TEMP)


		else:

			if record['mime'] == 'binary':
				encrypt2( path, _v.techFolder + record[thisOS]['encrypt'] )
			else:
				file = _.getText( path, raw=True )
				compressed_pickle( encrypt(file), _v.techFolder + record[thisOS]['encrypt'] )

		server.put( _v.techFolder + record[thisOS]['encrypt'], save=crypt )
		_.saveTableDB( index, 'crypt.index' )
	



	elif _.switches.values('Crypt')[0].lower() == 'de':



		filename = path

		record = None
		if path in index['aliases'].keys():
			record = index['records'][  index['aliases'][path]  ]


		if record is None:
			if os.path.isfile(path) or os.path.isdir(path):
				path = os.path.abspath(path)
				filename = _.fileFolder( path )['file']

			if filename in index['crypt'].keys():
				record = index['records'][  index['crypt'][filename]  ]
			elif filename in index['file'].keys():
				if filename.lower().endswith('.py') or filename.lower().endswith('.pyc'):
					record = index['records'][  index['file'][thisOS+filename]  ]
				else:
					record = index['records'][  index['file'][filename]  ]
				if record is None and filename.lower().endswith('.py') or filename.lower().endswith('.pyc'):
					record = index['records'][  index['file'][filename]  ]
			else:
				_.colorThis( [  '\t', 'Error: no file', filename  ], 'red' )
				return None

   

		if record['base'] == 'apps':
			base_path = _v.appsFolder
		elif record['base'] == 'tech':
			base_path = _v.techFolder
		elif record['base'] == 'drive':
			base_path = _v.techDrive
		elif record['base'] == 'other':
			base_path = ''



		if _.switches.isActive('Location') and 's' in _.switches.values('Location')[0].lower():
				server.get( record['crypt'], save=_v.techFolder + record[thisOS]['encrypt'] )

		if record['dir'] == 'folder':
			ZIP_FOLDER_TEMP = _v.techFolder + record[thisOS]['decrypt']+'.tmp.zip'
			decrypt2( _v.techFolder + record[thisOS]['encrypt'], ZIP_FOLDER_TEMP )

		else:
			file = decompress_pickle( _v.techFolder + record[thisOS]['encrypt'] )

		if _.switches.isActive('RestoreOriginalPath'):
			if not record['base'] == 'other':
				fileLocation = base_path + record[thisOS]['path']
			elif record['base'] == 'other':
				fileLocation = _v.userprofile + _v.slash + 'Downloads'
				if not os.path.isdir( fileLocation ):
					os.mkdir( fileLocation )

			if os.path.isfile( fileLocation ):
				_.colorThis( [  '\n\t *** Warning ***'  ], 'red' )
				_.colorThis( [  '\t\t File exists'  ], 'yellow' )
				replaceFile = 'no'
				replaceFile = input( '        REPLACE FILE ? ' )
				if 'y' in replaceFile.lower():
					if record['mime'] == 'binary':
						decrypt2( _v.techFolder + record[thisOS]['encrypt'], fileLocation )
					else:
						_.saveText( decrypt( file ), fileLocation )
						_.colorThis( [  '\nFile replaced'  ], 'green' )
				else:
					_.colorThis( [  '\nFile NOT replaced'  ], 'green' )
			else:
				if record['dir'] == 'folder':
					shutil.unpack_archive( ZIP_FOLDER_TEMP, fileLocation, 'zip' )
					os.remove(ZIP_FOLDER_TEMP)
				else:
					_.saveText( decrypt( file ), fileLocation )
		else:
			if record['dir'] == 'folder':
				shutil.unpack_archive( ZIP_FOLDER_TEMP, _v.techFolder + record[thisOS]['decrypt'], 'zip' )
				os.remove(ZIP_FOLDER_TEMP)
			else:
				if record['mime'] == 'binary':
					decrypt2( file, _v.techFolder + record[thisOS]['decrypt'] )
				else:
					_.saveText( decrypt( file ), _v.techFolder + record[thisOS]['decrypt'] )


class Server():
	# https://pythonprogramming.net/ftp-transfers-python-ftplib/
	def __init__( self ):
		self.connected = False

	def connect( self ):
		if not self.connected:
			self.ftp = FTP('107.180.50.181')
			self.ftp.login(user='E06E7C8A994F@tools.rightthumb.com', passwd = '{5F8E70B1-60AE-498C-BB9D-60CACE1208B6}')
			self.connected = True
		
	def get( self, file, save=None ):
		self.connect()
		_.colorThis( [ '\t file:', file ], 'yellow' )
		_.colorThis( [ '\t save:', save ], 'yellow' )
		if save is None:
			save = file
		localfile = open(save, 'wb')
		self.ftp.retrbinary('RETR ' + file, localfile.write, 1024)
		localfile.close()
		

	def put( self, file, save=None ):
		self.connect()
		_.colorThis( [ '\t file:', file ], 'yellow' )
		_.colorThis( [ '\t save:', save ], 'yellow' )
		if save is None:
			save = file
		self.ftp.storbinary('STOR '+save, open(file, 'rb'))

	def close( self ):
		self.ftp.quit()


def action():
	global index
	load()

	# _.pr( _.appData[__.appReg]['pipe'] )
	if type( _.appData[__.appReg]['pipe'] ) == bool:
		_.colorThis( [  '\n','Error: no files','\n'  ], 'red' )
		_.colorThis( [  '\t', 'check folder', '\n'  ], 'yellow' )
		sys.exit()
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			if _.switches.isActive('Alias'):
				process( row, _.switches.values('Alias')[i] )
			else:
				process( row )

	server.put( _v.dbTables + _v.slash + 'crypt.index' , 'crypt.index' )
	server.close()
def load():
	global index
	global server
	server = Server()
	if _.switches.isActive('Location') and 's' in _.switches.values('Location')[0].lower():
		server.get( 'crypt.index', _v.dbTables + _v.slash + 'crypt.index' )
	index = _.getTableDB( 'crypt.index' )



server = None
index = None
maxPassword = 72
maxPassword = 30
# defaultNumber = 230358556087838562505042281951026793951636743471603964423051916043939034799925600969375258059814027290350438564312280919741722145713923874154996634001023523757244534564376895689643453456876543535647865436243578684564326879576354645623454357685012354376659878
defaultNumber = None
thePassword = None
xyz = None


########################################################################################
if __name__ == '__main__':
	action()







