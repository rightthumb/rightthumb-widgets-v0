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

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('NoCount', '--c')

_.appInfo=    {
	'file': 'execute.py',
	'description': 'Execute pipe data',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('type %tmpf1% | p execute ')

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
	for pip in pipeData:
		pip = pip.replace('\n','')
		if not  _.switches.isActive('NoCount'):
			print(pip)
		try:
			os.system(pip)
		except Exception as e:
			print('Error')
		



########################################################################################
if __name__ == '__main__':
	action()



