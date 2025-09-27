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

import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import _rightThumb._base1 as _

_.switches.register('NoFolder', '--c2')
_.switches.register('Count', '-c,-count,--c')
_.switches.register('Path', '-p')
_.switches.register('Text', '-t,-text')

# p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute
_.switches.process()
if __name__ == '__main__':
	if _.switches.isActive('NoFolder') == True:
		print('Folders:\n')

	folder = os.getcwd()
	dirList = os.listdir(folder)
	i = 0
	for item in dirList:
		path = folder + _v.slash + item
		# if os.path.isfile(item) == True:
		if os.path.isdir(item) == True:
			if _.showLine(item) == True:
				i = i + 1
				# print(item)
				if _.switches.isActive('NoFolder') == True:
					print('\t',item)
				else:
					print(item)


	if _.switches.isActive('Count') == False and _.switches.isActive('NoFolder') == False:
		print('\n{}\n{}'.format(i,folder))
	if _.switches.isActive('NoFolder') == True:
		print('',i)