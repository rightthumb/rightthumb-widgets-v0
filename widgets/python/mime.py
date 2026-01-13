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
	pass
	#b)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob', description='Files', isRequired=False )
	_.switches.register( 'Full-Path', '-rr,-relative' )
	_.switches.register( 'Recursive', '-r,-recursive' )
	_.switches.register( 'No-Pre-Space', '-nospace' )
	_.switches.register( 'Text', '-t,-txt,-text' )
	_.switches.register( 'Binary', '-b,-bin,-binary' )
	_.switches.register( 'Corrupt', '-cc,-co,-cpt,-corrupt' )
	#e)--> examples

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
						_.hp('p mime + "application/x-dosexec"'),
						# _.linePrint(label='simple',p=0),
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
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--#
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

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
os=__.imp('os.system')
import sys
magic = __.imp('magic')
import sys


# mimetypes = {}
def fix(path,mimetype):
	global mimetypes
	global mimeLEN
	global text_plain
	global text_plain_fi
	global text_plain_fi_raw
	if mimetype == 'text/plain':
		fi = path.split(os.sep)[-1]
		if not '.' in fi:
			if fi in text_plain_fi_raw: return text_plain_fi_raw[fi]
			if fi in text_plain_fi:
				file = open( path, 'r' ).read(35).lower()
				# size scan mime
				for rec in text_plain_fi[fi]:
					if rec['size'] > len(file): file = open( path, 'r' ).read(rec['size']).lower()
					good=True
					for txt in rec['scan'].lower().split(','):
						if not txt in file: good=False
					if good: return rec['mime']

		else:
			ex=path.split('.')[-1]
			if ex in text_plain:
				file = open( path, 'r' ).read(35).lower()
				# size scan mime
				for rec in text_plain[ex]:
					if rec['size'] > len(file): file = open( path, 'r' ).read(rec['size']).lower()
					good=True
					for txt in rec['scan'].lower().split(','):
						if not txt in file: good=False
					if good: return rec['mime']

	path=path.lower()
	if not mimetype in mimetypes: return None

	if os.sep in path: path = path.split(os.sep)[-1]
	if not '.' in path: return None
	
	if '.folder.meta' in path: return 'text/efm-folder-meta'
	testing = 'backup,bk'.split(',')
	if path.split('.')[-1] in testing:
		for test in testing:
			if path.endswith('.'+test): path = path[0:len(path)-len('.'+test)]

	parts = path.split('.')

	if len(parts) > 1 and len(parts[-2]) <= mimeLEN and parts[-2]+'.'+parts[-1] in mimetypes[mimetype]: return mimetypes[mimetype][parts[-2]+'.'+parts[-1]]
	if parts[-1] in mimetypes[mimetype]: return mimetypes[mimetype][parts[-1]]
	return None
def genMime(path):
	result = genMimeRun(path)
	if result.startswith('application/office-') and result.endswith('ml'): result = result[0:len(result)-2]
	return result
def genMimeRun(path):
	global slowAF
	if path in slowAF:
		if os.stat( path ).st_size == slowAF[path]['bytes']: return slowAF[path]['mimetype']
	start=time.time()
	mimetype = mime.from_file(path)
	duration=time.time()-start
	if duration > .7:
		slowAF[path]={
						'bytes': os.stat( path ).st_size,
						'mimetype': mimetype,
		}
		_.saveTable(slowAF,'mime-slow.index')
	# if 'text/plain' == mimetype:
	fx = fix(path,mimetype)
	if fx: mimetype=fx



	# return mimetype
	# application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
	# application/vnd.openxmlformats-officedocument.wordprocessingml.document
	# application/office-openxmlformats-
	if 'officedocument.' in mimetype:
		for xXx in mimetype.split('officedocument.'):
			try:
				xx = mimetype.split('.')[2]
			except Exception as e:
				print(xXx)
				print(mimetype)
				sys.exit()
			
			xx = xx.replace('application/','application/office-')
			yy = 'application/office-'+xx
			return yy
	else: return mimetype

def script(path):
	global tb
	global full
	global mime
	global base
	global nospace
	# _.pr(path)
	path = __.path(path)
	path2=path
	if not full and path.startswith(base): path2 = path[len(base):]
	m = genMime(path)
	m=m.strip()
	# print('tb',tb)
	if tb:
		if m == 'inode/x-empty': return None
		elif tb == 'c' and not m.startswith('corrupt/'): return None
		elif tb == 'b' and m.startswith('corrupt/'): return None
		elif tb == 'b' and m.startswith('text/'): return None

	if _.showLine(m+'  '+path2) and not 'No such file or directory' in m:
		if nospace:
			mm = m
		else:
			_.fields.register( 'mime', 'mimetype',m )
			mm = _.fields.value( 'mime', 'mimetype', m , right=True )
		_.pr(mm+'  '+path2)
		# try:
		# except: pass

def action():
	

	
	# mime.from_file("HelpPane.exe")
	
	_.fields.register( 'mime', 'mimetype','text/ssh-key-private' )
	# _.fields.register( 'mime', 'mimetype','application/office-wordprocessingml' )

	if _.isData():
		for path in _.isData(): script(path)
	else: _.fo(r=_.switches.isActive('Recursive'),script=script)


	
base=os.getcwd()+os.sep

if _.switches.isActive('Text'): tb = 't'
elif _.switches.isActive('Binary'): tb = 'b'
elif _.switches.isActive('Corrupt'): tb = 'c'
else: tb = None
# print('tb',tb)


full=_.switches.isActive('Full-Path')
nospace=_.switches.isActive('No-Pre-Space')
mime = magic.Magic(mime=True)
slowAF = _.getTable('mime-slow.index')


corrupt = {
				'zip': 'corrupt/zip',
				'crypt': 'corrupt/crypt',
				'pdf': 'corrupt/pdf',
}

mimeLEN = 5
mimetypes = {}
mimetypes['inode/x-empty'] = corrupt
mimetypes['text/plain'] = {


				'bat': 'text/x-msdos-batch',
				'txt': 'text/txt',
				'md': 'text/markdown',
				'ps1': 'text/x-powershell',
				'cfg': 'text/config',
				'ini': 'text/config',
				'conf': 'text/config',
				'js': 'text/javascript',
				'json': 'text/json',
				'css': 'text/json',
				'log': 'text/log',
				'xml': 'text/xml',
				'csv': 'text/csv',
				'html': 'text/html',
				'htm': 'text/html',
				'ovpn': 'text/config-vpn',
				'rdp': 'text/config-desktop',
				'sql': 'text/config-database',
				'nfo': 'text/info',
				'info': 'text/info',
				'url': 'text/website-url',
				# 'logs': 'text/log',
}
mimetypes['application/octet-stream'] = {
				'lnk': 'application/website-link',
}
for k in corrupt: mimetypes['text/plain'][k]=corrupt[k]

text_plain = {
				'key': [
							{'size':35,'scan':'OPENSSH,PRIVATE,KEY','mime':'text/ssh-key-private'}
				],
				'pub': [
							{'size':len(' ssh-rsa '),'scan':'ssh-rsa','mime':'text/ssh-key-public'}
				],
}

text_plain_fi = {
				'id_rsa': [
							{'size':35,'scan':'OPENSSH,PRIVATE,KEY','mime':'text/ssh-key-private'}
				],
}
text_plain_fi_raw = {
				'known_hosts': 'text/ssh-hosts',
}

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