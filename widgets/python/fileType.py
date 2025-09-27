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

import os
import sys
# import simplejson as json
# import shutil
import mimetypes

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


import _rightThumb._mimetype as _mime



# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'fileType.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('dir /b | p fileType')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()


pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if not pipeData[0][0] in _str.safeChar:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass

########################################################################################
def binORtext(file):
	isText = _mime.isText(file)
	if isText:
		result = 'Text'
	else:
		result = 'Binary'
	return result
def action():
	global pipeData
	files = []
	for data in pipeData:
		data = data.replace('\r','')
		data = data.replace('\n','')
		if os.path.isfile(data) == True:
			# files.append({'file': data, 'mimetype': str(mimetypes.guess_type(data))})
			files.append({'file': data, 'mimetype': binORtext(data)})

	_.tables.register('files',files)
	_.tables.print('files','mimetype,file')        

_.switches.fieldSet('Long','active',True)
########################################################################################
if __name__ == '__main__':
	action()