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
	_.switches.register( 'Files', '-f,-file,-files', 'file.txt' )
	_.switches.register( 'Folders', '-fo,-folder,-folders', 'desk docs' )
	_.switches.register( 'Recursive', '-r,-recursive' )
	_.switches.register( 'SubFolders', '-sf,-sub,-subfolders' )
	_.switches.register( 'Version', '-v,-version' )
	_.switches.register( 'Versions', '-vs,-versions' )
	_.switches.register( 'Case', '-case' )
	_.switches.register( 'Extensions', '-ext', 'db image graphic video app audio doc script archive' )
	_.switches.register( 'FileExists', '-e,-exist,-exists' )
	_.switches.register( 'FileDoesNotExist', '-ne,-dne,-notexist,-notexists,-doesnotexist' )
	_.switches.register( 'Copy', '-copy' )
	_.switches.register( 'SuppressAsk', '-y' )
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'Date', '-date' )
	_.switches.register( 'AllFields', '-all' )


	pass


# _.autoBackupData = __.autoCreationConfiguration['backup']
_.autoBackupData = False
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'inBackup.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'find things in backup',
	'categories': [
						'backup',
						'tool',
						'os',
						'files',
						'folders',
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
						'p inBackup',
						'p inBackup -file file.txt',
						'p inBackup -subfolders',
						'p inBackup -subfolders -recursive',
						'p inBackup -sub -r',
						'',
						'b doc',
						'p inBackup -folders -files -version',
						'p inBackup -folder doc    -sub  -files -version',
						'p inBackup -folder doc    -sub -r -files -version',
						'',
						'p inBackup -folder D:\\_Scott    -sub -case',
						'',
						'p inBackup -folder D:\\_Scott    -sub -case -r -files + *.txt -v -vs',
						'',
						'p inBackup -f %tmpf0%    -vs -v',
						'p inBackup -v -vs -f %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9%',
						'',
						'p inBackup -folder D:\\_Scott    -sub -case -r -files + *.txt    -v -vs  -ago 2020-08-01',
						'p inBackup -folder D:\\_Scott    -sub -case -r -files + *.txt    -v -vs  -ago 2019-08-01 2020-08-02',
						'',
						'p inBackup -folder D:\\_Scott    -sub -case -r + *.txt    -v -vs  -ago 2020-08-01 2020-08-01    -files',
						'p inBackup -folder D:\\_Scott    -sub -case -r + *.txt    -v -vs  ',
						'p inBackup -folder D:\\_Scott    -sub -case -r + *.txt    -v -vs -files',
						'p inBackup -folder D:\\_Scott    -sub -case -r + *.txt    -v  -files',
						'',
						'10 C:\\Users\\Scott\\Documents\\00.txt',
						' isfile inBK  PATH',
						'',
						'',
						'p inBackup -f ls.py   -c n v b d c    -copy',
						'p inBackup -f ls.py   -c n v b d c    -copy  -vs',
						'',
						'p inBackup -v -vs -f %tmpf0% %tmpf1% %tmpf2% %tmpf3% %tmpf4% %tmpf5% %tmpf6% %tmpf7% %tmpf8% %tmpf9% -c n r v b -aggregate "eot?newest-date=max(date,?date); eof?bk-total = add(bk); config(?var,?all,?first); format(eot?newest-date,?date); format(eof?bk-total,?comma); bk = add(len(backup)); eof?latest=max(date,?date); format(eof?latest,?date);"',
						'',
						'p inBackup -f ls.py -v -vs -c n t v b ago woy month -aggregate " isDate(timestamp); "',
						'',
	],
	'columns': [
					{ 'name': 'name', 'abbreviation': 'n' },
					# { 'name': 'path', 'abbreviation': 'p' },
					{ 'name': 'resolved', 'abbreviation': 'r' },
					{ 'name': 'date', 'abbreviation': 'd' },
					{ 'name': 'backup', 'abbreviation': 'b' },
					{ 'name': 'copied', 'abbreviation': 'c' },
					{ 'name': 'version', 'abbreviation': 'v' },
					{ 'name': 'timestamp', 'abbreviation': 't' },
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folders', _.myFolderLocations )
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


class backupLogManager:
	def __init__( self, 
							recursive=False,
							subfolders=False,
							allfields=False,
							date=False,
							version=False,
							versions=False,
							case=False,
							extensions=False,
							extensionList=[],
							fileExists=False,
							fileNotExists=False,
							copy=False,
							noAsk=False,
							ago=[],
							files=False,
							columns=[],
				):

		_.fields.register( 'epoch', 'val', 12, m=12 )
		self.settings = _.dot()
		self.settings.recursive = recursive
		self.settings.subfolders = subfolders
		self.settings.allFields = allfields
		self.settings.date = date
		self.settings.version = version
		self.settings.versions = versions
		self.settings.case = case
		if _.isWin and not case:
			self.settings.case = True

		self.settings.extensions = extensions

		self.settings.fileExists = fileExists
		self.settings.fileNotExists = fileNotExists
		self.settings.copy = copy
		self.settings.files = files
		self.settings.columns = columns
		self.firstTable = True

		if 'version' in columns:
			self.settings.version = True


		# if copy and self.settings.versions:
		#     _.cp( [ 'Disabled: log.settings.versions' ], 'green' )
		#     self.settings.versions = False


		self.ago = ago

		# _.pr(self.ago)
		# _.pr( _.switches.value('Ago') )
		# sys.exit()

		if noAsk:
			self.settings.ask = False
		else:
			self.settings.ask = True


		self.extensions = extensionList
		global registered_ids
		self.registered_ids = registered_ids


		self.log = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )
		self.files = {}
		self.folders = {}
		self.folders_recursive = {}
		self.spent = {}
		self.spent_copy = {}
		self.spent_folders = {}

		self.lastBlank = False
		self.folder_files = []
		self.hasID = False
		self.index()
		# id timestamp file backup mime status session version v v1 v2 v3 flag
		
		# self.settings.columns
		# name resolved version date backup

	def subject( self, subject ):
		if self.settings.case:
			return subject
		else:
			return subject.lower()

	def newestFile( self, subject ):
		if self.subject(subject) in self.files:
			rec = self.files[self.subject(subject)]

			record = self.log[ rec[ len(rec)-1 ] ]
			parts = record['file'].split(_v.slash)
			parts.reverse()
			record['name'] = parts.pop(0)
			return record
		return None
	
	def newestFileID( self, fileID ):
		subject = self.log[fileID]['file']
		return self.newestFile(subject)

	def index( self ):
		for i,record in enumerate(self.log):
			f = self.subject(record['file'])
			if not f in self.files:
				self.files[f] = []
			self.files[f].append(i)
			fl = _v.popFile( f )
			# _.pr(fl)
			# _.pr( len(self.log) )
			if not fl in self.folders:
				self.folders[fl] = []
			self.folders[fl].append(i)
			# if not fl in self.folders_recursive:
			# self.folders_recursive[fl] = {}
			self.folders_not_recursive = {}
			if _.isWin:
				if not fl[0]+':' in self.folders_recursive:
					self.folders_recursive[ fl[0]+':' ] = {}
				if not fl in self.folders_recursive[ fl[0]+':' ]:
					self.folders_recursive[ fl[0]+':' ][fl] = {}
			bs = fl
			last = fl
			while not fl is None and fl.count(_v.slash) > 1:
				fl = _v.popFile( fl )
				# if fl == 'D:\\_Scott' and last.count('\\') == 2: _.pr( last );
				# if fl == 'D:\\_Scott': _.pr( bs );
				# if fl.startswith('d:') and fl.count(_v.slash) <= 1: _.pr(fl);

				if not fl in self.folders_recursive:
					self.folders_recursive[fl] = {}
				self.folders_recursive[fl][bs] = {}
				if not last in self.folders_recursive[fl]:
					self.folders_recursive[fl][last] = {}
					# if fl == 'D:\\_Scott' and last.count('\\') == 2: _.pr( last );

				if _.isWin:
					if not fl[0]+':' in self.folders_recursive:
						self.folders_recursive[ fl[0]+':' ] = {}
					if not fl in self.folders_recursive[ fl[0]+':' ]:
						self.folders_recursive[ fl[0]+':' ][fl] = {}
				last = fl


				# _.pr( fl, bs )
	def folder( self, subject ):
		if _.isWin:
			subject = _str.cleanBE( subject, _v.slash )
		if os.path.isdir(subject):
			exist = '1'
		else:
			exist = '0'
		if self.subject(subject) in self.folders:
			exist += '1'
		else:
			exist += '0'
		_.cp( [ exist, subject ], 'yellow' )
		if self.settings.files:
			showFiles = True
		else:
			showFiles = False

		if self.settings.subfolders:
			c = subject.count(_v.slash)
			# _.pr(subject)
			if self.subject(subject) in self.folders_recursive:
				result = []
				for f in self.folders_recursive[self.subject(subject)]:
					if self.settings.recursive:
						result.append( f )
					else:
						if f.count(_v.slash) == c+1:
							result.append(f)
				result.sort()
				
				for f in result:
					self.folder_files = []
					self.hasID = False
					files = []
					# _.pr(self.settings.files)
					if not self.settings.files:
						_.pr()
						_.cp( [ '\t', f ], 'cyan' )
					if showFiles:
						if self.subject(f) in self.folders:
							for fileID in self.folders[self.subject(f)]:
								self.file( fileID=fileID, build=True )

									# _.cp( [ '\t\t', file['version'], file['name'],'\t',file['backup'] ], 'darkcyan' )
					self.printFiles(f)
								

	def printFiles( self, folder=None ):
		if len(self.folder_files):
			if self.folder_files[ len(self.folder_files)-1 ]['backup'] == '':
				self.folder_files.pop( len(self.folder_files)-1 )
			_.tables.register( 'files', self.folder_files, tab='\t  ' )
			
			# self.fields = 'name,resolved,version,date,backup,path'
			self.fields = 'name,resolved,version,date,backup'
			fields_backup = self.fields
			if not self.settings.version:
				self.fields = self.fields.replace( 'version,', '' )
			if not self.hasID:
				self.fields = self.fields.replace( 'resolved,', '' )

			if not folder is None and not self.subject(folder) in self.spent_folders:
				self.spent_folders[self.subject(folder)] = 1
				_.pr()
				_.cp( [ '\t', folder ], 'cyan' )

			if self.settings.copy:
				self.fields = self.fields.replace( 'backup', 'copied' )

			if not self.settings.date:
				self.fields = self.fields.replace( 'date,', '' )

			if self.settings.allFields:
				self.fields = fields_backup

			if len(self.settings.columns):
				xFields = []
				for xF in self.settings.columns:
					if not xF in xFields:
						xFields.append(xF)
				self.fields = ','.join(xFields)


			_.tables.print( 'files', self.fields, printColumns=self.firstTable )
			self.firstTable = False


		# for record in self.log:
		#     _.pr( ' '.join(list(record.keys())) )
		#     sys.exit()

	def copyFile( self, path=None, fileID=None ):
		if not fileID is None:
			file = self.newestFileID(fileID)
		if not path is None:
			file = self.newestFile(path)
		if file is None:
			# _.cp( 'Error: unable to copy file', 'red' )
			# _.cp( [ '\t', path ], 'red' )
			return 'Error: path'

		if not os.path.isfile( file['backup'] ):
			# _.cp( 'Error: unable to copy file', 'red' )
			# _.cp( [ '\t', file['file'] ], 'red' )
			return 'Error: backup'
		if os.path.isfile( file['file'] ):
			# _.cp( [ 'File exists, skipped:', file['file'] ], 'green' )
			return 'Skipped: exists'


		if self.subject(file['file']) in self.spent_copy:
			return 'Skipped: alread copied'
		self.spent_copy[self.subject(file['file'])] = 1

		if not _v.popFileDir(file['file']):
			return 'Error: folder'


		try:
			copyfile( file['backup'], file['file'] )
			return file
		except Exception as e:
			return 'Error: copy failure'


	def file( self, path=None, fileID=None, build=False, single=False ):
		
		if single:
			self.folder_files = []
			self.hasID = False


		if not fileID is None:
			files = [self.newestFileID(fileID)]
		if not path is None:
			files = [self.newestFile(path)]
		if len(files):
			try:
				path = files[0]['file']
			except Exception as e:
				return None
		if self.settings.versions:
			filesX = []
			if self.subject( files[0]['file'] ) in self.files:
				for file in self.files[self.subject( files[0]['file'] )]:
					record = self.log[file]
					filesX.append( record )
			files = filesX
			

		for file in files:
			if not file is None:
				path = file['file']
				# if True:
				if not self.subject(file['backup']) in self.spent:
					self.spent[ self.subject(file['backup']) ] = 1
					if _.showLine(file['name']):
						shouldAdd = True
						if self.settings.extensions:
							shouldAdd = False
							
							for ext in self.extensions:
								if file['name'].lower().endswith( ext ):
									shouldAdd = True
						
						if self.settings.fileExists:
							if not os.path.isfile( file['file'] ):
								shouldAdd = False
						if self.settings.fileNotExists:
							if os.path.isfile( file['file'] ):
								shouldAdd = False


						if shouldAdd and len(self.ago):
							shouldAdd = False
							if len(self.ago) == 2:
								if file['timestamp'] > self.ago[0] and file['timestamp'] < self.ago[1]:
									shouldAdd = True
							if len(self.ago) == 1:
								if file['timestamp'] > self.ago[0]:
									shouldAdd = True


						if shouldAdd:
							if build:
								self.lastBlank = False
								record = { 'version': file['version'], 'name': file['name'], 'backup': file['backup'], 'resolved': '', 'date': _.friendlyDate(file['timestamp']), 'copied': 'not attempted', 'path': file['file'], 'timestamp': file['timestamp'] }
								if self.settings.copy:
									copyStatus = self.copyFile( file['file'] )
									if type(copyStatus) == str:
										record['copied'] = copyStatus
									elif type(copyStatus) == dict:
										record['version'] = copyStatus['version']
										record['backup'] = copyStatus['backup']
										record['copied'] = 'copied :)'
										record['date'] = _.friendlyDate(copyStatus['timestamp'])
										
							
								if record['name'] in self.registered_ids:
									self.hasID = True
									record['resolved'] = self.registered_ids[record['name']]
								self.folder_files.append(record)
		if self.settings.versions:
			if build:
				if len(self.folder_files) and not self.lastBlank:
					self.lastBlank = True
					# self.folder_files.append({ 'version': '', 'name': '', 'backup': '' })

		if single:
			if os.path.isfile(path):
				exist = '1'
			else:
				exist = '0'
			if self.subject(path) in self.files:
				exist += '1'
			else:
				exist += '0'

			_.cp( [ exist, path ], 'yellow' )
			self.printFiles()

	def ts( self, timestamp ):
		return _.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[0]  ) )+'.'+_.fields.padZeros( 'epoch', 'val', int(  str(timestamp).split('.')[1] ) )


extensionList = []
def extensionsDatabank():
	global extensionList
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )

	for index in _.switches.values('Extensions'):
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )
				


def action():
	
	global selection
	global log
	load()



	for subject in selection:
		if os.path.isfile( subject ):
			subject = os.path.abspath( subject )
			log.file( path=subject,  build=True, single=True )
		elif os.path.isdir( subject ):
			log.folder( subject )
		elif _.switches.isActive('Folders'):
			log.folder( subject )
		elif _.switches.isActive('Files'):
			log.file( path=subject,  build=True, single=True )
	try:
		if not log.settings.copy and 'copied' in log.fields:
			_.cp( [ '\n\n','', 'add: -copy' ], 'red' )
	except Exception as e:
		_.cp( 'Error: not found', 'red' )


def load():
	global selection
	global extensionList
	global log
	global registered_ids

	registered_ids = _.getTable('registered-ids.index')

	if _.switches.isActive('Extensions'):
		extensionsDatabank()


	if _.switches.isActive('Versions'):
		_.switches.fieldSet( 'GroupBy', 'active', True )
		_.switches.fieldSet( 'GroupBy', 'value', 'name,resolved' )
		_.switches.fieldSet( 'GroupBy', 'values', 'name,resolved'.split(',') )
		_bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )
		_bkLog.do( _bkLog.imp.autoFileVersion )

	_.switches.fieldSet( 'Long', 'active', True )
	if _.switches.isActive('Folders') and not len(_.switches.value('Folders')):
		_.switches.fieldSet( 'SubFolders', 'active', True )

	if _.switches.isActive('Files') and not len(_.switches.value('Files')):
		showFiles = True
	else:
		showFiles = False

	log = backupLogManager(
								recursive=_.switches.isActive('Recursive'),
								subfolders=_.switches.isActive('SubFolders'),
								allfields=_.switches.isActive('AllFields'),
								date=_.switches.isActive('Date'),
								version=_.switches.isActive('Version'),
								versions=_.switches.isActive('Versions'),
								case=_.switches.isActive('Case'),
								extensions=_.switches.isActive('Extensions'),
								extensionList=extensionList,
								fileExists=_.switches.isActive('FileExists'),
								fileNotExists=_.switches.isActive('FileDoesNotExist'),
								copy=_.switches.isActive('Copy'),
								noAsk=_.switches.isActive('SuppressAsk'),
								ago=_.switches.values('Ago'),
								files=showFiles,
								columns=_.switches.values('Column'),
							)
	selection = []
	if type(_.appData[__.appReg]['pipe']) == list:
		selection = selection + _.appData[__.appReg]['pipe']
	if _.switches.isActive('Files'):
		selection = selection + _.switches.values('Files')
	if _.switches.isActive('Folders'):
		selection = selection + _.switches.values('Folders')

	if not selection:
		selection = [os.getcwd()]

if _.switches.isActive('Copy'):
	from shutil import copyfile



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()






