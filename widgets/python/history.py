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
	_.switches.register('Ago', '-ago','1m cd, 1y, 1d')
	_.switches.register('Count', '-count','2')
	_.switches.register('Select_I', '-i','0')
	_.switches.register('DoNotColorize', '-nocolor')
	_.switches.register('Copy', '+copy', 'inBackup -1')
	_.switches.register('App-Switches', '-sw','files.py')
	_.switches.register('Specify-App-Switches', '+sw','_-ago _+ (add _ to switch your searching for)')
	_.switches.register('Path', '-path')
	_.switches.register('TicketPath', '-tp')


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'history.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'History tail',
	'categories': [
						'log',
						'history',
						'tail',
						'logs',
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
						'',
						'p history',
						'p history + thunder',
						'',
						'p history -ago 1m + traverse',
						'',
						'p history -copy inBackup -1',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n', 'sort': '' },
						{ 'name': 'path', 'abbreviation': 'p', 'sort': '' },
						{ 'name': 'name', 'abbreviation': 'n', 'sort': '' },
						{ 'name': 'folder', 'abbreviation': 'f', 'sort': '' },
						{ 'name': 'bytes', 'abbreviation': 'b', 'sort': '' },
						{ 'name': 'size', 'abbreviation': 's', 'sort': 'bytes' },
						{ 'name': 'md5', 'abbreviation': '5', 'sort': '' },
						{ 'name': 'ext', 'abbreviation': 'e', 'sort': '' },
						{ 'name': 'year', 'abbreviation': 'y', 'sort': 'date_modified_raw' },
						{ 'name': 'date_modified', 'abbreviation': 'md,dm', 'sort': 'date_modified_raw' },
						{ 'name': 'date_created', 'abbreviation': 'cd,dc', 'sort': 'date_created_raw' },
						{ 'name': 'friendly_month', 'abbreviation': 'm', 'sort': 'date_modified_raw' },
						{ 'name': 'friendly_week', 'abbreviation': 'w', 'sort': 'date_modified_raw' },
						{ 'name': 'week_of_year', 'abbreviation': 'woy', 'sort': 'date_modified_raw' },
						{ 'name': 'day_of_the_week', 'abbreviation': 'dow', 'sort': 'date_modified_raw' },
						{ 'name': 'date_accessed', 'abbreviation': 'a,ad,da', 'sort': '' },
						{ 'name': 'movie', 'abbreviation': 'mv,mt', 'sort': '' },
						# { 'name': 'hash', 'abbreviation': '?', 'sort': '' },
					
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



import _rightThumb._dir as _dir

def colorize( code ):
	global history_items
	history_items.append( code )
	if _.switches.isActive('DoNotColorize'):
		return code
	result = ''
	
	colors = {
				'cmd': 'purple',
				'py': 'yellow',
				'pipe': 'red',
				'switches': 'green',
				'value': 'cyan',
	}

		
	lastP=False
	lastSwitch=False
	lastCMD=False
	lastPipe=False
	for i,x in enumerate(code.split(' ')):
		if x.lower() == 'p' or x.lower() == '%py%' or x.lower() == 'pp' or x.lower() == 'python' or x.lower() == 'python.exe' or x.lower().endswith('python.exe'):
			lastP = True
			result += _.colorThis( x, colors['cmd'], p=0 )
			lastSwitch = False
			lastPipe = False
		elif i == 0 or lastPipe:
			lastPipe = False
			lastCMD = True
			result += _.colorThis( x, colors['cmd'], p=0 )
		elif lastP:
			lastSwitch = False
			if not x in __.relevant_py and os.path.isfile(_v.py+os.sep+x+'.py'): __.relevant_py.append(x)
			result += _.colorThis( x, colors['py'], p=0 )
		elif x.startswith('+'):
			lastSwitch = True
			result += _.colorThis( x, colors['switches'], p=0 )
		elif x.startswith('-'):
			lastSwitch = True
			result += _.colorThis( x, colors['switches'], p=0 )
		elif x.startswith('/'):
			lastSwitch = True
			result += _.colorThis( x, colors['switches'], p=0 )
		elif x == '|' or x == '&':
			lastCMD = False
			lastSwitch = False
			lastPipe = True
			result += _.colorThis( x, colors['pipe'], p=0 )
		elif lastSwitch:
			result += _.colorThis( x, colors['value'], p=0 )
		elif lastCMD:
			result += _.colorThis( x, colors['value'], p=0 )
		else:
			result += x
		result += ' '

		if not x == 'p':
			lastP = False
	return result

def process( path ):
	ticket = path.split(os.sep)[-1].replace('.txt','')
	ticket = ticket.replace( 'closed-','' )
	if 'op' in ticket: tStatus = 'open'
	else: tStatus = 'closed'

	file = _.getText( path, raw=True, clean=2 )
	hasPrinted = False
	theTotal = 0
	for row in file.split('\n'):

		# if row.startswith('<'):
		#     _.pr( row )
		# if True:
		if not row.startswith('<'):
			if row.startswith('Session:'):
				hasPrinted = False
				
				if 'isAdmin:True' in row:
					# fileLabel = _.colorThis( row+'______________________________________ ______________________________________', 'Background.red', p=0 )
					# fileLabel = _.linePrint(p=0,c='Background.red')
					fileLabel = _.linePrint(p=0,c='red')
					header = _.pr( row, c='red', p=0 )
				else:
					# fileLabel = _.linePrint(p=0,c='Background.green')
					fileLabel = _.linePrint(p=0,c='green')
					header = _.pr( row.replace(' isAdmin:False', ''), c='green', p=0 )
					# fileLabel = _.colorThis( row, 'Background.green', p=0 )

			else:
				if _.showLine( row ):
					if not hasPrinted:
						hasPrinted = True
						# _.colorThis( ['\n\n___________________________________________________________________________________________________________'], 'red' )
						# _.pr(); _.pr(); _.linePrint(c='red');
						_.pr(); _.pr(); _.linePrint(c='white');
						_.pr( fileLabel )
						_.pr( header )
						if tStatus == 'open': _.pr( tStatus, c='red' )
						if _.switches.isActive('Path'): _.pr(path)

						# _.pr( ticket )
					if 'echo this is ' in row and 'test' in row and 'file.txt' in row and '>' in row and not 'force' in row.lower():
						pass
					else:
						row = row.replace( '&', ' & ' )
						row = row.replace( '|', ' | ' )
						row = _str.replaceDuplicate( row, ' ' )
						row = _str.cleanBE( row, ' ' )
						row = '    ' + colorize(row)
						_.pr( row )
						theTotal+=1
	pass
	_.saveText(__.relevant_py,_v.tt+os.sep+'history-relevant-py.list')
	if theTotal:
		_.cp( [ '', theTotal ], 'yellow' )
			# sys.exit()
def action():
	if _.switches.isActive('App-Switches') and _.switches.values('App-Switches'):
		sw = []
		if _.switches.isActive('Specify-App-Switches'):
			sw = _.switches.values('Specify-App-Switches')
			xsw=[]
			for s in sw:
				s=s.strip()
				while '  ' in s: s=s.replace('  ', ' ')
				if not ' ' in s:
					xsw.append(s)
				else:
					for w in s.split(' '):
						xsw.append(w)
			sw=xsw
			for i,s in enumerate(sw):
				sw[i]=s.replace('_','')


		_sw=_.getTableDB('history_index[py-switches].index')
		 

		for app in _.switches.values('App-Switches'):
			app=app.replace('.py','')
			if app in _sw:
				if not sw:
					for k in _sw[app]:
						_.pr(k)
				elif len(sw) == 1:
					for k in _sw[app]:
						if k in sw:
							for sess in _sw[app][k]:
								if _.switches.isActive('TicketPath'):
									o=_v.myTickets+os.sep+'open-'+sess+'.txt'
									c=_v.myTickets+os.sep+'closed-'+sess+'.txt'
									if os.path.isfile(o):
										_.pr('\t',sess,o)
									elif os.path.isfile(c):
										_.pr('\t',sess,c)
									else:
										_.pr('\t',sess)

								else:
									_.pr('\t',sess)
				else:
					sessions={}
					for k in _sw[app]:
						if k in sw:
							for sess in _sw[app][k]:
								if not sess in sessions: sessions[sess]=0
								sessions[sess]+=1
					for sess in sessions:
						if sessions[sess] >= len(sw):
							if _.switches.isActive('TicketPath'):
								o=_v.myTickets+os.sep+'open-'+sess+'.txt'
								c=_v.myTickets+os.sep+'closed-'+sess+'.txt'
								if os.path.isfile(o):
									_.pr('\t',sess,o)
								elif os.path.isfile(c):
									_.pr('\t',sess,c)
								else:
									_.pr('\t',sess)

							else:
								_.pr('\t',sess)


		return None


	# if not _.switches.isActive('Select_I') and not _.switches.isActive('Count'):

	if not _.switches.isActive('Sort'):
		_.switches.fieldSet( 'Sort', 'active', True )
		_.switches.fieldSet( 'Sort', 'value', 'desc.date_modified_raw' )
		_.switches.fieldSet( 'Sort', 'values', ['desc.date_modified_raw'] )

	if not _.switches.isActive('Ago'):
		_.switches.fieldSet( 'Ago', 'active', True )
		_.switches.fieldSet( 'Ago', 'value', '1d' )
		_.switches.fieldSet( 'Ago', 'values', ['1d'] )

	load()
	global records

	

	
	if _.switches.isActive('Count'):
		if _.switches.isActive('Sort'): records = _.tables.returnSorted( 'data', 'desc.date_modified_raw', records );
		mx = int( _.switches.values('Count')[0] )
		for i,record in enumerate(records):
			if i+1 > mx:
				break
			process( record['path'] )

	elif _.switches.isActive('Select_I'):
		if _.switches.isActive('Sort'): records = _.tables.returnSorted( 'data', 'desc.date_modified_raw', records );
		mx = int( _.switches.values('Select_I')[0] )
		# _.pr(mx)
		for i,record in enumerate(records):
			if i > mx:
				break
			if i == mx:
				process( record['path'] )

	else:
		if _.switches.isActive('Sort'): records = _.tables.returnSorted( 'data', 'asc.date_modified_raw', records );
		for i,record in enumerate(records):
			process( record['path'] )

	if _.switches.isActive('Copy'):
		global history_items
		last = 0
		if len(_.switches.values('Copy')) > 1:
			last = abs(int( _.switches.values('Copy')[1] ))
		ii = -1
		history_items.reverse()
		for i, item in enumerate(history_items):
			if _.showLine( item, _.switches.values('Copy')[0] ):
				ii+=1

			if ii == last:
				
				_.pr()
				_.pr()
				_.cp(  [ 'Copied:\n\t', item ]  , 'green' )
				_.setClip( item )
				break
	pass
	_.pr()
	_.pr()
	_.linePrint(c='darkcyan')
	# _.linePrint(c='darkcyan')
	_.pr()
	_.pr( '\thistory-relevant-py.list', c='cyan' )


def load():
	if os.path.isfile(_v.tt+os.sep+'history-relevant-py.list'):
		__.relevant_py=_.getText(_v.tt+os.sep+'history-relevant-py.list',raw=True,clean=2).split('\n')
	else: __.relevant_py=[]
	global records
	folder = _v.myTickets
	dirList = os.listdir(folder)
	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(path):
			shouldAdd = False
			if ( item.startswith('closed-') or item.startswith('open-') ) and item.endswith('.txt'):
				shouldAdd = True
			if shouldAdd:
				shouldAdd = False
				record = _dir.fileInfo( path )
				if _.switches.isActive('Ago'):

					run = 'default'
					if len( _.switches.values('Ago') ) > 1:
						if 'a' in _.switches.values('Ago')[1]:
							run = 'a'
						elif 'md' in _.switches.values('Ago')[1]:
							run = 'md'
						elif 'cd' in _.switches.values('Ago')[1]:
							run = 'cd'
						elif 'resent' in _.switches.values('Ago')[1]:
							run = 'resent'

					# _.pr(  len( _.switches.values('Ago') )  )
					# _.pr(  ( _.switches.values('Ago') )  )
					# sys.exit()
					# accessed_raw


					if run == 'default':
						# _.pr(record['date_modified_raw'])
						# _.pr(_.switches.values('Ago'))
						if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True
					elif run == 'resent':
						if record['date_modified_raw'] > _.switches.values('Ago')[0] or record['date_created_raw'] > _.switches.values('Ago')[0] or record['accessed_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True
					elif run == 'a':
						if record['accessed_raw'] > _.switches.values('Ago')[0]:
							# _.pr( _.friendlyDate(_.switches.values('Ago')[0]), _.switches.values('Ago')[0], record['accessed_raw'], _.friendlyDate(record['accessed_raw']) )
							shouldAdd = True
					elif run == 'cd':
						if record['date_created_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True
					elif run == 'md':
						if record['date_modified_raw'] > _.switches.values('Ago')[0]:
							shouldAdd = True



			if shouldAdd:
				records.append(record)


records = []
history_items = []


########################################################################################
if __name__ == '__main__':
	action()








