# import os

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
# import simplejson as json
import _rightThumb._base as _
import _rightThumb._vars as _v
import _rightThumb._string as _str


_.switch.append({'name': 'File','switch': '-file', 'pos': None, 'active': False,'expected_input_example': None})

_.appInfo=    {
	'file': 'drive.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p drive -scan')

_.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

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

_.setExternalScriptTrigger('Column',formatColumns)
_.processSwitches(sys.argv)

_.tableProfile.append({
	'field': 'timestamp', 
	'script_trigger_external': _.float2Date
	})

if _.isSwitchActive('File') == False:
	file = _.getSwitchValue('File')
	variable = _.getTable(file)
	_.saveTable(xRefList,file)

	variable = _.getTable2(file)
	_.saveTable2(xRefList,file)

	line = _str.replaceAll(line,'  ',' ')
	line = _str.cleanFirst(line,' ')
	line = _str.cleanLast(line,' ')
	line = _str.cleanSpecial(line)
	line = _str.totalStrip(line)
	line = _str.removeAll(line)
	line = _str.replaceDuplicate(line,' ')
	if _isSwitchActive('Sort'):
		xRefList = _.sortThis(xRefList, _.getSwitchValue('Sort'))
	_.printColumns(_.switch,'name,switch,expected_input_example')
	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)
	_.updateSwitchField('name','column','value')



	# if _.showLine(string):
		# print(line)
pipeResults = ''

if not sys.stdin.isatty():
	pipeResults = sys.stdin.readlines()
	try:
		if pipeResults[0][0].isalnum() == False:
			pipeResults[0] = pipeResults[0][1:]
	except Exception as e:
		pass

########################################################################################
def action():
	pass



########################################################################################
if __name__ == '__main__':
	action()





