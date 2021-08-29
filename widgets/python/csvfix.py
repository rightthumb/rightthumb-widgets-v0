#!/usr/bin/python3
# import os
import sys
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

import csv

_.switches.register('Input', '-input')

_.appInfo=	{
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



