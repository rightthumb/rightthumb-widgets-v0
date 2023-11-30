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



_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'history_index.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'History index tool',
	'categories': [
						'index',
						'history',
						'logs',
						'log',
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
						'p history_index',
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

def dx( ticket, dex, key, cmd, sw=None, val=None  ):

	global index_tickets
	global index_py_switches
	global index_cmd
	global index_py



	if not key == 'py':
		if not cmd in index_cmd:
			index_cmd[cmd] = {}
		if not ticket in index_cmd[cmd]:
			index_cmd[cmd][ticket] = {}

	if key == 'py':
		if not cmd in index_py_switches:
			index_py_switches[cmd] = {}

		if not cmd in index_py:
			index_py[cmd] = {}

		if not ticket in index_py[cmd]:
			index_py[cmd][ticket] = {}



	if not ticket in index_tickets:
		index_tickets[ticket] = {}

	if not key in index_tickets[ticket]:
		index_tickets[ticket][key] = {}

	if not cmd in index_tickets[ticket][key]:
		index_tickets[ticket][key][cmd] = {}
	
	if not sw is None:

		if not sw in index_tickets[ticket][key][cmd]:
			index_tickets[ticket][key][cmd][sw] = {}

		if not cmd in index_py_switches:
			index_py_switches[cmd] = {}

		if not sw in index_py_switches[cmd]:
			index_py_switches[cmd][sw] = {}

		if not ticket in index_py_switches[cmd][sw]:
			index_py_switches[cmd][sw][ticket] = {}



	if not key in dex:
		dex[key] = {}
	if not cmd in dex[key]:
		dex[key][cmd] = {}

	elif sw is None and not val is None:
		if not val in dex[key][cmd]:
			dex[key][cmd][val] = {}

	elif not sw is None and not val is None:
		if not sw in dex[key][cmd]:
			dex[key][cmd][sw] = {}
		if not val in dex[key][cmd][sw]:
			dex[key][cmd][sw][val] = {}
	elif not sw is None:
		if not sw in dex[key][cmd]:
			dex[key][cmd][sw] = {}

	return dex
def build_dex( code, ticket ):
	if _.switches.isActive('DoNotColorize'):
		return code
	
	dex = {}

		
	lastP=False
	lastSwitch=False
	lastCMD=False
	lastPipe=False
	last_CMD = ''
	last_Switch = ''
	last_CMD_Type = ''
	for i,x in enumerate(code.split(' ')):
		if x.lower() == 'p' or x.lower() == '%py%' or x.lower() == 'pp' or x.lower() == 'python' or x.lower() == 'python.exe' or x.lower().endswith('python.exe'):
			lastP = True
			lastSwitch = False
			lastPipe = False
			last_CMD_Type = 'py'
			# dex = dx( ticket, dex, key='cmd', cmd='p' )
		elif i == 0 or lastPipe:
			lastPipe = False
			lastCMD = True
			last_CMD = x
			last_CMD_Type = 'cmd'
			dex = dx( ticket, dex, key=last_CMD_Type, cmd=x )
		elif lastP:
			lastSwitch = False
			last_CMD = x
			dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD )
		elif x.startswith('+'):
			last_Switch = x
			lastSwitch = True
			dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD, sw=last_Switch )
		elif x.startswith('-'):
			last_Switch = x
			lastSwitch = True
			dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD, sw=last_Switch )
		elif x.startswith('/'):
			last_Switch = x
			lastSwitch = True
			dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD, sw=last_Switch )
		elif x == '|' or x == '&':
			lastCMD = False
			lastSwitch = False
			lastPipe = True
			
		elif lastSwitch:
			pass
			# dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD, sw=last_Switch, val=x )
			# _.pr( 'val', x, '\t\t', code )
		elif lastCMD:
			pass
			# dex = dx( ticket, dex, key=last_CMD_Type, cmd=last_CMD, val=x )

		if not x == 'p':
			lastP = False
	return dex

def extractDaysFromSession( row, ticket ):
	# row = row.replace( '2020.09.13 @ 7:55', '2020.09.17 @ 7:55' )

	result = []
	try:

		# _.pr( row )
		theDate = row.split('(')[1].split(')')[0]
		start = theDate.split('-')[0]
		end = theDate.split('-')[1]
		start = _str.cleanBE( start, ' ' )
		end = _str.cleanBE( end, ' ' )

		newStart = _.friendlyDate( _.autoDate( start ) ).split(' ')[0].replace( ' ', '' )
		newEnd = _.friendlyDate( _.autoDate( end ) ).split(' ')[0].replace( ' ', '' )

		result.append( newStart )

		if not newStart == newEnd:
			# _.pr( 'started' )
			thisDate = newStart
			while not thisDate == newEnd:
				# _.pr( 'pre', thisDate, newEnd )
				thisDate = str(_.dateAdd2( thisDate  , 1, delim='-' )).replace( ' ', '' )
				# _.pr( 'thisDate', thisDate, newEnd )
				if not thisDate in result:
					result.append( thisDate )



	except Exception as e:
		pass

	# _.pr(  'result', result  )
	# sys.exit()
	return result

def process( path, ticket ):

	global index_edit_files
	global index_edit_py
	global index_rename

	global index_day
	global index_tickets_day
	global index_day_edit

	global index_labs

	# _.colorThis( ['\n\n___________________________________________________________________________________________________________'], 'red' )
	file = _.getText( path, raw=True, clean=2 )
	for row in file.split('\n'):
		# if row.startswith('<'):
		#     _.pr( row )
		# if True:
		if not row.startswith('<'):
			if row.startswith('Session:'):
				days = extractDaysFromSession( row, ticket )
				if not days: continue
				for day in days:
					if not day in index_day:
						index_day[day] = {}
					if not ticket in index_day[day]:
						index_day[day][ticket] = {}

					if not ticket in index_tickets_day:
						index_tickets_day[ticket] = {}
					if not day in index_tickets_day[ticket]:
						index_tickets_day[ticket][day] = {}

				if 'isAdmin:True' in row:
					_.colorThis( row, 'Background.red' )

				else:
					_.colorThis( row, 'Background.green' )
			else:
				if _.showLine( row ):
					row = row.lower()

					row = row.replace( '&', ' & ' )
					row = row.replace( '|', ' | ' )
					row = _str.replaceDuplicate( row, ' ' )
					row = _str.cleanBE( row, ' ' )
					shouldDex = True
					editPy = None
					if row.startswith('rename'):
						if '.py' in row:
							rowSp = row.split(' ')
							rowSp[0] = rowSp[0].replace( '.py', '' )
							rowSp[1] = rowSp[1].replace( '.py', '' )

							if not rowSp[0] in index_rename:
								index_rename[ rowSp[0] ] = {}
							if not rowSp[1] in index_rename[ rowSp[0] ]:
								index_rename[ rowSp[0] ][ rowSp[1] ] = {}
							
							if not rowSp[1] in index_rename:
								index_rename[ rowSp[1] ] = {}
							if not rowSp[0] in index_rename[ rowSp[1] ]:
								index_rename[ rowSp[1] ][ rowSp[0] ] = {}

					elif row.startswith('epyi ') and '-build' in row:
						try:
							rowSp = row.split(' ')[3]
							rowSp = rowSp.replace( '.py', '' )
							editPy = rowSp
							if not rowSp in index_edit_py:
								index_edit_py[rowSp] = {}
							if not ticket in index_edit_py[rowSp]:
								index_edit_py[rowSp][ticket] = {}
						except Exception as e:
							_.pr( 'epyi', row )
							pass
					elif row.startswith('n ') and '.py' in row:
						try:
							rowSp = row.split('n ')[1]
							rowSp = rowSp.replace( '.py', '' )
							editPy = rowSp
							if not rowSp in index_edit_py:
								index_edit_py[rowSp] = {}
							if not ticket in index_edit_py[rowSp]:
								index_edit_py[rowSp][ticket] = {}
						except Exception as e:
							_.pr( 'n', row )
							pass
					elif row.startswith('epy ') or row.startswith('myepy '):
						try:
							rowSp = row.split('epy ')[1]
							rowSp = rowSp.replace( '.py', '' )
							editPy = rowSp
							if not rowSp in index_edit_py:
								index_edit_py[rowSp] = {}
							if not ticket in index_edit_py[rowSp]:
								index_edit_py[rowSp][ticket] = {}
						except Exception as e:
							_.pr( 'epy', row )
							pass
					
					if not editPy is None:
						try:
							for day in days:
								if not editPy in index_day_edit:
									index_day_edit[ editPy ] = {}
								if not day in index_day_edit[editPy]:
									index_day_edit[editPy][day] = {}
								if not ticket in index_day_edit[editPy][day]:
									index_day_edit[editPy][day][ticket] = {}
						except Exception as e:
							print('Err:',ticket)
						

					if shouldDex:
						dex = build_dex( row, ticket )

			# sys.exit()
def action():
	# if not _.switches.isActive('Select_I') and not _.switches.isActive('Count'):
	index_EPOCH = _.getTable( 'history_index(EPOCH).index' )

	if not _.switches.isActive('Sort'):
		_.switches.fieldSet( 'Sort', 'active', True )
		_.switches.fieldSet( 'Sort', 'value', 'desc.date_modified_raw' )
		_.switches.fieldSet( 'Sort', 'values', ['desc.date_modified_raw'] )

	if not _.switches.isActive('Ago'):
		
		_.switches.fieldSet( 'Ago', 'active', True )
		
		if not 'EPOCH' in index_EPOCH:
			_.switches.fieldSet( 'Ago', 'value', '1d' )
			_.switches.fieldSet( 'Ago', 'values', ['1d'] )
		else:
			_.switches.fieldSet( 'Ago', 'value', index_EPOCH['EPOCH'] )
			_.switches.fieldSet( 'Ago', 'values', [ index_EPOCH['EPOCH'] ] )

	load()


	global records
	
	global index_tickets
	global index_py_switches
	global index_cmd
	global index_py

	global index_edit_files
	global index_edit_py
	global index_rename

	global index_day
	global index_tickets_day
	global index_day_edit

	global index_labs


	

	for i,record in enumerate(records):
		process( record['path'], ticket=record['ticket'] )
	pass
	_.saveTable( index_py_switches, 'history_index[py-switches].index' )
	_.saveTable( index_edit_py, 'history_index[edit-py].index' )
	_.saveTable( index_cmd, 'history_index[cmd].index' )

	_.saveTable( index_edit_files, 'history_index[edit-files].index' )
	_.saveTable( index_tickets, 'history_index[tickets].index' )
	_.saveTable( index_rename, 'history_index[rename].index' )
	
	_.saveTable( index_day, 'history_index[day].index' )
	_.saveTable( index_tickets_day, 'history_index[tickets-day].index' )

	_.saveTable( index_day_edit, 'history_index[day-edit].index' )

	_.saveTable( index_labs, 'history_index[labs].index' )
	
	_.saveTable( {'EPOCH':time.time()}, 'history_index[EPOCH].index' )

def load():
	global records
	
	global index_tickets
	global index_py_switches
	global index_cmd
	global index_py

	global index_edit_files
	global index_edit_py
	global index_rename

	global index_day
	global index_tickets_day
	global index_day_edit

	global index_labs


	index_py_switches    = _.getTableDB( 'history_index[py-switches].index' )
	index_edit_py        = _.getTableDB( 'history_index[edit-py].index' )
	index_cmd            = _.getTableDB( 'history_index[cmd].index' )
	index_py             = _.getTableDB( 'history_index[py].index' )

	index_edit_files     = _.getTableDB( 'history_index[edit-files].index' )
	index_tickets        = _.getTableDB( 'history_index[tickets].index' )
	index_rename         = _.getTableDB( 'history_index[rename].index' )

	index_day            = _.getTableDB( 'history_index[day].index' )
	index_tickets_day    = _.getTableDB( 'history_index[tickets-day].index' )
	index_day_edit       = _.getTableDB( 'history_index[day-edit].index' )

	index_labs           = _.getTableDB( 'history_index[labs].index' )

	
	

	folder = _v.myTickets
	dirList = os.listdir(folder)
	for item in dirList:
		path = folder + _v.slash + item
		if os.path.isfile(path):
			shouldAdd = False
			if ( item.startswith('closed-') or item.startswith('open-') ) and item.endswith('.txt'):
				ticket = item
				ticket = ticket.replace( 'closed-', '' )
				ticket = ticket.replace( 'open-', '' )
				ticket = ticket.replace( '.txt', '' )
				
				shouldAdd = True
			if shouldAdd:
				shouldAdd = False
				record = _dir.fileInfo( path )
				record['ticket'] = ticket
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
index = {}


########################################################################################
if __name__ == '__main__':
	action()







