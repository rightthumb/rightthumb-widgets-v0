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

_.switches.register('Table', '-table','_reph_signature_+staff')
_.switches.register('Fields', '-fields','first last')

# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[__name__] = {
	'file': 'crud.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['examples'].append('p crud -table _reph_signature_+staff -fields first last')

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

if not __name__ == '__main__':
	_.argvProcess = False


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
#         print('This is a valid switch')




#     if _.switches.isActive('Output') == True:


#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
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

# if _.switches.isActive('Move'):
	# shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))


########################################



#     json = _.getTable('base64Key.json')
#    books = _.getText(_v.myTables + _v.slash+'bible_books.csv')

# _.saveTable(jsonFile,'file.json')
# _.saveText(convertedFile,_.ci(_.switches.value('Output')))
# _.saveText(convertedFile,'file.txt')
# _.showLine(item)
########################################################################################
def funcname():
	table = _.switches.value('Table')
	# print(table)
	# sys.exit()
	table = table.split('+')[1]
	# print(table)
	table = table.replace('_',' ')
	table = table.title()
	table = table.replace(' ','_')
	return table
def funcfields():
	fields = _.switches.value('Fields')
	field = fields.split(',')
	f = ''
	for fl in field:
		f += '$' + fl + ', '
	f = _str.cleanBE(f,', ')
	return f
def tfields():
	fields = _.switches.value('Fields')
	field = fields.split(',')
	f = ''
	for fl in field:
		f += fl + ', '
	f = _str.cleanBE(f,', ')
	return f
def vfields():
	fields = _.switches.value('Fields')
	field = fields.split(',')
	f = ''
	for fl in field:
		f += "'"+'$' + fl + "'" + ', '
	f = _str.cleanBE(f,', ')
	return f
def readfields():
	fields = _.switches.value('Fields')
	field = fields.split(',')
	b = "\n        'FIELD' => $row['FIELD'],"
	f = ''
	for fl in field:
		f += b.replace('FIELD',fl)
	return f
def thetable():
	table = _.switches.value('Table')
	table = table.replace('+','')
	return table
def updatefields():
	fields = _.switches.value('Fields')
	field = fields.split(',')
	b = "FIELD='$FIELD', "
	f = ''
	for fl in field:
		f += b.replace('FIELD',fl)
	f = _str.cleanBE(f,', ')
	return f
def action():
	crudBase = _.getText(_v.myTables + _v.slash+'crud.php')
	crud = ''

	for i,c in enumerate(crudBase):
		if i > 0:
			crud += c

	funcname0 = '[funcname]'
	funcname1 = funcname()
	crud = crud.replace(funcname0,funcname1)

	funcfields0 = '[funcfields]'
	funcfields1 = funcfields()
	crud = crud.replace(funcfields0,funcfields1)

	tfields0 = '[tfields]'
	tfields1 = tfields()
	crud = crud.replace(tfields0,tfields1)

	vfields0 = '[vfields]'
	vfields1 = vfields()
	crud = crud.replace(vfields0,vfields1)

	readfields0 = '[readfields]'
	readfields1 = readfields()
	crud = crud.replace(readfields0,readfields1)

	table0 = '[table]'
	table1 = thetable()
	crud = crud.replace(table0,table1)

	updatefields0 = '[updatefields]'
	updatefields1 = updatefields()
	crud = crud.replace(updatefields0,updatefields1)

	print(crud)

########################################################################################
if __name__ == '__main__':
	action()


# n %tmpf3%

#  -table _reph_signature_+staff_type -fields label
# -table _reph_signature_+staff -fields first last email availabilityjson addressjson stafftypeid
# -table _reph_signature_+services -fields label durationjson dvalue stafftypeid
# -table _reph_signature_+appointments -fields customerid time_start time_end
# -table _reph_signature_+appointment_items -fields appointmentid serviceid dvalue duration
# -table _reph_signature_+customers -fields first last email availabilityjson addressjson

# n %tmpf4%


# type %tmpf3% | p line --c -make "p crud {} >> %tmpf4% " | p execute




