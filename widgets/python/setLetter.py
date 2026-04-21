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

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Dictionary', '-dic','4 + *ro*')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT'
				],
	'relatedapps': [
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						'p string2Dic -i A B C D E F G H I J K L M N O P Q R S T U V W X Y Z -keys letter code -default {} true',
						'',
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

	_.switches.trigger('Input',_.myFileLocations)
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
########################################################################################
# START

def action():
	global needed
	msg = 'WB MNQ TZTL KMBG WMBNRJI DS T KBMG BK CBZTMEDCI TQE, ZVDJI DW DS WMNI WVTW WVI SNDCDEI RMTAIS EITWV, VI EBIS DW QBW KBM SBGI QBRJI BRUICW RNW KBM SBGI QBRJI BRUICW RNW WB ISCTFI SBGI DJJ'
	_.pr( msg )
	decoded = msg
	# sys.exit()
	load()
	needed = []
	encoded = []
	spent = []
	# # _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
	if _.switches.isActive('Input'):
		_.setPipeData( _.getText( _.switches.value('Input') ), focus() )
		# if type( _.appData[__.appReg]['pipe'] ) == bool:
		#     _.appData[__.appReg]['pipe'] = []
		#     for row in _.switches.value('Input').split( ',' ):
		#         _.appData[__.appReg]['pipe'].append( row )
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.pr( _.printVar(_.appData) )
		result = ''
		for c in decoded:

			for i,row in enumerate(_.appData[__.appReg]['pipe']):
				if ',' in row:
					code = row.split( ',' )
					# _.printVar( code )
					if c.upper() == code[0].upper():
						if code[1] == '_':
							if not code[0] in encoded:
								encoded.append( code[0] )
						else:
							if not code[0] in spent:
								spent.append( code[0] )

						# if c.upper() == 'B':
						#     _.pr( c, code )
						c = code[1].upper()
						# if c.upper() == 'O':
						#     _.pr( c, code )
						break
			result += c
					
			
	_.pr( result )
	_.pr()
	_.pr()

	for en in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split( ' ' ):
		if not en in spent:
			needed.append( en )

	_.pr( 'encoded:', ' '.join( encoded ) )
	_.pr( ' needed:', ' '.join( needed ) )
	_.pr()
	_.pr()

	if _.switches.isActive( 'Dictionary' ):
		dicWord()

def dicWord():
	global needed
	global data
	dic = _.switches.value( 'Dictionary' ).split( ',' )

	try:
		cnt = int( dic[0] )
	except Exception as e:
		cnt = len( dic[0] )

	if not _.switches.isActive( 'Plus' ):
		_.switches.fieldSet( 'Plus', 'active', True )

		plus = []
		p = ''
		lastU = False
		findPattern = _str.replaceDuplicate( dic[0], '_' )
		if findPattern == '_':
			return False

		# _.pr( findPattern.split( '_' ) )
		
		test = '*,*'.join( findPattern.split( '_' ) )

		# test = _str.replaceDuplicate( test,rWhat)
		test = _str.cleanFirst( test, '*,' )
		test = _str.cleanEnd( test, ',*' )

		_.switches.fieldSet( 'Plus', 'value', test )
	_.pr( cnt, _.switches.value( 'Plus' ) )

	# sys.exit()




	omit = [
				' ',
				'-',
				'_',
				'.'
	]

	i = 0
	for word in data.keys():
		if len( word ) == cnt:
			if _.showLine( word ):
				good = True
				for o in omit:
					if o in word:
						good = False
				if good:
					for y,x in enumerate(dic[0]):
						if not x == '_':
							# _.pr( x, word[y] )
							if not word[y].lower() == x.lower():
								good = False
						elif not word[y].upper() in needed:
							good = False


				if good:
					_.pr( word )
					i+=1

	_.pr(  )
	_.pr( i )

# def find( criteria, test ):
#     if criteria.startswith('*') and criteria.endswith('*'):
#         criteria = criteria.replace( '*', '' )
#         if 'criteria' in test and not test.startswith( criteria ) and not test.endswith( criteria ):
#             return True
#     elif criteria.startswith('*') and test.startswith( criteria ):
#             return True
#     elif criteria.endswith('*') and test.endswith( criteria ):
#             return True
#     elif criteria in test:
#             return True
#     else:
#             return False


def load():
	global data
	data = _.getTable( 'dic_all.json' )
data = []
needed = []
########################################################################################
if __name__ == '__main__':
	action()

# A,_
# B,_
# C,_
# D,_
# E,_
# F,_
# G,_
# H,_
# I,E
# J,L
# K,_
# L,_
# M,R
# N,_
# O,_
# P,_
# Q,_
# R,_
# S,S
# T,_
# U,_
# V,_
# W,T
# X,_
# Y,_
# Z,_




