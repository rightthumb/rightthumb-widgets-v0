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
import simplejson as json
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

# _bm = _.regImp( __.appReg, 'bookmarks' )
	# index = _bm.imp.index()
# _dirList = _.regImp( __.appReg, 'dirList' )
#   _dirList.switch( 'Files' )
#   _dirList.switch( 'Recursion' )
#   _dirList.switch( 'Binary' )
#   _dirList.switch( 'Path','D:\\Apps' )
#   files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#   profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#   _blowfish.encrypt( infilepath, outfilepath, key )
#   _blowfish.decrypt( infilepath, outfilepath, key )
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
#   _file_folder.switch( 'Save,Clean' )
#   _file_folder.switch( 'Compair,Clean' )
#   _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#   _fileNameDate.imp.newName( filename )
#   _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#   fileBackup.switch( 'Input', filename )
#   fileBackup.switch( 'Flag', 'pre replaceText' )
#   recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#   _folderContent.switch( 'Silent' )
#   _folderContent.switch( 'Folder', _v.myAppsBatch )
#   _folderContent.switch( 'NoExtension' )

#   _folderContent.switch( 'Recursive' )

#   _folderContent.switch( 'Text' )
#   _folderContent.switch( 'Binary' )
#   _folderContent.switch( 'Label', 'App: ' )
#   _folderContent.switch( 'Prefix', ';t' )
#   files = _folderContent.do( 'action' )['files']
#   folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#   _tickets.switch( 'ReturnFiles' )
#   records = _tickets.do( 'records' )

##################################################

from lxml import html
import requests
# import cssselect
# import sqlite3
import cssselect
from bs4 import BeautifulSoup

##################################################


def appSwitches():
	_.switches.register( 'URL', '-u,-url', 'file.htm, https://lxml.de/tutorial.html', isRequired=True )



_.autoBackupData = True
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START



def extractID(text):
	global removeThis
	text = str(text)
	text = text.replace('\n','')
	text = text.replace('\r','')
	text = text.replace(' ','')
	before = len(text)
	for rt in removeThis:
		text = text.replace(rt,'')
	after = len(text)
	if before == after:
		text = ''
	return text


def getPage(url):
	global thisWebPage

	if thisWebPage is None:
	
		if url.startswith('http'):
			page = requests.get(url)
			thisWebPage = BeautifulSoup( page.content, 'html.parser' )

		else:

			f = open(url, 'r', encoding='UTF-8')
			file = f.read()
			file = file.encode('latin-1','ignore')
			file = file.decode('utf-8','ignore')
			thisWebPage = BeautifulSoup(file,"html.parser")

	return thisWebPage













def thinkOfTheChildren( obj, parentID ):
	global nextID
	global projectReport

	nextID += 1

	record = {
						'rID': nextID,
						'tag': None,
						'text': None,
						'id': None,
						'classes': [],
						'attributes_n': [],
						'attributes_v': [],
						'childIDs': [],
						'parentID': parentID,
						'parentIDs': [],
	}


	# for x in dir(obj):
	#     _.pr( x )
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr( obj.name )    
	# sys.exit()


	try:
		record['tag'] = obj.name
	except Exception as e:
		try:
			record['tag'] = obj.namespace
		except Exception as e:
			pass


	try:
		record['text'] = obj.text
	except Exception as e:
		pass

	try:
		record['id'] = obj.get('id')
	except Exception as e:
		pass


	if not record['id'] is None:
		projectReport['ids'].append( record['id'] )


	try:
		record['classes'] = obj.get('class')
	except Exception as e:
		pass

	# _.pr(  'classes', record['classes'] )



	if not record['classes'] is None:
		for thisClass in record['classes']:
			if not thisClass in projectReport['classes']:
				projectReport['classes'].append( thisClass )



	attr = None

	try:
		attr = dict( obj.attrs.items() )
	except Exception as e:
		try:
			attr = dict( obj.attrs.values() )
		except Exception as e:
			try:
				attr = list( obj.attrs.values() )
			except Exception as e:
				pass

	record['attributes_v'] = attr



	if not record['attributes_v'] is None:
		for name in record['attributes_v'].keys():
			values = record['attributes_v'][name]

			if type(values) == list:
				value = ' '.join( values )
			else:
				value = str(values)
			try:
				projectReport['indexes'][name]['IDs'].append( record['rID'] )
			except Exception as e:
				projectReport['indexes'][name] = {
													'IDs': [],
													'values': {},
				}
				projectReport['indexes'][name]['IDs'].append( record['rID'] )
				projectReport['indexes'][name]['values'][value] = []
				projectReport['indexes'][name]['values'][value].append( record['rID'] )



			if type(values) == str:
				values = [values]



			for value in values:

				try:
					if not record['rID'] in projectReport['indexes'][name]['values'][value]:
						projectReport['indexes'][name]['values'][value].append( record['rID'] )
				except Exception as e:
					projectReport['indexes'][name]['values'][value] = []
					projectReport['indexes'][name]['values'][value].append( record['rID'] )

			record['attributes_n'].append( name )
			if not name == 'id' and not name == 'class' and not name in projectReport['attributes']:
				projectReport['attributes'].append( name )




	# _.pr( 'attr:', attr )

	pass

	try:
		for ch in obj.children:
			record_child = thinkOfTheChildren( ch, record['rID'] )
			record['childIDs'].append( record_child['rID'] )
	except Exception as e:
		pass

	projectReport['records'][  record['rID']  ] = record

	return record








def action():
	global thisWebPage
	global projectReport
	load()


	obj = thisWebPage.find("body")
	parentID = None

	thinkOfTheChildren( obj, parentID )




	for rID in projectReport['records'].keys():
		record = projectReport['records'][rID]

		parentList = []
		found = True
		theParent = rID

		# theParent = projectReport['records'][rID]['parentID']
		# if not theParent is None:
		#     parentList.append( theParent )

		while not theParent is None:
			theParent = projectReport['records'][theParent]['parentID']
			if not theParent is None:
				parentList.append( theParent )
				# _.pr( rID, theParent )



		projectReport['records'][rID]['parentIDs'] = parentList

		projectReport['indexes']






					# var parentList = [];
					# var theParent = window.hackData.records[ keys[i] ].parentID;
					# if ( typeof theParent === 'number' ) { parentList.push( theParent ); }
					# while ( typeof theParent === 'number' ) {
					#     theParent = window.hackData.records[ theParent ].parentID;
					#     // console.log( 'theParent:', theParent );
					#     if ( typeof theParent === 'number' ) { parentList.push( theParent ); }
					# }



	# _.printVar1( projectReport )
	_.saveTable( projectReport, 'auditHTML3.json', s=1)

	# try:
	# except Exception as e:
	#     pass





def load():
	global thisWebPage
	global projectReport
	thisWebPage = getPage( _.switches.values('URL')[0] )
	projectReport = {
						'epoch': time.time(),
						'title': None,
						'ids': [],
						'classes': [],
						'attributes': [],
						'records': {},
						'indexes': {},
	}
	try:
		projectReport['title'] = thisWebPage.title.string
	except Exception as e:
		pass



projectReport = {}
thisWebPage = None
nextID = -1
########################################################################################
if __name__ == '__main__':
	action()






