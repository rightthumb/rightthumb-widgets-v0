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
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Word', '-w,-word','house')
_.switches.register('File', '-f,-file','%tmpf2%')

_.appInfo=    {
	'file': 'wordType.py',
	'description': 'Identifies type of word',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p wordType -word house')
_.appInfo['examples'].append('')
_.appInfo['examples'].append('p wordType -file file.txt')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


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
def action():
	verb = _.getTable('dic_verb.json')
	noun = _.getTable('dic_noun.json')
	adv = _.getTable('dic_adv.json')
	adj = _.getTable('dic_adj.json')
	if _.switches.isActive('File'):
		file = _.getText(_.switches.value('File'))
		words = {'noun': [], 'verb': [], 'adv': [], 'adj': [], 'none': []}
		for fL in file:
			fL = fL.replace('\n','').replace(' ','')
			found = False
			if fL in noun:
				found = True
				print('noun:',fL)
				words['noun'].append(fL)
			if fL in verb:
				found = True
				print('verb:',fL)
				words['verb'].append(fL)
			if fL in adv:
				found = True
				print('adv:',fL)
				words['adv'].append(fL)
			if fL in adj:
				found = True
				print('adj:',fL)
				words['adj'].append(fL)
			if not found:
				print('none:',fL)
				words['none'].append(fL)
		_.saveTable(words,'bible_word_type.json')
	if _.switches.isActive('Word'):
		fL = _.switches.value('Word')
		found = False
		if fL in noun:
			found = True
			print('noun:',fL)
		if fL in verb:
			found = True
			print('verb:',fL)
		if fL in adv:
			found = True
			print('adv:',fL)
		if fL in adj:
			found = True
			print('adj:',fL)
		if not found:
			print('none:',fL)



########################################################################################
if __name__ == '__main__':
	action()





