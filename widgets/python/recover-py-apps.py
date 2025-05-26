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
	_.switches.register( 'Date', '-date' )
	_.switches.register( 'Ago', '-ago' )
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='name', description='Files', isRequired=True )

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
	'file': 'recover-py-apps.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'recover a bunch of apps to a  specific date to test if legacy versions work',
	'categories': [
						'python',
						'py',
						'date',
						'restore',
						'recover',
						'list',
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
						_.hp('p recover-py-apps -date 2021-10-27 14:43:10 -f encryptString decrypt-docs fileBackup cryptFile secureFiles backupLog vault dir '),
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



def action():
	if _.switches.isActive('Ago'):
		ago = _.switches.value('Ago')
	if _.switches.isActive('Date'):
		ago = _.autoDate( ' '.join( _.switches.values('Date') ) )


	_.cp( _.isDate(ago)['fdate'], 'green' )


	done = []
	recover = {}
	backups = {}
	paths = []



	for path in _.switches.values('Files'):
		path = path.replace(os.sep+os.sep,os.sep)
		path = path.replace(os.sep+os.sep,os.sep)
		if _.isWin:
			path = path.lower()
		paths.append( path )
		fileBackup.switch( 'Input', path )
		fb = fileBackup.action()
		backups[path] = fb

		# _.pr(path)


	_.linePrint()
	_.pr( '#backups' )
	for f in backups:
		_.pr()
		_.pr(f)
		_.pr(backups[f])
	_.pr()

	# _.pv(paths)
	# _.pv(backups)
	log = _.tables.returnSorted( 'data', 'd.timestamp', _.getTable('fileBackup.json') )
	'''
			id
			timestamp
			file
			backup
			mime
			status
			name
			log
			session
			version
			v
			v1
			v2
			v3
			flag
	'''


	for rec in log:
		if _.isWin:
			f = rec['file'].lower()
		else:
			f = rec['file']
		f = f.replace(os.sep+os.sep,os.sep)
		# if not f in done and f in paths:
		# if 'decrypt-docs.py' in f:
		#     _.pr(f, f in paths)
		if f in paths:
			# _.pr(f)
			if not f in done and os.path.isfile(rec['backup']):
				recover[f] = rec['backup']

			if rec['timestamp'] < ago:
				if not f in done:
					done.append(f)
		if len(done) == len(paths):
			# _.e('done')
			# _.pr('break')
			break

	# _.pv(done)
	# _.pv(recover)
	_.linePrint()
	_.pr( '#restore' )
	for f in recover:
		_.pr()
		_.pr(f)
		_.pr(recover[f])
	_.pr()
	_.linePrint()



	ask=input('restore? Y/n: ')
	if not 'n' in ask.lower():
		_.pr()
		for f in recover:
			copyfile( recover[f], f )


		ask=input('back to original? Y/n: ')
		if not 'n' in ask.lower():
			for f in backups:
				copyfile( backups[f], f )



fileBackup = _.regImp( focus(), 'fileBackup' )
fileBackup.switch( 'Silent' )
fileBackup.switch( 'Flag', 'imdb' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )

from shutil import copyfile

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





