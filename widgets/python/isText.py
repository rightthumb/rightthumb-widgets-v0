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
# import mimetypes
import os, subprocess

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import _rightThumb._mimetype as _mime

# _.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'isText.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('type file.txt | p isText')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


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
def action():
	global pipeData
	for line in pipeData:
		line = line.replace('\r','')
		line = line.replace('\n','')
		shouldKeep = True
		if not len(line) > 0:
			shouldKeep = False
		else:
			if not os.path.isfile(line) == True:
				shouldKeep = False
			else:
				# if not str(mimetypes.guess_type(line)) == "('text/plain', None)":
				if _mime.isBinary(line):
					shouldKeep = False
		if shouldKeep:
			print(line)


########################################################################################
if __name__ == '__main__':
	action()