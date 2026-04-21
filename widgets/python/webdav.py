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
import sys, time, os
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################


def sw():
	pass
	#b)--> examples
	_.switches.register( 'Download', '-dl,-download' )
	_.switches.register( 'Clean', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
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
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): _.pr(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: _.pr(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start





_vault = _.regImp( __.appReg, '_rightThumb._vault' )
import os
import requests
from requests.auth import HTTPDigestAuth

class WebDAVClient:
	def __init__(self):
		self.webdavMeta = '.webdav.meta'
		_.v.quiet = _.switches.isActive('Clean')

	def create_all_folders(self, remote_folder_path):
		"""Recursively creates all folders in the path."""
		folders = remote_folder_path.split('/')
		current_path = ''
		for folder in folders:
			current_path += folder + '/'
			_.pr(current_path)
			if not self.create_folder(current_path):  # If it returns False, there was an error
				_.pr(f"Failed to create {current_path}")
				return False
		return True

	def create_folder(self, remote_folder_path):
		""" Creates a folder on the WebDAV server. """
		if self.folder_exists(remote_folder_path):
			return True
		else:
			response = requests.request(
				'MKCOL',
				f"{self.host_url}/{remote_folder_path}",
				auth=(self.username, self.password)
			)
			
			if response.status_code in [201, 405]:  # 201 means Created, 405 means Already exists
				return True
			else:
				_.pr(f"Failed to create folder. HTTP Status Code: {response.status_code}")
				_.pr(response.text)
				return False

	def folder_exists(self, remote_folder_path):
		"""Check if a folder exists on the WebDAV server."""
		response = requests.request(
			'PROPFIND',
			f"{self.host_url}/{remote_folder_path}",
			auth=(self.username, self.password)
		)
		
		return response.status_code == 207

	def upload(self, path):
		self.scan(path)
		local_file_path  = self.local
		remote_file_path = self.remote
		if '/' in remote_file_path:
			remote_folder_path = os.path.dirname(remote_file_path).replace(os.sep,'/')
			_.pr(len(self.remote.split('/')))
			if len(self.remote.split('/')) > 2:
				self.create_all_folders(remote_folder_path)
			else:
				self.create_folder(remote_folder_path)
		with open(local_file_path, 'rb') as file:
			response = requests.put(
				f"{self.host_url}/{remote_file_path}",
				data=file,
				auth=(self.username, self.password)
			)

			if response.status_code == 201:
				_.pr('uploaded')
				# _.pr(f"File uploaded successfully to {self.host_url}/{remote_file_path}")
				return True
			else:
				_.pr(f"Failed to upload file. HTTP Status Code: {response.status_code}")
				_.pr(response.text)
				return False

	def download(self, path):
		self.scan(path)
		local_file_path  = self.local
		remote_file_path = self.remote
		remote_folder_path = os.path.dirname(remote_file_path)
		response = requests.get(
			f"{self.host_url}/{remote_file_path}",
			auth=(self.username, self.password)
		)

		if response.status_code == 200:
			with open(local_file_path, 'wb') as file:
				file.write(response.content)
			_.pr('downloaded')
			# _.pr(f"File downloaded successfully to {local_file_path}")
			return True
		else:
			_.pr(f"Failed to download file. HTTP Status Code: {response.status_code}")
			_.pr(response.text)
			return False

	def scan(self, path):
		global folder
		if not _.v.quiet: _.pr(path,c='cyan')
		self.meta = {}
		try:
			file = os.path.abspath(path)
		except Exception as e:
			file = path
		if os.path.isfile(path):
			folder = __.path(path,pop=True)
		else:
			folder = __.path(path)
		if os.path.isdir(path):folder+=os.sep
		i=0

		while not os.path.isfile( folder+os.sep+self.webdavMeta ):
			i+=1
			if i > 100:
				_.e('missing folder meta,9ba3')
			try:
				folder = __.path(folder,pop=True)
			except Exception as e:
				break
		mPath = folder+os.sep+self.webdavMeta
		locations=_.getTable('webdav-locations.list')
		loc=locations.copy()
		if not mPath in locations: locations.append(mPath)
		if not locations == loc: _.saveTable(locations,'webdav-locations.list')

		if _.getText( mPath, raw=True ).strip().startswith('{'): self.meta = _.getTable2( mPath )
		else: self.meta = _.getYML( mPath )
		if not _.v.quiet:
			if not _.switches.isActive('mkdir'):
				_.cp(mPath,'yellow')
				_.pv(self.meta)
		fiA = mPath.replace(self.webdavMeta,'')
		# self.local=file.replace(fiA,'')
		self.remote=file.replace(fiA,'').replace(os.sep,'/')
		# self.remote=self.meta['webdav']['server']+'/'+self.local
		self.local=path
		self.host_url = self.meta['webdav']['server'].rstrip('/')
		self.username = self.meta['webdav']['user']
		self.password = _vault.imp.s.de(self.meta['webdav']['password'])
		# _.pr(self.host_url)
		# _.pr(self.username)
		# _.pr(self.password)
		# _.pr(self.local)
		# _.pr(self.local)
		return self.meta



def aliases(fi):
	aliases=_.getTable('file-open-aliases.hash')
	if not 'aliases' in aliases: aliases['aliases']={}
	if not 'files' in aliases: aliases['files']={}
	if fi in aliases['aliases']:
		fi = aliases['aliases'][fi]
	return fi

def action():
	client = WebDAVClient()
	for path in _.pp():
		if not os.path.isfile(path):
			path = aliases(path)
		if _.switches.isActive('Download'):
			client.download(path)
		else:
			client.upload(path)
	
	# client = WebDAVClient("https://your-webdav-server.com/dav", "your_username", "your_password")
	# client.upload("path/to/local/upload/file.txt", "destination/on/webdav/file.txt")
	# client.download("destination/on/webdav/file.txt", "path/to/local/download/file.txt")


##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)





