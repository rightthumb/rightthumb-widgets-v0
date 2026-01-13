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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._date as _date
import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################
from datetime import datetime as dt, timedelta
import datetime
from datetime import date
##################################################

__.setting('receipt-log',True)

def appSwitches():
	_.switches.register('Ago', '-ago')
	_.switches.register('Date', '-date')
	_.switches.register('BackupRunOnce', '-include_once')
	_.switches.register('fileBackup-Log', '-fileBackupLog')
	



_.appInfo[focus()] = {
	'file': 'autoBackup.py',
	'description': 'Backup files since specified date',
	'categories': [
						'auto',
						'backup',
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

_.appInfo[focus()]['examples'].append('p autoBackup -date')

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
	_.defaultScriptTriggers()

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = True

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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


def ago():
	do = _.switches.value('Ago')
	if type(do) == int:
		return do
	if type(do) == float:
		return do
	do = do.lower()
	md = True
	# _.pr(do)
	# sys.exit()
	if ',' in do:
		d = do.lower().split(',')
		do = d[0]
		if 'cd' in d:
			md = False
	fnd = 'ymwd'
	nmb = do
	for t in fnd:
		nmb = nmb.replace(t,'')
	if len(nmb) == 0:
		nmb = 1
	try:
		nmb = int(nmb)
	except Exception as e:
		nmb = 1
	if 'y' in do:
		start_date = datetime.date.today() + datetime.timedelta(-365 * nmb)
	if 'm' in do:
		start_date = datetime.date.today() + datetime.timedelta(-30 * nmb)
	if 'w' in do:
		start_date = datetime.date.today() + datetime.timedelta(-7 * nmb)
	if 'd' in do:
		start_date = datetime.date.today() + datetime.timedelta(-1 * nmb)
	return start_date



def action():
	backupLog = _.tables.returnSorted( 'backupLog', 'a.timestamp', _.getTable('fileBackup.json') )
	schedulerLog = _.tables.returnSorted( 'schedulerLog', 'a.timestamp', _.getTable('fileBackupSchedule.json') )
	# backupLog = _.getTable('fileBackup.json')
	backupLog.reverse()
	maxEpoch = _.ago('1d')

	if _.switches.isActive('Ago'):
		maxEpoch = _.autoDate(_.resolveEpochTest(ago()))
		# _.pr( maxEpoch )
		# _.pr( _.autoDate(_.resolveEpochTest(maxEpoch)) )
		# sys.exit()

	if _.switches.isActive('Date'):
		maxEpoch = _.autoDate(_.resolveEpochTest( _.switches.value('Date') ))
	# _.pr()
	# _.pr( _.autoDate(_.resolveEpochTest(maxEpoch)), '\t', _.resolveEpochTest(maxEpoch) )
	# _.pr()
	# maxEpoch = _.autoDate(_.resolveEpochTest(maxEpoch))
	# date_modified_raw
	# _.pr( _.autoDate(_.resolveEpochTest(ago())), _.resolveEpochTest(ago()) )
	# maxEpoch = _.autoDate(_.resolveEpochTest(ago()))
	_.pr( 'maxEpoch:', maxEpoch, _.resolveEpochTest(maxEpoch) )
	# sys.exit()




	fileList = []
	runOnceFiles = []
	doNotBackup = []


	status = {
				'default': 0,
				'defaultSpent': 1,
				'defaultSpentAltID': 2,
				'defaultDeactivated': 33,

				'onceActive': 50,
				'onceSpent': 100,

				'onceDeactivated': 333,
	}

	# status['default']
	# status['defaultSpent']
	# status['onceActive']
	# status['onceSpent']



	# if _.switches.isActive('BackupRunOnce'):
	#     _.pr( 'BackupRunOnce: Active' )
	#     pause=input('pause')

	myFileLocations = _.getTable('myFileLocations.index')
	myFileLocationsFiles = []
	if _.switches.isActive('Ago'):
		for path in myFileLocations:
			if myFileLocations[path]['epoch'] > maxEpoch:
				myFileLocationsFiles.append(path)
	elif not _.switches.isActive('Ago'):
		for path in myFileLocations:
			if myFileLocations[path]['epoch'] > _.timeAgo('1d'):
				myFileLocationsFiles.append(path)
	_.pr(line=1)
	for path in myFileLocationsFiles:
		rec = myFileLocations[path]
		fileBackup=_fileBackup()
		if rec['session']:
			fileBackup.switch( 'Session', rec['session'] )
		fileBackup.switch( 'Input', path )
		fileBackup.do(     'action' )
	_.pr(line=1)

	for ii,log in enumerate(schedulerLog):
		if not 'status' in log:log['status'] = status['default'];
		if log['status'] == status['default'] or log['status'] == status['defaultSpent']:
			pass
		elif log['status'] == status['onceActive']:
			if _.switches.isActive('BackupRunOnce'):
				if not log['file'] in runOnceFiles:
					fileList.append( log['file'] )
					runOnceFiles.append( log['file'] )

					notice = _.colorThis( [  'Special: '  ], 'green', p=0 )
					notice += _.colorThis( [  log['file']  ], 'cyan', p=0 )
					_.pr( notice )
					fileBackup=_fileBackup()
					if 'session' in log:
						fileBackup.switch( 'Session', log['session'] )


					fileBackup.switch( 'Input', log['file'] )
					fileBackup.do(     'action' )
					del fileBackup
					fileBackup=None


					schedulerLog[ii]['status'] = status['onceSpent']


			else:
				if not log['file'] in doNotBackup:
					doNotBackup.append( log['file'] )



	
	_.pr( 'runOnceFiles:', runOnceFiles )
	_.pr( 'doNotBackup:', doNotBackup )
	try: _.pr( 'log:', log )
	except Exception as e: pass

	# pause=input('pause')

	maxEpochDate = _.resolveEpochTest( maxEpoch )

	# fileBackup.switch( 'isRunOnce', delete=True )

	i=0
	for ii,log in enumerate(schedulerLog):



		shoulRunPreGame = True
		if not 'status' in log:log['status'] = status['default'];
		if log['status'] == status['default'] or log['status'] == status['defaultSpent']:
			pass
		else:
			shoulRunPreGame = False

		# if _.resolveEpochTest( log['timestamp'] ) < maxEpochDate:
		# if ( log['timestamp'] ) < maxEpoch:
		#     shoulRunPreGame = False

		if log['file'] in fileList:
			shoulRunPreGame = False

		if shoulRunPreGame:



			shouldBackup = True

			if log['file'] in doNotBackup:
				shouldBackup = False



			if shouldBackup:
				if not os.path.isfile(log['file']): shouldBackup = False
				else:
					me = os.path.getmtime(log['file'])
					if not me: shouldBackup = False
					# if me > maxEpoch: shouldBackup = False
					# print(shouldBackup,maxEpoch,me,log['file'])

			if shouldBackup:
				
				fileList.append( log['file'] )
				if os.path.isfile(log['file']):
					# fd = _dir.fileInfo( log['file'] )
					fd = { 'date_modified_raw': os.path.getmtime( log['file'] ) }

					shoulRun = False
					try:
						if not type( fd['date_modified_raw'] ) == bool:
							shoulRun = True
						else:
							shoulRun = False
					except Exception as e:
						shoulRun = False


					if shoulRun:
						# if not _.resolveEpochTest(fd['date_modified_raw']) < maxEpochDate:

						if (log['timestamp']) > maxEpoch:
						# if True:
							i=0
							# _.pr( _.resolveEpochTest( fd['date_modified_raw'] ) )
							if True and ( not 'fileBackup.json' in log['file'] and not 'fileBackupSchedule.json' in log['file'] and not 'ID.sys' in log['file'] ):
								# _.pr( 'Scheduler: Start' )
								if not 'status' in log:log['status'] = status['default'];
								if log['status'] == status['default'] or log['status'] == status['defaultSpent']:

									# if 'netblock.py' in log['file']:
									#     _.pr( 'Scheduler', _.resolveEpochTest( log['timestamp'] ) )
									#     _.pr( _.resolveEpochTest(fd['date_modified_raw']), maxEpochDate )
									#     _.printTest( log )
									fileBackup=_fileBackup()
									if 'session' in log:
										fileBackup.switch( 'Session', log['session'] )

									fileBackup.switch( 'Input', log['file'] )
									fileBackup.do( 'action' )
									if log['status'] == status['default']:
										schedulerLog[ii]['status'] = status['defaultSpent']

										


								# _.pr( 'Scheduler: End' )
						else:
							pass
							if i > 25:
								break
							i+=1
	pass
	

	############################        ############################
	# _.pr( 'Should have backed up' )
	# pause=input('pause')

	for ii,log in enumerate(schedulerLog):
		if not log['file'] in __.spent:
			__.spent.append(log['file'])
			if not 'status' in log:log['status'] = status['default'];
			if log['status'] == status['default'] and log['file'] in fileList:
				schedulerLog[ii]['status'] = status['defaultSpentAltID']
				log['status'] = status['defaultSpentAltID']

			if log['status'] == status['default']:
				fileBackup=_fileBackup()
				if 'session' in log:
					fileBackup.switch( 'Session', log['session'] )


				fileBackup.switch( 'Input', log['file'] )
				fileBackup.do( 'action' )

				schedulerLog[ii]['status'] = status['defaultSpent']

	_.saveTable( schedulerLog, 'fileBackupSchedule.json', p=0, lock=True )
	if not _.switches.isActive('fileBackup-Log'): return None
	for log in backupLog:
		if not log['file'] in __.spent:
			__.spent.append(log['file'])
			# shoulRunPreGame = True

			# if log['status'] == status['default'] or log['status'] == status['defaultSpent']:
			#     pass
			# else:
			#     shoulRunPreGame = False

			# # if _.resolveEpochTest( log['timestamp'] ) > maxEpochDate:
			# if ( log['timestamp'] ) > maxEpoch:
			#     shoulRunPreGame = False

			# if log['file'] in fileList:
			#     shoulRunPreGame = False

			# if shoulRunPreGame:
			#     fileList.append( log['file'] )
			#     if os.path.isfile(log['file']):
			#         # fd = _dir.fileInfo( log['file'] )
			#         fd = { 'date_modified_raw': _.mod( log['file'] ) }
			#         # _.pr( log['file'] )
			#         shoulRun = False
			#         try:
			#             if not type( fd['date_modified_raw'] ) == bool:
			#                 shoulRun = True
			#             else:
			#                 shoulRun = False
			#         except Exception as e:
			#             shoulRun = False


			if not 'status' in log:log['status'] = status['default'];
			if log['status'] == status['default'] or log['status'] == status['defaultSpent']:
				pass
			else:
				shoulRunPreGame = False

			# if _.resolveEpochTest( log['timestamp'] ) < maxEpochDate:
			# if ( log['timestamp'] ) < maxEpoch:
			#     shoulRunPreGame = False

			if log['file'] in fileList:
				shoulRunPreGame = False

			if shoulRunPreGame:


				

				shouldBackup = True

				if log['file'] in doNotBackup:
					shouldBackup = False


				if shouldBackup:
					if not os.path.isfile(log['file']): shouldBackup = False
					else:
						me = os.path.getmtime(log['file'])
						if not me: shouldBackup = False
						if me > maxEpoch: shouldBackup = False
				if shouldBackup:

					fileList.append( log['file'] )
					if os.path.isfile(log['file']):
						# fd = _dir.fileInfo( log['file'] )
						fd = { 'date_modified_raw': os.path.getmtime( log['file'] ) }

						shoulRun = False
						try:
							if not type( fd['date_modified_raw'] ) == bool:
								shoulRun = True
							else:
								shoulRun = False
						except Exception as e:
							shoulRun = False


						if shoulRun:

						# fd['date_modified_raw']date_modified_raw
						# if shoulRun:
							# if not _.resolveEpochTest(fd['date_modified_raw']) < maxEpochDate:
							if (fd['date_modified_raw']) > maxEpoch:
								i=0
								_.pr( _.resolveEpochTest( fd['date_modified_raw'] ) )
								if not 'fileBackup.json' in log['file'] and not 'fileBackupSchedule.json' in log['file'] and not 'ID.sys' in log['file']:
									if not 'status' in log:log['status'] = status['default'];
									if log['status'] == status['default'] or log['status'] == status['defaultSpent']:
										pass
									if log['file'] in doNotBackup:
										_.colorThis( [   'Skipped:', log['file']    ], 'red' )
									else:

										if log['status'] == status['default'] or log['status'] == status['defaultSpent']:


											# if 'netblock.py' in log['file']:
											#     _.pr( 'Backup Log', _.resolveEpochTest( log['timestamp'] ) )
											#     _.pr( _.resolveEpochTest(fd['date_modified_raw']), maxEpochDate )
											#     _.printTest( log )
											fileBackup=_fileBackup()
											if 'session' in log:
												fileBackup.switch( 'Session', log['session'] )
											
											fileBackup.switch( 'Input', log['file'] )
											fileBackup.do( 'action' )

										else:
											_.colorThis( [   'Skipped:', log['file']    ], 'red' )
							else:
								pass
								if i > 25:
									break
								i+=1
								# _.pr(log['file'])
							# else:
								# _.pr( fd['date_modified'], log['file'] )
	pass
	# logFi = _v.tt+os.sep+'file-open'+os.sep+_.day()[:-1]+'.hash'
	def script(jsonFi):
		if os.path.isfile(jsonFi):
			_.pr('file-open:', jsonFi,c='yellow')
			table = _.getTable2(jsonFi)
			for path in table:
				a=False
				if not path in __.spent:
					a=True
					__.spent.append(path)
					sessions = []
					fileBackup = _fileBackup()
					fileBackup.switch( 'Session', '-'.join(table[path]) )
					fileBackup.switch( 'Input', path )
					fileBackup.do( 'action' )
				print(a,path)
			os.unlink(jsonFi)



	_.fo(_v.tt+os.sep+'file-open',script=script,r=1)
		
__.spent = []

def _fileBackup():
	
	_.v=_.dot()

	fileBackup.switch( 'Flag', 'A' )
	fileBackup.switch( 'DoNotSchedule' )
	fileBackup.switch( 'isRunOnce' )
	fileBackup.deleteSwitch( 'Session' )
	__.appReg=appReg
	return fileBackup
appReg=__.appReg
if 'fileBackup' in globals(): globals()['fileBackup'] = None
fileBackup = _.regImp( __.appReg, 'fileBackup' )
__.appReg=appReg

########################################################################################
if __name__ == '__main__':
	action()

# autoBackup
# if shouldBackup: