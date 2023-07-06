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

# import mimetypes
import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import _rightThumb._base1 as _


import _rightThumb._mimetype as _mime


_.switches.register('Path', '-p')
_.switches.register('Text', '-t,-text')
_.switches.register('Binary', '-bin')
_.switches.register('Count', '-c,-count,--c')

# p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute
_.switches.process()


if __name__ == '__main__':
	if not _.switches.isActive('Count'):
		print('Files:\n')



	folder = os.getcwd()
	dirList = os.listdir(folder)
	i = 0
	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(item) == True:
		# if os.path.isdir(item) == True:
			if _.showLine(item) == True:
				if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
					i = i + 1
					# print(0,_mime.what(path),path)
					# print(path)
					if _.switches.isActive('Path'):
						print( path )
					elif not _.switches.isActive('Count'):
						print( '\t', item )
					else:
						print( item )
				else:
					if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and _mime.isText(path):
						i = i + 1
						# print(1,_mime.what(path),path)
						# print(path)
						print( '\t', item )
					if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
						i = i + 1
						# print(2,_mime.what(path),path)
						# print(path)
						print( '\t', item )

					if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not _mime.isText(path):
						i = i + 1
						# print(3,_mime.what(path),path)
						# print(path)
						print( '\t', item )
					if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
						i = i + 1
						# print(4,_mime.what(path),path)
						# print(path)
						print( '\t', item )

	# if _.switches.isActive('Count') == False and _.switches.isActive('NoFolder') == False:
	#     print('\n{}\n{}'.format(i,folder))
	# if _.switches.isActive('NoFolder') == True:
	#     print('',i)
	if not _.switches.isActive('Count'):
		print('',i)


