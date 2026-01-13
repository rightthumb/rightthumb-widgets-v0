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
# import sys
# import simplejson as json
# import shutil
import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

if __name__ == '__main__':
	_.switches.register('Input', '-i','data.db')
	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=    {
		'file': 'databaseInfo.py',
		'description': 'Provides database information',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p databaseInfo -i har.db')

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
def hasChildren(rows):
	try:
		rows['zChildren']
		result = True
	except Exception as e:
		result = False
	return result
depth = 0
def tables(fields,parent):
	global depth
	depth += 1
	result = []
	for fDs in fields:
		if not hasChildren(fDs):
			pass
			result.append({ 'field': fDs['field'], 'type': fDs['type'], 'table': parent })
			# thisTable += number2Words(fDs['field']) + ' ' + str(fDs['type']) + ', '
			# print(spacerX() + str(fDs['field']),parent)
		else:
			newParent = parent + '_x_' + str(fDs['field'])
			# print(fDs['field'])
			# print(fields)
			# print(fDs['zChildren'])
			children = tables(fDs['zChildren'],newParent)
			result.append({'field': fDs['field'], 'type': fDs['type'], 'zChildren': children, 'parent': parent, 'table': newParent })
	return result
	depth -= 1
def action():
	con = sqlite3.connect(_.switches.value('Input'))
	cursor = con.cursor()
	con.row_factory = sqlite3.Row
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	info = cursor.fetchall()
	table_fields = []
	for iNF in info:
		print()
		print()
		print(iNF[0])
		t = iNF[0]
		f = []
		try:
			cursor = con.execute('select * from ' +  iNF[0])
			# instead of cursor.description:
			row = cursor.fetchone()
			names = row.keys()
			for n in names:

				print('\t',n,'\t',type(row[n]))
				f.append(n)
		except Exception as e:
			pass
		table_fields.append({'name': t, 'fields': f})
newStructure = []
def generateStructure():
	global newStructure
	jf = _.switches.value('Input')
	json = _.getTable2(jf)
	newStructure = tables(json['zstructure'],jf.replace('_Generated_App_Database_Config.json',''))
	# _.saveTable2(newStructure,'_test.json')
	# os.system('type _test.json')
	return newStructure

def findParent(table):
	global newStructure

	if len(newStructure) == 0:
		generateStructure()

	result = parentSearch(newStructure,table)

	print(result)
	return result

def findColumnType(table,field):
	global newStructure

	if len(newStructure) == 0:
		generateStructure()

	result = columnTypeSearch(newStructure,table,field)

	print(result)
	return result

def parentSearch(fields,table):
	global depth
	depth += 1
	result = ''
	for fDs in fields:
		if hasChildren(fDs):
			# print(fDs['table'])
			if fDs['table'] == table:
				result = fDs['parent']
				return result
			result = parentSearch(fDs['zChildren'],table)
	depth -= 1
	return result

def columnTypeSearch(fields,table,field):
	global depth
	depth += 1
	result = ''
	for fDs in fields:
		if hasChildren(fDs):
			# print(fDs['table'])
			result = columnTypeSearch(fDs['zChildren'],table,field)
		else:
			if fDs['table'] == table and fDs['field'] == field:
				result = fDs['type']
				return result

	depth -= 1
	return result
def test():

	meta = []
	db = _.switches.value('Input')
	con = sqlite3.connect(db)
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
				f.append({'field': fd[0], 'type': fd[1] })
			meta.append({'table': table, 'fields': f})
		elif 'INSERT INTO' in line:
			pass
			# break
	for m in meta:
		print(m['table'])
		for f in m['fields']:
			print('\t',f)
def appProcess():
	app = _.switches.value('Input')
	database = _.Database(app)
	meta = database.metaPrint()
	check = 'sample_x_family'
	parent = database.findParent(check)
	print('check:',check,parent)
	children = database.findChildren(parent)
	print()
	print()
	print('children')
	for c in children:
		print('\t',c)


	# meta = database.metaGen()


########################################################################################
if __name__ == '__main__':
	appProcess()
	# action()
	# findParent('har_x_log_x_entries')
	# findColumnType('har_x_log_x_entries','connection')