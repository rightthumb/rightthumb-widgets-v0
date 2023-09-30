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
	global change
	global delete
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
			if delete: continue
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
			if not delete:
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
	global delete
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
			if not delete:
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
		if fnd and delete: continue
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
			if not delete:
				db.append(__.path(path.replace(src,dst)))
			_.pr(_sites[i],c='cyan')
		elif os.path.isfile(path):
			db.append(path)
		else:
			change['sites']+=1
	_sites=db





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
			if _.switches.isActive('Ghost'):
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and delete: continue
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
			found['crypt_meta']+=1
			if _.switches.isActive('Ghost'):
				backup(path,True)
			else:
				backup(path)
			path=__.path(path.replace(src,dst))
			_.pr(path,c='cyan')
		if fnd and delete: continue
		elif not os.path.isfile(opath):
			change['crypt_settings']+=1
			continue
		db[path]=_crypt_settings[opath]
	_crypt_settings=db


def book_log(src,dst):
	global _book_log
	global isFoS
	global isFoD
	global found
	found['book_log']=0
	if not isFoS: return False
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('book_log',c='yellow')
	for bm in _book_log:
		for i,rec in enumerate(_book_log[bm]):
			path=__.path(_v.resolveFolderIDs(rec['location']))
			if path == srcS:
				path=dst
				found['book_log']+=1
				# _.pr(path,c='cyan')
			elif path.startswith(src):
				cnt+=1
				found['book_log']+=1
				path=path.replace(src,dst)
				# _.pr(path,c='cyan')
			_book_log[bm][i]['location']=__.path(_v.sanitizeFolder(path))
	_.pr(found['book_log'],c='cyan')

def fileBackup(src,dst):
	global _fileBackup
	global isFoS
	global isFoD
	global found
	_fileBackup = _.getTable('fileBackup.json')
	found['fileBackup']=0
	srcS = src[:-1]
	dstS = dst[:-1]
	_.pr(line=True,c='purple')
	_.pr('fileBackup',c='yellow')
	for i,rec in enumerate(_fileBackup):
		path=__.path(rec['file'])
		if path.startswith(src):
			found['fileBackup']+=1
			path=path.replace(src,dst)
			# _.pr(path,c='cyan')
		_fileBackup[i]['file']=__.path(path)
	_.pr(found['fileBackup'],c='cyan')

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
			if not delete:
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

def action():
	load()
	global isFoS
	global isFoD
	global found
	global change
	global delete
	global _bk
	global _sites
	global _aliases
	global _book_log
	global _bookmarks
	global _MoveDelete
	global _crypt_meta
	global _fileBackup
	global _crypt_settings
	global _backup_schedule
	found={}
	change={}
	if len(_.switches.values('Source')) > 1: _.e('Multiple Sources Detected','Please specify only 1 Source')
	delete = _.switches.isActive('Delete')
	if _.switches.isActive('Ghost'):
		delete = True
	src = __.path(_.switches.values('Source')[0])
	if _.switches.isActive('Destination'):
		dst = _.switches.values('Destination')[0]
	else:
		dst = None
	if dst is None:
		dst = os.getcwd()
	src=__.path(src)
	dst=__.path(dst)
	isFoS = os.path.isdir(src)
	isFoD = os.path.isdir(dst)
	if isFoS and not src.endswith(os.sep): src+=os.sep
	if isFoS and not dst.endswith(os.sep): dst+=os.sep
	if isFoD and not dst.endswith(os.sep): dst+=os.sep
	if not 'force' in _.switches.value('Destination'):
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
	if not delete and src == dst: _.e('unable to move','same location')

	if not delete:

		if not 'y' in input('Move: '+src+'\n  To: '+dst+'\n ?: ').lower(): return None
	elif delete:
		if not 'y' in input('Delete: '+src+'?: ').lower(): return None
	aliases(src,dst)
	bookmarks(src,dst)
	sites(src,dst)
	crypt_meta(src,dst)
	crypt_settings(src,dst)
	backup_schedule(src,dst)
	if not delete:
		book_log(src,dst)
		fileBackup(src,dst)

	# def aliases
	# def bookmarks
	# def sites
	# def crypt_meta
	# def crypt_settings






	if found['sites'] or change['sites']:                        _.saveTable(_sites,'site-locations.list')
	if found['aliases'] or change['aliases']:                    _.saveTable(_aliases,'file-open-aliases.hash')
	if found['bookmarks'] or change['bookmarks']:                _.saveTable(_bookmarks,'bookmarks.index')
	if found['crypt_meta'] or change['crypt_meta']:              _.saveTable(_crypt_meta,'secure-crypt-local.meta')
	if found['crypt_settings'] or change['crypt_settings']:      _.saveTable(_crypt_settings,'secure-crypt-local.settings')
	if found['backup_schedule'] or change['backup_schedule']:    _.saveTable(_backup_schedule,'fileBackupSchedule.json')
	if not delete:
		if found['book_log']:     _.saveTable(_book_log,'bookmarks.logs')
		if found['fileBackup']:   _.saveTable(_fileBackup,'fileBackup.json')
	fnd=False
	for f in found:
		if found[f]: fnd=True
	if delete: did='delete'
	else: did='move'
	if _.switches.isActive('Ghost'): did='ghost'
	inlogs={}
	for k in found:
		if found[k]: inlogs[k]=found[k]
	if delete:
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
		dst=_v.myBIN+os.sep+'deleted'+os.sep+str(__.startTime)+'-'+item+'.zip'
	rec = {
				'epoch': __.startTime,
				'type': did,
				'source': src,
				'destination': dst,
				'inlogs': inlogs,
	}
	_MoveDelete.append(rec)
	_.saveTable(_MoveDelete,'MoveDelete.json')
	_.pv(found)

	if not _.switches.isActive('Ghost') and _.switches.isActive('Backup') and delete:
		import _rightThumb._zipper as _zipper
		_zipper.zip(src,dst)
		shutil.rmtree(src)
	else:
		shutil.move(src, dst)









def load():
	global _sites
	global _aliases
	global _book_log
	global _bookmarks
	global _MoveDelete
	global _crypt_meta
	global _fileBackup
	global _crypt_settings
	global _backup_schedule

	_sites          = _.getTable('site-locations.list')
	_aliases        = _.getTable('file-open-aliases.hash')
	_book_log       = _.getTable('bookmarks.logs')
	_bookmarks      = _.getTable('bookmarks.index')
	_MoveDelete     = _.getTable('MoveDelete.json')
	_crypt_meta     = _.getTable('secure-crypt-local.meta')
	_crypt_settings = _.getTable('secure-crypt-local.settings')
	_backup_schedule = _.getTable('fileBackupSchedule.json')




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


 
