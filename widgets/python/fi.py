#!/usr/bin/python3
import sys
import glob
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext

folder = os.getcwd()
dirList = os.listdir(folder)
i = 0
for item in dirList:
	path = folder + _v.slash + item
	if os.path.isfile(item) == True:
	# if os.path.isdir(item) == True:
		i = i + 1
		print(item)
print('\n{}\n{}'.format(i,folder))
