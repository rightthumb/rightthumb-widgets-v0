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

folder = os.getcwd()
i = 0
def getFolder(folder):
	global i
	try:
		dirList = os.listdir(folder)
		action = True
	except Exception as e:
		action = False
	if action == True:
		for item in dirList:
			path = folder + _v.slash + item
			# if os.path.isfile(item) == True:
			if os.path.isdir(path) == True:
				i = i + 1
				print(path)
				newFolder = folder + _v.slash + item
				try:
					getFolder(newFolder)
				except Exception as e:
					pass
getFolder(folder)
print('\n{}\n'.format(i))