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


_.switches.register('Input', '-i','file.json')
_.switches.register('Output', '-o','folder\file.json')
_.switches.register('Fields', '-fields','field value;field2 value')
_.switches.register('Move', '-move','folder_2_move_completed_input_files')


import shutil


_.appInfo=    {
	'file': 'appendjson.py',
	'description': 'add a field and set data for an entire json file',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p appendjson -i file.json -o appended\\file.json -move done ')
_.appInfo['examples'].append('p appendjson -i Alababama_b.CSV.json -o appended\\Alababama_b.CSV.json -move done -fields State AL')
_.appInfo['examples'].append('p appendjson -i Arizona_Phoe_Scotts_b.CSV.json -o appended\\Arizona_Phoe_Scotts_b.CSV.json -move done -fields State AZ;City Phoenix')
_.appInfo['examples'].append('')
_.switches.process()



########################################################################################
def action():
	if _.switches.isActive('Input') == False or _.switches.isActive('Output') == False or _.switches.isActive('Fields') == False:
		print('Error: Missing input')
		sys.exit()

	jsonFile = _.getTable2(_.ci(_.switches.value('Input')))
	fields = _.switches.value('Fields')
	i = 0
	for item in jsonFile:
		for thisField in fields.split(';'):
			field = thisField.split(',')
			jsonFile[i][field[0]] = field[1]
		i += 1

	_.saveTable2(jsonFile,_.switches.value('Output'))

	if _.switches.isActive('Move') == True:
		shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + _v.slash + _.ci(_.switches.value('Input')))
########################################################################################
if __name__ == '__main__':
	action()