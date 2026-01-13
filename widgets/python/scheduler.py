import sys, time
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
	pass
	_.switches.register( 'NoBeep', '-nobeep' )
	_.switches.register( 'List', '-list' )
	_.switches.register( 'DaysOfWeek', '-dow,-day,-days', 'mon tue wed thu fri sat sun' )
	_.switches.register( 'Delete', '-del' )
	_.switches.register( 'Every', '-e,-every', 'day hour min sec OR d h m s' )
	_.switches.register( 'Python', '-py', 'autoBackup' )
	_.switches.register( 'Arguments', '-args' '-ago 1d  (USE THIS SWITCH LAST)' )
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	'file': 'scheduler.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Added to always running hotkeys.py to schedule tasks',
	'categories': [
						'scheduler',
						'',
				],
	'usage': [
	],
	'relatedapps': [
	],
	'prerequisite': [
	],
	'examples': [
						_.hp('p scheduler -py ephemeral--job-test -e m 2 '),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [
	],
	'notes': [
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
#n)--> start


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
########################################################################################

if __name__ == '__main__':
	action()
	_.isExit(__file__)