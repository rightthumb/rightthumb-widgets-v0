import datetime

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
import time

# auto = autoDate( data )

class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'

def dayStrip():
	return str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d'))

def friendlyDate( theDate ):
	try:
		return resolveEpoch( float(theDate) )
	except Exception as e:
		try:
			return resolveEpoch( autoDate( str(theDate) ) )
		except Exception as e:
			return Color.red + 'error: friendlyDate()' + Color.end
			# return colorThis( [ 'error: friendlyDate()' ], 'red' )
			# return 'error: friendlyDate()'

def friendlyDateTouch( theDate ):
	xyz = friendlyDate(theDate)
	# 2020-12-29 07:40:16
	partsA = xyz.split(' ')
	a = partsA[0].replace('-', '')
	partsB = partsA[1].split(':')
	a = a + partsB[0] + partsB[1] 
	return int(a)
def resolveEpoch( string, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	# onlyEpoch = True, False, 'day' 

	auto = autoDate( string )
	if not type( auto ) == bool:
		string = auto


	rData = False

	try:
		float( string )
	except Exception as e:
		test = 0

	word = string
	if test == 1:

		if showPrintTry:
			print( 'try:', 1 )
		try:
			if showPrint:
				print( 'success:', 1 )
			result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
			epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpoch( string, 2, showPrint, showPrintTry, onlyEpoch, delim )
	

	if test == 2:

		if showPrintTry:
			print( 'try:', 2 )
		try:
			if showPrint:
				print( 'success:', 2 )
			result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.))) + ' } } '
			epoch = str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpoch( string, 3, showPrint, showPrintTry, onlyEpoch, delim )



	if test == 3:

		if showPrintTry:
			print( 'try:', 3 )
		try:
			if showPrint:
				print( 'success:', 3 )
			result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)/1000.)) + ' } } '
			epoch = str(datetime.datetime.fromtimestamp(float(word)/1000.))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpoch( string, 4, showPrint, showPrintTry, onlyEpoch, delim )


	if test == 4:

		if showPrintTry:
			print( 'try:', 4 )
		try:
			if showPrint:
				print( 'success:', 4 )
			result = ' { { ' + str(time.ctime(float(word))) + ' } } '
			epoch = str(time.ctime(float(word)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpoch( string, 5, showPrint, showPrintTry, onlyEpoch, delim )



	if test == 5:

		if showPrintTry:
			print( 'try:', 5 )
		try:
			if showPrint:
				print( 'success:', 5 )
			result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.))) + ' } } '
			epoch = str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(float(word)/1000.)))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpoch( string, 6, showPrint, showPrintTry, onlyEpoch, delim )

	if test == 6:

		if showPrintTry:
			print( 'try:', 6 )
		try:
			if showPrint:
				print( 'success:', 6 )
			result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
			epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
			rData = [ result, epoch ]
		except Exception as e:
			pass

	if not type( rData ) == bool:
		if not type( onlyEpoch ) == bool:
			rData = rData[1].split(' ')[0].replace( '-', delim )
		elif onlyEpoch == True:
			rData = rData[1].replace( '-', delim )
		else:
			rData[1] = rData[1].replace( '-', delim )

	if falseBlank and type( rData ) == bool:
		rData = ''
	return rData

def findDelims( data ):
	data = str( data )
	d = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	delims = []
	for c in data:
		if not c in d:
			delims.append(c)
	return delims

def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( float(date) ).strftime('%Y.%m.%d-%H.%M-%S')
	# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate

def epoch2TextTimestamp( date ):
	date = str( date )
	try:
		theDate = formatDate( date )
	except Exception as e:
		if not '.' in date and len( date ) > 10:
			nDate = int( date )
			date = nDate / 1000
		theDate = datetime.datetime.fromtimestamp( float(date) ).strftime('%Y.%m.%d-%H.%M-%S')
		# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
	theDate = str(theDate)
	return theDate

def hasAlpha( data ):
	data = str( data )
	d = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = False
	for c in data:
		if c in d:
			result = True
	return result

def hasInt( data ):
	data = str( data )
	d = '0123456789'
	result = False
	for c in data:
		if c in d:
			result = True
	return result

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



def isEpoch( data ):
	result = True
	try:
		epoch2TextTimestamp( data )
	except Exception as e:
		result = False
	return result

def date2epoch( theDate, delim='-' ):
	theDate = str(theDate)
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(delim)
	try:
		stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
		result = float(time.mktime(stmp.timetuple()))
	except Exception as e:
		try:
			stmp = datetime.date(int(fdtl[2]), int(fdtl[0]), int(fdtl[1]))
			result = float(time.mktime(stmp.timetuple()))
		except Exception as e:
			result = False
	
	# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
	return result



def singlDelim( data, newDelim='-' ):
	data = str( data )
	for x in findDelims( data ):
		data = data.replace( x, newDelim )
	return data

def hasYear( data ):
	foundYear = False
	for x in singlDelim( data ).split('-'):
		if isInt( x ) and len( x ) == 4:
			if int( x ) > 1000:
				foundYear = True
	return foundYear

def stripDelimBE( data, delim='-' ):
	data = str( data )
	delim = str( delim )
	if data.startswith(delim):
		data = data[1:]
	if data.endswith(delim):
		data = data[:-1]
	return data

def removeDuplicatesDelim( data, delim='-' ):
	data = str( data )
	delim = str( delim )
	dup = delim + delim
	if dup in data:
		done = False
		while not done:
			data = data.replace( dup, delim )
			if not dup in data:
				done = True
	return data

def hasWeekday( data ):
	data = str( data )
	data = data.lower()
	setA = 'sun mon tue wed thu fri sat'.split(' ')
	setB = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.lower().split(' ')

	result = False
	for i,test in enumerate(setA):
		if setA[i] in data or setB[i] in data:
			result = True
	return result

def hasTextMonth( data ):
	data = str( data )
	data = data.lower()
	setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
	setB = 'January February March April May June July August September October November December'.lower().split(' ')

	result = False
	for i,test in enumerate(setA):
		if setA[i] in data or setB[i] in data:
			result = True
	return result

def isWeekday( data ):
	data = str( data )
	data = data.lower()
	setA = 'sun mon tue wed thu fri sat'.split(' ')
	setB = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.lower().split(' ')

	result = False
	for i,test in enumerate(setA):
		if data == setA[i] or data == setB[i]:
			result = True
	return result


def isMonth( data ):
	data = str( data )
	data = data.lower()
	setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
	setB = 'January February March April May June July August September October November December'.lower().split(' ')

	result = False
	for i,test in enumerate(setA):
		if data == setA[i] or data == setB[i]:
			result = True
	return result

def month2Number( data ):
	data = str( data )
	data = data.lower()
	setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
	setB = 'January February March April May June July August September October November December'.lower().split(' ')

	result = False
	for i,test in enumerate(setA):
		if data == setA[i] or data == setB[i]:
			result = i+1
	return padZero(result)

def removeDayOfWeek( data, delim='-' ):
	data = str( data )
	if hasWeekday( data ):
		result = ''
		for row in data.split(delim):
			if not isWeekday( row ):
				result += row + delim
		data = removeDuplicatesDelim( result, delim )
		data = stripDelimBE( data, delim )


	return data
def isYear( data ):
	result = False
	data = str(data)
	if isInt( data ) and len( data ) == 4:
		result = True
	return result
def validDay( data ):
	result = False
	data = str(data)
	if isInt( data ):
		if int( data ) < 32:
			result = True
	return result
def padZero( data, pad=2 ):
	data = str(data)
	l = len(data)
	if not l == pad:
		x = l
		pre = ''
		while not x == pad:
			pre += '0'
			x += 1
		data = pre + data
	return data
def cleanDate( data, delim='-' ):
	data = str(data)
	if delim in data:

		y  = False
		m  = False
		d  = False
		sData = data.split(delim)
		if isMonth( sData[0] ):
			m = month2Number( sData[0] )
			if isYear( sData[1] ):
				y = sData[1]
				if validDay( sData[2] ):
					d = sData[2]
				
			if isYear( sData[2] ):
				y = sData[2]
				if validDay( sData[1] ):
					d = sData[1]
		if isMonth( sData[1] ):
			m = month2Number( sData[1] )

			if isYear( sData[0] ):
				y = sData[0]
				if validDay( sData[2] ):
					d = sData[2]
				
			if isYear( sData[2] ):
				y = sData[2]
				if validDay( sData[0] ):
					d = sData[0]
		if not type( y ) == bool and not type( m ) == bool and not type( d ) == bool:
			sData[0] = y
			sData[1] = m
			sData[2] = d
			result = ''
			for row in sData:
				result += row + delim
			data = removeDuplicatesDelim( result, delim )
			data = stripDelimBE( data, delim )
	return data



def address24Hr( data, hr, delim='-' ):
	data = str(data)
	if hr == 12:
		sData = data.split(delim)
		if len( sData ) == 5 or len( sData ) == 4:
			result = ''
			for i,row in enumerate(sData):
				if i == 3 and isInt( row ):
					row = str( int( row ) + 12 )
				result += row + delim
			data = removeDuplicatesDelim( result, delim )
			data = stripDelimBE( data, delim )
	return data


def autoDate( data, theFormat=False, fail=False ):
	# print('data',data)
	try:
		import datefinder
		for match in datefinder.find_dates(data):
			# print( 'match.timestamp()', match.timestamp() )
			return match.timestamp()
	except Exception as e:
		pass

	if type(data) == float or type(data) == int:
		return data
	try:
		if 'T' in data:
			data = data.replace( 'T', ' ' )
	except Exception as e:
		pass
		# print( data )
	try:
		if '+' in data:
			data = data.split('+')[0]
	except Exception as e:
		pass

	try:
		float(data)
		return False
	except Exception as e:
		pass

	originalData = data
	data = str( data )
	if not hasInt( data ):
		if fail:
			print( 'Error: not a date', 0 )
			sys.exit()
		data = False
	data = singlDelim( data )
	data = data.lower()
	data = data.replace( 't', '-' )
	data = data.replace( 'at', '-' )
	hr = 24
	if 'pm' in data:
		hr = 12
	data = data.replace( 'am', '' ).replace( 'am', '' )
	data = removeDuplicatesDelim( data )
	data = stripDelimBE( data )
	data = removeDayOfWeek( data )
	data = cleanDate( data )
	delims = findDelims( data )
	

	if type( theFormat ) == bool and not hasAlpha( data ):
		if len( delims ) == 0:
			if not isEpoch( data ):
				if fail:
					print( 'Error: not a date', 1 )
					sys.exit()
				data = False
			else:
				data = str( int( data ) / 1000 )
		elif isEpoch( data ):
			data
			
		else:
			if not hasYear( data ):
				if fail:
					print( 'Error: not a date', 2 )
					sys.exit()
				data = False
			else:
				if len( delims ) == 2:
					data = date2epoch( data, delims[0] )
					if fail and type(data) == bool:
						print( 'Error: not a date', 3 )
						sys.exit()

				elif len( delims ) == 5:
					sData = data.split('-')
					try:
						test = datetime.datetime.strptime( address24Hr( data, hr ), '%Y-%m-%d-%H-%M-%S' )
						data = test.timestamp()
					except Exception as e:
						if fail:
							print( 'Error: not a date', 4 )
							sys.exit()
						data = False
				elif len( delims ) == 4:
					sData = data.split('-')
					try:
						test = datetime.datetime.strptime( address24Hr( data, hr ), '%Y-%m-%d-%H-%M' )
						data = test.timestamp()
					except Exception as e:
						if fail:
							print( 'Error: not a date', 5 )
							sys.exit()
						data = False
				else:
					if fail:
						print( 'Error: not a date', 6 )
						sys.exit()
					data = False

	if not type( data ) == bool:
		if isFloat( data ):
			data = float( data )

	d = str(data)
	if d.endswith('.0'):
		d = d.replace('.0','')
		data = int(d)
	return data



