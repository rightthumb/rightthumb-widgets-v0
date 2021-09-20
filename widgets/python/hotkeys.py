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
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Print-Keys', '-print' )

#   finds the file in probable locations
#   and 
#       if  _.autoBackupData = True
#       and __.releaseAcquiredData = True
#           GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#       you can run apps on usb at a clients office
#           when you get home run: p app -loadepoch epoch 
#               backed up
#                   pipe
#                   files
#                   tables
_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs'] 
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'hotkeys.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'hotkeys',
	'categories': [
						'hotkeys',
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
						_.hp('p hotkeys'),
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	# _.switches.trigger( 'Files',_.inRelevantFolder )  
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
#                                                   if platform.system() == 'Windows':
########################################################################################
# START

from pynput.keyboard import Key, Controller
keyboard = Controller()

from pynput.keyboard import Listener

def log_keystroke(key):
	global log
	global table
	global keyboard
	key = str(key).replace("'", "")
	log.append(key)
	if _.switches.isActive('Print-Keys'):
		print(key)
	log0=log.copy()
	log0.reverse()
	
	for k in table:
		good=True
		count=0
		for i,t in enumerate(table[k]['test']):
			try:
				if not t.startswith('Key.'):
					count+=1
				if not log0[i].startswith(t):
					# print(log0[i],t)
					good=False
					break
			except Exception as e:
				good=False
				break
		if good:
			ii=0
			while not ii == count:
				ii+=1
				keyboard.press(Key.backspace)
				keyboard.release(Key.backspace)
			print(k)
			# print(k,table[k]['do'])
			exec(table[k]['do'])
			log=[]
			break


def win_path():
	_copy = _.regImp( __.appReg, '-copy' )
	_paste = _.regImp( __.appReg, '-paste' )
	data  = _paste.imp.paste()
	if '\\\\' in data:
		data = _str.replaceDuplicate(data,'\\')
	else:
		data = _str.replaceDuplicate(data,'\\')
		data = data.replace('\\','\\\\')
	_copy.imp.copy( data, p=0 )

def ty(text,back=0):
	global keyboard
	for t in text:
		keyboard.press(t)
		keyboard.release(t)

	ii=0
	while not ii == back:
		ii+=1
		keyboard.press(Key.left)
		keyboard.release(Key.left)

def action():
	load()
	with Listener(on_press=log_keystroke) as l:
		l.join()

def load():
	global table
	global log
	log = []
	table = {
				'EXIT': { 'raw': [ '22','Key.esc,3' ], 'do': 'sys.exit()' },
				'tester': { 'raw': [ 'Key.ctrl,3', 'test' ], 'do': 'print("works!!")' },
				'win-path': { 'raw': [ 'Key.ctrl,2', 'win' ], 'do': 'win_path()' },
				'mom': { 'raw': [ 'Key.ctrl,2', 'mom' ], 'do': 'ty("your_mother()",back=1)' },

	}
	for k in table:
		table[k]['test']=[]
		for t in table[k]['raw']:
			if t.startswith('Key.') and not ',' in t:
				table[k]['test'].append(t)
			elif t.startswith('Key.') and ',' in t:
				p=t.split(',')
				n=int(p[1])
				i=0
				while not i == n:
					i+=1
					table[k]['test'].append(p[0])
			else:
				for tt in t:
					table[k]['test'].append(tt)
		table[k]['test'].reverse()
		# _.pv(table)





########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




