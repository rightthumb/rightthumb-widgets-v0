import _rightThumb._construct as __
import sys
# Column

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# Switch
# import _rightThumb._string as _str

'''

		line = cleanFirst(line,' ')
		line = cleanLast(line,' ')

replaceAll(string,rWhat,rWith)
cleanAll(string,rWhat,rWith)
removeAll(string,rWhat)


_str.replaceDuplicate(string,rWhat)
_str.cleanBE(string,rWhat)
_str.cleanEnd(string,' ')
_str.cleanFirst(string,' ')

row = _str.replaceDuplicate( row, ' ' )
row = _str.cleanBE( row, ' ' )


_str.cleanEnd(string,rWhat)

row = row.replace( '\n', '' )
row = row.replace( '\r', '' )
row = _str.replaceDuplicate( row, ' ' )
row = _str.replaceDuplicate( row, '\t' )
row = _str.cleanBE( row, ' ' )
row = _str.cleanBE( row, '\t' )
if not row.startswith( '#' ):


_str.stripNonAlphaNumaric(string)
_str.charFix(string)
_str.autoFloatInt(string)
_str.removeNonNumber(string)
_str.removeNonAlpha2(string)
_str.replaceDuplicate(string,rWhat)
_str.cleanBE(string,rWhat)


keys = ','.join(rec.keys())
question_marks = ','.join(list('?'*len(rec)))
values = tuple(rec.values())

if len(list( filter(lambda itemX: itemX['name'] == field, theListName) )) == 0:

_str.safeChar

https://stackoverflow.com/questions/2049502/what-characters-are-allowed-in-an-email-address

_str.hasAlpha( row )
'''

## Start: Latest Version
import platform
import re

# Set slash character depending on OS
slash = chr(92) if platform.system() == 'Windows' else chr(47)

# Common character sets
upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerChar = 'abcdefghijklmnopqrstuvwxyz'
alphaChar = lowerChar + upperChar
printable = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
printable2 = printable + '🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷🛶🥕🍒🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🖕🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈🐳🦑🚀🙈🙊🙉🌮🥒🐅🐯🍉🚽🍅👅🎩🍷'
alphanumeric = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
safeChar = printable
visibleChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
notFilenameSafe = '/\\?%*:|"<>'
safe = alphanumeric + '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c' + '¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿'
safe2 = safe + 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß' + 'àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'

# ────────────────────────────
# Utility Functions
# ────────────────────────────

def randomStr(s):
	import random
	char_list = list(s)
	random.shuffle(char_list)
	return ''.join(char_list)

def printClean(text):
	text = str(text)
	return ''.join([x for x in text if x in printable])

def minimalistClean(row):
	result = ''.join([x if x in printable else ' ' for x in row])
	result = replaceDuplicate(result, ' ')
	result = cleanBE(result, ' ')
	return result

def hasAlpha(row):
	row = str(row)
	for r in row:
		if r in alphaChar:
			return True
	return False

def totalClean(row):
	row = row.replace('\n', '').replace('\r', '')
	row = replaceDuplicate(row, ' ')
	row = replaceDuplicate(row, '\t')
	row = cleanBE(row, ' ')
	row = cleanBE(row, '\t')
	return row

def filenameSafe(data):
	data = str(data)
	result = ''.join([d if d in printable and d not in notFilenameSafe else ' ' for d in data])
	result = replaceDuplicate(result, ' ')
	result = cleanBE(result, ' ')
	return result

def hasVisible(data):
	for char in data:
		if char in visibleChar:
			return True
	return False

def removeUnsave(data):
	return ''.join([char for char in data if char in safeChar])

def spaceba(string, what):
	if what in string:
		i = 0
		while f' {what}' in string or f'{what} ' in string:
			i += 1
			if i > 1000: break
			string = string.replace(f' {what}', what)
			string = string.replace(f'{what} ', what)
	return string

def makePrintable(string, replaceWith=' ', appropriate=False):
	if appropriate is False:
		appropriate = safeChar
	result = ''.join([char if char in appropriate else replaceWith for char in string])
	result = replaceDuplicate(result, replaceWith)
	result = cleanBE(result, replaceWith)
	return result

def namespace(app, data):
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
	data = makePrintable(data, replaceWith=' ', appropriate=chars)
	for row in data.split(' '):
		if row.startswith(str(app) + '.'):
			return row
	return False

def _ws():
	string = __.imp('string')
	return string.whitespace











# ════════════════════════════════════════════════════════════════════════════════
# Legacy String Utilities
# Full Module: Cleaners, Strip Functions, Type Checkers, Character Fixes
# Preserved in original functionality, cleaned formatting, ready for production
# ════════════════════════════════════════════════════════════════════════════════

# SECTION: Basic Replace and Cleanup Utilities

def replaceAll(string, rWhat, rWith):
	if not len(rWhat):
		return string
	if rWhat not in string:
		return string
	tmp = '{C9DCAA81-3B8A-68E9-E4CF-A405E2199CB9}'
	while rWhat in string:
		string = string.replace(rWhat, tmp)
	while tmp in string:
		string = string.replace(tmp, rWith)
	return string

def removeAll(string, rWhat):
	if not len(rWhat):
		return string
	if rWhat not in string:
		return string
	return replaceAll(string, rWhat, '')

def replaceDuplicate(string, rWhat):
	if not isinstance(string, str):
		return string
	if not len(rWhat):
		return string
	if rWhat not in string:
		return string
	while rWhat + rWhat in string:
		string = string.replace(rWhat + rWhat, rWhat)
	return string

def cleanFirst(string, rWhat):
	if not len(rWhat) or rWhat not in string:
		return string
	while string.startswith(rWhat):
		string = string[len(rWhat):]
	return string

def cleanEnd(string, rWhat):
	if not len(rWhat) or rWhat not in string:
		return string
	while string.endswith(rWhat):
		string = string[:-len(rWhat)]
	return string

def cleanBE(string, rWhat):
	return cleanFirst(cleanEnd(string, rWhat), rWhat)

def cleanAll(string, rWhat, rWith):
	while rWhat in string:
		string = string.replace(rWhat, rWith)
	return string

# SECTION: Strip Functions

def totalStrip(line):
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\""
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip1b(line, add=''):
	permitted = " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + (add or '')
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip2(line):
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip2b(line):
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_ "
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip3(line):
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-,"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip4(line):
	permitted = "0123456789"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip5(line):
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip6(line):
	line = characterClean(removeAll(removeAll(line, '\n'), '\r'))
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip7(line):
	line = underscore(removeAll(removeAll(line, '\n'), '\r'))
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip8(line):
	line = characterClean(removeAll(removeAll(line, '\n'), '\r'))
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	return ' '.join(''.join(c for c in word if c in permitted) for word in line.split())

def totalStrip9(line):
	line = underscore(removeAll(removeAll(line, '\n'), '\r'))
	permitted = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
	result = ''.join(char if char in permitted else ' ' for char in line)
	return replaceDuplicate(cleanBE(result, ' '), ' ')

def underscore(line):
	return line.replace('\u005F', ' ').replace('\uFF3F', ' ').replace('\u2017', ' ').replace('\u203E', ' ').replace('\u0332', ' ').replace('_', ' ')

# SECTION: Type and Numeric Utilities

def isInt(data):
	return isinstance(data, int) or (isinstance(data, str) and data.isdigit())

def isFloat(data):
	try:
		float(data)
		return '.' in str(data) and not isInt(data)
	except:
		return False

def autoFloatInt(data):
	if isInt(data):
		return int(data)
	elif isFloat(data):
		return float(data)
	return data

def onlyDigits(line):
	permitted = "0123456789-"
	return ''.join(c if c in permitted else ' ' for c in characterClean(removeAll(removeAll(line, '\n'), '\r')))

def removeNonAlpha(string):
	permitted = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return ''.join(c for c in str(string) if c in permitted)

def removeNonNumber(string):
	return ''.join(c for c in str(string) if c.isdigit())

# SECTION: Character Cleaning Utilities

def characterClean(string):
	return string.replace('\xe2\x80\x9c','\"').replace('\xe2\x80\x9d','\"').replace('\xe2\x80\x99',"'").replace('\xe2\x80\x93','-')

def cleanupString(string, beforeAfter=True):
	string = replaceAll(string, '\n', ' ')
	string = replaceAll(string, '\t', ' ')
	string = replaceDuplicate(string, ' ')
	string = cleanFirst(string, ' ')
	string = cleanLast(string, ' ')
	string = characterClean(string)
	if beforeAfter:
		string = string.split('(')[0]
	else:
		string = string.split('(')[-1]
	string = string.split('/')[0]
	return string.strip()

# SECTION: do() Dispatcher

def do(what=None, string='', a=None, b=None, c=None, d=None):
	if what in 'an alphan'.split(): return totalStrip1b(string, a)
	if what in 'file'.split(): return clean_filename(string, a, b, c)
	if what == 'trim': return string.strip()
	if what == 'nows': return ''.join(string.split())
	if what == 'all': return replaceAll(string, a, b)
	if what == 'cleanAll': return cleanAll(string, a, b)
	if what == 'dup': return replaceDuplicate(string, a)
	if what == 'be': return cleanBE(string, a)
	if what == 'b': return cleanFirst(string, a)
	if what == 'e': return cleanEnd(string, a)
	if 'alpha' in what and 'nu' in what: return totalStrip1b(string)
	if what in 'n'.split(): return removeNonNumber(string)
	if what in 'ra remove'.split(): return removeAll(string, a)
	return string

# SECTION: JSON Classes

class st(str):
	def all(self,a,b): return do('all',self,a,b)
	def cleanAll(self,a,b): return do('cleanAll',self,a,b)
	def dup(self,a): return do('dup',self,a)
	def be(self,a): return do('be',self,a)
	def b(self,a): return do('b',self,a)
	def e(self,a): return do('e',self,a)
	def alpha(self): return do('n',self)
	def num(self): return do('nu',self)
	def remove(self,a): return do('remove',self,a)
	def ra(self,a): return do('remove',self,a)
	def json(self):
		import json
		result = json.loads(self)
		return dic(result) if isinstance(result, dict) else lis(result)

class dic(dict):
	def string(self):
		import json
		return json.dumps(self, indent=4)
	def inline(self):
		import json
		return json.dumps(self)

class lis(list):
	def string(self):
		import json
		return json.dumps(self, indent=4)
	def inline(self):
		import json
		return json.dumps(self)


## END: Latest Version
## END: Latest Version
## END: Latest Version
## END: Latest Version






























## Legacy
import platform
slash = 0
if platform.system() == 'Windows':
	slash = chr(92)
else:
	slash = chr(47)

import re

upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerChar = 'abcdefghijklmnopqrstuvwxyz'
alphaChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
printable = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~ \t\n\r\x0b\x0c'
printable2 = printable + '🧻🧪💀🦆🦉🥓🦄🦀🖕🍣🍤🍥🍡🥃🥞🐕👾🐉🐓🐋🐌🐢👽👿🥑🐡🐗💐🏹🎨🐔🐛🎯🌯📷🛶🥕🍒🍸🍳🐲🎣🐟🦅👀🐸🤞💪💾👻🐊🍔🌭🍀🕓🦊🍟🥝🖕🐒🥞🐼📎🐧💩🍕🍍🦏🍗🌈🐳🦑🚀🙈🙊🙉🌮🥒🐅🐯🍉🚽🍅👅🎩🍷'
alphanumeric = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
safeChar = printable
visibleChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
notFilenameSafe = '/\\?%*:|"<>'
safe = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~ \t\n\r\x0b\x0c' + '¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿'
safe2 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~ \t\n\r\x0b\x0c' + '¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿' + 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß' + 'àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ'



def randomStr(s):
	import random
	char_list = list(s)
	random.shuffle(char_list)
	return ''.join(char_list)

def printClean(text):
	global printable
	text = str(text)
	fix = []
	for x in text:
		if x in printable:
			fix.append(x)
	return ''.join(fix)

def minimalistClean( row ):
	global printable
	result = ''
	for x in row:
		if not x in printable:
			result+=' '
		else:
			result+=x
	result = replaceDuplicate( result, ' ' )
	result = cleanBE( result, ' ' )
	return result




def hasAlpha( row ):
	row = str(row)
	global alphaChar
	for r in row:
		for a in alphaChar:
			if r == a:
				return True
	return False

def totalClean( row ):
	row = row.replace( '\n', '' )
	row = row.replace( '\r', '' )
	row = replaceDuplicate( row, ' ' )
	row = replaceDuplicate( row, '\t' )
	row = cleanBE( row, ' ' )
	row = cleanBE( row, '\t' )
	return row



def filenameSafe( data ):
	global printable
	global notFilenameSafe

	PERMITTED_CHARS = printable
	data = str( data )

	result = ''
	for d in data:
		if d in PERMITTED_CHARS and not d in notFilenameSafe:
			result += d
		else:
			result += ' '
	result = replaceDuplicate( result, ' ' )
	result = cleanBE( result, ' ' )
	return result



def hasVisible( data ):
	global visibleChar
	for char in data:
		if char in visibleChar:
			return True
	return False

def removeUnsave( data ):
	global safeChar
	result = ''
	for char in data:
		if char in safeChar:
			result += char
	return result

def spaceba( string, what ):
	# import string
	if what in string:
		i=0
		while ' '+what in string or what+' ' in string:
			i=i+1
			if i > 1000: break
			string = string.replace( ' '+what, what )
			string = string.replace( what+' ', what )
	return string


def makePrintable( string, replaceWith=' ', appropriate=False ):
	global safeChar
	if type(appropriate) == bool:
		appropriate = printable
	result = ''

	for char in string:
		if char in appropriate:
			result += char
		else:
			result += replaceWith
	result = replaceDuplicate( result, replaceWith )
	result = cleanBE( result, replaceWith )
	return result

def namespace( app, data ):
	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
	data = makePrintable( data, replaceWith=' ', appropriate=string )
	result = False
	# _.pr( type( app ) )
	for row in data.split(' '):
		if row.startswith( str(app)+'.' ):
			result = row
	# try:
	# except Exception as e:
	#   return app, result

	return result

def _ws():
	string=__.imp('string')
	return string.whitespace


# import MySQLdb

############################################### ###############################################

LATIN_1_CHARS = (
	( '\xe2\x80\x99', "'" ),
	( '\xc3\xa9', 'e' ),
	( '\xe2\x80\x90', '-' ),
	( '\xe2\x80\x91', '-' ),
	( '\xe2\x80\x92', '-' ),
	( '\xe2\x80\x93', '-' ),
	( '\xe2\x80\x94', '-' ),
	( '\xe2\x80\x94', '-' ),
	( '\xe2\x80\x98', "'" ),
	( '\xe2\x80\x9b', "'" ),
	( '\xe2\x80\x9c', '"' ),
	( '\xe2\x80\x9c', '"' ),
	( '\xe2\x80\x9d', '"' ),
	( '\xe2\x80\x9e', '"' ),
	( '\xe2\x80\x9f', '"' ),
	( '\xe2\x80\xa6', '...' ),
	( '\xe2\x80\xb2', "'" ),
	( '\xe2\x80\xb3', "'" ),
	( '\xe2\x80\xb4', "'" ),
	( '\xe2\x80\xb5', "'" ),
	( '\xe2\x80\xb6', "'" ),
	( '\xe2\x80\xb7', "'" ),
	( '\xe2\x81\xba', "+" ),
	( '\xe2\x81\xbb', "-" ),
	( '\xe2\x81\xbc', "=" ),
	( '\xe2\x81\xbd', "( " ),
	( '\xb3', '' ),
	( '\xe2\x81\xbe', ")" )
)

def xChar( data ):
	global slash
	char = 'abcdefghijklmnopqrstuvwxyz0123456789'

	for x in char:
		for y in char:
			data = data.replace( slash+'x' + x + y, ' ' )
	
	data = replaceDuplicate( data, ' ' )
	data = cleanBE( data, ' ' )

	return data


def clean_latin1( data ):
	global LATIN_1_CHARS
	global slash
	# data = str( data )
	data = data.encode('latin1', 'ignore')
	data = data.decode('latin1')
	# Source: https://gist.github.com/tushortz/9fbde5d023c0a0204333267840b592f9
	# data = data.encode('utf-8')
	# try:
	#   pass
	#   # return data.encode('latin1')
	#   # return data.encode('utf-8')
	#   data = data.decode('iso-8859-1')
	# except UnicodeDecodeError:
	#   pass
	for _hex, _char in LATIN_1_CHARS:
		data = data.replace( _hex, _char )
	# return data.encode('utf8')
	# return data.encode('latin1')
	data = data.replace( 'Alien\\xb3', 'Alien 3' )
	if slash+'x' in data:
		data = xChar( data )
	return data

def cleanChar( data ):
	# data = str( data )
	
	# Source: https://stackoverflow.com/questions/6539881/python-converting-from-iso-8859-1-latin1-to-utf-8

	# data = data.encode('ascii', 'ignore') 
	# data = data.decode('latin1').encode('utf8').rstrip()
	# data = data.decode('utf8').encode('latin1', 'ignore') 
	# data = str( data )
	# data = str( data )
	data = clean_latin1( data )
	# data = data.encode('ascii', 'ignore')
	data = data.encode('latin1', 'ignore')
	# data = data.decode('latin1').encode('utf8')
	# data = data.decode('utf8').encode('latin1', 'ignore') 
	data = data.decode('latin1')
	# data = str( data )
	return data

############################################### ###############################################

def stripNonAlphaNumaric( data, also='' ):
	PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' + also
	data = str( data )

	result = ''
	for d in data:
		if d in PERMITTED_CHARS:
			result += d
		else:
			result += ' '
	result = replaceDuplicate( result, ' ' )
	result = cleanBE( result, ' ' )
	return result


def autoFloatInt( data ):
	if isInt( data ):
		return int( data )
	if isFloat( data ):
		return float( data )
	return data

def isInt( data ):
	data = str( data )
	d = '0123456789'
	result = True
	for c in data:
		if not c in d:
			result = False
	return result

def isFloat( data ):
	data = str( data )
	result = True
	if isInt( data ):
		result = False
	else:
		try:
			float( data )
		except Exception as e:
			result = False

	return result

def removeNonNumber( string ):
	PERMITTED_CHARS = '0123456789'
	string = str(string)

	result = ''

	for cha in string:
		if cha in PERMITTED_CHARS:
			result += cha
	return result

def removeNonAlpha( string ):
	PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	string = str(string)

	result = ''

	for cha in string:
		if cha in PERMITTED_CHARS:
			result += cha
	return result

def removeNonAlpha2( string ):
	PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
	string = str(string)

	result = ''

	for cha in string:
		if cha in PERMITTED_CHARS:
			result += cha
	return result

def padZeros(string,count):
	string = str(string)

	diff = count - len(string)
	pre = ''
	for x in range(1,diff+1):
		pre += '0'
	result = pre + string
	return result


def replaceAll(string,rWhat,rWith):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	tmp = '{C9DCAA81-3B8A-68E9-E4CF-A405E2199CB9}'


	done=False
	string = str(string)
	while done == False:
		if string.count(str(rWhat)) > 0:
			string = string.replace(str(rWhat),tmp)
		else:
			done=True


	done=False
	string = str(string)
	while done == False:
		if string.count(str(rWhat)) > 0:
			string = string.replace(str(rWhat),tmp)
		else:
			done=True



	done=False
	while done == False:
		if string.count(tmp) > 0:
			string = string.replace(tmp,str(rWith))
		else:
			done=True

	string = string.replace(tmp,str(rWith))
	return string
# def replaceAll(string,rWhat,rWith):
#   if not rWhat == rWith:
#       done=False
#       while done == False:
#           if string.count(rWhat) > 0:
#               string = string.replace(rWhat,rWith)
#           else:
#               done=True
#   return string

def removeAll(string,rWhat):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	rWith = ''
	return replaceAll(string,rWhat,rWith)

def replaceDuplicate(string,rWhat):
	if not type(string) == str: return string;
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	string = str(string)
	rWith = str(rWhat)

	while rWhat+rWhat in string: string = string.replace(rWhat+rWhat,rWhat)

	# rWhat = 
	# string = replaceAll(string,rWhat,rWith)
	# for x in range(10):
	#     string = string.replace( rWhat, rWith )
	return string

def cleanBE(string,rWhat):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	string = cleanEnd(string,rWhat)
	string = cleanFirst(string,rWhat)
	return string
def cleanEnd(string,rWhat):
	if not rWhat in string:
		return string
	string = str(string)
	rWhat = str(rWhat)
	# string = replaceDuplicate(string,rWhat)
	while string.endswith(rWhat): string=string[:-1]

	# string +=  '*?*'
	# string = string.replace(rWhat + '*?*', '')
	# string = string.replace('*?*', '')
	if string.endswith(rWhat):
		string = cleanEnd(string,rWhat)

	return string

def cleanEnd2(string,rWhat):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	string = str(string)
	rWhat = str(rWhat)
	string = totalStrip3(string)
	string = cleanSpecial(string)
	string = replaceDuplicate(string,rWhat)
	string +=  '*?*'
	string = string.replace(rWhat + '*?*', '')
	string = string.replace('*?*', '')
	return string

def cleanLast(string,rWhat):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	return cleanEnd(string,rWhat)

def cleanFirst(string,rWhat):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	string = str(string)
	rWhat = str(rWhat)

	while string.startswith(rWhat): string=string[1:]

	# string = replaceDuplicate(string,rWhat)
	# string = '*?*' + str(string)
	# string = string.replace('*?*' + rWhat, '')
	# string = string.replace('*?*', '')
	if string.startswith(rWhat):
		string = cleanFirst(string,rWhat)
	return string

def cleanAll(string,rWhat,rWith):
	if not len(rWhat): return string;
	if not rWhat in string:
		return string
	done=False
	while done == False:
		if string.count(rWhat) > 0:
			string = string.replace(rWhat,rWith)
		else:
			done=True
	return string
def cleanSpecial(line,special1=False):
	global slash
	line = str(line)
	if line.startswith("b'") and line.endswith("'"): line=line[:-1]; line=line[2:];
	if not len(line): return line
	OG_MF=line[0]
	if not special1:
		line = replaceAll(str(line),slash,'--/--')
		try:
			pass
			line = line.encode('latin-1')
			line = str(line)
			if line.startswith("b'") and line.endswith("'"): line=line[:-1]; line=line[2:];
			line = replaceAll(line,slash+'t',' ')
			line = replaceAll(line,slash+'xa0',' ')
			line = replaceAll(line,slash+'xe9',"'")
			line = replaceDuplicate(line,' ')
			line = cleanFirst(line,' ')
			line = cleanLast(line,' ')
		except Exception as e:
			pass
			try:
				line = line.encode('utf-8')
				pass
			except Exception as e:
				pass
	else:
		line = replaceAll(line,'\u0092',"'")
	try:
		line = line.replace('…','...')
	except Exception as e:
		pass
	if line.startswith("b'") and line.endswith("'"): line=line[:-1]; line=line[2:];
	i = 0
	skip = False
	string = ''
	for char in str(line):
		# _.pr(item)
		char = str(char)
		if char == slash:
			i = 0
			skip = True
		if skip == True:
			if i == 4:
				i = 0
				skip = False
			else:
				i += 1
		if skip == False:
			string += char
		else:
			string += ' '

	# line = string
	if not special1:
		line = replaceAll(str(line),'--/--',slash)
		# line = replaceAll(str(line),'_-_',',')
		line = replaceDuplicate(str(line),  ' ')
		line = cleanEnd(str(line),'"')
		line = cleanEnd(str(line),"'")
		line = cleanEnd(str(line),' ')
		line = cleanFirst(str(line),"b'")
		line = cleanFirst(str(line),'b"')
		line = cleanFirst(str(line),'.')
		# line = line.replace('  ',' ')
	# if not OG_MF[0]==line[0] and len(line) > len(OG_MF) and line.startswith("'"): line=line[1:]
	return line

def cleanSpecial2(line,special1=False):
	global slash
	line = str(line)
	def cleanup(line):
		line = replaceAll(line,slash+'t',' ')
		line = replaceAll(line,slash+'xc3',' ')
		
		line = replaceAll(line,slash+'xb1',' ')
		line = replaceAll(line,slash+'xf3',' ')
		line = replaceAll(line,slash+'xf6',' ')
		line = replaceAll(line,slash+'xe4',' ')

		line = replaceAll(line,slash+'xa0',' ')
		line = replaceAll(line,slash+'xe9',"'")
		line = replaceAll(line,slash+'xe2\\x80\\x93','-')
		line = replaceAll(line,slash+'\\xe2\\\\x80\\\\x93','-')
	if not special1:
		line = replaceAll(str(line),slash,'--/--')
		try:
			pass
			try:
				line = cleanup(line)
				line = line.decode('utf-8','ignore')
			except Exception as e:
				pass
			try:
				line = cleanup(line)
				line = line.encode('utf-8').decode('utf-8')
			except Exception as e:
				pass
			try:
				line = cleanup(line)
				line = line.encode('latin-1')
			except Exception as e:
				pass
			try:
				line = cleanup(line)
				line = line.encode('latin-1').decode('latin-1')
			except Exception as e:
				pass
			try:
				line = cleanup(line)
			except Exception as e:
				pass



			line = replaceDuplicate(line,' ')
			line = cleanFirst(line,' ')
			line = cleanLast(line,' ')
		except Exception as e:
			try:
				line = line.encode('utf-8')
				pass
			except Exception as e:
				pass
	else:
		line = replaceAll(line,'\u0092',"'")
	try:
		line = line.replace('…','...')
	except Exception as e:
		pass
	i = 0
	skip = False
	string = ''
	for char in str(line):
		# _.pr(item)
		char = str(char)
		if char == slash:
			i = 0
			skip = True
		if skip == True:
			if i == 4:
				i = 0
				skip = False
			else:
				i += 1
		if skip == False:
			string += char
		else:
			string += ' '

	# line = string
	if not special1:
		line = replaceAll(str(line),'--/--',slash)
		# line = replaceAll(str(line),'_-_',',')
		line = replaceDuplicate(str(line),  ' ')
		line = cleanEnd(str(line),'"')
		line = cleanEnd(str(line),"'")
		line = cleanEnd(str(line),' ')
		line = cleanFirst(str(line),"b'")
		line = cleanFirst(str(line),'b"')
		line = cleanFirst(str(line),'.')
		# line = line.replace('  ',' ')
	return line

def totalStrip(line):
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\""
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def alpha(line):
	PERMITTED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'"
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip1b(line,add=''):
	if add is None: add='';
	PERMITTED_CHARS = " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+add
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip2(line):
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-" 
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip2b(line):
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_ " 
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip3(line):
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-," 
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip4(line):
	PERMITTED_CHARS = "0123456789" 
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip5(line):
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ''
	# line = section + ']'
	# line = line.replace(' ]','')
	# line = line.replace(']','')
	return line
def totalStrip6(line):
	line = removeAll(line,'\n')
	line = removeAll(line,'\r')
	line = characterClean(line)
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def totalStrip9(line):
	line = removeAll(line,'\n')
	line = removeAll(line,'\r')
	line = underscore(line)
	# line = cleanupString(line)
	# line = cleanSpecial2(line)
	# line = characterClean(line)
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
	section = ''
	for cha in line:
		if cha in PERMITTED_CHARS:
			section += cha
		else:
			section += ' '
	line = section
	line = cleanBE(line,' ')
	line = replaceDuplicate(line,' ')
	return line
def underscore(line):
	# http://www.fileformat.info/
	line = line.replace('\u005F',' ')
	line = line.replace('\uFF3F',' ')
	line = line.replace('\u2017',' ')
	line = line.replace('\u203E',' ')
	line = line.replace('\u0332',' ')
	line = line.replace('_',' ')
	return line

def totalStrip7(line):
	line = removeAll(line,'\n')
	line = removeAll(line,'\r')
	line = underscore(line)
	# line = cleanupString(line)
	# line = cleanSpecial2(line)
	# line = characterClean(line)
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section
	line = cleanBE(line,' ')
	line = replaceDuplicate(line,' ')
	return line
def onlyDigits(line):
	line = removeAll(line,'\n')
	line = removeAll(line,'\r')
	line = characterClean(line)
	PERMITTED_CHARS = "0123456789-"
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def onlyDigits2(line):
	line = str( line )
	line = line.replace( '–', '-' )
	PERMITTED_CHARS = '0123456789-'
	result = ''
	for char in line:
		if char in PERMITTED_CHARS:
			result += char
	return result
def totalStrip8(line):
	line = removeAll(line,'\n')
	line = removeAll(line,'\r')
	line = characterClean(line)
	PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.,-@:'#\"()"
	section = ''
	for word in line.split(' '):
		section += ''.join(c for c in word if c in PERMITTED_CHARS)
		section += ' '
	line = section + ']'
	line = line.replace(' ]','')
	line = line.replace(']','')
	return line
def cleanupString0(string):
	string = replaceAll(string,'\n',' ')
	string = replaceDuplicate(string,' ')
	string = cleanLast(string,' ')
	string = cleanFirst(string,' ')
	string = cleanSpecial(string)
	string = cleanFirst(string,' ')
	return string
def cleanupString(string,beforeAfter=True):
	string = replaceAll(string,'\n',' ')
	string = replaceAll(string,'\t',' ')
	string = replaceDuplicate(string,' ')
	string = cleanLast(string,' ')
	string = cleanFirst(string,' ')
	string = cleanSpecial(string)
	string = cleanFirst(string,' ')
	string = string.replace(slash+'xe2\\x80\\x93','-')
	string = string.replace(slash+'\\xe2\\\\x80\\\\x93','-')
	if beforeAfter:
		string = string.split('(')[0]
	else:
		string = string.split('(')[1]
	string = string.split('/')[0]
	return string

def characterClean(string):
	global slash
	string = string.replace('\xe2\x80\x9c','"').replace('\xe2\x80\x9d','"').replace('\xe2\x80\x99',"'").replace(slash+'xe2\\x80\\x93','-')
	# string = string.encode('latin-1')
	return string

def basic(string):
	pattern = re.compile(r'([^\s\w]|_)+')
	string = pattern.sub('', string)
	string = replaceDuplicate(string, ' ')
	string = cleanFirst(string, ' ')
	string = cleanLast(string, ' ')

	return string

def charFix( string ):
	global slash
	global charFixData
	for ch in charFixData:
		chs = ch[1].split(',')
		for c in chs:
			string = string.replace( slash+c, ch[0] )
	return string

charFixData = ['','x00'],
['','x01'],
['','x02'],
['','x03'],
['','x04'],
['','x05'],
['','x06'],
['','x07'],
['','x08'],
['','x09'],
['','x0a'],
['','x0b'],
['','x0c'],
['','x0d'],
['','x0e'],
['','x0f'],
['','x10'],
['','x11'],
['','x12'],
['','x13'],
['','x14'],
['','x15'],
['','x16'],
['','x17'],
['','x18'],
['','x19'],
['','x1a'],
['','x1b'],
['','x1c'],
['','x1d'],
['','x1e'],
['','x1f'],
['','x20'],
['!','x21'],
[''','x22'],
['#','x23'],
['$','x24'],
['%','x25'],
['&','x26'],
[''','x27'],
['(','x28'],
[')','x29'],
['*','x2a'],
['+','x2b'],
[',','x2c'],
['-','x2d'],
['.','x2e'],
['/','x2f'],
['0','x30'],
['1','x31'],
['2','x32'],
['3','x33'],
['4','x34'],
['5','x35'],
['6','x36'],
['7','x37'],
['8','x38'],
['9','x39'],
[':','x3a'],
[';','x3b'],
['<','x3c'],
['=','x3d'],
['>','x3e'],
['?','x3f'],
['@','x40'],
['A','x41'],
['B','x42'],
['C','x43'],
['D','x44'],
['E','x45'],
['F','x46'],
['G','x47'],
['H','x48'],
['I','x49'],
['J','x4a'],
['K','x4b'],
['L','x4c'],
['M','x4d'],
['N','x4e'],
['O','x4f'],
['P','x50'],
['Q','x51'],
['R','x52'],
['S','x53'],
['T','x54'],
['U','x55'],
['V','x56'],
['W','x57'],
['X','x58'],
['Y','x59'],
['Z','x5a'],
['[','x5b'],
['','x5c'],
[']','x5d'],
['^','x5e'],
['_','x5f'],
['','x60'],
['a','x61'],
['b','x62'],
['c','x63'],
['d','x64'],
['e','x65'],
['f','x66'],
['g','x67'],
['h','x68'],
['i','x69'],
['j','x6a'],
['k','x6b'],
['l','x6c'],
['m','x6d'],
['n','x6e'],
['o','x6f'],
['p','x70'],
['q','x71'],
['r','x72'],
['s','x73'],
['t','x74'],
['u','x75'],
['v','x76'],
['w','x77'],
['x','x78'],
['y','x79'],
['z','x7a'],
['{','x7b'],
['|','x7c'],
['}','x7d'],
['~','x7e'],
['','x7f'],
['','xc2,x80'],
['','xc2,x81'],
['','xc2,x82'],
['','xc2,x83'],
['','xc2,x84'],
['','xc2,x85'],
['','xc2,x86'],
['','xc2,x87'],
['','xc2,x88'],
['','xc2,x89'],
['','xc2,x8a'],
['','xc2,x8b'],
['','xc2,x8c'],
['','xc2,x8d'],
['','xc2,x8e'],
['','xc2,x8f'],
['','xc2,x90'],
['','xc2,x91'],
['','xc2,x92'],
['','xc2,x93'],
['','xc2,x94'],
['','xc2,x95'],
['','xc2,x96'],
['','xc2,x97'],
['','xc2,x98'],
['','xc2,x99'],
['','xc2,x9a'],
['','xc2,x9b'],
['','xc2,x9c'],
['','xc2,x9d'],
['','xc2,x9e'],
['','xc2,x9f'],
['','xc2,xa0'],
['','xc2,xa1'],
['','xc2,xa2'],
['','xc2,xa3'],
['-','xc2,xa4'],
['','xc2,xa5'],
['','xc2,xa6'],
['','xc2,xa7'],
['','xc2,xa8'],
['(C)','xc2,xa9'],
['-','xc2,xaa'],
['-','xc2,xab'],
['-','xc2,xac'],
['-','xc2,xad'],
['-','xc2,xae'],
['-','xc2,xaf'],
['-','xc2,xb0'],
['','xc2,xb1'],
['','xc2,xb2'],
['','xc2,xb3'],
['´','xc2,xb4'],
['','xc2,xb5'],
['','xc2,xb6'],
['-','xc2,xb7'],
['','xc2,xb8'],
['','xc2,xb9'],
['-','xc2,xba'],
['-','xc2,xbb'],
[' 1/4','xc2,xbc'],
[' 1/2','xc2,xbd'],
[' 3/4','xc2,xbe'],
['','xc2,xbf'],
['','xc3,x80'],
['','xc3,x81'],
['','xc3,x82'],
['','xc3,x83'],
['','xc3,x84'],
['','xc3,x85'],
['','xc3,x86'],
['','xc3,x87'],
['','xc3,x88'],
['','xc3,x89'],
['','xc3,x8a'],
['','xc3,x8b'],
['','xc3,x8c'],
['','xc3,x8d'],
['','xc3,x8e'],
['','xc3,x8f'],
['','xc3,x90'],
['','xc3,x91'],
['','xc3,x92'],
['','xc3,x93'],
['','xc3,x94'],
['','xc3,x95'],
['','xc3,x96'],
['x','xc3,x97'],
['','xc3,x98'],
['','xc3,x99'],
['','xc3,x9a'],
['','xc3,x9b'],
['','xc3,x9c'],
['','xc3,x9d'],
['','xc3,x9e'],
['','xc3,x9f'],
['','xc3,xa0'],
['','xc3,xa1'],
['','xc3,xa2'],
['','xc3,xa3'],
['','xc3,xa4'],
['','xc3,xa5'],
['','xc3,xa6'],
['','xc3,xa7'],
['','xc3,xa8'],
['','xc3,xa9'],
['','xc3,xaa'],
['','xc3,xab'],
['','xc3,xac'],
['','xc3,xad'],
['','xc3,xae'],
['','xc3,xaf'],
['','xc3,xb0'],
['','xc3,xb1'],
['','xc3,xb2'],
['','xc3,xb3'],
['','xc3,xb4'],
['','xc3,xb5'],
['','xc3,xb6'],
['÷','xc3,xb7'],
['','xc3,xb8'],
['','xc3,xb9'],
['','xc3,xba'],
['','xc3,xbb'],
['','xc3,xbc'],
['','xc3,xbd'],
['','xc3,xbe'],
['','xc3,xbf']

def clean_filename(filename, dup=False, replace=None, whitelist=None):
	if not filename:
		return ''
	unicodedata = __.imp('unicodedata')
	string = __.imp('string')
	valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
	char_limit = 255
	if whitelist is None: whitelist = valid_filename_chars;
	if replace is None: replace = ' ';
	# replace spaces
	for r in replace:
		if r:
			filename = filename.replace(r,replace)
	
	# keep only valid ascii chars
	cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
	
	# keep only whitelisted chars
	cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
	cleaned_filename = cleanBE(cleaned_filename,' ')
	if len(cleaned_filename)>char_limit:
		_.pr("Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
	if dup:
		cleaned_filename = do( 'dup', cleaned_filename, replace )
	return cleaned_filename[:char_limit]

def do(what=None,string='',a=None,b=None,c=None,d=None):
	'''( what=None, string='', a=None, b=None, c=None, d=None )'''

	# if what in 'file'.split(' ') and not string: _.pr( '(filename, dup=False, replace=None, whitelist=None)' );
	if what in 'an alphan'.split(' '): return totalStrip1b( string, a );
	if what in 'file'.split(' '): return clean_filename( string, a, b, c );

	if what is None:
		import _rightThumb._base3 as _
		_.pv('''
			if what in 'an'.split(' '): return re.sub(r'[^A-Za-z0-9 ]+', '', string);
			if what in 'all'.split(' '): return replaceAll(string,a,b);
			if what in 'cleanAll'.split(' '): return cleanAll(string,a,b);
			if what in 'dup'.split(' '): return replaceDuplicate(string,a);
			if what in 'be'.split(' '): return cleanBE(string,a);
			if what in 'b'.split(' '): return cleanFirst(string,a);
			if what in 'e'.split(' '): return cleanEnd(string,a);
			if 'alpha' in what and 'nu' in what : return stripNonAlphaNumaric(string);
			if what in 'n'.split(' '): return removeNonNumber(string);
			if what in 'ra remove'.split(' '): return removeAll(string,a);
		''')
		sys.exit()

	try:
		if what in 'an'.split(' '): import re; return re.sub(r'[^A-Za-z0-9 ]+', '', string);
	except Exception as e:
		if what in 'an'.split(' '): return re.sub(r'[^A-Za-z0-9 ]+', '', string);

	
	# if what in 'file'.split(' '): import re; return re.sub(r'[0-9a-zA-Z_\-+$ ]', '', string);
	# if what in 'file'.split(' '): import re; return re.sub(r'^[0-9a-zA-Z_\-. ]+$', '', string);
	
	if what in 'trim'.split(' '): return trim(string);
	if what in 'nows'.split(' '): return nows(string);

	if what in 'sh2'.split(' '): return sh2(string);
	if what in '.sh sh sh1 bash linux 2linux fix script x +x'.split(' '): return sh(string);

	if what in 'all'.split(' '): return replaceAll(string,a,b);
	if what in 'cleanAll'.split(' '): return cleanAll(string,a,b);
	if what in 'dup'.split(' '): return replaceDuplicate(string,a);
	if what in 'be'.split(' '): return cleanBE(string,a);
	if what in 'b'.split(' '): return cleanFirst(string,a);
	if what in 'e'.split(' '): return cleanEnd(string,a);
	if 'alpha' in what and 'nu' in what : return stripNonAlphaNumaric(string);
	if what in 'n'.split(' '): return removeNonNumber(string);
	if what in 'ra remove'.split(' '): return removeAll(string,a);

def sp(cnt,t=' '):
	'''  spaces '''
	output=''
	while not len(output) == cnt: output+=t
	# print('sp:',cnt,'|'+output+'|')
	return output

def es(data,be='',margin='',m=None):
	'''  endspace '''
	if not m is None: margin=m
	if type(be) == int: be=sp(be)
	if type(margin) == float: margin=int(margin)
	if type(margin) == int: margin=abs(margin)
	if type(margin) == int: margin=sp(margin)
	if type(data) == list: data='\n'.join(data)
	def _ad_space_(line,mx,be='',margin=''):
		while not len(line)==mx: line+=' '
		# print(mx,be+margin+line+margin+be)
		_out=be+margin+line+margin+be
		if len(_out) == __.terminal.width-1:_out=be+margin+line+margin+margin[0]+be

		return _out
	# data=do('sh',data)
	lines=[]
	mx=0
	for line in data.split('\n'):
		ln=len(line)
		if ln > mx: mx=ln
	for line in data.split('\n'):
		lines.append( _ad_space_(line, mx, be, margin) )
	# print('\n'.join(lines))
	return '\n'.join(lines)

def nows(string):
	if not type(string) == str: return string
	if not string: return string
	for ws in _ws():
		while ws in string: string = string.replace(ws,'')
	return string


def trim(string):
	if not type(string) == str: return string
	if not string: return string
	for ws in _ws():
		string = cleanBE(string,ws)
	return string


	# if not string: return string
	# for elem in string.whitespace: sample_str = sample_str.replace(elem, '')
	# testing=[' ', '\t', '\n']
	# if not len(string.replace(' ','').replace('\r','').replace('\n','').replace('\t','')): return ''
	# try:
	#     while string[0] in testing or string[-1] in testing:
	#         for tst in testing: string = cleanBE(string,tst)
	# except Exception as e:
	#     try: _
	#     except Exception as e: import _rightThumb._base3 as _
	#     _.pr('trim:',e,c='red')
	# return string


	# string=string.replace('\r','')
	
	# # def _trim_true_(string,testing):
	# #     r=False
	# #     for test in testing:
	# #         if (string.startswith(test)): r=True
	# #         if (string.endswith(test)): r=True
	# #     return r
	# def trimmer(string,testing=list(' \t\n')):
	#     for test in testing:
	#         string=do('be',string,test)
	#     return string
	# testing=list(' \t\n')
	# while string[0] in testing or string[-1] in testing: string=trimmer(string,testing)
	# # try:
	# # except Exception as e:
	# #     return string
	
	# # while _trim_true_(string,testing): string=trimmer(string,testing);
	# return string

def sh2(string):
	try:
		if os.path.isfile(string): string=__.getText(string,raw=True);
	except Exception as e: pass;
	string=str(string)
	string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' ).replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
	while '\t' in string: string = string.replace( '\t', '    ' );
	while ' \n' in string: string = string.replace( ' \n', '\n' );
	while '    ' in string: string = string.replace( '    ', '\t' );
	string=do('be',string,'\n')

	string = string.replace( chr(10), '\n' )
	string = string.replace( chr(27), '' )
	string = string.replace( '\r', '' )

	return string

def sh(string='f928ca8e68c6'):
	if string=='f928ca8e68c6':
		import _rightThumb._base3 as _
		_.e("_str.do('sh')",'missing data')
	try:
		if os.path.isfile(string): string=__.getText(string,raw=True);
	except Exception as e: pass;
	string=str(string)


	string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
	string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
	string=do('be',string,'\n')
	lines=string.split('\n')
	for i, line in enumerate(lines):
		if not line.replace(' ','').replace('\t',''):
			lines[i]=''
		while lines[i].endswith(' ') or lines[i].endswith('\t'): lines[i]=lines[i][:-1]
	string='\n'.join(lines)
	# if string.startswith('#!'):
	#     if '#!/bin/' in string or '#!/usr/bin/' in string:
	#         while '\t' in string: string = string.replace( '\t', '    ' );
	#         while '    ' in string: string = string.replace( '    ', '\t' );

	# string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
	string=do('be',string,'\n')
	string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )

	return string

#b)--> before 2022-08-03
# def sh(string):
#     try:
#         if os.path.isfile(string): string=__.getText(string,raw=True);
#     except Exception as e: pass;
#     string=str(string)
#     string=string.replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' ).replace( chr(10), '\n' ).replace( '\r', '' ).replace( chr(27), '' )
#     while '\t' in string: string = string.replace( '\t', '    ' );
#     while ' \n' in string: string = string.replace( ' \n', '\n' );
#     while '    ' in string: string = string.replace( '    ', '\t' );
#     string=do('be',string,'\n')

#     string = string.replace( chr(10), '\n' )
#     string = string.replace( chr(27), '' )
#     string = string.replace( '\r', '' )

#     return string
#e)--> before 2022-08-03


# class st(str):
#     def sh(self): self=do('.sh',self); return self.string(self);
#     def all(self,a,b): self=do('all',self,a,b); return self.string(self);
#     def cleanAll(self,a,b): self=do('cleanAll',self,a,b); return self.string(self);
#     def dup(self,a): self=do('dup',self,a); return self.string(self);
#     def be(self,a): self=do('be',self,a); return self.string(self);
#     def b(self,a): self=do('b',self,a); return self.string(self);
#     def e(self,a): self=do('e',self,a); return self.string(self);
#     def alpha(self): self=do('n',self); return self.string(self);
#     def num(self): self=do('nu',self); return self.string(self);
#     def remove(self,a): self=do('remove',self,a); return self.string(self);
#     def ra(self,a): self=do('remove',self,a); return self.string(self);
#     def json(self):
#         simplejson = __.imp('simplejson')
#         json=simplejson.loads(self)
#         isa='dic'
#         if do('.sh',self).replace(' ','').replace('\n','').startswith('{'):
#             isa='dic'
#         elif do('.sh',self).replace(' ','').replace('\n','').startswith('['):
#             isa='lis'
#         self=json
#         if isa=='lis': return lis(self);
#         if isa=='dic': return dic(self);
#         return 

class st(str):
	def sh(self): self=do('.sh',self); return string(self);
	def all(self,a,b): self=do('all',self,a,b); return string(self);
	def cleanAll(self,a,b): self=do('cleanAll',self,a,b); return string(self);
	def dup(self,a): self=do('dup',self,a); return self.string(self);
	def be(self,a): self=do('be',self,a); return string(self);
	def b(self,a): self=do('b',self,a); return string(self);
	def e(self,a): self=do('e',self,a); return string(self);
	def alpha(self): self=do('n',self); return string(self);
	def num(self): self=do('nu',self); return string(self);
	def remove(self,a): self=do('remove',self,a); return string(self);
	def ra(self,a): self=do('remove',self,a); return string(self);
	def json(self):
		simplejson = __.imp('simplejson')
		json=simplejson.loads(self)
		isa='dic'
		if do('.sh',self).replace(' ','').replace('\n','').startswith('{'):
			isa='dic'
		elif do('.sh',self).replace(' ','').replace('\n','').startswith('['):
			isa='lis'
		self=json
		if isa=='lis': return lis(self);
		if isa=='dic': return dic(self);
		return 

class dic(dict):
	def string(self):
		simplejson = __.imp('simplejson')
		return string(simplejson.dumps(self, indent=4, sort_keys=False))
	def inline(self):
		simplejson = __.imp('simplejson')
		return string(simplejson.dumps(self))

class lis(list):
	def string(self):
		simplejson = __.imp('simplejson')
		return string(simplejson.dumps(self, indent=4, sort_keys=False))
	def inline(self):
		simplejson = __.imp('simplejson')
		return string(simplejson.dumps(self))


