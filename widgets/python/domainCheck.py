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
import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

from socket import getaddrinfo



_.switches.register('Domain', '-domain','appIn.py')
# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p thisApp -file file.txt')

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

if _.switches.isActive('File_'):
	file = _.switches.value('File')
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

	i = 0
	for value in _.switches.value('Plus'):
		p[i] = _.svc(value)
		i += 1



	if _.switches.isActive('Output') == True:
		_.saveTable2(jsonFile,_.switches.value('Output'))
		_.saveText(convertedFile,_.ci(_.switches.value('Output')))

	if _.switches.isActive('Move') == True:
			shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
	# if _.showLine(string):
		# print(line)
# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
class Domain:
	def __init__(self, node, platform='', cpus=0, memory=0, disk=0):
			if node.find('*') < 0:
				try:
					info = getaddrinfo(node, None)[0]
					self.ip = info[4][0]
					ip_addr = info[4][0]
					if info[0] == socket.AF_INET4:
						ip_addr = re.sub(r'^0*', '', ip_addr)
						ip_addr = re.sub(r':0*', ':', ip_addr)
						ip_addr = re.sub(r'::+', '::', ip_addr)
					node = ip_addr
				except:
					node = ''

			if node:
				self.ip_rex = node.replace('.', _v.slash+'.').replace('*', '.*')
			else:
				pass
				self.ip_rex = ''
				# logger.warning('node "%s" is invalid', node)
			self.platform = platform.lower()
			self.cpus = cpus
			self.memory = memory
			self.disk = disk 
########################################################################################
def action():
	if _.switches.isActive('Domain'):
		result = Domain(_.switches.value('Domain'))
		try:
			result = Domain(_.switches.value('Domain'))
			if '198.105.244.114' in str(result.ip):
				result = 'Bad'
			else:
				result = str(result.ip)
		except Exception as e:
			result = 'Error'
		print(_.switches.value('Domain'),result)
		# print(result.__dict__.keys())



########################################################################################
if __name__ == '__main__':
	action()





