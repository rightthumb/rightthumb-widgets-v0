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

# https://boldpreciousmetals.com/product/2012-s-silver-proof-america-the-beautiful-quarter-el-yunque/


# import os
import sys
# import simplejson as json
# import shutil
# import sqlite3

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str




if __name__ == '__main__':
	_.switches.register('Add', '-a,-add','cat category coin both')
	_.switches.register('Find', '-f,-find')
	_.switches.register('Coin', '-coin','q d n p')
	_.switches.register('Label', '-label,-st,-state','SC')
	_.switches.register('Year', '-y,-year','1999')
	_.switches.register('Type', '-type')
	_.switches.register('Value', '-value')
	_.switches.register('Hashtag', '-t,-tag,-tags,-hashtag,-hashtags,#,-#','bird mountain')
	_.switches.register('Research', '-research','state quarter')
	_.switches.register('Verbiage', '-text,-verbiage,-verbage','Puerto Rico')
	_.switches.register('Currency', '-cu,-currency')

	_.appInfo=    {
		'file': 'coins.py',
		'description': 'Manage coins',
		'prerequisite': [],
		'examples': [],
		'columns': [],
		}

	_.appInfo['examples'].append('p coins -add both -coin q -state SC -year 1999 -type state -hashtags horse person cowboy -text test')
	_.appInfo['examples'].append('')
	_.appInfo['examples'].append('p coins -find -research + state quarter')
	_.appInfo['examples'].append('p coins -add -research "https://en.wikipedia.org/wiki/50_State_Quarters" -hashtags state quarters')
	_.appInfo['examples'].append('')

	_.appInfo['columns'].append({'name': 'quarter', 'abbreviation': 'q'})
	_.appInfo['columns'].append({'name': 'quarter', 'abbreviation': 'quarters'})

	_.appInfo['columns'].append({'name': 'dime', 'abbreviation': 'd'})
	_.appInfo['columns'].append({'name': 'dime', 'abbreviation': 'dimes'})

	_.appInfo['columns'].append({'name': 'nickel', 'abbreviation': 'n'})
	_.appInfo['columns'].append({'name': 'nickel', 'abbreviation': 'nickels'})

	_.appInfo['columns'].append({'name': 'penny', 'abbreviation': 'p'})
	_.appInfo['columns'].append({'name': 'penny', 'abbreviation': 'pennies'})

	_.appInfo['columns'].append({'name': 'state', 'abbreviation': 's'})
	_.appInfo['columns'].append({'name': 'state', 'abbreviation': 'states'})


def cleanCategory(string):
	# print(type(string))
	if not type(string) == str:
		string = ''
	# sys.exit()
	result = string
	if 'ca' in string.lower():
		result = 'category'
	if 'b' in string.lower():
		result = 'both'
	if 'co' in string.lower():
		result = 'coin'
	return result


def cleanCurrency(string):
	if not type(string) == str:
		string = ''
	result = string
	try:
		if string.lower() in 'puerto rico':
			result = 'PR'
		if string.lower() in 'united states of america':
			result = 'USA'
		if string.lower() in 'usa':
			result = 'USA'
		if string.lower() in '':
			result = 'USA'
	except Exception as e:
		result = 'USA'
	# print(result)
	# sys.exit()
	return result.upper()



def formatColumns(columns):
	if not type(columns) == str:
		columns = ''
	result = ''
	for c in columns.split(','):
		for col in _.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result


def buildAbbreviations():
	abbreviations = []
	statesRaw = 'ALABAMA,AL;ALASKA,AK;ARIZONA,AZ;ARKANSAS,AR;CALIFORNIA,CA;COLORADO,CO;CONNECTICUT,CT;DELAWARE,DE;FLORIDA,FL;GEORGIA,GA;HAWAII,HI;IDAHO,ID;ILLINOIS,IL;INDIANA,IN;IOWA,IA;KANSAS,KS;KENTUCKY,KY;LOUISIANA,LA;MAINE,ME;MARYLAND,MD;MASSACHUSETTS,MA;MICHIGAN,MI;MINNESOTA,MN;MISSISSIPPI,MS;MISSOURI,MO;MONTANA,MT;NEBRASKA,NE;NEVADA,NV;NEW HAMPSHIRE,NH;NEW JERSEY,NJ;NEW MEXICO,NM;NEW YORK,NY;NORTH CAROLINA,NC;NORTH DAKOTA,ND;OHIO,OH;OKLAHOMA,OK;OREGON,OR;PENNSYLVANIA,PA;RHODE ISLAND,RI;SOUTH CAROLINA,SC;SOUTH DAKOTA,SD;TENNESSEE,TN;TEXAS,TX;UTAH,UT;VERMONT,VT;VIRGINIA,VA;WASHINGTON,WA;WEST VIRGINIA,WV;WISCONSIN,WI;WYOMING,WY'
	states = statesRaw.split(';')
	for s in states:
		item = s.split(',')
		abbreviations.append({'name': item[0].title(), 'abbreviation': item[1]})
	return abbreviations

def cleanStates(state):
	abbreviations = buildAbbreviations()
	state = state.replace(',',' ')

	
	_.switches.fieldSet('Plus','active',True)
	_.switches.fieldSet('Plus','value',state)
	found = False
	data = []
	if len(state) < 3 and len(state) > 0:
		i = 0
		for abb in abbreviations:
			if _.showLine(abb['abbreviation']):
				data.append({'id': i, 'name': abb['name'], 'abbreviation': abb['abbreviation']})
				i += 1
	else:
		i = 0
		for abb in abbreviations:
			if _.showLine(abb['name']):
				data.append({'id': i, 'name': abb['name'], 'abbreviation': abb['abbreviation']})
				i += 1

	if len(data) > 1:
		_.tables.register('states',data)
		_.tables.print('states','id,name,abbreviation')
		chosenID = input('Choose a state: ')
		try:
			result = data[int(chosenID)]['abbreviation']
		except Exception as e:
			print('State error')
			sys.exit()
			
	if len(data) == 1:
		result = data[0]['abbreviation']
	if len(data) == 0:
		_.tables.register('states',abbreviations)
		_.tables.print('states','id,name,abbreviation')
		chosenID = input('Choose a state: ')
		try:
			result = data[int(chosenID)]['abbreviation']
		except Exception as e:
			print('State error')
			sys.exit()
	# print(result)
	# sys.exit()
	return result


if __name__ == '__main__':
	_.switches.trigger('Coin',formatColumns)
	_.switches.trigger('Type',formatColumns)
	_.switches.trigger('Verbiage',formatColumns)

	_.switches.trigger('Currency',cleanCurrency)
	_.switches.trigger('Add',cleanCategory)

	_.switches.trigger('Label',cleanStates)


if __name__ == '__main__':
	_.switches.process()




# if __name__ == '__main__':



# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass


# if _.switches.isActive('_File_'):
#     _.tables.register('toCheck') # table, rows = []
#     _.switches.fieldSet('_File_','active',True)
#     _.switches.fieldSet('_File_','value','toCheck.json')
#     _.tables.get('toCheck',_.switches.value('_File_'))
#     _.tables.trigger('toCheck','stamp,time,date',_.float2Dated,True)
#     _.tables.sort('toCheck', 'name')

#     _.tables.registerView('test_table','sample3','name,age','age') # table, view, fields, sort
#     _.tables.view('test_table','sample') # table, view

#     _.switches.fieldGet('Column','pos')
#     if _.switches.exists('Column2'):
#         print('This is a valid switch')




#     if _.switches.isActive('Output') == True:
#         _.saveTable2(jsonFile,_.switches.value('Output'))
#         # _.saveText(convertedFile,_.ci(_.switches.value('Output')))

#     if _.switches.isActive('Move') == True:
#             shutil.move(_.ci(_.switches.value('Input')), _.switches.value('Move') + '\\' + _.ci(_.switches.value('Input')))
#     # if _.showLine(string):
#         # print(line)

#     json = _.getTable('base64Key.json')

#    books = _.getText(_v.myTables + '\\bible_books.csv')

########################################################################################
# class TheChildItems:

#     def __init__(self, name, switch):
#         self.name = name
#         self.active = False
#         self.value = None

#     def trigger(self,script):
#         self.script_trigger = script

#     def changeStatus(self,newStatus):
#         self.active = newStatus
# class TheParentItems:

#     def __init__(self):
#         self.childItemRows = []

#     def register(self, name):
#         self.childItemRows.append(TheChildItems(name))
#     def print(self):
#         childItems = []
#         for ci in self.childItemRows:
#             childItems.append({'name':ci.name})
#         _.tables.register('childClassItems',childItems)
#         # tables.trigger('switches','switch,name',test,True)
#         _.tables.print('childClassItems','name')
#     def printStatus(self):
#         childItems = []
#         for ci in self.childItemRows:
#             if ci.active:
#                 active = 'True'
#             else:
#                 active = 'False'
#             value = ci.value
#             if ci.value == True:
#                 value = 'True'
#             elif ci.value == False:
#                 value = 'False'

#             childItems.append({'name':ci.name ,'active':active,'value': value})
#         _.tables.register('childClassItems',childItems)
#         _.tables.print('childClassItems','name,active,value')
#     def status(self,name,newStatus):
#         for i,ci in enumerate(self.childItemRows):
#             if ci.name == name:
#                 self.childItemRows[i].changeStatus(newStatus)
# _.showLine(item)
########################################################################################








	# _.switches.register('Add', '-a,-add')
	# _.switches.register('Find', '-f,-find')
	# _.switches.register('Coin', '-coin','q d n p')
	# _.switches.register('Label', '-st,-state','SC')
	# _.switches.register('Year', '-y,-year','1999')
	# _.switches.register('Type', '-type')
	# _.switches.register('Hashtag', '-t,-tag,-hashtag','bird mountain')
def confirmCoin():
	global coins
	def blank():
		print()
		print('q n d p quarters')
		newValue = input('What a coin: ')
		if len(newValue) > 0:
			_.switches.fieldSet('Coin','active',True)
			_.switches.fieldSet('Coin','value',newValue)
		else:
			print('Label Error')
			sys.exit()
	if not _.switches.isActive('Coin'):
		if len(coins) > 0:
			data = []
			i = 0
			for cur in coins['currency']:
				for dk in cur['data'].keys():
					data.append({'id': i, 'name': cur['type'], 'coin': dk})
					i += 1

			if len(data) == 0:
				blank()
			else:
				_.tables.register('Coin',data)
				_.tables.print('Coin','id,name,coin')
				print()
				chosenID = input('Choose a coin: ')
				if len(chosenID) > 0:
					try:
						_.switches.fieldSet('Coin','active',True)
						_.switches.fieldSet('Coin','value',data[int(chosenID)]['coin'])
						# _.switches.fieldSet('Currency','value',data[int(chosenID)]['name'])
					except Exception as e:
						_.switches.fieldSet('Coin','active',True)
						_.switches.fieldSet('Coin','value',chosenID.replace(' ','_'))
				else:
					print('Type error')
					sys.exit()
		else:
			blank()

	## END

def confirmLabel():
	if not _.switches.isActive('Label'):
		# print(_.switches.value('Type'))
		if _.switches.value('Type') == 'states':
			print()
			newValue = input('What state: ')
		else:
			print()
			newValue = input('What is the label: ')
		if len(newValue) > 0:
			_.switches.fieldSet('Label','active',True)
			_.switches.fieldSet('Label','value',newValue)
		else:
			print('Label Error')
			sys.exit()

def confirmType():
	global coins
	def blank():
		print()
		print('state')
		newValue = input('What a type: ')
		if len(newValue) > 0:
			_.switches.fieldSet('Type','active',True)
			_.switches.fieldSet('Type','value',newValue)
		else:
			print('Type Error')
			sys.exit()
	if not _.switches.isActive('Type'):
		if len(coins) > 0:
			data = []
			i = 0
			for cur in coins['currency']:
				for dk in cur['data'].keys():
					for tdk in cur['data'][dk].keys():
						# print({'id': i, 'name': cur['type'], 'coin': dk, 'type': tdk})
						data.append({'id': i, 'name': cur['type'], 'coin': dk, 'type': tdk})
						i += 1

			if len(data) == 0:
				blank()
			else:
				_.tables.register('type',data)
				_.tables.print('type','id,name,coin,type')
				print()
				chosenID = input('Choose a type: ')
				if len(chosenID) > 0:
					try:
						_.switches.fieldSet('Type','active',True)
						_.switches.fieldSet('Type','value',data[int(chosenID)]['type'])
						_.switches.fieldSet('Currency','value',data[int(chosenID)]['name'])
						_.switches.fieldSet('Coin','active',True)
						_.switches.fieldSet('Coin','value',data[int(chosenID)]['coin'])
					except Exception as e:
						_.switches.fieldSet('Type','active',True)
						_.switches.fieldSet('Type','value',chosenID.replace(' ','_'))
				else:
					print('Type error')
					sys.exit()
		else:
			blank()

	## END

def confirmYear():
	if not _.switches.isActive('Year'):
		print()
		year = input('Year: ')
		if len(year) > 0:
			_.switches.fieldSet('Year','active',True)
			_.switches.fieldSet('Year','value',year)
		else:
			print('Year error')
			sys.exit()

def confirmHashtag():
	if not _.switches.isActive('Hashtag'):
		print()
		tags = input('Hashtags: ')
		if len(tags) > 0:
			_.switches.fieldSet('Hashtag','active',True)
			_.switches.fieldSet('Hashtag','value',tags)
		else:
			print('Hashtag error')
			sys.exit()

def confirmVerbiage():
	if not _.switches.isActive('Verbiage'):
		print()
		print('What is written on the coin??')
		verbiage = input('Verbiage: ')
		if len(verbiage) > 0:
			_.switches.fieldSet('Verbiage','active',True)
			_.switches.fieldSet('Verbiage','value',verbiage)
		else:
			print('Verbiage error')
			sys.exit()

def addCategory():
	global coins
	global coinsFile

	confirmType()
	confirmCoin()
	confirmLabel()
	confirmYear()
	confirmHashtag()
	confirmVerbiage()

	alreadyExists = findItem(True)
	# print(alreadyExists)
	# print('eof')
	# sys.exit()

	if len(alreadyExists) > 0:
		pass
		print('Exists')
	else:
		theType = _.switches.value('Type')
		coin = _.switches.value('Coin')
		label = _.switches.value('Label')
		year = _.switches.value('Year')
		tags = _.switches.value('Hashtag')
		verbiage = _.switches.value('Verbiage')


		if _.switches.isActive('Value'):
			value = _.switches.value('Value')
		else:
			value = 0.25
		try:
			coins['currency'][0]
		except Exception as e:
			coins['currency'].append({ 'type': _.switches.value('Currency'), 'data': { coin : {} }})
		try:
			coins['currency'][0]['data'][coin]
		except Exception as e:
			coins['currency'][0]['data'][coin] = {}
		try:
			coins['currency'][0]['data'][coin][theType]
		except Exception as e:
			coins['currency'][0]['data'][coin][theType] = {'data':[], 'research':[], 'value': value}
		# for t in tags.split(','):1
		#     data['Hashtag'].append(t)

		
		data = {'label': label.upper(), 'year': year, 'hashtag': tags, 'verbiage': verbiage, 'coins':[]}
		coins['currency'][0]['data'][coin][theType]['data'].append(data)

		_.saveTable(coins,coinsFile)













def findItem(context=False):
	global coins
	result = []
	data = []
	# theType = _.switches.value('Type')
	# coin = _.switches.value('Coin')
	# label = _.switches.value('Label')
	# year = _.switches.value('Year')
	# tags = _.switches.value('Hashtag')
	# verbiage = _.switches.value('Verbiage')

	theType = _.switches.value('Type')
	coin = _.switches.value('Coin')
	print(type(theType),type(coin),_.switches.value('Year'))
	sys.exit()

	found = False
	if context:
			pass

	if _.switches.isActive('Label'):
		newValue = _.switches.value('Label')
	if not context:
		
		if _.switches.isActive('Label'):
			pass
		elif _.switches.isActive('Hashtag'):
			newValue = _.switches.value('Hashtag')
			newValue = newValue.replace(' ',',')
			_.switches.fieldSet('Plus','active',True)
			_.switches.fieldSet('Plus','value',newValue)
		elif _.switches.isActive('Verbiage'):
			newValue = _.switches.value('Verbiage')
			newValue = newValue.replace('  ',' ')
			newValue = newValue.replace('  ',' ')
			newValue = newValue.replace(' ',',')
			_.switches.fieldSet('Plus','active',True)
			_.switches.fieldSet('Plus','value',newValue)
		else:
			confirmHashtag()
			newValue = _.switches.value('Hashtag')
			newValue = newValue.replace(' ',',')
			_.switches.fieldSet('Plus','active',True)
			_.switches.fieldSet('Plus','value',newValue)




	if len(coins) > 0:
		i = 0

		# coins['currency'][0]['data'][coin][theType]['data'].append(data)
		# data = {'label': label.upper(), 'year': year, 'hashtag': tags, 'verbiage': verbiage, 'coins':[]}


		for cur in coins['currency']:
			for dk in cur['data'].keys():
				for tdk in cur['data'][dk].keys():
					for tdkx in cur['data'][dk][tdk].keys():
						try:
							for ii,tdkxy in enumerate(cur['data'][dk][tdk][tdkx]):
								if _.switches.isActive('Label'):
									if newValue == tdkxy['label']:
										data.append({'realID': ii, 'id': i, 'name': cur['type'], 'coin': dk, 'type': tdk, 'hashtag': tdkxy['hashtag'], 'verbiage': tdkxy['verbiage']})
								else:
									if _.showLine(tdkxy['hashtag']):
										data.append({'realID': ii, 'id': i, 'name': cur['type'], 'coin': dk, 'type': tdk, 'hashtag': tdkxy['hashtag'], 'verbiage': tdkxy['verbiage']})
										i += 1
						except Exception as e:
							pass
					i += 1
		# print(data)
	else:
		print('No Data')
		sys.exit()

	if len(data) == 1:
		result = data
	elif len(data) > 0:
		_.tables.register('Found',data)
		_.tables.print('Found','id,name,coin,type,hashtag,verbiage')

		chosenID = input('Choose an item: ')

		if len(chosenID) > 0:
			try:
				result = data[int(chosenID)]
			except Exception as e:
				print('Selected item error')
				sys.exit()
		else:
			print('Selected item error')
			sys.exit()
	# print(result)
	return result



def addCoin():
	global coins
	confirmYear()
	record = findItem()
	# print(record)
	if len(record) > 0:
		i = 0
		for curi,cur in enumerate(coins['currency']):
			for dk in coins['currency'][curi]['data'].keys():
				for tdk in coins['currency'][curi]['data'][dk].keys():
					for tdkx in coins['currency'][curi]['data'][dk][tdk].keys():
						if tdkx == 'data':
							for ii,tdkxy in enumerate(coins['currency'][curi]['data'][dk][tdk][tdkx]):
								# print(coins['currency'][curi]['data'][dk][tdk][tdkx][ii]['coins'])
								coins['currency'][curi]['data'][dk][tdk][tdkx][ii]['coins'].append(_.switches.value('Year'))
								i += 1
								# info = coins['currency'][curi]['data'][dk][tdk][tdkx][tdkxy]['label']
								
						# try:
						#     print((coins['currency'][curi]['data'][dk][tdk][tdkx]))
						#     pass
						# except Exception as e:
						#     pass
						# try:


						# except Exception as e:
						#     pass

		# print(i)
		if i == 1:
			_.saveTable(coins,coinsFile)
		else:
			print('Error:',i)


def action():
	global coins
	global coinsFile
	coins = _.getTable(coinsFile)

	if not _.switches.isActive('Currency'):
		_.switches.fieldSet('Currency','active',True)
		_.switches.fieldSet('Currency','value','MERICA')

	if len(coins) == 0:
		coins = { 'currency' : [] }

	if not _.switches.isActive('Add') and not _.switches.isActive('Find'):
		print('Switch issue')
		sys.exit()
	# print(_.switches.value('Coin'))
	else:
		if _.switches.value('Add') == 'both' or _.switches.value('Add') == 'category':
			addCategory()
		if _.switches.value('Add') == 'both' or _.switches.value('Add') == 'coin':
			addCoin()

coins = []
coinsFile = 'coins.json'
coins = _.getTable(coinsFile)
########################################################################################
if __name__ == '__main__':
	# pass
	action()
	# confirmType()
	# findItem()





