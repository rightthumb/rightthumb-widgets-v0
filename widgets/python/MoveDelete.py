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
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'move.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'changes the path in the backup log (so auto versions are accurate)',
		_.ail(1,'including all meta files')+
		# _.aib('one')+
	'categories': [
						'rename',
						'mv',
						'move',
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
						_.hp('p MoveDelete -src D:\\websites\\domains\\test.file -dst C:\\Users\\Scott\\.rt\\profile\\daily\\2023\\38\\09-23'),
						_.linePrint(label='simple',p=0),
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


def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--#
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();

	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

os=__.os

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
found={}
def aliases(src,dst):
	global _aliases
	global isFoS
	global isFoD
	global found
	found['aliases']=False
	if not 'aliases' in _aliases: return None
	_.pr(line=True,c='purple')
	_.pr('aliases',c='yellow')
	# print(_aliases.keys());sys.exit();
	db=_aliases['aliases']
	for a in db:
		db[a]=db[a].replace(os.sep+os.sep,os.sep)
		if not isFoS and src == db[a]:
			found['aliases']=True
			_.pr('aliases:',a,db[a],c='cyan')
			if isFoD:
				fo=folder(db[a])
				_aliases['aliases'][a]=db[a].replace(fo,dst)
			else:
				_aliases['aliases'][a]=dst
		elif db[a].startswith(src):
			found['aliases']=True
			_.pr('aliases:',a,db[a],c='cyan')
			_aliases['aliases'][a]=db[a].replace(src,dst)
	db=_aliases['files']
	for p in db:
		if not isFoS:
			if p == src:
				found['aliases']=True
				_.pr(p)
				if not isFoD:
					_aliases['files'][p]=src
				else:
					fo=folder(p)
					_aliases['files'][p]=p.replace(fo,dst)

		elif p.startswith(src):
			found['aliases']=True
			_.pr(p,c='cyan')
			_aliases['files'][p]=p.replace(src,dst)




def bookmarks(src,dst):
	global _bookmarks
	global isFoS
	global isFoD
	global found
	found['bookmarks']=False
	if not isFoS: return False
	if not 'labels' in _bookmarks: return False
	# print(_bookmarks.keys());sys.exit();
	_.pr(line=True,c='purple')
	_.pr('bookmarks',c='yellow')
	db=_bookmarks['labels']
	srcS = src[:-1]
	dstS = dst[:-1]
	# sanitizeFolder
	for a in db:
		path=_v.resolveFolderIDs(db[a])
		if path == srcS:
			found['bookmarks']=True
			_bookmarks['labels'][a]=_v.sanitizeFolder(dstS)
			_.pr(a,_bookmarks['labels'][a],c='cyan')
		elif path.startswith(src):
			found['bookmarks']=True
			_bookmarks['labels'][a]=_v.sanitizeFolder(path.replace(src,dst))
			_.pr(a,_bookmarks['labels'][a],c='cyan')
	db={}
	for path in _bookmarks['paths']:
		opath=path
		path=_v.resolveFolderIDs(path)
		if path == srcS:
			path=srcS
			found['bookmarks']=True
			_.pr(path,c='cyan')
		elif path.startswith(src):
			found['bookmarks']=True
			path=path.replace(src,dst)
			_.pr(path,c='cyan')
		path=_v.sanitizeFolder(path)
		db[path]=_bookmarks['paths'][opath]
	_bookmarks['paths']=db

def sites(src,dst):
	global _sites
	global isFoS
	global isFoD
	global found
	found['sites']=False
	if not isFoS: return False
	_.pr(line=True,c='purple')
	_.pr('sites',c='yellow')
	for i,path in enumerate(_sites):
		if path.startswith(src):
			_sites[i] = path.replace(src,dst)
			_.pr(_sites[i],c='cyan')



def crypt_meta(src,dst):
	global _crypt_meta
	global isFoS
	global isFoD
	global found
	found['crypt_meta']=False
	_.pr(line=True,c='purple')
	_.pr('crypt_meta',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_meta:
		opath=path
		if src in path:
			found['crypt_meta']=True
			path=path.replace(src,dst)
			_.pr(path,c='cyan')
		db[path]=_crypt_meta[opath]
	_crypt_meta=db

def crypt_settings(src,dst):
	global _crypt_settings
	global isFoS
	global isFoD
	global found
	found['crypt_settings']=False
	_.pr(line=True,c='purple')
	_.pr('crypt_settings',c='yellow')
	# print(_crypt_meta.keys())
	db={}
	for path in _crypt_settings:
		opath=path
		if src in path:
			found['crypt_meta']=True
			path=path.replace(src,dst)
			_.pr(path,c='cyan')
		db[path]=_crypt_settings[opath]
	_crypt_settings=db


def book_log(src,dst):
	global _book_log
	global isFoS
	global isFoD
	global found
	found['book_log']=False
	if not isFoS: return False
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('book_log',c='yellow')
	cnt=0
	for bm in _book_log:
		for i,rec in enumerate(_book_log[bm]):
			path=_v.resolveFolderIDs(rec['location'])
			if path == srcS:
				cnt+=1
				path=dst
				found['book_log']=True
				# _.pr(path,c='cyan')
			elif path.startswith(src):
				cnt+=1
				found['book_log']=True
				path=path.replace(src,dst)
				# _.pr(path,c='cyan')
			_book_log[bm][i]['location']=_v.sanitizeFolder(path)
	_.pr(cnt,c='cyan')

def fileBackup(src,dst):
	global _fileBackup
	global isFoS
	global isFoD
	global found
	found['fileBackup']=False
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('fileBackup',c='yellow')
	cnt=0
	for i,rec in enumerate(_fileBackup):
		path=rec['file']
		if path.startswith(src):
			cnt+=1
			found['fileBackup']=True
			path=path.replace(src,dst)
			# _.pr(path,c='cyan')
		_fileBackup[i]['file']=path
	_.pr(cnt,c='cyan')

def action():
	load()
	global isFoS
	global isFoD
	global found
	src = __.path(_.switches.values('Source')[0])
	if _.switches.isActive('Destination'):
		dst = _.switches.values('Destination')[0]
	else:
		dst = None
	if dst is None and not _.switches.isActive('Delete'):
		dst = os.getcwd()
	src=__.path(src)
	dst=__.path(dst)
	isFoS = os.path.isdir(src)
	isFoD = os.path.isdir(dst)
	if isFoS and not src.endswith(os.sep): src+=os.sep
	if isFoS and not dst.endswith(os.sep): dst+=os.sep
	if isFoD and not dst.endswith(os.sep): dst+=os.sep
	if isFoS and isFoD: dst=dst+src.split(os.sep)[-2]+os.sep
	if os.path.isfile(src) and isFoD: dst=dst+src.split(os.sep)[-1]
	if isFoS and not isFoD:
		if not os.path.isdir(dst):
			_v.mkdir(dst)
			dst=__.path(dst)
			os.rmdir(dst)
	src=src.replace(os.sep+os.sep,os.sep)
	dst=dst.replace(os.sep+os.sep,os.sep)
	if isFoS and os.path.isfile(dst): _.e('Error: dst','if src is folder dst can not be a file')
	if not isFoD: _v.mkdir(dst)
	if src == dst: _.e('unable to move','same location')
	# if not 'y' in input('Move: '+src+'\n  To: '+dst+'\n ?: ').lower(): return None
	aliases(src,dst)
	bookmarks(src,dst)
	sites(src,dst)
	crypt_meta(src,dst)
	crypt_settings(src,dst)
	book_log(src,dst)
	fileBackup(src,dst)

	if found['aliases']: _.saveTable(_aliases,'file-open-aliases.hash')
	if found['bookmarks']: _.saveTable(_bookmarks,'bookmarks.index')
	if found['sites']: _.saveTable(_sites,'site-locations.list')
	if found['crypt_meta']: _.saveTable(_crypt_meta,'secure-crypt-local.meta')
	if found['crypt_settings']: _.saveTable(_crypt_settings,'secure-crypt-local.settings')
	if found['book_log']: _.saveTable(_book_log,'bookmarks.logs')
	if found['fileBackup']: _.saveTable(_fileBackup,'fileBackup.json')
	shutil.move(src, dst)








def load():
	global _sites
	global _aliases
	global _book_log
	global _bookmarks
	global _crypt_meta
	global _fileBackup
	global _crypt_settings

	_sites          = _.getTable('site-locations.list')
	_aliases        = _.getTable('file-open-aliases.hash')
	_book_log       = _.getTable('bookmarks.logs')
	_bookmarks      = _.getTable('bookmarks.index')
	_crypt_meta     = _.getTable('secure-crypt-local.meta')
	_fileBackup     = _.getTable('fileBackup.json')
	_crypt_settings = _.getTable('secure-crypt-local.settings')




	# folder-registration
	# C:\Users\Scott\.rt\profile\tables\fo

import shutil
import os

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


 
