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

_.switches.register('Level', '-level')

_.appInfo=    {
	'file': 'sortThis.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('type out_file.txt | p inChar | p sortThis | p countEach | sort')

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
	# sorted(var, key=lambda v: (v.upper(), v[0].islower()))
	if _.switches.isActive( 'Level' ):
		# print( 'HERE' )
		newPipe = []
		for i,row in enumerate(pipeData):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			row = row.lower()
			row = _str.clean_latin1( row )
			row = _str.cleanBE(row,' ')
			if len( row ):
				newPipe.append( row )

		pipeData = newPipe

	for d in sorted(pipeData, key=lambda v: (v.upper(), v[0].islower())):
		d = d.replace('\n','')
		d = d.replace('\r','')
		print(d)



########################################################################################
if __name__ == '__main__':
	action()





