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

_.switches.register('Input', '-i','file0.json file2.json')
_.switches.register('Output', '-o','combined\file.json')
_.switches.register('Move', '-move','folder_2_move_completed_input_files')

_.appInfo=    {
	'file': 'combinejsonfiles.py',
	'description': 'Combine json files',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p combinejsonfiles -i file0.json file1.json -o combined\\file.json -move completed')

_.switches.process()





########################################################################################
def action():
	if _.switches.isActive('Input') == False or _.switches.isActive('Output') == False:
		print('Error: Missing input')
		sys.exit()
	newJSON = []
	jsonInput = []
	files = _.switches.value('Input')
	for file in files.split(','):
		jsonInput.append(_.getTable2(_.ci(file)))
	for ji in jsonInput:
		for j in ji:
			newJSON.append(j)

	_.saveTable2(newJSON,_.switches.value('Output'))

	if _.switches.isActive('Move') == True:
		for file in files.split(','):
			shutil.move(_.ci(file), _.switches.value('Move') + _v.slash + _.ci(file))

########################################################################################
if __name__ == '__main__':
	action()