#!/usr/bin/python3
# import mimetypes
import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import _rightThumb._base1 as _

import _rightThumb._mimetype as _mime

import shutil

_.switches.register('Count', '-c,-count,--c')
_.switches.register('Path', '-p')
_.switches.register('Text', '-t,-text')
_.switches.register('Undo', '-u,-undo')

# p file + bm- | p f + { -jn | p line --c -make "xcopy /d/y {} Default(bookmarks)\\" | p execute
_.switches.process()

def isText(file):
	result = True
	if _.switches.isActive('Text') == True:
		mime = mimetypes.guess_type(file)
		if str(mime) == "('text/plain', None)":
			result = True
		else:
			result = False
	return result





folder = os.getcwd()
dirList = os.listdir(folder)
i = 0
for item in dirList:
	path = folder + _v.slash + item
	if os.path.isfile(item) == True:
	# if os.path.isdir(item) == True:
		if _.showLine(item) == True:
			# if isText(item) == True:
			if _mime.isText(item):
				i = i + 1
				if _.switches.isActive('Undo') == True:
					shutil.move(item, item.replace('_',' '))
					print(item.replace('_',' '))
				else:
					shutil.move(item, item.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace(' ','_').replace('y2mate.com_-_',''))
					print(item.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace(' ','_'))
if _.switches.isActive('Count') == False:
	print('\n{}\n{}'.format(i,folder))
