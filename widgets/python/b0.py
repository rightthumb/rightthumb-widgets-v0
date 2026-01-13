#!/usr/bin/python3


import sys
import datetime
import _rightThumb._vars as _v
from os import sep, environ
import time
import platform
import _rightThumb._date as _date
def day(theDate):
	year  = yr(theDate)
	woy   = _woy(theDate)
	date  = _date.friendlyDate( theDate )[len('2022-'):].split(' ')[0]
	today = str(year)+sep+woy+sep+date
	# print(today)
	return today
def epochs(dy=0):
	dy=int(dy)
	# https://chat.openai.com/chat
	if dy==0: return time.time()
	dt = datetime.datetime.fromtimestamp(time.time())
	ndt = dt - datetime.timedelta(days=dy)
	return int(ndt.timestamp())

def _woy(theDate):
	w=str(datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[1])
	if len(w)==1:w='0'+w
	return w
def yr(theDate): return str(datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0])

if '-print' in sys.argv:
	dx=_v.rtp+'daily'+sep+day(epochs(0))+sep+'invoice_'
	if '-date' in sys.argv:
		dx=dx+_date.dayStrip()
	print( dx )
if '-0' in sys.argv:

	




	def wsl(path):
		subject = path
		git_path = subject
		git_path = git_path.replace( _v.slashes['w'], _v.slashes['u'] )
		git_path = git_path.replace( ':', '' )
		git_path = _v.slashes['u'] + git_path
		wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
		wsl5=wsl5.replace(' ','\\ ')
		wsl5=wsl5.replace('/mnt//home/scott','/mnt/c/Users/Scott')
		wsl5=wsl5.replace('/home/scott','/mnt/c/Users/Scott')
		return wsl5
	def fdrA(dy=0):
		dy=int(dy)
		fo = _v.rtp+'daily'+sep+day(epochs(dy));
		_v.mkdir(fo)
		a='alias '+str(dy)+'="cd '+wsl(fo)+'"'
		# print(a)
		return a

	

	lines=[
				'alias woy="cd /mnt/c/Users/Scott/.rt/profile/daily/'+yr(time.time())+'/'+_woy(time.time())+'"',
				'alias y="cd /mnt/c/Users/Scott/.rt/profile/daily/'+yr(time.time())+'"',
				'alias yr="cd /mnt/c/Users/Scott/.rt/profile/daily/'+yr(time.time())+'"',
				'alias year="cd /mnt/c/Users/Scott/.rt/profile/daily/'+yr(time.time())+'"',

				'alias 00="cd /mnt/c/Users/Scott/.rt/profile/daily"',
				'alias da="cd /mnt/c/Users/Scott/.rt/profile/daily"',
				'alias daily="cd /mnt/c/Users/Scott/.rt/profile/daily"',
				'alias day="cd /mnt/c/Users/Scott/.rt/profile/daily"',

				fdrA(0),
				fdrA(1),
				fdrA(2),
				fdrA(3),
				fdrA(4),
				fdrA(5),
				fdrA(6),
				fdrA(7),

	]
	if 'win' in platform.system().lower():
		path=environ['USERPROFILE']+'\\.rt\\profile\\daily\\.seven.sh'
	else:
		path='/mnt/c/Users/Scott/.rt/profile/daily/.seven.sh'
	with open(path, "w") as file:
		for line in lines: file.write(line + "\n")

	sys.exit()
import os
vbm = _v.rtp+'bookmarks'+os.sep
b0 = vbm+'BM-0.txt'
today = datetime.date.today()
day_str = today.strftime('%Y-%m-%d')
day = datetime.datetime.strptime(day_str, "%Y-%m-%d").date()
start_of_day = datetime.datetime.combine(day, datetime.time.min)
epoch_of_day_start = int(start_of_day.timestamp())
file_modified_time = os.path.getmtime(b0)

# import _rightThumb._base3 as _; print(_.getText(b0,raw=True,clean=2));
if file_modified_time >= epoch_of_day_start: sys.exit()
print('b0')
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
	# _.switches.register( 'Input', '-i' )
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
	global vbm
	global b0
	epoch = time.time()
	today = _.day(epoch)
	fo =  _v.rtp+'daily'+os.sep+today
	_v.mkdir(fo)
	_.saveText(fo,b0)
	bm = _.getTable('bookmarks.index')
	bm['labels'][str(0)]=fo
	_.saveTable(bm,'bookmarks.index',p=0)


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