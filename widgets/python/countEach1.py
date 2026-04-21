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

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('CleanUp', '-cleanup')
_.switches.register('SkipFirst', '-first,-skip')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'countEach.py',
	'description': 'counts each',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p files --c | p line -p \\ 3 --c | p countEach')
_.appInfo['examples'].append('p files --c| p line --c -p "." e | p sortThis | p counTeach')
_.appInfo['examples'].append('p files --c| p line --c -p "." e | p sortThis | p counTeach -cleanup')

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
	last = ''
	count = 0
	result = []
	for line in pipeData:
		line = line.replace('\n','')
		if _.switches.isActive('CleanUp'):
			line = line.lower()    
			line = line.replace(' ','')
		count += 1
		if not line == last:
			if _.switches.isActive('SkipFirst'):
				if len(last) > 0:
					result.append({'cnt': count, 'line': last})
			else:
				result.append({'cnt': count, 'line': last})
			count = 0
		last = line
	result0 = _.sort(result,'cnt')
	for data in result0:
		print('',data['cnt'],'\t',data['line'])

	# print(count, last)
	# print(line,count)




########################################################################################
if __name__ == '__main__':
	action()
	# print(pipeData)