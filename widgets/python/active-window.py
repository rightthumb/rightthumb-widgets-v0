#!/usr/bin/python3

"""Find the currently active window."""
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
from threading import Timer
##################################################

def sw():
	_.switches.register( 'Log', '-log' )
	_.switches.register( 'Stop', '-stop' )
	_.switches.register( 'Start', '-start' )
	pass
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
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
	'file': 'active-window.py',
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
						_.hp('p active-window -file file.txt'),
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


if _.switches.isActive('Stop'): time.sleep(4); sys.exit();
if _.switches.isActive('Start'): time.sleep(4); sys.exit();


import logging
import sys
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
					level=logging.DEBUG,
					stream=sys.stdout)

def get_active_window():
	"""
	Get the currently active window.
	Returns
	-------
	string :
		Name of the currently active window.
	"""
	import sys
	active_window_name = None
	if sys.platform in ['linux', 'linux2']:
		# Alternatives: https://unix.stackexchange.com/q/38867/4784
		try:
			import wnck
		except ImportError:
			logging.info("wnck not installed")
			wnck = None
		if wnck is not None:
			screen = wnck.screen_get_default()
			screen.force_update()
			window = screen.get_active_window()
			if window is not None:
				pid = window.get_pid()
				with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
					active_window_name = f.read()
		else:
			try:
				from gi.repository import Gtk, Wnck # type: ignore
				gi = "Installed"
			except ImportError:
				logging.info("gi.repository not installed")
				gi = None
			if gi is not None:
				Gtk.init([])  # necessary if not using a Gtk.main() loop
				screen = Wnck.Screen.get_default()
				screen.force_update()  # recommended per Wnck documentation
				active_window = screen.get_active_window()
				pid = active_window.get_pid()
				with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
					active_window_name = f.read()
	elif sys.platform in ['Windows', 'win32', 'cygwin']:
		# https://stackoverflow.com/a/608814/562769
		import win32gui # type: ignore
		window = win32gui.GetForegroundWindow()
		active_window_name = win32gui.GetWindowText(window)
	elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
		# https://stackoverflow.com/a/373310/562769
		from AppKit import NSWorkspace # type: ignore
		active_window_name = (NSWorkspace.sharedWorkspace()
							.activeApplication()['NSApplicationName'])
	else:
		print("sys.platform={platform} is unknown. Please report."
			.format(platform=sys.platform))
		print(sys.version)
	return active_window_name
# print("Active window: %s" % str(get_active_window()))


def strip(text):
	text=text.replace('\t',' ')
	result=''
	for ch in text:
		if ch in ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
			result+=ch
		else:
			result+=' '
	return clean(result)

def clean(text):
	while '  ' in text: text=text.replace('  ',' ')
	while text.endswith(' '): text=text[:-1]
	while text.startswith(' '): text=text[1:]
	return text

def action():
	global idle_group
	global idle_time
	global aw
	global fi
	Timer( .1, idle_monitor ).start()
	# return None
	load(); global c3po;
	LOG=_.switches.isActive('Log')
	fi=_.dot()
	# day=_.day(sep='-',e=0)
	day=_.isDate(time.time(),f='date')
	fi.log = 'active-window-'+day+'-log.json'
	fi.index = 'active-window-'+day+'-title.index'
	fi.groups = 'active-window-'+day+'-groups.index'


	

	aw=_.dot()
	aw.log=[]
	aw.index={}
	aw.indexg={}
	aw.idle={}
	aw.idleg={}



	if LOG:
		aw.log=_.getTable(fi.log)
		aw.index=_.getTable(fi.index)
		aw.indexg=_.getTable(fi.groups)
	else:
		_.pr('no logging',c='red')

	aw.aw=''
	aw.group=''
	aw.saved=time.time()
	aw.last=_.dot()
	aw.last.aw=''
	aw.last.group=''
	aw.last.start=0
	aw.last.startg=0
	isStop=False

	
	while __.v.active:
		aw.aw=str(get_active_window()).replace('(LICENSE UPGRADE REQUIRED)','')
		aw.aw=clean(aw.aw)
		if isStop and scan(aw.aw) == 'start': isStop=False;continue;
		elif not isStop and scan(aw.aw) == 'stop': isStop=True
		
		if isStop:
			time.sleep(.2)
			continue

		if '(documents) - Sublime Text' in aw.aw:
			aw.aw=aw.aw.replace('(documents) - Sublime Text','')
			while not aw.aw[-1] == strip(aw.aw[-1]): aw.aw=aw.aw[:-1]
			aw.aw+=' - Sublime Text'
		# aw.aw=clean(aw.aw)
		
		z=False
		if not ' - ' in aw.aw:
			if aw.aw == 'local': z=True
			elif aw.aw.startswith('admin'): z=True
			elif aw.aw.startswith('scott'): z=True
			elif aw.aw.startswith('root'): z=True
		if z:
			aw.aw=strip(aw.aw)
			if not aw.aw == 'local':
				aw.aw=aw.aw.replace(' ','@')
			# if len(aw.aw.split(' ')) == 1: 
			
			aw.group=aw.aw
		elif not ' - ' in aw.aw:
			aw.group=aw.aw
		else:
			_gr=aw.aw.split(' - ')
			z=False
			if _gr[0] == 'local': z=True
			elif _gr[0].startswith('admin'): z=True
			elif _gr[0].startswith('scott'): z=True
			elif _gr[0].startswith('root'): z=True
			if z:
				aw.aw=strip(aw.aw)
				aw.group=strip(_gr[0])
			else:
				aw.group=_gr[-1]
		if not aw.group in aw.indexg: aw.indexg[aw.group]=0
		if not aw.aw in aw.index: aw.index[aw.aw]=0
		
		if not aw.aw in aw.idle: aw.idle[aw.aw]={}
		if not aw.group in aw.idleg: aw.idleg[aw.group]={}
		if not aw.group == aw.last.group:
			if aw.last.startg>0:
				end=time.time()
				diff=end-aw.last.startg
				aw.indexg[aw.group]+=diff
			aw.last.startg=time.time()
			aw.last.group=aw.group
		if not aw.aw == aw.last.aw:
			_.pr()
			if aw.last.start>0:
				end=time.time()
				diff=end-aw.last.start
				aw.index[aw.aw]+=diff
				

				fo={
						'g': aw.group,
						'w': aw.aw,
				}
				if fo['g'] == fo['w']: del fo['g']
				if 'g' in fo and fo['g']+' - ' in fo['w']: fo['w']=fo['w'].replace(fo['g']+' - ','')
				if 'g' in fo and ' - '+fo['g'] in fo['w']: fo['w']=fo['w'].replace(' - '+fo['g'],'')

				rec={
						'group': aw.group,
						'label': fo['w'],
						'window': aw.aw,
						'start': aw.last.start,
						'end': end,
						'diff': diff,
						'w-total': aw.index[aw.aw],
						'g-total': aw.indexg[aw.group],
					}
				if diff < 60:
					aw.log.append(rec)
					if LOG and time.time()-aw.saved > 300:
						day=_.isDate(time.time(),f='date')
						if not fi.log == 'active-window-'+day+'-log.json':
							_.saveTable(aw.log,fi.log,p=0)
							_.saveTable(aw.index,fi.index,p=0)
							_.saveTable(aw.indexg,fi.groups,p=0)
							aw.log=[]
							aw.index={}
							aw.indexg={}
							aw.idle={}
							aw.idleg={}
							continue
						fi.log = 'active-window-'+day+'-log.json'
						fi.index = 'active-window-'+day+'-title.index'
						fi.groups = 'active-window-'+day+'-groups.index'
						_.saveTable(aw.log,fi.log,p=0)
						_.saveTable(aw.index,fi.index,p=0)
						_.saveTable(aw.indexg,fi.groups,p=0)
						_.pr()
						_.pr(fi.log,c='green')
						_.pr(fi.index,c='green')
						_.pr(fi.groups,c='green')
						_.pr()
			aw.last.aw=aw.aw
			aw.last.start=time.time()
			# print(_._2dates(aw.last.start),"Active: %s" % aw.aw)
		active=(aw.index[aw.aw]+(time.time()-aw.last.start))
		activeg=(aw.indexg[aw.group]+(time.time()-aw.last.startg))
		guess=time.time()-active
		# _.pr(_._2dates(aw.last.start),aw.aw,end=1)
		a=round(active,2)
		b=round(activeg,2)
		if not a == b:
			fo={
					'g': aw.group,
					'at': a,
					'gt': b,
					'df': _._2dates(guess),
					'w': aw.aw,
			}
			if fo['g'] == fo['w']: del fo['g']
			if 'g' in fo and fo['g']+' - ' in fo['w']: fo['w']=fo['w'].replace(fo['g']+' - ','')
			if 'g' in fo and ' - '+fo['g'] in fo['w']: fo['w']=fo['w'].replace(' - '+fo['g'],'')
			txt=str(fo).replace('"','').replace("'",'').replace(',','   ').replace('}','').replace('{','')
			_.pr(txt,end=1)
			# _.pr(a,'-',b,'-',_._2dates(guess),aw.aw,end=1)
		else:
			fo={
					'g': aw.group,
					'at': a,
					'gt': '-',
					'df': _._2dates(guess),
					'w': aw.aw,
			}
			if fo['g'] == fo['w']: del fo['g']
			if 'g' in fo and fo['g']+' - ' in fo['w']: fo['w']=fo['w'].replace(fo['g']+' - ','')
			if 'g' in fo and ' - '+fo['g'] in fo['w']: fo['w']=fo['w'].replace(' - '+fo['g'],'')
			txt=str(fo).replace('"','').replace("'",'').replace(',','   ').replace('}','').replace('{','')
			_.pr(txt,end=1)
			# _.pr(a,'-',_._2dates(guess),aw.aw,'-',aw.group,end=1)
		time.sleep(.2)
		if idle_time > 600:
			if not aw.aw in aw.idle: aw.idle[aw.aw] ={}
			if not idle_group in aw.idle[aw.aw]: aw.idle[aw.aw][idle_group]=idle_time
			else: aw.idle[aw.aw][idle_group]+=idle_time-aw.idle[aw.aw][idle_group]
			if not idle_group in aw.idleg[aw.group]: aw.idleg[aw.group][idle_group]=idle_time
			else: aw.idleg[aw.group][idle_group]+=idle_time-aw.idleg[aw.group][idle_group]

	# aw.idleg[aw.group]
	# aw.idleg[aw.group]
	# global idle_group
	# global idle_time

def scan(win):
	if ' active-window -stop' in win: return 'stop'
	if ' active-window -start' in win: return 'start'
	return ''


idle_group=0
idle_time=0
def idle_monitor():
	# print('idle_monitor')
	# print('idle_monitor')
	# print('idle_monitor')
	# print('idle_monitor')
	global idle_group
	global idle_time



	from ctypes import Structure, windll, c_uint, sizeof, byref
	import time
	import winsound
	# http://stackoverflow.com/questions/911856/detecting-idle-time-in-python
	class LASTINPUTINFO(Structure):
		_fields_ = [
			('cbSize', c_uint),
			('dwTime', c_uint),
		]

	def get_idle_duration():
		lastInputInfo = LASTINPUTINFO()
		lastInputInfo.cbSize = sizeof(lastInputInfo)
		windll.user32.GetLastInputInfo(byref(lastInputInfo))
		millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
		return millis / 1000.0
	last=0
	while __.v.active:
		GetLastInputInfo = int(get_idle_duration())
		# print(GetLastInputInfo)
		if last and not GetLastInputInfo : idle_group+=1
		idle_time=GetLastInputInfo
		last=GetLastInputInfo
		time.sleep(1)















	# while 1:
	#     GetLastInputInfo = int(get_idle_duration())
	#     print(GetLastInputInfo)
	#     time.sleep(1)



	#     if GetLastInputInfo == 480:
	#         # if GetLastInputInfo is 8 minutes, play a sound
	#         sound = r"c:\windows\media\notify.wav"
	#         winsound.PlaySound(sound, winsound.SND_FILENAME)
	#     if GetLastInputInfo == 560:
	#         # if GetLastInputInfo is 9 minutes, play a more annoying sound
	#         sound = r"c:\windows\media\ringout.wav"
	#         winsound.PlaySound(sound, winsound.SND_FILENAME)
	#         winsound.PlaySound(sound, winsound.SND_FILENAME)
	#         winsound.PlaySound(sound, winsound.SND_FILENAME)


# idle time monitor
# idle time monitor
# idle time monitor
# idle time monitor
from ctypes import Structure, windll, c_uint, sizeof, byref

# # http://stackoverflow.com/questions/911856/detecting-idle-time-in-python
class LASTINPUTINFO(Structure):
	_fields_ = [
		('cbSize', c_uint),
		('dwTime', c_uint),
	]

def get_idle_duration():
	lastInputInfo = LASTINPUTINFO()
	lastInputInfo.cbSize = sizeof(lastInputInfo)
	windll.user32.GetLastInputInfo(byref(lastInputInfo))
	millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
	return millis / 1000.0

def load():
	global c3po
	c3po = _.getTable( 'active_window.json' )
	#n)--> print table
	_.pt(c3po)



__.v.active = True
import signal
import sys
import time

def sigint_handler(signal, frame):
	global aw
	global fi
	__.v.active = False
	print()
	_.pr('Closing...',end=1)
	time.sleep(1)
	_.pr('               ',end=1)
	if _.switches.isActive('Log'):
		_.pr('Saved',c='green')
		_.saveTable(aw.log,fi.log,p=0)
		_.saveTable(aw.index,fi.index,p=0)
		_.saveTable(aw.indexg,fi.groups,p=0)
	sys.exit()

signal.signal(signal.SIGINT, sigint_handler)




##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)