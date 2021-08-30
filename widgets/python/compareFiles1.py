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
import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v

thresholdCount = 10
thresholdPercent = 2
fileCount = 0


_.switches.register('Count', '-c,-count,--c')
_.switches.register('Show', '-show','n, o, s, d ; new, old, same, deleted')

_.appInfo = {
	'file': 'compareFiles.py',
	'description': 'Automatic audit of pre-negotiated file structures',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['prerequisite'].append('type files0.txt | p line -x files1.txt \ -xs')
_.appInfo['prerequisite'].append('type techfolder.txt | p line -x temp_e.txt \ -xs')
_.appInfo['prerequisite'].append('type techfolder.txt | p line -xu temp_e.txt \ -xi build')

_.appInfo['examples'].append('p compareFiles -show new')
_.appInfo['examples'].append('p compareFiles -show s')
_.appInfo['examples'].append('p compareFiles -show o')
_.appInfo['examples'].append('p compareFiles -show deleted')
_.appInfo['examples'].append('---------------------------------------------------')
_.appInfo['examples'].append('    \t new: both files exist and shows newer one')
_.appInfo['examples'].append('     \t old: both files exist and shows older one')
_.appInfo['examples'].append('      \tsame: both files have same modification date')
_.appInfo['examples'].append('   unmatched: one is deleted')
_.appInfo['examples'].append('both_deleted: both files are deleted')
# _.appInfo['examples'].append('   missing: ')

_.appInfo['columns'].append({'name': 'new', 'abbreviation': 'n'})
_.appInfo['columns'].append({'name': 'old', 'abbreviation': 'o'})
_.appInfo['columns'].append({'name': 'same', 'abbreviation': 's'})
_.appInfo['columns'].append({'name': 'deleted', 'abbreviation': 'd'})
_.appInfo['columns'].append({'name': 'unmatched', 'abbreviation': 'u'})
_.appInfo['columns'].append({'name': 'both_deleted', 'abbreviation': 'b'})
# _.appInfo['columns'].append({'name': 'missing', 'abbreviation': 'm'})


def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']

		result += c + ','
	result = result[:-1]
	return result

_.switches.trigger('Show',formatColumns)


_.switches.process()








def process():
	global xRefList
	global xRefBase

	global thresholdCount
	global thresholdPercent

	global fileCount

	i = 0
	cntOmited = 0
	for xRef in xRefList:
		if (xRefBase[xRefList[i]['files'][0]['nStat_id']]['value'] > thresholdPercent and xRefBase[xRefList[i]['files'][1]['nStat_id']]['value'] > thresholdPercent) or xRefBase[xRefList[i]['files'][1]['nStat_id']]['count'] > thresholdCount:
			# print(xRef['negotiated'])
			xRefList[i]['relevant'] = 1
			missing = 0
			if os.path.isfile(xRefList[i]['files'][0]['path']):
				xRefList[i]['files'][0]['date'] = os.path.getmtime(xRefList[i]['files'][0]['path'])
				xRefList[i]['files'][0]['exists'] = 1
			else:
				missing += 1
				xRefList[i]['files'][0]['date'] = 0
				xRefList[i]['files'][0]['exists'] = 0

			if os.path.isfile(xRefList[i]['files'][1]['path']):
				xRefList[i]['files'][1]['date'] = os.path.getmtime(xRefList[i]['files'][1]['path'])
				xRefList[i]['files'][1]['exists'] = 1
			else:
				missing += 1
				xRefList[i]['files'][1]['date'] = 0
				xRefList[i]['files'][1]['exists'] = 0
			xRefList[i]['missing'] = missing
			if xRefList[i]['files'][0]['date'] > xRefList[i]['files'][1]['date']:
				xRefList[i]['new'] = 0
				new = 0
				old = 1
			else:
				xRefList[i]['new'] = 1
				new = 1
				old = 0
		else:
			xRefList[i]['relevant'] = 0
			cntOmited += 1
		i += 1

def display():
	global xRefList
	global xRefBase

	global thresholdCount
	global thresholdPercent

	global fileCount
	xRefList = _.sort(xRefList, 'new')
	i = 0
	cntOmited = 0
	for xRef in xRefList:
		if xRefList[i]['relevant'] == 1:



			if xRefList[i]['files'][0]['date'] > xRefList[i]['files'][1]['date']:
				new = 0
				old = 1
			else:
				new = 1
				old = 0

			if xRefList[i]['files'][0]['exists'] == 1 and xRefList[i]['files'][1]['exists'] == 1:
				if _.switches.value('Show') == 'new':
					print(xRefList[i]['files'][new]['path'])
				if _.switches.value('Show') == 'old':
					print(xRefList[i]['files'][old]['path'])
				if _.switches.value('Show') == 'same':
					if xRefList[i]['files'][0]['date'] == xRefList[i]['files'][1]['date']:
						print(xRefList[i]['negotiated'])


			if _.switches.value('Show') == 'deleted':
				if xRefList[i]['files'][0]['exists'] == 0:
					print(xRefList[i]['files'][0]['path'])
				if xRefList[i]['files'][1]['exists'] == 0:
					print(xRefList[i]['files'][1]['path'])
			if (xRefList[i]['files'][0]['exists'] == 1 and xRefList[i]['files'][1]['exists'] == 0) or (xRefList[i]['files'][0]['exists'] == 0 and xRefList[i]['files'][1]['exists'] == 1):
				if _.switches.value('Show') == 'unmatched':
					print(xRefList[i]['files'][1]['path'])
					print(xRefList[i]['files'][0]['path'])
					print('')
			if xRefList[i]['files'][0]['exists'] == 0 and xRefList[i]['files'][1]['exists'] == 0:
				if _.switches.value('Show') == 'both_deleted':
					print(xRefList[i]['files'][1]['path'])
					print(xRefList[i]['files'][0]['path'])
					print('')
		else:
			cntOmited += 1
		i += 1
xRefList = _.getTable('file_negotiation_table.json')
xRefBase = _.getTable('file_negotiation_statistics.json')

# print(type(xRefBase))
# print(type(xRefList))
# print(_.switches.value('Show'))
# sys.exit()


process()
display()

_.saveTable(xRefList,'processed_file_negotiation_table.json',False)


