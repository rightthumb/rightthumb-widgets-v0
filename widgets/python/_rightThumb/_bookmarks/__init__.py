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
	'file': 'bookmarks.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage bookmarks',
	'categories': [
						'bm',
						'bookmarks',
						'manage',
						'system',
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



class Bookmarks:
	def __init__( self, alias=None, path=None ):
		self.index = _.getTable( 'bookmarks.index' )
		if self.index == {}:
			self.index = {
							'labels': {},
							'paths': {},
			}

		self.current = os.getcwd()
		self.alias = alias
		self.path = path
		self.folder = None

		if path is None:
			self.bm = 'b'
		else:
			self.bm = 'm'

	pass
	


	def sanitize( self ):
		self.folder = _v.sanitizeFolder( self.path )
		return self.folder

	def resolve( self, path ):
		self.folder = _v.resolveFolderIDs(path)
		if not _.isWin:
			self.folder = self.folder.replace( '\\', '/' )
		return self.folder

	def file( self ):
		return _v.bookmarkFormat.replace( 'ALIASHERE', self.alias )

	def log( self ):
		log = _.getTable( 'bookmarks.logs' )
		if not self.bm in log:
			log[self.bm] = []
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
				_.colorThis( [  '\told', old  ], 'yellow' )
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
		return self.folder
	###########################################################################################
	def get( self ):
		if not self.alias in self.index['labels'] and not self.alias.lower() in self.index['labels']:

			return None
		try:
			self.resolve( self.index['labels'][self.alias] )
		except Exception as e:
			self.resolve( self.index['labels'][self.alias.lower()] )

		self.log()
		return self.folder

def action():
	pass

made={}
if 'wprofile' in _v.config_hash:
	made['h'] = 1
	h  = _v.config_hash['wprofile']
if 'ww' in _v.config_hash:
	made['ww'] = 1
	ww = _v.config_hash['ww']
# print('made',made)
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





