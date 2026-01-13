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


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register( 'Data', '-data' )
	_.switches.register( 'JSON', '-json' )
	_.switches.register( 'URL', '-url', 'font' )
	_.switches.register( 'Index', '-index' )
	_.switches.register( 'Fields', '-field,-fields', 'encoding base64' )
	_.switches.register( 'harFile', '-har,-f,-file','littlealchemy.com.har',  isRequired=True, description='harFile' )
	_.switches.register( 'Post', '-post', 'text https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png' )
	_.switches.register( 'Save', '-save', 'base64 file.png https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png' )

	# _.switches.register( 'Pre', '-pre', 'text https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png' )
	_.switches.register( 'Clean', '--c' )


	

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','harFile','Plus']

_.appInfo[focus()] = {
	'harFile': 'harResearch.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Research data in har file',
	'categories': [
						'har',
						'web',
						'tool',
						'research',
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
						'p harResearch -f littlealchemy.com.har -json',
						'p harResearch -f florida_health_temp.covid19_dashboard.har.json -json + hillsborough',
						'',
						'p harResearch -f codepen.io.har -field encoding base64',
						'p harResearch -f codepen.io.har -post mimeType https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png',
						'p harResearch -f codepen.io.har -post text https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png',
						'p harResearch -f codepen.io.har -save base64 chrome.png https://cdn0.iconfinder.com/data/icons/jfk/512/chrome-512.png',
						'',
						'p harResearch -f codepen.io.har -save text alchemy.js http://littlealchemy.com/js/alchemy.580.js',
						'',
						'',
						'p harResearch -f codepen.io.har -field encoding base64 + .png |  p harResearch -f codepen.io.har -save base64',
						'p harResearch -f codepen.io.har -field encoding base64 + .svg |  p harResearch -f codepen.io.har -save base64 2',
						'',
						'',
						'p harResearch -f www.google.com.har -field encoding base64 | p harResearch -f www.google.com.har -save base64',
						'p file -bin --c | p fileheader -noext -rename jpg png svg gif ico',
						'',
						_.hp('p harResearch -f curaleaf.com-08.har -url + dutchie'),
						_.hp('p harResearch -f curaleaf.com-08.har -fields text url'),
						_.hp('p harResearch -f curaleaf.com-08.har -data + mango'),
						_.hp('p harResearch -f curaleaf.com-08.har -data 1 + mango'),
						_.hp('p harResearch -f curaleaf.com-08.har -data ask + mango'),
						'',
						'',
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
	__.constructRegistration( _.appInfo[__.appReg]['harFile'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	# _.switches.trigger( 'harFile', _.myFileLocations )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	
	
	
	# _.defaultScriptTriggers()
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
# __.appRegPipe
########################################################################################
# START

import base64
__._last_val=''
__._last_url=''
__._last_urls=[]
__.val_data_i=0
__.val_data={}
__.val_data_url={}
__.val_data_info={}

def profile( data, field='text', parents=[], json=False, plus=False ):
	global research
	global spent
	global pipeData
	if data and key == 'url' and _.switches.isActive('URL') and not _.switches.value('URL'): _.pr(data[key])
	def sliceVar( var, newP ):
		# _.pr(newP)
		n = None
		if type(var) == list:
			n = []
			for x in var:
				n.append(x)

			n.append(str(newP))
		return n

	
	
	if type(data) == list:
		for i,row in enumerate(data):
			np = sliceVar(parents, i)
			profile( row, field, np, json, plus )
		try:
			pass
		except Exception as e:
			len(data)

	if type(data) == dict:
		for key in data.keys():
			last=__._last_val
			__._last_val=str(data[key])
			np = sliceVar(parents, key)
			# _.pr(data[key])
			if _.switches.isActive('Data'):
				if key == 'url': __._last_url=data[key]
				# if key == 'url': _.pr(data[key])
				if key == 'text' and last == 'application/json' and _.switches.isActive('Data'):
					omit_end='.js'
					valid=True
					for test5 in omit_end.split(' '):
						if __._last_url.endswith(test5): valid=False
					
					valid_scan='[({'

					valid2=False
					for test5 in list(valid_scan):
						for x in range(10):
							try:
								if data[key][x] == test5: valid2=True; break;
							except Exception as e: pass
					
					# valid2=True

					rank=data[key].count('[')+data[key].count('{')

					if valid and valid2 and rank >  __.setting('rank-threshold') and _.showLine(__._last_url) and _.showLine(data[key]):
						if not __._last_url in __._last_urls:
							__._last_urls.append(__._last_url)
							if rank:
								spread=len(data[key])/rank
							else:
								spread=0
							__.val_data_i+=1
							__.val_data[str(__.val_data_i)]=data[key]
							__.val_data_url[str(__.val_data_i)]=__._last_url
							report={
										'id': __.val_data_i,
										'rank': _.addComma(rank),
										'spread': _.addComma(spread),
										'size': _.addComma(len(data[key])),
										'flags': _.addComma(data[key].count('(')),
							}
							__.val_data_info[str(__.val_data_i)]=report
							_.pr(__._last_url,c='green')
							_.pr(report,pvs=True)

			if _.switches.isActive('Save') and key.lower() == 'text' and research['url'].lower() in pipeData:
				thePath = research['url'].split('/')
				p0 = thePath.pop()
				try:
					p1 = thePath.pop()
				except Exception as e:
					p1 = ''

				try:
					p2 = thePath.pop()
				except Exception as e:
					p2 = ''

				try:
					p3 = thePath.pop()
				except Exception as e:
					p3 = ''


				if len(_.switches.values('Save')) > 1 and _.switches.values('Save')[1] == '2':
					theFile = p1+'_'+p0
				elif len(_.switches.values('Save')) > 1 and _.switches.values('Save')[1] == '3':
					theFile = p2+'_'+p1+'_'+p0
				elif len(_.switches.values('Save')) > 1 and _.switches.values('Save')[1] == '4':
					theFile = p3+'_'+p2+'_'+p1+'_'+p0
				else:
					theFile = p0
				theFile = theFile.split('?')[0]
				theFile = theFile.replace(':','')
				
				if theFile in spent:
					temp = theFile.split('.')
					ext = temp.pop()
					tmpFile = '.'.join(temp)
					i=1
					while tmpFile+'_'+str(i)+'.'+ext in spent:
						i+=1
					theFile = tmpFile+'_'+str(i)+'.'+ext
				spent.append(theFile)

				if _.switches.values('Save')[0] == 'base64':
					try:
						_.saveBin( base64.urlsafe_b64decode(data[key]), theFile )
						_.colorThis( [ 'Saved:', theFile ], 'green' )
					except Exception as e:
						_.colorThis( [ 'Error:', theFile ], 'red' )
						_.pr( e )
						_.colorThis( [ 'Error:', theFile ], 'red' )
				elif _.switches.values('Save')[0] == 'text':
					try:
						_.saveText( data[key], theFile )
						try:
							if theFile.lower().endswith('.json'):
								tbl = _.getTable2(theFile)
								_.saveTable2(tbl,theFile)
						except Exception as e:
							pass


						_.colorThis( [ 'Saved:', theFile ], 'green' )
					except Exception as e:
						_.colorThis( [ 'Error:', theFile ], 'red' )
						_.pr( e )
						_.colorThis( [ 'Error:', theFile ], 'red' )

				
			if _.switches.isActive('Save') and len(_.switches.values('Save')) > 2 and research['url'].lower() == _.switches.values('Save')[2].lower() and key.lower() == 'text':
				if _.switches.values('Save')[0] == 'base64':
					_.saveBin( base64.urlsafe_b64decode(data[key]), _.switches.values('Save')[1] )
				elif _.switches.values('Save')[0] == 'text':
					_.saveText( data[key], _.switches.values('Save')[1] )

			if _.switches.isActive('Post') and research['url'].lower() == _.switches.values('Post')[1].lower() and key.lower() == _.switches.values('Post')[0].lower():
				
				if _.showLine( data[key] ) and not data[key] in spent:
					spent.append(data[key])
					_.colorThis( data[key] , 'cyan' )

			if _.switches.isActive('Field') and key.lower() == _.switches.values('Field')[0] and _.showLine( data[key], _.switches.values('Field')[1] ):
				
				if _.showLine( research['url'] ) and not research['url'] in spent:
					spent.append(research['url'])
					_.colorThis( research['url'] , 'cyan' )


			if key == 'url':
				research['url'] = data[key]
				# _.pr( key )
				if key == 'url' and _.switches.isActive('URL') and not _.switches.value('URL'):
					_.pr(data[key])
				elif key == 'url' and _.switches.isActive('URL') and _.showLine( data[key], _.switches.value('URL') ):
					# last
					if _.showLine( data[key] ) and not data[key] in spent:
						spent.append(data[key])
						_.pr()
						_.colorThis( data[key] , 'cyan' )

				if not plus and json and 'json' in data[key].lower():
					_.pr()
					_.colorThis( data[key] , 'cyan' )
					# _.pr(  )
			if plus and key == field and _.showLine( data[key] ):
				# _.pr( 'found in text' )
				# _.pr( research['url'] )
				# _.colorThis(  [len(data[key]),'char\t', ','.join(parents) ], 'yellow'  )
				if not research['url'] in research['payload']:
					if json:
						if 'json' in research['url'].lower():
							research['payload'].append( research['url'] )
					else:
						research['payload'].append( research['url'] )
					# if not json:
					#   research['payload'].append( research['url'] )
					# else:
					#   if 'json' in research['url'].lower():
					#       research['payload'].append( research['url'] )
					
				

			profile( data[key], field, np, json, plus )



def secondApproach():
	global data
	global research
	lastURL = ''
	json   = _.switches.isActive('JSON')
	search = _.switches.isActive('Plus')

	for row in data:
		if '"url":' in row:
			url = row.split('"')[3]
			lastURL = url
			if not search and json and 'json' in url.lower():
				_.pr()
				_.colorThis( url, 'yellow' )
				_.pr()
		if search and '"text":' in row and _.showLine(row):
			if not lastURL in research['payload']:
				if json:
					if 'json' in lastURL.lower():
						research['payload'].append( lastURL )

				else:
					research['payload'].append( lastURL )


# dic_spent = []
# def dict_generator(indict, pre=None):
#     pre = pre[:] if pre else []
#     if isinstance(indict, dict):
#         for key, value in indict.items():
#             if isinstance(value, dict):
#                 for d in dict_generator(value, pre + [key]):
#                     yield d
#             elif isinstance(value, list) or isinstance(value, tuple):
#                 for v in value:
#                     for d in dict_generator(v, pre + [key]):
#                         yield d
#             else:
#                 # yield pre + [key, value]
#                 if _.switches.isActive('Field'):
#                     for k in _.switches.values('Field'):
#                         if k.lower() == key:
#                             if not value in dic_spent:
#                                 dic_spent.append(value)
#                                 _.pr(value)
#                 yield pre + [key]

#     else:
#         # yield pre + [indict]
#         _.pr(pre)
#         yield pre 


def action():



	global pipeData
	load()
	# import pytest
	# for x in dir(pytest):
	#   _.pr(x)

	# sys.exit()

	global data
	global research
	# load()

	file = _.switches.values('harFile')[0]


	approach_type = ''
	json = _.switches.isActive('JSON')
	plus = _.switches.isActive('Plus')

	try:
		data = _.tableGet( file )

		if _.switches.isActive('Index'):
			_.switches.fieldSet( 'Long', 'active', True )
			spent_xXx=[]
			key_results=[]
			key_table=[]
			pass
			for x in _.dict_generator(data):
				pass

			for k in _.dict_generator_index:
				key_table.append({ 'path': k, 'cnt': _.dict_generator_index[k] })
			key_table2 = _.tables.returnSorted( 'data', 'a.cnt', key_table )
			_.tables.print( 'data', 'cnt,path' )
			return None
				

		if _.switches.isActive('Fields'):
			for x in _.dict_generator(data,fields=_.switches.values('Fields')):
				pass
			return None


		# data = getLargeTable( file )
		if _.switches.isActive('Data'):
			profile( data, json=json, plus=plus )
			if 'a' in _.switches.value('Data'):
				_.linePrint(c='cyan')
				for i in __.val_data:
					_.pr(str(__.val_data_info[i]).replace("'",''))
				_.linePrint(c='cyan')
				ask=input(' : ')
				ask=ask.replace(' ','')
				if ask:
					data=__.val_data[ask]
					_.pr(data)
					# simplejson=__.imp('simplejson')
					# data2=simplejson.loads(data)
					data2 = _.tableGet(data)
					_.pr(data2,pv=1)
					_.pr((__.val_data_url[ask]))



			return None
		elif _.switches.isActive('Plus'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('JSON'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('URL'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('Field'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('Pre'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('Post'):
			profile( data, json=json, plus=plus )
		elif _.switches.isActive('Save'):
			profile( data, json=json, plus=plus )
		approach_type = 'Approach: A'
	except Exception as e:
		data = _.getText( file )
		secondApproach()
		approach_type = 'Approach: B'
		if not _.switches.isActive('Clean'):
			_.colorThis( [ '\n\n', approach_type ] , 'red' )

	if not _.switches.isActive('Field'):
		for url in research['payload']:
			_.pr()
			_.colorThis( url , 'yellow' )
	return research['payload']

def load():
	global pipeData
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			pipeData.append( row.lower() )

# def load():
#   global data
#   data = _.getTable( 'table' )


# getTableBIG
__.setting('rank-threshold',5)
if _.switches.isActive('Data') and _.switches.value('Data') and _.switches.value('Data')[0] in '0123456789':
	__.setting('rank-threshold',int(_.switches.value('Data')))

research = {
				'url': '',
				'payload': [],
}
spent = []
data = []
pipeData = []
########################################################################################
if __name__ == '__main__':
	action()