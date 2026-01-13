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

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import sys
import simplejson as json
import os, subprocess
from os.path import join, getsize, isfile, isdir, splitext

_.switches.register('File', '-file','file.txt')
_.switches.register('Folder', '-folder','table, temp')
_.switches.process()

folder = ''
if _.switches.isActive('Folder'):
	if _.switches.value('Folder') == 'table':
		# print('table')
		folder = _v.myTables + _v.slash
		tableTemp = False
	if _.switches.value('Folder') == 'temp':
		# print('temp')
		folder = _v.stmp + _v.slash
		tableTemp = True
path = folder + _.switches.value('File')
if os.path.isfile(path):
	print('\nfile exists\n')
	# print(os.path.realpath(path))
	file = _.getTable(_.switches.value('File'),tableTemp,True)
	# print(type(file))
	print()
	print(len(file))
else:
	print('\n',path,'\n')
	print('file does NOT exists\n')