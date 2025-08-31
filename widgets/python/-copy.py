#!/usr/bin/python3

dirty=False
dirty=True
returns=0

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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
	_.switches.register( 'Copy-String', '-cp,-string,-text,-txt,-str,-this' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'NoPrint', '-noprint,--c' )
	_.switches.register( 'Subject', '-j,-subject' )
	_.switches.register( 'Specific', '-specific' )
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Get', '-get' )
	_.switches.register( 'Nano', '-nano' )
	_.switches.register( 'Lines', '-l,-line,-lines' )
	_.switches.register( 'NoClean', '-noclean' )
	_.switches.register( 'Add-Return', '-r,-return,-returns' )
	_.switches.register( 'CleanPipe', '-cl' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '-copy.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'copy',
	'spaces': 'KEEP-QUOTES',
	'categories': [
						'copy',
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
						'pp franchises-old | p line -make "p franchise -l 2 -f {} " --c | p -copy',
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

__.hasPipeData = False


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
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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



_.postLoad( __file__ )
if __name__ == '__main__':
	if not sys.stdin.isatty():
		__.hasPipeData = True
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=_.switches.isActive('CleanPipe') )
		# print(888);sys.exit();
# appData[theFocus]['pipe']
if _.switches.isActive('CleanPipe'):
	_.pipeCleaner(0)
########################################################################################
# START

# _.switches.fieldSet( 'NoPrint', 'active', True )


def formatData( result ):
	try:
		result = str(result,'utf-8')
	except Exception as e:
		try:
			result = str(result,'iso-8859-1')
		except Exception as e:
			result = result.encode('utf-8')
	return result

def clip_set_0(data,end=''):
	global win32clipboard
	if win32clipboard is None:
		import win32clipboard
	# set clipboard data
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	try:
		win32clipboard.SetClipboardText( cleanString(data)+end )
	except Exception as e:
		win32clipboard.EmptyClipboard()
		_.colorThis(  [ 'Unable to set clipboard data' ], 'red'  )
	win32clipboard.CloseClipboard()


def clip_set_2(data,end='',clean=False):
	
	if clean:
		pyperclip.copy( cleanString(data)+end )
	else:
		pyperclip.copy( data+end )

def clip_set_3(data,end='',clean=False):
	import subprocess
	if _.isWin:
		if not _.switches.isActive('NoPrint'):
			if _.isWin:
				_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	if clean:
		_.saveText( cleanString(data)+end, tmpA )
	else:
		_.saveText( data+end, tmpA )
	time.sleep(.3)
	# print(tmpA)
	if not os.path.isfile(tmpA):
		if not _.switches.isActive('NoPrint'):
			_.pr( 'no file' )
		return None
	if __.UnixCopy == 'xsel':
		cmd = ["cat", tmpA, "|",  "xsel", "--clipboard", "--input"  ]
	else:
		cmd = ["cat", tmpA, "|",  "pbcopy"  ]
	mycmd=subprocess.getoutput( ' '.join(cmd) )
	test = clip_get_3()
	if not data in test:

		try:
			cmd = ["xsel", "--clipboard"]

			with open(tmpA, 'r') as file:
				p = subprocess.Popen(cmd, stdin=file, stdout=subprocess.PIPE)
			# cmd = ["xsel", "--clipboard",  "<", tmpA ]
			# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
			return data+end
		except Exception as e:
			print(e)
	# try:
	# 	from subprocess import Popen, PIPE
	# 	p = Popen(['xsel','-pi'], stdin=PIPE)
	# 	p.communicate(input= formatData(data) )

	# 	p = Popen(['xsel', '-bi'], stdin=PIPE)
	# 	p.communicate(input= formatData(data) )
	# 	# p.communicate(input=data)
	# except Exception as e:
	# 	pass


	result = None
	try:
		result = clip_get_3()
	except Exception as e:
		result = None

	if not result:
		# _.pr( ' '.join(cmd) )
		if not _.switches.isActive('NoPrint'):
			if _.isWin:
				_.cp( 'Error: unable to copy', 'red' )
			_.pr(data)

	# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

	# p1 = subprocess.Popen(["cat", tmpA], stdout=subprocess.PIPE)
	# p2 = subprocess.Popen(["xsel", "--clipboard", "--input"], stdin=p1.stdout, stdout=subprocess.PIPE)
	# p2.communicate()


	time.sleep(.2)
	if os.path.isfile(tmpA):
		return _.getText( tmpA, raw=True, clean=2 )
	return None


def clip_set_1(data,end='',clean=False):
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	if clean:
		r.clipboard_append( cleanString(data)+end )
	else:
		r.clipboard_append( data+end )
	# r.destroy()

def clip_set( data, end='', p=True, clean=False ):
	data=str(data)
	data = _.stripColor(data)
	# print(data,99);sys.exit();
	if not _.switches.isActive('NoPrint'):
		if p:
			_.pr(data)

	# clip_set_3(data)
	try:
		if platform.system() == 'Linux':
			try:
				clip_set_3(data,end,clean)
			except:
				clip_set_2(data,end,clean)
		else:
			clip_set_2(data,end,clean)
	except Exception as e:
		try:
			clip_set_2(data,end,clean)
		except Exception as e:
			try:
				clip_set_1(data,end,clean)
			except Exception as e:
				if not _.switches.isActive('NoPrint'):
					if _.isWin:
						_.cp( 'Error: clipboard error', 'red' )
				sys.exit()


def clip_get(p=False):
	result = 'error'
	try:
		if platform.system() == 'Linux':
			try:
				result = cleanString(clip_get_3())
			except: 
				result = cleanString(clip_get_2())
		else:
			result = cleanString(clip_get_2())
	except Exception as e:
		if not _.switches.isActive('NoPrint'):
			_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		try:
			result = cleanString(clip_get_1())
		except Exception as e:
			try:
				result = cleanString(clip_get_3())
			except Exception as e:
				if not _.switches.isActive('NoPrint'):
					if _.isWin:
						_.cp( 'Error: clipboard error', 'red' )
						_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )

	if not result:
		if not _.switches.isActive('NoPrint'):
			if _.isWin:
				_.cp( 'Error: clipboard error', 'red' )
				_.cp( '\tpython3 -m pip install pyperclip', 'yellow' )
		sys.exit()
	else:
		if p:
			_.pr(result)
	# _.pr( result )
	# sys.exit()
	return result


def clip_get_1():
	from tkinter import Tk
	r = Tk()
	r.withdraw()
	r.clipboard_clear()
	return r.clipboard_get()


def clip_get_3():
	import subprocess
	# _.pr('_.isWin:',_.isWin)
	if _.isWin:
		_.cp( 'Error: clipboard error', 'red' )
		return None

	tmpA = _v.stmp +_v.slash+ 'cryptString-A.txt'
	tmpB = _v.stmp +_v.slash+ 'cryptString-B.txt'
	if os.path.isfile(tmpA):
		os.unlink(tmpA)
	if os.path.isfile(tmpB):
		os.unlink(tmpB)
	if not _.which('xsel'):
		if not _.isWin:
			_.pr( '\tsudo apt install xclip xsel' )
			return None

	cmd = ["xsel", "--clipboard", "--output"]

	with open(tmpA, 'w') as file:
		p = subprocess.Popen(cmd, stdout=file)

	# cmd = ["xsel", "--clipboard", "--output", ">", tmpA ]
	# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	time.sleep(.3)
	# print(p)
	# cmd = ["xsel", "--clipboard", "--output"]
	# with open(tmpA, 'w') as file: p = subprocess.Popen(cmd, stdout=file)
	# _.pr( ' '.join(cmd) )
	# print(tmpA)
	if os.path.isfile(tmpA):
		text = _.getText2( tmpA, 'text' )
		if text == None: text = 'err'
		lines = text.split('\n')
		lines.reverse()
		if 'No newline at end of selection' in lines[0]: lines.pop(0)
		lines.reverse()
		text = '\n'.join(lines)
		# print(text)
		return text
	return 'err'

def clip_get_2():
	# import pyperclip
	return cleanString( pyperclip.paste() )

	# global win32clipboard
	# if win32clipboard is None:
	#   import win32clipboard
	# # get clipboard data
	# win32clipboard.OpenClipboard()
	# data = win32clipboard.GetClipboardData()
	# win32clipboard.CloseClipboard()
	# return data

win32clipboard = None
import platform
def cleanString(data):
	data=data.replace('\r','')
	data=data.rstrip()
	while '\r' in data:  data=data.replace('\r','')
	while ' \n' in data:  data=data.replace(' \n','\n')
	while '\t\n' in data: data=data.replace('\t\n','\n')
	global dirty
	if dirty: return data
	global returns
	if returns:
		n=''
		i=0
		while not i == returns:  i+=1; n+='\n';
		if not data.endswith(n): data+=n
		return data

	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	data = cleanStringA(data)
	return data

def cleanStringA(data):
	data = _str.cleanBE(data,_v.default_powershell)
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\n')
	data = _str.cleanBE(data,'\r')
	data = _str.cleanBE(data,'\t')
	data = _str.cleanBE(data,' ')
	return data

copy=clip_set
paste=clip_get

win32clipboard = None


def subject():
		
		subject = {}
		subject['py'] = {}
		subject['py']['micro'] = '''#!/usr/bin/python3
import os, sys
if sys.platform[0] == 'w': _rt = os.getenv('USERPROFILE') + os.sep + '.rt' + os.sep
else: _rt = os.getenv('HOME') + os.sep + '.rt' + os.sep
app = _rt + 'micro.py'
try:
    with open(app, 'r') as file: exec(file.read())
except FileNotFoundError:
    print(f"{app} not found")
except Exception as e:
    print(f"An error occurred while executing {app}: {str(e)}")
'''
		
		subject['b'] = {}
		subject['base'] = {}
		subject['base']['micro'] = '''
import os,sys
if sys.platform[0] == 'w': _rt=os.getenv('USERPROFILE') +os.sep+'.rt'
else: _rt=os.getenv('HOME') +os.sep+'.rt'

sys.path.append(_rt); import micro; exec(micro.loader);

'''
		subject['b']['m'] = subject['base']['micro']
		subject['base']['import'] = '''
#!/usr/bin/python3
import os,sys,time,importlib,simplejson
if sys.platform[0] == 'w': figpath=os.getenv('USERPROFILE') +os.sep+'.rt'+os.sep+ '.config.hash'
else: figpath=os.getenv('HOME') +os.sep+'.rt'+os.sep+ '.config.hash'


def getTable( file ):
		json_data={}
		if os.path.isfile(file):
				with open(file,'r', encoding="latin-1") as json_file: json_data = simplejson.load(json_file)
		return json_data


fig=getTable(figpath)
sys.path.append( fig['w']+'/widgets/python'.replace('/',os.sep) )
import _rightThumb._construct as __
import _rightThumb._vars as _v
__.appReg = __.clearFocus( '__main__', 'D:\\\\tech\\\\hosts\\\\VULCAN\\\\widgets\\\\python\\\\testing123.py' )
f = __.appName( __.appReg, '', '' )
__.registeredApps.append( __.appReg )
import _rightThumb._matrix as _matrix
import _rightThumb._base3 as _
_.load()
import _rightThumb._base4 as ___
import _rightThumb._string as _str
import _rightThumb._dir as _dir

_.appInfo[__.appReg] = {"file": "testing123.py", "liveAppName": "testing123", "description": "Changes the world", "categories": [""], "usage": [], "relatedapps": [], "prerequisite": [], "examples": [""], "columns": [], "aliases": [], "notes": []}
_.appData[__.appReg] = {"start": __.startTime, "uuid": "", "audit": [], "pipe": False, "data": {"field": {"sent": [], "received": []}, "table": {"sent": [], "received": []}}}

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
_.defaultScriptTriggers()
_.switches.process()
_.argvProcess = True
_.postLoad( 'D:\\\\tech\\\\hosts\\\\VULCAN\\\\widgets\\\\python\\\\testing123.py' )

# fileBackup = _.regImp( __.appReg, 'fileBackup' )
# fileBackup.switch( 'Silent,isRunOnce,DoNotSchedule,Flag', 'dirty' )
# fileBackup.switch( 'Input',  _.f('appData',2)  )
# fileBackup.action()

# imp = importlib.import_module(app)
# _.wrapText(  ' '.join(  _.files(  _.back()  )  )  )
# _.f()
# _.f('secure',1)
# _.f('appData',2)
# _.f(p=1)
# _.printVarSimple(  _dir.info(  _.f( 'secure', r=1 )  )  )
# os.system('cls')
# _.pr( str( '\\n'.join( dir(_v) )  ) )


		'''
		# subject['base']['import'] = subject['base']['import'].replace( '__name__', '"__null__"' )
		# subject['base']['import'] = subject['base']['import'].replace( '__file__', '"'+_v.py+_v.slash+'null.py'+'"' )
		subject['base']['import'] = subject['base']['import'].replace( '\t', '    ' )
		# subject['base']['import'] = subject['base']['import'].replace( '\n', '; ' )
		# subject['base']['import'] = _str.cleanBE(  subject['base']['import']  , ';' )
		# subject['base']['import'] = _str.cleanBE(  subject['base']['import']  , ' ' )
		# subject['base']['import'] = _str.cleanBE(  subject['base']['import']  , ';' )
		# subject['base']['import'] = _str.cleanBE(  subject['base']['import']  , ' ' )
		# subject['base']['import'] = _str.cleanBE(  subject['base']['import']  , ';' )

		# new = []
		# for line in subject['base']['import'].split('\n'):
		#   test = _str.cleanBE(line,'\t')
		#   test = _str.cleanBE(line,' ')
		#   test = _str.cleanBE(line,'\t')
		#   test = _str.cleanBE(line,' ')
		#   if not test.startswith('#') and len(test):
		#     new.append( line )
		# subject['base']['import'] = '\n'.join(new)
		# subject['base']['import'] = subject['base']['import'].replace('\r','\n')



		subject['dir'] = {}
		subject['dir']['import'] = subject['base']['import']

		subject['matrix'] = {}
		subject['matrix']['import'] = subject['base']['import']
		
		subject['hacks'] = {}
		subject['code'] = {}

		subject['code']['fn']='''
 b py                                
 p ls -ago 5d c -long -c p --c > %tmpf%
cat %tmpf% | p line --c -make "p inFunc -f {} | + clean" | p execute 
'''


		subject['hacks']['murray2']='''
_the_i_=500;
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		_the_i_++; tag.src = 'https://www.fillmurray.com/500/'+_the_i_;
});
'''
		subject['hacks']['img']='''
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		tag.src = 'https://img.sds.sh/'+tag.getAttribute('width')+'/'+tag.getAttribute('height')+'/';
});
'''
		subject['hacks']['murray']='''
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		tag.src = 'https://www.fillmurray.com/'+tag.getAttribute('width')+'/'+tag.getAttribute('height')+'/';
});
'''
		subject['hacks']['steven2']='''
_the_i_=500;
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		_the_i_++; tag.src = 'https://www.stevensegallery.com/500/'+_the_i_;
});
'''
		subject['hacks']['steven']='''
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		tag.src = 'https://www.stevensegallery.com/'+tag.getAttribute('width')+'/'+tag.getAttribute('height')+'/';
});
'''

		subject['hacks']['cage2']='''
_the_i_=500;
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		_the_i_++; tag.src = 'https://www.placecage.com/500/'+_the_i_;
});
'''

		subject['hacks']['cage']='''
Array.prototype.slice.call(
	document.querySelectorAll('img')).map(function(tag){
		tag.src = 'https://www.placecage.com/'+tag.getAttribute('width')+'/'+tag.getAttribute('height')+'/';
});
'''

		subject['hacks']['cage33']='''
	cat settings.json | p -copy
	p -paste | p pipe-dics -sort keys command
'''


		subject['hacks']['rotate']='''
Array.prototype.slice.call(
	document.querySelectorAll(
		'div,p,span,img,a,body')).map(function(tag){
		tag.style['transform'] = 'rotate(' + (
		Math.floor(Math.random() * 3) - 1) + 'deg)';
});
'''



		subject['tools'] = {}
		subject['tools']['ssh'] = _v.config().cloud.ssh.password
		subject['tools']['vps'] = 'O8zLx1LUTOS1r+htI/XklVfXa4Fseeqkf/8PGhHbjVqQQa1SX7Rf1A=='
		subject['tools']['vps.scott'] = 'wuhx2MkyByouOQWCoKfuJQ=='
		subject['tools']['vps.scott.desktop'] = 'ssh -L 59000:localhost:5901 -C -N -l scott vps.rightthumb.com'
		subject['tools']['vps.scott.desktop.ssh'] = 'ssh -L 59000:localhost:5901 -C -N -l scott vps.rightthumb.com'
		subject['tools']['vps.scott.desktop.id'] = 'localhost:59000'
		subject['tools']['vps.scott.desktop.login'] = '+JB6DdFB+ZcRaCKxB7NwxFYQhWkJyohLCQZMiE/drv2QQa1SX7Rf1A=='
		subject['tools']['vps.tmp'] = '8rOB/r5hfQ5SUzT6uSBZSw=='
		subject['tools']['reph.ssh'] = 'ssh thisreph@reph.us'
		subject['tools']['reph.l'] = 'E4ws935YMwJtLEv5rr29Tg=='
		
		subject['js'] = {}
		subject['js']['q'] = "document.querySelectorAll('')"
		subject['js']['get'] = '''
var get = (url, callback = null) => {
    var asyncStatus = callback !== null;
    var request = new XMLHttpRequest();
    request.open('GET', url, asyncStatus);
    request.send(null);
    var contentType = request.getResponseHeader('Content-Type');
    if (request.status === 200) {
        var response = contentType && contentType.includes('application/json') ? JSON.parse(request.responseText) : request.responseText;
        if (typeof callback === 'function') {
            callback(response);
        }
        return response;
    } else {
        throw new Error('Request failed with status ' + request.status);
    }
}
'''.strip()
		subject['js']['qq'] = """$ = document.querySelectorAll.bind(document);
$('td').forEach(div => div.style.background = 'orange');
"""


		a = 'base'
		b = 'import'
		if len( _.switches.values('Subject') ) > 0:
			a = _.switches.values('Subject')[0]
		if len( _.switches.values('Subject') ) > 1:
			b = _.switches.values('Subject')[1]

		

		subject = autoText( subject )


		if a == 'tools' or a == 'js':
			_.v.end = ''
		elif a == 'base' or a == 'matrix':
		
			_.v.end = '\n\n'


		if not a in subject or not len( _.switches.values('Subject') ) > 0:
			if not _.switches.isActive('NoPrint'):
				if _.isWin:
					_.cp(  'Error: a, expected', 'red'  )
			c = []
			d = []
			for w in subject:
				if type(subject[w]) == str:
					d.append(w)
				else:
					c.append(w)
			if not _.switches.isActive('NoPrint'):
				_.cp(   _.autoWrapText(  ' '.join( c )  ,  __.terminal.width-10, txt=True, prefix='    ', breakOn=' ' )   , 'cyan'  )
				_.cp(   _.autoWrapText(  ' '.join( d )  ,  __.terminal.width-10, txt=True, prefix='    ', breakOn=' ' )   , 'darkcyan'  )
			return None

		if type(subject[a]) == str:
			# _.pr( subject[a] )
			return subject[a]

		if not b in subject[a] or not len( _.switches.values('Subject') ) > 1:
			if not _.switches.isActive('NoPrint'):
				if _.isWin:
					_.cp(  'Error: b, expected', 'red'  )
					_.cp(   _.autoWrapText(  ' '.join( list(subject[a].keys()) )  ,  __.terminal.width-10, txt=True, prefix='    ', breakOn=' ' )   , 'cyan'  )
			return None


		return subject[a][b]



def autoText( data ):
	table = {}
	for k in data:
		table[k] = data[k]
	autxt = _v.dbTables  +_v.slash+ 'AutoText.csv'
	if not os.path.isfile(autxt):
		return table
	try:
		raw = _.getText( autxt, raw=True )
	except Exception as e:
		raw = ''
	if len(raw) < 5:
		return table


	for line in raw.split('\n'):

		c=line.count('%<')
		line = line.replace( '%<', '' )
		if not line == ';':
			if ';' in line:
				f=_.find_all(line,';')
				a=line[0:f[0]]
				b=line[f[0]+1:]
				b = b.replace( '{#crlf#}', '\n' )
				# table[a] = {}
				# table[a]['text'] = b
				# table[a]['back'] = c
				table[a] = b

	return table


def action():
	global returns
	if _.switches.isActive('Add-Return'):
		returns=1
		if len(_.switches.values('Add-Return')): returns=int(_.switches.value('Add-Return'))


	# print('aaa')
	if _.switches.isActive('Copy-String'):
		# print('bbb')
		data = ' '.join( _.switches.values('Copy-String') )
		clip_set(data,p=1)
		return None
	# print('ccc')

	if __.hasPipeData:
		# print('pipe')
		# _.pr('|')
		# _.pr(input())
		# _.pr('|')
		# _.pr(sys.stdin)
		# _.pr('|')
		# _.pr(sys.stdin.readlines())
		# _.pr('|')
		# _.pr( _.appData[focus()]['pipe'] )
		# _.pr('|')
		# _.pr(_.isData())
		# _.pr('|')
		data = '\n'.join( _.isData() )
		# _.pr('|')
		# _.pr(data)
		# _.pr('|')
		clip_set(data,p=1)
		# _.pr('|')
		return None
		
	_.v.end = ''
	

	if _.switches.isActive('Save'):
		data = cleanString(clip_get())
		_.saveText( data, '-copy-transfer.txt' )
		return None
	if _.switches.isActive('Get'):
		data = cleanString( _.getText(_v.myTables+_v.slash+'-copy-transfer.txt',raw=True) )
		clip_set( data, _.v.end )
		return None
	if _.switches.isActive('Nano'):
		os.system( 'nano "'+  _v.myTables+_v.slash+'-copy-transfer.txt'   +'"' )
		return None

	# autoText()
	# return None

	if not _.switches.isActive('Subject') and not _.switches.isActive('Specific'):

		data = '\n'.join( _.isData(r=0) )
		if _.switches.isActive('Lines'):
			data2 = ''
			lines = _.switches.values('Lines')
			for i,line in enumerate( _.isData(r=0) ):
				if str(i) in lines:
					data2 += line + '\n'
			data = data2




	elif _.switches.isActive('Specific'):
		data = ' '.join( _.switches.values('Specific') )

	elif _.switches.isActive('Subject'):
		# end='\n\n'
		data = subject()

		# end Subject


	# shall we begin
	if _.switches.isActive('NoClean'):
		clean = False
	else:
		clean = True


	if not _.switches.isActive('Print'):
		clip_set( data, _.v.end, clean )
	
try:
	import pyperclip
except Exception as e:
	pass


# from pynput import keyboard
# https://stackoverflow.com/questions/64197868/how-to-track-and-simulate-arrow-keys-through-pynput-in-python
	


########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()






