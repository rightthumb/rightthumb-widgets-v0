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

import mimetypes
import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext
import _rightThumb._base1 as _

import _rightThumb._mimetype as _mime

if __name__ == '__main__':
	_.switches.register('Count', '-c,-count,--c')
	_.switches.register('Path', '-p')
	_.switches.register('Text', '-t,-text,-txt')
	_.switches.register('Binary', '-bin')

	# _.switches.register('Output', '-o','folder\\appOut.py')
	# _.switches.register('Move', '-move','completed_in-folder_name')

	_.appInfo=    {
		'file': 'files.py',
		'description': 'Lists files',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p files ')
	_.appInfo['examples'].append('')
	_.appInfo['examples'].append('p files --c | p line --c -p "." e | p sortthis | p counteach')





	_.switches.process()



def isText(file):
	# result = True
	# if _.switches.isActive('Text') == True:
	#     mime = mimetypes.guess_type(file)
	#     if str(mime) == "('text/plain', None)":
	#         result = True
	#     else:
	#         result = False
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'
	return result

def getFolder(folder):
	global i
	try:
		dirList = os.listdir(folder)
		action = True
	except Exception as e:
		action = False
	if action == True:
		if os.path.isdir(folder) == True:
			dirList = os.listdir(folder)
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path) == True:

				if _.showLine(item) == True:

					if not _.switches.isActive('Text') and not _.switches.isActive('Binary'):
						i = i + 1
						# print(0,whatIsIt(path),path)
						print(path)
					else:
						if not _.switches.isActive('Binary') and  _.switches.isActive('Text') and isText(path):
							i = i + 1
							# print(1,whatIsIt(path),path)
							print(path)
						if not _.switches.isActive('Binary') and not _.switches.isActive('Text'):
							i = i + 1
							# print(2,whatIsIt(path),path)
							print(path)

						if not _.switches.isActive('Text') and  _.switches.isActive('Binary') and not isText(path):
							i = i + 1
							# print(3,whatIsIt(path),path)
							print(path)
						if not _.switches.isActive('Text') and  not _.switches.isActive('Binary'):
							i = i + 1
							# print(4,whatIsIt(path),path)
							print(path)


			if os.path.isdir(path) == True:
				newFolder = folder + _v.slash + item
				if os.path.isdir(newFolder) == True:
					try:
						getFolder(newFolder)
					except Exception as e:
						pass
				else:
					print('error')



if __name__ == '__main__':
	if _.switches.isActive('Path') == False:
		folder = os.getcwd()
	else:
		folder = _.switches.value('Path')
	i = 0
	getFolder(folder)
	if _.switches.isActive('Count') == False:
		print('\n{}\n'.format(i))


