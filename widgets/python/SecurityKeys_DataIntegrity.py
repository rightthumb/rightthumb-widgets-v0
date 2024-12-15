import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'Gen', '-gen' )
	_.switches.register( 'Check', '-check', 'en, duration' )
	_.switches.register( 'Encrypt', '-en,-encrypt', 'str_to_en' )
	_.switches.register( 'Decrypt', '-de,-decrypt', 'en' )
	_.switches.register( 'KeyGen', '-keyGen', 'duration dic' )
	_.switches.register( 'KeyCheck', '-keyCheck' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'EncodeForURL', '-web,-url,-urlencode' )
	_.switches.register( 'EncodeStringForURL', '-str,-string', "{test:123,key:string} reformats as json if contains {" )
	_.switches.register( 'CurlReverse', '-curl', 'wsl just url' )

_._default_settings_()

duration = {
			'sec': 1,
			'min': 60,
			'h': 3600,
			'd': 86400,
			'w': 604800,
			'mo': 2592000,
			'y': 31536000,
		}
duration = ', '.join(list(duration.keys()))
_.appInfo[focus()] = {
	'file': 'ephemeral.py',
	'description': [
		'Security Key Generator with Soft or Hard Coded Expiration',
		'Used to generate codes that expire.',
		'Created or Checked in this app or by https://cli.sds.sh/ephemeral/',
		'',
		'The encryption methods were added as bonus feature but not main purpose or app',
		
	],
	'categories': [
						_.pr('security',c='Background.green',p=0),
						'keys',
						_.pr('online integration',c='Background.red',p=0),
						'cli.sds.sh',
				],
	'examples': [

						_.linePrint(label='simple',p=0),
						# ,c='Background.light_blue',p=0),
						_.hp(''),
						_.pr('KeyGen Generates Hard Coded Expiration Keys, the expiration is encrypted in the key and does not change',c='Background.green',p=0),
						_.pr('\tThe keys it generates can be checked by this app or on https://cli.sds.sh/ephemeral/',c='Background.green',p=0),
						_.pr('\t\tdurations: ' + duration + ' --> ex: 1h 10min 2d 1w 2mo 10y',c='Background.yellow',p=0),
						_.hp('p ephemeral -keyGen 2d'),
						_.hp('p ephemeral -keyCheck [U2FsdGVkX1/zrS5rOlngkwuMml/Kt75A2zFiokOc+XQ=][U2FsdGVkX18Hftr8s5O4Rkw0wzdilh2BxZhOH3CrT4w=] -password 123'),
						_.pr('https://cli.sds.sh/ephemeral/?keyCheck=%5BU2FsdGVkX1/zrS5rOlngkwuMml/Kt75A2zFiokOc%2BXQ%3D%5D%5BU2FsdGVkX18Hftr8s5O4Rkw0wzdilh2BxZhOH3CrT4w%3D%5D&password=123',c='yellow',p=0),
						_.hp(''),
						_.hp(''),
						_.pr('Gen Generates Soft Coded Keys, the expiration given when checked',c='Background.green',p=0),
						_.pr('\tThe keys it generates can be checked by this app or on https://cli.sds.sh/ephemeral/',c='Background.green',p=0),
						_.hp('p ephemeral -gen -password 123'),
						_.hp('p ephemeral -check U2FsdGVkX19QuHm65qfu4tvgtifSTVk9QcXEb3IMNco= 10y -password 123'),
						_.pr('https://cli.sds.sh/ephemeral/?check=U2FsdGVkX19QuHm65qfu4tvgtifSTVk9QcXEb3IMNco%3D&password=123&duration=10y',c='yellow',p=0),
						_.hp(''),

						_.linePrint(label='simple',p=0),
						_.hp(''),
						_.pr('durations: ' + duration + ' --> ex: 1h 10min 2d 1w 2mo 10y',c='Background.yellow',p=0),
						_.hp(''),
						_.hp('p ephemeral -gen'),
						_.hp('p ephemeral -check U2FsdGVkX1/aDBdtxFXct0oXXJ9dUslxt8qSjBeYokA= 2d'),
						_.hp('p ephemeral -check U2FsdGVkX1/aDBdtxFXct0oXXJ9dUslxt8qSjBeYokA= 10y'),
						_.hp(''),
						_.pr('https://cli.sds.sh/ephemeral/?gen=1&password=123',c='yellow',p=0),
						_.hp('p ephemeral -check U2FsdGVkX1/TiMjKIJmY4xvWqpjyuYfFe9O4YAjJhE0= 2y -password 123'),
						_.hp(''),
						_.linePrint(label='simple',p=0),
						_.hp(''),
						_.hp('p ephemeral -encrypt test'),
						_.hp('p ephemeral -decrypt "U2FsdGVkX18EdZ/7AF0ig1Rsd0UKfhadL7U34qXIU7U="'),
						_.hp(''),
						_.hp('p ephemeral -encrypt test -password 123'),
						_.hp('p ephemeral -decrypt "U2FsdGVkX19ifdxB5JquLYGokn+nNR0uaxKS29wd+nI=" -password 123'),
						_.hp(''),
						_.hp('p ephemeral -encrypt test -password 123 -url'),
						_.pr('https://cli.sds.sh/ephemeral/?decrypt=U2FsdGVkX19nM%2Ba06CtvKPTM8kzlNS1yt2SXV2pMcF8%3D&password=123',c='yellow',p=0),
						_.hp(''),
						_.hp('https://cli.sds.sh/ephemeral/?encrypt=test&password=123'),
						_.hp('p ephemeral -decrypt U2FsdGVkX1/ps0aqGaDpls3+sPYEbyNGCKftv97ew5A= -password 123'),
						_.linePrint(label='simple',p=0),
						_.hp(''),
						_.pr('durations: ' + duration + ' --> ex: 1h 10min 2d 1w 2mo 10y',c='Background.yellow',p=0),
						_.hp(''),
						_.hp('p ephemeral -keyGen 2d'),
						_.hp('p ephemeral -keyCheck [U2FsdGVkX1/VcHfk=][U2FsdGVkX1/kb6P1o=]'),
						_.hp(''),
						_.hp('p ephemeral -keyGen 2d {test:123,key:string}'),
						_.hp('p ephemeral -keyCheck [U2FsdGVkX196xVBkvyW=][U2FsdG=][U2FsdGVkX1/Qmm=][U2FsdGVkX1/2FQlsm=][U2FsdGVkX18G=][U2FsdG=] {test:123,key:string}'),
						_.hp(''),
						_.hp('p ephemeral -keyGen 2d -password 123 -url'),
						_.pr('https://cli.sds.sh/ephemeral/?keyCheck=%5BU2FsdGVkX1%2BCXn6XDi6KvV7gez7wBqEZJaOCta3eiqc%3D%5D%5BU2FsdGVkX18dRnzeD59FsVEVebJ9Fwp0NPOqiK4OweI%3D%5D&password=123',c='yellow',p=0),
						_.hp(''),
						_.hp('https://cli.sds.sh/ephemeral/?keyGen=2d&password=123'),
						_.hp('p ephemeral -keyCheck [U2FsdGVkX18Lek+GT1bJE9qlldjeZwcmBh4VrvhGK/Y=][U2FsdGVkX1/aZ04mAqwt/utF+S5nq1rFUs/Ugyz0l1Q=] -password 123'),
						_.hp(''),
						_.hp(''),
						_.hp('p ephemeral -string {test:123,key:string}'),
						_.hp(''),
						_.linePrint(label='simple',p=0),
						_.hp(''),
						_.pr('\tAdd -curl or -curl wsl',c='Background.light_blue',p=0),
						_.pr('\t-curl url: shows url and not the curl command',c='Background.light_blue',p=0),
						_.pr('\t-curl just: shows just the curl command not the results of the command',c='Background.light_blue',p=0),
						_.hp(''),

						_.hp('p ephemeral -keyGen 2d -password 123 -curl'),
						_.hp('p ephemeral -encrypt test -curl -password this is the password'),
						_.hp('p ephemeral -encrypt test -curl wsl -password this is the password'),
						_.hp(''),
						_.pr('\tTest in Linux by adding to the end | bash',c='Background.light_blue',p=0),
						_.hp('p ephemeral -encrypt test -curl just  -password this is the password | bash'),
						_.pr('\tTest in Windows by adding to the end | cmd',c='Background.light_blue',p=0),
						_.hp('p ephemeral -encrypt test -curl just -password this is the password | cmd'),
						_.hp('p ephemeral -encrypt test -curl just wsl -password this is the password | cmd'),
						_.hp(''),
						_.pr('\t-curl works with: Gen Encrypt Decrypt KeyGen',c='Background.red',p=0),
						_.hp(''),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [
		_.pr('https://cli.sds.sh/ephemeral/?keyCheck=[U2FsdGVkX18X5Pj2lqpfuSEp2vCBZ7ZDRlN/LHnZXqA=][U2FsdGVkX19IQkaULjznIEdrJ6BELcmBpB/AaJENGQ8=]',c='yellow',p=0),
	],
	'prerequisite': [],
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


try:
	from AesEverywhere import aes256
except:
	_.e('AesEverywhere not installed','pip3 install aes-everywhere')

class AESApp:
	def __init__(self, password: str):
		self.password = password  # Keep the password as a string

	def encrypt(self, plaintext: str, password=None):
		if password is None:
			password = self.password
		elif isinstance(password, bytes):  # Decode if password is bytes
			password = password.decode('utf-8')
		return aes256.encrypt(plaintext, password).decode('utf-8')

	def decrypt(self, encoded_data: str, password=None):
		if password is None:
			password = self.password
		elif isinstance(password, bytes):  # Decode if password is bytes
			password = password.decode('utf-8')
		return aes256.decrypt(encoded_data, password).decode('utf-8')




import base64
import hashlib
import re
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import re
import binascii
import os

class ephemeralLinkManagerAES:
	DEFAULT_KEY = 'c37b2b38-7d23-4123-9247-4e2a52550397'
	log = []

	def __init__(self):
		if _.switches.isActive('Password'):
			self.SECRET_KEY = _.switches.values('Password')[0]
		else:
			if 'ephemeral' in _v.fig: self.DEFAULT_KEY = _v.fig['ephemeral']
			self.SECRET_KEY = self.DEFAULT_KEY
		self.aes_app = AESApp(self.SECRET_KEY)
		self.durations = {
			'sec': 1,
			's': 1,
			'mn': 60,
			'n': 60,
			'min': 60,
			'h': 3600,
			'd': 86400,
			'w': 604800,
			'mo': 2592000,
			'm': 2592000,
			'y': 31536000,
		}

	def enLen(self, uuid, length):
		while len(uuid) < length:
			uuid += uuid
		return uuid[:length]

	def gen(self):
		data = str(int(time.time()))
		encrypted_data = self.aes_app.encrypt(data)
		return encrypted_data


	def check(self, en, duration):
		try:
			timestamp = int(self.aes_app.decrypt(en))
		except Exception as e:
			self.log.append(f"Decryption failed: {e}")
			return False

		duration_seconds = self.parseDuration(duration)
		if not duration_seconds:
			return False

		current_epoch = int(time.time())
		difference_in_seconds = current_epoch - timestamp
		return difference_in_seconds < duration_seconds


	def encrypt(self, data, password=None):
		return self.aes_app.encrypt(data,password)

	def is_valid_base64(self, data):
		# Ensure string is valid Base64 (length multiple of 4 and correct characters)
		if len(data) % 4 != 0:
			return False
		base64_pattern = r'^[A-Za-z0-9-_]+={0,2}$'
		return re.match(base64_pattern, data) is not None

	def decrypt(self, data, password=None):
		return self.aes_app.decrypt(data,password)






	def parseDuration(self, duration):
		match = re.match(r'^\d+[a-z]*$', duration)
		if not match:
			return False

		time_value, period = int(match.group()[:-1]), match.group()[-1]
		return time_value * self.durations.get(period, 0)

	def cryptEn(self, string, password=None):
		if password is None:
			password = self.SECRET_KEY
		encrypted_string = ''.join(
			chr(ord(string[i]) + ord(password[i % len(password)]))
			for i in range(len(string))
		)
		return base64.urlsafe_b64encode(encrypted_string.encode()).decode().replace('=', '|')

	def cryptDe(self, encrypted_string, password=None):
		if password is None:
			password = self.SECRET_KEY
		encrypted_string = base64.urlsafe_b64decode(encrypted_string.replace('|', '=').encode()).decode()
		return ''.join(
			chr(ord(encrypted_string[i]) - ord(password[i % len(password)]))
			for i in range(len(encrypted_string))
		)

	def keyGen(self, duration='1h', dic=None):
		if dic is None:
			dic = {}

		timestamp = self.gen()
		encrypted_duration = self.encrypt(duration)

		key_parts = [f"[{timestamp}]", f"[{encrypted_duration}]"]

		for k, v in dic.items():
			# Convert both key and value to strings before encryption
			key_parts.append(f"[{self.encrypt(str(k))}]" + f"[{self.encrypt(str(v))}]")

		return ''.join(key_parts)

	def keyCheck(self, key, dic=None):
		if dic is None:
			dic = {}
		self.log.append(f"Dictionary Received for KeyCheck: {str(dic)}")

		# Parse the key into its components
		rec = self.parseKey(key)
		if not rec or 'timestamp' not in rec or 'duration' not in rec:
			self.log.append(f"Invalid Key Structure: {str(rec)}")
			return False

		# Decrypt and validate the duration
		try:
			duration = self.decrypt(rec['duration'])
			self.log.append(f"Decrypted Duration: {str(duration)}")
		except Exception as e:
			self.log.append(f"Decryption of duration failed: {e}")
			return False

		# Check if the timestamp is within the allowed duration
		if not self.check(rec['timestamp'], duration):
			self.log.append("Timestamp validation failed.")
			return False

		# Validate dictionary key-value pairs
		for encrypted_key, encrypted_value in rec['keys'].items():
			try:
				key_decrypted = self.decrypt(encrypted_key)
				value_decrypted = self.decrypt(encrypted_value)
				self.log.append(f"Decrypted Key: {key_decrypted}, Decrypted Value: {value_decrypted}")
			except Exception as e:
				self.log.append(f"Decryption failed for key-value pair: {encrypted_key}-{encrypted_value}, Error: {e}")
				return False

			# Retrieve expected value from the dictionary and compare
			expected_value = dic.get(key_decrypted)
			self.log.append(f"Comparing: Expected {expected_value}, Got {value_decrypted}")

			# Normalize both values to strings before comparison
			if str(expected_value) != str(value_decrypted):
				self.log.append(f"Dictionary mismatch at key '{key_decrypted}': Expected {str(expected_value)}, Got {str(value_decrypted)}")
				return False

		return True




	def parseKey(self, input):
		matches = re.findall(r'\[(.*?)\]', input)
		if len(matches) < 2 or len(matches) % 2 != 0:
			self.log.append(f"Key parsing failed. Matches: {str(matches)}")
			return False

		keys = {matches[i]: matches[i + 1] for i in range(2, len(matches), 2)}
		logItem = {"timestamp": matches[0], "duration": matches[1], "keys": keys}
		self.log.append(f"Parsed Key: {str(logItem)}")
		return {
			'timestamp': matches[0],
			'duration': matches[1],
			'keys': keys
		}


def fixJSON(pseudo_json,i=False):
	import re
	import json
	pseudo_json = pseudo_json.replace("'", '"')
	pseudo_json = re.sub(r'(?<!")(\b[a-zA-Z_][a-zA-Z0-9_]*\b)(?!")(?=\s*:)', r'"\1"', pseudo_json)
	pseudo_json = re.sub(r':\s*([a-zA-Z_][a-zA-Z0-9_]*)(?!")(?=\s*[},])', r': "\1"', pseudo_json)
	try:
		json_obj = json.loads(pseudo_json)
		# Return the formatted JSON string
		if i:
			return json.dumps(json_obj, indent=4)
		else:
			return json.dumps(json_obj)
	except json.JSONDecodeError as e:
		raise ValueError(f"Invalid pseudo-JSON string: {e}")

def encodeURL(input_string):
	import urllib.parse
	return urllib.parse.quote(input_string)

def action():
	manager = ephemeralLinkManagerAES()
	if _.switches.isActive('Password'):
		password = ' '.join(_.switches.values('Password'))
		curlPassword = password
	else:
		curlPassword = False
		password = None
	curl = None
	if _.switches.isActive('Gen'):
		result = manager.gen()
		if not curlPassword:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?check='+encodeURL(result)+'"'
		else:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?check='+encodeURL(result)+'&password='+encodeURL(password)+'"'
	elif _.switches.isActive('Check'): # en, duration
		result = manager.check(_.switches.values('Check')[0], _.switches.values('Check')[1])
	elif _.switches.isActive('Encrypt'):
		result = manager.encrypt(_.switches.values('Encrypt')[0], password)
		if not curlPassword:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?decrypt='+encodeURL(result)+'"'
		else:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?decrypt='+encodeURL(result)+'&password='+encodeURL(password)+'"'
	elif _.switches.isActive('Decrypt'):
		result = manager.decrypt(_.switches.values('Decrypt')[0],password)
		if not curlPassword:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?encrypt='+encodeURL(result)+'"'
		else:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?encrypt='+encodeURL(result)+'&password='+encodeURL(password)+'"'
	elif _.switches.isActive('KeyGen'): # duration dic
		try:
			import json
			# JSON = _.switches.values('KeyGen')[1].replace("'", '"')
			JSON = fixJSON(_.switches.values('KeyGen')[1])
			dic = json.loads(JSON)
		except:
			dic = None
		result = manager.keyGen(_.switches.values('KeyGen')[0], dic )
		if dic is None:
			curlDic = ''
		else:
			curlDic = '&dic='+encodeURL(JSON)

		if not curlPassword:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?keyCheck='+encodeURL(result)+curlDic+'"'
		else:
			curl = 'curl -s "https://cli.sds.sh/ephemeral/?keyCheck='+encodeURL(result)+curlDic+'&password='+encodeURL(password)+'"'
	elif _.switches.isActive('KeyCheck'):
		import json
		try:
			# JSON = _.switches.values('KeyCheck')[1].replace("'", '"')
			JSON = fixJSON(_.switches.values('KeyCheck')[1])
			dic = json.loads(JSON)
		except:
			dic = None
		# print(dic); _.isExit(__file__)
		# print( json.dumps(dic) ); _.isExit(__file__)
		result = manager.keyCheck(_.switches.values('KeyCheck')[0],dic)

	elif _.switches.isActive('EncodeStringForURL'):
		string = ''.join(_.switches.values('EncodeStringForURL'))
		if '{' in string: string = fixJSON(string)
		print(string)
		result = encodeURL(string)
	end = False
	if _.switches.isActive('CurlReverse') and not curl is None:
		if 'url' in _.switches.value('CurlReverse'):
			curl = curl.replace('curl -s','').replace('"','').strip()
			CURL = curl
		else:
			if 'wsl' in _.switches.value('CurlReverse'):
				CURL = 'wsl ' +curl
			else:
				CURL = curl
		if 'just' in _.switches.value('CurlReverse'):
			if not 'url' in _.switches.value('CurlReverse'):
				print( _.hp(CURL) )
			else:
				_.pr(CURL,c='yellow')
			return None
		else:
			_.pr()
			end = CURL
	if _.switches.isActive('EncodeForURL') and not _.switches.isActive('EncodeStringForURL'):
		result = encodeURL(result)

	_.pr(result,c='green')

	if end:
		_.pr()
		_.pr(end,c='yellow')
		_.pr()

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);