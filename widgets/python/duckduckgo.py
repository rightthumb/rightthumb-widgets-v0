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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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

# _dirList = _.regImp( __.appReg, 'dirList' )
#     _dirList.switch( 'Files' )
#     _dirList.switch( 'Recursion' )
#     _dirList.switch( 'Binary' )
#     _dirList.switch( 'Path','D:\\Apps' )
#     files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#     fileBackup.switch( 'Input', filename )
#     fileBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register( 'Query', '-q,-query', isRequired=True )
	_.switches.register( 'Links', '-l,-links' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Force', '-force' )
	_.switches.register( 'Path', '-path' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'duckduckgo.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search the internet with the search engine duckduckgo',
	'categories': [
						'internet',
						'search',
						'search engine',
						'duckduckgo',
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
						'p duckduckgo -query love',
						'',
						'p duckduckgo  -q python + pro',
						'',
						'p duckduckgo  -q smell -l',
						'',
						'p duckduckgo  -q python + pro --c',
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

# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )



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
	_.switches.trigger( 'Files',_.myFileLocations )
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	
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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START

import urllib.request
import urllib.parse

def action():
	
	resultsLink = _v.duckDuckGo + _v.slash+'duckduckgo_' + _.switches.value('Query').replace( ',', '_' ) + '.json'
	data = _.getTable2( resultsLink )
	hasData = True

	dataFrom = 'archive'

	if data is None:
		hasData = False
	if hasData and not len( data ):
		hasData = False

	if _.switches.isActive('Force'):
		hasData = False

	if not hasData:

		dataFrom = 'live'

		url = 'https://api.duckduckgo.com/?q=' + urllib.parse.quote(  _.switches.value('Query').replace( ',', ' ' )  ) + '&format=json'

		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		header = {
					'User-Agent': user_agent,
					'Accept': 'application/json'
		}
		request = urllib.request.Request(url,headers=header)
		response = urllib.request.urlopen(request)
		html = response.read()

		_.saveText( html, resultsLink )

		data = _.getTable2( resultsLink )
		_.saveTable2( data, resultsLink )
		# _.printVar( data )


	if not _.switches.isActive('Clean'):
		_.pr()
		_.colorThis(   _.switches.value('Query').replace( ',', ' ' )   , 'green' )
		_.pr()
		_.pr()

	i = 0

	relevant = []


	for result  in data['RelatedTopics']:
		try:

			relevant.append({ 'text': result['Text'], 'link': result['FirstURL'],  })

		except Exception as e:
			try:
				for item in result['Topics']:
					relevant.append({ 'text': item['Text'], 'link': item['FirstURL'],  })
			except Exception as e:
				pass

	ix = 0
	for record in relevant:
		printSpace()
		if not _.switches.isActive('Plus'):

			_.colorThis(   [  record['text']  ]   , 'cyan' )
			if _.switches.isActive('Links'):
				_.colorThis(   [  record['link']  ]   , 'yellow' )

		else:
			if _.showLine( record['text'] ):
				ix+=1
				_.pr( _.colorPlus( record['text'], color='cyan' ) )
				if _.switches.isActive('Links'):
					_.colorThis(   [  record['link']  ]   , 'yellow' )
			
















	if False:

		for result  in data['RelatedTopics']:
			try:
				_.colorThis( result['Text'], 'cyan' )
				i+=1
				if not _.switches.isActive('NoLinks'):
					_.colorThis( result['FirstURL'], 'yellow' )
					_.pr()
				if not _.switches.isActive('Clean'):
					_.pr()
			except Exception as e:
				try:
					for item in result['Topics']:
						_.colorThis( item['Text'], 'cyan' )
						i+=1
						if not _.switches.isActive('NoLinks'):
							_.colorThis( item['FirstURL'], 'yellow' )        
							_.pr()
						if not _.switches.isActive('Clean'):
							_.pr()
				except Exception as e:
					_.printVar( result )


	i = len( relevant )
	# if len(_.switches.value('Clean')):
	if not _.switches.isActive('Clean'):
		notes = '\n'
		if not _.switches.isActive('Plus'):
			notes += _.colorThis( [  '', i  ], 'yellow', p=0 )
		else:
			notes += _.colorThis( [  '', ix ,'' ], 'yellow', p=0 )
			notes += 'of'
			notes += _.colorThis( [  '', i ,'' ], 'yellow', p=0 )
		notes += _.colorThis( [  ' (', dataFrom , ')' ], 'darkcyan', p=0 )
		_.pr( notes )

	if _.switches.isActive('Path'):
		_.colorThis( [  resultsLink  ], 'green' )



def printSpace():
	if not _.switches.isActive('Clean'):
		if _.switches.isActive('Links'):
			_.pr()
			_.pr()
		




########################################################################################
if __name__ == '__main__':
	action()