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
import sys
# import simplejson as json
# import shutil
# import sqlite3
import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Input', '-i,-f,-file','payroll.sql')
_.switches.register('App', '-app','signature')
_.switches.register('Prefix', '-pre,-prefix','_reph_signature_')

_.appInfo[__name__] = {
	'file': 'auditSQL.py',
	'description': 'Generate JSON report of SQL CREATE TABLE fields',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}


_.appInfo[__name__]['examples'].append('p auditSQL -prefix _reph_signature_ -app signature -file payroll.sql')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('')

# _.appInfo[__name__]['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo[__name__]['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)

_.argvProcess = False

if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

_.switches.process()

appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f

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
#         print('This is a  switch')




#     if _.switches.isActive('Output') == True:


#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)



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




#     json = _.getTable('base64Key.json')
#    books = _.getText(_v.myTables + '\\bible_books.csv')

# _.saveTable(jsonFile,'file.json')
# _.saveText(convertedFile,_.ci(_.switches.value('Output')))
# _.saveText(convertedFile,'file.txt')
# _.showLine(item)
########################################################################################
def hasChildren(string):
	result = False
	if string.startswith( '@' ):
		result = True
	return result

def prep(string):
	global commentOpen
	global commentClose
	string = string.replace('\n','')
	string = string.replace(commentOpen,'\n' + commentOpen)
	string = string.replace(commentClose,commentClose + '\n')
	tmp = ''

	for x in string.split('\n'):
		# print(x)
		if not commentOpen in x:
			tmp += x
		else:
			pass
			# print(x)
	string = ''
	string = tmp
	# string = string.replace('(','(\n')
	# string = string.replace(')','\n)\n')
	# string = string.replace("'",'"')
	string = string.replace(';',';\n')
	# string = re.sub(r'<[^>]+>', string, '')
	return string
def clean(string):
	# string = _str.replaceAll(string,'\t',' ')
	string = string.replace('\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string

def fieldProfile(field,t,length,default):
	result = ''
	# if t == 'int' and length == 1:
	if length == 1:
		result = 'toggle,' + field
	elif field == 'guid' or field == 'id':
		result = 'thisID'
	elif not field == 'id' and (field.endswith('_id') or field.endswith('_mid')):
		result = 'altID'
	elif 'date' in field and 'create' in field and t == 'int':
		result = 'epochCreate'
	return result

def action():
	global issues
	global commentOpen
	global commentClose

	# if _.switches.isActive('HTML'):
		# sys.exit()
	if not _.switches.isActive('Input'):
		print(_.switches.value('Input'))
		print('exit')
		sys.exit()
	sqlFile = _.ci(_.switches.value('Input'))
	# print(sqlFile)
	# sys.exit()
	sqlFileX = _.getText(sqlFile)

	sqlFile = ''
	for line in sqlFileX:
		line = line.replace('\n','')
		line = line.replace('/*',commentOpen)
		line = line.replace('*/',commentClose)
		sqlFile += line.split('--')[0]
	sqlFile = prep(clean(sqlFile))
	# print(sqlFile)
	
	# print(sql)
	
	sql = []
	action = False
	for i,line in enumerate(sqlFile.split('\n')):
		# print(i,line)

		if 'create table' in line.lower():
			action = True
			label = clean(line.split('(')[0])
			table = clean(label.lower().replace('create table',''))
			# pipeData[0][1:]
			fieldsRaw = clean(line.split(label)[1])[1:][:-2]
			# print(fieldsRaw)
			fields = []
			for fr in fieldsRaw.split(','):
				fr = fr.lower()
				fr = clean(fr)
				fx = fr.split(' ')
				if '(' in fx[1]:
					length = int(clean(fx[1].split('(')[1].split(')')[0]))
				else:
					length = 0
				t = fx[1].split('(')[0]
				if 'auto_increment' in fr:
					default = 'auto_increment'
				elif 'default' in fx:
					dx = fr.split('default ')[1].split(' ')[0]
					default = clean(dx.replace('"','').replace("'",''))
				else:
					default = ''
				field = clean(fx[0])
				profile = fieldProfile(field,t,length,default)
				fields.append({'field': field, 'type': t, 'length': length, 'default': default, 'note': profile})
			sql.append({'table': table, 'fields': fields})
	if  _.switches.isActive('Prefix') and _.switches.isActive('App'):
		app = {'prefix': _.switches.value('Prefix'), 'app': _.switches.value('App'), 'sql': sql}
		_.saveTable2(app,'sql.json')
		result = app
	else:
		_.saveTable2(sql,'sql.json')
		result = sql

	return result
	# sys.exit()





commentOpen = 'DD0C39A6D9B0'
commentClose = 'F108383C7791'
########################################################################################
if __name__ == '__main__':
	action()





