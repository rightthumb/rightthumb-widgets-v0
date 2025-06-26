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
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'Delete', '-rm,-r,-delete' )

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
	'file': 'backup-rm.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Can delete files from backup table and secure delete backup files',
	'categories': [
						'backup',
						'log',
						'delete',
						'tool',
						'manage',
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
						_.hp('p backup-rm -f %wprofile%\\projects\\project-log.txt -ago 10h'),
						_.hp('p backup-rm -f %wprofile%\\projects\\project-log.txt -ago 10h -rm'),
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

	if _.switches.isActive('Files'):
		backupLog = _.getTable('fileBackup.json')
		for path in _.switches.values('Files'):
			path = __.path(path)
			_.pr(path)
			# _.pr(type(_.switches.value('Ago')))
			# _.pr( _.isDate(_.switches.value('Ago'))['sdate'] )
			newLog=[]
			found=0
			for log in backupLog:
				delete=False
				if log['file'] == path and log['timestamp'] > _.switches.value('Ago'):
					delete=True
					_.pr( _.isDate(log['timestamp'])['sdate'] )
					found+=1
				# if log['file'] == path:
					# _.pr(log['backup'])
					# _.pr(_.switches.isActive('Ago'))
					# _.pr(log['timestamp'] < _.switches.isActive('Ago'))
					# _.pr(log['timestamp'] > _.switches.isActive('Ago'))
					# sys.exit()
				if _.switches.isActive('Delete'):
					if delete:
						if os.path.isfile(log['backup']):
							try:
								file_data = _.getText(log['backup'],raw=True)
							except Exception as e:
								file_data = open( log['backup'] , 'rb' ).read()
							# _.pr(type(file_data))
							newFile=''
							i=0
							for x in file_data:
								i+=1
								newFile+='0'

							_.saveText( newFile, log['backup'] )
							_.cp( ['secure',_.addComma(i)], 'green' )
							os.unlink(log['backup'])
							_.cp( [ 'deleted:', log['backup'] ], 'red' )
					else:
						newLog.append(log)



			if _.switches.isActive('Delete'):
				_.saveTable( newLog, 'fileBackup.json' )
			_.cp( ['',found], 'yellow' )
	# {
	#     "id": "{CE9728A3-099F-FB91-EA3A-67DC4E9E48FF}",
	#     "timestamp": 1376586282.0,
	#     "file": "D:\\projects\\backup_scripts\\Bud_Stansell\\server.bat",
	#     "backup": "D:\\.rightthumb-widgets\\hosts\\VULCAN\\backup\\txt\\1623522385.0573013-2013_08_15-13_04_42-server.bat",
	#     "mime": "text",
	#     "status": 1,
	#     "session": "",
	#     "version": "0.0.0.1",
	#     "v": 0,
	#     "v1": 0,
	#     "v2": 0,
	#     "v3": 1,
	#     "name": "server.bat",
	#     "flag": ""
	# }


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





