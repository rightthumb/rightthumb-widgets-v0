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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
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
						'p thisApp -file file.txt',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [
					# 'this',
					# 'app',
	],
	'notes': [
					# {},
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START

from operator import itemgetter
from lxml import html
import requests
import cssselect


def getIdFromUrl(url):
	if not 'imdb.com' in url:
		return None
	else:
		urls = url.split('/')
		for x in urls:
			if x.startswith('tt'):
				return x

		return None


def google(search):
	global index

	imdbID = None
	try:
		imdbID = index['searches'][ search ]
	except Exception as e:
		pass
	if not imdbID is None:
		return imdbID

	url = 'https://www.google.com/search?q=imdb+'
	newURL = url + _str.replaceAll(_str.replaceAll(search,',','+'),' ','+')
	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	# tables = tree.cssselect('.r')
	tables = tree.cssselect('a')
	result = ''
	for t in tables:
		try:
			item = t.text_content()
		except Exception as e:
			item = ''
		# _.pr(item)
		if 'imdb' in item.lower():
			# links = t.cssselect('a')
			link = str(t.attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			###################################################################################################
			# _.pr(item,link)

			if '/title/' in link:
				imdbID = getIdFromUrl( link )
				if not imdbID is None:
					index['searches'][ search ] = imdbID
					index['imdb'][ imdbID ] = search
					_.saveTableDB( index, 'imdb-search.index' )
					return imdbID
	return None


						


def action():
	global records
	global index
	load()


	for i,record in enumerate(records['data']):
		if 'movie' in record.keys() and type(record['movie']) == list:
			# _.pr( record['movie'] )
			imdbID = None
			try:
				imdbID = index['searches'][ record['movie'][0]+' '+record['movie'][1] ]
			except Exception as e:
				pass
			if imdbID is None:
				try:
					imdbID = index['searches'][ record['movie'][1]+' '+record['movie'][0] ]
				except Exception as e:
					pass
			if imdbID is None:
				try:
					imdbID = index['searches'][ record['movie'][1] ]
				except Exception as e:
					pass
			if imdbID is None:
				for movie in index['searches'].keys():
					if record['movie'][0] in movie and record['movie'][1].lower() in  movie.lower():
						imdbID = index['searches'][movie]
			if imdbID is None:
				testA = record['movie'][0]+' '+record['movie'][1]
				testB = ''
				for x in testA:
					if x in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
						testB += x
				testB = _str.replaceDuplicate( testB, ' ' )
				testB = _str.cleanBE( testB, ' ' )
				testB = testB.lower()

				for movie in index['searches'].keys():
					found = True
					for word in testB.split(' '):
						if not word in movie:
							found = False
					if found:
						imdbID = index['searches'][movie]


			if not imdbID is None:
				_.pr( imdbID, record['movie'][0]+' '+record['movie'][1], _.colorThis( index['imdb'][imdbID], 'green', p=0 ) )
			else:
				imdbID = google( record['movie'][0]+' '+record['movie'][1] )
				if not imdbID is None:
					_.pr( imdbID,     record['movie'][0]+' '+record['movie'][1], _.colorThis( index['imdb'][imdbID], 'green', p=0 ) )

				else:
					_.colorThis( record['movie'], 'red' )

def load():
	global records
	global index
	records = _.getTableDB( 'movie.cache' )
	index = _.getTableDB('imdb-search.index')
	# _.pr(index)
	# sys.exit()
	#             _.pr( index.keys() )
	#             _.pr( index['searches'].keys() )

records = []
index = {}

# harry potter
# 2017 X Men Logan


########################################################################################
if __name__ == '__main__':
	action()






