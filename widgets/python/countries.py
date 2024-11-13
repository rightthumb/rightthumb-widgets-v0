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


_.switches.register('Country', '-country')
_.switches.register('States', '-states')
_.switches.register('Count', '-count')
_.switches.register('HasStates', '-hasstates')

_.appInfo=    {
	'file': 'countries.py',
	'description': 'Manages drives and indexes',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p countries -country "United States" -states')
_.appInfo['examples'].append('p countries + un -hasstates -count')
_.appInfo['examples'].append('p countries -hasstates -count')


_.switches.process()



########################################################################################
def action():
	jsonFile = 'countries_from_adobe_web_form.json'
	countriesAndStates = variable = _.getTable(jsonFile)
	
	if _.switches.isActive('Country') == True and _.switches.isActive('States') == True:
		foundCount = 0
		found = []
		for cs in countriesAndStates:
			if _.switches.value('Country') in cs['name']:
				foundCount += 1
				found.append(cs['name'])
				if _.switches.value('Country') == cs['name']:
					break
		if foundCount == 0:
			print('Error: Country not found')
		elif foundCount == 1:

			for cs in countriesAndStates:
				if _.switches.value('Country') == cs['name']:
					print()
					print(len(cs['states']),' ', cs['name'])
					print()
					i = 0
					if len(cs['states']) > 0:
						for st in cs['states']:
							if _.showLine(st['name']) == True:
								if not st['name'] == 'Select':
									print('\t',st['name'])
								i += 1
			print()
			print(i)

		elif foundCount > 1:
			for fnd in found:
				print(fnd)

	else:
		if _.switches.isActive('Country') == True and len(_.switches.value('Country')) > 0:
			_.switches.fieldSet('Plus','active',True)
			_.switches.fieldSet('Plus','value',_.switches.value('Country'))
		i = 0
		for cs in countriesAndStates:
			if _.showLine(cs['name']) == True:
				if _.switches.isActive('HasStates') == True:
					if len(cs['states']) > 0:
						if _.switches.isActive('Count') == True:
							print(len(cs['states']),'\t', cs['name'])
							i += 1
						else:
							print(cs['name'])
							i += 1
				elif _.switches.isActive('Count') == True:
					pass
					print(len(cs['states']),'\t', cs['name'])
					i += 1
				else:
					pass
					print(cs['name'])
					i += 1
		print()
		print(i)

########################################################################################
if __name__ == '__main__':
	action()





