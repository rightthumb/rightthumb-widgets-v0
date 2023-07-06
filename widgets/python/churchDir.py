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

_.switches.register('First', '-f,-first','ju*')
_.switches.register('Last', '-l,-last','p*')
# _.switches.register('Data', '-data','f,e')

_.appInfo=    {
	'file': 'churchDir.py',
	'description': 'Lookup directory information',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p churchDir -first justin -last p*')

_.appInfo['columns'].append({'name': 'first', 'abbreviation': 'f'})
_.appInfo['columns'].append({'name': 'last', 'abbreviation': 'l'})
_.appInfo['columns'].append({'name': 'phone', 'abbreviation': 'p'})
_.appInfo['columns'].append({'name': 'email', 'abbreviation': 'e'})
_.appInfo['columns'].append({'name': 'address', 'abbreviation': 'a'})

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

_.switches.trigger('Column',formatColumns)
_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass
data = _.getTable2('D:\\_Scott\\S_Documents\\Projects\\self\\Church_Directory\\Church_Directory.json')
########################################################################################
def action():
	global data
	
	_.switches.fieldSet('Long','active',True)
	_.tables.fieldProfileSet('members','first','alignment','right')
	_.tables.fieldProfileSet('members','last','alignment','left')
	# _.tables.fieldProfileSet('members','phone,email,address','alignment','center')
	_.tables.fieldProfileSet('members','_header_','alignment','center')
	_.tables.fieldProfileSet('members','*','alignment','center')
	# _.tables.registerView('members','data','first,last,phone','last')
	# _.tables.printView('data')
	_.tables.fieldProfileSet('members','phone','trigger',_.formatPhone0)
	_.tables.fieldProfileSet('members','email','trigger',_.validateEmail)
	_.tables.fieldProfileSet('members','first,last,address','trigger',_str.totalStrip6)
	# _.tables.alignmentMasterSupersedes('members',True)
	# _.tables.trigger('members','phone',_.formatPhone0)

	def check(first,last):
		ok = True
		for fam in data:
			for peeps in fam['people']:
				if len(peeps['phone']) > 9:
					if peeps['first'].lower() == first.lower() and fam['last'].lower() == last.lower():
						ok = False
		return ok



	newData = []
	for family in data:
		for person in family['people']:
			if len(person['first']) > 0:
				for them0 in person['first'].split(','):
					for them in them0.split('&'):
						them = _str.cleanBE(them,' ')
						family['last'] = _str.cleanBE(family['last'],' ')
						if len(them) > 1:
							if len(person['phone']) > 9:
								newData.append({'first': them, 'last': family['last'], 'phone': person['phone'], 'email': person['email'], 'address': _str.cleanEnd2(family['address1'],' ') + ', ' + family['address2']})
							if check(them,family['last']):
								newData.append({'first': them, 'last': family['last'], 'phone': person['phone'], 'email': person['email'], 'address': _str.cleanEnd2(family['address1'],' ') + ', ' + family['address2']})
	data = []
	print()


	if _.switches.isActive('Last') == False and _.switches.isActive('First') == False:
		# for family in data:
		#     print()
		#     print('___________________________________')
		#     print(family['last'])

		#     print('\t',_str.cleanEnd2(family['address1'],' ') + ', ' + family['address2'])
		#     print()
		#     _.tables.register('members',family['people'])
		#     _.tables.print('members','first,phone,email')

		print()
		_.tables.register('members',newData)
		if _.switches.isActive('Column'):
			
			_.tables.print('members',_.switches.value('Column'))
		else:
			_.tables.print('members','first,last,phone,email')





	if _.switches.isActive('Last') and _.switches.isActive('First') == False:
		for person in newData:
			if _.switches.isActive('Last'):
				_.switches.fieldSet('Plus','active',True)
				_.switches.fieldSet('Plus','value',_.switches.value('Last'))
				if _.showLine(person['last']):
					data.append({'first': person['first'], 'last': person['last'], 'phone': person['phone'], 'email': person['email'], 'address': _str.cleanEnd2(family['address1'],' ') + ', ' + family['address2']})
		_.tables.register('members',data)
		if _.switches.isActive('Column'):
			_.switches.fieldSet('Long','active',True)
			_.tables.print('members',_.switches.value('Column'))
		else:
			_.tables.print('members','first,last,phone,email')

	if _.switches.isActive('Last') == False and _.switches.isActive('First'):
		for person in newData:
			if _.switches.isActive('First'):
				_.switches.fieldSet('Plus','active',True)
				_.switches.fieldSet('Plus','value',_.switches.value('First'))
				if _.showLine(person['first']):
					data.append({'first': person['first'], 'last': person['last'], 'phone': person['phone'], 'email': person['email'], 'address': _str.cleanEnd2(family['address1'],' ') + ', ' + family['address2']})
		_.tables.register('members',data)
		if _.switches.isActive('Column'):
			_.switches.fieldSet('Long','active',True)
			_.tables.print('members',_.switches.value('Column'))
		else:
			_.tables.print('members','first,last,phone,email')

	if _.switches.isActive('Last') and _.switches.isActive('First'):
		for person in newData:
			if _.switches.isActive('Last'):
				_.switches.fieldSet('Plus','active',True)
				_.switches.fieldSet('Plus','value',_.switches.value('Last'))
				if _.showLine(person['last']):
					_.switches.fieldSet('Plus','value',_.switches.value('First'))
					if _.showLine(person['first']):    
						data.append({'first': person['first'], 'last': person['last'], 'phone': person['phone'], 'email': person['email'], 'address': _str.cleanEnd2(family['address1'],' ') + ', ' + family['address2']})
		_.tables.register('members',data)
		if _.switches.isActive('Column'):
			_.switches.fieldSet('Long','active',True)
			_.tables.print('members',_.switches.value('Column'))
		else:
			_.tables.print('members','first,last,phone,email')




########################################################################################
if __name__ == '__main__':
	action()





