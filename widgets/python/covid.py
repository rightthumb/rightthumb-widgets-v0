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

import os
import sys
import time
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )


import _rightThumb._base3c as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str



	# profile = _profile.records.audit( 'name', asset )
##################################################

def appSwitches():
	pass
	_.switches.register( 'Live', '-live' )


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'covid.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Covid-19 realtime Florida statistics report',
	'categories': [
						'report',
						'research',
						'covid',
						'covid 19',
						'covid-19',
						'covid19',
						'virus',
						'health',
						'safety',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p covid ',
						'p covid -live',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],

	}

_.appData[focus()] = {
	'start': __.startTime,
	'uuid': '',
	'audit': [],
	'pipe': False,
	'data': {
				'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
				'table': {'sent': [], 'received': [] }, 
	},
	}



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


# from operator import itemgetter
import requests
# import webbrowser
# import datetime
# import arrow
# import pickle

def formatData( result ):
	try:
		result = str(result,'iso-8859-1')
	except Exception as e:
		pass
		try:
			result = str(result,'utf-8')
		except Exception as e:
			try:
				result = str(result,'iso-8859-1')
			except Exception as e:
				result = result.encode('utf-8')
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			pass
	return result
		

def cleanupString0( string ):
	string = formatData( string )
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')
	return string


def sliceVar( var, newP ):
	# print(newP)
	n = None
	if type(var) == list:
		n = []
		for x in var:
			n.append(x)

		n.append(str(newP))
	return n


def listAllData( data ):
	allTheData = []
	if type(data) == list:
		for i,row in enumerate(data):
			np = sliceVar(parents, i)
			theProfile = profile( row )
		try:
			pass
		except Exception as e:
			len(data)
	elif type(data) == dict:
		for key in data.keys():
			theProfile = profile( data[key], field, search, theProfile, np )
	else:
		allTheData.append( str(data) )



def profile( data, field, search, theProfile=[], parents=[] ):
	global lastURLFound
	global lastURL
	if type(data) == list:
		# print( ','.join(parents), '\tlen', len(data) )
		for i,row in enumerate(data):
			np = sliceVar(parents, i)
			theProfile = profile( row, field, search, theProfile, np )
		try:
			pass
		except Exception as e:
			len(data)
	if type(data) == dict:
		for key in data.keys():
			# print( 'asdf', key )
			np = sliceVar(parents, key)
			# print( ','.join(parents), '\tkey', key )
			if key == 'url':
				lastURL = data[key]
			if key == field and data[key] == search or search in str(data[key]):
				pass
				print()
				_.colorThis(  [len(data[key]),'\t', ','.join(parents), '\tkey', key], 'yellow'  )
				if not lastURL == lastURLFound:
					print( lastURL )
				lastURLFound = lastURL
				# pause=input('pause: ')
				# print( parents )
				# print( data[key] )

				# sys.exit()
			theProfile = profile( data[key], field, search, theProfile, np )
	
def action():
	print()
	if _.switches.isActive('Live'):

		shouldRun = True
		if shouldRun:
			# url = 'https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/arcgis/rest/services/Florida_COVID19_Cases/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&maxAllowableOffset=1222&geometry=%7B%22xmin%22%3A-9392582.035684975%2C%22ymin%22%3A3130860.678565018%2C%22xmax%22%3A-8766409.899972979%2C%22ymax%22%3A3757032.814277012%2C%22spatialReference%22%3A%7B%22wkid%22%3A102100%2C%22latestWkid%22%3A3857%7D%7D&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100&resultType=tile'
			url = 'https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/arcgis/rest/services/Florida_COVID19_Cases/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=County_1%20asc&resultOffset=0&resultRecordCount=68&cacheHint=true'
			page = requests.get(url)
			data = str(page.content,'iso-8859-1')
			# data = formatData(page.content)
			_.saveText( data, _v.myTables + _v.slash+'floridahealthcovid19_data.json' )
			florida = _.getTable( 'floridahealthcovid19_data.json' )


		shouldRun = True
		if shouldRun:
			url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?f=json&where=Country_Region%3D%27US%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
			page = requests.get(url)
			data = str(page.content,'iso-8859-1')
			# data = formatData(page.content)
			_.saveText( data, _v.myTables + _v.slash+'floridahealthcovid19_data.json' )
			data = _.getTable( 'floridahealthcovid19_data.json' )
			data = str( data['features'][0]['attributes']['value'] )
			florida['USA_Cases'] = data


		shouldRun = True
		if shouldRun:
			url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/0/query?f=json&where=Country_Region%3D%27US%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
			page = requests.get(url)
			data = str(page.content,'iso-8859-1')
			# data = formatData(page.content)
			_.saveText( data, _v.myTables + _v.slash+'floridahealthcovid19_data.json' )
			data = _.getTable( 'floridahealthcovid19_data.json' )
			data = str( data['features'][0]['attributes']['value'] )
			florida['USA_Deaths'] = data


		shouldRun = True
		if shouldRun:
			url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
			page = requests.get(url)
			data = str(page.content,'iso-8859-1')
			# data = formatData(page.content)
			_.saveText( data, _v.myTables + _v.slash+'floridahealthcovid19_data.json' )
			data = _.getTable( 'floridahealthcovid19_data.json' )
			data = str( data['features'][0]['attributes']['value'] )
			florida['Global_Cases'] = data


		shouldRun = True
		if shouldRun:
			url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true'
			page = requests.get(url)
			data = str(page.content,'iso-8859-1')
			# data = formatData(page.content)
			_.saveText( data, _v.myTables + _v.slash+'floridahealthcovid19_data.json' )
			data = _.getTable( 'floridahealthcovid19_data.json' )
			data = str( data['features'][0]['attributes']['value'] )
			florida['Global_Deaths'] = data



		
		# print( 'test:', test )
		# _.printVarSimple( florida )
		_.saveTable( florida, 'global_covid19.json' )
		data = florida
		# sys.exit()
		# print(data)
	else:
		data = _.getTable( 'global_covid19.json' )

	# _.printVarSimple( data )
	# return False
	# file = 'floridahealthcovid19_data_temp.json'
	# data = _.getTable2( file )
	
	# USA_Cases USA_Deaths Global_Cases Global_Deaths
	print()
	_.colorThis( [  'Global Cases:', _.addComma(data['Global_Cases'])  ], 'yellow' )
	_.colorThis( [  'Global Deaths:', _.addComma(data['Global_Deaths'])  ], 'red' )
	print()
	print()
	_.colorThis( [  'USA Cases:', _.addComma(data['USA_Cases'])  ], 'yellow' )
	_.colorThis( [  'USA Deaths:', _.addComma(data['USA_Deaths'])  ], 'red' )
	print()
	print()

	_.colorThis( [  'Florida in depth report by county:'  ], 'yellow' )
	records = []
	# print(data['features'])
	for i,record in enumerate(data['features']):
		records.append( record['attributes'] )
		# if not i:
		#     for x in record.keys():
		#         print(x)
		# print( record )

	# profile( data, 'text', 'Hillsborough' )


	# for i,record in enumerate( records ):
	#     if not i:
	#         for x in record.keys():
	#             print(x)

	# for x in data[]
	records = _.tables.returnSorted( 'data', 'd.CasesAll', records )
	highest = records[0]['CasesAll']
	total = 0
	Hillsborough = None
	for i,record in enumerate(records):
		if  'Hillsborough' in record['County_1']:
			Hillsborough = i
		total += int(records[i]['CasesAll'])
	for i,record in enumerate(records):
		records[i]['state_rank'] = i+1
		try:
			records[i]['state_percent'] = _.percentageDiffInt( int(records[i]['CasesAll']) , total )
			records[i]['state_max'] = _.percentageDiffInt( int(records[i]['CasesAll']), highest )
		except Exception as e:
			records[i]['state_percent'] = 0
			records[i]['state_max'] = 0

	_.tables.register( 'data', records )
	_.tables.fieldProfileSet('data','state_rank','alignment','right')
	_.tables.print( 'data', 'state_rank,County_1,CasesAll,state_percent,state_max' )

	print( len(records[0].keys()), 'Fields' )
	print()
 
	above = []
	for record in records:
		for x in record.keys():
			try:
				if int(record[x]) > int(record['CasesAll']):
					above.append(x)
					
			except Exception as e:
				pass
	below = []
	above.append('state_percent')
	above.append('state_max')
	for x in records[0].keys():
		if not x in above:
			try:
				if int(record[x]) == int(record['CasesAll']):
					below.append( x )

				if int(record[x]) < int(record['CasesAll']):
					below.append( x )
			except Exception as e:
				pass
	i = Hillsborough
	autoCat( records[i], below )
	return False


	for x in below:
		print( records[i][x], '\t' ,x )
	print( '\nRelevant Fields:', len(below) )
	# _.printTest( records[4] )

def autoCat( record, fields, totalField='CasesAll' ):
	color = 0
	sections = {}
	colors = 'green purple cyan yellow red'

	# for x in fields:
	#     if 'dea' in x.lower():
	#         print( x )


	groups = [ 'Age', 'ED', 'Hosp' ]
	# fields = []
	sections = {}
	for xx in fields:
		# print(xx)
		for x in xx.split('_'):
			if x in groups:
				# print(x)
				try:
					sections[x].append(xx)
				except Exception as e:
					sections[x] = []
					sections[x].append(xx)

	for xx in sections.keys():
		print()
		total = 0
		for x in sections[xx]:
			_.colorThis( [ record[x], '\t', x ], colors.split(' ')[color] )
			# print( record[x], '\t', x )
		color += 1
	print()
	_.colorThis( [ record['C_Men'], '\t', 'C_Men' ], colors.split(' ')[color] )
	_.colorThis( [ record['C_Women'], '\t', 'C_Women' ], colors.split(' ')[color] )
	color += 1
	print()
	_.colorThis( [ record['Deaths'], '\t', 'Deaths' ], 'red' )
	
	

	if False:
		for xx in fields:
			for x in xx.split('_'):
				try:
					sections[x].append(xx)
				except Exception as e:
					sections[x] = []
					sections[x].append(xx)

		for xx in sections.keys():
			total = 0
			for x in sections[xx]:
				total += int(record[x])
			if total == int(record[totalField]):
				pass
				if not len(sections[xx]) == 1:
					print( xx )
			# print( total, xx )
		print()

	# _.colorThis( 'asdf', 'asdf' )

def action10():
	allTheData = []

lastURLFound = ''
lastURL = ''
allTheData = []
def action9():
	file = 'florida_health_temp.covid19_dashboard.har.json'
	data = _.getTable2( file )
	profile( data, 'text', 'Hillsborough' )
	# print( data['text'] )

def action8():
	file = 'florida_health_temp.covid19_dashboard.har.json'
	file2 = 'florida_health_temp.covid19_dashboard.har_PROFILE_.json'
	data = _.getTable2( file )
	profile = _profile.records.audit( 'name', data )
	_.saveTable2( profile, file2 )
	# _.printVarSimple( profile )
def action7():
	file = 'floridahealthcovid19_data_temp.json'
	data = _.getTable2( file )
	_.saveTable2( data, file )
def action6():
	# url = 'https://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429'
	url = 'https://fdoh.maps.arcgis.com/apps/opsdashboard/index.html#/8d0de33f260d444c852a615dc7837c86'
	_browser.imp.project.open( url )
	data = _browser.imp.project.code()
	while not 'exit' in input('pause: ').lower():
		print( data )
		data = data.replace( '"', _.colorThis( '"', 'bold', p=0 ) )
		data = data.replace( '.js', _.colorThis( '.js', 'yellow', p=0 ) )
		if 'frame' in data.lower():

			if 'frame' in data:
				print( data.replace( 'frame', _.colorThis( 'frame', 'green', p=0 ) ) )
			else:
				print( data.lower().replace( 'frame', _.colorThis( 'frame', 'green', p=0 ) ) )
			_.colorThis( ' ** has frames **', 'green' )
		else:
			print( data )
			_.colorThis( ' ** has NO frames **', 'red' )
			
	_browser.imp.project.close()



def action5():
	file = 'florida_health_temp.covid19_dashboard.har.json'
	data = _.getText( file, raw=True, clean=1 )
	for i, quote in enumerate(  data.split('"')  ):
		if (i % 2) == 0:
			pass
		else:
			if quote.endswith('.js'):
				pass
				# print( quote )
			else:
				pass
				find = [  'http', '/', '../'  ]
				shouldPrint = False
				for test in find:
					if quote.startswith(test):
						shouldPrint = True
				if shouldPrint:
					print( quote )
				# print( quote )
def action4():
	file = 'florida_health_temp.htm'
	data = _.getText( file, raw=True, clean=1 )
	for xx in data.split('<'):
		tag = xx.split('>')[0]
		# print( tag )
		tag = tag.replace( "'", '"' )
		quotes = tag.split('"')
		for i, quote in enumerate(quotes):
			if (i % 2) == 0:
				pass
			else:
				print( quote )

	# print( data )


def action3():
	page = requests.get('https://experience.arcgis.com/experience/96dd742462124fa0b38ddedb9b25e429')
	data = formatData(  page.content  )
	file = 'florida_health_temp.htm'
	_.saveText( data, file )
	print( file )
def action2():
	pass
	# global data
	# load()
	page = requests.get('https://floridahealthcovid19.gov/')
	tree = html.fromstring(page.content)
	tables = tree.cssselect('.stat--box h2')
	for i,t in enumerate(tables):
		if i == 2:
			print(t.text_content())
		try:
			item = t.text_content()
		except Exception as e:
			item = ''
		if 'imdb' in item.lower():
			links = t.cssselect('a')
			link = str(links[0].attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			# print(text)
			print()
			print(text)



# def load():
#     global data
#     data = _.getTable( 'table' )


# data = []
########################################################################################
if __name__ == '__main__':
	action()






