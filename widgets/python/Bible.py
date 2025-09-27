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
	_.switches.register( 'ListBooks', '-books' )
	_.switches.register( 'Verses', '-v,-vs,-verse,-verses' )
	_.switches.register( 'Build', '-build', 'indices' )
	_.switches.register( 'EditCMDs', '-edit' )
_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'Bible.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Bible Reader',
	'categories': [
						'Bible',
						'reader',
						'research',
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
						'p Bible -vs jn 3:16 - 4:5 rom 1:2-7',
						'',
						'p Bible -vs jn 3:16 - 4:5 rom 1:2-7 + jew',
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
	# _.switches.trigger( 'Verses', Verses_trigger )
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
# START

def action():
	load()
	mx = 200
	for q in _B.query:
		_.pr()
		_.pr()
		_print.label(q)
		cnt = 0
		result = []
		for vs in _verses.build(q):
			if 'ch' in vs:
				cnt = 0
				_.pr()
				result.append( '\n'+  _.colorThis( vs['ch'], 'yellow', p=0 )  + '\n' )
			else:
				# if _.showLine(vs['word']):
				if True:
					# _.pr( vs['vs'], _.colorThis( vs['word'], 'cyan', p=0 ) )
					word = vs['word']
					for tmp in str(vs['vs']):
						cnt +=1
					if cnt > mx:
						cnt=0
						result.append( '\n' )
					result.append( ' '+_.colorThis( vs['vs'], 'yellow', p=0 )+' ' )
					rx=''
					past = False
					for tw in word:
						cnt +=1
						if cnt > mx:
							past=True
						if past and  tw==' ':
							rx+='\n'
							cnt=0
							past=False
						rx+=tw
					if _.switches.isActive('Plus'):
						for x in _.switches.values('Plus'):
							for y in _.caseUnspecific(rx,x):
								rx = rx.replace( y, _.colorThis( y, 'cyan', p=0 ) )
					result.append( rx )
		_.pr( ''.join( result ) )
			# _.pr(vs)

def load():
	if _.switches.isActive('EditCMDs'):
		_.pr( """
	epy Bible
	epyi Bible
	epyi Bible -file _query
	epyi Bible -file _verses
	epyi Bible -file _print
	epyi Bible -file _build_indices
	epyi Bible -file _query_indices
			""" )
		# _.pr(' epy Bible ')
		# _.pr(' epyi Bible ')
		# _.pr(' epyi Bible -file _query ')
		# _.pr(' epyi Bible -file _verses ')
		# _.pr(' epyi Bible -file _print ')
		# _.pr(' epyi Bible -file _build_indices ')
		# _.pr(' epyi Bible -file _query_indices ')
		sys.exit()
	_B.load()
	if _.switches.isActive('Verses'):
		_query.build()
	elif _.switches.isActive('Plus'):
		_query_indices.query( _.switches.values('Plus') )
	# buildTables()
	if _.switches.isActive('Build'):
		if _.switches.value('Build') == 'indices':
			_build_indices.all(include_query=True)
		else:
			_build_indices.all(include_query=False)
	# _build_indices.search_indices()
# p Bible -vs 1 jn 1:1-2 2:4 - 6 3:4-7 1 jn 3:16
# p Bible -vs 1 jn 1:1- 2:4 - 6 3:4-7 1 jn 3:16
import _rightThumb._Bible as _B
if _.switches.isActive('ListBooks'):
	# labels Books Bible
	_B.load()
	BKs = {}
	for i in _B.Books:
		BKs[_B.Books[i]] = {}
	for i in _B.Books:
		BKs[_B.Books[i]] = i
	for i in _B.Books:
		# BKs[_B.Books[i]][i] = {}
		# if _B.Books[i] == 55:
		#     _.pr( i )
		if len(i) <= len(BKs[_B.Books[i]]):
			BKs[_B.Books[i]] = i.lower()
		# _.pr( i, _B.Books[i] )
	# _.pr( _B.Books )
	# for i in BKs:
	#     # _.pr( i, type(i) )
	#     _.pr( i, BKs[i] )
	table = []
	for i in _B.labels:
		# table.append({ 'number': i, 'book': _B.labels[i] })
		if _.showLine(_B.labels[i]):
			if not _.switches.isActive('Plus') and int(i) == 40:
				table.append({ 'number': '', 'book': '', 'mini': '' })
				table.append({ 'number': '', 'book': '', 'mini': '' })
			table.append({ 'number': i, 'book': _B.labels[i], 'mini': BKs[int(i)] })
		# _.pr( i, _B.labels[i] )
	_.tables.register( 'Books', table )
	_.tables.fieldProfileSet( 'Books', 'number', 'alignment', 'left' )
	_.tables.fieldProfileSet( 'Books', 'mini', 'alignment', 'left' )
	_.tables.fieldProfileSet( 'Books', 'book', 'alignment', 'right' )
	# _.tables.print( 'Books', 'number,book' )
	# _.tables.print( 'Books', 'number,mini,book' )
	_.tables.print( 'Books', 'book,mini,number' )
	sys.exit()
from _rightThumb._Bible import _query
from _rightThumb._Bible import _verses
from _rightThumb._Bible import _print
from _rightThumb._Bible import _build_indices
from _rightThumb._Bible import _query_indices
"""
ISSUE
	capital letters in index ????????????????????????????????????????
pp nest_dim_sort_test
"""
# from os.path import isfile, isdir

########################################################################################
if __name__ == '__main__':
	action()