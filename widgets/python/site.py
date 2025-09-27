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
	_.switches.register( 'Upload-Scp', '-u,-up,-upload' )
	_.switches.register( 'Download-Scp', '-d,-dl,-down,-download' )
	_.switches.register( 'rsync', '-rsync' )
	_.switches.register( 'Test', '-t,-test' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt',  description='glob', isRequired=True )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData="name", isRequired=False )
	_.switches.register( 'InBrowser', '-b,-browser,-inbrowser' )

	_.switches.register( 'mkdir', '-mkdir' )
	_.switches.register( 'Servers', '-srv,-server,-vps', 'hoth bespin h b' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'Status', '-status' )
	_.switches.register( 'NotWSL', '-notwsl' )
	_.switches.register( 'Verbose', '-v' )
	_.switches.register( 'SSH-Remote_Folder', '-remote' )
	_.switches.register( 'URL', '-url,-edit,--u' )
	_.switches.register( 'Print-Remote-Location', '-where' )
	_.switches.register( 'Remote-Location', '-rp,-rpath' )
	_.switches.register( 'CMD', '-cmd' )
	_.switches.register( 'NoPassword', '-nopass' )
	_.switches.register( 'Toggle-Url/.folder.meta', '-tu,-turl' )
	_.switches.register( 'Find.folder.meta', '-meta' )
	# _.switches.register( 'IsFile', '-isfi' )


# __.setting('omit-switch-triggers',['Files'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])


_.appInfo[focus()] = {
	'file': 'site.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage website files and open in url based on parentfolder meta',
	'categories': [
						'meta',
						'site',
						'test',
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
						_.hp('p site -f default.js -test'),
						_.hp('p site -f default.js -up'),
						_.hp('p site -f default.js -dl'),
						'',
						_.hp('u. file.txt -srv b h m t'),
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

file_trigger_data=None
def file_trigger(data):
	global file_trigger_data
	data=_.myFileLocations(data)
	# _.pr(data)
	# _.pr(data)
	if type(data) == list:
		file_trigger_data=data
		# _.switches.fieldSet( 'Files', 'values', data )
		# _.switches.fieldSet( 'Files', 'value', data[0] )
		# data = data[0]
	elif not os.path.isfile(data) and not os.path.isdir(data):
		__.trigger_isPipe='glob'
		data=_.myFileLocations(data)
	return data

def triggers():
	_.switches.trigger( 'Files', file_trigger )
	# _.switches.trigger( 'Files', _.myFileLocations )


_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
if type(file_trigger_data) == list:
	_.switches.fieldSet( 'Files', 'values', file_trigger_data )
	_.switches.fieldSet( 'Files', 'value', ','.join(file_trigger_data) )
	_.setPipeData(file_trigger_data)

########################################################################################
# START


import os
import sys

def find_meta_file(filename='.folder.meta'):
    current_dir = os.path.abspath(os.getcwd())
    
    while True:
        candidate = os.path.join(current_dir, filename)
        if os.path.isfile(candidate):
            print(candidate)
            return
        parent_dir = os.path.dirname(current_dir)
        if current_dir == parent_dir:
            # Reached the root
            break
        current_dir = parent_dir
    print('not found')





def tail():
	if _.switches.isActive('Verbose'):
		_.switches.fieldSet( 'Print', 'active', True )
	if _.switches.isActive('Print'):
		return ''
	# return ''
	if _.switches.isActive('Status'): return ''
	if _.isWin:
		return ' > nul 2>&1'
	else:
		return ' > /dev/null 2>&1'

def urlpr(url,meta):
	if url is None: return None
	if url.endswith('/index.html'): url = url[:-len('index.html')]
	if url.endswith('/index.htm'): url = url[:-len('index.htm')]
	if url.endswith('/index.php'): url = url[:-len('index.php')]
	url=URL_APPS(url,meta)
	url=url.replace('f=/','f=')
	return url


def meta_scan2(path='',end=''):
	if not path: path = __.path(os.getcwd())
	# path = __.path(path)
	# print(path,end)
	global folder
	global meta
	# if not _.v.quiet:
	# 	if not _.switches.isActive('mkdir'):
	# 		_.pr(path,c='cyan')
	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	if os.path.isfile(path):
		folder = __.path(path,pop=True)
	else:
		folder = __.path(path)
	if os.path.isdir(path):folder+=os.sep
	# if os.path.isfile(path): folder = __.path(path,pop=True)
	# else: folder = __.path(path)
	i=0
	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		# print(os.path.isfile( folder+os.sep+'.folder.meta'+end ),folder+os.sep+'.folder.meta'+end)
		i+=1
		if i > 100:
			_.e('missing folder meta,aec7')
		try:
			folder = __.path(folder,pop=True)
		except Exception as e:
			break
	mPath = folder+os.sep+'.folder.meta'+end
	locations=_.getTable('site-locations.list')
	loc=locations.copy()
	if not mPath in locations: locations.append(mPath)
	if not locations == loc: _.saveTable(locations,'site-locations.list')

	if _.getText( mPath, raw=True ).strip().startswith('{'): meta = _.getTable2( mPath )
	else: meta = _.getYML( mPath )
	
	# _.cp(mPath.replace('.folder.meta'+end,''),'yellow')
	# if not _.v.quiet:
	# 	if not _.switches.isActive('mkdir'):
	# 		_.cp(mPath,'yellow')
	# 		_.pv(meta)
	_.v.fp='\nsftp:\n\tpath:\n\n not in .folder.meta'
	if 'sftp' in meta:
		rpath = meta['sftp']['path'].rstrip('/')
		fpath = file.replace( __.path(folder), rpath ).replace('\\','/')
		if os.path.isdir(path) and not fpath.endswith('/'): fpath += '/'
		try:
			_.v.fp=fpath.replace(rpath+'/',meta['sftp']['path']+'/')
			_.v.fp=_.v.fp.replace('//','/').replace('//','/')
		except: pass

	return _.v.fp

def meta_scan(path,end=''):
	# path = __.path(path)
	# print(path,end)
	global folder
	global meta
	if not _.v.quiet:
		if not _.switches.isActive('mkdir'):
			_.pr(path,c='cyan')
	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	if type(path) == str and os.path.isfile(path):
		folder = __.path(path,pop=True)
	else:
		folder = __.path(path)
	if os.path.isdir(path):folder+=os.sep
	# if os.path.isfile(path): folder = __.path(path,pop=True)
	# else: folder = __.path(path)
	i=0
	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		# print(os.path.isfile( folder+os.sep+'.folder.meta'+end ),folder+os.sep+'.folder.meta'+end)
		i+=1
		if i > 100:
			_.e('missing folder meta,aec7')
		try:
			folder = __.path(folder,pop=True)
		except Exception as e:
			break
	mPath = folder+os.sep+'.folder.meta'+end
	locations=_.getTable('site-locations.list')
	loc=locations.copy()
	if not mPath in locations: locations.append(mPath)
	if not locations == loc: _.saveTable(locations,'site-locations.list')

	if _.getText( mPath, raw=True ).strip().startswith('{'): meta = _.getTable2( mPath )
	else: meta = _.getYML( mPath )
	
	# _.cp(mPath.replace('.folder.meta'+end,''),'yellow')
	if not _.v.quiet:
		if not _.switches.isActive('mkdir'):
			_.cp(mPath,'yellow')
			_.pv(meta)
	url=None
	if 'url' in meta:

		url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')	
		# print(url)
		if os.path.isdir(path) and not url.endswith('/'): url += '/'
		try:
			_.v.fp=url.replace(meta['url']+'/',meta['sftp']['path']+'/')
			_.v.fp=_.v.fp.replace('//','/').replace('//','/')
		except: pass
	theUrl = urlpr(url,meta)
	if os.path.isdir(path):
		try:
			theUrl = theUrl.replace('?loader&url=%3Fview%3D1%26f%3D','?fo=').rstrip('/')
			theUrl = theUrl.replace('?view=1&f=','?fo=').rstrip('/')
		except:
			theUrl=''
	return theUrl

def meta_scanR(path,end):
	global folder
	global meta

	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	if os.path.isfile(path):
		folder = __.path(path,pop=True)
	else:
		folder = __.path(path)
	if os.path.isdir(path):folder+=os.sep
	# if os.path.isfile(path): folder = __.path(path,pop=True)
	# else: folder = __.path(path)
	i=0
	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		# print(os.path.isfile( folder+os.sep+'.folder.meta'+end ),folder+os.sep+'.folder.meta'+end)
		i+=1
		if i > 100:
			_.e('missing folder meta,a71d')
		try:
			folder = __.path(folder,pop=True)
		except Exception as e:
			break
	mPath = folder+os.sep+'.folder.meta'+end
	locations=_.getTable('site-locations.list')
	loc=locations.copy()
	if not mPath in locations: locations.append(mPath)
	if not locations == loc: _.saveTable(locations,'site-locations.list')

	if _.getText( mPath, raw=True ).strip().startswith('{'): meta = _.getTable2( mPath )
	else: meta = _.getYML( mPath )
	
	if 'url' in meta:

		url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
		# print(url)
		if os.path.isdir(path) and not url.endswith('/'): url += '/'
		try:
			_.v.fp=url.replace(meta['url']+'/',meta['sftp']['path']+'/')
			_.v.fp=_.v.fp.replace('//','/').replace('//','/')
		except: pass
		try:
			rPath = _.v.fp.replace(meta['url'],meta['sftp']['path'])
			return rPath
		except: pass
	return ''
APPS = {
	'notes': {
		# 'path': '/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/TECH/ddoc/asdf',
		'path': 'asdf',
		'remove': 'https://eyeformeta.com/',
		'add': 'https://eyeformeta.com/apps/Scrolls/?view=1&f=',
		'slash': '/',
	},
}
def URL_APPS(url,meta):
	rPath = None
	if 'sftp' in meta and 'path' in meta['sftp']:
		rPath = meta['sftp']['path']
	if rPath is None: return url
	global APPS
	for app in APPS:
		if APPS[app]['path'] in rPath:
			url=APPS[app]['add']+rPath.replace(APPS[app]['path'],'')+APPS[app]['slash']+url.replace(APPS[app]['remove'],'')
	return url


def process(path,end='',ft=None):
	if _.switches.isActive('Verbose'):
		_.switches.fieldSet( 'Print', 'active', True )
		verbos = ' -v '
	else:
		verbos = ''
	if type(path) == str and not os.path.exists(path): return None
	global folder
	global meta
	# _.pr(path,c='cyan')
	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	# folder = __.path(path,pop=True)

	meta_scan(path,end)




	
	# Upload-Scp Download-Scp Test
	ftp=None
	url=None
	for k in meta:
		for su in meta[k]:
			if su == 'path':
				ftp=meta[k]
				break
		if not ftp is None:
			break

	scp='scp'
	ssh='ssh'
	if _.isWin:
		scp='"C:\\Program Files\\Git\\usr\\bin\\scp.exe"'
	if type(ftp['server']) == list:
		servers = ftp['server']
	else:
		servers = [ftp['server']]
	
	for s in servers:
		if not _.showLine(s): continue
		if not _.switches.isActive('mkdir'):
			_.pr(s,c='green')
		f=ftp['path']
		u=ftp['user']
		if _.switches.isActive('NoPassword') and 'password' in ftp:
			pw=ftp['password']
		else:
			if _.switches.isActive('NoPassword'): _.pr('NoPassword: True', 'Using keychain:', u+'@'+s ,c='red')
			try:
				pw=_keychain.imp.key(u+'@'+s)
			except:
				_.e('Login error')
		_ssh=sshpass(pw,'ssh')
		_scp=sshpass(pw,'scp')
		if _.switches.isActive('Verbose'):
			_rsync=sshpass(pw,'rsync -avvz ')
		else:
			_rsync=sshpass(pw,'rsync -az ')

		if _.isWin and not _.switches.isActive('NotWSL'):
			scp=_scp
			ssh=_ssh
			_file=wsl(file)
			_path=wsl(path)
		else:
			_file=file
			_path=path
		if not _.isWin:
			scp=_scp[len('wsl '):]
			ssh=_ssh[len('wsl '):]
			if _scp.startswith('wsl '):
				scp=_scp[len('wsl '):]
			if _ssh.startswith('wsl '):
				ssh=_ssh[len('wsl '):]
			if _rsync.startswith('wsl '):
				rsync=_rsync[len('wsl '):]




		if 'url' in meta:
			url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
			if os.path.isdir(path):
				url += '/'
			if not _.switches.isActive('mkdir'):
				_.pr(path,c='cyan')
				url=url.replace('=/','=')
				theUrl = urlpr(url,meta)
				if os.path.isdir(path):
					theUrl = theUrl.replace('?loader&url=%3Fview%3D1%26f%3D','?fo=').rstrip('/')
					theUrl = theUrl.replace('?view=1&f=','?fo=').rstrip('/')
					_.pr(theUrl,c='Background.blue')
				else:
					_.pr(theUrl,c='Background.blue')
			if url.endswith('.js'): _.pr( '<script src="'+url+'"></script>' ,c='yellow')
			elif url.endswith('.css'): _.pr( '<link rel="stylesheet" href="'+url+'">' ,c='yellow')
			elif url.endswith('.jpg'): _.pr( '<img src="'+url+'"/>' ,c='yellow')
			elif url.endswith('.png'): _.pr( '<img src="'+url+'"/>' ,c='yellow')
			elif url.endswith('.gif'): _.pr( '<img src="'+url+'"/>' ,c='yellow')
			

			try:
				if not _.switches.isActive('mkdir'):
					_.pr(_.v.fp,c='Background.light_blue')
			except: pass
			

			if _.switches.isActive('Test'):
				try:
					import webbrowser
				except Exception as e:
					pass
				try:
					webbrowser.open(url, new=2)
				except Exception as e:
					_.e(e)
		# _.pr(ftp, pvs=1)
		if ft:
			for k in ft: ftp[k]=ft[k]


		if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
			# if ftp is None or url is None:
			#     _.e('meta missing fields')

			fi = file.replace( __.path(folder), f ).replace('\\','/')
			# _.pr(fi,c='cyan')
			if os.path.isdir(path):
				fi = "/".join(fi.split("/")[:-1])+'/'

			#     fi=__.path(fi,pop=True)
			#     fi += '/'
			#     path+=os.sep
			# _.pr(fi,c='yellow')
		if _.switches.isActive('mkdir'):
		# if True:
			fi = file.replace( __.path(folder), f ).replace('\\','/')
			rfo = _.tailpop(fi,'/')
			

			#new
			if _.switches.isActive('NoPassword') and 'password' in ftp:
				pw=ftp['password']
			else:
				if _.switches.isActive('NoPassword'): _.pr('NoPassword: True', 'Using keychain:', u+'@'+s ,c='red')
				try:
					pw=_keychain.imp.key(u+'@'+s)
				except:
					_.e('Login error',u+'@'+s)
			
			# #old
			# if _.switches.isActive('NoPassword'):
			# 	pw=ftp['password']
			# else:
			# 	try:
			# 		pw=_vault.imp.s.de( ftp['password'] )
			# 	except:
			# 		_.e('Login error')
			
			
			
			# if os.path.isdir(path):
			#     fi=__.path(fi,pop=True)
			#     fi += '/'
			#     path+=os.sep
			
			mkdir=f'{ssh} {verbos} -f {u}@{s} "/bin/python3 /opt/rightthumb-widgets-v0/widgets/python/mkdir.py -folder {rfo}"'+tail()

			if _.switches.isActive('Print'):
				_.pr(_.password_filter(mkdir))
			try:
				os.system( mkdir )
			except Exception as e:
				_.e(e)
			_.switches.fieldSet( 'mkdir', 'active', False )
			# for x in dir(_.switches): print(x)
			action()
			return None




		# wsl sshpass -p 'THE_PASSWORD' scp /mnt/c/Users/Scott/.rt/profile/tables/keychain.crypt root@yavin.sds.sh:/opt/
		#                                                                                                                                <--( WSL )

		#                                                                                                                                <--( WSL )




		if _.switches.isActive('rsync'):
			# do=f'{scp} {path}  {u}@{s}:{fi}'
			if os.path.isdir(file):
				do=f'{rsync} -r {_file}  {u}@{s}:{fi}'+tail()
			else:
				__fo = __.path(_file,pop=1)
				do=f'{rsync} {__fo}  {u}@{s}:{fi}'+tail()
		else:
			if _.switches.isActive('Upload-Scp'):
				# do=f'{scp} {path}  {u}@{s}:{fi}'
				if os.path.isdir(file):
					do=f'{scp} -r {_file}  {u}@{s}:{fi}'+tail()
				else:
					do=f'{scp} {_file}  {u}@{s}:{fi}'+tail()
			if _.switches.isActive('Download-Scp'):
				if os.path.isdir(path):
					the_file=_file.split('/')[-1]
					do=f'{scp} -r {u}@{s}:{fi}{the_file}/* {_file}/  '+tail()
					# print(do);sys.exit();
					# do=f'{scp} -r {u}@{s}:{fi} {_path}'+tail()
				else:
					do=f'{scp} {u}@{s}:{fi} {_path}'+tail()
		# if _.switches.isActive('Print'): _.pr(do)

		if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp') or _.switches.isActive('rsync'):
			#here
			#do
			# print(do)
			# print(do)
			# print(do)
			# print(do)
			# print(do)
			# print(do)
			# print(do)
			# print(do)
			if _.switches.isActive('Print'):
				if 'p' in _.switches.value('Print'):
					_.pr(do)
				else:
					_.pr(_.password_filter(do))
			if not _.switches.isActive('rsync'):
				try:
					do = ' '+do
					do=do.replace(' scp ',' scp '+verbos)
					if _.switches.isActive('CMD'):
						_.pr(do)
					else:
						do = str(do)
						# print(do)
						os.system( do )
				except Exception as e:
					_.e(e)
			elif _.switches.isActive('rsync'):
				try:
					if _.switches.isActive('CMD'):
						_.pr(do)
					else:
						os.system( do )
				except Exception as e:
					_.e(e)

_keychain = _.regImp( __.appReg, 'keychain' )
__.keychain_copy=False
# _keychain.imp.key('')

def remoteFolder():
	global meta
	global folder
	path=os.getcwd()
	meta_scan(path,'')
	ftp=None
	# Upload-Scp Download-Scp Test
	for k in meta:
		for su in meta[k]:
			if su == 'path':
				ftp=meta[k]
				break
		if not ftp is None:
			break

	ssh='ssh'
	if type(ftp['server']) == list:
		servers = ftp['server']
	else:
		servers = [ftp['server']]
	
	for s in servers:
		if not _.showLine(s): continue
		_.pr(s,c='green')
		f=ftp['path']
		u=ftp['user']

		# 

		#new
		if _.switches.isActive('NoPassword') and 'password' in ftp:
			pw=ftp['password']
		else:
			if _.switches.isActive('NoPassword'): _.pr('NoPassword: True', 'Using keychain:', u+'@'+s ,c='red')
			try:
				pw=_keychain.imp.key(u+'@'+s)
			except:
				_.e('Login error',u+'@'+s)
		
		# #old
		# if _.switches.isActive('NoPassword'):
		# 	pw=ftp['password']
		# else:
		# 	try:
		# 		pw=_vault.imp.s.de( ftp['password'] )
		# 	except:
		# 		_.e('Login error')
		
		
		
		_ssh=sshpass(pw,'ssh')
		# print(_.isWin)
		# print(_.switches.isActive('NotWSL'))
		# sys.exit()
		if _.isWin and not _.switches.isActive('NotWSL'):
			ssh=_ssh
			_path=wsl(path)
			folder=wsl(folder)
			# print(_path)
			# sys.exit()
		else:
			_path=path
		if not _.isWin:
			ssh=_ssh[len('wsl '):]
		
		fo = _path.replace( folder, f ).replace('\\','/')
		fo += '/'
		us=u+'@'+s
		ssh+=f' -t "{us}" "cd \"{fo}\"; exec bash -l";'
		# print(ssh)
		# sys.exit()
		if _.switches.isActive('CMD'):
			print(ssh)
		os.system(ssh)
		_.pr()
		_.pr()
		_.pr(os.getcwd(),c='cyan')
		sys.exit()



def print_remote_location(urls=None):
	if not _.switches.isActive('Files'):
		_.pr(meta_scan2())
	else:
		for path in _.switches.values('Files'):
			_.pr(meta_scan2(path,''))



def URL(urls=None):

	spent=[]
	RETURN=False
	if not __.site_url is None:
		RETURN=True
	if not urls is None:
		RETURN=True
		if type(urls) == str:
			urls=[urls]
	if not RETURN:
		urls=_.switches.values('URL')
		_file_open = _.regImp( __.appReg, 'file-open' )
		_file_open.switch('App',_v.meta['code_editor'])
	for url in urls:
		url=url.replace('https://www.','https://')
		if '?' in url: url=url.split('?')[0]
		sites=_.getTable('site-locations.list')
		for mPath in sites:
			if os.path.isfile(mPath):
				p = __.path(mPath,pop=True)
				if _.getText( mPath, raw=True ).strip().startswith('{'): meta = _.getTable2( mPath )
				else: meta = _.getYML( mPath )
				if 'url' in meta:
					u = meta['url'].replace('https://www.','https://')
					if url.startswith(u):
						x=url[len(u):].replace('/',os.sep)
						y=p+os.sep+x
						if os.path.isdir(y):
							test='index.php index.htm index.html'.split(' ')
							for t in test:
								yt=str(y+os.sep+t).replace(os.sep+os.sep,os.sep)
								if os.path.isfile(yt):
									y=yt
						y=y.replace(os.sep+os.sep,os.sep)
						if os.path.isfile(y):
							if not y in spent:
								spent.append(y)
								# _.pr(y,c='yellow')
								if RETURN:
									__.site_url = y
									return y
								else:
									_file_open.switch('Files',y)
									_file_open.action()


def action():
	if _.switches.isActive('Find.folder.meta'):
		find_meta_file()
		return None


	# _.switches.fieldSet( 'NotWSL', 'active', True )
	if _.switches.isActive('Remote-Location'):
		for path in _.switches.values(1):
			rPath = meta_scanR(path,'')
			_.pr(rPath,c='green')
			# print('snap')
		return None
	if _.switches.isActive('URL'):
		url = URL()

		return None

	if _.switches.isActive('Print-Remote-Location'):
		print_remote_location()
		return None
	global meta


	# print( wsl(_.switches.values('Files')[0]) )
	# sys.exit()
	if _.switches.isActive('SSH-Remote_Folder'):
		remoteFolder()
		return None

	if _.switches.isActive('Files') and len(_.switches.all())==1:
		_.v.quiet = True
		for path in _.switches.values('Files'):
			url=meta_scan(path,'')
			url=url.replace('=/','=')
			if _.switches.isActive('InBrowser'):
				import webbrowser
				webbrowser.open(url, new=2)
			if url: _.pr(url,c='Background.blue')
			if url.endswith('.js'): _.pr( '<script src="'+url+'"></script>' ,c='yellow')
			return url

	if _.switches.isActive('Servers') and not len(_.switches.value('Servers')):
		_.switches.fieldSet( 'Servers', 'value', 'b,h,m,t' )
		_.switches.fieldSet( 'Servers', 'values', 'b,h,m,t'.split(',') )
	if not _.switches.isActive('Test') and not _.switches.isActive('Upload-Scp') and not _.switches.isActive('Download-Scp'):
		_.switches.fieldSet( 'Test', 'active', True )
	if _.switches.isActive('Server'): end='.'+_.switches.value('Server');
	else: end='';
	# for i,path in enumerate( _.switches.values('Files') ):
	for i,path in enumerate( _.isData(r=1) ):
		path = __.path(path)
		# process(path,end)
		if not _.switches.isActive('Servers'):
			process(path,end)
		else:
			for srv in _.switches.values('Servers'):
				srv_dic = {}
				if srv in srv_dic: srv = srv_dic[srv]
				sv = {
						'server': srv+'.sds.sh'
				}
				process(path,end,sv)
				_.linePrint(c='red')
				_.pr()
				_.pr('\tServer Override',c='Background.red')
				_.pr()
				_.pr('\t\t'+srv+'.sds.sh',c='yellow')
				_.pr()

				_.linePrint(c='red')

_fileBackup = None
def encrypt_markdown(path):
	if os.path.isfile(path) and path.endswith('.md'):
		if _fileBackup is None:
			_fileBackup = _.regImp( focus(), 'fileBackup' )
			_fileBackup.switch( 'Silent' )
			_fileBackup.switch( 'Flag', 'imdb' )
			_fileBackup.switch( 'isRunOnce' )
			_fileBackup.switch( 'DoNotSchedule' )
		_fileBackup.switch( 'Input', path )
		_fileBackup.action()


def wsl(path):
	subject = __.path(path)
	git_path = subject
	git_path = git_path.replace( _v.slashes['w'], _v.slashes['u'] )
	git_path = git_path.replace( ':', '' )
	git_path = _v.slashes['u'] + git_path
	wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
	wsl5=wsl5.replace(' ','\\ ')
	return wsl5

def sshpass(pw,cmd):
	if _.switches.isActive('NoPassword'):
		return f"wsl {cmd} "
	return f'''wsl sshpass -p "{pw}" {cmd} '''
if not _.switches.isActive('NoPassword'):
	_vault = _.regImp( __.appReg, '_rightThumb._vault' )
_.v.quiet = False







# import subprocess
# result = subprocess.run(['wsl', 'which'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# print(result.stdout)
# result = subprocess.run(['C:\\path\\to\\wsl.exe', 'which'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# print(result.stdout)
# sys.exit()

# os.system('wsl');sys.exit();
# os.system('C:\\Windows\\System32\\wsl.exe');sys.exit();




########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()


# URL()

# dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart