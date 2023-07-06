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
# import sys
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Input', '-i','file.txt')
_.switches.register('Output', '-o','file.json')
_.switches.register('Enumerate', '-enu')

_.appInfo=    {
	'file': 'genDic.py',
	'description': 'Generates dictionary',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}





_.appInfo['examples'].append('p gendic -i _adj.txt -o dic_adj.json')
_.appInfo['examples'].append('p gendic -i _adv.txt -o dic_adv.json')
_.appInfo['examples'].append('p gendic -i _noun.txt -o dic_noun.json')
_.appInfo['examples'].append('p gendic -i _verb.txt -o dic_verb.json')
_.appInfo['examples'].append('p gendic -i all5 -o dic_all.json')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
def action():
	if not _.switches.isActive('Input') or not _.switches.isActive('Output'):
		_.switches.process(True)
	else:
		pass
		theText = _.getText(_.switches.value('Input'))
		theJSON = {}
		if _.switches.isActive('Enumerate'):
			for i,d in enumerate(theText):
				d = d.replace('\n','')
				theJSON[d] = i
		else:
			for d in theText:
				d = d.replace('\n','')
				theJSON[d] = 1
		_.saveTable(theJSON,_.switches.value('Output'))



########################################################################################
if __name__ == '__main__':
	action()





