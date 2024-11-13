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
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import shutil


_.switches.register('Input', '-i','appIn.py')
_.switches.register('Output', '-o','folder\\appOut.py')
_.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'convertBase.py',
	'description': 'Converts old apps to new base',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p convertBase -file app.py')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Column',formatColumns)
_.switches.process()


# _.tables.trigger(field,script,includes = False)

if _.switches.isActive('FileX'):
	file = _.switches.value('Input')
	variable = _.getTable(file)
	_.saveTable(xRefList,file)

	variable = _.getTable2(file)
	_.saveTable2(xRefList,file)

	line = _str.replaceAll(line,'  ',' ')
	line = _str.cleanFirst(line,' ')
	line = _str.cleanLast(line,' ')
	line = _str.cleanSpecial(line)
	line = _str.totalStrip(line)
	line = _str.removeAll(line)
	line = _str.replaceDuplicate(line,' ')
	_.tables.register('xRef',xRefList)
	_.tables.get('xRef','fileName')
	

	file = _.switches.value('Files')
	_.tables.register('toCheck')
	_.tables.get('toCheck',file)
	_.tables.register('processes')
	_.tables.get('processes','processes')

	_.tables.trigger('xRef','date',_.float2Dated,True)
	_.tables.sort('xRef', 'name')
	
	_.switches.fieldSet('Sort','active',True)
	_.switches.fieldSet('Sort','value','name')

	testTable = []
	testTable.append({'name': 'Scott', 'age': '37'})
	testTable.append({'name': 'Sarah', 'age': '55'})
	testTable.append({'name': 'Sam', 'age': '22'})
	_.tables.register('test_table',testTable)
	_.tables.print('test_table','name,age')

	_.tables.registerView('test_table','sample','name','name')
	_.tables.registerView('test_table','sample2','age,name','desc.name')
	_.tables.registerView('test_table','sample3','name,age','age')
	# _.tables.registerView('tableName','viewName','includeField1,name','desc.sortBy')
	_.tables.view('test_table','sample')
	_.tables.view('test_table','sample2')
	_.tables.view('test_table','sample3')

	_.switches.print()

	if _.switches.exists('Column2'):
		print('This is a valid switch')

	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)1111
	_.switches.fieldSet('Sort','value','name')
	_.switches.fieldGet('Column','pos')



	# if _.showLine(string):
		# print(line)
def registerSwitch(line):
	try:
		pass
		line = line.replace('_.switch.append(','')
		line = line.replace('})','}')
		switch = eval(line)
		if type(switch['expected_input_example']) == str:
			newLine = '_.switches.register(\'' + switch['name'] + '\', \'' + switch['switch'] + '\',\'' + switch['expected_input_example'] + '\')'
		else:
			newLine = '_.switches.register(\'' + switch['name'] + '\', \'' + switch['switch'] + '\')'
		line = newLine
	except Exception as e:
		pass
	return line

def printColumns(line):
	def getSpaces(theLine):
		# i = 0
		# found = False
		# result = ''
		# for tl in theLine:
		#     if found == False and (tl == ' ' or tl == '\t'):
		#         result += tl
		result = theLine.split('_.printColumns(')[0]
		return result

	try:
		dic0 = line.split('printColumns(')
		dic1 = dic0[1].split(',')
		dic = dic1[0]
		fields0 = str(dic0[1].split(')')[0])
		fields = fields0.split("'")[1]
		code = '_.printColumns(' + str(dic0[1].split(')')[0]) + ')'
		pre_spaces = getSpaces(line)
		replacementCode = '_.tables.print(\'Auto\',\'' + fields + '\')'
		# + '\n' + line + '\n' + code + '\n' + fields0 + '\n'
		newLine = pre_spaces + '_.tables.register(\'Auto\',' + dic + ')\n' + line.replace(code,replacementCode)
		line = newLine
	except Exception as e:
		pass

	return line
# _.switches.register('Input', '-file','app.py')
########################################################################################
def action():
	if _.switches.isActive('Input'):
		file = _.getText(_.switches.value('Input'))
		# functions = []
		# i = 0
		# activeFunction = False
		# for line in file:
		#     line = line.replace('\n','')
		#     if activeFunction == True and not line.startswith(' ') and not line.startswith('\t'):
		#         activeFunction = False
		#         end = i - 1
		#         if not functions[len(functions) - 1]['start'] == end:
		#             functions[len(functions) - 1]['end'] = end
		#             functions[len(functions) - 1]['length'] = end - functions[len(functions) - 1]['start']
		#     if line.startswith('def ') and '(' in line and ':' in line:
		#         activeFunction = True
		#         name0 = line.replace('def ','')
		#         name1 = name0.split('(')
		#         name = name1[0]
		#         functions.append({'line': line, 'name': name, 'start': i, 'end': 0, 'length': 0, 'hasGlobalX': False})
		#     i += 1

		# for fun in functions:
		#     print(fun['start'],'\t',fun['end'],'\t',fun['length'],'\t',fun['name'])
		# sys.exit()
		convertedFile = []
		for line in file:
			line = line.replace('\n','')
			if _.showLine(line):
				if '_.printColumns(' in line:
					line = printColumns(line)
				if '_.switch.append(' in line:
					line = registerSwitch(line)
				line = _str.replaceAll(line,'_.isSwitchActive(','_.switches.isActive(')
				line = _str.replaceAll(line,'_.getSwitchValue(','_.switches.value(')
				line = _str.replaceAll(line,'_.printSwitches()','_.switches.print()')
				line = line.replace('_rightThumb._base ','_rightThumb._base2 ')
				line = _str.replaceAll(line,'_.processSwitches(sys.argv)','_.switches.process()')
				line = _str.replaceAll(line,'_.setExternalScriptTrigger(','_.switches.trigger(')
				line = _str.replaceAll(line,'_.sortThis(','_.sort(')
				line = _str.replaceAll(line,'_.updateSwitchField(','_.switches.fieldSet(')
				line = _str.replaceAll(line,'_.svc(','_.ci(')
				line = _str.replaceAll(line,'_.textFile(','_.getText(')
				# line = _str.replaceAll(line,'','')
				if _.switches.isActive('Output') == True:
					convertedFile.append(line)
				else:
					print(line)
					
	if _.switches.isActive('Output') == True:
		_.saveText(convertedFile,_.ci(_.switches.value('Output')))

	if _.switches.isActive('Move') == True:
			shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))

########################################################################################
if __name__ == '__main__':
	action()





