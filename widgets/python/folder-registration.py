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
	_.switches.register( 'relevant', '-r' )
	_.switches.register( 'WSL', '-wsl' )
	_.switches.register( 'Ago', '-ago', '1m' )
	_.switches.register( 'Folder', '-f,-fo,-folder', '1m' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

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
	'file': 'folder-registration.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Realtime(ish) documentation of folder usage',
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
		# globals()['var']
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


def action():
	if len(_.switches.all())==0:
		register()
		return None

	if _.switches.isActive('relevant'):
		relevant()
		return None


def relevant():
	load()
	global epoch
	global day
	global last
	global lastFi
	global xFo

	threshold_bytes = 20
	threshold_lines = 20
	# threshold_ago   = _.timeAgo('5min')
	threshold_ago   = _.timeAgo('1d')
	if _.switches.isActive('Ago'): threshold_ago = _.switches.value('Ago')



	_relevant=xFo+'relevant'
	relevant=[]
	import _rightThumb._dir as _dir
	records=[]
	for path in _.fo(xFo+'log'):
		rec = _dir.info(path,lines=True)
		records.append(rec)
	records = _.tables.returnSorted( 'data', 'd.lines', records )
	for i,rec in enumerate(records):
		if not rec['me']: rec['me']=0
		path=rec['path']
		good=False

		# if rec['bytes'] > threshold_bytes: good=True
		if rec['lines'] > threshold_lines: good=True
		if rec['me'] > threshold_ago: good=True
		if good:
			print(path)
			# print(rec)
			p=path.split(os.sep)
			fi=p.pop(-1)
			f0=xFo+'resolve'+os.sep+fi
			f1=_v.resolveFolderIDs(_.getText(f0,raw=True,clean=2))
			relevant.append(f1)
			# print(fi,rec['lines'],f1)
			# print (path)
			# print(fi)
			# print(f0)
			# _.pv(rec)
			# sys.exit()
	_.saveText(relevant,_relevant)
	_.pr(_relevant,c='cyan')


def register():
	load()
	global epoch
	global day
	global last
	global lastFi
	global xFo
	
	session = os.environ['Session_ID']
	_v.mkdir(day+session)

	lastFi = day+session+os.sep+'id'
	if os.path.isfile(lastFi): last=_.getText(lastFi,raw=True,clean=2)

	if _.switches.isActive('Folder'):
		fo = _v.sanitizeFolder(_.switches.values('Folder')[0])
	else:
		fo = _v.sanitizeFolder(os.getcwd())
	sha = _md5.string(fo,'sha1')

	sess = day+session+'.csv'


	# print(day)
	# print(last)
	# print(sha)


	if not sha == last:
		# print(os.path.isfile(lastFi))
		_.afile(epoch,xFo+'log'+os.sep+sha)
		if not os.path.isfile(xFo+'resolve'+os.sep+sha): _.saveText(fo,xFo+'resolve'+os.sep+sha)
		_.saveText(sha,lastFi)

	
	_.afile(str(epoch),day+session+os.sep+sha)



def load():
	global epoch
	global day
	global last
	global lastFi
	global xFo

	epoch=int(str(time.time()).split('.')[0])
	last=''

	if _.switches.isActive('WSL'):
		tt='/mnt/c/Users/Scott/.rt/profile/tables'
	else:
		tt=_v.myLogs

	xFo=tt+os.sep+'folders'+os.sep
	day = xFo+'daily'+os.sep+_.day(epoch)
	_v.mkdir(day)
	_v.mkdir(xFo+'resolve')
	_v.mkdir(xFo+'log')







import _rightThumb._md5 as _md5

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

