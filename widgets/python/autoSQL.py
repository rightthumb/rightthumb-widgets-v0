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

# import os
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Input', '-i','appIn.json')
_.switches.register('Output', '-o','folder\\appOut.db')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'autoSQL.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p autoSQL -i file.txt')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p importsql -sql dump.sql -db dump.db')



_.switches.process()



########################################################################################
def rows2Text(rows):
	result = ''
	for r in  rows:
		result += r + '\n'
	return result
	
def printRows(rows):
	print()
	for r in  rows:
		print(r)
def formatText(string):
	string = str(string)
	return string
def action():
	result = []
	json = _.getTable(_.switches.value('Input'))
	fields = []
	jsonKeys = {}
	for  i,jN in enumerate(json):
		# if i < 10:
			# print(jN)
		for kS in jN.keys():
			if i == 0:
				print(kS,)
			# int(kS)
			try:
				int(jN[kS])
				if i == 0:
					jsonKeys[kS] = 'int'
			except Exception as e:
				if len(kS) > 0:
					jsonKeys[kS] = 'str'
				# jsonKeys[kS] 
				# print(kS,str(type(kS)))
	for tK in jsonKeys.keys():
		fields.append({'type': jsonKeys[tK], 'field': tK})
	tableName = 'auto'
	create = 'CREATE TABLE ' + tableName + ' ('
	for fS in fields:
		print(fS)
		create += fS['field'].replace(' ','_') + ' ' + fS['type'] + ', '
	create = _str.cleanLast(create,', ')
	create += ');'
	result.append('BEGIN TRANSACTION;')
	result.append(create)
	for  i,jN in enumerate(json):
		# if i < 10:
		if True:
			line = 'INSERT INTO "' + tableName + '" VALUES('
			for kS in fields:
				# print(kS)
				# print(kS['field'])
				if kS['type'] == 'int':
					line += "" + formatText(jN[kS['field']]) + ", "
				else:
					line += "'" + formatText(jN[kS['field']]) + "', "
			line = _str.cleanLast(line,', ')
			line += ');'
			result.append(line)
	result.append('COMMIT;')
	printRows(result)
	textFile = rows2Text(result)
	_.saveText(textFile,'dump.sql')


########################################################################################
if __name__ == '__main__':
	action()