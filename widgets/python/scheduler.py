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
	_.switches.register( 'NoBeep', '-nobeep' )
	_.switches.register( 'List', '-list' )
	_.switches.register( 'DaysOfWeek', '-dow,-day,-days', 'mon tue wed thu fri sat sun' )
	_.switches.register( 'Delete', '-del' )
	_.switches.register( 'Every', '-e,-every', 'day hour min sec OR d h m s' )
	# _.switches.register( 'At', '-at', '13:30' )
	_.switches.register( 'Python', '-py', 'autoBackup' )
	_.switches.register( 'Arguments', '-args' '-ago 1d  (USE THIS SWITCH LAST)' )
	# _.switches.register('Help', '?,??,/?,/??,-?,-??,--??,/h,/help,-help,--help', '(?? Print Table Help Without Global Switches) copy  OR ids  OR  12  OR  ?? x ')

	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])
# __.setting('default-switches',False)


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
						_.hp('p scheduler -py ephemeral--job-test -e m 2 '),
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




# {
# 	'once': True,
# 	'status': True,
# 	'command': '',
# 	'beep': True,
# 	'day': 1,
# 	'at': '13:30',

# 	'min': 1,
# 	'sec': 1,
# }


def scheduler():
	db=_.getTable('scheduler.json')
	if __.isWin: run=_v.ww+'\\batch\\rp.bat'
	else: run=_v.ww+'/bash/nav/rp.sh'
	for py in _.switches.values('Python'):
		rec={}
		if _.switches.isActive('NoBeep'):
			rec['beep']=False
		else:
			rec['beep']=True
		rec['status']=True
		rec['id']=_.genUUID()
		args=[]
		start=False
		for k in sys.argv:
			if start: args.append(k)
			if k == '-args': start=True

		rec['command']=f"{run} {py} {' '.join(args)}"
		if _.switches.isActive('Every') and len(_.switches.values('Every')):
			every=_.switches.values('Every')
			if every[0].lower().startswith('d'):
				key='day'
			elif every[0].lower().startswith('h'):
				key='hour'
			elif every[0].lower().startswith('m'):
				key='min'
			elif every[0].lower().startswith('s'):
				key='sec'
			rec[key]=1
			if len(every) >1: rec[key]=int(every[1])


		if _.switches.isActive('At'):
			if not 'day' in rec: rec['day']=1
			rec['at']=_.switches.values('At')[0]
		if _.switches.isActive('DaysOfWeek'):
			rec['days']=_.switches.values('DaysOfWeek')

		db.append(rec)
		print()
		_.saveTable(db,'scheduler.json')
		sys.exit()




def action():
	if _.switches.isActive('List'):
		db=_.getTable('scheduler.json')
		_.pt(db)
		sys.exit()
	elif _.switches.isActive('Python'):
		scheduler()
		print('Scheduled')
		sys.exit()
	elif _.switches.isActive('Delete'):
		for delete in _.switches.values('Delete'):
			try: schedule.clear(delete)
			except: print('Unable to delete:',delete)
		sys.exit()




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

