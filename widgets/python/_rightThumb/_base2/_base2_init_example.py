# import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

# import sys
# import simplejson as json
# import shutil
# import sqlite3
##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __name__
__.appReg = appDBA
__.registeredApps.append(appDBA)
def focus():
	global appDBA
	__.appReg = appDBA
	return appDBA
##################################################

import _rightThumb._base as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

_.switches.register('Input', '-i,-f,-file','file.txt')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'var': '',
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})


# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         hasPre = False
#         if '.' in c or ':' in c:
#             hasPre = True
#             c = c.replace(':','.')
#             preDataR = c.split('.')
#             preData = preDataR[0]
#             c = preDataR[1]

#         for col in _.appInfo[focus()]['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         if hasPre:
#             c = preData + '.' + c
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
# _.switches.trigger('Sort',formatColumns)
# _.switches.trigger('GroupBy',formatColumns)




if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()



def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# __.pipeData = list(data)
	# _.appData[focus()]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[focus()]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[focus()]['pipe'].append(pd)

def pipeCleaner():
	if _.appData[focus()]['pipe'][0][0].isalnum() == False:
		_.appData[focus()]['pipe'][0] = _.appData[focus()]['pipe'][0][1:]
	for i,pipeData in enumerate(_.appData[focus()]['pipe']):
		_.appData[focus()]['pipe'][i] = _.appData[focus()]['pipe'][i].replace('\n','')




# _.appData[focus()]['pipe'] = ''
# if not sys.stdin.isatty():
#     _.appData[focus()]['pipe'] = sys.stdin.readlines()
#     pipeCleaner()















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
#         print('This is a switch')




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

# if _.switches.isActive('Move'):
	# shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))


########################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.uuidLogData = {  'app': _.appInfo[focus()]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
########################################



#     json = _.getTable('base64Key.json')
#    books = _.getText(_v.myTables + '\\bible_books.csv')

# _mime.isText(file)
# _mime.isBinary(file)


# _.saveTable(jsonFile,'file.json')
# _.saveText(convertedFile,_.ci(_.switches.value('Output')))
# _.saveText(convertedFile,'file.txt')
# _.showLine(item)
########################################################################################
def action():
	pass



########################################################################################
if __name__ == '__main__':
	action()





