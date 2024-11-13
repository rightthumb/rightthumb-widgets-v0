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

from _rightThumb._hub import _construct as __
from _rightThumb._hub import app
from _rightThumb._hub import _vars as _v
from _rightThumb._hub import _string as _str

def temp():
	print()
	pass



############################################################## copy-fn-class


def find_all(a_str, sub):
	return list(find_all_do(a_str, sub))


def find_all_do(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)


def reFormatSize( start ):
	start = start.replace( ' ', '' )
	start = start.replace( ',', '' )
	start = start.replace( '?', '' )
	b = unFormatSize( start )
	end = formatSize( b )
	return end


def formatSize(size):
	try:
		size = int(size)
	except Exception as e:
		size = float(size)
	result = ''
	if size == None:
		result = ''
	elif size < 1024:
		result = str(size) + ' B'
	elif size >= 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size >= 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size >= 1073741824 and size < 1099511627776 :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	elif size >= 1099511627776 and size < 1125899906842624 :
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	elif size >= 1125899906842624 and size < 1152921504606847000 :
		num = round(size / 1125899906842624, 2)
		result = str(num) + ' PB'
	elif size >= 1152921504606847000 and size < 1180591620717411303424 :
		num = round(size / 1152921504606847000, 2)
		result = str(num) + ' EB'
	elif size >= 1180591620717411303424 and size < 1208925819614629174706176 :
		num = round(size / 1180591620717411303424, 2)
		result = str(num) + ' ZB'
	else:
		num = round(size / 1208925819614629174706176, 2)
		result = str(num) + ' YB'
	# 1152921504606846976

	# if size < 1:
	#   result = ''
	return result


def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''
	# 1152921504606846976
	if False:
		pass
	elif 'YB' in size:
		factor = 1208925819614629174706176
	elif 'ZB' in size:
		factor = 1180591620717411303424
	elif 'EB' in size:
		factor = 1152921504606847000
	elif 'PB' in size:
		factor = 1125899906842624
	elif 'TB' in size:
		factor = 1099511627776
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('X','')
	size = size.replace('Y','')
	size = size.replace('Z','')
	size = size.replace('E','')
	size = size.replace('P','')
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	if str(size).endswith('.0'):
		size = int(size)

	result = round(size * factor,0)
	# print( size, factor )
	# result = size * factor
	return result


def timeAgo( do='', startDate=None ):

	try:
		do = float(do)
		return do
	except Exception as e:
		pass

	global timeAgoBase
	global timeAgoBaseCount
	if not len(timeAgoBase) and timeAgoBaseCount == 0:
		if ',' in do:
			timeAgoBase = do.split(',')
			# print(do)
			# sys.exit()
	timeAgoBaseCount += 1
	# print( do, friendlyDate(startDate) )
	if len(do) == 19 and do.count('-') == 2 and do.count(':') == 2:
		return autoDate( do )
	if len(do) == 16 and do.count('-') == 2 and do.count(':') == 1:
		return autoDate( do )
	if len(do) == 21 and do.count('-') == 4:
		result = []
		for x in do.split(','):
			result.append( timeAgo( x, startDate ) )
		return result
	if len(do) == 10 and do.count('-') == 2:
		ts = autoDate( do )
	else:
		if not do.startswith('+'):
			ts = timeAgo_past(do,startDate)
		elif do.startswith('+'):
			ts = timeFuture(do,startDate)


	if len(timeAgoBase) > 1 and do == timeAgoBase[1]:
		if timeAgoBaseCount == 3 or timeAgoBaseCount == 5 :
			pass
			ts += 86400-1
	# print( timeAgoBaseCount, ts )
	return ts


def timeAgo_past(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime
	# return do
	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('-'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = app.switch.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate - remove  
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate - remove  


	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1
	if 'y' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
		# start_date = dateMathEpoch( startDate, 365 * nmb, '-' )
		start_date = yearMath( startDate, nmb, do='-' )
	if 'm' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
		# start_date = dateMathEpoch( startDate, 30 * nmb, '-' )
		start_date = monthMath( startDate, nmb, do='-' )
	if 'w' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
		start_date = dateMathEpoch( startDate, 7 * nmb, '-' )
	if 'd' in do:
		# start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
		start_date = dateMathEpoch( startDate, nmb, '-' )
	return start_date


def timeFuture(do='', startDate=None):
	if startDate is None:
		startDate = time.time()
	global isTime

	if '.' in do:
		dos = do.split('.')
		e = timeAgo( dos[0], startDate )
		# return e
		for di,ds in enumerate(dos):
			if di:
				e = timeAgo( dos[di], e )
		return e
	if do.startswith('+'):
		do = do[1:]
	if do is None:
		colorThis( '\t Error: Ago is Missing parameters', 'red' )
		sys.exit()
	if type(do) == float:
		return do
	if do.lower() == 'r':
		return 'resent'
	if 're' in do.lower():
		return 'resent'
	if 'a' in do.lower():
		return 'a'
	if 'cd' in do:
		return do.lower()
	if 'md' in do:
		return do.lower()
	if 'mod' in do.lower():
		return 'md'
	if 'crea' in do.lower():
		return 'cd'
	if 'o' in do.lower():
		return 'one'

	if len(do) == 0:
		do = app.switch.values('Ago')[0]
	do = do.lower()

	if 't' in do:
		one = resolveEpochTest( startDate )
		two = autoDate( one.split(' ')[0] )
		return two
	if 'mm' in do or 'min' in do:
		each = 60
		units = do
		units = units.replace( 'min', '' )
		units = units.replace( 'm', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if isTime:
		if 'm' in do:
			each = 60
			units = do
			units = units.replace( 'm', '' )
			units = int( units )
			remove = units * each
			return startDate + remove  

	if 'h' in do:
		each = 3600
		units = do
		units = units.replace( 'h', '' )
		units = int( units )
		remove = units * each
		return startDate + remove  
	if 's' in do:
		units = do
		units = units.replace( 's', '' )
		units = int( units )
		return startDate + units


	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1

	if 'y' in do:
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		# start_date = dateMathEpoch( startDate, 365 * nmb, '+' )
		start_date = yearMath( startDate, nmb, do='+' )
	if 'm' in do:
		# start_date = dateMathEpoch( startDate, 30 * nmb, '+' )
		start_date = monthMath( startDate, nmb, do='+' )
	if 'w' in do:
		start_date = dateMathEpoch( startDate, 7 * nmb, '+' )
	if 'd' in do:
		start_date = dateMathEpoch( startDate, nmb, '+' )
	return start_date



############################################################## copy-fn-class





############################################################## copy-fn-class


def formatPhone00(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)
	data = _str.cleanBE(data,'.')
	return data


def formatPhone1(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '-' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData


def formatPhone2(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = data[0] + data[1] + data[2] + '.' + data[3] + data[4] + data[5] + '.' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData


def formatColumns_OLD(columns):
	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[0]
				c = preDataR[1]

			for col in appInfo[__.appReg]['columns']:
				for a in col['abbreviation'].split(','):
					if a == c:
						c = col['name']
			if hasPre:
				c = preData + '.' + c
			result += c + ','
		result = result[:-1]
	# print(result)
	return result


def formatColumnsSort(columns):

	if type(columns) == str:
		if columns.startswith('a.'):
			columns = 'a:' + columns[2:]
		if ',a.' in columns:
			columns = columns.replace( ',a.', ',a:' )

		if columns.startswith('d.'):
			columns = 'd:' + columns[2:]
		if ',d.' in columns:
			columns = columns.replace( ',d.', ',d:' )


	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if ':' in c:
				hasPre = True
				# c = c.replace(':','.')
				preDataR = c.split(':')
				preData = preDataR[1]
				c = preDataR[0]

			for col in appInfo[__.appReg]['columns']:
				if 'sort' in list(col.keys()) and len(col['sort']):
					for a in col['abbreviation'].split(','):
						if a == c:
							c = col['sort']
				else:
					for a in col['abbreviation'].split(','):
						if a == c:
							c = col['name']
			if hasPre:
				c = preData + ':' + c
				# c = c + '.' + preData

			result += c + ','
		result = result[:-1]
	# print( result )
	return result


def formatColumnsSortOld(columns):
	# print(__.appReg)
	# print(columns)
	result = ''
	if columns is None:
		result = columns
	else:
		for c in columns.split(','):
			hasPre = False
			if '.' in c or ':' in c:
				hasPre = True
				c = c.replace(':','.')
				preDataR = c.split('.')
				preData = preDataR[1]
				c = preDataR[0]

			for col in appInfo[__.appReg]['columns']:
				if 'sort' in list(col.keys()) and len(col['sort']):
					for a in col['abbreviation'].split(','):
						if a == c:
							c = col['sort']
				else:
					for a in col['abbreviation'].split(','):
						if a == c:
							c = col['name']
			if hasPre:
				c = preData + '.' + c
				# c = c + '.' + preData

			result += c + ','
		result = result[:-1]
	# print( result )
	return result


def isDate( theDate, record={}, tz=None, q=True ):
	s = time.time()
	# slow from loading pandas
	if not tz is None and not len(tz):
		tz = None

	global _tz
	if _tz is None:
		import _rightThumb._tz as _tz

	local_tz = str(time.strftime("%z")).replace(':','')

	hasTZ = False
	if type(theDate) == str and len(theDate) > 11:
		if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
			hasTZ = theDate[-6:].replace(':','')

	if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
		if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
			hasTZ = theDate[-5:].replace(':','')








	epoch = autoDate(theDate)

	if not type(hasTZ) == bool:
		if not hasTZ == local_tz:
			epoch = _tz.convert( epoch, hasTZ, local_tz )

	if not tz is None and not local_tz == tz:
		epoch = _tz.convert( epoch, local_tz, tz )
		local_tz = tz


		if '/' in tz:
			global arrow
			if arrow is None:
				import arrow
			utc = arrow.utcnow()
			theDate = str(utc.to(tz))
			hasTZ = False
			if type(theDate) == str and len(theDate) > 11:
				if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
					hasTZ = theDate[-6:].replace(':','')

			if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
				if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
					hasTZ = theDate[-5:].replace(':','')
			local_tz = hasTZ

	

	if not epoch:
		return record
	global _dir
	global pandas
	if pandas is None:
		if q:
			try:
				#  pandas  takes .5 seconds to load 
				import pandas
			except Exception as e:
				pass
	if _dir is None:
		import _rightThumb._dir as _dir
	ss = time.time()
	record['epoch'] = epoch
	record['ordinal'] = datetime.datetime.fromtimestamp( epoch ).toordinal()
	record['sdate'] = friendlyDate2( epoch )
	record['strip'] = onlyNumbers_strip(friendlyDate( epoch ).split(' ')[0])
	record['stript'] = onlyNumbers_strip(friendlyDate( epoch ))
	record['date'] = friendlyDate( epoch ).split(' ')[0]
	record['time'] = friendlyDate2( epoch ).split(' ')[1]
	record['fdate'] = friendlyDate( epoch )
	record['month'] = _dir.getMonthFromEpoch( epoch )
	record['year'] = _dir.getYearFromEpoch( epoch )
	record['woy'] = _dir.getWeekAndYear( epoch )
	record['dow'] = _dir.getDOWromEpochText( epoch )
	record['ago'] = _dir.dateDiffText( epoch )
	record['days'] = daysDiff(  epoch, time.time()  )
	record['tz'] = local_tz
	

	try:
		import _rightThumb._nID as _nID
		_nID.mini.password( '1970' )
		eee = ''
		ee = str(record['epoch'])
		for c in ee:
			if '.' == c:
				break
			eee+=c
		record['nID'] = _nID.mini.gen( record['strip'] )
		record['nIDt'] = _nID.mini.gen( record['stript'] )
		record['nIDe'] = _nID.mini.gen( int(eee) )
	except Exception as e:
		pass


	try:
		import _rightThumb._stardate as _sd
		record['stardate'] = _sd.gen(  epoch  )
	except Exception as e:
		pass

	dt = record['fdate'].split(' ')[0].split('-')
	try:
		record['quarter'] = str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
	except Exception as e:
		pass

	e = time.time()
	# print( e-s )
	# print( e-ss )
	return record


def daysDiff( one, two ):
	global date_datetime
	oneA = autoDate( one )
	twoB = autoDate( two )
	g = 1
	if two > one:
		g = 2

	if one == two:
		return 0
	elif one > two:
		one = friendlyDate( oneA ).split(' ')[0]
		two = friendlyDate( twoB ).split(' ')[0]
	else:
		one = friendlyDate( twoB ).split(' ')[0]
		two = friendlyDate( oneA ).split(' ')[0]


	# print( '090', one, two )

	oneB = one.split('-')
	twoB = two.split('-')
	if date_datetime is None:
		from datetime import date as date_datetime
	d0 = date_datetime(int(oneB[0]), int(oneB[1]), int(oneB[2]))
	# print( '080', twoB )
	d1 = date_datetime(int(twoB[0]), int(twoB[1]), int(twoB[2]))
	delta = d1 - d0
	dd = delta.days
	if g == 1:
		dd = abs(dd)
	return dd


def friendlyDate( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDate( theDate )


def autoDate( theDate ):
	# if type(theDate) == float or type(theDate) == int:
	#   return theDate
	import _rightThumb._date as _date
	return _date.autoDate( theDate )


def friendlyDate2( theDate ):
	fd = friendlyDate( theDate )
	if type(fd) == str and len(fd):
		fd = fd[:-3][2:]
		# if fd.startswith('21-'):
		#   fd = fd[3:]
	return fd


def onlyNumbers_strip(n):
	n = str(n)
	t = ''
	for c in n:
		if c in '0123456789':
			t+=c
	return t


def friendlyDateTouch( theDate ):
	import _rightThumb._date as _date
	return _date.friendlyDateTouch( theDate )


def fileDate( theDate ):
	friendly = friendlyDate( theDate )
	friendly = friendly.replace( ' ', '_' )
	friendly = friendly.replace( ':', '-' )
	return friendly


def dateAdd2( theDate, addDays, delim='-' ):
	
	theDate = str( theDate )

	if not delim in theDate:
		try:
			float( theDate )
			theDate = resolveEpochTest( theDate, onlyEpoch='day', delim=delim )
			if type(theDate) == bool:
				print( 'Error:', theDate )
				sys.exit()
		except Exception as e:
			printBold( 'Error: '+ theDate, 'red' )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)


def printBold( string, color='white', prefix='' ):
	
	if '\n' in string:
		string = string.replace( '\n', '\n'+prefix )
	else:
		string = prefix + string
	
	global switches
	if app.switch.isActive( 'NoColor' ):
		print( string )
		return False

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'white':
		print( ColorBold.white + string + ColorBold.end )
	elif color == 'red':
		print( ColorBold.red + string + ColorBold.end )
	elif color == 'gray' or color == 'grey':
		print( ColorBold.gray + string + ColorBold.end )
	elif color == 'green':
		print( ColorBold.green + string + ColorBold.end )
	elif color == 'yellow':
		print( ColorBold.yellow + string + ColorBold.end )
	elif color == 'blue':
		print( ColorBold.blue + string + ColorBold.end )
	elif color == 'magenta':
		print( ColorBold.magenta + string + ColorBold.end )
	elif color == 'cyan':
		print( ColorBold.cyan + string + ColorBold.end )


def resolveEpochTest( theDate, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
	import _rightThumb._date as _date
	return _date.resolveEpoch( theDate, test, showPrint, showPrintTry, onlyEpoch, delim, falseBlank )


def dateMathEpoch( epoch, theDays, do='+' ):
	# print(epoch, theDays)
	epoch = autoDate(epoch)
	# if do == '+':
	#   return epoch + ( theDays*86400 )
	# elif do == '-':
	#   return epoch - ( theDays*86400 )


	date0 = datetime.datetime.fromtimestamp((epoch))
	if do == '+':
		date1 = date0 + datetime.timedelta(days=theDays)
	elif do == '-':
		date1 = date0 - datetime.timedelta(days=theDays)
	else:
		print( "dateMathEpoch( epoch, theDays, do='+' )" )
		sys.exit()
	# print(date1.timestamp())
	return autoDate((date1.timestamp()))


def txt2Date(text):
	# _.app.switch.trigger('Watched', _.txt2Date)

	try:
		if not type(text) == str:
			text = ''
	except Exception as e:
		text = ''

	if text == '':
		theDate = datetime.date.today()
		result = str( theDate ).split()[0]
	elif '-' in text:
		if text.count('-') == 2:
			try:
				textSplit = text.split('-')
				# print(textSplit)
				theDate = datetime.datetime( int(textSplit[0]), int(textSplit[1]), int(textSplit[2]), 0, 0 )
				result = str( theDate ).split()[0]
			except Exception as e:
				printBold('Date error: using today\'s date','red')
				theDate = datetime.date.today()
				result = str( theDate ).split()[0]
		else:
			print('Date error: using today\'s date')
			theDate = datetime.date.today()
			result = str( theDate ).split()[0]
	else:
		fnd = 'ymwd'
		do = text.lower().replace(' ','')
		nmb = do
		for t in fnd:
			nmb = nmb.replace(t,'')
		if len(nmb) == 0:
			nmb = 1
		try:
			nmb = int(nmb)
		except Exception as e:
			nmb = 1
		if 'y' in do:
			theDate = datetime.date.today() + datetime.timedelta(-365 * nmb)
		if 'm' in do:
			theDate = datetime.date.today() + datetime.timedelta(-30 * nmb)
		if 'w' in do:
			theDate = datetime.date.today() + datetime.timedelta(-7 * nmb)
		if 'd' in do:
			theDate = datetime.date.today() + datetime.timedelta(-1 * nmb)
		result = str( theDate ).split()[0]
	return result


def stamp2Date(ts):
	# print(ts)
	# print(datetime.datetime.fromtimestamp(int(ts) / 1e3))
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)


def float2Date(ts):
	import _rightThumb._date as _date
	auto = _date.autoDate( ts )
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
		# print( stamp2Date(ts) )
	return stamp2Date(ts)


def float2Date2(ts):
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
	return str(datetime.datetime.fromtimestamp(ts)).split('.')[0]


def float2Date3(ts):
	return str(datetime.datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))


def float2Date3B(ts,isJson = True):
	stmp = float2Date3(ts)
	dtx = stmp.split(' ')[0]
	preResult = {'year': dtx.split('-')[0],'month': dtx.split('-')[1],'day': dtx.split('-')[2]}
	if isJson:
		result = preResult
	else:
		result = str(preResult['year']) + '-' + str(preResult['month']) + '-' + str(preResult['day'])

	return result


def dateDiff( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		try:
			theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )
			if type(theDate0) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate0), 'red' )
			sys.exit()


	if not delim in theDate1:
		try:
			theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )
			if type(theDate1) == bool:
				printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
				sys.exit()
		except Exception as e:
			printBold( 'Error: _.dateDiff '+ str(theDate1), 'red' )
			sys.exit()

	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))


def dateDiffX( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )



	if not delim in theDate1:
		theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )



	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))


def dateSub(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 - datetime.timedelta(days=addDays)


def date2epoch(theDate,delim='-'):
	theDate = str(theDate)
	if len( theDate ) == 0:
		return ''
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(' ')[0].split('-')
	if ':' in theDate:
		theDate = theDate.replace('.',':')
		if theDate.count(':') == 2:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S')
		elif theDate.count(':') == 1:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M')
		elif theDate.count(':') == 3:
			stmp = dt.strptime(theDate, '%Y-%m-%d %H:%M:%S:%f')
		else:
			print('Error: date2epoch')
			sys.exit()

	else:
		stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
	return float(time.mktime(stmp.timetuple()))


def validateEmail(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip(data)
	good = True
	# if not '@' in data:
	if not data.count('@') == 1:
		good = False
	if good:
		if not '.' in data.split('@')[1]:
			good = False
	# if data.count('@') == 1:
	if not good and len(data) > 0:
		data = ' ___________ * BAD * ___________'
	return data


def figureOutDate(theDate, theFormat):
	theFormat = str(theFormat)
	theFormat = _str.replaceDuplicate(theFormat,' ')
	theFormat = _str.cleanBE(theFormat,' ')
	theFormat = theFormat.lower()

	theFormatExp = 'dmy'
	if not len(theFormat) == 3:
		print('format error, expected: dmy, ymd')
		sys.exit()
	if theFormat[0] in theFormatExp and theFormat[1] in theFormatExp and theFormat[2] in theFormatExp:
		pass
	else:
		print('format error, expected: dmy, ymd')
		sys.exit()
	# theFormat = 'dmy'
	theDate = str(theDate)
	theDate = _str.replaceDuplicate(theDate,' ')
	theDate = _str.cleanBE(theDate,' ')

	
	n = '0123456789'
	a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	autoDelim = ''
	for d in theDate:
		if d in n:
			pass
		elif d in a:
			pass
		else:
			autoDelim = d
			break

	theDateDe = theDate.split(autoDelim)
	info = {}

	info[theFormat[0]] = theDateDe[0]
	info[theFormat[1]] = theDateDe[1]
	info[theFormat[2]] = theDateDe[2]
	if info['m'][0] in a:
		m = info['m']
		m = m.lower()
		found = False
		for monththeDate in getMonthData():
			# print(monththeDate)
			# sys.exit()
			full = monththeDate['month']
			abbrev = monththeDate['abbrev']
			mNumber = monththeDate['number']
			full = full.lower()
			abbrev = abbrev.lower()
			if m == full or m == abbrev:
				found = True
				info['m'] = mNumber
		if not found:
			ans = input('What Month? ')
			if len(ans) == 0:
				print('Month error')
				sys.exit()
			try:
				int(ans)
			except Exception as e:
				printBold('Month error','red')
				sys.exit()
			if len(ans) == 1:
				info['m'] = 0 + ans
			elif len(ans) == 2:
				info['m'] = ans
			else:
				printBold('Month error','red')
				sys.exit()

	ifoy = info['y']
	ifom = info['m']
	ifod = info['d']
	pResult = info['y'] + '-' + info['m'] + '-' + info['d']
	hasDup = False
	if pResult.count(ifoy) > 1:
		hasDup = True
	if pResult.count(ifom) > 1:
		hasDup = True
	if pResult.count(ifod) > 1:
		hasDup = True


	changed = []
	def test(l):
		result = ''
		if int(l) > 1000:
			result = 'y'
		elif int(l) > 12:
			result = 'd'
		return result
	fList = ''
	if test(ifom) == 'y':
		fList += 'y'
		info['y'] = ifom
		# info['m'] = ifoy
	if test(ifod) == 'y':
		fList += 'y'
		info['y'] = ifod
		# info['d'] = ifoy
	if test(ifod) == 'd':
		fList += 'd'
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifom) == 'd':
		fList += 'd'
		info['d'] = ifom
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == '' and 'd' in fList:
		fList += 'm'
		info['m'] = ifoy
	if test(ifoy) == 'd':
		fList += 'd'
		info['d'] = ifoy
	if test(ifod) == '' and 'd' in fList:
		info['m'] = ifod
	# print(test(ifoy))
	# print(fList)

	result = info['y'] + '-' + info['m'] + '-' + info['d']
	# print(result)
	if not hasDup:
		hasDup = False
		if result.count(ifoy) > 1:
			hasDup = True
		if result.count(ifom) > 1:
			hasDup = True
		if result.count(ifod) > 1:
			hasDup = True
		if hasDup:
			print('Error please specify format: ymd')
			sys.exit()
	else:
		if result.count(info['y']) > 1:
			print('Error please specify format: ymd')
			sys.exit()

	print(result)
	sys.exit()
	return result


def getMonthData():
	monthData = getText(_v.myTables + _v.slash+'month.txt')
	monthList = []
	for md in monthData:
		md = md.replace('\n','')
		mds = md.split(',')
		monthList.append({'month': mds[0], 'abbrev': mds[1], 'number': mds[2]})
	return monthList


def getText( theFile, raw=False, clean=False,  e=0, c=0 ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	HD.chmod(theFile)
	lines = None
	if os.path.isfile(theFile):
		try:
			f = open(theFile, 'r', encoding='utf-8')
			lines = f.readlines()
			f.close()
		except Exception as e:
			try:
				f = open(theFile, 'r', encoding='latin-1')
				lines = f.readlines()
				f.close()
			except Exception as e:
				f = open(theFile, 'r')
				lines = f.readlines()
				f.close()
	else:
		if not e:
			return None
		print('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print( row )
			lines[i] = row
		return lines
	else:
		return lines


def updateLine( string, clear=True, color=None, sleep=None ):
	global updateLine_disable
	if updateLine_disable:
		clear = False
	if type(string) == list:
		for i,s in enumerate(string):
			string[i]=str(s)
		string = ' '.join(string)
	a=None
	b=None
	c=None
	if type(clear) == str:
		b = clear
	if type(color) == bool:
		a = color
	if type(clear) == int or type(clear) == float:
		c = clear
	if type(color) == int or type(color) == float:
		c = color

	if not a is None:
		clear = a
	if not b is None:
		color = b
	if not c is None:
		sleep = c


	if type(color) == str:
		string = cp( string, color, p=0 )

	if clear:
		txt = linePrint(txt=' ',p=0)
		updateLine(txt,clear=False)


	if updateLine_disable:
		print(string)
	else:
		print('{}\r'.format(string), end="")


	if not sleep is None:
		time.sleep(sleep)


def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2 ):
	ln = mn
	if text is None and label is None:
		if __.terminal.width:
			ln = __.terminal.width
			add = 0


	if not label is None:
		global line_length_hash_table
		if not label in line_length_hash_table:
			line_length_hash_table[label] = ln
		else:
			ln = line_length_hash_table[label]
		if not text is None:
			if not p == True and not p == 1:
				p = 0
			if type(text) == str:
				t = len( str(text) )
				if t > ln:
					ln = t
					line_length_hash_table[label] = ln
			elif type(text) == list:
				for texty in text:
					t = len( str(texty) )
					if t > ln:
						ln = t
						line_length_hash_table[label] = ln

	if text is None and ln > 0:
		i = 0
		result = ''
		if add:
			add+=1
		ln += add
		while not i == ln:
			result += txt
			i+=1
		if p:
			print( result )
		return result


def dateDiffDic( one, two ):

	oA = autoDate( friendlyDate( autoDate(one) ).split(' ') )
	tA = autoDate( friendlyDate( autoDate(two) ).split(' ') )
	if oA > tA:
		o = oA
		t = tA
	else:
		o = tA
		t = oA



	md1 = monthsDiff( one, two )
	# md1 = autoDate( friendlyDate( autoDate(md1) ).split(' ') )
	print( 'md1', md1 )
	md2 = md1
	mx1 = monthMath( t, md1, do='+' )
	print( 'mx1', friendlyDate(mx1) )
	mx1 = autoDate( friendlyDate( autoDate(mx1) ).split(' ') )
	print( 'mx1', friendlyDate(mx1) )
	# if mx1 > t:
	if abs(mx1 - o) > 86420:
		print( 'error a' )
		print( '-', abs(mx1 - o) )
		print( friendlyDate(mx1), friendlyDate(o) )
		print( (mx1), (o) )
		print( 'error a' )
		md1-=1
		mx1 = monthMath( o, md1-1, do='+' )
	d1 = abs(daysDiff( o, mx1 ))

	# mx2 = monthMath( o, md2, do='+' )
	# mx2 = autoDate( friendlyDate( autoDate(mx2) ).split(' ') )
	# # if mx2 > o:
	# if abs(mx2 - t) > 86420:

	#   print( 'error b' )
	#   print( '-', abs(mx2 - t) )
	#   print( friendlyDate(mx2), friendlyDate(t) )
	#   print( (mx2), (t) )

	#   print( 'error b' )
	#   md2-=1
	#   mx2 = monthMath( t, md2, do='+' )
	# d2 = daysDiff( t, mx2 )


	return md1, d1

	# one = friendlyDate( autoDate( one ) ).split(' ')[0]
	# two = friendlyDate( autoDate( two ) ).split(' ')[0]

	# # print( 'here' )
	# # print( 'one', one )
	# # print( 'two', two )
	# oneB = one.split('-')
	# twoB = two.split('-')
	# # print( 'here' )

	# oneA = float( oneB[0]+'.'+oneB[1] )
	# twoA = float( twoB[0]+'.'+twoB[1] )

	# if oneA == twoA:
	#   return 0
	# elif oneA < twoA:
	#   do = '-'
	# else:
	#   do = '+'

	# oneB[0] = int(oneB[0])
	# oneB[1] = int(oneB[1])
	# oneB[2] = int(oneB[2])

	# twoB[0] = int(twoB[0])
	# twoB[1] = int(twoB[1])
	# twoB[2] = int(twoB[2])

	# cnt = {
	#           'y': 0,
	#           'm': 0,
	#           'd': 0,
	# }
	# # print(  )
	# # print(' i',i, do)
	# done = False

	# done = False

	# # print(  )



	# while  not done:
	#   print( oneB, twoB )
	#   if oneB[0] == twoB[0] and  oneB[1] == twoB[1]  and  oneB[2] == twoB[2] :
	#       done = True
	#   if not done:
	#       twoB[2]+=1
	#       cnt['d'] += 1
	#       if twoB[2] > days_in_month( twoB[1], twoB[0] ):
	#           twoB[2] = 1
	#           twoB[1] += 1
	#           cnt['d'] = 0
	#           cnt['m'] += 1

	#       if twoB[1] == 13:
				
	#           twoB[1] = 1
	#           twoB[0] += 1
	cnt['y'] = int(str( cnt['m']/12 ).split('.')[0])
	cnt['m'] = cnt['m'] - ( cnt['y']*12 )
	return cnt


def days_in_month( m, y=None ):
	global cal_days
	if cal_days is None:
		cal_days = getTableDB( 'cal-days.hash' )
	if m == 2:
		if y is None:
			return 28
		elif not y is None:
			if isLeapYear( y ):
				return 29
			else:
				return 28
	return cal_days[str(m)]


def isLeapYear( year ):
	global leap_years_table
	if leap_years_table is None:
		leap_years_table = getTableDB( 'leap-years.list' )

	if year in leap_years_table:
		return True
	return False


def getTableDB( theFile,     isDic=None, isList=None ):
	if os.path.isfile(theFile): v.opened_file_me[theFile] = os.path.getmtime( theFile );
	simplejson = __.imp('simplejson')
	theFile = _v.dbTables + _v.slash + theFile
	if os.path.isfile(theFile):
		if isTar.bz2(theFile) or isTar.gz(theFile):
			global _tar
			if _tar is None:
				import _rightThumb._tar as _tar
				_tar.unzip( theFile )


		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
			# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()


def monthMath( thisDate, months, do='+' ):
	months = abs(months)
	# print( '040', thisDate, autoDate( thisDate ), friendlyDate(thisDate) )
	theDateParts = friendlyDate( autoDate( thisDate ) ).split(' ')
	theDate = theDateParts[0]
	parts = theDate.split('-')
	parts[0] = int(parts[0])
	parts[1] = int(parts[1])
	parts[2] = int(parts[2])
	i = 0
	while not i == months:
		# print( months, 1, parts )
		if do == '+':
			parts[1]+=1
			if parts[1] == 13:
				parts[1] = 1
				parts[0] += 1
		elif do == '-':
			parts[1]-=1
			if parts[1] == 0:
				parts[1] = 12
				parts[0] -= 1
		i+=1
	# print( '048a' )
	bb = str(parts[1])
	cc = str(parts[2])
	# print( '048b' )
	if parts[1] < 10:
		bb = '0'+bb
	if parts[2] < 10:
		cc = '0'+cc
	# print( '048c' )
	text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
	# print( '049', text )
	result = autoDate(  text  )
	# print( '050a', text, type( result ) )
	while type( result ) == bool:

		parts[2]-=1

		bb = str(parts[1])
		cc = str(parts[2])
		if parts[1] < 10:
			bb = '0'+bb
		if parts[2] < 10:
			cc = '0'+cc
		text = str(parts[0])+'-'+bb+'-'+cc +' '+ theDateParts[1]
		result = autoDate(  text  )
		# print( '050b', text, type( result ) )



	# print( '050c', text )
	# print( '060', result )
	return result


def monthsDiff( one, two ):
	one = friendlyDate( autoDate( one ) ).split(' ')[0]
	two = friendlyDate( autoDate( two ) ).split(' ')[0]

	# print( 'here' )
	# print( 'one', one )
	# print( 'two', two )
	oneB = one.split('-')
	twoB = two.split('-')
	# print( 'here' )

	oneA = float( oneB[0]+'.'+oneB[1] )
	twoA = float( twoB[0]+'.'+twoB[1] )

	if oneA == twoA:
		return 0
	elif oneA < twoA:
		do = '-'
	else:
		do = '+'

	oneB[0] = int(oneB[0])
	oneB[1] = int(oneB[1])

	twoB[0] = int(twoB[0])
	twoB[1] = int(twoB[1])
	i=0
	# print(  )
	# print(' i',i, do)
	done = False
	while  not done:
		if oneB[0] == twoB[0] and  oneB[1] == twoB[1]:
			done = True
		if not done:
			i+=1
			if do == '+':
				twoB[1]+=1
				if twoB[1] == 13:
					twoB[1] = 1
					twoB[0] += 1
			elif do == '-':
				twoB[1]-=1
				if twoB[1] == 0:
					twoB[1] = 12
					twoB[0] -= 1
	#   print('i',i, twoB[0], twoB[1])
	# print(' i',i, do, oneB[0], oneB[1], '|', twoB[0], twoB[1] )
	return i


def woy2dates( woy ):
	s = woy2date( woy ) 
	e = days_math( s, 7, '+' )-1
	return [s, e]


def days_math( epoch, days=1, do='+'):
	if do == '+':
		now = autoDate( friendlyDate( autoDate(epoch) ).split(' ')[0] ) + (  86400*days  )
	elif do == '-':
		now = autoDate( friendlyDate( autoDate(epoch) ).split(' ')[0] ) - (  86400*days  )
	else:
		print('Error: ', "days_math( epoch, days=1, do='+')")
		sys.exit()
	tdy0 = autoDate(friendlyDate( now ).split(' ')[0])
	return tdy0


def woy2datesFriendly( woy ):
	es = woy2dates( woy )
	return friendlyDate(es[0]), friendlyDate(es[1])


def dateDiffText( theDate, epoch=None ):

	y=0
	m=0
	w=0

	theDate = autoDate( theDate )
	if epoch is None:
		epoch = time.time()
	# woy = getWOY( theDate )
	days = abs(daysDiff( theDate, epoch ))
	
	if theDate < epoch:
		end = '<'
	else:
		end = '>'

	msDiff = epoch - theDate

	if msDiff > 0 and msDiff <= 86400:
		return 'today'
	elif msDiff > 0 and msDiff <= 82800:
		return 'today'
	elif msDiff > 0 and msDiff <= 169200:
		return 'yesterday'
	elif msDiff > 0 and msDiff <= 604801:
		return 'this week'



	# print( theDate, days, theDate < epoch, theDate > epoch, epoch, time.time() )
	if days == 0:
		return 'today'
	elif theDate < epoch:
		if days == 1:
			return 'yesterday'
		elif days < 7:
			return 'this week'
	elif theDate > epoch:
		if days == 1:
			return 'tommorow'
		elif days < 7:
			return 'next week'

	if days >= 365:
		tmp = float(days / 365)
		y = int(str(tmp).split('.')[0])
		days = days - ( y*365 )
	if days >= 30:
		tmp = float(days / 30)
		m = int(str(tmp).split('.')[0])
		days = days - ( m*30 )
	if days >= 7:
		tmp = float(days / 7)
		w = int(str(tmp).split('.')[0])
		days = days - ( w*7 )

	result = []
	if y:
		result.append( str(y)+'y' )
	if m:
		result.append( str(m)+'m' )
	if w:
		result.append( str(w)+'w' )
	result.append( end )
	return ' '.join( result )


def getWOY( theDate ):
	theDate = autoDate( theDate )
	woy = getWOYFromEpoch(theDate)
	year = getYearFromEpoch(theDate)
	weekAndYear = round(woy * 0.01,2) + year
	weekAndYear = str(weekAndYear)
	if len(weekAndYear) == 6:
		weekAndYear += '0' 
	return weekAndYear


def getYearFromEpoch(theDate):
	theDate = autoDate(theDate)
	return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]


def getWOYFromEpoch(theDate):
	# print('theDate:',theDate)
	theDate = autoDate(theDate)

	try:
		return datetime.datetime.fromtimestamp( theDate ).isocalendar()[1]
	except Exception as e:
		print( 'Error:', theDate )
		sys.exit()

_tz = None
arrow = None
_dir = None
pandas = None
date_datetime = None
# app.switch.= app.switch.)
updateLine_disable = False
line_length_hash_table = {}
cal_days = None
leap_years_table = None
_tar = None




