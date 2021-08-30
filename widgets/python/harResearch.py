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
	_.switches.register( 'JSON', '-json' )
	_.switches.register( 'URL', '-url', 'font' )
	_.switches.register( 'Field', '-field', 'encoding base64' )
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

def profile( data, field='text', parents=[], json=False, plus=False ):
	global research
	global spent
	global pipeData

	def sliceVar( var, newP ):
		# print(newP)
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
			np = sliceVar(parents, key)

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
						print( e )
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
						print( e )
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
				# print( key )

				if key == 'url' and _.switches.isActive('URL') and _.showLine( data[key], _.switches.value('URL') ):
					
					if _.showLine( data[key] ) and not data[key] in spent:
						spent.append(data[key])
						_.colorThis( data[key] , 'cyan' )

				if not plus and json and 'json' in data[key].lower():
					print()
					_.colorThis( data[key] , 'cyan' )
					# print(  )
			if plus and key == field and _.showLine( data[key] ):
				# print( 'found in text' )
				# print( research['url'] )
				# _.colorThis(  [len(data[key]),'char\t', ','.join(parents) ], 'yellow'  )
				if not research['url'] in research['payload']:
					if json:
						if 'json' in research['url'].lower():
							research['payload'].append( research['url'] )
					else:
						research['payload'].append( research['url'] )
					# if not json:
					# 	research['payload'].append( research['url'] )
					# else:
					# 	if 'json' in research['url'].lower():
					# 		research['payload'].append( research['url'] )
					
				

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
				print()
				_.colorThis( url, 'yellow' )
				print()
		if search and '"text":' in row and _.showLine(row):
			if not lastURL in research['payload']:
				if json:
					if 'json' in lastURL.lower():
						research['payload'].append( lastURL )

				else:
					research['payload'].append( lastURL )

	

def action():
	global pipeData
	load()
	# import pytest
	# for x in dir(pytest):
	# 	print(x)

	# sys.exit()

	global data
	global research
	# load()

	file = _.switches.values('harFile')[0]

	# _.colorThis( 'finish second secondApproach()' )
	approach_type = ''
	json = _.switches.isActive('JSON')
	plus = _.switches.isActive('Plus')

	try:
		data = _.getTable2( file )
		# data = getLargeTable( file )
		if _.switches.isActive('Plus'):
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
			print()
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
# 	global data
# 	data = _.getTable( 'table' )


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






