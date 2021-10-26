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
	_.switches.register( 'Convert-AutoText', '-autotext' )
	_.switches.register( 'Add-Text-Trigger', '-add' )
	_.switches.register( 'Add-Text-Text', '-text' )
	_.switches.register( 'Add-Text-Back', '-back' )
	_.switches.register( 'Add-Text-Note', '-note' )

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
						_.hp('p hotkeys -add ...lines -text "sum(1 for line in open(''))" -back 2 -note python-file-lines'),
						'#      IF YOU DO NOT USE -text when -add it will take from the copied clipboard',
						_.hp('p hotkeys -add ...lines -back 2 -note python-file-lines'),
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

class HOTKEYS:
	def __init__( self ):
		pass

			

	def log_keystroke( self, key ):
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
			# spacer=[]
			for i,t in enumerate(table[k]['test']):
				try:
					if not t.startswith('Key.'):
						count+=1
						# spacer.append(t)
					elif t.startswith('Key.space'):
						# spacer.append(t)
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
				# count-=1
				if ii<count:
					while not ii == count:
						ii+=1
						keyboard.press(Key.backspace)
						keyboard.release(Key.backspace)
				print(k)
				# print(spacer)
				# print(k,table[k]['do'])
				exec(table[k]['do'])
				# log=[]
				break
# class Hotkeys:END


class CLIP:
	def win_path(self):
		_copy = _.regImp( __.appReg, '-copy' )
		_paste = _.regImp( __.appReg, '-paste' )
		data  = _paste.imp.paste()
		if '\\\\' in data:
			data = _str.replaceDuplicate(data,'\\')
		else:
			data = _str.replaceDuplicate(data,'\\')
			data = data.replace('\\','\\\\')
		_copy.imp.copy( data, p=0 )

	def implode(self):
		_paste = _.regImp( __.appReg, '-paste' )
		_copy = _.regImp( __.appReg, '-copy' )
		text = _paste.imp.paste()
		text=_str.replaceDuplicate( text, '\n' )
		text=_str.cleanBE( text, '\n' )
		text=_str.cleanBE( text, '\t' )
		text=_str.cleanBE( text, ' ' )
		text = text.replace('\r','')
		text = text.replace('\n',', ')
		text=_str.replaceDuplicate( text, ' ' )
		_copy.imp.copy( text, p=0 )

	def explode(self):
		_paste = _.regImp( __.appReg, '-paste' )
		_copy = _.regImp( __.appReg, '-copy' )
		text = _paste.imp.paste()
		text=_str.replaceDuplicate( text, ' ' )
		text=_str.cleanBE( text, '\n' )
		text=_str.cleanBE( text, '\t' )
		text=_str.cleanBE( text, ' ' )
		text = text.replace('\r','')
		text = text.replace('\n','')
		text = text.replace(', ',',')
		text = text.replace(',','\n')
		_copy.imp.copy( text, p=0 )



	def del_activate(self):
		Timer( .001, self.del_run ).start()

	def del_run(self):
		global log
		global keyboard
		x='x'
		while not x in '123456789':
			# print('x',x)
			log0=log.copy()
			log0.reverse()
			x=log0[0]
		if x in '123456789':
			keyboard.press(Key.backspace)
			keyboard.release(Key.backspace)
			# print('y',x)
			x=int(x)
			_paste = _.regImp( __.appReg, '-paste' )
			text = _paste.imp.paste()
			_copy = _.regImp( __.appReg, '-copy' )
			newText = []
			for line in text.split('\n'):
				line=_str.replaceDuplicate( line, ' ' )
				line=_str.cleanBE( line, ' ' )
				parts=line.split(' ')
				i=0
				while not i == x:
					i+=1
					parts.pop(0)
				newLine=' '.join(parts)
				newText.append(newLine)
			_copy.imp.copy( '\n'.join(newText), p=0 )

# class CLIP:END

class TYPING:
	def __init__(self):
		pass

	def ty(self,text,back=0):
		global keyboard
		for t in text:
			self.keyboard_typing(t)

		ii=0
		while not ii == back:
			ii+=1
			keyboard.press(Key.left)
			keyboard.release(Key.left)

	def ty_h(self,k,back=0):
		global keyboard
		global hot_text

		text = hot_text[k]['text']
		text = text.replace('\r','')
		for t in text:
			self.keyboard_typing(t)

		ii=0
		while not ii == back:
			ii+=1
			keyboard.press(Key.left)
			keyboard.release(Key.left)
	def ty_a(self,k,back=0):
		global keyboard
		global auto_text

		text = auto_text[k]['text']
		text = text.replace('\r','')
		for t in text:
			self.keyboard_typing(t)


		ii=0
		while not ii == back:
			ii+=1
			keyboard.press(Key.left)
			keyboard.release(Key.left)

	def keyboard_typing(self,t):
		global keyboard
		if t == '\n':
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
		elif t == '\t':
			keyboard.press(Key.tab)
			keyboard.release(Key.tab)
			
			# keyboard.press(Key.space)
			# keyboard.release(Key.space)
			
			# keyboard.press(Key.space)
			# keyboard.release(Key.space)
			
			# keyboard.press(Key.space)
			# keyboard.release(Key.space)
			
			# keyboard.press(Key.space)
			# keyboard.release(Key.space)

		else:
			keyboard.press(t)
			keyboard.release(t)
# class TYPE:END

class LOADER:
	def __init__(self):
		pass

	def autoText(self):
		autxt = _v.dbTables  +_v.slash+ 'AutoText.csv'
		if not os.path.isfile(autxt):
			return None
		try:
			raw = _.getText( autxt, raw=True )
		except Exception as e:
			raw = ''
		if len(raw) < 5:
			return None

		table = {}

		for line in raw.split('\n'):

			c=line.count('%<')
			line = line.replace( '%<', '' )
			if not line == ';':
				if ';' in line:
					f=_.find_all(line,';')
					a=line[0:f[0]]
					b=line[f[0]+1:]
					b = b.replace( '{#crlf#}', '\n' )
					table[a] = {}
					table[a]['text'] = b
					table[a]['back'] = c

		return table

	def flip_table_test(self):
		global table
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

	def add_text(self, add,text,back,note):
		hot_text  = _.getTableDB('hotkeys-Text.dex')
		hot_text[add]={
							'text': text,
							'back': back,
							'note': note,
		}
		_.saveTableDB( hot_text, 'hotkeys-Text.dex' )

	def build_table(self):
		global table
		global hot_text
		global auto_text
		for k in hot_text:
			if len(hot_text[k]['note']):
				table[hot_text[k]['note']] = { 'raw': [ k ], 'do': 'Typing.ty_h("'+k+'",back='+str(hot_text[k]['back'])+')' }
			else:
				table[k] = { 'raw': [ k ], 'do': 'Typing.ty_h("'+k+'",back='+str(hot_text[k]['back'])+')' }

		for k in auto_text:
			table[k] = { 'raw': [ k ], 'do': 'Typing.ty_a("'+k+'",back='+str(auto_text[k]['back'])+')' }
# class LOADER:END

def action():

	if _.switches.isActive('Convert-AutoText'):
		table = Loader.autoText()
		if table:
			_.saveTableDB( table, 'hotkeys-AutoText.dex' )
		return None
	if _.switches.isActive('Add-Text-Trigger'):
		add  = _.switches.value('Add-Text-Trigger')
		text = _.switches.value('Add-Text-Text')
		back = _.switches.value('Add-Text-Back')
		note = _.switches.value('Add-Text-Note')
		if len(back):
			back = int(back)
		else:
			back = 0
		if len(text) < 2:
			_paste = _.regImp( __.appReg, '-paste' )
			text = _paste.imp.paste()
		text = text.replace('\r','')
		Loader.add_text(add,text,back,note)
		return None

	load()
	with Listener(on_press=Hotkeys.log_keystroke) as l:
		l.join()




def load():
	global table
	global auto_text
	global hot_text
	global log
	log = []
	table = {
				'EXIT': { 'raw': [ '22','Key.esc,3' ], 'do': 'sys.exit()' },
				'tester': { 'raw': [ 'Key.ctrl,3', 'test' ], 'do': 'print("works!!")' },
				'win-path': { 'raw': [ 'Key.ctrl,2', 'win' ], 'do': 'Clip.win_path()' },
				'mom': { 'raw': [ 'Key.ctrl,2', 'mom' ], 'do': 'Typing.ty("your_mother()",back=1)' },
				'pre-clean': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'del' ], 'do': 'Clip.del_activate()' },
				'implode': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'imp' ], 'do': 'Clip.implode()' },
				'explode': { 'raw': [ 'Key.ctrl,2', 'Key.space', 'exp' ], 'do': 'Clip.explode()' },
				'reload': { 'raw': [ 'Key.ctrl', 'Key.shift', 'Key.space' ], 'do': 'load()' },

	}
	auto_text = _.getTableDB('hotkeys-AutoText.dex')
	hot_text  = _.getTableDB('hotkeys-Text.dex')
	Loader.build_table()
	Loader.flip_table_test()
	# _.pv(table)

Hotkeys=HOTKEYS()
Typing=TYPING()
Loader=LOADER()
Clip=CLIP()


from threading import Timer

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




