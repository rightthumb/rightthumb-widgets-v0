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
	### EXAMPLE: START
	_.switches.register( 'Start-Epoch', '-start,-epoch' )
	_.switches.register( 'Wait-For', '-wait', '120' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
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

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
### EXAMPLE: START


	#--> make hotkey ad-description soon:  <--<w#
	#-->    - outer most typed first
	#-->    - blank pipe
	#-->    __.setting('hotkey-clip.ad_description-start1',d=False)
	#--> _________________________________
	#--> describe selection area two
	#--> 3 write a note here wrap text
	#--> two dignissim
	#--> 1 inceptos
	#--> _________________________________
	#--> describe selection area two
	#-->              |           |
	#-->              |           | - write a note here
	#-->              |           |   wrap text
	#-->              |           |
	#-->              |           | - dignissim
	#-->              |
	#-->              | - inceptos

	# if _.switches.isActive('Test'): test(); return None;
	# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
	# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
	#--> a=(1 if True else 0) <--# 
	#--> m=[[row[i] for row in matrix] for i in range(4)]
	# requests=__.imp('requests.post')
	# data=str(requests.post(url,data={}).content,'iso-8859-1')
	# for k in globals(): print(k, eval(k) )


### EXAMPLE: END
########################################################################################
# START
try: import _rightThumb._beep as _beep
except Exception as e: pass
import os

# def process()
def b(path): return os.stat(path).st_size

def action():
	index={}

	for path in _.isData(r=0): index[path] = b(path)
	done=0
	if _.switches.isActive('Start-Epoch'):
		start=float(_.switches.value('Start-Epoch'))
	else:
		start=time.time()
	_.pr('epoch:',start,c='darkcyan')
	_.pr('start:',_.isDate( start, f='fdatea' ),c='cyan')

	if _.switches.isActive('Wait-For'):
		waitFor = int(_.switches.value('Wait-For'))
	else:
		waitFor = 120
	while True:
		_.waiting(waitFor,txt=[ _dir.info(path,f='size'), _dir.info(path,f='bytes'), _._2dates(time.time(),start) ])
		for path in _.isData(r=0):
			by = b(path)
			if by == index[path]:
				_.pr(line=1,c='yellow')
				_.pr('file stopped growing',c='green')
				_.pr(path,c='cyan')
				_beep.mission_impossible()
				done+=1
				if done == len(_.isData()): break
			index[path]=by
		if done == len(_.isData()): break
	end=time.time()
	_.linePrint(c='yellow')
	_.pr('start:',start,c='darkcyan')
	_.pr('end:',end,c='darkcyan')
	_.pr('diff:',  _._2dates(time.time(),start)  ,c='cyan')
	for path in _.isData(r=0):
		_.pr(path)
		_.pr('\tsize:',_dir.info(path,f='size'))


import _rightThumb._dir as _dir


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()