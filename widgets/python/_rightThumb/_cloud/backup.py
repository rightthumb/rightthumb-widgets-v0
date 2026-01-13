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
### EXAMPLE: START
# import simplejson as json
# from threading import Timer
# from lxml import html
# import requests
# import cssselect
# import sqlite3
### EXAMPLE: END
##################################################


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
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# date = _.friendlyDate( theDate )
# _.addComma()
### EXAMPLE: END
########################################################################################
# START



class Cloud:
	def __init__( self  ):
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
							'documentation': _v.programs +_v.slash+ 'documentation',
							'shell': _v.programs +_v.slash+ 'webApps' + _v.slash + 'shell',
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
			_.colorThis( 'Error:', 'red' )
			_.pr( '\t', e )

		_.colorThis( 'status: db connecting', 'yellow' )
		self.db( ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix )
		_.colorThis( 'status: db initialized', 'yellow' )
		# _.pr()
		# _.pr()
		# test = __.cloud.db.search_table_version('files')
		# _.pr(test)
		# _.printVarSimple(__.cloud.db.table_fields)
		# _.printVarSimple(test)
		# # _.pr(test)
		# _.pr()
		# _.pr()



		# __.cloud.COMPLETED = True
		# return None



		# time.sleep(3)

		self.ssh_connection(ssh_password)

		_.colorThis( 'status: ssh connected', 'yellow' )
		__.cloud.db.insert( 'connection', { 'unixID': _v.unixID, 'zone': __.cloud.tz, 'sessionID': __.cloud.sessionID } )
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

	def syncDates( self ):
		_.colorThis( 'status: sftp indexing', 'yellow' )

		_.pr( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files' )

		for record in __.cloud.db.query( 'SELECT * FROM '+__.cloud.db.table_prefix+'_files', 'files' ):
			_.pr(record)
			paths = __.cloud.db.gen_paths( record['cloud_path'] )
			record['local'] = paths['local']
			record['remote'] = paths['remote']
			self.index['remote'][ paths['cloud'] ] = record


		_.colorThis( 'status: synchronizing dates', 'yellow' )
		_.pr(self.index['remote'])
		for rp in self.index['remote']:
			rec = self.index['remote'][rp]
			paths = __.cloud.db.gen_paths( rp )
			_.pr(paths['local'])
			_.changeM( paths['local'], rec['modified'] )
			_.changeC( paths['local'], rec['created'] )
			# changeM( paths['local'], rec['modified'] )

		__.cloud.COMPLETED = True
	def ftp( self ):
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
		self.updateDeleted()

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
			# _.pr( diff, _.friendlyDate(info['me']), _.friendlyDate(rd) )


	def recursiveRemoteIndex( self, epoch=None ):



		folderGroups = groupFoldersList( self.folderGroup )
		for x in self.program_folders_active:
			if not x in folderGroups:
				folderGroups.append(x)
		xx = []
		for x in folderGroups:
			xx.append('cloud_path LIKE "%'+x+'%"')


		sql = 'SELECT * FROM '+__.cloud.db.table_prefix+'_files WHERE eol=0 AND ' + ' OR '.join( xx )

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
				#     _.pr( record['local'] )
				if os.path.isfile( record['local'] ):
					_.pr( 'del', record['local'] )
					# fileBackup.switch( 'Input', record['local'] )
					# backup_file = fileBackup.do( 'action' )
					# if os.path.isfile(backup_file):
					#     os.unlink(backup_file)
					# os.link( record['local'], backup_file )
					# _.pr( 'backup:', backup_file )
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








	def recursiveLocalIndex( self, folder, base=None, plus=None, minus=None, plusOr=None, first=True, epoch=None ):
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
			if os.path.isfile(path):
				
				includeThis = False
				if plus is None and minus is None:
					includeThis = True
				else:
					includeThis = _.showLine( path )

				if includeThis:

					try:

						# _.pr( '000' )
						info = _dir.info( path )
						# _.pr(path)
						self.counter['files']+=1
						# self.index['local'].append( path ) #########################################################################
						# _.pr( 'PRE' )
						paths = __.cloud.db.gen_paths( path )
						# _.pr( 'POST' )
						# _.pr( paths, path )
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
						pass
			elif os.path.isdir(path):
				try:
					self.recursiveLocalIndex( path, base, plus, minus, first=False, epoch=epoch )
				except Exception as e:
					pass
		
	def build_indices( self ):
		if len( self.index['local'].keys() )  == 0:
			# self.recursiveLocalIndex( self.structure['local']['shell'],self.structure['local']['tech']  )
			self.find_program_folders()
			# _.pr(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['python'],self.structure['local']['tech'] , plus=['*.py','*.htm'], plusOr=True )
			# _.pr(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['bash'],self.structure['local']['tech']  )
			# _.pr(len(self.index['local'].keys())  )
			self.recursiveLocalIndex( self.structure['local']['powershell'],self.structure['local']['tech'] )
			self.recursiveLocalIndex( self.structure['local']['javascript'],self.structure['local']['tech']  )
			self.recursiveLocalIndex( self.structure['local']['documentation'],self.structure['local']['tech']  )
			_.pr(len(self.index['local'].keys())  )
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








		# backup first
		if paths['cloud'] in self.index['remote']:
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
					task_completed = actionRequest( 'Cloud', 'upload', action=paths['cloud'], error=e )
				else:
					actionRequest( 'Cloud', 'upload', action=paths['cloud'], success=True)
					task_completed = True


					__.cloud.db.insert( 'backup', backup_record )









		task_completed = False
		while not task_completed:
			try:
				self.sftp.put(l,r)
			except Exception as e:
				task_completed = actionRequest( 'Cloud', 'upload', action=paths['cloud'], error=e )
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
			ev = self.evaluate(l)
			shouldTransfer = False
			if ev == 'n' or ev == 'r':
				self.download( r, l, d, epoch )
		_.changeC_END()

	def download( self, r, l, d=None, epoch=0 ):

		self.build_local(l)
		paths = __.cloud.db.gen_paths(l)

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
			# _.pr( 'get_remote_file stat:', stat )
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

	def dir_check_create( self, folder ):
		if self.remote_isdir( folder ):
			# _.pr( folder )
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
				#     f = techDrive+dDim+slash+f
				f = f.replace( _v.slashes['u']+_v.slashes['u'], _v.slashes['u'] )
				# _.pr(f)

				exist = self.remote_isdir( f )
				# _.pr( 'exist:', exist, f, '\r\n' )
				if not exist:


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






					# _.pr( 'Error:', f )
		return True

	def db( self, ssh_server, ssh_port, ssh_user, ssh_password, db_server, db_port, db_user, db_password, db_name, db_prefix ):
		# _.pr( 'HERE A' )
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
		# _.pr( 'HERE B' )
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
		#                         'accounts',
		#                         'files',
		#                         'log_connection',
		#                         'log_transfer',
		#                         'log_error',
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

		# _.pr( 'HERE C' )
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
		#     _.pr(x)
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
		_.pr(data)

	def close( self ):
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
			# _.pr( '\t\t', table_label )
			for rec in table:
				record = {}
				for i,field in enumerate(rec):
					record[  self.table_fields[table_label][i]  ] = field
					if type(field) == datetime.datetime:
						record[  self.table_fields[table_label][i]  ] = str(field)
					# _.pr( '\t\t\t', self.table_fields[table_label][i], type(field), field )
				records.append(record)
			return records
		return table

	def check_structure( self ):
		self.tables_app_live = []
		# _.pr('A')
		for tbl in self.tables_app_list:
			self.tables_app_live.append( self.table_prefix+'_'+tbl )

		self.live_tables = []
		for table in self.query('show tables'):
			self.live_tables.append(table[0])

		# _.pr('B')
		for table in self.tables_app_live:
			if not table in self.live_tables:
				self.table_setup(table)
			# else:
				# _.pr(table)

		# _.pr('C')
		for table in self.query('show tables'):
			if table[0] in self.tables_app_live:
				this_label = table[0][len(self.table_prefix+'_'):]
				self.table_fields[ this_label ] = []
				# _.pr( this_label )
				for field in self.query('SHOW COLUMNS FROM ' + table[0]):
					# _.pr( '\t', field[0] )
					self.table_fields[ this_label ].append( field[0] )
		# _.pr('D')


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
		# _.pr( 'cloud_path:', cloud_path )
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
			# _.pr( 'updating...' )
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
			# _.pr( 'inserting...' )
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

		# _.pr(sql)
		# _.pr(sql)

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
		# _.pr(sql)
		records =  self.query(sql,table)
		# _.pr( records )
		if single is None:
			return records
		else:
			if not len(records):
				return None
			else:
				# _.pr(records[0][single])
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
			_.pr( 'Error: gen_paths - ', __.LOOP['gen_paths'], path )
			if __.LOOP['gen_paths'] < 10:
				cloud_path = self.gen_paths(path)['cloud']
			else:
				cloud_path = path

		result = {
					'local': __.cloud.structure['local']['tech'] + cloud_path.replace( _v.slashes['u'], _v.slash ),
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
			_.pr( 'Error: gen_paths - ', __.LOOP['gen_paths'], path )
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


def actionRequest( classy, label, action=None, error=None, success=None ):

	if success:
		return True
	if action is None:
		_.colorThis( [ 'Error:', classy, label ], 'red' )
	elif not action is None:
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
		if __.cloud.attempt[classy][label][attempt] > 0:
			rest_for += 2
		if __.cloud.attempt[classy][label][attempt] > 1:
			rest_for += 2
		if __.cloud.attempt[classy][label][attempt] > 2:
			rest_for += 2
		error_rest( rest_for, __.cloud.attempt[classy][label][attempt])
		

		if __.cloud.attempt[classy][label][attempt] < 4:
			_.pr( 'return False' )
			return False
		else:
			_.pr( 'return True' )
			return True

	elif not action is None:
		if not file_action in __.cloud.attempt[classy][label]:
			__.cloud.attempt[classy][label][  file_action  ] = {}
			__.cloud.attempt[classy][label][  file_action  ][attempt] = 0
		__.cloud.attempt[classy][label][  file_action  ][attempt] +=1

		rest_for = 0
		if __.cloud.attempt[classy][label][  file_action  ][attempt] > 0:
			rest_for += 2
		if __.cloud.attempt[classy][label][  file_action  ][attempt] > 1:
			rest_for += 2
		if __.cloud.attempt[classy][label][  file_action  ][attempt] > 2:
			rest_for += 2

		error_rest( rest_for, __.cloud.attempt[classy][label][  file_action  ][attempt])
		if __.cloud.attempt[classy][label][  file_action  ][attempt] < 4:
			_.pr( 'return False' )
			return False
		else:
			_.pr( 'return True' )
			return True
			
# def result( classy, label, record=None ):
#     attempt = '0012814A-B08D-448D-89C9-715BEB6182F1'
#     if record is None:
#         on = 



# class Negotiator:
#     def __init__( self, db ):
#         self.db = db

def error_rest( cnt, eN ):
	_.colorThis(   ['Attempt:', eN, 'resting for', cnt], 'red'   )
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
		file = _.getText( path, raw=True )
		file = file.replace( chr(10), '\n' )
		_.saveText( file, path )


def formatDate(date):
	theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y_%m_%d-%H_%M_%S')
	theDate = str(theDate)
	return theDate








__.cloud = CLOUD_VAR()

import _rightThumb._md5 as _md5

import _rightThumb._simpleThreads as _threads

import _rightThumb._tz as _tz
# _.pr( '__.cloud' )


# import inspect
# x = inspect.getargspec(SSHTunnelForwarder)
# _.pr(x)

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


# https://www.reddit.com/r/learnpython/comments/53wph1/connecting_to_a_mysql_database_in_a_python_script/

########################################################################################
if __name__ == '__main__':
	action()


# check_structure
# search_table_version



