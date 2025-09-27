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

import _rightThumb._construct as __
__.appReg = __name__
import _rightThumb._base2 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

# _.switches.register('Input', '-i','appIn.py')


_.appInfo[__name__]=    {
	'file': 'findfunc.py',
	'description': 'returns the function that contains the search string',
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo[__name__]['relatedapps'].append('p iterateTest ?')


_.appInfo[__name__]['examples'].append('type imdb.py | p findfunc + "global relationships"')
_.appInfo[__name__]['examples'].append('')
_.appInfo[__name__]['examples'].append('type imdb.py | p findfunc + "relationships" - global "for "')
_.appInfo[__name__]['examples'].append('type imdb.py | p findfunc + "relationships" - global "for " -long')

# _.appInfo[__name__]['columns'].append({'name': 'name', 'abbreviation': 'n'})



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True


_.switches.process()
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f


def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)



pipeData = ''

if not sys.stdin.isatty():
	pipeData = sys.stdin.readlines()
	try:
		if not pipeData[0][0] in _str.safeChar:
			pipeData[0] = pipeData[0][1:]
	except Exception as e:
		pass

########################################################################################
def findInFunc(i,functions):
	if len(functions) == 0:
		print('No Functions')
	found = 'No Function'
	for fun in functions:
		if i >= fun['start'] and i < fun['end']:
			found = fun['function']
	return found

def cleanupString(string,beforeAfter=True):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	# string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = string.replace(_v.slash+'xe2\\x80\\x93','-')
	string = string.replace(_v.slash+'\\xe2\\\\x80\\\\x93','-')
	# if beforeAfter:
	#     string = string.split('(')[0]
	# else:
	#     string = string.split('(')[1]
	# string = string.split('/')[0]
	return string

def action():
	global pipeData

	
	for ii, line in enumerate(pipeData):
		maxLine = ii + 1

	inFunc = False
	functions = []
	thisFunc = ''
	thisFuncStart = 0
	for ii, line in enumerate(pipeData):
		line = line.replace('\n','')
		i = ii + 1
		# print(i)
		try:
			if line[0].isalnum():
			# if not line.startswith(' ') and not line.startswith('\t') and not line.startswith('\n'):
				if inFunc:
					row = {'function': thisFunc, 'start': thisFuncStart, 'end': i}
					functions.append(row)
					# print(row)
					inFunc = False
			# print(line[0])
		except Exception as e:
			pass
			# raise e
		if line.startswith('def '):
			inFunc = True
			thisFunc = line.replace('def ','').split('(')[0]
			thisFuncStart = i
			# print(line)
	foundSet = []
	for ii, line in enumerate(pipeData):
		line = line.replace('\n','')
		i = ii + 1

		if _.showLine(line):
			foundSet.append({'function': findInFunc(i,functions), 'line': i, 'text': cleanupString(line)})
	print('')
	_.tables.register('Auto',foundSet)
	_.tables.print('Auto','function,line,text')
	print('')
	print(len(foundSet))
_.switches.fieldSet('GroupBy','active',True)
_.switches.fieldSet('GroupBy','value','function')
########################################################################################
if __name__ == '__main__':
	action()