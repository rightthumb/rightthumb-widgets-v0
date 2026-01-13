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
##################################################
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
	_.switches.register( 'Widgets', '-w' )
	_.switches.register( 'Unlock', '-unlock' )
	_.switches.register( 'View', '-view' )
	_.switches.register( 'All', '-all' )
	_.switches.register( 'Timer', '-timer' )

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'lock-files.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'lock secure files',
	'categories': [
						'lock',
						'files',
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
						_.hp('p lock-files -w '),
						_.hp('p lock-files -w '),
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



def page_line():
	columns = os.get_terminal_size().columns
	num_underscores = max(0, columns - 5)
	return '_' * num_underscores


def process(table):
	for i,path in enumerate( table ):
		run = True
		if _.switches.isActive('Widgets'):
			run = False
			if path.lower().startswith(_v.w.lower()):
				run = True
		if not os.path.isfile(path):
			run=False
		if run:
			_.pr()
			fileBackup = _.regImp( focus(), 'fileBackup' )
			fileBackup.switch( 'Silent' )
			fileBackup.switch( 'Flag', 'lock' )
			fileBackup.switch( 'isRunOnce' )
			fileBackup.switch( 'DoNotSchedule' )
			fileBackup.switch( 'Input', path )
			if _.switches.isActive('Unlock'):
				fileBackup.switch( 'isPreOpen' )
			fb = fileBackup.action()
			_.pr(path)
			_.pr(fb)
			del fileBackup
			fileBackup=None

def view(table):
	global dirs
	global good
	global errors
	for i,path in enumerate( table ):
		run = True
		if _.switches.isActive('Widgets'):
			run = False
			if path.lower().startswith(_v.w.lower()):
				run = True
		if os.path.isdir(path): dirs.append(path)
		if os.path.isfile(path): good.append(path)
		else:  errors.append(path)



def action():
	if _.switches.isActive('View'):
		global dirs
		global good
		global errors
		dirs=[]
		good=[]
		errors=[]
		view(  _.getTable('crypt-docs.list')  )
		view(  _.getTable('secure-crypt-local.meta')  )
		# dirs=_.sort(dirs)
		# good=_.sort(good)
		# errors=_.sort(errors)
		for path in dirs: _.pr(path,c='darkcyan')
		for path in good: _.pr(path,c='cyan')

		if _.switches.isActive('All'):
			for path in errors: _.pr(path,c='red')
	else:
		timer = _v.stmp + os.sep + 'lock-files.timer'
		# print(timer); sys.exit();
		shouldRun = False
		if not _.switches.isActive('Timer'):
			shouldRun = True
		elif _.switches.isActive('Timer'):
			if not os.path.isfile(timer):
				shouldRun = True
			else:
				THREE_DAYS_IN_SECONDS = 3 * 24 * 60 * 60
				timeData = float(_.getText2( timer, 'text' ).strip())
				time_diff  = time.time() - timeData
				if time_diff  > THREE_DAYS_IN_SECONDS:
					shouldRun = True
				else:
					shouldRun = False
					time_remaining = THREE_DAYS_IN_SECONDS - time_diff
					days_remaining = int(time_remaining // (24 * 60 * 60))
					hours_remaining = int((time_remaining % (24 * 60 * 60)) // 3600)
					minutes_remaining = int((time_remaining % 3600) // 60)
					seconds_remaining = int(time_remaining % 60)

					# _.pr(f"\tlock-files timer: {days_remaining} days, "
					# 	f"{hours_remaining} hours, {minutes_remaining} minutes, "
					# 	f"{seconds_remaining} seconds.",c='Background.purple')

					_.pr(f"\tlock-files timer: {days_remaining} days, "
						f"{hours_remaining} hours",c='Background.purple')

		if shouldRun:
			_.pr(page_line(),c='Background.red')
			_.pr(page_line(),c='Background.red')
			_.pr()
			_.pr()
			if _.switches.isActive('Unlock'):
				_.pr('Unlocking Secure Files',c='Background.green')
			else:
				_.pr('Locking Secure Files',c='Background.green')
			_.pr()
			_.pr()
			if _.switches.isActive('Timer'): time.sleep(2)
			_.saveText( str(time.time()), timer )
			process(  _.getTable('crypt-docs.list')  )
			process(  _.getTable('secure-crypt-local.meta')  )
			_.pr()
			_.pr()
			_.pr('Secure Files Locked',c='Background.green')
			_.pr()
			_.pr()
			_.pr(page_line(),c='Background.red')
			_.pr(page_line(),c='Background.red')
			if _.switches.isActive('Timer'): time.sleep(2)





########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()