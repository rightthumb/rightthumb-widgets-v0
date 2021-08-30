import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import sys
import time
import platform

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
import requests
##################################################



__.testing = [ 'invoke_shell' ]
__.testing = []
# 











def appSwitches():
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )
	### EXAMPLE: END


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '_cloud.py',
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
# 	if os.path.isdir( row ):
# 	if os.path.isfile( row ):
#	os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START



class Cloud:
	def __init__( self  ):

		delete = _.getTableDB( 'delete.index' )
		self.delete = {}
		for d in delete:
			f = _v.resolveFolderIDs( d )
			if _.isWin:
				f = f.lower()
			self.delete[f] = 1
			if os.path.isfile(f):
				os.unlink(f)
				_.cp( [ 'deleted, local:', f ], 'red' )
		_.colorThis( 'status: start', 'yellow' )
		self.index = { 'local': {}, 'remote': {} }

		if platform.system() == 'Windows':
			theOS = 'unity'
		else:
			theOS = 'unity'
		user = 'ximlickficfp'

		self.folderGroup = 'linux-basic'

		self.cloud_sync_index = _v.myTables+_v.slash+'cloud_sync.index'
		self.transfer_success = False

		self.folder_check = { 'remote': [], 'local': [] }

		self.sync_index = None

		self.replace_all_files = { 'remote': None, 'local': None }

		self.ftp_status = False

		self.structure = {
						'remote': {
							'base': '/home/'+user+'/cloud',
							'config': '/home/'+user+'/cloud/config',
							'files': '/home/'+user+'/cloud/files',
							'tech': '/home/'+user+'/cloud/files/tech',
							'backup': '/home/'+user+'/cloud/files/backup',
							'backup-txt': '/home/'+user+'/cloud/files/backup/txt',
							'backup-bin': '/home/'+user+'/cloud/files/backup/binary',
							'programs': '/home/'+user+'/cloud/files/tech/programs',
							# 'python': '/home/'+user+'/cloud/files/tech/programs/python',
							'bash': '/home/'+user+'/cloud/files/tech/programs/bash',
							'batch': '/home/'+user+'/cloud/files/tech/programs/batch',
							'web': '/home/'+user+'/public_html',
							# 'shell': '/home/'+user+'/cloud/files/tech/programs/webApps/shell',
						},
						'local': {
							'tech': _v.techFolder,
							'programs': _v.programs,
							'python': _v.programs +_v.slash+ 'python' +_v.slash+ 'src' +_v.slash+ 'unity',
							'bash': _v.programs +_v.slash+ 'bash',
							'batch': _v.programs +_v.slash+ 'batch',
							'powershell': _v.programs +_v.slash+ 'powershell',
							'javascript': _v.programs +_v.slash+ 'javascript',
							'library': _v.programs +_v.slash+ 'library',
							'remote.app': _v.programs +_v.slash+ 'remote',
							'documentation': _v.programs +_v.slash+ 'documentation',
							'shell': _v.programs +_v.slash+ 'webApps' + _v.slash + 'shell',
							'databank_tables': _v.programs +_v.slash+ 'databank'  +_v.slash+ 'tables' ,
							'ssl_keys': _v.programs +_v.slash+ 'keys'  +_v.slash+ 'ssl' ,
							'databank_db_vault': _v.programs +_v.slash+ 'databank'  +_v.slash+ 'vault' ,
							'databank_db_indexes': _v.programs +_v.slash+ 'databank'  +_v.slash+ 'indexes' ,
						}

		}
		__.cloud.structure = self.structure

		# self.index['local'] = []
		self.counter = { 'files': 0, 'folders': 0 }
		self.program_folders = []
		self.program_folders_active = []
		

	def find_program_folders( self ):
		self.program_folders = []
		for x in os.listdir( _v.programs ):
			y = _v.programs + _v.slash + x + _v.slash
			if os.path.isdir( y ):
				self.program_folders.append(  __.cloud.db.gen_paths(y)['cloud']  )
		__.cloud_program_folders = self.program_folders
		# _.printVarSimple(self.program_folders)
		# sys.exit()
	
	def connect( self, ssh_server, ssh_user, ssh_password, db_server, db_user, db_password, db_name='tools_2020', ssh_port=22, db_port=3306, db_prefix=None ): # ? db_port=3308
		_.colorThis( 'status: connecting', 'yellow' )
		self.server = ssh_server
		self.user = ssh_user
		self.ssh_port = ssh_port
		# completed_success() completed_error()
		try:
			pass
		except Exception as e:
			_.cp( '.', 'red' )
			# _.colorThis( 'Error:', 'red' )
			# print( '\t', e )

		_.colorThis( 'status: db connecting', 'yellow' )


		if not 'invoke_shell' in __.testing:
			if not 'testing' in __.specifications:
				self.db( ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix )




		_.colorThis( 'status: db initialized', 'yellow' )
		# print()
		# print()
		# test = __.cloud.db.search_table_version('files')
		# print(test)
		# _.printVarSimple(__.cloud.db.table_fields)
		# _.printVarSimple(test)
		# # print(test)
		# print()
		# print()



		# __.cloud.COMPLETED = True
		# return None



		# time.sleep(3)

		self.ssh_connection(ssh_password)
		if 'invoke_shell' in __.testing:
			self.invoke( '~/cloud/files/tech/programs/remote/bash/p.sh files -save -folder ~/cloud/files/tech/programs --c' )
			self.ftp()

			if os.path.isfile( _v.stmp +_v.slash+ 'cloud.cache' ):
				print( 'cleared cache' )
				os.unlink( _v.stmp +_v.slash+ 'cloud.cache' )

			time.sleep(.5)
			print(  )
			print( '~/cloud/files/tech/programs/remote/files-last.json' )
			print( _v.stmp +_v.slash+ 'cloud.cache' )
			print(  )
			# result = self.sftp.get(   '~/cloud/files/tech/programs/remote/files-last.json'   ,   _v.stmp +_v.slash+ 'cloud.cache'   )
			result = self.sftp.get(   '/home/ximlickficfp/cloud/files/tech/programs/remote/files-last.json'   ,   _v.stmp +_v.slash+ 'cloud.cache'   )
			print(_v.stmp +_v.slash+ 'cloud.cache')
			try:
				self.sftp.close()
			except Exception as e:
				pass
			try:
				self.ssh.close()
			except Exception as e:
				pass

			sys.exit()

		_.colorThis( 'status: ssh connected', 'yellow' )
		__.cloud.db.insert( 'connection', { 'unixID': _v.unixID, 'zone': __.cloud.tz, 'sessionID': __.cloud.sessionID } )
	
	def invoke( self, cmd ):
		# https://stackoverflow.com/questions/8783009/how-to-execute-a-script-remotely-in-python-using-ssh
		chan = self.ssh.invoke_shell()
		# chan.send( cmd )
		# chan.send('cd ~/cloud/files/tech/programs' + '\n')
		time.sleep(.2)
		chan.send(cmd + '\n')
		time.sleep(2)
		buff = ''
		while chan.recv_ready():
			print('Reading buffer')
			resp = chan.recv(9999)
			buff = resp.decode()
			print(resp.decode())


			time.sleep(2)

		print('\nCommand was successful: \n  ' + cmd)
		print()
		# print('Command was successful: ' + cmd)

	def ssh_connection( self, ssh_password ):
		# return None
		self.ssh=paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		task_completed = False
		while not task_completed:
			try:
				self.ssh.connect( hostname=self.server, username=self.user, password=ssh_password, port=self.ssh_port )
			except Exception as e:
				task_completed = actionRequest( 'Cloud', 'ssh_connection', error=e )
			else:
				actionRequest( 'Cloud', 'connect', success=True)
				task_completed = True

		if 'testing' in __.specifications:
			pass
			pass
			pass
			self.ftp()

			remote_table_remote = '~/cloud/share/remote.table'
			remote_table_local = _v.stmp +_v.slash+ 'cloud-remote.table'
			if os.path.isfile(remote_table_local):
				os.unlink(remote_table_local)
			exists = True
			while exists:
				try:
					self.sftp.stat( remote_table_remote )
					self.sftp.remove( remote_table_remote )
				except Exception as e:
					pass
				time.sleep(.5)
				try:
					self.sftp.stat( remote_table_remote )
					exists = True
				except Exception as e:
					exists = False


			exists = False
			while not exists:
				print( 'indexing cloud' )
				stdin, stdout, stderr = self.ssh.exec_command('sh ~/cloud/files/tech/programs/remote/bash/p.sh index')
				time.sleep(.5)
				try:
					print(  self.sftp.stat( remote_table_remote )  )
					exists = True
				except Exception as e:
					exists = False
				
			task_completed = False
			while not task_completed:
				try:
					print(  self.sftp.get(   remote_table_remote   ,   remote_table_local   )  )
					time.sleep(.5)
					if not os.path.isfile(remote_table_local):
						raise TypeError("Download Error")
				except Exception as e:
					task_completed = actionRequest( 'Cloud', 'download', action=remote_table_remote, error=e )
				else:
					actionRequest( 'Cloud', 'download', action=remote_table_remote, success=True)
					task_completed = True


			time.sleep(.5)
			print(  'file:',os.path.isfile(remote_table_local)  )
			remote_table = _.getTable2( remote_table_local )
			remote_index = {}
			for i,record in enumerate(remote_table):
				# paths = __.cloud.db.gen_paths( record['path'] )
				paths = gen_paths( record['path'] )
				remote_index[ paths['cloud'] ] = record
				if not i:
					_.printVarSimple( record )
					_.printVarSimple( paths )


			pass
			__.local_table = []
			getFolder( self.structure['local']['python'] )
			getFolder( self.structure['local']['bash'] )
			getFolder( self.structure['local']['library'] )
			getFolder( self.structure['local']['batch'] )
			getFolder( self.structure['local']['remote.app'] )
			getFolder( self.structure['local']['powershell'] )
			getFolder( self.structure['local']['javascript'] )
			getFolder( self.structure['local']['documentation'] )
			getFolder( self.structure['local']['databank_tables'] )
			getFolder( self.structure['local']['ssl_keys'] )
			getFolder( self.structure['local']['databank_db_vault'] )
			getFolder( self.structure['local']['databank_db_indexes'] )
			
			print(__.v.secure.sync)

			for sec_file in __.v.secure.sync:
				print(sec_file)
				addThisFile( sec_file )


			action_table = {
								'upload': {},
								'download': {}
			}
			local_index = {}
			for local in __.local_table:
				paths = gen_paths( local['path'] )
				local_index[paths['cloud']] = local
				if paths['cloud'] in remote_index:
					# compare_date_local = _tz.convert( local['modified'], local['tz'], remote_index[paths['cloud']]['tz'] )
					compare_date_remote = _tz.convert( remote_index[paths['cloud']]['tz'], remote_index[paths['cloud']]['tz'], local['tz'] )
					if not local['modified'] == compare_date_remote:
						print( local['modified'], compare_date_remote, paths['cloud'] )
						if 'FixDates' in __.specifications:
							pass
							# os.utime(local['path'],(compare_date_remote, compare_date_remote))
						elif 'FixDates' in __.specifications:
							if not local['modified'] > compare_date_remote:
								print( 'upload', paths['cloud'] )
								action_table['upload'][paths['cloud']] = {
																			'local': local,
																			'remote': remote_index[paths['cloud']],
								}
							else:
								print( 'download', paths['cloud'] )
								action_table['download'][paths['cloud']] = {
																			'local': local,
																			'remote': remote_index[paths['cloud']],
								}

			pass
			if 'FixDates' in __.specifications:
				try:
					self.sftp.close()
				except Exception as e:
					pass
				self.ssh.close()
				sys.exit()






			pass
			# remote_index = _.getTable2( remote_table_local )
			# _.printVarSimple( remote_index )
			# _.printVarSimple( _dir.info(remote_table_local) )

				
			# print( 'DONE' )
			# stdin, stdout, stderr = self.ssh.exec_command(  open("D:\\tech\\programs\\python.remote\\run.sh").read()  )
			# print('__________________________________________')
			# print(stdin)
			# print('__________________________________________')
			# print(stdout)
			# print('__________________________________________')
			# print(stderr)
			# print('__________________________________________')
			# print( result )
			try:
				self.sftp.close()
			except Exception as e:
				pass
			self.ssh.close()
			sys.exit()
			pass
			pass
			pass

	def syncDates( self ):
		_.colorThis( 'status: sftp indexing', 'yellow' )

		print( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files' )

		for record in __.cloud.db.query( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files', 'files' ):
			print(record)
			paths = __.cloud.db.gen_paths( record['cloud_path'] )
			record['local'] = paths['local']
			record['remote'] = paths['remote']
			self.index['remote'][ paths['cloud'] ] = record


		_.colorThis( 'status: synchronizing dates', 'yellow' )
		print(self.index['remote'])
		for rp in self.index['remote']:
			rec = self.index['remote'][rp]
			paths = __.cloud.db.gen_paths( rp )
			print(paths['local'])
			_.changeM( paths['local'], rec['modified'] )
			_.changeC( paths['local'], rec['created'] )
			# changeM( paths['local'], rec['modified'] )

		__.cloud.COMPLETED = True
	def ftp( self ):
		if not self.ftp_status:
			self.ftp_status = True
			task_completed = False
			while not task_completed:
				try:
					self.sftp=self.ssh.open_sftp()
				except Exception as e:
					task_completed = actionRequest( 'Cloud', 'ssh.open_sftp', error=e )
				else:
					actionRequest( 'Cloud', 'ssh.open_sftp', success=True)
					task_completed = True

			_.colorThis( 'status: sftp connected', 'yellow' )



	def sync( self, upload=None, download=None, close=True ):
		if upload is None and download is None:
			upload = True
			download = True
		if upload == 2 or download == 2:
			updateDate = False
		else:
			updateDate = True
		self.ftp()
		_.colorThis( 'status: sftp indexing', 'yellow' )
		self.build_indices()
		_.colorThis( 'status: sftp update deleted', 'yellow' )
		print('skipped')
		# self.updateDeleted()

		if upload:
			_.colorThis( 'status: sftp uploading', 'yellow' )
			self.sync_up()
		if download:
			_.colorThis( 'status: sftp downloading', 'yellow' )
			self.sync_down()
		_.colorThis( 'status: sftp complete', 'yellow' )
		if updateDate:
			__.cloud.db.insert( 'synchronized', { 'unixID': _v.unixID, 'epoch': time.time(), 'sessionID': __.cloud.sessionID }, 'unixID' )
		if close:
			_.colorThis( 'status: sftp closing', 'yellow' )

			task_completed = False
			while not task_completed:
				try:
					self.sftp.close()
				except Exception as e:
					task_completed = actionRequest( 'Cloud', 'sftp.close', error=e )
				else:
					actionRequest( 'Cloud', 'sftp.close', success=True)
					task_completed = True

			_.colorThis( 'status: ssh closing', 'yellow' )

			task_completed = False
			while not task_completed:
				try:
					self.ssh.close()
				except Exception as e:
					task_completed = actionRequest( 'Cloud', 'ssh.close', error=e )
				else:
					actionRequest( 'Cloud', 'ssh.close', success=True)
					task_completed = True

			
		__.cloud.COMPLETED = True

	def evaluate( self, path ):
		paths = paths = __.cloud.db.gen_paths( path )
		l = paths['local']
		epoch = __.cloud.epoch
		if epoch is None or type(epoch) == bool or epoch == 'false':
			epoch = None
		if __.setting( 'print-errors' ):
			if not __.setting('printed-epoch'):
				__.setting('printed-epoch',1)
				print( 'epoch:', epoch )
		isNew = True
		if os.path.isfile(l):
			if paths['cloud'] in self.index['remote']:
				isNew = False
				rm = self.index['remote'][paths['cloud']]['modified']
				rc = self.index['remote'][paths['cloud']]['created']
				rtz = self.index['remote'][paths['cloud']]['tz']
				# changeM(  l, rm  )
				# changeC(  l, rc  )
				info = _dir.info(l)
				# diff = _.dateDiff( info['me'], _tz.convert( rm, rtz, __.cloud.tz ) )
				if rm > info['me']:
					newer = 'r'
				elif rm < info['me']:
					newer = 'l'
				else:
					newer = 's'
		if isNew:
			newer = 'n'
		return newer
			# print( diff, _.friendlyDate(info['me']), _.friendlyDate(rd) )


	def recursiveRemoteIndex( self, epoch=None ):


		# print( self.folderGroup )
		folderGroups = groupFoldersList( self.folderGroup )
		for x in self.program_folders_active:
			if not x in folderGroups:
				folderGroups.append(x)
		xx = []
		for x in folderGroups:
			xx.append('cloud_path LIKE "%'+x+'%"')


		sql = 'SELECT * FROM '+__.cloud.db.table_prefix+'_files WHERE eol=0 AND ' + ' OR '.join( xx )
		# print(sql)
		isFirst = True

		if False:
			for record in __.cloud.db.query( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files WHERE eol=1', 'files' ):
				if isFirst:
					isFirst = False

					fileBackup = _.regImp( focus(), 'fileBackup' )
					fileBackup.switch( 'Silent' )
					fileBackup.switch( 'Flag', 'cloud.del' )
					fileBackup.switch( 'isRunOnce' )
					fileBackup.switch( 'DoNotSchedule' )

				paths = __.cloud.db.gen_paths( record['cloud_path'] )
				record['local'] = paths['local']
				record['remote'] = paths['remote']

				# if not os.path.isfile( record['local'] ):
				# 	print( record['local'] )
				if os.path.isfile( record['local'] ):
					print( 'del', record['local'] )
					# fileBackup.switch( 'Input', record['local'] )
					# backup_file = fileBackup.do( 'action' )
					# if os.path.isfile(backup_file):
					# 	os.unlink(backup_file)
					# os.link( record['local'], backup_file )
					# print( 'backup:', backup_file )
					# os.unlink( record['local'] )


		# for record in __.cloud.db.query( sql, 'files' ):
		for record in __.cloud.db.query( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files WHERE eol=0', 'files' ):
			paths = __.cloud.db.gen_paths( record['cloud_path'] )
			record['local'] = paths['local']
			record['remote'] = paths['remote']
			self.index['remote'][ record['cloud_path'] ] = record

	def remoteExist( self, file ):
		try:
			self.sftp.stat(file)
			return True
		except IOError:
			return False

	def updateDeleted( self ):
		delete_table = _.getTable( 'cloud.delete.json' )
		for i,deleted in enumerate(delete_table):
			if self.remoteExist( deleted['remote'] ):
				__.cloud.db.insert( 'files', { 'cloud_path': deleted['cloud'], 'unixID': _v.unixID, 'eol': 1 }, key='cloud_path' )
				paths = __.cloud.db.gen_paths( deleted['cloud'] )


				nParts = paths['cloud'].split('/')
				nParts.reverse()
				file_name = nParts.pop(0)
				backup_name = self.structure['remote']['backup-txt'] + '/' + str(__.cloud.now) + '-' + formatDate( deleted['record']['me'] ) +  '-' + file_name
				
				backup_record = {
									'file': paths['cloud'],
									'backup': backup_name,
									'created': deleted['record']['ce'],
									'modified': deleted['record']['me'],
									'tz': str(time.strftime("%z")).replace(':',''),
									'mime': 'text',
									'flag': '',
									'unixID': _v.unixID,
									'terminalID': '',
									'sessionID': __.cloud.sessionID,
				}

				task_completed = False
				while not task_completed:
					try:
						self.sftp.rename(paths['remote'], backup_name)
					except Exception as e:
						task_completed = actionRequest( 'Cloud', 'upload', action=paths['cloud'], error=e )
					else:
						actionRequest( 'Cloud', 'upload', action=paths['cloud'], success=True)
						task_completed = True


						__.cloud.db.insert( 'backup', backup_record )





	def fileLocalIndex( self, path, base=None, plus=None, minus=None, plusOr=None, first=True, epoch=None ):
		# print(path)
		__.v.fileLocalIndex = {}
		__.v.fileLocalIndex['base'] = base
		__.v.fileLocalIndex['epoch'] = epoch
		# print( 'isfile:', epoch, _.friendlyDate(epoch), path )
		includeThis = False
		if plus is None and minus is None:
			includeThis = True
		else:
			includeThis = _.showLine( path )

		if includeThis:

			try:

				# print( '000' )
				info = _dir.info( path )
				# print(path)
				self.counter['files']+=1
				# self.index['local'].append( path ) #########################################################################
				# print( 'PRE' )
				paths = __.cloud.db.gen_paths( path )
				# print( 'POST' )
				# print( paths, path )
				cloud_path = paths['cloud']
				for testX in self.program_folders:
					if testX in cloud_path:
						if not testX in self.program_folders_active:
							self.program_folders_active.append(testX)

				if info['me'] > epoch:
					if not cloud_path in self.index['local']:
						self.index['local'][cloud_path] = {}
					# if not 'local' in self.index['local'][cloud_path]:
					self.index['local'][cloud_path]['created'] = info['ce']
					self.index['local'][cloud_path]['modified'] = info['me']
						# self.index['local'][cloud_path]['accessed'] = info['ae']
					self.index['local'][cloud_path]['local'] = path
					self.index['local'][cloud_path]['remote'] = paths['cloud']


			except Exception as e:
				print()
				print(path)
				print(e)
				print()

	def recursiveLocalIndex( self, folder, base=None, plus=None, minus=None, plusOr=None, first=True, epoch=None ):
		_v.dir_check_create(folder)
		if epoch is None:
			epoch = __.cloud.epoch
			if epoch is None or type(epoch) == bool or epoch == 'false':
				epoch = __.cloud.epoch_past
				_.colorThis( 'No epoch', 'red' )

		if not plusOr is None:
			_.switches.fieldSet( 'PlusOr', 'active', True )
		if not plus is None:
			_.switches.fieldSet( 'Plus', 'active', True )
			_.switches.fieldSet( 'Plus', 'value', ','.join( plus ) )
			_.switches.fieldSet( 'Plus', 'values', plus )
		if not minus is None:
			_.switches.fieldSet( 'Minus', 'active', True )
			_.switches.fieldSet( 'Minus', 'value', ','.join( minus ) )
			_.switches.fieldSet( 'Minus', 'values', minus )



		if first:
			if base is None:
				self.folder = folder
			else:
				self.folder = base

		items = os.listdir(folder)
		self.counter['folders'] += 1
		for item in items:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			path = __.path(path)
			if os.path.isfile(path):
				self.fileLocalIndex( path, base, plus, minus, first=False, epoch=epoch )
			elif os.path.isdir(path):
				try:
					self.recursiveLocalIndex( path, base, plus, minus, first=False, epoch=epoch )
				except Exception as e:
					pass
		
	def build_indices( self ):
		if len( self.index['local'].keys() )  == 0:
			# self.recursiveLocalIndex( self.structure['local']['shell'],self.structure['local']['tech']  )
			self.find_program_folders()
			# print( 'batch, pre', len(self.index['local'].keys()) )
			self.recursiveLocalIndex( self.structure['local']['batch'],self.structure['local']['tech']  )
			# print( 'batch, post', len(self.index['local'].keys()) )
			# print(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['python'],self.structure['local']['tech'] , plus=['*.py','*.htm'], plusOr=True )
			# print(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['bash'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['library'],self.structure['local']['tech']  )
			# print(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['remote.app'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['powershell'],self.structure['local']['tech'] )
			self.recursiveLocalIndex( self.structure['local']['javascript'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['documentation'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['databank_tables'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['ssl_keys'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['databank_db_vault'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['databank_db_indexes'],self.structure['local']['tech']  )

			# print(__.v.secure.sync)
			for sec_file in __.v.secure.sync:
				# print(sec_file)
				self.fileLocalIndex( sec_file, base=__.v.fileLocalIndex['base'], epoch=__.v.fileLocalIndex['epoch'] )
				# addThisFile( sec_file )

			print(len(self.index['local'].keys())  )
			# _.printVarSimple(self.index)
		if len( self.index['remote'].keys() )  == 0:
			self.recursiveRemoteIndex()


	def sync_up( self ):
		
		self.build_indices()

		epoch = __.cloud.epoch
		if epoch is None or type(epoch) == bool or epoch == 'false':
			epoch = __.cloud.epoch_past
			_.colorThis( 'No epoch', 'red' )
		


		for item in self.index['local']:
			d = self.index['local'][item]['modified']
			l = self.index['local'][item]['local']
			r = self.structure['remote']['tech'] + item

			ev = self.evaluate(l)
			if ev == 'n' or ev == 'l':
				if ev == 'n':
					# self.dir_check_create(r)
					self.check_remote_file_BUILD( r )
				self.upload( l, r, d, epoch )
				

		

	def upload( self, l, r, d=None, epoch=0 ):
		paths = __.cloud.db.gen_paths( l )


		if l in __.v.secure.nosync:
			return None


		if l in __.v.secure.crypt:
			_.cp( [ 'SECURE FILE:', l ], 'Background.red' )
			secureFile( l )



		


		# backup first
		# if not paths['cloud'] in self.index['remote']:
		# 	self.dir_check_create_FORCE( __.cloud.db.gen_paths( _v.popFile(l) )['remote'] )



			
		if paths['cloud'] in self.index['remote']:
			crfe = self.check_remote_file_exist(paths['remote'])
			if not crfe is None:
				if not __.cloud.checked_backup_folders:
					self.dir_check_create( self.structure['remote']['backup-txt'] )
					self.dir_check_create( self.structure['remote']['backup-bin'] )
				nParts = paths['cloud'].split('/')
				nParts.reverse()
				file_name = nParts.pop(0)
				backup_name = self.structure['remote']['backup-txt'] + '/' + str(__.cloud.now) + '-' + formatDate( self.index['remote'][paths['cloud']]['modified'] ) +  '-' + file_name
				
				backup_record = {
									'file': paths['cloud'],
									'backup': backup_name,
									'created': self.index['remote'][ paths['cloud'] ]['created'],
									'modified': self.index['remote'][ paths['cloud'] ]['modified'],
									'tz': self.index['remote'][ paths['cloud'] ]['tz'],
									'mime': 'text',
									'flag': '',
									'unixID': self.index['remote'][ paths['cloud'] ]['unixID'],
									'terminalID': '',
									'sessionID': __.cloud.sessionID,
				}

				task_completed = False
				while not task_completed:
					try:
						self.sftp.rename(r, backup_name)
					except Exception as e:
						task_completed = actionRequest( 'Cloud', 'pre upload backup', action=paths['cloud'], error=e )
					else:
						actionRequest( 'Cloud', 'upload', action=paths['cloud'], success=True)
						task_completed = True


						__.cloud.db.insert( 'backup', backup_record )








		# self.check_remote_file_BUILD(r)

		ranFix = False

		task_completed = False
		while not task_completed:
			try:
				self.sftp.put(l,r)
			except Exception as e:
				task_completed = actionRequest( 'Cloud', 'upload', action=paths['cloud'], error=e )

				if not ranFix:
					print('ranFix')
					mkdir_script = 'sh ~/cloud/files/tech/programs/remote/bash/p.sh mkdirs -file '+ paths['remote']
					# mkdir_script = 'sh ~/cloud/files/tech/programs/bash/p.sh mkdir -file '+ paths['remote']
					# mkdir_script = 'sh /home/ximlickficfp/cloud/files/tech/programs/remote/bash/p.sh mkdir -file "'+ paths['remote']+'"'
					ranFix = True
					# print( mkdir_script )
					task_completed_fx = False
					while not task_completed_fx:
						try:
							# stdin, stdout, stderr = self.ssh.exec_command( mkdir_script )
							i, o, e = self.ssh.exec_command( mkdir_script )
							# i, o, e = self.ssh.exec_command( _v.mkdir( paths['remote'], isFile=True, p=True ) )

							for line_res in o.readlines():
								print( line_res )
							for line_res in e.readlines():
								print( line_res )


							# print(stdin, stdout, stderr)
						except Exception as e:
							print(e)
							task_completed_fx = actionRequest( 'Cloud', 'pre upload backup', action=paths['cloud'], error=e )
						else:
							actionRequest( 'Cloud', 'upload', action=paths['cloud'], success=True)
							task_completed_fx = True






			else:
				actionRequest( 'Cloud', 'upload', action=paths['cloud'], success=True)
				task_completed = True

		
		__.cloud.db.insert_file( 'upload', l, paths['cloud'] )
		_.colorThis( paths['cloud'], 'cyan' )
		self.transfer_success = True
		return None






	def sync_down( self ):
		self.build_indices()
		epoch = None
		epoch = __.cloud.epoch
		if epoch is None or type(epoch) == bool or epoch == 'false':
			# epoch = __.cloud.epoch_future
			epoch = __.cloud.epoch_past
			_.colorThis( 'No epoch', 'red' )
		for item in self.index['remote']:
			paths = __.cloud.db.gen_paths(item)
			d = _.autoDate( self.index['remote'][item]['date_modified'] )
			r = paths['remote']
			l = paths['local']
			lx = l
			if _.isWin:
				lx = lx.lower()
			if not lx in self.delete:
				ev = self.evaluate(l)
				shouldTransfer = False
				if ev == 'n' or ev == 'r':
					self.download( r, l, d, epoch )
			# else:
			# 	try:
			# 		self.sftp.remove( paths['remote'] )
			# 		_.cp( [ 'deleted, server:', paths['cloud'] ], 'red' )
			# 	except Exception as e:
			# 		pass
					# _.cp( [ 'NOT deleted, server:', paths['cloud'] ], 'red' )
					# _.printVarSimple(paths)	

		_.changeC_END()

	def download( self, r, l, d=None, epoch=0 ):
		_v.popFileDir( l )

		paths = __.cloud.db.gen_paths(l)


		try:
			self.sftp.stat( r )
		except Exception as e:
			pass
			# print( 'eol:', paths['cloud'] )
			return 

		self.build_local(l)

		paths = __.cloud.db.gen_paths( l )

		task_completed = False
		while not task_completed:
			try:
				self.sftp.get(r,l)
			except Exception as e:
				task_completed = actionRequest( 'Cloud', 'download', action=paths['cloud'], error=e )
			else:
				actionRequest( 'Cloud', 'download', action=paths['cloud'], success=True)
				task_completed = True


		shCleanFile( l )
		finagleFile(l)
		_.changeM(l, self.index['remote'][paths['cloud']]['modified'] )
		_.changeC(l, self.index['remote'][paths['cloud']]['created'] )
		_.colorThis( paths['cloud'], 'cyan' )
		self.transfer_success = True
		return None





	def get_remote_file( self, remote, local, force=False ):
		stat = self.check_remote_file_exist( remote )
		if stat is None:
			return False
		else:
			# print( 'get_remote_file stat:', stat )
			# sys.exit()
			self.build_local( local )
			try:
				self.sftp.get( remote, local )
				return True
			except Exception as e:
				time.sleep(.5)
				try:
					self.sftp.get( remote, local )
					return True
				except Exception as e:
					return False

				return False


	def check_remote_file_exist( self, file ):
		stat = None
		try:
			stat = self.sftp.stat(file).st_mtime
		except Exception as e:
			time.sleep(.5)
			try:
				stat = self.sftp.stat(file).st_mtime
			except Exception as e:
				stat = None
		return stat


	def check_remote_file_BUILD( self, file ):
		stat = self.check_remote_file_exist( file )
		if not stat is None:
			return stat
		parts = file.split(_v.slashes['u'])
		parts.reverse()
		parts.pop(0)
		parts.reverse()
		f = _v.slashes['u'].join( parts )
		if not f.startswith(_v.slashes['u']):
			f = _v.slashes['u'] + f
		f = f.replace( _v.slashes['u']+_v.slashes['u'],_v.slashes['u'] )
		if not f in self.folder_check['remote']:

			self.dir_check_create( f )
			self.folder_check['remote'].append(f)
		return None

	def build_local( self, file ):
		parts = file.split(_v.slash)
		parts.reverse()
		parts.pop(0)
		parts.reverse()
		f = _v.slash.join( parts )
		if not f in self.folder_check['local']:
			_v.dir_check_create( f )
			self.folder_check['local'].append(f)

	def remote_isdir( self, folder ):
		try:
			self.sftp.chdir(folder)
			return True
		except IOError:
			time.sleep(.5)
			try:
				self.sftp.chdir(folder)
				return True
			except IOError:
				return False
			return False

	def dir_check_create_FORCE( self, folder ):


		slash = _v.slashes['u']
		parts = folder.split( slash )
		# parts.pop(0)

		newParts = []
		newParts.append(_v.slashes['u'])
		for p in parts:
			if len(p):
				newParts.append( p )
				f = slash.join( newParts )
				# if not techDrive in f:
				# 	f = techDrive+dDim+slash+f
				f = f.replace( _v.slashes['u']+_v.slashes['u'], _v.slashes['u'] )
				# print(f)

				# exist = self.remote_isdir( f )
				# print( 'exist:', exist, f, '\r\n' )
				# if not exist:
				if True:


					task_completed = False
					while not task_completed:
						try:
							self.sftp.mkdir( f )
						except Exception as e:
							task_completed = actionRequest( 'Cloud', 'dir_check_create', action=f, error=e, attempts=1 )
						else:
							actionRequest( 'Cloud', 'dir_check_create', action=f, success=True, attempts=1)
							task_completed = True
							return True
						if task_completed:
							break






					# print( 'Error:', f )
		return True

	def dir_check_create( self, folder ):
		#################################################################################################################
		return False
		if self.remote_isdir( folder ):
			# print( folder )
			return False




		slash = _v.slashes['u']
		parts = folder.split( slash )
		# parts.pop(0)

		newParts = []
		newParts.append(_v.slashes['u'])
		for p in parts:
			if len(p):
				newParts.append( p )
				f = slash.join( newParts )
				# if not techDrive in f:
				# 	f = techDrive+dDim+slash+f
				f = f.replace( _v.slashes['u']+_v.slashes['u'], _v.slashes['u'] )
				# print(f)

				# exist = self.remote_isdir( f )
				# print( 'exist:', exist, f, '\r\n' )
				# if not exist:
				if True:


					task_completed = False
					while not task_completed:
						try:
							self.sftp.mkdir( f )
						except Exception as e:
							task_completed = actionRequest( 'Cloud', 'dir_check_create', action=f, error=e )
						else:
							actionRequest( 'Cloud', 'dir_check_create', action=f, success=True)
							task_completed = True
							return True
						if task_completed:
							break






					# print( 'Error:', f )
		return True

	def db( self, ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix ):
		# print( 'HERE A' )
		__.cloud.waiting = True
		_.colorThis( 'status: db creating thread', 'yellow' )
		_threads.manager.register(
			name = 'Database',
			fn = db_manager,
			timeout = None,
			k = {
					'ssh_server': ssh_server,
					'ssh_port': ssh_port,
					'ssh_user': ssh_user,
					'ssh_password': ssh_password,
					'db_server': db_server,
					'db_port': db_port,
					'db_user': db_user,
					'db_password': db_password,
					'db_name': db_name,
					'db_prefix': db_prefix,
				}
		)
		# _.colorThis( 'status: db thread complete', 'yellow' )

		while __.cloud.waiting:
			time.sleep(.5)
		return None
		# print( 'HERE B' )
		# DB( ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name )



def db_manager( ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix ):
	__.cloud.db = DB( ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix )
	# __.cloud.Neg = Negotiator( __.cloud.db )
	__.cloud.waiting = False
	_.colorThis( 'status: db ready', 'yellow' )
	while not __.cloud.COMPLETED:
		time.sleep(.5)
	_.colorThis( 'status: db connection closing', 'yellow' )
	__.cloud.db.close()
	
class DB:
	def __init__( self, ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix ):

		_.colorThis( 'status: db pre', 'yellow' )
		self.table_prefix = db_prefix
		# __.cloud.db.table_prefix = 'cloud'
		# _.colorThis( 'status: db B', 'yellow' )
		# self.tables_app_list = [
		# 						'accounts',
		# 						'files',
		# 						'log_connection',
		# 						'log_transfer',
		# 						'log_error',
		# ]
		self.tables_app_live = []
		self.tables_app_list = [
								'table_versions',
								'files',
								'connection',
								'synchronized',
								'backup',
								'file_version',
		]

		self.table_fields = {}

		# print( 'HERE C' )
		time.sleep(.5)
		_.colorThis( 'status: db ssh connecting', 'yellow' )
		task_completed = False
		while not task_completed:
			try:
				self.ssh = SSHTunnelForwarder(
						(ssh_server, ssh_port),
						ssh_username=ssh_user,
						ssh_password=ssh_password,
						remote_bind_address=(db_server, db_port))
			except Exception as e:
				task_completed = actionRequest( 'DB', 'ssh connect', error=e )
			else:
				actionRequest( 'DB', 'ssh connect', success=True)
				task_completed = True


		task_completed = False
		while not task_completed:
			try:
				self.ssh.start()
			except Exception as e:
				task_completed = actionRequest( 'Cloud', 'ssh.start', error=e )
			else:
				actionRequest( 'Cloud', 'ssh.start', success=True)
				task_completed = True

		
		_.colorThis( 'status: db ssh connected', 'yellow' )
		# for x in dir(self.ssh):
		# 	print(x)
		_.colorThis( 'status: db pymysql connecting', 'yellow' )

		task_completed = False
		while not task_completed:
			try:
				self.conn = pymysql.connect(host='127.0.0.1', user=db_user,
						passwd=db_password, db=db_name,
						port=self.ssh.local_bind_port)
			except Exception as e:
				task_completed = actionRequest( 'DB', 'db connect', error=e )
			else:
				actionRequest( 'DB', 'db connect', success=True)
				task_completed = True

		task_completed = False
		while not task_completed:
			try:
				self.db = self.conn.cursor()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'conn.cursor', error=e )
			else:
				actionRequest( 'DB', 'conn.cursor', success=True)
				task_completed = True

		
		_.colorThis( 'status: db pymysql connected', 'yellow' )
		_.colorThis( 'status: db auditing and indexing structure', 'yellow' )
		self.check_structure()
		_.colorThis( 'status: db structure indexed and auditing complete', 'yellow' )
		__.cloud.epoch = self.find1( 'synchronized', { 'unixID': _v.unixID }, 'epoch' )



	def db_test( self ):
		query = '''SELECT VERSION();'''
		data = pd.read_sql_query(query, self.db)
		print(data)

	def close( self ):

		delete = _.getTableDB( 'delete.index' )
		self.delete = {}
		for d in delete:
			f = _v.resolveFolderIDs( d )
			if _.isWin:
				f = f.lower()
			self.delete[f] = 1
			if os.path.isfile(f):
				os.unlink(f)
				_.cp( [ 'deleted, local:', f ], 'red' )

		# sys.exit()
		_.colorThis( 'status: db closing cursor', 'yellow' )

		task_completed = False
		while not task_completed:
			try:
				self.db.close()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'db.close', error=e )
			else:
				actionRequest( 'DB', 'db.close', success=True)
				task_completed = True

		_.colorThis( 'status: db closing connection', 'yellow' )


		task_completed = False
		while not task_completed:
			try:
				self.conn.close()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'conn.close', error=e )
			else:
				actionRequest( 'DB', 'conn.close', success=True)
				task_completed = True

		
		_.colorThis( 'status: ssh closing', 'yellow' )

		task_completed = False
		while not task_completed:
			try:
				self.ssh.close()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'ssh.close', error=e )
			else:
				actionRequest( 'DB', 'ssh.close', success=True)
				task_completed = True


		
		# sys.exit()

	def query( self, sql, table_label=None ):
		# return pd.read_sql_query(sql, self.db)

		task_completed = False
		while not task_completed:
			try:
				self.db.execute(sql)
			except Exception as e:
				task_completed = actionRequest( 'DB', 'query', action=sql, error=e )
			else:
				actionRequest( 'DB', 'query', action=sql, success=True)
				task_completed = True

		task_completed = False
		while not task_completed:
			try:
				table = self.db.fetchall()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'query', action='fetchall'+sql, error=e )
			else:
				actionRequest( 'DB', 'query', action='fetchall'+sql, success=True)
				task_completed = True


		
		# if not 'show' in sql.lower() and 'table' in sql.lower():
		if not table_label is None:
			if table_label.startswith(self.table_prefix):
				table_label = table_label[len(self.table_prefix+'_'):]
			records = []
			# print( '\t\t', table_label )
			for rec in table:
				record = {}
				for i,field in enumerate(rec):
					record[  self.table_fields[table_label][i]  ] = field
					if type(field) == datetime.datetime:
						record[  self.table_fields[table_label][i]  ] = str(field)
					# print( '\t\t\t', self.table_fields[table_label][i], type(field), field )
				records.append(record)
			return records
		return table

	def check_structure( self ):
		self.tables_app_live = []
		# print('A')
		for tbl in self.tables_app_list:
			self.tables_app_live.append( self.table_prefix+'_'+tbl )

		self.live_tables = []
		for table in self.query('show tables'):
			self.live_tables.append(table[0])

		# print('B')
		for table in self.tables_app_live:
			if not table in self.live_tables:
				self.table_setup(table)
			# else:
				# print(table)

		# print('C')
		for table in self.query('show tables'):
			if table[0] in self.tables_app_live:
				this_label = table[0][len(self.table_prefix+'_'):]
				self.table_fields[ this_label ] = []
				# print( this_label )
				for field in self.query('SHOW COLUMNS FROM ' + table[0]):
					# print( '\t', field[0] )
					self.table_fields[ this_label ].append( field[0] )
		# print('D')


	def table_setup( self, label ):

		_.colorThis(  ['creating table:',label], 'green'  )

		item = 'table_versions'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	date_modified timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	label varchar(60),
	version varchar(30)
);
			'''



		item = 'files'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	date_modified timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	cloud_path varchar(1000),
	name varchar(200),
	ext varchar(20),
	size int,
	folder varchar(1000),
	md5 varchar(40),
	created double,
	modified double,
	tz varchar(8),
	unixID varchar(40),
	sessionID varchar(40),
	auto int(1) default 1,
	eol int(1) default 0
);
			'''



		item = 'connection'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	date_modified timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	unixID varchar(40),
	sessionID varchar(40),
	zone varchar(200)
);
			'''





		item = 'synchronized'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	date_modified timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	unixID varchar(40),
	epoch double,
	sessionID varchar(40)
);
			'''



		item = 'backup'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	file varchar(600),
	backup varchar(600),
	created double,
	modified double,
	tz varchar(8),
	md5 varchar(40),
	mime varchar(10),
	flag varchar(40),
	unixID varchar(40),
	terminalID varchar(40),
	sessionID varchar(40),
	counted int(1) default 0
);
			'''



		item = 'file_version'
		if label == self.table_prefix+'_'+item:
			selected = { 'label': item, 'version': '0.1' }
			sql = '''
CREATE TABLE '''+self.table_prefix+'_'+item+''' (
	id int auto_increment primary key, 
	date_created timestamp NOT NULL default CURRENT_TIMESTAMP,
	date_modified timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
	file varchar(600),
	version varchar(50),
	v0 int,
	v1 int,
	v2 int,
	v3 int

);
			'''




		task_completed = False
		while not task_completed:
			try:
				self.db.execute(sql)
			except Exception as e:
				task_completed = actionRequest( 'DB', 'table_setup', action=sql, error=e )
			else:
				actionRequest( 'DB', 'table_setup', action=sql, success=True)
				task_completed = True

		
		sql = "INSERT INTO `"+self.table_prefix+'_'+self.tables_app_list[0]+"` (`label`, `version`) VALUES (%s, %s)"


		task_completed = False
		while not task_completed:
			try:
				self.db.execute(sql, (   selected['label'],   selected['version']   ))
			except Exception as e:
				task_completed = actionRequest( 'DB', 'table_setup', action=sql, error=e )
			else:
				actionRequest( 'DB', 'table_setup', action=sql, success=True)
				task_completed = True

		task_completed = False
		while not task_completed:
			try:
				self.conn.commit()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'table_setup', action='commit'+sql, error=e )
			else:
				actionRequest( 'DB', 'table_setup', action='commit'+sql, success=True)
				task_completed = True

		

	def search_file( self, path ):
		sql = 'SELECT * FROM `'+self.table_prefix+'_files'+ '` WHERE cloud_path = "'+path+'" '
		return self.query(sql,'files' )

	def file_epoch( self, path ):
		record = self.search_file(path)
		return record[0]['modified']

	def search_table_version( self, table ):
		sql = 'SELECT * FROM `'+self.table_prefix+'_'+self.tables_app_list[0]+'` WHERE label = "'+table+'" '
		return self.query(sql,self.tables_app_list[0] )

	def insert_file( self, direction, local, cloud_path ):
		# print( 'cloud_path:', cloud_path )
		shouldAdd = True
		cp = cloud_path
		if direction == 'upload':
			info = _dir.info(local)
			folderParts = cloud_path.split(_v.slashes['u'])
			folderParts.reverse()
			folderParts.pop(0)
			folderParts.reverse()

			name = info['name']
			ext = info['ext']
			size = info['bytes']
			folder = _v.slashes['u'].join(folderParts)
			modified = info['me']
			created = info['ce']
			deleted = 0

			record = {
						'cloud_path': cloud_path,
						'name': name,
						'ext': ext,
						'size': size,
						'folder': folder,
						'created': created,
						'modified': modified,
						'tz': str(time.strftime("%z")).replace(':',''),
						'eol': 0,
						'unixID': _v.unixID,
						'sessionID': __.cloud.sessionID
			}
			self.insert( 'files', record, 'cloud_path' )
			return None


	def insert( self, table, dic, key=None ):
		if not self.table_prefix in table:
			table = self.table_prefix+'_'+table
		shouldAdd = True

		if not key is None:
			if type(dic[key]) == str:
				value = '"'+dic[key]+'"'
			else:
				value = str(dic[key])

			result = self.query(' SELECT * FROM '+table+' WHERE '+key+'='+value)
			if len(result):
				shouldAdd = False
			else:
				shouldAdd = True


		if not shouldAdd:
			# print( 'updating...' )
			sql = 'UPDATE '+table+' SET NEW_VALUES WHERE '+key+' = '+value
			build_set = []
			for field in dic.keys():
				v = None
				if type(dic[field]) == str:
					v = '"'+dic[field]+'"'
				else:
					v = str(dic[field])
				build_set.append( '`'+field+'` = '+ v )
			sql = sql.replace( 'NEW_VALUES', ','.join(build_set) )
		elif shouldAdd:
			# print( 'inserting...' )
			sql = "INSERT INTO `"+table+"` ( FIELD_NAMES ) VALUES ( FIELD_VALUES )"
			build_names = []
			build_values = []
			for field in dic.keys():
				build_names.append( '`'+field+'`' )
				if type(dic[field]) == str:
					build_values.append(  '"'+dic[field]+'"'  )
				else:
					build_values.append(  str(dic[field])  )
			sql = sql.replace( 'FIELD_NAMES',','.join(build_names) )
			sql = sql.replace( 'FIELD_VALUES',','.join(build_values) )

		# print(sql)
		# print(sql)

		task_completed = False
		while not task_completed:
			try:
				self.db.execute( sql )
			except Exception as e:
				task_completed = actionRequest( 'DB', 'insert', action=sql, error=e )
			else:
				actionRequest( 'DB', 'insert', action=sql, success=True)
				task_completed = True

		

		task_completed = False
		while not task_completed:
			try:
				self.conn.commit()
			except Exception as e:
				task_completed = actionRequest( 'DB', 'insert', action='commit'+sql, error=e )
			else:
				actionRequest( 'DB', 'insert', action='commit'+sql, success=True)
				task_completed = True



	def find1( self, table, dic, single=None ):
		if not table.startswith(self.table_prefix+'_'):
			table = self.table_prefix+'_'+table
		key = str(list(dic.keys())[0])
		if type(dic[key]) == str:
			v = '"'+dic[key]+'"'
		else:
			v = str(dic[key])
		sql = 'SELECT * FROM '+table+' WHERE '+key+' = '+v
		# print(sql)
		records =  self.query(sql,table)
		# print( records )
		if single is None:
			return records
		else:
			if not len(records):
				return None
			else:
				# print(records[0][single])
				return records[0][single]



	def gen_cloud_path( self, what, path ):
		if what == 'l' or what == 'local':
			cloud_path = path.replace( __.cloud.structure['local']['tech'], '' ).replace( _v.slash, _v.slashes['u'] )
		elif what == 'r' or what == 'remote':
			cloud_path = path.replace( __.cloud.structure['remote']['tech'], '' ).replace( _v.slash, _v.slashes['u'] )
		return cloud_path

	def gen_paths( self, path ):
		if __.cloud.structure['local']['tech'].lower() in path.lower():
			cloud_path = self.gen_cloud_path( 'local', path )
		elif __.cloud.structure['remote']['tech'].lower() in path.lower():
			cloud_path = self.gen_cloud_path( 'remote', path )
		elif path.startswith('/programs/'):
			cloud_path = path
		else:
			if not 'gen_paths' in __.LOOP:
				__.LOOP['gen_paths'] = 0
			__.LOOP['gen_paths']+=1
			print( 'Error: gen_paths - ', __.LOOP['gen_paths'], path )
			if __.LOOP['gen_paths'] < 10:
				cloud_path = self.gen_paths(path)['cloud']
			else:
				cloud_path = path

		result = {
					'local': __.path(__.cloud.structure['local']['tech'] + cloud_path.replace( _v.slashes['u'], _v.slash )),
					'remote': __.cloud.structure['remote']['tech'] + cloud_path.replace( _v.slash, _v.slashes['u'] ),
					'cloud': cloud_path
		}
		return result









		# raise e
	# time.sleep(.02)

def gen_cloud_path( what, path ):
	if what == 'l' or what == 'local':
		cloud_path = path.replace( __.cloud.structure['local']['tech'], '' ).replace( _v.slash, _v.slashes['u'] )
	elif what == 'r' or what == 'remote':
		cloud_path = path.replace( __.cloud.structure['remote']['tech'], '' ).replace( _v.slash, _v.slashes['u'] )
	return cloud_path

def gen_paths( path ):
	if __.cloud.structure['local']['tech'].lower() in path.lower():
		cloud_path = gen_cloud_path( 'local', path )
	elif __.cloud.structure['remote']['tech'].lower() in path.lower():
		cloud_path = gen_cloud_path( 'remote', path )
	elif path.startswith('/programs/'):
		cloud_path = path
	else:
		if not 'gen_paths' in __.LOOP:
			__.LOOP['gen_paths'] = 0
		__.LOOP['gen_paths']+=1
		if 'show_path_errors' in __.specifications and __.specifications['show_path_errors']:
			print( 'Error: gen_paths - ', __.LOOP['gen_paths'], path )
		if __.LOOP['gen_paths'] < 10:
			cloud_path = gen_paths(path)['cloud']
		else:
			cloud_path = path

	result = {
				'local': __.cloud.structure['local']['tech'] + cloud_path.replace( _v.slashes['u'], _v.slash ),
				'remote': __.cloud.structure['remote']['tech'] + cloud_path.replace( _v.slash, _v.slashes['u'] ),
				'cloud': cloud_path
	}
	return result



def completed_success():
	__.cloud.COMPLETED_SUCCESS = True
	__.cloud.COMPLETED_ERROR = False
	__.cloud.COMPLETED = True

def completed_error():
	__.cloud.COMPLETED_ERROR = True
	__.cloud.COMPLETED_SUCCESS = False
	__.cloud.COMPLETED = True


def actionRequest( classy, label, action=None, error=None, success=None, attempts=3 ):

	if success:
		return True
	if action is None:
		_.cp( '.', 'red' )
		if __.setting( 'print-errors' ):
			_.colorThis( [ 'Error:', classy, label ], 'red' )
	elif not action is None:
		_.cp( '.', 'red' )
		if __.setting( 'print-errors' ):
			_.colorThis( [ 'Error:', classy, label, action ], 'red' )

	if not action is None:
		file_action = _md5.md5( str(label)+str(action) )

	attempt = '0012814A-B08D-448D-89C9-715BEB6182F1'
	if not classy in __.cloud.attempt:
		__.cloud.attempt[classy] = {}
		__.cloud.attempt[classy][attempt] = 0
	__.cloud.attempt[classy][attempt] += 1
	if not label in __.cloud.attempt[classy]:
		__.cloud.attempt[classy][label] = {}
		__.cloud.attempt[classy][label][attempt] = 0
	
	if action is None:
		__.cloud.attempt[classy][label][attempt] +=1
		rest_for = 0
		if __.cloud.attempt[classy][label][attempt] < 50:
			rest_for += 2
		error_rest( rest_for, __.cloud.attempt[classy][label][attempt])
		

		if __.cloud.attempt[classy][label][attempt] < attempts:
			# print( 'return False' )
			return False
		else:
			print( 'err' )
			return True

	elif not action is None:
		if not file_action in __.cloud.attempt[classy][label]:
			__.cloud.attempt[classy][label][  file_action  ] = {}
			__.cloud.attempt[classy][label][  file_action  ][attempt] = 0
		__.cloud.attempt[classy][label][  file_action  ][attempt] +=1

		rest_for = 0
		if __.cloud.attempt[classy][label][  file_action  ][attempt] < 50:
			rest_for += 2

		error_rest( rest_for, __.cloud.attempt[classy][label][  file_action  ][attempt])
		if __.cloud.attempt[classy][label][  file_action  ][attempt] < attempts:
			# print( 'return False' )
			return False
		else:
			print( 'err' )
			# print( 'return gave up' )
			return True
			
# def result( classy, label, record=None ):
# 	attempt = '0012814A-B08D-448D-89C9-715BEB6182F1'
# 	if record is None:
# 		on = 



# class Negotiator:
# 	def __init__( self, db ):
# 		self.db = db

def error_rest( cnt, eN ):
	# _.cp( '..', 'red' )
	# _.colorThis(   ['Attempt:', eN, 'resting for', cnt], 'red'   )
	time.sleep(cnt)



# epyi simpleThreads

class CLOUD_VAR:
	def __init__( self ):
		# self.tz_index = _tz.index
		self.checked_backup_folders = False
		self.now = time.time()
		self.tz = str(time.strftime("%z")).replace(':','')
		self.epoch = None
		self.epoch_past = _.autoDate( '1971-01-01' )
		self.epoch_future = _.autoDate( '3000-01-01' )
		self.sessionID = _.genUUID()
		self.structure = {}
		self.waiting = False
		self.COMPLETED_SUCCESS = None
		self.COMPLETED_ERROR = None
		self.COMPLETED = False
		self.attempt = {}
		self.table_prefix = 'cloud'
		self.attempt_threshold = {
									'Cloud': {
												'connect': { 'record': False, 'threshold': 4, 'action': 'fail' },
												'upload': { 'record': True, 'threshold': 3, 'action': 'skip' },
												'download': { 'record': True, 'threshold': 3, 'action': 'skip' },
									},
									'DB': {
												'connect': { 'record': False, 'threshold': 4, 'action': 'fail' },
												'upload': { 'record': True, 'threshold': 3, 'action': 'skip' },
												'download': { 'record': True, 'threshold': 3, 'action': 'skip' },
									},
		}

def finagleFile( path ):
	if path.lower().endswith('.sh'):
		# print('.sh', os.path.isfile(path))
		if os.path.isfile(path):
			file = _.getText( path, raw=True )
			file = file.replace( chr(10), '\n' )
			_.saveText( file, path )


def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y_%m_%d-%H_%M_%S')
	theDate = str(theDate)
	return theDate


secure_files = None
def secureFile( path ):
	global secure_files
	try:

		if secure_files is None:
			secure_files = _.getTableDB( 'secure-files.settings' )
	except Exception as e:
			secure_files = _.getTableDB( 'secure-files.settings' )

	if _v.sanitizeFolder(path) in secure_files['files']  or _v.sanitizeFolder(_v.popFile(path)) in secure_files['folders']:
		# _.cp( [ 'SECURE FILE' ], 'Background.red' )
		
		if _v.sanitizeFolder(path) in secure_files['files']:
			secure_record = secure_files['files'][ _v.sanitizeFolder(path) ]
		elif _v.sanitizeFolder(_v.popFile(path)) in secure_files['folders']:
			secure_record = secure_files['folders'][ _v.sanitizeFolder(_v.popFile(path)) ]

		secureFiles_Encrypt( path, secure_record['Password'] )
		
		

_cryptFile = None
def secureFiles_Encrypt( path, pw ):
	global _cryptFile
	if _cryptFile is None:

		try:
			_cryptFile = _.regImp( __.appReg, 'cryptFile' )
			_cryptFile.switch( 'NoExt' )
			# if _.switches.isActive('Clean'):
			_cryptFile.switch( 'Clean' )
			_cryptFile.imp.appDBA = _cryptFile.focus
		except Exception as e:
			_.colorThis( 'Error: missing pyAesCrypt', 'red' )


	
	if _.isCrypt(path):
		return None
	
	_.cp( 'crypt.en', 'Background.light_blue' )
	_cryptFile.switch( 'Password', delete=True )
	if len(pw):
		_cryptFile.switch( 'Password', _blowfish.decrypt( pw, _vault.key() ) )
	_cryptFile.switch( 'Encrypt' )
	_cryptFile.switch( 'Decrypt', delete=True )
	_cryptFile.switch( 'Files', path )

	epoch = _dir.info(path)['me']
	_cryptFile.do( 'action' )
	while epoch == _dir.info(path)['me']:
		time.sleep(.2)


__.cloud = CLOUD_VAR()

import _rightThumb._md5 as _md5

import _rightThumb._simpleThreads as _threads

import _rightThumb._tz as _tz
# print( '__.cloud' )


# import inspect
# x = inspect.getargspec(SSHTunnelForwarder)
# print(x)

import _rightThumb._md5 as _md5
import _rightThumb._dir as _dir
_vault = _.regImp( __.appReg, '_rightThumb._vault' )

import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser




import subprocess



import datetime

def getFolder(folder):
	_v.dir_check_create(folder)
	for item in os.listdir(folder):
		path = __.path(folder + os.sep + item)
		if os.path.isfile(path):
			addThisFile( path )
		elif os.path.isdir(path):
			getFolder(path)



def addThisFile( path ):
	if not path in __.v.secure.nosync:
		record = {	
			'name': 	item,
			'path': 	path,
			'bytes':	os.stat(path).st_size,
			'created': 	os.path.getctime(path),
			'modified': os.path.getmtime(path),
			'tz': str(time.strftime("%z")).replace(':',''),

		}
		__.local_table.append(record)


def groupFoldersList( folderGroup ):
	if folderGroup == 'linux-basic':
		folderGroups = [
			'/programs/python/',
			'/programs/bash/',
		]
	if folderGroup == 'windows-basic':
		folderGroups = [
			'/programs/python/',
			'/programs/bash/',
		]
	if folderGroup == 'all':
		folderGroups = __.cloud_program_folders
	
	return folderGroups

shCleanFile_announce = False
def shCleanFile(path):
	global shCleanFile_announce
	if _tool.cloud_loaded:
		if not shCleanFile_announce:
			shCleanFile_announce=True
			print( 'cleaner = tool' )
		_tool.vc.HEAD.bashFileHeader(path)
		_tool.vc.SH.processSHfile(path)
	else:
		if not shCleanFile_announce:
			shCleanFile_announce=True
			print( 'cleaner = cloud' )
		if not _.isWin:
			os.chmod( path, 0o777 )
		shouldRun = False
		for testy in [ '.sh', '.py', '.ovpn' ]:
			if path.endswith(testy):
				shouldRun = True
		if shouldRun:
			_.cp( [ 'CLEANED:', path ], 'cyan' )
			file = _.getText( path, raw=True )
			file = file.replace( chr(10), '\n' )
			file = file.replace( chr(27), '' )
			file = file.replace( '\r', '' )
			_.saveText( file, path )





try:
	__.v.secure.files
except Exception as e:
	secure_files = _.regImp( __.appReg, 'secureFiles' )
	secure_files.imp.scanFolders(sync=True, meta=True)
	del secure_files

def do_nothing(var1=None,var2=None,var3=None,var4=None,p=1):
	return None

# print( tool_path )
rt = _v.home +os.sep+ '.rt'
t = _v.home +os.sep+ '.rt' +os.sep+ 'tool'
if not os.path.isdir(rt):
	os.mkdir(rt)
if not os.path.isfile( t ):
	url = 'http://reph.us/tools/tool'
	page = requests.get(url)
	page_code = str(page.text)
	page_code = page_code.replace( chr(10), '\n' )
	page_code = page_code.replace( chr(27), '' )
	page_code = page_code.replace( '\r', '' )
	# for x in dir(page):
	# 	print(x)
	# print(page_code)
	# print(type(page_code))
	_.saveText( page_code, t )
time.sleep(.05)

if os.path.isfile( t ):
	_tool = _.import_path( '?tool' )
	try:
		_tool.loader()
		_tool.cloud_loaded = True
	except Exception as e:
		_tool.cloud_loaded = False

else:
	# print('no tool')

	_tool = _.dot()
	_tool.v = _.dot()
	_tool.v.bash = {}
	_tool.processSHfile = do_nothing
	_tool.bashFileHeader = do_nothing
	_tool.bash_vars = do_nothing
	_tool.cloud_loaded = False


if _tool.cloud_loaded:
	_tool.vc.FIG.bash_vars(p=0)

# sys.exit()

# try:
# except Exception as e:
# 	pass
# print( _tool.v.bash )
# sys.exit()
# https://www.reddit.com/r/learnpython/comments/53wph1/connecting_to_a_mysql_database_in_a_python_script/

########################################################################################
if __name__ == '__main__':
	action()

__.local_table = []
# check_structure
# search_table_version

# batch, pre
# batch, post

# __.specifications['testing'] = True







