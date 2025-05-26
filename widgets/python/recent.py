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
# import platform
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
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'Dates', '-date,-dates,-between' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'BackupFile', '-f,-backup' )
	_.switches.register( 'ShowBackups', '-show' )



_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'recent.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'List of projects worked on recent',
	'categories': [
						'tool',
						'history',
						'fileBackup',
						'log',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						'p fileRecover',
						'p history',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p recent',
						'',
						'p recent -ago 45min',
						'p recent -ago 1h',
						'p recent -ago 1d',
						'p recent -ago 1w',
						'p recent -ago 1m',
						'p recent -ago 1y',
						'',
						'p recent + *.ps1 -ago 2w 1w',
						'p recent + *.ps1 -ago 2m 1m',
						'p recent + *.ps1 -ago 2y 1y',
						'',
						'p recent -between 2019-02-01 2019-03-01',
						'p recent -between 2019-02-01 2019-03-01 -backup',
						'p recent -between 2019-02-01 2019-03-01 -backup + *.txt',
						'',
						'p recent -ago 10y + *.py site-packages',
						'',
						'p recent | p files --c | p ls -s md -c n - .txt ',
						'p recent | p files --c | p ls -c ext | p countEach',
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
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()
# print(_.switches.values('Ago'))

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


def get_computer_name():
	import platform
	import socket
	if platform.system() == "Windows":
		computer_name = socket.gethostname()
	elif platform.system() == "Linux":
		computer_name = socket.gethostname()
	else:
		raise OSError("Unsupported operating system")
	return computer_name

def fileBackup_archive():
	parts = _v.myHome.split(os.sep)
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	pcFolder = os.sep.join( parts ) +os.sep+ get_computer_name() +os.sep+ 'tables'
	os.makedirs(pcFolder, exist_ok=True)
	return pcFolder + os.sep + 'fileBackup.json'


def clean_index(index):
	tmp = {}
	x = list(index.keys())
	x.sort()
	for y in x:
		tmp[y] = index[y]
	return tmp

def sorted_keys( index ):
	x = list(index.keys())
	x.sort()
	return x


def action():

	if _.switches.isActive('BackupFile') and not len(_.switches.values('BackupFile')):
		fB = _v.tt+__.os.sep+'fileBackup.json'
		_.switches.fieldSet( 'BackupFile', 'value', fB )
		_.switches.fieldSet( 'BackupFile', 'values', [fB] )

	if _.switches.isActive('ShowBackups'): load()


	dexy = {}
	_.fields.register( 'woy', 'val', 2, m=2 )
	_.fields.register( 'epoch', 'val', 12, m=12 )

	

	ago1 = None
	ago2 = None
	# _.pr(_.switches.value('Ago'))
	# _.pr(_.switches.values('Ago'))
	# sys.exit()
	if _.switches.isActive('Ago'):
		if len( _.switches.values('Ago') ) > 1:
			if not _.switches.values('Ago')[0] == _.switches.values('Ago')[1]:
				if _.switches.values('Ago')[0] < _.switches.values('Ago')[1]:
					ago1 = _.switches.values('Ago')[0]
					ago2 = _.switches.values('Ago')[1]
				else:
					ago1 = _.switches.values('Ago')[1]
					ago2 = _.switches.values('Ago')[0]
	if _.switches.isActive('Dates'):
		if len( _.switches.values('Dates') ) > 1:
			if not _.autoDate(_.switches.values('Dates')[0]) == _.autoDate(_.switches.values('Dates')[1]):
				if _.autoDate(_.switches.values('Dates')[0]) < _.autoDate(_.switches.values('Dates')[1]):
					ago1 = _.autoDate(_.switches.values('Dates')[0])
					ago2 = _.autoDate(_.switches.values('Dates')[1])
				else:
					ago1 = _.autoDate(_.switches.values('Dates')[1])
					ago2 = _.autoDate(_.switches.values('Dates')[0])
	# _.pr(ago1)
	# _.pr(_.friendlyDate(ago1))
	# _.pr(ago2)
	# _.pr(_.friendlyDate(ago2))
	# sys.exit()
	global default_days_ago

	# _.pr( fileBackup_archive(), os.path.isfile(fileBackup_archive()) )
	# sys.exit()
	if _.switches.isActive('BackupFile'):
		backupLog = _.getTable2(_.switches.value('BackupFile'))
	else:
		backupLog = _.getTable('fileBackup.json')

	# if os.path.isfile(fileBackup_archive()):
	#     backupLog = backupLog + _.getTable2( fileBackup_archive() )

	if _.switches.isActive('Ago'):
		ago = _.switches.value('Ago')
	elif _.switches.isActive('Dates'):
		ago = _.autoDate( _.switches.value('Dates') )
	else:
		ago = _.autoDate( _.dateSub( _.friendlyDate( time.time() ).split(' ')[0],'-', default_days_ago ) )

	index = {}

	# _.printVarSimple( backupLog[0] )


	# _.pr( ago )

	# sys.exit()

	# timestamp
	relevant = {}
	spent = []
	for record in backupLog:
		t = record['timestamp']
		should_include = False
		if not ago1 is None:
			if t > ago1 and t < ago2:
				should_include = True
				# _.pr( _.friendlyDate(record['timestamp']) )
		else:
			if t > ago:
				should_include = True
		if should_include:
			if 'profile\\backup\\txt' in record['file'].lower() or 'profile'+os.sep+'backup'+os.sep+'txt' in record['file'].lower(): should_include = False
			if 'profile\\backup\\bin' in record['file'].lower() or 'profile'+os.sep+'backup'+os.sep+'bin' in record['file'].lower(): should_include = False
		if should_include:
			woy = str(_dir.getYearFromEpoch( float(t) )) +'.'+ _.fields.padZeros( 'woy', 'val', int(_dir.getWOYFromEpoch(  float(t)  )) )
			
			day = _.friendlyDate(t).split(' ')[0]
			if not woy in index:
				index[woy] = {}
			if not day in index[woy]:
				index[woy][day] = {}
			if not record['file'] in index[woy][day]:
				if 'version' in record:
					index[woy][day][record['file']] = { 'backup': record['backup'], 'version': record['version'] }
				else:
					index[woy][day][record['file']] = { 'backup': record['backup'] }

				if not record['file'].lower() in relevant:
					relevant[ record['file'].lower() ] = 1

		# if record['file'].lower() in relevant:
		if not record['file'].lower() in dexy:
			dexy[ record['file'].lower() ] = {}
		timestamp = record['timestamp']
		if 'version' in record:
			dexy[ record['file'].lower() ][    _.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[0]  ) )+'.'+_.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[1]  ) )    ] = { 'backup': record['backup'], 'version': record['version'] }
		else:
			dexy[ record['file'].lower() ][    _.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[0]  ) )+'.'+_.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[1]  ) )    ] = { 'backup': record['backup'] }

	# _.printVarSimple( index )
	# _.printVarSimple( dexy )
	# sys.exit()
	backupSpent = []
	cnt = 0
	for woy in sorted_keys(index):
		cntA = 0
		for dayX in sorted_keys(index[woy]):
			for fileX in sorted_keys(index[woy][dayX]):
				if _.showLine( fileX ):
					# _.pr(fileX)
					cntA+=1
		if cntA:
			if not _.switches.isActive('Clean'):
				_.pr()
				_.pr()
				_.pr()
				_.pr()
				# _.pr( _.colorThis( woy, 'green', p=0 ) ,'   ', _.colorThis( _.addComma( len(index[woy]) ), 'blue', p=0 ),'   ', _.colorThis( _.addComma( cntA ), 'yellow', p=0 ) )
				diff_label = _.dateDiffText( time.time(), _.woy2date(woy) )
				if diff_label == 'tommorow' or diff_label == 'yesterday' or diff_label == 'today'or diff_label == 'next week':
					diff_label = 'this week'
				_.pr( _.colorThis(   diff_label, 'green', p=0   ) ,'   ', _.colorThis( _.addComma( len(index[woy]) ), 'blue', p=0 ),'   ', _.colorThis( _.addComma( cntA ), 'yellow', p=0 ) )
				# _.pr(_.woy2date(woy), _.friendlyDate(_.woy2date(woy)) )
				# _.pr( _.colorThis(   _.dateDiffText( time.time() ), 'green', p=0   ) ,'   ', _.colorThis( _.addComma( len(index[woy]) ), 'blue', p=0 ),'   ', _.colorThis( _.addComma( cntA ), 'yellow', p=0 ) )
				# _.pr( _.colorThis(   _.dateDiffText( _.woy2date(woy) ), 'green', p=0   ) ,'   ', _.colorThis( _.addComma( len(index[woy]) ), 'blue', p=0 ),'   ', _.colorThis( _.addComma( cntA ), 'yellow', p=0 ) )
			# _.printVarSimple( index )
			# _.printVarSimple( index[woy] )
			# sys.exit()
			for day in sorted_keys(index[woy]):

				cntB = 0
				for fileY in sorted_keys(index[woy][day]):
					if _.showLine( fileY ):
						# _.pr(fileY)
						cntB+=1
				if cntB:
					if not _.switches.isActive('Clean'):
						_.pr( _.colorThis( [ '\t', day ], 'white', p=0 ) ,'   ', _.colorThis( _.addComma( cntB ), 'yellow', p=0 ) )
					# _.colorThis(  [ '\t', day ], 'white'  )
					for file in sorted_keys(index[woy][day]):
						if _.showLine( file ):
							if not _.switches.isActive('Clean'):
								_.colorThis(  [ '\t\t', file ], 'cyan'  )
								cnt+=1
								if _.switches.isActive('BackupFile'):
									idex = index[woy][day][file]
									xXx = sorted_keys(dexy[ file.lower() ])
									if _.switches.isActive('ShowBackups'):
										if not idex['backup'] in backupSpent:
											backupSpent.append(idex['backup'])
											_.colorThis(  [ '\t\t\t', idex['version'], idex['backup'] ], 'darkcyan'  )
											# _.colorThis(  [ '\t\t\t', len(xXx) ], 'gray'  )
									# _.pr(xXx[len(xXx)-1])
									# _.pr(dexy[ file.lower() ][ xXx[len(xXx)-1] ])
									# _.colorThis(  [ '\t\t\t\t', dexy[ file.lower() ][ xXx[0] ] ], 'purple'  )
									dex = dexy[ file.lower() ][ xXx[len(xXx)-1] ]
									if _.switches.isActive('ShowBackups'):
										if not dex['backup'] in backupSpent:
											backupSpent.append(dex['backup'])
											_.colorThis(  [ '\t\t\t', dex['version'],dex['backup'] ], 'purple'  )
											_.colorThis(  [ '\t\t\t', len(xXx) ], 'gray'  )
							else:
								if not file in spent:
									spent.append(file)
									_.colorThis(  [ file ], 'cyan'  )
									cnt+=1
									if _.switches.isActive('BackupFile'):
										idex = index[woy][day][file]
										if _.switches.isActive('ShowBackups'):
											if not idex['backup'] in backupSpent:
												backupSpent.append(idex['backup'])
												_.colorThis(  [ '\t\t\t', idex['version'], idex['backup'] ], 'darkcyan'  )
										xXx = sorted_keys(dexy[ file.lower() ])
										# _.pr(xXx[len(xXx)-1])
										# _.pr(dexy[ file.lower() ][ xXx[len(xXx)-1] ])
										# _.colorThis(  [ '\t\t\t\t', dexy[ file.lower() ][ xXx[0] ] ], 'purple'  )
										dex = dexy[ file.lower() ][ xXx[len(xXx)-1] ]
										if _.switches.isActive('ShowBackups'):
											if not dex['backup'] in backupSpent:
												backupSpent.append(dex['backup'])
												_.colorThis(  [ '\t\t\t', dex['version'],dex['backup'] ], 'purple'  )
												_.colorThis(  [ '\t\t\t', len(xXx) ], 'gray'  )

	if not _.switches.isActive('Clean'):
		if _.switches.isActive('Ago'):
			_.pr()
			_.pr('Ago:')
			# _.pr( '  ', _.friendlyDate(ago) )
			if not ago1 is None:
				_.colorThis(  [ '  ', _.dateDiffText( ago2, ago1 ) ] , 'purple'   )
			else:
				_.colorThis(  [ '  ', _.dateDiffText( time.time(), ago ) ] , 'purple'   )
			_.colorThis(  [ '    ', _.friendlyDate(ago) ] , 'purple'   )
			_.pr()
		_.colorThis( [ 'found:', _.addComma(cnt) ], 'yellow' )


def load():
	_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )
	if _.switches.isActive('BackupFile'):
		_bkLog.imp.setBackupFile( _.switches.value('BackupFile') )
	# print(_bkLog.imp.autoFileVersion)
	_bkLog.do( _bkLog.imp.loadBackupFile )
	_bkLog.do( _bkLog.imp.autoFileVersion )
	# test = _bkLog.imp.backupLog
	# print(test)
	# _.isExit(__file__)



default_days_ago = 7
import _rightThumb._dir as _dir

# sorted_keys

########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)







