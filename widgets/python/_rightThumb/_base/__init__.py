# import _rightThumb._base as _

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

'''
p[0] = _.svc(p[0])

### VAR ###
_.columnNickname = []
_.errors = []
_.switch = []
_.tableProfile = []
_.defaultTimeout = 60
_.maxNameLength = 35

### FUNCTIONS ###

# Main
_.processSwitches(switchInput)
_.listPrintColumn(rows,'n,column')





# Switch
_.processSwitches(switchInput)
_.isSwitchActive('name')
_.getSwitchValue('name')
_.getSwitchField('name','column')
_.updateSwitchField('name','column','value')
_.doesFieldExist('name','column')
_.printSwitches()

# Tools
_.nameLength(string,suffix)
_.countThis(rows)
_.getSize(fileobject)
_.formatSize(size)
_.monthByNumber(month)
_.weeks_between(start_date, end_date)
_.months_between(start_date, end_date)
_.calculate_monthdelta(date1, date2)
'''

import _rightThumb._string as _str
import _rightThumb._vars as _v

'''
_str.replaceAll(string,rWhat,rWith)
_str.cleanAll(string,rWhat,rWith)
_str.removeAll(string,rWhat)
_str.replaceDuplicate(string,rWhat)
_str.cleanEnd(string,rWhat)
'''

###################################################
# import _rightThumb._getPipe as _getPipe


import sys
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
# from dateutil.rrule import rrule, MONTHLY
# from datetime import datetime
from dateutil import relativedelta
import math
import calendar
import ast
import simplejson as json

from collections import OrderedDict

# import arrow

# DEFAULT_TIMEOUT = 1

# for x in sys.argv:
#     print(x)
# print('')
# os.listdir(sys.argv[1]) # returns list


#################################################################

def getSize(fileobject):
	fileobject.seek(0,2) # move the cursor to the end of the file
	size = fileobject.tell()
	return size

def formatSize(size):
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
	elif size > 1073741824 and size < 137438953472:
		num = round(size / 1073741824, 2)
		result = str(num) + ' GB'
	# if size < 1:
	#     result = ''
	return result





#########################################################
#########################################################

#########################################################
#########################################################

def nameLength(string,suffix):
	global maxNameLength
	result = ''
	toLong = False
	try:
		i = 0
		for L in string:
			if i <= maxNameLength:
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


#########################################################
#########################################################

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


def tabGetMaxSpace(rows,name):
	global errors
	spacer = 1
	# print('*** ' + name)
	size = len(name) + spacer
	try:
		pass
		rows[0][name]
	except Exception as e:
		errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
		print('Error:')
		print('\tBad column input.')
		print(name)
		os._exit(0)
	# print(name)
	for item in rows:
		shorten = True
		if isSwitchActive('Long') == True:
			shorten = False
			if isSwitchActive('ShortenColumn') == True:
				shortenColumn = getSwitchValue('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == name:
						shorten = True

		if shorten == True:
			text = nameLength(item[name],'')
		else:
			text = item[name]
		
		itemSize = len(str(text)) + spacer
		if itemSize > size:
			size = itemSize
		# print(item)
	return size

def addSpace(string,max):
	dif = int(max) - len(string)
	build = ''
	for x in range(dif):
		build = build + ' '
	return build

def showColumn(rows,column,i,columnHeaderLength):
	global errors
	global lastGroup
	global groupByList


	columnList = column

	value = externalScriptTriggerField(column,rows[i][column])
	shorten = True
	if isSwitchActive('Long') == True:
		shorten = False
		if isSwitchActive('ShortenColumn') == True:
			shortenColumn = getSwitchValue('ShortenColumn')
			for sc in shortenColumn.split(','):
				if sc == column:
					shorten = True
	text = str(value)
	if shorten == True:
		text = nameLength(str(value),'')
	else:
		text = str(value)


	groupBy = getSwitchValue('GroupBy')
	global spaces
	try:
		tabFix = spaces[column]
	except Exception as e:
		# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
		tabFix = tabGetMaxSpace(rows,column)
		spaces[column] = tabFix

	if isSwitchActive('GroupBy') == True:
		for gb in groupBy.split(','):
			gb = str(gb)
			if column == gb:
				# print('- -',last,text)
				if not test(groupByList[gb],text) == True:
					if groupBy.split(',')[0] == column:
						print(groupLine(columnList,columnHeaderLength))
						for g in groupBy.split(','):
							groupByList[g] = ''
					else:
						print('')
					groupByList[gb] = text
				else:
					pass
					text = ''

	result = text + addSpace(text,tabFix)

	return result
def groupLine(columnList,columnHeaderLength):
	global groupSeparator
	columnNumber = len(columnList.split(','))
	loop = 0
	result = ''
	while loop < columnHeaderLength + (columnNumber * 4):
		result += groupSeparator
		loop += 1
	return result
def test(one,two):
	# print(one,two)
	if (one) == (two):
		return True
	else:
		return False
def showColumnHeader(rows,column):
	global spaces
	global columnTab
	result = ''
	for c in column.split(','):
		try:
			tabFix = spaces[c]
		except Exception as e:
			# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
			tabFix = tabGetMaxSpace(rows,c)
			spaces[c] = tabFix
		result += c.replace('_',' ').upper() + addSpace(c,tabFix) + columnTab
	result += '\n'
	return result


def printColumns(rows,column):
	if not type(rows) == list or len(rows) == 0:
		print('Table Blank')
		sys.exit()
	global errors
	global columnTab
	global groupByList
	global switchDefault

	# if not len(groupByList):
	groupByList = {}
	try:
		for gb in getSwitchValue('GroupBy').split(','):
			groupByList[str(gb)] = ''
	except Exception as e:
		pass


	if not column == False:
		updateSwitchField('Column','value',column)
	column = getSwitchValue('Column')
	if isSwitchActive('Sort') == True:
		rows = sortThis(rows, False)
	elif isSwitchActive('GroupBy') == True:
		rows = sortThis(rows, getSwitchValue('GroupBy'))
	columnHeader = showColumnHeader(rows,column)
	columnHeaderLength = len(columnHeader)
	print(columnHeader)
	i = 0
	for item in rows:
		result = ''    
		for c in column.split(','):
			# result += showColumn(rows,c,i,columnHeaderLength) + columnTab
			try:
				result += showColumn(rows,c,i,columnHeaderLength) + columnTab
			except Exception as e:
				errors.append({'id': 12, 'function': 'dirPrintColumn()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + _v.slash+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
				print('Error:')
				print('\tBad column input.')
				print(c)
				print(12)
				os._exit(0)
		print(result)
		i += 1
		if 'expected_input_example' in getSwitchValue('Column') and 'switch' in getSwitchValue('Column') and  switchDefault == i:
			print('')





#################################################################



#################################################################
def externalScriptTriggerField(field,value):
	global tableProfile
	i = 0
	for s in tableProfile:
		if field == tableProfile[i]['field']:
			value = tableProfile[i]['script_trigger_external'](value)
		i += 1
	return value
def externalScriptTrigger(name,value):
	global switch
	i = 0
	for s in switch:
		if name == switch[i]['name']:
			value = switch[i]['script_trigger_external'](value)
		i += 1
	return value
def updateSwitchField(name,column,value):
	global switch
	if column == 'value':
		if doesFieldExist(name,'script_trigger_external') == True:
			value = externalScriptTrigger(name,value)
			# getSwitchField(name,'script_trigger')(value)
		elif doesFieldExist(name,'script_trigger') == True:
			script = '{}(\'{}\',\'{}\')'.format(getSwitchField(name,'script_trigger'),name,value)
			value = eval(script)
	i = 0
	for row in switch:
		if row['name'] == name:
			switch[i][column] = value
		i += 1
	return ''
def getSwitchField(name,column):
	global switch
	result = ''
	for row in switch:
		if row['name'] == name:
			result = row[column]
	return result
def doesFieldExist(name,column):
	global switch
	try:
		for row in switch:
			if row['name'] == name:
				row[column]
				result = True
	except Exception as e:
		result = False
	return result
def isSwitchActive(name):
	return getSwitchField(name,'active')
def getSwitchValue(name):
	result = getSwitchField(name,'value')
	if result is None:
		result = ''
	return result

def checkIfSwitch(string):
	global switch
	result = False
	for a in switch:
		for b in a['switch'].split(','):
			if b == string:
				result = True
				# print(b,result)
	return result


def getSwitchValue2(name):
	global errors
	global switchInput
	try:
		switchInput[getSwitchField(name,'pos') + 1]
		i = 0
		# print(switchInput[getSwitchField(name,'pos')].split(':')[1])
		# try:
		#     result = switchInput[getSwitchField(name,'pos')].split(':')[1]
		# except Exception as e:
		#     # errors.append({'id': 14, 'function': 'getSwitchValue()', 'cnt': 2, 'location': "result = switchInput[getSwitchField(name,'pos')].split(':')[1]", 'vars': [{'name': 'name', 'value': name}], 'error': e})
		#     result = ''
		result = ''

		for a in switchInput:
			if i > getSwitchField(name,'pos'):
				if checkIfSwitch(switchInput[i]) == True:
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
		# errors.append({'id': 15, 'function': 'getSwitchValue()', 'cnt': 1, 'location': "switchInput[getSwitchField(name,'pos') + 1]", 'vars': [{'name': 'name', 'value': name}], 'error': e})
		result = None
	return result

def processSwitches(inList):
	# print(inList)
	global switchInput
	global switch
	global customHelp

	switchInput = inList
	ii = 0
	for sw in switch:
		switch[ii]['pos'] = None
		switch[ii]['active'] = False
		switch[ii]['value'] = None
		ii += 1
	i = 0
	for a in switchInput:
		a = a.replace(':','')
		ii = 0
		for sw in switch:
			# print(sw['name'])
			for s in sw['switch'].split(','):
				# print(s)
				if s.lower() == a.lower():
					switch[ii]['pos'] = i
					switch[ii]['active'] = True
					switch[ii]['value'] = processSwitchFormatting(switch[ii]['name'])
			ii += 1
		i += 1
	if checkSwitchExist('_Raw') == True:
		# print('test')
		updateSwitchField('_Raw','pos',1)
		updateSwitchField('_Raw','active',True)
		updateSwitchField('_Raw','value',processSwitchFormatting('_Raw'))
		# i = 0
		# for a in switchInput:
		#     print(i,a)
		#     i += 1
	if isSwitchActive('Help') == True:
		# os.system('cls')
		print('')
		try:
			print('Description: \t', appInfo['description'] + '\n')
			configured = True
		except Exception as e:
			configured = False
		try:
			if len(appInfo['prerequisite']) > 0:
				print('Prerequisite:')
				for prereq in appInfo['prerequisite']:
					print('\t' + prereq)
				print('\n')
		except Exception as e:
			pass


		if configured:
			if len(appInfo['examples']) > 0:
				print('Examples:')
				for ex in appInfo['examples']:
					print('\t' + ex)
				print('\n')
			if len(appInfo['columns']) > 0:
				print('Columns and abbreviations:')
				result = ''
				for col in appInfo['columns']:
					result += col['name'] + '(' + col['abbreviation'] + '), '
				result = result[:-2]
				print('\t' + result + '\n')
				# print('\n')
		printColumns(switch,'name,switch,expected_input_example')
		sys.exit()
	if isSwitchActive('Debug') == True or isSwitchActive('Errors') == True:
		printSwitches()
		sys.exit()

	theErrors()

def processSwitchFormatting(name):
	value = getSwitchValue2(name)
	if doesFieldExist(name,'script_trigger_external') == True:
		value = externalScriptTrigger(name,value)
	elif doesFieldExist(name,'script_trigger') == True:
		script = '{}(\'{}\',\'{}\')'.format(getSwitchField(name,'script_trigger'),name,value)
		value = eval(script)
	return value
def printSwitches():
	global switch
	for s in switch:
		if s['active'] == True:
			print('---------------')
			print('Name: ' + s['name'])
			print('Pos: ' + str(s['pos']))
			print('Value: ' + svc(str(getSwitchValue(s['name']))))
			print('\n')

def checkSwitchExist(name):
	global switch
	result = False
	for sw in switch:
		if sw['name'] == name:
			result = True
	return result

def sortThis(rows, name):
	global errors
	if isSwitchActive('Sort') == True:
		if not name == False:
			updateSwitchField('Sort','value',name)
		name = getSwitchValue('Sort')
	

	global columnList_test
	# print(columnList_test)
	# print(name)

	# print(name)
	# print('1: ' + getSwitchValue('Sort'))
	# print('2: ' + getSwitchField('Sort','value'))
	# print('3: ' + name)
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
			# rows[0][sb]
		except Exception as e:
			errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			# print('Error:')
			# print('\tBad sort input.')
			# print(item)
			# print(16)
			# os._exit(0)


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

def countThis(rows):
	i = 0
	for x in rows:
		i += 1
	return i

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

	# print(completed)
def formatSwitchValueHelperA(name,column,typ):
	result = ' '
	column = column.lower()
	column = _str.replaceAll(column,' ','')
	column = _str.replaceAll(column,',,',',')
	for c in column.split(','):
		if c.count(':') > 0:
			if c.split(':')[0].count('a') > 0:
				result += ' asc:'
			else:
				result += ' desc:'

			if typ == 1:
				sb = columnNickname4Sort(c.split(':')[1])
			else:
				sb = columnNicknameRegular(c.split(':')[1])
			result += sb + ' , '
		else:
			if typ == 1:
				sb = columnNickname4Sort(c)
			else:
				sb = columnNicknameRegular(c)
			result += sb + ' , '
	# print(columnList)
	return result
def formatSwitchValueHelperB(result):
	result = _str.replaceAll(result,' ','')
	result = _str.replaceAll(result,',,',',')
	result = _str.cleanEnd(result,',')
	# ####################################################################  delim to array
	return result
def formatSwitchValueHelperC(column,typ):
	i = 0
	columnList = []
	for c in column.split(','):
		if c.count(':') > 0:
			if c.split(':')[0].count('a') > 0:
				direction = 'asc'
			else:
				direction = 'desc'
			if typ == 1:
				sb = columnNickname4Sort(c.split(':')[1])
			else:
				sb = columnNicknameRegular(c.split(':')[1])
		else:
			direction = 'asc'
			if typ == 1:
				sb = columnNickname4Sort(c)
			else:
				sb = columnNicknameRegular(c)
		if typ == 1:
			columnList.append({'direction': direction, 'column': sb})
		else:
			columnList.append({'column': sb})        
		i += 1
	return columnList
def formatSwitchValueColumn(name,column):
	# script_trigger
	result = formatSwitchValueHelperA(name,column,2)
	result = formatSwitchValueHelperB(result)
	# formatSwitchValueHelperC(column,2)

	# column = 'day_of_the_week'
	return result
def formatSwitchValueSort(name,column):
	global columnList_test
	# script_trigger
	global columnNickname
	result = formatSwitchValueHelperA(name,column,1)
	result = result.replace(' friendly_week ','desc:date_modified_raw')
	result = result.replace(' friendly_month ','desc:date_modified_raw')
	result = result.replace(' day_of_the_week ','desc:date_modified_raw')
	result = formatSwitchValueHelperB(result)
	columnList_test = formatSwitchValueHelperC(column,1)
	# column = 'day_of_the_week'
	return result

def columnNickname4Sort(column):
	# Sort
	global columnNickname
	try:
		column = columnNicknameRegular(column)
		column = column.replace('size','bytes')
		if column == 'type':
			column = 'typesort'

	except Exception as e:
		column = 'date_modified_raw'
	
	return column
def columnNicknameRegular(column):
	global columnNickname
	try:
		column = column.lower()
		column = _str.replaceAll(column,' ','')

		if (isSwitchActive('GroupBy') == True and isSwitchActive('LongFileName') == False) or isSwitchActive('ShortFileName') == True:
			if column == 'name':
				column = 'name_'

		if column == 'cd' or column == 'dc' or column == 'datec' or column == 'cdate':
			column = 'date_created'
		if column == 'woy' or column == 'w':
			column = 'week_of_year'
		if column == 'woy2' or column == 'w2':
			column = 'week_of_year_'


	except Exception as e:
		pass
		column = 'date_modified_raw'
	
	return column

#################################################################
#################################################################

def processTimeout():
	global defaultTimeout
	if isSwitchActive('Timeout') == True:
		try:
			defaultTimeout = int(getSwitchValue('Timeout'))
		except Exception as e:
			errors.append({'id': 18, 'function': 'parent', 'cnt': 1, 'location': "defaultTimeout = int(getSwitchValue('Timeout'))", 'vars': [{'name': 'timeout', 'value': getSwitchValue('Timeout')}], 'error': e})
			print('Error:')
			print('\tBad timeout value.')
			os._exit(0)

	# print(defaultTimeout)
	x = Timer(0.0, timeout, ('start',defaultTimeout))
	x.start()

#################################################################
#################################################################
## Timout ##

#####################

columnNickname = []

#####################

errors = []
spaces = {}
switch = []
tableProfile = []
defaultTimeout = 60
maxNameLength = 35
columnTab = '\t'
customHelp = False
appInfo = []
groupSeparator = '_'
# {'table': 'directory', 'fields': [{}]}

# tableProfile.append()

#####################

columnNickname.append({'name': 'name','nickname': 'n'})

#####################

switch.append({'name': 'Help','switch': '?,/?,-?,/h,help,/help,-help,--help', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Column','switch': '-c,-column', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'size, name', 'script_trigger': 'formatSwitchValueColumn'})
switch.append({'name': 'Sort','switch': '-s,-sort', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'Asc:type, Desc:ext', 'script_trigger': 'formatSwitchValueSort'})
switch.append({'name': 'Debug','switch': '-d,-debug', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Errors','switch': '-e,-Error,-Errors', 'pos': None, 'active': False, 'value': None, 'expected_input_example': '8,11 OR hide:8,11'})
switch.append({'name': 'Timeout','switch': '-t,-Timeout', 'pos': None, 'active': False, 'value': None, 'expected_input_example': '5 OR 10 OR 60'})
switch.append({'name': 'GroupBy','switch': '-g,-group,-groupby', 'pos': None, 'active': False, 'value': None,'groupByDefault': False ,'expected_input_example': None, 'script_trigger': 'formatSwitchValueColumn'})
switch.append({'name': 'ShortenColumn','switch': '-sc,-shortencolumn', 'pos': None, 'active': False, 'value': None, 'expected_input_example': 'name, columnHere', 'script_trigger': 'formatSwitchValueColumn'})
switch.append({'name': 'Long','switch': '-l,-long', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Report','switch': '-report', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Plus','switch': '+', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'Minus','switch': '-', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})
switch.append({'name': 'PlusOr','switch': '-or', 'pos': None, 'active': False, 'value': None, 'expected_input_example': None})

switchDefault = len(switch)
#################################################################


def listPrintColumn(rows,column):
	printColumns(rows,column)
	return ''


class switches:

	def __init__(self, name):
		self.name = name
		self.tricks = []    # creates a new empty list for each dog

	def add_trick(self, trick):
		self.tricks.append(trick)

def theErrors():

	if isSwitchActive('Errors') == True:
		printSwitches()
		try:
			# print('*** ' + getSwitchValue('Sort') + ' ***')
			errors = sorted(errors, key=itemgetter('id'))
			print('\n\n-----------------------------------------------\nErrors:\n')
			showHide = getSwitchValue('Errors')
			# showHide = 'hide:8,11'
			if showHide == None:
				showHide = ''
			sh = 'show'
			shList = ''
			try:
				showHide = showHide.lower()
				if len(showHide) > 0:
					if showHide.find(':') == -1:
						sh = 'show'
						shList = showHide
					else:
						sh = showHide.split(':')[0]
						shList = showHide.split(':')[1]
			except Exception as e:
				pass
			if len(shList) > 0:
				print('------------')
				print(sh)
				print(shList)
				print('------------')

			for error in errors:
				if sh == 'show':
					show = False
				else:
					show = True

				if len(shList) == 0:
					show = True


				eId = error['id']
				function = error['function']
				cnt = error['cnt']
				location = error['location']
				e = error['error']
				var = error['vars']
				if len(shList) > 0:
					for f in shList.split(','):
						if int(f) == eId:
							if sh == 'show':
								show = True
							else:
								show = False
				# if not eId == 8 and not eId == 11:
				if show == True:
					print('\tid: {} function: {} error: {}'.format(eId,function,e))
					for v in var:
						name = v['name']
						value = v['value']
						print('\t\t{}: {}'.format(name,value))
		except Exception as e:
			pass

def external(func,funcIn0=None,funcIn1=None,funcIn2=None,funcIn3=None,funcIn4=None,funcIn5=None,funcIn6=None,funcIn7=None,funcIn8=None,funcIn9=None,funcIn10=None):
	if not funcIn10 == None:
		print('0 - 9 inputs excepted')
	elif not funcIn9 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4,funcIn5,funcIn6,funcIn7,funcIn8,funcIn9)
	elif not funcIn8 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4,funcIn5,funcIn6,funcIn7,funcIn8)
	elif not funcIn7 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4,funcIn5,funcIn6,funcIn7)
	elif not funcIn6 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4,funcIn5,funcIn6)
	elif not funcIn5 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4,funcIn5)
	elif not funcIn4 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3,funcIn4)
	elif not funcIn3 == None:
		func(funcIn0,funcIn1,funcIn2,funcIn3)
	elif not funcIn2 == None:
		func(funcIn0,funcIn1,funcIn2)
	elif not funcIn1 == None:
		func(funcIn0,funcIn1)
	elif not funcIn0 == None:
		func(funcIn0)
	else:
		func()


# def inputCheck():
#     global replaceWith

#     replaceWit = "*,*"
#     replaceWith = replaceWit.split(',')
#     if _.isSwitchActive('Replace') == True:
#         replaceWith = _.getSwitchValue('Replace').split(',')


#     if len(_.getSwitchValue('Plus')) == 0:
#         _.updateSwitchField('Plus','value',_.getSwitchValue('_Raw'))
#         _.updateSwitchField('Plus','pos',_.getSwitchField('_Raw','pos'))

#     _.updateSwitchField('Plus','active',True)
#     _.updateSwitchField('_Raw','active',False)


# inputCheck()


def setExternalScriptTrigger(name,script):
	global switch
	i = 0
	for s in switch:
		
		if name == switch[i]['name']:
			switch[i]['script_trigger_external'] = script
		i += 1

def showLine(string):
	# print(string)
	if isSwitchActive('Plus') == True:
		result = positiveResults(string)
	else:
		result = True
	if result == True and  isSwitchActive('Minus') == True:
		result = minusResults(string)
	return result
def positiveResults(string):
	plusInput = getSwitchValue('Plus')
	string = string.lower()
	result = False
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
		elif not string.find(svc(s)) == -1:
			cnt += 1


		if length == cnt:
			result = True
			break
		if isSwitchActive('PlusOr') == True:
			if cnt > 0:
				result = True
	return result

def minusResults(string):
	string = string.lower()
	result = True
	try:
		for s in getSwitchValue('Minus').split(','):
			s = s.lower()
			if not string.find(svc(s)) == -1:
				result = False
				break
	except Exception as e:
		pass
	return result


def saveTable(rows,theFile,tableTemp = True,printThis = True):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
	else:
		file0 = _v.stmp + _v.slash + theFile
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(file0,'w')
	f.write(str(dataDump))
	f.close()
	if printThis:
		print('Saved: ' + file0)

def getTable(theFile,tableTemp = True,printThis = False):
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
		return json_data

def getTable2(theFile):
	if os.path.isfile(theFile) == True:
		with open(theFile,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
		return json_data
def saveTable2(rows,theFile):
	dataDump = json.dumps(rows, indent=4, sort_keys=True)
	f = open(theFile,'w')
	f.write(str(dataDump))
	f.close()

def tempFile(rows,theFile):
	file0 = _v.stmp + _v.slash + theFile
	file = open(file0,'w')
	for r in rows:
		file.write(r)                 
	file.close()

def stamp2Date(ts):
	return datetime.datetime.fromtimestamp(int(ts) / 1e3)
def float2Date(ts):
	return stamp2Date(ts)

def svc(string): 
	#switchValueClean
	string = string.replace(';;',',')
	string = string.replace(';p;','%')
	string = string.replace(';q;','"')
	string = string.replace(';.',':')
	string = string.replace(";'",'"')
	string = string.replace('_;192A;_',',')
	string = string.replace('_;192B;_',':')
	string = string.replace(_v.slash+'n','\n')
	string = string.replace(';n','\n')
	string = string.replace(';t','\t')
	string = string.replace('"\'"',"'")
	string = string.replace('"\'", "\'"',"','")
	string = string.replace(';return','\n')

	string = string.replace('null00','"",')

	return string

def updateLine(string):
	string = str(string)
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(" " * len(string))
	sys.stdout.write("\b" * len(string))
	sys.stdout.write(string)
	sys.stdout.flush()


def saveTableSplitNew(rows,theFile,tableTemp = True,printThis = True):
	# defaults to myTables
	if tableTemp == True:
		file0 = _v.myTables + _v.slash + theFile
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



'''

_.appInfo = {
	'file': 'f.py',
	'description': 'Search in indexes or files',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['prerequisite'].append('type files0.txt | p line -x files1.txt \ -xs')
_.appInfo['prerequisite'].append('type files0.txt | p line -xu files1.txt \ -xi')

_.appInfo['examples'].append('p f -i *.py + name -jn')
_.appInfo['examples'].append('p f -papa + \GLENNALLEN\ \AppData\ - \Local\ . | p line --c -p \ 5 > ~dup.txt')
_.appInfo['examples'].append('p f -bm + tmp -n | p dir -b')
_.appInfo['examples'].append('p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
_.appInfo['columns'].append({'name': 'path', 'abbreviation': 'p'})
_.appInfo['columns'].append({'name': 'size', 'abbreviation': 's'})

'''





