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
# import simplejson as json
# import shutil
# import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# from datetime import datetime as dt, timedelta
# import datetime
# from datetime import datetime

import time
# from threading import Timer

# from datetime import date
# import calendar

from datetime import timedelta, datetime
import datetime as dt

if __name__ == '__main__':
	_.switches.register('Input', '-i','file.json')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=    {
		'file': 'isDim.py',
		'description': 'Multidimensional test',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p isDim -i file.json')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
if __name__ == '__main__':
	_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


# if _.switches.isActive('_File_'):
#     _.tables.register('toCheck') # table, rows = []
#     _.switches.fieldSet('_File_','active',True)
#     _.switches.fieldSet('_File_','value','toCheck.json')
#     _.tables.get('toCheck',_.switches.value('_File_'))
#     _.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
#     _.tables.sort('toCheck', 'name')

#     _.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
#     _.tables.view('test_table','sample') # table, view

#     _.switches.fieldGet('Column','pos')
#     if _.switches.exists('Column2'):
#         print('This is a valid switch')




#     if _.switches.isActive('Output') == True:
#         _.saveTable2(jsonFile,_.switches.value('Output'))
#         # _.saveText(convertedFile,_.ci(_.switches.value('Output')))

#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')

#    books = _.getText(_v.myTables + '\\bible_books.csv')

########################################################################################

########################################################################################
def processDic(rows,thisDic):
	fields = []
	for tK in thisDic.keys():
		if thisDic[tK] == 'dic':
			try:
				if type(rows[tK]) == dict:
					dicRow = []
					dicRow.append(rows[tK])
				fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(dicRow)})
			except Exception as e:
				try:
					fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(rows[0][tK])})
				except Exception as e:
					fields.append({'type': thisDic[tK], 'field': tK })
		elif thisDic[tK] == 'multidimensional' or thisDic[tK] == 'list':
			try:
				try:
					fields.append({'type': thisDic[tK]+'1', 'field': tK, 'zChildren': processRows(rows[0][tK])})
				except Exception as e:
					# print('dic')
					fields.append({'type': thisDic[tK]+'2', 'field': tK, 'zChildren': processRows(rows[tK])})
					# print('dic')
			except Exception as e:
				# try:
				#     print(rows[0][tK])
				# except Exception as e:
				#     pass
				# print(rows[0][tK])
				# print(tK)


				
				# if 'date_test' in tK:
				#     print("'"+tK+"'")
				#     print('it was found')
				#     print(rows)
				#     # fields.append({'type': thisDic[tK]+'3', 'field': tK, 'zChildren': processRows2(rows[0][tK])})
				#     print('done')
				#     sys.exit()
				# else:
				#     fields.append({'type': thisDic[tK]+'3', 'field': tK})
				fields.append({'type': thisDic[tK]+'3', 'field': tK})
		else:
			fields.append({'type': thisDic[tK], 'field': tK})
	# print(fields)
	return fields












def processRows2(rows):
	print(type(rows))
	sys.exit()
	jsonKeys = {}
	# print('yes')
	# if type(rows) == list:
		# rows = rows[0]
	# print(type(rows))
	if type(rows) == dict:
		# print(rows)
		# print('dic')
		# print(rows)
		# print('dic')
		for i,kS in enumerate(rows.keys()):
			if i == 0:
				pass
				# print(kS,type(rows[kS]))
			try:
				try:
					float(rows[kS])
				except Exception as e:
					int(rows[kS])
				if i == 0:
					jsonKeys[kS] = 'int'
			except Exception as e:
				if len(kS) > 0:
					jsonKeys[kS] = 'str'
			if jsonKeys[kS] == 'int' and isDate(rows[kS]):
				jsonKeys[kS] = 'date'
			if type(rows[kS]) == list:
				try:
					if len(jsonKeys[kS][0].keys()) > 0:
						jsonKeys[kS] = 'multidimensional'
					else:
						jsonKeys[kS] = 'list'
				except Exception as e:
					jsonKeys[kS] = 'list'
	else:
		for  i,jN in enumerate(rows):
			# print(jN)

			try:
				for kS in jN.keys():
					if i == 0:
						pass
						# print(kS,type(jN[kS]))
					try:
						int(jN[kS])
						if i == 0:
							jsonKeys[kS] = 'int'
					except Exception as e:
						if len(kS) > 0:
							jsonKeys[kS] = 'str'
					if jsonKeys[kS] == 'int' and isDate(jN[kS]):
						jsonKeys[kS] = 'date'
					if type(jN[kS]) == list:
						print(jN[kS])
						sys.exit()
						try:
							if len(jsonKeys[kS][0].keys()) > 0:
								jsonKeys[kS] = 'multidimensional'
							else:
								jsonKeys[kS] = 'list'
						except Exception as e:
							jsonKeys[kS] = 'list'
					if type(jN[kS]) == dict:
						jsonKeys[kS] = 'dic'
						# print(jN[kS])
				pass
			except Exception as e:
				# print(rows)
				try:
					try:
						float(jN[i])
					except Exception as e:
						int(jN[i])
					jsonKeys[i] = 'int'
				except Exception as e:
					try:
						jN[i]
						jsonKeys[i] = 'str'
					except Exception as e:
						pass
				try: ###
					if jsonKeys[i] == 'int' and isDate(jN[i]):
						jsonKeys[i] = 'date'
				except Exception as e:
					pass
	return processDic(rows,jsonKeys)










































def processRows(rows):
	jsonKeys = {}
	# print('yes')
	# if type(rows) == list:
		# rows = rows[0]
	# print(type(rows))
	if type(rows) == dict:
		# print(rows)
		# print('dic')
		# print(rows)
		# print('dic')
		for i,kS in enumerate(rows.keys()):
			if i == 0:
				pass
				# print(kS,type(rows[kS]))
			try:
				try:
					float(rows[kS])
				except Exception as e:
					int(rows[kS])
				if i == 0:
					jsonKeys[kS] = 'int'
			except Exception as e:
				if len(kS) > 0:
					jsonKeys[kS] = 'str'
			if jsonKeys[kS] == 'int' and isDate(rows[kS]):
				jsonKeys[kS] = 'date'
			if type(rows[kS]) == list:
				try:
					if len(jsonKeys[kS][0].keys()) > 0:
						jsonKeys[kS] = 'multidimensional'
					else:
						jsonKeys[kS] = 'list'
				except Exception as e:
					jsonKeys[kS] = 'list'
	else:
		for  i,jN in enumerate(rows):
			# print(jN)

			try:
				for kS in jN.keys():
					if i == 0:
						pass
						# print(kS,type(jN[kS]))
					try:
						int(jN[kS])
						if i == 0:
							jsonKeys[kS] = 'int'
					except Exception as e:
						if len(kS) > 0:
							jsonKeys[kS] = 'str'
					if jsonKeys[kS] == 'int' and isDate(jN[kS]):
						jsonKeys[kS] = 'date'
					if type(jN[kS]) == list:
						try:
							if len(jsonKeys[kS][0].keys()) > 0:
								jsonKeys[kS] = 'multidimensional'
							else:
								jsonKeys[kS] = 'list'
						except Exception as e:
							jsonKeys[kS] = 'list'
					if type(jN[kS]) == dict:
						jsonKeys[kS] = 'dic'
						# print(jN[kS])
				pass
			except Exception as e:
				# print(rows)
				try:
					try:
						float(jN[i])
					except Exception as e:
						int(jN[i])
					jsonKeys[i] = 'int'
				except Exception as e:
					try:
						jN[i]
						jsonKeys[i] = 'str'
					except Exception as e:
						pass
				try: ###
					if jsonKeys[i] == 'int' and isDate(jN[i]):
						jsonKeys[i] = 'date'
				except Exception as e:
					pass
	return processDic(rows,jsonKeys)
def isDate(n):
	try:
		try:
			n = int(n)
		except Exception as e:
			n = float(n)
		test = cal_days_diff(n)
		if test < 7000:
			result = True
		else:
			result = False
	except Exception as e:
		result = False
	return result


def epoch2date(ep):
	# theDt = str(dt.datetime.fromtimestamp(float(ep)).strftime('%Y-%m-%d'))
	# theDate = theDt.split('-')
	# print(type(ep))
	if type(ep) == str:
		try:
			result = str(dt.datetime.fromtimestamp(int(ep)).strftime('%Y-%m-%d')).split('-')
		except Exception as e:
			result = str(dt.datetime.fromtimestamp(float(ep)).strftime('%Y-%m-%d')).split('-')
	else:
		result = str(dt.datetime.fromtimestamp(ep).strftime('%Y-%m-%d')).split('-')
	return result
	# return str(dt.datetime.fromtimestamp(float(ep)).strftime('%Y-%m-%d-%H-%M-%S')).split('-')



def cal_days_diff(a):
	one0 = epoch2date(a)
	# two0 = epoch2date(b)
	# print(one0)
	one1 = datetime(int(one0[0]),int(one0[1]),int(one0[2]),0,0)
	# two1 = datetime(two0[0],two0[1],two0[2],0,0)
	two1 = datetime(2018,10,10,0,0)
	A = one1.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
	B = two1.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
	return abs((A - B).days)
	# return (one1 - two1).days

# if __name__ == '__main__':

#     x = datetime(2013, 06, 18, 16, 00)
#     y = datetime(2013, 06, 19, 2, 00)

#     print (y - x).days          # 0
#     print cal_days_diff(y, x)   # 1 

#     z = datetime(2013, 06, 20, 2, 00)

#     print (z - x).days          # 1
#     print cal_days_diff(z, x)   # 2 

def timestamp():
	return int(round(time.time() * 1000))
def action():
	global json
	json = _.getTable2(_.switches.value('Input'))


	if type(json) == dict:
		newJSON = []
		newJSON.append(json)
		json = newJSON
		newJSON = []
	if type(json) == list:
		fields = processRows(json)
	else:
		print('error')
		sys.exit()
	# print('')
	# print('****************************')
	# print('')
	# print(fields)
	if __name__ == '__main__':
		_.saveTable2(fields,'_tmp_isdim.json')
		os.system('type _tmp_isdim.json')
	return fields

def test():
	# result = dateDelta(_.switches.value('Input'),timestamp())
	# int(_.switches.value('Input'))
	# result = datetime.fromtimestamp(int(_.switches.value('Input')))
	# result = datetime.datetime.utcfromtimestamp(posix_time).strftime('%Y-%m-%dT%H:%M:%SZ')

	
	# result = epoch2date(_.switches.value('Input'))
	# result = cal_days_diff(_.switches.value('Input'),timestamp())
	# result = datetime.datetime.today().strftime('%Y-%m-%d')

	# result = datetime.datetime.utcfromtimestamp(float(_.switches.value('Input')))

	# result = cal_days_diff(_.switches.value('Input'))
	result = isDate(_.switches.value('Input'))

	print(result)
########################################################################################
if __name__ == '__main__':
	action()
	# test()





