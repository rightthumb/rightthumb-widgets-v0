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
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import csv

_.switches.register('Input', '-input')

_.appInfo=    {
	'file': 'csvfix.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p csvfix -i')


_.switches.process()


########################################################################################
def action():

	csv.register_dialect('myDialect', delimiter='/', quoting=csv.QUOTE_NONE)

	with open(_.switches.value('Input'), newline='') as myFile:  
	reader = csv.reader(myFile, dialect='myDialect')
	for row in reader:
		print(row) 


########################################################################################
if __name__ == '__main__':
	action()