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
_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'joplin.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'read Joplin export json files',
	'categories': [
						'joplin',
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
						'p joplin',
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

def standardize():
	global data
	fields = []
	for i,record in enumerate(data):
		for key in record.keys():
			if not key in fields:
				fields.append(key)
	for i,record in enumerate(data):
		for field in fields:
			if not field in record.keys():
				data[i][field] = ''

def process( level=0, parent='' ):
	global data
	global spent
	table = []
	for record in data:
		# _.pr( record['parent_id'] )
		if record['parent_id'] == parent and not record['title'].endswith('.png') and not record['title'] == '?':
			if not record['id'] in spent['A']:
				table.append( record )
				spent['A'].append( record['id'] )
	table = _.tables.returnSorted( 'table', 'a.title', table )
	for record in table:
		# _.printTest(record)
		# _.pr('HERE')
		printLevel( level, record )
		if not record['id'] in spent['B']:
			spent['B'].append(record['id'])
			process( level=level+1, parent=record['id'] )
		# printLevel( record['title'], level )

def printLevel( level, record ):
	global prefix
	global spent
	i=0
	pre = ''
	while not i == level:
		# _.pr('here', i, text, level)
		# sys.exit()
		pre += prefix
		i+=1
	if not record['id'] in spent['C']:
		spent['C'].append(record['id'])
		_.pr( record['id'], pre, record['title'], record['parent_id'] )
		# _.pr( record['type_'], pre, record['title'] )
		# _.pr( pre, record['title'] )

def process2( parent='' ):
	global data
	global spent
	table = []
	for record in data:
		# _.pr( record['parent_id'] )
		if record['parent_id'] == parent and not record['title'].endswith('.png') and not record['title'] == '?':
			if not record['id'] in spent['A']:
				record['children'] = process2( parent=record['id'] )
				table.append( record )
				spent['A'].append( record['id'] )
	return _.sort( table, 'type_,title' )

def printLevel2( records, level ):
	global prefix
	global spent
	i=0
	pre = ''
	while not i == level:
		# _.pr('here', i, text, level)
		# sys.exit()
		pre += prefix
		i+=1
	for record in records:
		if record['type_'] == 2:
			_.pr( pre, _.colorThis( record['title'], 'green', p=0 ) )
		elif record['type_'] == 1:
			_.pr( pre, _.colorThis( record['title'], 'white', p=0 ) )
		else:
			_.pr( pre, _.colorThis( record['title'], 'yellow', p=0 ) )
		printLevel2( records=record['children'], level=level+1 )

def action():
	global data
	global NewData
	load()
	standardize()
	_.printVarSimple( data )
	# NewData = process2()
	# printLevel2( records=NewData, level=0 )

def load():
	global data
	if _.switches.isActive( 'Folder' ):
		folder = _.switches.values( 'Folder' )[0]
	else:
		folder = os.getcwd()
	folder = _v.programs + _v.slash+'Joplin'+_v.slash+'export'+_v.slash
	folder = _v.programs + _v.slash+'Joplin'+_v.slash+'export'
	dirList = os.listdir(folder)
	for file in dirList:
		if file.endswith('.json'):
			data.append( _.getTable2( folder+_v.slash+file ) )
data = []
prefix = '  '
spent = []
spent2 = []
spent = {
			'A': [],
			'B': [],
			'C': [],
}
NewData = []

########################################################################################
if __name__ == '__main__':
	action()