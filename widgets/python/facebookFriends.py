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

from lxml import html
import requests
import cssselect


_.switches.register('Person', '-person','scott.reph')
# _.switches.register('Input', '-i','appIn.py')
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
# https://www.facebook.com/tara.mcmahan.3/friends_all?
########################################################################################
def lookupFriends(url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	friendsList = tree.cssselect('.fsl')
	friends = []

	for friend in friendsList:
		# links = friend.cssselect('a')
		# link0 = str(links[0].attrib['href'])
		print(friend.text_content())

def action():
	url = 'https://www.facebook.com/scott.reph/friends_all?'
	lookupFriends(url)



########################################################################################
if __name__ == '__main__':
	action()





