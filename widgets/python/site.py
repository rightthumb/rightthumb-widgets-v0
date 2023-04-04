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
	_.switches.register( 'Test', '-t,-test' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt',  description='glob', isRequired=True )
	_.switches.register( 'Files', '-f,-file,-files','vps-tf', isData="name", isRequired=False )
	_.switches.register( 'mkdir', '-mkdir' )
	_.switches.register( 'Servers', '-v,-srv,-server,-vps', 'b h m t' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'Status', '-status' )
	_.switches.register( 'NotWSL', '-notwsl' )




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
						_.hp('u. vps-tf -srv b h m t'),
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

def tail():
	# return ''
	if _.switches.isActive('Status'): return ''
	if _.isWin:
		return ' > nul 2>&1'
	else:
		return ' > /dev/null 2>&1'

def urlpr(url):
	if url is None: return None
	if url.endswith('/index.html'): url = url[:-len('index.html')]
	if url.endswith('/index.htm'): url = url[:-len('index.htm')]
	if url.endswith('/index.php'): url = url[:-len('index.php')]
	return url


def meta_scan(path,end):
	global folder
	global meta
	if not _.v.quiet:
		_.pr(path,c='cyan')
	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	if os.path.isfile(path): folder = __.path(path,pop=True)
	else: folder = __.path(path)
	i=0
	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		# print(os.path.isfile( folder+os.sep+'.folder.meta'+end ),folder+os.sep+'.folder.meta'+end)
		i+=1
		if i > 100:
			_.e('missing folder meta')
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
		_.cp(mPath,'yellow')
		_.pv(meta)
	url=None
	if 'url' in meta:

		url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
		if os.path.isdir(path) and not url.endswith('/'): url += '/'
		try:
			_.v.fp=url.replace(meta['url']+'/',meta['sftp']['path']+'/')
			_.v.fp=_.v.fp.replace('//','/').replace('//','/')
		except: pass
	return urlpr(url)

def process(path,end='',ft=None):
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
		f=ftp['path']
		u=ftp['user']
		pw=_vault.imp.s.de( ftp['password'] )
		_ssh=sshpass(pw,'ssh')
		_scp=sshpass(pw,'scp')

		if _.isWin and not _.switches.isActive('NotWSL'):
			scp=_scp
			ssh=_ssh
			_file=wsl(file)
			_path=wsl(path)
		else:
			_file=file
			_path=path



		if 'url' in meta:
			url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
			if os.path.isdir(path):
				url += '/'
			_.pr(urlpr(url),c='Background.blue')
			try: _.pr(_.v.fp,c='Background.light_blue')
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
			# 	_.e('meta missing fields')

			fi = file.replace( __.path(folder), f ).replace('\\','/')
			if os.path.isdir(path):
				fi=__.path(fi,pop=True)
				fi += '/'
				path+=os.sep


		# if _.switches.isActive('mkdir'):
		if True:
			fi = file.replace( __.path(folder), f ).replace('\\','/')
			rfo = _.tailpop(fi,'/')
			pw=_vault.imp.s.de( ftp['password'] )
			if os.path.isdir(path):
				fi=__.path(fi,pop=True)
				fi += '/'
				path+=os.sep
			
			mkdir=f'{ssh} -f {u}@{s} "/bin/python3 /opt/rightthumb-widgets-v0/widgets/python/mkdir.py -folder {rfo}"'+tail()
			# _.pr(mkdir)
			if not _.switches.isActive('Print'):
				try:
					# _.cp('creating folder structure','yellow')
					os.system( mkdir )
				except Exception as e:
					_.e(e)




		# wsl sshpass -p 'THE_PASSWORD' scp /mnt/c/Users/Scott/.rt/profile/tables/keychain.crypt root@yavin.m-eta.app:/opt/
		#                                                                                                                                <--( WSL )

		#                                                                                                                                <--( WSL )




		if _.switches.isActive('Upload-Scp'):
			# do=f'{scp} {path}  {u}@{s}:{fi}'
			if os.path.isdir(file):
				do=f'{scp} -r {_file}  {u}@{s}:{fi}'+tail()
			else:
				do=f'{scp} {_file}  {u}@{s}:{fi}'+tail()
		if _.switches.isActive('Download-Scp'):
			if os.path.isdir(path):
				do=f'{scp} -r {u}@{s}:{fi} {_path}'+tail()
			else:
				do=f'{scp}  {u}@{s}:{fi} {_path}'+tail()
		if _.switches.isActive('Print'):
			_.pr(do)

		if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
			# _.pr(do)
			if not _.switches.isActive('Print'):
				try:
					os.system( do )
				except Exception as e:
					_.e(e)


	

def action():
	global meta

	# print( wsl(_.switches.values('Files')[0]) )
	# sys.exit()

	if _.switches.isActive('Files') and len(_.switches.all())==1:
		_.v.quiet = True
		for path in _.switches.values('Files'):
			url=meta_scan(path,'')
			if url: _.pr(url,c='Background.blue')
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
		# process(path,end)
		if not _.switches.isActive('Servers'):
			process(path,end)
		else:
			for srv in _.switches.values('Servers'):
				srv_dic = {
								'h': 'hoth',
								't': 'tatooine',
								'b': 'bespin',
								'm': 'mortis',
				}
				if srv in srv_dic: srv = srv_dic[srv]
				sv = {
						'server': srv+'.m-eta.app'
				}
				process(path,end,sv)
				_.linePrint(c='red')
				_.pr()
				_.pr('\tServer Override',c='Background.red')
				_.pr()
				_.pr('\t\t'+srv+'.m-eta.app',c='yellow')
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

def sshpass(pw,cmd): return f"wsl sshpass -p '{pw}' {cmd} "

_vault = _.regImp( __.appReg, '_rightThumb._vault' )
_.v.quiet = False
	
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





