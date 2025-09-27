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
# import platform
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
	_.switches.register( 'Size', '--s,-z,-size,-i', '15mb  OR 356900864  ' )
	_.switches.register( 'Print', '-p,-print', 'also for -math: -print bytes | b | format | f | kb | mb | gb | tb | -tb add dash for bits | +tb for bits to bytes | --- for bits in bytes | +++ to convert bits to bytes ' )
	_.switches.register( 'Math', '-m,-math', '1024 * 5 OR + 1024  or   p ls -c bytes | p size' )
	_.switches.register( 'Clean', '--c' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'size.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'to bytes or from bytes',
	'categories': [
						'size',
						'calc',
						'bytes',
						'file size',
						'file',
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
						'p size -size 1kb ',
						'p size -size 1mb ',
						'p size -size 1gb ',
						'p size -size 1tb ',
						'',
						'p size -size 2899102925',
						'p size -size 2.7gb',
						'p size -size 57646075230342348809999',
						'p size -size 57.65zb',
						'p size -size 1.75yb',
						'',
						'',
						'p size -size 1kb 1mb 1gb 1tb 1pb 1eb 1zb 1yb',
						'',
						'p size -size 1024 1048576 1073741824 1099511627776 1125899906842624 1152921504606847000 1180591620717411303424 1208925819614629174706176',
						# 'p size -size 1024 1048576 1073741824 1099511627776 1125899906842624',
						# 'p size -size 1152921504606847000 1180591620717411303424 1208925819614629174706176',
						'',
						'includes:',
						'            petabyte, exabyte, zettabyte, yottabyte',
						'',
						'p size -print',
						'p size -print g',
						'p size -print g f',
						'',
						':: Math Section ::',
						'p size -m 1024 * 4',
						'p size -m 2048 + 1024',
						'p ls -c bytes | p size',
						'p ls -c bytes | p size -p bytes',
						'p ls -c bytes | p size -p gb',
						'p ls -c bytes | p size -p ---',
						'p ls -c bytes | p size -p +++',
						'p size -m 1024 * 100',
						'p size -math 1024gb * 2 -print gb',
						'p size -math 1024gb * 2 -print -gb',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START

sizes="""
1 Bit = Binary Digit
8 Bits = 1 Byte
1024 Bytes = 1 Kilobyte
1024 Kilobytes = 1 Megabyte
1024 Megabytes = 1 Gigabyte
1024 Gigabytes = 1 Terabyte
1024 Terabytes = 1 Petabyte
1024 Petabytes = 1 Exabyte
1024 Exabytes = 1 Zettabyte
1024 Zettabytes = 1 Yottabyte
1024 Yottabytes = 1 Brontobyte
1024 Brontobytes = 1 Geopbyte
"""

def hasAlpha(s): return any(c.isalpha() for c in str(s))

def toBytes(size):
	if hasAlpha(size):
		size = size.strip()
		if size.count(' ') > 1: return 0
		# formatted = ''
		# first = True
		# firstfirst = True
		# for c in size:
		# 	if c in '0123456789.':
		# 		formatted += c
		# 	if first and not c in '0123456789.':
		# 		formatted += ' '
		# 		firstfirst = False
		# 	if not first and not c in '0123456789.':
		# 		formatted += c
		# 	first = firstfirst


		try:
			return int(_.unFormatSize( size ))
		except:
			return 0
	return int(size)


def isPlusMinusTimesDivide(arg):
	items = [
		'+',
		'-',
		'*',
		'/',
	]
	if arg in items:
		return True
	return False

def mathMe(plusMinusTimesDivide, byteSybject):
	pmtd = plusMinusTimesDivide
	global total
	if pmtd == '+':
		total += byteSybject
	elif pmtd == '-':
		total -= byteSybject
	elif pmtd == '*':
		total *= byteSybject
	elif pmtd == '/':
		total /= byteSybject

total = 0

factor = {
	# 'B': 1,
	'KB': 1024,
	'MB': 1024**2,
	'GB': 1024**3,
	'TB': 1024**4,
}

def format_size(size, unit):
	global factor
	global total
	size = total
	unit = unit.upper()

	if '-' in unit:
		unit = unit.replace('-','')
		size = size/8

	elif '+' in unit:
		unit = unit.replace('+','')
		size = size*8
	

	if unit not in factor:
		raise ValueError(f"Unsupported unit: {unit}")

	value = size / factor[unit]
	rounded = round(value, 2)
	rounded = int(rounded) if rounded == int(rounded) else rounded

	return f"{rounded} {unit}".replace('.0 ',' ')





def printMathTotal():
	global factor
	global total
	global outputFormat
	global forceBits
	global forceBytes

	Total = total
	did = False
	if forceBits:
		did = '/8'
		total = total / 8
	elif forceBytes:
		did = '*8'
		total = total * 8

	if not _.switches.isActive('Clean'):
		if did:
			_.pr(did, c='cyan')
	# print(Total,total, len(str(Total)), len(str(total)), did )

	if type(outputFormat) == str:
		test = outputFormat.replace('-','').replace('+','')
	if type(outputFormat) == str and test and test in factor.keys():
		_.pr( format_size(total, outputFormat), c='yellow' )
	elif not type(outputFormat) == bool and outputFormat == -1:
		if len(str(total)) < 6:
			_.pr( total, c='yellow' )
		else:
			_.pr( _.formatSize( total ).replace('.0 ',' '), c='yellow' )
			
	elif outputFormat:
		_.pr( total, c='yellow' )
	elif not outputFormat:
		_.pr( _.formatSize( total ).replace('.0 ',' '), c='yellow' )
	return



def action():
	global total
	global outputFormat
	global forceBits
	global forceBytes
	forceBits = False
	forceBytes = False
	if _.isData(r=0) and not _.switches.isActive('Math'):
		_.switches.fieldSet( 'Math', 'active', True )
		# _.switches.fieldSet( 'Math', 'values', ['+;'] )
	if _.switches.isActive('Math'):
		values = _.switches.values('Math')
		if not values: values = ['+']
		# print(values)
		outputFormat = -1
		if _.switches.isActive('Print'):
			pr = _.switches.value('Print')
			# print(pr)
			if not hasAlpha(pr) and '-' in pr:
				outputFormat = True
				forceBits = True
			elif not hasAlpha(pr) and '+' in pr:
				forceBytes = True
				outputFormat = True
			else:
				if pr.upper().replace('-','').replace('+','')  in factor.keys():
					# print('here')
					outputFormat = pr.upper()

				elif 'b' in pr.lower():
					outputFormat = True
				elif 'f' in pr.lower():
					outputFormat = False
		if not _.isData(r=0):
			lastPMTD = None
			for value in values:
				if isPlusMinusTimesDivide(value):
					lastPMTD = value
				else:
					size = toBytes(value)
					if total == 0:
						total = size
						continue
					mathMe(lastPMTD, size)
			printMathTotal()
			return
		elif _.isData(r=0):
			pmtd = values[0].replace(';','')
			for line in _.isData():
				line = line.strip().replace(',','')
				sp = line.split(' ')
				if len(sp) == 2 and sp[1].lower() in factor.keys():
					line = line.replace(' ','')
				size = toBytes(line)
				mathMe(pmtd, size)
			printMathTotal()
			return
		return







		return None
	if _.switches.isActive('Print'):
		_.pr()
		global sizes
		s = []
		for row in sizes.split('\n'):
			row = _str.cleanBE(row,' ')
			if '=' in row:
				a = row.split('=')[0]
				b = row.split('=')[1]
				a = _str.cleanBE(a,' ')
				b = _str.cleanBE(b,' ')
				s.append({ 'a': a, 'b': b })
		m=True
		if 'f' in _.switches.value('Print').lower():
			m=False
		if 'g' in _.switches.value('Print').lower():
			_.size_group__.pr(m)
		else:
			_.tables.r_.pr(s,h=0,l=0, p='  ')


	if len( _.switches.value('Size') ):
		for do in _.switches.values('Size'):
			if len(do):
				byt = True
				for x in do:
					if x in _str.alphaChar:
						byt = False
				if byt:
					_.pr( _.formatSize( int(do) ) )
				else:
					_.pr( int(_.unFormatSize( do )) )



########################################################################################
if __name__ == '__main__':
	action()







