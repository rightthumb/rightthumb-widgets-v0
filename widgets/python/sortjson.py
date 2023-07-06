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

from collections import OrderedDict

_.switches.register('File', '-file')
_.switches.register('Order', '-order')

_.appInfo=    {
	'file': 'sortjson.py',
	'description': 'Change the order of json fields',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p sortjson -file outfile.json -order "First Name" "Last Name" "E-mail Address"')


_.switches.process()
if __name__ == '__main__':
	if _.switches.isActive('File') == False:
		file = _.switches.value('File')
		variable = _.getTable(file)
		_.saveTable(xRefList,file)
		line = _str.replaceAll(line,'  ',' ')
		line = _str.cleanFirst(line,' ')
		line = _str.cleanLast(line,' ')
		line = _str.cleanSpecial(line)
		line = _str.totalStrip(line)
		line = _str.removeAll(line)
		line = _str.replaceDuplicate(line,' ')
		if _isSwitchActive('Sort'):
			xRefList = _.sort(xRefList, _.switches.value('Sort'))
		_.tables.register('Auto',_.switch)
		_.tables.print('Auto','name,switch,expected_input_example')

########################################################################################
def action():
	newOrder = []
	i = 1
	for c in _.switches.value('Order').split(','):
		newOrder[c] = i
		i += 1
	variable = _.getTable(file)
	data = json.loads(newOrder, object_pairs_hook=OrderedDict)
	print (json.dumps(data, indent=4))




########################################################################################
if __name__ == '__main__':
	action()





