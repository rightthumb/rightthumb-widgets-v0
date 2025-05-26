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
import sys, time
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
	_.switches.register( 'Source', '-src,-from,-f,-file','file.txt', isRequired=True )
	_.switches.register( 'Destination', '-dst,-to','file2.txt', isRequired=False )
	_.switches.register( 'Delete', '-del,-delete', isRequired=False )
	_.switches.register( 'Backup', '-bk,-backup', isRequired=False )
	_.switches.register( 'Ghost', '-ghost', isRequired=False )
	_.switches.register( 'Yes', '-y,-yes', isRequired=False )


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
#n)--> start


found={}
def file(path):
	return path.split(os.sep)[-1]
def folder(path):
	parts=path.split(os.sep)
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	fo=os.sep.join(parts)+os.sep
	# fo=fo.replace(os.sep+os.sep,os.sep)
	return fo
def aliases(src,dst):
	global _aliases
	global isFoS
	global isFoD
	global found
	global change
	
	found['aliases']=0
	change['aliases']=0
	if not 'aliases' in _aliases: return None
	_.pr(line=True,c='purple')
	_.pr('aliases',c='yellow')
	# print(_aliases.keys());sys.exit();
	db={}
	for a in _aliases['aliases']:
		path=_aliases['aliases'][a]
		fnd=False
		path=__.path(path.replace(os.sep+os.sep,os.sep))
		if not isFoS and src == path:
			fnd=True
			found['aliases']+=1
			path=dst
		elif path.startswith(src):
			fnd=True
			found['aliases']+=1
			path=__.path(path.replace(src,dst))
		if fnd:
			_.pr('aliases:',a,path,c='cyan')
			if __.v.Delete: continue
		elif not os.path.isfile(path):
			change['aliases']+=1
			continue
		db[a]=path
	_aliases['aliases']=db
	db={}
	for path in _aliases['files']:
		opath=path
		path=__.path(path)
		fnd=False
		if not isFoS:
			if path == src:
				fnd=True
				found['aliases']+=1
				path=dst
		elif path.startswith(src):
			fnd=True
			found['aliases']+=1
			path=__.path(path.replace(src,dst))
		if fnd:
			_.pr(path,c='cyan')
			if not __.v.Delete:
				db[path]=_aliases['files'][opath]
		elif os.path.isfile(path):
			db[path]=_aliases['files'][opath]
		else:
			change['aliases']+=1
	_aliases['files']=db




def bookmarks(src,dst):
	global _bookmarks
	global isFoS
	global isFoD
	global found
	global change
	
	found['bookmarks']=0
	change['bookmarks']=0
	if not isFoS: return False
	if not 'labels' in _bookmarks: return False
	# print(_bookmarks.keys());sys.exit();
	_.pr(line=True,c='purple')
	_.pr('bookmarks',c='yellow')
	db={}
	srcS = src[:-1]
	dstS = dst[:-1]
	# sanitizeFolder
	for a in _bookmarks['labels']:
		fnd=False
		path=__.path(_v.resolveFolderIDs(_bookmarks['labels'][a]))
		if path == srcS:
			fnd=True
			found['bookmarks']+=1
			path=_v.sanitizeFolder(__.path(dstS))
		elif path.startswith(src):
			fnd=True
			found['bookmarks']+=1
			path=_v.sanitizeFolder(__.path(path.replace(src,dst)))
		if fnd:
			if not __.v.Delete:
				db[a]=path
			_.pr(a,_v.resolveFolderIDs(path),c='cyan')
		elif os.path.isdir(path):
			db[a]=path
		else:
			change['bookmarks']+=1
	_bookmarks['labels']=db
	db={}
	for path in _bookmarks['paths']:
		fnd=False
		opath=path
		path=__.path(_v.resolveFolderIDs(path))
		if path == srcS:
			fnd=True
			found['bookmarks']+=1
			path=srcS
		elif path.startswith(src):
			fnd=True
			found['bookmarks']+=1
			path=path.replace(src,dst)
		path=__.path(_v.sanitizeFolder(path))
		if fnd:
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isdir(path):
			change['bookmarks']+=1
			continue
		db[path]=_bookmarks['paths'][opath]
	_bookmarks['paths']=db

def sites(src,dst):
	global _sites
	global isFoS
	global isFoD
	global found
	global change
	found['sites']=0
	change['sites']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('sites',c='yellow')
	db=[]
	for i,path in enumerate(_sites):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['sites']+=1
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_sites[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['sites']+=1
	_sites=db


def meta_folders(src,dst):
	global _meta_folders
	global isFoS
	global isFoD
	global found
	global change
	found['meta_folders']=0
	change['meta_folders']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('meta_folders',c='yellow')
	db=[]
	for i,path in enumerate(_meta_folders):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['meta_folders']+=1
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_meta_folders[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['meta_folders']+=1
	_meta_folders=db


def relevant_folders(src,dst):
	global _relevant_folders
	global isFoS
	global isFoD
	global found
	global change
	found['relevant_folders']=0
	change['relevant_folders']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('relevant_folders',c='yellow')
	db=[]
	for i,path in enumerate(_relevant_folders):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['relevant_folders']+=1
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_relevant_folders[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['relevant_folders']+=1
	_relevant_folders=db


def webdav(src,dst):
	global _webdav
	global isFoS
	global isFoD
	global found
	global change
	found['webdav']=0
	change['webdav']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('webdav',c='yellow')
	db=[]
	for i,path in enumerate(_webdav):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['webdav']+=1
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_webdav[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['webdav']+=1
	_webdav=db


def rename_space(src,dst):
	global _rename_space
	global isFoS
	global isFoD
	global found
	global change
	found['rename_space']=0
	change['rename_space']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('rename_space',c='yellow')
	db=[]
	for i,path in enumerate(_rename_space):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['rename_space']+=1
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_rename_space[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['rename_space']+=1
	_rename_space=db


def crypt_docs(src,dst):
	global _crypt_docs
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_docs']=0
	change['crypt_docs']=0
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('crypt_docs',c='yellow')
	db=[]
	for i,path in enumerate(_crypt_docs):
		path=__.path(path)
		fnd=False
		if path.startswith(src):
			fnd=True
			found['crypt_docs']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			if not __.v.Delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_crypt_docs[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['crypt_docs']+=1
	_crypt_docs=db

def crypt_meta(src,dst):
	global _crypt_meta
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_meta']=0
	change['crypt_meta']=0
	_.pr(line=True,c='purple')
	_.pr('crypt_meta',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_meta:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['crypt_meta']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['crypt_meta']+=1
			continue
		db[path]=_crypt_meta[opath]
	_crypt_meta=db

def crypt_settings(src,dst):
	global _crypt_settings
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_settings']=0
	change['crypt_settings']=0
	_.pr(line=True,c='purple')
	_.pr('crypt_settings',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_settings:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['crypt_settings']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['crypt_settings']+=1
			continue
		db[path]=_crypt_settings[opath]
	_crypt_settings=db


def crypt_secure(src,dst):
	global _crypt_secure
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_secure']=0
	change['crypt_secure']=0
	_.pr(line=True,c='purple')
	_.pr('crypt_secure',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_secure:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['crypt_secure']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['crypt_secure']+=1
			continue
		db[path]=_crypt_secure[opath]
	_crypt_secure=db

def crypt_secure_settings(src,dst):
	global _crypt_secure_settings
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_secure_settings']=0
	change['crypt_secure_settings']=0
	_.pr(line=True,c='purple')
	_.pr('crypt_secure_settings',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_secure_settings:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['crypt_secure_settings']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['crypt_secure_settings']+=1
			continue
		db[path]=_crypt_secure_settings[opath]
	_crypt_secure_settings=db

def crypt_secure_file_local_settings(src,dst):
	global _crypt_secure_file_local_settings
	global isFoS
	global isFoD
	global found
	global change
	found['crypt_secure_file_local_settings']=0
	change['crypt_secure_file_local_settings']=0
	_.pr(line=True,c='purple')
	_.pr('crypt_secure_file_local_settings',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_secure_file_local_settings:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['crypt_secure_file_local_settings']+=1
			if __.v.Ghost:
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['crypt_secure_file_local_settings']+=1
			continue
		db[path]=_crypt_secure_file_local_settings[opath]
	_crypt_secure_file_local_settings=db


def touchi(src,dst):
	global _touchi
	global isFoS
	global isFoD
	global found
	global change
	found['touchi']=0
	change['touchi']=0
	_.pr(line=True,c='purple')
	_.pr('touchi',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _touchi:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['touchi']+=1
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['touchi']+=1
			continue
		db[path]=_touchi[opath]
	_touchi=db



def touchm(src,dst):
	global _touchm
	global isFoS
	global isFoD
	global found
	global change
	found['touchm']=0
	change['touchm']=0
	_.pr(line=True,c='purple')
	_.pr('touchm',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _touchm:
		opath=path
		path=__.path(path)
		fnd=False
		if src in path:
			fnd=True
			found['touchm']+=1
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and __.v.Delete: continue
		elif not os.path.isfile(opath):
			change['touchm']+=1
			continue
		db[path]=_touchm[opath]
	_touchm=db



def book_log(src,dst):
	global _book_log
	global isFoS
	global isFoD
	global found
	global change
	found['book_log']=0
	change['book_log']=0
	if not isFoS: return False
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('book_log',c='yellow')
	if __.v.Delete: rm={}
	for bm in _book_log:
		for i,rec in enumerate(_book_log[bm]):
			path=__.path(_v.resolveFolderIDs(rec['location']))
			if path == srcS:
				path=dst
				found['book_log']+=1
				if __.v.Delete:
					if not bm in rm: rm[bm]=[]
					rm[bm].append(i)
				# _.pr(path,c='cyan')
			elif path.startswith(src):
				if __.v.Delete:
					if not bm in rm: rm[bm]=[]
					rm[bm].append(i)
				found['book_log']+=1
				path=path.replace(src,dst)
				# _.pr(path,c='cyan')
			_book_log[bm][i]['location']=__.path(_v.sanitizeFolder(path))
	_.pr(found['book_log'],c='cyan')
	if __.v.Delete:
		for bm in rm:
			rm[bm].reverse()
			for i in rm[bm]:
				change['book_log']+=1
				del _book_log[bm][i]
def fileBackup(src,dst):
	global _fileBackup
	global isFoS
	global isFoD
	global found
	global change
	_fileBackup = _.getTable('fileBackup.json')
	found['fileBackup']=0
	change['fileBackup']=0
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('fileBackup',c='yellow')
	if __.v.Delete: rm=[]
	for i,rec in enumerate(_fileBackup):
		path=__.path(rec['file'])
		if path.startswith(src):
			if __.v.Delete: rm.append(i)
			found['fileBackup']+=1
			path=path.replace(src,dst)
			# _.pr(path,c='cyan')
		_fileBackup[i]['file']=__.path(path)
	_.pr(found['fileBackup'],c='cyan')
	if __.v.Delete:
		rm.reverse()
		for i in rm:
			change['fileBackup']+=1
			del _fileBackup[i]

def backup_schedule(src,dst):
	global _backup_schedule
	global isFoS
	global isFoD
	global found
	global change
	found['backup_schedule']=0
	change['backup_schedule']=0
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('backup_schedule',c='yellow')
	db=[]
	for i,rec in enumerate(_backup_schedule):
		fnd=False
		path=__.path(rec['file'])
		if path.startswith(src):
			fnd=True
			found['backup_schedule']+=1
			path=path.replace(src,dst)
		if fnd:
			if not __.v.Delete:
				rec['file']=__.path(path)
				db.append(rec)
		elif os.path.isfile(path):
			db.append(rec)
		else:
			change['backup_schedule']+=1
	_backup_schedule=db
	_.pr(found['backup_schedule'],c='cyan')

def backup(path,decrypt=False):
	appReg=__.appReg
	_bk = _.regImp( __.appReg, 'fileBackup' )
	# _bk.switch( 'Silent' )
	if decrypt:
		_bk.switch( 'isPreOpen' )
	_bk.switch( 'Input', path )
	bkfi = _bk.action()
	del _bk
	__.appReg=appReg

def changeFound():
	global found
	global change
	found['aliases']=0
	found['bookmarks']=0
	found['sites']=0
	found['meta_folders']=0
	found['relevant_folders']=0
	found['webdav']=0
	found['rename_space']=0
	found['crypt_docs']=0
	found['crypt_meta']=0
	found['crypt_settings']=0
	found['crypt_secure']=0
	found['crypt_secure_settings']=0
	found['crypt_secure_file_local_settings']=0
	found['touchi']=0
	found['touchm']=0
	found['book_log']=0
	found['fileBackup']=0
	found['backup_schedule']=0

	change['aliases']=0
	change['bookmarks']=0
	change['sites']=0
	change['meta_folders']=0
	change['relevant_folders']=0
	change['webdav']=0
	change['rename_space']=0
	change['crypt_docs']=0
	change['crypt_meta']=0
	change['crypt_settings']=0
	change['crypt_secure']=0
	change['crypt_secure_settings']=0
	change['crypt_secure_file_local_settings']=0
	change['touchi']=0
	change['touchm']=0
	change['book_log']=0
	change['fileBackup']=0
	change['backup_schedule']=0

def ifHas(dic):
	d={}
	for k in dic:
		if dic[k]: d[k]=dic[k]
	return d

def run(s,d=None):
	global src
	global dst
	global isFoS
	global isFoD
	global found
	global change
	src=s
	dst=d
	if dst is None: __.v.Delete = True
	if __.v.Ghost: __.v.Delete = True

	found={}
	change={}

	if dst is None: dst = os.getcwd()
	src=__.path(src)
	dst=__.path(dst)
	isFoS = os.path.isdir(src)
	isFoD = os.path.isdir(dst)
	if isFoS and not src.endswith(os.sep): src+=os.sep
	if isFoS and not dst.endswith(os.sep): dst+=os.sep
	if isFoD and not dst.endswith(os.sep): dst+=os.sep
	if not __.v.Force:
		if isFoS and isFoD: dst=dst+src.split(os.sep)[-2]+os.sep
	if os.path.isfile(src) and isFoD: dst=dst+src.split(os.sep)[-1]
	if isFoS and not isFoD:
		if not os.path.isdir(dst):
			_v.mkdir(dst)
			dst=__.path(dst)
			os.rmdir(dst)
	src=__.path(src.replace(os.sep+os.sep,os.sep))
	dst=__.path(dst.replace(os.sep+os.sep,os.sep))
	if isFoS and os.path.isfile(dst): _.e('Error: dst','if src is folder dst can not be a file')
	if not isFoD: _v.mkdir(dst)
	if not __.v.Delete and src == dst: _.e('unable to move','same location')
	if not __.v.Yes:
		if not __.v.Delete:
			if not 'y' in input('Move: '+src+'\n  To: '+dst+'\n ?: ').lower(): _.e('Move','Exit Activated')
		elif __.v.Delete:
			if __.v.Ghost:
				if _.lis('a all', __.v.Ghostbusters ):        ghost = ' '+'all'
				elif _.lis('backup bk', __.v.Ghostbusters ):  ghost = ' '+'backup'
				elif _.lis('l log logs', __.v.Ghostbusters ): ghost = ' '+'logs'

				if not 'y' in input('Ghost'+ghost+': '+src+'?: ').lower(): _.e('Ghost','Exit Activated')
			else:
				if not 'y' in input('Delete: '+src+'?: ').lower(): _.e('Delete','Exit Activated')
	changeFound()
	aliases(src,dst)
	bookmarks(src,dst)
	sites(src,dst)
	crypt_meta(src,dst)
	crypt_settings(src,dst)
	backup_schedule(src,dst)
	touchi(src,dst)
	touchm(src,dst)
	crypt_secure(src,dst)
	crypt_secure_settings(src,dst)
	crypt_secure_file_local_settings(src,dst)
	rename_space(src,dst)
	crypt_docs(src,dst)
	relevant_folders(src,dst)
	meta_folders(src,dst)
	webdav(src,dst)

	if not __.v.Delete:
		book_log(src,dst)
		fileBackup(src,dst)
	else:
		if _.lis('a all', __.v.Ghostbusters ):
			book_log(src,dst)
			fileBackup(src,dst)
		elif _.lis('backup bk', __.v.Ghostbusters ):
			fileBackup(src,dst)
		elif _.lis('l log logs', __.v.Ghostbusters ):
			book_log(src,dst)




def save():
	global src
	global dst
	global isFoS
	global isFoD
	global found
	global change
	global _sites
	global _webdav
	global _touchi
	global _touchm
	global _aliases
	global _book_log
	global _bookmarks
	global _MoveDelete
	global _crypt_meta
	global _fileBackup
	global _crypt_docs
	global _crypt_secure
	global _rename_space
	global _meta_folders
	global _crypt_settings
	global _backup_schedule
	global _relevant_folders
	global _crypt_secure_settings
	global _crypt_secure_file_local_settings

	# nth if found['{0}'] or change['{0}']: _.saveTable(_{0},'{1}')

	if found['sites'] or change['sites']:                                                         _.saveTable(_sites,'site-locations.list')
	if found['webdav'] or change['webdav']:                                                       _.saveTable(_webdav,'webdav-locations.list')
	if found["touchi"] or change["touchi"]:                                                       _.saveTable(_touchi,"touch.index")
	if found["touchm"] or change["touchm"]:                                                       _.saveTable(_touchm,"touch.meta")
	if found['aliases'] or change['aliases']:                                                     _.saveTable(_aliases,'file-open-aliases.hash')
	if found['bookmarks'] or change['bookmarks']:                                                 _.saveTable(_bookmarks,'bookmarks.index')
	if found["crypt_docs"] or change["crypt_docs"]:                                               _.saveTable(_crypt_docs,"crypt-docs.list")
	if found['crypt_meta'] or change['crypt_meta']:                                               _.saveTable(_crypt_meta,'secure-crypt-local.meta')
	if found["rename_space"] or change["rename_space"]:                                           _.saveTable(_rename_space,"renameSpace-undo.dex")
	if found["meta_folders"] or change["meta_folders"]:                                           _.saveTable(_meta_folders,"meta-folders.list")
	if found["crypt_secure"] or change["crypt_secure"]:                                           _.saveTable(_crypt_secure,"secure-crypt.meta")
	if found['crypt_settings'] or change['crypt_settings']:                                       _.saveTable(_crypt_settings,'secure-crypt-local.settings')
	if found['backup_schedule'] or change['backup_schedule']:                                     _.saveTable(_backup_schedule,'fileBackupSchedule.json')
	if found["relevant_folders"] or change["relevant_folders"]:                                   _.saveText(_relevant_folders,_v.tt+os.sep+'relevantFolders.txt')
	if found["crypt_secure_settings"] or change["crypt_secure_settings"]:                         _.saveTable(_crypt_secure_settings,"secure-crypt.settings")
	if found["crypt_secure_file_local_settings"] or change["crypt_secure_file_local_settings"]:   _.saveTable(_crypt_secure_file_local_settings,"secure-files-local.settings")
	if found['book_log'] or change['book_log']:                                                   _.saveTable(_book_log,'bookmarks.logs')
	if found['fileBackup'] or change['fileBackup']:                                               _.saveTable(_fileBackup,'fileBackup.json')
	fnd=False
	for f in found:
		if found[f]: fnd=True
	if __.v.Delete: did='__.v.Delete'
	else: did='move'
	if __.v.Ghost: did='ghost'
	inlogs={}
	for k in found:
		if found[k]: inlogs[k]=found[k]
	if __.v.Delete:
		if isFoS: am='fo'
		else:  am='fi'
		try:
			try:
				item=src.split(os.sep)[-3]+'__'+src.split(os.sep)[-2]+'__'+src.split(os.sep)[-1]
			except Exception as e:
				item=src.split(os.sep)[-2]+'__'+src.split(os.sep)[-1]
		except Exception as e:
			item=src.split(os.sep)[-1]
		item+='-'+am
		dst=_v.myBIN+os.sep+'__.v.Deleted'+os.sep+str(__.startTime)+'-'+item+'.zip'
	rec = {
				'epoch': __.startTime,
				'type': did,
				'source': src,
				'destination': dst,
				'inlogs': inlogs,
	}
	_MoveDelete.append(rec)
	_.saveTable(_MoveDelete,'MoveDelete.json')
	fnd=ifHas(found)
	cng=ifHas(change)
	if fnd:
		_.pr('\nFound:',c='yellow')
		_.pv(_.dicSort(fnd))
	if cng:
		_.pr('\nChange:',c='yellow')
		_.pv(_.dicSort(cng))

	if not __.v.Ghost and __.v.Backup and __.v.Delete:
		if not __.v.Ghost:
			print('Ghost:',__.v.Ghost)
			import _rightThumb._zipper as _zipper
			_zipper.zip(src,dst)
			shutil.rmtree(src)
	elif not __.v.Delete:
		shutil.move(src, dst)



__.v.Yes = False
__.v.Backup = False
__.v.Force = False
__.v.Ghost = False
__.v.Delete = False
__.v.Ghostbusters = ''



def load():
	global _sites
	global _webdav
	global _touchi
	global _touchm
	global _aliases
	global _book_log
	global _bookmarks
	global _MoveDelete
	global _crypt_meta
	global _fileBackup
	global _crypt_docs
	global _crypt_secure
	global _rename_space
	global _meta_folders
	global _crypt_settings
	global _backup_schedule
	global _relevant_folders
	global _crypt_secure_settings
	global _crypt_secure_file_local_settings

	_sites                             = _.getTable('site-locations.list')
	_touchi                            = _.getTable('touch.index')
	_touchm                            = _.getTable('touch.meta')
	_webdav                            = _.getTable('webdav-locations.list')
	_aliases                           = _.getTable('file-open-aliases.hash')
	_book_log                          = _.getTable('bookmarks.logs')
	_bookmarks                         = _.getTable('bookmarks.index')
	_crypt_docs                        = _.getTable('crypt-docs.list')
	_MoveDelete                        = _.getTable('MoveDelete.json')
	_crypt_meta                        = _.getTable('secure-crypt-local.meta')
	_meta_folders                      = _.getTable('meta-folders.list')
	_rename_space                      = _.getTable('renameSpace-undo.dex')
	_crypt_secure                      = _.getTable('secure-crypt.meta')
	_crypt_settings                    = _.getTable('secure-crypt-local.settings')
	_backup_schedule                   = _.getTable('fileBackupSchedule.json')
	_relevant_folders                  = _.getText(_v.tt+os.sep+'relevantFolders.txt')
	_crypt_secure_settings             = _.getTable('secure-crypt.settings')
	_crypt_secure_file_local_settings  = _.getTable('secure-files-local.settings')


	# nth _{0}  = _.getTable('{1}')


	# secure-nosync-local.settings
	# cloud.delete.json
	# cloud_sync.index
	# cloud_sync_files_cache.json
	# folderSizeTotals.index


	# folder-registration
	# C:\Users\Scott\.rt\profile\tables\fo

import shutil
import os

def action():
	__.v.Yes = _.switches.isActive('Yes')
	__.v.Backup = _.switches.isActive('Backup')
	__.v.Ghost = _.switches.isActive('Ghost')
	__.v.Ghostbusters = str('|'+'|'.join(_.switches.values('Ghost'))+'|').lower().replace(' ','')
	__.v.Delete = _.switches.isActive('Delete')
	__.v.Force = False
	if _.switches.isActive('Destination') and len(_.switches.values('Destination')) > 1 and 'force' in _.switches.values('Destination')[1]:
		__.v.Force = True
	load()
	if len(_.switches.values('Source')) > 1: _.e('Multiple Sources Detected','Please specify only 1 Source')
	delete = _.switches.isActive('Delete')
	src = __.path(_.switches.values('Source')[0])
	if _.switches.isActive('Destination'):
		dst = _.switches.values('Destination')[0]
	else:
		dst = None
	# print(__.v.Ghost); sys.exit();
	run(src,dst)
	save()

########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)

