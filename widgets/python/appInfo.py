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
import simplejson as json
import importlib
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
import _rightThumb._dir as _dir




def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Folder', '-folder')
	_.switches.register('Version', '-version')
	



_.appInfo[focus()] = {
	'file': 'appInfo.py',
	'description': 'Extracts app info',
	'categories': [
						'research',
						'text manipulation',
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


_.appInfo[focus()]['examples'].append('b py')
_.appInfo[focus()]['examples'].append('Fast ▽')
_.appInfo[focus()]['examples'].append('   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == \'__main__\';." - # -jn  | p appInfo')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append("""   p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p line --c -make "echo {}| p appInfo" | p execute""")
_.appInfo[focus()]['examples'].append('Accurate △')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()



def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')



_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################
# START


def processInstances(ns,nsx):
	result = []
	for xXx in nsx.split('='):
		if ns+'.' in xXx:
			xXx = xXx.replace( '(', '( ' )
			testing = '._(0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

			# Y = xXx.split(ns+'.')[1]
			xYx = ''
			for ch in xXx:
				if not ch in testing:
					xYx += ' '
				else:
					xYx += ch
			for vVv in xYx.split(' '):
				if ns+'.' in vVv and not '_'+ns+'.' in vVv:
					vVv = vVv.replace( '.append(', '' )
					result.append( vVv  )


	return result


def myApps():
	global myAppList
	if not len( myAppList ):
		folder = os.getcwd()
		dirList = os.listdir(folder)
		i = 0
		for item in dirList:
			path = folder + _v.slash + item
			if os.path.isfile(item) and item.lower().endswith('.py'):
				myAppList.append( appFromFileName( item ) )
	return myAppList



def appFromFileName( file ):
	x = file.split( '.' )
	x.pop( len(x)-1 )
	return '.'.join( x )

def addKeys( appInfo, fileInfo, version, fileProfile ):
	error = False
	errors = []
	for record in fileProfile['imports']:
		if not error:
			if not len( record['examples'] ):
				error = True
				errors.append({ 'field': 'file_profile', 'error': 'has include that is not used', 'effects': 'speed' })

	# _.pr( 'VVVVVVVVVVVVVVVVVVVVV' )
	# _.printVar( appInfo )
	# sys.exit()
	appInfo['live_file'] = fileInfo['name']
	# appInfo['live_app'] = appFromFileName( fileInfo['name'] )
	appInfo['live_app'] = '' + appFromFileName( fileInfo['name'] )

	if '.' in appInfo['live_app']:
		error = False
		errors.append({ 'field': 'live_app', 'error': '. in name', 'effects': 'unable to import' })

	appInfo['error'] = error
	appInfo['errors'] = errors

	if 'thisApp' in appInfo['file']:
		error = False
		errors.append({ 'field': 'file', 'error': 'default data', 'effects': 'documentation' })
	if 'Changes the world' in str(appInfo['description']):
		error = False
		errors.append({ 'field': 'file', 'error': 'default data', 'effects': 'documentation' })

	try:
		len( appInfo['categories'] )
	except Exception as e:
		appInfo['categories'] = []

	try:
		len( appInfo['relatedapps'] )
	except Exception as e:
		appInfo['relatedapps'] = []


	try:
		len( appInfo['prerequisite'] )
	except Exception as e:
		appInfo['prerequisite'] = []

	try:
		len( appInfo['examples'] )
	except Exception as e:
		appInfo['examples'] = []

	try:
		len( appInfo['aliases'] )
	except Exception as e:
		appInfo['aliases'] = []

	try:
		len( appInfo['columns'] )
	except Exception as e:
		appInfo['columns'] = []

	if len( appInfo['examples'] ):
		if appInfo['examples'][0] == 'DEFAULT':
			error = False
			errors.append({ 'field': 'examples', 'error': 'default data', 'effects': 'documentation' })


	if len( appInfo['categories'] ) == 1:
		if appInfo['categories'][0] == 'DEFAULT':
			error = False
			errors.append({ 'field': 'categories', 'error': 'default data', 'effects': 'documentation' })

	if len( appInfo['categories'] ) > 1:
		if appInfo['categories'][0] == 'research' and appInfo['categories'][1] == 'text manipulation' and len(appInfo['categories']) == 2:
			error = False
			errors.append({ 'field': 'categories', 'error': 'default data', 'affect': 'documentation' })
	# _.pr( 'HERE', 0 )
# switches
# can have pipeData
# must have pipeData

# alias

	return appInfo


def auditAppInfo( appInfo, fileInfo, version, fileProfile ):
	inject = addKeys( appInfo, fileInfo, version, fileProfile )
	for key in inject.keys():
		appInfo[key] = inject[key]
	return appInfo


def auditImportLine( row ):

	row = row.replace( '\n', '' )
	row = row.replace( '\r', '' )
	row = row.replace( '\t', ' ' )
	row = _str.replaceDuplicate( row, ' ' )
	row = _str.cleanBE( row, ' ' )

	row = _str.spaceba( row, '=' )
	row = _str.spaceba( row, '(' )
	row = _str.spaceba( row, ')' )
	row = _str.spaceba( row, ',' )
	row = _str.spaceba( row, '#' )

	if 'from ' in row:
		if not row.lower().startswith( 'from ' ):
			return False

	if not row.startswith( '#' ):
		if '#' in row:
			row = row.split( '#' )[0]
		return row

	return False



def createRecord( data ):

	info = {}
	info['app'] = ''
	info['examples'] = []
	info['raw'] = data
	info['instantiated'] = False
	info['myapp'] = False
	if '_rightThumb' in data:
		info['myimport'] = True
		info['myapp'] = True
	else:
		info['myimport'] = False
	info['from'] = []
	info['namespace'] = []
	# return info
	done_namespace = False
	if not '_.regimp' in data.lower():
		if ' as ' in data:
			done_namespace = True
			a = data.split( ' as ' )
			data = a[0]
			for alias in a[1].split( ',' ):
				info['namespace'].append( alias )


		if data.startswith( 'from ' ):
			test = '931B695AF62A' + data
			data = test.replace( '931B695AF62Afrom ', '' )
			imp = data.split( ' import ' )
			for using in imp[1].split( ',' ):
				info['from'].append( using )
			appSpace = imp[0]

		elif data.startswith( 'import ' ):
			test = '931B695AF62A' + data
			data = test.replace( '931B695AF62Aimport ', '' )
			appSpace = data
		# _.pr( 'appSpace:', appSpace )
		if ',' in appSpace:
			newResults = []
			for app in appSpace.split( ',' ):
				# _.cp(app,'yellow')
				xInfo = {}
				xInfo['examples'] = []
				xInfo['raw'] = info['raw']
				xInfo['from'] = []
				xInfo['namespace'] = []
				info['myapp'] = False
				if '_rightThumb' in app:
					info['myimport'] = True
				else:
					info['myimport'] = False
				if '.' in app:
					if not info['myapp']:
						if xx in myApps():
							info['myapp'] = True

					if info['myimport']:
						xInfo['app'] = app
					else:
						xInfo['app'] = app.split( '.' )[0]
					xInfo['namespace'].append( xInfo['app'] )
					xInfo['namespace'].append( app )
				else:
					xInfo['app'] = app
					xInfo['namespace'].append( app )

				newResults.append( xInfo )
			return newResults

		
		if '.' in appSpace:
			# _.cp(appSpace,'green')
			if '_rightThumb' in appSpace:
				info['app'] = appSpace
			else:
				info['app'] = appSpace.split( '.' )[0]
			if not done_namespace:
				info['namespace'].append( info['app'] )
				info['namespace'].append( appSpace )
		else:
			info['app'] = appSpace
			if not done_namespace:
				info['namespace'].append( info['app'] )
		if not info['myapp']:
			if info['app'] in myApps():
				info['myapp'] = True
		return info
	else:
		data = data.replace( '"', "'" )
		info = {}
		info['examples'] = []
		info['raw'] = data
		info['instantiated'] = False
		info['myapp'] = False
		info['myapp'] = True
		if '_rightThumb' in data:
			info['myimport'] = True
		else:
			info['myimport'] = False
		info['from'] = []
		info['namespace'] = []

		info['namespace'].append( data.split( '=' )[0] )
		try:
			info['app'] = data.split( "')" )[0].split( ",'" )[1]
		except Exception as e:
			_.pr()
			_.pr( data )
			sys.exit()

		return info


	if '931B695AF62A' in data:
		_.pr( 'Error: 931B695AF62A' )
	return info

# from os.path import isfile, isdir
# import uuid
# from datetime import datetime as dt, timedelta
# from datetime import date
# import _rightThumb._construct as __
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase')


# from . import (ValueWidget, Text,
# from . import *
# from . import __config__
# from  .axis_artist import AxisArtist
# from %(module)s import %(import_name)s
# from (0, 0) to (1, 1).
# from (key, rank) sequences.
# from . import  canvas
# from . import *
# from . import __version__
# from .. import path
# from ...runner._exit import ExitStatus
# from ._compat import open_stream, text_type, filename_to_ui, \
# from ._distn_infrastructure import (entropy, rv_discrete, rv_continuous,
# from ._exceptions import SAXException, SAXNotRecognizedException, \
# from .auibook import *
# from .australia import shrimp as prawns
# from twisted.conch.client.knownhosts import \


def processApp( path ):
	global data
	
	# for x in myApps():
	#     _.pr(x)

	# return {}
	test = False

	# _.pr( os.path.abspath(path), os.path.isfile(path) )
	fileInfo = _dir.fileInfo( os.path.abspath(path) )
	if fileInfo['name'].startswith( 'blank' ):
		return False
	if '.' in appFromFileName( fileInfo['name'] ):
		return False
	file = _.getText( os.path.abspath(path) )



	version = 0
	fileProfile = {}
	fileProfile['imports'] = []
	# fileProfile['instances'] = {}

	# fileProfile['imports'] = {}
	# fileProfile['imports']['records'] = []
	# fileProfile['imports']['instances'] = []

	for row in file:


		if 'import ' in row.lower() or ( 'from ' in row.lower() and 'import ' in row.lower() ) or '_.regimp(' in row.lower():
			# _.pr( 'here' )
			if row.startswith( 'import ' ) or ( row.startswith( 'from ' ) and ' import ' in row.lower() ) or '_.regimp(' in row.lower():
				importData = auditImportLine( row )
				if not type( importData ) == bool:
					record = createRecord( importData )
					if type( record ) == dict:
						fileProfile['imports'].append( record )
					if type( record ) == list:
						for x in record:
							fileProfile['imports'].append( x )



		if version == 0:
			if '_rightThumb._base' in row:
				v = row.split( '_rightThumb._base' )[1][0]
				try:
					version = int( v )
				except Exception as e:
					_.pr( row )
					_.pr( v )
					_.pr( 'Error: int( v )' )
					# sys.exit()
					version = 0
	if len( fileProfile['imports'] ):
		exampleSpent=[]
		for rowX in file:
			rowX = ' '+rowX+' '
			row = ''
			for ch in rowX:
				if ch in '(._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
					row += ch
				else:
					row += ' '+ch+' '
			row = row.replace( '(', '( ' )
			row = row.replace( '\t', ' ' )
			while '  ' in row:
				row = row.replace('  ',' ')
			# _.pr(row)
			for i,record in enumerate(fileProfile['imports']):
				if not 'instances' in fileProfile['imports'][i]:
					fileProfile['imports'][i]['instances'] = {}
				for ns in record['namespace']:
					nss = ns+'.'
					if nss in row:
						r = row
						# r = auditImportLine( row )
						if not type( r ) == bool:
							if nss in r:
								for nsx in r.split( ' ' ):
									if ns+'.' in nsx:
										nsxXx = processInstances(ns,nsx)
										# _.pr( nsxXx )
										for nsxXxY in nsxXx:
											if len(nsxXxY):
												# _.pr( type(nsxXxY), nsxXxY )
												if not nsxXxY in fileProfile['imports'][i]['instances']:
													fileProfile['imports'][i]['instances'][nsxXxY] = 0
												fileProfile['imports'][i]['instances'][nsxXxY] +=1
										
										if not nsx in exampleSpent:
											exampleSpent.append( nsx )
											fileProfile['imports'][i]['examples'].append( nsx )



	file = []



	if test:
		if version == 0:
			_.pr( 'Version Error' )
		else:
			_.pr( 'version:', version )

		# _.pr()
		# _.pr( 'fileInfo:', path, os.path.abspath(path) )
		# _.printVar( fileInfo )
		# _.pr()

	appName = path.replace( _v.py,'' ).replace('.py','').replace( os.sep, '.' ).replace(' ','')
	try:
	# if True:

		# imp = importlib.util.spec_from_file_location( path )
		imp = importlib.import_module( appName )

		# if test:
		#     _.pr( 'imp:' )
		#     _.printVar( imp._.appInfo )
		#     _.pr()
		

		iKeys = 0
		first = ''
		found = False
		result = {}



		foundVersion = False
		if version == 1:
			foundVersion = True
			appInfo = imp._.appInfo


		if version == 2:
			foundVersion = True
			appInfo = imp._.appInfo

			autoKey = appFromFileName( fileInfo['name'] )
			foundKey = False
			for key in appInfo.keys():
				if key.lower() == autoKey.lower():
					foundKey = True

			if foundKey:
				appInfo = appInfo[autoKey]

		if version == 3:
			foundVersion = True
			appInfo = imp._.appInfo


			autoKey = appFromFileName( fileInfo['name'] )
			foundKey = False
			for key in appInfo.keys():
				if key.lower() == autoKey.lower():
					foundKey = True

			if foundKey:
				appInfo = appInfo[autoKey]

			# _.printVar( appInfo )


		if foundVersion:
			appInfo = auditAppInfo( appInfo, fileInfo, version, fileProfile )
			_.pr( 'WORKS' )
			appInfo['base_version'] = version
			appInfo['file_profile'] = fileProfile
			appInfo['app_version'] = findRevision( fileInfo['path'] )

	# *
	# *
	# *
	# *


			return appInfo



		if foundVersion:
			if test:
				_.pr( 'appInfo:' )
				_.printVar( appInfo )
				_.pr()
			for i,key in enumerate(appInfo.keys()):
				iKeys += 1
				
				if i == 0:
					first = key
				try:
					if appInfo['file'] == fileInfo['name']:
						found = True
						result = appInfo[ key ]
				except Exception as e:
					_.pr( 'Error:', appInfo[ key ]['file'], fileInfo['name'] )



			if not found:
				pass


			if test:
				_.pr( 'found:', found )
			result['livefile'] = fileInfo['name']
			return result

		if test:
			_.pr( 'Error: version not found', version )
	except Exception as e:
		with open(  _v.myTables+os.sep+'appInfo-errors'  , 'a' ) as file: file.write( appName + '\n' );
		_.e( appName, e, kill=False )

		pass
	return False

def action():
	records = _.getTableDB( 'appRegistration.hash' )
	__.appInfoScan = True

	global data

	test = False

	if _.switches.isActive('Input'):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = []
			for row in _.switches.value('Input').split( ',' ):
				_.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			row = row.replace( '\n', '' )
			_.pr( row )
			if test:
				_.pr( '______________________________' )
				_.pr( '______________________________' )
			info = processApp( row )
			# try:
			# except Exception as e:
			#     info = False
			if not type( info ) == bool:
				a = info['file']
				if 'liveAppName' in info:
					if not 'thisApp' in info['liveAppName']:
						a = info['liveAppName']
				if 'live_file' in info:
					if not 'thisApp' in info['live_file']:
						a = info['live_file']
				if 'live_app' in info:
					if not 'thisApp' in info['live_app']:
						a = info['live_app']
				a = a.replace('.py','')
				records[a] = info
				# data.append( info )
				_.pr( 'Good' )
			else:
				_.pr( 'Bool' )
					

			
			if test:
				_.pr( '______________________________' )
				_.printVar( info )
				return False
		_.saveTableDB( records, 'appRegistration.hash' )
		_.pr()
		_.pr()
		_.colorThis( 'DONE', 'green' )

myAppList = []

data = {}

def findRevision( path ):
	global autoRevision
	for record in autoRevision:
		if path in record['file']:
			return record['version']
	return '0.0.0.0'



autoRevision = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# data = _.getTable( 'appRegistration.json' )

# p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo
# p f -in *.py + _rightThumb._base2  -jn | p f + "if __name__ == '__main__';." import - # -jn | p f + "from " import - # -jn
# p f -in *.py + _rightThumb._base2  -jn | p f + "if __name__ == '__main__';." - # -jn | p appInfo

# p appInfo -i appendjson.py auditCSS.py txtBackup.py

# p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn | p find_execute_on_load_apps


########################################################################################
if __name__ == '__main__':
	action()