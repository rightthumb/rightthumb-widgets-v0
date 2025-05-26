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

import csv
import shutil


_.switches.register('Input', ',-i','file.json')
_.switches.register('Output', ',-o','folder\file.json')
_.switches.register('Move', '-move','folder_2_move_completed_input_files')
_.switches.register('Fields', '-fields','City State')

_.switches.register('GetColumns', '-gc,-getcolumns')

_.appInfo=    {
	'file': 'csvColumnOrder.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p csvColumnOrder -i file.csv -o newFile.csv -move done -fields First Last Email')
_.appInfo['examples'].append('p csvColumnOrder -getcolumns -i file.csv ')
_.appInfo['examples'].append('p file --c + .csv | p line --c -make "p csvColumnOrder -i {} -o ordered\\{} -move done -fields ;\'First Name;\' ;\'Last Name;\'  ;\'E-mail Address;\' ;\'City;\' ;\'State;\' "')
_.switches.process()

# if _.switches.isActive('File') == False:
#     file = _.switches.value('File')
#     variable = _.getTable(file)
#     _.saveTable(xRefList,file)
#     line = _str.replaceAll(line,'  ',' ')
#     line = _str.cleanFirst(line,' ')
#     line = _str.cleanLast(line,' ')
#     line = _str.cleanSpecial(line)
#     line = _str.totalStrip(line)
#     line = _str.removeAll(line)
#     line = _str.replaceDuplicate(line,' ')
#     if _isSwitchActive('Sort'):
#         xRefList = _.sort(xRefList, _.switches.value('Sort'))
#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')


########################################################################################
def refineColumns():
	currentColumns = []
	file = _.switches.value('Input')
	with open(file, mode='r', encoding='utf-8') as f:
		reader = csv.DictReader(f, delimiter=',')
		i = 0
		for row in reader:
			if i == 0:
				for col in reader.fieldnames:
					currentColumns.append(col)
			i += 1
	newColumns = []
	fields = _.switches.value('Fields').split(',')
	for flds in fields:
		found = False
		for cc in currentColumns:
			if cc == flds:
				found = True
		if found == True:
			newColumns.append(flds)
	# print(newColumns)
	# print(currentColumns)
	return newColumns
def action():
	if _.switches.isActive('Input') == True and _.switches.isActive('Output') == True and _.switches.isActive('Fields') == True:
		with open(_.switches.value('Input'), 'r') as infile, open(_.switches.value('Output'), 'a') as outfile:
			# output dict needs a list for new column ordering
			# fieldnames = _.switches.value('Fields').split(',')
			fieldnames = refineColumns()
			writer = csv.DictWriter(outfile, fieldnames=fieldnames)
			# reorder the header first
			writer.writeheader()
			for row in csv.DictReader(infile):
				# writes the reordered rows to the new file
				writer.writerow(row)
	elif _.switches.isActive('GetColumns') == True:
		# refineColumns()

		file = _.switches.value('Input')
		with open(file, mode='r', encoding='utf-8') as f:
			reader = csv.DictReader(f, delimiter=',')
			i = 0
			for row in reader:
				if i == 0:
					for col in reader.fieldnames:
						print('"' + col + '"')
				i += 1




	if _.switches.isActive('Move') == True:
		shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
########################################################################################
if __name__ == '__main__':
	action()





