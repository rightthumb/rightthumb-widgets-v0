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
	_.switches.register( 'Subject', '-app,-sub,subject', 'ftp' )
	_.switches.register( 'Files', '-f,-file,-files','app.py', isData='name', description='Files' )
	_.switches.register( 'Folders', '-fo,-folder,-folders', 'python' )
	pass

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
	'file': 'meta.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'simple meta editor ( in external json files )',
	'categories': [
						'meta',
						'file',
						'folder',
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
						_.hp('p meta -app ftp'),
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

def scan_meta(pathy=None):
	if pathy is None:
		pathy = os.getcwd()
	if os.path.isfile(pathy):
		p = __.path(pathy,pop=True)
	elif os.path.isdir(pathy):
		p = __.path(pathy)
	else:
		return {}
	children_meta = []
	while True:
		test = p +os.sep+ '.folder.meta'
		test = test.replace(os.sep+os.sep,os.sep)
		if os.path.isfile(test):
			meta_folders_table(test)
			_.cp( [str(len(children_meta))+':',p], 'yellow')
			children_meta.append( __.getTable(test) )
		p = __.path(p,pop=True)
		if not os.sep in p:
			return children_meta
		# try:
		#     p = __.path(p,pop=True)
		# except Exception as e:
		#     return children_meta



def dic_order(m):
	n = {}
	for k in v.order:
		if k in m:
			n[k] = m[k]
	for k in m:
		if not k in n:
			n[k] = m[k]
	return n

def action():
	load()
	global meta
	if _.switches.isActive('Subject'):
		for k in _.switches.values('Subject'):
			if not k in meta:
				meta[k] = template(k)
				meta = dic_order(meta)

		_.saveTable2( meta, '.folder.meta' )
		meta_folders_table('.folder.meta')

	if os.path.isfile('.folder.meta'):
		os.system( 'n .folder.meta' )
	
	if v.f:
		for p in v.f:
			m = scan_meta(p)
			_.pv(m)
	




def load():
	global meta
	if os.path.isfile('.folder.meta'):
		meta_folders_table('.folder.meta')
		meta = _.getTable2( '.folder.meta' )
	else:
		meta = {}


	v.f = {}
	for path in _.switches.values('Files'):
		if os.path.isfile(path):
			path = __.path(path)
			v.f[path] = 0
		elif os.path.isdir(path):
			path = __.path(path)
			v.f[path] = 1
	for path in _.switches.values('Folders'):
		if os.path.isfile(path):
			path = __.path(path)
			v.f[path] = 0
		elif os.path.isdir(path):
			path = __.path(path)
			v.f[path] = 1
	if _.switches.isActive('Folders') and not len(v.f):
		v.f[ os.getcwd() ] = 1


def meta_folders_table(path):
	path = __.path(path)
	if os.path.isfile(path):
		path = __.path(path,pop=True)
	if _.isWin:
		path = path.lower()
	table = _.getTable('meta-folders.list')
	test=table.copy()
	if not __.path(path) in table:
		table.append( __.path(path) )
	# _.pv( table )
	newTable = []
	for ntf in table:
		if not ntf in newTable:
			newTable.append(ntf)
	table = newTable
	if not str(table)==str(test):
		_.saveTable( table, 'meta-folders.list', p=0 )
		_.cp(['added',path,'to meta database'],'yellow')
	# else:
	#     pass
	#     _.cp('in meta database','yellow')


def template(subject):
	global meta
	if subject == 'url':
		return ''

	ftp = {
			'server':        '',
			'user':            '',
			'password':        '',
			'path':            '',
			'full-path':    '',
	}
	if subject == 'ftp':
		return ftp

	if subject == 'sftp':
		return ftp
	
	if subject == 'client':
		return {
			'company': '',
			'contact': '',
			'email': '',
			'phone': '',
		}

	if subject == 'project' or subject == 'note' or subject == 'info':
		return {
			'description': '',
			'tags': '',
		}
	
	
	return ''


v = _.dot()
v.order = 'url client project note info sftp ftp'.split(' ')



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




