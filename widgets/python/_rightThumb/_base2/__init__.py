# import sys

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import uuid
from operator import itemgetter
from datetime import datetime as dt, timedelta
import datetime
import time
from threading import Timer

from datetime import date
from dateutil import rrule
from dateutil import relativedelta
import math
import calendar
import ast
import simplejson as json

from collections import OrderedDict
import _rightThumb._construct as __
import _rightThumb._vars as _v
import _rightThumb._string as _str

import sqlite3

import re



# print(__name__)
# print(type(__name__))
# sys.exit()

def resolveEpochTest( string, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-' ):
	# onlyEpoch = True, False, 'day'  
	# resolveEpochTest( epoch, onlyEpoch='day' )
	import _rightThumb._date as _date
	auto = _date.autoDate( string )
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
			rData = resolveEpochTest( string, 2, showPrint, showPrintTry, onlyEpoch, delim )
	

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
			rData = resolveEpochTest( string, 3, showPrint, showPrintTry, onlyEpoch, delim )



	if test == 3:

		if showPrintTry:
			print( 'try:', 3 )
		try:
			if showPrint:
				print( 'success:', 3 )
			result = ' { { ' + str(datetime.datetime.utcfromtimestamp(float(word)/1000.)) + ' } } '
			epoch = str(datetime.datetime.utcfromtimestamp(float(word)/1000.))
			rData = [ result, epoch ]
		except Exception as e:
			pass
			rData = resolveEpochTest( string, 4, showPrint, showPrintTry, onlyEpoch, delim )


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
			rData = resolveEpochTest( string, 5, showPrint, showPrintTry, onlyEpoch, delim )



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
			rData = resolveEpochTest( string, 6, showPrint, showPrintTry, onlyEpoch, delim )

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


	return rData

def txt2Date(text):
	# _.switches.trigger('Watched', _.txt2Date)

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
				print('Date error: using today\'s date')
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

uuidLogData = ''
def genUUID(project=''):
	global uuidLogData
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	if not type(uuidLogData) == str:
		uuidLogData['uuid'] = string
		uuidLogData['timestamp'] = time.time()
		if not project == '':
			uuidLogData['project'] = project
		uuidLog = getTable('uuid_log.json')
		uuidLog.append(uuidLogData)
		saveTable(uuidLog,'uuid_log.json',printThis=False)
		# _.uuidLogData = { 'uuid': theID, 'timestamp': time.time(), 'project': theProject, 'app': 'guid' }
	return string

def saveText(rows,theFile):
	# print(type(rows))
	if type(rows) == bytes:
		rows = str(rows,'utf-8')
	f = open(theFile,'w', encoding='utf-8')
	# if type(rows) == str:

	# print(type(rows))
	# f.write(str(rows))
	# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
	# f.write(rows)
	# f.write(rows.encode("iso-8859-1", "replace"))

	# print(type(rows))
	if type(rows) == str:
		# print(rows)
		f.write(rows)
	else:
		for i,row in enumerate(rows):
			# f.write(str(row) + os.linesep)
			if i == 0:
				if len(str(row)) > 0:
					f.write(str(row) + '\n')
			else:
				f.write(str(row) + '\n')
	f.close()

def getText(theFile):
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
		print('Error: No File')
		sys.exit()

	return lines

def getSize(fileobject):
	fileobject.seek(0,2) # move the cursor to the end of the file
	size = fileobject.tell()
	return size

# def formatSize(size):
#     result = ''
#     if size == None:
#         result = ''
#     elif size < 1024:
#         result = str(size) + ' B'
#     elif size > 1024 and size < 1048576:
#         num = round(size / 1024, 2)
#         result = str(num) + ' KB'
#     elif size > 1048576 and size < 1073741824:
#         num = round(size / 1048576, 2)
#         result = str(num) + ' MB'
#     elif size > 1073741824 and size < 137438953472:
#         num = round(size / 1073741824, 2)
#         result = str(num) + ' GB'
#     # if size < 1:
#     #     result = ''
#     return result

def monthByNumber(month):
	result = ''
	if str(month) == '01':
		result = 'Jan'
	if str(month) == '02':
		result = 'Feb'
	if str(month) == '03':
		result = 'Mar'
	if str(month) == '04':
		result = 'Apr'
	if str(month) == '05':
		result = 'May'
	if str(month) == '06':
		result = 'Jun'
	if str(month) == '07':
		result = 'Jul'
	if str(month) == '08':
		result = 'Aug'
	if str(month) == '09':
		result = 'Sep'
	if str(month) == '10':
		result = 'Oct'
	if str(month) == '11':
		result = 'Nov'
	if str(month) == '12':
		result = 'Dec'
	return result

def weeks_between(start_date, end_date):
	start_date = datetime.date(int(formatDateYear(start_date)),int(formatDateMonth(start_date)),int(formatDateDay(start_date)))
	start_date_monday = (start_date - datetime.timedelta(days=start_date.weekday()))
	end_date = datetime.date(int(formatDateYear(end_date)),int(formatDateMonth(end_date)),int(formatDateDay(end_date)))
	num_of_weeks = math.ceil((end_date - start_date_monday).days / 7.0)
	return num_of_weeks - 1
def months_between(start_date, end_date):
	# start_date = int(start_date)
	# end_date = int(end_date)
	# st = str(formatDateYear(start_date)) + '-' + str(formatDateMonth(start_date)) + '-' +  str(formatDateDay(start_date)) 
	# en = str(formatDateYear(end_date)) + '-' + str(formatDateMonth(end_date)) + '-' +  str(formatDateDay(end_date))
	start = datetime.date(int(formatDateYear(start_date)), int(formatDateMonth(start_date)), int(formatDateDay(start_date)) )
	end = datetime.date(int(formatDateYear(end_date)), int(formatDateMonth(end_date)), int(formatDateDay(end_date)) )
	months = calculate_monthdelta(start, end)
	return months
def calculate_monthdelta(date1, date2):
	def is_last_day_of_the_month(date):
		days_in_month = calendar.monthrange(date.year, date.month)[1]
		return date.day == days_in_month
	imaginary_day_2 = 31 if is_last_day_of_the_month(date2) else date2.day
	monthdelta = (
		(date2.month - date1.month) +
		(date2.year - date1.year) * 12 +
		(-1 if date1.day > imaginary_day_2 else 0)
		)
	# print monthdelta
	return monthdelta


def timeout(start,t):
	# os._exit(0)
	# print('loop')
	global completed
	global killTime
	global timeoutKill
	ts = dt.now()

	if start == 'start':
		timeoutKill = False
		completed = False
		killTime = ts + timedelta(seconds=int(t))

	if completed == False and ts < killTime:
		x = Timer(0.0, timeout, ('loop',t))
		x.start()
	elif completed == False:
		timeoutKill = True
		completed = True
		print('\n*** Timeout ***()')
		# os._exit(0)

def processTimeout():
	global switches
	global defaultTimeout
	if switches.isActive('Timeout') == True:
		try:
			defaultTimeout = int(switches.value('Timeout'))
		except Exception as e:
			errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(switches.value('Timeout'))", 'vars': [{'name': 'timeout', 'value': switches.value('Timeout')}], 'error': e})
			print('Error:')
			print('\tBad timeout value.')
			os._exit(0)

	# print(defaultTimeout)
	x = Timer(0.0, timeout, ('start',defaultTimeout))
	x.start()


def showLine(string,plusA='',minusA='',plusOr=False):
	# print(plusA)
	# print(string)
	global switches
	if switches.isActive('Plus') or not plusA == '':
		# print('asdf')
		result = positiveResults(string,plusA,plusOr)
	else:
		result = True
	if result == True and  (switches.isActive('Minus') or not minusA == ''):
		result = minusResults(string,minusA)
	# print(result)
	return result
def positiveResults(string,plusA='',plusOr=False):
	global switches
	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	if not plusA == '':
		plusInput = plusA
	else:
		plusInput = switches.value('Plus')
	plusInput = plusInput.lower()
	string = string.lower()
	result = False
	# print((plusInput))
	plusList = plusInput.split(',')
	length = len(plusList)
	cnt = 0
	for s in plusList:
		s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not string.find(ci(s)) == -1 or s in string:
			cnt += 1


		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result

def minusResults(string,minusA=''):
	global switches
	string = string.lower()
	result = True
	if not minusA == '':
		minusInput = minusA
	else:
		minusInput = switches.value('Minus')
	minusInput = minusInput.lower()
	try:
		for s in minusInput.split(','):
			s = s.lower()
			if len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					result = False
					break
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					result = False
					break
			if not string.find(ci(s)) == -1 or s in string:
				result = False
				break
	except Exception as e:
		pass
	return result


def saveTable(rows,theFile,tableTemp = True,printThis = True,indentCode = True):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
	if indentCode:
		dataDump = json.dumps(rows, indent=4, sort_keys=True)
	else:
		dataDump = json.dumps(rows)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + file0)

def getTable(theFile,tableTemp = True,printThis = False):
	# defaults to myTables
	if tableTemp == 'split':
		file0 = _v.myTables + _v.slash+'tablesets'+_v.slash + theFile
	elif tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile

	if printThis:
		print('Loaded: ' + file0)
	if os.path.isfile(file0) == True:
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
	else:
		json_data = []
	return json_data

def getTable3(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r') as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data

def getTable2(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
def saveTable2(rows,theFile,printThis = False):
	# print('*******************',theFile)
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)

def saveTable3(rows,theFile,printThis = False):
	# print('*******************',theFile)
	dataDump = json.dumps(rows)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + theFile)


def tempFile(rows,theFile):
	file0 = _v.stmp + _v.slash + theFile
	file = open(file0,'w')
	for r in rows:
		file.write(r)                 
	file.close()

def stamp2Date(ts):
	# print(ts)
	# print(datetime.datetime.fromtimestamp(int(ts) / 1e3))
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)
def float2Date(ts):
	if type(ts) == str:
		ts = ts.replace('_','.')
		if '.' in ts:
			ts = float(ts)
		else:
			ts = int(ts)
		# print(type(ts))
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
	# return str(datetime.datetime.fromtimestamp(ts / 1e3))
	# return str(ts)
	# return str(datetime.datetime.fromtimestamp(ts)).split('.')[0] + '\t' + str(ts)
	# return str(ts).split('.')[0] + '\t' + str(datetime.datetime.fromtimestamp(ts)).split('.')[0]
def float2Date3(ts):
	return str(datetime.datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))
def float2Date3B(ts,isJson = True):
	stmp = float2Date3(ts)
	dt = stmp.split(' ')[0]
	preResult = {'year': dt.split('-')[0],'month': dt.split('-')[1],'day': dt.split('-')[2]}
	if isJson:
		result = preResult
	else:
		result = str(preResult['year']) + '-' + str(preResult['month']) + '-' + str(preResult['day'])

	return result

def expireCheck(theDate,delim):
	now = datetime.datetime.now()
	today = now.strftime("%Y-%m-%d")
	fdtl = theDate.split(delim)
	foundDate = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
	td = str(today).split('-')
	tdd = datetime.date(int(td[0]), int(td[1]), int(td[2]))
	diff = tdd - foundDate
	return int(diff.days)

def dateDiff( theDate0, theDate1, delim='-' ):
	theDate0 = str(theDate0)
	theDate1 = str(theDate1)


	if not delim in theDate0:
		try:
			float( theDate0 )
			theDate0 = resolveEpochTest( theDate0, onlyEpoch='day', delim=delim )
			if type(theDate0) == bool:
				print( 'Error:', theDate0 )
				sys.exit()
		except Exception as e:
			print( 'Error:', theDate0 )
			sys.exit()


	if not delim in theDate1:
		try:
			float( theDate1 )
			theDate1 = resolveEpochTest( theDate1, onlyEpoch='day', delim=delim )
			if type(theDate1) == bool:
				print( 'Error:', theDate1 )
				sys.exit()
		except Exception as e:
			print( 'Error:', theDate1 )
			sys.exit()


	# print(theDate0,theDate1,delim)
	# sys.exit()
	fdtl0 = theDate0.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))

	fdtl1 = theDate1.split(delim)
	date1 = datetime.date(int(fdtl1[0]), int(fdtl1[1]), int(fdtl1[2]))

	diff = date1 - date0
	return (int(diff.days))

def dateAdd( theDate, delim, addDays ):

	theDate = str( theDate )

	if not delim in theDate:
		try:
			float( theDate )
			theDate = resolveEpochTest( theDate, onlyEpoch='day', delim=delim )
			if type(theDate) == bool:
				print( 'Error:', theDate )
				sys.exit()
		except Exception as e:
			print( 'Error:', theDate )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

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
			print( 'Error:', theDate )
			sys.exit()

	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 + datetime.timedelta(days=addDays)

def dateSub(theDate,delim,addDays):
	fdtl0 = theDate.split(delim)
	date0 = datetime.date(int(fdtl0[0]), int(fdtl0[1]), int(fdtl0[2]))
	return date0 - datetime.timedelta(days=addDays)

def listAverage(theList):
	total = 0
	for item in theList:
		total += item
	result =  total / len(theList)
	return result 
def date2epoch(theDate,delim):
	theDate = str(theDate)
	theDate = theDate.replace(delim,'-')
	fdtl = theDate.split(delim)
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
				print('Month error')
				sys.exit()
			if len(ans) == 1:
				info['m'] = 0 + ans
			elif len(ans) == 2:
				info['m'] = ans
			else:
				print('Month error')
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



def formatPhone00(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)
	data = _str.cleanBE(data,'.')
	return data

def formatPhone0(data):
	data = _str.removeAll(data,' ')
	data = _str.totalStrip4(data)

	newData = '(' + data[0] + data[1] + data[2] + ') ' + data[3] + data[4] + data[5] + '-' + data[6] + data[7] + data[8] + data[9]
	if not len(data) == 10:
		newData = 'generic error'
	if len(data) == 0:
		newData = ''
	return newData

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

def updateLine(string):
	string = str(string)
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(" " * len(string))
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(string)
	sys.stdout.flush()

def getLastTableSplit(theFile,tableTemp = 'split'):
	if tableTemp == 'split':
		basePath = _v.myTables + _v.slash+'tablesets'
	else:
		basePath = _v.stmp
	# print(basePath)
	dirList = os.listdir(basePath)
	fileList = []
	for d in dirList:
		if d.startswith(theFile):
			fileList.append(d)
	# print(fileList)
	fileList.sort()
	# print(fileList)
	# print()
	# print(fileList[len(fileList)-1])
	# print(fileList)
	# file0 = basePath + _v.slash + fileList[len(fileList)-1]
	# print(file0)
	return getTable(fileList[len(fileList)-1],tableTemp)

def saveTableSplitNew(rows,theFile,tableTemp = True,printThis = True):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash+'tablesets' + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile

	def count(cnt):
		char = 6
		cnt = str(cnt)
		lencnt = len(cnt)
		if lencnt == 1:
			cnt = '00000' + cnt
		if lencnt == 2:
			cnt = '0000' + cnt
		if lencnt == 3:
			cnt = '000' + cnt
		if lencnt == 4:
			cnt = '00' + cnt
		if lencnt == 5:
			cnt = '0' + cnt
		cnt = '_' + cnt
		return cnt

	suffix = '.json'
	cnt = 0
	path = file0 + count(cnt) + suffix
	while os.path.isfile(path) == True:
		cnt += 1
		path = file0 + count(cnt) + suffix

	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(path,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + path)

def sort(rows, name):
	global errors

	sortBy = {}
	sortList = name.split(',')
	sortList.reverse()

	### Check for bad sort input
	for item in sortList:
		item = item
		try:
			if item.count(':') > 0:
				sb = item.split(':')[1]
			else:
				sb = item
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})



	for item in sortList:
		try:
			direction = item.split(':')[0]
			sb = item.split(':')[1]
			if direction == 'asc':
			# if direction.find('a') == 0:
				rows = sorted(rows, key=itemgetter(sb))
			else:
				rows = sorted(rows, key=itemgetter(sb), reverse=True)
		except Exception as e:
			try:
				pass
				rows = sorted(rows, key=itemgetter(item))
			except Exception as e:
				errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			

		sortBy[item] = str(uuid.uuid4())
		i = 0
		for row in rows:
			rows[i][sortBy[item]] = i
			i += 1

	# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

	sortCode = 'rows = sorted(rows, key=lambda d: ('
	for item in sortList:
		sortCode += "d['" + str(sortBy[item]) + "'],"
	sortCode = sortCode[:-1]
	sortCode += '))'
	exec(sortCode)
	return rows


class Switch:

	def __init__(self, name, switch, expected_input_example):
		self.appReg = __.appReg
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = None
		self.expected_input_example = expected_input_example

	def trigger(self,script):
		self.script_trigger = script




class Switches:

	def __init__(self):
		self.index = {}
		self.switches = []
		self.appReg = __.appReg

	def regtest(self):
		print(self.appReg)
	def register(self, name, switch, expected_input_example = None):
		self.switches.append(Switch(name, switch, expected_input_example))

	def fieldSet(self,name,column,value):# updateSwitchField
		if column == 'value':
			if self.fieldExists(name,'script_trigger') == True:
				value = self.scriptTrigger(name,value)
				# self.fieldGet(name,'script_trigger')(value)
			elif self.fieldExists(name,'script_trigger') == True:
				script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)# script_trigger_external
				value = eval(script)
		
		for i,row in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if row.name == name:
					if column == 'active':
						if value == True:
							self.switches[i].active = True
						else:
							self.switches[i].active = False
					elif column == 'value':
						if value == True:
							self.switches[i].value = True
						elif value == False:
							self.switches[i].value = False
						else:
							self.switches[i].value = value

					else:
						value = str(value)
						try:
							exec('self.switches[i].' + column + '=str(\'' + value + '\')')
						except Exception as e:
							exec('self.switches[i].' + column + '=\'' + value + '\'')
			
		return ''



	def fieldExists(self,name,column):# doesFieldExist
		result = False
		try:
			for i,row in enumerate(self.switches):
				if self.switches[i].appReg == __.appReg:
					if row.name == name:
						eval('row.' + column)
						result = True
		except Exception as e:
			result = False
		return result
	def scriptTrigger(self,name,value):# externalScriptTrigger
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					value = self.switches[i].script_trigger(value)# script_trigger_external
		return value

	def fieldGet2(self,name,column):# getSwitchField
		# print(name,column)
		result = ''
		for i,row in enumerate(self.switches):
			if row.name == name:
				result = eval('row.' + column)
		return result

	def fieldGet(self,name,column):# getSwitchField
		# print(name,column)
		# switch = self.switches
		# result = ''
		# for row in switch:
		#     if row.name == name:
		#         result = eval('row.' + column)




		result = ''
		if not column == 'pos':
			i = self.searchIndex( name )
			if i is None:

				if column == 'active':
					return False

				if column == 'value':
					return ''

				print( 'Error: Nonexistent Switch' )
				sys.exit()
			row = self.switches[i]
			result = eval('row.' + column)

		else:
			switch = self.switches
			result = ''
			for row in switch:
				if row.name == name:
					result = eval('row.' + column)
		return result

	def isActive(self,name):# isSwitchActive
		return self.fieldGet(name,'active')

	def value(self,name):# getSwitchValue
		result = self.fieldGet(name,'value')
		if result is None:
			result = ''
		return result

	def trigger(self,name,script):
		for i,s in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if name == self.switches[i].name:
					self.switches[i].trigger(script)


	def value2(self,name):
		switchInput = sys.argv

		try:
			switchInput[self.fieldGet(name,'pos') + 1]
			result = ''

			i = 0
			for a in switchInput:
				if i > self.fieldGet(name,'pos'):
					if self.isSwitch(switchInput[i]) == True:
						break
					else:

						if switchInput[i] == ':':
							switchInput[i] = switchInput[i].replace(':','_;192B;_')
						if switchInput[i] == ',':
							switchInput[i] = switchInput[i].replace(',','_;192A;_')
						result += str(switchInput[i]) + ','
				i += 1
			result = result[:-1]
			result = _str.cleanAll(result,'"','')
			result = _str.cleanAll(result,':,',':')
			result = _str.cleanAll(result,',,',',')

		except Exception as e:
			result = None
		return result
	def isSwitch(self,string):# checkIfSwitch
		result = False
		for i,a in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				for b in a.switch.split(','):
					if b == string:
						result = True
					# print(b,result)
		return result

	def format(self,name):# processSwitchFormatting
		value = self.value2(name)
		if self.fieldExists(name,'script_trigger') == True:
			value = self.scriptTrigger(name,value)
		elif self.fieldExists(name,'script_trigger') == True:
			script = '{}(\'{}\',\'{}\')'.format(self.fieldGet(name,'script_trigger'),name,value)
			value = eval(script)
		return value

	def exists(self,name):# checkSwitchExist
		result = False
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.name == name:
					result = True
		return result

	def process(self,helpx=False):
		global customHelp
		global argvProcess

		for ii,sw in enumerate(self.switches):
			if self.switches[ii].appReg == __.appReg:
				self.switches[ii].pos = None
				self.switches[ii].active = False
				self.switches[ii].value = None
		if argvProcess:
			for i,a in enumerate(sys.argv):
				a = a.replace(':','')
				for ii,sw in enumerate(self.switches):
					for s in sw.switch.split(','):
						if s.lower() == a.lower():
							if self.switches[ii].appReg == __.appReg:
								self.switches[ii].pos = i
								self.switches[ii].active = True
								self.switches[ii].value = self.format(self.switches[ii].name)

		if self.exists('_Raw') == True:
			# print('test')
			self.fieldSet('_Raw','pos',1)
			self.fieldSet('_Raw','active',True)
			self.fieldSet('_Raw','value',self.format('_Raw'))

		for i,record in enumerate(self.switches):
			self.index[self.switches[i].name] = i


		if self.isActive('Help') == True or helpx:
			global appInfo
			# os.system('cls')
			print('')
			try:
				print('Description: \t', appInfo[__.appReg]['description'] + '\n')
				configured = True
			except Exception as e:
				configured = False
			try:
				if len(appInfo[__.appReg]['prerequisite']) > 0:
					print('Prerequisite:')
					for prereq in appInfo[__.appReg]['prerequisite']:
						print('\t' + prereq)
					print('\n')
			except Exception as e:
				pass
			try:
				if len(appInfo[__.appReg]['relatedapps']) > 0:
					print('Related Apps:')
					for relapps in appInfo[__.appReg]['relatedapps']:
						print('\t' + relapps)
					print('\n')
			except Exception as e:
				pass

			if configured:
				if len(appInfo[__.appReg]['examples']) > 0:
					print('Examples:')
					for ex in appInfo[__.appReg]['examples']:
						print('\t' + ex)
					print('\n')
				if len(appInfo[__.appReg]['columns']) > 0:
					print('Columns and abbreviations:')
					result = ''
					for col in appInfo[__.appReg]['columns']:
						result += col['name'] + '(' + col['abbreviation'] + '), '
					result = result[:-2]
					print('\t' + result + '\n')
					# print('\n')
			self.print()
			sys.exit()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			# self.print()
			self.printStatus()
			sys.exit()

		# theErrors()

	def searchIndex( self, name ):

		try:
			result = self.index[ name ]
		except Exception as e:
			result = None

		return result


	def print(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				switch.append({'name':sw.name ,'switch':sw.switch,'expected_input_example': sw.expected_input_example})
		# def test(value):
		#     value = value + '_V_'
		#     return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,switch,expected_input_example')
	def printStatus(self):
		switch = []
		global tables
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				if sw.active:
					active = 'True'
				else:
					active = 'False'
				value = sw.value
				if sw.value == True:
					value = 'True'
				elif sw.value == False:
					value = 'False'

				switch.append({'name':sw.name ,'active':active,'value': value})
		# def test(value):
		#     value = value + '_V_'
		#     return value
		tables.register('switches',switch)
		# tables.trigger('switches','switch,name',test,True)
		tables.print('switches','name,active,value')
	def length(self):
		ii = 0
		for i,sw in enumerate(self.switches):
			if self.switches[i].appReg == __.appReg:
				ii += 1
		return ii

#     def getSelf(self,name):
#         result = ''
#         for sw in self.switches:
#             if sw.name == name:
#                 result = sw
#         return result
# def getSwitchSelf(name):
#     global switches
#     return switches.getSelf(name)
def ci2(string):
	string = ci(string)
	string = _str.replaceAll(string,',',' ')
	return string

class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table
		# print(self.name)



class Table:

	def __init__(self,name,asset=[]):
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print()
			# for x in dir(self.views[i]):
			#     print(x)

			if self.views[i].name == name:
				# print('found')
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				# print(switches.value('Sort'))
				# try:
					
				# except Exception as e:
				#     pass
				# print('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#     self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if switches.isActive('Length'):
			result = self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += '  .' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += '  .' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print('*** ' + name)
		size = len(name) + spacer
		
		# print(name,00)
		# rows[0][name]
		try:
			pass
			rows[0][name]
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			print('Error:')
			print('\tBad column input.')
			print(9)
			print(name)
			os._exit(0)
		# print(name)
		for item in rows:
			shorten = True
			if switches.isActive('Long') == True:
				shorten = False
				if switches.isActive('ShortenColumn') == True:
					shortenColumn = switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
				
			if shorten == True and not switches.isActive('Length'):
				text = self.nameLength(item[name],'')
			else:
				if switches.isActive('Length'):
					# print('asdf')
					# sys.exit()
					text = self.nameLengthFix(item[name],switches.value('Length'),'')
				else:
					# sys.exit()
					text = item[name]
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print('ran')
		field = field.lower()
		i = 0
		value = ''
		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1
		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader
		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print(rows)

		columnList = column
		value = self.triggerExecute(column,str(rows[i][column]))
		# value = rows[i][column]
		# print(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if switches.isActive('Long') == True:
			shorten = False
			if switches.isActive('ShortenColumn') == True:
				shortenColumn = switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = switches.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							print(self.groupLine(columnList,columnHeaderLength))
							for g in groupBy.split(','):
								groupByList[g] = ''
						else:
							print('')
						groupByList[gb] = text
					else:
						pass
						text = ''
		alignment = self.fieldProfileGet(column,'alignment')
		# print(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print(column,theLeft,theRight,'0' + result + '0')
			# print(totalSpace,theLeft,theRight)
		#     result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ''
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',True)
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'right'


			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		result += '\n'
		return result


	def print(self,column,fieldLengths=False):
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print(column)
		# print(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()
		global errors
		global switches
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			column += cs.split('=')[0] + ','
			# print(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								if len(str(dpi[dpic])) > 1:
									hasData = True
								y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print(newData)
			# print('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print('IS')
								# print(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if switches.isActive('PlusOr') == True:
										#     if cnt > 0:
										#         rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(ci(s)) == -1:
												cnt += 1
											# if not string.find(ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print(self.asset)






		if not type(self.asset) == list or len(self.asset) == 0:
			print('Table Blank')
			sys.exit()



		# if not len(groupByList):
		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		# if not column == False:
			# switches.fieldSet('Column','value',column)
			# column = switches.value('Column')
		if switches.isActive('Sort') == True:
			self.asset = self.sort()
		elif switches.isActive('GroupBy') == True:
			
			switches.fieldSet('Sort','active',True)
			switches.fieldSet('Sort','value',switches.value('GroupBy'))
			self.asset = self.sort()
		# print('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		print(columnHeader)
		i = 0
		# print(self.asset)
		for item in self.asset:
			# print(item)
			result = ''    
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print(result)
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					errors.append({'id': 12, 'function': 'print()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					print('Error:')
					print('\tBad column input.')
					print(12)
					print(c)
					print(12)
					os._exit(0)
			# print(_str.totalStrip5(result)) #TESTING
			if len(result) > 0:
				print(result)
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:

				print('')
		if len(oldData) > 0:
			self.asset = oldData
	def sort(self):# sortThis
		rows = self.asset
		global errors
		global switches
		# self.sort = name
		delim = '.'
		name = switches.value('Sort')
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})


		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = item.split(delim)[1]
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(item))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				

			sortBy[item] = str(uuid.uuid4())
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True):
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(_v.myTables) + str(_v.slash) + str(theFile)
		else:
			file0 = _v.stmp + _v.slash + theFile
		dataDump = json.dumps(self.asset, indent=4, sort_keys=True)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		if printThis:
			print('Saved: ' + file0)
	def get(self,theFile = '',tableTemp = True,printThis = False):
		if theFile == '':
			theFile = self.file
		self.file = theFile
		# defaults to myTables
		if tableTemp == True:
			file0 = _v.myTables + _v.slash + theFile
		else:
			file0 = _v.stmp + _v.slash + theFile
		if printThis:
			print('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = json.load(json_file)
				# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

class Tables:

	def __init__(self):
		self.tables = []

		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'


	def register(self,name,asset = []):
		i = 0
		found = False
		for t in self.tables:
			if t.name == name:
				found = True
				if len(asset) > 0:
					self.tables[i].set(asset)
			i += 1
		if not found:
			self.tables.append(Table(name,asset))

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False):
		# print(name,fields)
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					self.tables[i].print(fields,fieldLengths)
				else:
					print('Table Blank')
			i += 1

	def sort(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#     if spaces > totalColumnWidth:
		#         totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#     if not type(fieldLengths) == dict:
		#         fieldLengths = data
		#     for name in fieldLengths.keys():
		#         if data[name] > fieldLengths[name]:
		#             fieldLengths[name] = data[name]




		# for m in self.meta['data']:
		#     genLine(totalColumnWidth,'=')
		#     print('Table:\t',m['table'])
		#     print('Parent:\t',m['parent'])
		#     print('Records:',m['count'])
		#     print()
		#     tables.register(m['table'],m['fields'])
		#     tables.fieldProfileSet(m['table'],'*','alignment','center')
		#     tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#     genLine(totalColumnWidth,'=')
		# print()
		# print('Records:',self.meta['records'])
		# print()
		# print('Errors:')
		# for e in self.meta['errors']:
		#     print('\t',e)

		return result

###########################################################################################
def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
	return hash_md5.hexdigest()


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
	elif size > 1024 and size < 1048576:
		num = round(size / 1024, 2)
		result = str(num) + ' KB'
	elif size > 1048576 and size < 1073741824:
		num = round(size / 1048576, 2)
		result = str(num) + ' MB'
	elif size > 1073741824 and size < 1099511627776    :
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	else:
		num = round(size / 1099511627776, 2)
		result = str(num) + ' TB'
	# if size < 1:
	#     result = ''
	return result

def unFormatSize(size):
	size = str(size)
	size = size.upper()
	factor = ''

	if 'TB' in size:
		factor = 1099511627776    
	elif 'GB' in size:
		factor = 1073741824
	elif 'MB' in size:
		factor = 1048576
	elif 'KB' in size:
		factor = 1024
	else:
		factor = 1
	size = size.replace('T','')
	size = size.replace('B','')
	size = size.replace('M','')
	size = size.replace('K','')
	size = size.replace('G','')
	size = float(size)
	result = round(size * factor,0)
	return result

def timeAgo(do=''):
	if len(do) == 0:
		do = switches.value('Ago')
	do = do.lower()
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
		start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
	if 'm' in do:
		start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
	if 'w' in do:
		start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
	if 'd' in do:
		start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
	dT = str(start_date)
	# print(dT)
	# print(dT)
	# print(dT)
	# print(dT)
	d = dT.split('-')
	result = datetime.datetime(int(d[0]),int(d[1]),int(d[2]),0,0).timestamp()

	# print(start_date)
	# print(result)]
	# print(result)
	return result
def epoch(string,end=False):
	string = str(string)
	if '.' in string:
		d = string.split('.')
	elif _v.slash in string:
		d = string.split(_v.slash)
	elif '-' in string:
		d = string.split('-')
	elif len(string) == 6:
		t = string[:4] + '-' + string[-2:]
		d = t.split('-')
	elif len(string) == 8:
		x = string[-4:]
		t = string[:4] + '-' + x[:2] + '-' + x[-2:]
		d = t.split('-')

	if not len(d) == 3:
		day = 1
	else:
		day = d[2]
	# print(d)
	# sys.exit()
	if end:
		y = int(d[0])
		m = int(d[1])
		if m == 12:
			y += 1
			m = 1
		else:
			m += 1
		start_date = datetime.datetime(y,m,1,0,0) + datetime.timedelta(-1)
		result = start_date.timestamp()
	else:
		result = datetime.datetime(int(d[0]),int(d[1]),int(day),0,0).timestamp()
	# result = d
	return result
def isNu(string):
	result = True
	for s in string:
		try:
			int(s)
		except Exception as e:
			result = False
	return result
def isNu2(string):
	result = True
	string = str(string).replace('.','').replace('-','').replace(_v.slash,'').replace('/','')
	try:
		try:
			int(string)
		except Exception as e:
			float(string)
	except Exception as e:
		result = False
	return result
def number2Words(n):
	global numberWords
	try:
		numberWords
		if len(numberWords) == 0:
			numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	except Exception as e:
		numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	numberWords = getText(_v.myTables + _v.slash+'numberWords.txt')
	if type(n) == int:
		result = numberWords[n].replace(' ','_').replace('-','_').replace('\n','')
	else:
		result = n.replace(' ','_')
	return result
###########################################################################################

class Database:

	def __init__(self, data):

		appDB = '_Generated_App_Database.db'
		appJSON = '_Generated_App_Database_Config.json'
		appPyRaw = '_Gen_App_Database_Data'
		appPy = appPyRaw + '.py'
		self.appPyDefault = _v.myDatabases + _v.slash+'_default.py'


		self.data = {}
		self.tables = []
		self.name = data.replace(appDB,'').replace(appJSON,'').replace(appPy,'').replace('.json','')
		if os.path.isfile(self.name + appDB):
			self.appDB =   self.name + appDB
			self.appJSON = self.name + appJSON
			self.appPy =   self.name + appPy

		else:
			self.appDB = _v.myDatabases + _v.slash + self.name + appDB
			self.appJSON = _v.myDatabases + _v.slash + self.name + appJSON
			self.appPy = _v.myDatabases + _v.slash + self.name + appPy
		self.appPyRaw = self.name + appPyRaw

		self.tableDelim = '_x_'

		self.meta = []

	def registerTable(self, name):
		self.tables.append(TablesDB(name))

	def TableFieldCount(self):
		result = 0
		for i,ci in enumerate(self.tables):
			if ci.name == name:
				result = self.tables[i].getCount()
		return result
# {
#     'table': 'table,name',
#     'fields': [
#         {'names': 'one,two'},
#         {'names': 'three', 'table': 'name', 'as': 'threeish'}
#     ],
#     'action': [
#        { 'type': 'text', 'names': 'field', 'table': 'your_mom', 'search': '*.txt,desktop'},
#        { 'type': 'text', 'names': 'testy', 'and_or': 'or', 'table': 'or_test', 'search': '*.py,*.txt'},
#         { 'type': 'field_type(text)', 'table': 'name', 'names': 'field,names', 'and_or': 'and',  'search': '*.py,tech'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': '1000,2000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'g,1000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'l,1000'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(ago(2000))'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07))'},
#         { 'type': 'field_type(number)', 'names': 'field,names', 'search': 'str(epoch(2018.07)),str(epoch('2018.10',True))'},
#         { 'type': 'field_type(sort)', 'names': 'field', 'order': 'asc'},
#         { 'type': 'field_type(sort)', 'names': 'field', 'order': 'desc'},
#     ]
# }    

	def queryBuilder(self,data): # queryBuilder
		self.data = data
		# print(data['fields'])
		# sys.exit()
		self.qbFields = []
		tbls = data['table'].split(',')
		if len(tbls) > 1:
			multi_Table = True
		else:
			multi_Table = False
		if multi_Table:
			sql = 'SELECT '
			# print(data['fields'])
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' '
			for iJ,tJ in enumerate(tbls):
				if iJ > 0:
					sql += ' JOIN ' + tJ + ' ON ' + tJ + '.id_parent = ' + tbls[0] + '.id_uuid '
				
			sql += ' WHERE '
		else:
			sql = 'SELECT '
			for field in data['fields']:
				for name in field['names'].split(','):
					thisT = ''
					try:
						thisT = field['table']
					except Exception as e:
						thisT =  tbls[0]
					try:
						asF = field['as']
					except Exception as e:
						asF =  name
					name = "" + thisT + '.' + name + " AS " + asF
					self.qbFields.append(asF)
					sql += name + ', '
			sql = _str.cleanLast(sql,', ')
			sql += ' FROM ' + tbls[0] + ' WHERE '
		# JOIN albums ON albums.albumid = tracks.albumid
		orderBy = False
		for i,action in enumerate(data['action']):
			if action['type'] == 'text':
				sql += '('
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "" + thisT + '.' + name + ""
					try:
						and_or = action['and_or']
					except Exception as e:
						and_or =  'and'
					for tv in action['search'].split(','):
						if tv.startswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '%" + tv + "' " + and_or + ' '
						elif tv.endswith('*'):
							tv = tv.replace('*','')
							sql += ' ' + name + " like '" + tv + "%' " + and_or + ' '
						else:
							sql += ' ' + name + " like '%" + tv + "%' " + and_or + ' '
				sql = _str.replaceDuplicate(sql,' ')
				sql = _str.cleanLast(sql,' and ')
				sql = _str.cleanLast(sql,' or ')
				sql += ') and '
			sql = sql.replace('WHERE and ','WHERE ')
			if action['type'] == 'number':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						print('bad input')
						sys.exit()
					if isNu(coin[0]):
						do = 'b'
					else:
						do = coin[0]
					if do == 'b':
						sql += name + ' > ' + str(coin[0]) + " and " + name + " < " + str(coin[1]) + ' and '
					if do == 'l':
						sql += name + ' < ' + str(coin[1]) + ' and '
					if do == 'g':
						sql += name + ' > ' + str(coin[1]) + ' and '












			if action['type'] == 'date':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if not len(coin) == 2:
						if isNu2(coin[0]):
							sql += name + ' > ' + str(epoch(coin[0])) + ' and '
						else:
							sql += name + ' > ' + str(timeAgo(coin[0])) + ' and '
					else:
						if isNu2(coin[0]):
							do = 'b'
						else:
							do = coin[0]
						if do == 'b':
							sql += name + ' > ' + str(epoch(coin[0])) + " and " + name + " < " + str(epoch(coin[1],True)) + ' and '
						if do == 'l':
							sql += name + ' < ' + str(epoch(coin[1])) + ' and '
						if do == 'g':
							sql += name + ' > ' + str(epoch(coin[1])) + ' and '




			if action['type'] == 'bytes':
				for name in action['names'].split(','):
					if multi_Table:
						try:
							thisT =  action['table']
						except Exception as e:
							thisT =  tbls[0]
						name = "'" + thisT + '.' + name + "'"

					coin = action['search'].split(',')
					if coin[0] == 'l':
						sql += name + ' < ' + str(unFormatSize(coin[1])) + ' and '
					elif coin[0] == 'g':
						sql += name + ' > ' + str(unFormatSize(coin[1])) + ' and '
					else:
						sql += name + ' > ' + str(unFormatSize(coin[0])) + " and " + name + " < " + str(unFormatSize(coin[1])) + ' and '














			if action['type'] == 'sort':
				orderBy = True
		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		if orderBy:
			sql += ' ORDER BY '
			for i,action in enumerate(data['action']):
				if action['type'] == 'sort':
					try:
						if 'a' in action['order'].lower():
							order = 'ASC'
						else:
							order = 'DESC'
					except Exception as e:
						order = 'ASC'
					for name in action['names'].split(','):
						if multi_Table:
							try:
								thisT =  action['table']
							except Exception as e:
								thisT =  tbls[0]
							name = "'" + thisT + '.' + name + "'"
						sql += name + ' ' + order + ', '

		sql = _str.cleanLast(sql,' and ')
		sql = _str.cleanLast(sql,' or ')
		sql = _str.cleanLast(sql,', ')
		sql = _str.replaceDuplicate(sql,' ')
		sql = _str.cleanLast(sql,' ')
		sql += ';'
		sql = sql.replace('WHERE;',';')
		return sql
	def metaGen(self):
		import numpy as np
		meta = []
		con = sqlite3.connect(self.appDB)
		for line in con.iterdump():
			if 'CREATE TABLE' in line and not 'INSERT INTO' in line:
				# print(line)
				one = line.split('CREATE TABLE ')[1]
				two = one.split(' (')
				table = two[0]
				# print(table)
				fieldRaw = two[1].split(')')[0]
				f = []
				for field in fieldRaw.split(', '):
					# print('\t',field)
					fd = field.split(' ')
					f.append({'type': fd[1], 'field': fd[0], 'max': 0, 'min': 0, 'average': 0})


				if self.tableDelim in table:
					parent = ''
					mx = len(table.split(self.tableDelim))-1
					for iT,tX in enumerate(table.split(self.tableDelim)):
						if iT < mx:
							parent += tX + self.tableDelim
					parent = _str.cleanLast(parent,self.tableDelim)
				else:
					parent = ''


				meta.append({'table': table, 'parent': parent, 'fields': f})
			elif 'INSERT INTO' in line:
				pass
				# break
		average = {}
		for im,m in enumerate(meta):
			sql = 'SELECT * FROM ' + m['table']
			conn = sqlite3.connect(self.appDB)
			c = conn.cursor()
			c.execute(sql)
			rows = c.fetchall()
			for row in rows:
				# print(row)
				for fi,field in enumerate(m['fields']):
					# print(field['field'],row[fi])
					aKey = str(m['table']) + '-' + str(number2Words(field['field']))
					# print(aKey)
					
					try:
						if not type(average[aKey]['datapoints']) == list:
							average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}

						# print(type())                        
					except Exception as e:
						average[aKey] = {'max': 0, 'min': 'first', 'average': 0, 'datapoints': [], 'count': 0}
					average[aKey]
					# print(aKey)
					if field['type'] == 'int':
						if type(row[fi]) == int:
							size = row[fi]
						else:
							string = re.sub('[^0-9]', '', str(row[fi]))
							# print(type(string),string)
							# print(string)
							if len(string) == 0:
								size = 0
							else:
								size = int(string)
					if field['type'] == 'str':
						size = len(str(row[fi]))
					# print()
					# print(type(average[aKey]['max']),average[aKey]['max'])
					# print(type(size),size)
					if average[aKey]['max'] < size:
						average[aKey]['max'] = size
					if average[aKey]['min'] == 'first':
						average[aKey]['min'] = size
					elif average[aKey]['min'] > size:
						average[aKey]['min'] = size
					average[aKey]['datapoints'].append(size)

		errors = []
		totalCount = 0
		for im,m in enumerate(meta):

			for row in rows:
				# print(row)
				for fi,field in enumerate(m['fields']):
					# print(meta[im]['fields'][fi]['max'])
					aKey = m['table'] + '-' + number2Words(field['field'])
					# print(aKey)
					try:
						# print(average[aKey]['max'])
						meta[im]['fields'][fi]['max'] = average[aKey]['max']
						meta[im]['fields'][fi]['min'] = average[aKey]['min']
						meta[im]['fields'][fi]['average'] = int(np.mean(average[aKey]['datapoints']))
						meta[im]['count'] = len(average[aKey]['datapoints'])
						total = meta[im]['count']
					except Exception as e:
						errors.append(aKey)
				totalCount += total

		self.meta = {'data': meta, 'records': totalCount, 'errors': errors}
		saveTable2(meta,'database_meta.json')

		return meta
	def metaPrint(self):
		if self.meta == []:
			self.metaGen()

		totalColumnWidth = 0
		for m in self.meta['data']:
			tables.register(m['table'],m['fields'])
			spaces = tables.getLength(m['table'],'type,field,max,min,average')
			if spaces > totalColumnWidth:
				totalColumnWidth = spaces



		# fieldLengths = 0
		# for m in self.meta['data']:
		#     tables.register(m['table'],m['fields'])
		#     data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#     if not type(fieldLengths) == dict:
		#         fieldLengths = data
		#     for name in fieldLengths.keys():
		#         if data[name] > fieldLengths[name]:
		#             fieldLengths[name] = data[name]




		for m in self.meta['data']:
			genLine(totalColumnWidth,'=')
			print('Table:\t',m['table'])
			print('Parent:\t',m['parent'])
			print('Records:',m['count'])
			print()
			tables.register(m['table'],m['fields'])
			# tables.fieldProfileSet(m['table'],'*','alignment','center')
			# tables.print(m['table'],'type,field,max,min,average',fieldLengths)
			tables.print(m['table'],'type,field,max,min,average')

			genLine(totalColumnWidth,'=')
		print()
		print('Records:',self.meta['records'])
		print()
		print('Errors:')
		for e in self.meta['errors']:
			print('\t',e)
		print()
		print()
		print('Example:')
		print('\t p dba -app',self.name)
		print()
		print()
	def findParent(self,table):
		# parent = 'Error'
		# for m in self.meta['data']:
		#     if m['table'] == table:
		#         parent = m['parent']
		#         break
		if self.tableDelim in table:
			parent = ''
			mx = len(table.split(self.tableDelim))-1
			for iT,tX in enumerate(table.split(self.tableDelim)):
				if iT < mx:
					parent += tX + self.tableDelim
			parent = _str.cleanLast(parent,self.tableDelim)
		else:
			parent = ''
		return parent

	def findChildren(self,table):
		if self.meta == []:
			self.metaGen()
		children = []
		for m in self.meta['data']:
			if m['parent'] == table:
				children.append(m['table'])

		return children

	def findType(self,column):
		mainTable = self.data['table'].split(',')[0]
		found = False
		nm = ''
		result = ''

		for action in self.data['fields']:
			for name in action['names'].split(','):
				if name == column:
					try:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']
					except Exception as e:
						pass

		if len(result) == 0:
			for action in self.data['action']:
				for name in action['names'].split(','):
					if name == column:
						if action['type'] == 'date' or 'byte' in action['type']:
							result = action['type']

		if len(result) == 0:
			for field in self.data['fields']:
				try:
					table = field['table']
				except Exception as e:
					table = mainTable
				if ',' in field['names']:
					for name in field['names'].split(','):
						if name == column:
							nm = name
							found = True
				else:
					try:
						newName = field['as']
					except Exception as e:
						newName = field['names']
					if newName == column:
						nm = newName
						found = True
				# print(field)
				if found:
					break

			result = self.checkConfig(table,nm)
		# print(mainTable)
		return result
	def checkConfig(self,tbl,nm):
		self.appJSON
		# print(self.appJSON)
		# print(tbl,nm)
		structure = getTable2(self.appJSON)
		result = ''
		if tbl == structure['name']:
			for zs in structure['zstructure']:
				if zs['field'] == nm:
					result = zs['type']
					break
		return result

	def executeSQL(self,sql,group=0):
		conn = sqlite3.connect(self.appDB)
		c = conn.cursor()
		c.execute(sql)
		all_rows = c.fetchall()
		records = []
		for f in all_rows:
			row = {}
			for ic,c in enumerate(self.qbFields):
				row[c] = f[ic]

			records.append(row)
		col = ''
		for c in self.qbFields:
			col += c + ','
		col = _str.cleanLast(col,',')
		tables.register('sql',records)
		for ic,c in enumerate(self.qbFields):
			if self.findType(c) == 'date':
				tables.fieldProfileSet('sql',c,'trigger',float2Date2)
			if 'byte' in self.findType(c):
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			if self.findType(c) == 'bytes':
				tables.fieldProfileSet('sql',c,'trigger',formatSize)
			# print(self.findType(c))
		tables.print('sql',col)


















class TablesDB:

	def __init__(self):
		self.columns = []

	def register(self, name):
		self.columns.append(ColumnsDB(name))
		self.fieldCount = len(self.columns)

	def getCount(self):
		return self.fieldCount


class ColumnsDB:

	def __init__(self, name, kind):
		self.name = name
		self.active = False
		self.kind = kind

	# def trigger(self,script):
	#     self.script_trigger = script

	# def changeStatus(self,newStatus):
	#     self.active = newStatus

	# def print(self):
	#     childItems = []
	#     for ci in self.columns:
	#         childItems.append({'name':ci.name})
	#     tables.register('childClassItems',childItems)
	#     # tables.trigger('switches','switch,name',test,True)
	#     tables.print('childClassItems','name')


	#         childItems.append({'name':ci.name ,'active':active,'value': value})
	#     tables.register('childClassItems',childItems)
	#     tables.print('childClassItems','name,active,value')

	# def status(self,name,newStatus):
	#     for i,ci in enumerate(self.columns):
	#         if ci.name == name:
	#             self.columns[i].changeStatus(newStatus)


###########################################################################################
def get_size(obj, seen=None):
	# https://medium.com/@alexmaisiura/python-how-to-reduce-memory-consumption-by-half-by-adding-just-one-line-of-code-56be6443d524
	# From https://goshippo.com/blog/measure-real-size-any-python-object/
	# Recursively finds size of objects
	size = sys.getsizeof(obj)
	if seen is None:
		seen = set()
	obj_id = id(obj)
	if obj_id in seen:
		return 0


###########################################################################################
def genLine(count,what):
	count = int(count)
	what = str(what)
	cnt = 0
	result = ''
	while cnt < count:
		result += what
		cnt += 1
	print(result)
	return result


def ci(string): 
	#switchValueClean
	string = string.replace(';;',',')
	string = string.replace(';p','%')
	string = string.replace(';p;','%')
	string = string.replace(';q;','"')
	string = string.replace(';.',':')
	string = string.replace(";'",'"')
	string = string.replace(";;'",_v.slash+'"')
	string = string.replace('_;192A;_',',')
	string = string.replace('_;192B;_',':')
	string = string.replace(_v.slash+'n','\n')
	string = string.replace(';n','\n')
	string = string.replace(';t','\t')
	string = string.replace('"\'"',"'")
	string = string.replace('"\'", "\'"',"','")
	string = string.replace(';return','\n')
	string = string.replace(';-','-')
	string = string.replace('[star]','*')
	string = string.replace('[a]','*')
	string = string.replace('[eq]','=')

	string = string.replace('[pipe]','|')

	string = string.replace('null00','"",')

	return string
errors = []
appInfo = {}
appData = {}


switches = Switches()

switches.register('Help', '?,/?,-?,/h,help,/help,-help,--help')
switches.register('Column', '-c,-column', 'size, name')
switches.register('Sort','-s,-sort', 'Asc:type, Desc:ext')
switches.register('Debug', '-d,-debug')
switches.register('Errors', '-e,-Error,-Errors', '8,11 OR hide:8,11')
switches.register('Timeout', '-t,-Timeout')
switches.register('GroupBy', '-g,-group,-groupby', 'ext, month')
switches.register('ShortenColumn', '-sc,-shortencolumn')
switches.register('Long', '-l,-long')
switches.register('Length', '-length','x3')
switches.register('Report', '-report')
switches.register('Plus', '+')
switches.register('Minus', '-')
switches.register('PlusOr', '-or')
switchDefault = switches.length()

tables = Tables()

argvProcess = True







