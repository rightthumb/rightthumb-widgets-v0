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
import secrets
import string
import hashlib
import base64
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

# Register switches for different API key options
_.switches.register('Length', '-l,-length', '32')
_.switches.register('Format', '-f,-format', 'hex')
_.switches.register('Prefix', '-p,-prefix', '')
_.switches.register('Suffix', '-s,-suffix', '')
_.switches.register('Clipboard', '-c,-clip')
_.switches.register('Project', '-project', '')
_.switches.register('Silent', '-silent')
_.switches.register('Count', '-n,-count', '1')

_.appInfo[focus()] = {
	'file': 'api-key-gen.py',
	'description': 'Generates secure API keys with various formats and options',
	'categories': [
		'security', 'api', 'key', 'generator', 'crypto', 'auth', 'authentication'
	],
	'relatedapps': ['guid', 'keychain', 'pw-gen'],
	'prerequisite': [],
	'examples': [
		'p api-key-gen',
		'p api-key-gen -l 64',
		'p api-key-gen -f base64',
		'p api-key-gen -f alphanumeric -l 48',
		'p api-key-gen -p "api_" -s "_v1"',
		'p api-key-gen -c',
		'p api-key-gen -n 5',
		'p api-key-gen -project "MyApp" -silent'
	],
	'columns': [],
}

_.appData[focus()] = {
	'var': '',
	'pipe': [],
}

def generateSecureKey(length=32, format_type='hex'):
	"""Generate a cryptographically secure API key"""
	if format_type == 'hex':
		# Generate random bytes and convert to hex
		return secrets.token_hex(length // 2)
	elif format_type == 'base64':
		# Generate random bytes and encode as base64
		random_bytes = secrets.token_bytes(length)
		return base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')
	elif format_type == 'alphanumeric':
		# Generate using letters and digits only
		alphabet = string.ascii_letters + string.digits
		return ''.join(secrets.choice(alphabet) for _ in range(length))
	elif format_type == 'mixed':
		# Generate using letters, digits, and safe symbols
		alphabet = string.ascii_letters + string.digits + '-_'
		return ''.join(secrets.choice(alphabet) for _ in range(length))
	else:
		# Default to hex format
		return secrets.token_hex(length // 2)

def formatKey(key, prefix='', suffix=''):
	"""Apply prefix and suffix to the key"""
	return f"{prefix}{key}{suffix}"

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

def logKey(key, project=''):
	"""Log the generated API key"""
	if not _.switches.isActive('Silent'):
		if not project:
			project = input('Project name (Enter to skip): ').strip()
		
		if project and project.lower() != 'n':
			try:
				keyLog = _.getTable('api_key_log.json')
				data = {
					'key_hash': hashlib.sha256(key.encode()).hexdigest()[:16],  # Store only hash for security
					'timestamp': time.time(),
					'project': project,
					'app': 'api-key-gen',
					'length': len(key),
					'format': _.switches.value('Format') if _.switches.isActive('Format') else 'hex'
				}
				keyLog.append(data)
				_.saveTable(keyLog, 'api_key_log.json')
				print(f"Logged to: {_v.myTables}/api_key_log.json")
			except Exception as e:
				print(f"Warning: Could not log key - {e}")

def action():
	"""Main action function"""
	# Get parameters from switches
	length = int(_.switches.value('Length')) if _.switches.isActive('Length') else 32
	format_type = _.switches.value('Format').lower() if _.switches.isActive('Format') else 'hex'
	prefix = _.switches.value('Prefix') if _.switches.isActive('Prefix') else ''
	suffix = _.switches.value('Suffix') if _.switches.isActive('Suffix') else ''
	count = int(_.switches.value('Count')) if _.switches.isActive('Count') else 1
	project = _.switches.value('Project') if _.switches.isActive('Project') else ''
	
	# Validate format
	valid_formats = ['hex', 'base64', 'alphanumeric', 'mixed']
	if format_type not in valid_formats:
		print(f"Error: Invalid format '{format_type}'. Valid formats: {', '.join(valid_formats)}")
		return
	
	# Validate length
	if length < 8:
		print("Error: Minimum key length is 8 characters")
		return
	if length > 512:
		print("Error: Maximum key length is 512 characters")
		return
	
	# Generate and display keys
	keys = []
	for i in range(count):
		key = generateSecureKey(length, format_type)
		formatted_key = formatKey(key, prefix, suffix)
		keys.append(formatted_key)
		
		print()
		if count > 1:
			print(f"API Key {i+1}:")
		else:
			print("Generated API Key:")
		print(formatted_key)
		print()
		
		# Log only the first key if multiple
		if i == 0:
			logKey(formatted_key, project)
	
	# Copy to clipboard if requested
	if _.switches.isActive('Clipboard'):
		if count == 1:
			if copyToClipboard(keys[0]):
				print("✓ Copied to clipboard")
			else:
				print("✗ Could not copy to clipboard")
		else:
			# For multiple keys, copy all separated by newlines
			all_keys = '\n'.join(keys)
			if copyToClipboard(all_keys):
				print(f"✓ Copied {count} keys to clipboard")
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