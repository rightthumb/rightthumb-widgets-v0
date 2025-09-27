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

# import os
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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._encryptString as _blowfish
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
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


#     fileBackup.switch( 'Input', filename )
#     fileBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = fileBackup.do( 'action' )
##################################################
from lxml import html
import requests
import cssselect
import socket
##################################################


def appSwitches():
	_.switches.register('Input', '-i,-ip','8.8.8.8')
	_.switches.register('Host', '-host','google.com')
	_.switches.register('JSON', '-json')
	_.switches.register('Dump', '-dump')
	_.switches.register('Test', '-test')
	_.switches.register('NoCache', '-nocache')
	



_.appInfo[focus()] = {
	'file': 'netblock.py',
	'description': 'lookup netblock owner',
	'categories': [
						'DEFAULT'
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('netstat -a -n | p line + ESTABLISHED | p line -p " " 2 + . - " 127." | p line -p ;. 0 | p netblock')
_.appInfo[focus()]['examples'].append('netstat -n | p line + ESTABLISHED | p line -p " " 2 + . - " 127." | p line -p ;. 0 | p netblock')
_.appInfo[focus()]['examples'].append('netstat -n | p line | p line -p " " 2 + . - " 127." | p line -p ;. 0 | p netblock')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('netstat -n | p line | p line -p " " 2 + . - " 127." | p line -p ;. 0 | p netblock -c org ip -g org')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p netblock -ip 216.58.192.46')
_.appInfo[focus()]['examples'].append('p netblock -host google.com')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p printTable -long -i fileBackup.json -last 50 -c timestamp file backup + netblock_owner.json')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c org ip -g org')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c timezone org -g timezone')
_.appInfo[focus()]['examples'].append('p printTable -long -i D:\\tech\\hosts\\MSI\\txt\\1571025031.332114-2019_10_13-23_50_31-netblock_owner.json -c timezone org ip -g timezone org')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')

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
# START

def cleanupString(string,beforeAfter=True):
	string = _str.replaceAll(string,'\n',' ')
	string = _str.replaceAll(string,'\t',' ')
	string = _str.cleanLast(string,' ')
	string = _str.cleanFirst(string,' ')
	string = _str.cleanSpecial(string)
	string = _str.cleanFirst(string,' ')
	string = _str.charFix(string)
	string = string.replace(_v.slash+'xe2\\x80\\x93','-')
	string = string.replace(_v.slash+'\\xe2\\\\x80\\\\x93','-')
	if beforeAfter:
		string = string.split('(')[0]
	else:
		string = string.split('(')[1]
	string = string.split('/')[0]
	string = string.replace(_v.slash+'xbb','')
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string


import urllib.request

def checkCache( ip ):
	if _.switches.isActive('NoCache'):
		return False
	global netblockCache

	for record in netblockCache:
		if record['ip'] == ip:
			return record
	return False

def process( ip ):
	global spent
	if ip in spent:
		return False
	else:
		spent.append( ip )
	cache = checkCache( ip )
	if not type(cache) == bool:
		return cache
	# url = ''
	url = 'http://ipinfo.io/'
	
	# url = 'http://www.rightthumb.com/projects/widget/proxy.php?p=http://ipinfo.io/'
	# url = 'http://www.pillerbeauty.com/proxy.php?p=http://ipinfo.io/'
	
	
	if _.switches.isActive('Test'):
		url = 'http://www.rightthumb.com/projects/widget/head.php'
		url = 'http://www.pillerbeauty.com/head.php'



		# url = 'https://httpbin.org/user-agent'
		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		header = {
					'User-Agent': user_agent,
					'Accept': 'application/json'
		}
		request = urllib.request.Request(url,headers=header)
		response = urllib.request.urlopen(request)
		html = response.read()

		for line in html.decode('utf-8').split('\n'):
			_.printBold( line, 'green' )
		# _.printBold( thePath, 'red' )
		sys.exit()



		# header = {
		#             'q': 'requests+language:python'
		# }
		# page = requests.get( url, params=header )
		# # thePath = _v.stmp + _v.slash + 'netblock_' + str( time.time() ) + '.txt'
		# # _.saveText( page.content, thePath )
		# # dump = _.getText( thePath, raw=True, clean=2 ).split('\n')
		# for line in page.content.decode('utf-8').split('\n'):
		#     _.printBold( line, 'green' )
		# # _.printBold( thePath, 'red' )
		# sys.exit()
	else:

		user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		header = {
					'User-Agent': user_agent,
					'Accept': 'application/json'
		}
		request = urllib.request.Request(url,headers=header)
		response = urllib.request.urlopen(request)
		html = response.read()

		# page = requests.get( url + ip )

	# _.pr( page.content )
	# _.printVar( eval( page.content ) )
	testing = False
	# _.pr( html )
	if sys.getsizeof( html ) < 350:
		good = True
		tests = [
					'"ip":',
					'"org":'
				]
		found = 0
		t = str( html )
		t = t.encode('latin1', 'ignore')
		t = t.decode('latin1')
		t = t.replace( ' ', '' )
		if testing:
			_.pr()
			_.pr( t )
			_.pr()
		if not t.startswith( "b'{" ):
			if testing:
				_.pr( 'Error: start', t[0] )
			good = False
		if not t.endswith( "}'" ):
			if testing:
				_.pr( 'Error: end', t[-1] )
			good = False
		for test in tests:
			if not test in t:
				if testing:
					_.pr( 'Error:', test )
				good = False



		if good:
			thePath = _v.stmp + _v.slash + 'netblock_' + str( time.time() ) + '.txt'
			_.saveText( html, thePath )


			if _.switches.isActive('Dump'):
				dump = _.getText( thePath, raw=True, clean=2 ).split('\n')
				for line in dump:
					_.printBold( line, 'green' )
				sys.exit()


			# _.pr( thePath )
			# sys.exit()
			data = eval( html )
			data['co'] = resolveCountry( data['country'] )
			# try:
			# except Exception as e:
			#     data['co'] = ''
			if not type( data ) == dict:
				_.pr()
				_.pr( 'Error: BAD CODE !!!!!!!!!!!!' )
				_.pr( '\t', thePath )
				sys.exit()

			return data
		else:
			return False

	else:
		if testing:
			_.pr( sys.getsizeof( html ) )
		return False
		# _.printFields( eval( page.content ) )
	# for row in  li:
	#     span = tables.cssselect('span')
	#     _.pr( cleanupString(span[0]), '\t', cleanupString(span[1]) )
	#     _.pr(x.text_content())

	# for x in dir( page ):
	#     _.pr(x)
	# _.pr( tree.body )
	# _.pr( tree.text_content() )
	# tables = tree.cssselect('.r')
def checkExist( row, data ):
	for record in data:
		if record['ip'] == row:
			return True
	return False

def checkExist2( check, data ):
	for record in data:
		if record['ip'] == check['ip']:
			return True
	return False

def action():
	global netblockCache
	if _.switches.isActive('Host'):
		_.switches.fieldSet( 'Input', 'active', True )
		_.switches.fieldSet( 'Input', 'value', socket.gethostbyname( _.switches.value('Host') ) )
		

	
	if _.switches.isActive('Input'):
		_.setPipeData( [  _.switches.value('Input')  ], focus() )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		load()
		# _.pr( _.printVar(_.appData) )
		data = []
		errors = []
		spent = []
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			if len( row ):
				# _.pr( row )
				hasAlpha = False
				for char in row:
					if char in _str.alphaChar:
						hasAlpha = True
						break
				if hasAlpha:
					row = socket.gethostbyname( row )


				if not checkExist( row, data ):
					record = process( row )
					if not type( record ) == bool:
						if not checkExist2( record, data ):
							data.append( record )
					else:
						errors.append( row )
					# try:
					# except Exception as e:
					#     pass

		if _.switches.isActive('JSON'):
			data = cleanData( data )
			_.printVar( data )
		else:

			data = cleanData( data )
			# data = _.tables.returnSorted( 'data', 'd.postal', data )
			# _.switches.fieldSet( 'GroupBy', 'active', True )
			# _.switches.fieldSet( 'GroupBy', 'value', 'org' )
			_.switches.fieldSet( 'Long', 'active', True )
			if not _.switches.isActive('Sort') and not _.switches.isActive('GroupBy'):
				_.tables.returnSorted( 'data', 'a.org', data )
			else:
				_.tables.register( 'data', data )
			if not _.switches.isActive('Column'):
				_.tables.print( 'data', 'ip,org' )
			else:
				_.tables.print( 'data', _.switches.value('Column') )
			# _.pr()
			# _.pr('', len(data))
			# _.pr()
		for error in errors:
			_.printBold( error, 'red' )
		if not len(data):
			_.printBold( 'No results', 'red' )
		else:
			cacheIPs = []
			for record in netblockCache:
				cacheIPs.append( record['ip'] )
			for record in data:
				if not record['ip'] in cacheIPs:
					cacheIPs.append(record['ip'])
					record['timestamp'] = time.time()
					netblockCache.append( record )
			_.saveTable( netblockCache, 'netblockCache.json', printThis=False )
			_.saveTable( data, 'netblock_owner.json', printThis=False )

			fileBackup = _.regImp( focus(), 'fileBackup' )
			fileBackup.switch( 'Silent' )
			fileBackup.switch( 'Flag', 'netblock' )
			fileBackup.switch( 'isRunOnce' )
			fileBackup.switch( 'DoNotSchedule' )

			fileBackup.switch( 'Input', _v.myTables + _v.slash+'netblock_owner.json' )
			recoveryFile = fileBackup.do( 'action' )
			_.printBold( recoveryFile, 'green' )
def cleanData( data ):
	fields = []
	newFields = []
	# _.pr( len(data) )
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
	# _.pr( len(data) )
	return data

def resolveCountry( data ):
	global co

	data = data.replace( ' ', '' )

	for row in co:
		if row['abbreviation'].lower() == data.lower():
			return row['name']
	return ''
def load():
	global co
	global netblockCache
	co = _.getTable( 'countries_abbreviations.json' )
	netblockCache = _.getTable( 'netblockCache.json' )

co=[]
netblockCache=[]
spent = []
########################################################################################
if __name__ == '__main__':
	action()