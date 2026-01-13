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
import _rightThumb._encryptString as _blowfish
_browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
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

# from lxml import html
import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'yahooGroupSyFyTranscripts.py',
	'description': 'Acquire transcripts for SyFy stuff',
	'categories': [
						'online',
						'syfy',
						'yahoo',
						'yahoo group',
						'acquire',
						'transcripts',
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
						'p yahooGroupSyFyTranscripts',
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

# from subprocess import call
# from selenium import webdriver
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.keys import Keys


def action():
	global data
	# load()

	# _.pr( _v.chromedriver )
	# sys.exit()

	url                = 'https://groups.yahoo.com/neo/groups/Stargate_SG-1_and_Atlantis_Transcripts/files/Stargate%20Atlantis%20Transcripts/'
	login              = 'scottreph'
	password           = '5FmlcmV1xo9q1dRft6lGY2AY/89PwSeU'
	# password           = _blowfish.decrypt( '5FmlcmV1xo9q1dRft6lGY2AY/89PwSeU' )
	login_selector     = "[name='username']"
	password_selector  = "[name='password']"
	# password_selector  = '#login-passwd'

	# _.pr( password )

	_browser.imp.project.loginIndividually( url, login, password, login_selector, password_selector )




	code = _.getText( _v.myAppsJs + _v.slash+'yahoo_groups_SyFy_transcripts.js' )
	_browser.imp.project.jqueryInject()
	_browser.imp.project.inject( code )
	


	# _browser.imp.project.open( 'http://rightthumb.com/projects/john/' )
	# data =_browser.imp.project.injectReturn( 'family.v.auditOverflow' )
	data =_browser.imp.project.injectReturn( 'window.hack.acquire.audit()' )
	
	_.printVar( data )

	for i,record in enumerate(data):
		_browser.imp.project.open( record['href'] )
		time.sleep( 1 )
		_browser.imp.project.jqueryInject()
		_browser.imp.project.inject( code )
		try:
			d =_browser.imp.project.injectReturn( 'window.hack.acquire.auditChildren()' )
		except Exception as e:
			d = ''
		data[i]['children'] = d
		# _.pr( 'Click: Pre' )
		# _browser.imp.project.clickEach( '.yg-list-title' )
		# _.pr( 'Click: Post' )

		# try:
		# except Exception as e:
		#     _.pr( 'Click Error' )


		time.sleep( .5 )


		# test = False
		# _.pr( test )
		# while not test:
		#     time.sleep( 1 )
		#     try:
		#         test = _browser.imp.project.injectReturn( 'window.hack.acquire.pause()' )
		#         how = 0
		#     except Exception as e:
		#         test = False
		#         how = 1
		#     _.pr( test, how )

		
		# data = _browser.imp.project.injectReturn( 'return window.hack.acquire.data;' )

		# files = []
		# for rec in data:
		#     files.append( rec['file'] )
			

		# _.printVar( data )
		# # _browser.imp.project.close()
		# # sys.exit()

		# test = False
		# _.pr( test )
		# while not test:
		#     time.sleep( 1 )
		#     cnt = 0
		#     downloads = os.listdir( _v.downloads )
		#     for file in files:
		#         if file in downloads:
		#             cnt += 1
		#     if cnt == len(files):
		#         test = True
		#     else:
		#         _.pr( 'Waiting on downloads:', cnt, 'of', len(files) )




# 

		# break

	for row in data:
		f = _v.downloads + _v.slash+'Transcripts'
		if not os.path.isdir(f):
			os.mkdir(f)
		f += _v.slash  + row['file']
		if not os.path.isdir(f):
			os.mkdir(f)
		for record in row['children']:
			fX = f
			fX += _v.slash + record['file']
			r = requests.get( record['href'] )
			open(fX, 'wb').write(r.content)
			# _.saveText( _str.clean_latin1(r.content), fX )
			



	_.printVar( data )
	_.saveTable( data, 'Stargate_Atlantis.json' )
# 

	pause = input( 'pause' )
	_browser.imp.project.close()



# def load():
#     global data
#     data = _.getTable( 'table.json' )
data = []
########################################################################################
if __name__ == '__main__':
	action()


# p dir3 -ago 1d -c n --c | p cleanEnd | p line --c -make "del ;'{};'" | p execute
# window.hack.acquire.done = true;
# p dir3 -ago 1d -c n
# p dirdb + *.py selenium chrome techApps Python36











