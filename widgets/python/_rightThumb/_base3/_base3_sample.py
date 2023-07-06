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

import sys
# import simplejson as json
# import shutil
# import sqlite3

##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __name__
__.appReg = appDBA
__.registeredApps.append(appDBA)

def focus(parentApp=''):
	global appDBA
	__.appReg = appDBA + parentApp
	return __.appReg

import _rightThumb._base3 as _
_.load()

##################################################


import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'research',
						'text manipulation',
				],
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





def registerSwitches():
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
		__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# __.pipeData = list(data)
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if _.appData[__.appReg]['pipe'][0][0].isalnum() == False:
		_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
	for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
		_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	pipeCleaner()















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
#         _.pr('This is a switch')




#     if _.switches.isActive('Output') == True:


#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # _.pr(line)

# _.appInfo[focus()]['categories']

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



# if _.switches.isActive('Move'):
	# shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))



# os.path.isfile(files)
# os.system('cls')

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})

# _.randomizeCase(_.genUUID())
# _.randomizeCase(_.longID(howMany=2))
# x = _.randomizeCase(_.longID(howMany=2))
# _.pr(_.onlyNumbers(x))
# _.pr(_.onlyAlpha(x))
# _.onlyAlphaNumeric(_.randomizeCase(_.genUUID()))

# True False same in a row
# diff = int((_.randomTrueFalseSame/_.randomTrueFalseCount)*100)
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + '\\bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:

########################################################################################
# START

def action():
	pass



########################################################################################
if __name__ == '__main__':
	action()







