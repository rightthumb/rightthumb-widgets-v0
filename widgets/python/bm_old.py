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

import glob
import os.path
import sys
from os.path import join, getsize, isfile, isdir, splitext
# import _rightThumb._vars as _v


def formatName(string):
	global myBookmarks
	string = string.replace('BM-','')
	string = string.replace('.txt','')
	string = string.replace(myBookmarks,'')
	return string

indexFiles = myBookmarks + '*.txt'
bm = []
for files in glob.glob( indexFiles ):
	if os.path.isfile(files) == True:
		with open(files,  'r', encoding='latin-1') as f:
			for line in f:
				pass
				fname = formatName(str(f.name))
				line = line.replace('\n','')
				if os.path.isdir(line) == True:
					valid = True
				else:
					valid = False
				bm.append({'name': fname, 'path': line, 'valid': valid})
			f.close()
val = 0
notval = 0
for b in bm:
	# print(b['valid'])
	if b['valid'] == True:
		val += 1
	else:
		notval += 1

print('valid: {}     not valid: {}     total: {}'.format(val,notval,val+notval    ))