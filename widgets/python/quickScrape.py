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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()

##################################################

import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword('string')
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
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
	# _filePathPatterns.switch( 'Files', _.switches.value('Files') )
	# folderReport = _filePathPatterns.action()

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register( 'ReportAll', '-all' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


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


_.appInfo[focus()] = {
	'file': 'quickScrape.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Quick Scrape',
	'categories': [
						'quick',
						'scrape',
						'web',
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
						'p quickScrape',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
# _.setPipeData( os.listdir(os.getcwd()), focus() )
# _.showLine(item)
#     if os.path.isdir(row):
#     if os.path.isfile(row):
# __.appRegPipe
########################################################################################
# START


def ask_question( field, label, validateionRule=False ):


	_.pr()
	theEnd = ''
	if not type(validateionRule) == bool:
		if validateionRule == 'yn_y':
			theEnd += '(y)'
		if validateionRule == 'yn_n':
			theEnd += '(n)'
		if validateionRule == 'notBlankText':
			theEnd += '*'
		if validateionRule == 'selector':
			theEnd += '*'
	theEnd += ' '
	data = input( label+theEnd )


	shouldClean = True
	if type(validateionRule) == str:
		for x in [ 'password' ]:
			if x == validateionRule:
				shouldClean = False


	if shouldClean:
		# _.pr(data)
		data = _str.replaceDuplicate( data, ' ' )
		data = _str.cleanBE( data, ' ' )


	# _.pr(data)
	result = data
	if not type(validateionRule) == bool:
		result = validateask_question( field, validateionRule, data )
	else:
		result = data
	if type(validateionRule) == bool:
		display = result
	else:
		if 'yn_' in validateionRule:
			if result:
				display = 'yes'
			else:
				display = 'no'
		else:
			display = result
	# _.pr(data)
	_.pr( display )

	
	return result


def validateask_question( field, what, data ):


	if what == 'project_type':
		# _.pr( field, what, data )
		# sys.exit()
		if 'f' in data.lower():
			result = 'front_end'
		else:
			result = 'direct'

	elif what == 'selector_or_function':
		if 'f' in data.lower():
			result = 'function'
		else:
			result = 'selector'

	elif what == 'yn_n':
		result = False
		test = [ 't', 'y' ]
		for x in test:
			if x in data.lower():
				result = True

	elif what == 'yn_y':
		result = True
		test = [ 'n', 'f' ]
		for x in test:
			if x in data.lower():
				result = False

	elif what == 'yn_o':
		result = 'only'
		if 'o' in data.lower():
			result = 'only'
		else:
			for x in [ 'n', 'f' ]:
				if data.lower().startswith(x):
					result = 'no'
			for x in [ 'y', 't' ]:
				if data.lower().startswith(x):
					result = 'yes'

	elif what == 'url':
		if data.lower() == 'n':
			result = False
		elif data.lower() == 'f':
			result = False
		elif not 'http' in data.lower():
			_.pr( 'Error: bad url' )
			result = validateask_question( field, what, ask_question( field, 'url:' ) )
		else:
			result = data

	elif what == 'notBlankText':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			result = data

	elif what == 'textFalse':
		if 'false' in data.lower():
			result = False
		else:
			if not len(data):
				result = False
			else:
				result = data


	elif what == 'password':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			if data.endswith('='):
				result = data
			else:
				result = _blowfish.encrypt( data )

	elif what == 'selector':
		if not len(data):
			_.pr( 'Error: cannot be blank' )
			result = validateask_question( field, what, ask_question( field, field2Label(field) ) )
		else:
			result = data

	elif what == 'this,item,all':
		if not len(data):
			result = 'all'
		else:
			if data.lower().startswith('a'):
				result = 'all'
			elif data.lower().startswith('i'):
				result = 'item'
			elif data.lower().startswith('t'):
				result = 'this'
			else:
				result = 'all'

	elif what == 'this,item,all-this':
		if not len(data):
			result = 'this'
		else:
			if data.lower().startswith('a'):
				result = 'all'
			elif data.lower().startswith('i'):
				result = 'item'
			elif data.lower().startswith('t'):
				result = 'this'
			else:
				result = 'this'


	elif what == 'single,list,auto':
		if not len(data):
			result = 'auto'
		else:
			if data.lower().startswith('a'):
				result = 'auto'
			elif data.lower().startswith('s'):
				result = 'single'
			elif data.lower().startswith('l'):
				result = 'list'
			else:
				result = 'auto'

	elif what == 'single,list,dic,list_dic,auto':
		if not len(data):
			result = 'auto'
		else:
			if 'l' in data.lower() and 'd' in data.lower():
				result = 'list_dic'
			elif data.lower().startswith('a'):
				result = 'auto'
			elif data.lower().startswith('s'):
				result = 'single'
			elif data.lower().startswith('l'):
				result = 'list'
			elif data.lower().startswith('d'):
				result = 'dic'
			else:
				result = 'auto'

	else:
		_.pr( 'Error: validateAsk' )
		sys.exit()

	return result


def action():
	global config
	masterData = _.getTable( 'quickScrape.json' )
	# config['description'] = ask_question( 'description', 'Description:' )
	config['url'] = ask_question( 'url', 'URL:' )
	config['injectjQuery'] = ask_question( 'inject_jQuery', 'inject jQuery:', 'yn_y' )




	code = _.getText( _v.myAppsJs + _v.slash+'quickScrape.js' )

	config['selector'] = ask_question( 'selector', 'selector:', 'selector' )
	_.pr()
	_.pr( 'dog==.media-heading;personality==[id^=\'breed-personality\']' )
	config['child_selectors'] = ask_question( 'child_selectors', 'child selector:' )

	config['hasNext'] = ask_question( 'has_next', 'next button:', 'yn_n' )
	if config['hasNext']:
		config['next_selector'] = ask_question( 'next_selector', 'next selector:' )
		
		config['next_selector_specific'] = ask_question( 'next_selector_specific', 'is selector specific:', 'yn_y' )
		if not config['next_selector_specific']:
			config['next_selector_isLink'] = ask_question( 'next_selector_isLink', 'is selector link:', 'yn_y' )



	# if config['hasNext']:

	_browser.imp.project.open( config['url'] )
	pause=input('pause')
	isDone = False
	while not isDone:
		isLoaded = ''
		while not isLoaded == 'complete':
			isLoaded = _browser.imp.project.injectReturn( 'document.readyState' )
			time.sleep( 5 )




		data = []
		if config['injectjQuery']:
			_browser.imp.project.jqueryInject()
		_browser.imp.project.inject( code )

		if len( config['child_selectors'] ):
			data =_browser.imp.project.injectReturn( 'window.acquirePayload("'+config['selector']+'", "'+config['child_selectors']+'")' )
		else:
			data =_browser.imp.project.injectReturn( 'window.acquirePayload("'+config['selector']+'")' )

		

		if len(data):
			data = cleanData( data )
			fields = data[0].keys()
			_.tables.register( 'data', data )

			if 'Personality' in fields:
				try:
					_.tables.print( 'data', 'data,Personality' )
				except Exception as e:
					pass
			else:
				try:
					_.tables.print( 'data', 'data' )
				except Exception as e:
					pass

			if _.switches.isActive( 'ReportAll' ):
				_.pr()
				_.pr()
				try:
					_.tables.print( 'data', ','.join( fields ) )
				except Exception as e:
					pass
			for record in data:
				masterData.append( record )
			_.saveTable( masterData, 'quickScrape.json' )
			_.printBold( 'Saved' )

		if not config['hasNext']:
			isDone = True
		else:
			if not len(config['next_selector']):
				isDone = True
				_.pr( 'Error: missing selector for next' )
			else:
				if config['next_selector_specific']:
					nextFound =_browser.imp.project.injectReturn( 'return window.clickNext_exists("'+config['next_selector']+'");' )
					if nextFound:
						_browser.imp.project.inject( 'window.clickNext("'+config['next_selector']+'")' )
					if not nextFound:
						isDone = True
				else:
					if config['next_selector_isLink']:
						# _.pr( config['next_selector'] )
						# _.pr( 'window.findNextLink_exists("'+config['next_selector']+'")' )
						_.pr()
						_.pr()
						_.pr()
						nextFound =_browser.imp.project.injectReturn( 'return window.findNextLink_exists("'+config['next_selector']+'");' )
						# nextFound = True
						# _.pr( 'nextFound:', nextFound )
						# nextFound = True
						if nextFound:
							# pause = input('pause')
							_browser.imp.project.inject( 'window.findNextLink("'+config['next_selector']+'");' )
							# pause = input('pause')
						if not nextFound:
							isDone = True

	_browser.imp.project.close()
# window.findNextLink('.idog-result-info-line a')
def cleanData( data ):
	fields = []
	newFields = []
	for record in data:
		for key in record.keys():
			if not key in fields:
				fields.append( key )
	for i,record in enumerate(data):
		for key in fields:
			if not key in record.keys():
				record[key] = ''

		for key in record.keys():
			if ' ' in key:
				data[i][ key.replace( ' ', '_' ) ] = record[key]
				del data[i][key]

		

		for key in record.keys():
			if not key in newFields:
				newFields.append( key )
			data[i][key] = str(record[key])
			# _.pr( key, record[key] )
			# _.pr( type( record[key] ), key )
	return data

# 'li.media', 

config = {}
########################################################################################
if __name__ == '__main__':
	action()



# https://bigd.big.ac.cn/idog/breed/getAllBreed.action
# n
# li.media

# y
# .idog-result-info-line a
# n
# y






