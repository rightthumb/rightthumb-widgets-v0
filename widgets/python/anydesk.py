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

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.appInfo=    {
	'file': 'anydesk.py',
	'description': 'AnyDesk IDs',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}
# if __name__ == '__main__':
	# _.switches.register('Search', '-search,-i','cl')
_.switches.register('Add', '-add')
	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')


_.appInfo['examples'].append('p anydesk -search cl')

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



########################################################################################
def isNumber(string):
	try:
		int(string)
		result = True
	except Exception as e:
		result = False
	return result

def formatID(string):
	string = str(string)
	string = string.replace(' ','')
	if not len(string) == 9 or not isNumber(string):
		print('ID Error')
		sys.exit()
	result = string[:3] + ' ' + string[3:6] + ' ' + string[6:9]
	# print(result)
	# sys.exit()
	return result

def formatID2(string):
	string = str(string)
	string = string.replace(' ','')
	if not len(string) == 9 or not isNumber(string):
		print('ID Error')
		sys.exit()
	result = string[:3] + '-' + string[3:6] + '-' + string[6:9]
	# print(result)
	# sys.exit()
	return result

def action():
	json = _.getTable('AnyDesk.json')


	if len(json) == 0:
		database = False
	else:
		database = True


	if not database:
		print('No Database\n')
	
	if not _.switches.isActive('Add'):

		if not database:
			anyDeskID = input('ID: ')
			_.saveTable({'name': name, 'id': anyDeskID},'AnyDesk.json')
		data = []
		if database:
			found = False

			for item in json:
				if _.showLine(item['name']):
					found = True
					data.append(item)

			if found:
				print()
				print()
				_.tables.register('AnyDesk',data)
				# _.tables.fieldProfileSet('AnyDesk','id','trigger',clearSpaces)
				# _.tables.fieldProfileSet('AnyDesk','id','trigger',formatID2)
				_.tables.print('AnyDesk','id,name')
			else:
				print('Not Found')
				

	if _.switches.isActive('Add'):
		name = input('Name: ')
		anyDeskID = input('ID: ')
		if not database:
			_.saveTable([{'name': name, 'id': formatID(anyDeskID)}],'AnyDesk.json')
		else:
			json.append({'name': name, 'id': formatID(anyDeskID)})
			_.saveTable(json,'AnyDesk.json')

	

def clearSpaces(string):
	return string.replace(' ','')

########################################################################################
if __name__ == '__main__':
	action()





