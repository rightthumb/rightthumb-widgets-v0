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

_.switches.register('Input', '-i','appIn.py')
# _.switches.register('Output', '-o','folder\\appOut.py')
# _.switches.register('Move', '-move','completed_in-folder_name')

_.appInfo=    {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p thisApp -file file.txt')

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
# dic_adj.json
# dic_adv.json
# dic_noun.json
# dic_verb.json
# dic_all.json
########################################################################################
def action():
	theText = _.getText(_.switches.value('Input'))
	adj = _.getTable('dic_adj.json')
	adv = _.getTable('dic_adv.json')
	noun = _.getTable('dic_noun.json')
	verb = _.getTable('dic_verb.json')
	# alld = _.getTable('dic_all.json')
	# print(theText)
	has_key = lambda a, d: any(k in a for k in d)

	for tx in theText:
		# if has_key(tx,adj):
		#     print('adj')
		# if has_key(tx,adv):
		#     print('adv')
		# if has_key(tx,noun):
		#     print('noun')
		# if has_key(tx,verb):
		#     print('verb')

		if tx in adj.keys():
			print('adj')
		if tx in adv.keys():
			print('adv')
		if tx in noun.keys():
			print('noun')
		if tx in verb.keys():
			print('verb')


		# if tx in adj.keys():
			# print('adj')


########################################################################################
if __name__ == '__main__':
	action()





