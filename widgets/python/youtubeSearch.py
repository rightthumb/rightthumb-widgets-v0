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
	_.switches.register( 'Search', '-search' )
	_.switches.register( 'Official', '-o,-off,-official' )
	_.switches.register( 'Song', '-song' )
	_.switches.register( 'Band', '-band' )
	_.switches.register( 'Offset', '-offset', '1' )
	_.switches.register( 'PrintTestStuff', '-test' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'youtubeSearch.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search YouTube',
	'categories': [
						'youtube',
						'internet',
						'research',
						'url',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						'type %tmpf2% | a.playlist',
						'',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'type %tmpf2% | p youtubeSearch -official -song',
						'',
						'type  %tmpf2% | p youtubeSearch -official -song +close',
						'',
						'type %tmpf2% | p youtubeSearch -official -song +close -offset 0 | p youtube -n',
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
# __.appRegPipe
########################################################################################
# START

from lxml import html
import requests
import cssselect
from urllib.parse import unquote

def getUrlList( url, obscure=False ):
	global printTestStuff
	# _.pr( 'omit:', omit )
	# _.pr( 'url:', url )
	# sys.exit()
	theList = []
	omitWords = [
					'v',
					'iii',
					'in',
					'day',
					'part',
					'two',
					'me',
					'episode',
					'ii',
					'a',
					'to',
					'pm',
					'and',
					'am',
					'of',
					'the'
	]
	newURL = url.replace(',','+').replace(' ','+')
	# _.pr(newURL)
	# brandNewURL = 'http://www.rightthumb.com/projects/widget/proxy.php?p=' + newURL.replace('&','[and]')
	# _.pr(newURL)
	# sys.exit()

	

	page = requests.get(newURL)
	tree = html.fromstring(page.content)
	tables = tree.cssselect('a')
	for t in tables:
		try:
			item = t.text_content()
		except Exception as e:
			item = ''
		# _.pr(item)
		if 'youtube' in item.lower():
			links = t.cssselect('a')
			link = str(links[0].attrib['href'])
			link = link.replace('/url?q=http:','http:')
			text = t.text_content()
			# _.pr(text)
			# _.pr()
			# _.pr(text)


			# pause = input('pause')
			shouldRun = False
			if obscure:
				shouldRun = True


			if _.showLine( text ):
				shouldRun = True
			if printTestStuff:
				_.pr( shouldRun, text )

			# _.pr( 'shouldRun:', shouldRun )
			if shouldRun:
				if 'youtube.com/watch' in link:
					theURL = link.replace('/url?q=','').split('/&sa=U')[0]
					# _.pr(theURL)
					theList.append({'name': text,'link': theURL})
	return theList



def action():
	global printTestStuff
	base = 'https://www.google.com/search?q=site%3Awww.youtube.com+'
	youtubeVideos = []
	# _.switches.fieldSet( 'Plus', 'active', True )
	if _.switches.isActive('Search'):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = [ ' '.join( _.switches.values('Search') ) ]
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			if len(row):
				if _.switches.isActive('Band'):
					row = _.switches.values('Band')[0] + ' ' + row
					# print(row)
					# sys.exit()
				row = row.replace( "'s", 's' )
				row = row.replace( "'S", 'S' )
				row = _str.stripNonAlphaNumaric( row, also='+_-' )


				_.switches.fieldSet( 'Plus', 'value', ','.join( row.split(' ') ) )
				_.switches.fieldSet( 'Plus', 'values', row.split(' ') )

				if _.switches.isActive('Official'):
					row += ' Official'

				if _.switches.isActive('Song'):
					row += ' Song'
				if printTestStuff:
					_.pr(  )
					_.pr(  )
					_.pr( row )
					_.pr(  )

				row = row.replace( ' ', '+' )
				records = getUrlList( base+row )
				if printTestStuff:
					_.pr(  )
				offset = 0
				if _.switches.isActive('Offset') and len(_.switches.value('Offset')):
					offset = int( _.switches.value('Offset') )
				try:
					result = unquote(records[offset]['link']).split('&')[0]
					_.pr( result )
				except Exception as e:
					pass
	#             youtubeVideos.append( unquote(records[0]['link']).split('&')[0] )

	# for url in youtubeVideos:
	#     _.pr( url )


printTestStuff = _.switches.isActive( 'PrintTestStuff' )

########################################################################################
if __name__ == '__main__':
	action()







