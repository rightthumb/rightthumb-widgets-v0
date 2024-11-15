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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
import _rightThumb._encryptString as _blowfish
##################################################

def appSwitches():
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files', isRequired=True )
	_.switches.register( 'Encrypt', '-en,-encrypt' )
	_.switches.register( 'Decrypt', '-de,-decrypt' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Vault', '-vault' )
	_.switches.register( 'DeleteOriginal', '-r,-rm,-del,-delete,-remove' )
	_.switches.register( 'NoExt', '-no,-noext' )
	_.switches.register( 'isCrypt', '-iscrypt' )
	_.switches.register( 'Clean', '--c' )
	

_.autoBackupData = False
__.releaseAcquiredData = False
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Encrypt','Decrypt']

_.appInfo[focus()] = {
	'file': 'cryptFile.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'encrypt or decrypt string',
	'categories': [
						'encrypt',
						'decrypt',
						'crypt',
						'string',
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
						'p cryptFile -vault -r -f dnd.jpg  -en  ',
						'p cryptFile -vault -r -f dnd.jpg.crypt  -de  ',
						'',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations,vs=True)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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




def action():
	global encrypted_file_ext
	global appDBA
	# focus()
	# focus()
	# _.pr('appDBA',appDBA)
	# _.pr( _.switches.isActive('Files',appDBA), 'Files', _.switches.value('Files',appDBA) )
	# _.pr( _.switches.isActive('Decrypt',appDBA), 'Decrypt' )
	# _.pr( _.switches.isActive('Encrypt',appDBA), 'Encrypt' )
	# _.pr( _.switches.isActive('isCrypt',appDBA), 'isCrypt' )

	# sys.exit()

	if _.switches.isActive('Files',appDBA):
		files=_.switches.values('Files',appDBA)
		for fii, filepath in enumerate(files):
			original = filepath
			done = False
			if not os.path.isfile(filepath):
				return None

			# _.pr( _.switches.isActive('isCrypt',appDBA), 'isCrypt' )
			# sys.exit()

			if  _.switches.isActive('isCrypt',appDBA):
				# _.pr('here')
				# sys.exit()
				done = True
				if _.isCrypt(filepath):
					_.colorThis( [ 'True ', filepath ], 'red' )
				else:
					_.colorThis( [ 'False', filepath ], 'cyan' )
				sys.exit()


			if not done:

				if  _.switches.isActive('Password',appDBA):
					password = _.switches.values('Password',appDBA)[0]
					passwordIs = False
				else:
					password = _vault.key()
					passwordIs = True

				if  _.switches.isActive('Vault',appDBA):
					password = _vault.key()
					passwordIs = True




				# encryption/decryption buffer size - 64K
				bufferSize = 64 * 1024
				# password = "foopassword"


				filepath = original
				# _.pr(  " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ])  )
				if " ".join(['{:02X}'.format(byte) for byte in     open( filepath, 'rb' ).read(32)    ]).startswith( '41 45 53 02 00 00 1B' ):
				# if _.isCrypt(filepath):
					confirmed_encrypted = True
				else:
					confirmed_encrypted = False

				# _.pr( _.switches.isActive('Decrypt',appDBA) )
				if not _.switches.isActive('Decrypt',appDBA) and not _.switches.isActive('Encrypt',appDBA):
					# _.pr(0)
					if confirmed_encrypted:
						# _.pr(1)
						_.switches.fieldSet( 'Decrypt', 'active', True, appDBA )
					else:
						# _.pr(2)
						_.switches.fieldSet( 'Encrypt', 'active', True, appDBA )


				# _.pr( _.switches.isActive('Decrypt',appDBA) )
				if not confirmed_encrypted and _.switches.isActive('Decrypt',appDBA):
					_.colorThis( [ 'Error: not encrypted' ], 'red' )
					sys.exit()

				if _.switches.isActive('Encrypt',appDBA):
					if not _.switches.isActive('Clean'):
						_.colorThis(['Encrypt:',filepath],'cyan')
					# new = _blowfish.encrypt( file, password )
					# encrypt
					encrypted_file_ext_use = encrypted_file_ext
					if _.switches.isActive('NoExt',appDBA): encrypted_file_ext_use = '';


					output = filepath+encrypted_file_ext_use
					filepath = os.path.abspath(filepath)
					if output.lower() == filepath.lower():
						output=filepath

					if not output == filepath:
						output = _.replaceFile( filepath, output )
					# decrypt
					tmp = False
					outputBK = output
					if filepath == output:
						if not _.switches.isActive('Clean'):
							_.pr('same',c='red')
						tmp = True
						# os.rename( output, filepath )
						# time.sleep(.2)
						output = output+'-'+_.genUUID()+'.de'


					if passwordIs:
						if not _blowfish.myDecrypt():
							_.pr('Bad Password')
							sys.exit()
					with open( filepath, 'rb' ) as fIn:
						with open( output , 'wb' ) as fOut:
							pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

					if tmp:
						time.sleep(.2)
						if os.path.isfile(filepath):
							os.remove( filepath )
						time.sleep(.2)
						os.rename( output, outputBK )
						time.sleep(.2)
						if os.path.isfile(output):
							os.remove( output )


					if _.switches.isActive('DeleteOriginal',appDBA):
						_.secureDeleteFile(filepath)
						
				# _.pr( _.switches.isActive('Decrypt',appDBA) )
				if _.switches.isActive('Decrypt',appDBA):
					if not _.switches.isActive('Clean'):
						_.colorThis(['Decrypt:',filepath],'cyan')

					# get encrypted file size
					encFileSize = os.stat(  filepath  ).st_size


					# new = _blowfish.decrypt( file, password )
					output = filepath
					if not _.switches.isActive('NoExt'):
						if output.endswith(encrypted_file_ext):
							output = output[:len(output) - len(encrypted_file_ext)]

					if len(_.switches.value('Decrypt',appDBA)):
						output = _.switches.values('Decrypt',appDBA)[fii]

					filepath = os.path.abspath(filepath)
					output = _.replaceFile( filepath, output )
					# decrypt
					tmp = False
					outputBK = output
					if filepath == output:
						tmp = True
						filepath = output+'-'+_.genUUID()+'.en'

						os.rename( output, filepath )
						time.sleep(.2)    
						output = output+'-'+_.genUUID()+'.de'

					with open(  filepath, 'rb'  ) as fIn:
						try:
							with open(  output , 'wb'  ) as fOut:
								# decrypt file stream
								pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
						except ValueError:
							if not _.switches.isActive('Clean'):
								_.pr('Err:', 0)
							if os.path.isfile( output ):
								if not _.switches.isActive('Clean'):
									_.pr('Err:', 1)
								os.remove( output )
								time.sleep(.2)
							# remove output file on error
							# remove("dataout.txt")
					if tmp:
						time.sleep(.2)
						os.rename( output, outputBK )
						time.sleep(.2)
						os.rename( filepath, output )

						time.sleep(.2)
						if os.path.isfile(output):
							os.remove( output )
						



					if _.switches.isActive('DeleteOriginal',appDBA):
						os.remove(filepath)
			filepath = original
			if not _.switches.isActive('Clean'):
				try:
					_.pr( 'isCrypt', _.isCrypt(filepath) )
				except:
					try:
						_.pr( 'isCrypt', _.isCrypt(output) )
					except: pass



encrypted_file_ext = '.crypt'

# __.appRegBK=__.appReg
# _del = _.regImp( __.appReg, 'secure-delete-file' )
# _del.switch('Files', output); _del.action();

import _rightThumb._vault as _vault
# import _rightThumb._encryptString as _blowfish
try:
	import pyAesCrypt
except Exception as e:
	pass
focus()
# from os import stat, remove

########################################################################################
if __name__ == '__main__':
	start=time.time()
	action()
	diff=time.time()-start
	print(diff)







