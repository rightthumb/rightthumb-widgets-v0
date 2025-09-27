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
from os.path import join, getsize, isfile, isdir, splitext
import re


import sys
# import simplejson as json
# import shutil
# import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import uuid

if __name__ == '__main__':
	_.switches.register('Input', '-i','file.json')


	_.switches.register('Build', '-build')

	_.switches.register('Database', '-db,-database','%i%/C_Drive.db')
	_.switches.register('File', '-file,-sql','%i%/dump.sql')

	_.switches.register('GenerateApp', '-app,-generate,-generateapp')

	_.appInfo=    {
		'file': 'jsonStructureNav.py',
		'description': 'Changes the world',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p jsonStructureNav -i sample.json')
	_.appInfo['examples'].append('')
	_.appInfo['examples'].append('p jsonStructureNav -app -i sample.json')
	_.appInfo['examples'].append('p jsonStructureNav -build -app -i sample.json')
	_.appInfo['examples'].append('')
	_.appInfo['examples'].append('p importsql -sql dump.sql -db dump.db')

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
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')

#    books = _.getText(_v.myTables + _v.slash+'bible_books.csv')

########################################################################################
# class TheChildItems:

#     def __init__(self, name, switch):
#         self.name = name
#         self.active = False
#         self.value = None

#     def trigger(self,script):
#         self.script_trigger = script

#     def changeStatus(self,newStatus):
#         self.active = newStatus
# class TheParentItems:

#     def __init__(self):
#         self.childItemRows = []

#     def register(self, name):
#         self.childItemRows.append(TheChildItems(name))
#     def print(self):
#         childItems = []
#         for ci in self.childItemRows:
#             childItems.append({'name':ci.name})
#         _.tables.register('childClassItems',childItems)
#         # tables.trigger('switches','switch,name',test,True)
#         _.tables.print('childClassItems','name')
#     def printStatus(self):
#         childItems = []
#         for ci in self.childItemRows:
#             if ci.active:
#                 active = 'True'
#             else:
#                 active = 'False'
#             value = ci.value
#             if ci.value == True:
#                 value = 'True'
#             elif ci.value == False:
#                 value = 'False'

#             childItems.append({'name':ci.name ,'active':active,'value': value})
#         _.tables.register('childClassItems',childItems)
#         _.tables.print('childClassItems','name,active,value')
#     def status(self,name,newStatus):
#         for i,ci in enumerate(self.childItemRows):
#             if ci.name == name:
#                 self.childItemRows[i].changeStatus(newStatus)
########################################################################################
def genUUID():
	string = str(uuid.uuid4())
	string = uuid.uuid4().hex
	string = uuid.uuid4()
	string = str(string)
	string = '{' + string.upper() + '}'
	return string
########################################################################################
def hasChildren(rows):
	try:
		rows['zChildren']
		result = True
	except Exception as e:
		result = False
	return result
def spacerX():
	global depth
	cnt = 0
	space = ' '
	while cnt < depth:
		cnt += 1
		space += '    '
	return space
def rows2Text(rows):
	result = ''
	for r in  rows:
		result += r + '\n'
	return result
def isNu(string):
	string = str(string)
	result = True
	for s in string:
		try:
			int(s)
		except Exception as e:
			result = False
	return result
def number2Words(n):
	global numberWords
	if type(n) == int:
		result = numberWords[n].replace(' ','_').replace('-','_').replace('\n','')
	else:
		result = n.replace(' ','_')
	return result

depth = 0
theSQL = []
# def tableClean(theSQL):

#     result = []
#     badTables = []
#     for line in theSQL:
#         bad = False
#         for bt in badTables:
#             if bt in line:
#                 bad = True

#         if not '(id_parent str, id_uuid str)' in line and bad == False:
#             result.append(line)
#         else:
#             if not '_x_' in line:
#                 result.append(line)
#             elif 'CREATE TABLE' in line:
#                 one = line.split('CREATE TABLE ')[1]
#                 two = one.split(' (')
#                 table = two[0]
#                 badTables.append('"' + table + '"')
#     theSQL = result
#     return result

def tableClean(theSQL):

	result = []
	badTables = []
	for line in theSQL:
		if not '(id_parent str, id_uuid str)' in line:
			pass
		else:
			if not '_x_' in line:
				pass
			elif 'CREATE TABLE' in line:
				one = line.split('CREATE TABLE ')[1]
				two = one.split(' (')
				table = two[0]
				badTables.append({'table': '"' + table + '"', 'insert': False, 'isParent': False})

	for line in theSQL:
		bad = False
		if 'INSERT INTO' in line:
			for ib,bt in enumerate(badTables):
				if bt['table'] in line:
					badTables[ib]['insert'] = True
		if 'CREATE TABLE' in line:
			for ib,bt in enumerate(badTables):
				ctTable = bt['table'].replace('"','')
				check = ctTable + '_x_'
				if check in line:
					badTables[ib]['isParent'] = True

	for line in theSQL:
		bad = False
		for ib,bt in enumerate(badTables):
			ctTable = bt['table'].replace('"','')
			if 'CREATE TABLE' in line and ctTable in line and bt['insert'] == False and bt['isParent'] == False:
				bad = True
			if bt['table'] in line and bt['insert'] == False and bt['isParent'] == False:
				bad = True
		if not bad:
			result.append(line)

	for ib,bt in enumerate(badTables):
		if bt['insert'] == False and bt['isParent'] == True:
			print()
			print()
			print('Parent without insert error:')
			print('\t',bt['table'])
			sys.exit()

	theSQL = result
	return result


def genTables(fields,parent):
	global depth
	global theSQL
	depth += 1
	thisTable = 'CREATE TABLE ' + parent + ' (id_parent str, id_uuid str, '
	for fDs in fields:
		if not hasChildren(fDs):
			thisTable += number2Words(fDs['field']) + ' ' + str(fDs['type']).replace('date','int') + ', '
			# print(spacerX() + str(fDs['field']),parent)
		else:
			newParent = parent + '_x_' + str(fDs['field'])
			# if not newParent in tableList:
				# tableList.append(newParent)
			genTables(fDs['zChildren'],newParent)
	thisTable = _str.cleanLast(thisTable,', ')
	thisTable += ');'
	theSQL.append(thisTable)
	depth -= 1
def process(rows,fields,parent,parentID):
	global depth
	global theSQL
	depth += 1
	if type(rows) == dict:
		thisID = genUUID()
		line = 'INSERT INTO "' + parent + '" ('+"'"+'id_parent'+"'"+', '+"'"+'id_uuid'+"'"+', '
		for fDs in fields:
			if not hasChildren(fDs):
				line += "'" + number2Words(fDs['field']) + "', "
		line = _str.cleanLast(line,', ')
		iX = 0
		line += ") VALUES('" + str(parentID) + "','" + str(thisID) + "', "

		for fDs in fields:
			if not hasChildren(fDs):
				if (fDs['type'] == 'int' or fDs['type'] == 'date') and isNu(rows[fDs['field']]):
					line += "" + formatText(rows[fDs['field']],True) + ", "
				else:
					line += "'" + formatText(rows[fDs['field']]) + "', "
				# print(spacerX() + fDs['field'],parent)
			else:
				newParent = parent + '_x_' + fDs['field']
				# print(fDs['field'])
				# print(fields)
				# print(fDs['zChildren'])
				process(rows[fDs['field']],fDs['zChildren'],newParent,thisID)
		line = _str.cleanLast(line,', ')
		line += ');'
		theSQL.append(line)
	else:

		for rW in rows:
			thisID = genUUID()
			line = 'INSERT INTO "' + parent + '" ('+"'"+'id_parent'+"'"+', '+"'"+'id_uuid'+"'"+', '
			iX = 0
			for fDs in fields:
				if not hasChildren(fDs):
					if type(rW) == list:
						try:
							if fDs['type'] == 'int' and isNu(rW[iX]):
								line += "'" + number2Words(fDs['field']) + "', "
							else:
								line += "'" + number2Words(fDs['field']) + "', "
						except Exception as e:
							pass
					else:
						try:                            
							rW[fDs['field']]
							line += "'" + number2Words(fDs['field']) + "', "
						except Exception as e:
							pass
					iX += 1
			line = _str.cleanLast(line,', ')
			iX = 0
			line += ") VALUES('" + str(parentID) + "','" + str(thisID) + "', "
			for fDs in fields:
				if not hasChildren(fDs):
					pass
					
					# print(type(rW))
					if type(rW) == list:
						# print(rW[iX])
						pass

						try:
							
							if (fDs['type'] == 'int' or fDs['type'] == 'date') and isNu(rW[iX]):
								line += "" + formatText(rW[iX],True) + ", "
							else:
								line += "'" + formatText(rW[iX]) + "', "
						except Exception as e:
							pass
							# print(fDs['field'])
							# print(iX)
							# print(rW)
							
					else:
						try:
							
							# print(rW[fDs['field']])
							if (fDs['type'] == 'int' or fDs['type'] == 'date') and isNu(rW[fDs['field']]):
								line += "" + formatText(rW[fDs['field']],True) + ", "
							else:
								line += "'" + formatText(rW[fDs['field']]) + "', "
						except Exception as e:
							# print(fDs['field'])
							# print(rW)
							pass
					iX += 1
					# print(fDs['field'])
					# print(rW)
					# print(rW[fDs['field']])
					# if fDs['type'] == 'int':
					#     line += "" + formatText(rW[fDs['field']]) + ", "
					# else:
					#     line += "'" + formatText(rW[fDs['field']]) + "', "
					# print(spacerX() + str(fDs['field']),parent)
				else:
					newParent = parent + '_x_' + fDs['field']
					process(rW[fDs['field']],fDs['zChildren'],newParent,thisID)
			line = _str.cleanLast(line,', ')
			line += ');'
			theSQL.append(line)
	depth -= 1


def formatText(string,n=False):
	if not n:
		string = str(string)
		string = re.sub('[^0-9a-zA-Z]+', '_', string)
	else:
		one = int(string)
		two = float(string)
		if one == two:
			string = one
		else:
			string = two
		string = str(string)
	string = string.replace('_','.')

	return string
def printRows(rows):
	print()
	for r in  rows:
		# if 'har_x_log_x_entries_x_response_x_cookies' in r:
		print(r)

def action():
	global depth
	global numberWords
	global theSQL

	isDefaultDB = False
	if not _.switches.isActive('Input'):
		print('expected input failure')
		sys.exit()
	else:
		jsonFile = _.switches.value('Input')
		jsonFilePath = jsonFile
		if _v.slash in jsonFile:
			a = jsonFile.split(_v.slash)
			jsonFile = a[len(a)-1]

	if _.switches.isActive('Database'):
		if len(_.switches.value('Database')) > 1:
			databaseFile = _.switches.value('Database')
			if not '.db' in databaseFile:
				databaseFile += '_Generated_App_Database.db'
			dbName = databaseFile.split('.db')[0]
	else:
		databaseFile = jsonFile.split('.')[0] + '_Generated_App_Database.db'
		dbName = jsonFile.split('.')[0]
	if _v.slash in dbName:
		a = dbName.split(_v.slash)
	dbName = a[len(a)-1]
	dbName = re.sub('[^0-9a-zA-Z]+', '_', dbName)
	dbName = _str.cleanBE(dbName,'_')
	dbName = _str.replaceDuplicate(dbName,'_')
	if _.switches.isActive('File'):
		if len(_.switches.value('File')) > 1:
			sqlFile = _.switches.value('File')
	else:
		sqlFile = 'dump_' + dbName + '.sql'




	# print(dbName)
	# sys.exit()
	import jsonStructure
	structure = jsonStructure.action()
	numberWords = _.getText(_v.myTables + _v.slash+'numberWords.txt')
	# print(structure)
	# if __name__ == '__main__':

	if _.switches.isActive('GenerateApp'):
		# _.switches.fieldSet('Build','active',True)
		appJSON = dbName + '_Generated_App_Database_Config' + '.json'
		appJSON_fullPath = _v.myDatabases + _v.slash + appJSON
		stop = False
		if os.path.isfile(appJSON_fullPath):
			print('')
			question = input('Overwrite config file: ' + appJSON + '? (y): ')
			if 'y' in  question.lower() or len(question) == 0:
				# do = 'del /q ' + ' "' + _v.myDatabases + _v.slash + dbName.replace('_data_json','') + '*"'
				do = 'del /q ' + ' "' + _v.myDatabases + _v.slash + appJSON + '"'
				os.system('"' + do + '"')
				do = 'del /q ' + ' "' + _v.myDatabases + _v.slash + databaseFile + '"'
				os.system('"' + do + '"')
				# do = 'pause'
				# os.system(do)
				# os.system('"' + do + '"')
				# sys.exit()
			else:
				stop = True
		if stop:
			print('Operation aborted')
			sys.exit()
		appData = {
			'name': dbName,
			'database_file': databaseFile,
			'zstructure': structure,

		}
		_.saveTable2(appData,appJSON_fullPath)
	# os.system('type _tmp_isdim.json')
	depth = 0
	# print(depth)
	theSQL.append('BEGIN TRANSACTION;')
	# print(structure)
	genTables(structure,dbName)
	for i,jS in enumerate(jsonStructure.json):
		process(jS,structure,dbName,0)
	
	theSQL = tableClean(theSQL)
	theSQL.append('COMMIT;')
	# printRows(theSQL)
	# sys.exit()
	textFile = rows2Text(theSQL)



	if _.switches.isActive('Build'):
		_.switches.fieldSet('Database','active',True)
		_.switches.fieldSet('Database','value',databaseFile)
		_.switches.fieldSet('File','active',True)
		_.switches.fieldSet('File','value',sqlFile)

		import importsql
		importsql.theSQL = theSQL
		action = importsql.action()
	else:
		_.saveText(textFile,sqlFile)




########################################################################################
if __name__ == '__main__':
	action()