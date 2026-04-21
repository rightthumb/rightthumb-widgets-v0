import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'Encrypt', '-e,-en,-encrypt' )
	_.switches.register( 'Decrypt', '-d,-de,-decrypt' )
	_.switches.register( 'Password', '-password' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'cryptStringSimple.py',
	'description': 'crypt string simple',
	'categories': [
						'encryption',
						'crypt',
						'string',
						'simple',
				],
	'examples': [
						_.hp('p cryptStringSimple -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start



from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

def myPad(password: bytes, min_length: int) -> bytes:
	# Ensure the password is at least the specified minimum length by padding with spaces
	return password.ljust(min_length, b' ')[:56]  # Blowfish key max length is 56 bytes

def encrypt(plaintext: str, password: str) -> str:
	password = password.strip()
	
	# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
	key = myPad(password.encode(), 4)
	
	# Create the cipher with CBC mode and generate an IV
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)
	iv = cipher.iv
	
	# Pad the plaintext to match the Blowfish block size and encrypt
	padded_text = pad(plaintext.encode(), Blowfish.block_size)
	encrypted = cipher.encrypt(padded_text)
	
	# Combine IV with the encrypted text and encode in base64
	encrypted_text = base64.b64encode(iv + encrypted).decode('utf-8')
	
	return encrypted_text

def decrypt(encrypted_text: str, password: str) -> str:
	password = password.strip()
	
	try:
		# Decode the base64-encoded encrypted text
		encrypted_data = base64.b64decode(encrypted_text)
		
		# Extract the IV and encrypted message
		iv = encrypted_data[:Blowfish.block_size]
		encrypted_message = encrypted_data[Blowfish.block_size:]
		
		# Pad the key to ensure it is at least 4 bytes long and at most 56 bytes
		key = myPad(password.encode(), 4)
		
		# Create the cipher with CBC mode and the extracted IV
		cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
		
		# Decrypt and unpad the plaintext
		decrypted_padded = cipher.decrypt(encrypted_message)
		decrypted = unpad(decrypted_padded, Blowfish.block_size).decode('utf-8')
		
		return decrypted
	except (ValueError, KeyError) as e:
		print(f'Decryption error: {e}')
		return "Decryption failed. Incorrect padding or invalid key."






def action():
	
	if not _.switches.isActive('Password'):
		password = _v.cryptoKeyPad + _v.scrampleIDs(_v.getMachineID2())
	else:
		password = ' '.join( _.switches.values('Password') )
	
	if _.switches.isActive('Encrypt'):
			text = ' '.join( _.switches.values('Encrypt') )
			result = encrypt(text, password)
	elif _.switches.isActive('Decrypt'):
			text = ' '.join( _.switches.values('Decrypt') )
			result = decrypt(text, password)
	else:
		_.e('No action specified')
	
	print(result)
########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);