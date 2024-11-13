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
			# print(tK,thisDic[tK])
			# print(rows)
			# print()
			# print()
			# print(rows[0][tK])
			# print()
			# print()
			# print()
			print(tK)
			try:
				if type(rows[tK]) == dict:
					dicRow = []
					dicRow.append(rows[tK])

				# print(rows[tK])
				# print(type(rows[tK]))

				fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(dicRow)})
			except Exception as e:
				# print(rows[0][tK])
				# print(type(rows[0][tK]))
				fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(rows[0][tK])})
		if thisDic[tK] == 'multidimensional' or thisDic[tK] == 'list':
			try:
				try:
					fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(rows[0][tK])})
				except Exception as e:
					# print('dic')
					fields.append({'type': thisDic[tK], 'field': tK, 'zChildren': processRows(rows[tK])})
					# print('dic')
			except Exception as e:
				fields.append({'type': thisDic[tK], 'field': tK})
		else:
			fields.append({'type': thisDic[tK], 'field': tK})
	# print(fields)
	return fields

def processRows(rows):
	jsonKeys = {}
	# print('yes')
	# if type(rows) == list:
		# rows = rows[0]
	# print(type(rows))
	if type(rows) == dict:
		# print('dic')
		# print(rows)
		# print('dic')
		for i,kS in enumerate(rows.keys()):
			if i == 0:
				pass
				# print(kS,type(rows[kS]))
			try:
				int(rows[kS])
				if i == 0:
					jsonKeys[kS] = 'int'
			except Exception as e:
				if len(kS) > 0:
					jsonKeys[kS] = 'str'
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
				pass
			except Exception as e:
				# print(rows)
				try:
					int(jN[i])
					jsonKeys[i] = 'int'
				except Exception as e:
					jsonKeys[i] = 'str'
	return processDic(rows,jsonKeys)
def action():
	json = _.getTable2(_.switches.value('Input'))


	if type(json) == dict:
		fields = processRows(json)
	elif type(json) == list:
		fields = processRows(json)
	else:
		print('error')
		sys.exit()
	# print('')
	# print('****************************')
	# print('')
	# print(fields)
	_.saveTable2(fields,'_tmp_isdim.json')
	os.system('type _tmp_isdim.json')
	return fields



########################################################################################
if __name__ == '__main__':
	action()





