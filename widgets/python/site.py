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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isRequired=True )
	_.switches.register( 'mkdir', '-mkdir' )
	_.switches.register( 'Server', '-v,-srv,-server' )
	_.switches.register( 'Print', '-print' )




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
	if _.isWin:
		return ' > nul 2>&1'
	else:
		return ' > /dev/null 2>&1'

def process(path,end=''):
	_.pr(path,c='cyan')
	meta = {}
	try:
		file = os.path.abspath(path)
	except Exception as e:
		file = path
	folder = __.path(path,pop=True)
	i=0



	while not os.path.isfile( folder+os.sep+'.folder.meta'+end ):
		i+=1
		if i > 100:
			_.e('missing folder meta')
		try:
			folder = __.path(folder,pop=True)
		except Exception as e:
			break
	mPath = folder+os.sep+'.folder.meta'+end
	meta = _.getTable2( mPath )
	_.cp(mPath.replace('.folder.meta'+end,''),'yellow')
	_.pv(meta)
	

	# Upload-Scp Download-Scp Test
	ftp=None
	url=None
	for k in meta:
		for su in meta[k]:
			if su == 'full-path':
				ftp=meta[k]
				break
		if not ftp is None:
			break
	if 'url' in meta:
		url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
		if os.path.isdir(path):
			url += '/'
		_.pr(url)
		if _.switches.isActive('Test'):
			try:
				import webbrowser
			except Exception as e:
				pass
			try:
				webbrowser.open(url, new=2)
			except Exception as e:
				_.e(e)

	scp='scp'
	if _.isWin:
		scp='scp'
		scp='"C:\\Program Files\\Git\\usr\\bin\\scp.exe"'

	if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
		# if ftp is None or url is None:
		# 	_.e('meta missing fields')
		s=ftp['server']
		f=ftp['full-path']
		u=ftp['user']
		# pw=_vault.imp.s.de( ftp['password'] )
		fi = file.replace( __.path(folder), f ).replace('\\','/')
		if os.path.isdir(path):
			fi=__.path(fi,pop=True)
			fi += '/'
			path+=os.sep


		
		


	if _.switches.isActive('mkdir'):
		s=ftp['server']
		f=ftp['full-path']
		u=ftp['user']
		fi = file.replace( __.path(folder), f ).replace('\\','/')
		rfo = _.tailpop(fi,'/')
		# pw=_vault.imp.s.de( ftp['password'] )
		if os.path.isdir(path):
			fi=__.path(fi,pop=True)
			fi += '/'
			path+=os.sep
		mkdir=f'ssh -f {u}@{s} "/bin/python3 /opt/rightthumb-widgets-v0/widgets/python/mkdir.py -folder {rfo}"'+tail()
		_.pr(mkdir)
		if not _.switches.isActive('Print'):
			try:
				_.cp('creating folder structure','yellow')
				os.system( mkdir )
			except Exception as e:
				_.e(e)

	if _.switches.isActive('Upload-Scp'):
		# do=f'{scp} {path}  {u}@{s}:{fi}'
		if os.path.isdir(file):
			do=f'{scp} -r {file}  {u}@{s}:{fi}'+tail()
		else:
			do=f'{scp} {file}  {u}@{s}:{fi}'+tail()
	if _.switches.isActive('Download-Scp'):
		if os.path.isdir(path):
			do=f'{scp} -r {u}@{s}:{fi} {path}'+tail()
		else:
			do=f'{scp}  {u}@{s}:{fi} {path}'+tail()
	
	if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
		# _.pr(do)
		if not _.switches.isActive('Print'):
			try:
				os.system( do )
			except Exception as e:
				_.e(e)


	
		 
def action():
	if not _.switches.isActive('Test') and not _.switches.isActive('Upload-Scp') and not _.switches.isActive('Download-Scp'):
		_.switches.fieldSet( 'Test', 'active', True )
	if _.switches.isActive('Server'): end='.'+_.switches.value('Server');
	else: end='';
	for i,path in enumerate( _.switches.values('Files') ):
		process(path,end)

# _vault = _.regImp( __.appReg, '_rightThumb._vault' )


	
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





