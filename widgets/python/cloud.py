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
	_.switches.register( 'Sync', '-sync' )
	_.switches.register( 'FixDates', '-dates' )
	_.switches.register( 'Upload', '-u,-up,-upload' )
	_.switches.register( 'Download', '-d,-dl,-down,-download' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Delete', '-del,-delete' )
	_.switches.register( 'UnDelete', '-ud,-udel,-udelete,-undel,-undelete' )
	


	_.switches.register( 'Folders', '-folder,-folders' )
	_.switches.register( 'Files', '-file,-files' )

	_.switches.register( 'PrintErrors', '-e' )
	

	# _.switches.register( 'SyncDates', '-syncdates' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.isRequired_or_List = ['Sync','FixDates','Files']
__.specifications['show_path_errors'] = False

_.appInfo[focus()] = {
	'file': 'cloud.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'synchronize folders and maintain databases over ssh/sftp ',
	'categories': [
						'synchronize',
						'sftp',
						'ssh',
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
						'p cloud -sync',
						'p cloud -sync -download',
						'p cloud -sync -upload',
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
	# _.switches.trigger( 'Files', _.myFileLocations )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
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
	ONLINE = _.ONLINE()
	s = ONLINE.status()
	if not s:
		_.cp( [ 'offline' ], 'red' )
		return None

	if _.switches.isActive('PrintErrors'):
		__.setting( 'print-errors' )
		# __.v.printErrors = True


	__.v.v = _.dot()
	__.v.v.cloud = _.dot()
	__.v.v.cloud.folder = _.switches.values('Folders')
	__.v.v.cloud.files = _.switches.values('files')

	# sys.exit()
	if _.switches.isActive('FixDates'):
		__.specifications['FixDates'] = True


	focus()
	if _.switches.isActive('Upload') or _.switches.isActive('Download'):
		_.switches.fieldSet( 'Sync', 'active', True )

	cloud = _cloud.Cloud()
	if _.isWin:
		cloud.folderGroup = 'windows-basic'
	else:
		cloud.folderGroup = 'linux-basic'

	if _.switches.isActive('Delete'):
		
		fileBackup = _.regImp( focus(), 'fileBackup' )
		fileBackup.switch( 'Silent' )
		fileBackup.switch( 'Flag', 'cloud.del' )
		fileBackup.switch( 'isRunOnce' )
		fileBackup.switch( 'DoNotSchedule' )
		
		delete_table = _.getTable( 'cloud.delete.json' )
		for i,path in enumerate(_.isData(r=1)):
			if os.path.isfile(path):
				path = os.path.abspath(path)
				paths = _cloud.gen_paths(path)

				fileBackup.switch( 'Input', path )
				paths['backup'] = fileBackup.do( 'action' )
				paths['record'] = _dir.info( path )
				if os.path.isfile(paths['backup']):
					os.unlink( paths['backup'] )
				try:
					os.link(path, paths['backup'])
					os.unlink( path )
					delete_table.append( paths )
					_.saveTable( delete_table, 'cloud.delete.json', p=0 )
					_.pr( 'Deleted:', path )
					# _.printVarSimple(paths)

				except Exception as e:
					_.colorThis( [ 'Error: backing up file, delete aborted' ], 'red' )
		
		sys.exit()
	if _.switches.isActive('UnDelete'):
		# sys.exit()
		fileBackup = _.regImp( focus(), 'fileBackup' )
		fileBackup.switch( 'Silent' )
		fileBackup.switch( 'Flag', 'cloud.del' )
		fileBackup.switch( 'isRunOnce' )
		fileBackup.switch( 'DoNotSchedule' )

		delete_table = _.getTable( 'cloud.delete.json' )
		for i,path in enumerate(_.isData(r=1)):
			if True:
				path = os.path.abspath(path)
				paths = _cloud.gen_paths(path)
				for i,deleted in enumerate(delete_table):
					if paths['cloud'] == deleted['cloud']:
						shouldRecover = True
						if os.path.isfile( deleted['local'] ):
							ask = 'NO'
							ask = input( 'File exists: ', deleted['cloud'], ' replace ? ' )
							if not 'y' in ask.lower():
								shouldRecover = False

						if shouldRecover:
							if os.path.isfile( deleted['backup'] ):
								if os.path.isfile( deleted['local'] ):
									fileBackup.switch( 'Input', path )
									backup_file = fileBackup.do( 'action' )
									_.pr( 'backup:', backup_file )
									os.unlink( deleted['local'] )

							try:
								os.link(deleted['backup'], deleted['local'])
								del delete_table[i]
								_.saveTable( delete_table, 'cloud.delete.json', p=0 )
								_.pr( 'Recovered:', path )
								# _.printVarSimple(delete_table)
							except Exception as e:
								pass

		pass
		sys.exit()        



	# ssh_server, ssh_user, ssh_password, db_server, db_user, db_password, db
	cloud.connect(
						ssh_server=        'tools.rightthumb.com',
						ssh_user=        'ximlickficfp',
						ssh_password=    _keychain.imp.key('cloud-ssh-pass'),
						db_server=        'localhost',
						db_user=        'scott_20',
						db_password=    _keychain.imp.key('cloud-db-pass'),
						db_name=        'tools_2020',
						db_prefix=        'cloud',
	)
	focus()
	if _.switches.isActive('Sync'):
		if not _.switches.isActive('Upload') and not _.switches.isActive('Download'):
			cloud.sync()
		if _.switches.isActive('Upload'):
			if _.switches.value('Upload') == 'no' :
				cloud.sync( upload=2 )
			else:
				cloud.sync( upload=True )
		if _.switches.isActive('Download'):
			if _.switches.value('Download') == 'no' :
				cloud.sync( download=2 )
			else:
				cloud.sync( download=True )
	if _.switches.isActive('FixDates'):
		cloud.syncDates()
	try:
		cloud.close()
	except Exception as e:
		pass

	try:
		cloud.sftp.close()
	except Exception as e:
		pass
	try:
		cloud.ssh.close()
	except Exception as e:
		pass
	# testA = 
	# testB = _.friendlyDate( testA )
	# _.pr( testA )
	# _.pr( testB )

	# _.printVarSimple( cloud.index )

import _rightThumb._vault as _vault
import _rightThumb._cloud as _cloud
import _rightThumb._dir as _dir
_keychain = _.regImp( __.appReg, 'keychain' )


# _cloud = _.regImp( __.appReg, '_rightThumb._cloud' )
# _vault = _.regImp( __.appReg, '_rightThumb._vault' )

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







