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
# import _rightThumb._encryptString as _blowfish
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
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

##################################################

from lxml import html
import requests
import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register('Prefix', '-pre,-prefix','What is ')
	_.switches.register('Suffix', '-post,-suffix','Wikipedia')
	
	_.switches.register('Input', '-i,-search','Slack')

	_.switches.register('Save', '-save','zapier')

	_.switches.register('Print', '-print')

	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'google.py',
	'description': 'Returns the first google result',
	'categories': [
						'research',
						'online',
						'google',
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
						'p google -search twitter',
						'type %tmpf0% | p google -suffix Wikipedia -save zapier',
						'p google -save zapier -i %tmpf0%',
						'p google -save zapier -i %tmpf0% -print > %tmpf7%',
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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )


########################################################################################
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# os.system('"' + do + '"')
########################################################################################
# START

def cleanupString0(string):
	# string = str( string )
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanBE(string,' ')
	string = _str.clean_latin1( string )
	return string


def google( subject, data ):
	additionalData = []
	
	url = 'https://www.google.com/search?q=' + data
	newURL = url.replace(',','+').replace(' ','+')
	page = requests.get(newURL)
	tree = html.fromstring(page.content)

	# _.saveText( cleanupString0(page.content), _v.html_temp )
	# _.pr( _v.html_temp )

	record = tree.cssselect('.ZINbbc')
	i = 'x'
	for ix,row in enumerate(record):
		payload = record[ix].cssselect('.s3v9rd')
		if len( payload ) and i == 'x':
			i = ix
		if len( payload ) > 1:
			if 'wikipedia' in row.text_content().lower():
				i = ix
				break
		


	# _.pr( 'i:', i )
	if i == 'x':
		payload = tree.cssselect('.s3v9rd')
	else:
		payload = record[i].cssselect('.s3v9rd')
		addition = record[i].cssselect('.vbShOe')

		if len( addition ):
			for row in record[i].cssselect('.AVsepf'):
				additionalData.append( cleanupString0( row.text_content() ) )
		x = ''
		try:
			try:
				result = cleanupString0( payload[0].text_content() )
			except Exception as e:
				x = e
				result = cleanupString0( payload.text_content() )
		except Exception as ee:
			try:
				
				result = cleanupString0( payload[0].text_content() )
			except Exception as e:
				_.pr(  )
				s = cleanupString0( subject )
				s = s.replace(',','_').replace(' ','_')
				f = _v.html_temp
				f = f.replace( '_temp.htm', '_temp_'+s+'.htm' )
				_.saveText( cleanupString0(page.content), f )
				
				if 'range' in str(x):
					error = 'out of range'
				else:
					error = 'unknown'

				_.pr( 'Search:', subject )
				_.pr( 'Error:', error )
				_.pr( 'Page:', f )
				result = 'Error: ' + error
		# sys.exit()

	






	

	return [ result, additionalData ]

def fileName():
	f = _.switches.value( 'Save' )
	if not '.json' in f.lower():
		f = f + '.json'
	return 'google_' + f

def printRecord( record ):
	_.pr()
	_.pr()
	_.pr( '________________________________________________' )
	_.pr( record['q'] )
	# if not record['search'] == record['q']:
	#     _.pr()
	#     _.pr( '\t(', record['search'],')' )
	#     _.pr()
	_.pr()
	_.pr( record['a'] )
	if len( record['notes'] ):
		_.pr()

		for row in record['notes']:
			_.pr( '\t', row )


def action():
	global data
	load()

	if len( data ):
		if _.switches.isActive( 'Print' ):
			ask = 'y'
		else:
			ask = input( 'Search Again? ' )
	if not 'y' in ask.lower():
		for record in data:
			printRecord( record )
		sys.exit()


	# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	if _.switches.isActive('Input'):
		if os.path.isfile( _.switches.value('Input') ):
			_.setPipeData( _.getText( _.switches.value('Input') ), focus() )
		else:
			if type( _.appData[__.appReg]['pipe'] ) == bool:
				_.appData[__.appReg]['pipe'] = []
				for row in _.switches.value('Input').split( ',' ):
					_.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		records = []
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			q = row
			if _.switches.isActive( 'Prefix' ):
				q = _.switches.value( 'Prefix' ) + ' ' + q
			if _.switches.isActive( 'Suffix' ):
				q = q + ' ' + _.switches.value( 'Suffix' )
			test = False
			if test:
				a = google( row, q )
			else:
				try:
					a = google( row, q )
				except Exception as e:
					a = ['',[]]
			record = { 'search': q, 'q': row, 'a': a[0], 'notes': a[1] }

			printRecord( record )

			records.append( record )

		if _.switches.isActive( 'Save' ):
			_.saveTable( records, fileName() )


def load():
	global data
	data = _.getTable( fileName() )
data = []
########################################################################################
if __name__ == '__main__':
	action()


# https://zapier.com/apps