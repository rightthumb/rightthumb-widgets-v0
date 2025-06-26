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

import os, sys, time
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
	_.switches.register( 'Table', '-t,-table' )
	_.switches.register( 'myTables', '-tt' )
	_.switches.register( 'Local', '-local' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'tableDB.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'print tables',
	'categories': [
						'json',
						'tables',
						'vps',
						'web',
						'print',
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
						_.hp('p thisApp -file file.txt'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
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

simplejson = __.imp('simplejson')
# focus()

def process(data):
	records = []
	for rec in data:
		dic = {}
		for k in rec:
			saved = False
			for kk in [ 'status' ]:
				if k == kk:
					saved = True
					dic[k+'_'] = rec[k]
			if not saved:
				dic[k] = rec[k]
		records.append(dic)
	return records

			




def action():
	load()
	if _.switches.isActive('WebTable'):
		return None
	global data
	dataDump = simplejson.dumps(data, indent=4, sort_keys=False)
	if not dataDump:
		_.pr('[]')
	else:
		_.pr( dataDump )

	
def load():
	global data
	data = ''
	if _.switches.isActive('Local'):
		data = _.getTable2( _.switches.values('Table')[0] )
	elif _.switches.isActive('myTables'):
		data = _.getTable( _.switches.values('Table')[0] )
		# p = _v.myTables+os.sep+_.switches.values('Table')[0]
		# _.pr(os.path.isfile(p),p)
		# if os.path.isfile(p):
		#     data = _.getText( p )
	else:
		data = _.getTableDB( _.switches.values('Table')[0] )
		# p = _v.ttt +os.sep+ _.switches.values('Table')[0]
		# _.pr(os.path.isfile(p),p)
		# if os.path.isfile(p):
		#     data = _.getText( p )

	data = process(data)
	if len(data):
		keys = list( data[0].keys() )
		# _.pr('web',_.switches.values('WebTable'))
		if _.switches.isActive('WebTable'):
			# _.pr('spreadsheet.js')
			sheet = _.getText( 'spreadsheet.js' )
			spread = []
			test = '750DD885FC69'
			for line in sheet:
				line = line.replace('\n','')
				line = line.replace('\r','')
				if not test in line:
					spread.append(line)
				else:
					for k in keys:
						ln = line.replace( test, k )
						spread.append(ln)
			_.saveText( '\n'.join(spread), 'spreadsheet-'+_.switches.values('WebTable')[0]+'.js' )

			sheet = _.getText( 'index-helper.htm' )
			spread = []
			test = '750DD885FC69'
			for line in sheet:
				line = line.replace('\n','')
				line = line.replace('\r','')
				if not test in line:
					spread.append(line)
				else:
					for k in keys:
						ln = line.replace( test, k )
						spread.append(ln)
			_.saveText( '\n'.join(spread), 'index-helper-'+_.switches.values('WebTable')[0]+'.htm' )
			





########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







