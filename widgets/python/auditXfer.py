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
from datetime import datetime
from os.path import getmtime
import time
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('File1', '-f1','_chat_out')
_.switches.register('File2', '-f2','_chat_in')
_.switches.register('Note', '-note','985 DB')


_.appInfo=    {
	'file': 'auditXfer.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p auditXfer -f1 _chat_out -f2 _chat_in -note 985 DB')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


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


########################################################################################
def action():
	file1 = _.switches.value('File1')
	file2 = _.switches.value('File2')
	fileDate1 = ''
	fileDate2 = ''
	newDate1 = ''
	newDate2 = ''
	FMT = '%H:%M:%S'
	while not fileDate1 == newDate1:
		try:
			newDate1 = os.path.getmtime(file1)
			if not newDate1 == fileDate1:
				fileDate1 = newDate1

		except Exception as e:
			print('File 1 Error')
	stamp1 = time.strftime(FMT, time.gmtime(os.path.getmtime(file1)))
	while not fileDate2 == newDate2:
		try:
			newDate2 = os.path.getmtime(file2)
			if not newDate2 == fileDate2:
				fileDate2 = newDate2

		except Exception as e:
			print('File 2 Error')
	stamp2 = time.strftime(FMT, time.gmtime(os.path.getmtime(file2)))
	
	tdelta = datetime.strptime(stamp2, FMT) - datetime.strptime(stamp1, FMT)
	print(tdelta,_.switches.value('Note'))
########################################################################################
if __name__ == '__main__':
	action()