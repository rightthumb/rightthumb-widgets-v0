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
	pass
	# _.switches.register( 'Alias', '-a' )
	# _.switches.register( 'Save', '-save' )
	# _.switches.register( 'm', '-m' )
	# _.switches.register( 'b', '-b' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '_rightThumb._bookmarks',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage bookmarks',
	'categories': [
						'bm',
						'bookmarks',
						'manage',
						'system',
				],
	'usage': [
						'import _rightThumb._bookmarks as _bm',
						'path = _bm.Bookmarks( _.switches.value(\'Alias\') ).get()',
						'',
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
						'',
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

def c41(strin):
	return strin.replace('\\',os.sep).replace('/',os.sep)
this = _.Meta_Namespace()

class Bookmarks:
	def __init__( self, alias=None, path=None ):
		self.index = _.getTable( 'bookmarks.index' )
		if self.index == {}:
			self.index = {
							'labels': {},
							'paths': {},
			}

		self.current = __.path('.')
		self.alias = alias
		self.path = path
		self.folder = None

		if path is None:
			self.bm = 'b'
		else:
			self.bm = 'm'

	pass
	
	def this_index( self, db ):
		try:
			this.index
			return this.index
		except: pass
		new = False
		this.index = _.getTable2( db )
		if not 'labels' in this.index:
			new = True
			this.index['labels'] = {}
		if not 'paths' in this.index:
			new = True
			this.index['paths'] = {}
		_.saveTable2( this.index, db, p=0 )
		if new:
			_.pr( 'Created:', db )
			os.chmod( db, 0o777)
		return this.index

	def xferToUser( self, path=None ):
		if path is None: path = __.path( os.getcwd() )
		home = '/root/'
		subjects = []
		subjects.append( '/home/UNIVERSAL' )
		if  path.startswith( '/home/' ):
			parts = path.split( '/' )
			if len(parts) > 2:
				subjects.append( '/home/'+parts[2] )
				home = '/home/'+parts[2] + '/'
		else:
			subjects.append( path )
			home = 'b4b6842130c8'
			while not os.path.isdir( home ):
				home = '/home/'+ input('user: ') + '/'
		db = home + '.rt/profile/tables/bookmarks.index'
		if not _.canWrite( db ):
			_.e( 'Cannot write to:', db )
			return
		self.this_index( db )
		labels = {}
		paths = {}

		spent = []
		
		# if path in self.index['labels']:
			# for bm in self.index['labels'][path]: _.pr( bm )
		for bm in this.index['labels']:
			spent.append( bm )



		for bm in self.index['labels']:
			if bm not in spent:
				for sub in subjects:
					if self.index['labels'][bm].startswith( sub ):
						_.pr( bm, self.index['labels'][bm], c='cyan' )
						labels[bm] = self.index['labels'][bm]
						paths[self.index['labels'][bm]] = bm
						spent.append( bm )
		for bm in labels:
			this.index['labels'][bm] = labels[bm]
		for pth in paths:
			if not pth in this.index['paths']:
				this.index['paths'][pth] = []
			this.index['paths'][pth].append( paths[pth] )		
		
		


	def reverse( self, path=None ):
		spent = []
		if path is None: path = __.path('.')
		# if path in self.index['labels']:
			# for bm in self.index['labels'][path]: _.pr( bm )
		for bm in self.index['labels']:
			if path == self.index['labels'][bm]:
				if bm not in spent:
					_.pr( bm )
					spent.append( bm )

				# _.pr( self.index['labels'][path] )
			if path == self.index['labels'][bm]:
				if bm not in spent:
					_.pr( bm )
					spent.append( bm )
		spath = self.sanitize(path).replace('\\','/')
		if spath in self.index['labels']:
			for bm in self.index['labels'][spath]:
				if bm not in spent:
					_.pr( bm )
					spent.append( bm )
		# spath = spath.replace('\\','/')
		spath2 = spath.replace('/','\\')
		# print( spath )
		# if spath in self.index['labels']:
			# for bm in self.index['labels'][spath]: _.pr( bm )
		for bm in self.index['labels']:
			if spath2 == self.index['labels'][bm]:
				if bm not in spent:
					_.pr( bm )
					spent.append( bm )
			if spath == self.index['labels'][bm]:
				if bm not in spent:
					_.pr( bm )
					spent.append( bm )
		# _.pr(spath)
		# return None
		# if spath in self.index['paths']:
		# 	for bm in self.index['paths'][spath]:
		# 		_.pr( bm )


	def sanitize( self, path=None ):
		if not path is None: self.folder = _v.sanitizeFolder( path );
		else: self.folder = _v.sanitizeFolder( self.path );
		return c41(self.folder)

	def resolve( self, path ):
		self.folder = _v.resolveFolderIDs(path)
		if not _.isWin: self.folder = self.folder.replace( '\\', '/' );
		return c41(self.folder)

	def file( self ):
		return _v.bookmarkFormat.replace( 'ALIASHERE', self.alias )

	def log( self ):
		log = _.getTable( 'bookmarks.logs' )
		if not self.bm in log: log[self.bm] = [];
		log[self.bm].append({ 'epoch': time.time(), 'alias': self.alias, 'location': self.folder, 'session': _v.session() })
		_.saveTable( log, 'bookmarks.logs', p=0 )

	###########################################################################################
	def save( self ):
		b = self.file()
		p = self.sanitize()
		_.saveText( p, b )

		if self.alias in self.index['labels'].keys():
			old = self.index['labels'][self.alias]
			if p in self.index['paths'].keys():
				nX = []
				for record in self.index['paths'][p]:
					if not record == self.alias:
						nX.append( record )
				self.index['paths'][p] = nX
			if not _.switches.isActive('Clean'):
				old2=self.resolve(old)
				_.colorThis( [  '\told', old  ], 'yellow' )
				if not old==old2:
					_.colorThis( [  '\told', old2  ], 'yellow' )
			if os.path.isdir(  self.resolve(old)  ):
				status = 'still exists'
				if not _.switches.isActive('Clean'):
					_.colorThis( [  '\t\t', status  ], 'green' )
			else:
				status = 'no longer exists'
				if not _.switches.isActive('Clean'):
					_.colorThis( [  '\t\t', status  ], 'red' )
		self.index['labels'][self.alias] = p
		self.index['labels'][self.alias.lower()] = p

		if p in self.index['paths'].keys():
			self.index['paths'][p].append( self.alias )
		else:
			self.index['paths'][p] = []
			if not self.alias in self.index['paths'][p]:
				self.index['paths'][p].append( self.alias )
		_.saveTable( self.index, 'bookmarks.index', p=0 )
		if not _.switches.isActive('Clean'):
			_.colorThis( [  self.alias, self.current  ], 'cyan' )
		self.log()
		return c41(self.folder)
	###########################################################################################

	def get2( self ):
		if not self.alias in self.index['labels'] and not self.alias.lower() in self.index['labels']:
			return None
		for alias in self.index['labels']:
			if alias == self.alias or alias.lower() == self.alias:
				fo = _v.resolveFolderIDs(self.index['labels'][alias])
				# print('Alias:',fo)
				return fo

	def get( self ):
		if not self.alias in self.index['labels'] and not self.alias.lower() in self.index['labels']:

			return None
		try:
			self.resolve( self.index['labels'][self.alias] )
		except Exception as e:
			self.resolve( self.index['labels'][self.alias.lower()] )

		self.log()
		return c41(self.folder)

def action():
	pass

made={}
if 'wprofile' in _v.config_hash:
	made['h'] = 1
	h  = _v.config_hash['wprofile']
if 'ww' in _v.config_hash:
	made['ww'] = 1
	ww = _v.config_hash['ww']
# _.pr('made',made)
if 'ww' in made  and 'h' in made:
	try:
		a = ww+os.sep+'databank'+os.sep+'tables'+os.sep+'bookmarks.index'
		b = h+os.sep+'tables'+os.sep+'bookmarks.index'
		if not os.path.isfile(b) and os.path.isfile(a):
			from shutil import copyfile
			copyfile(a,b)
	except Exception as e:
		pass


########################################################################################
if __name__ == '__main__':
	action()






