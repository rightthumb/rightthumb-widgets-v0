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
	# _.switches.register( 'DisableAutoLink', '-nolink' )
	_.switches.register( 'Delete', '-unlink,-del,-delete' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'FolderBase', '-base', 'D:\\websites\\domains\\eyeformeta.com\\public_html', isRequired=True )
	_.switches.register( 'To', '-to', 'D:\\websites\\domains\\eyeformeta.com\\LARGE', isRequired=True )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('require-pipe||file',True)
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'move-files-keep-folder-structure.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Move Files',
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
						_.hp('p files -size g 5mb --c | p move-files-keep-folder-structure  -base D:\\websites\\domains\\eyeformeta.com\\public_html  -to D:\\websites\\domains\\eyeformeta.com\\LARGE'),
						_.hp('p files -size g 5mb --c | p move-files-keep-folder-structure  -base D:\\websites\\domains\\eyeformeta.com\\public_html  -to D:\\websites\\domains\\eyeformeta.com\\LARGE -delete'),
						_.hp('p files + *.mp3 --c | p move-files-keep-folder-structure  -base D:\\websites\\domains\\eyeformeta.com\\public_html  -to D:\\websites\\domains\\eyeformeta.com\\LARGE -delete'),
						_.linePrint(label='simple',p=0),
						_.hp('reverse'),
						_.hp('p files --c | p move-files-keep-folder-structure  -to D:\\websites\\domains\\eyeformeta.com\\public_html  -base D:\\websites\\domains\\eyeformeta.com\\LARGE -delete'),
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

errors=[]
notDeleted=[]

def clean(path):
	while os.sep+os.sep in path:
		path=path.replace(os.sep+os.sep, os.sep)
	return path


def convert(path):
	global errors
	global bases
	global to
	for fo in bases:
		if fo in path: return path.replace(fo,to)
	errors.append(path)
	return None

def process(path):
	path=clean(path)
	global delete
	global notDeleted
	new = convert(path)
	if new is None:
		_.pr(path,c='red')
		return None
	_.pr(path,c='cyan')
	# print(new)
	# print(path)
	# sys.exit()
	_v.mkdir(new,isFile=True)
	# if _.isWin:
	if os.path.isfile(new):
		if delete:
			try: os.unlink(new)
			except: notDeleted.append(new)
				

	if not os.path.isfile(new):
		try: os.link(path,new)
		except: shutil.copy(path,new)

	if delete:
		try: os.unlink(path)
		except: notDeleted.append(path)



	


def action():
	global errors
	global notDeleted
	load()

	for path in _.isData(r=0):
		if os.path.isfile(path): process(path)

	if errors: _.pr('Errors:')
	for err in errors: _.pr('\t',err,c='red')

	if notDeleted: _.pr('Not Deleted:')
	for err in notDeleted: _.pr('\t',err,c='red')

def load():
	global bases
	global to
	global delete
	delete = _.switches.isActive('Delete')
	
	bases = _.switches.values('FolderBase')
	for i,b in enumerate(bases):
		if b.endswith(os.sep): b=b[:-1]
		bases[i] = clean(b)
	to = _.switches.values('To')[0]
	to=clean(to)
	if to.endswith(os.sep): to=to[:-1]
	
import os
import shutil

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

