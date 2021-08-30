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

import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Input', '-i','appIn.py')
_.switches.register('Output', '-o','folder\\appOut.py')
_.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=	{
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

if _.switches.isActive('_File_'):
	_.tables.register('toCheck') # table, rows = []
	_.switches.fieldSet('_File_','active',True)
	_.switches.fieldSet('_File_','value','toCheck.json')
	_.tables.get('toCheck',_.switches.value('_File_'))
	_.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
	_.tables.sort('toCheck', 'name')

	_.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
	_.tables.view('test_table','sample') # table, view

	_.switches.fieldGet('Column','pos')
	if _.switches.exists('Column2'):
		print('This is a valid switch')




	if _.switches.isActive('Output') == True:
		_.saveTable2(jsonFile,_.switches.value('Output'))
		# _.saveText(convertedFile,_.ci(_.switches.value('Output')))

	if _.switches.isActive('Move') == True:
	        shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
	# if _.showLine(string):
		# print(line)

	_.getTable('base64Key.json')

pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if pipeData[0][0].isalnum() == False:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass



########################################################################################
def action():
	pass



########################################################################################
if __name__ == '__main__':
	action()





