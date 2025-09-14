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
import secrets
import string
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
import _rightThumb._base2 as _
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

# Register switches for password generation options
_.switches.register('Length', '-l,-length', '16')
_.switches.register('NoSymbols', '-ns,-nosymbols')
_.switches.register('NoNumbers', '-nn,-nonumbers')
_.switches.register('NoUpper', '-nu,-noupper')
_.switches.register('NoLower', '-nl,-nolower')
_.switches.register('Count', '-n,-count', '1')
_.switches.register('Clipboard', '-c,-clip')

_.appInfo[focus()] = {
	'file': 'pw-gen.py',
	'description': 'Generates secure passwords with customizable character sets',
	'categories': [
		'security', 'password', 'generator', 'crypto', 'auth'
	],
	'relatedapps': ['api-key-gen', 'guid', 'keychain'],
	'prerequisite': [],
	'examples': [
		'p pw-gen',
		'p pw-gen -l 20',
		'p pw-gen -ns',
		'p pw-gen -l 12 -n 5',
		'p pw-gen -c'
	],
	'columns': [],
}

_.appData[focus()] = {
	'var': '',
	'pipe': [],
}

def generatePassword(length=16, use_symbols=True, use_numbers=True, use_upper=True, use_lower=True):
	"""Generate a secure password with specified character sets"""
	
	# Build character set based on options
	charset = ''
	if use_lower:
		charset += string.ascii_lowercase
	if use_upper:
		charset += string.ascii_uppercase
	if use_numbers:
		charset += string.digits
	if use_symbols:
		charset += '!@#$%^&*()_+-=[]{}|;:,.<>?'
	
	# Ensure we have at least one character type
	if not charset:
		charset = string.ascii_letters + string.digits
	
	# Generate password ensuring at least one character from each selected type
	password = []
	
	# Add one character from each selected type first
	if use_lower and string.ascii_lowercase in charset:
		password.append(secrets.choice(string.ascii_lowercase))
	if use_upper and string.ascii_uppercase in charset:
		password.append(secrets.choice(string.ascii_uppercase))
	if use_numbers and string.digits in charset:
		password.append(secrets.choice(string.digits))
	if use_symbols and any(c in charset for c in '!@#$%^&*()_+-=[]{}|;:,.<>?'):
		password.append(secrets.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))
	
	# Fill the rest randomly
	for _ in range(length - len(password)):
		password.append(secrets.choice(charset))
	
	# Shuffle the password to avoid predictable patterns
	secrets.SystemRandom().shuffle(password)
	
	return ''.join(password)

def copyToClipboard(text):
	"""Copy text to clipboard if possible"""
	try:
		import pyperclip
		pyperclip.copy(text)
		return True
	except ImportError:
		try:
			# Try using system clipboard commands
			import subprocess
			if os.name == 'nt':  # Windows
				subprocess.run(['clip'], input=text.encode(), check=True)
			elif os.system('which xclip > /dev/null 2>&1') == 0:  # Linux with xclip
				subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode(), check=True)
			elif os.system('which pbcopy > /dev/null 2>&1') == 0:  # macOS
				subprocess.run(['pbcopy'], input=text.encode(), check=True)
			else:
				return False
			return True
		except:
			return False

def action():
	"""Main action function"""
	# Get parameters from switches
	length = int(_.switches.value('Length')) if _.switches.isActive('Length') else 16
	count = int(_.switches.value('Count')) if _.switches.isActive('Count') else 1
	
	# Character set options
	use_symbols = not _.switches.isActive('NoSymbols')
	use_numbers = not _.switches.isActive('NoNumbers')
	use_upper = not _.switches.isActive('NoUpper')
	use_lower = not _.switches.isActive('NoLower')
	
	# Validate length
	if length < 4:
		print("Error: Minimum password length is 4 characters")
		return
	if length > 256:
		print("Error: Maximum password length is 256 characters")
		return
	
	# Generate and display passwords
	passwords = []
	for i in range(count):
		password = generatePassword(length, use_symbols, use_numbers, use_upper, use_lower)
		passwords.append(password)
		
		print()
		if count > 1:
			print(f"Password {i+1}:")
		else:
			print("Generated Password:")
		print(password)
		print()
	
	# Copy to clipboard if requested
	if _.switches.isActive('Clipboard'):
		if count == 1:
			if copyToClipboard(passwords[0]):
				print("✓ Copied to clipboard")
			else:
				print("✗ Could not copy to clipboard")
		else:
			# For multiple passwords, copy all separated by newlines
			all_passwords = '\n'.join(passwords)
			if copyToClipboard(all_passwords):
				print(f"✓ Copied {count} passwords to clipboard")
			else:
				print("✗ Could not copy to clipboard")

# Process switches and handle pipe data
if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

_.switches.process()

########################################################################################
if __name__ == '__main__':
	action()