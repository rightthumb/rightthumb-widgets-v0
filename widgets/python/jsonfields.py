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
import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


_.switches.register('Input', ',-i','file.json')
_.switches.register('Output', ',-o','folder\file.json')
_.switches.register('Move', '-move','folder_2_move_completed_input_files')
# {'name': 'Action','switch': '-action', 'pos': None, 'active': False,'expected_input_example': 'len'}
_.switches.register('CheckFields', '-fields','field0 field1')
_.switches.register('NewField', '-newfield','fieldName')
_.switches.register('Default', '-default','Dallas')


import shutil


_.appInfo=    {
	'file': 'jsonfields.py',
	'description': 'add a field and set data for an entire json file',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p jsonfields -i file.json -o appended\\file.json -move done -fields "Business City" "Other City" -newfield City')
_.appInfo['examples'].append('p jsonfields -i file.json -o _file.json -fields "Business City" "Other City" -newfield City -default Dallas')
_.appInfo['examples'].append('')
_.switches.process()



########################################################################################
def action():
	if _.switches.isActive('Input') == False or _.switches.isActive('Output') == False or _.switches.isActive('Fields') == False:
		print('Error: Missing input')
		sys.exit()

	jsonFile = _.getTable2(_.ci(_.switches.value('Input')))
	fields = _.switches.value('CheckFields')
	# if _.switches.isActive('Action') == 'len':
	i = 0
	for item in jsonFile:
		cnt = 0
		jsonFile[i][_.ci(_.switches.value('NewField'))] = ''
		newfieldData = ''
		if _.switches.isActive('Default') == True:
			newfieldData = _.switches.value('Default')

		for thisField in fields.split(','):
			if len(jsonFile[i][thisField]) > cnt:
				# print(jsonFile[i][thisField])
				cnt = len(jsonFile[i][thisField])
				newfieldData = jsonFile[i][thisField]
		jsonFile[i][_.ci(_.switches.value('NewField'))] = newfieldData
		i += 1

	_.saveTable2(jsonFile,_.switches.value('Output'))

	if _.switches.isActive('Move') == True:
		shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
########################################################################################
if __name__ == '__main__':
	action()