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
	_.switches.register( 'Beep-Minute', '-beep,-m,-min,-mins', '2' )
	_.switches.register( 'Session-Timer', '-cmd,-ss,-session' )
	_.switches.register( 'Add-Hours', '+hr', '.25' )
	_.switches.register( 'Add-Min', '+min', '15' )
	_.switches.register( 'Minus-Hours', '-hr', '.25' )
	_.switches.register( 'Minus-Min', '-min', '15' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
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
	'file': 'beeps.py',
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
						_.hp('p terminal-timer -file file.txt'),
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
#n)--> start

def timer(total=0):
	if _.switches.isActive('Session-Timer') and _.isWin:
		start = _v.cmdGetVar('timestamp_start')
		epoch = _.autoDate(start)
		dic = _.isDate(epoch,f='ago-dic')
		dic2={}
		for k in dic:
			if not k == 's':
				if not dic[k] == 0:
					if k == 'mi': dic2['m']=dic[k]
					else: dic2[k]=dic[k]
		return dic2
	return total
	print(start)
	print(epoch)
	print(dic2)
	sys.exit()

def run(mins=2):
	tt = 'total'
	if _.switches.isActive('Session-Timer'): tt = 'session-total'
	timer()
	total=0
	while True:
		_beep.play_note(3, "c", "half")
		m=0
		s=0
		done=False
		while not done:
			time.sleep(1)
			s+=1
			if s%60 == 0:
				s=0
				m+=1
				total+=1
				if m == mins:
					done=True
			to=timer(total)
			t={ tt: to, '| beep':mins,'m': m, 's':s }
			_.pr('\t',t,dic=5,end=1)

os=__.imp('os.sep')

def action():

	if _.isData():
		for path in _.isData():
			if not os.path.isfile(path):
				path = _v.ticketPath(path)
			if not os.path.isfile(path):
				_.pr('path error',c='red')
				sys.exit()
			path=__.path(path)
			print(path)
		return None


	if _.switches.isActive('Add-Hours') and _.switches.value('Add-Hours'):
		ti = float(_.switches.value('Add-Hours')) * 60 * 60
		epoch = _.autoDate(_v.cmdGetVar('timestamp_start'))
		epoch -= ti; new = _.isDate(epoch,f='cmd'); print(new);
		return None
	if _.switches.isActive('Add-Min') and _.switches.value('Add-Min'):
		ti = float(_.switches.value('Add-Min')) * 60
		epoch = _.autoDate(_v.cmdGetVar('timestamp_start'))
		epoch -= ti; new = _.isDate(epoch,f='cmd'); print(new);
		return None

	if _.switches.isActive('Minus-Hours') and _.switches.value('Minus-Hours'):
		ti = float(_.switches.value('Minus-Hours')) * 60 * 60
		epoch = _.autoDate(_v.cmdGetVar('timestamp_start'))
		epoch += ti; new = _.isDate(epoch,f='cmd'); print(new);
		return None
	if _.switches.isActive('Minus-Min') and _.switches.value('Minus-Min'):
		ti = float(_.switches.value('Minus-Min')) * 60
		epoch = _.autoDate(_v.cmdGetVar('timestamp_start'))
		epoch += ti; new = _.isDate(epoch,f='cmd'); print(new);
		return None


	mins=2
	if _.switches.isActive('Beep-Minute'):
		mins=int(_.switches.value('Beep-Minute'))
	run(mins)
	# try: run(mins)
	# except KeyboardInterrupt:
	#     sys.exit()
# cmdGetVar
import signal
import sys

def sigint_handler(signal, frame):
	# time.sleep(2)
	# _.pr('                                                          ',end=1)
	# _.pr('p beeps -session',end=1)
	# time.sleep(3)
	_.pr('                                                          ',end=1)
	sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
import _rightThumb._beep as _beep
##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
