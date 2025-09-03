#!/usr/bin/python3

# bashrc a3bc42ec51e9

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import os,sys,datetime,time,platform

def _printME_(*args):
	pr=[]
	for p in args: pr.append(str(p))
	print(' '.join(pr))


try:
	import pickle
except Exception as e:
	pass

class dot:
	def __init__(self): pass;

def nothing(*args):
	return ''
	pass

vc = dot()
v = dot()
__ = dot()
_=dot()
_v = dot()
A = dot()
vclasses = dot()
v.subprocess = None
v.appsFolder=''
v.appInfo={
	'file': 'tool',
	'description': 'little awkward bits of HIGHLY RELEVANT algorithms',
	'version': '1.4.21.58',
	'prerequisite': [],
	'examples': [
					'',
					'python3 installer.py -install h',
					'python3 installer.py -install h',
					'',
					'python3 installer.py -rc.d h',
					'python3 installer.py -rc.d h',
					'',
					'$widgets/install/installer.py ',
					'',
					't -rc.d h strip print clear home auto',
					'',
					't -rc.d h auto',
					'',
					'installer.py -json ~/.rt-config.hash',
					'',
					'installer.py -import simplejson',
					'',
					'installer.py -config.py /usr/bin/python3',
					'installer.py -config.path /opt/rightthumb-widgets-v0',
					'installer.py -config.editor code-oss',
					'',
					'installer.py -sh.file app.py',
					'installer.py -sh.folder',
					'installer.py -sh.folder.r',
					'',
					'installer.py -header.read owl.png',
					'',
					'installer.py -bash.vars',
					'',
					'installer.py -header.fix.self',
					'installer.py -header.fix.file installer.py',
					'installer.py -header.fix.folder',
					'installer.py -header.fix.folder.r',
					'',
					'installer.py -ext.folder',
					'installer.py -ext.folder.r',
					'',
					'installer.py -url.get http://reph.us/tools/tool.sh | bash',
					'',
					'installer.py -dl',
					'',
					'installer.py -config.skip r',
					'',
					'',
					'installer.py -u.p.l 65432',
					'installer.py -u.p.k 65432',
					'',
					't -sh.folder.r $widgets',
					'',
					'',
					'',
	],
	'columns': [],
}

def cl(key):
	key = key.replace('-','_')
	key = key.replace('.','_')
	key = key.replace(' ','')
	if os.sep in key:
		return '_err'
	return key
def testImport(app):
	try:
		exec( 'import ' + app )
	except Exception as e:
		_printME_( 'no' )
	else:
		_printME_( 'yes' )

try:
	import colorama
	colorama.init()
except Exception as e:
	colorama = None

######################################################
def subdo(do,p=0):
	if p:
		_printME_(do)
	if v.subprocess is None:
		import subprocess
		v.subprocess = subprocess
	try:
		result = str(v.subprocess.check_output(do.split(' ')),'iso-8859-1')
	except Exception as e:
		result = ''
	if p > 1:
		_printME_(result)
	return result
######################################################
def loader():
	try:
		__.theDelim
		loadThis = False
	except Exception as e:
		loadThis = True
		
	if not loadThis:
		return None
		
	__.theDelim = '|||'
	v.pipe=[]
	if not sys.stdin.isatty():
		v.pipe = setPipeData( sys.stdin.readlines(), clean=switches.isActive('Setting-PIPE-Clean') )
	A.vfiles = virtualFiles()
	A.ff     = Files_Folders()
	
	if os.sep == '/':
		isWin = False
	elif os.sep == '\\':
		isWin = True
	else:
		isWin = False

	vc.HD = HD()
	# v.pipe = []
	v.f = dot()
	vc.DIR = DIR()
	vc.IS = IS()
	vc.SH = SH()
	vc.FIG = FIG()
	vc.HEAD = HEAD()
	vc.EXT = EXT()
	vc.STR = STR()
	vc.HEAD = HEAD()
	vc.Color = Color()
	vc.ONLINE = ONLINE()
	vc.virtualFiles = virtualFiles()
	vc.DATE = DATE()
	vc.Files_Folders = Files_Folders()
	vc.PATHS = PATHS()
	vc.EXIT = EXIT()
	vc.md5 = _md5()


	v.isWin = isWin
	v.home = None
	v.gui = False
	v.config = None
	v.config_py = None
	v.bash = {}
	v.bash_defaults = {
							'widgets': '/opt/rightthumb-widgets-v0',
							'PY': sys.executable,
							'PY2': '/usr/bin/python2',
							'pip3': 'pip3',

							'SHELL': '/bin/bash',
							'CAT': '[widgets]/widgets/python/cat.py -f',


	}
	# v.bash_defaults['widgets']

	v.bash_defaults_no_gui = {
								'code_editor': 'nano',
								'code_editor_pre': '',
								'code_editor_suff': '',
	}
	code_editors=[
					'C:\\Program Files\\Sublime Text\\sublime_text.exe',
					'C:\\Program Files (x86)\\Sublime Text\\sublime_text.exe',
					'C:\\Users\\Scott\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
					'',
	]
	v.bash_defaults['widgets'] = 'C:\\.rightthumb-widgets'
	if v.isWin:
		for ce in code_editors:
			if ce and os.path.isfile(ce):
				v.bash_defaults_no_gui['code_editor']=ce
				break

	# if v.isWin:
	#   if os.path.isfile():
	#       v.bash_defaults_no_gui['code_editor']='C:\\Program Files\\Sublime Text\\sublime_text.exe'
	#   elif os.path.isfile('C:\\Program Files (x86)\\Sublime Text\\sublime_text.exe'):
	#       v.bash_defaults_no_gui['code_editor']='C:\\Program Files (x86)\\Sublime Text\\sublime_text.exe'
	#   else:
	#       v.bash_defaults_no_gui['code_editor']='C:\\Windows\\system32\\notepad.exe'

	v.bash_defaults = dics([ v.bash_defaults, v.bash_defaults_no_gui ])


	v.vVv = {
				'h': '[profile]',
				'pr': '[profile]/projects',
				'tt': '[profile]/tables',
				'pp': '[widgets]/programs',

				'p': '[home]',
				'rt': '[home]/.rt',

				'b': '[widgets]/widgets/bash',
				'bash': '[widgets]/widgets/bash',
				's': '[widgets]/widgets/batch',
				'bat': '[widgets]/widgets/batch',
				'git': '[widgets]/widgets/git',
				'js': '[widgets]/widgets/javascript',
				'db': '[widgets]/widgets/databank',
				'ttt': '[widgets]/widgets/databank/tables', 
				'dnd.db': '[widgets]/widgets/databank/tables/projects/DnD',
				
				'ps': '[widgets]/widgets/powershell',
				'ps1': '[home]/Documents/WindowsPowerShell',
	}

	v.f.mkdir = createDestinationFolders

	v.shClean_ext = '.py,.sh,.php,.ps1,.txt,'
	v.folder_ext_wipe_pre = '.tar,.bak'
	v.folder_ext_final_suffix = '.py,.json,.js,.txt,.bat,.vbs'

	# os.chmod( path, 0o777 )
	fig = FIG()
	hd = HD()
	fig.home()
	_vars_fo=v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'vars' +os.sep
	if not os.path.isfile( _vars_fo+'percentage.txt' ): vc.HD.saveText( '%', _vars_fo+'percentage.txt' )
	if not os.path.isfile( _vars_fo+'quote.txt' ): vc.HD.saveText( '"', _vars_fo+'quote.txt' )
	if os.path.isfile( v.config ):
		v.bash = hd.getTableSimp( v.config )
	vc.FIG.bash_vars(p=0)




	v.tables=v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'tables'
	v.temp=v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'temp'
	v.f.mkdir(v.temp)
	v.f.mkdir( v.tables )

	if v.isWin:
		v.computername = os.getenv('COMPUTERNAME')
	elif not v.isWin:
		import socket
		v.computername = socket.gethostname()

	v.computername2 = v.computername.replace(' ','_')
	# v.host = v.bash['widgets'] +os.sep+'hosts'+os.sep+v.computername2
	if 'profile' in v.bash:
		v.host = v.bash['profile']
	elif 'host' in v.bash:
		v.host = v.bash['host']
	elif 'widgets' in v.bash:
		v.host = v.bash['widgets'] +os.sep+'hosts'+os.sep+v.computername2

	if 'apps' in v.bash:
		v.appsFolder =  v.bash['apps']
	elif 'tech_drive' in v.bash:
		v.appsFolder =  v.bash['tech_drive']

	vc.FIG.load()



	isTar = dot()
	isTar.gz = vc.IS.isGz
	isTar.bz2 = vc.IS.isBz2

	import base64

	emoji_encoded = b'8J+nuyDwn6eqIPCfkoAg8J+mhiDwn6aJIPCfpZMg8J+mhCDwn6aAIPCflpUg8J+NoyDwn42kIPCfjaUg8J+NoSDwn6WDIPCfpZ4g8J+QlSDwn5G+IPCfkIkg8J+QkyDwn5CLIPCfkIwg8J+QoiDwn5G9IPCfkb8g8J+lkSDwn5ChIPCfkJcg8J+SkCDwn4+5IPCfjqgg8J+QlCDwn5CbIPCfjq8g8J+MryDwn5O3IPCfm7Yg8J+llSDwn42SIPCfjbgg8J+NsyDwn5CyIPCfjqMg8J+QnyDwn6aFIPCfkYAg8J+QuCDwn6SeIPCfkqog8J+SviDwn5G7IPCfkIog8J+NlCDwn4ytIPCfjYAg8J+VkyDwn6aKIPCfjZ8g8J+lnSDwn5aVIPCfkJIg8J+lniDwn5C8IPCfk44g8J+QpyDwn5KpIPCfjZUg8J+NjSDwn6aPIPCfjZcg8J+MiCDwn5CzIPCfppEg8J+agCDwn5mIIPCfmYog8J+ZiSDwn4yuIPCfpZIg8J+QhSDwn5CvIPCfjYkg8J+avSDwn42FIPCfkYUg8J+OqSDwn423IPCfkLUg8J+QkiDwn6aNIPCfpqcg8J+QtiDwn5CVIPCfpq4g8J+QleKAjfCfprog8J+QqSDwn5C6IPCfpoog8J+mnSDwn5CxIPCfkIgg8J+QiOKAjeKsmyDwn6aBIPCfkK8g8J+QhSDwn5CGIPCfkLQg8J+QjiDwn6aEIPCfppMg8J+mjCDwn6asIPCfkK4g8J+QgiDwn5CDIPCfkIQg8J+QtyDwn5CWIPCfkJcg8J+QvSDwn5CPIPCfkJEg8J+QkCDwn5CqIPCfkKsg8J+mmSDwn6aSIPCfkJgg8J+moyDwn6aPIPCfppsg8J+QrSDwn5CBIPCfkIAg8J+QuSDwn5CwIPCfkIcg8J+QvyDwn6arIPCfppQg8J+mhyDwn5C7IPCfkLvigI3inYTvuI8g8J+QqCDwn5C8IPCfpqUg8J+mpiDwn6aoIPCfppgg8J+moSDwn5C+IPCfpoMg8J+QlCDwn5CTIPCfkKMg8J+QpCDwn5ClIPCfkKYg8J+QpyDwn5WKIPCfpoUg8J+mhiDwn6aiIPCfpokg8J+mpCDwn6q2IPCfpqkg8J+mmiDwn6acIPCfkLgg8J+QiiDwn5CiIPCfpo4g8J+QjSDwn5CyIPCfkIkg8J+mlSDwn6aWIPCfkLMg8J+QiyDwn5CsIPCfpq0g8J+QnyDwn5CgIPCfkKEg8J+miCDwn5CZIPCfkJog8J+QjCDwn6aLIPCfkJsg8J+QnCDwn5CdIPCfqrIg8J+QniDwn6aXIPCfqrMg8J+VtyDwn5W4IPCfpoIg8J+mnyDwn6qwIPCfqrEg8J+moCDwn5KQIPCfjLgg8J+SriDwn6q3IPCfj7Ug8J+MuSDwn6WAIPCfjLog8J+MuyDwn4y8IPCfjLcg8J+MsSDwn6q0IPCfjLIg8J+MsyDwn4y0IPCfjLUg8J+MviDwn4y/IOKYmCDwn42AIPCfjYEg8J+NgiDwn42DIPCfjYcg8J+NiCDwn42JIPCfjYog8J+NiyDwn42MIPCfjY0g8J+lrSDwn42OIPCfjY8g8J+NkCDwn42RIPCfjZIg8J+NkyDwn6uQIPCfpZ0g8J+NhSDwn6uSIPCfpaUg8J+lkSDwn42GIPCfpZQg8J+llSDwn4y9IPCfjLYg8J+rkSDwn6WSIPCfpawg8J+lpiDwn6eEIPCfp4Ug8J+NhCDwn6WcIPCfjLAg8J+NniDwn6WQIPCfpZYg8J+rkyDwn6WoIPCfpa8g8J+lniDwn6eHIPCfp4Ag8J+NliDwn42XIPCfpakg8J+lkyDwn42UIPCfjZ8g8J+NlSDwn4ytIPCfpaog8J+MriDwn4yvIPCfq5Qg8J+lmSDwn6eGIPCfpZog8J+NsyDwn6WYIPCfjbIg8J+rlSDwn6WjIPCfpZcg8J+NvyDwn6eIIPCfp4Ig8J+lqyDwn42xIPCfjZgg8J+NmSDwn42aIPCfjZsg8J+NnCDwn42dIPCfjaAg8J+NoiDwn42jIPCfjaQg8J+NpSDwn6WuIPCfjaEg8J+lnyDwn6WgIPCfpaEg8J+mgCDwn6aeIPCfppAg8J+mkSDwn6aqIPCfjaYg8J+NpyDwn42oIPCfjakg8J+NqiDwn46CIPCfjbAg8J+ngSDwn6WnIPCfjasg8J+NrCDwn42tIPCfja4g8J+NryDwn428IPCfpZsg4piVIPCfq5Yg8J+NtSDwn422IPCfjb4g8J+NtyDwn424IPCfjbkg8J+NuiDwn427IPCfpYIg8J+lgyDwn6WkIPCfp4sg8J+ngyDwn6eJIPCfp4og8J+loiDwn429IPCfjbQg8J+lhCDwn5SqIPCfj7og8J+MjSDwn4yOIPCfjI8g8J+MkCDwn5e6IPCfl74g8J+nrSDwn4+UIOKbsCDwn4yLIPCfl7sg8J+PlSDwn4+WIPCfj5wg8J+PnSDwn4+eIPCfj58g8J+PmyDwn4+XIPCfp7Eg8J+qqCDwn6q1IPCfm5Yg8J+PmCDwn4+aIPCfj6Ag8J+PoSDwn4+iIPCfj6Mg8J+PpCDwn4+lIPCfjrUg8J+OtiDjgL0g4pyUIOKdjCDigYkg4p2TIOKdlCDinZUg4p2XIPCfprQg8J+ZiCDwn5mJIPCfmYog8J+SgCDimKAg8J+SqSDwn6ShIPCfkbkg8J+RuiDwn5G7IPCfkb0g8J+RviDwn6SWIPCfmLog8J+SiyDwn4yAIPCfjIgg8J+MkSDwn4ySIPCfjJMg8J+MlCDwn4yVIPCfjJYg8J+MlyDwn4yYIPCfjJkg8J+MmiDwn4ybIPCfjJwg8J+MoSDimIAg8J+MnSDwn4yeIPCfqpAg4q2QIPCfjJ8g8J+MoCDwn4yMIOKYgSDim4Ug4puIIPCfjKQg8J+MpSDwn4ymIPCfjKcg8J+MqCDwn4ypIPCfjKog8J+MqyDwn4ysIPCfjIIg4piCIOKYlCDim7Eg4pqhIOKdhCDimIMg4puEIOKYhCDwn5SlIPCfkqcg8J+MiiDwn46DIPCfjoQg4pmgIOKZpSDimaYg4pmjIOKZnyDwn46yIPCfp6k='

	decoded = base64.b64decode(emoji_encoded)
	v.emojis = ''
	# print(v.emojis)

	for x in str(decoded.decode('utf-8')):
		v.emojis+=x
		vc.STR.printable2+=x
	# print(v.emojis)
	tables = Tables()
	_v.myTables = v.tables
	__.validator_Project='test'

	__.objectPath=v.tables + os.sep+'objects'+ os.sep+'auditCodeBase_MD5.object'

######################################################

	__.switch_skimmer = dot()
	__.switch_skimmer.scan = [ '??' ]
	__.switch_skimmer.active = []

	__.aggregate = dot()
	__.aggregate.eof = dot()
	__.aggregate.eof.storage = {}
	__.aggregate.obj = None
	__.aggregate.prefixes = {
								'eot?':  1,
								'eof?':  1,
								'eog?':  1,
								'bog?':  1,
								'eoga?':  1,
								'run?':  1,
							}

	__.aggregate.group_prefixes = {
								'eog?':  1,
								'bog?':  3,
								'eoga?':  1,
								'run?':  2,
							}
	__.aggregate.fn = dot()
	# '?date' '?comma' '?size' '?bytes'
	__.aggregate.fn.format = {
								'add': '?comma',
								'isDate': '?date',
							}
	__.aggregate.fn.order = {
								'isDate': 1
							}

	# if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):


	__.terminal = dot()
	try:
		# cols, rows
		__.terminal.width, __.terminal.height = list( os.get_terminal_size() )
	except Exception as e:
		# try:
		#   __.terminal.height, __.terminal.width = os.popen('stty size', 'r').read().split()
		# except Exception as e:
		__.terminal.width = 0
		__.terminal.height = 0

	# print(__.terminal.width)

	__.terminal.cols = __.terminal.width


######################################################

def spaces(cnt):
	result = ''
	i=0
	while not i == cnt:
		i+=1
		result += ' '
	return result



# class ColorBold:
# gray = '\033[1;30;40m'
# red = '\033[1;31;40m'
# green = '\033[1;32;40m'
# yellow = '\033[1;33;40m'
# blue = '\033[1;34;40m'
# magenta = '\033[1;35;40m'
# cyan = '\033[1;36;40m'
# white = '\033[1;37;40m'
# underline = '\033[4m'
# end = '\033[0m'


class Color:
	def __init__( self ): pass;
 
 
 
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


# class Background:
# red = '\033[1;37;41m'
# green = '\033[1;37;42m'
# yellow = '\033[1;37;43m'
# blue = '\033[1;37;44m'
# purple = '\033[1;37;45m'
# light_blue = '\033[1;37;46m'
# grey = '\033[1;37;47m'
# black = '\033[1;37;48m'
# end = '\033[0m'

# class BackgroundGrey:
# black = '\033[0;30;47m'
# red = '\033[0;31;47m'
# green = '\033[0;32;47m'
# brown = '\033[0;33;47m'
# blue = '\033[0;34;47m'
# magenta = '\033[0;35;47m'
# cyan = '\033[0;36;47m'
# gray = '\033[0;37;40m'
# end = '\033[0m'
	
# class BackgroundGreyBold:
# black = '\033[1;30;47m'
# red = '\033[1;31;47m'
# green = '\033[1;32;47m'
# brown = '\033[1;33;47m'
# blue = '\033[1;34;47m'
# magenta = '\033[1;35;47m'
# cyan = '\033[1;36;47m'
# gray = '\033[1;37;40m'
# end = '\033[0m'

# colorHelp_colorList = [
# "ColorBold.gray",
# "ColorBold.red",
# "ColorBold.green",
# "ColorBold.yellow",
# "ColorBold.blue",
# "ColorBold.magenta",
# "ColorBold.cyan",
# "ColorBold.white",

# "",

# "vc.Color.purple",
# "vc.Color.cyan",
# "vc.Color.darkcyan",
# "vc.Color.blue",
# "vc.Color.green",
# "vc.Color.yellow",
# "vc.Color.red",
# "vc.Color.bold",
	
# "",

# "Background.red",
# "Background.green",
# "Background.yellow",
# "Background.blue",
# "Background.purple",
# "Background.light_blue",
# "Background.grey",
# "Background.black",

# "",

# "BackgroundGrey.black",
# "BackgroundGrey.red",
# "BackgroundGrey.green",
# "BackgroundGrey.brown",
# "BackgroundGrey.blue",
# "BackgroundGrey.magenta",
# "BackgroundGrey.cyan",
# "BackgroundGrey.gray",

# "",

# "BackgroundGreyBold.black",
# "BackgroundGreyBold.red",
# "BackgroundGreyBold.green",
# "BackgroundGreyBold.blue",
# "BackgroundGreyBold.magenta",
# "BackgroundGreyBold.cyan",
# "BackgroundGreyBold.gray"
# ]

def linePrint(  label=None, text=None, txt='_', mn=50, add=5, p=2 ):
	loader()
	ln = mn
	if text is None and label is None:
		if __.terminal.width:
			ln = __.terminal.width
			add = 0


	if not label is None:
		global line_length_hash_table
		if not label in line_length_hash_table:
			line_length_hash_table[label] = ln
		else:
			ln = line_length_hash_table[label]
		if not text is None:
			if not p == True and not p == 1:
				p = 0
			if type(text) == str:
				t = len( str(text) )
				if t > ln:
					ln = t
					line_length_hash_table[label] = ln
			elif type(text) == list:
				for texty in text:
					t = len( str(texty) )
					if t > ln:
						ln = t
						line_length_hash_table[label] = ln

	if text is None and ln > 0:
		i = 0
		result = ''
		if add:
			add+=1
		ln += add
		while not i == ln:
			result += txt
			i+=1
		if p:
			_printME_( result )
		return result




def cp( string, color='red', p=1 ):
	if type(string) == list:
		for i,s in enumerate(string):
			string[i] = str(s)
		string = ' '.join( string )

	global colorama
	if colorama is None:
		# print('no colorama installed')
		if p:
			_printME_('error')
			_printME_( string )
		return string
	subject = inlineColor( string, color )
	if p:
		_printME_( subject )
	return subject


def e( msg , e=None, kill=True):
	
	cp( linePrint(txt='*',p=0), 'red' )
	
	cp( '  Error', 'red' )
	if type(msg) == str:
		cp( [ '  \t', msg ], 'yellow' )
	if type(msg) == list:
		msgN = ['  \t']
		for x in msg:
			msgN.append(x)
		cp( msgN, 'yellow' )
	if not e is None:
		cp( ['  \t\t',e], 'cyan' )
		
	# cp( '**********************************************************************', 'red', isError=True )
	# linePrint()
	cp( linePrint(txt='*',p=0), 'red' )
	if kill:
		sys.exit()
	# △ ▽

err = e

def inlineColor( string, color='red' ):
	loader()
	# global switches
	# if switches.isActive( 'NoColor' ):
	# return string

	color = color.lower()
	if not type(string) == str:
		string = str(string)
	if color == 'red':
		return vc.Color.red + string + vc.Color.end
	elif color == 'cyan':
		return vc.Color.cyan + string + vc.Color.end
	elif color == 'darkcyan' or color == 'grey':
		return vc.Color.darkcyan + string + vc.Color.end
	elif color == 'blue':
		return vc.Color.blue + string + vc.Color.end
	elif color == 'green':
		return vc.Color.green + string + vc.Color.end
	elif color == 'yellow':
		return vc.Color.yellow + string + vc.Color.end
	elif color == 'underline':
		return vc.Color.underline + string + vc.Color.end




# try:
# import simplejson as json
# except Exception as e:
# print( 'simplejson not installed' )
# print()
def null( data ):
	return data
class Switch:
	def __init__( self, name, switch, expected_input_example = None ):
		self.name = name
		self.switch = switch
		self.pos = 0
		self.active = False
		self.value = []
		self.expected_input_example = expected_input_example
		self.script_trigger_external = None

	def trigger( self, script ):
		self.script_trigger_external = script

class Switches:
	def __init__( self ):
		self.switches = {}
 
 
	def statuses( self ):
		sws = dot()
		sws.status = {}
		sws.active = {}
		for name in self.switches:
			if self.switches[name].active:
				sws.active[name] = 1
				sws.status[name] = 1
			else:
				sws.status[name] = 0
		return sws

 
	def register( self, name, switch, expected_input_example = None ):
 
 
 
		self.switches[name] = Switch(name, switch, expected_input_example)
	def updateSwitchField( self, name, column, value ):
 
 
 
		if column == 'value':
			if not type(value) is list:
				value = [value]
			for i,vv in enumerate(value):
				if self.doesFieldExist(name,'script_trigger_external') == True:
					value[i] = self.externalScriptTrigger(name,value[i])
					# self.getSwitchField(name,'script_trigger')(value)
				elif self.doesFieldExist(name,'script_trigger') == True:
					script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
					value[i] = eval(script)
		if name in self.switches:
			exec('self.switches[\''+name+'\'].' + column + '=value')
	def doesFieldExist( self, name, column ):
 
 
 
		if name in self.switches:
			if column in self.switches[name].__dict__:
				return True
		return False
		return None
	def externalScriptTrigger( self, name, value ):
 
 
 
		if name in self.switches:
			try:
				return self.switches[name].script_trigger_external(value)
			except Exception as e:
				return value
				
	def getSwitchField( self, name, column ):
 
 
 
		if name in self.switches:
			return eval("self.switches['"+name+"']." + column )
	def isActive( self, name ):
 
 
 
		return self.getSwitchField(name,'active')
	def values( self, name ):
 
 
 
		return self.value(name)
	def value( self, name ):
 
 
 
		if name in self.switches:
			return self.switches[name].value
		return []
	def trigger( self, name, script ):
 
 
 
		if name in self.switches:
			return self.switches[name].trigger(script)
			# return script( self.switches[name].value )
	def getSwitchValue2( self, name ):
 
 
 
		switchInput = sys.argv
		try:
			switchInput[self.getSwitchField(name,'pos') + 1]
			result = []
			i = 0
			for a in switchInput:
				if i > self.getSwitchField(name,'pos'):
					if self.checkIfSwitch(switchInput[i]) == True:
						break
					else:
						result.append(switchInput[i])
				i += 1
		except Exception as e:
			result = []
		return result
	def checkIfSwitch( self, string ):
 
 
 
		result = False
		
		for key in self.switches:
			for b in self.switches[key].switch.split(','):
				if b == string:
					result = True
					# print(b,result)
		return result
	def processSwitchFormatting( self, name ):
 
 
 
		value = self.getSwitchValue2(name)
		# print('value',value)
		for i,vv in enumerate(value):
			if self.doesFieldExist(name,'script_trigger_external') == True:
				value[i] = self.externalScriptTrigger(name,value[i])
			elif self.doesFieldExist(name,'script_trigger') == True:
				script = '{}(\'{}\',\'{}\')'.format(self.getSwitchField(name,'script_trigger'),name,value[i])
				value[i] = eval(script)
		return value
	def checkSwitchExist( self, name ):
 
 
 
		if name in self.switches:
			return True
		return False
	def process( self ):
 
 
 
		# print(inList)
		global customHelp
		switchInput = sys.argv
		for sw in self.switches:
			self.switches[sw].pos = None
			self.switches[sw].active = False
			self.switches[sw].value = []
		for i,a in enumerate(sys.argv):
			# a = a.replace(':','')
			# print('a',a)
			for sw in self.switches:
				# print(sw['name'])
				for s in self.switches[sw].switch.split(','):
					# print(s)
					# print( s,a )
					if s.lower() == a.lower():
						self.switches[sw].pos = i
						self.switches[sw].active = True
						self.switches[sw].value = self.processSwitchFormatting(self.switches[sw].name)
		if self.isActive('Help'):
			print_help()
		if self.isActive('Debug') == True or self.isActive('Errors') == True:
			self.print()
			sys.exit()
		# theErrors()
	def print( self ):
 
 
 
		p = 'FB2DEDECEA7E'
		return None
		_printME_( 'print aborted' )
def printVar( data , p=1 ):
	simplejson = vc.FIG.imp('simplejson')
	j = simplejson.dumps(data, indent=4, sort_keys=False)
	if p:
		_printME_(j)
	return j

def jsoncode( data ):
	return printVar( data , p=0 )

switches = Switches()

# v.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})
# v.appInfo['columns'].append({'name': 'initiated', 'abbreviation': 'i'})
# v.appInfo['columns'].append({'name': 'type', 'abbreviation': 't'})
# v.appInfo['columns'].append({'name': 'priority', 'abbreviation': 'p'})
# v.appInfo['columns'].append({'name': 'drive', 'abbreviation': 'd,l,dr'})
# v.appInfo['columns'].append({'name': 'machineID', 'abbreviation': 'm'})
# v.appInfo['columns'].append({'name': 'timestamp', 'abbreviation': 'ts,time,date'})
def formatColumns(columns):
	result = ''
	for c in columns.split(','):
		for col in v.appInfo['columns']:
			for a in col['abbreviation'].split(','):
				if a == c:
					c = col['name']
		result += c + ','
	result = result[:-1]
	return result

class HD:
	def __init__( self ): pass;
 

	def process_code( self, code ):
		validator=Validator()
		validator.register( code, 'javascript' )
		status=validator.createIndex( code, 'javascript', skipLoad=True, simple=False, A=False, B=True, C=False )
		return validator.genJson()

 
	def json( self, path ):
		code=self.getText( path, raw=True )
		return self.process_code(code)


	def head( self, path, l=5 ):
 
 
 
		try:
			head = " ".join(['{:02X}'.format(byte) for byte in   open( path, 'rb' ).read(32)    ])
		except Exception as e:
			head = ''
		return head

	def headTXT( self, path, l=5 ):
 
 
 
		try:
			head = open( path , 'r' ).read(l)
		except Exception as e:
			head = ''
		return head


	def chmod( self, path ):
 
 
 
		if not v.isWin and os.path.isfile(path):
			try:
				os.chmod( path, 0o777 )
			except Exception as e:
				pass

	def saveTable( self, data, file, p=0 ):
		simplejson = vc.FIG.imp('simplejson')
		path = v.tables +os.sep+ file
		open( path , 'w').write(    simplejson.dumps(data, indent=4, sort_keys=False)   )
		vc.HD.chmod(file)
		if p:
			cp( path, 'cyan' )
		
	def getTable( self, file ):
		simplejson = vc.FIG.imp('simplejson')
		path = v.tables +os.sep+ file
		if os.path.isfile(path):
			vc.HD.chmod(path)
			with open(path,'r', encoding="latin-1") as json_file:
				json_data = simplejson.load(json_file)
			return json_data
		else:
			dics = 'index,indexes,dex,ls,hash,hashes,tables,logs,lists,indices,meta,setting,settings'
			lists = 'table,cache,log,list'
			for x in dics.split(','):
				if path.endswith( '.'+x ):
					return {}
			for x in lists.split(','):
				if path.endswith( '.'+x ):
					return []

			return []


	def yamlSimp(yaml_string):
		table = {}
		lines = yaml_string.split('\n')
		for line in lines:
			if ':' in line:
				key, value = line.split(':', 1)
				table[key.strip()] = value.strip()
			return table


	def getTableSimp( self, file ):
 
 
 
		# print(file)
		txt = vc.HD.getText(file,raw=True)
		if not txt[0] == '{': return vc.HD.yamlSimp(txt)
		# print(type(txt))
		# print(txt)
		table = {}
		for i,a in enumerate(txt.split('"')):
			ii=i+1
			if ii % 4 == 0:
				# print( 4, a )
				table[last] = a
			elif ii % 2 == 0:
				last=a
				# print( 2, a )
			else:
				pass
				# print( 0, a )
		return table
	def getText( self, theFile, raw=False, clean=False, e=0, c=0 ):
		theFile=theFile.replace(os.sep+os.sep,os.sep)
		if not os.path.isfile(theFile):
			if raw:
				return ''
			else:
				return []
		lines = None
		if os.path.isfile(theFile):
			try:
				f = open(theFile, 'r', encoding='utf-8')
				lines = f.readlines()
				f.close()
			except Exception as e:
				try:
					f = open(theFile, 'r', encoding='latin-1')
					lines = f.readlines()
					f.close()
				except Exception as e:
					f = open(theFile, 'r')
					lines = f.readlines()
					f.close()
		if clean:
			def c20(sub,a,b):
				while a in sub:
					sub=sub.replace(a,b)
				return sub
			d20=''.join(lines)
			d20=c20(d20,'\r','')
			d20=c20(d20,'\n\n','\n')
			if clean==2:
				d20=c20(d20,' \n','\n')
				d20=c20(d20,'\t\n','\n')
				d20=c20(d20,'\n\n','\n')
			lines=d20.split('\n')

		if raw:
			return ''.join(lines)
		return lines

	def saveText( self, rows, theFile, errors=True ):
		if theFile.endswith('/.bashrc'):
			if type(rows) == list:
				rows.prepend('#!/bin/bash')
			elif type(rows) == str:
				rows='#!/bin/bash\n'+rows



		theFile=theFile.replace(os.sep+os.sep,os.sep)
		# print(vc.STR.printable)
		# v.f.mkdir
		if os.sep in theFile:
			parts = theFile.split(os.sep)
			parts.reverse()
			parts.pop(0)
			parts.reverse()
			v.f.mkdir(os.sep.join(parts))


		vc.HD.chmod(theFile)
		# print(type(rows))
		try:
			if type(rows) == bytes:
				rows = str(rows,'utf-8')
			f = open(theFile,'w', encoding='utf-8')
			# if type(rows) == str:

			# print(type(rows))
			# f.write(str(rows))
			# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
			# f.write(rows)
			# f.write(rows.encode("iso-8859-1", "replace"))

			# print(type(rows))
			if type(rows) == str:
				# print(rows)
				f.write(rows)
			else:
				for i,row in enumerate(rows):
					# f.write(str(row) + os.linesep)
					if i == 0:
						if len(str(row)) > 0:
							f.write(str(row) + '\n')
					else:
						f.write(str(row) + '\n')
			f.close()
		except Exception as e:
			if type(rows) == list:
				result = ''
				for i,row in enumerate(rows):
					# f.write(str(row) + os.linesep)
					if i == 0:
						if len(str(row)) > 0:
							result += str(row) + '\n'
					else:
						result += str(row) + '\n'

				rows = result
			try:
				open(theFile, 'wb').write(rows)
			except Exception as e:
				try:
					open(theFile, 'w').write(rows)
				except Exception as e:
					new_text = ''
					for x in rows:
						if x in vc.STR.printable2:
							new_text+=x
					open(theFile, 'w', encoding='utf-8').write(new_text)
			vc.HD.chmod(theFile)

	def saveText2( self, rows, theFile, errors=True ):
		theFile=theFile.replace(os.sep+os.sep,os.sep)
 
		if os.sep in theFile:
			parts = theFile.split(os.sep)
			parts.reverse()
			parts.pop(0)
			parts.reverse()
			v.f.mkdir(os.sep.join(parts))
 
 
		# print(type(rows))
		try:
			if type(rows) == bytes:
				rows = str(rows,'utf-8')
			f = open(theFile,'w', encoding='utf-8')
			# if type(rows) == str:
			# print(type(rows))
			# f.write(str(rows))
			# rows = [unicode(x.strip()) if x is not None else u'' for x in rows]
			# f.write(rows)
			# f.write(rows.encode("iso-8859-1", "replace"))
			# print(type(rows))
			if type(rows) == str:
				# print(rows)
				f.write(rows)
			else:
				for i,row in enumerate(rows):
					# f.write(str(row) + os.linesep)
					if i == 0:
						if len(str(row)) > 0:
							f.write(str(row) + '\n')
					else:
						f.write(str(row) + '\n')
			f.close()
		except Exception as e:
			if type(rows) == list:
				result = ''
				for i,row in enumerate(rows):
					# f.write(str(row) + os.linesep)
					if i == 0:
						if len(str(row)) > 0:
							result += str(row) + '\n'
					else:
						result += str(row) + '\n'
				# rows = result
				rows = '\n'.join( rows )
				rows.encode('ascii')
			open(theFile, 'w').write(rows)

			if errors:
				_printME_( 'Auto correction when saving text' )

	def saveTableSimp( self, data, file ):
		if os.path.isfile(file): return None
		if os.sep in file:
			parts = file.split(os.sep)
			parts.reverse()
			parts.pop(0)
			parts.reverse()
			v.f.mkdir(os.sep.join(parts))
		
		for k in data:
			data[k]=data[k].replace('\\\\','\\')
			data[k]=data[k].replace('\\','\\\\')
			data[k]=data[k].replace('"','')
		text = printDic( data, p=0 )
		vc.HD.saveText( text, file )



def showLine( string, plus = '', minus = '', plusOr = False, end=None ):
	# print(plus)
	# print(string)
	
	global switches
	if switches.isActive('Plus') or not plus == '':
		# print('asdf')
		result = positiveResults(string,plus,plusOr,end)
		if not result and switches.isActive('PlusClose'):
			result = closeResults( string )

	else:
		result = True
	if result == True and (switches.isActive('Minus') or not minus == ''):
		result = minusResults(string,minus)
	# print(result)
	return result
def closeResults( string ):
	global switches
	global plusClose
	
	if len( switches.value('PlusClose') ):
		try:
			plusClose = float( switches.value('PlusClose') )
		except Exception as e:
			pass

	test = patternDiff( string, switches.value('Plus') )
	# print( int(test), string, switches.value('Plus') )
	if test >= plusClose:
		# print( test, string )
		return True
	else:
		return False



def positiveResults(string,plus='',plusOr=False,end=None):
	global switches

	if plusOr or switches.isActive('PlusOr'):
		plusOr = True
	if not plus == '':
		plusInput = plus
	else:
		plusInput = switches.values('Plus').copy()
	if not end is None:
		if type( plusInput ) == str:
			plusInput += end
		else:
			for i,yh in enumerate(plusInput):
				plusInput[i] += end
		
	pi = []
	for x in plusInput:
		pi.append( vc.STR.ci(x) )
	plusInput = pi
	del pi
	if type( plusInput ) == str:
		if not switches.isActive('StrictCase'):
			plusInput = plusInput.lower()
		plusList = plusInput.split(',')
	else:
		for i,row in enumerate(plusInput):
			if not switches.isActive('StrictCase'):
				plusInput[i] = plusInput[i].lower()
		plusList = plusInput
	length = len(plusList)
	cnt = 0
	result = False
	if not switches.isActive('StrictCase'):
		string = string.lower()
	# print( plusList )
	# sys.exit()
	for s in plusList:
		if not switches.isActive('StrictCase'):
			s = s.lower()
		
		if len(s) > 1 and s[0] == '*':
			s = s.replace('*','')
			if string.endswith(s):
				cnt += 1
		elif len(s) > 1 and s[-1] == '*':
			s = s.replace('*','')
			if string.startswith(s):
				cnt += 1
		elif not switches.isActive('PlusDuplicate') and ( not string.find(vc.STR.ci(s)) == -1 or s in string ):
			cnt += 1
		elif switches.isActive('PlusDuplicate') and ( string.count(vc.STR.ci(s)) > 1 or string.count(s) > 1 ):
			cnt += 1
		# if 'opus' in string:
		# print(cnt, string)
		if length == cnt:
			result = True
			break
		if plusOr:
			if cnt > 0:
				result = True
	return result

def minusResults(string,minus=''):
	global switches
	if not switches.isActive('StrictCase'):
		string = string.lower()
	result = True
	if not minus == '':
		minusInput = minus
	else:
		minusInput = switches.values('Minus')
	if type( minusInput ) == str:
		if not switches.isActive('StrictCase'):
			minusInput = minusInput.lower()
		else:
			minusInput = minusInput
		minusList = minusInput.split(',')
	else:
		for i,row in enumerate(minusInput):
			if not switches.isActive('StrictCase'):
				minusInput[i] = minusInput[i].lower()

		minusList = minusInput

	try:
		for s in minusList:
			if not switches.isActive('StrictCase'):
				s = s.lower()
			if len(s) > 1 and s[0] == '*':
				s = s.replace('*','')
				if string.endswith(s):
					result = False
					break
			elif len(s) > 1 and s[-1] == '*':
				s = s.replace('*','')
				if string.startswith(s):
					result = False
					break
			if not string.find(vc.STR.ci(s)) == -1 or s in string:
				result = False
				break
	except Exception as e:
		pass
	return result




########################################################################################

class SH:
	def __init__( self ): pass;
 
 
 
	def getFolderSH( self, folder ):
 
		if os.sep+'backup'+os.sep in folder:
			return None
 
		if not os.path.isdir(folder):
			return None
		try:
			dirList = os.listdir(folder)
		except Exception as e:
			return None
		# i = 0
		for item in dirList:
			path = folder + os.sep + item
			if os.path.isfile(path):
				shouldProcess = False
				if path.endswith('.sh') or path.endswith('.py'):
					shouldProcess = True

				if not shouldProcess:
					head = vc.HD.headTXT(path)
					if len(head) and head[0] == '#':
						if 'python' in head or 'bash' in head:
							shouldProcess = True

				if shouldProcess:
					self.processSHfile(path)

			if os.path.isdir(path):
				if switches.isActive('SH-Folder-Recursive'):
					try:
						self.getFolderSH(path)
					except Exception as e:
						pass


	def ReplaceSequence(self, inFilename, outFilename, oldSeq, newSeq=None):
		inputFile  = open(inFilename, "rb")
		outputFile = open(outFilename, "wb")

		data = ""
		chunk = 1024

		while 1:
			data = inputFile.read(chunk)
			for x in data:
				if not x == oldSeq:
					try:
						outputFile.write(x.encode('utf-8'))
					except Exception as e:
						outputFile.write(ord(x).decode())
			# if not newSeq is None:
			#   data = data.replace(oldSeq, newSeq)

			inputFile.seek(-len(oldSequence), 1)
			outputFile.seek(-len(oldSequence), 1)

			if len(data) < chunk:
				break

		inputFile.close()
		outputFile.close()

	def processSHfile( self, path ):
 
		try:
			os.chmod( path, 0o777 )
		except Exception as e:
			pass
 
		vc.HD.chmod(path)
		if not os.path.isfile(path):
			cp([ 'Error: not a file-',path ],'red')
			return None
		shouldProcess = False

		for ex in v.shClean_ext.split(','):
			if path.lower().endswith(ex):
				shouldProcess = True
	
		if not shouldProcess and vc.HD.headTXT(path).startswith('#!'):
			shouldProcess = True

		if not shouldProcess and vc.IS.isText(path):
			shouldProcess = True
		if shouldProcess:
			
				
			if not switches.isActive('Clean'):
				cp( path, 'cyan' )
			file = vc.HD.getText( path, raw=True )
			# while chr(10) in file or chr(27) in file:
			file = file.replace( chr(10), '\n' )
			file = file.replace( chr(27), '' )
			# file = file.replace( '0xC2', '' )
			# file = file.replace( 0xC2, '' )
			file = file.replace( chr(0xC2), '' )
			file = file.replace( '\r', '' )
			vc.HD.saveText( file, path )
			# temp = v.temp+os.sep+'tool.processSHfile.tmp'
			# if os.path.isfile(temp):
			#   os.unlink(temp)
			# self.ReplaceSequence(path,temp,chr(0xC2),'')
			# from shutil import copyfile
			# if os.path.isfile(temp):
			#   if os.path.isfile(path):
			#       os.unlink(path)
			#   copyfile( temp, path )
			vc.HD.chmod(path)
			









isBinCharTest = None
class IS:
	def __init__( self ): pass;
 
 
 
	def isBinChar( self ):
 
 
 
		global isBinCharTest
		if isBinCharTest is None:
			isBinCharTest = [ "Z", "c", "1", "y", "Q", "W", "m", "L", "k", "A", "E", "B", "z", "g", "0", "q", "C", "D", "u", "e", "w", "-", "4", "M", "p", "b", "O", "v", "K", "8", "I", "j", "7", "n", "r", "s", "V", "G", "X", "P", "l", "a", "x", "N", "3", "T", "t", "_", "d", "i", "Y", "o", "2", "9", "J", "F", "6", "U", "h", "f", "R", "S", "H", " ", ",", ".", "\n", "[", "5", "]", "{", "\"", ":", "\\", "}", "(", ")", "?", "'", "/", "$", "!", "|", ";", "&", "*", "+", "=", "#", "<", ">", "@", "`", "%", "~", "^", "\u00a0", "\u2014", "\u2019", "\u2013", "\u2022", "\u201c", "\u201d", "\u0093", "\u0094", "\u0097", "\u2018", "\u2003", "\ufffc", "\u00d7", "\u2060", "\u2212", "\u00b0", "\u00c5", "\u0431", "\u0433", "\u00f4", "\u00e7", "\u00f1", "\u00f8", "\u00e9", "\u00cd", "\u0101", "\u0441", "\u0440", "\u0444", "\u00e3", "\u00ed", "\u00fc", "\u0627", "\u0644", "\u062c", "\u0632", "\u0626", "\u0631", "\u0570", "\u0561", "\u0575", "\u0628", "\u062d", "\u064a", "\u0646", "\u09ac", "\u09be", "\u0982", "\u09b2", "\u0435", "\u043b", "\u4e2d", "\u56fd", "\u014d", "\u00f3", "\u570b", "\u0645", "\u0635", "\u1e63", "\u044e", "\u03b5", "\u03c5", "\u10d2", "\u10d4", "\u03bb", "\u9999", "\u6e2f", "\u092d", "\u093e", "\u0930", "\u0924", "\u06be", "\u062a", "\u0c2d", "\u0c3e", "\u0c30", "\u0c24", "\u0c4d", "\u0aad", "\u0abe", "\u0ab0", "\u0aa4", "\u0a2d", "\u0a3e", "\u0a30", "\u0a24", "\u012b", "\u0b87", "\u0ba8", "\u0bcd", "\u0ba4", "\u0bbf", "\u0baf", "\u0bbe", "\u09ad", "\u09b0", "\u09a4", "\u0cad", "\u0cbe", "\u0cb0", "\u0ca4", "\u0d2d", "\u0d3e", "\u0d30", "\u0d24", "\u0d02", "\u09f0", "\u0b2d", "\u0b3e", "\u0b30", "\u0b24", "\u092e", "\u094d", "\u094b", "\u0680", "\u06cc", "\u012a", "\u0639", "\u0642", "\u02bf", "\u05d9", "\u05e9", "\u05e8", "\u05d0", "\u05dc", "\u062f", "\u049b", "\u0430", "\u0437", "\u0ea5", "\u0eb2", "\u0ea7", "\u6fb3", "\u95e8", "\u00c0", "\u9580", "\u0633", "\u0648", "\u016b", "\u043c", "\u043e", "\u043d", "\u063a", "\u0121", "\u043a", "\u0434", "\u067e", "\u06a9", "\u0641", "\u0637", "\u1e6d", "\u0629", "\u65b0", "\u52a0", "\u5761", "\u0b9a", "\u0b99", "\u0b95", "\u0baa", "\u0bc2", "\u0bb0", "\ud55c", "\uad6d", "\u0dbd", "\u0d82", "\u0d9a", "\u0dcf", "\u0bb2", "\u0bc8", "\u1e45", "\u53f0", "\u6e7e", "\u00e1", "\u7063", "\u0e44", "\u0e17", "\u0e22", "\u0443", "\u00e4", "\u00fa", "\u01ce", "\u7f51", "\u7db2", "\u4eba", "\u624b", "\u673a", "\u014f", "\u56fe", "\u4e66", "\u8d2d", "\u00f2", "\u5fae", "\u535a", "\u0113", "\u559c", "\u6b22", "\u01d0", "\u4fe1", "\u00ec", "\u00e0", "\u0926", "\u0947", "\u0938", "\u0940", "\u0936", "\u093f", "\u0915", "\u0937", "\u0643", "\u062b", "\u0634", "\u00e2", "\u5728", "\u7ebf", "\u6587", "\u5740", "\u7ad9", "\u7edc", "\u516c", "\u53f8", "\u5546", "\u57ce", "\u6784", "\u6211", "\u7231", "\u4f60", "\u01d2", "\u6807", "\u4e16", "\u754c", "\u00e8", "\u96c6", "\u56e2", "\u6148", "\u5584", "\u516b", "\u5366", "\u76ca", "\u0442", "\u0438", "\u0439", "\u0902", "\u0917", "\u0920", "\u0928", "\u0949", "\u091f", "\ub2f7", "\ucef4", "\ub137", "\u05e7", "\u05d5", "\u05dd", "\u307f", "\u3093", "\u306a", "\u30bb", "\u30fc", "\u30eb", "\u30d5", "\u30a1", "\u30c3", "\u30b7", "\u30e7", "\u30f3", "\u30b9", "\u30c8", "\u30a2", "\u30dd", "\u30a4", "\u30af", "\u30e9", "\u30a6", "\u30c9", "\u30b3", "\u30e0", "\u0e04", "\u0e2d", "\u0e21", "\u0130", "\u1e92", "\u00f6", "\u8054", "\u901a", "\u79fb", "\u52a8", "\u683c", "\u91cc", "\u62c9", "\u2010", "\u6de1", "\u9a6c", "\u9521", "\u5927", "\u4f17", "\u6c7d", "\u8f66", "\u30b0", "\u8c37", "\u6b4c", "\u01d4", "\u5de5", "\u884c", "\u5609", "\u9152", "\u5e97", "\u98de", "\u5229", "\u6d66", "\u8bfa", "\u57fa", "\u4e9a", "\u96fb", "\u8a0a", "\u76c8", "\u79d1", "\uc0bc", "\uc131", "\u00ff", "\u00ad", "\u25bd", "\u25b3", "\ud83e\uddfb", "\ud83e\uddea", "\ud83d\udc80", "\ud83e\udd86", "\ud83e\udd89", "\ud83e\udd53", "\ud83e\udd84", "\ud83e\udd80", "\ud83d\udd95", "\ud83c\udf63", "\ud83c\udf64", "\ud83c\udf65", "\ud83c\udf61", "\ud83e\udd43", "\ud83e\udd5e", "\ud83d\udc15", "\ud83d\udc7e", "\ud83d\udc09", "\ud83d\udc13", "\ud83d\udc0b", "\ud83d\udc0c", "\ud83d\udc22", "\ud83d\udc7d", "\ud83d\udc7f", "\ud83e\udd51", "\ud83d\udc21", "\ud83d\udc17", "\ud83d\udc90", "\ud83c\udff9", "\ud83c\udfa8", "\ud83d\udc14", "\ud83d\udc1b", "\ud83c\udfaf", "\ud83c\udf2f", "\ud83d\udcf7", "\ud83d\udef6", "\ud83e\udd55", "\ud83c\udf52", "\ud83c\udf78", "\ud83c\udf73", "\ud83d\udc32", "\ud83c\udfa3", "\ud83d\udc1f", "\ud83e\udd85", "\ud83d\udc40", "\ud83d\udc38", "\ud83e\udd1e", "\ud83d\udcaa", "\ud83d\udcbe", "\ud83d\udc7b", "\ud83d\udc0a", "\ud83c\udf54", "\ud83c\udf2d", "\ud83c\udf40", "\ud83d\udd53", "\ud83e\udd8a", "\ud83c\udf5f", "\ud83e\udd5d", "\ud83d\udc12", "\ud83d\udc3c", "\ud83d\udcce", "\ud83d\udc27", "\ud83d\udca9", "\ud83c\udf55", "\ud83c\udf4d", "\ud83e\udd8f", "\ud83c\udf57", "\ud83c\udf08", "\ud83d\udc33", "\ud83e\udd91", "\ud83d\ude80", "\ud83d\ude48", "\ud83d\ude4a", "\ud83d\ude49", "\ud83c\udf2e", "\ud83e\udd52", "\ud83d\udc05", "\ud83d\udc2f", "\ud83c\udf49", "\ud83d\udebd", "\ud83c\udf45", "\ud83d\udc45", "\ud83c\udfa9", "\ud83c\udf77", "\u327f", "\u250c", "\u2500", "\u2514", "\u00b6", "\u2588", "\u0095", "\u2026", "\u00b4", "\u00f7", "\ud83c\udfff", "\ud83c\udffb", "\ud83c\udffe", "\ud83c\udffc", "\ud83c\udffd", "\ud83d\uddbc", "\u001b", "\u00fe", "\u0000", "\u0088", "\u00f9", "\u00d6", "\u00b5", "\u0003", "\u00b8", "\u00b3", "\b", "\u0080", "\u0099", "\u00c2", "\u00b2", "\u00a9", "\u00ac", "\u0005", "\u0014", "\u0001", "\u00bc", "\u00fd", "\u009e", "\u00b9", "\u00c8", "\u0002", "\u0098", "\u00f5", "\u008a", "\u00b7", "\u008f", "\u00bb", "\u0096", "\u00af", "\u0004", "\u00f0", "\u00aa", "\u00a1", "\f", "\u00bf", "\u0086", "\u000b", "\u00d5", "\u00ee", "\u009a", "\u001f", "\u009f", "\u00a6", "\u00b1", "\u00dc", "\u0011", "\u000e", "\u009d", "\u001e", "\u00de", "\u00ab", "\u0085", "\u00c7", "\u001c", "\u00c4", "\u00d9", "\u007f", "\u0089", "\u00eb", "\u0082", "\u00df", "\u00d2", "\u0091", "\u00ea", "\u0010", "\u00be", "\u00d0", "\u008b", "\u0006", "\u00db", "\u00d3", "\u009c", "\u00c9", "\u009b", "\u00cf", "\u0084", "\u00da", "\u00c6", "\u0007", "\u0018", "\u00cb", "\u00ba", "\u00e6", "\u00c1", "\u00bd", "\u00a2", "\u00dd", "\u0012", "\u0423", "\u0420", "\u044f", "\u0131", "\u00a5", "\u00ef", "\u0151", "\u0161", "\u0107", "\u010d", "\u1ec5", "\u1ecd", "\u1ea1", "\u0219", "\u00e5", "\u0160", "\u00d8", "\u0647", "\u06d0", "\u069a", "\u062e", "\u0693", "\u06ab", "\u0696", "\u0685", "\u06cd", "\u0698", "\u067c", "\u0689", "\u0686", "\u06bc", "\u0681", "\u060c", "\u0411", "\u0456", "\u043f", "\u0414", "\u045e", "\u044b", "\u044c", "\u0447", "\u0432", "\u044d", "\u0448", "\u0451", "\u041d", "\u0446", "\u041f", "\u0445", "\u0436", "\u0428", "\u0417", "\u0421", "\u041a", "\u041b", "\u042d", "\u0422", "\u0412", "\u041c", "\u041e", "\u0416", "\u0410", "\u042c", "\u0426", "\u0424", "\u0454", "\u0406", "\u0413", "\u0457", "\u0449", "\u0415", "\u0427", "\u0419", "\u0654", "\u0638", "\u200c", "\u200e", "\u06af", "\u0650", "\u200f", "\u0630", "\u061b", "\u0622", "\u064b", "\u0636", "\u00fb", "\u0905", "\u092a", "\u092f", "\u0941", "\u0923", "\u0935", "\u0932", "\u090f", "\u0939", "\u0948", "\u0908", "\u0927", "\u091a", "\u0906", "\u0901", "\u0921", "\u093c", "\u0942", "\u094c", "\u091c", "\u092b", "\u0943", "\u0925", "\u0916", "\u0907", "\u092c", "\u0909", "\u0922", "\u091e", "\u0910", "\u0914", "\u0903", "\u091b", "\u0913", "\u0911", "\u0651", "\u0652", "\u0623", "\u0625", "\u0649", "\u064f", "\u0621", "\u0640", "\u0624", "\u202a", "\u202c", "\u064e", "\ufefb", "\u201e", "\u045a", "\u0458", "\u0459", "\u045b", "\u0418", "\u0452", "\u7518", "\u9732", "\u015f", "\u017d", "\u017e", "\u0259", "\u018f", "\ufffd", "\u0f62", "\u0f7a", "\u0f0b", "\u0f56", "\u0f58", "\u0f51", "\u0f54", "\u0f60", "\u0f72", "\u0f41", "\u0fb1", "\u0f46", "\u0f7c", "\u0f66", "\u0f64", "\u0f42", "\u0f53", "\u0f63", "\u0f74", "\u0f0d", "\u0f5a", "\u0f50", "\u0f44", "\u0f9f", "\u0f90", "\u0fa1", "\u0fa3", "\u0f45", "\u0f61", "\u0f68", "\u0f67", "\u0f5b", "\u0f92", "\u0f5f", "\u0f5e", "\u0fb2", "\u0fb3", "\u0fb7", "\u0f55", "\u0f4a", "\u0f47", "\u0f40", "\u0f4c", "\u0f49", "\u0f0c", "\u0f71", "\u0fa4", "\u0f4f", "\u0fa9", "\u0f5d", "\u0f28", "\u0fa6", "\u0f59", "\u0f97", "\u0fab", "\u0f21", "\u0f26", "\u044a", "\u200a", "\u042f", "\u042e", "\u0111", "\u010c", "\u0c35", "\u0c3f", "\u0c15", "\u0c02", "\u0c2b", "\u0c23", "\u0c40", "\u0c26", "\u0c21", "\u0c41", "\u0c2a", "\u0c38", "\u0c2e", "\u0c2f", "\u0c42", "\u0c32", "\u0c05", "\u0c28", "\u0c4b", "\u0c1f", "\u0c2c", "\u0c4a", "\u0c47", "\u0c17", "\u0c46", "\u0c48", "\u0c12", "\u0c1a", "\u0c1c", "\u0c39", "\u0c0e", "\u0c37", "\u0c27", "\u0c09", "\u0c06", "\u0c10", "\u0c25", "\u0c07", "\u0c13", "\u0c03", "\u0c43", "\u0c1b", "\u0c36", "\u0c20", "\u0c16", "\u0c33", "\u0c0a", "\u0c0f", "\u200d", "\u0c08", "\u0c69", "\u0c68", "\u0c4c", "\u0549", "\u056b", "\u057b", "\u0578", "\u0572", "\u057e", "\u0565", "\u056c", "\u056f", "\u0580", "\u0564", "\u057d", "\u0574", "\u0582", "\u0568", "\u055d", "\u057a", "\u0576", "\u0562", "\u0581", "\u056d", "\u057f", "\u0569", "\u0586", "\u0583", "\u056e", "\u0563", "\u0567", "\u0579", "\u054d", "\u057c", "\u0584", "\u0553", "\u0587", "\u0585", "\u053f", "\u0551", "\u0541", "\u0556", "\u306f", "\u3068", "\u3044", "\u3046", "\u8981", "\u7d20", "\u306b", "\u5bfe", "\u3057", "\u3066", "\u60f3", "\u5b9a", "\u5916", "\u306e", "\u5c5e", "\u6027", "\u3067", "\u3059", "\u3042", "\u308a", "\u307e", "\u305b", "\u30bf", "\u305f", "\u30c7", "\u30fb", "\u30a3", "\u30ec", "\u30ea", "\u59a5", "\u5f53", "\u30d6", "\u30de", "\u304c", "\u65e2", "\u5b58", "\u898b", "\u3064", "\u304b", "\u578b", "\u7fa9", "\u3055", "\u308c", "\u30d7", "\u30d9", "\u30b1", "\u3092", "\u767b", "\u9332", "\u5c55", "\u958b", "\u304d", "\u3089", "\u5b57", "\u5408", "\u3078", "\u5909", "\u63db", "\u30b5", "\u51e6", "\u7406", "\u3051", "\u308b", "\u5165", "\u529b", "\u7121", "\u52b9", "\u30d0", "\u4e26", "\u3073", "\u30a8", "\u6700", "\u5f8c", "\u4e0d", "\u5b8c", "\u5168", "\u30a9", "\u30ad", "\u7d76", "\u542b", "\u3060", "\u30ed", "\u30ab", "\u6b63", "\u304f", "\u30db", "\u540d", "\u9593", "\u9055", "\u3063", "\u30d1", "\u6642", "\u78ba", "\u4fdd", "\u8aad", "\u8fbc", "\u5fc5", "\u51fa", "\u30ba", "\u304e", "\u3081", "\u53d6", "\u5f97", "\u5931", "\u6557", "\u66f4", "\u751f", "\u6210", "\u66f8", "\u30e2", "\u524a", "\u9664", "\u30c6", "\u3053", "\u30dc", "\u6b8b", "\u30c1", "\u30e3", "\u30cd", "\u7d42", "\u308f", "\u76ee", "\u524d", "\u5217", "\u3002", "\u53c2", "\u7167", "\u6570", "\u4f8b", "\u304a", "\u305d", "\u30df", "\u3082", "\u4f7f", "\u7528", "\u53ef", "\u80fd", "\u7a7a", "\u660e", "\u3087", "\u3088", "\u30e5", "\u30e1", "\u59cb", "\u7d9a", "\u672b", "\u5c3e", "\u5024", "\u8a2d", "\u7b49", "\u53f7", "\u8a18", "\u5f15", "\u9589", "\u3058", "\u4f55", "\u73fe", "\u3001", "\u767d", "\u30ae", "\u76f4", "\u4e86", "\u7a81", "\u7136", "\u3071", "\u9014", "\u6b21", "\u6307", "\u793a", "\u5b50", "\u30aa", "\u30b8", "\u30a7", "\u5185", "\u90e8", "\u8db3", "\u4e0a", "\u9650", "\u9054", "\u5206", "\u6761", "\u4ef6", "\u65b9", "\u518d", "\u5e30", "\u4f5c", "\u696d", "\u9818", "\u57df", "\u6539", "\u9023", "\u643a", "\u539f", "\u56e0", "\u7aef", "\u8a8d", "\u8b58", "\u308d", "\u5c0f", "\u633f", "\u91cf", "\u9806", "\u756a", "\u8868", "\u7e70", "\u8fd4", "\u4ed8", "\u898f", "\u9577", "\u56fa", "\u5f62", "\u5f0f", "\u4e8c", "\u4ee5", "\u5e8f", "\u547c", "\u540c", "\u4e0b", "\u591a", "\u500b", "\uff18", "\u9032", "\uff11", "\u77db", "\u76fe", "\uff10", "\u8d85", "\u3048", "\u969b", "\u9069", "\u5316", "\u534a", "\u5fdc", "\u4ee3", "\u66ff", "\u89e3", "\u6790", "\u52d5", "\u8d77", "\u74b0", "\u5883", "\u30d8", "\u30c0", "\u5b9f", "\u5341", "\u7bc4", "\u56f2", "\u6cd5", "\u6574", "\u691c", "\u7d22", "\u5e38", "\u30da", "\u91c8", "\u6301", "\u8ad6", "\u6e21", "\u64cd", "\u7a2e", "\u985e", "\u65e9", "\u5230", "\u9805", "\u30e6", "\u30b6", "\u72ec", "\u81ea", "\u5074", "\u88c5", "\u300c", "\u300d", "\u505c", "\u6b62", "\u4f53", "\u30d4", "\u8c61", "\u7684", "\u7279", "\u5225", "\u30b4", "\u7bb1", "\u6271", "\u5207", "\u63d0", "\u4f9b", "\u30bd", "\u5145", "\u76e3", "\u8996", "\u30cb", "\u60c5", "\u5831", "\u62e1", "\u5f35", "\u72b6", "\u614b", "\u6a29", "\u6240", "\u6709", "\u8005", "\u65e5", "\u3080", "\u53e4", "\u6c42", "\u914d", "\u63a8", "\u6e2c", "\u671f", "\u6c7a", "\u9006", "\u30d3", "\u4e00", "\u521d", "\u63a5", "\uff1a", "\u53d7", "\u9001", "\u5f85", "\u8ffd", "\u3061", "\u88dc", "\u52a9", "\u62bd", "\u7d44", "\u96a0", "\u89a7", "\u3070", "\u7d0d", "\u7701", "\u7565", "\u3069", "\u8907", "\u1295", "\u1270", "\u1240", "\u1265", "\u120f", "\u120d", "\u12e8", "\u12a5", "\u130d", "\u12f3", "\u1263", "\u12ed", "\u1235", "\u121d", "\u134b", "\u1208", "\u121b", "\u1260", "\u1205", "\u1275", "\u12a0", "\u1366", "\u1230", "\u122b", "\u133d", "\u1211", "\u134d", "\u1236", "\u12a8", "\u00c3", "\u015c", "\u011d", "\u0109", "\u015d", "\u016d", "\u0408", "\u0b17", "\u0b41", "\u0b23", "\u0b09", "\u0b2a", "\u0b26", "\u0b28", "\u0b07", "\u0b01", "\u0b05", "\u0b4d", "\u0b2f", "\u0b36", "\u0b3f", "\u0b1f", "\u0b47", "\u0b15", "\u0b16", "\u0b4b", "\u0b1c", "\u0b32", "\u0b39", "\u0b38", "\u0b42", "\u0b1a", "\u0b06", "\u0b25", "\u0b2e", "\u0b27", "\u0b1b", "\u0b21", "\u0b19", "\u0b4c", "\u0b2c", "\u0b48", "\u0b33", "\u0b0f", "\u0b5f", "\u0b1e", "\u0b37", "\u0b2b", "\u0b02", "\u0b40", "\u0b22", "\u0b3c", "\u0b20", "\u0b68", "\u0b69", "\u0b6a", "\u0b03", "\u0b43", "\u0b71", "\u0b6e", "\u0b67", "\u0b6c", "\u0964", "\u0b18", "\u011f", "\u015e", "\u0919", "\u05de", "\u05b8", "\u05d3", "\u05e0", "\u05e2", "\u05e4", "\u05bf", "\u05d8", "\u05e6", "\u05f2", "\u05db", "\u05df", "\u05f0", "\u05b7", "\u05da", "\u05d1", "\u05be", "\u05d2", "\u05e1", "\u05e5", "\u05f1", "\u05ea", "\u05d4", "\u05e3", "\u05d6", "\u05bc", "\u0918", "\u0933", "\u0945", "\u090a", "\u091d", "\u1ed9", "\u1ea5", "\u01b0", "\u1edd", "\u1ebf", "\u1ed1", "\u1ee7", "\u1ebb", "\u1ee3", "\u1ead", "\u1ec7", "\u1ee5", "\u1eef", "\u1ecb", "\u1ec3", "\u1eb7", "\u1ee9", "\u0103", "\u1ed7", "\u1edf", "\u1ef1", "\u1eb1", "\u1ea3", "\u1ed5", "\u1eeb", "\u1ea7", "\u1ed3", "\u1eed", "\u1eab", "\u1edb", "\u1ee1", "\u1ecf", "\u1ebd", "\u1ea9", "\u1eaf", "\u1ec9", "\u1ec1", "\u1eb3", "\u01a1", "\u0169", "\u0129", "\u1ecc", "\u0110", "\u1eac", "\u0171", "\u10d5", "\u10da", "\u10d0", "\u10d3", "\u10d8", "\u10db", "\u10e0", "\u10e1", "\u10ed", "\u10dc", "\u10dd", "\u10e3", "\u10e2", "\u10d1", "\u10d7", "\u10eb", "\u10ea", "\u10e7", "\u10e8", "\u10d9", "\u10e4", "\u10de", "\u10ef", "\u10ee", "\u10e5", "\u10d6", "\u10ec", "\u10e9", "\u10e6", "\u021b", "\u0218", "\u021a", "\u00ce", "\u0985", "\u09aa", "\u09cd", "\u09af", "\u09b6", "\u09bf", "\u0997", "\u09c1", "\u09a3", "\u09a6", "\u09a5", "\u09c7", "\u09cb", "\u09f1", "\u09a8", "\u099a", "\u09b9", "\u0986", "\u0995", "\u09c8", "\u099b", "\u099e", "\u099c", "\u09a7", "\u0987", "\u09ae", "\u09b8", "\u09df", "\u09b7", "\u099f", "\u09a0", "\u09c0", "\u09c2", "\u09c3", "\u09ab", "\u0996", "\u0981", "\u098f", "\u09dd", "\u09a1", "\u0999", "\u0993", "\u0983", "\u0989", "\u09e8", "\u09e9", "\u09ea", "\u0998", "\u09e7", "\u09e6", "\u09dc", "\u098a", "\u09ce", "\u09eb", "\u203a", "\u011e", "\u0175", "\u0e1e", "\u0e1a", "\u0e41", "\u0e15", "\u0e23", "\u0e34", "\u0e27", "\u0e4c", "\u0e35", "\u0e48", "\u0e49", "\u0e07", "\u0e01", "\u0e32", "\u0e2a", "\u0e33", "\u0e2b", "\u0e31", "\u0e25", "\u0e40", "\u0e19", "\u0e47", "\u0e02", "\u0e13", "\u0e30", "\u0e20", "\u0e43", "\u0e1f", "\u0e0a", "\u0e14", "\u0e39", "\u0e38", "\u0e42", "\u0e1b", "\u0e37", "\u0e08", "\u0e16", "\u0e1c", "\u0e0b", "\u0e2e", "\u0e18", "\u0e0d", "\u0e29", "\u0e36", "\u0e12", "\u0e28", "\u0e10", "\u0e46", "\u0e1d", "\u015b", "\u0105", "\u0119", "\u0142", "\u017c", "\u017a", "\u017b", "\u0144", "\u015a", "\u0a10", "\u0a32", "\u0a40", "\u0a2e", "\u0a48", "\u0a02", "\u0a1f", "\u0a08", "\u0a17", "\u0a41", "\u0a23", "\u0a28", "\u0a39", "\u0a71", "\u0a3f", "\u0a06", "\u0a4b", "\u0a5c", "\u0a26", "\u0a38", "\u0a35", "\u0a1a", "\u0a21", "\u0a07", "\u0a15", "\u0a22", "\u0a2c", "\u0a2b", "\u0a2a", "\u0a4c", "\u0a1c", "\u0a42", "\u0a3c", "\u0a4d", "\u0a47", "\u0a70", "\u0a09", "\u0a27", "\u0a20", "\u0a05", "\u0a16", "\u0a36", "\u0a1d", "\u0a1b", "\u0a5b", "\u0a33", "\u0a25", "\u0a2f", "\u0a69", "\u0a68", "\u0a67", "\u0a66", "\u0a13", "\u0a6d", "\u0a0a", "\u0a6c", "\u0a98", "\u0a9f", "\u0a95", "\u0aae", "\u0ac7", "\u0a85", "\u0aa8", "\u0abf", "\u0a9a", "\u0acd", "\u0a9b", "\u0ac0", "\u0aaf", "\u0ab2", "\u0ab7", "\u0aa3", "\u0ac1", "\u0a82", "\u0ab3", "\u0ab9", "\u0a97", "\u0a88", "\u0a8f", "\u0aa1", "\u0a93", "\u0acb", "\u0aac", "\u0aab", "\u0aaa", "\u0aa5", "\u0a9c", "\u0ab5", "\u0a96", "\u0ac2", "\u0ab8", "\u0a86", "\u0aa7", "\u0ab6", "\u0a87", "\u0ac8", "\u0aa6", "\u0aa2", "\u0a89", "\u0acc", "\u0a83", "\u0a9e", "\u0aa0", "\u0ae9", "\u0ae8", "\u0ae7", "\u0ae6", "\u0a9d", "\u0aee", "\u0aec", "\u0ac3", "\u039c", "\u03b7", "\u03b1", "\u03bd", "\u03bc", "\u03cc", "\u03bf", "\u03b3", "\u03ce", "\u03c1", "\u03b9", "\u03c3", "\u03c4", "\u03c7", "\u03af", "\u03a4", "\u03b4", "\u03b2", "\u03ad", "\u03b8", "\u03ba", "\u0391", "\u03c0", "\u0394", "\u03c2", "\u03c9", "\u03a5", "\u03ac", "\u03ae", "\u03cd", "\u039a", "\u03c6", "\u03be", "\u0397", "\u03b6", "\u03a3", "\u03c8", "\u039f", "\u0395", "\u03a0", "\u0386", "\u03a7", "\u0399", "\u039b", "\u0393", "\u03a1", "\u0990", "\u04af", "\u04e8", "\u04e9", "\u0425", "\u0b8e", "\u0ba3", "\u0bc1", "\u0bb1", "\u0b89", "\u0bae", "\u0bb5", "\u0b92", "\u0b9f", "\u0bb3", "\u0b85", "\u0ba9", "\u0bcb", "\u0b8f", "\u0bc7", "\u0bca", "\u0bb4", "\u0bc6", "\u0b90", "\u0b86", "\u0bc0", "\u0b93", "\u0b9c", "\u0b88", "\u0b83", "\u0bb8", "\u0b8a", "\u5143", "\u672a", "\u9810", "\u5c6c", "\u627e", "\u6a19", "\u7c64", "\uff0c", "\u61c9", "\u70ba", "\u8cc7", "\u6599", "\u9304", "\u6548", "\u6a94", "\u6848", "\u5df2", "\u7d93", "\u6c92", "\u79c1", "\u65d7", "\u5e5f", "\u7fa3", "\u7a0b", "\u8a3b", "\u518a", "\u652f", "\u63f4", "\u5c07", "\u7b26", "\u8f49", "\u81f3", "\u8f38", "\u9047", "\u4f4d", "\u767c", "\u932f", "\u8aa4", "\u7d50", "\u675f", "\u4ecd", "\u5099", "\u4e32", "\u662f", "\u7d55", "\u5c0d", "\u672c", "\u6a5f", "\u4e3b", "\u7a31", "\u8df3", "\u8def", "\u5f91", "\u555f", "\u7f6e", "\u4f86", "\u8b80", "\u592a", "\u904e", "\u5de8", "\u7372", "\u7531", "\u5efa", "\u7acb", "\u5beb", "\u95dc", "\u6a23", "\u5305", "\u865f", "\u5668", "\u7de9", "\u885d", "\u5340", "\u4e4b", "\u7ba1", "\u9053", "\u7b2c", "\u7de8", "\u78bc", "\u53c3", "\u5167", "\u8a72", "\u6578", "\uff08", "\u5982", "\uff09", "\uff1b", "\u5f88", "\u4f46", "\u5b83", "\u8b8a", "\u5be6", "\u9ad4", "\u8acb", "\u4efb", "\u610f", "\u9808", "\u9019", "\u4efd", "\u53ea", "\u5c0b", "\u65bc", "\u6216", "\u4e5f", "\u8a31", "\u7576", "\u503c", "\u5141", "\u5c16", "\u89d2", "\u62ec", "\u8655", "\u640d", "\u6bc0", "\u7269", "\u61b6", "\u8017", "\u76e1", "\u56de", "\u6eaf", "\u6b64", "\u6a21", "\u6bd4", "\u53cd", "\u5411", "\u689d", "\u905e", "\u5efb", "\u8fa8", "\u7740", "\u88cf", "\u985b", "\u5012", "\u7f3a", "\u5c11", "\u812b", "\u570d", "\u6771", "\u897f", "\u91cd", "\u547d", "\u55ae", "\u982d", "\u5224", "\u65b7", "\u5ea6", "\u5169", "\u77e5", "\u53eb", "\u5708", "\u5177", "\u76f8", "\u81f4", "\u9078", "\u96a8", "\u5f27", "\u975e", "\u96f6", "\u6ea2", "\u6d41", "\u8b6f", "\u5148", "\u6838", "\u5eab", "\u4f73", "\u4ee4", "\u5176", "\u5c31", "\u5f9e", "\u526f", "\u548c", "\u6e9d", "\u57f7", "\u5354", "\u8a08", "\u884d", "\u5c0e", "\u5920", "\u8aaa", "\u986f", "\u7d66", "\u96d9", "\u7cbe", "\u6d6e", "\u9ede", "\u9375", "\u88ab", "\u908f", "\u8f2f", "\u50b3", "\u6d88", "\u684c", "\u9762", "\u6b04", "\u593e", "\u88dd", "\u9000", "\u529f", "\u5a92", "\u8f2a", "\u8a62", "\u7248", "\u639b", "\u8f09", "\u88fd", "\u6b8a", "\u6536", "\u7b52", "\u5132", "\u5c1a", "\u8209", "\u7570", "\u826f", "\u641c", "\u622a", "\u77ed", "\u4ecb", "\u6b78", "\u5716", "\u5730", "\u7cfb", "\u7d71", "\u6839", "\u5553", "\u9802", "\u5c64", "\u7d1a", "\u5ef6", "\u4f38", "\u72c0", "\u63cf", "\u8ff0", "\u6b0a", "\u64c1", "\u4fee", "\u523b", "\u806f", "\u820a", "\u66ab", "\u9663", "\u5378", "\u5bb9", "\u6b65", "\u6e90", "\u670d", "\u52d9", "\u7d00", "\u9060", "\u807d", "\u7d81", "\u7dda", "\u5019", "\u6cc1", "\u606f", "\u7a97", "\u90f5", "\u63a7", "\u5236", "\u537b", "\u8f14", "\u6388", "\u96b1", "\u85cf", "\u679c", "\u50cf", "\u994b", "\u5426", "\u7e2e", "\u5247", "\u5ffd", "\u0165", "\u013e", "\u010f", "\u013a", "\u013d", "\u0148", "\u013c", "\u0146", "\u0db8", "\u0dd6", "\u0dba", "\u0dc3", "\u0db3", "\u0dc4", "\u0db6", "\u0db4", "\u0ddc", "\u0dbb", "\u0dad", "\u0dca", "\u0dd4", "\u0db1", "\u0dc0", "\u0dd2", "\u0dc1", "\u0dda", "\u0dc2", "\u0dab", "\u0dd9", "\u0dd0", "\u0da7", "\u0d9c", "\u0dc5", "\u0d87", "\u0daf", "\u0db7", "\u0dd8", "\u0db0", "\u0ddd", "\u0dd3", "\u0d85", "\u0d89", "\u0d86", "\u0da9", "\u0d9b", "\u0d8b", "\u045c", "\u0453", "\u0403", "\u0c98", "\u0c9f", "\u0c95", "\u0ccd", "\u0cc6", "\u0c85", "\u0ca8", "\u0caa", "\u0cc7", "\u0cb7", "\u0cbf", "\u0c97", "\u0cc1", "\u0ca3", "\u0cb5", "\u0cb6", "\u0ca6", "\u0caf", "\u0cb2", "\u0c9a", "\u0c9b", "\u0cb8", "\u0c92", "\u0cb3", "\u0c82", "\u0ccb", "\u0cae", "\u0cac", "\u0ca1", "\u0c88", "\u0c96", "\u0cc2", "\u0cb9", "\u0c9c", "\u0c8e", "\u0cca", "\u0cab", "\u0c86", "\u0cc8", "\u0ca7", "\u0ca5", "\u0cc0", "\u0c93", "\u0c89", "\u0ca0", "\u0c87", "\u0c83", "\u0ccc", "\u0c8f", "\u0c9e", "\u0cc3", "\u0c8a", "\u0159", "\u011b", "\u016f", "\u0158", "\uc608", "\uc0c1", "\uce58", "\ubabb", "\ud558", "\uac8c", "\uc5d8", "\ub9ac", "\uba3c", "\ud2b8", "\uc5d0", "\uc560", "\ubdf0", "\uac00", "\uc788", "\uc2b5", "\ub2c8", "\ub2e4", "\uc5c6", "\ud0dc", "\uadf8", "\uc5b4", "\uc57c", "\ud569", "\uc548", "\ub370", "\uc774", "\ud130", "\ub514", "\ub809", "\ud1a0", "\uc62c", "\ubc14", "\ub978", "\ubd81", "\ub9c8", "\ud06c", "\ud30c", "\uc77c", "\ub300", "\ubbf8", "\ud0c0", "\uc785", "\uac1c", "\uc778", "\ud50c", "\ub798", "\ub8f9", "\uc124", "\uc815", "\ub418", "\uc9c0", "\uc54a", "\ub984", "\ub5a4", "\ud504", "\ub85c", "\ub7a8", "\ub3c4", "\ub97c", "\ub4f1", "\ub85d", "\uc558", "\uc744", "\uc0ac", "\uc6a9", "\ud574", "\uc2e4", "\ud589", "\uc904", "\ud655", "\uc7a5", "\uae30", "\ud328", "\ud588", "\ubb38", "\uc790", "\uc14b", "\uc11c", "\uc73c", "\ubcc0", "\ud658", "\uc740", "\uc6d0", "\ub294", "\uc5f4", "\uc218", "\ub825", "\uc798", "\ub41c", "\uc21c", "\uc911", "\uc624", "\ub958", "\uc758", "\ub05d", "\ubd80", "\ubd84", "\uc801", "\ucf54", "\ub4dc", "\uccb4", "\ud568", "\uc2a4", "\ud0a4", "\uc808", "\uacbd", "\uc544", "\ub2d9", "\uceec", "\ub4e4", "\uac08", "\uc5c8", "\ud638", "\ucf00", "\uc5ec", "\uc77d", "\ud560", "\ub2f9", "\ub108", "\ubb34", "\ud07d", "\uc18d", "\uc838", "\uafb8", "\ub9cc", "\uc4f0", "\ub2eb", "\uc874", "\uc6b8", "\ud15c", "\uba74", "\ub429", "\uc2ec", "\ubcfc", "\ub9ad", "\ub9c1", "\uc74c", "\ubc84", "\ud37c", "\ub0a8", "\uaca8", "\ub460", "\ucc44", "\ub110", "\ub0c4", "\ub9e4", "\ud551", "\uc9f8", "\ub529", "\ud14d", "\ub974", "\uad6c", "\uc11d", "\ucc38", "\uc870", "\uc22b", "\uc368", "\ud074", "\uc138", "\ucf5c", "\ub860", "\ub098", "\uc6b0", "\uc5d4", "\ud2f0", "\uc2dc", "\uc791", "\ub824", "\uace0", "\uacf3", "\uac83", "\ub7f0", "\ub77c", "\uc2ed", "\uc751", "\ud5c8", "\ube44", "\ucc3e", "\uc54c", "\ub3d9", "\ubc88", "\uc5ed", "\uc4f8", "\ube48", "\ub0b4", "\ud639", "\uac70", "\uc640", "\uc4f4", "\uac12", "\ub54c", "\ub530", "\uc634", "\ud45c", "\ud614", "\ud604", "\uc7ac", "\uacf5", "\ubc31", "\uac11", "\ub7fd", "\ub0ac", "\ub9c9", "\ub358", "\uc8fc", "\ucc98", "\uc190", "\ub610", "\uba54", "\ubaa8", "\uc871", "\ucd94", "\ucd5c", "\ub2ec", "\ud134", "\ud56d", "\ubaa9", "\ud6c4", "\uc704", "\uac74", "\uadc0", "\uc5c5", "\uac04", "\uafc8", "\uc2dd", "\uc18c", "\ubc97", "\uad04", "\ube60", "\uc84c", "\ud000", "\ubc94", "\ubc18", "\ubcf5", "\ub124", "\uc784", "\ube0c", "\uaddc", "\ubcf4", "\ub8e9", "\uc158", "\uae38", "\ud615", "\ub79c", "\ub9ce", "\uc804", "\ucd9c", "\ud788", "\uae00", "\uac19", "\uae41", "\uc9c4", "\ub7ec", "\uad00", "\uc635", "\ub458", "\uc2fc", "\ub2cc", "\ub118", "\uac14", "\uac80", "\ub9de", "\ubc1c", "\uc0dd", "\ud654", "\uafc0", "\ub2a5", "\ub9d0", "\ub5bb", "\uba85", "\ub839", "\uc178", "\ud1b5", "\uc2e0", "\uc6c0", "\ud3ec", "\ud544", "\uc694", "\ubc16", "\ubc95", "\ubd05", "\ub4e0", "\ubc30", "\uc0c9", "\uc30d", "\ub2e8", "\ubd88", "\uc5b8", "\uae34", "\uce74", "\uc6b4", "\ub9bc", "\ucde8", "\uc885", "\ucc0d", "\ud3f4", "\ub354", "\ud070", "\ub36e", "\ud2b9", "\ud734", "\ub968", "\ub274", "\uba38", "\ub808", "\ud398", "\ucf58", "\ucf13", "\ubcf8", "\ub8e8", "\uc81c", "\ub9b4", "\uc62e", "\ub9bd", "\uad8c", "\uc720", "\uac01", "\uc811", "\uadfc", "\ucee8", "\uc678", "\ub00c", "\uccad", "\uacc4", "\ub0bc", "\ucd08", "\uaca9", "\uc5f0", "\uacb0", "\ubc1b", "\ubc00", "\ub9b0", "\uc708", "\uc988", "\ub864", "\ub2c9", "\uacfc", "\uc228", "\ub7fc", "\uc644", "\u0117", "\u0173", "\u012f", "\u0179", "\u0141", "\u7b7e", "\u9700", "\u65e0", "\u636e", "\u5f55", "\u7ecf", "\u4e49", "\u7c7b", "\u5fd7", "\u8bbe", "\u7ec4", "\u6ca1", "\u4e3a", "\u5e94", "\u6ce8", "\u518c", "\u5f00", "\u8d25", "\u4ece", "\u8f6c", "\u6362", "\u6253", "\u8f93", "\u73b0", "\u8fc7", "\u9519", "\u5c3d", "\u540e", "\u5907", "\u7edd", "\u5bf9", "\u5f84", "\u65f6", "\u53d1", "\u8bef", "\u8282", "\u8bfb", "\u83b7", "\u5c06", "\u521b", "\u5199", "\u5173", "\u95ed", "\u5220", "\u677f", "\u8be5", "\u94fe", "\u51fd", "\u8fdb", "\u7f13", "\u51b2", "\u7559", "\u7ec8", "\u4e8e", "\u6620", "\u5c04", "\u4e2a", "\u7f16", "\u7801", "\u79f0", "\u7ed3", "\u60a8", "\u800c", "\u53c8", "\u5b9e", "\u8fd9", "\u53d8", "\u8bb8", "\u6863", "\u987b", "\u5934", "\u6765", "\u8bb0", "\u7d27", "\u8ddf", "\u7ed9", "\u8d4b", "\u4ec5", "\u8fd8", "\u53f3", "\u91ca", "\u5904", "\u8fbe", "\u5339", "\u9879", "\u9012", "\u5f52", "\u95f4", "\u8bc6", "\u522b", "\u98a0", "\u8303", "\u56f4", "\u590d", "\u5219", "\u957f", "\u65ad", "\u8a00", "\u786e", "\u4e24", "\u8c03", "\u5bfc", "\u5faa", "\u73af", "\u9009", "\u82b1", "\u9884", "\u8bd1", "\u533a", "\u68c0", "\u67e5", "\u5e93", "\u4f18", "\u671b", "\u516d", "\u4e22", "\u4ed6", "\u4e0e", "\u8baf", "\u6267", "\u5f02", "\u591f", "\u5e2e", "\u663e", "\u53cc", "\u952e", "\u666e", "\u70b9", "\u5e03", "\u5c14", "\u4f20", "\u8ba1", "\u6237", "\u5939", "\u9a71", "\u63a2", "\u5f39", "\u8f6e", "\u8be2", "\u6302", "\u8f7d", "\u5783", "\u573e", "\u5377", "\u679a", "\u4e3e", "\u53e3", "\u5957", "\u9ed8", "\u8ba4", "\u76d1", "\u89c6", "\u7edf", "\u653e", "\u9876", "\u7ea7", "\u6269", "\u6001", "\u6743", "\u8bbf", "\u95ee", "\u542f", "\u65e7", "\u62f7", "\u8d1d", "\u4e34", "\u8bf7", "\u731c", "\u6d4b", "\u52a1", "\u6682", "\u534f", "\u8bae", "\u64a4", "\u9500", "\u8fdc", "\u542c", "\u7ed1", "\u8fde", "\u51b3", "\u589e", "\u5374", "\u8f85", "\u6458", "\u9690", "\u90fd", "\u628a", "\u7f29", "\u521a", "\u0d0e", "\u0d32", "\u0d2e", "\u0d46", "\u0d28", "\u0d4d", "\u0d31", "\u0d3f", "\u0d05", "\u0d2a", "\u0d40", "\u0d15", "\u0d37", "\u0d2f", "\u0d38", "\u0d35", "\u0d36", "\u0d47", "\u0d23", "\u0d1f", "\u0d41", "\u0d17", "\u0d1a", "\u0d09", "\u0d33", "\u0d21", "\u0d27", "\u0d2c", "\u0d2b", "\u0d42", "\u0d4a", "\u0d12", "\u0d4b", "\u0d1c", "\u0d07", "\u0d48", "\u0d39", "\u0d19", "\u0d25", "\u0d06", "\u0d43", "\u0d34", "\u0d26", "\u0d16", "\u0d13", "\u0d1e", "\u0d08", "\u0d14", "\u0d4c", "\u0d0f", "\u0d10", "\u7fa4", "\u8457", "\u88e1", "\u8a02", "\u8a9e", "\u0307", "\u0345", "\u0314", "\u00cc", "\u0300", "\u0301", "\u0128", "\u0303", "\u0328", "\u012e", "\ufb04", "\u00ca", "\u00d1", "\u00d4", "\u0178", "\u0100", "\u0102", "\u0104", "\u0106", "\u0108", "\u010a", "\u010b", "\u010e", "\u0112", "\u0114", "\u0115", "\u0116", "\u0118", "\u011a", "\u011c", "\u0120", "\u0122", "\u0123", "\u0124", "\u0125", "\u0126", "\u0127", "\u012c", "\u012d", "\u0132", "\u0133", "\u0134", "\u0135", "\u0136", "\u0137", "\u0138", "\u0139", "\u013b", "\u013f", "\u0140", "\u0143", "\u0145", "\u0147", "\u0149", "\u02bc", "\u014a", "\u014b", "\u014c", "\u014e", "\u0150", "\u0152", "\u0153", "\u0154", "\u0155", "\u0156", "\u0157", "\u0162", "\u0163", "\u0164", "\u0166", "\u0167", "\u0168", "\u016a", "\u016c", "\u016e", "\u0170", "\u0172", "\u0174", "\u0176", "\u0177", "\u017f", "\u0180", "\u0243", "\u0181", "\u0253", "\u0182", "\u0183", "\u0184", "\u0185", "\u0186", "\u0254", "\u0187", "\u0188", "\u0189", "\u0256", "\u018a", "\u0257", "\u018b", "\u018c", "\u018d", "\u018e", "\u01dd", "\u0190", "\u025b", "\u0191", "\u0192", "\u0193", "\u0260", "\u0194", "\u0263", "\u0195", "\u01f6", "\u0196", "\u0269", "\u0197", "\u0268", "\u0198", "\u0199", "\u019a", "\u023d", "\u019b", "\u019c", "\u026f", "\u019d", "\u0272", "\u019e", "\u0220", "\u019f", "\u0275", "\u01a0", "\u01a2", "\u01a3", "\u01a4", "\u01a5", "\u01a6", "\u0280", "\u01a7", "\u01a8", "\u01a9", "\u0283", "\u01aa", "\u01ab", "\u01ac", "\u01ad", "\u01ae", "\u0288", "\u01af", "\u01b1", "\u028a", "\u01b2", "\u028b", "\u01b3", "\u01b4", "\u01b5", "\u01b6", "\u01b7", "\u0292", "\u01b8", "\u01b9", "\u01ba", "\u01bc", "\u01bd", "\u01be", "\u01bf", "\u01f7", "\u01c4", "\u01c6", "\u01c5", "\u01c7", "\u01c9", "\u01c8", "\u01ca", "\u01cc", "\u01cb", "\u01cd", "\u01cf", "\u01d1", "\u01d3", "\u01d5", "\u01d6", "\u01d7", "\u01d8", "\u01d9", "\u01da", "\u01db", "\u01dc", "\u01de", "\u01df", "\u01e0", "\u01e1", "\u01e2", "\u01e3", "\u01e4", "\u01e5", "\u01e6", "\u01e7", "\u01e8", "\u01e9", "\u01ea", "\u01eb", "\u01ec", "\u01ed", "\u01ee", "\u01ef", "\u01f0", "\u030c", "\u01f1", "\u01f3", "\u01f2", "\u01f4", "\u01f5", "\u01f8", "\u01f9", "\u01fa", "\u01fb", "\u01fc", "\u01fd", "\u01fe", "\u01ff", "\u0200", "\u0201", "\u0202", "\u0203", "\u0204", "\u0205", "\u0206", "\u0207", "\u0208", "\u0209", "\u020a", "\u020b", "\u020c", "\u020d", "\u020e", "\u020f", "\u0210", "\u0211", "\u0212", "\u0213", "\u0214", "\u0215", "\u0216", "\u0217", "\u021c", "\u021d", "\u021e", "\u021f", "\u0221", "\u0222", "\u0223", "\u0224", "\u0225", "\u0226", "\u0227", "\u0228", "\u0229", "\u022a", "\u022b", "\u022c", "\u022d", "\u022e", "\u022f", "\u0230", "\u0231", "\u0232", "\u0233", "\u0234", "\u0235", "\u0236", "\u0237", "\u0238", "\u0239", "\u023a", "\u2c65", "\u023b", "\u023c", "\u023e", "\u2c66", "\u023f", "\u0240", "\u0241", "\u0242", "\u0244", "\u0289", "\u0245", "\u028c", "\u0246", "\u0247", "\u0248", "\u0249", "\u024a", "\u024b", "\u024c", "\u024d", "\u024e", "\u024f", "\u0250", "\u2c6f", "\u0251", "\u2c6d", "\u0252", "\u0255", "\u0258", "\u025a", "\u025c", "\u025d", "\u025e", "\u025f", "\u0261", "\u0262", "\u0264", "\u0265", "\u0266", "\u0267", "\u026a", "\u026b", "\u2c62", "\u026c", "\u026d", "\u026e", "\u0270", "\u0271", "\u2c6e", "\u0273", "\u0274", "\u0276", "\u0277", "\u0278", "\u0279", "\u027a", "\u027b", "\u027c", "\u027d", "\u2c64", "\u027e", "\u027f", "\u0281", "\u0282", "\u0284", "\u0285", "\u0286", "\u0287", "\u028d", "\u028e", "\u028f", "\u0290", "\u0291", "\u0293", "\u0295", "\u0296", "\u0297", "\u0298", "\u0299", "\u029a", "\u029b", "\u029c", "\u029d", "\u029e", "\u029f", "\u02a0", "\u02a1", "\u02a2", "\u02a3", "\u02a4", "\u02a5", "\u02a6", "\u02a7", "\u02a8", "\u02a9", "\u02aa", "\u02ab", "\u02ac", "\u02ad", "\u02ae", "\u02af", "\u0370", "\u0371", "\u0372", "\u0373", "\u0376", "\u0377", "\u037b", "\u03fd", "\u037c", "\u03fe", "\u037d", "\u03ff", "\u0388", "\u0389", "\u038a", "\u038c", "\u038e", "\u038f", "\u0390", "\u0308", "\u0392", "\u0396", "\u0398", "\u039d", "\u039e", "\u03a6", "\u03a8", "\u03a9", "\u03aa", "\u03ca", "\u03ab", "\u03cb", "\u03b0", "\u03cf", "\u03d7", "\u03d0", "\u03d1", "\u03d2", "\u03d3", "\u03d4", "\u03d5", "\u03d6", "\u03d8", "\u03d9", "\u03da", "\u03db", "\u03dc", "\u03dd", "\u03de", "\u03df", "\u03e0", "\u03e1", "\u03e2", "\u03e3", "\u03e4", "\u03e5", "\u03e6", "\u03e7", "\u03e8", "\u03e9", "\u03ea", "\u03eb", "\u03ec", "\u03ed", "\u03ee", "\u03ef", "\u03f0", "\u03f1", "\u03f2", "\u03f9", "\u03f3", "\u03f4", "\u03f5", "\u03f7", "\u03f8", "\u03fa", "\u03fb", "\u03fc", "\u0400", "\u0450", "\u0401", "\u0402", "\u0404", "\u0405", "\u0455", "\u0407", "\u0409", "\u040a", "\u040b", "\u040c", "\u040d", "\u045d", "\u040e", "\u040f", "\u045f", "\u0429", "\u042a", "\u042b", "\u0460", "\u0461", "\u0462", "\u0463", "\u0464", "\u0465", "\u0466", "\u0467", "\u0468", "\u0469", "\u046a", "\u046b", "\u046c", "\u046d", "\u046e", "\u046f", "\u0470", "\u0471", "\u0472", "\u0473", "\u0474", "\u0475", "\u0476", "\u0477", "\u0478", "\u0479", "\u047a", "\u047b", "\u047c", "\u047d", "\u047e", "\u047f", "\u0480", "\u0481", "\u048a", "\u048b", "\u048c", "\u048d", "\u048e", "\u048f", "\u0490", "\u0491", "\u0492", "\u0493", "\u0494", "\u0495", "\u0496", "\u0497", "\u0498", "\u0499", "\u049a", "\u049c", "\u049d", "\u049e", "\u049f", "\u04a0", "\u04a1", "\u04a2", "\u04a3", "\u04a4", "\u04a5", "\u04a6", "\u04a7", "\u04a8", "\u04a9", "\u04aa", "\u04ab", "\u04ac", "\u04ad", "\u04ae", "\u04b0", "\u04b1", "\u04b2", "\u04b3", "\u04b4", "\u04b5", "\u04b6", "\u04b7", "\u04b8", "\u04b9", "\u04ba", "\u04bb", "\u04bc", "\u04bd", "\u04be", "\u04bf", "\u04c0", "\u04cf", "\u04c1", "\u04c2", "\u04c3", "\u04c4", "\u04c5", "\u04c6", "\u04c7", "\u04c8", "\u04c9", "\u04ca", "\u04cb", "\u04cc", "\u04cd", "\u04ce", "\u04d0", "\u04d1", "\u04d2", "\u04d3", "\u04d4", "\u04d5", "\u04d6", "\u04d7", "\u04d8", "\u04d9", "\u04da", "\u04db", "\u04dc", "\u04dd", "\u04de", "\u04df", "\u04e0", "\u04e1", "\u04e2", "\u04e3", "\u04e4", "\u04e5", "\u04e6", "\u04e7", "\u04ea", "\u04eb", "\u04ec", "\u04ed", "\u04ee", "\u04ef", "\u04f0", "\u04f1", "\u04f2", "\u04f3", "\u04f4", "\u04f5", "\u04f6", "\u04f7", "\u04f8", "\u04f9", "\u04fa", "\u04fb", "\u04fc", "\u04fd", "\u04fe", "\u04ff", "\u0500", "\u0501", "\u0502", "\u0503", "\u0504", "\u0505", "\u0506", "\u0507", "\u0508", "\u0509", "\u050a", "\u050b", "\u050c", "\u050d", "\u050e", "\u050f", "\u0510", "\u0511", "\u0512", "\u0513", "\u0514", "\u0515", "\u0516", "\u0517", "\u0518", "\u0519", "\u051a", "\u051b", "\u051c", "\u051d", "\u051e", "\u051f", "\u0520", "\u0521", "\u0522", "\u0523", "\u0531", "\u0532", "\u0533", "\u0534", "\u0535", "\u0536", "\u0566", "\u0537", "\u0538", "\u0539", "\u053a", "\u056a", "\u053b", "\u053c", "\u053d", "\u053e", "\u0540", "\u0571", "\u0542", "\u0543", "\u0573", "\u0544", "\u0545", "\u0546", "\u0547", "\u0577", "\u0548", "\u054a", "\u054b", "\u054c", "\u054e", "\u054f", "\u0550", "\u0552", "\u0554", "\u0555", "\u10a0", "\u2d00", "\u10a1", "\u2d01", "\u10a2", "\u2d02", "\u10a3", "\u2d03", "\u10a4", "\u2d04", "\u10a5", "\u2d05", "\u10a6", "\u2d06", "\u10a7", "\u2d07", "\u10a8", "\u2d08", "\u10a9", "\u2d09", "\u10aa", "\u2d0a", "\u10ab", "\u2d0b", "\u10ac", "\u2d0c", "\u10ad", "\u2d0d", "\u10ae", "\u2d0e", "\u10af", "\u2d0f", "\u10b0", "\u2d10", "\u10b1", "\u2d11", "\u10b2", "\u2d12", "\u10b3", "\u2d13", "\u10b4", "\u2d14", "\u10b5", "\u2d15", "\u10b6", "\u2d16", "\u10b7", "\u2d17", "\u10b8", "\u2d18", "\u10b9", "\u2d19", "\u10ba", "\u2d1a", "\u10bb", "\u2d1b", "\u10bc", "\u2d1c", "\u10bd", "\u2d1d", "\u10be", "\u2d1e", "\u10bf", "\u2d1f", "\u10c0", "\u2d20", "\u10c1", "\u2d21", "\u10c2", "\u2d22", "\u10c3", "\u2d23", "\u10c4", "\u2d24", "\u10c5", "\u2d25", "\u1d00", "\u1d01", "\u1d02", "\u1d03", "\u1d04", "\u1d05", "\u1d06", "\u1d07", "\u1d08", "\u1d09", "\u1d0a", "\u1d0b", "\u1d0c", "\u1d0d", "\u1d0e", "\u1d0f", "\u1d10", "\u1d11", "\u1d12", "\u1d13", "\u1d14", "\u1d15", "\u1d16", "\u1d17", "\u1d18", "\u1d19", "\u1d1a", "\u1d1b", "\u1d1c", "\u1d1d", "\u1d1e", "\u1d1f", "\u1d20", "\u1d21", "\u1d22", "\u1d23", "\u1d24", "\u1d25", "\u1d26", "\u1d27", "\u1d28", "\u1d29", "\u1d2a", "\u1d2b", "\u1d62", "\u1d63", "\u1d64", "\u1d65", "\u1d66", "\u1d67", "\u1d68", "\u1d69", "\u1d6a", "\u1d6b", "\u1d6c", "\u1d6d", "\u1d6e", "\u1d6f", "\u1d70", "\u1d71", "\u1d72", "\u1d73", "\u1d74", "\u1d75", "\u1d76", "\u1d77", "\u1d79", "\ua77d", "\u1d7a", "\u1d7b", "\u1d7c", "\u1d7d", "\u2c63", "\u1d7e", "\u1d7f", "\u1d80", "\u1d81", "\u1d82", "\u1d83", "\u1d84", "\u1d85", "\u1d86", "\u1d87", "\u1d88", "\u1d89", "\u1d8a", "\u1d8b", "\u1d8c", "\u1d8d", "\u1d8e", "\u1d8f", "\u1d90", "\u1d91", "\u1d92", "\u1d93", "\u1d94", "\u1d95", "\u1d96", "\u1d97", "\u1d98", "\u1d99", "\u1d9a", "\u1e00", "\u1e01", "\u1e02", "\u1e03", "\u1e04", "\u1e05", "\u1e06", "\u1e07", "\u1e08", "\u1e09", "\u1e0a", "\u1e0b", "\u1e0c", "\u1e0d", "\u1e0e", "\u1e0f", "\u1e10", "\u1e11", "\u1e12", "\u1e13", "\u1e14", "\u1e15", "\u1e16", "\u1e17", "\u1e18", "\u1e19", "\u1e1a", "\u1e1b", "\u1e1c", "\u1e1d", "\u1e1e", "\u1e1f", "\u1e20", "\u1e21", "\u1e22", "\u1e23", "\u1e24", "\u1e25", "\u1e26", "\u1e27", "\u1e28", "\u1e29", "\u1e2a", "\u1e2b", "\u1e2c", "\u1e2d", "\u1e2e", "\u1e2f", "\u1e30", "\u1e31", "\u1e32", "\u1e33", "\u1e34", "\u1e35", "\u1e36", "\u1e37", "\u1e38", "\u1e39", "\u1e3a", "\u1e3b", "\u1e3c", "\u1e3d", "\u1e3e", "\u1e3f", "\u1e40", "\u1e41", "\u1e42", "\u1e43", "\u1e44", "\u1e46", "\u1e47", "\u1e48", "\u1e49", "\u1e4a", "\u1e4b", "\u1e4c", "\u1e4d", "\u1e4e", "\u1e4f", "\u1e50", "\u1e51", "\u1e52", "\u1e53", "\u1e54", "\u1e55", "\u1e56", "\u1e57", "\u1e58", "\u1e59", "\u1e5a", "\u1e5b", "\u1e5c", "\u1e5d", "\u1e5e", "\u1e5f", "\u1e60", "\u1e61", "\u1e62", "\u1e64", "\u1e65", "\u1e66", "\u1e67", "\u1e68", "\u1e69", "\u1e6a", "\u1e6b", "\u1e6c", "\u1e6e", "\u1e6f", "\u1e70", "\u1e71", "\u1e72", "\u1e73", "\u1e74", "\u1e75", "\u1e76", "\u1e77", "\u1e78", "\u1e79", "\u1e7a", "\u1e7b", "\u1e7c", "\u1e7d", "\u1e7e", "\u1e7f", "\u1e80", "\u1e81", "\u1e82", "\u1e83", "\u1e84", "\u1e85", "\u1e86", "\u1e87", "\u1e88", "\u1e89", "\u1e8a", "\u1e8b", "\u1e8c", "\u1e8d", "\u1e8e", "\u1e8f", "\u1e90", "\u1e91", "\u1e93", "\u1e94", "\u1e95", "\u1e96", "\u0331", "\u1e97", "\u1e98", "\u030a", "\u1e99", "\u1e9a", "\u02be", "\u1e9b", "\u1e9c", "\u1e9d", "\u1e9e", "\u1e9f", "\u1ea0", "\u1ea2", "\u1ea4", "\u1ea6", "\u1ea8", "\u1eaa", "\u1eae", "\u1eb0", "\u1eb2", "\u1eb4", "\u1eb5", "\u1eb6", "\u1eb8", "\u1eb9", "\u1eba", "\u1ebc", "\u1ebe", "\u1ec0", "\u1ec2", "\u1ec4", "\u1ec6", "\u1ec8", "\u1eca", "\u1ece", "\u1ed0", "\u1ed2", "\u1ed4", "\u1ed6", "\u1ed8", "\u1eda", "\u1edc", "\u1ede", "\u1ee0", "\u1ee2", "\u1ee4", "\u1ee6", "\u1ee8", "\u1eea", "\u1eec", "\u1eee", "\u1ef0", "\u1ef2", "\u1ef3", "\u1ef4", "\u1ef5", "\u1ef6", "\u1ef7", "\u1ef8", "\u1ef9", "\u1efa", "\u1efb", "\u1efc", "\u1efd", "\u1efe", "\u1eff", "\u1f00", "\u1f08", "\u1f01", "\u1f09", "\u1f02", "\u1f0a", "\u1f03", "\u1f0b", "\u1f04", "\u1f0c", "\u1f05", "\u1f0d", "\u1f06", "\u1f0e", "\u1f07", "\u1f0f", "\u1f10", "\u1f18", "\u1f11", "\u1f19", "\u1f12", "\u1f1a", "\u1f13", "\u1f1b", "\u1f14", "\u1f1c", "\u1f15", "\u1f1d", "\u1f20", "\u1f28", "\u1f21", "\u1f29", "\u1f22", "\u1f2a", "\u1f23", "\u1f2b", "\u1f24", "\u1f2c", "\u1f25", "\u1f2d", "\u1f26", "\u1f2e", "\u1f27", "\u1f2f", "\u1f30", "\u1f38", "\u1f31", "\u1f39", "\u1f32", "\u1f3a", "\u1f33", "\u1f3b", "\u1f34", "\u1f3c", "\u1f35", "\u1f3d", "\u1f36", "\u1f3e", "\u1f37", "\u1f3f", "\u1f40", "\u1f48", "\u1f41", "\u1f49", "\u1f42", "\u1f4a", "\u1f43", "\u1f4b", "\u1f44", "\u1f4c", "\u1f45", "\u1f4d", "\u1f50", "\u0313", "\u1f51", "\u1f59", "\u1f52", "\u1f53", "\u1f5b", "\u1f54", "\u1f55", "\u1f5d", "\u1f56", "\u0342", "\u1f57", "\u1f5f", "\u1f60", "\u1f68", "\u1f61", "\u1f69", "\u1f62", "\u1f6a", "\u1f63", "\u1f6b", "\u1f64", "\u1f6c", "\u1f65", "\u1f6d", "\u1f66", "\u1f6e", "\u1f67", "\u1f6f", "\u1f70", "\u1fba", "\u1f71", "\u1fbb", "\u1f72", "\u1fc8", "\u1f73", "\u1fc9", "\u1f74", "\u1fca", "\u1f75", "\u1fcb", "\u1f76", "\u1fda", "\u1f77", "\u1fdb", "\u1f78", "\u1ff8", "\u1f79", "\u1ff9", "\u1f7a", "\u1fea", "\u1f7b", "\u1feb", "\u1f7c", "\u1ffa", "\u1f7d", "\u1ffb", "\u1f80", "\u1f88", "\u1f81", "\u1f89", "\u1f82", "\u1f8a", "\u1f83", "\u1f8b", "\u1f84", "\u1f8c", "\u1f85", "\u1f8d", "\u1f86", "\u1f8e", "\u1f87", "\u1f8f", "\u1f90", "\u1f98", "\u1f91", "\u1f99", "\u1f92", "\u1f9a", "\u1f93", "\u1f9b", "\u1f94", "\u1f9c", "\u1f95", "\u1f9d", "\u1f96", "\u1f9e", "\u1f97", "\u1f9f", "\u1fa0", "\u1fa8", "\u1fa1", "\u1fa9", "\u1fa2", "\u1faa", "\u1fa3", "\u1fab", "\u1fa4", "\u1fac", "\u1fa5", "\u1fad", "\u1fa6", "\u1fae", "\u1fa7", "\u1faf", "\u1fb0", "\u1fb8", "\u1fb1", "\u1fb9", "\u1fb2", "\u1fb3", "\u1fbc", "\u1fb4", "\u1fb6", "\u1fb7", "\u1fbe", "\u1fc2", "\u1fc3", "\u1fcc", "\u1fc4", "\u1fc6", "\u1fc7", "\u1fd0", "\u1fd8", "\u1fd1", "\u1fd9", "\u1fd2", "\u1fd3", "\u1fd6", "\u1fd7", "\u1fe0", "\u1fe8", "\u1fe1", "\u1fe9", "\u1fe2", "\u1fe3", "\u1fe4", "\u1fe5", "\u1fec", "\u1fe6", "\u1fe7", "\u1ff2", "\u1ff3", "\u1ffc", "\u1ff4", "\u1ff6", "\u1ff7", "\u2071", "\u207f", "\u2102", "\u2107", "\u210a", "\u210b", "\u210c", "\u210d", "\u210e", "\u210f", "\u2110", "\u2111", "\u2112", "\u2113", "\u2115", "\u2119", "\u211a", "\u211b", "\u211c", "\u211d", "\u2124", "\u2126", "\u2128", "\u212a", "\u212b", "\u212c", "\u212d", "\u212f", "\u2130", "\u2131", "\u2132", "\u214e", "\u2133", "\u2134", "\u2139", "\u213c", "\u213d", "\u213e", "\u213f", "\u2145", "\u2146", "\u2147", "\u2148", "\u2149", "\u2183", "\u2184", "\u2c00", "\u2c30", "\u2c01", "\u2c31", "\u2c02", "\u2c32", "\u2c03", "\u2c33", "\u2c04", "\u2c34", "\u2c05", "\u2c35", "\u2c06", "\u2c36", "\u2c07", "\u2c37", "\u2c08", "\u2c38", "\u2c09", "\u2c39", "\u2c0a", "\u2c3a", "\u2c0b", "\u2c3b", "\u2c0c", "\u2c3c", "\u2c0d", "\u2c3d", "\u2c0e", "\u2c3e", "\u2c0f", "\u2c3f", "\u2c10", "\u2c40", "\u2c11", "\u2c41", "\u2c12", "\u2c42", "\u2c13", "\u2c43", "\u2c14", "\u2c44", "\u2c15", "\u2c45", "\u2c16", "\u2c46", "\u2c17", "\u2c47", "\u2c18", "\u2c48", "\u2c19", "\u2c49", "\u2c1a", "\u2c4a", "\u2c1b", "\u2c4b", "\u2c1c", "\u2c4c", "\u2c1d", "\u2c4d", "\u2c1e", "\u2c4e", "\u2c1f", "\u2c4f", "\u2c20", "\u2c50", "\u2c21", "\u2c51", "\u2c22", "\u2c52", "\u2c23", "\u2c53", "\u2c24", "\u2c54", "\u2c25", "\u2c55", "\u2c26", "\u2c56", "\u2c27", "\u2c57", "\u2c28", "\u2c58", "\u2c29", "\u2c59", "\u2c2a", "\u2c5a", "\u2c2b", "\u2c5b", "\u2c2c", "\u2c5c", "\u2c2d", "\u2c5d", "\u2c2e", "\u2c5e", "\u2c60", "\u2c61", "\u2c67", "\u2c68", "\u2c69", "\u2c6a", "\u2c6b", "\u2c6c", "\u2c71", "\u2c72", "\u2c73", "\u2c74", "\u2c75", "\u2c76", "\u2c77", "\u2c78", "\u2c79", "\u2c7a", "\u2c7b", "\u2c7c", "\u2c80", "\u2c81", "\u2c82", "\u2c83", "\u2c84", "\u2c85", "\u2c86", "\u2c87", "\u2c88", "\u2c89", "\u2c8a", "\u2c8b", "\u2c8c", "\u2c8d", "\u2c8e", "\u2c8f", "\u2c90", "\u2c91", "\u2c92", "\u2c93", "\u2c94", "\u2c95", "\u2c96", "\u2c97", "\u2c98", "\u2c99", "\u2c9a", "\u2c9b", "\u2c9c", "\u2c9d", "\u2c9e", "\u2c9f", "\u2ca0", "\u2ca1", "\u2ca2", "\u2ca3", "\u2ca4", "\u2ca5", "\u2ca6", "\u2ca7", "\u2ca8", "\u2ca9", "\u2caa", "\u2cab", "\u2cac", "\u2cad", "\u2cae", "\u2caf", "\u2cb0", "\u2cb1", "\u2cb2", "\u2cb3", "\u2cb4", "\u2cb5", "\u2cb6", "\u2cb7", "\u2cb8", "\u2cb9", "\u2cba", "\u2cbb", "\u2cbc", "\u2cbd", "\u2cbe", "\u2cbf", "\u2cc0", "\u2cc1", "\u2cc2", "\u2cc3", "\u2cc4", "\u2cc5", "\u2cc6", "\u2cc7", "\u2cc8", "\u2cc9", "\u2cca", "\u2ccb", "\u2ccc", "\u2ccd", "\u2cce", "\u2ccf", "\u2cd0", "\u2cd1", "\u2cd2", "\u2cd3", "\u2cd4", "\u2cd5", "\u2cd6", "\u2cd7", "\u2cd8", "\u2cd9", "\u2cda", "\u2cdb", "\u2cdc", "\u2cdd", "\u2cde", "\u2cdf", "\u2ce0", "\u2ce1", "\u2ce2", "\u2ce3", "\u2ce4", "\ua640", "\ua641", "\ua642", "\ua643", "\ua644", "\ua645", "\ua646", "\ua647", "\ua648", "\ua649", "\ua64a", "\ua64b", "\ua64c", "\ua64d", "\ua64e", "\ua64f", "\ua650", "\ua651", "\ua652", "\ua653", "\ua654", "\ua655", "\ua656", "\ua657", "\ua658", "\ua659", "\ua65a", "\ua65b", "\ua65c", "\ua65d", "\ua65e", "\ua65f", "\ua662", "\ua663", "\ua664", "\ua665", "\ua666", "\ua667", "\ua668", "\ua669", "\ua66a", "\ua66b", "\ua66c", "\ua66d", "\ua680", "\ua681", "\ua682", "\ua683", "\ua684", "\ua685", "\ua686", "\ua687", "\ua688", "\ua689", "\ua68a", "\ua68b", "\ua68c", "\ua68d", "\ua68e", "\ua68f", "\ua690", "\ua691", "\ua692", "\ua693", "\ua694", "\ua695", "\ua696", "\ua697", "\ua722", "\ua723", "\ua724", "\ua725", "\ua726", "\ua727", "\ua728", "\ua729", "\ua72a", "\ua72b", "\ua72c", "\ua72d", "\ua72e", "\ua72f", "\ua730", "\ua731", "\ua732", "\ua733", "\ua734", "\ua735", "\ua736", "\ua737", "\ua738", "\ua739", "\ua73a", "\ua73b", "\ua73c", "\ua73d", "\ua73e", "\ua73f", "\ua740", "\ua741", "\ua742", "\ua743", "\ua744", "\ua745", "\ua746", "\ua747", "\ua748", "\ua749", "\ua74a", "\ua74b", "\ua74c", "\ua74d", "\ua74e", "\ua74f", "\ua750", "\ua751", "\ua752", "\ua753", "\ua754", "\ua755", "\ua756", "\ua757", "\ua758", "\ua759", "\ua75a", "\ua75b", "\ua75c", "\ua75d", "\ua75e", "\ua75f", "\ua760", "\ua761", "\ua762", "\ua763", "\ua764", "\ua765", "\ua766", "\ua767", "\ua768", "\ua769", "\ua76a", "\ua76b", "\ua76c", "\ua76d", "\ua76e", "\ua76f", "\ua771", "\ua772", "\ua773", "\ua774", "\ua775", "\ua776", "\ua777", "\ua778", "\ua779", "\ua77a", "\ua77b", "\ua77c", "\ua77e", "\ua77f", "\ua780", "\ua781", "\ua782", "\ua783", "\ua784", "\ua785", "\ua786", "\ua787", "\ua78b", "\ua78c", "\ufb00", "\ufb01", "\ufb02", "\ufb03", "\ufb05", "\ufb06", "\ufb13", "\ufb14", "\ufb15", "\ufb16", "\ufb17", "\uff21", "\uff41", "\uff22", "\uff42", "\uff23", "\uff43", "\uff24", "\uff44", "\uff25", "\uff45", "\uff26", "\uff46", "\uff27", "\uff47", "\uff28", "\uff48", "\uff29", "\uff49", "\uff2a", "\uff4a", "\uff2b", "\uff4b", "\uff2c", "\uff4c", "\uff2d", "\uff4d", "\uff2e", "\uff4e", "\uff2f", "\uff4f", "\uff30", "\uff50", "\uff31", "\uff51", "\uff32", "\uff52", "\uff33", "\uff53", "\uff34", "\uff54", "\uff35", "\uff55", "\uff36", "\uff56", "\uff37", "\uff57", "\uff38", "\uff58", "\uff39", "\uff59", "\uff3a", "\uff5a", "\ud801\udc00", "\ud801\udc28", "\ud801\udc01", "\ud801\udc29", "\ud801\udc02", "\ud801\udc2a", "\ud801\udc03", "\ud801\udc2b", "\ud801\udc04", "\ud801\udc2c", "\ud801\udc05", "\ud801\udc2d", "\ud801\udc06", "\ud801\udc2e", "\ud801\udc07", "\ud801\udc2f", "\ud801\udc08", "\ud801\udc30", "\ud801\udc09", "\ud801\udc31", "\ud801\udc0a", "\ud801\udc32", "\ud801\udc0b", "\ud801\udc33", "\ud801\udc0c", "\ud801\udc34", "\ud801\udc0d", "\ud801\udc35", "\ud801\udc0e", "\ud801\udc36", "\ud801\udc0f", "\ud801\udc37", "\ud801\udc10", "\ud801\udc38", "\ud801\udc11", "\ud801\udc39", "\ud801\udc12", "\ud801\udc3a", "\ud801\udc13", "\ud801\udc3b", "\ud801\udc14", "\ud801\udc3c", "\ud801\udc15", "\ud801\udc3d", "\ud801\udc16", "\ud801\udc3e", "\ud801\udc17", "\ud801\udc3f", "\ud801\udc18", "\ud801\udc40", "\ud801\udc19", "\ud801\udc41", "\ud801\udc1a", "\ud801\udc42", "\ud801\udc1b", "\ud801\udc43", "\ud801\udc1c", "\ud801\udc44", "\ud801\udc1d", "\ud801\udc45", "\ud801\udc1e", "\ud801\udc46", "\ud801\udc1f", "\ud801\udc47", "\ud801\udc20", "\ud801\udc48", "\ud801\udc21", "\ud801\udc49", "\ud801\udc22", "\ud801\udc4a", "\ud801\udc23", "\ud801\udc4b", "\ud801\udc24", "\ud801\udc4c", "\ud801\udc25", "\ud801\udc4d", "\ud801\udc26", "\ud801\udc4e", "\ud801\udc27", "\ud801\udc4f", "\ud835\udc00", "\ud835\udc01", "\ud835\udc02", "\ud835\udc03", "\ud835\udc04", "\ud835\udc05", "\ud835\udc06", "\ud835\udc07", "\ud835\udc08", "\ud835\udc09", "\ud835\udc0a", "\ud835\udc0b", "\ud835\udc0c", "\ud835\udc0d", "\ud835\udc0e", "\ud835\udc0f", "\ud835\udc10", "\ud835\udc11", "\ud835\udc12", "\ud835\udc13", "\ud835\udc14", "\ud835\udc15", "\ud835\udc16", "\ud835\udc17", "\ud835\udc18", "\ud835\udc19", "\ud835\udc1a", "\ud835\udc1b", "\ud835\udc1c", "\ud835\udc1d", "\ud835\udc1e", "\ud835\udc1f", "\ud835\udc20", "\ud835\udc21", "\ud835\udc22", "\ud835\udc23", "\ud835\udc24", "\ud835\udc25", "\ud835\udc26", "\ud835\udc27", "\ud835\udc28", "\ud835\udc29", "\ud835\udc2a", "\ud835\udc2b", "\ud835\udc2c", "\ud835\udc2d", "\ud835\udc2e", "\ud835\udc2f", "\ud835\udc30", "\ud835\udc31", "\ud835\udc32", "\ud835\udc33", "\ud835\udc34", "\ud835\udc35", "\ud835\udc36", "\ud835\udc37", "\ud835\udc38", "\ud835\udc39", "\ud835\udc3a", "\ud835\udc3b", "\ud835\udc3c", "\ud835\udc3d", "\ud835\udc3e", "\ud835\udc3f", "\ud835\udc40", "\ud835\udc41", "\ud835\udc42", "\ud835\udc43", "\ud835\udc44", "\ud835\udc45", "\ud835\udc46", "\ud835\udc47", "\ud835\udc48", "\ud835\udc49", "\ud835\udc4a", "\ud835\udc4b", "\ud835\udc4c", "\ud835\udc4d", "\ud835\udc4e", "\ud835\udc4f", "\ud835\udc50", "\ud835\udc51", "\ud835\udc52", "\ud835\udc53", "\ud835\udc54", "\ud835\udc56", "\ud835\udc57", "\ud835\udc58", "\ud835\udc59", "\ud835\udc5a", "\ud835\udc5b", "\ud835\udc5c", "\ud835\udc5d", "\ud835\udc5e", "\ud835\udc5f", "\ud835\udc60", "\ud835\udc61", "\ud835\udc62", "\ud835\udc63", "\ud835\udc64", "\ud835\udc65", "\ud835\udc66", "\ud835\udc67", "\ud835\udc68", "\ud835\udc69", "\ud835\udc6a", "\ud835\udc6b", "\ud835\udc6c", "\ud835\udc6d", "\ud835\udc6e", "\ud835\udc6f", "\ud835\udc70", "\ud835\udc71", "\ud835\udc72", "\ud835\udc73", "\ud835\udc74", "\ud835\udc75", "\ud835\udc76", "\ud835\udc77", "\ud835\udc78", "\ud835\udc79", "\ud835\udc7a", "\ud835\udc7b", "\ud835\udc7c", "\ud835\udc7d", "\ud835\udc7e", "\ud835\udc7f", "\ud835\udc80", "\ud835\udc81", "\ud835\udc82", "\ud835\udc83", "\ud835\udc84", "\ud835\udc85", "\ud835\udc86", "\ud835\udc87", "\ud835\udc88", "\ud835\udc89", "\ud835\udc8a", "\ud835\udc8b", "\ud835\udc8c", "\ud835\udc8d", "\ud835\udc8e", "\ud835\udc8f", "\ud835\udc90", "\ud835\udc91", "\ud835\udc92", "\ud835\udc93", "\ud835\udc94", "\ud835\udc95", "\ud835\udc96", "\ud835\udc97", "\ud835\udc98", "\ud835\udc99", "\ud835\udc9a", "\ud835\udc9b", "\ud835\udc9c", "\ud835\udc9e", "\ud835\udc9f", "\ud835\udca2", "\ud835\udca5", "\ud835\udca6", "\ud835\udca9", "\ud835\udcaa", "\ud835\udcab", "\ud835\udcac", "\ud835\udcae", "\ud835\udcaf", "\ud835\udcb0", "\ud835\udcb1", "\ud835\udcb2", "\ud835\udcb3", "\ud835\udcb4", "\ud835\udcb5", "\ud835\udcb6", "\ud835\udcb7", "\ud835\udcb8", "\ud835\udcb9", "\ud835\udcbb", "\ud835\udcbd", "\ud835\udcbe", "\ud835\udcbf", "\ud835\udcc0", "\ud835\udcc1", "\ud835\udcc2", "\ud835\udcc3", "\ud835\udcc5", "\ud835\udcc6", "\ud835\udcc7", "\ud835\udcc8", "\ud835\udcc9", "\ud835\udcca", "\ud835\udccb", "\ud835\udccc", "\ud835\udccd", "\ud835\udcce", "\ud835\udccf", "\ud835\udcd0", "\ud835\udcd1", "\ud835\udcd2", "\ud835\udcd3", "\ud835\udcd4", "\ud835\udcd5", "\ud835\udcd6", "\ud835\udcd7", "\ud835\udcd8", "\ud835\udcd9", "\ud835\udcda", "\ud835\udcdb", "\ud835\udcdc", "\ud835\udcdd", "\ud835\udcde", "\ud835\udcdf", "\ud835\udce0", "\ud835\udce1", "\ud835\udce2", "\ud835\udce3", "\ud835\udce4", "\ud835\udce5", "\ud835\udce6", "\ud835\udce7", "\ud835\udce8", "\ud835\udce9", "\ud835\udcea", "\ud835\udceb", "\ud835\udcec", "\ud835\udced", "\ud835\udcee", "\ud835\udcef", "\ud835\udcf0", "\ud835\udcf1", "\ud835\udcf2", "\ud835\udcf3", "\ud835\udcf4", "\ud835\udcf5", "\ud835\udcf6", "\ud835\udcf7", "\ud835\udcf8", "\ud835\udcf9", "\ud835\udcfa", "\ud835\udcfb", "\ud835\udcfc", "\ud835\udcfd", "\ud835\udcfe", "\ud835\udcff", "\ud835\udd00", "\ud835\udd01", "\ud835\udd02", "\ud835\udd03", "\ud835\udd04", "\ud835\udd05", "\ud835\udd07", "\ud835\udd08", "\ud835\udd09", "\ud835\udd0a", "\ud835\udd0d", "\ud835\udd0e", "\ud835\udd0f", "\ud835\udd10", "\ud835\udd11", "\ud835\udd12", "\ud835\udd13", "\ud835\udd14", "\ud835\udd16", "\ud835\udd17", "\ud835\udd18", "\ud835\udd19", "\ud835\udd1a", "\ud835\udd1b", "\ud835\udd1c", "\ud835\udd1e", "\ud835\udd1f", "\ud835\udd20", "\ud835\udd21", "\ud835\udd22", "\ud835\udd23", "\ud835\udd24", "\ud835\udd25", "\ud835\udd26", "\ud835\udd27", "\ud835\udd28", "\ud835\udd29", "\ud835\udd2a", "\ud835\udd2b", "\ud835\udd2c", "\ud835\udd2d", "\ud835\udd2e", "\ud835\udd2f", "\ud835\udd30", "\ud835\udd31", "\ud835\udd32", "\ud835\udd33", "\ud835\udd34", "\ud835\udd35", "\ud835\udd36", "\ud835\udd37", "\ud835\udd38", "\ud835\udd39", "\ud835\udd3b", "\ud835\udd3c", "\ud835\udd3d", "\ud835\udd3e", "\ud835\udd40", "\ud835\udd41", "\ud835\udd42", "\ud835\udd43", "\ud835\udd44", "\ud835\udd46", "\ud835\udd4a", "\ud835\udd4b", "\ud835\udd4c", "\ud835\udd4d", "\ud835\udd4e", "\ud835\udd4f", "\ud835\udd50", "\ud835\udd52", "\ud835\udd53", "\ud835\udd54", "\ud835\udd55", "\ud835\udd56", "\ud835\udd57", "\ud835\udd58", "\ud835\udd59", "\ud835\udd5a", "\ud835\udd5b", "\ud835\udd5c", "\ud835\udd5d", "\ud835\udd5e", "\ud835\udd5f", "\ud835\udd60", "\ud835\udd61", "\ud835\udd62", "\ud835\udd63", "\ud835\udd64", "\ud835\udd65", "\ud835\udd66", "\ud835\udd67", "\ud835\udd68", "\ud835\udd69", "\ud835\udd6a", "\ud835\udd6b", "\ud835\udd6c", "\ud835\udd6d", "\ud835\udd6e", "\ud835\udd6f", "\ud835\udd70", "\ud835\udd71", "\ud835\udd72", "\ud835\udd73", "\ud835\udd74", "\ud835\udd75", "\ud835\udd76", "\ud835\udd77", "\ud835\udd78", "\ud835\udd79", "\ud835\udd7a", "\ud835\udd7b", "\ud835\udd7c", "\ud835\udd7d", "\ud835\udd7e", "\ud835\udd7f", "\ud835\udd80", "\ud835\udd81", "\ud835\udd82", "\ud835\udd83", "\ud835\udd84", "\ud835\udd85", "\ud835\udd86", "\ud835\udd87", "\ud835\udd88", "\ud835\udd89", "\ud835\udd8a", "\ud835\udd8b", "\ud835\udd8c", "\ud835\udd8d", "\ud835\udd8e", "\ud835\udd8f", "\ud835\udd90", "\ud835\udd91", "\ud835\udd92", "\ud835\udd93", "\ud835\udd94", "\ud835\udd95", "\ud835\udd96", "\ud835\udd97", "\ud835\udd98", "\ud835\udd99", "\ud835\udd9a", "\ud835\udd9b", "\ud835\udd9c", "\ud835\udd9d", "\ud835\udd9e", "\ud835\udd9f", "\ud835\udda0", "\ud835\udda1", "\ud835\udda2", "\ud835\udda3", "\ud835\udda4", "\ud835\udda5", "\ud835\udda6", "\ud835\udda7", "\ud835\udda8", "\ud835\udda9", "\ud835\uddaa", "\ud835\uddab", "\ud835\uddac", "\ud835\uddad", "\ud835\uddae", "\ud835\uddaf", "\ud835\uddb0", "\ud835\uddb1", "\ud835\uddb2", "\ud835\uddb3", "\ud835\uddb4", "\ud835\uddb5", "\ud835\uddb6", "\ud835\uddb7", "\ud835\uddb8", "\ud835\uddb9", "\ud835\uddba", "\ud835\uddbb", "\ud835\uddbc", "\ud835\uddbd", "\ud835\uddbe", "\ud835\uddbf", "\ud835\uddc0", "\ud835\uddc1", "\ud835\uddc2", "\ud835\uddc3", "\ud835\uddc4", "\ud835\uddc5", "\ud835\uddc6", "\ud835\uddc7", "\ud835\uddc8", "\ud835\uddc9", "\ud835\uddca", "\ud835\uddcb", "\ud835\uddcc", "\ud835\uddcd", "\ud835\uddce", "\ud835\uddcf", "\ud835\uddd0", "\ud835\uddd1", "\ud835\uddd2", "\ud835\uddd3", "\ud835\uddd4", "\ud835\uddd5", "\ud835\uddd6", "\ud835\uddd7", "\ud835\uddd8", "\ud835\uddd9", "\ud835\uddda", "\ud835\udddb", "\ud835\udddc", "\ud835\udddd", "\ud835\uddde", "\ud835\udddf", "\ud835\udde0", "\ud835\udde1", "\ud835\udde2", "\ud835\udde3", "\ud835\udde4", "\ud835\udde5", "\ud835\udde6", "\ud835\udde7", "\ud835\udde8", "\ud835\udde9", "\ud835\uddea", "\ud835\uddeb", "\ud835\uddec", "\ud835\udded", "\ud835\uddee", "\ud835\uddef", "\ud835\uddf0", "\ud835\uddf1", "\ud835\uddf2", "\ud835\uddf3", "\ud835\uddf4", "\ud835\uddf5", "\ud835\uddf6", "\ud835\uddf7", "\ud835\uddf8", "\ud835\uddf9", "\ud835\uddfa", "\ud835\uddfb", "\ud835\uddfc", "\ud835\uddfd", "\ud835\uddfe", "\ud835\uddff", "\ud835\ude00", "\ud835\ude01", "\ud835\ude02", "\ud835\ude03", "\ud835\ude04", "\ud835\ude05", "\ud835\ude06", "\ud835\ude07", "\ud835\ude08", "\ud835\ude09", "\ud835\ude0a", "\ud835\ude0b", "\ud835\ude0c", "\ud835\ude0d", "\ud835\ude0e", "\ud835\ude0f", "\ud835\ude10", "\ud835\ude11", "\ud835\ude12", "\ud835\ude13", "\ud835\ude14", "\ud835\ude15", "\ud835\ude16", "\ud835\ude17", "\ud835\ude18", "\ud835\ude19", "\ud835\ude1a", "\ud835\ude1b", "\ud835\ude1c", "\ud835\ude1d", "\ud835\ude1e", "\ud835\ude1f", "\ud835\ude20", "\ud835\ude21", "\ud835\ude22", "\ud835\ude23", "\ud835\ude24", "\ud835\ude25", "\ud835\ude26", "\ud835\ude27", "\ud835\ude28", "\ud835\ude29", "\ud835\ude2a", "\ud835\ude2b", "\ud835\ude2c", "\ud835\ude2d", "\ud835\ude2e", "\ud835\ude2f", "\ud835\ude30", "\ud835\ude31", "\ud835\ude32", "\ud835\ude33", "\ud835\ude34", "\ud835\ude35", "\ud835\ude36", "\ud835\ude37", "\ud835\ude38", "\ud835\ude39", "\ud835\ude3a", "\ud835\ude3b", "\ud835\ude3c", "\ud835\ude3d", "\ud835\ude3e", "\ud835\ude3f", "\ud835\ude40", "\ud835\ude41", "\ud835\ude42", "\ud835\ude43", "\ud835\ude44", "\ud835\ude45", "\ud835\ude46", "\ud835\ude47", "\ud835\ude48", "\ud835\ude49", "\ud835\ude4a", "\ud835\ude4b", "\ud835\ude4c", "\ud835\ude4d", "\ud835\ude4e", "\ud835\ude4f", "\ud835\ude50", "\ud835\ude51", "\ud835\ude52", "\ud835\ude53", "\ud835\ude54", "\ud835\ude55", "\ud835\ude56", "\ud835\ude57", "\ud835\ude58", "\ud835\ude59", "\ud835\ude5a", "\ud835\ude5b", "\ud835\ude5c", "\ud835\ude5d", "\ud835\ude5e", "\ud835\ude5f", "\ud835\ude60", "\ud835\ude61", "\ud835\ude62", "\ud835\ude63", "\ud835\ude64", "\ud835\ude65", "\ud835\ude66", "\ud835\ude67", "\ud835\ude68", "\ud835\ude69", "\ud835\ude6a", "\ud835\ude6b", "\ud835\ude6c", "\ud835\ude6d", "\ud835\ude6e", "\ud835\ude6f", "\ud835\ude70", "\ud835\ude71", "\ud835\ude72", "\ud835\ude73", "\ud835\ude74", "\ud835\ude75", "\ud835\ude76", "\ud835\ude77", "\ud835\ude78", "\ud835\ude79", "\ud835\ude7a", "\ud835\ude7b", "\ud835\ude7c", "\ud835\ude7d", "\ud835\ude7e", "\ud835\ude7f", "\ud835\ude80", "\ud835\ude81", "\ud835\ude82", "\ud835\ude83", "\ud835\ude84", "\ud835\ude85", "\ud835\ude86", "\ud835\ude87", "\ud835\ude88", "\ud835\ude89", "\ud835\ude8a", "\ud835\ude8b", "\ud835\ude8c", "\ud835\ude8d", "\ud835\ude8e", "\ud835\ude8f", "\ud835\ude90", "\ud835\ude91", "\ud835\ude92", "\ud835\ude93", "\ud835\ude94", "\ud835\ude95", "\ud835\ude96", "\ud835\ude97", "\ud835\ude98", "\ud835\ude99", "\ud835\ude9a", "\ud835\ude9b", "\ud835\ude9c", "\ud835\ude9d", "\ud835\ude9e", "\ud835\ude9f", "\ud835\udea0", "\ud835\udea1", "\ud835\udea2", "\ud835\udea3", "\ud835\udea4", "\ud835\udea5", "\ud835\udea8", "\ud835\udea9", "\ud835\udeaa", "\ud835\udeab", "\ud835\udeac", "\ud835\udead", "\ud835\udeae", "\ud835\udeaf", "\ud835\udeb0", "\ud835\udeb1", "\ud835\udeb2", "\ud835\udeb3", "\ud835\udeb4", "\ud835\udeb5", "\ud835\udeb6", "\ud835\udeb7", "\ud835\udeb8", "\ud835\udeb9", "\ud835\udeba", "\ud835\udebb", "\ud835\udebc", "\ud835\udebd", "\ud835\udebe", "\ud835\udebf", "\ud835\udec0", "\ud835\udec2", "\ud835\udec3", "\ud835\udec4", "\ud835\udec5", "\ud835\udec6", "\ud835\udec7", "\ud835\udec8", "\ud835\udec9", "\ud835\udeca", "\ud835\udecb", "\ud835\udecc", "\ud835\udecd", "\ud835\udece", "\ud835\udecf", "\ud835\uded0", "\ud835\uded1", "\ud835\uded2", "\ud835\uded3", "\ud835\uded4", "\ud835\uded5", "\ud835\uded6", "\ud835\uded7", "\ud835\uded8", "\ud835\uded9", "\ud835\udeda", "\ud835\udedc", "\ud835\udedd", "\ud835\udede", "\ud835\udedf", "\ud835\udee0", "\ud835\udee1", "\ud835\udee2", "\ud835\udee3", "\ud835\udee4", "\ud835\udee5", "\ud835\udee6", "\ud835\udee7", "\ud835\udee8", "\ud835\udee9", "\ud835\udeea", "\ud835\udeeb", "\ud835\udeec", "\ud835\udeed", "\ud835\udeee", "\ud835\udeef", "\ud835\udef0", "\ud835\udef1", "\ud835\udef2", "\ud835\udef3", "\ud835\udef4", "\ud835\udef5", "\ud835\udef6", "\ud835\udef7", "\ud835\udef8", "\ud835\udef9", "\ud835\udefa", "\ud835\udefc", "\ud835\udefd", "\ud835\udefe", "\ud835\udeff", "\ud835\udf00", "\ud835\udf01", "\ud835\udf02", "\ud835\udf03", "\ud835\udf04", "\ud835\udf05", "\ud835\udf06", "\ud835\udf07", "\ud835\udf08", "\ud835\udf09", "\ud835\udf0a", "\ud835\udf0b", "\ud835\udf0c", "\ud835\udf0d", "\ud835\udf0e", "\ud835\udf0f", "\ud835\udf10", "\ud835\udf11", "\ud835\udf12", "\ud835\udf13", "\ud835\udf14", "\ud835\udf16", "\ud835\udf17", "\ud835\udf18", "\ud835\udf19", "\ud835\udf1a", "\ud835\udf1b", "\ud835\udf1c", "\ud835\udf1d", "\ud835\udf1e", "\ud835\udf1f", "\ud835\udf20", "\ud835\udf21", "\ud835\udf22", "\ud835\udf23", "\ud835\udf24", "\ud835\udf25", "\ud835\udf26", "\ud835\udf27", "\ud835\udf28", "\ud835\udf29", "\ud835\udf2a", "\ud835\udf2b", "\ud835\udf2c", "\ud835\udf2d", "\ud835\udf2e", "\ud835\udf2f", "\ud835\udf30", "\ud835\udf31", "\ud835\udf32", "\ud835\udf33", "\ud835\udf34", "\ud835\udf36", "\ud835\udf37", "\ud835\udf38", "\ud835\udf39", "\ud835\udf3a", "\ud835\udf3b", "\ud835\udf3c", "\ud835\udf3d", "\ud835\udf3e", "\ud835\udf3f", "\ud835\udf40", "\ud835\udf41", "\ud835\udf42", "\ud835\udf43", "\ud835\udf44", "\ud835\udf45", "\ud835\udf46", "\ud835\udf47", "\ud835\udf48", "\ud835\udf49", "\ud835\udf4a", "\ud835\udf4b", "\ud835\udf4c", "\ud835\udf4d", "\ud835\udf4e", "\ud835\udf50", "\ud835\udf51", "\ud835\udf52", "\ud835\udf53", "\ud835\udf54", "\ud835\udf55", "\ud835\udf56", "\ud835\udf57", "\ud835\udf58", "\ud835\udf59", "\ud835\udf5a", "\ud835\udf5b", "\ud835\udf5c", "\ud835\udf5d", "\ud835\udf5e", "\ud835\udf5f", "\ud835\udf60", "\ud835\udf61", "\ud835\udf62", "\ud835\udf63", "\ud835\udf64", "\ud835\udf65", "\ud835\udf66", "\ud835\udf67", "\ud835\udf68", "\ud835\udf69", "\ud835\udf6a", "\ud835\udf6b", "\ud835\udf6c", "\ud835\udf6d", "\ud835\udf6e", "\ud835\udf70", "\ud835\udf71", "\ud835\udf72", "\ud835\udf73", "\ud835\udf74", "\ud835\udf75", "\ud835\udf76", "\ud835\udf77", "\ud835\udf78", "\ud835\udf79", "\ud835\udf7a", "\ud835\udf7b", "\ud835\udf7c", "\ud835\udf7d", "\ud835\udf7e", "\ud835\udf7f", "\ud835\udf80", "\ud835\udf81", "\ud835\udf82", "\ud835\udf83", "\ud835\udf84", "\ud835\udf85", "\ud835\udf86", "\ud835\udf87", "\ud835\udf88", "\ud835\udf8a", "\ud835\udf8b", "\ud835\udf8c", "\ud835\udf8d", "\ud835\udf8e", "\ud835\udf8f", "\ud835\udf90", "\ud835\udf91", "\ud835\udf92", "\ud835\udf93", "\ud835\udf94", "\ud835\udf95", "\ud835\udf96", "\ud835\udf97", "\ud835\udf98", "\ud835\udf99", "\ud835\udf9a", "\ud835\udf9b", "\ud835\udf9c", "\ud835\udf9d", "\ud835\udf9e", "\ud835\udf9f", "\ud835\udfa0", "\ud835\udfa1", "\ud835\udfa2", "\ud835\udfa3", "\ud835\udfa4", "\ud835\udfa5", "\ud835\udfa6", "\ud835\udfa7", "\ud835\udfa8", "\ud835\udfaa", "\ud835\udfab", "\ud835\udfac", "\ud835\udfad", "\ud835\udfae", "\ud835\udfaf", "\ud835\udfb0", "\ud835\udfb1", "\ud835\udfb2", "\ud835\udfb3", "\ud835\udfb4", "\ud835\udfb5", "\ud835\udfb6", "\ud835\udfb7", "\ud835\udfb8", "\ud835\udfb9", "\ud835\udfba", "\ud835\udfbb", "\ud835\udfbc", "\ud835\udfbd", "\ud835\udfbe", "\ud835\udfbf", "\ud835\udfc0", "\ud835\udfc1", "\ud835\udfc2", "\ud835\udfc4", "\ud835\udfc5", "\ud835\udfc6", "\ud835\udfc7", "\ud835\udfc8", "\ud835\udfc9", "\ud835\udfca", "\ud835\udfcb", "\u2160", "\u2170", "\u2161", "\u2171", "\u2162", "\u2172", "\u2163", "\u2173", "\u2164", "\u2174", "\u2165", "\u2175", "\u2166", "\u2176", "\u2167", "\u2177", "\u2168", "\u2178", "\u2169", "\u2179", "\u216a", "\u217a", "\u216b", "\u217b", "\u216c", "\u217c", "\u216d", "\u217d", "\u216e", "\u217e", "\u216f", "\u217f", "\u24b6", "\u24d0", "\u24b7", "\u24d1", "\u24b8", "\u24d2", "\u24b9", "\u24d3", "\u24ba", "\u24d4", "\u24bb", "\u24d5", "\u24bc", "\u24d6", "\u24bd", "\u24d7", "\u24be", "\u24d8", "\u24bf", "\u24d9", "\u24c0", "\u24da", "\u24c1", "\u24db", "\u24c2", "\u24dc", "\u24c3", "\u24dd", "\u24c4", "\u24de", "\u24c5", "\u24df", "\u24c6", "\u24e0", "\u24c7", "\u24e1", "\u24c8", "\u24e2", "\u24c9", "\u24e3", "\u24ca", "\u24e4", "\u24cb", "\u24e5", "\u24cc", "\u24e6", "\u24cd", "\u24e7", "\u24ce", "\u24e8", "\u24cf", "\u24e9", "\u20ac", "\u0083", "\u0090", "\u0081", "\u0087", "\u008c", "\u008d", "\u008e", "\u0092", "\u00a3", "\u00a4", "\u00a7", "\u00a8", "\u00ae", "\uff7a", "\uff9d", "\uff86", "\uff81", "\uff8a", "\u8bdd", "\u6c49", "\u8bed", "\u597d", "\u7cb5", "\u5ee3", "\u8a71", "\u6668", "\ub155", "\uae4c", "\u6c14", "\u6c17", "\u767a", "\u6c23", "\u2318", "\u202f", "\u3000", "\u259f", "\u2596", "\u30ef", "\u3079", "\u5358", "\u30ca", "\u629e", "\u6392", "\u53e5", "\u69cb", "\u8a66", "\u5075", "\u64c7", "\uff0f", "\u9644", "\u983b", "\u6bcf", "\u9031", "\u4f3a", "\u6e05", "\u5feb", "\u554f", "\u9418", "\u544a", "\u8a34", "\u5011", "\u904b", "\u586b", "\u8abf", "\u8b1d", "\u984c", "\u6aa2", "\u64f7", "\u9a57", "\u89ba", "\u8b70", "\u8b93", "\u5b89", "\u7a69", "\u5929", "\u6703", "\u964d", "\u4f4e", "\u6309", "\u57e0", "\u6846", "\u67b6", "\u7a0d", "\u505a", "\u61c2", "\uff01", "\u900f", "\u7e3d", "\u5171", "\ub82c", "\uc601", "\ube4c", "\ud14c", "\uc120", "\ud0dd", "\uac1d", "\ub4c8", "\ud83d\udc4d", "\ud83d\udc4e", "\u200b", "\u240d", "\u2424", "\u21da", "\u223e", "\u223f", "\u0333", "\u2061", "\u2135", "\u2a3f", "\u2a55", "\u2a53", "\u2227", "\u2a5c", "\u2a58", "\u2a5a", "\u2220", "\u29a4", "\u29a8", "\u29a9", "\u29aa", "\u29ab", "\u29ac", "\u29ad", "\u29ae", "\u29af", "\u2221", "\u221f", "\u22be", "\u299d", "\u2222", "\u237c", "\u2a6f", "\u2248", "\u2a70", "\u224a", "\u224b", "\u2254", "\u224d", "\u2233", "\u2a11", "\u224c", "\u03f6", "\u2035", "\u223d", "\u22cd", "\u2216", "\u2ae7", "\u22bd", "\u2305", "\u2306", "\u23b5", "\u23b6", "\u2235", "\u29b0", "\u2136", "\u226c", "\u22c2", "\u25ef", "\u22c3", "\u2a00", "\u2a01", "\u2a02", "\u2a06", "\u2605", "\u2a04", "\u22c1", "\u22c0", "\u290d", "\u29eb", "\u25aa", "\u25b4", "\u25be", "\u25c2", "\u25b8", "\u2423", "\u2592", "\u2591", "\u2593", "\u20e5", "\u2261", "\u2aed", "\u2310", "\u22a5", "\u22c8", "\u29c9", "\u2510", "\u2555", "\u2556", "\u2557", "\u2552", "\u2553", "\u2554", "\u2550", "\u252c", "\u2564", "\u2565", "\u2566", "\u2534", "\u2567", "\u2568", "\u2569", "\u229f", "\u229e", "\u22a0", "\u2518", "\u255b", "\u255c", "\u255d", "\u2558", "\u2559", "\u255a", "\u2502", "\u2551", "\u253c", "\u256a", "\u256b", "\u256c", "\u2524", "\u2561", "\u2562", "\u2563", "\u251c", "\u255e", "\u255f", "\u2560", "\u02d8", "\u204f", "\u29c5", "\u27c8", "\u224e", "\u2aae", "\u224f", "\u2a44", "\u2a49", "\u2a4b", "\u2229", "\u22d2", "\u2a47", "\u2a40", "\ufe00", "\u2041", "\u02c7", "\u2a4d", "\u2230", "\u2a4c", "\u2a50", "\u29b2", "\u2713", "\u02c6", "\u2257", "\u21ba", "\u21bb", "\u229b", "\u229a", "\u229d", "\u2299", "\u2296", "\u2295", "\u2297", "\u25cb", "\u29c3", "\u2a10", "\u2aef", "\u29c2", "\u2232", "\u2663", "\u2237", "\u2a74", "\u2201", "\u2218", "\u2245", "\u2a6d", "\u222e", "\u222f", "\u2210", "\u2117", "\u21b5", "\u2717", "\u2a2f", "\u2acf", "\u2ad1", "\u2ad0", "\u2ad2", "\u22ef", "\u2938", "\u2935", "\u22de", "\u22df", "\u21b6", "\u293d", "\u2a48", "\u2a46", "\u222a", "\u22d3", "\u2a4a", "\u228d", "\u2a45", "\u21b7", "\u293c", "\u22ce", "\u22cf", "\u2231", "\u232d", "\u2020", "\u2021", "\u2138", "\u2193", "\u21a1", "\u21d3", "\u2ae4", "\u22a3", "\u290f", "\u02dd", "\u21ca", "\u2911", "\u2a77", "\u2207", "\u29b1", "\u297f", "\u2965", "\u21c3", "\u21c2", "\u02d9", "\u02dc", "\u22c4", "\u2666", "\u22f2", "\u22c7", "\u231e", "\u230d", "\u20dc", "\u2250", "\u2251", "\u2238", "\u2214", "\u22a1", "\u21d0", "\u21d4", "\u27f8", "\u27fa", "\u27f9", "\u21d2", "\u22a8", "\u21d1", "\u21d5", "\u2225", "\u2913", "\u21f5", "\u0311", "\u2950", "\u295e", "\u2956", "\u21bd", "\u295f", "\u2957", "\u21c1", "\u21a7", "\u22a4", "\u2910", "\u231f", "\u230c", "\u29f6", "\u22f1", "\u25bf", "\u296f", "\u29a6", "\u27ff", "\u2a6e", "\u2256", "\u2255", "\u2252", "\u2a9a", "\u2a96", "\u2a98", "\u2a99", "\u2208", "\u23e7", "\u2a95", "\u2a97", "\u2205", "\u25fb", "\u25ab", "\u2004", "\u2005", "\u2002", "\u22d5", "\u29e3", "\u2a71", "\u2242", "\u2a75", "\u225f", "\u21cc", "\u2a78", "\u29e5", "\u2971", "\u2253", "\u2a73", "\u2203", "\u2640", "\u25fc", "\u266d", "\u25b1", "\u2200", "\u22d4", "\u2ad9", "\u2a0d", "\u2153", "\u2155", "\u2159", "\u215b", "\u2154", "\u2156", "\u2157", "\u215c", "\u2158", "\u215a", "\u215d", "\u215e", "\u2044", "\u2322", "\u2a86", "\u2265", "\u2267", "\u2a8c", "\u22db", "\u2a7e", "\u2aa9", "\u2a80", "\u2a82", "\u2a84", "\u2a94", "\u226b", "\u22d9", "\u2137", "\u2aa5", "\u2277", "\u2a92", "\u2aa4", "\u2a8a", "\u2a88", "\u2269", "\u22e7", "\u2aa2", "\u2273", "\u2a8e", "\u2a90", "\u2aa7", "\u2a7a", "\u22d7", "\u2995", "\u2a7c", "\u2978", "\u2948", "\u2194", "\u21ad", "\u2665", "\u22b9", "\u2925", "\u2926", "\u21ff", "\u223b", "\u21a9", "\u21aa", "\u2015", "\u2043", "\u2063", "\u2a0c", "\u222d", "\u29dc", "\u2129", "\u22b7", "\u2105", "\u221e", "\u29dd", "\u22ba", "\u222b", "\u222c", "\u2a17", "\u2a3c", "\u2062", "\u22f5", "\u22f9", "\u22f4", "\u22f3", "\u29b4", "\u27e8", "\u27ea", "\u2991", "\u2a85", "\u21e4", "\u291f", "\u2190", "\u219e", "\u291d", "\u21ab", "\u2939", "\u2973", "\u21a2", "\u2919", "\u291b", "\u2aab", "\u2aad", "\u290c", "\u290e", "\u2772", "\u298b", "\u298f", "\u298d", "\u2308", "\u2936", "\u2967", "\u294b", "\u21b2", "\u2264", "\u2266", "\u21c6", "\u27e6", "\u2961", "\u2959", "\u230a", "\u21bc", "\u21c7", "\u21cb", "\u294e", "\u21a4", "\u295a", "\u22cb", "\u29cf", "\u22b2", "\u22b4", "\u2951", "\u2960", "\u2958", "\u21bf", "\u2952", "\u2a8b", "\u22da", "\u2a7d", "\u2aa8", "\u2a7f", "\u2a81", "\u2a83", "\u2a93", "\u22d6", "\u2276", "\u2aa1", "\u2272", "\u297c", "\u2a91", "\u2962", "\u296a", "\u2584", "\u226a", "\u22d8", "\u296b", "\u25fa", "\u23b0", "\u2a89", "\u2a87", "\u2268", "\u22e6", "\u27ec", "\u21fd", "\u27f5", "\u27f7", "\u27fc", "\u27f6", "\u21ac", "\u2985", "\u2a2d", "\u2a34", "\u2217", "\u2199", "\u2198", "\u25ca", "\u2993", "\u296d", "\u22bf", "\u2039", "\u21b0", "\u2a8d", "\u2a8f", "\u201a", "\u2aa6", "\u2a79", "\u22c9", "\u2976", "\u2a7b", "\u25c3", "\u2996", "\u294a", "\u2966", "\u2642", "\u2720", "\u2905", "\u21a6", "\u21a5", "\u25ae", "\u2a29", "\u223a", "\u205f", "\u2127", "\u2af0", "\u2223", "\u2a2a", "\u2213", "\u2adb", "\u22a7", "\u22b8", "\u20d2", "\u2249", "\u0338", "\u266e", "\u2a43", "\u2247", "\u2a42", "\u2924", "\u2197", "\u21d7", "\u2260", "\u2262", "\u2928", "\u2204", "\u2271", "\u2275", "\u226f", "\u21ae", "\u21ce", "\u2af2", "\u220b", "\u22fc", "\u22fa", "\u219a", "\u21cd", "\u2025", "\u2270", "\u226e", "\u2274", "\u22ea", "\u22ec", "\u2224", "\u2aec", "\u226d", "\u2226", "\u2209", "\u2279", "\u22f7", "\u22f6", "\u2278", "\u220c", "\u22fe", "\u22fd", "\u2280", "\u2aaf", "\u22e0", "\u29d0", "\u22eb", "\u22ed", "\u228f", "\u22e2", "\u2290", "\u22e3", "\u2282", "\u2288", "\u2281", "\u2ab0", "\u22e1", "\u227f", "\u2283", "\u2289", "\u2241", "\u2244", "\u2afd", "\u2202", "\u2a14", "\u2933", "\u219b", "\u21cf", "\u219d", "\u2284", "\u2ac5", "\u2285", "\u2ac6", "\u2116", "\u2007", "\u22ac", "\u22ad", "\u22ae", "\u22af", "\u2904", "\u29de", "\u2902", "\u2903", "\u22b5", "\u223c", "\u2923", "\u2196", "\u21d6", "\u2927", "\u2a38", "\u29bc", "\u29bf", "\u02db", "\u29c1", "\u29b5", "\u29be", "\u29bb", "\u203e", "\u29c0", "\u29b6", "\u29b7", "\u29b9", "\u2a54", "\u2228", "\u2a5d", "\u22b6", "\u2a56", "\u2a57", "\u2a5b", "\u2298", "\u2a36", "\u2a37", "\u233d", "\u23de", "\u23b4", "\u23dc", "\u2af3", "\u2030", "\u2031", "\u260e", "\u2a23", "\u2a22", "\u2a25", "\u2a72", "\u2a26", "\u2a27", "\u2a15", "\u2ab7", "\u2abb", "\u227a", "\u227c", "\u227e", "\u2ab9", "\u2ab5", "\u22e8", "\u2ab3", "\u2032", "\u2033", "\u220f", "\u232e", "\u2312", "\u2313", "\u221d", "\u22b0", "\u2008", "\u2057", "\u2a16", "\u21db", "\u221a", "\u29b3", "\u27e9", "\u27eb", "\u2992", "\u29a5", "\u2975", "\u21e5", "\u2920", "\u2192", "\u21a0", "\u291e", "\u2945", "\u2974", "\u2916", "\u21a3", "\u291a", "\u291c", "\u2236", "\u2773", "\u298c", "\u298e", "\u2990", "\u2309", "\u2937", "\u2969", "\u21b3", "\u25ad", "\u297d", "\u230b", "\u2964", "\u21c0", "\u296c", "\u21c4", "\u27e7", "\u295d", "\u2955", "\u21c9", "\u22a2", "\u295b", "\u22cc", "\u22b3", "\u294f", "\u295c", "\u2954", "\u21be", "\u2953", "\u02da", "\u23b1", "\u2aee", "\u27ed", "\u21fe", "\u2986", "\u2a2e", "\u2a35", "\u2970", "\u2994", "\u2a12", "\u21b1", "\u22ca", "\u25b9", "\u29ce", "\u29f4", "\u2968", "\u211e", "\u2ab8", "\u2abc", "\u227b", "\u227d", "\u2ab4", "\u2aba", "\u2ab6", "\u22e9", "\u2a13", "\u22c5", "\u2a66", "\u21d8", "\u2929", "\u2736", "\u266f", "\u2191", "\u2a6a", "\u2243", "\u2a9e", "\u2aa0", "\u2a9d", "\u2a9f", "\u2246", "\u2a24", "\u2972", "\u2a33", "\u29e4", "\u2323", "\u2aaa", "\u2aac", "\u233f", "\u29c4", "\u2660", "\u2293", "\u2294", "\u2291", "\u2292", "\u25a1", "\u22c6", "\u2606", "\u22d0", "\u2abd", "\u2286", "\u2ac3", "\u2ac1", "\u2acb", "\u228a", "\u2abf", "\u2979", "\u2ac7", "\u2ad5", "\u2ad3", "\u2211", "\u266a", "\u22d1", "\u2abe", "\u2ad8", "\u2287", "\u2ac4", "\u27c9", "\u2ad7", "\u297b", "\u2ac2", "\u2acc", "\u228b", "\u2ac0", "\u2ac8", "\u2ad4", "\u2ad6", "\u21d9", "\u292a", "\u2316", "\u20db", "\u2315", "\u2234", "\u2009", "\u2a31", "\u2a30", "\u2336", "\u2af1", "\u2ada", "\u2034", "\u2122", "\u25b5", "\u225c", "\u25ec", "\u2a3a", "\u2a39", "\u29cd", "\u2a3b", "\u23e2", "\u219f", "\u2949", "\u21c5", "\u296e", "\u297e", "\u2963", "\u2580", "\u231c", "\u230f", "\u25f8", "\u23df", "\u23dd", "\u228e", "\u2912", "\u2195", "\u21c8", "\u231d", "\u230e", "\u25f9", "\u22f0", "\u29a7", "\u299c", "\u2ae8", "\u2aeb", "\u2ae9", "\u22a9", "\u22ab", "\u2ae6", "\u22bb", "\u225a", "\u22ee", "\u2016", "\u2758", "\u2240", "\u22aa", "\u299a", "\u2a5f", "\u2259", "\u2118", "\u22fb", "\u21dd", "\u2303", "\u2325", "\u21e7", "\u0661", "\u0662", "\u0663", "\u0664", "\u0665", "\u0666", "\u0667", "\u0668", "\u0669", "\u0660", "\u09ec", "\u09ed", "\u09ee", "\u09ef", "\u0f22", "\u0f23", "\u0f24", "\u0f25", "\u0f27", "\u0f29", "\u0f20", "\u0f94", "\u0796", "\u07ac", "\u0782", "\u07aa", "\u0787", "\u07a6", "\u0783", "\u07a9", "\u078a", "\u0784", "\u07b0", "\u0789", "\u07a7", "\u07a8", "\u0797", "\u07ad", "\u0795", "\u078d", "\u07ab", "\u07af", "\u078e", "\u0790", "\u0793", "\u07ae", "\u0786", "\u0788", "\u0791", "\u078b", "\u078c", "\u0780", "\u0794", "\u0785", "\u06f1", "\u06f2", "\u06f3", "\u06f4", "\u06f5", "\u06f6", "\u06f7", "\u06f8", "\u06f9", "\u06f0", "\u0aea", "\u0aeb", "\u0aed", "\u0aef", "\u0a91", "\u05f3", "\u05d7", "\u0967", "\u0968", "\u0969", "\u096a", "\u096b", "\u096c", "\u096d", "\u096e", "\u096f", "\u0966", "\u6708", "\u4e09", "\u56db", "\u4e94", "\u4e03", "\u4e5d", "\u66dc", "\u706b", "\u6c34", "\u6728", "\u91d1", "\u571f", "\u5e74", "\u5348", "\u4eca", "\u6628", "\u79d2", "\u30f6", "\u17e1", "\u17e2", "\u17e3", "\u17e4", "\u17e5", "\u17e6", "\u17e7", "\u17e8", "\u17e9", "\u17e0", "\u1798", "\u1780", "\u179a", "\u17b6", "\u17bb", "\u17d2", "\u1797", "\u17c8", "\u17b8", "\u1793", "\u17c1", "\u179f", "\u17a7", "\u17b7", "\u1790", "\u178a", "\u17a0", "\u1789", "\u178f", "\u179b", "\u179c", "\u1785", "\u1786", "\u1792", "\u17bc", "\u17a2", "\u1791", "\u1799", "\u17d0", "\u1784", "\u1782", "\u1796", "\u1794", "\u17cd", "\u17c5", "\u17b9", "\u17c3", "\u17c7", "\u17c9", "\u17c4", "\u17c2", "\u17c0", "\u17bd", "\u1781", "\u17c6", "\u0ce7", "\u0ce8", "\u0ce9", "\u0cea", "\u0ceb", "\u0cec", "\u0ced", "\u0cee", "\u0cef", "\u0ce6", "\u0cd5", "\u0cd6", "\uc6d4", "\uae08", "\ub144", "\ub298", "\ub09c", "\uba87", "\u06d5", "\u06ce", "\u06c6", "\u0695", "\u06b5", "\u0ea1", "\u0eb1", "\u0e87", "\u0e81", "\u0ead", "\u0e99", "\u0eb8", "\u0e9e", "\u0eb5", "\u0ec0", "\u0eaa", "\u0eb6", "\u0e94", "\u0eb0", "\u0eb4", "\u0e96", "\u0ecd", "\u0ebb", "\u0eab", "\u0e8d", "\u0e95", "\u0e88", "\u0e97", "\u0e84", "\u0e8a", "\u0ec9", "\u0ec1", "\u0eb7", "\u0ec8", "\u0edc", "\u0e9c", "\u0e9a", "\u0ec3", "\u0ec2", "\u0e9b", "\u0d7c", "\u0d7d", "\u0d7a", "\u0d7e", "\u0d7b", "\u1041", "\u1042", "\u1043", "\u1044", "\u1045", "\u1046", "\u1047", "\u1048", "\u1049", "\u1040", "\u1007", "\u1014", "\u103a", "\u101d", "\u102b", "\u101b", "\u102e", "\u1016", "\u1031", "\u102c", "\u1019", "\u1010", "\u1027", "\u1015", "\u103c", "\u103d", "\u1030", "\u101c", "\u102d", "\u102f", "\u1004", "\u101e", "\u1002", "\u1005", "\u1000", "\u1018", "\u1021", "\u1012", "\u1039", "\u1017", "\u1013", "\u101f", "\u1038", "\u101a", "\u103e", "\u1001", "\u1032", "\u1037", "\u100a", "\u0a6a", "\u0a6b", "\u0a6e", "\u0a6f", "\u0a18", "\u067d", "\u06aa", "\u068a", "\u06b1", "\u0687", "\u0684", "\u06bb", "\u06b3", "\u068f", "\u0da2", "\u0d94", "\u0d9f", "\u0d8a", "\u0be7", "\u0be8", "\u0be9", "\u0bea", "\u0beb", "\u0bec", "\u0bed", "\u0bee", "\u0bef", "\u0be6", "\u0b9e", "\u0e24", "\u0e0e", "\u2d49", "\u2d4f", "\u2d30", "\u2d62", "\u2d54", "\u2d31", "\u2d55", "\u2d4e", "\u2d5a", "\u2d53", "\u2d4d", "\u2d63", "\u2d56", "\u2d5b", "\u2d5c", "\u2d3d", "\u2d5f", "\u2d61", "\u2d37", "\u2d4a", "\u2d59", "\u2d39", "\u2d45", "\u2d34", "\u2d3a", "\u2d44", "\u2d33", "\u02e4", "\u06cb", "\u06c7", "\u06c8", "\u06ad", "\u06c1", "\u0688", "\u0679", "\u06d2", "\u661f", "\u5468", "\u51cc", "\u665a", "\u51e0", "\u949f", "\u5e7e", "\ue63e", "\ue6f9", "\ue6fa", "\ue6f8", "\ue6f7", "\ue67c", "\ue6d2", "\ue74b", "\ue603", "\ue605", "\ue602", "\ue604", "\ue727", "\ue726", "\ue722", "\ue724", "\ue725", "\ue723", "\ue6f0", "\ue735", "\ue621", "\ue907", "\ue65f", "\ue6e3", "\ue69d", "\ue76f", "\ue676", "\ue900", "\ue768", "\ue606", "\ue6b8", "\ue61a", "\ue6bf", "\ue674", "\ue90a", "\ue72d", "\ue70b", "\ue62b", "\ue69e", "\u2304", "\u2329", "\u232a", "\ue770", "\ue623", "\ue67e", "\ue689", "\ue6df", "\ue697", "\ue6e0", "\ue694", "\ue695", "\ue696", "\ue66a", "\ue68e", "\ue68c", "\ue68b", "\ue68d", "\ue61b", "\ue7c5", "\ue61d", "\u2601", "\ue690", "\ue691", "\ue661", "\ue6c5", "\ue645", "\ue763", "\ue6da", "\ue68a", "\ue637", "\ue79c", "\ue6c0", "\ue639", "\ue79b", "\ue6cb", "\ue67f", "\ue649", "\ue7b4", "\ue7c8", "\ue7c9", "\ue7d0", "\ue71b", "\ue6ef", "\ue751", "\ue908", "\ue683", "\ue644", "\ue739", "\ue6af", "\ue7b3", "\ue681", "\ue682", "\ue600", "\ue630", "\ue71e", "\ue71f", "\ue6c7", "\ue6c6", "\ue703", "\ue6ff", "\ue701", "\ue702", "\ue6ce", "\ue62f", "\ue716", "\ue715", "\ue66b", "\ue615", "\ue69c", "\u270e", "\u23cf", "\ue75f", "\u2709", "\ue7d9", "\ue773", "\ue648", "\ue636", "\ue6ea", "\ue764", "\ue633", "\ue6cc", "\ue75a", "\ue66f", "\ue6a8", "\ue6ac", "\ue656", "\ue78f", "\ue6a1", "\ue638", "\ue78c", "\ue6ee", "\ue7d7", "\ue78d", "\u2691", "\ue7a9", "\ue6b3", "\ue6b7", "\ue7c1", "\ue7c4", "\ue7c0", "\ue7c2", "\ue7c3", "\ue659", "\ue652", "\ue7b0", "\ue651", "\ue653", "\ue670", "\ue760", "\ue761", "\ue6b4", "\ue63a", "\ue795", "\ue685", "\ue75e", "\ue699", "\ue6e5", "\ue6f4", "\ue640", "\ue613", "\ue72a", "\ue72b", "\ue729", "\ue749", "\ue728", "\ue72c", "\ue748", "\ue6b1", "\ue666", "\ue7b5", "\ue673", "\ue609", "\ue7e1", "\ue7e2", "\ue6d0", "\ue6e4", "\ue60a", "\ue75d", "\ue6de", "\ue6bb", "\ue6bc", "\ue6b9", "\ue6ba", "\ue6b5", "\ue793", "\ue794", "\ue6dc", "\ue7a2", "\ue6f3", "\ue614", "\ue66d", "\ue6ed", "\ue64a", "\u2302", "\ue70c", "\ue75c", "\ue71d", "\ue720", "\ue771", "\ue73a", "\ue73b", "\ue632", "\ue629", "\ue7d1", "\ue7d2", "\ue7d3", "\ue7d4", "\ue7d5", "\ue7a3", "\ue66c", "\ue765", "\ue772", "\ue774", "\ue776", "\ue775", "\ue607", "\ue738", "\ue78e", "\ue707", "\ue705", "\ue704", "\ue708", "\ue70a", "\ue709", "\ue742", "\ue706", "\ue757", "\ue73c", "\ue665", "\ue6cf", "\ue618", "\ue60c", "\ue60d", "\ue6d3", "\ue60e", "\ue610", "\ue611", "\ue60f", "\ue6c3", "\ue612", "\ue6d4", "\ue904", "\ue7a4", "\ue7e3", "\ue7e4", "\ue7c7", "\ue6b0", "\ue62d", "\u2630", "\ue7b9", "\ue743", "\ue619", "\ue625", "\ue69a", "\ue64c", "\ue6f6", "\ue74a", "\ue662", "\ue741", "\ue67d", "\ue635", "\ue62c", "\ue762", "\ue655", "\ue654", "\ue74f", "\ue60b", "\ue634", "\ue717", "\ue69f", "\ue754", "\ue62a", "\ue7b1", "\ue693", "\ue6db", "\ue680", "\ue6a6", "\ue905", "\ue747", "\ue902", "\ue903", "\ue65c", "\ue65d", "\ue6e9", "\ue78b", "\ue65b", "\ue675", "\ue7e0", "\ue624", "\ue7b8", "\ue746", "\ue756", "\ue69b", "\ue67a", "\ue73f", "\ue658", "\ue7a8", "\ue660", "\ue777", "\ue778", "\ue664", "\ue76c", "\ue753", "\ue65e", "\ue6a9", "\ue63d", "\ue76a", "\ue63c", "\ue684", "\ue646", "\ue6f1", "\ue6eb", "\ue6ab", "\ue6d1", "\ue6d9", "\ue617", "\ue78a", "\ue687", "\u2399", "\ue622", "\ue631", "\ue65a", "\ue752", "\ue6e8", "\ue698", "\ue6ae", "\ue6c4", "\ue643", "\ue758", "\ue63f", "\ue755", "\ue6fd", "\ue6fe", "\ue6fc", "\ue6fb", "\ue692", "\ue7d6", "\ue672", "\ue740", "\ue7a5", "\ue6f2", "\ue6e1", "\ue6e2", "\ue76b", "\ue6b6", "\ue73e", "\ue64b", "\ue608", "\ue628", "\ue663", "\ue6ec", "\ue616", "\ue66e", "\ue736", "\ue737", "\ue796", "\ue79a", "\ue799", "\ue798", "\ue797", "\ue6a2", "\ue62e", "\ue7b2", "\ue6c2", "\ue6c1", "\ue909", "\ue718", "\ue769", "\ue6d7", "\ue70e", "\ue70d", "\ue6d8", "\ue7b6", "\ue671", "\ue64f", "\ue64d", "\ue6c8", "\ue6d5", "\ue6d6", "\ue64e", "\ue6c9", "\ue750", "\ue686", "\ue6e7", "\ue6a7", "\ue70f", "\ue6ad", "\ue6aa", "\ue901", "\ue7a6", "\ue601", "\ue745", "\ue744", "\ue72e", "\ue731", "\ue730", "\ue72f", "\ue733", "\ue732", "\ue61c", "\ue6ca", "\ue79e", "\ue6dd", "\ue667", "\ue669", "\ue7d8", "\ue7c6", "\ue668", "\ue6be", "\ue6bd", "\ue779", "\u23f2", "\ue6cd", "\ue620", "\ue61e", "\ue61f", "\ue6b2", "\ue677", "\ue90c", "\ue79f", "\ue759", "\ue63b", "\ue7b7", "\ue71a", "\ue719", "\ue90b", "\ue657", "\ue906", "\u2381", "\u238c", "\ue688", "\ue73d", "\ue626", "\ue650", "\ue679", "\ue7a7", "\ue68f", "\ue627", "\ue6f5", "\ue75b", "\ue71c", "\ue721", "\ue6a0", "\ue6a4", "\ue6a3", "\ue6a5", "\ue79d", "\ue647", "\ue6e6", "\ue678", "\ue790", "\ue792", "\ue791", "\ue734", "\ue641", "\ue642", "\ue67b", "\ufffe", "\uffff", "\u2340", "\u2363", "\u2373", "\u235f", "\u2339", "\u2377", "\u2371", "\u2372", "\u2374", "\u236a", "\u2349", "\u2337", "\u234b", "\u2352", "\u2355", "\u234e", "\u236c", "\u235d", "\u80cc", "\u666f", "\u5834", "\u7db1", "\u573a", "\u7eb2", "\u5287", "\u5267", "\u90a3", "\u9ebc", "\u4e48", "\u4e14", "\u5e76", "\u5047", "\uc800", "\uc57d", "\u02ff", "\u037f", "\u1fff", "\u2070", "\u218f", "\u2fef", "\ud7ff", "\uf900", "\ufdcf", "\ufdf0", "\u036f", "\u203f", "\u2040", "\u25bc", "\ufe15", "\uff03", "\uff04", "\uff05", "\uff06", "\ufe35", "\ufe36", "\uff0a", "\uff0b", "\ufe10", "\ufe32", "\ufe13", "\ufe14", "\ufe3f", "\uff1d", "\ufe40", "\ufe16", "\uff20", "\ufe47", "\uff3c", "\ufe48", "\uff3e", "\ufe33", "\uff40", "\ufe37", "\ufe38", "\uff5e", "\uffe0", "\uffe1", "\uffe5", "\uffe4", "\uffe2", "\uffe3", "\ufe31", "\ufe43", "\ufe44", "\ufe41", "\ufe42", "\ufe19", "\u2027", "\u20a9", "\uffe6", "\ufe11", "\ufe12", "\u3008", "\u3009", "\u300a", "\ufe3d", "\u300b", "\ufe3e", "\u300e", "\u300f", "\u3010", "\ufe3b", "\u3011", "\ufe3c", "\u3014", "\ufe39", "\u3015", "\ufe3a", "\u3016", "\ufe17", "\u3017", "\ufe18", "\uff0d", "\uff0e", "\uff1c", "\uff1e", "\uff1f", "\uff3b", "\uff3d", "\uff3f", "\uff5b", "\uff5c", "\uff5d", "\uff5f", "\uff60", "\uff61", "\uff62", "\uff63", "\u95f0", "\u25c4", "\u25ba", "\u25b2", "\u25cf", "\u25a0", "\u25c6", "\u25c7", "\u274c", "\u2000", "\u2001", "\u2006", "\u20bd", "\u231b", "\u26fa", "\u270f", "\ue001", "\ue002", "\ue003", "\ue005", "\ue006", "\ue007", "\ue008", "\ue009", "\ue010", "\ue011", "\ue012", "\ue013", "\ue014", "\ue015", "\ue016", "\ue017", "\ue018", "\ue019", "\ue020", "\ue021", "\ue022", "\ue023", "\ue024", "\ue025", "\ue026", "\ue027", "\ue028", "\ue029", "\ue030", "\ue031", "\ue032", "\ue033", "\ue034", "\ue035", "\ue036", "\ue037", "\ue038", "\ue039", "\ue040", "\ue041", "\ue042", "\ue043", "\ue044", "\ue045", "\ue046", "\ue047", "\ue048", "\ue049", "\ue050", "\ue051", "\ue052", "\ue053", "\ue054", "\ue055", "\ue056", "\ue057", "\ue058", "\ue059", "\ue060", "\ue062", "\ue063", "\ue064", "\ue065", "\ue066", "\ue067", "\ue068", "\ue069", "\ue070", "\ue071", "\ue072", "\ue073", "\ue074", "\ue075", "\ue076", "\ue077", "\ue078", "\ue079", "\ue080", "\ue081", "\ue082", "\ue083", "\ue084", "\ue085", "\ue086", "\ue087", "\ue088", "\ue089", "\ue090", "\ue091", "\ue092", "\ue093", "\ue094", "\ue095", "\ue096", "\ue097", "\ue101", "\ue102", "\ue103", "\ue104", "\ue105", "\ue106", "\ue107", "\ue108", "\ue109", "\ue110", "\ue111", "\ue112", "\ue113", "\ue114", "\ue115", "\ue116", "\ue117", "\ue118", "\ue119", "\ue120", "\ue121", "\ue122", "\ue123", "\ue124", "\ue125", "\ue126", "\ue127", "\ue128", "\ue129", "\ue130", "\ue131", "\ue132", "\ue133", "\ue134", "\ue135", "\ue136", "\ue137", "\ue138", "\ue139", "\ue140", "\ue141", "\ue142", "\ue143", "\ue144", "\ue145", "\ue146", "\ue148", "\ue149", "\ue150", "\ue151", "\ue152", "\ue153", "\ue154", "\ue155", "\ue156", "\ue157", "\ue158", "\ue159", "\ue160", "\ue161", "\ue162", "\ue163", "\ue164", "\ue165", "\ue166", "\ue167", "\ue168", "\ue169", "\ue170", "\ue171", "\ue172", "\ue173", "\ue174", "\ue175", "\ue176", "\ue177", "\ue178", "\ue179", "\ue180", "\ue181", "\ue182", "\ue183", "\ue184", "\ue185", "\ue186", "\ue187", "\ue188", "\ue189", "\ue190", "\ue191", "\ue192", "\ue193", "\ue194", "\ue195", "\ue197", "\ue198", "\ue199", "\ue200", "\ue201", "\ue202", "\ue203", "\ue204", "\ue205", "\ue206", "\ue209", "\ue210", "\ue211", "\ue212", "\ue213", "\ue214", "\ue215", "\ue216", "\ue218", "\ue219", "\ue221", "\ue223", "\ue224", "\ue225", "\ue226", "\ue227", "\ue230", "\ue231", "\ue232", "\ue233", "\ue234", "\ue235", "\ue236", "\ue237", "\ue238", "\ue239", "\ue240", "\ue241", "\ue242", "\ue243", "\ue244", "\ue245", "\ue246", "\ue247", "\ue248", "\ue249", "\ue250", "\ue251", "\ue252", "\ue253", "\ue254", "\ue255", "\ue256", "\ue257", "\ue258", "\ue259", "\ue260", "\uf8ff", "\uf511", "\uf6aa", "\u1680", "\u180e", "\u4ea4", "\u25b6", "\uff64", "\u7766", "\u5f25", "\u536f", "\u7690", "\u8449", "\u795e", "\u971c", "\u5e2b", "\u8d70", "\u20aa", "\u5186", "\u02c1", "\u02d1", "\u02e0", "\u02ec", "\u02ee", "\u0374", "\u037a", "\u052f", "\u0559", "\u0620", "\u066e", "\u066f", "\u0671", "\u06d3", "\u06e5", "\u06e6", "\u06ee", "\u06ef", "\u06fa", "\u06fc", "\u06ff", "\u0710", "\u0712", "\u072f", "\u074d", "\u07a5", "\u07b1", "\u07ca", "\u07ea", "\u07f4", "\u07f5", "\u07fa", "\u0800", "\u0815", "\u081a", "\u0824", "\u0828", "\u0840", "\u0858", "\u08a0", "\u08b2", "\u0904", "\u093d", "\u0950", "\u0958", "\u0961", "\u0971", "\u0980", "\u098c", "\u09bd", "\u09e1", "\u0a0f", "\u0a59", "\u0a5e", "\u0a72", "\u0a74", "\u0a8d", "\u0abd", "\u0ad0", "\u0ae0", "\u0ae1", "\u0b0c", "\u0b10", "\u0b13", "\u0b35", "\u0b3d", "\u0b5c", "\u0b5d", "\u0b61", "\u0bb9", "\u0bd0", "\u0c0c", "\u0c3d", "\u0c58", "\u0c59", "\u0c60", "\u0c61", "\u0c8c", "\u0c90", "\u0cbd", "\u0cde", "\u0ce0", "\u0ce1", "\u0cf1", "\u0cf2", "\u0d0c", "\u0d3a", "\u0d3d", "\u0d4e", "\u0d60", "\u0d61", "\u0d7f", "\u0d96", "\u0dc6", "\u0e82", "\u0e9f", "\u0ea3", "\u0eb3", "\u0ebd", "\u0ec4", "\u0ec6", "\u0edf", "\u0f00", "\u0f6c", "\u0f88", "\u0f8c", "\u102a", "\u103f", "\u1050", "\u1055", "\u105a", "\u105d", "\u1061", "\u1065", "\u1066", "\u106e", "\u1070", "\u1075", "\u1081", "\u108e", "\u10c7", "\u10cd", "\u10fa", "\u10fc", "\u1248", "\u124a", "\u124d", "\u1250", "\u1256", "\u1258", "\u125a", "\u125d", "\u1288", "\u128a", "\u128d", "\u1290", "\u12b0", "\u12b2", "\u12b5", "\u12b8", "\u12be", "\u12c0", "\u12c2", "\u12c5", "\u12c8", "\u12d6", "\u12d8", "\u1310", "\u1312", "\u1315", "\u1318", "\u135a", "\u1380", "\u138f", "\u13a0", "\u13f4", "\u1401", "\u166c", "\u166f", "\u167f", "\u1681", "\u169a", "\u16a0", "\u16ea", "\u16ee", "\u16f8", "\u1700", "\u170c", "\u170e", "\u1711", "\u1720", "\u1731", "\u1740", "\u1751", "\u1760", "\u176c", "\u176e", "\u1770", "\u17b3", "\u17d7", "\u17dc", "\u1820", "\u1877", "\u1880", "\u18a8", "\u18aa", "\u18b0", "\u18f5", "\u1900", "\u191e", "\u1950", "\u196d", "\u1970", "\u1974", "\u1980", "\u19ab", "\u19c1", "\u19c7", "\u1a00", "\u1a16", "\u1a20", "\u1a54", "\u1aa7", "\u1b05", "\u1b33", "\u1b45", "\u1b4b", "\u1b83", "\u1ba0", "\u1bae", "\u1baf", "\u1bba", "\u1be5", "\u1c00", "\u1c23", "\u1c4d", "\u1c4f", "\u1c5a", "\u1c7d", "\u1ce9", "\u1cec", "\u1cee", "\u1cf1", "\u1cf5", "\u1cf6", "\u1dbf", "\u2090", "\u209c", "\u2188", "\u2ceb", "\u2cee", "\u2cf2", "\u2cf3", "\u2d27", "\u2d2d", "\u2d67", "\u2d6f", "\u2d80", "\u2d96", "\u2da0", "\u2da6", "\u2da8", "\u2dae", "\u2db0", "\u2db6", "\u2db8", "\u2dbe", "\u2dc0", "\u2dc6", "\u2dc8", "\u2dce", "\u2dd0", "\u2dd6", "\u2dd8", "\u2dde", "\u2e2f", "\u3005", "\u3007", "\u3021", "\u3029", "\u3031", "\u3035", "\u3038", "\u303c", "\u3041", "\u3096", "\u309d", "\u309f", "\u30fa", "\u30ff", "\u3105", "\u312d", "\u3131", "\u318e", "\u31a0", "\u31ba", "\u31f0", "\u31ff", "\u3400", "\u4db5", "\u9fcc", "\ua000", "\ua48c", "\ua4d0", "\ua4fd", "\ua500", "\ua60c", "\ua610", "\ua61f", "\ua62a", "\ua62b", "\ua66e", "\ua67f", "\ua69d", "\ua6a0", "\ua6ef", "\ua717", "\ua71f", "\ua788", "\ua78e", "\ua790", "\ua7ad", "\ua7b0", "\ua7b1", "\ua7f7", "\ua801", "\ua803", "\ua805", "\ua807", "\ua80a", "\ua80c", "\ua822", "\ua840", "\ua873", "\ua882", "\ua8b3", "\ua8f2", "\ua8f7", "\ua8fb", "\ua90a", "\ua925", "\ua930", "\ua946", "\ua960", "\ua97c", "\ua984", "\ua9b2", "\ua9cf", "\ua9e0", "\ua9e4", "\ua9e6", "\ua9ef", "\ua9fa", "\ua9fe", "\uaa00", "\uaa28", "\uaa40", "\uaa42", "\uaa44", "\uaa4b", "\uaa60", "\uaa76", "\uaa7a", "\uaa7e", "\uaaaf", "\uaab1", "\uaab5", "\uaab6", "\uaab9", "\uaabd", "\uaac0", "\uaac2", "\uaadb", "\uaadd", "\uaae0", "\uaaea", "\uaaf2", "\uaaf4", "\uab01", "\uab06", "\uab09", "\uab0e", "\uab11", "\uab16", "\uab20", "\uab26", "\uab28", "\uab2e", "\uab30", "\uab5a", "\uab5c", "\uab5f", "\uab64", "\uab65", "\uabc0", "\uabe2", "\ud7a3", "\ud7b0", "\ud7c6", "\ud7cb", "\ud7fb", "\ufa6d", "\ufa70", "\ufad9", "\ufb1d", "\ufb1f", "\ufb28", "\ufb2a", "\ufb36", "\ufb38", "\ufb3c", "\ufb3e", "\ufb40", "\ufb41", "\ufb43", "\ufb44", "\ufb46", "\ufbb1", "\ufbd3", "\ufd3d", "\ufd50", "\ufd8f", "\ufd92", "\ufdc7", "\ufdfb", "\ufe70", "\ufe74", "\ufe76", "\ufefc", "\uff66", "\uffbe", "\uffc2", "\uffc7", "\uffca", "\uffcf", "\uffd2", "\uffd7", "\uffda", "\uffdc", "\u0483", "\u0487", "\u0591", "\u05bd", "\u05c1", "\u05c2", "\u05c4", "\u05c5", "\u05c7", "\u0610", "\u061a", "\u06dc", "\u06df", "\u06e8", "\u06ea", "\u074a", "\u07c0", "\u082d", "\u085b", "\u08e4", "\u0963", "\u09bc", "\u09c4", "\u09d7", "\u09e3", "\u0a01", "\u0a03", "\u0a51", "\u0a75", "\u0a81", "\u0abc", "\u0ac5", "\u0ac9", "\u0ae3", "\u0b44", "\u0b56", "\u0b57", "\u0b63", "\u0b66", "\u0b6f", "\u0b82", "\u0bd7", "\u0c00", "\u0c44", "\u0c55", "\u0c56", "\u0c63", "\u0c66", "\u0c6f", "\u0c81", "\u0cbc", "\u0cc4", "\u0ce3", "\u0d01", "\u0d03", "\u0d44", "\u0d57", "\u0d63", "\u0d66", "\u0d6f", "\u0d83", "\u0ddf", "\u0de6", "\u0def", "\u0df2", "\u0df3", "\u0e3a", "\u0e4e", "\u0e50", "\u0e59", "\u0eb9", "\u0ed0", "\u0ed9", "\u0f18", "\u0f19", "\u0f35", "\u0f37", "\u0f39", "\u0f3e", "\u0f84", "\u0f86", "\u0f99", "\u0fbc", "\u0fc6", "\u109d", "\u135d", "\u135f", "\u1714", "\u1734", "\u1753", "\u1772", "\u1773", "\u17d3", "\u17dd", "\u180b", "\u180d", "\u1810", "\u1819", "\u1920", "\u192b", "\u1930", "\u193b", "\u1946", "\u19b0", "\u19c9", "\u19d0", "\u19d9", "\u1a1b", "\u1a5e", "\u1a60", "\u1a7c", "\u1a7f", "\u1a89", "\u1a90", "\u1a99", "\u1ab0", "\u1abd", "\u1b00", "\u1b50", "\u1b59", "\u1b6b", "\u1b73", "\u1b80", "\u1bf3", "\u1c37", "\u1c40", "\u1c49", "\u1cd0", "\u1cd2", "\u1cd4", "\u1cf8", "\u1cf9", "\u1df5", "\u1dfc", "\u2054", "\u20d0", "\u20e1", "\u20f0", "\u2d7f", "\u2de0", "\u2dff", "\u302f", "\u3099", "\u309a", "\ua66f", "\ua674", "\ua67d", "\ua69f", "\ua6f1", "\ua827", "\ua880", "\ua8c4", "\ua8d0", "\ua8d9", "\ua8e0", "\ua900", "\ua92d", "\ua953", "\ua980", "\ua9c0", "\ua9d9", "\uaa36", "\uaa4d", "\uaa50", "\uaa59", "\uaaef", "\uaaf6", "\uabea", "\uabec", "\uabed", "\uabf0", "\uabf9", "\ufe0f", "\ufe20", "\ufe2d", "\ufe34", "\ufe4d", "\ufe4f", "\uff19", "\u2103", "\uff65", "\u309e", "\u30fd", "\u30fe", "\u30a5", "\u30ee", "\u30f5", "\u3043", "\u3045", "\u3047", "\u3049", "\u3083", "\u3085", "\u308e", "\u3095", "\u31f1", "\u31f2", "\u31f3", "\u31f4", "\u31f5", "\u31f6", "\u31f7", "\u31f8", "\u31f9", "\u31fa", "\u31fb", "\u31fc", "\u31fd", "\u31fe", "\u303b", "\uff67", "\uff68", "\uff69", "\uff6a", "\uff6b", "\uff6c", "\uff6d", "\uff6e", "\uff6f", "\uff70", "\u23ce", "\uffeb", "\u030d", "\u030e", "\u0304", "\u0305", "\u033f", "\u0306", "\u0310", "\u0352", "\u0357", "\u0351", "\u034a", "\u034b", "\u034c", "\u0302", "\u0350", "\u030b", "\u030f", "\u0312", "\u033d", "\u0309", "\u0363", "\u0364", "\u0365", "\u0366", "\u0367", "\u0368", "\u0369", "\u036a", "\u036b", "\u036c", "\u036d", "\u036e", "\u033e", "\u035b", "\u0346", "\u031a", "\u0316", "\u0317", "\u0318", "\u0319", "\u031c", "\u031d", "\u031e", "\u031f", "\u0320", "\u0324", "\u0325", "\u0326", "\u0329", "\u032a", "\u032b", "\u032c", "\u032d", "\u032e", "\u032f", "\u0330", "\u0332", "\u0339", "\u033a", "\u033b", "\u033c", "\u0347", "\u0348", "\u0349", "\u034d", "\u034e", "\u0353", "\u0354", "\u0355", "\u0356", "\u0359", "\u035a", "\u0323", "\u0315", "\u031b", "\u0358", "\u0321", "\u0322", "\u0327", "\u0334", "\u0335", "\u0336", "\u035c", "\u035d", "\u035e", "\u035f", "\u0360", "\u0362", "\u0337", "\u0361", "\u0489", "\u2206", "\u258c", "\u2590", "\u2219", "\u2320", "\u2321", "\u0e03", "\u0e05", "\u0e06", "\u0e09", "\u0e0c", "\u0e0f", "\u0e11", "\u0e26", "\u0e2c", "\u0e2f", "\u0e3f", "\u0e45", "\u0e4a", "\u0e4b", "\u0e4d", "\u0e4f", "\u0e51", "\u0e52", "\u0e53", "\u0e54", "\u0e55", "\u0e56", "\u0e57", "\u0e58", "\u0e5a", "\u0e5b", "\u0385", "\u0384", "\u05b0", "\u05b1", "\u05b2", "\u05b3", "\u05b4", "\u05b5", "\u05b6", "\u05b9", "\u05ba", "\u05bb", "\u05c0", "\u05c3", "\u05f4", "\u0691", "\u06ba", "\u061f", "\u064c", "\u064d", "\u20ab", "\u20af", "\u2017", "\u20a7", "\u066a", "\ufef7", "\ufef8", "\ufe82", "\ufe84", "\ufe8e", "\ufe8f", "\ufe95", "\ufe99", "\ufe9d", "\ufea1", "\ufea5", "\ufed1", "\ufeb1", "\ufeb5", "\ufeb9", "\ufe80", "\ufe81", "\ufe83", "\ufe85", "\ufeca", "\ufe8b", "\ufe8d", "\ufe91", "\ufe93", "\ufe97", "\ufe9b", "\ufe9f", "\ufea3", "\ufea7", "\ufea9", "\ufeab", "\ufead", "\ufeaf", "\ufeb3", "\ufeb7", "\ufebb", "\ufebf", "\ufec1", "\ufec5", "\ufecb", "\ufecf", "\ufec9", "\ufed3", "\ufed7", "\ufedb", "\ufedf", "\ufee3", "\ufee7", "\ufeeb", "\ufeed", "\ufeef", "\ufef3", "\ufebd", "\ufecc", "\ufece", "\ufecd", "\ufee1", "\ufe7d", "\ufee5", "\ufee9", "\ufeec", "\ufef0", "\ufef2", "\ufed0", "\ufed5", "\ufef5", "\ufef6", "\ufedd", "\ufed9", "\ufef1", "\ufe88", "\uf8f6", "\uf8f5", "\uf8f4", "\uf8f7", "\ufe71", "\ufe79", "\ufe7b", "\ufe7f", "\ufe77", "\ufe8a", "\ufefa", "\uf8fa", "\uf8f9", "\uf8f8", "\uf8fb", "\ufec7", "\uf8fc", "\ufef9", "\u0e9d", "\u0ea2", "\u0eae", "\u0eaf", "\u0ebc", "\u0eca", "\u0ecb", "\u0ecc", "\u0edd", "\u20ad", "\u0ed1", "\u0ed2", "\u0ed3", "\u0ed4", "\u0ed5", "\u0ed6", "\u0ed7", "\u0ed8", "\u0387", "\uf88c", "\uf88f", "\uf892", "\uf895", "\uf898", "\uf88b", "\uf88e", "\uf891", "\uf894", "\uf897", "\uf899", "\uf884", "\uf889", "\uf885", "\uf886", "\uf887", "\uf888", "\uf88a", "\uf88d", "\uf890", "\uf893", "\uf896", "\ufeff", "\u0589", "\u058a", "\u055c", "\u055b", "\u055e", "\u055a", "\u10df", "\u10f0", "\u10f1", "\u10f2", "\u10f3", "\u10f4", "\u10f5", "\u10f6", "\u02cb", "\u20a4", "\u4e02", "\u4e04", "\u4e05", "\u4e06", "\u4e0f", "\u4e12", "\u4e17", "\u4e1f", "\u4e20", "\u4e21", "\u4e23", "\u4e29", "\u4e2e", "\u4e2f", "\u4e31", "\u4e33", "\u4e35", "\u4e37", "\u4e3c", "\u4e40", "\u4e41", "\u4e42", "\u4e44", "\u4e46", "\u4e4a", "\u4e51", "\u4e55", "\u4e57", "\u4e5a", "\u4e5b", "\u4e62", "\u4e63", "\u4e64", "\u4e65", "\u4e67", "\u4e68", "\u4e6a", "\u4e72", "\u4e74", "\u4e7f", "\u4e87", "\u4e8a", "\u4e90", "\u4e96", "\u4e97", "\u4e99", "\u4e9c", "\u4e9d", "\u4e9e", "\u4ea3", "\u4eaa", "\u4eaf", "\u4eb0", "\u4eb1", "\u4eb4", "\u4eb6", "\u4eb7", "\u4eb8", "\u4eb9", "\u4ebc", "\u4ebd", "\u4ebe", "\u4ec8", "\u4ecc", "\u4ecf", "\u4ed0", "\u4ed2", "\u4eda", "\u4edb", "\u4edc", "\u4ee0", "\u4ee2", "\u4ee6", "\u4ee7", "\u4ee9", "\u4eed", "\u4eee", "\u4eef", "\u4ef1", "\u4ef4", "\u4ef8", "\u4ef9", "\u4efa", "\u4efc", "\u4efe", "\u4f00", "\u4f02", "\u4f0b", "\u4f0c", "\u4f12", "\u4f1c", "\u4f1d", "\u4f21", "\u4f23", "\u4f28", "\u4f29", "\u4f2c", "\u4f2d", "\u4f2e", "\u4f31", "\u4f33", "\u4f35", "\u4f37", "\u4f39", "\u4f3b", "\u4f3e", "\u4f44", "\u4f45", "\u4f47", "\u4f52", "\u4f54", "\u4f56", "\u4f61", "\u4f62", "\u4f66", "\u4f68", "\u4f6a", "\u4f6b", "\u4f6d", "\u4f6e", "\u4f71", "\u4f72", "\u4f75", "\u4f77", "\u4f78", "\u4f79", "\u4f7a", "\u4f7d", "\u4f80", "\u4f81", "\u4f82", "\u4f85", "\u4f87", "\u4f8a", "\u4f8c", "\u4f8e", "\u4f90", "\u4f92", "\u4f93", "\u4f95", "\u4f96", "\u4f98", "\u4f99", "\u4f9a", "\u4f9c", "\u4f9e", "\u4f9f", "\u4fa1", "\u4fa2", "\u4fa4", "\u4fab", "\u4fad", "\u4fb0", "\u4fb6", "\u4fc0", "\u4fc1", "\u4fc2", "\u4fc6", "\u4fc7", "\u4fc8", "\u4fc9", "\u4fcb", "\u4fcc", "\u4fcd", "\u4fd2", "\u4fd9", "\u4fdb", "\u4fe0", "\u4fe2", "\u4fe4", "\u4fe5", "\u4fe7", "\u4feb", "\u4fec", "\u4ff0", "\u4ff2", "\u4ff4", "\u4ff5", "\u4ff6", "\u4ff7", "\u4ff9", "\u4ffb", "\u4ffc", "\u4ffd", "\u4fff", "\u500e", "\u5010", "\u5013", "\u5015", "\u5016", "\u5017", "\u501b", "\u501d", "\u501e", "\u5020", "\u5022", "\u5023", "\u5027", "\u502b", "\u502f", "\u503b", "\u503d", "\u503f", "\u5040", "\u5041", "\u5042", "\u5044", "\u5045", "\u5046", "\u5049", "\u504a", "\u504b", "\u504d", "\u5050", "\u5056", "\u5057", "\u5058", "\u5059", "\u505b", "\u505d", "\u5066", "\u506d", "\u5078", "\u5079", "\u507a", "\u507c", "\u507d", "\u5081", "\u5082", "\u5083", "\u5084", "\u5086", "\u5087", "\u5089", "\u508a", "\u508b", "\u508c", "\u508e", "\u50a4", "\u50a6", "\u50aa", "\u50ab", "\u50ad", "\u50bc", "\u50bd", "\u50d0", "\u50d7", "\u50d8", "\u50d9", "\u50db", "\u50e8", "\u50e9", "\u50ea", "\u50eb", "\u50ef", "\u50f0", "\u50f1", "\u50f2", "\u50f4", "\u50f6", "\u50fc", "\u5108", "\u5109", "\u510a", "\u510c", "\u5113", "\u5122", "\u5142", "\u5147", "\u514a", "\u514c", "\u514e", "\u514f", "\u5150", "\u5152", "\u5153", "\u5157", "\u5158", "\u5159", "\u515b", "\u515d", "\u5163", "\u5164", "\u5166", "\u516a", "\u516f", "\u5172", "\u517a", "\u517e", "\u517f", "\u5183", "\u5184", "\u5187", "\u518b", "\u518e", "\u518f", "\u5190", "\u5191", "\u5193", "\u5194", "\u5198", "\u519a", "\u519d", "\u519e", "\u519f", "\u51a1", "\u51a3", "\u51a6", "\u51ad", "\u51ae", "\u51b4", "\u51b8", "\u51b9", "\u51ba", "\u51be", "\u51bf", "\u51c1", "\u51c2", "\u51c3", "\u51c5", "\u51c8", "\u51ca", "\u51cd", "\u51ce", "\u51d0", "\u51d2", "\u51d8", "\u51d9", "\u51da", "\u51dc", "\u51de", "\u51df", "\u51e2", "\u51e3", "\u51e5", "\u51ec", "\u51ee", "\u51f1", "\u51f2", "\u51f4", "\u51f7", "\u51fe", "\u5204", "\u5205", "\u5209", "\u520b", "\u520c", "\u520f", "\u5210", "\u5213", "\u5214", "\u5215", "\u521c", "\u521e", "\u521f", "\u5221", "\u5222", "\u5223", "\u5226", "\u5227", "\u522a", "\u522c", "\u522f", "\u5231", "\u5232", "\u5234", "\u5235", "\u523c", "\u523e", "\u5244", "\u524b", "\u524e", "\u524f", "\u5252", "\u5253", "\u5255", "\u5257", "\u5258", "\u5259", "\u525a", "\u525b", "\u525d", "\u525f", "\u5260", "\u5262", "\u5263", "\u5264", "\u5266", "\u5268", "\u526b", "\u526c", "\u526d", "\u526e", "\u5270", "\u5271", "\u5273", "\u527e", "\u5280", "\u5283", "\u5289", "\u5291", "\u5292", "\u5294", "\u529c", "\u52a4", "\u52a5", "\u52a6", "\u52a7", "\u52ae", "\u52af", "\u52b0", "\u52b4", "\u52c0", "\u52c1", "\u52c2", "\u52c4", "\u52c5", "\u52c6", "\u52c8", "\u52ca", "\u52cc", "\u52cd", "\u52ce", "\u52cf", "\u52d1", "\u52d3", "\u52d4", "\u52d7", "\u52e0", "\u52e1", "\u52e2", "\u52e3", "\u52e5", "\u52f1", "\u52fb", "\u52fc", "\u52fd", "\u5301", "\u5302", "\u5303", "\u5304", "\u5307", "\u5309", "\u530a", "\u530b", "\u530c", "\u530e", "\u5311", "\u5312", "\u5313", "\u5314", "\u5318", "\u531b", "\u531c", "\u531e", "\u531f", "\u5322", "\u5324", "\u5325", "\u5327", "\u5328", "\u5329", "\u532b", "\u532c", "\u532d", "\u532f", "\u533c", "\u533d", "\u5342", "\u5344", "\u5346", "\u534b", "\u534c", "\u534d", "\u5350", "\u5359", "\u535b", "\u535d", "\u5365", "\u5368", "\u536a", "\u536c", "\u536d", "\u5372", "\u5376", "\u5379", "\u537c", "\u537d", "\u537e", "\u5380", "\u5381", "\u5383", "\u5387", "\u5388", "\u538a", "\u538e", "\u538f", "\u5390", "\u5396", "\u5397", "\u5399", "\u539b", "\u539c", "\u539e", "\u53a0", "\u53a1", "\u53a4", "\u53a7", "\u53aa", "\u53ab", "\u53ac", "\u53ad", "\u53af", "\u53b7", "\u53b8", "\u53b9", "\u53ba", "\u53bc", "\u53bd", "\u53be", "\u53c0", "\u53ce", "\u53cf", "\u53d0", "\u53d2", "\u53d3", "\u53d5", "\u53da", "\u53dc", "\u53dd", "\u53de", "\u53e1", "\u53e2", "\u53e7", "\u53f4", "\u53fa", "\u53fe", "\u53ff", "\u5400", "\u5402", "\u5405", "\u5407", "\u540b", "\u5414", "\u5418", "\u5419", "\u541a", "\u541c", "\u5422", "\u5424", "\u5425", "\u542a", "\u5430", "\u5433", "\u5436", "\u5437", "\u543a", "\u543d", "\u543f", "\u5441", "\u5442", "\u5444", "\u5445", "\u5447", "\u5449", "\u544c", "\u544d", "\u544e", "\u544f", "\u5451", "\u545a", "\u545d", "\u5463", "\u5465", "\u5467", "\u5469", "\u5474", "\u5479", "\u547a", "\u547e", "\u547f", "\u5481", "\u5483", "\u5485", "\u5487", "\u5488", "\u5489", "\u548a", "\u548d", "\u5491", "\u5493", "\u5497", "\u5498", "\u549c", "\u549e", "\u549f", "\u54a0", "\u54a1", "\u54a2", "\u54a5", "\u54ae", "\u54b0", "\u54b2", "\u54b5", "\u54b6", "\u54b7", "\u54b9", "\u54ba", "\u54bc", "\u54be", "\u54c3", "\u54c5", "\u54ca", "\u54cb", "\u54d6", "\u54d8", "\u54db", "\u54e0", "\u54eb", "\u54ec", "\u54ef", "\u54f0", "\u54f1", "\u54f4", "\u54fb", "\u54fe", "\u5500", "\u5502", "\u5503", "\u5504", "\u5505", "\u5508", "\u550a", "\u5512", "\u5513", "\u5515", "\u551c", "\u551d", "\u551e", "\u551f", "\u5521", "\u5525", "\u5526", "\u5528", "\u5529", "\u552b", "\u552d", "\u5532", "\u5534", "\u5535", "\u5536", "\u5538", "\u5539", "\u553a", "\u553b", "\u553d", "\u5540", "\u5542", "\u5545", "\u5547", "\u5548", "\u554b", "\u5551", "\u5552", "\u5554", "\u5557", "\u555d", "\u555e", "\u5560", "\u5562", "\u5563", "\u5568", "\u5569", "\u556b", "\u556f", "\u5579", "\u557a", "\u557d", "\u557f", "\u5585", "\u5586", "\u558c", "\u558d", "\u558e", "\u5590", "\u5592", "\u5593", "\u5595", "\u5596", "\u5597", "\u559a", "\u559b", "\u559e", "\u55a0", "\u55a8", "\u55b2", "\u55b4", "\u55b6", "\u55b8", "\u55ba", "\u55bc", "\u55bf", "\u55c6", "\u55c7", "\u55c8", "\u55ca", "\u55cb", "\u55ce", "\u55cf", "\u55d0", "\u55d5", "\u55d7", "\u55de", "\u55e0", "\u55e2", "\u55e7", "\u55e9", "\u55ed", "\u55ee", "\u55f0", "\u55f1", "\u55f4", "\u55f6", "\u55f8", "\u55ff", "\u5602", "\u5603", "\u5604", "\u5605", "\u5606", "\u5607", "\u560a", "\u560b", "\u560d", "\u5610", "\u5619", "\u561a", "\u561c", "\u561d", "\u5620", "\u5621", "\u5622", "\u5625", "\u5626", "\u5628", "\u5629", "\u562a", "\u562b", "\u562e", "\u562f", "\u5630", "\u5633", "\u5635", "\u5637", "\u5638", "\u563a", "\u563c", "\u563d", "\u563e", "\u5640", "\u564f", "\u5655", "\u5656", "\u565a", "\u565b", "\u565d", "\u5663", "\u5665", "\u5666", "\u5667", "\u566d", "\u566e", "\u566f", "\u5670", "\u5672", "\u5673", "\u5674", "\u5675", "\u5677", "\u5678", "\u5679", "\u567a", "\u567d", "\u5687", "\u5690", "\u5691", "\u5692", "\u5694", "\u56a4", "\u56b0", "\u56b8", "\u56b9", "\u56ba", "\u56bb", "\u56bd", "\u56cb", "\u56d5", "\u56d6", "\u56d8", "\u56d9", "\u56dc", "\u56e3", "\u56e5", "\u56ec", "\u56ee", "\u56ef", "\u56f3", "\u56f6", "\u56f7", "\u56f8", "\u56fb", "\u56fc", "\u5700", "\u5701", "\u5702", "\u5705", "\u5707", "\u5712", "\u571d", "\u571e", "\u5720", "\u5721", "\u5722", "\u5724", "\u5725", "\u5726", "\u5727", "\u572b", "\u5731", "\u5732", "\u5734", "\u573c", "\u573d", "\u573f", "\u5741", "\u5743", "\u5744", "\u5745", "\u5746", "\u5748", "\u5749", "\u574b", "\u5752", "\u5758", "\u5759", "\u5762", "\u5763", "\u5765", "\u5767", "\u576c", "\u576e", "\u5770", "\u5771", "\u5772", "\u5774", "\u5775", "\u5778", "\u5779", "\u577a", "\u577d", "\u577e", "\u577f", "\u5780", "\u5781", "\u5787", "\u5788", "\u5789", "\u578a", "\u578d", "\u5794", "\u579c", "\u579d", "\u579e", "\u579f", "\u57a5", "\u57a8", "\u57aa", "\u57ac", "\u57af", "\u57b0", "\u57b1", "\u57b3", "\u57b5", "\u57b6", "\u57b7", "\u57b9", "\u57c4", "\u57cc", "\u57cd", "\u57d0", "\u57d1", "\u57d3", "\u57d6", "\u57d7", "\u57db", "\u57dc", "\u57de", "\u57e1", "\u57e2", "\u57e3", "\u57e5", "\u57ee", "\u57f0", "\u57f1", "\u57f2", "\u57f3", "\u57f5", "\u57f6", "\u57fb", "\u57fc", "\u57fe", "\u57ff", "\u5801", "\u5803", "\u5804", "\u5805", "\u5808", "\u5809", "\u580a", "\u580c", "\u580e", "\u580f", "\u5810", "\u5812", "\u5813", "\u5814", "\u5816", "\u5817", "\u5818", "\u581a", "\u581b", "\u581c", "\u581d", "\u581f", "\u5822", "\u5823", "\u5825", "\u582b", "\u5832", "\u5833", "\u5836", "\u583e", "\u5845", "\u584e", "\u584f", "\u5850", "\u5852", "\u5853", "\u5855", "\u5856", "\u5857", "\u5859", "\u585f", "\u5866", "\u586d", "\u587f", "\u5882", "\u5884", "\u5886", "\u5887", "\u5888", "\u588a", "\u588b", "\u588c", "\u588d", "\u5894", "\u589b", "\u589c", "\u589d", "\u58a0", "\u58aa", "\u58bd", "\u58be", "\u58bf", "\u58c0", "\u58c2", "\u58c3", "\u58c4", "\u58c6", "\u58d2", "\u58d3", "\u58d4", "\u58d6", "\u58e5", "\u58ed", "\u58ef", "\u58f1", "\u58f2", "\u58f4", "\u58f5", "\u58f7", "\u58f8", "\u58fa", "\u5903", "\u5905", "\u5906", "\u5908", "\u590e", "\u5910", "\u5911", "\u5912", "\u5913", "\u5917", "\u5918", "\u591b", "\u591d", "\u591e", "\u5921", "\u5922", "\u5923", "\u5926", "\u5928", "\u592c", "\u5930", "\u5932", "\u5933", "\u5935", "\u5936", "\u593b", "\u593d", "\u593f", "\u5940", "\u5943", "\u5945", "\u5946", "\u594a", "\u594c", "\u594d", "\u5950", "\u5952", "\u5953", "\u5959", "\u595b", "\u5961", "\u5963", "\u5964", "\u5966", "\u5975", "\u5977", "\u597a", "\u597b", "\u597c", "\u597e", "\u597f", "\u5980", "\u5985", "\u5989", "\u598b", "\u598c", "\u598e", "\u598f", "\u5990", "\u5991", "\u5994", "\u5995", "\u5998", "\u599a", "\u599b", "\u599c", "\u599d", "\u599f", "\u59a0", "\u59a1", "\u59a2", "\u59a6", "\u59a7", "\u59ac", "\u59ad", "\u59b0", "\u59b1", "\u59b3", "\u59ba", "\u59bc", "\u59bd", "\u59bf", "\u59c7", "\u59c8", "\u59c9", "\u59cc", "\u59cd", "\u59ce", "\u59cf", "\u59d5", "\u59d6", "\u59d9", "\u59db", "\u59de", "\u59e4", "\u59e6", "\u59e7", "\u59e9", "\u59ea", "\u59eb", "\u59ed", "\u59fa", "\u59fc", "\u59fd", "\u59fe", "\u5a00", "\u5a02", "\u5a0a", "\u5a0b", "\u5a0d", "\u5a0e", "\u5a0f", "\u5a10", "\u5a12", "\u5a14", "\u5a15", "\u5a16", "\u5a17", "\u5a19", "\u5a1a", "\u5a1b", "\u5a1d", "\u5a1e", "\u5a21", "\u5a22", "\u5a24", "\u5a26", "\u5a27", "\u5a28", "\u5a2a", "\u5a33", "\u5a35", "\u5a37", "\u5a3d", "\u5a3e", "\u5a3f", "\u5a41", "\u5a47", "\u5a48", "\u5a4b", "\u5a56", "\u5a57", "\u5a58", "\u5a59", "\u5a5b", "\u5a61", "\u5a63", "\u5a64", "\u5a65", "\u5a66", "\u5a68", "\u5a69", "\u5a6b", "\u5a78", "\u5a79", "\u5a7b", "\u5a7c", "\u5a7d", "\u5a7e", "\u5a80", "\u5a93", "\u5a9c", "\u5aab", "\u5aac", "\u5aad", "\u5ab4", "\u5ab6", "\u5ab7", "\u5ab9", "\u5abf", "\u5ac0", "\u5ac3", "\u5aca", "\u5acb", "\u5acd", "\u5ad3", "\u5ad5", "\u5ad7", "\u5ad9", "\u5ada", "\u5adb", "\u5add", "\u5ade", "\u5adf", "\u5ae2", "\u5ae4", "\u5ae5", "\u5ae7", "\u5ae8", "\u5aea", "\u5aec", "\u5af2", "\u5b0a", "\u5b18", "\u5b33", "\u5b35", "\u5b36", "\u5b38", "\u5b41", "\u5b48", "\u5b52", "\u5b56", "\u5b5e", "\u5b60", "\u5b61", "\u5b67", "\u5b68", "\u5b6b", "\u5b6d", "\u5b6e", "\u5b6f", "\u5b72", "\u5b74", "\u5b76", "\u5b77", "\u5b78", "\u5b79", "\u5b7b", "\u5b7c", "\u5b7e", "\u5b7f", "\u5b82", "\u5b86", "\u5b8a", "\u5b8d", "\u5b8e", "\u5b90", "\u5b91", "\u5b92", "\u5b94", "\u5b96", "\u5ba7", "\u5ba8", "\u5ba9", "\u5bac", "\u5bad", "\u5bae", "\u5baf", "\u5bb1", "\u5bb2", "\u5bb7", "\u5bba", "\u5bbb", "\u5bbc", "\u5bc0", "\u5bc1", "\u5bc3", "\u5bc8", "\u5bc9", "\u5bca", "\u5bcb", "\u5bcd", "\u5bce", "\u5bcf", "\u5bd1", "\u5bd4", "\u5be0", "\u5be2", "\u5be3", "\u5be7", "\u5be9", "\u5bef", "\u5bf1", "\u5bfd", "\u5c00", "\u5c02", "\u5c03", "\u5c05", "\u5c08", "\u5c0c", "\u5c10", "\u5c12", "\u5c13", "\u5c17", "\u5c19", "\u5c1b", "\u5c1e", "\u5c1f", "\u5c20", "\u5c21", "\u5c23", "\u5c26", "\u5c28", "\u5c29", "\u5c2a", "\u5c2b", "\u5c2d", "\u5c2e", "\u5c2f", "\u5c30", "\u5c32", "\u5c33", "\u5c35", "\u5c36", "\u5c37", "\u5c43", "\u5c44", "\u5c46", "\u5c47", "\u5c4c", "\u5c4d", "\u5c52", "\u5c53", "\u5c54", "\u5c56", "\u5c57", "\u5c58", "\u5c5a", "\u5c5b", "\u5c5c", "\u5c5d", "\u5c5f", "\u5c62", "\u5c67", "\u5c70", "\u5c72", "\u5c7b", "\u5c7c", "\u5c7d", "\u5c7e", "\u5c80", "\u5c83", "\u5c89", "\u5c8a", "\u5c8b", "\u5c8e", "\u5c8f", "\u5c92", "\u5c93", "\u5c95", "\u5c9d", "\u5ca4", "\u5caa", "\u5cae", "\u5caf", "\u5cb0", "\u5cb2", "\u5cb4", "\u5cb6", "\u5cb9", "\u5cba", "\u5cbb", "\u5cbc", "\u5cbe", "\u5cc0", "\u5cc2", "\u5cc3", "\u5cc5", "\u5ccc", "\u5cd3", "\u5cda", "\u5ce2", "\u5ce3", "\u5ce7", "\u5ce9", "\u5ceb", "\u5cec", "\u5cee", "\u5cef", "\u5cf1", "\u5cfc", "\u5d01", "\u5d04", "\u5d05", "\u5d08", "\u5d0f", "\u5d15", "\u5d17", "\u5d18", "\u5d19", "\u5d1a", "\u5d1c", "\u5d1d", "\u5d1f", "\u5d25", "\u5d28", "\u5d2a", "\u5d2b", "\u5d2c", "\u5d2f", "\u5d35", "\u5d3f", "\u5d48", "\u5d49", "\u5d4d", "\u5d59", "\u5d5a", "\u5d5c", "\u5d5e", "\u5d6a", "\u5d6d", "\u5d6e", "\u5d70", "\u5d71", "\u5d72", "\u5d73", "\u5d75", "\u5d83", "\u5d9a", "\u5d9b", "\u5d9c", "\u5d9e", "\u5d9f", "\u5da0", "\u5da1", "\u5db8", "\u5dc6", "\u5dce", "\u5ddc", "\u5ddf", "\u5de0", "\u5de3", "\u5de4", "\u5dea", "\u5dec", "\u5ded", "\u5df0", "\u5df5", "\u5df6", "\u5df8", "\u5dff", "\u5e00", "\u5e04", "\u5e07", "\u5e09", "\u5e0a", "\u5e0b", "\u5e0d", "\u5e0e", "\u5e12", "\u5e13", "\u5e17", "\u5e1e", "\u5e28", "\u5e2f", "\u5e32", "\u5e39", "\u5e3a", "\u5e3e", "\u5e3f", "\u5e40", "\u5e41", "\u5e43", "\u5e46", "\u5e4d", "\u5e56", "\u5e5c", "\u5e5d", "\u5e60", "\u5e63", "\u5e75", "\u5e77", "\u5e79", "\u5e81", "\u5e82", "\u5e83", "\u5e85", "\u5e88", "\u5e89", "\u5e8c", "\u5e8d", "\u5e8e", "\u5e92", "\u5e98", "\u5e9b", "\u5e9d", "\u5ea1", "\u5ea2", "\u5ea3", "\u5ea4", "\u5ea8", "\u5eae", "\u5eb4", "\u5eba", "\u5ebb", "\u5ebc", "\u5ebd", "\u5ebf", "\u5ec6", "\u5ec7", "\u5ec8", "\u5ecb", "\u5ed4", "\u5ed5", "\u5ed7", "\u5ed8", "\u5ed9", "\u5eda", "\u5edc", "\u5ee9", "\u5eeb", "\u5ef5", "\u5ef8", "\u5ef9", "\u5efc", "\u5efd", "\u5f05", "\u5f06", "\u5f07", "\u5f09", "\u5f0c", "\u5f0d", "\u5f0e", "\u5f10", "\u5f12", "\u5f14", "\u5f16", "\u5f19", "\u5f1a", "\u5f1c", "\u5f1d", "\u5f1e", "\u5f21", "\u5f22", "\u5f23", "\u5f24", "\u5f28", "\u5f2b", "\u5f2c", "\u5f2e", "\u5f30", "\u5f32", "\u5f3b", "\u5f3d", "\u5f3e", "\u5f3f", "\u5f41", "\u5f51", "\u5f54", "\u5f59", "\u5f5a", "\u5f5b", "\u5f5c", "\u5f5e", "\u5f5f", "\u5f60", "\u5f63", "\u5f65", "\u5f67", "\u5f68", "\u5f6b", "\u5f6e", "\u5f6f", "\u5f72", "\u5f74", "\u5f75", "\u5f76", "\u5f78", "\u5f7a", "\u5f7d", "\u5f7e", "\u5f7f", "\u5f83", "\u5f86", "\u5f8d", "\u5f8e", "\u5f8f", "\u5f93", "\u5f94", "\u5f96", "\u5f9a", "\u5f9b", "\u5f9d", "\u5f9f", "\u5fa0", "\u5fa2", "\u5fa9", "\u5fab", "\u5fac", "\u5faf", "\u5fb6", "\u5fb8", "\u5fb9", "\u5fba", "\u5fbb", "\u5fbe", "\u5fc7", "\u5fc8", "\u5fca", "\u5fcb", "\u5fce", "\u5fd3", "\u5fd4", "\u5fd5", "\u5fda", "\u5fdb", "\u5fde", "\u5fdf", "\u5fe2", "\u5fe3", "\u5fe5", "\u5fe6", "\u5fe8", "\u5fe9", "\u5fec", "\u5fef", "\u5ff0", "\u5ff2", "\u5ff3", "\u5ff4", "\u5ff6", "\u5ff7", "\u5ff9", "\u5ffa", "\u5ffc", "\u6007", "\u6008", "\u6009", "\u600b", "\u600c", "\u6010", "\u6011", "\u6013", "\u6017", "\u6018", "\u601a", "\u601e", "\u601f", "\u6022", "\u6023", "\u6024", "\u602c", "\u602d", "\u602e", "\u6030", "\u6036", "\u603d", "\u603e", "\u6040", "\u6044", "\u604c", "\u604e", "\u604f", "\u6051", "\u6053", "\u6054", "\u6056", "\u6057", "\u6058", "\u605b", "\u605c", "\u605e", "\u605f", "\u6060", "\u6061", "\u6065", "\u6066", "\u606e", "\u6071", "\u6072", "\u6074", "\u6075", "\u6077", "\u607e", "\u6080", "\u6081", "\u6082", "\u6085", "\u6086", "\u6087", "\u6088", "\u608a", "\u608b", "\u608e", "\u608f", "\u6090", "\u6091", "\u6093", "\u6095", "\u6097", "\u6098", "\u6099", "\u609c", "\u609e", "\u60a1", "\u60a2", "\u60a4", "\u60a5", "\u60a7", "\u60a9", "\u60aa", "\u60ae", "\u60b0", "\u60b3", "\u60b5", "\u60b6", "\u60b7", "\u60b9", "\u60ba", "\u60bd", "\u60c7", "\u60c8", "\u60c9", "\u60cc", "\u60d2", "\u60d3", "\u60d4", "\u60d6", "\u60d7", "\u60d9", "\u60db", "\u60de", "\u60e1", "\u60ea", "\u60f1", "\u60f2", "\u60f5", "\u60f7", "\u60f8", "\u60fb", "\u6102", "\u6103", "\u6104", "\u6105", "\u6107", "\u610a", "\u610b", "\u610c", "\u6110", "\u6116", "\u6117", "\u6118", "\u6119", "\u611b", "\u611c", "\u611d", "\u611e", "\u6121", "\u6122", "\u6125", "\u6128", "\u6129", "\u612a", "\u612c", "\u6140", "\u6147", "\u6149", "\u614d", "\u614f", "\u6150", "\u6152", "\u6153", "\u6154", "\u6156", "\u615e", "\u615f", "\u6160", "\u6161", "\u6163", "\u6164", "\u6165", "\u6166", "\u6169", "\u6171", "\u6172", "\u6173", "\u6174", "\u6176", "\u6178", "\u618c", "\u618d", "\u618f", "\u6195", "\u6196", "\u619e", "\u61aa", "\u61ab", "\u61ad", "\u61b8", "\u61bf", "\u61c0", "\u61c1", "\u61c3", "\u61cc", "\u61d3", "\u61d5", "\u61e7", "\u61f6", "\u6200", "\u6207", "\u6209", "\u6213", "\u6214", "\u6219", "\u621c", "\u621d", "\u621e", "\u6220", "\u6223", "\u6226", "\u6227", "\u6228", "\u6229", "\u622b", "\u622d", "\u622f", "\u6230", "\u6231", "\u6232", "\u6235", "\u6236", "\u6238", "\u6242", "\u6244", "\u6245", "\u6246", "\u624a", "\u624f", "\u6250", "\u6255", "\u6256", "\u6257", "\u6259", "\u625a", "\u625c", "\u6264", "\u6265", "\u6268", "\u6272", "\u6274", "\u6275", "\u6277", "\u6278", "\u627a", "\u627b", "\u627d", "\u6281", "\u6282", "\u6283", "\u6285", "\u6286", "\u6287", "\u6288", "\u628b", "\u6294", "\u6299", "\u629c", "\u629d", "\u62a3", "\u62a6", "\u62a7", "\u62a9", "\u62aa", "\u62ad", "\u62ae", "\u62af", "\u62b0", "\u62b2", "\u62b3", "\u62b4", "\u62b6", "\u62b7", "\u62b8", "\u62ba", "\u62be", "\u62c0", "\u62c1", "\u62c3", "\u62cb", "\u62cf", "\u62d1", "\u62d5", "\u62dd", "\u62de", "\u62e0", "\u62e4", "\u62ea", "\u62eb", "\u62f0", "\u62f2", "\u62f5", "\u62f8", "\u62f9", "\u62fa", "\u62fb", "\u6300", "\u6303", "\u6304", "\u6305", "\u6306", "\u630a", "\u630b", "\u630c", "\u630d", "\u630f", "\u6310", "\u6312", "\u6313", "\u6314", "\u6315", "\u6317", "\u6318", "\u6319", "\u631c", "\u6326", "\u6327", "\u6329", "\u632c", "\u632d", "\u632e", "\u6330", "\u6331", "\u6333", "\u633b", "\u633c", "\u633e", "\u6340", "\u6341", "\u6344", "\u6347", "\u6348", "\u634a", "\u6351", "\u6352", "\u6353", "\u6354", "\u6356", "\u6360", "\u6364", "\u6365", "\u6366", "\u6368", "\u636a", "\u636b", "\u636c", "\u636f", "\u6370", "\u6372", "\u6373", "\u6374", "\u6375", "\u6378", "\u6379", "\u637c", "\u637d", "\u637e", "\u637f", "\u6381", "\u6383", "\u6384", "\u6385", "\u6386", "\u638b", "\u638d", "\u6391", "\u6393", "\u6394", "\u6395", "\u6397", "\u6399", "\u63a1", "\u63a4", "\u63a6", "\u63ab", "\u63af", "\u63b1", "\u63b2", "\u63b5", "\u63b6", "\u63b9", "\u63bb", "\u63bd", "\u63bf", "\u63c0", "\u63c1", "\u63c2", "\u63c3", "\u63c5", "\u63c7", "\u63c8", "\u63ca", "\u63cb", "\u63cc", "\u63d1", "\u63d3", "\u63d4", "\u63d5", "\u63d7", "\u63df", "\u63e2", "\u63e4", "\u63eb", "\u63ec", "\u63ee", "\u63ef", "\u63f0", "\u63f1", "\u63f3", "\u63f5", "\u63f7", "\u63f9", "\u63fa", "\u63fb", "\u63fc", "\u63fe", "\u6403", "\u6404", "\u6406", "\u640e", "\u6411", "\u6412", "\u6415", "\u641d", "\u641f", "\u6422", "\u6423", "\u6424", "\u6425", "\u6427", "\u6428", "\u6429", "\u642b", "\u642e", "\u6435", "\u643b", "\u643c", "\u643e", "\u6440", "\u6442", "\u6443", "\u6449", "\u644b", "\u6453", "\u6455", "\u6456", "\u6457", "\u6459", "\u645f", "\u6468", "\u646a", "\u646b", "\u646c", "\u646e", "\u647b", "\u6483", "\u6486", "\u6488", "\u6493", "\u6494", "\u6497", "\u6498", "\u649a", "\u649b", "\u649c", "\u649d", "\u649f", "\u64a5", "\u64a6", "\u64a7", "\u64a8", "\u64aa", "\u64ab", "\u64af", "\u64b1", "\u64b2", "\u64b3", "\u64b4", "\u64b6", "\u64b9", "\u64bb", "\u64bd", "\u64be", "\u64bf", "\u64c3", "\u64c4", "\u64c6", "\u64cf", "\u64d1", "\u64d3", "\u64d4", "\u64d5", "\u64d6", "\u64d9", "\u64da", "\u64db", "\u64dc", "\u64dd", "\u64df", "\u64e0", "\u64e1", "\u64e3", "\u64e5", "\u64e7", "\u6501", "\u650a", "\u6513", "\u6519", "\u6522", "\u6523", "\u6524", "\u6526", "\u652c", "\u652d", "\u6530", "\u6531", "\u6532", "\u6533", "\u6537", "\u653a", "\u653c", "\u653d", "\u6540", "\u6546", "\u6547", "\u654a", "\u654b", "\u654d", "\u654e", "\u6550", "\u6552", "\u6553", "\u6554", "\u6558", "\u655a", "\u655c", "\u655f", "\u6560", "\u6561", "\u6564", "\u6565", "\u6567", "\u6568", "\u6569", "\u656a", "\u656d", "\u656e", "\u656f", "\u6571", "\u6573", "\u6575", "\u6576", "\u6588", "\u6589", "\u658a", "\u658d", "\u658e", "\u658f", "\u6592", "\u6594", "\u6595", "\u6596", "\u6598", "\u659a", "\u659d", "\u659e", "\u65a0", "\u65a2", "\u65a3", "\u65a6", "\u65a8", "\u65aa", "\u65ac", "\u65ae", "\u65b1", "\u65ba", "\u65bb", "\u65be", "\u65bf", "\u65c0", "\u65c2", "\u65c7", "\u65c8", "\u65c9", "\u65ca", "\u65cd", "\u65d0", "\u65d1", "\u65d3", "\u65d4", "\u65d5", "\u65d8", "\u65e1", "\u65e3", "\u65e4", "\u65ea", "\u65eb", "\u65f2", "\u65f3", "\u65f4", "\u65f5", "\u65f8", "\u65f9", "\u65fb", "\u6601", "\u6604", "\u6605", "\u6607", "\u6608", "\u6609", "\u660b", "\u660d", "\u6610", "\u6611", "\u6612", "\u6616", "\u6617", "\u6618", "\u661a", "\u661b", "\u661c", "\u661e", "\u6621", "\u6622", "\u6623", "\u6624", "\u6626", "\u6629", "\u662a", "\u662b", "\u662c", "\u662e", "\u6630", "\u6632", "\u6633", "\u6637", "\u663d", "\u663f", "\u6640", "\u6644", "\u664d", "\u664e", "\u6650", "\u6651", "\u6658", "\u6659", "\u665b", "\u665c", "\u665d", "\u665e", "\u6660", "\u6662", "\u6663", "\u6665", "\u6667", "\u6669", "\u6671", "\u6672", "\u6673", "\u6675", "\u6678", "\u6679", "\u667b", "\u667c", "\u667d", "\u667f", "\u6680", "\u6681", "\u6683", "\u6685", "\u6686", "\u6688", "\u6689", "\u668a", "\u668b", "\u668d", "\u668e", "\u668f", "\u6690", "\u6692", "\u6693", "\u6694", "\u6695", "\u6698", "\u669e", "\u66a9", "\u66af", "\u66b5", "\u66b6", "\u66b7", "\u66b8", "\u66ba", "\u66bb", "\u66bc", "\u66bd", "\u66bf", "\u66da", "\u66de", "\u66e7", "\u66e8", "\u66ea", "\u66f1", "\u66f5", "\u66f6", "\u66fa", "\u66fb", "\u66fd", "\u6701", "\u6702", "\u6704", "\u6705", "\u6706", "\u6707", "\u670c", "\u670e", "\u670f", "\u6711", "\u6712", "\u6713", "\u6716", "\u6718", "\u6719", "\u671a", "\u671c", "\u671e", "\u6720", "\u6727", "\u6729", "\u672e", "\u6730", "\u6732", "\u6733", "\u6736", "\u6737", "\u6738", "\u6739", "\u673b", "\u673c", "\u673e", "\u673f", "\u6741", "\u6744", "\u6745", "\u6747", "\u674a", "\u674b", "\u674d", "\u6752", "\u6754", "\u6755", "\u6757", "\u675d", "\u6762", "\u6763", "\u6764", "\u6766", "\u6767", "\u676b", "\u676c", "\u676e", "\u6774", "\u6776", "\u6778", "\u6779", "\u677a", "\u677b", "\u677d", "\u6780", "\u6782", "\u6783", "\u6785", "\u6786", "\u6788", "\u678a", "\u678c", "\u678d", "\u678e", "\u678f", "\u6791", "\u6792", "\u6793", "\u6794", "\u6796", "\u6799", "\u679b", "\u679f", "\u67a0", "\u67a1", "\u67a4", "\u67a6", "\u67a9", "\u67ac", "\u67ae", "\u67b1", "\u67b2", "\u67b4", "\u67b9", "\u67c2", "\u67c5", "\u67d5", "\u67d6", "\u67d7", "\u67db", "\u67df", "\u67e1", "\u67e3", "\u67e4", "\u67e6", "\u67e7", "\u67e8", "\u67ea", "\u67eb", "\u67ed", "\u67ee", "\u67f2", "\u67f5", "\u67fe", "\u6801", "\u6802", "\u6803", "\u6804", "\u6806", "\u680d", "\u6810", "\u6812", "\u6814", "\u6815", "\u6818", "\u681e", "\u681f", "\u6820", "\u6822", "\u682b", "\u6834", "\u6835", "\u6836", "\u683a", "\u683b", "\u683f", "\u6847", "\u684b", "\u684d", "\u684f", "\u6852", "\u6856", "\u685c", "\u685d", "\u685e", "\u685f", "\u686a", "\u686c", "\u6875", "\u6878", "\u6882", "\u6884", "\u6887", "\u6890", "\u6891", "\u6892", "\u6894", "\u6895", "\u6896", "\u6898", "\u68a3", "\u68a4", "\u68a5", "\u68a9", "\u68aa", "\u68ab", "\u68ac", "\u68ae", "\u68b1", "\u68b2", "\u68b4", "\u68b6", "\u68b7", "\u68b8", "\u68b9", "\u68c1", "\u68c3", "\u68ca", "\u68cc", "\u68ce", "\u68cf", "\u68d0", "\u68d1", "\u68d3", "\u68d4", "\u68d6", "\u68d7", "\u68d9", "\u68db", "\u68e1", "\u68e2", "\u68e4", "\u68ef", "\u68f2", "\u68f3", "\u68f4", "\u68f6", "\u68f7", "\u68f8", "\u68fb", "\u68fd", "\u68fe", "\u68ff", "\u6900", "\u6902", "\u6903", "\u6904", "\u6906", "\u690c", "\u690f", "\u6911", "\u6913", "\u6921", "\u6922", "\u6923", "\u6925", "\u692e", "\u692f", "\u6931", "\u6932", "\u6933", "\u6935", "\u6936", "\u6937", "\u6938", "\u693a", "\u693b", "\u693c", "\u693e", "\u6940", "\u6941", "\u6943", "\u6955", "\u6956", "\u6958", "\u6959", "\u695b", "\u695c", "\u695f", "\u6961", "\u6962", "\u6964", "\u6965", "\u6967", "\u6968", "\u6969", "\u696a", "\u696c", "\u696f", "\u6970", "\u6972", "\u697a", "\u697b", "\u697d", "\u697e", "\u697f", "\u6981", "\u6983", "\u6985", "\u698a", "\u698b", "\u698c", "\u698e", "\u6996", "\u6997", "\u6999", "\u699a", "\u699d", "\u69a9", "\u69aa", "\u69ac", "\u69ae", "\u69af", "\u69b0", "\u69b2", "\u69b3", "\u69b5", "\u69b6", "\u69b8", "\u69b9", "\u69ba", "\u69bc", "\u69bd", "\u69be", "\u69bf", "\u69c0", "\u69c2", "\u69cd", "\u69cf", "\u69d1", "\u69d2", "\u69d3", "\u69d5", "\u69dc", "\u69dd", "\u69de", "\u69e1", "\u69ee", "\u69ef", "\u69f0", "\u69f1", "\u69f3", "\u69fe", "\u6a00", "\u6a0b", "\u6a20", "\u6a22", "\u6a2b", "\u6a2c", "\u6a2d", "\u6a2e", "\u6a30", "\u6a32", "\u6a33", "\u6a34", "\u6a36", "\u6a3f", "\u6a45", "\u6a46", "\u6a48", "\u6a51", "\u6a5a", "\u6a5c", "\u6a62", "\u6a63", "\u6a64", "\u6a66", "\u6a72", "\u6a7a", "\u6a7b", "\u6a7d", "\u6a7e", "\u6a7f", "\u6a81", "\u6a82", "\u6a83", "\u6a85", "\u6a8f", "\u6a92", "\u6a98", "\u6aa1", "\u6aa7", "\u6aa8", "\u6aaa", "\u6aad", "\u6b25", "\u6b26", "\u6b28", "\u6b2f", "\u6b30", "\u6b31", "\u6b33", "\u6b34", "\u6b35", "\u6b36", "\u6b38", "\u6b3b", "\u6b3c", "\u6b3d", "\u6b3f", "\u6b40", "\u6b41", "\u6b42", "\u6b44", "\u6b45", "\u6b48", "\u6b4a", "\u6b4b", "\u6b4d", "\u6b5a", "\u6b68", "\u6b69", "\u6b6b", "\u6b7a", "\u6b7d", "\u6b7e", "\u6b7f", "\u6b80", "\u6b85", "\u6b88", "\u6b8c", "\u6b8e", "\u6b8f", "\u6b90", "\u6b91", "\u6b94", "\u6b95", "\u6b97", "\u6b98", "\u6b99", "\u6b9c", "\u6ba2", "\u6bab", "\u6bb6", "\u6bb8", "\u6bc3", "\u6bc4", "\u6bc6", "\u6bcc", "\u6bce", "\u6bd0", "\u6bd1", "\u6bd8", "\u6bda", "\u6bdc", "\u6be2", "\u6bec", "\u6bed", "\u6bee", "\u6bf0", "\u6bf1", "\u6bf2", "\u6bf4", "\u6bf6", "\u6bf7", "\u6bf8", "\u6bfa", "\u6bfb", "\u6bfc", "\u6bfe", "\u6c08", "\u6c0e", "\u6c12", "\u6c1c", "\u6c1d", "\u6c1e", "\u6c20", "\u6c25", "\u6c2b", "\u6c2c", "\u6c2d", "\u6c31", "\u6c33", "\u6c36", "\u6c37", "\u6c39", "\u6c3a", "\u6c3b", "\u6c3c", "\u6c3e", "\u6c3f", "\u6c43", "\u6c44", "\u6c45", "\u6c48", "\u6c4b", "\u6c51", "\u6c52", "\u6c53", "\u6c56", "\u6c58", "\u6c59", "\u6c5a", "\u6c62", "\u6c63", "\u6c65", "\u6c66", "\u6c67", "\u6c6b", "\u6c71", "\u6c73", "\u6c75", "\u6c77", "\u6c78", "\u6c7b", "\u6c7c", "\u6c7f", "\u6c80", "\u6c84", "\u6c87", "\u6c8a", "\u6c8b", "\u6c8d", "\u6c8e", "\u6c91", "\u6c95", "\u6c96", "\u6c97", "\u6c98", "\u6c9a", "\u6c9c", "\u6c9d", "\u6c9e", "\u6ca0", "\u6ca2", "\u6ca8", "\u6cac", "\u6caf", "\u6cb0", "\u6cb4", "\u6cb5", "\u6cb6", "\u6cb7", "\u6cba", "\u6cc0", "\u6cc2", "\u6cc3", "\u6cc6", "\u6cc7", "\u6cc8", "\u6ccb", "\u6ccd", "\u6cce", "\u6ccf", "\u6cd1", "\u6cd2", "\u6cd8", "\u6cd9", "\u6cda", "\u6cdc", "\u6cdd", "\u6cdf", "\u6ce4", "\u6ce6", "\u6ce7", "\u6ce9", "\u6cec", "\u6ced", "\u6cf2", "\u6cf4", "\u6cf9", "\u6cff", "\u6d00", "\u6d02", "\u6d03", "\u6d05", "\u6d06", "\u6d08", "\u6d09", "\u6d0a", "\u6d0d", "\u6d0f", "\u6d10", "\u6d11", "\u6d13", "\u6d14", "\u6d15", "\u6d16", "\u6d18", "\u6d1c", "\u6d1d", "\u6d1f", "\u6d26", "\u6d28", "\u6d29", "\u6d2c", "\u6d2d", "\u6d2f", "\u6d30", "\u6d34", "\u6d36", "\u6d37", "\u6d38", "\u6d3a", "\u6d3f", "\u6d40", "\u6d42", "\u6d44", "\u6d49", "\u6d4c", "\u6d50", "\u6d55", "\u6d56", "\u6d57", "\u6d58", "\u6d5b", "\u6d5d", "\u6d5f", "\u6d61", "\u6d62", "\u6d64", "\u6d65", "\u6d67", "\u6d68", "\u6d6b", "\u6d6c", "\u6d6d", "\u6d70", "\u6d71", "\u6d72", "\u6d73", "\u6d75", "\u6d76", "\u6d79", "\u6d7a", "\u6d7b", "\u6d7d", "\u6d83", "\u6d84", "\u6d86", "\u6d87", "\u6d8a", "\u6d8b", "\u6d8d", "\u6d8f", "\u6d90", "\u6d92", "\u6d96", "\u6d9c", "\u6da2", "\u6da5", "\u6dac", "\u6dad", "\u6db0", "\u6db1", "\u6db3", "\u6db4", "\u6db6", "\u6db7", "\u6db9", "\u6dc1", "\u6dc2", "\u6dc3", "\u6dc8", "\u6dc9", "\u6dca", "\u6dcd", "\u6dce", "\u6dcf", "\u6dd0", "\u6dd2", "\u6dd3", "\u6dd4", "\u6dd5", "\u6dd7", "\u6dda", "\u6ddb", "\u6ddc", "\u6ddf", "\u6de2", "\u6de3", "\u6de5", "\u6de7", "\u6de8", "\u6de9", "\u6dea", "\u6ded", "\u6def", "\u6df0", "\u6df2", "\u6df4", "\u6df5", "\u6df6", "\u6df8", "\u6dfa", "\u6dfd", "\u6e06", "\u6e07", "\u6e08", "\u6e09", "\u6e0b", "\u6e0f", "\u6e12", "\u6e13", "\u6e15", "\u6e18", "\u6e19", "\u6e1b", "\u6e1c", "\u6e1e", "\u6e1f", "\u6e22", "\u6e26", "\u6e27", "\u6e28", "\u6e2a", "\u6e2e", "\u6e30", "\u6e31", "\u6e33", "\u6e35", "\u6e36", "\u6e37", "\u6e39", "\u6e3b", "\u6e45", "\u6e4f", "\u6e50", "\u6e51", "\u6e52", "\u6e55", "\u6e57", "\u6e59", "\u6e5a", "\u6e5c", "\u6e5d", "\u6e5e", "\u6e60", "\u6e6c", "\u6e6d", "\u6e6f", "\u6e80", "\u6e81", "\u6e82", "\u6e84", "\u6e87", "\u6e88", "\u6e8a", "\u6e91", "\u6e99", "\u6e9a", "\u6e9b", "\u6e9e", "\u6ea0", "\u6ea1", "\u6ea3", "\u6ea4", "\u6ea6", "\u6ea8", "\u6ea9", "\u6eab", "\u6eac", "\u6ead", "\u6eae", "\u6eb0", "\u6eb3", "\u6eb5", "\u6eb8", "\u6eb9", "\u6ebc", "\u6ebe", "\u6ebf", "\u6ec0", "\u6ec3", "\u6ec4", "\u6ec5", "\u6ec6", "\u6ec8", "\u6ec9", "\u6eca", "\u6ecc", "\u6ecd", "\u6ece", "\u6ed0", "\u6ed2", "\u6ed6", "\u6ed8", "\u6ed9", "\u6edb", "\u6edc", "\u6edd", "\u6ee3", "\u6ee7", "\u6eea", "\u6ef0", "\u6ef1", "\u6ef2", "\u6ef3", "\u6ef5", "\u6ef6", "\u6ef7", "\u6ef8", "\u6efa", "\u6f03", "\u6f04", "\u6f05", "\u6f07", "\u6f08", "\u6f0a", "\u6f10", "\u6f11", "\u6f12", "\u6f16", "\u6f21", "\u6f22", "\u6f23", "\u6f25", "\u6f26", "\u6f27", "\u6f28", "\u6f2c", "\u6f2e", "\u6f30", "\u6f32", "\u6f34", "\u6f35", "\u6f37", "\u6f3f", "\u6f40", "\u6f41", "\u6f42", "\u6f43", "\u6f44", "\u6f45", "\u6f48", "\u6f49", "\u6f4a", "\u6f4c", "\u6f4e", "\u6f59", "\u6f5a", "\u6f5b", "\u6f5d", "\u6f5f", "\u6f60", "\u6f61", "\u6f63", "\u6f64", "\u6f65", "\u6f67", "\u6f6f", "\u6f70", "\u6f71", "\u6f73", "\u6f75", "\u6f76", "\u6f77", "\u6f79", "\u6f7b", "\u6f7d", "\u6f85", "\u6f86", "\u6f87", "\u6f8a", "\u6f8b", "\u6f8f", "\u6f9d", "\u6f9e", "\u6f9f", "\u6fa0", "\u6fa2", "\u6fa8", "\u6fb4", "\u6fb5", "\u6fb7", "\u6fb8", "\u6fba", "\u6fc1", "\u6fc3", "\u6fca", "\u6fd3", "\u6fdf", "\u6fe2", "\u6fe3", "\u6fe4", "\u6fe5", "\u6fe6", "\u6ff0", "\u7012", "\u701c", "\u7024", "\u702b", "\u7036", "\u7037", "\u7038", "\u703a", "\u704d", "\u704e", "\u7050", "\u705f", "\u706e", "\u7071", "\u7072", "\u7073", "\u7074", "\u7077", "\u7079", "\u707a", "\u707b", "\u707d", "\u7081", "\u7082", "\u7083", "\u7084", "\u7086", "\u7087", "\u7088", "\u708b", "\u708c", "\u708d", "\u708f", "\u7090", "\u7091", "\u7093", "\u7097", "\u7098", "\u709a", "\u709b", "\u709e", "\u70b0", "\u70b2", "\u70b4", "\u70b5", "\u70b6", "\u70be", "\u70bf", "\u70c4", "\u70c5", "\u70c6", "\u70c7", "\u70c9", "\u70cb", "\u70da", "\u70dc", "\u70dd", "\u70de", "\u70e0", "\u70e1", "\u70e2", "\u70e3", "\u70e5", "\u70ea", "\u70ee", "\u70f0", "\u70f8", "\u70fa", "\u70fb", "\u70fc", "\u70fe", "\u710b", "\u7111", "\u7112", "\u7114", "\u7117", "\u711b", "\u7127", "\u7132", "\u7133", "\u7134", "\u7135", "\u7137", "\u7146", "\u7147", "\u7148", "\u7149", "\u714b", "\u714d", "\u714f", "\u715d", "\u715f", "\u7165", "\u7169", "\u716f", "\u7170", "\u7171", "\u7174", "\u7175", "\u7176", "\u7177", "\u7179", "\u717b", "\u717c", "\u717e", "\u7185", "\u718b", "\u718c", "\u718d", "\u718e", "\u7190", "\u7191", "\u7192", "\u7193", "\u7195", "\u7196", "\u7197", "\u719a", "\u71a1", "\u71a9", "\u71aa", "\u71ab", "\u71ad", "\u71b4", "\u71b6", "\u71b7", "\u71b8", "\u71ba", "\u71c4", "\u71cf", "\u71d6", "\u71e1", "\u71e2", "\u71e3", "\u71e4", "\u71e6", "\u71e8", "\u71ef", "\u71fa", "\u7207", "\u721b", "\u721c", "\u721e", "\u7229", "\u722b", "\u722d", "\u722e", "\u722f", "\u7232", "\u7233", "\u7234", "\u723a", "\u723c", "\u723e", "\u7240", "\u7249", "\u724a", "\u724b", "\u724e", "\u724f", "\u7250", "\u7251", "\u7253", "\u7254", "\u7255", "\u7257", "\u7258", "\u725a", "\u725c", "\u725e", "\u7260", "\u7263", "\u7264", "\u7265", "\u7268", "\u726a", "\u726b", "\u726c", "\u726d", "\u7270", "\u7271", "\u7273", "\u7274", "\u7276", "\u7277", "\u7278", "\u727b", "\u727c", "\u727d", "\u7282", "\u7283", "\u7285", "\u728c", "\u728e", "\u7290", "\u7291", "\u7293", "\u72a0", "\u72ae", "\u72b1", "\u72b2", "\u72b3", "\u72b5", "\u72ba", "\u72c5", "\u72c6", "\u72c7", "\u72c9", "\u72ca", "\u72cb", "\u72cc", "\u72cf", "\u72d1", "\u72d3", "\u72d4", "\u72d5", "\u72d6", "\u72d8", "\u72da", "\u72db", "\u02c9", "\u3003", "\u25ce", "\u203b", "\u3013", "\u2488", "\u2474", "\u2460", "\u3220", "\uff02", "\u02ca", "\u2109", "\u2215", "\u2581", "\u2594", "\u2595", "\u25e2", "\u25e3", "\u25e4", "\u25e5", "\u2609", "\u3012", "\u301d", "\u301e", "\u32a3", "\u338e", "\u338f", "\u339c", "\u339d", "\u339e", "\u33a1", "\u33c4", "\u33ce", "\u33d1", "\u33d2", "\u33d5", "\ufe30", "\u2121", "\u3231", "\u309b", "\u309c", "\u3006", "\ufe49", "\ufe54", "\ufe55", "\ufe56", "\ufe57", "\ufe59", "\ufe62", "\ufe68", "\ufe69", "\ufe6a", "\ufe6b", "\u72dc", "\u72dd", "\u72df", "\u72e2", "\u72ea", "\u72eb", "\u72f5", "\u72f6", "\u72f9", "\u72fd", "\u72fe", "\u72ff", "\u7300", "\u7302", "\u7304", "\u730b", "\u730c", "\u730d", "\u730f", "\u7310", "\u7311", "\u7312", "\u7314", "\u7318", "\u7319", "\u731a", "\u731f", "\u7320", "\u7323", "\u7324", "\u7326", "\u7327", "\u7328", "\u732d", "\u732f", "\u7330", "\u7332", "\u7333", "\u7335", "\u7336", "\u733a", "\u733b", "\u733c", "\u733d", "\u7340", "\u7349", "\u734a", "\u734b", "\u734c", "\u734e", "\u734f", "\u7351", "\u7353", "\u7354", "\u7355", "\u7356", "\u7358", "\u7361", "\u736e", "\u7370", "\u7371", "\u737f", "\u7385", "\u7386", "\u7388", "\u738a", "\u738c", "\u738d", "\u738f", "\u7390", "\u7392", "\u7393", "\u7394", "\u7395", "\u7397", "\u7398", "\u7399", "\u739a", "\u739c", "\u739d", "\u739e", "\u73a0", "\u73a1", "\u73a3", "\u73aa", "\u73ac", "\u73ad", "\u73b1", "\u73b4", "\u73b5", "\u73b6", "\u73b8", "\u73b9", "\u73bc", "\u73bd", "\u73be", "\u73bf", "\u73c1", "\u73c3", "\u73cb", "\u73cc", "\u73ce", "\u73d2", "\u73da", "\u73db", "\u73dc", "\u73dd", "\u73df", "\u73e1", "\u73e2", "\u73e3", "\u73e4", "\u73e6", "\u73e8", "\u73ea", "\u73eb", "\u73ec", "\u73ee", "\u73ef", "\u73f0", "\u73f1", "\u73f3", "\u73f8", "\u7404", "\u7407", "\u7408", "\u740b", "\u740c", "\u740d", "\u740e", "\u7411", "\u741c", "\u7423", "\u7424", "\u7427", "\u7429", "\u742b", "\u742d", "\u742f", "\u7431", "\u7432", "\u7437", "\u743d", "\u743e", "\u743f", "\u7440", "\u7442", "\u744e", "\u7456", "\u7458", "\u745d", "\u7460", "\u746e", "\u746f", "\u7471", "\u7478", "\u7479", "\u747a", "\u747b", "\u747c", "\u747d", "\u747f", "\u7482", "\u7484", "\u7485", "\u7486", "\u7488", "\u7489", "\u748a", "\u748c", "\u748d", "\u748f", "\u7491", "\u749d", "\u749f", "\u74aa", "\u74bb", "\u74c8", "\u74d3", "\u74dd", "\u74df", "\u74e1", "\u74e5", "\u74e7", "\u74f0", "\u74f1", "\u74f2", "\u74f3", "\u74f5", "\u74f8", "\u7500", "\u7501", "\u7502", "\u7503", "\u7505", "\u750e", "\u7510", "\u7512", "\u7514", "\u7515", "\u7516", "\u7517", "\u751b", "\u751d", "\u751e", "\u7520", "\u7526", "\u7527", "\u752a", "\u752e", "\u7534", "\u7536", "\u7539", "\u753c", "\u753d", "\u753f", "\u7541", "\u7542", "\u7543", "\u7544", "\u7546", "\u7547", "\u7549", "\u754a", "\u754d", "\u7550", "\u7551", "\u7552", "\u7553", "\u7555", "\u7556", "\u7557", "\u7558", "\u755d", "\u7567", "\u7568", "\u7569", "\u756b", "\u7573", "\u7575", "\u7577", "\u757a", "\u7580", "\u7581", "\u7582", "\u7584", "\u7585", "\u7587", "\u7588", "\u7589", "\u758a", "\u758c", "\u758d", "\u758e", "\u7590", "\u7593", "\u7595", "\u7598", "\u759b", "\u759c", "\u759e", "\u75a2", "\u75a6", "\u75ad", "\u75b6", "\u75b7", "\u75ba", "\u75bb", "\u75bf", "\u75c0", "\u75c1", "\u75c6", "\u75cb", "\u75cc", "\u75ce", "\u75cf", "\u75d0", "\u75d1", "\u75d3", "\u75d7", "\u75d9", "\u75da", "\u75dc", "\u75dd", "\u75df", "\u75e0", "\u75e1", "\u75e5", "\u75e9", "\u75ec", "\u75ed", "\u75ee", "\u75ef", "\u75f2", "\u75f3", "\u75f5", "\u75f6", "\u75f7", "\u75f8", "\u75fa", "\u75fb", "\u75fd", "\u75fe", "\u7602", "\u7604", "\u7606", "\u7607", "\u7608", "\u7609", "\u760b", "\u760d", "\u760e", "\u760f", "\u7611", "\u7612", "\u7613", "\u7614", "\u7616", "\u761a", "\u761c", "\u761d", "\u761e", "\u7621", "\u7623", "\u7627", "\u7628", "\u762c", "\u762e", "\u762f", "\u7631", "\u7632", "\u7636", "\u7637", "\u7639", "\u763a", "\u763b", "\u763d", "\u7641", "\u7642", "\u7644", "\u7645", "\u764e", "\u7655", "\u7657", "\u765d", "\u765f", "\u7660", "\u7661", "\u7662", "\u7664", "\u766c", "\u766d", "\u766e", "\u7670", "\u7679", "\u767f", "\u7680", "\u7681", "\u7683", "\u7685", "\u7689", "\u768a", "\u768c", "\u768d", "\u768f", "\u7692", "\u7694", "\u7695", "\u7697", "\u7698", "\u769a", "\u769b", "\u769c", "\u76a5", "\u76af", "\u76b0", "\u76b3", "\u76b5", "\u76c0", "\u76c1", "\u76c3", "\u554a", "\u963f", "\u57c3", "\u6328", "\u54ce", "\u5509", "\u54c0", "\u7691", "\u764c", "\u853c", "\u77ee", "\u827e", "\u788d", "\u9698", "\u978d", "\u6c28", "\u4ffa", "\u6697", "\u5cb8", "\u80fa", "\u80ae", "\u6602", "\u76ce", "\u51f9", "\u6556", "\u71ac", "\u7ff1", "\u8884", "\u50b2", "\u5965", "\u61ca", "\u82ad", "\u634c", "\u6252", "\u53ed", "\u5427", "\u7b06", "\u75a4", "\u5df4", "\u62d4", "\u8dcb", "\u9776", "\u8019", "\u575d", "\u9738", "\u7f62", "\u7238", "\u67cf", "\u767e", "\u6446", "\u4f70", "\u62dc", "\u7a17", "\u6591", "\u73ed", "\u642c", "\u6273", "\u822c", "\u9881", "\u626e", "\u62cc", "\u4f34", "\u74e3", "\u529e", "\u7eca", "\u90a6", "\u6886", "\u699c", "\u8180", "\u68d2", "\u78c5", "\u868c", "\u9551", "\u508d", "\u8c24", "\u82de", "\u80de", "\u8912", "\u5265", "\u76c4", "\u76c7", "\u76c9", "\u76cb", "\u76cc", "\u76d3", "\u76d5", "\u76d9", "\u76da", "\u76dc", "\u76dd", "\u76de", "\u76e0", "\u76e6", "\u76f0", "\u76f3", "\u76f5", "\u76f6", "\u76f7", "\u76fa", "\u76fb", "\u76fd", "\u76ff", "\u7700", "\u7702", "\u7703", "\u7705", "\u7706", "\u770a", "\u770c", "\u770e", "\u771b", "\u771c", "\u771d", "\u771e", "\u7721", "\u7723", "\u7724", "\u7725", "\u7727", "\u772a", "\u772b", "\u772c", "\u772e", "\u7730", "\u7739", "\u773b", "\u773d", "\u773e", "\u773f", "\u7742", "\u7744", "\u7745", "\u7746", "\u7748", "\u7752", "\u775c", "\u8584", "\u96f9", "\u5821", "\u9971", "\u5b9d", "\u62b1", "\u62a5", "\u66b4", "\u8c79", "\u9c8d", "\u7206", "\u676f", "\u7891", "\u60b2", "\u5351", "\u5317", "\u8f88", "\u94a1", "\u500d", "\u72c8", "\u60eb", "\u7119", "\u5954", "\u82ef", "\u7b28", "\u5d29", "\u7ef7", "\u752d", "\u6cf5", "\u8e66", "\u8ff8", "\u903c", "\u9f3b", "\u9119", "\u7b14", "\u5f7c", "\u78a7", "\u84d6", "\u853d", "\u6bd5", "\u6bd9", "\u6bd6", "\u5e01", "\u5e87", "\u75f9", "\u655d", "\u5f0a", "\u8f9f", "\u58c1", "\u81c2", "\u907f", "\u965b", "\u97ad", "\u8fb9", "\u8d2c", "\u6241", "\u4fbf", "\u535e", "\u8fa9", "\u8fab", "\u904d", "\u5f6a", "\u8198", "\u9cd6", "\u618b", "\u762a", "\u5f6c", "\u658c", "\u6fd2", "\u6ee8", "\u5bbe", "\u6448", "\u5175", "\u51b0", "\u67c4", "\u4e19", "\u79c9", "\u997c", "\u70b3", "\u775d", "\u775e", "\u775f", "\u7760", "\u7764", "\u7767", "\u7769", "\u776a", "\u776d", "\u777a", "\u777b", "\u777c", "\u7781", "\u7782", "\u7783", "\u7786", "\u778f", "\u7790", "\u7793", "\u77a1", "\u77a3", "\u77a4", "\u77a6", "\u77a8", "\u77ab", "\u77ad", "\u77ae", "\u77af", "\u77b1", "\u77b2", "\u77b4", "\u77b6", "\u77bc", "\u77be", "\u77c0", "\u77ce", "\u77d8", "\u77d9", "\u77da", "\u77dd", "\u77e4", "\u75c5", "\u73bb", "\u83e0", "\u64ad", "\u62e8", "\u94b5", "\u6ce2", "\u52c3", "\u640f", "\u94c2", "\u7b94", "\u4f2f", "\u5e1b", "\u8236", "\u8116", "\u818a", "\u6e24", "\u6cca", "\u9a73", "\u6355", "\u535c", "\u54fa", "\u8865", "\u7c3f", "\u6016", "\u64e6", "\u88c1", "\u6750", "\u624d", "\u8d22", "\u776c", "\u8e29", "\u91c7", "\u5f69", "\u83dc", "\u8521", "\u9910", "\u8695", "\u60ed", "\u60e8", "\u707f", "\u82cd", "\u8231", "\u4ed3", "\u6ca7", "\u7cd9", "\u69fd", "\u66f9", "\u8349", "\u5395", "\u7b56", "\u4fa7", "\u5c42", "\u8e6d", "\u63d2", "\u53c9", "\u832c", "\u8336", "\u78b4", "\u643d", "\u5bdf", "\u5c94", "\u5dee", "\u8be7", "\u62c6", "\u67f4", "\u8c7a", "\u6400", "\u63ba", "\u8749", "\u998b", "\u8c17", "\u7f20", "\u94f2", "\u4ea7", "\u9610", "\u98a4", "\u660c", "\u7316", "\u77e6", "\u77e8", "\u77ea", "\u77ef", "\u77f0", "\u77f1", "\u77f2", "\u77f4", "\u77f5", "\u77f7", "\u77f9", "\u77fa", "\u77fb", "\u77fc", "\u7803", "\u780a", "\u780b", "\u780e", "\u780f", "\u7810", "\u7813", "\u7815", "\u7819", "\u781b", "\u781e", "\u7820", "\u7821", "\u7822", "\u7824", "\u7828", "\u782a", "\u782b", "\u782e", "\u782f", "\u7831", "\u7832", "\u7833", "\u7835", "\u7836", "\u783d", "\u783f", "\u7841", "\u7842", "\u7843", "\u7844", "\u7846", "\u7848", "\u7849", "\u784a", "\u784b", "\u784d", "\u784f", "\u7851", "\u7853", "\u7854", "\u7858", "\u7859", "\u785a", "\u785b", "\u785c", "\u785e", "\u786f", "\u7878", "\u7879", "\u787a", "\u787b", "\u787d", "\u5c1d", "\u507f", "\u80a0", "\u5382", "\u655e", "\u7545", "\u5531", "\u5021", "\u6284", "\u949e", "\u671d", "\u5632", "\u6f6e", "\u5de2", "\u5435", "\u7092", "\u626f", "\u63a3", "\u5f7b", "\u6f88", "\u90f4", "\u81e3", "\u8fb0", "\u5c18", "\u5ff1", "\u6c89", "\u9648", "\u8d81", "\u886c", "\u6491", "\u6a59", "\u5448", "\u4e58", "\u60e9", "\u6f84", "\u8bda", "\u627f", "\u901e", "\u9a8b", "\u79e4", "\u5403", "\u75f4", "\u5319", "\u6c60", "\u8fdf", "\u5f1b", "\u9a70", "\u803b", "\u9f7f", "\u4f88", "\u5c3a", "\u8d64", "\u7fc5", "\u65a5", "\u70bd", "\u866b", "\u5d07", "\u5ba0", "\u916c", "\u7574", "\u8e0c", "\u7a20", "\u6101", "\u7b79", "\u4ec7", "\u7ef8", "\u7785", "\u4e11", "\u81ed", "\u6a71", "\u53a8", "\u8e87", "\u9504", "\u96cf", "\u6ec1", "\u695a", "\u7884", "\u7885", "\u7886", "\u7888", "\u788a", "\u788b", "\u788f", "\u7890", "\u7892", "\u7894", "\u7895", "\u7896", "\u7899", "\u789d", "\u789e", "\u78a0", "\u78a2", "\u78a4", "\u78a6", "\u78a8", "\u78b5", "\u78b6", "\u78b7", "\u78b8", "\u78bb", "\u78bd", "\u78bf", "\u78c0", "\u78c2", "\u78c3", "\u78c4", "\u78c6", "\u78c7", "\u78c8", "\u78cc", "\u78cd", "\u78ce", "\u78cf", "\u78d1", "\u78d2", "\u78d3", "\u78d6", "\u78d7", "\u78d8", "\u78da", "\u78e4", "\u78e5", "\u78e6", "\u78e7", "\u78e9", "\u78ea", "\u78eb", "\u78ed", "\u78f3", "\u78f5", "\u78f6", "\u78f8", "\u78f9", "\u78fb", "\u7902", "\u7903", "\u7904", "\u7906", "\u7840", "\u50a8", "\u77d7", "\u6410", "\u89e6", "\u63e3", "\u5ddd", "\u7a7f", "\u693d", "\u8239", "\u5598", "\u75ae", "\u5e62", "\u5e8a", "\u95ef", "\u5439", "\u708a", "\u6376", "\u9524", "\u5782", "\u6625", "\u693f", "\u9187", "\u5507", "\u6df3", "\u7eaf", "\u8822", "\u6233", "\u7ef0", "\u75b5", "\u8328", "\u78c1", "\u96cc", "\u8f9e", "\u74f7", "\u8bcd", "\u523a", "\u8d50", "\u806a", "\u8471", "\u56f1", "\u5306", "\u4e1b", "\u51d1", "\u7c97", "\u918b", "\u7c07", "\u4fc3", "\u8e7f", "\u7be1", "\u7a9c", "\u6467", "\u5d14", "\u50ac", "\u8106", "\u7601", "\u7cb9", "\u6dec", "\u7fe0", "\u6751", "\u5bf8", "\u78cb", "\u64ae", "\u6413", "\u63aa", "\u632b", "\u642d", "\u7b54", "\u7629", "\u5446", "\u6b79", "\u50a3", "\u6234", "\u5e26", "\u6b86", "\u8d37", "\u888b", "\u902e", "\u790d", "\u7914", "\u791f", "\u7925", "\u7935", "\u793d", "\u793f", "\u7942", "\u7943", "\u7944", "\u7945", "\u7947", "\u794a", "\u7954", "\u7955", "\u7958", "\u7959", "\u7961", "\u7963", "\u7964", "\u7966", "\u7969", "\u796a", "\u796b", "\u796c", "\u796e", "\u7970", "\u7979", "\u797b", "\u7982", "\u7983", "\u7986", "\u7987", "\u7988", "\u7989", "\u798b", "\u798c", "\u798d", "\u798e", "\u7990", "\u7991", "\u7992", "\u6020", "\u803d", "\u62c5", "\u4e39", "\u5355", "\u90f8", "\u63b8", "\u80c6", "\u65e6", "\u6c2e", "\u60ee", "\u8bde", "\u86cb", "\u6321", "\u515a", "\u8361", "\u5200", "\u6363", "\u8e48", "\u5c9b", "\u7977", "\u7a3b", "\u60bc", "\u76d7", "\u5fb7", "\u8e6c", "\u706f", "\u77aa", "\u51f3", "\u9093", "\u5824", "\u6ef4", "\u8fea", "\u654c", "\u7b1b", "\u72c4", "\u6da4", "\u7fdf", "\u5ae1", "\u62b5", "\u5e95", "\u8482", "\u5e1d", "\u5f1f", "\u7f14", "\u6382", "\u6ec7", "\u7898", "\u5178", "\u975b", "\u57ab", "\u7535", "\u4f43", "\u7538", "\u60e6", "\u5960", "\u6dc0", "\u6bbf", "\u7889", "\u53fc", "\u96d5", "\u51cb", "\u5201", "\u6389", "\u540a", "\u9493", "\u8dcc", "\u7239", "\u789f", "\u8776", "\u8fed", "\u8c0d", "\u53e0", "\u7993", "\u799b", "\u79a8", "\u79b4", "\u79bc", "\u79bf", "\u79c2", "\u79c4", "\u79c5", "\u79c7", "\u79c8", "\u79ca", "\u79cc", "\u79ce", "\u79cf", "\u79d0", "\u79d3", "\u79d4", "\u79d6", "\u79d7", "\u79d9", "\u79e0", "\u79e1", "\u79e2", "\u79e5", "\u79e8", "\u79ea", "\u79ec", "\u79ee", "\u79f1", "\u79f9", "\u79fa", "\u79fc", "\u79fe", "\u79ff", "\u7a01", "\u7a04", "\u7a05", "\u7a07", "\u7a08", "\u7a09", "\u7a0a", "\u7a0c", "\u7a0f", "\u7a15", "\u7a16", "\u7a18", "\u7a19", "\u7a1b", "\u7a1c", "\u4e01", "\u76ef", "\u53ee", "\u9489", "\u9f0e", "\u952d", "\u8ba2", "\u4e1c", "\u51ac", "\u8463", "\u680b", "\u4f97", "\u606b", "\u51bb", "\u6d1e", "\u515c", "\u6296", "\u6597", "\u9661", "\u8c46", "\u9017", "\u75d8", "\u7763", "\u6bd2", "\u728a", "\u5835", "\u7779", "\u8d4c", "\u675c", "\u9540", "\u809a", "\u5992", "\u953b", "\u6bb5", "\u7f0e", "\u5806", "\u5151", "\u961f", "\u58a9", "\u5428", "\u8e72", "\u6566", "\u987f", "\u56e4", "\u949d", "\u9041", "\u6387", "\u54c6", "\u593a", "\u579b", "\u8eb2", "\u6735", "\u8dfa", "\u8235", "\u5241", "\u60f0", "\u5815", "\u86fe", "\u5ce8", "\u9e45", "\u4fc4", "\u989d", "\u8bb9", "\u5a25", "\u6076", "\u5384", "\u627c", "\u904f", "\u9102", "\u997f", "\u6069", "\u513f", "\u8033", "\u9975", "\u6d31", "\u7a1d", "\u7a1f", "\u7a21", "\u7a22", "\u7a24", "\u7a34", "\u7a35", "\u7a36", "\u7a38", "\u7a3a", "\u7a3e", "\u7a40", "\u7a47", "\u7a52", "\u7a58", "\u7a71", "\u7a72", "\u7a73", "\u7a75", "\u7a7b", "\u7a7c", "\u7a7d", "\u7a7e", "\u7a82", "\u7a85", "\u7a87", "\u7a89", "\u7a8a", "\u7a8b", "\u7a8c", "\u7a8e", "\u7a8f", "\u7a90", "\u7a93", "\u7a94", "\u7a99", "\u7a9a", "\u7a9b", "\u7a9e", "\u7aa1", "\u7aa2", "\u8d30", "\u7f5a", "\u7b4f", "\u4f10", "\u4e4f", "\u9600", "\u73d0", "\u85e9", "\u5e06", "\u7ffb", "\u6a0a", "\u77fe", "\u9492", "\u7e41", "\u51e1", "\u70e6", "\u8d29", "\u72af", "\u996d", "\u6cdb", "\u574a", "\u82b3", "\u80aa", "\u623f", "\u9632", "\u59a8", "\u4eff", "\u7eba", "\u83f2", "\u5561", "\u80a5", "\u532a", "\u8bfd", "\u5420", "\u80ba", "\u5e9f", "\u6cb8", "\u8d39", "\u82ac", "\u915a", "\u5429", "\u6c1b", "\u7eb7", "\u575f", "\u711a", "\u6c7e", "\u7c89", "\u594b", "\u5fff", "\u6124", "\u7caa", "\u4e30", "\u5c01", "\u67ab", "\u8702", "\u5cf0", "\u950b", "\u98ce", "\u75af", "\u70fd", "\u9022", "\u51af", "\u7f1d", "\u8bbd", "\u5949", "\u51e4", "\u4f5b", "\u592b", "\u6577", "\u80a4", "\u5b75", "\u6276", "\u62c2", "\u8f90", "\u5e45", "\u6c1f", "\u4f0f", "\u4fd8", "\u7aa3", "\u7aa4", "\u7aa7", "\u7aa9", "\u7aaa", "\u7aab", "\u7aae", "\u7ab4", "\u7ac0", "\u7acc", "\u7ad7", "\u7ad8", "\u7ada", "\u7adb", "\u7adc", "\u7add", "\u7ae1", "\u7ae2", "\u7ae4", "\u7ae7", "\u7aee", "\u7af0", "\u7af1", "\u7af2", "\u7af3", "\u7af4", "\u7afb", "\u7afc", "\u7afe", "\u7b00", "\u7b01", "\u7b02", "\u7b05", "\u7b07", "\u7b09", "\u7b0c", "\u7b0d", "\u7b0e", "\u7b10", "\u7b12", "\u7b13", "\u7b16", "\u7b17", "\u7b18", "\u7b1a", "\u7b1c", "\u7b1d", "\u7b1f", "\u7b21", "\u7b22", "\u7b23", "\u7b27", "\u7b29", "\u7b2d", "\u6daa", "\u798f", "\u88b1", "\u5f17", "\u752b", "\u629a", "\u4fef", "\u91dc", "\u65a7", "\u812f", "\u8151", "\u5e9c", "\u8150", "\u8d74", "\u8986", "\u5085", "\u961c", "\u7236", "\u8179", "\u8d1f", "\u5bcc", "\u8ba3", "\u5987", "\u7f1a", "\u5490", "\u5676", "\u560e", "\u6982", "\u9499", "\u76d6", "\u6e89", "\u5e72", "\u6746", "\u67d1", "\u7aff", "\u809d", "\u8d76", "\u611f", "\u79c6", "\u6562", "\u8d63", "\u5188", "\u94a2", "\u7f38", "\u809b", "\u5c97", "\u6760", "\u7bd9", "\u768b", "\u9ad8", "\u818f", "\u7f94", "\u7cd5", "\u641e", "\u9550", "\u7a3f", "\u54e5", "\u6401", "\u6208", "\u9e3d", "\u80f3", "\u7599", "\u5272", "\u9769", "\u845b", "\u86e4", "\u9601", "\u9694", "\u94ec", "\u5404", "\u8015", "\u5e9a", "\u7fb9", "\u7b2f", "\u7b30", "\u7b32", "\u7b34", "\u7b35", "\u7b36", "\u7b37", "\u7b39", "\u7b3b", "\u7b3d", "\u7b3f", "\u7b46", "\u7b48", "\u7b4a", "\u7b4d", "\u7b4e", "\u7b53", "\u7b55", "\u7b57", "\u7b59", "\u7b5c", "\u7b5e", "\u7b5f", "\u7b61", "\u7b63", "\u7b6f", "\u7b70", "\u7b73", "\u7b74", "\u7b76", "\u7b78", "\u7b7a", "\u7b7c", "\u7b7d", "\u7b7f", "\u7b81", "\u7b82", "\u7b83", "\u7b84", "\u7b86", "\u7b8e", "\u7b8f", "\u7b91", "\u7b92", "\u7b93", "\u7b96", "\u7b98", "\u7b99", "\u7b9a", "\u7b9b", "\u7b9e", "\u7b9f", "\u7ba0", "\u7ba3", "\u7ba4", "\u7ba5", "\u7bae", "\u7baf", "\u7bb0", "\u7bb2", "\u7bb3", "\u7bb5", "\u7bb6", "\u7bb7", "\u7bb9", "\u7bc2", "\u7bc3", "\u57c2", "\u803f", "\u6897", "\u653b", "\u606d", "\u9f9a", "\u8eac", "\u5bab", "\u5f13", "\u5de9", "\u6c5e", "\u62f1", "\u8d21", "\u94a9", "\u52fe", "\u6c9f", "\u82df", "\u72d7", "\u57a2", "\u8f9c", "\u83c7", "\u5495", "\u7b8d", "\u4f30", "\u6cbd", "\u5b64", "\u59d1", "\u9f13", "\u86ca", "\u9aa8", "\u80a1", "\u6545", "\u987e", "\u96c7", "\u522e", "\u74dc", "\u5250", "\u5be1", "\u8902", "\u4e56", "\u62d0", "\u602a", "\u68fa", "\u5b98", "\u51a0", "\u89c2", "\u9986", "\u7f50", "\u60ef", "\u704c", "\u8d2f", "\u5149", "\u5e7f", "\u901b", "\u7470", "\u89c4", "\u572d", "\u7845", "\u9f9f", "\u95fa", "\u8f68", "\u9b3c", "\u8be1", "\u7678", "\u6842", "\u67dc", "\u8dea", "\u8d35", "\u523d", "\u8f8a", "\u6eda", "\u68cd", "\u9505", "\u90ed", "\u88f9", "\u54c8", "\u7bc5", "\u7bc8", "\u7bc9", "\u7bca", "\u7bcb", "\u7bcd", "\u7bce", "\u7bcf", "\u7bd0", "\u7bd2", "\u7bd4", "\u7bdb", "\u7bdc", "\u7bde", "\u7bdf", "\u7be0", "\u7be2", "\u7be3", "\u7be4", "\u7be7", "\u7be8", "\u7be9", "\u7beb", "\u7bec", "\u7bed", "\u7bef", "\u7bf0", "\u7bf2", "\u7bf8", "\u7bf9", "\u7bfa", "\u7bfb", "\u7bfd", "\u7bff", "\u7c08", "\u7c09", "\u7c0a", "\u7c0d", "\u7c0e", "\u7c10", "\u7c17", "\u7c18", "\u7c19", "\u7c1a", "\u7c20", "\u7c28", "\u7c29", "\u7c2b", "\u7c39", "\u7c42", "\u9ab8", "\u5b69", "\u6d77", "\u6c26", "\u4ea5", "\u5bb3", "\u9a87", "\u9163", "\u61a8", "\u90af", "\u97e9", "\u6db5", "\u5bd2", "\u558a", "\u7f55", "\u7ff0", "\u64bc", "\u634d", "\u65f1", "\u61be", "\u608d", "\u710a", "\u6c57", "\u592f", "\u676d", "\u822a", "\u58d5", "\u568e", "\u8c6a", "\u6beb", "\u90dd", "\u6d69", "\u5475", "\u559d", "\u8377", "\u83cf", "\u79be", "\u76d2", "\u8c89", "\u9602", "\u6cb3", "\u6db8", "\u8d6b", "\u8910", "\u9e64", "\u8d3a", "\u563f", "\u9ed1", "\u75d5", "\u72e0", "\u6068", "\u54fc", "\u4ea8", "\u6a2a", "\u8861", "\u6052", "\u8f70", "\u54c4", "\u70d8", "\u8679", "\u9e3f", "\u6d2a", "\u5b8f", "\u5f18", "\u7ea2", "\u5589", "\u4faf", "\u7334", "\u543c", "\u539a", "\u4e4e", "\u745a", "\u58f6", "\u846b", "\u80e1", "\u8774", "\u72d0", "\u7cca", "\u6e56", "\u7c43", "\u7c4e", "\u7c75", "\u7c7e", "\u7c88", "\u7c8a", "\u7c93", "\u7c94", "\u7c96", "\u7c99", "\u7c9a", "\u7c9b", "\u7ca0", "\u7ca1", "\u7ca3", "\u7ca6", "\u7ca7", "\u7ca8", "\u7ca9", "\u7cab", "\u7cac", "\u7cad", "\u7caf", "\u7cb0", "\u7cb4", "\u7cba", "\u7cbb", "\u864e", "\u552c", "\u62a4", "\u4e92", "\u6caa", "\u54d7", "\u534e", "\u733e", "\u6ed1", "\u753b", "\u5212", "\u69d0", "\u5f8a", "\u6000", "\u6dee", "\u574f", "\u6853", "\u60a3", "\u5524", "\u75ea", "\u8c62", "\u7115", "\u6da3", "\u5ba6", "\u5e7b", "\u8352", "\u614c", "\u9ec4", "\u78fa", "\u8757", "\u7c27", "\u7687", "\u51f0", "\u60f6", "\u714c", "\u6643", "\u5e4c", "\u604d", "\u8c0e", "\u7070", "\u6325", "\u8f89", "\u5fbd", "\u6062", "\u86d4", "\u6bc1", "\u6094", "\u6167", "\u5349", "\u60e0", "\u6666", "\u8d3f", "\u79fd", "\u4f1a", "\u70e9", "\u6c47", "\u8bb3", "\u8bf2", "\u7ed8", "\u8364", "\u660f", "\u5a5a", "\u9b42", "\u6d51", "\u6df7", "\u8c41", "\u6d3b", "\u4f19", "\u60d1", "\u970d", "\u8d27", "\u7978", "\u51fb", "\u7578", "\u7a3d", "\u79ef", "\u7b95", "\u7cbf", "\u7cc0", "\u7cc2", "\u7cc3", "\u7cc4", "\u7cc6", "\u7cc9", "\u7ccb", "\u7cce", "\u7cd8", "\u7cda", "\u7cdb", "\u7cdd", "\u7cde", "\u7ce1", "\u7ce9", "\u7cf0", "\u7cf9", "\u7cfa", "\u7cfc", "\u7d0b", "\u7d11", "\u7d21", "\u7d23", "\u7d24", "\u7d25", "\u7d26", "\u7d28", "\u7d29", "\u7d2a", "\u7d2c", "\u7d2d", "\u7d2e", "\u7d30", "\u808c", "\u9965", "\u8ff9", "\u6fc0", "\u8ba5", "\u9e21", "\u59ec", "\u7ee9", "\u7f09", "\u5409", "\u6781", "\u68d8", "\u8f91", "\u7c4d", "\u53ca", "\u6025", "\u75be", "\u6c72", "\u5373", "\u5ac9", "\u6324", "\u810a", "\u5df1", "\u84df", "\u6280", "\u5180", "\u5b63", "\u4f0e", "\u796d", "\u5242", "\u60b8", "\u6d4e", "\u5bc4", "\u5bc2", "\u5fcc", "\u9645", "\u5993", "\u7ee7", "\u7eaa", "\u67b7", "\u5bb6", "\u835a", "\u988a", "\u8d3e", "\u7532", "\u94be", "\u7a3c", "\u4ef7", "\u9a7e", "\u5ac1", "\u6b7c", "\u575a", "\u7b3a", "\u714e", "\u517c", "\u80a9", "\u8270", "\u5978", "\u7f04", "\u8327", "\u67ec", "\u78b1", "\u7877", "\u62e3", "\u6361", "\u7b80", "\u4fed", "\u526a", "\u51cf", "\u8350", "\u69db", "\u9274", "\u8df5", "\u8d31", "\u89c1", "\u7bad", "\u7d37", "\u7d6f", "\u7d78", "\u5065", "\u8230", "\u5251", "\u996f", "\u6e10", "\u6e85", "\u6da7", "\u50f5", "\u59dc", "\u6d46", "\u6c5f", "\u7586", "\u848b", "\u6868", "\u5956", "\u8bb2", "\u5320", "\u9171", "\u8549", "\u6912", "\u7901", "\u7126", "\u80f6", "\u90ca", "\u6d47", "\u9a84", "\u5a07", "\u56bc", "\u6405", "\u94f0", "\u77eb", "\u4fa5", "\u811a", "\u72e1", "\u997a", "\u7f34", "\u7ede", "\u527f", "\u6559", "\u9175", "\u8f7f", "\u8f83", "\u7a96", "\u63ed", "\u7686", "\u79f8", "\u8857", "\u9636", "\u52ab", "\u6854", "\u6770", "\u6377", "\u776b", "\u7aed", "\u6d01", "\u59d0", "\u6212", "\u85c9", "\u82a5", "\u501f", "\u75a5", "\u8beb", "\u5c4a", "\u5dfe", "\u7b4b", "\u65a4", "\u6d25", "\u895f", "\u9526", "\u8c28", "\u9773", "\u664b", "\u7981", "\u8fd1", "\u70ec", "\u6d78", "\u7d99", "\u7da7", "\u7daf", "\u52b2", "\u8346", "\u5162", "\u830e", "\u775b", "\u6676", "\u9cb8", "\u4eac", "\u60ca", "\u7cb3", "\u4e95", "\u8b66", "\u9888", "\u9759", "\u656c", "\u955c", "\u75c9", "\u9756", "\u7adf", "\u7ade", "\u51c0", "\u70af", "\u7a98", "\u63ea", "\u7a76", "\u7ea0", "\u7396", "\u97ed", "\u4e45", "\u7078", "\u53a9", "\u6551", "\u81fc", "\u8205", "\u548e", "\u759a", "\u97a0", "\u62d8", "\u72d9", "\u75bd", "\u5c45", "\u9a79", "\u83ca", "\u5c40", "\u5480", "\u77e9", "\u6cae", "\u805a", "\u62d2", "\u8ddd", "\u8e1e", "\u952f", "\u4ff1", "\u60e7", "\u70ac", "\u6350", "\u9e43", "\u5a1f", "\u5026", "\u7737", "\u7ee2", "\u6485", "\u652b", "\u6289", "\u6398", "\u5014", "\u7235", "\u89c9", "\u8bc0", "\u5747", "\u83cc", "\u94a7", "\u519b", "\u541b", "\u5cfb", "\u7dfb", "\u7e3a", "\u7e3c", "\u7e42", "\u7e48", "\u4fca", "\u7ae3", "\u6d5a", "\u90e1", "\u9a8f", "\u5580", "\u5496", "\u5361", "\u54af", "\u63e9", "\u6977", "\u51ef", "\u6168", "\u520a", "\u582a", "\u52d8", "\u574e", "\u780d", "\u770b", "\u5eb7", "\u6177", "\u7ce0", "\u625b", "\u6297", "\u4ea2", "\u7095", "\u8003", "\u70e4", "\u9760", "\u5777", "\u82db", "\u67ef", "\u68f5", "\u78d5", "\u9897", "\u58f3", "\u54b3", "\u6e34", "\u514b", "\u5ba2", "\u8bfe", "\u80af", "\u5543", "\u57a6", "\u6073", "\u5751", "\u542d", "\u6050", "\u5b54", "\u62a0", "\u6263", "\u5bc7", "\u67af", "\u54ed", "\u7a9f", "\u82e6", "\u9177", "\u88e4", "\u5938", "\u57ae", "\u630e", "\u8de8", "\u80ef", "\u5757", "\u7b77", "\u4fa9", "\u5bbd", "\u6b3e", "\u5321", "\u7b50", "\u72c2", "\u77ff", "\u7736", "\u65f7", "\u51b5", "\u4e8f", "\u76d4", "\u5cbf", "\u7aa5", "\u8475", "\u594e", "\u9b41", "\u5080", "\u7e5e", "\u7e83", "\u7e9c", "\u7e9d", "\u7e9e", "\u7eae", "\u7eb4", "\u7ebb", "\u7ebc", "\u7ed6", "\u7ee4", "\u7eec", "\u7ef9", "\u7f0a", "\u7f10", "\u7f1e", "\u7f37", "\u7f39", "\u7f3b", "\u7f43", "\u7f46", "\u7f52", "\u7f53", "\u9988", "\u6127", "\u6e83", "\u5764", "\u6606", "\u6346", "\u56f0", "\u5ed3", "\u9614", "\u5587", "\u8721", "\u814a", "\u8fa3", "\u5566", "\u83b1", "\u8d56", "\u84dd", "\u5a6a", "\u680f", "\u62e6", "\u7bee", "\u9611", "\u5170", "\u6f9c", "\u8c30", "\u63fd", "\u89c8", "\u61d2", "\u7f06", "\u70c2", "\u6ee5", "\u7405", "\u6994", "\u72fc", "\u5eca", "\u90ce", "\u6717", "\u6d6a", "\u635e", "\u52b3", "\u7262", "\u8001", "\u4f6c", "\u59e5", "\u916a", "\u70d9", "\u6d9d", "\u52d2", "\u4e50", "\u96f7", "\u956d", "\u857e", "\u78ca", "\u7d2f", "\u5121", "\u5792", "\u64c2", "\u808b", "\u6cea", "\u68f1", "\u695e", "\u51b7", "\u5398", "\u68a8", "\u7281", "\u9ece", "\u7bf1", "\u72f8", "\u79bb", "\u6f13", "\u674e", "\u9ca4", "\u793c", "\u8389", "\u8354", "\u540f", "\u6817", "\u4e3d", "\u5389", "\u52b1", "\u783e", "\u5386", "\u5088", "\u4fd0", "\u7f56", "\u7f59", "\u7f5b", "\u7f5c", "\u7f5d", "\u7f5e", "\u7f60", "\u7f63", "\u7f6b", "\u7f6c", "\u7f6d", "\u7f6f", "\u7f70", "\u7f73", "\u7f75", "\u7f76", "\u7f77", "\u7f78", "\u7f7a", "\u7f7b", "\u7f7c", "\u7f7d", "\u7f7f", "\u7f80", "\u7f82", "\u7f8b", "\u7f8d", "\u7f8f", "\u7f95", "\u7f9b", "\u7f9c", "\u7fa0", "\u7fa2", "\u7fa5", "\u7fa6", "\u7fa8", "\u7fb1", "\u7fb3", "\u7fba", "\u7fbb", "\u7fbe", "\u7fc0", "\u7fc2", "\u7fc3", "\u7fc4", "\u7fc6", "\u7fc7", "\u7fc8", "\u7fc9", "\u7fcb", "\u7fcd", "\u7fcf", "\u7fd6", "\u7fd7", "\u7fd9", "\u7fe2", "\u7fe3", "\u75e2", "\u7c92", "\u6ca5", "\u96b6", "\u7483", "\u54e9", "\u4fe9", "\u83b2", "\u9570", "\u5ec9", "\u601c", "\u6d9f", "\u5e18", "\u655b", "\u8138", "\u604b", "\u70bc", "\u7ec3", "\u7cae", "\u51c9", "\u6881", "\u7cb1", "\u8f86", "\u667e", "\u4eae", "\u8c05", "\u64a9", "\u804a", "\u50da", "\u7597", "\u71ce", "\u5be5", "\u8fbd", "\u6f66", "\u6482", "\u9563", "\u5ed6", "\u88c2", "\u70c8", "\u52a3", "\u730e", "\u7433", "\u6797", "\u78f7", "\u9716", "\u90bb", "\u9cde", "\u6dcb", "\u51db", "\u8d41", "\u541d", "\u62ce", "\u73b2", "\u83f1", "\u9f84", "\u94c3", "\u4f36", "\u7f9a", "\u7075", "\u9675", "\u5cad", "\u9886", "\u53e6", "\u6e9c", "\u7409", "\u69b4", "\u786b", "\u998f", "\u5218", "\u7624", "\u67f3", "\u9f99", "\u804b", "\u5499", "\u7b3c", "\u7abf", "\u7fe4", "\u7fe7", "\u7fe8", "\u7fea", "\u7feb", "\u7fec", "\u7fed", "\u7fef", "\u7ff2", "\u7ff4", "\u7ffd", "\u7ffe", "\u7fff", "\u8002", "\u8007", "\u8008", "\u8009", "\u800a", "\u800e", "\u800f", "\u8011", "\u8013", "\u801a", "\u801b", "\u801d", "\u801e", "\u801f", "\u8021", "\u8023", "\u8024", "\u802b", "\u8032", "\u8034", "\u8039", "\u803a", "\u803c", "\u803e", "\u8040", "\u8041", "\u8044", "\u8045", "\u8047", "\u8048", "\u8049", "\u804e", "\u804f", "\u8050", "\u8051", "\u8053", "\u8055", "\u8056", "\u8057", "\u8059", "\u805b", "\u806b", "\u8072", "\u9686", "\u5784", "\u62e2", "\u9647", "\u697c", "\u5a04", "\u6402", "\u7bd3", "\u6f0f", "\u964b", "\u82a6", "\u5362", "\u9885", "\u5e90", "\u7089", "\u63b3", "\u5364", "\u864f", "\u9c81", "\u9e93", "\u788c", "\u8d42", "\u9e7f", "\u6f5e", "\u7984", "\u9646", "\u622e", "\u9a74", "\u5415", "\u94dd", "\u4fa3", "\u65c5", "\u5c65", "\u5c61", "\u7f15", "\u8651", "\u6c2f", "\u5f8b", "\u7387", "\u6ee4", "\u7eff", "\u5ce6", "\u631b", "\u5b6a", "\u6ee6", "\u5375", "\u4e71", "\u63a0", "\u62a1", "\u4f26", "\u4ed1", "\u6ca6", "\u7eb6", "\u8bba", "\u841d", "\u87ba", "\u7f57", "\u903b", "\u9523", "\u7ba9", "\u9aa1", "\u88f8", "\u843d", "\u6d1b", "\u9a86", "\u5988", "\u9ebb", "\u739b", "\u8682", "\u9a82", "\u561b", "\u5417", "\u57cb", "\u4e70", "\u9ea6", "\u5356", "\u8fc8", "\u8109", "\u7792", "\u9992", "\u86ee", "\u6ee1", "\u8513", "\u66fc", "\u6162", "\u6f2b", "\u807e", "\u8081", "\u8082", "\u8085", "\u8088", "\u808a", "\u808d", "\u8094", "\u8095", "\u8097", "\u8099", "\u809e", "\u80a3", "\u80a6", "\u80a7", "\u80a8", "\u80ac", "\u80b0", "\u80b3", "\u80b5", "\u80b6", "\u80b8", "\u80b9", "\u80bb", "\u80c5", "\u80c7", "\u80cf", "\u80d8", "\u80df", "\u80e0", "\u80e2", "\u80e3", "\u80e6", "\u80ee", "\u80f5", "\u80f7", "\u80f9", "\u80fb", "\u80fe", "\u80ff", "\u8100", "\u8101", "\u8103", "\u8104", "\u8105", "\u8107", "\u8108", "\u810b", "\u810c", "\u8115", "\u8117", "\u8119", "\u811b", "\u811c", "\u811d", "\u811f", "\u812d", "\u812e", "\u8130", "\u8133", "\u8134", "\u8135", "\u8137", "\u8139", "\u813f", "\u8c29", "\u8292", "\u832b", "\u76f2", "\u6c13", "\u5fd9", "\u83bd", "\u732b", "\u8305", "\u951a", "\u6bdb", "\u94c6", "\u8302", "\u5192", "\u5e3d", "\u8c8c", "\u8d38", "\u73ab", "\u6885", "\u9176", "\u9709", "\u7164", "\u7709", "\u9541", "\u7f8e", "\u6627", "\u5bd0", "\u59b9", "\u5a9a", "\u95f7", "\u4eec", "\u840c", "\u8499", "\u6aac", "\u76df", "\u9530", "\u731b", "\u68a6", "\u5b5f", "\u772f", "\u919a", "\u9761", "\u7cdc", "\u8ff7", "\u8c1c", "\u7c73", "\u79d8", "\u89c5", "\u6ccc", "\u871c", "\u5bc6", "\u5e42", "\u68c9", "\u7720", "\u7ef5", "\u5195", "\u514d", "\u52c9", "\u5a29", "\u7f05", "\u82d7", "\u7784", "\u85d0", "\u6e3a", "\u5e99", "\u5999", "\u8511", "\u706d", "\u6c11", "\u62bf", "\u76bf", "\u654f", "\u60af", "\u95fd", "\u879f", "\u9e23", "\u94ed", "\u8c2c", "\u6478", "\u8140", "\u8147", "\u8149", "\u814d", "\u814e", "\u814f", "\u8152", "\u8156", "\u8157", "\u8158", "\u815b", "\u8161", "\u8162", "\u8163", "\u8164", "\u8166", "\u8168", "\u816a", "\u816b", "\u816c", "\u816f", "\u8172", "\u8173", "\u8175", "\u8176", "\u8177", "\u8178", "\u8181", "\u8183", "\u8189", "\u818b", "\u818c", "\u818d", "\u818e", "\u8190", "\u8192", "\u8199", "\u819a", "\u819e", "\u81a4", "\u81a5", "\u81a7", "\u81a9", "\u81ab", "\u81b4", "\u81bc", "\u81bd", "\u81be", "\u81bf", "\u81c4", "\u81c5", "\u81c7", "\u81c8", "\u81c9", "\u81cb", "\u81cd", "\u6479", "\u8611", "\u819c", "\u78e8", "\u6469", "\u9b54", "\u62b9", "\u83ab", "\u58a8", "\u6cab", "\u6f20", "\u5bde", "\u964c", "\u8c0b", "\u725f", "\u67d0", "\u62c7", "\u7261", "\u4ea9", "\u59c6", "\u6bcd", "\u5893", "\u66ae", "\u5e55", "\u52df", "\u6155", "\u7267", "\u7a46", "\u62ff", "\u54ea", "\u5450", "\u94a0", "\u5a1c", "\u7eb3", "\u6c16", "\u4e43", "\u5976", "\u8010", "\u5948", "\u5357", "\u7537", "\u96be", "\u56ca", "\u6320", "\u8111", "\u607c", "\u95f9", "\u6dd6", "\u5462", "\u9981", "\u5ae9", "\u59ae", "\u9713", "\u502a", "\u6ce5", "\u5c3c", "\u62df", "\u533f", "\u817b", "\u6eba", "\u852b", "\u62c8", "\u78be", "\u64b5", "\u637b", "\u5ff5", "\u5a18", "\u917f", "\u9e1f", "\u5c3f", "\u634f", "\u8042", "\u5b7d", "\u556e", "\u954a", "\u954d", "\u6d85", "\u67e0", "\u72de", "\u51dd", "\u5b81", "\u81d4", "\u81e4", "\u81e5", "\u81e6", "\u81e8", "\u81e9", "\u81eb", "\u81ee", "\u81f5", "\u81fd", "\u81ff", "\u8203", "\u8207", "\u820e", "\u820f", "\u8211", "\u8213", "\u8215", "\u821d", "\u8220", "\u8224", "\u8225", "\u8226", "\u8227", "\u8229", "\u822e", "\u8232", "\u823a", "\u823c", "\u823d", "\u823f", "\u8240", "\u8241", "\u8242", "\u8243", "\u8245", "\u8246", "\u8248", "\u824a", "\u824c", "\u824d", "\u824e", "\u8250", "\u8259", "\u825b", "\u825c", "\u825d", "\u825e", "\u8260", "\u8269", "\u62e7", "\u6cde", "\u725b", "\u626d", "\u94ae", "\u7ebd", "\u8113", "\u6d53", "\u519c", "\u5f04", "\u5974", "\u52aa", "\u6012", "\u5973", "\u6696", "\u8650", "\u759f", "\u632a", "\u61e6", "\u7cef", "\u54e6", "\u6b27", "\u9e25", "\u6bb4", "\u85d5", "\u5455", "\u5076", "\u6ca4", "\u556a", "\u8db4", "\u722c", "\u5e15", "\u6015", "\u7436", "\u62cd", "\u724c", "\u5f98", "\u6e43", "\u6d3e", "\u6500", "\u6f58", "\u76d8", "\u78d0", "\u76fc", "\u7554", "\u53db", "\u4e53", "\u5e9e", "\u65c1", "\u802a", "\u80d6", "\u629b", "\u5486", "\u5228", "\u70ae", "\u888d", "\u8dd1", "\u6ce1", "\u5478", "\u80da", "\u57f9", "\u88f4", "\u8d54", "\u966a", "\u4f69", "\u6c9b", "\u55b7", "\u76c6", "\u7830", "\u62a8", "\u70f9", "\u6f8e", "\u5f6d", "\u84ec", "\u68da", "\u787c", "\u7bf7", "\u81a8", "\u670b", "\u9e4f", "\u6367", "\u78b0", "\u576f", "\u7812", "\u9739", "\u6279", "\u62ab", "\u5288", "\u7435", "\u6bd7", "\u826a", "\u826b", "\u826c", "\u826d", "\u8271", "\u8275", "\u8276", "\u8277", "\u8278", "\u827b", "\u827c", "\u8280", "\u8281", "\u8283", "\u8285", "\u8286", "\u8287", "\u8289", "\u828c", "\u8290", "\u8293", "\u8294", "\u8295", "\u8296", "\u829a", "\u829b", "\u829e", "\u82a0", "\u82a2", "\u82a3", "\u82a7", "\u82b2", "\u82b5", "\u82b6", "\u82ba", "\u82bb", "\u82bc", "\u82bf", "\u82c0", "\u82c2", "\u82c3", "\u82c5", "\u82c6", "\u82c9", "\u82d0", "\u82d6", "\u82d9", "\u82da", "\u82dd", "\u82e2", "\u82e7", "\u82e8", "\u82e9", "\u82ea", "\u82ec", "\u82ed", "\u82ee", "\u82f0", "\u82f2", "\u82f3", "\u82f5", "\u82f6", "\u82f8", "\u82fa", "\u82fc", "\u830a", "\u830b", "\u830d", "\u8310", "\u8312", "\u8313", "\u8316", "\u8318", "\u8319", "\u831d", "\u8329", "\u832a", "\u832e", "\u8330", "\u8332", "\u8337", "\u833b", "\u833d", "\u5564", "\u813e", "\u75b2", "\u76ae", "\u75de", "\u50fb", "\u5c41", "\u8b6c", "\u7bc7", "\u504f", "\u7247", "\u9a97", "\u98d8", "\u6f02", "\u74e2", "\u7968", "\u6487", "\u77a5", "\u62fc", "\u9891", "\u8d2b", "\u54c1", "\u8058", "\u4e52", "\u576a", "\u82f9", "\u840d", "\u5e73", "\u51ed", "\u74f6", "\u8bc4", "\u5c4f", "\u6cfc", "\u9887", "\u5a46", "\u7834", "\u9b44", "\u8feb", "\u7c95", "\u5256", "\u6251", "\u94fa", "\u4ec6", "\u8386", "\u8461", "\u83e9", "\u84b2", "\u57d4", "\u6734", "\u5703", "\u8c31", "\u66dd", "\u7011", "\u6b3a", "\u6816", "\u621a", "\u59bb", "\u51c4", "\u6f06", "\u67d2", "\u6c8f", "\u68cb", "\u5947", "\u6b67", "\u7566", "\u5d0e", "\u8110", "\u9f50", "\u7948", "\u7941", "\u9a91", "\u5c82", "\u4e5e", "\u4f01", "\u5951", "\u780c", "\u8fc4", "\u5f03", "\u6ce3", "\u8bab", "\u6390", "\u833e", "\u833f", "\u8341", "\u8342", "\u8344", "\u8345", "\u8348", "\u834a", "\u8353", "\u8355", "\u835d", "\u8362", "\u8370", "\u8379", "\u837a", "\u837e", "\u8387", "\u8388", "\u838a", "\u838b", "\u838c", "\u838d", "\u838f", "\u8390", "\u8391", "\u8394", "\u8395", "\u8396", "\u8397", "\u8399", "\u839a", "\u839d", "\u839f", "\u83a1", "\u83ac", "\u83ad", "\u83ae", "\u83af", "\u83b5", "\u83bb", "\u83be", "\u83bf", "\u83c2", "\u83c3", "\u83c4", "\u83c6", "\u83c8", "\u83c9", "\u83cb", "\u83cd", "\u83ce", "\u83d0", "\u83d1", "\u83d2", "\u83d3", "\u83d5", "\u83d7", "\u83d9", "\u83da", "\u83db", "\u83de", "\u83e2", "\u83e3", "\u83e4", "\u83e6", "\u83e7", "\u83e8", "\u83eb", "\u83ec", "\u83ed", "\u6070", "\u6d3d", "\u7275", "\u6266", "\u948e", "\u94c5", "\u5343", "\u8fc1", "\u4edf", "\u8c26", "\u4e7e", "\u9ed4", "\u94b1", "\u94b3", "\u6f5c", "\u9063", "\u6d45", "\u8c34", "\u5811", "\u5d4c", "\u6b20", "\u6b49", "\u67aa", "\u545b", "\u8154", "\u7f8c", "\u5899", "\u8537", "\u5f3a", "\u62a2", "\u6a47", "\u9539", "\u6572", "\u6084", "\u6865", "\u77a7", "\u4e54", "\u4fa8", "\u5de7", "\u9798", "\u64ac", "\u7fd8", "\u5ced", "\u4fcf", "\u7a8d", "\u8304", "\u602f", "\u7a83", "\u94a6", "\u4fb5", "\u4eb2", "\u79e6", "\u7434", "\u52e4", "\u82b9", "\u64d2", "\u79bd", "\u5bdd", "\u6c81", "\u9752", "\u8f7b", "\u6c22", "\u503e", "\u537f", "\u64ce", "\u6674", "\u6c30", "\u9877", "\u5e86", "\u743c", "\u7a77", "\u79cb", "\u4e18", "\u90b1", "\u7403", "\u56da", "\u914b", "\u6cc5", "\u8d8b", "\u86c6", "\u66f2", "\u8eaf", "\u5c48", "\u6e20", "\u83ee", "\u83ef", "\u83f3", "\u83fa", "\u83fb", "\u83fc", "\u83fe", "\u83ff", "\u8400", "\u8402", "\u8405", "\u8407", "\u8408", "\u8409", "\u840a", "\u8410", "\u8412", "\u8419", "\u841a", "\u841b", "\u841e", "\u8429", "\u8432", "\u8439", "\u843a", "\u843b", "\u843e", "\u8447", "\u8448", "\u844a", "\u8452", "\u8458", "\u845d", "\u845e", "\u845f", "\u8460", "\u8462", "\u8464", "\u846a", "\u846e", "\u846f", "\u8470", "\u8472", "\u8474", "\u8477", "\u8479", "\u847b", "\u847c", "\u5a36", "\u9f8b", "\u8da3", "\u53bb", "\u98a7", "\u919b", "\u6cc9", "\u75ca", "\u62f3", "\u72ac", "\u5238", "\u529d", "\u7094", "\u7638", "\u9e4a", "\u69b7", "\u96c0", "\u88d9", "\u71c3", "\u5189", "\u67d3", "\u74e4", "\u58e4", "\u6518", "\u56b7", "\u8ba9", "\u9976", "\u6270", "\u7ed5", "\u60f9", "\u70ed", "\u58ec", "\u4ec1", "\u5fcd", "\u97e7", "\u5203", "\u598a", "\u7eab", "\u6254", "\u620e", "\u8338", "\u84c9", "\u8363", "\u878d", "\u7194", "\u6eb6", "\u7ed2", "\u5197", "\u63c9", "\u67d4", "\u8089", "\u8339", "\u8815", "\u5112", "\u5b7a", "\u8fb1", "\u4e73", "\u6c5d", "\u8925", "\u8f6f", "\u962e", "\u854a", "\u745e", "\u9510", "\u6da6", "\u82e5", "\u5f31", "\u6492", "\u6d12", "\u8428", "\u816e", "\u9cc3", "\u585e", "\u8d5b", "\u53c1", "\u847d", "\u8483", "\u8484", "\u8485", "\u8486", "\u848a", "\u848d", "\u848f", "\u8498", "\u849a", "\u849b", "\u849d", "\u849e", "\u849f", "\u84a0", "\u84a2", "\u84b0", "\u84b1", "\u84b3", "\u84b5", "\u84b6", "\u84b7", "\u84bb", "\u84bc", "\u84be", "\u84c0", "\u84c2", "\u84c3", "\u84c5", "\u84c6", "\u84c7", "\u84c8", "\u84cb", "\u84cc", "\u84ce", "\u84cf", "\u84d2", "\u84d4", "\u84d5", "\u84d7", "\u84d8", "\u84de", "\u84e1", "\u84e2", "\u84e4", "\u84e7", "\u84ed", "\u84ee", "\u84ef", "\u84f1", "\u84fd", "\u84fe", "\u8500", "\u8501", "\u8502", "\u4f1e", "\u6563", "\u6851", "\u55d3", "\u4e27", "\u6414", "\u9a9a", "\u626b", "\u5ac2", "\u745f", "\u8272", "\u6da9", "\u68ee", "\u50e7", "\u838e", "\u7802", "\u6740", "\u5239", "\u6c99", "\u7eb1", "\u50bb", "\u5565", "\u715e", "\u7b5b", "\u6652", "\u73ca", "\u82eb", "\u6749", "\u5c71", "\u717d", "\u886b", "\u95ea", "\u9655", "\u64c5", "\u8d61", "\u81b3", "\u6c55", "\u6247", "\u7f2e", "\u5892", "\u4f24", "\u8d4f", "\u664c", "\u88f3", "\u68a2", "\u634e", "\u70e7", "\u828d", "\u52fa", "\u97f6", "\u54e8", "\u90b5", "\u7ecd", "\u5962", "\u8d4a", "\u86c7", "\u820c", "\u820d", "\u8d66", "\u6444", "\u6151", "\u6d89", "\u793e", "\u7837", "\u7533", "\u547b", "\u8eab", "\u6df1", "\u5a20", "\u7ec5", "\u6c88", "\u5ba1", "\u5a76", "\u751a", "\u80be", "\u614e", "\u6e17", "\u58f0", "\u7525", "\u7272", "\u5347", "\u7ef3", "\u8503", "\u850d", "\u850e", "\u850f", "\u8510", "\u8512", "\u8514", "\u8515", "\u8516", "\u8518", "\u8519", "\u851b", "\u851c", "\u851d", "\u851e", "\u8520", "\u8522", "\u852d", "\u853e", "\u8544", "\u8545", "\u8546", "\u8547", "\u854b", "\u8557", "\u8558", "\u855a", "\u855b", "\u855c", "\u855d", "\u855f", "\u8565", "\u8566", "\u8567", "\u8569", "\u8573", "\u8575", "\u8576", "\u8577", "\u8578", "\u857c", "\u857d", "\u857f", "\u8580", "\u8581", "\u76db", "\u5269", "\u80dc", "\u5723", "\u5e08", "\u72ee", "\u65bd", "\u6e7f", "\u8bd7", "\u5c38", "\u8671", "\u77f3", "\u62fe", "\u4ec0", "\u98df", "\u8680", "\u53f2", "\u77e2", "\u5c4e", "\u9a76", "\u58eb", "\u67ff", "\u4e8b", "\u62ed", "\u8a93", "\u901d", "\u52bf", "\u55dc", "\u566c", "\u9002", "\u4ed5", "\u4f8d", "\u9970", "\u6c0f", "\u5e02", "\u6043", "\u5ba4", "\u8bd5", "\u9996", "\u5b88", "\u5bff", "\u552e", "\u7626", "\u517d", "\u852c", "\u67a2", "\u68b3", "\u6292", "\u53d4", "\u8212", "\u6dd1", "\u758f", "\u8d4e", "\u5b70", "\u719f", "\u85af", "\u6691", "\u66d9", "\u7f72", "\u8700", "\u9ecd", "\u9f20", "\u672f", "\u6811", "\u620d", "\u7ad6", "\u5885", "\u5eb6", "\u6f31", "\u8582", "\u8583", "\u8586", "\u8588", "\u8590", "\u859d", "\u85a5", "\u85a6", "\u85a7", "\u85a9", "\u85ab", "\u85ac", "\u85ad", "\u85b1", "\u85b8", "\u85ba", "\u85c2", "\u85ca", "\u85d1", "\u85d2", "\u85d4", "\u85d6", "\u85dd", "\u85e5", "\u85e6", "\u85e7", "\u85e8", "\u85ea", "\u6055", "\u5237", "\u800d", "\u6454", "\u8870", "\u7529", "\u5e05", "\u6813", "\u62f4", "\u723d", "\u8c01", "\u7761", "\u7a0e", "\u542e", "\u77ac", "\u987a", "\u821c", "\u8bf4", "\u7855", "\u6714", "\u70c1", "\u65af", "\u6495", "\u5636", "\u601d", "\u4e1d", "\u6b7b", "\u8086", "\u5bfa", "\u55e3", "\u4f3c", "\u9972", "\u5df3", "\u677e", "\u8038", "\u6002", "\u9882", "\u5b8b", "\u8bbc", "\u8bf5", "\u8258", "\u64de", "\u55fd", "\u82cf", "\u9165", "\u4fd7", "\u901f", "\u7c9f", "\u50f3", "\u5851", "\u5bbf", "\u8bc9", "\u8083", "\u9178", "\u849c", "\u7b97", "\u867d", "\u968b", "\u968f", "\u7ee5", "\u9ad3", "\u788e", "\u5c81", "\u7a57", "\u9042", "\u96a7", "\u795f", "\u5b59", "\u635f", "\u7b0b", "\u84d1", "\u68ad", "\u5506", "\u7410", "\u9501", "\u584c", "\u5979", "\u5854", "\u85f9", "\u85fa", "\u85fc", "\u85fd", "\u85fe", "\u8600", "\u8606", "\u8612", "\u8613", "\u8614", "\u8615", "\u8617", "\u8628", "\u862a", "\u8639", "\u863a", "\u863b", "\u863d", "\u863e", "\u863f", "\u8640", "\u8641", "\u8652", "\u8653", "\u865b", "\u865c", "\u865d", "\u8660", "\u8661", "\u8663", "\u736d", "\u631e", "\u8e4b", "\u8e0f", "\u80ce", "\u82d4", "\u62ac", "\u6cf0", "\u915e", "\u6c70", "\u574d", "\u644a", "\u8d2a", "\u762b", "\u6ee9", "\u575b", "\u6a80", "\u75f0", "\u6f6d", "\u8c2d", "\u8c08", "\u5766", "\u6bef", "\u8892", "\u78b3", "\u53f9", "\u70ad", "\u6c64", "\u5858", "\u642a", "\u5802", "\u68e0", "\u819b", "\u5510", "\u7cd6", "\u5018", "\u8eba", "\u6dcc", "\u8d9f", "\u70eb", "\u638f", "\u6d9b", "\u6ed4", "\u7ee6", "\u8404", "\u6843", "\u9003", "\u6dd8", "\u9676", "\u8ba8", "\u85e4", "\u817e", "\u75bc", "\u8a8a", "\u68af", "\u5254", "\u8e22", "\u9511", "\u9898", "\u8e44", "\u557c", "\u568f", "\u60d5", "\u6d95", "\u5243", "\u5c49", "\u6dfb", "\u7530", "\u751c", "\u606c", "\u8214", "\u8146", "\u6311", "\u8fe2", "\u773a", "\u8d34", "\u94c1", "\u5e16", "\u5385", "\u70c3", "\u866d", "\u866f", "\u8670", "\u8672", "\u8683", "\u868e", "\u8694", "\u8696", "\u869e", "\u86a5", "\u86a6", "\u86ab", "\u86ad", "\u86ae", "\u86b2", "\u86b3", "\u86b7", "\u86b8", "\u86b9", "\u86bb", "\u86c1", "\u86c2", "\u86c3", "\u86c5", "\u86c8", "\u86cc", "\u86cd", "\u86d2", "\u86d3", "\u86d5", "\u86d6", "\u86d7", "\u86da", "\u86dc", "\u86dd", "\u86e0", "\u86e1", "\u86e2", "\u86e3", "\u86e5", "\u86e6", "\u86e7", "\u86e8", "\u86ea", "\u86eb", "\u86ec", "\u86ef", "\u86f5", "\u86f6", "\u86f7", "\u86fa", "\u86fb", "\u86fc", "\u86fd", "\u86ff", "\u8701", "\u8704", "\u8705", "\u8706", "\u870b", "\u870c", "\u870e", "\u870f", "\u8710", "\u8711", "\u8714", "\u8716", "\u6c40", "\u5ef7", "\u4ead", "\u5ead", "\u633a", "\u8247", "\u6850", "\u916e", "\u77b3", "\u94dc", "\u5f64", "\u7ae5", "\u6876", "\u6345", "\u75db", "\u5077", "\u6295", "\u51f8", "\u79c3", "\u5f92", "\u6d82", "\u5c60", "\u5410", "\u5154", "\u6e4d", "\u9893", "\u817f", "\u8715", "\u892a", "\u541e", "\u5c6f", "\u81c0", "\u62d6", "\u6258", "\u8131", "\u9e35", "\u9640", "\u9a6e", "\u9a7c", "\u692d", "\u62d3", "\u553e", "\u6316", "\u54c7", "\u86d9", "\u6d3c", "\u5a03", "\u74e6", "\u889c", "\u6b6a", "\u8c4c", "\u5f2f", "\u73a9", "\u987d", "\u4e38", "\u70f7", "\u7897", "\u633d", "\u7696", "\u60cb", "\u5b9b", "\u5a49", "\u4e07", "\u8155", "\u6c6a", "\u738b", "\u4ea1", "\u6789", "\u5f80", "\u65fa", "\u5fd8", "\u5984", "\u5a01", "\u8719", "\u871b", "\u871d", "\u871f", "\u8720", "\u8724", "\u8726", "\u8727", "\u8728", "\u872a", "\u872b", "\u872c", "\u872d", "\u872f", "\u8730", "\u8732", "\u8733", "\u8735", "\u8736", "\u8738", "\u8739", "\u873a", "\u873c", "\u873d", "\u8740", "\u874a", "\u874b", "\u874d", "\u874f", "\u8750", "\u8751", "\u8752", "\u8754", "\u8755", "\u8756", "\u8758", "\u875a", "\u8761", "\u8762", "\u8766", "\u876f", "\u8771", "\u8772", "\u8773", "\u8775", "\u8777", "\u8778", "\u8779", "\u877a", "\u877f", "\u8780", "\u8781", "\u8784", "\u8786", "\u8787", "\u8789", "\u878a", "\u878c", "\u878e", "\u8794", "\u8795", "\u8796", "\u8798", "\u87a0", "\u5dcd", "\u5371", "\u97e6", "\u8fdd", "\u6845", "\u552f", "\u60df", "\u6f4d", "\u7ef4", "\u82c7", "\u840e", "\u59d4", "\u4f1f", "\u4f2a", "\u7eac", "\u851a", "\u5473", "\u754f", "\u80c3", "\u5582", "\u9b4f", "\u6e2d", "\u8c13", "\u5c09", "\u6170", "\u536b", "\u761f", "\u6e29", "\u868a", "\u95fb", "\u7eb9", "\u543b", "\u7a33", "\u7d0a", "\u55e1", "\u7fc1", "\u74ee", "\u631d", "\u8717", "\u6da1", "\u7a9d", "\u65a1", "\u5367", "\u63e1", "\u6c83", "\u5deb", "\u545c", "\u94a8", "\u4e4c", "\u6c61", "\u8bec", "\u5c4b", "\u829c", "\u68a7", "\u543e", "\u5434", "\u6bcb", "\u6b66", "\u6342", "\u821e", "\u4f0d", "\u4fae", "\u575e", "\u620a", "\u96fe", "\u6664", "\u52ff", "\u609f", "\u6614", "\u7199", "\u7852", "\u77fd", "\u6670", "\u563b", "\u5438", "\u727a", "\u87a5", "\u87a6", "\u87a7", "\u87a9", "\u87aa", "\u87ae", "\u87b0", "\u87b1", "\u87b2", "\u87b4", "\u87b6", "\u87b7", "\u87b8", "\u87b9", "\u87bb", "\u87bc", "\u87be", "\u87bf", "\u87c1", "\u87c7", "\u87c8", "\u87c9", "\u87cc", "\u87d4", "\u87dc", "\u87dd", "\u87de", "\u87df", "\u87e1", "\u87e2", "\u87e3", "\u87e4", "\u87e6", "\u87e7", "\u87e8", "\u87e9", "\u87eb", "\u87ec", "\u87ed", "\u87ef", "\u87fa", "\u87fb", "\u87fc", "\u87fd", "\u87ff", "\u8800", "\u8801", "\u8802", "\u8804", "\u880b", "\u8814", "\u8817", "\u8818", "\u8819", "\u881a", "\u881c", "\u8823", "\u7a00", "\u5e0c", "\u6089", "\u819d", "\u5915", "\u60dc", "\u7184", "\u70ef", "\u6eaa", "\u6c50", "\u7280", "\u6a84", "\u88ad", "\u5e2d", "\u4e60", "\u5ab3", "\u94e3", "\u6d17", "\u9699", "\u620f", "\u7ec6", "\u778e", "\u867e", "\u5323", "\u971e", "\u8f96", "\u6687", "\u5ce1", "\u4fa0", "\u72ed", "\u53a6", "\u590f", "\u5413", "\u6380", "\u9528", "\u4ed9", "\u9c9c", "\u7ea4", "\u54b8", "\u8d24", "\u8854", "\u8237", "\u95f2", "\u6d8e", "\u5f26", "\u5acc", "\u9669", "\u732e", "\u53bf", "\u817a", "\u9985", "\u7fa1", "\u5baa", "\u9677", "\u53a2", "\u9576", "\u8944", "\u6e58", "\u4e61", "\u7fd4", "\u7965", "\u8be6", "\u54cd", "\u4eab", "\u5df7", "\u6a61", "\u8427", "\u785d", "\u9704", "\u54ee", "\u56a3", "\u5bb5", "\u6dc6", "\u6653", "\u8824", "\u8833", "\u883a", "\u883b", "\u883d", "\u883e", "\u883f", "\u8841", "\u8842", "\u8843", "\u8846", "\u884e", "\u8855", "\u8856", "\u8858", "\u885a", "\u8866", "\u8867", "\u886a", "\u886d", "\u886f", "\u8871", "\u8873", "\u8874", "\u8875", "\u8876", "\u8878", "\u8879", "\u887a", "\u887b", "\u887c", "\u8880", "\u8883", "\u8886", "\u8887", "\u8889", "\u888a", "\u888c", "\u888e", "\u888f", "\u8890", "\u8891", "\u8893", "\u8894", "\u8895", "\u8897", "\u889d", "\u88a3", "\u88a5", "\u5b5d", "\u6821", "\u8096", "\u5578", "\u7b11", "\u6954", "\u4e9b", "\u6b47", "\u874e", "\u978b", "\u631f", "\u90aa", "\u659c", "\u80c1", "\u8c10", "\u68b0", "\u87f9", "\u61c8", "\u6cc4", "\u6cfb", "\u8c22", "\u5c51", "\u85aa", "\u82af", "\u950c", "\u6b23", "\u8f9b", "\u5ffb", "\u5fc3", "\u8845", "\u8165", "\u7329", "\u60fa", "\u5174", "\u5211", "\u90a2", "\u9192", "\u5e78", "\u674f", "\u59d3", "\u5144", "\u51f6", "\u80f8", "\u5308", "\u6c79", "\u96c4", "\u718a", "\u4f11", "\u7f9e", "\u673d", "\u55c5", "\u9508", "\u79c0", "\u8896", "\u7ee3", "\u589f", "\u620c", "\u865a", "\u5618", "\u5f90", "\u84c4", "\u9157", "\u53d9", "\u65ed", "\u755c", "\u6064", "\u7d6e", "\u5a7f", "\u7eea", "\u7eed", "\u8f69", "\u55a7", "\u5ba3", "\u60ac", "\u65cb", "\u7384", "\u88ac", "\u88ae", "\u88af", "\u88b0", "\u88b2", "\u88b8", "\u88b9", "\u88ba", "\u88bb", "\u88bd", "\u88be", "\u88bf", "\u88c0", "\u88c3", "\u88c4", "\u88c7", "\u88c8", "\u88ca", "\u88cb", "\u88cc", "\u88cd", "\u88d0", "\u88d1", "\u88d3", "\u88d6", "\u88d7", "\u88da", "\u88e0", "\u88e6", "\u88e7", "\u88e9", "\u88f2", "\u88f5", "\u88f6", "\u88f7", "\u88fa", "\u88fb", "\u88ff", "\u8900", "\u8901", "\u8903", "\u8909", "\u890b", "\u8911", "\u8914", "\u891c", "\u8922", "\u8923", "\u8924", "\u8926", "\u8927", "\u8928", "\u8929", "\u892c", "\u892d", "\u892e", "\u892f", "\u8931", "\u8932", "\u8933", "\u8935", "\u8937", "\u7663", "\u7729", "\u7eda", "\u9774", "\u859b", "\u5b66", "\u7a74", "\u96ea", "\u8840", "\u52cb", "\u718f", "\u65ec", "\u5bfb", "\u9a6f", "\u5de1", "\u6b89", "\u6c5b", "\u8bad", "\u900a", "\u8fc5", "\u538b", "\u62bc", "\u9e26", "\u9e2d", "\u5440", "\u4e2b", "\u82bd", "\u7259", "\u869c", "\u5d16", "\u8859", "\u6daf", "\u96c5", "\u54d1", "\u8bb6", "\u7109", "\u54bd", "\u9609", "\u70df", "\u6df9", "\u76d0", "\u4e25", "\u7814", "\u8712", "\u5ca9", "\u989c", "\u960e", "\u708e", "\u6cbf", "\u5944", "\u63a9", "\u773c", "\u6f14", "\u8273", "\u5830", "\u71d5", "\u538c", "\u781a", "\u96c1", "\u5501", "\u5f66", "\u7130", "\u5bb4", "\u8c1a", "\u9a8c", "\u6b83", "\u592e", "\u9e2f", "\u79e7", "\u6768", "\u626c", "\u4f6f", "\u75a1", "\u7f8a", "\u6d0b", "\u9633", "\u6c27", "\u4ef0", "\u75d2", "\u517b", "\u6837", "\u6f3e", "\u9080", "\u8170", "\u5996", "\u7476", "\u8938", "\u8942", "\u8943", "\u8945", "\u8960", "\u8967", "\u897c", "\u897d", "\u897e", "\u8980", "\u8982", "\u8984", "\u8985", "\u8987", "\u6447", "\u5c27", "\u9065", "\u7a91", "\u8c23", "\u59da", "\u54ac", "\u8200", "\u836f", "\u8000", "\u6930", "\u564e", "\u8036", "\u7237", "\u91ce", "\u51b6", "\u9875", "\u6396", "\u4e1a", "\u53f6", "\u66f3", "\u814b", "\u591c", "\u6db2", "\u58f9", "\u533b", "\u63d6", "\u94f1", "\u4f9d", "\u4f0a", "\u8863", "\u9890", "\u5937", "\u9057", "\u4eea", "\u80f0", "\u7591", "\u6c82", "\u5b9c", "\u59e8", "\u5f5d", "\u6905", "\u8681", "\u501a", "\u4e59", "\u77e3", "\u827a", "\u6291", "\u6613", "\u9091", "\u5c79", "\u4ebf", "\u5f79", "\u81c6", "\u9038", "\u8084", "\u75ab", "\u4ea6", "\u88d4", "\u6bc5", "\u5fc6", "\u8be3", "\u8c0a", "\u7ffc", "\u7fcc", "\u7ece", "\u8335", "\u836b", "\u6bb7", "\u97f3", "\u9634", "\u59fb", "\u541f", "\u94f6", "\u6deb", "\u5bc5", "\u996e", "\u5c39", "\u89a2", "\u89c3", "\u89cd", "\u89d3", "\u89d4", "\u89d5", "\u89d7", "\u89d8", "\u89d9", "\u89db", "\u89dd", "\u89df", "\u89e0", "\u89e1", "\u89e2", "\u89e4", "\u89e7", "\u89e8", "\u89e9", "\u89ea", "\u89ec", "\u89ed", "\u89ee", "\u89f0", "\u89f1", "\u89f2", "\u89f4", "\u89fb", "\u8a01", "\u5370", "\u82f1", "\u6a31", "\u5a74", "\u9e70", "\u7f28", "\u83b9", "\u8424", "\u8425", "\u8367", "\u8747", "\u8fce", "\u8d62", "\u5f71", "\u9896", "\u786c", "\u54df", "\u62e5", "\u4f63", "\u81c3", "\u75c8", "\u5eb8", "\u96cd", "\u8e0a", "\u86f9", "\u548f", "\u6cf3", "\u6d8c", "\u6c38", "\u607f", "\u52c7", "\u5e7d", "\u60a0", "\u5fe7", "\u5c24", "\u90ae", "\u94c0", "\u72b9", "\u6cb9", "\u6e38", "\u9149", "\u53cb", "\u4f51", "\u91c9", "\u8bf1", "\u5e7c", "\u8fc2", "\u6de4", "\u76c2", "\u6986", "\u865e", "\u611a", "\u8206", "\u4f59", "\u4fde", "\u903e", "\u9c7c", "\u6109", "\u6e1d", "\u6e14", "\u9685", "\u4e88", "\u5a31", "\u96e8", "\u5c7f", "\u79b9", "\u5b87", "\u7fbd", "\u7389", "\u828b", "\u90c1", "\u5401", "\u55bb", "\u5cea", "\u5fa1", "\u6108", "\u6b32", "\u72f1", "\u80b2", "\u8a89", "\u8a1e", "\u8a3f", "\u8a49", "\u8a5f", "\u8a7a", "\u6d74", "\u5bd3", "\u88d5", "\u8c6b", "\u9a6d", "\u9e33", "\u6e0a", "\u51a4", "\u57a3", "\u8881", "\u8f95", "\u56ed", "\u5458", "\u5706", "\u733f", "\u7f18", "\u82d1", "\u613f", "\u6028", "\u9662", "\u66f0", "\u7ea6", "\u8d8a", "\u8dc3", "\u94a5", "\u5cb3", "\u7ca4", "\u60a6", "\u9605", "\u8018", "\u4e91", "\u90e7", "\u5300", "\u9668", "\u8fd0", "\u8574", "\u915d", "\u6655", "\u97f5", "\u5b55", "\u531d", "\u7838", "\u6742", "\u683d", "\u54c9", "\u707e", "\u5bb0", "\u54b1", "\u6512", "\u8d5e", "\u8d43", "\u810f", "\u846c", "\u906d", "\u7cdf", "\u51ff", "\u85fb", "\u67a3", "\u6fa1", "\u86a4", "\u8e81", "\u566a", "\u9020", "\u7682", "\u7076", "\u71e5", "\u8d23", "\u62e9", "\u6cfd", "\u8d3c", "\u600e", "\u618e", "\u66fe", "\u8d60", "\u624e", "\u55b3", "\u6e23", "\u672d", "\u8f67", "\u8a81", "\u8a8b", "\u8a94", "\u8ac3", "\u94e1", "\u95f8", "\u7728", "\u6805", "\u69a8", "\u548b", "\u4e4d", "\u70b8", "\u8bc8", "\u658b", "\u5b85", "\u7a84", "\u503a", "\u5be8", "\u77bb", "\u6be1", "\u8a79", "\u7c98", "\u6cbe", "\u76cf", "\u65a9", "\u8f97", "\u5d2d", "\u8638", "\u6808", "\u5360", "\u6218", "\u6e5b", "\u7efd", "\u6a1f", "\u7ae0", "\u5f70", "\u6f33", "\u5f20", "\u638c", "\u6da8", "\u6756", "\u4e08", "\u5e10", "\u8d26", "\u4ed7", "\u80c0", "\u7634", "\u969c", "\u62db", "\u662d", "\u6cbc", "\u8d75", "\u7f69", "\u5146", "\u8087", "\u53ec", "\u906e", "\u6298", "\u54f2", "\u86f0", "\u8f99", "\u9517", "\u8517", "\u6d59", "\u73cd", "\u659f", "\u771f", "\u7504", "\u7827", "\u81fb", "\u8d1e", "\u9488", "\u4fa6", "\u6795", "\u75b9", "\u8bca", "\u9707", "\u632f", "\u9547", "\u9635", "\u84b8", "\u6323", "\u7741", "\u5f81", "\u72f0", "\u4e89", "\u6014", "\u62ef", "\u653f", "\u8ae4", "\u8b08", "\u8b24", "\u8b25", "\u8b27", "\u5e27", "\u75c7", "\u90d1", "\u8bc1", "\u829d", "\u679d", "\u5431", "\u8718", "\u80a2", "\u8102", "\u6c41", "\u7ec7", "\u804c", "\u690d", "\u6b96", "\u4f84", "\u8dbe", "\u65e8", "\u7eb8", "\u631a", "\u63b7", "\u5e1c", "\u5cd9", "\u667a", "\u79e9", "\u7a1a", "\u8d28", "\u7099", "\u75d4", "\u6ede", "\u6cbb", "\u7a92", "\u76c5", "\u5fe0", "\u8877", "\u79cd", "\u80bf", "\u4ef2", "\u821f", "\u5dde", "\u6d32", "\u8bcc", "\u7ca5", "\u8f74", "\u8098", "\u5e1a", "\u5492", "\u76b1", "\u5b99", "\u663c", "\u9aa4", "\u73e0", "\u682a", "\u86db", "\u6731", "\u732a", "\u8bf8", "\u8bdb", "\u9010", "\u7af9", "\u70db", "\u716e", "\u62c4", "\u77a9", "\u5631", "\u67f1", "\u86c0", "\u8d2e", "\u94f8", "\u7b51", "\u8b46", "\u8b67", "\u8b6d", "\u8b87", "\u8bac", "\u8bb1", "\u8bbb", "\u8bc7", "\u8bd0", "\u8bea", "\u8c09", "\u8c1e", "\u4f4f", "\u795d", "\u9a7b", "\u6293", "\u722a", "\u62fd", "\u4e13", "\u7816", "\u64b0", "\u8d5a", "\u7bc6", "\u6869", "\u5e84", "\u5986", "\u649e", "\u58ee", "\u690e", "\u9525", "\u8d58", "\u5760", "\u7f00", "\u8c06", "\u51c6", "\u6349", "\u62d9", "\u5353", "\u7422", "\u8301", "\u914c", "\u5544", "\u707c", "\u6d4a", "\u5179", "\u54a8", "\u8d44", "\u59ff", "\u6ecb", "\u6dc4", "\u5b5c", "\u7d2b", "\u4ed4", "\u7c7d", "\u6ed3", "\u6e0d", "\u9b03", "\u68d5", "\u8e2a", "\u5b97", "\u7efc", "\u603b", "\u7eb5", "\u90b9", "\u594f", "\u63cd", "\u79df", "\u5352", "\u65cf", "\u7956", "\u8bc5", "\u963b", "\u94bb", "\u7e82", "\u5634", "\u9189", "\u7f6a", "\u5c0a", "\u9075", "\u5de6", "\u4f50", "\u67de", "\u5750", "\u5ea7", "\u8c38", "\u8c42", "\u8c43", "\u8c44", "\u8c45", "\u8c48", "\u8c4a", "\u8c4b", "\u8c4d", "\u8c56", "\u8c57", "\u8c58", "\u8c59", "\u8c5b", "\u8c63", "\u8c6c", "\u8c74", "\u8c75", "\u8c76", "\u8c77", "\u8c7b", "\u8c83", "\u8c84", "\u8c86", "\u8c87", "\u8c88", "\u8c8b", "\u8c8d", "\u8c95", "\u8c96", "\u8c97", "\u8c99", "\u4e8d", "\u4e0c", "\u5140", "\u4e10", "\u5eff", "\u5345", "\u4e15", "\u4e98", "\u4e1e", "\u9b32", "\u5b6c", "\u5669", "\u4e28", "\u79ba", "\u4e3f", "\u5315", "\u4e47", "\u592d", "\u723b", "\u536e", "\u6c10", "\u56df", "\u80e4", "\u9997", "\u6bd3", "\u777e", "\u9f17", "\u4e36", "\u4e9f", "\u9f10", "\u4e5c", "\u4e69", "\u4e93", "\u8288", "\u5b5b", "\u556c", "\u560f", "\u4ec4", "\u538d", "\u539d", "\u53a3", "\u53a5", "\u53ae", "\u9765", "\u8d5d", "\u531a", "\u53f5", "\u5326", "\u532e", "\u533e", "\u8d5c", "\u5363", "\u5202", "\u5208", "\u520e", "\u522d", "\u5233", "\u523f", "\u5240", "\u524c", "\u525e", "\u5261", "\u525c", "\u84af", "\u527d", "\u5282", "\u5281", "\u5290", "\u5293", "\u5182", "\u7f54", "\u4ebb", "\u4ec3", "\u4ec9", "\u4ec2", "\u4ee8", "\u4ee1", "\u4eeb", "\u4ede", "\u4f1b", "\u4ef3", "\u4f22", "\u4f64", "\u4ef5", "\u4f25", "\u4f27", "\u4f09", "\u4f2b", "\u4f5e", "\u4f67", "\u6538", "\u4f5a", "\u4f5d", "\u8cae", "\u8ced", "\u4f5f", "\u4f57", "\u4f32", "\u4f3d", "\u4f76", "\u4f74", "\u4f91", "\u4f89", "\u4f83", "\u4f8f", "\u4f7e", "\u4f7b", "\u4faa", "\u4f7c", "\u4fac", "\u4f94", "\u4fe6", "\u4fe8", "\u4fea", "\u4fc5", "\u4fda", "\u4fe3", "\u4fdc", "\u4fd1", "\u4fdf", "\u4ff8", "\u5029", "\u504c", "\u4ff3", "\u502c", "\u500f", "\u502e", "\u502d", "\u4ffe", "\u501c", "\u500c", "\u5025", "\u5028", "\u507e", "\u5043", "\u5055", "\u5048", "\u504e", "\u506c", "\u507b", "\u50a5", "\u50a7", "\u50a9", "\u50ba", "\u50d6", "\u5106", "\u50ed", "\u50ec", "\u50e6", "\u50ee", "\u5107", "\u510b", "\u4edd", "\u6c3d", "\u4f58", "\u4f65", "\u4fce", "\u9fa0", "\u6c46", "\u7c74", "\u516e", "\u5dfd", "\u9ec9", "\u9998", "\u5181", "\u5914", "\u52f9", "\u530d", "\u8a07", "\u5310", "\u51eb", "\u5919", "\u5155", "\u4ea0", "\u5156", "\u4eb3", "\u886e", "\u88a4", "\u4eb5", "\u8114", "\u88d2", "\u7980", "\u5b34", "\u8803", "\u7fb8", "\u51ab", "\u51b1", "\u51bd", "\u51bc", "\u8d0e", "\u8d20", "\u8d51", "\u8d52", "\u8d57", "\u8d5f", "\u8d65", "\u8d68", "\u8d69", "\u8d6a", "\u8d6c", "\u8d6e", "\u8d6f", "\u8d71", "\u8d72", "\u8d78", "\u8d82", "\u8d83", "\u8d86", "\u8d87", "\u8d88", "\u8d89", "\u8d8c", "\u8d92", "\u8d93", "\u8d95", "\u8da0", "\u8da1", "\u8da2", "\u8da4", "\u8db2", "\u8db6", "\u8db7", "\u8db9", "\u8dbb", "\u8dbd", "\u8dc0", "\u8dc1", "\u8dc2", "\u8dc5", "\u8dc7", "\u8dc8", "\u8dc9", "\u8dca", "\u8dcd", "\u8dd0", "\u8dd2", "\u8dd3", "\u8dd4", "\u51c7", "\u5196", "\u51a2", "\u51a5", "\u8ba0", "\u8ba6", "\u8ba7", "\u8baa", "\u8bb4", "\u8bb5", "\u8bb7", "\u8bc2", "\u8bc3", "\u8bcb", "\u8bcf", "\u8bce", "\u8bd2", "\u8bd3", "\u8bd4", "\u8bd6", "\u8bd8", "\u8bd9", "\u8bdc", "\u8bdf", "\u8be0", "\u8be4", "\u8be8", "\u8be9", "\u8bee", "\u8bf0", "\u8bf3", "\u8bf6", "\u8bf9", "\u8bfc", "\u8bff", "\u8c00", "\u8c02", "\u8c04", "\u8c07", "\u8c0c", "\u8c0f", "\u8c11", "\u8c12", "\u8c14", "\u8c15", "\u8c16", "\u8c19", "\u8c1b", "\u8c18", "\u8c1d", "\u8c1f", "\u8c20", "\u8c21", "\u8c25", "\u8c27", "\u8c2a", "\u8c2b", "\u8c2e", "\u8c2f", "\u8c32", "\u8c33", "\u8c35", "\u8c36", "\u5369", "\u537a", "\u961d", "\u9622", "\u9621", "\u9631", "\u962a", "\u963d", "\u963c", "\u9642", "\u9649", "\u9654", "\u965f", "\u9667", "\u966c", "\u9672", "\u9674", "\u9688", "\u968d", "\u9697", "\u96b0", "\u9097", "\u909b", "\u909d", "\u9099", "\u90ac", "\u90a1", "\u90b4", "\u90b3", "\u90b6", "\u90ba", "\u8dd5", "\u8dd8", "\u8dd9", "\u8ddc", "\u8de0", "\u8de1", "\u8de2", "\u8de5", "\u8de6", "\u8de7", "\u8de9", "\u8ded", "\u8dee", "\u8df0", "\u8df1", "\u8df2", "\u8df4", "\u8df6", "\u8dfc", "\u8dfe", "\u8e06", "\u8e07", "\u8e08", "\u8e0b", "\u8e0d", "\u8e0e", "\u8e10", "\u8e11", "\u8e12", "\u8e13", "\u8e15", "\u8e20", "\u8e21", "\u8e24", "\u8e2b", "\u8e2d", "\u8e30", "\u8e32", "\u8e33", "\u8e34", "\u8e36", "\u8e37", "\u8e38", "\u8e3b", "\u8e3c", "\u8e3e", "\u8e3f", "\u8e43", "\u8e45", "\u8e46", "\u8e4c", "\u8e53", "\u8e5a", "\u8e67", "\u8e68", "\u8e6a", "\u8e6b", "\u8e6e", "\u8e71", "\u90b8", "\u90b0", "\u90cf", "\u90c5", "\u90be", "\u90d0", "\u90c4", "\u90c7", "\u90d3", "\u90e6", "\u90e2", "\u90dc", "\u90d7", "\u90db", "\u90eb", "\u90ef", "\u90fe", "\u9104", "\u9122", "\u911e", "\u9123", "\u9131", "\u912f", "\u9139", "\u9143", "\u9146", "\u520d", "\u5942", "\u52a2", "\u52ac", "\u52ad", "\u52be", "\u54ff", "\u52d0", "\u52d6", "\u52f0", "\u53df", "\u71ee", "\u77cd", "\u5ef4", "\u51f5", "\u51fc", "\u9b2f", "\u53b6", "\u5f01", "\u755a", "\u5def", "\u574c", "\u57a9", "\u57a1", "\u587e", "\u58bc", "\u58c5", "\u58d1", "\u5729", "\u572c", "\u572a", "\u5733", "\u5739", "\u572e", "\u572f", "\u575c", "\u573b", "\u5742", "\u5769", "\u5785", "\u576b", "\u5786", "\u577c", "\u577b", "\u5768", "\u576d", "\u5776", "\u5773", "\u57ad", "\u57a4", "\u578c", "\u57b2", "\u57cf", "\u57a7", "\u57b4", "\u5793", "\u57a0", "\u57d5", "\u57d8", "\u57da", "\u57d9", "\u57d2", "\u57b8", "\u57f4", "\u57ef", "\u57f8", "\u57e4", "\u57dd", "\u8e73", "\u8e75", "\u8e77", "\u8e7d", "\u8e7e", "\u8e80", "\u8e82", "\u8e83", "\u8e84", "\u8e86", "\u8e88", "\u8e91", "\u8e92", "\u8e93", "\u8e95", "\u8e9d", "\u8e9f", "\u8ead", "\u8eae", "\u8eb0", "\u8eb1", "\u8eb3", "\u8ebb", "\u8ec3", "\u8ecf", "\u580b", "\u580d", "\u57fd", "\u57ed", "\u5800", "\u581e", "\u5819", "\u5844", "\u5820", "\u5865", "\u586c", "\u5881", "\u5889", "\u589a", "\u5880", "\u99a8", "\u9f19", "\u61ff", "\u8279", "\u827d", "\u827f", "\u828f", "\u828a", "\u82a8", "\u8284", "\u828e", "\u8291", "\u8297", "\u8299", "\u82ab", "\u82b8", "\u82be", "\u82b0", "\u82c8", "\u82ca", "\u82e3", "\u8298", "\u82b7", "\u82ae", "\u82cb", "\u82cc", "\u82c1", "\u82a9", "\u82b4", "\u82a1", "\u82aa", "\u829f", "\u82c4", "\u82ce", "\u82a4", "\u82e1", "\u8309", "\u82f7", "\u82e4", "\u830f", "\u8307", "\u82dc", "\u82f4", "\u82d2", "\u82d8", "\u830c", "\u82fb", "\u82d3", "\u8311", "\u831a", "\u8306", "\u8314", "\u8315", "\u82e0", "\u82d5", "\u831c", "\u8351", "\u835b", "\u835c", "\u8308", "\u8392", "\u833c", "\u8334", "\u8331", "\u839b", "\u835e", "\u832f", "\u834f", "\u8347", "\u8343", "\u835f", "\u8340", "\u8317", "\u8360", "\u832d", "\u833a", "\u8333", "\u8366", "\u8365", "\u8ee5", "\u8f24", "\u8368", "\u831b", "\u8369", "\u836c", "\u836a", "\u836d", "\u836e", "\u83b0", "\u8378", "\u83b3", "\u83b4", "\u83a0", "\u83aa", "\u8393", "\u839c", "\u8385", "\u837c", "\u83b6", "\u83a9", "\u837d", "\u83b8", "\u837b", "\u8398", "\u839e", "\u83a8", "\u83ba", "\u83bc", "\u83c1", "\u8401", "\u83e5", "\u83d8", "\u5807", "\u8418", "\u840b", "\u83dd", "\u83fd", "\u83d6", "\u841c", "\u8438", "\u8411", "\u8406", "\u83d4", "\u83df", "\u840f", "\u8403", "\u83f8", "\u83f9", "\u83ea", "\u83c5", "\u83c0", "\u8426", "\u83f0", "\u83e1", "\u845c", "\u8451", "\u845a", "\u8459", "\u8473", "\u8487", "\u8488", "\u847a", "\u8489", "\u8478", "\u843c", "\u8446", "\u8469", "\u8476", "\u848c", "\u848e", "\u8431", "\u846d", "\u84c1", "\u84cd", "\u84d0", "\u84e6", "\u84bd", "\u84d3", "\u84ca", "\u84bf", "\u84ba", "\u84e0", "\u84a1", "\u84b9", "\u84b4", "\u8497", "\u84e5", "\u84e3", "\u850c", "\u750d", "\u8538", "\u84f0", "\u8539", "\u851f", "\u853a", "\u8f45", "\u8f6a", "\u8f80", "\u8f8c", "\u8f92", "\u8f9d", "\u8fa0", "\u8fa1", "\u8fa2", "\u8fa4", "\u8fa5", "\u8fa6", "\u8fa7", "\u8faa", "\u8fac", "\u8fad", "\u8fae", "\u8faf", "\u8fb2", "\u8fb3", "\u8fb4", "\u8fb5", "\u8fb7", "\u8fb8", "\u8fba", "\u8fbb", "\u8fbf", "\u8fc0", "\u8fc3", "\u8fc6", "\u8fc9", "\u8fcf", "\u8fd2", "\u8fd6", "\u8fd7", "\u8fda", "\u8fe0", "\u8fe1", "\u8fe3", "\u8fe7", "\u8fec", "\u8fef", "\u8ff1", "\u8ff2", "\u8ff4", "\u8ff5", "\u8ff6", "\u8ffa", "\u8ffb", "\u8ffc", "\u8ffe", "\u8fff", "\u9007", "\u9008", "\u900c", "\u900e", "\u9013", "\u9015", "\u9018", "\u8556", "\u853b", "\u84ff", "\u84fc", "\u8559", "\u8548", "\u8568", "\u8564", "\u855e", "\u857a", "\u77a2", "\u8543", "\u8572", "\u857b", "\u85a4", "\u85a8", "\u8587", "\u858f", "\u8579", "\u85ae", "\u859c", "\u8585", "\u85b9", "\u85b7", "\u85b0", "\u85d3", "\u85c1", "\u85dc", "\u85ff", "\u8627", "\u8605", "\u8629", "\u8616", "\u863c", "\u5efe", "\u5f08", "\u593c", "\u5941", "\u8037", "\u5955", "\u595a", "\u5958", "\u530f", "\u5c22", "\u5c25", "\u5c2c", "\u5c34", "\u624c", "\u626a", "\u629f", "\u62bb", "\u62ca", "\u62da", "\u62d7", "\u62ee", "\u6322", "\u62f6", "\u6339", "\u634b", "\u6343", "\u63ad", "\u63f6", "\u6371", "\u637a", "\u638e", "\u63b4", "\u636d", "\u63ac", "\u638a", "\u6369", "\u63ae", "\u63bc", "\u63f2", "\u63f8", "\u63e0", "\u63ff", "\u63c4", "\u63de", "\u63ce", "\u6452", "\u63c6", "\u63be", "\u6445", "\u6441", "\u640b", "\u641b", "\u6420", "\u640c", "\u6426", "\u6421", "\u645e", "\u6484", "\u646d", "\u6496", "\u901c", "\u9024", "\u9025", "\u9027", "\u9030", "\u9037", "\u9039", "\u903a", "\u903d", "\u903f", "\u9040", "\u9043", "\u9045", "\u9046", "\u9048", "\u9056", "\u9059", "\u905a", "\u905c", "\u9064", "\u9066", "\u9067", "\u906a", "\u906b", "\u906c", "\u906f", "\u9076", "\u907e", "\u9081", "\u9084", "\u9085", "\u9086", "\u9087", "\u9089", "\u908a", "\u908c", "\u9092", "\u9094", "\u9096", "\u9098", "\u909a", "\u909c", "\u909e", "\u909f", "\u90a0", "\u90a4", "\u90a5", "\u90a7", "\u90a8", "\u90a9", "\u90ab", "\u90ad", "\u90b2", "\u90b7", "\u90bc", "\u90bd", "\u90bf", "\u90c0", "\u647a", "\u64b7", "\u64b8", "\u6499", "\u64ba", "\u64c0", "\u64d0", "\u64d7", "\u64e4", "\u64e2", "\u6509", "\u6525", "\u652e", "\u5f0b", "\u5fd2", "\u7519", "\u5f11", "\u535f", "\u53f1", "\u53fd", "\u53e9", "\u53e8", "\u53fb", "\u5412", "\u5416", "\u5406", "\u544b", "\u5452", "\u5453", "\u5454", "\u5456", "\u5443", "\u5421", "\u5457", "\u5459", "\u5423", "\u5432", "\u5482", "\u5494", "\u5477", "\u5471", "\u5464", "\u549a", "\u549b", "\u5484", "\u5476", "\u5466", "\u549d", "\u54d0", "\u54ad", "\u54c2", "\u54b4", "\u54d2", "\u54a7", "\u54a6", "\u54d3", "\u54d4", "\u5472", "\u54a3", "\u54d5", "\u54bb", "\u54bf", "\u54cc", "\u54d9", "\u54da", "\u54dc", "\u54a9", "\u54aa", "\u54a4", "\u54dd", "\u54cf", "\u54de", "\u551b", "\u54e7", "\u5520", "\u54fd", "\u5514", "\u54f3", "\u5522", "\u5523", "\u550f", "\u5511", "\u5527", "\u552a", "\u5567", "\u558f", "\u55b5", "\u5549", "\u556d", "\u5541", "\u5555", "\u553f", "\u5550", "\u553c", "\u90c2", "\u90c3", "\u90c6", "\u90c8", "\u90c9", "\u90cb", "\u90cc", "\u90cd", "\u90d2", "\u90d4", "\u90d5", "\u90d6", "\u90d8", "\u90d9", "\u90da", "\u90de", "\u90df", "\u90e0", "\u90e3", "\u90e4", "\u90e5", "\u90e9", "\u90ea", "\u90ec", "\u90ee", "\u90f0", "\u90f1", "\u90f2", "\u90f3", "\u90f6", "\u90f7", "\u90f9", "\u90fa", "\u90fb", "\u90fc", "\u90ff", "\u9100", "\u9101", "\u9103", "\u9105", "\u911a", "\u911b", "\u911c", "\u911d", "\u911f", "\u9120", "\u9121", "\u9124", "\u9130", "\u9132", "\u913a", "\u9144", "\u5537", "\u5556", "\u5575", "\u5576", "\u5577", "\u5533", "\u5530", "\u555c", "\u558b", "\u55d2", "\u5583", "\u55b1", "\u55b9", "\u5588", "\u5581", "\u559f", "\u557e", "\u55d6", "\u5591", "\u557b", "\u55df", "\u55bd", "\u55be", "\u5594", "\u5599", "\u55ea", "\u55f7", "\u55c9", "\u561f", "\u55d1", "\u55eb", "\u55ec", "\u55d4", "\u55e6", "\u55dd", "\u55c4", "\u55ef", "\u55e5", "\u55f2", "\u55f3", "\u55cc", "\u55cd", "\u55e8", "\u55f5", "\u55e4", "\u8f94", "\u561e", "\u5608", "\u560c", "\u5601", "\u5624", "\u5623", "\u55fe", "\u5600", "\u5627", "\u562d", "\u5658", "\u5639", "\u5657", "\u562c", "\u564d", "\u5662", "\u5659", "\u565c", "\u564c", "\u5654", "\u5686", "\u5664", "\u5671", "\u566b", "\u567b", "\u567c", "\u5685", "\u5693", "\u56af", "\u56d4", "\u56d7", "\u56dd", "\u56e1", "\u56f5", "\u56eb", "\u56f9", "\u56ff", "\u5704", "\u570a", "\u5709", "\u571c", "\u5e0f", "\u5e19", "\u5e14", "\u5e11", "\u5e31", "\u5e3b", "\u5e3c", "\u9145", "\u9147", "\u9148", "\u9151", "\u9153", "\u9154", "\u9155", "\u9156", "\u9158", "\u9159", "\u915b", "\u915c", "\u915f", "\u9160", "\u9166", "\u9167", "\u9168", "\u916b", "\u916d", "\u9173", "\u917a", "\u917b", "\u917c", "\u9180", "\u9186", "\u9188", "\u918a", "\u918e", "\u918f", "\u9193", "\u919c", "\u91a4", "\u91ab", "\u91ac", "\u91b0", "\u91b1", "\u91b2", "\u91b3", "\u91b6", "\u91b7", "\u91b8", "\u91b9", "\u91bb", "\u91bc", "\u91cb", "\u91d0", "\u91d2", "\u91dd", "\u5e37", "\u5e44", "\u5e54", "\u5e5b", "\u5e5e", "\u5e61", "\u5c8c", "\u5c7a", "\u5c8d", "\u5c90", "\u5c96", "\u5c88", "\u5c98", "\u5c99", "\u5c91", "\u5c9a", "\u5c9c", "\u5cb5", "\u5ca2", "\u5cbd", "\u5cac", "\u5cab", "\u5cb1", "\u5ca3", "\u5cc1", "\u5cb7", "\u5cc4", "\u5cd2", "\u5ce4", "\u5ccb", "\u5ce5", "\u5d02", "\u5d03", "\u5d27", "\u5d26", "\u5d2e", "\u5d24", "\u5d1e", "\u5d06", "\u5d1b", "\u5d58", "\u5d3e", "\u5d34", "\u5d3d", "\u5d6c", "\u5d5b", "\u5d6f", "\u5d5d", "\u5d6b", "\u5d4b", "\u5d4a", "\u5d69", "\u5d74", "\u5d82", "\u5d99", "\u5d9d", "\u8c73", "\u5db7", "\u5dc5", "\u5f73", "\u5f77", "\u5f82", "\u5f87", "\u5f89", "\u5f95", "\u5f99", "\u5f9c", "\u5fa8", "\u5fad", "\u5fb5", "\u5fbc", "\u8862", "\u5f61", "\u72ad", "\u72b0", "\u72b4", "\u72b7", "\u72b8", "\u72c3", "\u72c1", "\u72ce", "\u72cd", "\u72d2", "\u72e8", "\u72ef", "\u72e9", "\u72f2", "\u72f4", "\u72f7", "\u7301", "\u72f3", "\u7303", "\u72fa", "\u91e6", "\u9225", "\u72fb", "\u7317", "\u7313", "\u7321", "\u730a", "\u731e", "\u731d", "\u7315", "\u7322", "\u7339", "\u7325", "\u732c", "\u7338", "\u7331", "\u7350", "\u734d", "\u7357", "\u7360", "\u736c", "\u736f", "\u737e", "\u821b", "\u5925", "\u98e7", "\u5924", "\u5902", "\u9963", "\u9967", "\u9974", "\u9977", "\u997d", "\u9980", "\u9984", "\u9987", "\u998a", "\u998d", "\u9990", "\u9991", "\u9993", "\u9994", "\u9995", "\u5e80", "\u5e91", "\u5e8b", "\u5e96", "\u5ea5", "\u5ea0", "\u5eb9", "\u5eb5", "\u5ebe", "\u5eb3", "\u8d53", "\u5ed2", "\u5ed1", "\u5edb", "\u5ee8", "\u5eea", "\u81ba", "\u5fc4", "\u5fc9", "\u5fd6", "\u5fcf", "\u6003", "\u5fee", "\u6004", "\u5fe1", "\u5fe4", "\u5ffe", "\u6005", "\u6006", "\u5fea", "\u5fed", "\u5ff8", "\u6019", "\u6035", "\u6026", "\u601b", "\u600f", "\u600d", "\u6029", "\u602b", "\u600a", "\u603f", "\u6021", "\u6078", "\u6079", "\u607b", "\u607a", "\u6042", "\u9246", "\u9275", "\u9286", "\u928f", "\u606a", "\u607d", "\u6096", "\u609a", "\u60ad", "\u609d", "\u6083", "\u6092", "\u608c", "\u609b", "\u60ec", "\u60bb", "\u60b1", "\u60dd", "\u60d8", "\u60c6", "\u60da", "\u60b4", "\u6120", "\u6126", "\u6115", "\u6123", "\u60f4", "\u6100", "\u610e", "\u612b", "\u614a", "\u6175", "\u61ac", "\u6194", "\u61a7", "\u61b7", "\u61d4", "\u61f5", "\u5fdd", "\u96b3", "\u95e9", "\u95eb", "\u95f1", "\u95f3", "\u95f5", "\u95f6", "\u95fc", "\u95fe", "\u9603", "\u9604", "\u9606", "\u9608", "\u960a", "\u960b", "\u960c", "\u960d", "\u960f", "\u9612", "\u9615", "\u9616", "\u9617", "\u9619", "\u961a", "\u4e2c", "\u723f", "\u6215", "\u6c35", "\u6c54", "\u6c5c", "\u6c4a", "\u6ca3", "\u6c85", "\u6c90", "\u6c94", "\u6c8c", "\u6c68", "\u6c69", "\u6c74", "\u6c76", "\u6c86", "\u6ca9", "\u6cd0", "\u6cd4", "\u6cad", "\u6cf7", "\u6cf8", "\u6cf1", "\u6cd7", "\u6cb2", "\u6ce0", "\u6cd6", "\u6cfa", "\u6ceb", "\u6cee", "\u6cb1", "\u6cd3", "\u6cef", "\u6cfe", "\u92a8", "\u92af", "\u92c9", "\u92e9", "\u6d39", "\u6d27", "\u6d0c", "\u6d43", "\u6d48", "\u6d07", "\u6d04", "\u6d19", "\u6d0e", "\u6d2b", "\u6d4d", "\u6d2e", "\u6d35", "\u6d1a", "\u6d4f", "\u6d52", "\u6d54", "\u6d33", "\u6d91", "\u6d6f", "\u6d9e", "\u6da0", "\u6d5e", "\u6d93", "\u6d94", "\u6d5c", "\u6d60", "\u6d7c", "\u6d63", "\u6e1a", "\u6dc7", "\u6dc5", "\u6dde", "\u6e0e", "\u6dbf", "\u6de0", "\u6e11", "\u6de6", "\u6ddd", "\u6dd9", "\u6e16", "\u6dab", "\u6e0c", "\u6dae", "\u6e2b", "\u6e6e", "\u6e4e", "\u6e6b", "\u6eb2", "\u6e5f", "\u6e86", "\u6e53", "\u6e54", "\u6e32", "\u6e25", "\u6e44", "\u6edf", "\u6eb1", "\u6e98", "\u6ee0", "\u6f2d", "\u6ee2", "\u6ea5", "\u6ea7", "\u6ebd", "\u6ebb", "\u6eb7", "\u6ed7", "\u6eb4", "\u6ecf", "\u6e8f", "\u6ec2", "\u6e9f", "\u6f62", "\u6f46", "\u6f47", "\u6f24", "\u6f15", "\u6ef9", "\u6f2f", "\u6f36", "\u6f4b", "\u6f74", "\u6f2a", "\u6f09", "\u6f29", "\u6f89", "\u6f8d", "\u6f8c", "\u6f78", "\u6f72", "\u6f7c", "\u6f7a", "\u6fd1", "\u930a", "\u933f", "\u934a", "\u936b", "\u6fc9", "\u6fa7", "\u6fb9", "\u6fb6", "\u6fc2", "\u6fe1", "\u6fee", "\u6fde", "\u6fe0", "\u6fef", "\u701a", "\u7023", "\u701b", "\u7039", "\u7035", "\u704f", "\u705e", "\u5b80", "\u5b84", "\u5b95", "\u5b93", "\u5ba5", "\u5bb8", "\u752f", "\u9a9e", "\u6434", "\u5be4", "\u5bee", "\u8930", "\u5bf0", "\u8e47", "\u8b07", "\u8fb6", "\u8fd3", "\u8fd5", "\u8fe5", "\u8fee", "\u8fe4", "\u8fe9", "\u8fe6", "\u8ff3", "\u8fe8", "\u9005", "\u9004", "\u900b", "\u9026", "\u9011", "\u900d", "\u9016", "\u9021", "\u9035", "\u9036", "\u902d", "\u902f", "\u9044", "\u9051", "\u9052", "\u9050", "\u9068", "\u9058", "\u9062", "\u905b", "\u66b9", "\u9074", "\u907d", "\u9082", "\u9088", "\u9083", "\u908b", "\u5f50", "\u5f57", "\u5f56", "\u5f58", "\u5c3b", "\u54ab", "\u5c50", "\u5c59", "\u5b71", "\u5c63", "\u5c66", "\u7fbc", "\u5f2a", "\u5f29", "\u5f2d", "\u8274", "\u5f3c", "\u9b3b", "\u5c6e", "\u5981", "\u5983", "\u598d", "\u59a9", "\u59aa", "\u59a3", "\u936c", "\u9390", "\u93ac", "\u93cb", "\u93cc", "\u93cd", "\u5997", "\u59ca", "\u59ab", "\u599e", "\u59a4", "\u59d2", "\u59b2", "\u59af", "\u59d7", "\u59be", "\u5a05", "\u5a06", "\u59dd", "\u5a08", "\u59e3", "\u59d8", "\u59f9", "\u5a0c", "\u5a09", "\u5a32", "\u5a34", "\u5a11", "\u5a23", "\u5a13", "\u5a40", "\u5a67", "\u5a4a", "\u5a55", "\u5a3c", "\u5a62", "\u5a75", "\u80ec", "\u5aaa", "\u5a9b", "\u5a77", "\u5a7a", "\u5abe", "\u5aeb", "\u5ab2", "\u5ad2", "\u5ad4", "\u5ab8", "\u5ae0", "\u5ae3", "\u5af1", "\u5ad6", "\u5ae6", "\u5ad8", "\u5adc", "\u5b09", "\u5b17", "\u5b16", "\u5b32", "\u5b37", "\u5b40", "\u5c15", "\u5c1c", "\u5b5a", "\u5b65", "\u5b73", "\u5b51", "\u5b53", "\u5b62", "\u9a75", "\u9a77", "\u9a78", "\u9a7a", "\u9a7f", "\u9a7d", "\u9a80", "\u9a81", "\u9a85", "\u9a88", "\u9a8a", "\u9a90", "\u9a92", "\u9a93", "\u9a96", "\u9a98", "\u9a9b", "\u9a9c", "\u9a9d", "\u9a9f", "\u9aa0", "\u9aa2", "\u9aa3", "\u9aa5", "\u9aa7", "\u7e9f", "\u7ea1", "\u7ea3", "\u7ea5", "\u7ea8", "\u7ea9", "\u93ce", "\u93d7", "\u940e", "\u7ead", "\u7eb0", "\u7ebe", "\u7ec0", "\u7ec1", "\u7ec2", "\u7ec9", "\u7ecb", "\u7ecc", "\u7ed0", "\u7ed4", "\u7ed7", "\u7edb", "\u7ee0", "\u7ee1", "\u7ee8", "\u7eeb", "\u7eee", "\u7eef", "\u7ef1", "\u7ef2", "\u7f0d", "\u7ef6", "\u7efa", "\u7efb", "\u7efe", "\u7f01", "\u7f02", "\u7f03", "\u7f07", "\u7f08", "\u7f0b", "\u7f0c", "\u7f0f", "\u7f11", "\u7f12", "\u7f17", "\u7f19", "\u7f1c", "\u7f1b", "\u7f1f", "\u7f21", "\u7f2a", "\u7f2b", "\u7f2c", "\u7f2d", "\u7f2f", "\u7f35", "\u5e7a", "\u757f", "\u5ddb", "\u753e", "\u9095", "\u738e", "\u7391", "\u73ae", "\u73a2", "\u739f", "\u73cf", "\u73c2", "\u73d1", "\u73b7", "\u73b3", "\u73c0", "\u73c9", "\u73c8", "\u73e5", "\u73d9", "\u987c", "\u740a", "\u73e9", "\u73e7", "\u73de", "\u73ba", "\u73f2", "\u740f", "\u742a", "\u745b", "\u7426", "\u7425", "\u7428", "\u7430", "\u742e", "\u742c", "\u942f", "\u943f", "\u946c", "\u946d", "\u946e", "\u946f", "\u9470", "\u9491", "\u9496", "\u9498", "\u94c7", "\u94cf", "\u94d3", "\u94d4", "\u94da", "\u94e6", "\u94fb", "\u951c", "\u9520", "\u741b", "\u741a", "\u7441", "\u745c", "\u7457", "\u7455", "\u7459", "\u7477", "\u746d", "\u747e", "\u749c", "\u748e", "\u7480", "\u7481", "\u7487", "\u748b", "\u749e", "\u74a8", "\u74a9", "\u7490", "\u74a7", "\u74d2", "\u74ba", "\u97ea", "\u97eb", "\u97ec", "\u674c", "\u6753", "\u675e", "\u6748", "\u6769", "\u67a5", "\u6787", "\u676a", "\u6773", "\u6798", "\u67a7", "\u6775", "\u67a8", "\u679e", "\u67ad", "\u678b", "\u6777", "\u677c", "\u67f0", "\u6809", "\u67d8", "\u680a", "\u67e9", "\u67b0", "\u680c", "\u67d9", "\u67b5", "\u67da", "\u67b3", "\u67dd", "\u6800", "\u67c3", "\u67b8", "\u67e2", "\u680e", "\u67c1", "\u67fd", "\u6832", "\u6833", "\u6860", "\u6861", "\u684e", "\u6862", "\u6844", "\u6864", "\u6883", "\u681d", "\u6855", "\u6866", "\u6841", "\u6867", "\u6840", "\u683e", "\u684a", "\u6849", "\u6829", "\u68b5", "\u688f", "\u6874", "\u6877", "\u6893", "\u686b", "\u68c2", "\u696e", "\u68fc", "\u691f", "\u6920", "\u68f9", "\u9527", "\u9533", "\u953d", "\u9543", "\u9548", "\u954b", "\u9555", "\u955a", "\u9560", "\u956e", "\u9574", "\u9575", "\u95ab", "\u6924", "\u68f0", "\u690b", "\u6901", "\u6957", "\u68e3", "\u6910", "\u6971", "\u6939", "\u6960", "\u6942", "\u695d", "\u6984", "\u696b", "\u6980", "\u6998", "\u6978", "\u6934", "\u69cc", "\u6987", "\u6988", "\u69ce", "\u6989", "\u6966", "\u6963", "\u6979", "\u699b", "\u69a7", "\u69bb", "\u69ab", "\u69ad", "\u69d4", "\u69b1", "\u69c1", "\u69ca", "\u69df", "\u6995", "\u69e0", "\u698d", "\u69ff", "\u6a2f", "\u69ed", "\u6a17", "\u6a18", "\u6a65", "\u69f2", "\u6a44", "\u6a3e", "\u6aa0", "\u6a50", "\u6a5b", "\u6a35", "\u6a8e", "\u6a79", "\u6a3d", "\u6a28", "\u6a58", "\u6a7c", "\u6a91", "\u6a90", "\u6aa9", "\u6a97", "\u6aab", "\u7337", "\u7352", "\u6b81", "\u6b82", "\u6b87", "\u6b84", "\u6b92", "\u6b93", "\u6b8d", "\u6b9a", "\u6b9b", "\u6ba1", "\u6baa", "\u8f6b", "\u8f6d", "\u8f71", "\u8f72", "\u8f73", "\u8f75", "\u8f76", "\u8f78", "\u8f77", "\u8f79", "\u8f7a", "\u8f7c", "\u8f7e", "\u8f81", "\u8f82", "\u8f84", "\u8f87", "\u8f8b", "\u95cc", "\u95ec", "\u95ff", "\u9607", "\u9613", "\u9618", "\u961b", "\u961e", "\u9620", "\u9623", "\u962b", "\u962c", "\u962d", "\u962f", "\u9630", "\u9637", "\u9638", "\u9639", "\u963a", "\u963e", "\u9641", "\u9643", "\u964a", "\u964e", "\u964f", "\u9651", "\u9652", "\u9653", "\u9656", "\u9657", "\u9658", "\u9659", "\u965a", "\u965c", "\u965d", "\u965e", "\u9660", "\u9665", "\u9666", "\u966b", "\u966d", "\u9673", "\u9678", "\u9687", "\u9689", "\u968a", "\u8f8d", "\u8f8e", "\u8f8f", "\u8f98", "\u8f9a", "\u8ece", "\u620b", "\u6217", "\u621b", "\u621f", "\u6222", "\u6221", "\u6225", "\u6224", "\u622c", "\u81e7", "\u74ef", "\u74f4", "\u74ff", "\u750f", "\u7511", "\u7513", "\u6534", "\u65ee", "\u65ef", "\u65f0", "\u660a", "\u6619", "\u6772", "\u6603", "\u6615", "\u6600", "\u7085", "\u66f7", "\u661d", "\u6634", "\u6631", "\u6636", "\u6635", "\u8006", "\u665f", "\u6654", "\u6641", "\u664f", "\u6656", "\u6661", "\u6657", "\u6677", "\u6684", "\u668c", "\u66a7", "\u669d", "\u66be", "\u66db", "\u66e6", "\u66e9", "\u8d32", "\u8d33", "\u8d36", "\u8d3b", "\u8d3d", "\u8d40", "\u8d45", "\u8d46", "\u8d48", "\u8d49", "\u8d47", "\u8d4d", "\u8d55", "\u8d59", "\u89c7", "\u89ca", "\u89cb", "\u89cc", "\u89ce", "\u89cf", "\u89d0", "\u89d1", "\u726e", "\u729f", "\u725d", "\u7266", "\u726f", "\u727e", "\u727f", "\u7284", "\u728b", "\u728d", "\u728f", "\u7292", "\u6308", "\u6332", "\u63b0", "\u968c", "\u968e", "\u9691", "\u9692", "\u9693", "\u9695", "\u9696", "\u969a", "\u969d", "\u96b2", "\u96b4", "\u96b5", "\u96b7", "\u96b8", "\u96ba", "\u96bb", "\u96bf", "\u96c2", "\u96c3", "\u96c8", "\u96ca", "\u96cb", "\u96d0", "\u96d1", "\u96d3", "\u96d4", "\u96d6", "\u96e1", "\u96eb", "\u96ec", "\u96ed", "\u96ee", "\u96f0", "\u96f1", "\u96f2", "\u96f4", "\u96f5", "\u96f8", "\u96fa", "\u96fc", "\u96fd", "\u96ff", "\u9702", "\u9703", "\u9705", "\u970a", "\u970b", "\u970c", "\u9710", "\u9711", "\u9712", "\u9714", "\u9715", "\u9717", "\u971d", "\u971f", "\u9720", "\u643f", "\u64d8", "\u8004", "\u6bea", "\u6bf3", "\u6bfd", "\u6bf5", "\u6bf9", "\u6c05", "\u6c07", "\u6c06", "\u6c0d", "\u6c15", "\u6c18", "\u6c19", "\u6c1a", "\u6c21", "\u6c29", "\u6c24", "\u6c2a", "\u6c32", "\u6535", "\u6555", "\u656b", "\u724d", "\u7252", "\u7256", "\u7230", "\u8662", "\u5216", "\u809f", "\u809c", "\u8093", "\u80bc", "\u670a", "\u80bd", "\u80b1", "\u80ab", "\u80ad", "\u80b4", "\u80b7", "\u80e7", "\u80e8", "\u80e9", "\u80ea", "\u80db", "\u80c2", "\u80c4", "\u80d9", "\u80cd", "\u80d7", "\u6710", "\u80dd", "\u80eb", "\u80f1", "\u80f4", "\u80ed", "\u810d", "\u810e", "\u80f2", "\u80fc", "\u6715", "\u8112", "\u8c5a", "\u8136", "\u811e", "\u812c", "\u8118", "\u8132", "\u8148", "\u814c", "\u8153", "\u8174", "\u8159", "\u815a", "\u8171", "\u8160", "\u8169", "\u817c", "\u817d", "\u816d", "\u8167", "\u584d", "\u5ab5", "\u8188", "\u8182", "\u8191", "\u6ed5", "\u81a3", "\u81aa", "\u81cc", "\u6726", "\u81ca", "\u81bb", "\u9721", "\u972b", "\u972c", "\u972e", "\u972f", "\u9731", "\u9733", "\u973a", "\u973b", "\u973c", "\u973d", "\u973f", "\u9754", "\u9755", "\u9757", "\u9758", "\u975a", "\u975c", "\u975d", "\u975f", "\u9763", "\u9764", "\u9766", "\u9767", "\u9768", "\u976a", "\u9772", "\u9775", "\u9777", "\u977d", "\u9786", "\u978c", "\u978e", "\u978f", "\u9790", "\u9793", "\u9795", "\u9796", "\u9797", "\u9799", "\u81c1", "\u81a6", "\u6b24", "\u6b37", "\u6b39", "\u6b43", "\u6b46", "\u6b59", "\u98d1", "\u98d2", "\u98d3", "\u98d5", "\u98d9", "\u98da", "\u6bb3", "\u5f40", "\u6bc2", "\u89f3", "\u6590", "\u9f51", "\u6593", "\u65c6", "\u65c4", "\u65c3", "\u65cc", "\u65ce", "\u65d2", "\u65d6", "\u7080", "\u709c", "\u7096", "\u709d", "\u70bb", "\u70c0", "\u70b7", "\u70ab", "\u70b1", "\u70e8", "\u70ca", "\u7110", "\u7113", "\u7116", "\u712f", "\u7131", "\u7173", "\u715c", "\u7168", "\u7145", "\u7172", "\u714a", "\u7178", "\u717a", "\u7198", "\u71b3", "\u71b5", "\u71a8", "\u71a0", "\u71e0", "\u71d4", "\u71e7", "\u71f9", "\u721d", "\u7228", "\u706c", "\u7118", "\u7166", "\u71b9", "\u623e", "\u623d", "\u6243", "\u6248", "\u6249", "\u793b", "\u7940", "\u7946", "\u7949", "\u795b", "\u795c", "\u7953", "\u795a", "\u7962", "\u7957", "\u7960", "\u796f", "\u7967", "\u797a", "\u7985", "\u798a", "\u799a", "\u79a7", "\u79b3", "\u5fd1", "\u5fd0", "\u979e", "\u979f", "\u97a1", "\u97a2", "\u97a4", "\u97ac", "\u97ae", "\u97b0", "\u97b1", "\u97b3", "\u97b5", "\u97e4", "\u97e5", "\u97e8", "\u97ee", "\u97f4", "\u97f7", "\u603c", "\u605d", "\u605a", "\u6067", "\u6041", "\u6059", "\u6063", "\u60ab", "\u6106", "\u610d", "\u615d", "\u61a9", "\u619d", "\u61cb", "\u61d1", "\u6206", "\u8080", "\u807f", "\u6c93", "\u6cf6", "\u6dfc", "\u77f6", "\u77f8", "\u7800", "\u7809", "\u7817", "\u7818", "\u7811", "\u65ab", "\u782d", "\u781c", "\u781d", "\u7839", "\u783a", "\u783b", "\u781f", "\u783c", "\u7825", "\u782c", "\u7823", "\u7829", "\u784e", "\u786d", "\u7856", "\u7857", "\u7826", "\u7850", "\u7847", "\u784c", "\u786a", "\u789b", "\u7893", "\u789a", "\u7887", "\u789c", "\u78a1", "\u78a3", "\u78b2", "\u78b9", "\u78a5", "\u78d4", "\u78d9", "\u78c9", "\u78ec", "\u78f2", "\u7905", "\u78f4", "\u7913", "\u7924", "\u791e", "\u7934", "\u9f9b", "\u9ef9", "\u9efb", "\u9efc", "\u76f1", "\u7704", "\u770d", "\u76f9", "\u7707", "\u7708", "\u771a", "\u7722", "\u7719", "\u772d", "\u7726", "\u7735", "\u7738", "\u7750", "\u7751", "\u7747", "\u7743", "\u775a", "\u7768", "\u980f", "\u984e", "\u7762", "\u7765", "\u777f", "\u778d", "\u777d", "\u7780", "\u778c", "\u7791", "\u779f", "\u77a0", "\u77b0", "\u77b5", "\u77bd", "\u753a", "\u7540", "\u754e", "\u754b", "\u7548", "\u755b", "\u7572", "\u7579", "\u7583", "\u7f58", "\u7f61", "\u7f5f", "\u8a48", "\u7f68", "\u7f74", "\u7f71", "\u7f79", "\u7f81", "\u7f7e", "\u76cd", "\u76e5", "\u8832", "\u9485", "\u9486", "\u9487", "\u948b", "\u948a", "\u948c", "\u948d", "\u948f", "\u9490", "\u9494", "\u9497", "\u9495", "\u949a", "\u949b", "\u949c", "\u94a3", "\u94a4", "\u94ab", "\u94aa", "\u94ad", "\u94ac", "\u94af", "\u94b0", "\u94b2", "\u94b4", "\u94b6", "\u94bc", "\u94bd", "\u94bf", "\u94c4", "\u94c8", "\u94d0", "\u94d1", "\u94d2", "\u94d5", "\u94d6", "\u94d7", "\u94d9", "\u94d8", "\u94db", "\u94de", "\u94df", "\u94e0", "\u94e2", "\u94e4", "\u94e5", "\u94e7", "\u94e8", "\u94ea", "\u988b", "\u988e", "\u9892", "\u9895", "\u9899", "\u98a3", "\u98a8", "\u98cf", "\u98d0", "\u98d4", "\u98d6", "\u98d7", "\u98db", "\u98dc", "\u98dd", "\u98e0", "\u98e5", "\u98e6", "\u98e9", "\u94e9", "\u94eb", "\u94ee", "\u94ef", "\u94f3", "\u94f4", "\u94f5", "\u94f7", "\u94f9", "\u94fc", "\u94fd", "\u94ff", "\u9503", "\u9502", "\u9506", "\u9507", "\u9509", "\u950a", "\u950d", "\u950e", "\u950f", "\u9512", "\u9518", "\u951b", "\u951d", "\u951e", "\u951f", "\u9522", "\u952a", "\u952b", "\u9529", "\u952c", "\u9531", "\u9532", "\u9534", "\u9536", "\u9537", "\u9538", "\u953c", "\u953e", "\u953f", "\u9542", "\u9535", "\u9544", "\u9545", "\u9546", "\u9549", "\u954c", "\u954e", "\u954f", "\u9552", "\u9553", "\u9554", "\u9556", "\u9557", "\u9558", "\u9559", "\u955b", "\u955e", "\u955f", "\u955d", "\u9561", "\u9562", "\u9564", "\u956f", "\u9571", "\u9572", "\u9573", "\u953a", "\u77e7", "\u77ec", "\u96c9", "\u79d5", "\u79ed", "\u79e3", "\u79eb", "\u7a06", "\u5d47", "\u7a03", "\u7a02", "\u7a1e", "\u7a14", "\u9908", "\u990e", "\u990f", "\u9911", "\u992f", "\u994a", "\u9956", "\u9964", "\u9966", "\u9973", "\u9978", "\u9979", "\u997b", "\u997e", "\u9982", "\u9983", "\u9989", "\u7a39", "\u7a37", "\u7a51", "\u9ecf", "\u99a5", "\u7a70", "\u7688", "\u768e", "\u7693", "\u7699", "\u76a4", "\u74de", "\u74e0", "\u752c", "\u9e20", "\u9e22", "\u9e28", "\u9e32", "\u9e31", "\u9e36", "\u9e38", "\u9e37", "\u9e39", "\u9e3a", "\u9e3e", "\u9e41", "\u9e42", "\u9e44", "\u9e46", "\u9e47", "\u9e48", "\u9e49", "\u9e4b", "\u9e4c", "\u9e4e", "\u9e51", "\u9e55", "\u9e57", "\u9e5a", "\u9e5b", "\u9e5c", "\u9e5e", "\u9e63", "\u9e66", "\u9e71", "\u9e6d", "\u9e73", "\u7592", "\u7594", "\u7596", "\u75a0", "\u759d", "\u75ac", "\u75a3", "\u75b3", "\u75b4", "\u75b8", "\u75c4", "\u75b1", "\u75b0", "\u75c3", "\u75c2", "\u75d6", "\u75cd", "\u75e3", "\u75e8", "\u75e6", "\u75e4", "\u75eb", "\u75e7", "\u7603", "\u75f1", "\u75fc", "\u75ff", "\u7610", "\u7600", "\u7605", "\u760c", "\u7617", "\u760a", "\u7625", "\u7618", "\u7615", "\u7619", "\u998c", "\u998e", "\u999a", "\u99a6", "\u99a7", "\u99a9", "\u99d9", "\u761b", "\u763c", "\u7622", "\u7620", "\u7640", "\u762d", "\u7630", "\u763f", "\u7635", "\u7643", "\u763e", "\u7633", "\u764d", "\u765e", "\u7654", "\u765c", "\u7656", "\u766b", "\u766f", "\u7fca", "\u7ae6", "\u7a78", "\u7a79", "\u7a80", "\u7a86", "\u7a88", "\u7a95", "\u7aa6", "\u7aa0", "\u7aac", "\u7aa8", "\u7aad", "\u7ab3", "\u8864", "\u8869", "\u8872", "\u887d", "\u887f", "\u8882", "\u88a2", "\u88c6", "\u88b7", "\u88bc", "\u88c9", "\u88e2", "\u88ce", "\u88e3", "\u88e5", "\u88f1", "\u891a", "\u88fc", "\u88e8", "\u88fe", "\u88f0", "\u8921", "\u8919", "\u8913", "\u891b", "\u890a", "\u8934", "\u892b", "\u8936", "\u8941", "\u8966", "\u897b", "\u758b", "\u80e5", "\u76b2", "\u76b4", "\u77dc", "\u8012", "\u8014", "\u8016", "\u801c", "\u8020", "\u8022", "\u8025", "\u8026", "\u8027", "\u8029", "\u8028", "\u8031", "\u800b", "\u8035", "\u8043", "\u8046", "\u804d", "\u8052", "\u8069", "\u8071", "\u8983", "\u9878", "\u9880", "\u9883", "\u99fa", "\u9a39", "\u9889", "\u988c", "\u988d", "\u988f", "\u9894", "\u989a", "\u989b", "\u989e", "\u989f", "\u98a1", "\u98a2", "\u98a5", "\u98a6", "\u864d", "\u8654", "\u866c", "\u866e", "\u867f", "\u867a", "\u867c", "\u867b", "\u86a8", "\u868d", "\u868b", "\u86ac", "\u869d", "\u86a7", "\u86a3", "\u86aa", "\u8693", "\u86a9", "\u86b6", "\u86c4", "\u86b5", "\u86ce", "\u86b0", "\u86ba", "\u86b1", "\u86af", "\u86c9", "\u86cf", "\u86b4", "\u86e9", "\u86f1", "\u86f2", "\u86ed", "\u86f3", "\u86d0", "\u8713", "\u86de", "\u86f4", "\u86df", "\u86d8", "\u86d1", "\u8703", "\u8707", "\u86f8", "\u8708", "\u870a", "\u870d", "\u8709", "\u8723", "\u873b", "\u871e", "\u8725", "\u872e", "\u871a", "\u873e", "\u8748", "\u8734", "\u8731", "\u8729", "\u8737", "\u873f", "\u8782", "\u8722", "\u877d", "\u877e", "\u877b", "\u8760", "\u8770", "\u874c", "\u876e", "\u878b", "\u8753", "\u8763", "\u877c", "\u8764", "\u8759", "\u8765", "\u8793", "\u87af", "\u87a8", "\u87d2", "\u9a5a", "\u9a72", "\u9a83", "\u9a89", "\u9a8d", "\u9a8e", "\u9a94", "\u9a95", "\u9a99", "\u9aa6", "\u9aa9", "\u9ab2", "\u9ab3", "\u9ab4", "\u9ab5", "\u9ab9", "\u9abb", "\u9abd", "\u9abe", "\u9abf", "\u9ac3", "\u9ac4", "\u9ac6", "\u9acd", "\u9ace", "\u9acf", "\u9ad0", "\u9ad2", "\u9ad5", "\u9ad6", "\u9ad7", "\u9ad9", "\u9ada", "\u9adb", "\u9adc", "\u9add", "\u9ade", "\u9ae0", "\u9ae2", "\u9ae3", "\u9ae4", "\u9ae5", "\u9ae7", "\u9ae8", "\u9ae9", "\u9aea", "\u9aec", "\u9aee", "\u9af0", "\u9afa", "\u9afc", "\u9b04", "\u9b05", "\u9b06", "\u87c6", "\u8788", "\u8785", "\u87ad", "\u8797", "\u8783", "\u87ab", "\u87e5", "\u87ac", "\u87b5", "\u87b3", "\u87cb", "\u87d3", "\u87bd", "\u87d1", "\u87c0", "\u87ca", "\u87db", "\u87ea", "\u87e0", "\u87ee", "\u8816", "\u8813", "\u87fe", "\u880a", "\u881b", "\u8821", "\u8839", "\u883c", "\u7f36", "\u7f42", "\u7f44", "\u7f45", "\u8210", "\u7afa", "\u7afd", "\u7b08", "\u7b03", "\u7b04", "\u7b15", "\u7b0a", "\u7b2b", "\u7b0f", "\u7b47", "\u7b38", "\u7b2a", "\u7b19", "\u7b2e", "\u7b31", "\u7b20", "\u7b25", "\u7b24", "\u7b33", "\u7b3e", "\u7b1e", "\u7b58", "\u7b5a", "\u7b45", "\u7b75", "\u7b4c", "\u7b5d", "\u7b60", "\u7b6e", "\u7b7b", "\u7b62", "\u7b72", "\u7b71", "\u7b90", "\u7ba6", "\u7ba7", "\u7bb8", "\u7bac", "\u7b9d", "\u7ba8", "\u7b85", "\u7baa", "\u7b9c", "\u7ba2", "\u7bab", "\u7bb4", "\u7bd1", "\u7bc1", "\u7bcc", "\u7bdd", "\u7bda", "\u7be5", "\u7be6", "\u7bea", "\u7c0c", "\u7bfe", "\u7bfc", "\u7c0f", "\u7c16", "\u7c0b", "\u9b07", "\u9b09", "\u9b10", "\u9b11", "\u9b12", "\u9b14", "\u9b20", "\u9b21", "\u9b22", "\u9b24", "\u9b30", "\u9b31", "\u9b33", "\u9b3d", "\u9b3e", "\u9b3f", "\u9b40", "\u9b46", "\u9b4a", "\u9b4b", "\u9b4c", "\u9b4e", "\u9b50", "\u9b52", "\u9b53", "\u9b55", "\u9b5b", "\u7c1f", "\u7c2a", "\u7c26", "\u7c38", "\u7c41", "\u7c40", "\u81fe", "\u8201", "\u8202", "\u8204", "\u81ec", "\u8844", "\u8221", "\u8222", "\u8223", "\u822d", "\u822f", "\u8228", "\u822b", "\u8238", "\u823b", "\u8233", "\u8234", "\u823e", "\u8244", "\u8249", "\u824b", "\u824f", "\u825a", "\u825f", "\u8268", "\u887e", "\u8885", "\u8888", "\u88d8", "\u88df", "\u895e", "\u7f9d", "\u7f9f", "\u7fa7", "\u7faf", "\u7fb0", "\u7fb2", "\u7c7c", "\u6549", "\u7c91", "\u7c9d", "\u7c9c", "\u7c9e", "\u7ca2", "\u7cb2", "\u7cbc", "\u7cbd", "\u7cc1", "\u7cc7", "\u7ccc", "\u7ccd", "\u7cc8", "\u7cc5", "\u7cd7", "\u7ce8", "\u826e", "\u66a8", "\u7fbf", "\u7fce", "\u7fd5", "\u7fe5", "\u7fe1", "\u7fe6", "\u7fe9", "\u7fee", "\u7ff3", "\u7cf8", "\u7d77", "\u7da6", "\u7dae", "\u7e47", "\u7e9b", "\u9eb8", "\u9eb4", "\u8d73", "\u8d84", "\u8d94", "\u8d91", "\u8db1", "\u8d67", "\u8d6d", "\u8c47", "\u8c49", "\u914a", "\u9150", "\u914e", "\u914f", "\u9164", "\u9b7c", "\u9bbb", "\u9162", "\u9161", "\u9170", "\u9169", "\u916f", "\u917d", "\u917e", "\u9172", "\u9174", "\u9179", "\u918c", "\u9185", "\u9190", "\u918d", "\u9191", "\u91a2", "\u91a3", "\u91aa", "\u91ad", "\u91ae", "\u91af", "\u91b5", "\u91b4", "\u91ba", "\u8c55", "\u9e7e", "\u8db8", "\u8deb", "\u8e05", "\u8e59", "\u8e69", "\u8db5", "\u8dbf", "\u8dbc", "\u8dba", "\u8dc4", "\u8dd6", "\u8dd7", "\u8dda", "\u8dde", "\u8dce", "\u8dcf", "\u8ddb", "\u8dc6", "\u8dec", "\u8df7", "\u8df8", "\u8de3", "\u8df9", "\u8dfb", "\u8de4", "\u8e09", "\u8dfd", "\u8e14", "\u8e1d", "\u8e1f", "\u8e2c", "\u8e2e", "\u8e23", "\u8e2f", "\u8e3a", "\u8e40", "\u8e39", "\u8e35", "\u8e3d", "\u8e31", "\u8e49", "\u8e41", "\u8e42", "\u8e51", "\u8e52", "\u8e4a", "\u8e70", "\u8e76", "\u8e7c", "\u8e6f", "\u8e74", "\u8e85", "\u8e8f", "\u8e94", "\u8e90", "\u8e9c", "\u8e9e", "\u8c78", "\u8c82", "\u8c8a", "\u8c85", "\u8c98", "\u8c94", "\u659b", "\u89d6", "\u89de", "\u89da", "\u89dc", "\u9bdc", "\u9c1b", "\u89e5", "\u89eb", "\u89ef", "\u8a3e", "\u8b26", "\u9753", "\u96e9", "\u96f3", "\u96ef", "\u9706", "\u9701", "\u9708", "\u970f", "\u970e", "\u972a", "\u972d", "\u9730", "\u973e", "\u9f80", "\u9f83", "\u9f85", "\u9f8c", "\u9efe", "\u9f0b", "\u9f0d", "\u96b9", "\u96bc", "\u96bd", "\u96ce", "\u96d2", "\u77bf", "\u96e0", "\u928e", "\u92ae", "\u92c8", "\u933e", "\u936a", "\u93ca", "\u938f", "\u943e", "\u946b", "\u9c7f", "\u9c82", "\u9c85", "\u9c86", "\u9c87", "\u9c88", "\u7a23", "\u9c8b", "\u9c8e", "\u9c90", "\u9c91", "\u9c92", "\u9c94", "\u9c95", "\u9c9a", "\u9c9b", "\u9c9e", "\u9ca5", "\u9cab", "\u9cad", "\u9cae", "\u9cb0", "\u9cba", "\u9cbb", "\u9cbc", "\u9cbd", "\u9cc4", "\u9cc5", "\u9cc6", "\u9cc7", "\u9cca", "\u9ccb", "\u9c3c", "\u9c7b", "\u9c7d", "\u9c7e", "\u9c80", "\u9c83", "\u9c84", "\u9c89", "\u9c8a", "\u9c8c", "\u9c8f", "\u9c93", "\u9c96", "\u9c97", "\u9c98", "\u9c99", "\u9c9d", "\u9caa", "\u9cac", "\u9caf", "\u9cb9", "\u9cbe", "\u9cc8", "\u9cc9", "\u9cd1", "\u9cd2", "\u9cda", "\u9cdb", "\u9ce0", "\u9ce1", "\u9ccc", "\u9cd3", "\u9cd4", "\u9cd5", "\u9cd7", "\u9cd8", "\u9cd9", "\u9cdc", "\u9cdd", "\u9cdf", "\u9ce2", "\u977c", "\u9785", "\u9791", "\u9792", "\u9794", "\u97af", "\u97ab", "\u97a3", "\u97b2", "\u97b4", "\u9ab1", "\u9ab0", "\u9ab7", "\u9e58", "\u9ab6", "\u9aba", "\u9abc", "\u9ac1", "\u9ac0", "\u9ac5", "\u9ac2", "\u9acb", "\u9acc", "\u9ad1", "\u9b45", "\u9b43", "\u9b47", "\u9b49", "\u9b48", "\u9b4d", "\u9b51", "\u98e8", "\u990d", "\u992e", "\u9955", "\u9954", "\u9adf", "\u9ae1", "\u9ae6", "\u9aef", "\u9aeb", "\u9afb", "\u9aed", "\u9af9", "\u9b08", "\u9b0f", "\u9b13", "\u9b1f", "\u9b23", "\u9ebd", "\u9ebe", "\u7e3b", "\u9e82", "\u9e87", "\u9e88", "\u9e8b", "\u9e92", "\u93d6", "\u9e9d", "\u9e9f", "\u9edb", "\u9edc", "\u9edd", "\u9ee0", "\u9edf", "\u9ee2", "\u9ee9", "\u9ee7", "\u9ee5", "\u9eea", "\u9eef", "\u9f22", "\u9f2c", "\u9f2f", "\u9f39", "\u9f37", "\u9f3d", "\u9f3e", "\u9f44", "\u9ce3", "\u9d22", "\u9d43", "\u9d82", "\u9da3", "\u9de2", "\u9e03", "\u9e24", "\u9e27", "\u9e2e", "\u9e30", "\u9e34", "\u9e3b", "\u9e3c", "\u9e40", "\u9e4d", "\u9e50", "\u9e52", "\u9e53", "\u9e54", "\u9e56", "\u9e59", "\u9e5d", "\u9e5f", "\u9e60", "\u9e61", "\u9e62", "\u9e65", "\u9e6e", "\u9e6f", "\u9e72", "\u9e74", "\u9e80", "\u9e81", "\u9e83", "\u9e84", "\u9e85", "\u9e86", "\u9e89", "\u9e8a", "\u9e8c", "\u9e94", "\u9e9e", "\u9ea0", "\u9ea7", "\u9ea8", "\u9ea9", "\u9eaa", "\u9eab", "\u9eb5", "\u9eb6", "\u9eb7", "\u9eb9", "\u9eba", "\u9ebf", "\u9ec5", "\u9ec6", "\u9ec7", "\u9ec8", "\u9eca", "\u9ecb", "\u9ecc", "\u9ed0", "\u9ed2", "\u9ed3", "\u9ed5", "\u9ed6", "\u9ed7", "\u9ed9", "\u9eda", "\u9ee1", "\u9ee3", "\u9ee4", "\u9ee6", "\u9ee8", "\u9eeb", "\u9eec", "\u9eed", "\u9eee", "\u9ef0", "\u9efa", "\u9efd", "\u9eff", "\u9f06", "\u9f0c", "\u9f0f", "\u9f11", "\u9f12", "\u9f14", "\u9f15", "\u9f16", "\u9f18", "\u9f1a", "\u9f21", "\u9f23", "\u9f2d", "\u9f2e", "\u9f30", "\u9f31", "\u9f32", "\u9f38", "\u9f3a", "\u9f3c", "\u9f3f", "\u9f45", "\u9f52", "\u9f79", "\u9f81", "\u9f82", "\u9f8d", "\u9f9c", "\u9f9d", "\u9f9e", "\u9fa1", "\uf92c", "\uf979", "\uf995", "\uf9e7", "\uf9f1", "\ufa0c", "\ufa0d", "\ufa0e", "\ufa0f", "\ufa11", "\ufa13", "\ufa14", "\ufa18", "\ufa1f", "\ufa20", "\ufa21", "\ufa23", "\ufa24", "\ufa27", "\ufa28", "\ufa29", "\ue4c6", "\ue505", "\ue526", "\ue565", "\ue766", "\ue76d", "\ue76e", "\ue586", "\ue5c5", "\ue5e6", "\ue77d", "\ue785", "\ue7a0", "\ue7af", "\ue7bc", "\ue7ca", "\ue7cb", "\ue7cc", "\ue7cd", "\ue7e5", "\ue7e6", "\u303e", "\u2ff0", "\ue7f4", "\ue801", "\ue000", "\ue05e", "\ue0bc", "\ue11a", "\ue1d6", "\ue810", "\ue292", "\ue2f0", "\ue34e", "\ue3ac", "\ue40a", "\u2e81", "\ue816", "\ue817", "\ue818", "\u2e84", "\u3473", "\u3447", "\u2e88", "\u2e8b", "\ue81e", "\u359e", "\u361a", "\u360e", "\u2e8c", "\u2e97", "\u396e", "\u3918", "\ue826", "\u39cf", "\u39df", "\u3a73", "\u39d0", "\ue82b", "\ue82c", "\u3b4e", "\u3c6e", "\u3ce0", "\u2ea7", "\ue831", "\ue832", "\u2eaa", "\u4056", "\u415f", "\u2eae", "\u4337", "\u2eb3", "\u2eb6", "\u2eb7", "\ue83b", "\u43b1", "\u43ac", "\u2ebb", "\u43dd", "\u44d6", "\u4661", "\u464c", "\ue843", "\u4723", "\u4729", "\u477c", "\u478d", "\u2eca", "\u4947", "\u497a", "\u497d", "\u4982", "\u4983", "\u4985", "\u4986", "\u499f", "\u499b", "\u49b7", "\u49b6", "\ue854", "\ue855", "\u4ca3", "\u4c9f", "\u4ca0", "\u4ca1", "\u4c77", "\u4ca2", "\u4d13", "\u4dae", "\ue864", "\ue468", "\ufe50", "\ufe51", "\ufe52", "\u2574", "\ufe5a", "\ufe5b", "\ufe5c", "\ufe5d", "\ufe5e", "\u02cd", "\ufe4a", "\ufe4e", "\ufe4b", "\ufe4c", "\ufe5f", "\ufe60", "\ufe61", "\u515e", "\u5161", "\u74e9", "\u258f", "\u258e", "\u258d", "\u258b", "\u258a", "\u2589", "\u256d", "\u256e", "\u2570", "\u256f", "\u2571", "\u2572", "\u2573", "\u3110", "\u4f15", "\u6c4d", "\u6c4e", "\u4f48", "\u56ea", "\u8c9d", "\u8eca", "\u91c6", "\u52bb", "\u59c5", "\u5ca1", "\u73a8", "\u73a5", "\u7cfe", "\u8ecb", "\u4fb7", "\u5e25", "\u5e1f", "\u6046", "\u70a4", "\u7d02", "\u7d05", "\u7d09", "\u7d07", "\u7d04", "\u7d06", "\u8a03", "\u8c9e", "\u8ca0", "\u8ecd", "\u8ecc", "\u9582", "\u97cb", "\u9801", "\u5006", "\u5000", "\u5009", "\u54e1", "\u5cfd", "\u5cf6", "\u5cf4", "\u6649", "\u6645", "\u70cf", "\u7950", "\u7d17", "\u7d14", "\u7d10", "\u7d15", "\u7d1c", "\u7d19", "\u7d1b", "\u8a10", "\u8a0e", "\u8a0c", "\u8a15", "\u8a17", "\u8a13", "\u8a16", "\u8a0f", "\u8a11", "\u8ca1", "\u8ca2", "\u8ed2", "\u8ed4", "\u91d8", "\u91d7", "\u91d9", "\u9583", "\u98e2", "\u99ac", "\u9b25", "\u506f", "\u5d22", "\u5d11", "\u5e36", "\u5e33", "\u5f37", "\u687f", "\u68c4", "\u689f", "\u68a1", "\u6bba", "\u6dbc", "\u7522", "\u7562", "\u7d46", "\u7d43", "\u7d39", "\u7d3c", "\u7d40", "\u7d33", "\u7d32", "\u7d31", "\u7f3d", "\u7fd2", "\u8123", "\u8129", "\u8124", "\u83a2", "\u83a7", "\u8853", "\u889e", "\u8993", "\u8a2a", "\u8a1d", "\u8a23", "\u8a25", "\u8a1f", "\u8a1b", "\u8a22", "\u8ca9", "\u8cac", "\u8cab", "\u8ca8", "\u8caa", "\u8ca7", "\u8edb", "\u8edf", "\u91f5", "\u91e3", "\u91e7", "\u91ed", "\u91e9", "\u9670", "\u9803", "\u9b5a", "\u9ce5", "\u9e75", "\u9ea5", "\u50a2", "\u5091", "\u5096", "\u5098", "\u509a", "\u5274", "\u5275", "\u52de", "\u52dd", "\u52db", "\u55aa", "\u55ac", "\u55ab", "\u582f", "\u5aa7", "\u5d50", "\u5ec1", "\u5ec2", "\u5ec4", "\u6112", "\u63da", "\u68df", "\u68e7", "\u6bbc", "\u6e67", "\u6e4a", "\u6e3e", "\u6e63", "\u6e72", "\u6e69", "\u711c", "\u743a", "\u774f", "\u7d5e", "\u7d68", "\u7d72", "\u7d61", "\u7d62", "\u7d70", "\u7d73", "\u83f4", "\u8a60", "\u8a55", "\u8a5e", "\u8a3c", "\u8a41", "\u8a54", "\u8a5b", "\u8a50", "\u8a46", "\u8a3a", "\u8a36", "\u8a56", "\u8caf", "\u8cbc", "\u8cb3", "\u8cbd", "\u8cc1", "\u8cbb", "\u8cc0", "\u8cb4", "\u8cb7", "\u8cb6", "\u8cbf", "\u8cb8", "\u8efb", "\u8ef8", "\u8efc", "\u9109", "\u9214", "\u9215", "\u9223", "\u9209", "\u921e", "\u920d", "\u9210", "\u9207", "\u9211", "\u9594", "\u958f", "\u9591", "\u9592", "\u958e", "\u967d", "\u9684", "\u97cc", "\u98ea", "\u98ef", "\u98f2", "\u98ed", "\u99ae", "\u99ad", "\u9ec3", "\u4e82", "\u50b5", "\u50c5", "\u50be", "\u50b7", "\u50af", "\u50c7", "\u5277", "\u52e6", "\u55da", "\u5713", "\u585a", "\u584a", "\u5862", "\u584b", "\u5967", "\u5abd", "\u5abc", "\u6144", "\u613e", "\u6134", "\u6137", "\u6436", "\u6416", "\u6417", "\u6975", "\u694a", "\u6953", "\u6b72", "\u6e96", "\u7159", "\u716c", "\u7156", "\u7345", "\u787f", "\u797f", "\u842c", "\u7bc0", "\u7b67", "\u7d79", "\u7d91", "\u7d8f", "\u7d5b", "\u8466", "\u8435", "\u899c", "\u8a6b", "\u8a73", "\u8a69", "\u8a70", "\u8a87", "\u8a7c", "\u8a63", "\u8aa0", "\u8a85", "\u8a6d", "\u8a6e", "\u8a6c", "\u8a7b", "\u8a68", "\u8cca", "\u8cc8", "\u8cc4", "\u8cb2", "\u8cc3", "\u8cc2", "\u8cc5", "\u8f03", "\u8efe", "\u8f0a", "\u904a", "\u9112", "\u9117", "\u9237", "\u9257", "\u9238", "\u923d", "\u9240", "\u923e", "\u925b", "\u924b", "\u9264", "\u9251", "\u9234", "\u9249", "\u924d", "\u9245", "\u9239", "\u923f", "\u925a", "\u9598", "\u9811", "\u9813", "\u980a", "\u9812", "\u980c", "\u98fc", "\u98f4", "\u98fd", "\u98fe", "\u99b3", "\u99b1", "\u99b4", "\u9ce9", "\u50e5", "\u50d5", "\u50d1", "\u50ce", "\u5331", "\u5617", "\u5614", "\u5616", "\u5718", "\u5875", "\u5879", "\u587d", "\u58fd", "\u596a", "\u5969", "\u5d84", "\u5d87", "\u5e57", "\u5f46", "\u615a", "\u6158", "\u6451", "\u66a2", "\u69a6", "\u69c3", "\u69a3", "\u6efe", "\u6eff", "\u6eef", "\u6f38", "\u6eec", "\u6f01", "\u7296", "\u7344", "\u7464", "\u7463", "\u746a", "\u78a9", "\u7b8b", "\u7b87", "\u7dbb", "\u7db0", "\u7d9c", "\u7dbd", "\u7dbe", "\u7da0", "\u7dca", "\u7db4", "\u7dba", "\u7da2", "\u7dbf", "\u7db5", "\u7db8", "\u7dad", "\u7dd2", "\u7dc7", "\u7dac", "\u805e", "\u81fa", "\u8490", "\u88ef", "\u8aa6", "\u8a8c", "\u8aa3", "\u8aa1", "\u8aa5", "\u8aa8", "\u8a98", "\u8a91", "\u8a9a", "\u8aa7", "\u8cd3", "\u8cd1", "\u8cd2", "\u8d99", "\u8f12", "\u8f15", "\u8f13", "\u905d", "\u9118", "\u9278", "\u9280", "\u9285", "\u9298", "\u9296", "\u927b", "\u9293", "\u929c", "\u927c", "\u9291", "\u95a1", "\u95a8", "\u95a9", "\u95a3", "\u95a5", "\u95a4", "\u9817", "\u98af", "\u98b1", "\u9903", "\u9905", "\u990c", "\u9909", "\u99c1", "\u9aaf", "\u9cf4", "\u9cf6", "\u9cf3", "\u9f4a", "\u5104", "\u5100", "\u50f9", "\u5102", "\u5105", "\u528d", "\u528a", "\u53b2", "\u5653", "\u58b3", "\u58ae", "\u58a6", "\u596d", "\u5afb", "\u5b0b", "\u5af5", "\u5b0c", "\u5b08", "\u5bec", "\u5d94", "\u5ee2", "\u5edf", "\u5edd", "\u5ee0", "\u5f48", "\u616e", "\u6182", "\u617c", "\u616b", "\u617e", "\u6190", "\u619a", "\u61a4", "\u61ae", "\u646f", "\u6490", "\u64a2", "\u66b1", "\u69e8", "\u6a01", "\u6a1e", "\u6a13", "\u6a02", "\u6a05", "\u6a11", "\u6b50", "\u6b4e", "\u6ba4", "\u6f51", "\u6f54", "\u6f97", "\u71b1", "\u729b", "\u7469", "\u76ba", "\u76e4", "\u7787", "\u778b", "\u7aaf", "\u7de0", "\u7df4", "\u7def", "\u7dd8", "\u7dec", "\u7ddd", "\u7de3", "\u7dde", "\u7d9e", "\u7dd9", "\u7df2", "\u7df9", "\u81a0", "\u8523", "\u8525", "\u8506", "\u8768", "\u885b", "\u8915", "\u8abc", "\u8ad2", "\u8ac7", "\u8ac4", "\u8a95", "\u8af8", "\u8ab2", "\u8ac9", "\u8ac2", "\u8ab0", "\u8acd", "\u8ab6", "\u8ab9", "\u8adb", "\u8c4e", "\u8ce0", "\u8cde", "\u8ce6", "\u8ce4", "\u8cec", "\u8ce2", "\u8ce3", "\u8cdc", "\u8cea", "\u8ce1", "\u8f1d", "\u8f1b", "\u8f1f", "\u8f29", "\u8f26", "\u8f1c", "\u8f1e", "\u8f25", "\u9077", "\u912d", "\u9127", "\u9183", "\u92c5", "\u92bb", "\u92b7", "\u92ea", "\u92ac", "\u92e4", "\u92c1", "\u92b3", "\u92bc", "\u92d2", "\u92c7", "\u92f0", "\u92b2", "\u95ad", "\u95b1", "\u9821", "\u982b", "\u981c", "\u98b3", "\u990a", "\u9913", "\u9912", "\u9918", "\u99dd", "\u99d0", "\u99df", "\u99db", "\u99d1", "\u99d5", "\u99d2", "\u9b27", "\u9b77", "\u9b6f", "\u9d06", "\u9d09", "\u9d03", "\u5118", "\u5114", "\u5110", "\u5115", "\u51aa", "\u52f3", "\u58c7", "\u596e", "\u5b1d", "\u5f4a", "\u61b2", "\u6191", "\u618a", "\u61cd", "\u64cb", "\u66c6", "\u66c9", "\u66c4", "\u66c7", "\u6a38", "\u6a3a", "\u6a6b", "\u6a39", "\u6a4b", "\u6b77", "\u6fb1", "\u6fa4", "\u6fa6", "\u71be", "\u71c9", "\u71d0", "\u71d2", "\u71c8", "\u71d9", "\u71dc", "\u7368", "\u74a3", "\u7498", "\u750c", "\u76e7", "\u779e", "\u79a6", "\u7a4d", "\u7a4e", "\u7a4c", "\u7a4b", "\u7aba", "\u7c11", "\u7e0a", "\u7e11", "\u7e08", "\u7e1b", "\u7e23", "\u7e1e", "\u7e1d", "\u7e09", "\u7e10", "\u8208", "\u856d", "\u856a", "\u879e", "\u87a2", "\u89aa", "\u89a6", "\u8ae6", "\u8afa", "\u8aeb", "\u8af1", "\u8b00", "\u8adc", "\u8ae7", "\u8aee", "\u8afe", "\u8b01", "\u8b02", "\u8af7", "\u8aed", "\u8af3", "\u8af6", "\u8afc", "\u8c6d", "\u8c93", "\u8cf4", "\u8f3b", "\u8f33", "\u9072", "\u907c", "\u907a", "\u9134", "\u9320", "\u9336", "\u92f8", "\u9333", "\u9322", "\u92fc", "\u932b", "\u931a", "\u9310", "\u9326", "\u9321", "\u9315", "\u932e", "\u9319", "\u95bb", "\u96aa", "\u9830", "\u9838", "\u9837", "\u9839", "\u9824", "\u9928", "\u991e", "\u991b", "\u9921", "\u991a", "\u99ed", "\u99e2", "\u99f1", "\u9b28", "\u9b91", "\u9d15", "\u9d23", "\u9d26", "\u9d28", "\u9d12", "\u9d1b", "\u512a", "\u511f", "\u52f5", "\u5680", "\u58ce", "\u5b30", "\u5b2a", "\u5b24", "\u5c68", "\u5dbc", "\u5dba", "\u5dbd", "\u5e6b", "\u5f4c", "\u61c7", "\u64ca", "\u64f0", "\u64ec", "\u64f1", "\u64ed", "\u6582", "\u6583", "\u66d6", "\u6a9c", "\u6adb", "\u6aa3", "\u6b5c", "\u6bae", "\u6fd8", "\u6ff1", "\u6fdb", "\u6feb", "\u6f80", "\u6fec", "\u6fe9", "\u6fd5", "\u71df", "\u71ed", "\u71ec", "\u71f4", "\u7246", "\u74a6", "\u7646", "\u76ea", "\u78ef", "\u79aa", "\u7ce2", "\u7e3e", "\u7e46", "\u7e37", "\u7e32", "\u7e43", "\u7e2b", "\u7e31", "\u7e45", "\u7e34", "\u7e39", "\u7e35", "\u7e3f", "\u7e2f", "\u8070", "\u8073", "\u8591", "\u8594", "\u858a", "\u8667", "\u893b", "\u893d", "\u89ac", "\u8b0e", "\u8b17", "\u8b19", "\u8b1b", "\u8b0a", "\u8b20", "\u8b04", "\u8b10", "\u8c3f", "\u8cfa", "\u8cfd", "\u8cfc", "\u8cf8", "\u8cfb", "\u8da8", "\u8f44", "\u8f3e", "\u8f42", "\u8f3f", "\u919e", "\u934d", "\u9382", "\u9328", "\u9365", "\u934b", "\u9318", "\u937e", "\u935b", "\u9370", "\u935a", "\u9354", "\u95ca", "\u95cb", "\u95c8", "\u95c6", "\u97d3", "\u9846", "\u98b6", "\u9935", "\u9a01", "\u99ff", "\u9bae", "\u9bab", "\u9baa", "\u9bad", "\u9d3b", "\u9d3f", "\u9f4b", "\u5695", "\u56ae", "\u58d9", "\u58d8", "\u61e3", "\u64f4", "\u64f2", "\u64fe", "\u6506", "\u64fa", "\u64fb", "\u6ab3", "\u6ac3", "\u6abb", "\u6ab8", "\u6ac2", "\u6aae", "\u6aaf", "\u6b5f", "\u6baf", "\u7009", "\u700b", "\u6ffe", "\u7006", "\u6ffa", "\u700f", "\u71fb", "\u71fc", "\u71fe", "\u71f8", "\u7377", "\u7375", "\u74bf", "\u7658", "\u7652", "\u790e", "\u79ae", "\u7a61", "\u7a62", "\u7a60", "\u7ac4", "\u7ac5", "\u7c1e", "\u7c23", "\u7c21", "\u7ce7", "\u7e54", "\u7e55", "\u7e5a", "\u7e61", "\u7e52", "\u7e59", "\u7f48", "\u7ff9", "\u8077", "\u8076", "\u81cf", "\u85cd", "\u87f2", "\u89b2", "\u8b28", "\u8b39", "\u8b2c", "\u8b2b", "\u8c50", "\u8d05", "\u8e63", "\u8e64", "\u8e5f", "\u8e55", "\u8ec0", "\u8f4d", "\u9394", "\u938a", "\u9396", "\u93a2", "\u93b3", "\u93ae", "\u93b0", "\u9398", "\u939a", "\u9397", "\u95d4", "\u95d6", "\u95d0", "\u95d5", "\u96e2", "\u96dc", "\u96db", "\u96de", "\u9724", "\u97a6", "\u97f9", "\u984d", "\u984f", "\u9853", "\u98ba", "\u993e", "\u993f", "\u993d", "\u9a0e", "\u9bca", "\u9bc9", "\u9bfd", "\u9bc8", "\u9bc0", "\u9d51", "\u9d5d", "\u9d60", "\u5133", "\u56a5", "\u58de", "\u58df", "\u58e2", "\u5bf5", "\u9f90", "\u5eec", "\u61f2", "\u61f7", "\u650f", "\u66e0", "\u6ae5", "\u6add", "\u6ada", "\u6ad3", "\u701f", "\u7028", "\u701d", "\u7015", "\u7018", "\u720d", "\u72a2", "\u7378", "\u737a", "\u74bd", "\u74ca", "\u77c7", "\u7919", "\u79b1", "\u7a6b", "\u7c3e", "\u7c3d", "\u7c37", "\u7e6b", "\u7e6d", "\u7e79", "\u7e69", "\u7e6a", "\u7f85", "\u7e73", "\u7fb6", "\u81d8", "\u85f7", "\u8805", "\u880d", "\u8956", "\u8b41", "\u8b5c", "\u8b49", "\u8b5a", "\u8b4e", "\u8b4f", "\u8b59", "\u8d08", "\u8d0a", "\u8e7a", "\u8f54", "\u8f4e", "\u93e1", "\u93d1", "\u93df", "\u93c3", "\u93c8", "\u93dc", "\u93dd", "\u93e2", "\u93d8", "\u93e4", "\u93e8", "\u96e3", "\u9727", "\u97dc", "\u97fb", "\u9858", "\u98bc", "\u9945", "\u9949", "\u9a16", "\u9a19", "\u9b0d", "\u9be8", "\u9be7", "\u9bd6", "\u9bdb", "\u9d89", "\u9d61", "\u9d72", "\u9d6a", "\u9d6c", "\u9e97", "\u52f8", "\u56a8", "\u56b6", "\u56b4", "\u5b43", "\u5bf6", "\u5dc9", "\u61f8", "\u61fa", "\u6514", "\u6aec", "\u703e", "\u7030", "\u7032", "\u7210", "\u737b", "\u74cf", "\u7665", "\u7926", "\u792a", "\u792c", "\u792b", "\u7ac7", "\u7af6", "\u7c4c", "\u7e7d", "\u7e7c", "\u7f4c", "\u81da", "\u8266", "\u860b", "\u8607", "\u860a", "\u8964", "\u89f8", "\u8b5f", "\u8b6b", "\u8d0f", "\u8d0d", "\u8e89", "\u9403", "\u93fd", "\u95e1", "\u98c4", "\u9952", "\u9951", "\u9a2b", "\u9a30", "\u9a37", "\u9a35", "\u9c13", "\u9c0d", "\u9e79", "\u9f5f", "\u9f63", "\u9f61", "\u5137", "\u5138", "\u56c1", "\u56c0", "\u56c2", "\u61fc", "\u61fe", "\u651d", "\u651c", "\u6afb", "\u6afa", "\u6bb2", "\u72a7", "\u74d6", "\u74d4", "\u7669", "\u77d3", "\u7c50", "\u7e8f", "\u7e8c", "\u862d", "\u861a", "\u881f", "\u896a", "\u896c", "\u89bd", "\u8b74", "\u8b77", "\u8b7d", "\u8d13", "\u8e8a", "\u8e8d", "\u8e8b", "\u8f5f", "\u942e", "\u9433", "\u9435", "\u943a", "\u9438", "\u9432", "\u942b", "\u95e2", "\u97ff", "\u9867", "\u9865", "\u9957", "\u9a45", "\u9a43", "\u9a40", "\u9a3e", "\u9c2d", "\u9c25", "\u9daf", "\u9db4", "\u9dc2", "\u9db8", "\u9f5c", "\u9f66", "\u9f67", "\u513c", "\u513b", "\u56c8", "\u56c9", "\u5dd4", "\u5dd2", "\u5f4e", "\u6b61", "\u7051", "\u7058", "\u7380", "\u7c60", "\u7c5f", "\u81df", "\u8972", "\u896f", "\u89fc", "\u8d16", "\u8d17", "\u8f61", "\u9444", "\u9451", "\u9452", "\u97c3", "\u97c1", "\u986b", "\u9a55", "\u9a4d", "\u9b1a", "\u9c49", "\u9c31", "\u9c3e", "\u9c3b", "\u9dd3", "\u9dd7", "\u9f34", "\u9f6c", "\u9f6a", "\u9f94", "\u56cc", "\u5dd6", "\u652a", "\u66ec", "\u6b10", "\u74da", "\u7aca", "\u7c63", "\u7c65", "\u7e93", "\u7e96", "\u7e94", "\u81e2", "\u8831", "\u9090", "\u9463", "\u9460", "\u9464", "\u995c", "\u9a5b", "\u9c54", "\u9c57", "\u9c56", "\u9de5", "\u9ef4", "\u56d1", "\u58e9", "\u7671", "\u7672", "\u7f88", "\u8836", "\u8b92", "\u8b96", "\u8d1b", "\u91c0", "\u946a", "\u9742", "\u9748", "\u9744", "\u97c6", "\u9870", "\u9a5f", "\u9b58", "\u9c5f", "\u9df9", "\u9dfa", "\u9e7c", "\u9e7d", "\u9f07", "\u9f77", "\u9f72", "\u5ef3", "\u6b16", "\u7c6c", "\u7c6e", "\u89c0", "\u8ea1", "\u91c1", "\u9472", "\u9871", "\u995e", "\u7064", "\u8b9a", "\u9477", "\u97c9", "\u9a62", "\u9a65", "\u8b9c", "\u8eaa", "\u91c5", "\u947d", "\u947e", "\u947c", "\u9c77", "\u9c78", "\u9ef7", "\u8c54", "\u947f", "\u9e1a", "\u9a6a", "\u9e1b", "\u9e1e", "\u7c72", "\u5c74", "\u5c73", "\u79b8", "\u4f14", "\u4f08", "\u4f05", "\u4f13", "\u4f04", "\u625e", "\u6261", "\u6262", "\u6260", "\u6c4f", "\u6c4c", "\u9624", "\u4f49", "\u4f41", "\u4f3f", "\u56e7", "\u5c86", "\u623a", "\u628c", "\u628e", "\u628f", "\u6759", "\u675a", "\u6c6f", "\u6c6d", "\u72bf", "\u72bd", "\u8090", "\u8092", "\u9628", "\u4f4c", "\u5246", "\u52bc", "\u5392", "\u5394", "\u546b", "\u546c", "\u546f", "\u5461", "\u5460", "\u590c", "\u59b5", "\u59c1", "\u59b6", "\u59c3", "\u59c0", "\u59b4", "\u5ca0", "\u5ca8", "\u5c9f", "\u5ca7", "\u5ca5", "\u5ca6", "\u6032", "\u6034", "\u6033", "\u65fc", "\u65fd", "\u6bde", "\u73a4", "\u73a6", "\u74e8", "\u7cfd", "\u808f", "\u8fcb", "\u8fcd", "\u4fd3", "\u4fb2", "\u4fd4", "\u4fbb", "\u4fb3", "\u4fd6", "\u4fba", "\u4fb9", "\u5249", "\u5470", "\u5797", "\u5798", "\u578f", "\u5799", "\u579a", "\u5795", "\u59e1", "\u59ee", "\u59f1", "\u59f6", "\u59f2", "\u59f7", "\u59f3", "\u59f5", "\u59e0", "\u59f4", "\u5cd0", "\u5cd8", "\u5cd7", "\u5cdb", "\u5cde", "\u5cc9", "\u5cc7", "\u5cca", "\u5cd6", "\u5cd4", "\u5ccf", "\u5cc8", "\u5cc6", "\u5cce", "\u5cdf", "\u5cf8", "\u5df9", "\u5e21", "\u5e22", "\u5e23", "\u5e20", "\u5e24", "\u5eb0", "\u6037", "\u6039", "\u6045", "\u6047", "\u6049", "\u6541", "\u6543", "\u663a", "\u6639", "\u67c8", "\u67ba", "\u67bb", "\u67f8", "\u67c0", "\u67cd", "\u67f7", "\u67f6", "\u67ce", "\u67fc", "\u67c6", "\u67cc", "\u67fa", "\u67c9", "\u67ca", "\u67cb", "\u6be0", "\u6d20", "\u6d22", "\u709f", "\u70a1", "\u70a9", "\u7241", "\u72e4", "\u72e6", "\u72e3", "\u73c5", "\u73c7", "\u73c6", "\u74ec", "\u75a7", "\u75aa", "\u7806", "\u7805", "\u794c", "\u794b", "\u7ad1", "\u7c7a", "\u7c78", "\u7c79", "\u7c7f", "\u7c80", "\u7c81", "\u7d03", "\u7d08", "\u7d01", "\u7f91", "\u80d1", "\u80c8", "\u80d0", "\u80ca", "\u80d5", "\u80c9", "\u82fe", "\u8300", "\u8677", "\u8674", "\u8673", "\u8a04", "\u91d4", "\u91d3", "\u5005", "\u5007", "\u5030", "\u5033", "\u5037", "\u5035", "\u5031", "\u54e2", "\u5517", "\u54e4", "\u551a", "\u54f7", "\u54f8", "\u550e", "\u550b", "\u57ba", "\u57c6", "\u57bd", "\u57bc", "\u57bf", "\u57c7", "\u57c1", "\u5a2d", "\u5a2e", "\u5cff", "\u5cf7", "\u5d00", "\u5cf9", "\u5e29", "\u5eaa", "\u5eac", "\u5f33", "\u6336", "\u6334", "\u6358", "\u6359", "\u635a", "\u6338", "\u6357", "\u664a", "\u6647", "\u681a", "\u6831", "\u681c", "\u682d", "\u682f", "\u6826", "\u6828", "\u682e", "\u6825", "\u6b2c", "\u6b2d", "\u6b6d", "\u6be6", "\u6be4", "\u6be8", "\u6be3", "\u6be7", "\u6d7f", "\u6d97", "\u6d98", "\u6d7e", "\u6d80", "\u70d3", "\u70d1", "\u70d7", "\u70d2", "\u70d4", "\u70cd", "\u70ce", "\u7242", "\u73d3", "\u73d6", "\u73d4", "\u73d7", "\u73d8", "\u7521", "\u755f", "\u7710", "\u7713", "\u7712", "\u7711", "\u7715", "\u794f", "\u7952", "\u7951", "\u79dc", "\u79de", "\u79dd", "\u7c84", "\u7c8c", "\u7c8d", "\u7c85", "\u7d1e", "\u7d1d", "\u7d0e", "\u7d18", "\u7d16", "\u7d13", "\u7d1f", "\u7d12", "\u7d0f", "\u7d0c", "\u7f96", "\u7f92", "\u8325", "\u8356", "\u8326", "\u8322", "\u834e", "\u834d", "\u8324", "\u8320", "\u834c", "\u831e", "\u834b", "\u86a2", "\u8691", "\u8687", "\u8697", "\u8686", "\u869a", "\u8685", "\u8699", "\u86a1", "\u8698", "\u8690", "\u8a12", "\u8ca4", "\u8ca3", "\u8ed1", "\u8ed3", "\u91d5", "\u91e2", "\u91da", "\u98e3", "\u5070", "\u506a", "\u5061", "\u505e", "\u5060", "\u5053", "\u5072", "\u5062", "\u505f", "\u5069", "\u506b", "\u5063", "\u5064", "\u506e", "\u5073", "\u5051", "\u554d", "\u550c", "\u554e", "\u57ec", "\u57e7", "\u57e9", "\u595c", "\u5a60", "\u5a5e", "\u5a38", "\u5a6d", "\u5a50", "\u5a5f", "\u5a6c", "\u5a53", "\u5a43", "\u5a5d", "\u5a52", "\u5a44", "\u5a8e", "\u5a4d", "\u5a39", "\u5a4c", "\u5a70", "\u5a51", "\u5a42", "\u5a5c", "\u5d0b", "\u5d20", "\u5d0c", "\u5d0d", "\u5d30", "\u5d12", "\u5d23", "\u5e34", "\u5eb1", "\u5eb2", "\u5f36", "\u5f38", "\u60be", "\u60cf", "\u60e4", "\u60bf", "\u60c3", "\u60cd", "\u60c0", "\u639e", "\u639d", "\u639c", "\u639f", "\u6879", "\u689c", "\u686d", "\u686e", "\u686f", "\u687c", "\u6872", "\u6880", "\u6871", "\u687e", "\u689b", "\u688b", "\u68a0", "\u6889", "\u687b", "\u688c", "\u688a", "\u687d", "\u6e74", "\u6e00", "\u6dbe", "\u6dbd", "\u6dba", "\u6dbb", "\u710d", "\u70f4", "\u710c", "\u7104", "\u70f3", "\u70ff", "\u7106", "\u7100", "\u70f6", "\u7102", "\u710e", "\u7307", "\u7308", "\u73f6", "\u73f5", "\u7401", "\u73fd", "\u7400", "\u73fa", "\u73fc", "\u73ff", "\u73f4", "\u7564", "\u7563", "\u7731", "\u7732", "\u7734", "\u7733", "\u79f6", "\u79f7", "\u7d35", "\u7d3d", "\u7d38", "\u7d36", "\u7d3a", "\u7d45", "\u7d41", "\u7d47", "\u7d3e", "\u7d3f", "\u7d4a", "\u7d3b", "\u7fd0", "\u7fd1", "\u8125", "\u8121", "\u8127", "\u8122", "\u83a3", "\u8373", "\u83a4", "\u8374", "\u8381", "\u8375", "\u8383", "\u83a5", "\u837f", "\u83a6", "\u8376", "\u8659", "\u8656", "\u86bf", "\u86bc", "\u86bd", "\u86be", "\u8852", "\u88a8", "\u88aa", "\u889a", "\u88a1", "\u889f", "\u8898", "\u88a7", "\u8899", "\u889b", "\u8a30", "\u8a27", "\u8a2c", "\u8c39", "\u8c3b", "\u8c5c", "\u8c5d", "\u8c7d", "\u8ca5", "\u8d7d", "\u8d7b", "\u8d79", "\u8ed8", "\u8ede", "\u8edd", "\u8edc", "\u8ed7", "\u8ee0", "\u8ee1", "\u91ec", "\u91f4", "\u91f1", "\u91f3", "\u91f8", "\u91e4", "\u91f9", "\u91ea", "\u91eb", "\u91f7", "\u91e8", "\u91ee", "\u957a", "\u9586", "\u9588", "\u967c", "\u9671", "\u966f", "\u9804", "\u509b", "\u5095", "\u5094", "\u509e", "\u509d", "\u5068", "\u509c", "\u5092", "\u515f", "\u51d4", "\u55a5", "\u55ad", "\u5645", "\u55a2", "\u55a3", "\u55a4", "\u55a6", "\u55a1", "\u570c", "\u5829", "\u5837", "\u5827", "\u5828", "\u5848", "\u583f", "\u582e", "\u5839", "\u5838", "\u582d", "\u582c", "\u583b", "\u5aaf", "\u5a94", "\u5a9f", "\u5aa2", "\u5a9e", "\u5aa6", "\u5aa5", "\u5a95", "\u5aae", "\u5a84", "\u5a8a", "\u5a97", "\u5a83", "\u5a8b", "\u5aa9", "\u5a8c", "\u5a8f", "\u5a9d", "\u5bea", "\u5d37", "\u5d43", "\u5d41", "\u5d51", "\u5d4e", "\u5d55", "\u5d33", "\u5d3a", "\u5d52", "\u5d31", "\u5d42", "\u5d39", "\u5d38", "\u5d3c", "\u5d32", "\u5d36", "\u5d40", "\u5d45", "\u5fa6", "\u5fa5", "\u60e2", "\u60ce", "\u60c4", "\u6114", "\u6113", "\u60fc", "\u60fe", "\u60c1", "\u60ff", "\u63e5", "\u63e8", "\u6461", "\u63dd", "\u63dc", "\u63d8", "\u63d9", "\u666c", "\u666a", "\u68dc", "\u692a", "\u68ec", "\u68ea", "\u68eb", "\u6907", "\u6908", "\u68c6", "\u6914", "\u68e8", "\u690a", "\u6917", "\u68c8", "\u68dd", "\u68de", "\u68e6", "\u68e9", "\u6915", "\u68c7", "\u6bbd", "\u6e46", "\u6e47", "\u6e49", "\u6e3c", "\u6e3d", "\u6e62", "\u6e3f", "\u6e41", "\u6e73", "\u6e4b", "\u6e40", "\u6e03", "\u6e68", "\u6e61", "\u6e71", "\u6e65", "\u6e78", "\u6e64", "\u6e77", "\u6e79", "\u6e66", "\u7120", "\u711e", "\u712e", "\u7123", "\u7125", "\u7122", "\u711f", "\u7128", "\u713a", "\u7288", "\u7289", "\u7286", "\u7416", "\u7421", "\u741d", "\u7420", "\u74fb", "\u756f", "\u756c", "\u774d", "\u774a", "\u774e", "\u774b", "\u774c", "\u77de", "\u7860", "\u7864", "\u7865", "\u7871", "\u7870", "\u7869", "\u7868", "\u7862", "\u7974", "\u7973", "\u7972", "\u7b44", "\u7b40", "\u7d58", "\u7d63", "\u7d53", "\u7d56", "\u7d67", "\u7d6a", "\u7d4f", "\u7d6d", "\u7d5c", "\u7d6b", "\u7d52", "\u7d54", "\u7d69", "\u7d51", "\u7d5f", "\u7d4e", "\u7f3e", "\u7f3f", "\u7f65", "\u7f66", "\u80d4", "\u8143", "\u813d", "\u813a", "\u81f7", "\u81f8", "\u81f9", "\u8423", "\u83f6", "\u83f5", "\u8413", "\u8848", "\u88b6", "\u8995", "\u8998", "\u8997", "\u8a4e", "\u8a4d", "\u8a39", "\u8a59", "\u8a40", "\u8a57", "\u8a58", "\u8a44", "\u8a45", "\u8a52", "\u8a51", "\u8a4a", "\u8a4c", "\u8a4f", "\u8c5f", "\u8c81", "\u8c80", "\u8cba", "\u8cbe", "\u8cb0", "\u8cb9", "\u8cb5", "\u8d80", "\u8eef", "\u8ef7", "\u8efa", "\u8ef9", "\u8ee6", "\u8eee", "\u8ef5", "\u8ee7", "\u8ee8", "\u8ef6", "\u8eeb", "\u8ef1", "\u8eec", "\u8ef4", "\u8ee9", "\u9034", "\u9106", "\u912c", "\u9108", "\u9107", "\u9201", "\u920a", "\u9203", "\u921a", "\u9226", "\u920f", "\u920c", "\u9200", "\u9212", "\u91ff", "\u91fd", "\u9206", "\u9204", "\u9227", "\u9202", "\u921c", "\u9224", "\u9219", "\u9217", "\u9205", "\u9216", "\u957b", "\u958d", "\u958c", "\u9590", "\u967e", "\u9683", "\u9680", "\u976c", "\u9770", "\u976e", "\u9807", "\u98a9", "\u98eb", "\u9ce6", "\u4e83", "\u4e84", "\u50bf", "\u50c6", "\u50ae", "\u50c4", "\u50ca", "\u50b4", "\u50c8", "\u50c2", "\u50b0", "\u50c1", "\u50b1", "\u50cb", "\u50c9", "\u50b6", "\u50b8", "\u51d7", "\u527a", "\u5278", "\u527b", "\u527c", "\u55c3", "\u55db", "\u55c0", "\u55d9", "\u55c2", "\u5714", "\u5868", "\u5864", "\u5849", "\u586f", "\u585d", "\u585b", "\u583d", "\u5863", "\u5871", "\u58fc", "\u5ac7", "\u5ac4", "\u5aba", "\u5ab1", "\u5ab0", "\u5ac8", "\u5abb", "\u5ac6", "\u5a90", "\u5bd6", "\u5bd8", "\u5bd9", "\u5d63", "\u5d65", "\u5d68", "\u5d67", "\u5d62", "\u5e4f", "\u5e4e", "\u5e4a", "\u5e4b", "\u5ec5", "\u5ecc", "\u6145", "\u6136", "\u6132", "\u612e", "\u6146", "\u612f", "\u6409", "\u6433", "\u6418", "\u6439", "\u6437", "\u6430", "\u642f", "\u640a", "\u641a", "\u63e7", "\u6699", "\u694e", "\u6945", "\u6948", "\u6949", "\u6944", "\u6976", "\u6974", "\u694c", "\u694b", "\u694f", "\u6951", "\u6952", "\u6e93", "\u6e94", "\u6e92", "\u6e8e", "\u6e8d", "\u6e97", "\u7154", "\u7152", "\u7163", "\u7160", "\u7141", "\u7162", "\u716a", "\u7161", "\u7142", "\u7158", "\u7143", "\u7150", "\u7153", "\u7144", "\u715a", "\u7342", "\u7444", "\u744a", "\u744b", "\u7452", "\u7451", "\u744f", "\u7450", "\u7446", "\u744d", "\u7454", "\u74fe", "\u74fd", "\u7755", "\u7756", "\u7754", "\u7759", "\u77e0", "\u7883", "\u7880", "\u797c", "\u797d", "\u7a11", "\u7a12", "\u7a13", "\u7a10", "\u7aeb", "\u7b66", "\u7b64", "\u7b6d", "\u7b69", "\u7b65", "\u7d88", "\u7d86", "\u7d80", "\u7d8d", "\u7d7f", "\u7d85", "\u7d7a", "\u7d8e", "\u7d7b", "\u7d83", "\u7d7c", "\u7d8c", "\u7d94", "\u7d84", "\u7d7d", "\u7d92", "\u7f67", "\u7fdb", "\u7fdc", "\u815c", "\u6721", "\u815e", "\u8144", "\u843f", "\u8456", "\u8465", "\u8440", "\u8467", "\u8430", "\u844d", "\u8507", "\u8437", "\u8434", "\u8443", "\u8445", "\u844b", "\u842f", "\u8442", "\u842d", "\u844e", "\u844c", "\u8436", "\u8433", "\u8468", "\u847e", "\u8444", "\u842b", "\u8454", "\u8450", "\u88de", "\u88db", "\u899b", "\u8a76", "\u8a86", "\u8a7f", "\u8a61", "\u8a77", "\u8a82", "\u8a84", "\u8a75", "\u8a83", "\u8a74", "\u8c3c", "\u8c65", "\u8c64", "\u8c66", "\u8ccc", "\u8d8e", "\u8d8f", "\u8d8d", "\u8d90", "\u8f06", "\u8eff", "\u8f01", "\u8f00", "\u8f05", "\u8f07", "\u8f08", "\u8f02", "\u8f0b", "\u9049", "\u9110", "\u910d", "\u910f", "\u9111", "\u9116", "\u9114", "\u910b", "\u910e", "\u9248", "\u9252", "\u9230", "\u923a", "\u9266", "\u9233", "\u9265", "\u925e", "\u9283", "\u922e", "\u924a", "\u926d", "\u926c", "\u924f", "\u9260", "\u9267", "\u926f", "\u9236", "\u9261", "\u9270", "\u9231", "\u9254", "\u9263", "\u9250", "\u9272", "\u924e", "\u9253", "\u924c", "\u9256", "\u9232", "\u959f", "\u959c", "\u959e", "\u959b", "\u9778", "\u980d", "\u980e", "\u98ac", "\u98f6", "\u98f9", "\u99af", "\u99b2", "\u99b0", "\u99b5", "\u9aad", "\u9aab", "\u9cea", "\u9ced", "\u9ce7", "\u50d4", "\u50dd", "\u50e4", "\u50d3", "\u50e3", "\u50e0", "\u52e9", "\u52eb", "\u5330", "\u5615", "\u5612", "\u55fc", "\u5613", "\u55fa", "\u55f9", "\u587c", "\u5890", "\u5898", "\u5874", "\u587a", "\u5891", "\u588e", "\u5876", "\u587b", "\u588f", "\u58fe", "\u596b", "\u5aee", "\u5aed", "\u5af3", "\u5d80", "\u5d7d", "\u5d86", "\u5d7a", "\u5d81", "\u5d77", "\u5d8a", "\u5d89", "\u5d88", "\u5d7e", "\u5d7c", "\u5d8d", "\u5d79", "\u5d7f", "\u5e58", "\u5e59", "\u5e53", "\u5ece", "\u5f44", "\u5f43", "\u6141", "\u616c", "\u6180", "\u617a", "\u615b", "\u613b", "\u616a", "\u644d", "\u645b", "\u645d", "\u6474", "\u6476", "\u6472", "\u6473", "\u647d", "\u6475", "\u6466", "\u644e", "\u645c", "\u6460", "\u6450", "\u647f", "\u6465", "\u6477", "\u66a1", "\u66a0", "\u669f", "\u6722", "\u69c9", "\u69a0", "\u6991", "\u69c4", "\u69a4", "\u6993", "\u69a1", "\u699e", "\u69d9", "\u6990", "\u69a5", "\u69c6", "\u6b9e", "\u6b9f", "\u6ba0", "\u6efb", "\u6f19", "\u6f1a", "\u6f18", "\u6f3b", "\u6eed", "\u6eee", "\u6f3c", "\u6eeb", "\u6f0e", "\u6efd", "\u6f39", "\u6f1c", "\u6efc", "\u6f3a", "\u6f1f", "\u6f0d", "\u6f1e", "\u7187", "\u7189", "\u7180", "\u7182", "\u7186", "\u7181", "\u7244", "\u7297", "\u7295", "\u7343", "\u7462", "\u7473", "\u7475", "\u7472", "\u7467", "\u757d", "\u76b8", "\u776e", "\u776f", "\u78aa", "\u78ad", "\u787e", "\u78ab", "\u78ac", "\u7998", "\u7996", "\u7995", "\u7994", "\u7997", "\u7a2b", "\u7a4a", "\u7a30", "\u7a2f", "\u7a28", "\u7a26", "\u7b88", "\u7b8a", "\u7b8c", "\u5284", "\u7db7", "\u7dc2", "\u7da3", "\u7daa", "\u7dc1", "\u7dc0", "\u7dc5", "\u7d9d", "\u7dce", "\u7dc4", "\u7dc6", "\u7dcb", "\u7dcc", "\u7db9", "\u7d96", "\u7dbc", "\u7d9f", "\u7da9", "\u7da1", "\u7dc9", "\u7fde", "\u805d", "\u805c", "\u8186", "\u8187", "\u84a4", "\u84ac", "\u84ae", "\u84ab", "\u84aa", "\u84a7", "\u8494", "\u84a9", "\u84a8", "\u84db", "\u8491", "\u876b", "\u8743", "\u8741", "\u8746", "\u8742", "\u88ee", "\u88ec", "\u88eb", "\u899d", "\u89a1", "\u899f", "\u899e", "\u8aab", "\u8a99", "\u8a92", "\u8a8f", "\u8a96", "\u8c3d", "\u8c68", "\u8c69", "\u8cd5", "\u8ccf", "\u8cd7", "\u8d96", "\u8e02", "\u8dff", "\u8e03", "\u8e00", "\u8e04", "\u8f10", "\u8f11", "\u8f0e", "\u8f0d", "\u92a5", "\u92a4", "\u9276", "\u929b", "\u927a", "\u92a0", "\u9294", "\u92aa", "\u928d", "\u92a6", "\u929a", "\u92ab", "\u9279", "\u9297", "\u927f", "\u92a3", "\u92ee", "\u9282", "\u9295", "\u92a2", "\u927d", "\u9288", "\u92a1", "\u928a", "\u928c", "\u9299", "\u92a7", "\u927e", "\u9287", "\u92a9", "\u929d", "\u928b", "\u922d", "\u969e", "\u96a1", "\u977a", "\u977e", "\u9783", "\u9780", "\u9782", "\u977b", "\u9784", "\u9781", "\u977f", "\u97ce", "\u97cd", "\u9816", "\u98ad", "\u98ae", "\u9902", "\u9900", "\u9907", "\u999d", "\u999c", "\u99c3", "\u99b9", "\u99bb", "\u99ba", "\u99c2", "\u99bd", "\u99c7", "\u9b60", "\u9b61", "\u9b5f", "\u9cf1", "\u9cf2", "\u9cf5", "\u50ff", "\u5103", "\u5130", "\u50f8", "\u50fe", "\u50fd", "\u528b", "\u528c", "\u52ef", "\u5648", "\u5642", "\u5641", "\u564a", "\u5649", "\u5646", "\u571a", "\u58ab", "\u58b1", "\u58a3", "\u58af", "\u58ac", "\u58a5", "\u58a1", "\u58ff", "\u5aff", "\u5af4", "\u5afd", "\u5af7", "\u5af6", "\u5b03", "\u5af8", "\u5b02", "\u5af9", "\u5b01", "\u5b07", "\u5b05", "\u5b0f", "\u5d97", "\u5d92", "\u5da2", "\u5d93", "\u5d95", "\u5e69", "\u7df3", "\u5ede", "\u5ee1", "\u5f49", "\u5fb2", "\u6183", "\u6179", "\u61b1", "\u61b0", "\u61a2", "\u6189", "\u619b", "\u6193", "\u61af", "\u619f", "\u6192", "\u61a1", "\u61b3", "\u6470", "\u64a0", "\u648f", "\u648b", "\u648a", "\u648c", "\u64a3", "\u657a", "\u6579", "\u657b", "\u65b2", "\u65b3", "\u66b0", "\u66b2", "\u66aa", "\u6a06", "\u69e5", "\u69f8", "\u6a15", "\u69e4", "\u69ec", "\u69e2", "\u6a1b", "\u6a1d", "\u6a27", "\u6a14", "\u69f7", "\u69e7", "\u6a40", "\u6a08", "\u69e6", "\u69fb", "\u6a0d", "\u69fc", "\u69eb", "\u6a09", "\u6a04", "\u6a25", "\u6a0f", "\u69f6", "\u6a26", "\u6a07", "\u69f4", "\u6a16", "\u6b51", "\u6ba5", "\u6ba3", "\u6ba6", "\u6c01", "\u6c00", "\u6bff", "\u6c02", "\u6f7e", "\u6fc6", "\u6f92", "\u6f4f", "\u6f96", "\u6f6c", "\u6f82", "\u6f55", "\u6f52", "\u6f50", "\u6f57", "\u6f94", "\u6f93", "\u6f00", "\u6f6b", "\u6f90", "\u6f53", "\u6f69", "\u6f7f", "\u6f95", "\u6f6a", "\u71b2", "\u71af", "\u719b", "\u71b0", "\u719d", "\u71a5", "\u719e", "\u71a4", "\u719c", "\u71a7", "\u7298", "\u729a", "\u735e", "\u735f", "\u735d", "\u735b", "\u735a", "\u7359", "\u7362", "\u7508", "\u7507", "\u757e", "\u769d", "\u769e", "\u7789", "\u7788", "\u79a1", "\u79a0", "\u799c", "\u79a2", "\u6b76", "\u7ab2", "\u7bbe", "\u7df7", "\u7ddb", "\u7dea", "\u7de7", "\u7dd7", "\u7de1", "\u7e03", "\u7dfa", "\u7de6", "\u7df6", "\u7df1", "\u7df0", "\u7dee", "\u7ddf", "\u7fac", "\u7fad", "\u8064", "\u8067", "\u819f", "\u8195", "\u81a2", "\u8197", "\u8216", "\u8253", "\u8252", "\u8251", "\u8524", "\u8529", "\u8509", "\u850a", "\u8527", "\u84fb", "\u84fa", "\u8508", "\u84f4", "\u852a", "\u84f2", "\u84f7", "\u84eb", "\u84f3", "\u84ea", "\u84e9", "\u8528", "\u852e", "\u84f6", "\u8531", "\u8526", "\u84e8", "\u84f9", "\u8530", "\u850b", "\u852f", "\u875b", "\u875e", "\u876d", "\u876a", "\u875f", "\u875d", "\u876c", "\u875c", "\u8767", "\u8769", "\u8905", "\u890c", "\u8917", "\u8918", "\u8906", "\u8916", "\u890e", "\u89a4", "\u89a3", "\u8acf", "\u8ac6", "\u8ab8", "\u8ad3", "\u8ad1", "\u8ad4", "\u8ad5", "\u8abb", "\u8ad7", "\u8abe", "\u8ac0", "\u8ac5", "\u8ad8", "\u8aba", "\u8abd", "\u8ad9", "\u8c3e", "\u8c8f", "\u8ce5", "\u8cdf", "\u8cd9", "\u8ce8", "\u8cda", "\u8cdd", "\u8ce7", "\u8d9c", "\u8d9b", "\u8e25", "\u8e1b", "\u8e16", "\u8e19", "\u8e26", "\u8e27", "\u8e18", "\u8e1c", "\u8e17", "\u8e1a", "\u8f2c", "\u8f18", "\u8f1a", "\u8f20", "\u8f23", "\u8f16", "\u8f17", "\u9073", "\u9070", "\u912b", "\u9129", "\u912a", "\u9126", "\u912e", "\u9181", "\u9182", "\u9184", "\u92d0", "\u92c3", "\u92c4", "\u92c0", "\u92d9", "\u92b6", "\u92cf", "\u92f1", "\u92df", "\u92d8", "\u92d7", "\u92dd", "\u92cc", "\u92ef", "\u92c2", "\u92e8", "\u92ca", "\u92ce", "\u92e6", "\u92cd", "\u92d5", "\u92e0", "\u92de", "\u92e7", "\u92d1", "\u92d3", "\u92b5", "\u92e1", "\u92c6", "\u92b4", "\u957c", "\u95ac", "\u95ae", "\u95b0", "\u96a4", "\u96a2", "\u978a", "\u9788", "\u97d0", "\u97cf", "\u981e", "\u981d", "\u9826", "\u9829", "\u9828", "\u9820", "\u981b", "\u9827", "\u98b2", "\u98fa", "\u9914", "\u9916", "\u9917", "\u9915", "\u99dc", "\u99cd", "\u99cf", "\u99d3", "\u99d4", "\u99ce", "\u99c9", "\u99d6", "\u99d8", "\u99cb", "\u99d7", "\u99cc", "\u9af3", "\u9af2", "\u9af1", "\u9b67", "\u9b74", "\u9b71", "\u9b66", "\u9b76", "\u9b75", "\u9b70", "\u9b68", "\u9b64", "\u9b6c", "\u9cfc", "\u9cfa", "\u9cfd", "\u9cff", "\u9cf7", "\u9d07", "\u9d00", "\u9cf9", "\u9cfb", "\u9d08", "\u9d05", "\u9d04", "\u511c", "\u5117", "\u511a", "\u5111", "\u5334", "\u5660", "\u565e", "\u571b", "\u58c8", "\u58c9", "\u58ba", "\u5b19", "\u5b1b", "\u5b21", "\u5b14", "\u5b13", "\u5b10", "\u5b28", "\u5b1a", "\u5b20", "\u5b1e", "\u5dac", "\u5db1", "\u5da9", "\u5da7", "\u5db5", "\u5db0", "\u5dae", "\u5daa", "\u5da8", "\u5db2", "\u5dad", "\u5daf", "\u5db4", "\u5e67", "\u5e68", "\u5e66", "\u5e6f", "\u5ee7", "\u5ee6", "\u5ee5", "\u5f4b", "\u61c5", "\u61b4", "\u61c6", "\u61ba", "\u64c9", "\u6489", "\u64f3", "\u657f", "\u657c", "\u66c8", "\u66c0", "\u66ca", "\u66cb", "\u66cf", "\u66cc", "\u6723", "\u6a49", "\u6a67", "\u6a68", "\u6a5d", "\u6a6d", "\u6a76", "\u6a3b", "\u6a41", "\u6a6a", "\u6a4f", "\u6a54", "\u6a6f", "\u6a69", "\u6a60", "\u6a3c", "\u6a5e", "\u6a56", "\u6a55", "\u6a4d", "\u6a4e", "\u6b55", "\u6b54", "\u6b56", "\u6ba7", "\u6bc8", "\u6bc7", "\u6c04", "\u6c03", "\u6fad", "\u6fcb", "\u6fa3", "\u6fc7", "\u6fbc", "\u6fce", "\u6fc8", "\u6fc4", "\u6fbd", "\u7004", "\u6fa5", "\u6fae", "\u6fac", "\u6faa", "\u6fcf", "\u6fbf", "\u6fab", "\u6fcd", "\u6faf", "\u6fb2", "\u6fb0", "\u71c5", "\u71c2", "\u71bf", "\u71c0", "\u71c1", "\u71cb", "\u71ca", "\u71c7", "\u71bd", "\u71d8", "\u71bc", "\u71c6", "\u71da", "\u71db", "\u729d", "\u729e", "\u7369", "\u7366", "\u7367", "\u7365", "\u736b", "\u736a", "\u749a", "\u74a0", "\u7494", "\u7492", "\u7495", "\u74a1", "\u750b", "\u76bb", "\u779a", "\u779d", "\u779c", "\u779b", "\u7795", "\u7799", "\u7797", "\u78dd", "\u78de", "\u78e3", "\u78db", "\u78e1", "\u78e2", "\u78df", "\u78e0", "\u79a4", "\u7a44", "\u7a48", "\u7ab6", "\u7ab8", "\u7ab5", "\u7ab1", "\u7ab7", "\u7bd5", "\u7bd8", "\u7cd2", "\u7cd4", "\u7cd0", "\u7cd1", "\u7e12", "\u7e21", "\u7e17", "\u7e0c", "\u7e1f", "\u7e20", "\u7e13", "\u7e0e", "\u7e1c", "\u7e15", "\u7e1a", "\u7e22", "\u7e0b", "\u7e0f", "\u7e16", "\u7e0d", "\u7e14", "\u7e25", "\u7e24", "\u806c", "\u81b1", "\u81ae", "\u81b9", "\u81b5", "\u81b0", "\u81ac", "\u81b2", "\u81b7", "\u81f2", "\u8255", "\u8256", "\u8257", "\u856b", "\u854d", "\u8553", "\u8561", "\u8540", "\u8541", "\u8562", "\u8551", "\u8563", "\u8571", "\u854e", "\u856e", "\u8555", "\u8560", "\u858c", "\u8554", "\u856c", "\u8665", "\u8664", "\u879b", "\u878f", "\u8792", "\u87a3", "\u8790", "\u8791", "\u879d", "\u879c", "\u879a", "\u891e", "\u891f", "\u8ae0", "\u8ae2", "\u8af2", "\u8af4", "\u8af5", "\u8add", "\u8b14", "\u8adf", "\u8af0", "\u8ac8", "\u8ade", "\u8ae1", "\u8ae8", "\u8aff", "\u8aef", "\u8afb", "\u8c91", "\u8c92", "\u8c90", "\u8cf5", "\u8cee", "\u8cf1", "\u8cf0", "\u8cf3", "\u8da5", "\u8da7", "\u8ebd", "\u8f36", "\u8f2e", "\u8f35", "\u8f32", "\u8f39", "\u8f37", "\u8f34", "\u9079", "\u907b", "\u9133", "\u9135", "\u9136", "\u9327", "\u931e", "\u9308", "\u931f", "\u9306", "\u930f", "\u937a", "\u9338", "\u933c", "\u931b", "\u9323", "\u9312", "\u9301", "\u9346", "\u932d", "\u930e", "\u930d", "\u92cb", "\u931d", "\u92fa", "\u9325", "\u9313", "\u92f9", "\u92f7", "\u9334", "\u9302", "\u9324", "\u92ff", "\u9329", "\u9339", "\u9335", "\u932a", "\u9314", "\u930c", "\u930b", "\u92fe", "\u9309", "\u9300", "\u92fb", "\u9316", "\u95bc", "\u95cd", "\u95be", "\u95b9", "\u95ba", "\u95b6", "\u95bf", "\u95b5", "\u95bd", "\u96a9", "\u97f0", "\u97f8", "\u9835", "\u982f", "\u9832", "\u9924", "\u991f", "\u9927", "\u9929", "\u999e", "\u99ee", "\u99ec", "\u99e5", "\u99e4", "\u99f0", "\u99e3", "\u99ea", "\u99e9", "\u99e7", "\u9af6", "\u9af7", "\u9b80", "\u9b85", "\u9b87", "\u9b7e", "\u9b7b", "\u9b82", "\u9b93", "\u9b92", "\u9b90", "\u9b7a", "\u9b95", "\u9b7d", "\u9b88", "\u9d25", "\u9d17", "\u9d20", "\u9d1e", "\u9d14", "\u9d29", "\u9d1d", "\u9d18", "\u9d10", "\u9d19", "\u9d1f", "\u9eae", "\u9ead", "\u5126", "\u5125", "\u5124", "\u5120", "\u5129", "\u52f4", "\u568c", "\u568d", "\u5684", "\u5683", "\u567e", "\u5682", "\u567f", "\u5681", "\u58cf", "\u5b2d", "\u5b25", "\u5b23", "\u5b2c", "\u5b27", "\u5b26", "\u5b2f", "\u5b2e", "\u5bf2", "\u5e6c", "\u5e6a", "\u61b5", "\u61bc", "\u61e0", "\u61e5", "\u61e4", "\u61e8", "\u61de", "\u64ef", "\u64e9", "\u64eb", "\u64e8", "\u6581", "\u6580", "\u65b6", "\u65da", "\u66d2", "\u6a8d", "\u6a96", "\u6aa5", "\u6a89", "\u6a9f", "\u6a9b", "\u6a9e", "\u6a87", "\u6a93", "\u6a95", "\u6aa4", "\u6aa6", "\u6a9a", "\u6a8c", "\u6b5b", "\u6bad", "\u6c09", "\u6fcc", "\u6fa9", "\u6ff4", "\u6fd4", "\u6fdc", "\u6fed", "\u6fe7", "\u6ff2", "\u6fdd", "\u6fe8", "\u71f1", "\u71f2", "\u71f0", "\u7373", "\u7497", "\u74b2", "\u74ab", "\u74ad", "\u74b1", "\u74a5", "\u74af", "\u7648", "\u7649", "\u7647", "\u76e9", "\u77b7", "\u78fd", "\u78fc", "\u78fe", "\u79ab", "\u7a5c", "\u7a5b", "\u7a56", "\u7a54", "\u7a5a", "\u7abe", "\u7ac1", "\u7c05", "\u7c00", "\u7bf4", "\u7bf3", "\u7c02", "\u7c03", "\u7c01", "\u7c06", "\u7e2d", "\u7e33", "\u9848", "\u7e38", "\u7e2a", "\u7e49", "\u7e40", "\u7e29", "\u7e4c", "\u7e30", "\u7e36", "\u7e44", "\u802c", "\u8595", "\u85a0", "\u858b", "\u85a3", "\u859a", "\u859e", "\u8589", "\u85a1", "\u858e", "\u8596", "\u858d", "\u8599", "\u85a2", "\u8598", "\u859f", "\u8668", "\u87c5", "\u87c3", "\u87c2", "\u87c4", "\u893c", "\u893e", "\u8952", "\u89ad", "\u89af", "\u89ae", "\u8b1e", "\u8b18", "\u8b16", "\u8b11", "\u8b05", "\u8b0b", "\u8b22", "\u8b0f", "\u8b12", "\u8b15", "\u8b0d", "\u8b06", "\u8b1c", "\u8b13", "\u8b1a", "\u8c4f", "\u8c70", "\u8c72", "\u8c71", "\u8c6f", "\u8cf9", "\u8e4e", "\u8e4d", "\u8e50", "\u8f43", "\u8f40", "\u9138", "\u9199", "\u919f", "\u91a1", "\u919d", "\u91a0", "\u93a1", "\u9383", "\u93af", "\u9364", "\u9356", "\u9347", "\u937c", "\u9358", "\u935c", "\u9376", "\u9349", "\u9350", "\u9351", "\u9360", "\u936d", "\u934c", "\u9379", "\u9357", "\u9355", "\u9352", "\u934f", "\u9371", "\u9377", "\u937b", "\u9361", "\u935e", "\u9363", "\u9367", "\u9380", "\u934e", "\u9359", "\u95c7", "\u95c0", "\u95c9", "\u95c3", "\u95c5", "\u95b7", "\u96ae", "\u96ac", "\u9718", "\u9719", "\u979a", "\u979c", "\u979d", "\u97d5", "\u97d4", "\u97f1", "\u9841", "\u9844", "\u984a", "\u9849", "\u9845", "\u9843", "\u9925", "\u992b", "\u992c", "\u992a", "\u9933", "\u9932", "\u992d", "\u9931", "\u9930", "\u99a3", "\u99a1", "\u9a02", "\u99f4", "\u99f7", "\u99f9", "\u99f8", "\u99f6", "\u99fb", "\u99fd", "\u99fe", "\u99fc", "\u9a03", "\u9afe", "\u9afd", "\u9b01", "\u9b9a", "\u9ba8", "\u9b9e", "\u9b9b", "\u9ba6", "\u9ba1", "\u9ba5", "\u9ba4", "\u9b86", "\u9ba2", "\u9ba0", "\u9baf", "\u9d33", "\u9d41", "\u9d67", "\u9d36", "\u9d2e", "\u9d2f", "\u9d31", "\u9d38", "\u9d30", "\u9d45", "\u9d42", "\u9d3e", "\u9d37", "\u9d40", "\u9d3d", "\u7ff5", "\u9d2d", "\u9e8d", "\u9eb0", "\u9f24", "\u9f54", "\u5131", "\u512d", "\u512e", "\u5698", "\u569c", "\u5697", "\u569a", "\u569d", "\u5699", "\u5970", "\u5b3c", "\u5c69", "\u5c6a", "\u5dc0", "\u5e6d", "\u5e6e", "\u61d8", "\u61df", "\u61ed", "\u61ee", "\u61f1", "\u61ea", "\u61f0", "\u61eb", "\u61d6", "\u61e9", "\u64ff", "\u6504", "\u64fd", "\u64f8", "\u6503", "\u64fc", "\u65db", "\u66d8", "\u6ac5", "\u6ab9", "\u6abd", "\u6ae1", "\u6ac6", "\u6aba", "\u6ab6", "\u6ab7", "\u6ac7", "\u6ab4", "\u6b5e", "\u6bc9", "\u6c0b", "\u7007", "\u700c", "\u700d", "\u7001", "\u7005", "\u7014", "\u700e", "\u6fff", "\u7000", "\u6ffb", "\u7026", "\u6ffc", "\u6ff7", "\u700a", "\u7201", "\u71ff", "\u7203", "\u71fd", "\u7376", "\u74b8", "\u74c0", "\u74b5", "\u74c1", "\u74be", "\u74b6", "\u74c2", "\u7659", "\u7650", "\u7653", "\u765a", "\u76a6", "\u76bd", "\u76ec", "\u77c2", "\u77ba", "\u78ff", "\u790c", "\u7909", "\u7910", "\u7912", "\u7911", "\u79ad", "\u79ac", "\u7a5f", "\u7c1c", "\u7c2d", "\u7c1d", "\u7c22", "\u7c25", "\u7c30", "\u7e5c", "\u7e50", "\u7e56", "\u7e63", "\u7e58", "\u7e62", "\u7e5f", "\u7e51", "\u7e60", "\u7e57", "\u7e53", "\u7fb5", "\u7ff7", "\u7ff8", "\u8075", "\u81d1", "\u81d2", "\u81d0", "\u85b4", "\u85c6", "\u85c0", "\u85c3", "\u85b3", "\u85b5", "\u85bd", "\u85c7", "\u85c4", "\u85bf", "\u85cb", "\u85ce", "\u85c8", "\u85c5", "\u85b6", "\u8624", "\u85be", "\u8669", "\u87f3", "\u87d8", "\u87a4", "\u87d7", "\u87d9", "\u87f4", "\u8953", "\u894b", "\u894f", "\u894c", "\u8946", "\u8950", "\u8951", "\u8949", "\u8b2a", "\u8b23", "\u8b33", "\u8b30", "\u8b35", "\u8b47", "\u8b2f", "\u8b3c", "\u8b3e", "\u8b31", "\u8b37", "\u8b36", "\u8b2e", "\u8b3b", "\u8b3d", "\u8b3a", "\u8cfe", "\u8d04", "\u8d02", "\u8d00", "\u8e5c", "\u8e62", "\u8e60", "\u8e57", "\u8e56", "\u8e5e", "\u8e65", "\u8e5b", "\u8e61", "\u8e5d", "\u8e54", "\u8f46", "\u8f47", "\u8f48", "\u8f4b", "\u9128", "\u913b", "\u913e", "\u91a8", "\u91a5", "\u91a7", "\u93b5", "\u938c", "\u9392", "\u93b7", "\u939b", "\u939d", "\u9389", "\u93a7", "\u938e", "\u93aa", "\u939e", "\u93a6", "\u9395", "\u9388", "\u9399", "\u939f", "\u938d", "\u93b1", "\u9391", "\u93b2", "\u93a4", "\u93a8", "\u93b4", "\u93a3", "\u93a5", "\u95d2", "\u95d3", "\u95d1", "\u96d7", "\u96da", "\u5dc2", "\u96df", "\u96d8", "\u96dd", "\u9723", "\u9722", "\u9725", "\u97a8", "\u97aa", "\u97a5", "\u97d7", "\u97d9", "\u97d6", "\u97d8", "\u97fa", "\u9850", "\u9851", "\u9852", "\u98b8", "\u9941", "\u993c", "\u993a", "\u9a0f", "\u9a0b", "\u9a09", "\u9a0d", "\u9a04", "\u9a11", "\u9a0a", "\u9a05", "\u9a07", "\u9a06", "\u9b29", "\u9b35", "\u9bc7", "\u9bc6", "\u9bc3", "\u9bbf", "\u9bc1", "\u9bb5", "\u9bb8", "\u9bd3", "\u9bb6", "\u9bc4", "\u9bb9", "\u9bbd", "\u9d5c", "\u9d53", "\u9d4f", "\u9d4a", "\u9d5b", "\u9d4b", "\u9d59", "\u9d56", "\u9d4c", "\u9d57", "\u9d52", "\u9d54", "\u9d5f", "\u9d58", "\u9d5a", "\u9e8e", "\u9f01", "\u9f00", "\u9f25", "\u9f2b", "\u9f2a", "\u9f29", "\u9f28", "\u9f4c", "\u9f55", "\u5134", "\u5135", "\u5296", "\u52f7", "\u53b4", "\u56ab", "\u56ad", "\u56a6", "\u56a7", "\u56aa", "\u56ac", "\u58da", "\u58dd", "\u58db", "\u5b3d", "\u5b3e", "\u5b3f", "\u5dc3", "\u5e70", "\u5fbf", "\u61fb", "\u6507", "\u6510", "\u650d", "\u650c", "\u650e", "\u6584", "\u65de", "\u65dd", "\u6ae7", "\u6ae0", "\u6acc", "\u6ad1", "\u6ad9", "\u6acb", "\u6adf", "\u6adc", "\u6ad0", "\u6aeb", "\u6acf", "\u6acd", "\u6ade", "\u6b60", "\u6bb0", "\u6c0c", "\u7019", "\u7027", "\u7020", "\u7016", "\u7021", "\u7022", "\u7029", "\u7017", "\u702a", "\u720c", "\u720a", "\u7202", "\u7205", "\u72a5", "\u72a6", "\u72a4", "\u72a3", "\u72a1", "\u74cb", "\u74c5", "\u74b7", "\u74c3", "\u77c9", "\u77ca", "\u77c4", "\u791d", "\u791b", "\u7921", "\u791c", "\u7917", "\u79b0", "\u7a67", "\u7a68", "\u7c33", "\u7c3c", "\u7c2c", "\u7c3b", "\u7cec", "\u7cea", "\u7e76", "\u7e75", "\u7e78", "\u7e77", "\u7e6f", "\u7e7a", "\u7e72", "\u7e74", "\u7e68", "\u7f4b", "\u7f4a", "\u7f83", "\u7f86", "\u7fb7", "\u8078", "\u81d7", "\u81d5", "\u8264", "\u8261", "\u8263", "\u85eb", "\u85f1", "\u85ed", "\u85d9", "\u85e1", "\u85da", "\u85d7", "\u85ec", "\u85f2", "\u85f8", "\u85d8", "\u85df", "\u85e3", "\u85f0", "\u85ef", "\u85de", "\u85e2", "\u87f6", "\u87f7", "\u8809", "\u880c", "\u8806", "\u8808", "\u8962", "\u895a", "\u895b", "\u8957", "\u8961", "\u895c", "\u8958", "\u895d", "\u8959", "\u8988", "\u89b7", "\u89b6", "\u89f6", "\u8b50", "\u8b48", "\u8b4a", "\u8b40", "\u8b53", "\u8b56", "\u8b54", "\u8b4b", "\u8b55", "\u8b51", "\u8b42", "\u8b52", "\u8b57", "\u8c9a", "\u8d06", "\u8d07", "\u8d09", "\u8dac", "\u8daa", "\u8dad", "\u8dab", "\u8e78", "\u8e7b", "\u8ec2", "\u8f52", "\u8f51", "\u8f4f", "\u8f50", "\u8f53", "\u9140", "\u913f", "\u93de", "\u93c7", "\u93cf", "\u93c2", "\u93da", "\u93d0", "\u93f9", "\u93ec", "\u93d9", "\u93a9", "\u93e6", "\u93d4", "\u93ee", "\u93e3", "\u93d5", "\u93c4", "\u93c0", "\u93d2", "\u93e7", "\u957d", "\u95da", "\u95db", "\u9729", "\u9728", "\u9726", "\u97b7", "\u97b6", "\u97dd", "\u97de", "\u97df", "\u985c", "\u9859", "\u985d", "\u9857", "\u98bf", "\u98bd", "\u98bb", "\u98be", "\u9948", "\u9947", "\u9943", "\u9a1a", "\u9a15", "\u9a25", "\u9a1d", "\u9a24", "\u9a1b", "\u9a22", "\u9a20", "\u9a27", "\u9a23", "\u9a1e", "\u9a1c", "\u9a14", "\u9b0b", "\u9b0a", "\u9b0e", "\u9b0c", "\u9b37", "\u9bea", "\u9beb", "\u9be0", "\u9bde", "\u9be4", "\u9be6", "\u9be2", "\u9bf0", "\u9bd4", "\u9bd7", "\u9bec", "\u9bd9", "\u9be5", "\u9bd5", "\u9be1", "\u9bda", "\u9d77", "\u9d81", "\u9d8a", "\u9d84", "\u9d88", "\u9d71", "\u9d80", "\u9d78", "\u9d86", "\u9d8b", "\u9d8c", "\u9d7d", "\u9d6b", "\u9d74", "\u9d75", "\u9d70", "\u9d69", "\u9d85", "\u9d73", "\u9d7b", "\u9d6f", "\u9d79", "\u9d7f", "\u9d87", "\u9d68", "\u9e91", "\u9ec0", "\u9f40", "\u9f41", "\u9f4d", "\u9f56", "\u9f57", "\u9f58", "\u5337", "\u56b2", "\u56b5", "\u56b3", "\u58e3", "\u5b45", "\u5dc7", "\u5eee", "\u5eef", "\u5fc0", "\u5fc1", "\u61f9", "\u6517", "\u6516", "\u6515", "\u65df", "\u66e3", "\u66e4", "\u6af3", "\u6af0", "\u6aea", "\u6ae8", "\u6af9", "\u6af1", "\u6aee", "\u6aef", "\u703c", "\u702f", "\u7034", "\u7031", "\u7042", "\u703f", "\u7040", "\u703b", "\u7033", "\u7041", "\u7213", "\u7214", "\u72a8", "\u737d", "\u737c", "\u76ab", "\u76aa", "\u76be", "\u76ed", "\u77cc", "\u77cf", "\u7923", "\u7927", "\u7928", "\u7929", "\u79b2", "\u7a6e", "\u7a6c", "\u7a6d", "\u7af7", "\u7c49", "\u7c48", "\u7c4a", "\u7c47", "\u7c45", "\u7cee", "\u7e7b", "\u7e7e", "\u7e81", "\u7e80", "\u8079", "\u81db", "\u81d9", "\u820b", "\u8622", "\u8601", "\u861b", "\u85f6", "\u8604", "\u8609", "\u860c", "\u8810", "\u8811", "\u8963", "\u89b9", "\u89f7", "\u8b60", "\u8b6a", "\u8b5d", "\u8b68", "\u8b63", "\u8b65", "\u8dae", "\u8f59", "\u8f56", "\u8f57", "\u8f55", "\u8f58", "\u8f5a", "\u908d", "\u9141", "\u940b", "\u9413", "\u93fb", "\u9420", "\u940f", "\u9414", "\u93fe", "\u9415", "\u9410", "\u9428", "\u9419", "\u940d", "\u93f5", "\u9400", "\u93f7", "\u9407", "\u9416", "\u9412", "\u93fa", "\u9409", "\u93f8", "\u940a", "\u93ff", "\u93fc", "\u940c", "\u93f6", "\u9411", "\u9406", "\u95de", "\u95e0", "\u95df", "\u97b9", "\u97bb", "\u97fd", "\u97fe", "\u9860", "\u9862", "\u9863", "\u985f", "\u98c1", "\u98c2", "\u9950", "\u994e", "\u9959", "\u994c", "\u9953", "\u9a32", "\u9a34", "\u9a31", "\u9a2c", "\u9a2a", "\u9a36", "\u9a29", "\u9a2e", "\u9a38", "\u9a2d", "\u9ac7", "\u9aca", "\u9c0b", "\u9c08", "\u9bf7", "\u9c05", "\u9c12", "\u9bf8", "\u9c40", "\u9c07", "\u9c0e", "\u9c06", "\u9c17", "\u9c14", "\u9c09", "\u9d9f", "\u9d99", "\u9da4", "\u9d9d", "\u9d92", "\u9d98", "\u9d90", "\u9d9b", "\u9da0", "\u9d94", "\u9d9c", "\u9daa", "\u9d97", "\u9da1", "\u9d9a", "\u9da2", "\u9da8", "\u9d9e", "\u9dbf", "\u9da9", "\u9d96", "\u9da6", "\u9da7", "\u9e99", "\u9e9b", "\u9e9a", "\u9f5b", "\u9f60", "\u9f5e", "\u9f5d", "\u9f59", "\u9f91", "\u513a", "\u5139", "\u5298", "\u5297", "\u56c3", "\u56be", "\u5b47", "\u5dcb", "\u5dcf", "\u5ef1", "\u61fd", "\u651b", "\u6b02", "\u6afc", "\u6b03", "\u6af8", "\u6b00", "\u7043", "\u7044", "\u704a", "\u7048", "\u7049", "\u7045", "\u7046", "\u721a", "\u7219", "\u766a", "\u77d0", "\u792d", "\u7931", "\u792f", "\u7c54", "\u7c53", "\u7cf2", "\u7e8a", "\u7e87", "\u7e88", "\u7e8b", "\u7e86", "\u7e8d", "\u7f4d", "\u8030", "\u81dd", "\u8618", "\u8626", "\u861f", "\u8623", "\u861c", "\u8619", "\u862e", "\u8621", "\u8620", "\u861e", "\u8625", "\u8829", "\u881d", "\u8820", "\u882b", "\u884a", "\u896d", "\u8969", "\u896e", "\u896b", "\u89fa", "\u8b79", "\u8b78", "\u8b45", "\u8b7a", "\u8b7b", "\u8d10", "\u8d14", "\u8daf", "\u8e8e", "\u8e8c", "\u8f5e", "\u8f5b", "\u8f5d", "\u943b", "\u9436", "\u9429", "\u943d", "\u943c", "\u9430", "\u9439", "\u942a", "\u9437", "\u942c", "\u9440", "\u9431", "\u95e5", "\u95e4", "\u95e3", "\u9735", "\u97bf", "\u97e1", "\u9864", "\u98c9", "\u98c6", "\u98c0", "\u9958", "\u9a3d", "\u9a46", "\u9a44", "\u9a42", "\u9a41", "\u9a3a", "\u9a3f", "\u9b15", "\u9b17", "\u9b18", "\u9b16", "\u9b3a", "\u9c2b", "\u9c1d", "\u9c1c", "\u9c2c", "\u9c23", "\u9c28", "\u9c29", "\u9c24", "\u9c21", "\u9db7", "\u9db6", "\u9dbc", "\u9dc1", "\u9dc7", "\u9dca", "\u9dcf", "\u9dbe", "\u9dc5", "\u9dc3", "\u9dbb", "\u9db5", "\u9dce", "\u9db9", "\u9dba", "\u9dac", "\u9dc8", "\u9db1", "\u9dad", "\u9dcc", "\u9db3", "\u9dcd", "\u9db2", "\u9e7a", "\u9e9c", "\u9f1b", "\u9f4e", "\u9f65", "\u9f64", "\u9f92", "\u56c6", "\u56c5", "\u5971", "\u5b4b", "\u5b4c", "\u5dd5", "\u5dd1", "\u5ef2", "\u6521", "\u6520", "\u6b0b", "\u6b08", "\u6b09", "\u7055", "\u7056", "\u7057", "\u7052", "\u721f", "\u72a9", "\u74d8", "\u74d5", "\u74d9", "\u74d7", "\u76ad", "\u7c57", "\u7c5c", "\u7c59", "\u7c5b", "\u7c5a", "\u7cf4", "\u7cf1", "\u7e91", "\u7f4f", "\u7f87", "\u81de", "\u8634", "\u8635", "\u8633", "\u862c", "\u8632", "\u8636", "\u882c", "\u8828", "\u8826", "\u882a", "\u8825", "\u8971", "\u89bf", "\u89be", "\u8b7e", "\u8b84", "\u8b82", "\u8b86", "\u8b85", "\u8b7f", "\u8d15", "\u8e9a", "\u8e96", "\u8e97", "\u8f60", "\u8f62", "\u944c", "\u9450", "\u944a", "\u944b", "\u944f", "\u9447", "\u9445", "\u9448", "\u9449", "\u9446", "\u97e3", "\u986a", "\u9869", "\u98cb", "\u995b", "\u9a4e", "\u9a53", "\u9a54", "\u9a4c", "\u9a4f", "\u9a48", "\u9a4a", "\u9a49", "\u9a52", "\u9a50", "\u9b19", "\u9b2b", "\u9b56", "\u9c46", "\u9c48", "\u9c3f", "\u9c44", "\u9c39", "\u9c33", "\u9c41", "\u9c37", "\u9c34", "\u9c32", "\u9c3d", "\u9c36", "\u9ddb", "\u9dd2", "\u9dde", "\u9dda", "\u9dcb", "\u9dd0", "\u9ddc", "\u9dd1", "\u9ddf", "\u9de9", "\u9dd9", "\u9dd8", "\u9dd6", "\u9df5", "\u9dd5", "\u9ddd", "\u9f35", "\u9f33", "\u9f42", "\u9f6b", "\u9f95", "\u9fa2", "\u513d", "\u5299", "\u58e8", "\u58e7", "\u5972", "\u5b4d", "\u5dd8", "\u882f", "\u5f4f", "\u6201", "\u6203", "\u6204", "\u6529", "\u66eb", "\u6b11", "\u6b12", "\u6b0f", "\u6bca", "\u705b", "\u705a", "\u7222", "\u7382", "\u7381", "\u7383", "\u77d4", "\u7c67", "\u7c66", "\u7e95", "\u8631", "\u8830", "\u882e", "\u8976", "\u8974", "\u8973", "\u89fe", "\u8b8c", "\u8b8e", "\u8b8b", "\u8b88", "\u8d19", "\u8e98", "\u8f64", "\u8f63", "\u9462", "\u9455", "\u945d", "\u9457", "\u945e", "\u97c4", "\u97c5", "\u9800", "\u9a56", "\u9a59", "\u9b1e", "\u9c52", "\u9c58", "\u9c50", "\u9c4a", "\u9c4d", "\u9c4b", "\u9c55", "\u9c59", "\u9c4c", "\u9c4e", "\u9dfb", "\u9df7", "\u9def", "\u9de3", "\u9deb", "\u9df8", "\u9de4", "\u9df6", "\u9de1", "\u9dee", "\u9de6", "\u9df2", "\u9df0", "\u9dec", "\u9df4", "\u9df3", "\u9de8", "\u9ded", "\u9ec2", "\u9ef2", "\u9ef3", "\u9f1c", "\u9f36", "\u9f43", "\u9f4f", "\u9f71", "\u9f70", "\u9f6e", "\u9f6f", "\u56d3", "\u56cd", "\u5b4e", "\u5c6d", "\u66ed", "\u66ee", "\u6b13", "\u7061", "\u705d", "\u7060", "\u7223", "\u74db", "\u77d5", "\u7938", "\u79b7", "\u79b6", "\u7c6a", "\u7e97", "\u7f89", "\u8643", "\u8838", "\u8837", "\u8835", "\u884b", "\u8b94", "\u8b95", "\u8ea0", "\u91be", "\u91bd", "\u91c2", "\u9468", "\u9469", "\u96e5", "\u9746", "\u9743", "\u9747", "\u97c7", "\u9a5e", "\u9b59", "\u9c63", "\u9c67", "\u9c66", "\u9c62", "\u9c5e", "\u9c60", "\u9e02", "\u9dfe", "\u9e07", "\u9e06", "\u9e05", "\u9e00", "\u9e01", "\u9e09", "\u9dff", "\u9dfd", "\u9e04", "\u9f1e", "\u9f46", "\u9f74", "\u9f75", "\u9f76", "\u65b8", "\u6b18", "\u6b19", "\u6b17", "\u6b1a", "\u7062", "\u7226", "\u72aa", "\u7939", "\u7c69", "\u7c6b", "\u7cf6", "\u7e9a", "\u7e98", "\u7e99", "\u81e0", "\u81e1", "\u8646", "\u8647", "\u8648", "\u8979", "\u897a", "\u89ff", "\u8b98", "\u8b99", "\u8ea5", "\u8ea4", "\u8ea3", "\u9471", "\u9473", "\u9749", "\u9872", "\u995f", "\u9c68", "\u9c6e", "\u9c6d", "\u9e0b", "\u9e0d", "\u9e10", "\u9e0f", "\u9e12", "\u9e11", "\u9ea1", "\u9ef5", "\u9f09", "\u9f47", "\u9f78", "\u9f7b", "\u9f7a", "\u7066", "\u7c6f", "\u8ea6", "\u91c3", "\u9474", "\u9478", "\u9476", "\u9475", "\u9a60", "\u9c74", "\u9c73", "\u9c71", "\u9c75", "\u9e14", "\u9e13", "\u9ef6", "\u9f0a", "\u9fa4", "\u7068", "\u7065", "\u7cf7", "\u866a", "\u8b9e", "\u8c9c", "\u8ea9", "\u8ec9", "\u974b", "\u9873", "\u9874", "\u98cc", "\u9961", "\u99ab", "\u9a64", "\u9a66", "\u9a67", "\u9e15", "\u9e17", "\u9f48", "\u6b1e", "\u7227", "\u864c", "\u8ea8", "\u9482", "\u9480", "\u9481", "\u9a69", "\u9a68", "\u9b2e", "\u9e19", "\u864b", "\u8b9f", "\u9483", "\u9c79", "\u7675", "\u9a6b", "\u9c7a", "\u9e1d", "\u7069", "\u706a", "\u9ea4", "\u9f7e", "\u9f49", "\u9f98", "\u7881", "\u92b9", "\u58bb", "\u5afa", "\u0f0f", "\u0d69", "\u06dd", "\u0d70", "\u000f", "\u0013", "\u0015", "\u0016", "\u0017", "\u0019", "\u001a", "\u001d", "\u2501", "\u2503", "\u250f", "\u2513", "\u251b", "\u2517", "\u2523", "\u2533", "\u252b", "\u253b", "\u254b", "\u2520", "\u252f", "\u2528", "\u2537", "\u253f", "\u251d", "\u2530", "\u2525", "\u2538", "\u2542", "\u3349", "\u3314", "\u3322", "\u334d", "\u3318", "\u3327", "\u3303", "\u3336", "\u3351", "\u3357", "\u330d", "\u3326", "\u3323", "\u332b", "\u334a", "\u333b", "\u337b", "\u301f", "\u33cd", "\u32a4", "\u3232", "\u3239", "\u337e", "\u337d", "\u337c", "\u5516", "\u7a50", "\u9bf5", "\u9b8e", "\u7a32", "\u9c2f", "\u6b1d", "\u9834", "\u92ed", "\u99c5", "\u95b2", "\u7e01", "\u8597", "\u5869", "\u9d2c", "\u9d0e", "\u7a4f", "\u58ca", "\u61d0", "\u7d75", "\u920e", "\u6bbb", "\u899a", "\u691b", "\u7ac3", "\u52e7", "\u5dfb", "\u5bdb", "\u6b53", "\u89b3", "\u8acc", "\u95a2", "\u8218", "\u5dcc", "\u8d0b", "\u9854", "\u4e80", "\u5036", "\u99c6", "\u99c8", "\u55b0", "\u7c82", "\u52f2", "\u7d4c", "\u7e4b", "\u8efd", "\u981a", "\u9d8f", "\u5039", "\u570f", "\u967a", "\u9855", "\u9a13", "\u9e78", "\u53b3", "\u88b4", "\u5a2f", "\u9271", "\u67fb", "\u6b73", "\u583a", "\u7523", "\u8b83", "\u8cdb", "\u6b6f", "\u9d2b", "\u546a", "\u7e4d", "\u8b90", "\u7363", "\u7e26", "\u5968", "\u713c", "\u58cc", "\u5b22", "\u7a63", "\u8b72", "\u976d", "\u7c8b", "\u6919", "\u702c", "\u8aac", "\u7e4a", "\u8cce", "\u92ad", "\u9061", "\u60e3", "\u635c", "\u7dcf", "\u8061", "\u8358", "\u9a12", "\u5897", "\u81d3", "\u8535", "\u99c4", "\u9a28", "\u51e7", "\u7aea", "\u92f3", "\u5fb4", "\u8074", "\u9244", "\u8ee2", "\u5d8b", "\u68bc", "\u95d8", "\u50cd", "\u5ce0", "\u5fb3", "\u701e", "\u51ea", "\u7e04", "\u56a2", "\u5ec3", "\u6973", "\u7872", "\u7560", "\u9262", "\u6e8c", "\u9197", "\u92f2", "\u51a8", "\u5840", "\u8217", "\u7a42", "\u982c", "\u623b", "\u8a33", "\u9453", "\u69d8", "\u8b21", "\u983c", "\u7dd1", "\u96a3", "\u5841", "\u6d99", "\u9f62", "\u66a6", "\u6b74", "\u932c", "\u9c10", "\u4e85", "\u50de", "\u5101", "\u5116", "\u7af8", "\u51a9", "\u51e9", "\u52b5", "\u5333", "\u5338", "\u51d6", "\u53b0", "\u7c12", "\u545f", "\u554c", "\u55a9", "\u5650", "\u568a", "\u56a0", "\u56ce", "\u5737", "\u5738", "\u57c0", "\u5872", "\u5870", "\u58b9", "\u58b8", "\u58d7", "\u58dc", "\u58fb", "\u590a", "\u7ad2", "\u596c", "\u5ad0", "\u5bf3", "\u5c76", "\u5cfa", "\u5d8c", "\u5d76", "\u5d90", "\u5dd3", "\u5e64", "\u5e47", "\u5ed0", "\u5ecf", "\u5ef0", "\u6031", "\u603a", "\u604a", "\u613c", "\u613d", "\u6142", "\u6159", "\u616f", "\u6199", "\u6187", "\u61f4", "\u64f6", "\u6505", "\u65d9", "\u66c1", "\u6859", "\u68ba", "\u688d", "\u6926", "\u6928", "\u691a", "\u69f9", "\u6a12", "\u6ac1", "\u6a0c", "\u6a78", "\u6b05", "\u6b1f", "\u98ee", "\u6bb1", "\u6bdf", "\u6e76", "\u6f81", "\u6ff3", "\u6f91", "\u70f1", "\u7155", "\u7188", "\u71d7", "\u71f5", "\u7287", "\u74a2", "\u756d", "\u7668", "\u7667", "\u7676", "\u76b9", "\u862f", "\u77b9", "\u7874", "\u78af", "\u7907", "\u799d", "\u7a43", "\u7a49", "\u7ac8", "\u7ab0", "\u7acd", "\u7acf", "\u7ad5", "\u7ad3", "\u7b6c", "\u7c14", "\u7c13", "\u7bf6", "\u7c4f", "\u7c58", "\u7c56", "\u7c83", "\u7c90", "\u7d4b", "\u7d89", "\u7d9b", "\u7dab", "\u7ddc", "\u7de4", "\u7e05", "\u7e66", "\u7e67", "\u7e5d", "\u7dd5", "\u7e7f", "\u7e89", "\u7e92", "\u7e90", "\u7e8e", "\u7f4e", "\u7fae", "\u8b71", "\u805f", "\u8062", "\u8068", "\u815f", "\u8193", "\u81b8", "\u8262", "\u8323", "\u83f7", "\u8422", "\u8420", "\u842a", "\u84ad", "\u84d9", "\u84da", "\u8602", "\u8630", "\u87d0", "\u880f", "\u880e", "\u8827", "\u885e", "\u88b5", "\u8904", "\u891d", "\u8977", "\u898a", "\u89a9", "\u8ada", "\u8b0c", "\u8b4c", "\u8b5b", "\u8c3a", "\u8c8e", "\u8c7c", "\u8cad", "\u8ccd", "\u8e99", "\u8ec6", "\u8ebe", "\u8ec5", "\u8ec8", "\u8ee3", "\u8f19", "\u8f0c", "\u8f4c", "\u8f5c", "\u91d6", "\u91df", "\u91e1", "\u91db", "\u91fc", "\u91f6", "\u922c", "\u9344", "\u933a", "\u933b", "\u936e", "\u93ad", "\u93b9", "\u93e5", "\u941a", "\u9421", "\u9441", "\u945b", "\u9229", "\u945a", "\u9587", "\u958a", "\u9596", "\u9599", "\u95a0", "\u95a7", "\u6ff6", "\u894d", "\u976b", "\u9771", "\u9779", "\u97c8", "\u97f2", "\u983d", "\u984b", "\u98aa", "\u98c3", "\u991d", "\u9920", "\u9942", "\u99bc", "\u99f2", "\u9af4", "\u9b2a", "\u9b83", "\u9b96", "\u9b97", "\u9b9f", "\u9bb4", "\u9bcf", "\u9bd1", "\u9bd2", "\u9be3", "\u9c3a", "\u9bf2", "\u9bf1", "\u9c15", "\u9c0c", "\u9c0a", "\u9c04", "\u9c2e", "\u9c30", "\u9c47", "\u9c5a", "\u9c76", "\u9cec", "\u9cf0", "\u9ceb", "\u9d2a", "\u9d44", "\u9d46", "\u9d48", "\u9d5e", "\u9d64", "\u9d50", "\u9dab", "\u9d7a", "\u9dc4", "\u9dc6", "\u9e95", "\u9f08", "\u76b7", "\u69c7", "\u9348", "\u84dc", "\u5f45", "\u4f03", "\u5393", "\u57c8", "\ufa10", "\u58b2", "\u590b", "\u595d", "\u5cf5", "\u5d53", "\u5db9", "\u5dd0", "\u5f34", "\u6111", "\u6130", "\u6198", "\u663b", "\ufa12", "\uf929", "\u6a73", "\u6ae2", "\u6ae4", "\u6ff5", "\u710f", "\ufa15", "\u72be", "\ufa16", "\ufa17", "\u7930", "\ufa19", "\ufa1a", "\ufa1b", "\ufa1c", "\ufa1d", "\u7d48", "\u7dd6", "\u7f47", "\ufa1e", "\u8807", "\u8a37", "\ufa22", "\u8d12", "\ufa25", "\ufa26", "\u9115", "\u91de", "\u91e5", "\u923c", "\u9259", "\u9277", "\u93c6", "\uf9dc", "\u96af", "\u974d", "\u974f", "\u9751", "\ufa2a", "\ufa2b", "\ufa2c", "\u9b72", "\u9b8f", "\u9bb1", "\u9c00", "\ufa2d", "\uff07", "\ue03f", "\ue0fb", "\ue1b7", "\ue273", "\ue32f", "\ue3eb", "\ue4a7", "\ue524", "\ue563", "\ue5e0", "\u4e75", "\u4e79", "\u4f16", "\u4f40", "\u4f42", "\u4f4b", "\u4fbc", "\u4fbd", "\u4fbe", "\u5001", "\u5004", "\u500a", "\u5032", "\u5052", "\u5067", "\u5071", "\u508f", "\u5090", "\u5093", "\u50b9", "\u50c0", "\u50c3", "\u50cc", "\u50dc", "\u50df", "\u50e2", "\u50fa", "\u510d", "\u510e", "\u5119", "\u511b", "\u511d", "\u511e", "\u5123", "\u5127", "\u5128", "\u512c", "\u512f", "\u51d3", "\u51d5", "\u5245", "\u5279", "\u5285", "\u5295", "\u529a", "\u52b6", "\u52b7", "\u52b8", "\u52ba", "\u52bd", "\u52dc", "\u52e8", "\u52ea", "\u52ec", "\u52f6", "\u5332", "\u5335", "\u53b5", "\u53c5", "\u545e", "\u546d", "\u546e", "\u54f6", "\u550d", "\u5558", "\u555a", "\u555b", "\u55c1", "\u55d8", "\u5643", "\u5644", "\u564b", "\u5661", "\u5688", "\u568b", "\u569e", "\u569f", "\u56a9", "\u56b1", "\u56cf", "\u56d0", "\u5711", "\u5715", "\u57e6", "\u5826", "\u5861", "\u5867", "\u5878", "\u5896", "\u58a2", "\u58cd", "\u58d0", "\u58e1", "\u595e", "\u595f", "\u596f", "\u59b7", "\u59c4", "\u59df", "\u59ef", "\u5a30", "\u5a45", "\u5a96", "\u5a99", "\u5aa0", "\u5acf", "\u5b00", "\u5bf4", "\u5c75", "\u5c87", "\u5cdd", "\u5cf2", "\u5d46", "\u5d5f", "\u5d60", "\u5d61", "\u5d64", "\u5dab", "\u5dd9", "\u5e35", "\u5e50", "\u5e49", "\u5e51", "\u5f47", "\u5f4d", "\u5fa7", "\u5fa4", "\u5fb0", "\u5fb1", "\u6048", "\u60c2", "\u60e5", "\u60fd", "\u6131", "\u6135", "\u6139", "\u617b", "\u617f", "\u6181", "\u6184", "\u6197", "\u619c", "\u61a0", "\u61a5", "\u61b9", "\u61ce", "\u61cf", "\u61dc", "\u61dd", "\u61e1", "\u61e2", "\u61ec", "\u61ef", "\u6239", "\u628d", "\u6290", "\u6335", "\u635b", "\u639a", "\u644f", "\u645a", "\u6463", "\u64a1", "\u64cc", "\u64ea", "\u64f5", "\u6508", "\u651e", "\u651f", "\u657d", "\u6585", "\u65b4", "\u65fe", "\u65ff", "\u6646", "\u666b", "\u669a", "\u669b", "\u669c", "\u66a4", "\u66ad", "\u66c2", "\u66c3", "\u66ce", "\u66d4", "\u66df", "\u67bc", "\u67bd", "\u67f9", "\u6819", "\u6827", "\u682c", "\u6830", "\u6857", "\u6858", "\u685b", "\u687a", "\u6888", "\u689a", "\u68bb", "\u68c5", "\u68e5", "\u68ed", "\u6909", "\u6916", "\u6992", "\u69c5", "\u69c8", "\u69d6", "\u69d7", "\u69f5", "\u6a03", "\u6a1a", "\u6a24", "\u6a37", "\u6a4a", "\u6a52", "\u6a86", "\u6a8b", "\u6a9d", "\u6ab0", "\u6ab1", "\u6abe", "\u6abf", "\u6ac9", "\u6ac8", "\u6ad4", "\u6ad5", "\u6ad6", "\u6af2", "\u6afd", "\u6b06", "\u6b07", "\u6b1b", "\u6b2b", "\u6b52", "\u6b58", "\u6b5d", "\u6b6e", "\u6b70", "\u6b75", "\u6ba8", "\u6ba9", "\u6bac", "\u6bb9", "\u6bbe", "\u6e04", "\u6e48", "\u6e7b", "\u6e7d", "\u6f0c", "\u6f1b", "\u6f68", "\u6f83", "\u6f9a", "\u6fc5", "\u6fda", "\u6ff9", "\u6ffd", "\u704b", "\u7054", "\u70d5", "\u70d6", "\u7103", "\u712b", "\u712d", "\u7138", "\u7157", "\u71a2", "\u71cc", "\u71d3", "\u7200", "\u7208", "\u7209", "\u7217", "\u7224", "\u7243", "\u7245", "\u72e5", "\u7305", "\u7379", "\u73f7", "\u73f9", "\u73fb", "\u7439", "\u7443", "\u7447", "\u7466", "\u7468", "\u746b", "\u7499", "\u74ae", "\u74b9", "\u74c9", "\u74cc", "\u74d0", "\u74ea", "\u74eb", "\u74fa", "\u74fc", "\u7506", "\u7524", "\u755e", "\u7561", "\u7571", "\u764a", "\u764b", "\u7674", "\u769f", "\u76a0", "\u76a2", "\u76e8", "\u7714", "\u7717", "\u7757", "\u7770", "\u7772", "\u7773", "\u7774", "\u7794", "\u7796", "\u77c3", "\u77d1", "\u77d2", "\u77df", "\u7861", "\u7863", "\u7900", "\u791a", "\u7920", "\u797e", "\u79a9", "\u79af", "\u79da", "\u7a27", "\u7a2d", "\u7a45", "\u7a55", "\u7a59", "\u7a5d", "\u7a65", "\u7a6a", "\u7ab9", "\u7abb", "\u7abc", "\u7ac6", "\u7ac9", "\u7ace", "\u7ae8", "\u7ae9", "\u7aec", "\u7b41", "\u7b6a", "\u7b89", "\u7bba", "\u7bbb", "\u7bbc", "\u7bbd", "\u7bd6", "\u7bd7", "\u7bf5", "\u7c04", "\u7c1b", "\u7c31", "\u7c34", "\u7c36", "\u7c3a", "\u7c46", "\u7c55", "\u7c51", "\u7c52", "\u7c61", "\u7c6d", "\u7c70", "\u7c86", "\u7c87", "\u7c8f", "\u7cb6", "\u7cb7", "\u7ccf", "\u7cd3", "\u7ce6", "\u7ceb", "\u7cf5", "\u7d4d", "\u7d57", "\u7d59", "\u7d5a", "\u7d5d", "\u7d65", "\u7d82", "\u7d8b", "\u7d97", "\u7db3", "\u7db6", "\u7dcd", "\u7e00", "\u7de2", "\u7de5", "\u7deb", "\u7ded", "\u7df5", "\u7e27", "\u7e28", "\u7e2c", "\u7e4e", "\u7e65", "\u7e6e", "\u7f3c", "\u7f64", "\u7f90", "\u7f97", "\u7faa", "\u7fb4", "\u7ffa", "\u802e", "\u8060", "\u8066", "\u806d", "\u808e", "\u80d2", "\u8120", "\u813c", "\u8145", "\u8184", "\u8185", "\u8196", "\u81ce", "\u81f0", "\u81f1", "\u81f6", "\u8219", "\u821a", "\u8267", "\u82fd", "\u831f", "\u8321", "\u8357", "\u8380", "\u8382", "\u8384", "\u8415", "\u844f", "\u8481", "\u8492", "\u8493", "\u8495", "\u84a6", "\u8532", "\u8533", "\u8534", "\u8536", "\u853f", "\u854f", "\u856f", "\u8593", "\u85bc", "\u85e0", "\u85f3", "\u860d", "\u860e", "\u8610", "\u8642", "\u8657", "\u8658", "\u8675", "\u8676", "\u8688", "\u8745", "\u8799", "\u87ce", "\u87d5", "\u87d6", "\u87da", "\u87f1", "\u87f8", "\u8812", "\u881e", "\u882d", "\u8849", "\u8851", "\u885c", "\u885f", "\u8860", "\u88a0", "\u890d", "\u890f", "\u8920", "\u8939", "\u893a", "\u8940", "\u8970", "\u8975", "\u8989", "\u898d", "\u8990", "\u8994", "\u89a0", "\u89a5", "\u89b0", "\u89b4", "\u89b5", "\u89bc", "\u89f9", "\u89fd", "\u8a05", "\u8a14", "\u8a20", "\u8a24", "\u8a26", "\u8a2b", "\u8a2f", "\u8a35", "\u8a3d", "\u8a43", "\u8a47", "\u8a53", "\u8a5c", "\u8a5d", "\u8a65", "\u8a67", "\u8a7e", "\u8a80", "\u8a90", "\u8a97", "\u8a9f", "\u8aa9", "\u8aae", "\u8aaf", "\u8ab3", "\u8ab7", "\u8aca", "\u8aec", "\u8b1f", "\u8b2d", "\u8b4d", "\u8b5e", "\u8b76", "\u8b7c", "\u8b81", "\u8b8d", "\u8b8f", "\u8c51", "\u8c53", "\u8c7e", "\u8c9b", "\u8cc6", "\u8cc9", "\u8ccb", "\u8cd6", "\u8cef", "\u8cf2", "\u8cf7", "\u8cff", "\u8d01", "\u8d03", "\u8d7f", "\u8d9e", "\u8da6", "\u8e01", "\u8e4f", "\u8e79", "\u8e9b", "\u8ea2", "\u8ea7", "\u8eb5", "\u8ec1", "\u8ec4", "\u8ec7", "\u8ef0", "\u8eed", "\u8f0f", "\u8f21", "\u8f27", "\u8f28", "\u8f2d", "\u8f3a", "\u8f41", "\u8f65", "\u8fca", "\u9028", "\u9029", "\u902a", "\u902c", "\u9033", "\u904c", "\u908e", "\u9125", "\u9137", "\u913c", "\u913d", "\u9194", "\u9195", "\u9198", "\u91a6", "\u91bf", "\u91fb", "\u9213", "\u9218", "\u921d", "\u9228", "\u922f", "\u9235", "\u9242", "\u9243", "\u9247", "\u9258", "\u925c", "\u925d", "\u9268", "\u9269", "\u926e", "\u9289", "\u9292", "\u929f", "\u92b8", "\u92ba", "\u92bd", "\u92bf", "\u92dc", "\u92e3", "\u92e5", "\u92ec", "\u9311", "\u931c", "\u9337", "\u9369", "\u936f", "\u9373", "\u9374", "\u937d", "\u937f", "\u9381", "\u938b", "\u93ab", "\u93b6", "\u93ba", "\u93c1", "\u93c5", "\u93c9", "\u93d3", "\u9401", "\u9402", "\u9404", "\u9408", "\u9417", "\u941f", "\u9434", "\u9443", "\u9459", "\u945c", "\u945f", "\u9461", "\u9484", "\u9578", "\u9579", "\u957e", "\u9584", "\u959d", "\u95a6", "\u95b4", "\u95d9", "\u95dd", "\u95e6", "\u9625", "\u9626", "\u966e", "\u967b", "\u967f", "\u9681", "\u9682", "\u969f", "\u96a5", "\u96a6", "\u971a", "\u971b", "\u9741", "\u974a", "\u974e", "\u9789", "\u97b8", "\u97ba", "\u97bc", "\u97be", "\u97ca", "\u97d1", "\u97e0", "\u97db", "\u97ef", "\u9819", "\u9814", "\u9823", "\u982e", "\u9833", "\u9825", "\u983e", "\u9847", "\u9856", "\u985a", "\u9866", "\u986c", "\u98ab", "\u98b0", "\u98b4", "\u98b7", "\u98c5", "\u98c8", "\u98e1", "\u98f3", "\u991c", "\u9922", "\u9926", "\u9939", "\u993b", "\u9940", "\u9946", "\u994d", "\u9960", "\u999b", "\u999f", "\u99bf", "\u99da", "\u99de", "\u99eb", "\u99f5", "\u9a0c", "\u9a10", "\u9a33", "\u9a47", "\u9a4b", "\u9a51", "\u9a5d", "\u9aaa", "\u9aac", "\u9aae", "\u9ac8", "\u9af5", "\u9aff", "\u9b1b", "\u9b1c", "\u9b26", "\u9b2d", "\u9b34", "\u9b39", "\u9b57", "\u9b5e", "\u9b63", "\u9b65", "\u9b6a", "\u9b73", "\u9b78", "\u9b79", "\u9b7f", "\u9b84", "\u9b89", "\u9b8a", "\u9b8b", "\u9b8d", "\u9b94", "\u9b9d", "\u9ba7", "\u9ba9", "\u9bac", "\u9bb0", "\u9bb2", "\u9bb7", "\u9bbc", "\u9bbe", "\u9bce", "\u9bd0", "\u9bd8", "\u9bdd", "\u9bdf", "\u9bef", "\u9bf3", "\u9bf9", "\u9bfa", "\u9bff", "\u9c02", "\u9c0f", "\u9c11", "\u9c16", "\u9c18", "\u9c19", "\u9c1a", "\u9c1e", "\u9c22", "\u9c26", "\u9c35", "\u9c43", "\u9c45", "\u9c4f", "\u9c53", "\u9c5b", "\u9c5d", "\u9c69", "\u9c6a", "\u9c5c", "\u9c6b", "\u9c70", "\u9c72", "\u9d0b", "\u9d02", "\u9d11", "\u9d1c", "\u9d32", "\u9d34", "\u9d3a", "\u9d3c", "\u9d47", "\u9d63", "\u9d62", "\u9d65", "\u9d76", "\u9d7c", "\u9d7e", "\u9d83", "\u9d8d", "\u9d8e", "\u9d93", "\u9d95", "\u9dae", "\u9dc9", "\u9dd4", "\u9de0", "\u9de7", "\u9e0a", "\u9e0e", "\u9e16", "\u9e1c", "\u9e7b", "\u9e8f", "\u9e96", "\u9e98", "\u9eac", "\u9eaf", "\u9eb3", "\u9ef1", "\u9ef8", "\u9f02", "\u9f03", "\u9f1f", "\u9f26", "\u9f53", "\u9f5a", "\u9f68", "\u9f69", "\u9f6d", "\u9f73", "\u9f7d", "\u9f8f", "\u9f96", "\u9f97", "\u9fa3", "\u9fa5", "\uac02", "\uac03", "\uac05", "\uac06", "\uac0b", "\uac18", "\uac1e", "\uac1f", "\uac21", "\uac22", "\uac23", "\uac25", "\uac2e", "\uac32", "\uac33", "\uac34", "\uac35", "\uac36", "\uac37", "\uac3a", "\uac3b", "\uac3d", "\uac3e", "\uac3f", "\uac41", "\uac4c", "\uac4e", "\uac55", "\uac56", "\uac57", "\uac59", "\uac5a", "\uac5b", "\uac5d", "\uac72", "\uac73", "\uac75", "\uac76", "\uac79", "\uac7b", "\uac82", "\uac87", "\uac88", "\uac8d", "\uac8e", "\uac8f", "\uac91", "\uac92", "\uac93", "\uac95", "\uac9e", "\uaca2", "\uacab", "\uacad", "\uacae", "\uacb1", "\uacba", "\uacbe", "\uacbf", "\uacc0", "\uacc2", "\uacc3", "\uacc5", "\uacc6", "\uacc7", "\uacc9", "\uacca", "\uaccb", "\uaccd", "\uacd6", "\uacd8", "\uace2", "\uace3", "\uace5", "\uace6", "\uace9", "\uaceb", "\uaced", "\uacee", "\uacf2", "\uacf4", "\uacf7", "\uacfe", "\uacff", "\uad01", "\uad02", "\uad03", "\uad05", "\uad07", "\uad0e", "\uad10", "\uad12", "\uad13", "\uad14", "\uad15", "\uad16", "\uad17", "\uad19", "\uad1a", "\uad1b", "\uad1d", "\uad1e", "\uad1f", "\uad21", "\uad2a", "\uad2b", "\uad2e", "\uad36", "\uad37", "\uad39", "\uad3a", "\uad3b", "\uad3d", "\uad46", "\uad48", "\uad4a", "\uad51", "\uad52", "\uad53", "\uad55", "\uad56", "\uad57", "\uad59", "\uad62", "\uad64", "\uad6e", "\uad6f", "\uad71", "\uad72", "\uad77", "\uad78", "\uad79", "\uad7a", "\uad7e", "\uad80", "\uad83", "\uad8a", "\uad8b", "\uad8d", "\uad8e", "\uad8f", "\uad91", "\uad9e", "\uada5", "\uadb8", "\uadc2", "\uadc3", "\uadc5", "\uadc6", "\uadc7", "\uadc9", "\uadd2", "\uadd4", "\uaddd", "\uadde", "\uaddf", "\uade1", "\uade2", "\uade3", "\uade5", "\uadfa", "\uadfb", "\uadfd", "\uadfe", "\uae02", "\uae0a", "\uae0c", "\uae0e", "\uae15", "\uae1d", "\uae32", "\uae33", "\uae35", "\uae36", "\uae39", "\uae3b", "\uae3c", "\uae3d", "\uae3e", "\uae3f", "\uae42", "\uae44", "\uae47", "\uae48", "\uae49", "\uae4b", "\uae4f", "\uae51", "\uae52", "\uae53", "\uae55", "\uae57", "\uae5e", "\uae62", "\uae63", "\uae64", "\uae66", "\uae67", "\uae6a", "\uae6b", "\uae6d", "\uae6e", "\uae6f", "\uae71", "\uae7a", "\uae7e", "\uae86", "\uae8d", "\uaebf", "\uaec1", "\uaec2", "\uaec3", "\uaec5", "\uaece", "\uaed2", "\uaeda", "\uaedb", "\uaedd", "\uaee6", "\uaee7", "\uaee9", "\uaeea", "\uaeec", "\uaeee", "\uaef5", "\uaef6", "\uaef7", "\uaef9", "\uaefa", "\uaefb", "\uaefd", "\uaf06", "\uaf09", "\uaf0a", "\uaf0b", "\uaf0c", "\uaf0e", "\uaf0f", "\uaf11", "\uaf24", "\uaf2e", "\uaf2f", "\uaf31", "\uaf33", "\uaf35", "\uaf3e", "\uaf40", "\uaf44", "\uaf45", "\uaf46", "\uaf47", "\uaf4a", "\uaf51", "\uaf5e", "\uaf66", "\uaf7a", "\uaf81", "\uaf82", "\uaf83", "\uaf85", "\uaf86", "\uaf87", "\uaf89", "\uaf92", "\uaf93", "\uaf94", "\uaf96", "\uaf9d", "\uafba", "\uafbb", "\uafbd", "\uafbe", "\uafbf", "\uafc1", "\uafca", "\uafcc", "\uafcf", "\uafd5", "\uafdd", "\uafe2", "\uafea", "\uaff2", "\uaff3", "\uaff5", "\uaff6", "\uaff7", "\uaff9", "\ub002", "\ub003", "\ub005", "\ub00d", "\ub00e", "\ub00f", "\ub011", "\ub012", "\ub013", "\ub015", "\ub01e", "\ub029", "\ub046", "\ub047", "\ub049", "\ub04b", "\ub04d", "\ub04f", "\ub050", "\ub051", "\ub052", "\ub056", "\ub058", "\ub05a", "\ub05b", "\ub05c", "\ub05e", "\ub07e", "\ub07f", "\ub081", "\ub082", "\ub083", "\ub085", "\ub08e", "\ub090", "\ub092", "\ub09b", "\ub09d", "\ub09e", "\ub0a3", "\ub0a4", "\ub0a5", "\ub0a6", "\ub0a7", "\ub0aa", "\ub0b0", "\ub0b2", "\ub0b6", "\ub0b7", "\ub0b9", "\ub0ba", "\ub0bb", "\ub0bd", "\ub0c6", "\ub0ca", "\ub0d2", "\ub0d3", "\ub0d5", "\ub0d6", "\ub0d7", "\ub0d9", "\ub0e1", "\ub0e2", "\ub0e3", "\ub0e4", "\ub0e6", "\ub0f1", "\ub10a", "\ub10d", "\ub10e", "\ub10f", "\ub111", "\ub114", "\ub115", "\ub116", "\ub117", "\ub11a", "\ub11e", "\ub126", "\ub127", "\ub129", "\ub12a", "\ub12b", "\ub12d", "\ub136", "\ub13a", "\ub142", "\ub143", "\ub145", "\ub146", "\ub147", "\ub149", "\ub152", "\ub153", "\ub156", "\ub157", "\ub159", "\ub15a", "\ub15b", "\ub15d", "\ub15e", "\ub15f", "\ub161", "\ub17a", "\ub17b", "\ub17d", "\ub17e", "\ub17f", "\ub181", "\ub183", "\ub18a", "\ub18c", "\ub18e", "\ub18f", "\ub190", "\ub191", "\ub195", "\ub196", "\ub197", "\ub199", "\ub19a", "\ub19b", "\ub19d", "\ub19e", "\ub1a9", "\ub1b9", "\ub1cd", "\ub1ce", "\ub1cf", "\ub1d1", "\ub1d2", "\ub1d3", "\ub1d5", "\ub1d6", "\ub1de", "\ub1e0", "\ub1ea", "\ub1eb", "\ub1ed", "\ub1ee", "\ub1ef", "\ub1f1", "\ub1fa", "\ub1fc", "\ub1fe", "\ub206", "\ub207", "\ub209", "\ub20a", "\ub20d", "\ub216", "\ub218", "\ub21a", "\ub221", "\ub235", "\ub23d", "\ub259", "\ub25a", "\ub25b", "\ub25d", "\ub25e", "\ub25f", "\ub261", "\ub26a", "\ub26f", "\ub276", "\ub27d", "\ub286", "\ub287", "\ub288", "\ub28a", "\ub28f", "\ub292", "\ub293", "\ub295", "\ub296", "\ub297", "\ub29b", "\ub2a2", "\ub2a4", "\ub2a7", "\ub2a8", "\ub2a9", "\ub2ab", "\ub2ad", "\ub2ae", "\ub2af", "\ub2b1", "\ub2b2", "\ub2b3", "\ub2b5", "\ub2b6", "\ub2b7", "\ub2b8", "\ub2ca", "\ub2cb", "\ub2cd", "\ub2ce", "\ub2cf", "\ub2d1", "\ub2d3", "\ub2da", "\ub2dc", "\ub2de", "\ub2df", "\ub2e0", "\ub2e1", "\ub2e3", "\ub2e7", "\ub2e9", "\ub2ea", "\ub2f0", "\ub2f1", "\ub2f2", "\ub2f6", "\ub2fc", "\ub2fd", "\ub2fe", "\ub302", "\ub303", "\ub305", "\ub306", "\ub307", "\ub309", "\ub312", "\ub316", "\ub31d", "\ub357", "\ub359", "\ub35a", "\ub35d", "\ub360", "\ub361", "\ub362", "\ub363", "\ub366", "\ub368", "\ub36a", "\ub36c", "\ub36d", "\ub36f", "\ub372", "\ub373", "\ub375", "\ub376", "\ub377", "\ub379", "\ub382", "\ub386", "\ub38d", "\ub38e", "\ub38f", "\ub391", "\ub392", "\ub393", "\ub395", "\ub3a2", "\ub3a9", "\ub3aa", "\ub3ab", "\ub3ad", "\ub3ae", "\ub3c6", "\ub3c7", "\ub3c9", "\ub3ca", "\ub3cd", "\ub3cf", "\ub3d1", "\ub3d2", "\ub3d3", "\ub3d6", "\ub3d8", "\ub3da", "\ub3dc", "\ub3de", "\ub3df", "\ub3e1", "\ub3e2", "\ub3e3", "\ub3e5", "\ub3e6", "\ub3e7", "\ub3e9", "\ub3fd", "\ub411", "\ub419", "\ub41a", "\ub41b", "\ub41d", "\ub41e", "\ub41f", "\ub421", "\ub42a", "\ub42c", "\ub435", "\ub445", "\ub452", "\ub453", "\ub455", "\ub456", "\ub457", "\ub459", "\ub462", "\ub464", "\ub466", "\ub467", "\ub46d", "\ub481", "\ub482", "\ub483", "\ub489", "\ub49e", "\ub4a5", "\ub4a6", "\ub4a7", "\ub4a9", "\ub4aa", "\ub4ab", "\ub4ad", "\ub4b6", "\ub4b8", "\ub4ba", "\ub4c1", "\ub4c2", "\ub4c3", "\ub4c5", "\ub4c6", "\ub4c7", "\ub4c9", "\ub4d1", "\ub4d2", "\ub4d3", "\ub4d4", "\ub4d6", "\ub4de", "\ub4df", "\ub4e1", "\ub4e2", "\ub4e5", "\ub4e7", "\ub4ee", "\ub4f0", "\ub4f2", "\ub4f9", "\ub516", "\ub517", "\ub519", "\ub51a", "\ub51d", "\ub51e", "\ub526", "\ub52b", "\ub532", "\ub533", "\ub535", "\ub536", "\ub537", "\ub539", "\ub542", "\ub546", "\ub547", "\ub548", "\ub549", "\ub54a", "\ub54e", "\ub54f", "\ub551", "\ub552", "\ub553", "\ub555", "\ub55e", "\ub562", "\ub56b", "\ub5a2", "\ub5a3", "\ub5a5", "\ub5a6", "\ub5a7", "\ub5a9", "\ub5ac", "\ub5ad", "\ub5ae", "\ub5af", "\ub5b2", "\ub5b6", "\ub5be", "\ub5bf", "\ub5c1", "\ub5c2", "\ub5c3", "\ub5c5", "\ub5ce", "\ub5d2", "\ub5d9", "\ub5ed", "\ub600", "\ub612", "\ub613", "\ub615", "\ub616", "\ub617", "\ub619", "\ub61e", "\ub626", "\ub62d", "\ub635", "\ub63b", "\ub649", "\ub665", "\ub666", "\ub667", "\ub669", "\ub69e", "\ub69f", "\ub6a1", "\ub6a2", "\ub6a3", "\ub6a5", "\ub6ad", "\ub6ae", "\ub6af", "\ub6b0", "\ub6b2", "\ub6c3", "\ub6d5", "\ub6de", "\ub6f1", "\ub6f2", "\ub6f3", "\ub6f5", "\ub6f6", "\ub6f7", "\ub6f9", "\ub6fa", "\ub6fb", "\ub702", "\ub703", "\ub704", "\ub706", "\ub72a", "\ub72b", "\ub72d", "\ub72e", "\ub731", "\ub73a", "\ub73c", "\ub745", "\ub746", "\ub747", "\ub749", "\ub74a", "\ub74b", "\ub74d", "\ub756", "\ub761", "\ub762", "\ub763", "\ub765", "\ub766", "\ub767", "\ub769", "\ub772", "\ub774", "\ub776", "\ub77e", "\ub77f", "\ub781", "\ub782", "\ub783", "\ub785", "\ub78e", "\ub793", "\ub794", "\ub795", "\ub79a", "\ub79b", "\ub79d", "\ub79e", "\ub79f", "\ub7a1", "\ub7aa", "\ub7ae", "\ub7b6", "\ub7b7", "\ub7b9", "\ub7c2", "\ub7c8", "\ub7ca", "\ub7de", "\ub7ee", "\ub7ef", "\ub7f1", "\ub7f2", "\ub7f3", "\ub7f5", "\ub7fe", "\ub802", "\ub80a", "\ub80b", "\ub80d", "\ub80e", "\ub80f", "\ub811", "\ub81a", "\ub81c", "\ub81e", "\ub826", "\ub827", "\ub829", "\ub82a", "\ub82b", "\ub82d", "\ub836", "\ub83a", "\ub841", "\ub842", "\ub843", "\ub845", "\ub852", "\ub854", "\ub85e", "\ub85f", "\ub861", "\ub862", "\ub863", "\ub865", "\ub86e", "\ub870", "\ub872", "\ub879", "\ub87a", "\ub87b", "\ub87d", "\ub885", "\ub88e", "\ub8a0", "\ub8a9", "\ub8b1", "\ub8b2", "\ub8b3", "\ub8b5", "\ub8b6", "\ub8b7", "\ub8b9", "\ub8be", "\ub8bf", "\ub8c2", "\ub8c4", "\ub8c6", "\ub8cd", "\ub8ce", "\ub8cf", "\ub8d1", "\ub8d2", "\ub8d3", "\ub8d5", "\ub8de", "\ub8e0", "\ub8e2", "\ub8ea", "\ub8eb", "\ub8ed", "\ub8ee", "\ub8ef", "\ub8f1", "\ub8fa", "\ub8fc", "\ub8fe", "\ub905", "\ub919", "\ub921", "\ub93e", "\ub93f", "\ub941", "\ub942", "\ub943", "\ub945", "\ub94d", "\ub94e", "\ub950", "\ub952", "\ub95a", "\ub95b", "\ub95d", "\ub95e", "\ub95f", "\ub961", "\ub96a", "\ub96c", "\ub96e", "\ub976", "\ub977", "\ub979", "\ub97a", "\ub97b", "\ub97d", "\ub97e", "\ub986", "\ub988", "\ub98b", "\ub98c", "\ub98f", "\ub99f", "\ub9ae", "\ub9af", "\ub9b1", "\ub9b2", "\ub9b3", "\ub9b5", "\ub9be", "\ub9c0", "\ub9c2", "\ub9ca", "\ub9cb", "\ub9cd", "\ub9d3", "\ub9da", "\ub9dc", "\ub9df", "\ub9e0", "\ub9e2", "\ub9e6", "\ub9e7", "\ub9e9", "\ub9ea", "\ub9eb", "\ub9ed", "\ub9f6", "\ub9fb", "\uba02", "\uba09", "\uba16", "\uba3a", "\uba3b", "\uba3d", "\uba3e", "\uba3f", "\uba41", "\uba43", "\uba44", "\uba45", "\uba46", "\uba47", "\uba4a", "\uba4c", "\uba4f", "\uba50", "\uba51", "\uba52", "\uba56", "\uba57", "\uba59", "\uba5a", "\uba5b", "\uba5d", "\uba66", "\uba6a", "\uba72", "\uba73", "\uba75", "\uba76", "\uba77", "\uba79", "\uba86", "\uba88", "\uba89", "\uba8a", "\uba8b", "\uba8d", "\uba93", "\ubaaa", "\ubaad", "\ubaae", "\ubaaf", "\ubab1", "\ubab3", "\ubaba", "\ubabc", "\ubabe", "\ubac5", "\ubac6", "\ubac7", "\ubac9", "\ubada", "\ubafd", "\ubafe", "\ubaff", "\ubb01", "\ubb02", "\ubb03", "\ubb05", "\ubb0e", "\ubb10", "\ubb12", "\ubb19", "\ubb1a", "\ubb1b", "\ubb1d", "\ubb1e", "\ubb1f", "\ubb21", "\ubb28", "\ubb2a", "\ubb2c", "\ubb37", "\ubb39", "\ubb3a", "\ubb3f", "\ubb46", "\ubb48", "\ubb4a", "\ubb4b", "\ubb4c", "\ubb4e", "\ubb51", "\ubb52", "\ubb53", "\ubb55", "\ubb56", "\ubb57", "\ubb59", "\ubb62", "\ubb64", "\ubb6d", "\ubb72", "\ubb89", "\ubb8a", "\ubb8b", "\ubb8d", "\ubb8e", "\ubb8f", "\ubb91", "\ubba5", "\ubba6", "\ubba7", "\ubba9", "\ubbaa", "\ubbab", "\ubbad", "\ubbb5", "\ubbb6", "\ubbb8", "\ubbc1", "\ubbc2", "\ubbc3", "\ubbc5", "\ubbc6", "\ubbc7", "\ubbc9", "\ubbd1", "\ubbd2", "\ubbd4", "\ubbfa", "\ubbfb", "\ubbfd", "\ubbfe", "\ubc01", "\ubc03", "\ubc0a", "\ubc0e", "\ubc10", "\ubc12", "\ubc13", "\ubc19", "\ubc1a", "\ubc20", "\ubc21", "\ubc22", "\ubc23", "\ubc26", "\ubc28", "\ubc2a", "\ubc2b", "\ubc2c", "\ubc2e", "\ubc2f", "\ubc32", "\ubc33", "\ubc35", "\ubc36", "\ubc37", "\ubc39", "\ubc42", "\ubc46", "\ubc47", "\ubc48", "\ubc4a", "\ubc4b", "\ubc4e", "\ubc4f", "\ubc51", "\ubc5a", "\ubc5b", "\ubc5c", "\ubc5e", "\ubc86", "\ubc87", "\ubc89", "\ubc8a", "\ubc8d", "\ubc8f", "\ubc96", "\ubc98", "\ubc9b", "\ubca2", "\ubca3", "\ubca5", "\ubca6", "\ubca9", "\ubcb2", "\ubcb6", "\ubcbe", "\ubcbf", "\ubcc1", "\ubcc2", "\ubcc3", "\ubcc5", "\ubcce", "\ubcd2", "\ubcd3", "\ubcd4", "\ubcd6", "\ubcd7", "\ubcd9", "\ubcda", "\ubcdb", "\ubcdd", "\ubcf7", "\ubcf9", "\ubcfa", "\ubcfb", "\ubcfd", "\ubcfe", "\ubd06", "\ubd08", "\ubd0a", "\ubd11", "\ubd12", "\ubd13", "\ubd15", "\ubd1e", "\ubd25", "\ubd2d", "\ubd3a", "\ubd41", "\ubd4a", "\ubd4b", "\ubd4d", "\ubd4e", "\ubd4f", "\ubd51", "\ubd5a", "\ubd65", "\ubd66", "\ubd67", "\ubd69", "\ubd82", "\ubd83", "\ubd85", "\ubd86", "\ubd8b", "\ubd92", "\ubd94", "\ubd96", "\ubd97", "\ubd98", "\ubd9b", "\ubd9d", "\ubda5", "\ubdb1", "\ubdb9", "\ubdd2", "\ubdd3", "\ubdd6", "\ubdd7", "\ubdd9", "\ubdda", "\ubddb", "\ubddd", "\ubdea", "\ubdf1", "\ubdf2", "\ubdf3", "\ubdf5", "\ubdf6", "\ubdf7", "\ubdf9", "\ube01", "\ube02", "\ube04", "\ube06", "\ube0e", "\ube0f", "\ube11", "\ube12", "\ube13", "\ube15", "\ube1e", "\ube20", "\ube46", "\ube47", "\ube49", "\ube4a", "\ube4b", "\ube4d", "\ube4f", "\ube56", "\ube58", "\ube5c", "\ube5d", "\ube5e", "\ube5f", "\ube62", "\ube63", "\ube65", "\ube66", "\ube67", "\ube69", "\ube6b", "\ube72", "\ube76", "\ube7e", "\ube7f", "\ube81", "\ube82", "\ube83", "\ube85", "\ube8e", "\ube92", "\ube9a", "\ubea9", "\ubeb8", "\ubed2", "\ubed3", "\ubed5", "\ubed6", "\ubed9", "\ubee1", "\ubee2", "\ubee6", "\ubeed", "\ubef6", "\ubf02", "\ubf0a", "\ubf1a", "\ubf1e", "\ubf42", "\ubf43", "\ubf45", "\ubf46", "\ubf47", "\ubf49", "\ubf52", "\ubf53", "\ubf54", "\ubf56", "\ubf83", "\ubf95", "\ubf9e", "\ubfb1", "\ubfb9", "\ubfc6", "\ubfce", "\ubfcf", "\ubfd1", "\ubfd2", "\ubfd3", "\ubfd5", "\ubfdd", "\ubfde", "\ubfe0", "\ubfe2", "\uc03d", "\uc03e", "\uc03f", "\uc040", "\uc052", "\uc059", "\uc05a", "\uc05b", "\uc05d", "\uc05e", "\uc05f", "\uc061", "\uc06a", "\uc07a", "\uc092", "\uc093", "\uc095", "\uc096", "\uc097", "\uc099", "\uc0a2", "\uc0a4", "\uc0a6", "\uc0ae", "\uc0b1", "\uc0b2", "\uc0b7", "\uc0be", "\uc0c2", "\uc0c3", "\uc0c4", "\uc0c6", "\uc0c7", "\uc0ca", "\uc0cb", "\uc0cd", "\uc0ce", "\uc0cf", "\uc0d1", "\uc0da", "\uc0de", "\uc0e6", "\uc0e7", "\uc0e9", "\uc0ea", "\uc0eb", "\uc0ed", "\uc0f6", "\uc0f8", "\uc0fa", "\uc101", "\uc102", "\uc103", "\uc105", "\uc106", "\uc107", "\uc109", "\uc111", "\uc112", "\uc113", "\uc114", "\uc116", "\uc121", "\uc122", "\uc125", "\uc128", "\uc129", "\uc12a", "\uc12b", "\uc12e", "\uc132", "\uc133", "\uc134", "\uc135", "\uc137", "\uc13a", "\uc13b", "\uc13d", "\uc13e", "\uc13f", "\uc141", "\uc14a", "\uc14e", "\uc156", "\uc157", "\uc159", "\uc15a", "\uc15b", "\uc15d", "\uc166", "\uc16a", "\uc171", "\uc172", "\uc173", "\uc175", "\uc176", "\uc177", "\uc179", "\uc17a", "\uc17b", "\uc17c", "\uc186", "\uc18f", "\uc191", "\uc192", "\uc193", "\uc195", "\uc197", "\uc19e", "\uc1a0", "\uc1a2", "\uc1a3", "\uc1a4", "\uc1a6", "\uc1a7", "\uc1aa", "\uc1ab", "\uc1ad", "\uc1ae", "\uc1af", "\uc1b1", "\uc1be", "\uc1c5", "\uc1c6", "\uc1c7", "\uc1c9", "\uc1ca", "\uc1cb", "\uc1cd", "\uc1d5", "\uc1d6", "\uc1d9", "\uc1e1", "\uc1e2", "\uc1e3", "\uc1e5", "\uc1e6", "\uc1e7", "\uc1e9", "\uc1f2", "\uc1f4", "\uc1fe", "\uc1ff", "\uc201", "\uc202", "\uc203", "\uc205", "\uc20e", "\uc210", "\uc212", "\uc21a", "\uc21b", "\uc21d", "\uc21e", "\uc221", "\uc222", "\uc223", "\uc224", "\uc225", "\uc226", "\uc227", "\uc22a", "\uc22c", "\uc22e", "\uc230", "\uc233", "\uc235", "\uc246", "\uc247", "\uc249", "\uc252", "\uc253", "\uc255", "\uc256", "\uc257", "\uc259", "\uc261", "\uc262", "\uc263", "\uc264", "\uc266", "\uc267", "\uc26e", "\uc26f", "\uc271", "\uc272", "\uc273", "\uc275", "\uc27e", "\uc280", "\uc282", "\uc28a", "\uc291", "\uc299", "\uc29a", "\uc29c", "\uc29e", "\uc2a6", "\uc2a7", "\uc2a9", "\uc2aa", "\uc2ab", "\uc2ae", "\uc2b6", "\uc2b8", "\uc2ba", "\uc2de", "\uc2df", "\uc2e1", "\uc2e2", "\uc2e5", "\uc2ee", "\uc2f0", "\uc2f2", "\uc2f3", "\uc2f4", "\uc2f5", "\uc2f7", "\uc2fa", "\uc2fd", "\uc2fe", "\uc2ff", "\uc301", "\uc30a", "\uc30b", "\uc30e", "\uc30f", "\uc310", "\uc311", "\uc312", "\uc316", "\uc317", "\uc319", "\uc31a", "\uc31b", "\uc31d", "\uc326", "\uc327", "\uc32a", "\uc333", "\uc346", "\uc34e", "\uc36a", "\uc36b", "\uc36d", "\uc36e", "\uc36f", "\uc371", "\uc373", "\uc37a", "\uc37b", "\uc37e", "\uc385", "\uc386", "\uc387", "\uc389", "\uc38a", "\uc38b", "\uc38d", "\uc3c1", "\uc3da", "\uc3db", "\uc3dd", "\uc3de", "\uc3e1", "\uc3e3", "\uc3ea", "\uc3eb", "\uc3ec", "\uc3ee", "\uc3f6", "\uc3f7", "\uc3f9", "\uc3ff", "\uc409", "\uc411", "\uc41b", "\uc425", "\uc42d", "\uc42e", "\uc42f", "\uc431", "\uc432", "\uc433", "\uc435", "\uc43e", "\uc449", "\uc466", "\uc467", "\uc469", "\uc46a", "\uc46b", "\uc46d", "\uc476", "\uc477", "\uc478", "\uc47a", "\uc481", "\uc495", "\uc49d", "\uc4aa", "\uc4b9", "\uc4ba", "\uc4bb", "\uc4bd", "\uc4c6", "\uc4e0", "\uc4ea", "\uc4f2", "\uc4f3", "\uc4f5", "\uc4f6", "\uc4f7", "\uc4f9", "\uc4fb", "\uc4fc", "\uc4fd", "\uc4fe", "\uc502", "\uc50d", "\uc50e", "\uc50f", "\uc511", "\uc512", "\uc513", "\uc515", "\uc51d", "\uc52a", "\uc52b", "\uc52d", "\uc52e", "\uc52f", "\uc531", "\uc53a", "\uc53c", "\uc53e", "\uc546", "\uc547", "\uc54b", "\uc54f", "\uc550", "\uc551", "\uc552", "\uc556", "\uc55a", "\uc55b", "\uc55c", "\uc55f", "\uc562", "\uc563", "\uc565", "\uc566", "\uc567", "\uc569", "\uc572", "\uc576", "\uc57e", "\uc57f", "\uc581", "\uc582", "\uc583", "\uc585", "\uc586", "\uc588", "\uc589", "\uc58a", "\uc58b", "\uc58e", "\uc590", "\uc592", "\uc593", "\uc594", "\uc596", "\uc599", "\uc59a", "\uc59b", "\uc59d", "\uc59e", "\uc59f", "\uc5a1", "\uc5aa", "\uc5b6", "\uc5b7", "\uc5ba", "\uc5bf", "\uc5cb", "\uc5cd", "\uc5cf", "\uc5d2", "\uc5d3", "\uc5d5", "\uc5d6", "\uc5d7", "\uc5d9", "\uc5e2", "\uc5e4", "\uc5e6", "\uc5e7", "\uc5e8", "\uc5e9", "\uc5ea", "\uc5eb", "\uc5ef", "\uc5f1", "\uc5f2", "\uc5f3", "\uc5f5", "\uc5f8", "\uc5f9", "\uc5fa", "\uc5fb", "\uc602", "\uc603", "\uc604", "\uc609", "\uc60a", "\uc60b", "\uc60d", "\uc60e", "\uc60f", "\uc611", "\uc61a", "\uc61d", "\uc626", "\uc627", "\uc629", "\uc62a", "\uc62b", "\uc62f", "\uc631", "\uc632", "\uc636", "\uc638", "\uc63a", "\uc63c", "\uc63d", "\uc63e", "\uc63f", "\uc642", "\uc643", "\uc645", "\uc646", "\uc647", "\uc649", "\uc652", "\uc656", "\uc65e", "\uc65f", "\uc661", "\uc66d", "\uc66e", "\uc670", "\uc672", "\uc67a", "\uc67b", "\uc67d", "\uc67e", "\uc67f", "\uc681", "\uc68a", "\uc68c", "\uc68e", "\uc696", "\uc697", "\uc699", "\uc69a", "\uc69b", "\uc69d", "\uc6a6", "\uc6a8", "\uc6aa", "\uc6b2", "\uc6b3", "\uc6b5", "\uc6b6", "\uc6b7", "\uc6bb", "\uc6c2", "\uc6c4", "\uc6c6", "\uc6ce", "\uc6cf", "\uc6d1", "\uc6d2", "\uc6d3", "\uc6d5", "\uc6de", "\uc6df", "\uc6e2", "\uc6ea", "\uc6eb", "\uc6ed", "\uc6ee", "\uc6ef", "\uc6f1", "\uc6f2", "\uc6f3", "\uc6fa", "\uc6fb", "\uc6fc", "\uc6fe", "\uc706", "\uc707", "\uc709", "\uc70a", "\uc70b", "\uc70d", "\uc716", "\uc718", "\uc71a", "\uc722", "\uc723", "\uc725", "\uc726", "\uc727", "\uc729", "\uc732", "\uc734", "\uc736", "\uc738", "\uc739", "\uc73a", "\uc73b", "\uc73e", "\uc73f", "\uc741", "\uc742", "\uc743", "\uc745", "\uc74b", "\uc74e", "\uc750", "\uc759", "\uc75a", "\uc75b", "\uc75d", "\uc75e", "\uc75f", "\uc761", "\uc769", "\uc76a", "\uc76c", "\uc776", "\uc777", "\uc779", "\uc77a", "\uc77b", "\uc77f", "\uc780", "\uc781", "\uc782", "\uc786", "\uc78b", "\uc78c", "\uc78d", "\uc78f", "\uc792", "\uc793", "\uc795", "\uc799", "\uc79b", "\uc7a2", "\uc7a7", "\uc7ae", "\uc7af", "\uc7b1", "\uc7b2", "\uc7b3", "\uc7b5", "\uc7b6", "\uc7b7", "\uc7b8", "\uc7b9", "\uc7ba", "\uc7bb", "\uc7be", "\uc7c2", "\uc7ca", "\uc7cb", "\uc7cd", "\uc7cf", "\uc7d1", "\uc7d9", "\uc7da", "\uc7db", "\uc7dc", "\uc7de", "\uc7e5", "\uc7e6", "\uc7e7", "\uc7e9", "\uc7ea", "\uc7eb", "\uc7ed", "\uc7fb", "\uc802", "\uc803", "\uc805", "\uc806", "\uc807", "\uc809", "\uc80b", "\uc812", "\uc814", "\uc817", "\uc81e", "\uc81f", "\uc821", "\uc822", "\uc823", "\uc825", "\uc82e", "\uc830", "\uc832", "\uc839", "\uc83a", "\uc83b", "\uc83d", "\uc83e", "\uc83f", "\uc841", "\uc84a", "\uc84b", "\uc84e", "\uc855", "\uc872", "\uc873", "\uc875", "\uc876", "\uc877", "\uc879", "\uc87b", "\uc882", "\uc884", "\uc888", "\uc889", "\uc88a", "\uc88e", "\uc895", "\uc89e", "\uc8a0", "\uc8a2", "\uc8a3", "\uc8a4", "\uc8a5", "\uc8a6", "\uc8a7", "\uc8a9", "\uc8be", "\uc8bf", "\uc8c0", "\uc8c1", "\uc8c2", "\uc8c3", "\uc8c5", "\uc8c6", "\uc8c7", "\uc8c9", "\uc8ca", "\uc8cb", "\uc8cd", "\uc8d6", "\uc8d8", "\uc8da", "\uc8e2", "\uc8e3", "\uc8e5", "\uc8e6", "\uc8f6", "\uc8fe", "\uc8ff", "\uc901", "\uc902", "\uc903", "\uc907", "\uc90e", "\uc910", "\uc912", "\uc919", "\uc92d", "\uc935", "\uc948", "\uc952", "\uc953", "\uc955", "\uc956", "\uc957", "\uc959", "\uc962", "\uc964", "\uc96d", "\uc96e", "\uc96f", "\u02d0", "\u25c1", "\u25c0", "\u25b7", "\u2664", "\u2661", "\u2667", "\u25c8", "\u25a3", "\u25d0", "\u25d1", "\u25a4", "\u25a5", "\u25a8", "\u25a7", "\u25a6", "\u25a9", "\u2668", "\u260f", "\u261c", "\u261e", "\u2669", "\u266c", "\u321c", "\u33c7", "\u33c2", "\u33d8", "\uc971", "\uc972", "\uc973", "\uc975", "\uc97d", "\uc98a", "\uc98b", "\uc98d", "\uc98e", "\uc98f", "\uc991", "\uc99a", "\uc99c", "\uc99e", "\uc9af", "\uc9c2", "\uc9c3", "\uc9c5", "\uc9c6", "\uc9c9", "\uc9cb", "\uc9d2", "\uc9d4", "\uc9d7", "\uc9d8", "\uc9db", "\uc9de", "\uc9df", "\uc9e1", "\uc9e3", "\uc9e5", "\uc9e6", "\uc9e8", "\uc9e9", "\uc9ea", "\uc9eb", "\uc9ee", "\uc9f2", "\uc9fa", "\uc9fb", "\uc9fd", "\uc9fe", "\uc9ff", "\uca01", "\uca02", "\uca03", "\uca04", "\uca05", "\uca06", "\uca07", "\uca0a", "\uca0e", "\uca15", "\uca16", "\uca17", "\uca19", "\uca26", "\uca27", "\uca28", "\uca2a", "\uca47", "\uca4e", "\uca4f", "\uca51", "\uca52", "\uca53", "\uca55", "\uca5e", "\uca62", "\uca69", "\uca6a", "\uca6b", "\uca7e", "\uca85", "\uca86", "\uca87", "\uca99", "\ucaa8", "\ucabe", "\ucabf", "\ucac1", "\ucac2", "\ucac3", "\ucac5", "\ucac6", "\ucace", "\ucad0", "\ucad2", "\ucad4", "\ucad5", "\ucad6", "\ucad7", "\ucada", "\ucae1", "\ucae8", "\ucae9", "\ucaea", "\ucaeb", "\ucaed", "\ucaf5", "\ucb09", "\ucb0a", "\u2512", "\u2511", "\u251a", "\u2519", "\u2516", "\u2515", "\u250e", "\u250d", "\u251e", "\u251f", "\u2521", "\u2522", "\u2526", "\u2527", "\u2529", "\u252a", "\u252d", "\u252e", "\u2531", "\u2532", "\u2535", "\u2536", "\u2539", "\u253a", "\u253d", "\u253e", "\u2540", "\u2541", "\u2543", "\ucb0b", "\ucb11", "\ucb12", "\ucb13", "\ucb15", "\ucb16", "\ucb17", "\ucb19", "\ucb22", "\ucb2a", "\ucb42", "\ucb43", "\ucb44", "\ucb45", "\ucb46", "\ucb47", "\ucb4a", "\ucb4b", "\ucb4d", "\ucb4e", "\ucb4f", "\ucb51", "\ucb5a", "\ucb5b", "\ucb5c", "\ucb5e", "\ucb65", "\u3395", "\u3396", "\u3397", "\u3398", "\u33a3", "\u33a4", "\u33a5", "\u33a6", "\u3399", "\u33ca", "\u338d", "\u33cf", "\u3388", "\u3389", "\u33c8", "\u33a7", "\u33a8", "\u33b0", "\u3380", "\u33ba", "\u3390", "\u33c0", "\u33c1", "\u338a", "\u338b", "\u338c", "\u33d6", "\u33c5", "\u33ad", "\u33ae", "\u33af", "\u33db", "\u33a9", "\u33aa", "\u33ab", "\u33ac", "\u33dd", "\u33d0", "\u33d3", "\u33c3", "\u33c9", "\u33dc", "\u33c6", "\ucb6d", "\ucb7a", "\ucb89", "\ucb9d", "\ucba4", "\ucbb9", "\u3260", "\ucbc5", "\ucbd5", "\ucbe0", "\ucbe1", "\ucbe2", "\ucbe3", "\ucbe5", "\ucbe6", "\ucbe8", "\ucbea", "\ucbfd", "\ucc0e", "\ucc0f", "\ucc11", "\ucc12", "\ucc13", "\ucc15", "\ucc1e", "\ucc1f", "\ucc20", "\ucc23", "\ucc24", "\u3200", "\u249c", "\u2074", "\u2081", "\u2082", "\u2083", "\u2084", "\ucc25", "\ucc26", "\ucc2a", "\ucc2b", "\ucc2d", "\ucc2f", "\ucc31", "\ucc3a", "\ucc3f", "\ucc46", "\ucc47", "\ucc49", "\ucc4a", "\ucc4b", "\ucc4d", "\ucc4e", "\ucc4f", "\ucc56", "\ucc5a", "\ucc61", "\ucc62", "\ucc63", "\ucc65", "\ucc67", "\ucc69", "\ucc71", "\ucc72", "\ucc73", "\ucc74", "\ucc76", "\ucc94", "\ucc95", "\ucc96", "\ucc97", "\ucc9a", "\ucc9b", "\ucc9d", "\ucc9e", "\ucc9f", "\ucca1", "\uccaa", "\uccae", "\uccb6", "\uccb7", "\uccb9", "\uccba", "\uccbb", "\uccbd", "\uccc6", "\uccc8", "\uccca", "\uccd1", "\uccd2", "\uccd3", "\uccd5", "\uccdb", "\ucce5", "\ucced", "\uccee", "\uccef", "\uccf1", "\uccfe", "\uccff", "\ucd00", "\ucd02", "\ucd0a", "\ucd0b", "\ucd0d", "\ucd0e", "\ucd0f", "\ucd11", "\ucd1a", "\ucd1c", "\ucd1e", "\ucd1f", "\ucd20", "\ucd21", "\ucd22", "\ucd23", "\ucd25", "\ucd26", "\ucd27", "\ucd29", "\ucd2a", "\ucd2b", "\ucd2d", "\ucd3a", "\ucd3f", "\ucd5d", "\ucd5e", "\ucd5f", "\ucd61", "\ucd62", "\ucd63", "\ucd65", "\ucd6e", "\ucd70", "\ucd72", "\ucd79", "\ucd81", "\ucd89", "\ucd96", "\ucd97", "\ucd99", "\ucd9a", "\ucd9b", "\ucd9d", "\ucd9e", "\ucd9f", "\ucda0", "\ucda1", "\ucda2", "\ucda3", "\ucda6", "\ucda8", "\ucdaa", "\ucdb1", "\ucdc5", "\ucdc6", "\ucdcd", "\ucdce", "\ucdcf", "\ucdd1", "\ucde2", "\ucde9", "\ucdea", "\ucdeb", "\ucded", "\ucdee", "\ucdef", "\ucdf1", "\ucdfa", "\ucdfc", "\ucdfe", "\uce03", "\uce05", "\uce06", "\uce07", "\uce09", "\uce0a", "\uce0b", "\uce0d", "\uce15", "\uce16", "\uce17", "\uce18", "\uce1a", "\uce22", "\uce23", "\uce25", "\uce26", "\uce27", "\uce29", "\uce2a", "\uce2b", "\uce2c", "\uce2d", "\uce2e", "\uce2f", "\uce32", "\uce34", "\uce36", "\uce4a", "\uce5a", "\uce5b", "\uce5d", "\uce5e", "\uce62", "\uce6a", "\uce6c", "\uce6e", "\uce76", "\uce77", "\uce79", "\uce7a", "\uce7b", "\uce7d", "\uce86", "\uce88", "\uce8a", "\uce92", "\uce93", "\uce95", "\uce96", "\uce97", "\uce99", "\uce9a", "\ucea2", "\ucea6", "\uceae", "\ucebb", "\ucec2", "\uced6", "\ucee6", "\ucee7", "\ucee9", "\uceea", "\uceed", "\ucef6", "\ucefa", "\uac07", "\uac09", "\uac0a", "\uac10", "\uac20", "\uac24", "\uac2c", "\uac2d", "\uac2f", "\uac30", "\uac31", "\uac38", "\uac39", "\uac3c", "\uac40", "\uac4b", "\uac4d", "\uac54", "\uac58", "\uac5c", "\uac71", "\uac77", "\uac78", "\uac7a", "\uac81", "\uac84", "\uac85", "\uac86", "\uac89", "\uac8a", "\uac8b", "\uac90", "\uac94", "\uac9c", "\uac9d", "\uac9f", "\uaca0", "\uaca1", "\uacaa", "\uacac", "\uacaf", "\uacb8", "\uacb9", "\uacbb", "\uacbc", "\uacc1", "\uacc8", "\uaccc", "\uacd5", "\uacd7", "\uace1", "\uace4", "\uace7", "\uace8", "\uacea", "\uacec", "\uacef", "\uacf0", "\uacf1", "\uacf6", "\uacfd", "\uad06", "\ucf02", "\ucf03", "\ucf05", "\ucf06", "\ucf07", "\ucf09", "\ucf12", "\ucf14", "\ucf16", "\ucf1d", "\ucf1e", "\ucf1f", "\ucf21", "\ucf22", "\ucf23", "\ucf25", "\ucf2e", "\ucf32", "\ucf39", "\ucf45", "\ucf56", "\ucf57", "\ucf59", "\ucf5a", "\ucf5b", "\ucf5d", "\ucf66", "\ucf68", "\ucf6a", "\ucf6b", "\ucf6c", "\uad0c", "\uad0d", "\uad0f", "\uad11", "\uad18", "\uad1c", "\uad20", "\uad29", "\uad2c", "\uad2d", "\uad34", "\uad35", "\uad38", "\uad3c", "\uad44", "\uad45", "\uad47", "\uad49", "\uad50", "\uad54", "\uad58", "\uad61", "\uad63", "\uad70", "\uad73", "\uad74", "\uad75", "\uad76", "\uad7b", "\uad7c", "\uad7d", "\uad7f", "\uad81", "\uad82", "\uad88", "\uad89", "\uad90", "\uad9c", "\uad9d", "\uada4", "\uadb7", "\uadc1", "\uadc4", "\uadc8", "\uadd0", "\uadd1", "\uadd3", "\uade0", "\uade4", "\uadf9", "\uadff", "\uae01", "\uae09", "\uae0b", "\uae0d", "\uae14", "\uae31", "\uae37", "\uae3a", "\uae40", "\uae43", "\uae45", "\uae46", "\uae4a", "\uae4d", "\uae4e", "\uae50", "\uae54", "\uae56", "\uae5c", "\uae5d", "\uae5f", "\uae60", "\uae61", "\uae65", "\uae68", "\uae69", "\uae6c", "\uae70", "\uae78", "\ucf6d", "\ucf6e", "\ucf6f", "\ucf72", "\ucf73", "\ucf75", "\ucf76", "\ucf77", "\ucf79", "\ucf81", "\ucf82", "\ucf83", "\ucf84", "\ucf86", "\ucf8d", "\ucf8e", "\ucfa2", "\ucfa9", "\ucfaa", "\ucfb1", "\ucfc5", "\uae79", "\uae7b", "\uae7c", "\uae7d", "\uae84", "\uae85", "\uae8c", "\uaebc", "\uaebd", "\uaebe", "\uaec0", "\uaec4", "\uaecc", "\uaecd", "\uaecf", "\uaed0", "\uaed1", "\uaed8", "\uaed9", "\uaedc", "\uaee8", "\uaeeb", "\uaeed", "\uaef4", "\uaef8", "\uaefc", "\uaf07", "\uaf08", "\uaf0d", "\uaf10", "\uaf2c", "\uaf2d", "\uaf30", "\uaf32", "\uaf34", "\uaf3c", "\uaf3d", "\uaf3f", "\uaf41", "\uaf42", "\uaf43", "\uaf48", "\uaf49", "\uaf50", "\uaf5c", "\uaf5d", "\uaf64", "\uaf65", "\uaf79", "\uaf80", "\uaf84", "\uaf88", "\uaf90", "\uaf91", "\uaf95", "\uaf9c", "\uafb9", "\uafbc", "\uafc7", "\uafc9", "\uafcb", "\uafcd", "\uafce", "\uafd4", "\uafdc", "\uafe8", "\uafe9", "\uaff0", "\uaff1", "\uaff4", "\uaff8", "\ub000", "\ub001", "\ub004", "\ub010", "\ub014", "\ub01c", "\ub01d", "\ub028", "\ub044", "\ub045", "\ub048", "\ub04a", "\ub04c", "\ub04e", "\ub053", "\ub054", "\ub055", "\ub057", "\ub059", "\ucfcc", "\ucfe2", "\ucfe3", "\ucfe5", "\ucfe6", "\ucfe7", "\ucfe9", "\ucfea", "\ucff2", "\ucff4", "\ucff6", "\ucffd", "\ucffe", "\ucfff", "\ud001", "\ud002", "\ud003", "\ud005", "\ud00b", "\ud012", "\ud019", "\ub07c", "\ub07d", "\ub080", "\ub084", "\ub08c", "\ub08d", "\ub08f", "\ub091", "\ub099", "\ub09a", "\ub09f", "\ub0a0", "\ub0a1", "\ub0a2", "\ub0a9", "\ub0ab", "\ub0b1", "\ub0b3", "\ub0b5", "\ub0b8", "\ub0c5", "\ub0c7", "\ub0c8", "\ub0c9", "\ub0d0", "\ub0d1", "\ub0d4", "\ub0d8", "\ub0e0", "\ub0e5", "\ub109", "\ub10b", "\ub10c", "\ub112", "\ub113", "\ub119", "\ub11b", "\ub11c", "\ub11d", "\ub123", "\ub125", "\ub128", "\ub12c", "\ub134", "\ub135", "\ub138", "\ub139", "\ub140", "\ub141", "\ub148", "\ub150", "\ub151", "\ub154", "\ub158", "\ub15c", "\ub160", "\ub178", "\ub179", "\ub17c", "\ub180", "\ub182", "\ub188", "\ub189", "\ub18b", "\ub18d", "\ub192", "\ub193", "\ub194", "\ub198", "\ub19c", "\ub1a8", "\ub1cc", "\ub1d0", "\ub1d4", "\ub1dc", "\ub1dd", "\ud02e", "\ud036", "\ud037", "\ud039", "\ud03a", "\ud03b", "\ud03d", "\ud046", "\ud048", "\ud04a", "\ud051", "\ud052", "\ud053", "\ud055", "\ud056", "\ud057", "\ud059", "\ud061", "\ud06e", "\ud06f", "\ud071", "\ud072", "\ud073", "\ud075", "\ud07e", "\ud07f", "\ud080", "\ud082", "\ub1df", "\ub1e8", "\ub1e9", "\ub1ec", "\ub1f0", "\ub1f9", "\ub1fb", "\ub1fd", "\ub204", "\ub205", "\ub208", "\ub20b", "\ub20c", "\ub214", "\ub215", "\ub217", "\ub219", "\ub220", "\ub234", "\ub23c", "\ub258", "\ub25c", "\ub260", "\ub268", "\ub269", "\ub275", "\ub27c", "\ub284", "\ub285", "\ub289", "\ub290", "\ub291", "\ub299", "\ub29a", "\ub2a0", "\ub2a1", "\ub2a3", "\ub2a6", "\ub2aa", "\ub2ac", "\ub2b0", "\ub2b4", "\ub2d0", "\ub2d2", "\ub2d8", "\ub2db", "\ub2dd", "\ub2e2", "\ub2e5", "\ub2e6", "\ub2f3", "\ub2f4", "\ub2f5", "\ub2ff", "\ub301", "\ub304", "\ub308", "\ub310", "\ub311", "\ub313", "\ub314", "\ub315", "\ub31c", "\ub355", "\ub356", "\ub35b", "\ub35c", "\ub35e", "\ub35f", "\ub364", "\ub365", "\ud095", "\ud0a6", "\ud0a7", "\ud0a9", "\ud0aa", "\ud0ab", "\ud0ad", "\ud0b3", "\ud0b6", "\ud0b8", "\ud0ba", "\ud0c2", "\ud0c3", "\ud0c5", "\ud0c6", "\ud0c7", "\ud0ca", "\ud0d2", "\ud0d6", "\ud0db", "\ud0de", "\ud0df", "\ud0e1", "\ud0e2", "\ud0e3", "\ud0e5", "\ud0ee", "\ud0f2", "\ud0f9", "\ub367", "\ub369", "\ub36b", "\ub371", "\ub374", "\ub378", "\ub380", "\ub381", "\ub383", "\ub384", "\ub385", "\ub38c", "\ub390", "\ub394", "\ub3a0", "\ub3a1", "\ub3a8", "\ub3ac", "\ub3c5", "\ub3c8", "\ub3cb", "\ub3cc", "\ub3ce", "\ub3d0", "\ub3d4", "\ub3d5", "\ub3d7", "\ub3db", "\ub3dd", "\ub3e0", "\ub3e4", "\ub3e8", "\ub3fc", "\ub410", "\ub420", "\ub428", "\ub42b", "\ub434", "\ub450", "\ub451", "\ub454", "\ub461", "\ub463", "\ub465", "\ub46c", "\ub480", "\ub488", "\ub49d", "\ub4a4", "\ub4a8", "\ub4ac", "\ub4b5", "\ub4b7", "\ub4b9", "\ub4c0", "\ub4c4", "\ub4d0", "\ub4d5", "\ub4dd", "\ub4e3", "\ub4e6", "\ub4ec", "\ub4ed", "\ub4ef", "\ub4f8", "\ub515", "\ub518", "\ub51b", "\ub51c", "\ub524", "\ub525", "\ub527", "\ub528", "\ub52a", "\ub531", "\ub534", "\ub538", "\ud105", "\ud10e", "\ud120", "\ud132", "\ud133", "\ud135", "\ud136", "\ud137", "\ud139", "\ud13b", "\ud13c", "\ud13d", "\ud13e", "\ud13f", "\ud142", "\ud146", "\ud14e", "\ud14f", "\ud151", "\ud152", "\ud153", "\ud155", "\ud15e", "\ud160", "\ud162", "\ud169", "\ud16a", "\ud16b", "\ud16d", "\ub540", "\ub541", "\ub543", "\ub544", "\ub545", "\ub54b", "\ub54d", "\ub550", "\ub554", "\ub55c", "\ub55d", "\ub55f", "\ub560", "\ub561", "\ub5a0", "\ub5a1", "\ub5a8", "\ub5aa", "\ub5ab", "\ub5b0", "\ub5b1", "\ub5b3", "\ub5b4", "\ub5b5", "\ub5bc", "\ub5bd", "\ub5c0", "\ub5c4", "\ub5cc", "\ub5cd", "\ub5cf", "\ub5d0", "\ub5d1", "\ub5d8", "\ub5ec", "\ub611", "\ub614", "\ub618", "\ub625", "\ub62c", "\ub634", "\ub648", "\ub664", "\ub668", "\ub69c", "\ub69d", "\ub6a0", "\ub6a4", "\ub6ab", "\ub6ac", "\ub6b1", "\ub6d4", "\ub6f0", "\ub6f4", "\ub6f8", "\ub700", "\ub701", "\ub705", "\ub728", "\ub729", "\ub72c", "\ub72f", "\ub730", "\ub738", "\ub739", "\ub73b", "\ub744", "\ub748", "\ub74c", "\ub754", "\ub755", "\ub760", "\ub764", "\ub768", "\ub770", "\ub771", "\ub773", "\ub775", "\ub77d", "\ub780", "\ub784", "\ub78c", "\ub78d", "\ub78f", "\ub790", "\ub791", "\ub792", "\ub796", "\ub797", "\ud16e", "\ud17d", "\ud185", "\ud186", "\ud187", "\ud189", "\ud18a", "\ud18b", "\ud1a2", "\ud1a3", "\ud1a5", "\ud1a6", "\ud1a7", "\ud1a9", "\ud1b2", "\ud1b4", "\ud1b6", "\ud1b7", "\ud1b8", "\ud1b9", "\ud1bb", "\ud1bd", "\ud1be", "\ud1bf", "\ud1c1", "\ub799", "\ub7a0", "\ub7a9", "\ub7ab", "\ub7ac", "\ub7ad", "\ub7b4", "\ub7b5", "\ub7b8", "\ub7c7", "\ub7c9", "\ub7ed", "\ub7f4", "\ub7ff", "\ub800", "\ub801", "\ub807", "\ub80c", "\ub810", "\ub818", "\ub819", "\ub81b", "\ub81d", "\ub828", "\ub834", "\ub835", "\ub837", "\ub838", "\ub840", "\ub844", "\ub851", "\ub853", "\ub86c", "\ub86d", "\ub86f", "\ub871", "\ub878", "\ub87c", "\ub88d", "\ub8a8", "\ub8b0", "\ub8b4", "\ub8b8", "\ub8c0", "\ub8c1", "\ub8c3", "\ub8c5", "\ub8cc", "\ub8d0", "\ub8d4", "\ub8dd", "\ub8df", "\ub8e1", "\ub8ec", "\ub8f0", "\ub8f8", "\ub8fb", "\ub8fd", "\ub904", "\ub918", "\ub920", "\ub93c", "\ub93d", "\ub940", "\ub944", "\ub94c", "\ub94f", "\ub951", "\ub959", "\ub95c", "\ub960", "\ub969", "\ud1d0", "\ud1d9", "\ud1eb", "\ud1f5", "\ud1f6", "\ud1f7", "\ud1f9", "\ud208", "\ud20a", "\ud211", "\ub96b", "\ub96d", "\ub975", "\ub985", "\ub987", "\ub989", "\ub98a", "\ub98d", "\ub98e", "\ub9bf", "\ub9d8", "\ub9d9", "\ub9db", "\ub9dd", "\ub9e1", "\ub9e3", "\ub9e5", "\ub9e8", "\ub9ec", "\ub9f4", "\ub9f5", "\ub9f7", "\ub9f8", "\ub9f9", "\ub9fa", "\uba00", "\uba01", "\uba08", "\uba15", "\uba39", "\uba40", "\uba42", "\uba48", "\uba49", "\uba4b", "\uba4d", "\uba4e", "\uba53", "\uba55", "\uba58", "\uba5c", "\uba64", "\uba65", "\uba67", "\uba68", "\uba69", "\uba70", "\uba71", "\uba78", "\uba83", "\uba84", "\uba8c", "\ubaab", "\ubaac", "\ubab0", "\ubab2", "\ubab8", "\ubab9", "\ubabd", "\ubac4", "\ubac8", "\ubad8", "\ubad9", "\ubafc", "\ud22a", "\ud22b", "\ud22e", "\ud22f", "\ud231", "\ud232", "\ud233", "\ud235", "\ud23e", "\ud240", "\ud242", "\ud249", "\ud24a", "\ud24b", "\ud24c", "\ud24d", "\ud25d", "\ud265", "\ud266", "\ud267", "\ud268", "\ud269", "\ud282", "\ud283", "\ud285", "\ud286", "\ud287", "\ud289", "\ud28a", "\ud28b", "\ud28c", "\ubb00", "\ubb04", "\ubb0d", "\ubb0f", "\ubb11", "\ubb18", "\ubb1c", "\ubb20", "\ubb29", "\ubb2b", "\ubb35", "\ubb36", "\ubb3b", "\ubb3c", "\ubb3d", "\ubb3e", "\ubb44", "\ubb45", "\ubb47", "\ubb49", "\ubb4d", "\ubb4f", "\ubb50", "\ubb54", "\ubb58", "\ubb61", "\ubb63", "\ubb6c", "\ubb88", "\ubb8c", "\ubb90", "\ubba4", "\ubba8", "\ubbac", "\ubbb4", "\ubbb7", "\ubbc0", "\ubbc4", "\ubbc8", "\ubbd0", "\ubbd3", "\ubbf9", "\ubbfc", "\ubbff", "\ubc02", "\ubc08", "\ubc09", "\ubc0b", "\ubc0c", "\ubc0d", "\ubc0f", "\ubc11", "\ubc24", "\ubc25", "\ubc27", "\ubc29", "\ubc2d", "\ubc34", "\ubc38", "\ubc40", "\ubc41", "\ubc43", "\ubc44", "\ubc45", "\ubc49", "\ubc4c", "\ubc4d", "\ubc50", "\ubc5d", "\ubc85", "\ubc8b", "\ubc8c", "\ubc8e", "\ud28d", "\ud28e", "\ud28f", "\ud292", "\ud293", "\ud294", "\ud296", "\ud29d", "\ud29e", "\ud29f", "\ud2a1", "\ud2a2", "\ud2a3", "\ud2a5", "\ud2ad", "\ud2ae", "\ud2af", "\ud2b0", "\ud2b2", "\ud2ba", "\ud2bb", "\ud2bd", "\ud2be", "\ud2c1", "\ud2c3", "\ud2ca", "\ud2cc", "\ud2d2", "\ud2d3", "\ud2d5", "\ud2d6", "\ud2d7", "\ud2d9", "\ud2da", "\ud2db", "\ud2dd", "\ud2e6", "\ud2f2", "\ud2f3", "\ud2f5", "\ud2f6", "\ud2f7", "\ud2f9", "\ud2fa", "\ubc99", "\ubc9a", "\ubca0", "\ubca1", "\ubca4", "\ubca7", "\ubca8", "\ubcb0", "\ubcb1", "\ubcb3", "\ubcb4", "\ubcb5", "\ubcbc", "\ubcbd", "\ubcc4", "\ubccd", "\ubccf", "\ubcd0", "\ubcd1", "\ubcd5", "\ubcd8", "\ubcdc", "\ubcf6", "\ubd04", "\ubd07", "\ubd09", "\ubd10", "\ubd14", "\ubd24", "\ubd2c", "\ubd40", "\ubd48", "\ubd49", "\ubd4c", "\ubd50", "\ubd58", "\ubd59", "\ubd64", "\ubd68", "\ubd87", "\ubd89", "\ubd8a", "\ubd90", "\ubd91", "\ubd93", "\ubd95", "\ubd99", "\ubd9a", "\ubd9c", "\ubda4", "\ubdb0", "\ubdb8", "\ubdd4", "\ubdd5", "\ubdd8", "\ubddc", "\ubde9", "\ubdf4", "\ubdf8", "\ube00", "\ube03", "\ube05", "\ube0d", "\ube10", "\ube14", "\ube1c", "\ube1d", "\ube1f", "\ube45", "\ube4e", "\ube54", "\ube55", "\ube57", "\ube59", "\ube5a", "\ube5b", "\ube61", "\ube64", "\ud2fb", "\ud302", "\ud304", "\ud306", "\ud30f", "\ud311", "\ud312", "\ud313", "\ud315", "\ud317", "\ud31e", "\ud322", "\ud323", "\ud324", "\ud326", "\ud327", "\ud32a", "\ud32b", "\ud32d", "\ud32e", "\ud32f", "\ud331", "\ud33a", "\ud33e", "\ud346", "\ud347", "\ud348", "\ud349", "\ud34a", "\ube68", "\ube6a", "\ube70", "\ube71", "\ube73", "\ube74", "\ube75", "\ube7b", "\ube7c", "\ube7d", "\ube80", "\ube84", "\ube8c", "\ube8d", "\ube8f", "\ube90", "\ube91", "\ube98", "\ube99", "\ubea8", "\ubed0", "\ubed1", "\ubed4", "\ubed7", "\ubed8", "\ubee0", "\ubee3", "\ubee4", "\ubee5", "\ubeec", "\ubf01", "\ubf08", "\ubf09", "\ubf18", "\ubf19", "\ubf1b", "\ubf1c", "\ubf1d", "\ubf40", "\ubf41", "\ubf44", "\ubf48", "\ubf50", "\ubf51", "\ubf55", "\ubf94", "\ubfb0", "\ubfc5", "\ubfcc", "\ubfcd", "\ubfd0", "\ubfd4", "\ubfdc", "\ubfdf", "\ubfe1", "\uc03c", "\uc051", "\uc058", "\uc05c", "\uc060", "\uc068", "\uc069", "\uc090", "\uc091", "\uc094", "\uc098", "\uc0a0", "\uc0a1", "\uc0a3", "\uc0a5", "\uc0ad", "\uc0af", "\uc0b0", "\uc0b3", "\uc0b4", "\uc0b5", "\uc0b6", "\uc0bd", "\uc0bf", "\uc0c0", "\uc0c5", "\uc0c8", "\uc0cc", "\uc0d0", "\uc0d8", "\uc0d9", "\uc0db", "\uc0dc", "\uc0e4", "\ud36a", "\ud37e", "\ud37f", "\ud381", "\ud382", "\ud383", "\ud385", "\ud386", "\ud387", "\ud388", "\ud389", "\ud38a", "\ud38b", "\ud38e", "\ud392", "\ud39a", "\ud39b", "\ud39d", "\ud39e", "\ud39f", "\ud3a1", "\ud3aa", "\ud3ac", "\ud3ae", "\ud3af", "\ud3b5", "\ud3b6", "\ud3b7", "\ud3b9", "\ud3ba", "\ud3bb", "\ud3bd", "\ud3c6", "\ud3c7", "\ud3ca", "\ud3d1", "\uc0e5", "\uc0e8", "\uc0ec", "\uc0f4", "\uc0f5", "\uc0f7", "\uc0f9", "\uc100", "\uc104", "\uc108", "\uc110", "\uc115", "\uc123", "\uc126", "\uc127", "\uc12c", "\uc12d", "\uc12f", "\uc130", "\uc136", "\uc139", "\uc13c", "\uc140", "\uc148", "\uc149", "\uc14c", "\uc14d", "\uc154", "\uc155", "\uc15c", "\uc164", "\uc165", "\uc167", "\uc168", "\uc169", "\uc170", "\uc174", "\uc185", "\uc18e", "\uc194", "\uc196", "\uc19c", "\uc19d", "\uc19f", "\uc1a1", "\uc1a5", "\uc1a8", "\uc1a9", "\uc1ac", "\uc1b0", "\uc1bd", "\uc1c4", "\uc1c8", "\uc1cc", "\uc1d4", "\uc1d7", "\uc1d8", "\uc1e0", "\uc1e4", "\uc1e8", "\uc1f0", "\uc1f1", "\uc1f3", "\uc1fc", "\uc1fd", "\uc200", "\uc204", "\uc20c", "\uc20d", "\uc20f", "\uc211", "\uc219", "\uc21f", "\uc220", "\uc229", "\uc22d", "\ud3d7", "\ud3d9", "\ud3e2", "\ud3e4", "\ud3ee", "\ud3ef", "\ud3f1", "\ud3f2", "\ud3f3", "\ud3f5", "\ud3f6", "\ud3f7", "\ud3f8", "\ud3f9", "\ud3fa", "\ud3fb", "\ud3fe", "\ud400", "\ud402", "\ud409", "\ud417", "\ud41e", "\uc22f", "\uc231", "\uc232", "\uc234", "\uc248", "\uc250", "\uc251", "\uc254", "\uc258", "\uc260", "\uc265", "\uc26c", "\uc26d", "\uc270", "\uc274", "\uc27c", "\uc27d", "\uc27f", "\uc281", "\uc288", "\uc289", "\uc290", "\uc298", "\uc29b", "\uc29d", "\uc2a5", "\uc2a8", "\uc2ac", "\uc2ad", "\uc2b4", "\uc2b7", "\uc2b9", "\uc2e3", "\uc2eb", "\uc2ef", "\uc2f1", "\uc2f6", "\uc2f8", "\uc2f9", "\uc2fb", "\uc300", "\uc308", "\uc309", "\uc30c", "\uc313", "\uc314", "\uc315", "\uc318", "\uc31c", "\uc324", "\uc325", "\uc328", "\uc329", "\uc345", "\uc369", "\uc36c", "\uc370", "\uc372", "\uc378", "\uc379", "\uc37c", "\uc37d", "\uc384", "\uc388", "\uc38c", "\uc3c0", "\uc3d8", "\uc3d9", "\uc3dc", "\uc3df", "\uc3e0", "\uc3e2", "\uc3e8", "\uc3e9", "\uc3ed", "\uc3f4", "\uc3f5", "\uc3f8", "\uc408", "\uc410", "\uc424", "\uc42c", "\uc430", "\ud438", "\ud441", "\ud442", "\ud443", "\ud445", "\ud454", "\ud45d", "\ud45e", "\ud45f", "\ud461", "\ud462", "\ud463", "\ud465", "\ud46e", "\ud470", "\ud471", "\ud472", "\ud473", "\ud47a", "\ud47b", "\ud47d", "\ud47e", "\ud481", "\ud483", "\ud48a", "\ud48c", "\ud48e", "\ud495", "\uc434", "\uc43c", "\uc43d", "\uc448", "\uc464", "\uc465", "\uc468", "\uc46c", "\uc474", "\uc475", "\uc479", "\uc480", "\uc494", "\uc49c", "\uc4b8", "\uc4bc", "\uc4e9", "\uc4f1", "\uc4fa", "\uc4ff", "\uc500", "\uc501", "\uc50c", "\uc510", "\uc514", "\uc51c", "\uc528", "\uc529", "\uc52c", "\uc530", "\uc538", "\uc539", "\uc53b", "\uc53d", "\uc545", "\uc549", "\uc54d", "\uc54e", "\uc553", "\uc554", "\uc555", "\uc557", "\uc559", "\uc55d", "\uc55e", "\uc561", "\uc564", "\uc568", "\uc570", "\uc571", "\uc573", "\uc574", "\uc575", "\uc580", "\uc584", "\uc587", "\uc58c", "\uc58d", "\uc58f", "\uc591", "\uc595", "\uc597", "\uc598", "\uc59c", "\uc5a0", "\uc5a9", "\uc5b5", "\uc5b9", "\uc5bb", "\uc5bc", "\uc5bd", "\uc5be", "\uc5c4", "\uc5cc", "\uc5ce", "\ud49e", "\ud4aa", "\ud4b9", "\ud4cd", "\ud4ce", "\ud4cf", "\ud4d1", "\ud4d2", "\ud4d3", "\ud4d5", "\ud4d6", "\ud4dd", "\ud4de", "\ud4e0", "\ud4e9", "\ud4ea", "\ud4eb", "\ud4ed", "\ud4ee", "\ud4ef", "\ud4f1", "\ud4f9", "\ud4fa", "\ud4fc", "\uc5d1", "\uc5e0", "\uc5e1", "\uc5e3", "\uc5e5", "\uc5ee", "\uc5f6", "\uc5f7", "\uc5fc", "\uc605", "\uc606", "\uc607", "\uc60c", "\uc610", "\uc618", "\uc619", "\uc61b", "\uc61c", "\uc625", "\uc628", "\uc62d", "\uc630", "\uc633", "\uc637", "\uc639", "\uc63b", "\uc641", "\uc648", "\uc650", "\uc651", "\uc653", "\uc654", "\uc655", "\uc65c", "\uc65d", "\uc660", "\uc66c", "\uc66f", "\uc671", "\uc679", "\uc67c", "\uc680", "\uc688", "\uc689", "\uc68b", "\uc68d", "\uc695", "\uc698", "\uc69c", "\uc6a4", "\uc6a5", "\uc6a7", "\uc6b1", "\uc6b9", "\uc6ba", "\uc6c1", "\uc6c3", "\uc6c5", "\uc6cc", "\uc6cd", "\uc6dc", "\uc6dd", "\uc6e0", "\uc6e1", "\uc6e8", "\ud4fe", "\ud505", "\ud506", "\ud507", "\ud509", "\ud50a", "\ud50b", "\ud50d", "\ud516", "\ud518", "\ud51e", "\ud538", "\ud539", "\ud53a", "\ud53b", "\ud53e", "\ud53f", "\ud541", "\ud542", "\ud543", "\ud545", "\ud54e", "\ud550", "\ud552", "\ud55a", "\ud55b", "\ud55d", "\ud55e", "\ud55f", "\ud561", "\ud562", "\ud563", "\uc6e9", "\uc6ec", "\uc6f0", "\uc6f8", "\uc6f9", "\uc6fd", "\uc705", "\uc70c", "\uc714", "\uc715", "\uc717", "\uc719", "\uc721", "\uc724", "\uc728", "\uc730", "\uc731", "\uc733", "\uc735", "\uc737", "\uc73d", "\uc74a", "\uc74d", "\uc74f", "\uc75c", "\uc760", "\uc768", "\uc76b", "\uc775", "\uc77e", "\uc783", "\uc787", "\uc789", "\uc78a", "\uc78e", "\uc794", "\uc796", "\uc797", "\uc79a", "\uc7a0", "\uc7a1", "\uc7a3", "\uc7a4", "\uc7a6", "\uc7ad", "\uc7b0", "\uc7b4", "\uc7bc", "\uc7bd", "\uc7bf", "\uc7c0", "\uc7c1", "\uc7c8", "\uc7c9", "\uc7cc", "\uc7ce", "\uc7d0", "\uc7d8", "\uc7dd", "\uc7e4", "\uc7e8", "\uc7ec", "\uc80a", "\ud564", "\ud566", "\ud567", "\ud56a", "\ud56c", "\ud56e", "\ud576", "\ud577", "\ud579", "\ud57a", "\ud57b", "\ud57d", "\ud586", "\ud58a", "\ud58b", "\ud58c", "\ud58d", "\ud58e", "\ud58f", "\ud591", "\ud5a6", "\ud5a7", "\ud5a8", "\uc810", "\uc813", "\uc816", "\uc81d", "\uc820", "\uc824", "\uc82c", "\uc82d", "\uc82f", "\uc831", "\uc83c", "\uc840", "\uc848", "\uc849", "\uc84d", "\uc854", "\uc878", "\uc87a", "\uc880", "\uc881", "\uc883", "\uc886", "\uc887", "\uc88b", "\uc88c", "\uc88d", "\uc894", "\uc89d", "\uc89f", "\uc8a1", "\uc8a8", "\uc8bc", "\uc8bd", "\uc8c4", "\uc8c8", "\uc8cc", "\uc8d4", "\uc8d5", "\uc8d7", "\uc8d9", "\uc8e0", "\uc8e1", "\uc8e4", "\uc8f5", "\uc8fd", "\uc900", "\uc905", "\uc906", "\uc90c", "\uc90d", "\uc90f", "\uc918", "\uc92c", "\uc934", "\uc950", "\uc951", "\uc954", "\uc958", "\uc960", "\uc961", "\uc963", "\uc96c", "\uc970", "\uc974", "\uc97c", "\uc989", "\uc98c", "\uc990", "\uc998", "\uc999", "\uc99b", "\uc99d", "\uc9c1", "\uc9c7", "\uc9c8", "\uc9ca", "\uc9d0", "\uc9d1", "\uc9d3", "\ud5ca", "\ud5cb", "\ud5cd", "\ud5ce", "\ud5cf", "\ud5d1", "\ud5d3", "\ud5da", "\ud5dc", "\ud5de", "\ud5e6", "\ud5e7", "\ud5e9", "\ud5ea", "\ud5eb", "\ud5ed", "\ud5ee", "\ud5ef", "\ud5f6", "\ud5f8", "\ud5fa", "\ud602", "\ud603", "\ud605", "\ud606", "\ud607", "\ud609", "\ud612", "\ud616", "\ud61d", "\ud61e", "\ud61f", "\ud621", "\ud622", "\ud623", "\ud625", "\ud62e", "\ud63a", "\ud63b", "\uc9d5", "\uc9d6", "\uc9d9", "\uc9da", "\uc9dc", "\uc9dd", "\uc9e0", "\uc9e2", "\uc9e4", "\uc9e7", "\uc9ec", "\uc9ed", "\uc9ef", "\uc9f0", "\uc9f1", "\uc9f9", "\uc9fc", "\uca00", "\uca08", "\uca09", "\uca0b", "\uca0c", "\uca0d", "\uca14", "\uca18", "\uca29", "\uca4c", "\uca4d", "\uca50", "\uca54", "\uca5c", "\uca5d", "\uca5f", "\uca60", "\uca61", "\uca68", "\uca7d", "\uca84", "\uca98", "\ucabc", "\ucabd", "\ucac0", "\ucac4", "\ucacc", "\ucacd", "\ucacf", "\ucad1", "\ucad3", "\ucad8", "\ucad9", "\ucae0", "\ucaec", "\ucaf4", "\ucb08", "\ucb10", "\ucb14", "\ucb18", "\ucb20", "\ucb21", "\ucb41", "\ucb48", "\ucb49", "\ucb4c", "\ucb50", "\ucb58", "\ucb59", "\ucb5d", "\ucb64", "\ucb78", "\ucb79", "\ucb9c", "\ucbb8", "\ucbd4", "\ucbe4", "\ucbe7", "\ucbe9", "\ucc0c", "\ucc10", "\ucc14", "\ucc1c", "\ucc1d", "\ucc21", "\ucc22", "\ucc27", "\ucc28", "\ucc29", "\ucc2c", "\ucc2e", "\ucc30", "\ucc39", "\ucc3b", "\ud63d", "\ud63e", "\ud63f", "\ud641", "\ud642", "\ud643", "\ud644", "\ud646", "\ud647", "\ud64a", "\ud64c", "\ud64e", "\ud64f", "\ud650", "\ud652", "\ud653", "\ud656", "\ud657", "\ud659", "\ud65a", "\ud65b", "\ud65d", "\ud662", "\ud668", "\ud66a", "\ud672", "\ud673", "\ud675", "\ud681", "\ud682", "\ud684", "\ud686", "\ud68e", "\ud68f", "\ud691", "\ud692", "\ud693", "\ud695", "\ud69e", "\ud6a0", "\ud6a2", "\ud6a9", "\ud6aa", "\ucc3c", "\ucc3d", "\ucc45", "\ucc48", "\ucc4c", "\ucc54", "\ucc55", "\ucc57", "\ucc58", "\ucc59", "\ucc60", "\ucc64", "\ucc66", "\ucc68", "\ucc70", "\ucc75", "\ucc99", "\ucc9c", "\ucca0", "\ucca8", "\ucca9", "\uccab", "\uccac", "\uccb5", "\uccb8", "\uccbc", "\uccc4", "\uccc5", "\uccc7", "\uccc9", "\uccd0", "\uccd4", "\ucce4", "\uccec", "\uccf0", "\ucd01", "\ucd09", "\ucd0c", "\ucd10", "\ucd18", "\ucd19", "\ucd1b", "\ucd1d", "\ucd24", "\ucd28", "\ucd2c", "\ucd39", "\ucd60", "\ucd64", "\ucd6c", "\ucd6d", "\ucd6f", "\ucd71", "\ucd78", "\ucd88", "\ucd95", "\ucd98", "\ucda4", "\ucda5", "\ucda7", "\ucda9", "\ucdb0", "\ucdc4", "\ucdcc", "\ucdd0", "\ucdec", "\ucdf0", "\ucdf8", "\ucdf9", "\ucdfb", "\ucdfd", "\uce04", "\uce08", "\uce0c", "\uce14", "\uce19", "\uce20", "\uce21", "\uce24", "\uce28", "\uce30", "\uce31", "\uce33", "\uce35", "\ud6ab", "\ud6ad", "\ud6ae", "\ud6af", "\ud6b1", "\ud6ba", "\ud6bc", "\ud6c6", "\ud6c7", "\ud6c9", "\ud6ca", "\ud6cb", "\ud6cd", "\ud6ce", "\ud6cf", "\ud6d0", "\ud6d2", "\ud6d3", "\ud6d5", "\ud6d6", "\ud6d8", "\ud6da", "\ud6e1", "\ud6e2", "\ud6e3", "\ud6e5", "\ud6e6", "\ud6e7", "\ud6e9", "\ud6ee", "\ud6ef", "\ud6f1", "\ud6f2", "\ud6f3", "\ud6f4", "\ud6f6", "\ud6fe", "\ud6ff", "\ud701", "\ud702", "\ud703", "\ud705", "\ud712", "\ud713", "\ud714", "\uce59", "\uce5c", "\uce5f", "\uce60", "\uce61", "\uce68", "\uce69", "\uce6b", "\uce6d", "\uce75", "\uce78", "\uce7c", "\uce84", "\uce85", "\uce87", "\uce89", "\uce90", "\uce91", "\uce94", "\uce98", "\ucea0", "\ucea1", "\ucea3", "\ucea4", "\ucea5", "\uceac", "\ucead", "\ucec1", "\ucee4", "\ucee5", "\uceeb", "\ucef5", "\ucef7", "\ucef8", "\ucef9", "\ucf01", "\ucf04", "\ucf08", "\ucf10", "\ucf11", "\ucf15", "\ucf1c", "\ucf20", "\ucf24", "\ucf2c", "\ucf2d", "\ucf2f", "\ucf30", "\ucf31", "\ucf38", "\ucf55", "\ucf64", "\ucf65", "\ucf67", "\ucf69", "\ucf70", "\ucf71", "\ucf74", "\ucf78", "\ucf80", "\ucf85", "\ucf8c", "\ucfa1", "\ucfa8", "\ucfb0", "\ucfc4", "\ucfe0", "\ucfe1", "\ucfe4", "\ucfe8", "\ucff0", "\ucff1", "\ucff3", "\ucff5", "\ucffc", "\ud004", "\ud011", "\ud018", "\ud02d", "\ud034", "\ud035", "\ud038", "\ud03c", "\ud715", "\ud716", "\ud717", "\ud71a", "\ud71b", "\ud71d", "\ud71e", "\ud71f", "\ud721", "\ud72a", "\ud72c", "\ud72e", "\ud736", "\ud737", "\ud739", "\ud73a", "\ud73b", "\ud73d", "\ud745", "\ud746", "\ud748", "\ud74a", "\ud752", "\ud753", "\ud755", "\ud75a", "\ud75f", "\ud762", "\ud764", "\ud766", "\ud767", "\ud768", "\ud76a", "\ud76b", "\ud76d", "\ud76e", "\ud76f", "\ud771", "\ud772", "\ud773", "\ud775", "\ud77e", "\ud77f", "\ud780", "\ud782", "\ud78a", "\ud78b", "\ud044", "\ud045", "\ud047", "\ud049", "\ud050", "\ud054", "\ud058", "\ud060", "\ud06d", "\ud07c", "\ud081", "\ud0a5", "\ud0a8", "\ud0ac", "\ud0b4", "\ud0b5", "\ud0b7", "\ud0b9", "\ud0c1", "\ud0c4", "\ud0c8", "\ud0c9", "\ud0d0", "\ud0d1", "\ud0d3", "\ud0d4", "\ud0d5", "\ud0e0", "\ud0e4", "\ud0ec", "\ud0ed", "\ud0ef", "\ud0f0", "\ud0f1", "\ud0f8", "\ud10d", "\ud131", "\ud138", "\ud13a", "\ud140", "\ud141", "\ud143", "\ud144", "\ud145", "\ud150", "\ud154", "\ud15d", "\ud15f", "\ud161", "\ud168", "\ud16c", "\ud17c", "\ud184", "\ud188", "\ud1a1", "\ud1a4", "\ud1a8", "\ud1b0", "\ud1b1", "\ud1b3", "\ud1ba", "\ud1bc", "\ud1c0", "\ud1d8", "\ud1f4", "\ud1f8", "\ud207", "\ud209", "\ud210", "\ud22c", "\ud22d", "\ud230", "\ud234", "\ud23c", "\ud23d", "\ud23f", "\ud241", "\ud248", "\ud25c", "\ud78d", "\ud78e", "\ud78f", "\ud791", "\ud79a", "\ud79c", "\ud79e", "\ud264", "\ud280", "\ud281", "\ud284", "\ud288", "\ud290", "\ud291", "\ud295", "\ud29c", "\ud2a0", "\ud2a4", "\ud2ac", "\ud2b1", "\ud2bc", "\ud2bf", "\ud2c0", "\ud2c2", "\ud2c8", "\ud2c9", "\ud2cb", "\ud2d4", "\ud2d8", "\ud2dc", "\ud2e4", "\ud2e5", "\ud2f1", "\ud2f4", "\ud2f8", "\ud300", "\ud301", "\ud303", "\ud305", "\ud30d", "\ud30e", "\ud310", "\ud314", "\ud316", "\ud31c", "\ud31d", "\ud31f", "\ud320", "\ud321", "\ud325", "\ud329", "\ud32c", "\ud330", "\ud338", "\ud339", "\ud33b", "\ud33c", "\ud33d", "\ud344", "\ud345", "\ud37d", "\ud380", "\ud384", "\ud38c", "\ud38d", "\ud38f", "\ud390", "\ud391", "\ud399", "\ud39c", "\ud3a0", "\ud3a8", "\ud3a9", "\ud3ab", "\ud3ad", "\ud3b4", "\ud3b8", "\ud3bc", "\ud3c4", "\ud3c5", "\ud3c8", "\ud3c9", "\ud3d0", "\ud3d8", "\ud3e1", "\ud3e3", "\ud3ed", "\ud3f0", "\ud3fc", "\ud3fd", "\ud3ff", "\ud401", "\ud408", "\ud41d", "\ud440", "\ud444", "\ud460", "\ud464", "\ud46d", "\ud46f", "\ud478", "\ud479", "\ud47c", "\ud47f", "\ud480", "\ud482", "\ud488", "\ud489", "\ud48b", "\ud48d", "\ud494", "\ud4a9", "\ud4cc", "\ud4d0", "\ud4d4", "\ud4dc", "\ud4df", "\ud4e8", "\ud4ec", "\ud4f0", "\ud4f8", "\ud4fb", "\ud4fd", "\ud508", "\ud514", "\ud515", "\ud517", "\ud53c", "\ud53d", "\ud540", "\ud54c", "\ud54d", "\ud54f", "\ud559", "\ud565", "\ud56b", "\ud575", "\ud578", "\ud57c", "\ud584", "\ud585", "\ud587", "\ud590", "\ud5a5", "\ud5c9", "\ud5cc", "\ud5d0", "\ud5d2", "\ud5d8", "\ud5d9", "\ud5db", "\ud5dd", "\ud5e4", "\ud5e5", "\ud5e8", "\ud5ec", "\ud5f4", "\ud5f5", "\ud5f7", "\ud5f9", "\ud600", "\ud601", "\ud608", "\ud610", "\ud611", "\ud613", "\ud61c", "\ud620", "\ud624", "\ud62d", "\ud63c", "\ud640", "\ud645", "\ud648", "\ud649", "\ud64b", "\ud64d", "\ud651", "\ud65c", "\ud667", "\ud669", "\ud670", "\ud671", "\ud674", "\ud683", "\ud685", "\ud68c", "\ud68d", "\ud690", "\ud694", "\ud69d", "\ud69f", "\ud6a1", "\ud6a8", "\ud6ac", "\ud6b0", "\ud6b9", "\ud6bb", "\ud6c5", "\ud6c8", "\ud6cc", "\ud6d1", "\ud6d4", "\ud6d7", "\ud6d9", "\ud6e0", "\ud6e4", "\ud6e8", "\ud6f0", "\ud6f5", "\ud6fc", "\ud6fd", "\ud700", "\ud704", "\ud711", "\ud718", "\ud719", "\ud71c", "\ud720", "\ud728", "\ud729", "\ud72b", "\ud72d", "\ud735", "\ud738", "\ud73c", "\ud744", "\ud747", "\ud749", "\ud750", "\ud751", "\ud754", "\ud756", "\ud757", "\ud758", "\ud759", "\ud760", "\ud761", "\ud763", "\ud765", "\ud769", "\ud76c", "\ud770", "\ud774", "\ud77c", "\ud77d", "\ud781", "\ud789", "\ud78c", "\ud790", "\ud798", "\ud799", "\ud79b", "\ud79d", "\u4e6b", "\u69ea", "\uf901", "\uf902", "\uf903", "\uf904", "\uf905", "\uf906", "\uf907", "\uf908", "\uf909", "\uf90a", "\u802d", "\uf90b", "\uf90c", "\uf90d", "\uf90e", "\uf914", "\uf919", "\uf91a", "\uf91b", "\uf91c", "\uf91d", "\uf91e", "\uf91f", "\uf920", "\uf921", "\uf922", "\uf923", "\uf924", "\uf925", "\uf926", "\uf927", "\uf928", "\uf92d", "\uf92e", "\u5bd7", "\uf92f", "\uf930", "\uf931", "\uf932", "\uf933", "\uf939", "\uf944", "\uf945", "\uf946", "\uf947", "\uf948", "\uf949", "\uf94a", "\uf952", "\uf958", "\uf959", "\u6fbe", "\u4e6d", "\uf95a", "\uf95b", "\uf95c", "\uf95d", "\uf95e", "\uf95f", "\uf960", "\uf961", "\uf962", "\u6927", "\uf963", "\uf964", "\uf965", "\u5002", "\u9a08", "\u6e7a", "\u4e76", "\uf966", "\uf967", "\uf968", "\uf969", "\uf96a", "\u4e77", "\uf96b", "\uf96c", "\uf96d", "\u657e", "\u9425", "\uf96e", "\uf96f", "\uf970", "\u6a53", "\u5aa4", "\u67be", "\uf971", "\uf972", "\uf973", "\uf974", "\uf975", "\uf976", "\uf977", "\uf978", "\uf97a", "\uf97b", "\uf97c", "\uf97d", "\uf97e", "\uf97f", "\uf980", "\uf981", "\uf982", "\uf983", "\uf984", "\u7916", "\uf985", "\uf986", "\uf987", "\uf988", "\uf989", "\uf98a", "\uf98b", "\uf98c", "\uf98d", "\u59f8", "\uf98e", "\uf98f", "\uf990", "\uf991", "\uf992", "\uf993", "\uf994", "\uf996", "\uf997", "\uf998", "\uf999", "\uf99a", "\uf99b", "\uf99c", "\uf99d", "\uf99e", "\uf99f", "\uf9a0", "\uf9a1", "\uf9a2", "\uf9a3", "\uf9a4", "\uf9a5", "\uf9a6", "\uf9a7", "\uf9a8", "\uf9a9", "\uf9aa", "\uf9ab", "\uf9ac", "\uf9ad", "\uf9ae", "\uf9af", "\uf9b0", "\uf9b1", "\uf9b2", "\uf9b3", "\uf9b4", "\uf9b5", "\uf9b6", "\uf9b7", "\uf9b8", "\uf9b9", "\u7465", "\u7413", "\uf9ba", "\uf9bb", "\uf9bc", "\uf9bd", "\uf9be", "\uf9bf", "\uf9c0", "\uf9c1", "\uf9c2", "\uf9c3", "\uf9c4", "\uf9c5", "\uf9c6", "\uf9c7", "\uf9c8", "\uf9c9", "\uf9ca", "\uf9cb", "\uf9cc", "\uf9cd", "\uf9ce", "\uf9cf", "\uf9d0", "\uf9d1", "\uf9d2", "\uf9d3", "\uf9d4", "\uf9d5", "\uf9d6", "\u73a7", "\uf9d7", "\uf9d8", "\uf9d9", "\uf9da", "\uf9db", "\uf9dd", "\uf9de", "\uf9df", "\uf9e0", "\uf9e1", "\uf9e2", "\uf9e3", "\uf9e4", "\uf9e5", "\uf9e6", "\uf9e8", "\uf9e9", "\uf9ea", "\uf9eb", "\uf9ec", "\uf9ed", "\uf9ee", "\uf9ef", "\uf9f0", "\uf9f2", "\uf9f3", "\uf9f4", "\uf9f5", "\uf9f6", "\uf9f7", "\uf9f8", "\uf9f9", "\u6b0c", "\uf9fa", "\uf9fb", "\u8aea", "\uf9fc", "\u74c6", "\uf9fd", "\uf9fe", "\uf9ff", "\u617d", "\ufa00", "\ufa01", "\ufa02", "\u7438", "\ufa03", "\ufa04", "\ufa05", "\ufa06", "\ufa07", "\u98c7", "\ufa08", "\ufa09", "\u6af6", "\ufa0a", "\u66b3", "\ufa0b", "\u43f0", "\u4c32", "\u4603", "\u45a6", "\u4578", "\ud85c\ude67", "\u4d77", "\u45b3", "\ud85f\udcb1", "\u4ce2", "\ud85f\udcc5", "\u3b95", "\u4736", "\u4744", "\u4c47", "\u4c40", "\ud850\udebf", "\ud84d\ude17", "\ud85c\udf52", "\ud85b\ude8b", "\ud85c\udcd2", "\u4c57", "\ud868\udf51", "\u474f", "\u45da", "\u4c85", "\ud85f\udc6c", "\u4d07", "\u4aa4", "\u46a1", "\ud85a\udf23", "\u7225", "\ud856\ude54", "\ud846\ude63", "\ud84f\ude06", "\ud84f\udf61", "\u7d95", "\ud862\udfb9", "\u3df4", "\u9734", "\ud85e\udfef", "\ud847\udd5e", "\u3625", "\ud867\udeb0", "\u5ad1", "\ud866\udd45", "\u7461", "\u3875", "\ud847\udd53", "\ud84d\ude9e", "\ud858\udc21", "\u3eec", "\ud856\udcde", "\u3af5", "\ud850\udd61", "\ud862\udd0d", "\ud84c\uddea", "\ud842\ude8a", "\ud84c\ude5e", "\u430a", "\u4930", "\u744c", "\u7a2c", "\u34e6", "\u73c4", "\ud857\uddb9", "\u9fc7", "\u492f", "\u4131", "\ud84d\ude8e", "\ud85e\udf65", "\u46ae", "\ud85b\ude88", "\u4181", "\ud857\udd99", "\ud849\udcbc", "\u9fc8", "\ud849\udcc1", "\ud849\udcc9", "\ud849\udccc", "\u9fc9", "\u8504", "\ud84d\uddbb", "\u40b4", "\u9fca", "\u44e1", "\ud86b\uddff", "\u9fcb", "\u31c0", "\ud840\udd0c", "\u31c5", "\ud840\udcd1", "\ud840\udccd", "\u31c6", "\u31c7", "\ud840\udccb", "\ud847\udfe8", "\u31c8", "\ud840\udcca", "\u31c9", "\u31ca", "\u31cb", "\u31cc", "\ud840\udd0e", "\u31cd", "\u31ce", "\u0fff", "\u23da", "\u23db", "\ud868\udfa9", "\ud844\udd45", "\u9d4e", "\ud85d\udf35", "\u6946", "\ud842\udde7", "\u4ccd", "\u9e0c", "\u4c3e", "\ud867\uddf6", "\ud85c\udc0e", "\ud868\udd33", "\u35c1", "\u4911", "\ud861\udc6c", "\ud847\uddca", "\ud841\uddd0", "\ud84a\udee6", "\u4e81", "\u344c", "\u3e48", "\u5003", "\u347d", "\u3493", "\u34a5", "\u35c7", "\u3551", "\u3553", "\u356d", "\u3572", "\u3681", "\u5518", "\u3598", "\u35a5", "\u35bf", "\u35c5", "\ud85f\udd84", "\ud843\udc42", "\ud843\udd15", "\ud854\udd2b", "\ud84b\udcc6", "\u39ec", "\ud840\udf41", "\ud853\uddb8", "\ud865\udce5", "\u4053", "\ud860\udcbe", "\ud84b\udc38", "\u3a34", "\u47d5", "\ud860\udd5d", "\ud85a\uddf2", "\ud853\uddea", "\ud843\udd7c", "\ud843\udfb4", "\ud843\udcd5", "\ud844\udcf4", "\u648d", "\ud843\ude96", "\ud843\udc0b", "\ud843\udf64", "\ud84b\udca9", "\ud860\ude56", "\ud851\udcd3", "\ud843\udd46", "\ud866\ude4d", "\ud860\udce9", "\u47f4", "\ud853\udea7", "\ud84b\udcc2", "\u3a67", "\ud865\uddf4", "\u3fed", "\u3506", "\ud854\udec7", "\ud865\udfd4", "\ud85e\udcc8", "\ud84b\udd44", "\u9d6e", "\u9815", "\u43d9", "\ud858\udca5", "\u54e3", "\ud84b\udd4c", "\ud84a\udfca", "\ud844\udc77", "\u39fb", "\ud844\udc6f", "\ud859\udeda", "\ud859\udf16", "\ud85e\udda0", "\ud854\udc52", "\ud843\udc43", "\ud848\udda1", "\ud862\udf4c", "\ud841\udf31", "\u480b", "\ud840\udda9", "\u3ffa", "\u5873", "\ud84b\udd8d", "\ud851\uddc8", "\ud841\udcfc", "\ud858\udc97", "\ud843\udf4c", "\ud843\udd96", "\u40bb", "\u43ba", "\u4ab4", "\ud84a\ude66", "\ud844\udc9d", "\u98f5", "\ud843\udd9c", "\u39fe", "\ud849\udf75", "\u56a1", "\u647c", "\u3e43", "\ud869\ude01", "\ud843\ude09", "\ud84a\udecf", "\ud84b\udcc9", "\ud844\udcc8", "\ud84e\uddc2", "\u3992", "\u3a06", "\ud860\ude9b", "\u3578", "\ud857\ude49", "\ud848\udcc7", "\u5652", "\ud843\udf31", "\ud84b\udcb2", "\ud865\udf20", "\u34bc", "\ud853\ude3b", "\ud85d\udd74", "\ud84b\ude8b", "\ud848\ude08", "\ud869\ude5b", "\ud863\udccd", "\ud843\ude7a", "\ud843\udc34", "\ud85a\udc1c", "\u7f93", "\ud844\udccf", "\ud84a\udc03", "\ud84a\udd39", "\u35fb", "\ud854\udde3", "\ud843\ude8c", "\ud843\udf8d", "\ud843\udeaa", "\u3f93", "\ud843\udf30", "\ud843\udd47", "\ud844\udd4f", "\ud843\ude4c", "\ud843\udeab", "\ud842\udfa9", "\ud843\udd48", "\ud844\udcc0", "\ud844\udd3d", "\u3ff9", "\ud849\ude96", "\u6432", "\ud843\udfad", "\ud84c\udff4", "\ud85d\ude39", "\ud84a\udfce", "\ud843\udd7e", "\ud843\udd7f", "\ud84b\udc51", "\ud84b\udc55", "\u3a18", "\ud843\ude98", "\ud844\udcc7", "\ud843\udf2e", "\ud869\ude32", "\ud85a\udf50", "\ud863\udcd2", "\ud863\udd99", "\ud863\udcca", "\u95aa", "\ud867\udec3", "\ud85d\udf5e", "\ud84b\uddee", "\u7140", "\ud859\udd72", "\u3797", "\ud860\udcbd", "\ud843\udefa", "\ud843\ude0f", "\ud843\ude77", "\ud843\udefb", "\u35dd", "\ud853\uddeb", "\u3609", "\ud843\udcd6", "\ud849\udfb5", "\ud844\udcc9", "\ud843\ude10", "\ud843\ude78", "\ud844\udc78", "\ud844\udd48", "\ud860\ude07", "\ud845\udc55", "\ud843\ude79", "\ud853\ude50", "\ud84b\udda4", "\u5a54", "\ud844\udc1d", "\ud844\udc1e", "\ud844\udcf5", "\ud844\udcf6", "\ud843\ude11", "\ud85d\ude94", "\ud860\udecd", "\ud843\udfb5", "\ud843\ude7b", "\ud854\udd7e", "\u3703", "\ud843\udfb6", "\ud844\udd80", "\ud854\uded8", "\ud868\udebd", "\ud852\uddda", "\ud846\udc3a", "\ud850\udd77", "\ud860\ude7c", "\ud855\udf3d", "\u4800", "\u4b2c", "\u9f27", "\u49e7", "\u9c1f", "\ud856\udf74", "\ud84c\udd3d", "\u55fb", "\u35f2", "\u5689", "\ud846\udfc1", "\ud87e\udc78", "\ud840\udc86", "\u353e", "\u38fa", "\ud852\udce9", "\ud858\ude6a", "\u34c1", "\ud858\udf4b", "\ud859\ude12", "\ud85a\udd51", "\ud85e\udcb2", "\ud863\ude0f", "\ud866\udc10", "\ud840\udc87", "\u6dfe", "\ud867\udc73", "\u9fa6", "\u3dc9", "\ud850\udd4e", "\u4b20", "\ud854\uddcd", "\u3559", "\ud857\udd30", "\ud862\ude32", "\ud84c\ude81", "\ud868\udd07", "\u3c8b", "\ud846\udd80", "\u4b10", "\u7402", "\ud861\udf0f", "\u4009", "\ud868\udeba", "\u4223", "\u860f", "\ud842\ude6f", "\u7a2a", "\ud866\udd47", "\ud862\udeea", "\ud848\udc7e", "\u93f4", "\ud862\udde3", "\u9fa7", "\u9fa8", "\ud847\uddb6", "\u5fc2", "\ud849\udf12", "\ud84c\udff9", "\u6a43", "\ud84f\udc63", "\ud851\udd05", "\u3edb", "\ud852\ude13", "\u5b15", "\ud857\udca4", "\ud855\ude95", "\u7e6c", "\u9fa9", "\u9faa", "\u8eb9", "\u9fab", "\u99e0", "\u9221", "\u9fac", "\ud863\uddb9", "\ud845\udc3f", "\u4071", "\u42a2", "\u9868", "\u4276", "\ud852\udd7b", "\ud85c\udd0d", "\u4c81", "\ud85b\udd74", "\u5d7b", "\ud85a\udf15", "\ud85b\udfbe", "\u9fad", "\u9fae", "\u9faf", "\u7e5b", "\u3d88", "\u44c3", "\ud84c\ude56", "\ud849\udf96", "\u439a", "\u4536", "\u5cd5", "\ud84e\udf1a", "\u8af9", "\u5c78", "\u3d12", "\ud84d\udd51", "\u5d78", "\u9fb2", "\u4558", "\ud850\udcec", "\ud847\ude23", "\u3978", "\u344a", "\ud840\udda4", "\ud85b\udc41", "\u4fb4", "\ud840\ude39", "\ud866\udcfa", "\ud842\udf9f", "\ud848\uddc1", "\ud862\udd6d", "\u4102", "\u46bb", "\ud864\udc79", "\u3f07", "\u9fb3", "\ud868\uddb5", "\u40f8", "\u37d6", "\u46f7", "\ud85b\udc46", "\u417c", "\ud861\udeb2", "\ud85c\udfff", "\u456d", "\u38d4", "\ud855\udc9a", "\u4561", "\u451b", "\u4d89", "\u4c7b", "\u4d76", "\u45ea", "\u3fc8", "\ud852\udf0f", "\u3661", "\u44de", "\u44bd", "\u41ed", "\u5d56", "\u3dfc", "\u380f", "\u5da4", "\u3820", "\u3838", "\u3908", "\u3914", "\u393f", "\u394d", "\u3989", "\u39b8", "\u39f8", "\u3a03", "\u6407", "\u3a4b", "\u3a97", "\u6586", "\u3abd", "\u3af2", "\u3b22", "\u3b42", "\u3b58", "\u3b72", "\u3b71", "\u3b7b", "\u699f", "\u3bbc", "\u3bdd", "\u6a74", "\u3bec", "\u6a99", "\u3bf2", "\u6ab5", "\u3ccb", "\u6d81", "\u3cef", "\ud862\uddc0", "\u3d46", "\ud84f\udf41", "\u3d6a", "\u3d75", "\u3d8a", "\u3d91", "\ud840\udf25", "\u43c1", "\u35f1", "\ud843\uded8", "\ud84f\uded7", "\u57be", "\ud85b\uded3", "\u713e", "\ud855\udfe0", "\u364e", "\u69a2", "\ud862\udfe9", "\ud856\udce1", "\ud865\udcd9", "\ud856\uddac", "\u7ac2", "\u71d1", "\ud859\udc8d", "\u41ca", "\u41ef", "\ud857\udc01", "\ud854\udf0e", "\ud857\udcfe", "\ud856\udfb4", "\ud85b\udc7f", "\u8421", "\ud857\udd20", "\u3dad", "\ud857\udc65", "\u7c35", "\ud857\udcc1", "\u7c44", "\ud852\udc82", "\ud851\udd78", "\u7cf3", "\u451d", "\ud85b\ude44", "\ud85b\uded6", "\ud850\udc57", "\ud858\udc29", "\u3d13", "\ud845\udff9", "\ud860\udf6d", "\ud858\udd21", "\ud858\udd5a", "\u432b", "\u7f40", "\u7f41", "\u7936", "\ud858\uded0", "\u99e1", "\ud858\udf51", "\ud845\ude61", "\ud840\udc68", "\u455c", "\ud84d\udf66", "\u4503", "\ud860\udf3a", "\ud859\udc89", "\u802f", "\ud868\udc87", "\ud85b\udcc3", "\ud849\udf14", "\u4989", "\ud859\ude26", "\ud84f\udde3", "\ud859\udee8", "\u6725", "\ud862\ude48", "\u58b0", "\ud849\udef6", "\ud859\udc98", "\ud853\udfb8", "\ud845\udc8a", "\ud846\udc5e", "\ud852\ude65", "\ud852\ude95", "\u447a", "\ud842\udf0d", "\ud85a\ude52", "\ud84f\udd7e", "\ud845\udcfd", "\ud85a\udf0a", "\ud852\udda7", "\ud84d\udd30", "\ud845\udf73", "\ud84f\uddf8", "\ud87e\udd94", "\u41db", "\ud843\ude16", "\ud845\udfb4", "\u36c1", "\ud84c\udd7d", "\ud84d\udd5a", "\ud84f\ude8b", "\ud85b\udda3", "\ud85a\udf05", "\ud85a\udf97", "\ud84d\uddce", "\u3dbf", "\u450b", "\ud85b\udda5", "\u347e", "\ud85b\uded4", "\u6a57", "\u3496", "\ud85b\ude42", "\ud84b\udeef", "\ud856\udfe4", "\u3dd3", "\u44e4", "\ud84f\udcb5", "\ud85a\udf96", "\ud85b\ude77", "\ud85b\ude43", "\u44a0", "\ud857\udc91", "\u4240", "\ud857\udcc0", "\u4543", "\ud85b\ude99", "\u4527", "\u4516", "\u67bf", "\ud861\ude25", "\ud861\ude3b", "\ud85c\udc88", "\ud845\udd82", "\ud85c\udccd", "\ud87e\uddb2", "\u456a", "\u3648", "\ud846\udca2", "\ud85c\udf9a", "\ud868\udcf8", "\ud84b\udc27", "\u460f", "\ud85d\udde0", "\ud84f\uddb9", "\ud85d\udde4", "\u465b", "\u7777", "\ud85d\udf0f", "\ud862\ude25", "\ud85e\udd24", "\ud85e\udebd", "\u8a9c", "\u91fe", "\ud85e\ude59", "\ud85e\udf3a", "\ud84f\udf8f", "\u4713", "\ud85e\udf38", "\ud855\udc30", "\ud855\udd65", "\u8b3f", "\ud852\ude7a", "\u8b9b", "\ud845\udedf", "\u4615", "\u884f", "\ud85f\udd54", "\ud85f\udd8f", "\ud87e\uddd4", "\u3725", "\ud85f\udd53", "\ud85f\udd98", "\ud85f\uddbd", "\ud846\udd10", "\u705c", "\u8d11", "\ud853\udcc9", "\u3ed0", "\u8da9", "\ud860\udc02", "\ud844\udc14", "\ud852\udd8a", "\u3b7c", "\ud860\uddbc", "\ud85c\udd0c", "\u8eb6", "\u92d4", "\ud860\udf65", "\ud861\udc12", "\u9303", "\ud868\ude9f", "\ud842\ude50", "\u492a", "\ud862\uddde", "\ud861\udd3d", "\ud84f\uddbb", "\ud84c\ude62", "\ud868\udc14", "\ud861\udebc", "\ud861\udd01", "\ud848\udf25", "\u3980", "\ud85b\uded7", "\ud861\udd3c", "\ud85e\udebe", "\ud861\udd6c", "\ud861\ude0b", "\ud861\udf13", "\ud861\udee6", "\u3af0", "\u91a9", "\u91c4", "\ud862\udd33", "\ud847\ude89", "\u9241", "\ud855\uddb9", "\ud862\udec6", "\ud84f\udc9b", "\ud862\udf0c", "\ud855\udddb", "\ud843\udd31", "\ud862\udee1", "\ud862\udfeb", "\ud862\udee2", "\ud862\udee5", "\u4965", "\ud862\udfec", "\ud863\udc39", "\ud862\udfff", "\u8ebc", "\u9585", "\u9426", "\u42b9", "\ud849\ude7a", "\ud861\uded8", "\ud844\ude7c", "\ud84f\ude2e", "\u49df", "\u416c", "\ud85b\uded5", "\u61da", "\ud862\udee0", "\u49a1", "\ud85b\udcb8", "\ud840\ude74", "\ud859\udc10", "\ud864\udcaf", "\ud864\udce5", "\ud852\uded1", "\ud846\udd15", "\ud84c\udf0a", "\u9736", "\u4a0f", "\u453d", "\u4585", "\ud852\udee9", "\ud864\uddd5", "\u5b4a", "\ud864\uddeb", "\ud84c\udcb7", "\ud84c\udcbc", "\u97c0", "\u97d2", "\ud855\udc6c", "\ud865\udc33", "\ud865\udc1d", "\ud85e\udd7a", "\u4ad1", "\u3b0e", "\ud85c\udd75", "\u3d51", "\ud841\ude30", "\ud850\udd5c", "\ud855\udf06", "\u98ca", "\u4aff", "\ud85b\udd27", "\ud845\uded3", "\u98ec", "\u9378", "\ud852\ude29", "\u4b72", "\ud866\udc57", "\ud866\udd05", "\u9a3b", "\u9a58", "\ud855\udf25", "\u36c4", "\ud864\udcb1", "\ud866\udfd5", "\ud866\udf05", "\u4c0e", "\ud861\ude00", "\u5034", "\ud85a\udda8", "\u38c3", "\ud84c\udc7d", "\ud867\udd3e", "\ud846\udc63", "\ud850\ude4b", "\ud867\ude68", "\ud867\udfb7", "\ud868\udd92", "\ud868\uddab", "\ud868\udce1", "\ud868\udd23", "\ud868\udddf", "\ud868\udd34", "\ud848\udd5b", "\ud868\udd93", "\ud868\ude20", "\ud846\udd3b", "\ud868\ude33", "\u9d39", "\ud868\udcb9", "\ud868\udeb4", "\u9e90", "\u9ea2", "\u4d34", "\ud850\udf64", "\u9ec1", "\u3b60", "\u39e5", "\u3d1d", "\u37be", "\ud863\udc2b", "\u4b96", "\u9424", "\ud85b\udda2", "\u99b8", "\ud864\udc8b", "\u847f", "\u9f8e", "\u7216", "\u4bbe", "\ud852\udd75", "\ud852\uddbb", "\ud852\uddf8", "\ud850\udf48", "\ud852\ude51", "\ud862\udfda", "\ud846\udcfa", "\u799f", "\ud862\udd7e", "\ud863\ude36", "\u93f3", "\ud862\ude44", "\ud862\udd6c", "\ud851\udcb9", "\u3eeb", "\u70d0", "\ud851\udc73", "\ud850\udff8", "\ud845\udfef", "\u70a3", "\ud846\udcbe", "\ud84d\udd99", "\u3ec7", "\ud846\udc85", "\ud855\udc2f", "\ud845\udff8", "\u3722", "\ud845\udefb", "\ud846\udc39", "\u36e1", "\ud845\udf74", "\ud846\udcd1", "\ud857\udf4b", "\u3723", "\ud845\udec0", "\ud852\ude25", "\ud844\udffe", "\ud844\udea8", "\ud844\udfc6", "\ud845\udcb6", "\ud84d\udea6", "\u8455", "\ud852\udd94", "\ud85c\udd65", "\ud84f\ude31", "\ud855\udd5c", "\ud84f\udefb", "\ud85c\udc52", "\u44f4", "\ud84d\udeee", "\ud866\udd9d", "\ud85b\udf26", "\u3733", "\u3c15", "\u3de7", "\ud846\udd22", "\u4057", "\ud84d\udf3f", "\ud850\udce1", "\ud850\udc8b", "\ud850\udd0f", "\ud85b\udc21", "\ud859\udeb1", "\ud843\udfdf", "\ud842\udfa8", "\ud843\ude0d", "\ud862\udf13", "\u939c", "\u512b", "\u3819", "\ud851\udc36", "\ud841\udc65", "\ud840\udf7f", "\ud855\ude51", "\ud840\uddab", "\ud840\udfcb", "\u3999", "\ud840\udf0a", "\ud841\udc14", "\u3435", "\ud840\udec0", "\ud863\udeb3", "\ud840\ude75", "\ud840\ude0c", "\ud852\ude0e", "\ud84f\ude8a", "\ud84d\udd95", "\ud84f\ude39", "\ud84f\udebf", "\ud846\udc84", "\ud84f\ude89", "\ud841\udde0", "\u44dd", "\ud841\udca3", "\ud841\udc92", "\ud841\udc91", "\u8d7a", "\ud862\ude9c", "\ud841\udf0e", "\ud842\udc73", "\u467a", "\ud850\udf8c", "\ud843\udc20", "\ud852\uddac", "\ud844\udce4", "\ud843\ude1d", "\u3ede", "\u7414", "\u4b8e", "\ud852\udebc", "\ud850\udc8d", "\u3584", "\u720f", "\ud850\udcc9", "\ud840\udf45", "\ud842\udfc6", "\u9366", "\u363e", "\u58cb", "\ud862\ude46", "\ud845\udefa", "\ud845\udf6f", "\ud845\udf10", "\u5a2c", "\u59b8", "\ud856\udd46", "\ud846\uddf3", "\ud846\udc61", "\ud850\ude95", "\u36f5", "\ud857\ude83", "\u5a81", "\ud862\udfd7", "\ud841\udc13", "\u93e0", "\ud844\udf03", "\u7105", "\u4972", "\ud862\uddfb", "\u93bd", "\u37a0", "\u5c9e", "\u5e48", "\ud846\udd96", "\ud846\udd7c", "\ud84e\udeee", "\u5ecd", "\u5b4f", "\ud846\udd03", "\ud846\udd04", "\u3701", "\ud846\udca0", "\u36dd", "\ud845\udefe", "\u36d3", "\u812a", "\ud862\ude47", "\ud847\uddba", "\ud84d\udc72", "\ud862\udda8", "\ud846\udd27", "\ud845\udfab", "\ud845\udf3b", "\u5b44", "\ud85d\uddfd", "\ud84a\udc60", "\ud849\ude2b", "\u3eb8", "\ud849\uddaf", "\ud849\uddbe", "\ud864\udc88", "\ud85b\udf73", "\ud840\udc3e", "\ud840\udc46", "\ud849\ude1b", "\ud84b\udc9b", "\ud84b\udd07", "\ud851\uded4", "\ud864\udd4d", "\u6471", "\ud851\ude65", "\ud84a\udf6a", "\u3a29", "\ud84a\udf22", "\ud84d\udc50", "\ud866\udcea", "\ud84b\ude78", "\u6337", "\ud869\udc5b", "\ud852\udde3", "\ud84b\udd67", "\ud84b\udca1", "\u3bf4", "\ud84c\udc8e", "\ud84c\udead", "\ud852\udd89", "\ud84c\udeab", "\ud84c\udee0", "\ud846\udcd9", "\ud865\udc3f", "\ud84c\ude89", "\ud84c\uddb3", "\u3ae0", "\u4190", "\ud855\udd84", "\ud862\udf22", "\ud855\udd8f", "\ud845\udefc", "\ud855\udd5b", "\ud855\udc25", "\u78ee", "\ud84c\udd03", "\ud846\udc2a", "\ud84c\ude34", "\u3464", "\ud84c\ude0f", "\ud84c\udd82", "\ud850\udec9", "\ud85b\udd24", "\u4b93", "\ud85e\udc70", "\ud847\uddeb", "\ud84c\uded2", "\ud84c\udee1", "\ud856\udc72", "\u38d1", "\ud84e\udc3a", "\ud84d\udfbc", "\u3b99", "\ud84d\udfa2", "\ud84c\udffe", "\u3b96", "\ud851\ude2a", "\u3bc4", "\u3863", "\ud84d\udfd5", "\ud851\udc87", "\ud846\udd12", "\u6511", "\u6a4c", "\u3bd7", "\u6b57", "\ud84f\udfc0", "\ud84f\udc9a", "\u93a0", "\ud862\udfea", "\ud862\udecb", "\ud860\udc1e", "\ud862\udddc", "\u9467", "\u6f0b", "\ud852\uddec", "\ud84f\udf7f", "\u3d8f", "\ud850\udc3c", "\u5847", "\u6d24", "\u713b", "\ud850\udf1a", "\ud850\ude76", "\u7294", "\ud851\udf8f", "\ud851\udf25", "\ud852\udea4", "\ud841\uddeb", "\ud84f\udef8", "\ud84d\ude5f", "\ud852\ude4a", "\ud852\udd17", "\ud857\udfe1", "\u3f06", "\u3eb1", "\ud852\udedf", "\ud863\udc23", "\ud84f\udf35", "\u3ef3", "\u9387", "\u449f", "\ud85b\uddea", "\u4551", "\u3f63", "\ud853\udcd9", "\ud853\udd06", "\u3f58", "\u7673", "\ud869\uddc6", "\u3b19", "\ud862\udecc", "\ud852\uddab", "\ud852\udd8e", "\u3afb", "\u3dcd", "\ud852\ude4e", "\u3eff", "\ud852\uddc5", "\ud852\udcf3", "\u91fa", "\u9342", "\ud862\udee3", "\ud846\udc64", "\ud854\ude21", "\ud854\udde7", "\u7778", "\ud84c\ude32", "\u770f", "\ud851\ude97", "\ud84d\udf81", "\u3a5e", "\ud852\udcf0", "\u749b", "\u3ebf", "\ud852\udeba", "\ud852\udec7", "\u40c8", "\ud852\ude96", "\ud858\uddae", "\u9307", "\ud855\udd81", "\ud85d\udf41", "\ud855\udee3", "\u410e", "\u8496", "\u79a5", "\ud84f\udefa", "\u79f4", "\u416e", "\ud845\udee6", "\u4132", "\ud843\udd4c", "\ud852\udd8c", "\ud840\ude99", "\ud84f\uddba", "\ud845\udf6e", "\u3597", "\u3570", "\u36aa", "\ud840\uddd4", "\ud843\udc0d", "\ud849\udef5", "\ud856\udeaf", "\ud856\ude9c", "\ud840\ude5b", "\u78f0", "\ud856\udfc6", "\u41f9", "\u7c5d", "\u4211", "\ud856\udfb3", "\ud857\udebc", "\ud857\udea6", "\ud852\uddf9", "\ud845\udfb0", "\u7c8e", "\u6ab2", "\u7e07", "\u7dd3", "\ud858\ude61", "\ud858\udd5c", "\ud85e\udf48", "\ud857\ude82", "\u426a", "\ud85a\udf75", "\ud842\udd16", "\ud840\udc4e", "\ud84d\uddcf", "\ud859\udc12", "\ud858\udff8", "\ud852\udd62", "\u7fdd", "\ud842\udc2c", "\ud856\udee9", "\ud857\udd43", "\ud857\ude0e", "\u99e6", "\u8645", "\u9a63", "\u6a1c", "\ud84d\udc3f", "\u39e2", "\ud852\uddf7", "\ud859\uddad", "\u9a1f", "\ud859\udda0", "\u8480", "\ud85c\udd27", "\ud85b\udcd1", "\u44ea", "\u4402", "\u8142", "\ud859\udfb4", "\ud85a\ude42", "\u8265", "\ud85a\ude51", "\u8453", "\ud85b\udda7", "\ud85c\ude1b", "\u5a86", "\u417f", "\ud846\udc40", "\u5b2b", "\ud846\udca1", "\ud846\udcd8", "\u86a0", "\ud87e\uddbc", "\ud84f\udd8f", "\ud85d\udc22", "\u8965", "\ud855\ude83", "\u8954", "\ud85d\udf85", "\ud85d\udf84", "\ud862\udff5", "\ud862\udfd9", "\ud862\udf9c", "\ud862\uddf9", "\u3ead", "\u84a3", "\u46f5", "\u46cf", "\u37f2", "\u8a1c", "\ud865\udc48", "\u922b", "\ud850\ude84", "\u7129", "\ud846\udc45", "\u9d6d", "\u8c9f", "\u8ce9", "\ud85f\udddc", "\u59f0", "\u436e", "\u36d4", "\ud853\udc09", "\u8f30", "\u8f4a", "\u42f4", "\u6fbb", "\ud848\udf21", "\u489b", "\u6e8b", "\ud845\udfda", "\u9be9", "\u36b5", "\ud852\udd2f", "\u5571", "\u4906", "\ud862\ude4b", "\u4062", "\ud862\udefc", "\u9427", "\ud863\udc1d", "\ud863\udc3b", "\u9597", "\ud863\udd34", "\u7445", "\u3ec2", "\ud852\udcff", "\ud852\ude42", "\ud850\udfea", "\u3ee7", "\ud84c\ude25", "\ud863\udee7", "\ud863\ude66", "\ud863\ude65", "\u3ecc", "\ud852\udded", "\ud852\ude78", "\ud84f\udfee", "\u7412", "\u3efc", "\ud864\udcb0", "\u4a1d", "\ud864\udc93", "\ud855\udfdf", "\u9368", "\ud862\udd89", "\ud863\udc26", "\ud862\udf2f", "\ud858\udfbe", "\u5b11", "\u8b69", "\u493c", "\ud850\ude1b", "\u979b", "\u9938", "\ud843\udf26", "\u5dc1", "\ud862\udfc5", "\ud852\udeb2", "\u981f", "\ud865\udcda", "\u92f6", "\ud865\uddd7", "\u44c0", "\ud862\udf50", "\ud852\ude67", "\ud862\udf64", "\ud862\ude45", "\u3f00", "\u922a", "\u4925", "\u8414", "\ud85e\udf06", "\u3dfd", "\u4b6f", "\u99aa", "\u9a5c", "\ud862\udf65", "\ud856\udcc8", "\u9a21", "\u5afe", "\u9a2f", "\ud866\udcf1", "\u4b90", "\ud866\udd48", "\u4bbd", "\u4b97", "\ud844\udf02", "\ud852\uddb8", "\ud845\udce8", "\ud849\udf1f", "\ud84f\uddb8", "\u3d7d", "\u9458", "\u3927", "\ud849\udf81", "\ud84a\udd6b", "\ud867\ude2d", "\ud868\uddf5", "\ud868\udcfe", "\u9d21", "\u4cae", "\ud850\udd04", "\u9e18", "\u4cb0", "\u9d0c", "\ud868\uddb4", "\ud868\udced", "\ud868\udcf3", "\ud866\udd2f", "\u9da5", "\ud85b\ude12", "\ud85b\udfdf", "\ud85a\udf82", "\u4533", "\ud85b\udda4", "\ud85b\ude84", "\ud85b\uddf0", "\u85ee", "\ud85b\ude00", "\ud84d\udfd7", "\ud858\udc64", "\ud84d\udd9c", "\ud84d\ude40", "\u492d", "\ud852\uddde", "\u3d62", "\u93db", "\u92be", "\ud840\udebf", "\u944d", "\u3440", "\ud855\udd5d", "\ud845\udf57", "\ud84c\uddc9", "\ud852\udd41", "\u369a", "\u6fd9", "\ud850\uddb5", "\u57bb", "\u9d16", "\u34af", "\ud850\uddac", "\u71eb", "\ud85b\udc40", "\ud853\udf97", "\ud845\udfb5", "\ud862\ude49", "\u5ace", "\u42bc", "\ud851\udc88", "\u372c", "\u4b7b", "\ud862\uddfc", "\u93bb", "\u93b8", "\ud846\udcd6", "\ud843\udf1d", "\ud85b\udcc0", "\ud845\udc13", "\ud850\udefa", "\ud84b\udc26", "\ud850\udfc1", "\ud84f\uddb7", "\ud859\udf41", "\u7da8", "\ud858\udd5b", "\ud858\udca4", "\ud852\uddb9", "\ud852\udd8b", "\ud862\uddfa", "\u3ee9", "\u74b4", "\ud862\udf63", "\ud846\udc9f", "\u3ee1", "\ud852\udeb3", "\u6ad8", "\u3ed6", "\ud852\ude3e", "\ud852\ude94", "\ud845\udfd9", "\ud852\ude66", "\ud840\udfa7", "\ud845\udc24", "\ud852\udde5", "\u7448", "\ud852\udd16", "\u70a5", "\ud852\udd76", "\u9284", "\u935f", "\ud841\udcfe", "\u9331", "\ud862\udece", "\ud862\ude16", "\u9386", "\ud862\udfe7", "\ud855\uddd5", "\u4935", "\ud862\ude82", "\u716b", "\ud852\udd43", "\ud843\udcff", "\ud841\ude1a", "\ud842\udfeb", "\ud843\udcb8", "\ud845\udffa", "\u7dfe", "\ud845\udec2", "\ud852\ude50", "\ud846\udc52", "\u452e", "\u370a", "\ud862\udec0", "\ud852\uddad", "\ud846\udcbf", "\ud846\udc83", "\ud85d\udc84", "\u5aa1", "\u36e2", "\ud84f\udd5b", "\u36b0", "\u925f", "\ud862\ude81", "\ud846\udc62", "\u3ccd", "\ud842\udeb4", "\u4a96", "\u398a", "\u3d69", "\u3d4c", "\ud844\udf9c", "\u42fb", "\ud860\ude18", "\ud864\udce4", "\u44eb", "\ud85f\ude4f", "\u7067", "\u3cd6", "\ud84f\udfed", "\ud84f\ude2d", "\u6e02", "\u3d6f", "\ud840\udff5", "\u36bc", "\u34c8", "\u4680", "\u3eda", "\u4871", "\u493e", "\ud863\udc1c", "\ud85a\udfc0", "\u36d6", "\ud845\udc52", "\ud850\udf62", "\ud852\ude71", "\ud84b\udfe3", "\ud844\udeb0", "\ud848\udfbd", "\ud844\udf98", "\ud84d\udce5", "\ud85e\udff4", "\ud84d\udedf", "\ud862\ude83", "\ud84d\udfd6", "\ud84c\udffa", "\ud853\udc9f", "\ud84d\udead", "\ud85b\udcb7", "\u44df", "\u44ce", "\ud85b\udd26", "\ud85b\udd51", "\ud85b\udc82", "\ud85b\udfde", "\u6f17", "\ud85c\udd09", "\ud845\udf3a", "\ud85b\udc80", "\ud85c\udc53", "\ud845\udfdb", "\u5a82", "\ud845\udfb3", "\u5a71", "\ud846\udd05", "\ud850\uddfc", "\u372d", "\ud845\udf3c", "\u36c7", "\ud850\udea5", "\u5a6e", "\u5a2b", "\ud850\ude93", "\ud84f\udef9", "\ud85d\udf36", "\ud851\udc5b", "\ud850\udeca", "\u711d", "\ud850\ude59", "\ud862\udde1", "\ud85b\udd28", "\ud851\udcce", "\ud85f\ude4d", "\ud850\udfbd", "\ud850\ude56", "\ud844\udf04", "\u70a6", "\ud850\udfe9", "\u3da5", "\ud87e\udc25", "\ud852\ude4f", "\u3df3", "\ud852\ude5d", "\ud845\udfdf", "\u7da4", "\ud84e\udefa", "\ud84c\udf00", "\ud840\ude14", "\ud842\udcd5", "\ud841\ude19", "\u3fe5", "\ud847\udf9e", "\ud868\udeb6", "\u7003", "\ud864\udd5b", "\ud862\ude59", "\ud865\udc20", "\ud85e\udef4", "\ud855\udef6", "\u7341", "\u7348", "\u3ea9", "\ud85e\udf18", "\ud852\udcf2", "\u3eca", "\u3ed1", "\u7419", "\u741e", "\u741f", "\u3ee2", "\u3ef0", "\u3ef4", "\u3efa", "\u3f0e", "\u3f53", "\u3f7c", "\u3fc0", "\u3fd7", "\u3fdc", "\ud853\udf5c", "\u401d", "\u4039", "\u4045", "\u35db", "\u7798", "\u406a", "\u406f", "\u77cb", "\u40a8", "\u7866", "\ud855\udd35", "\u7933", "\u7932", "\u4103", "\u4109", "\u7999", "\u4167", "\u41b2", "\u41c4", "\u41cf", "\u4260", "\u427a", "\u428c", "\u7cb8", "\u4294", "\u7ced", "\ud843\udccf", "\u7dd4", "\u7dd0", "\u7dfd", "\u4397", "\u3dcc", "\u70a0", "\u43ed", "\u4401", "\u3b39", "\u4413", "\u4425", "\u442d", "\u8254", "\u448f", "\u82ff", "\u44b0", "\u70f5", "\u4504", "\u84f8", "\u8552", "\u453b", "\u8570", "\u4577", "\u8692", "\u4606", "\u4617", "\u8947", "\u8991", "\ud85e\udd67", "\u8a29", "\u8a38", "\u8ab4", "\u8cd4", "\u8d1c", "\u4798", "\u47ed", "\u5754", "\u4837", "\u8ee4", "\u8ef2", "\u8fcc", "\u48ad", "\u491e", "\u926b", "\u92b1", "\u92eb", "\u92f4", "\u92fd", "\u9343", "\u9384", "\u4945", "\u4951", "\u941d", "\u942d", "\u496a", "\u9454", "\u9479", "\u49a7", "\u49e5", "\u4a24", "\u9740", "\u4a35", "\u97c2", "\u4ae4", "\u98b9", "\u4b19", "\u98f1", "\u9919", "\u9937", "\u995d", "\u9962", "\u4b70", "\u4b9d", "\u9a3c", "\u9b69", "\u9b81", "\u9bf4", "\u4c6d", "\u9c20", "\u376f", "\ud846\udfc2", "\u9d49", "\u9dbd", "\u9dc0", "\u9dfc", "\u9eb1", "\ud840\udc94", "\ud840\udeb7", "\ud840\udfa0", "\ud841\udcd7", "\u37b9", "\ud841\uddd5", "\ud841\ude15", "\ud841\ude76", "\ud845\udeba", "\ud842\udec2", "\ud842\udecd", "\ud842\udfbf", "\ud87e\udc3b", "\ud842\udfcb", "\ud842\udffb", "\ud843\udc3b", "\ud843\udc53", "\ud843\udc65", "\ud843\udc7c", "\ud843\udc8d", "\ud843\udcb5", "\ud843\udcdd", "\ud843\udced", "\ud843\udd6f", "\ud843\uddb2", "\ud843\uddc8", "\ud843\ude04", "\ud843\ude0e", "\ud843\uded7", "\ud843\udf90", "\ud843\udf2d", "\ud843\ude73", "\ud843\udfbc", "\ud844\udc5c", "\ud844\udc4f", "\ud844\udc76", "\ud844\udc7b", "\ud844\udc88", "\ud844\udc96", "\u3647", "\ud844\udcbf", "\ud844\udcd3", "\ud844\udd2f", "\ud844\udd3b", "\ud844\udee3", "\ud844\udf75", "\ud844\udf36", "\ud845\udd77", "\ud845\ude19", "\ud845\udfc3", "\ud845\udfc7", "\u4e78", "\ud846\udc2d", "\ud846\udd6a", "\ud846\ude2d", "\ud846\ude45", "\ud847\udc2a", "\ud847\udc70", "\ud847\udcac", "\ud847\udec8", "\ud847\uded5", "\ud847\udf15", "\ud848\udc45", "\u69e9", "\u36c8", "\ud848\ude7c", "\ud848\udfd7", "\ud848\udffa", "\ud849\udf2a", "\ud84a\udc71", "\ud84a\udd4f", "\ud84a\udd67", "\ud84a\udd93", "\ud84a\uded5", "\ud84a\udee8", "\ud84a\udf0e", "\ud84a\udf3f", "\ud84b\udc4c", "\ud84b\udc88", "\ud84b\udcb7", "\ud856\udfe8", "\ud84b\udd08", "\ud84b\udd12", "\ud84b\uddb7", "\ud84b\udd95", "\ud84b\ude42", "\ud84b\udf74", "\ud84b\udfcc", "\ud84c\udc33", "\ud84c\udc66", "\ud84c\udf1f", "\ud84c\udfde", "\u6648", "\ud85e\ude79", "\ud84d\udd67", "\ud84d\uddf3", "\ud852\uddba", "\ud84d\ude1a", "\ud84d\udf16", "\ud840\udf46", "\u58b5", "\u6918", "\ud84e\udea7", "\ud85d\ude57", "\ud857\udfe2", "\ud84f\ude11", "\ud84f\udeb9", "\ud85d\uddfe", "\ud848\udc9a", "\u48d0", "\u4ab8", "\ud850\udd19", "\ud862\ude9a", "\ud850\udeee", "\ud850\udf0d", "\ud850\udc3b", "\ud850\udf34", "\ud850\udf96", "\ud852\ude45", "\ud841\uddca", "\ud841\ude11", "\ud847\udea8", "\u3bbe", "\ud84f\udcff", "\ud851\udc04", "\ud851\udcd6", "\ud851\ude74", "\u399b", "\ud851\udf2f", "\ud861\udde8", "\ud866\uddc9", "\u3762", "\ud848\uddc3", "\ud862\udf4e", "\ud852\udc12", "\ud852\udcfb", "\ud852\ude15", "\ud852\udec0", "\ud843\udc78", "\ud853\udea5", "\ud853\udf86", "\ud841\udf79", "\u8eda", "\ud854\udc2c", "\u528f", "\ud854\ude99", "\ud855\udc19", "\ud84f\udf4a", "\ud852\udea7", "\ud855\udc46", "\ud855\udc6e", "\ud85a\udf52", "\ud855\udd3f", "\ud85d\ude32", "\ud855\udd5e", "\u4718", "\ud855\udd62", "\ud855\udd66", "\ud855\udfc7", "\ud852\udd3f", "\ud856\udc5d", "\u34fb", "\ud84c\udfcc", "\ud856\udd03", "\ud862\udd48", "\ud856\udeae", "\ud856\udf89", "\ud857\udc06", "\ud847\udd90", "\u7151", "\ud858\udd02", "\ud85f\udc12", "\ud858\uddb2", "\ud853\udf9a", "\u8b62", "\ud859\udc02", "\ud859\udc4a", "\ud85a\udff7", "\ud859\udc84", "\ud846\udd1c", "\ud852\uddf6", "\ud859\udc88", "\ud84f\udfef", "\ud859\udd12", "\u4bc0", "\ud859\uddbf", "\ud859\udeb5", "\ud849\udf1b", "\u9465", "\ud855\udfe1", "\ud87e\udccd", "\ud851\udd21", "\ud859\udefc", "\ud852\udd34", "\ud85b\udcbd", "\u3618", "\ud859\udf99", "\ud85a\udc6e", "\ud859\udc11", "\ud85a\udc5e", "\ud85a\udcc7", "\u7b42", "\ud864\udcc0", "\ud842\ude11", "\ud85a\udd26", "\ud85a\udd39", "\ud85a\uddfa", "\u9a26", "\ud85a\ude2d", "\u365f", "\ud859\udc69", "\ud840\udc21", "\ud85a\ude34", "\ud85a\udf5b", "\ud84d\udd19", "\ud85a\udf9d", "\u46d0", "\ud85b\udca4", "\ud85b\uddae", "\u58b6", "\u371c", "\ud849\udd8d", "\ud85c\udc4b", "\ud85c\uddcd", "\u3c54", "\ud85c\ude80", "\ud85c\ude85", "\u9281", "\ud848\udd7a", "\ud85c\ude8b", "\u9330", "\ud85c\udee6", "\ud852\uddd0", "\ud85d\udc50", "\ud843\udef8", "\ud84a\udd26", "\ud861\udc73", "\ud845\udfb1", "\ud852\ude2a", "\ud846\udc20", "\u39a4", "\u36b9", "\u453f", "\ud867\udcad", "\ud866\udca4", "\ud85d\udfcc", "\ud85e\udc58", "\u40df", "\ud845\ude0a", "\u39a1", "\ud84d\udf2f", "\ud860\udce8", "\ud844\udfc5", "\ud85e\udddd", "\ud864\udda8", "\u4cb7", "\ud85c\udcaf", "\ud862\uddab", "\ud85e\uddfd", "\ud85e\ude0a", "\ud85e\udf0b", "\ud85f\udd66", "\ud850\udd7a", "\u7b43", "\ud860\udc09", "\ud868\udedf", "\ud860\udf18", "\ud85b\ude07", "\u93bf", "\ud860\udd6f", "\ud860\udc23", "\ud85a\uddb5", "\ud844\udfed", "\ud84c\ude2f", "\ud860\udc48", "\u5d85", "\ud863\udc30", "\ud860\udc83", "\ud862\udd49", "\ud852\udd88", "\ud852\udea5", "\ud84f\udf81", "\u3c11", "\ud860\udc90", "\ud860\udcf4", "\ud860\udd2e", "\ud847\udfa1", "\ud860\udd4f", "\ud860\udd89", "\ud860\uddaf", "\ud860\ude1a", "\ud860\udf06", "\ud860\udf2f", "\ud860\udf8a", "\u35ca", "\ud861\udc68", "\ud861\udeaa", "\u48fa", "\u63e6", "\ud862\udd56", "\u7808", "\u9255", "\ud862\uddb8", "\u43f2", "\ud862\udde7", "\u43df", "\ud862\udde8", "\ud862\udf46", "\ud862\udfd4", "\ud863\udc09", "\ud863\udfc5", "\ud864\udcec", "\ud864\udd10", "\ud864\udd3c", "\u3df7", "\ud864\udd5e", "\ud852\udeca", "\ud865\udce7", "\ud865\udde9", "\ud865\uddb0", "\ud865\uddb8", "\ud865\udf32", "\ud866\udcd1", "\ud866\udd49", "\ud866\udd6a", "\ud866\uddc3", "\ud866\ude28", "\ud866\udf0e", "\ud867\udd5a", "\ud867\udd9b", "\ud867\udef8", "\ud867\udf23", "\u4ca4", "\ud868\ude93", "\ud868\udeff", "\u4d91", "\ud869\uddcb", "\u4d9c", "\ud843\udc9c", "\ud849\udcb0", "\ud852\ude93", "\u4509", "\u6f56", "\u34e4", "\ud862\udf2c", "\ud85e\udc9d", "\u373a", "\ud845\udff5", "\ud860\udc24", "\ud862\udf6c", "\ud862\udf99", "\ud85e\ude3e", "\ud859\udeaf", "\u3deb", "\ud85d\ude55", "\ud84f\udcb7", "\ud855\ude35", "\ud856\udd56", "\ud857\ude81", "\ud858\ude58", "\u56bf", "\ud843\ude6d", "\ud84f\ude88", "\ud853\udc9e", "\ud845\udff6", "\ud846\udc7b", "\ud857\udc4a", "\ud854\udf11", "\u3dc6", "\ud867\udd98", "\u4c7d", "\u7f49", "\ud857\uded8", "\ud84f\udd40", "\ud843\udfea", "\ud843\udd49", "\ud84d\udeba", "\u8d18", "\u9345", "\ud843\ude9d", "\u35ce", "\ud860\udee2", "\u362d", "\u5572", "\ud843\udc41", "\ud843\udc96", "\ud854\udd48", "\ud843\ude76", "\ud84b\udc62", "\ud843\udea2", "\ud844\udc75", "\u71f6", "\ud84a\udf43", "\ud84b\udeb3", "\u34df", "\ud843\udda7", "\u51a7", "\u7666", "\ud85a\udc8a", "\u81b6", "\ud844\udcc1", "\u44ec", "\ud851\udf06", "\ud85a\udc93", "\ud849\udef4", "\ud85f\udd2f", "\ud850\udda3", "\ud85f\udd73", "\ud85b\uded0", "\ud85c\udeb6", "\ud844\uddd9", "\u9208", "\ud84f\udcfc", "\ud869\udea9", "\ud843\udeac", "\ud843\udef9", "\ud847\udca2", "\u474e", "\ud853\udfc2", "\ud85f\udff9", "\ud843\udfeb", "\u40fa", "\ud84b\udda0", "\u48f3", "\ud851\udfe0", "\ud867\udd7c", "\ud843\udfec", "\ud843\ude0a", "\ud85d\udda3", "\ud843\udfed", "\ud858\udc48", "\ud844\udd87", "\u71a3", "\u3577", "\u5b0d", "\u36ac", "\u39dc", "\u36a5", "\ud851\ude18", "\ud852\udf6e", "\ud856\ude95", "\ud842\udd79", "\u3a52", "\ud849\udc65", "\u7374", "\ud867\udeac", "\u4d09", "\u9bed", "\ud84f\udcfe", "\ud867\udf30", "\u4c5b", "\ud853\udfa9", "\ud865\udd9e", "\ud867\udfde", "\ud84f\uddb6", "\ud85c\udeb2", "\ud859\udfb3", "\ud84d\udf20", "\ud84f\udef7", "\ud84f\ude2c", "\u3a2a", "\u3e74", "\u367a", "\u45e9", "\ud841\udc8e", "\u5af0", "\ud843\udeb6", "\ud85f\udf2e", "\u58a7", "\u40bf", "\ud869\udc34", "\u4ce1", "\u37fb", "\ud84c\udcda", "\ud850\udff2", "\ud844\udea9", "\ud852\udd63", "\ud867\ude06", "\ud85c\udcae", "\u35ad", "\ud845\udf6c", "\ud865\udcd0", "\ud858\udf35", "\ud85c\udd64", "\ud843\udd28", "\ud85b\udd22", "\ud852\udee2", "\ud843\udd71", "\ud847\udf0f", "\u5d8e", "\ud847\uddd1", "\u9b02", "\u5cd1", "\ud852\udd3e", "\u5573", "\u3e06", "\u692c", "\u4c3b", "\ud845\udf6d", "\ud863\ude97", "\ud85b\udd23", "\u6aca", "\u5611", "\ud840\udffc", "\ud857\udc21", "\ud84f\udcfd", "\ud852\udd19", "\ud843\udcd4", "\ud840\uddf2", "\u35fe", "\u35f3", "\ud869\ude4a", "\ud860\udf7d", "\u8e28", "\ud852\ude77", "\ud862\ude5a", "\ud868\udeb2", "\ud87e\udc40", "\u8d0c", "\u8ceb", "\ud852\udebb", "\u44b7", "\ud846\udc3b", "\ud85b\ude05", "\ud849\udd1b", "\u87f5", "\u35d6", "\u4c07", "\ud858\udd59", "\u4c04", "\u3a5c", "\ud84c\udff5", "\u35d2", "\u5d57", "\ud862\udfc2", "\ud863\ude39", "\ud847\udd46", "\ud843\udf3b", "\u4065", "\ud857\udf1a", "\u8063", "\ud85d\udc86", "\ud859\udfcc", "\ud85b\uded1", "\u8b43", "\u3635", "\ud850\udc11", "\u3ddb", "\u3cd1", "\ud862\udf2d", "\u4b7e", "\u3c18", "\ud84f\udcc7", "\ud857\uded7", "\ud85d\ude56", "\ud855\udd31", "\ud846\udd44", "\ud844\udefe", "\ud866\udd03", "\ud85b\udddc", "\ud85c\udcad", "\ud858\uddad", "\ud862\ude0f", "\ud84d\ude77", "\ud840\udcee", "\ud85a\udc46", "\ud853\udf0e", "\u4562", "\u5b1f", "\ud858\udf4c", "\ud858\ude6b", "\u2400", "\u2421", "\u2f33", "\u273d", "\u21b8", "\u21b9", "\u31cf", "\ud840\udccc", "\ud840\udc8a", "\u4491", "\u9fb0", "\u9fb1", "\ud85d\ude07", "\u2e80", "\u2e86", "\u2e87", "\u2e8a", "\u2e8d", "\u2e95", "\u2e9c", "\u2e9d", "\u2ea5", "\u2eac", "\u2ebc", "\u2ebe", "\u2ec6", "\u2ecc", "\u2ecd", "\u2ecf", "\u2ed6", "\u2ed7", "\u2ede", "\u2ee3", "\uffed", "\ud841\udd47", "\u92db", "\ud841\udddf", "\ud84f\udfc5", "\u854c", "\u42b5", "\u3649", "\ud852\udd42", "\ud862\udde4", "\ud846\udddb", "\ud84f\udcc8", "\ud852\udd33", "\ud862\uddaa", "\ud840\udea0", "\ud85a\udfb3", "\ud844\udf05", "\ud849\udced", "\u5008", "\ud85b\udd29", "\ud85e\ude84", "\ud84d\ude00", "\ud852\udeb1", "\ud849\udd13", "\ud840\udf7e", "\ud840\udf80", "\ud840\udf47", "\ud841\udc1f", "\u347a", "\u3743", "\u8416", "\ud852\udda4", "\ud841\udc87", "\u5160", "\ud84c\udfb4", "\ud842\udfff", "\ud848\udcfc", "\ud840\udee5", "\ud849\udd30", "\ud841\udd8e", "\ud84c\ude33", "\ud846\udd83", "\ud841\uddb3", "\ud84f\udc99", "\u3cdc", "\ud852\udea6", "\ud84d\udf2d", "\u7c15", "\u8542", "\ud85a\udf13", "\ud862\udede", "\ud84f\udf80", "\ud842\udd54", "\ud84f\udfec", "\ud842\udfe2", "\ud845\udf26", "\u681b", "\u73d5", "\u3eaa", "\u38cc", "\ud845\udee8", "\u71dd", "\u44a2", "\ud861\udeab", "\ud845\udd96", "\ud845\ude13", "\ud862\ude9b", "\ud855\udf72", "\u3f59", "\u3aab", "\ud842\udf8f", "\ud84f\udfeb", "\ud84b\udda3", "\ud843\udc77", "\ud85a\udf53", "\ud843\udd74", "\u47a6", "\ud845\udf0d", "\ud843\udedd", "\u3db4", "\ud843\udd4d", "\ud862\uddbc", "\ud849\ude98", "\u4ced", "\u7417", "\ud846\udcd7", "\ud850\udc3a", "\u4552", "\ud851\udc35", "\ud844\udcb4", "\u66cd", "\ud84c\ude8a", "\u78f1", "\u9787", "\ud862\udf66", "\u3623", "\ud844\ude4f", "\ud850\udda5", "\u6c6e", "\u36b1", "\ud85b\udc7e", "\ud845\udc16", "\ud845\udc54", "\ud850\udf63", "\ud852\udff5", "\u585c", "\u3561", "\u58e0", "\ud844\ude3c", "\ud868\udd50", "\ud850\ude78", "\u35a1", "\u36c3", "\ud845\ude3e", "\ud845\ude92", "\u8505", "\ud843\udd4e", "\ud85b\udc81", "\ud85b\udd2a", "\ud845\udfdc", "\ud845\udffb", "\ud845\udfb2", "\ud85b\udda6", "\ud846\udc28", "\ud845\uded5", "\ud85b\ude45", "\u36e6", "\ud852\udda9", "\u3708", "\ud85b\udfa1", "\ud849\udd54", "\u3d85", "\ud846\udd11", "\u3732", "\ud845\udeb8", "\ud85e\ude0e", "\u4004", "\u485d", "\ud840\ude04", "\u5bd5", "\ud846\ude34", "\ud856\uddcc", "\ud841\udda5", "\u4d10", "\ud846\udf44", "\ud847\udca5", "\ud85a\udf28", "\u48dd", "\u5c85", "\ud847\uddf9", "\ud847\ude37", "\u5d10", "\ud847\udea4", "\u5dd7", "\u382d", "\ud852\udd01", "\ud848\udc49", "\ud848\udd73", "\u3836", "\u3bc2", "\u6a8a", "\ud851\udcbc", "\ud843\udcd3", "\ud845\udf71", "\ud861\udc82", "\u38a0", "\u941b", "\ud840\uddc1", "\ud87e\udc94", "\u3ade", "\u48ae", "\ud844\udf3a", "\ud85a\udc88", "\ud848\udfd0", "\ud849\udc71", "\u97bd", "\ud85b\ude6e", "\u9340", "\ud862\ude36", "\u5db6", "\u3d5f", "\ud854\ude50", "\ud847\udf6a", "\ud85c\udcf8", "\ud849\ude68", "\ud840\ude9e", "\ud862\ude29", "\ud846\udc77", "\u3963", "\u3dc7", "\u3639", "\u5790", "\ud849\udfb4", "\u7971", "\u3e40", "\ud852\udd82", "\ud852\udd8f", "\ud85e\ude53", "\u74a4", "\u50e1", "\ud87e\udca6", "\ud85b\uded2", "\ud841\ude56", "\ud84f\udfb7", "\ud84a\udc5f", "\ud862\udf9d", "\ud866\udd5d", "\u3932", "\ud84a\udd80", "\ud84a\udcc1", "\u615c", "\ud840\udd18", "\ud845\udf70", "\ud84b\ude0d", "\ud852\udddf", "\u3a17", "\u6438", "\ud844\udf8e", "\ud845\udffc", "\ud84b\ude36", "\ud850\udc8c", "\ud855\udf1d", "\u947b", "\u3a66", "\u3a57", "\ud852\ude28", "\ud852\ude23", "\ud84c\udc7e", "\u65b5", "\ud852\udd40", "\u4b37", "\u40d8", "\ud846\udc29", "\ud84d\udc00", "\ud84c\uddf7", "\ud84c\uddf8", "\ud84c\udda4", "\ud84c\udda5", "\ud843\ude75", "\ud854\udde6", "\ud847\ude3d", "\ud84c\ude31", "\ud861\uddf4", "\ud84c\uddc8", "\ud854\udf13", "\u77c5", "\ud84a\udcf7", "\u99a4", "\ud850\udf9c", "\ud852\ude21", "\u3b2b", "\u69fa", "\ud84d\udfc2", "\ud850\uddcd", "\ud864\udced", "\u44e9", "\ud84c\udfe6", "\ud85b\udda0", "\ud84d\udc6f", "\ud862\udedf", "\ud84d\uddcd", "\u3d32", "\u3a01", "\ud84d\ude3c", "\u3b80", "\ud862\ude4a", "\u42fc", "\u3ba1", "\ud840\udfc9", "\ud84d\ude59", "\ud848\udd2a", "\ud84d\udf03", "\u3bf3", "\ud864\udd9c", "\u3c0d", "\ud842\udd23", "\ud849\udfcd", "\ud84e\udedb", "\ud840\udfb5", "\ud846\udd58", "\u3740", "\ud84e\udf5a", "\ud84f\udefc", "\ud849\udc8b", "\ud852\udcf1", "\ud85a\udf51", "\ud84f\uddbc", "\u44c5", "\ud84f\uddbd", "\ud850\udda4", "\ud852\udd0c", "\ud852\udd00", "\ud84f\udcc9", "\u36e5", "\u3ceb", "\ud843\udd32", "\ud84c\uddf9", "\ud849\udc91", "\ud85b\udd25", "\ud85b\udda1", "\ud85b\uddeb", "\u6e7c", "\ud852\udd7f", "\ud850\udc85", "\ud85b\ude72", "\ud85b\udf74", "\u842e", "\ud862\udf21", "\ud84f\ude2f", "\u7453", "\ud84f\udf82", "\u5a91", "\ud84c\udc4b", "\u6ff8", "\u370d", "\ud84f\ude30", "\ud845\udc97", "\ud850\udc3d", "\u4555", "\u93f0", "\u3d4e", "\ud864\udd70", "\u3d3b", "\ud850\udd44", "\ud850\udc91", "\ud850\udd55", "\ud850\udc39", "\ud84f\udff0", "\ud84f\udfb4", "\ud850\udd3f", "\ud850\udd56", "\ud850\udd57", "\ud850\udd40", "\ud858\udddd", "\u70a7", "\u70cc", "\u4104", "\u3de8", "\ud850\ude77", "\u5a88", "\ud850\udf65", "\u9362", "\ud850\udec1", "\u712c", "\ud851\udc5a", "\ud852\ude27", "\ud852\ude22", "\ud862\udfe8", "\u720e", "\u9442", "\u7215", "\u9341", "\ud855\ude05", "\ud852\udd74", "\u68bd", "\u3e55", "\ud84c\udc44", "\u6f3d", "\ud852\udc23", "\ud862\udc2b", "\u48ed", "\ud862\udc04", "\ud843\udc3a", "\ud85a\ude2e", "\u7449", "\ud850\udde2", "\ud845\udee7", "\ud852\ude24", "\u36c5", "\ud852\uddb7", "\ud852\udd8d", "\ud852\uddfb", "\u7415", "\ud852\ude26", "\ud841\uddc3", "\u3ed7", "\ud84a\udcad", "\ud863\udeb2", "\u746c", "\u3730", "\u7474", "\u93f1", "\u4953", "\ud852\ude8c", "\ud850\udd5f", "\ud852\ude79", "\ud862\udf8f", "\u5b46", "\ud863\udc03", "\ud846\udc9e", "\ud846\udd88", "\ud863\uded9", "\ud846\ude4b", "\ud863\udeac", "\u9385", "\u756e", "\ud853\udf82", "\u3f04", "\ud853\udd13", "\u7651", "\u764f", "\ud858\udff5", "\u81ef", "\u37f8", "\ud85a\udd11", "\ud85a\udd0e", "\u76a1", "\ud85b\udf9f", "\ud854\udc9d", "\ud854\udd7d", "\ud847\ude1c", "\ud854\ude20", "\u7758", "\ud84c\udeac", "\ud862\udd64", "\ud862\udd68", "\ud845\udec1", "\ud844\udf76", "\ud852\ude12", "\u792e", "\ud855\udde0", "\ud85d\ude0c", "\ud862\udf2b", "\ud858\udc83", "\ud849\ude1c", "\ud856\udc57", "\ud85e\udf39", "\ud85c\udd26", "\u3ea8", "\ud864\udd0d", "\ud83d\ude1c", "\u093b", "\u094a", "\u094e", "\u094f", "\u09cc", "\u0bcc", "\u0c01", "\u0dd1", "\u0ddb", "\u0dde", "\u0f3f", "\u0f7f", "\u103b", "\u1056", "\u1057", "\u1062", "\u1063", "\u1064", "\u1067", "\u1068", "\u1069", "\u106a", "\u106b", "\u106c", "\u106d", "\u1083", "\u1084", "\u1087", "\u1088", "\u1089", "\u108a", "\u108b", "\u108c", "\u108f", "\u109a", "\u109b", "\u109c", "\u17be", "\u17bf", "\u1923", "\u1924", "\u1925", "\u1926", "\u1929", "\u192a", "\u1931", "\u1933", "\u1934", "\u1935", "\u1936", "\u1937", "\u1938", "\u1a19", "\u1a1a", "\u1a55", "\u1a57", "\u1a61", "\u1a63", "\u1a64", "\u1a6d", "\u1a6e", "\u1a6f", "\u1a70", "\u1a71", "\u1a72", "\u1b04", "\u1b35", "\u1b3b", "\u1b3d", "\u1b3e", "\u1b3f", "\u1b40", "\u1b41", "\u1b43", "\u1b44", "\u1b82", "\u1ba1", "\u1ba6", "\u1ba7", "\u1baa", "\u1be7", "\u1bea", "\u1beb", "\u1bec", "\u1bee", "\u1bf2", "\u1c24", "\u1c25", "\u1c26", "\u1c27", "\u1c28", "\u1c29", "\u1c2a", "\u1c2b", "\u1c34", "\u1c35", "\u1ce1", "\u1cf2", "\u1cf3", "\u1cf7", "\u302e", "\ua823", "\ua824", "\ua881", "\ua8b4", "\ua8b5", "\ua8b6", "\ua8b7", "\ua8b8", "\ua8b9", "\ua8ba", "\ua8bb", "\ua8bc", "\ua8bd", "\ua8be", "\ua8bf", "\ua8c0", "\ua8c1", "\ua8c2", "\ua8c3", "\ua952", "\ua983", "\ua9b4", "\ua9b5", "\ua9ba", "\ua9bb", "\ua9bd", "\ua9be", "\ua9bf", "\uaa2f", "\uaa30", "\uaa33", "\uaa34", "\uaa7b", "\uaa7d", "\uaaeb", "\uaaee", "\uaaf5", "\uabe3", "\uabe4", "\uabe6", "\uabe7", "\uabe9", "\u1082", "\u112c", "\u1182", "\u11b3", "\u11b4", "\u11b5", "\u11bf", "\u11c0", "\u122c", "\u122d", "\u122e", "\u1232", "\u1233", "\u12e0", "\u12e1", "\u12e2", "\u1302", "\u1303", "\u133e", "\u133f", "\u1341", "\u1342", "\u1343", "\u1344", "\u1347", "\u1348", "\u134c", "\u1357", "\u1362", "\u1363", "\u1435", "\u1436", "\u1437", "\u1440", "\u1441", "\u1445", "\u14b0", "\u14b1", "\u14b2", "\u14b9", "\u14bb", "\u14bc", "\u14bd", "\u14be", "\u14c1", "\u15af", "\u15b0", "\u15b1", "\u15b8", "\u15b9", "\u15ba", "\u15bb", "\u15be", "\u1630", "\u1631", "\u1632", "\u163b", "\u163c", "\u163e", "\u16ac", "\u16ae", "\u16af", "\u16b6", "\u1721", "\u1726", "\u1a07", "\u1a08", "\u1a39", "\u1a58", "\u1a97", "\u1c2f", "\u1c3e", "\u1ca9", "\u1cb1", "\u1cb4", "\ud165", "\ud166", "\ud16f", "\ud170", "\ud171", "\ud172", "\u0340", "\u0341", "\u0343", "\u0344", "\u034f", "\u0484", "\u0485", "\u0486", "\u0592", "\u0593", "\u0594", "\u0595", "\u0596", "\u0597", "\u0598", "\u0599", "\u059a", "\u059b", "\u059c", "\u059d", "\u059e", "\u059f", "\u05a0", "\u05a1", "\u05a2", "\u05a3", "\u05a4", "\u05a5", "\u05a6", "\u05a7", "\u05a8", "\u05a9", "\u05aa", "\u05ab", "\u05ac", "\u05ad", "\u05ae", "\u05af", "\u0611", "\u0612", "\u0613", "\u0614", "\u0615", "\u0616", "\u0617", "\u0618", "\u0619", "\u0653", "\u0655", "\u0656", "\u0657", "\u0658", "\u0659", "\u065a", "\u065b", "\u065c", "\u065d", "\u065e", "\u065f", "\u0670", "\u06d6", "\u06d7", "\u06d8", "\u06d9", "\u06da", "\u06db", "\u06e0", "\u06e1", "\u06e2", "\u06e3", "\u06e4", "\u06e7", "\u06eb", "\u06ec", "\u06ed", "\u0711", "\u0730", "\u0731", "\u0732", "\u0733", "\u0734", "\u0735", "\u0736", "\u0737", "\u0738", "\u0739", "\u073a", "\u073b", "\u073c", "\u073d", "\u073e", "\u073f", "\u0740", "\u0741", "\u0742", "\u0743", "\u0744", "\u0745", "\u0746", "\u0747", "\u0748", "\u0749", "\u07eb", "\u07ec", "\u07ed", "\u07ee", "\u07ef", "\u07f0", "\u07f1", "\u07f2", "\u07f3", "\u0816", "\u0817", "\u0818", "\u0819", "\u081b", "\u081c", "\u081d", "\u081e", "\u081f", "\u0820", "\u0821", "\u0822", "\u0823", "\u0825", "\u0826", "\u0827", "\u0829", "\u082a", "\u082b", "\u082c", "\u0859", "\u085a", "\u08d4", "\u08d5", "\u08d6", "\u08d7", "\u08d8", "\u08d9", "\u08da", "\u08db", "\u08dc", "\u08dd", "\u08de", "\u08df", "\u08e0", "\u08e1", "\u08e3", "\u08e5", "\u08e6", "\u08e7", "\u08e8", "\u08e9", "\u08ea", "\u08eb", "\u08ec", "\u08ed", "\u08ee", "\u08ef", "\u08f0", "\u08f1", "\u08f2", "\u08f3", "\u08f4", "\u08f5", "\u08f6", "\u08f7", "\u08f8", "\u08f9", "\u08fa", "\u08fb", "\u08fc", "\u08fd", "\u08fe", "\u08ff", "\u0900", "\u093a", "\u0944", "\u0946", "\u0951", "\u0952", "\u0953", "\u0954", "\u0955", "\u0956", "\u0957", "\u0962", "\u09e2", "\u0ac4", "\u0ae2", "\u0afa", "\u0afb", "\u0afc", "\u0afd", "\u0afe", "\u0aff", "\u0b62", "\u0c62", "\u0ce2", "\u0d00", "\u0d3b", "\u0d3c", "\u0d62", "\u0f73", "\u0f75", "\u0f76", "\u0f77", "\u0f78", "\u0f79", "\u0f7b", "\u0f7d", "\u0f7e", "\u0f80", "\u0f81", "\u0f82", "\u0f83", "\u0f87", "\u0f8d", "\u0f8e", "\u0f8f", "\u0f91", "\u0f93", "\u0f95", "\u0f96", "\u0f9a", "\u0f9b", "\u0f9c", "\u0f9d", "\u0f9e", "\u0fa0", "\u0fa2", "\u0fa5", "\u0fa7", "\u0fa8", "\u0faa", "\u0fac", "\u0fad", "\u0fae", "\u0faf", "\u0fb0", "\u0fb4", "\u0fb5", "\u0fb6", "\u0fb8", "\u0fb9", "\u0fba", "\u0fbb", "\u1033", "\u1034", "\u1035", "\u1036", "\u1058", "\u1059", "\u105e", "\u105f", "\u1060", "\u1071", "\u1072", "\u1073", "\u1074", "\u1085", "\u1086", "\u108d", "\u135e", "\u1712", "\u1713", "\u1732", "\u1733", "\u1752", "\u17b4", "\u17b5", "\u17ba", "\u17ca", "\u17cb", "\u17cc", "\u17ce", "\u17cf", "\u17d1", "\u180c", "\u1885", "\u1886", "\u18a9", "\u1921", "\u1922", "\u1927", "\u1928", "\u1932", "\u1939", "\u193a", "\u1a17", "\u1a18", "\u1a56", "\u1a59", "\u1a5a", "\u1a5b", "\u1a5c", "\u1a5d", "\u1a62", "\u1a65", "\u1a66", "\u1a67", "\u1a68", "\u1a69", "\u1a6a", "\u1a6b", "\u1a6c", "\u1a73", "\u1a74", "\u1a75", "\u1a76", "\u1a77", "\u1a78", "\u1a79", "\u1a7a", "\u1a7b", "\u1ab1", "\u1ab2", "\u1ab3", "\u1ab4", "\u1ab5", "\u1ab6", "\u1ab7", "\u1ab8", "\u1ab9", "\u1aba", "\u1abb", "\u1abc", "\u1b01", "\u1b02", "\u1b03", "\u1b34", "\u1b36", "\u1b37", "\u1b38", "\u1b39", "\u1b3a", "\u1b3c", "\u1b42", "\u1b6c", "\u1b6d", "\u1b6e", "\u1b6f", "\u1b70", "\u1b71", "\u1b72", "\u1b81", "\u1ba2", "\u1ba3", "\u1ba4", "\u1ba5", "\u1ba8", "\u1ba9", "\u1bab", "\u1bac", "\u1bad", "\u1be6", "\u1be8", "\u1be9", "\u1bed", "\u1bef", "\u1bf0", "\u1bf1", "\u1c2c", "\u1c2d", "\u1c2e", "\u1c30", "\u1c31", "\u1c32", "\u1c33", "\u1c36", "\u1cd1", "\u1cd5", "\u1cd6", "\u1cd7", "\u1cd8", "\u1cd9", "\u1cda", "\u1cdb", "\u1cdc", "\u1cdd", "\u1cde", "\u1cdf", "\u1ce0", "\u1ce2", "\u1ce3", "\u1ce4", "\u1ce5", "\u1ce6", "\u1ce7", "\u1ce8", "\u1ced", "\u1cf4", "\u1dc0", "\u1dc1", "\u1dc2", "\u1dc3", "\u1dc4", "\u1dc5", "\u1dc6", "\u1dc7", "\u1dc8", "\u1dc9", "\u1dca", "\u1dcb", "\u1dcc", "\u1dcd", "\u1dce", "\u1dcf", "\u1dd0", "\u1dd1", "\u1dd2", "\u1dd3", "\u1dd4", "\u1dd5", "\u1dd6", "\u1dd7", "\u1dd8", "\u1dd9", "\u1dda", "\u1ddb", "\u1ddc", "\u1ddd", "\u1dde", "\u1ddf", "\u1de0", "\u1de1", "\u1de2", "\u1de3", "\u1de4", "\u1de5", "\u1de6", "\u1de7", "\u1de8", "\u1de9", "\u1dea", "\u1deb", "\u1dec", "\u1ded", "\u1dee", "\u1def", "\u1df0", "\u1df1", "\u1df2", "\u1df3", "\u1df4", "\u1df6", "\u1df7", "\u1df8", "\u1df9", "\u1dfb", "\u1dfd", "\u1dfe", "\u1dff", "\u20d1", "\u20d3", "\u20d4", "\u20d5", "\u20d6", "\u20d7", "\u20d8", "\u20d9", "\u20da", "\u20e6", "\u20e7", "\u20e8", "\u20e9", "\u20ea", "\u20eb", "\u20ec", "\u20ed", "\u20ee", "\u20ef", "\u2cef", "\u2cf0", "\u2cf1", "\u2de1", "\u2de2", "\u2de3", "\u2de4", "\u2de5", "\u2de6", "\u2de7", "\u2de8", "\u2de9", "\u2dea", "\u2deb", "\u2dec", "\u2ded", "\u2dee", "\u2def", "\u2df0", "\u2df1", "\u2df2", "\u2df3", "\u2df4", "\u2df5", "\u2df6", "\u2df7", "\u2df8", "\u2df9", "\u2dfa", "\u2dfb", "\u2dfc", "\u2dfd", "\u2dfe", "\u302a", "\u302b", "\u302c", "\u302d", "\ua675", "\ua676", "\ua677", "\ua678", "\ua679", "\ua67a", "\ua67b", "\ua67c", "\ua69e", "\ua6f0", "\ua802", "\ua806", "\ua80b", "\ua825", "\ua826", "\ua8c5", "\ua8e1", "\ua8e2", "\ua8e3", "\ua8e4", "\ua8e5", "\ua8e6", "\ua8e7", "\ua8e8", "\ua8e9", "\ua8ea", "\ua8eb", "\ua8ec", "\ua8ed", "\ua8ee", "\ua8ef", "\ua8f0", "\ua8f1", "\ua926", "\ua927", "\ua928", "\ua929", "\ua92a", "\ua92b", "\ua92c", "\ua947", "\ua948", "\ua949", "\ua94a", "\ua94b", "\ua94c", "\ua94d", "\ua94e", "\ua94f", "\ua950", "\ua951", "\ua981", "\ua982", "\ua9b3", "\ua9b6", "\ua9b7", "\ua9b8", "\ua9b9", "\ua9bc", "\ua9e5", "\uaa29", "\uaa2a", "\uaa2b", "\uaa2c", "\uaa2d", "\uaa2e", "\uaa31", "\uaa32", "\uaa35", "\uaa43", "\uaa4c", "\uaa7c", "\uaab0", "\uaab2", "\uaab3", "\uaab4", "\uaab7", "\uaab8", "\uaabe", "\uaabf", "\uaac1", "\uaaec", "\uaaed", "\uabe5", "\uabe8", "\ufb1e", "\ufe01", "\ufe02", "\ufe03", "\ufe04", "\ufe05", "\ufe06", "\ufe07", "\ufe08", "\ufe09", "\ufe0a", "\ufe0b", "\ufe0c", "\ufe0d", "\ufe0e", "\ufe21", "\ufe22", "\ufe23", "\ufe24", "\ufe25", "\ufe26", "\ufe27", "\ufe28", "\ufe29", "\ufe2a", "\ufe2b", "\ufe2c", "\ufe2e", "\ufe2f", "\u0378", "\u0379", "\u0a0c", "\u0a0d", "\u0a0e", "\u0a3a", "\u0ae5", "\u107f", "\u1080", "\u1100", "\u1101", "\u1102", "\u1127", "\u1128", "\u1129", "\u112a", "\u112b", "\u112d", "\u112e", "\u112f", "\u1130", "\u1131", "\u1132", "\u1133", "\u1134", "\u1173", "\u1180", "\u1181", "\u11b6", "\u11b7", "\u11b8", "\u11b9", "\u11ba", "\u11bb", "\u11bc", "\u11bd", "\u11be", "\u11ca", "\u11cb", "\u11cc", "\u122f", "\u1231", "\u1234", "\u1237", "\u123e", "\u12df", "\u12e3", "\u12e4", "\u12e5", "\u12e6", "\u12e7", "\u12e9", "\u12ea", "\u1300", "\u1301", "\u133c", "\u1340", "\u1367", "\u1368", "\u1369", "\u136a", "\u136b", "\u136c", "\u1370", "\u1371", "\u1372", "\u1373", "\u1374", "\u1438", "\u1439", "\u143a", "\u143b", "\u143c", "\u143d", "\u143e", "\u143f", "\u1442", "\u1443", "\u1444", "\u1446", "\u14b3", "\u14b4", "\u14b5", "\u14b6", "\u14b7", "\u14b8", "\u14ba", "\u14bf", "\u14c0", "\u14c2", "\u14c3", "\u15b2", "\u15b3", "\u15b4", "\u15b5", "\u15bc", "\u15bd", "\u15bf", "\u15c0", "\u15dc", "\u15dd", "\u1633", "\u1634", "\u1635", "\u1636", "\u1637", "\u1638", "\u1639", "\u163a", "\u163d", "\u163f", "\u1640", "\u16ab", "\u16ad", "\u16b0", "\u16b1", "\u16b2", "\u16b3", "\u16b4", "\u16b5", "\u16b7", "\u171d", "\u171e", "\u171f", "\u1722", "\u1723", "\u1724", "\u1725", "\u1727", "\u1728", "\u1729", "\u172a", "\u172b", "\u1a01", "\u1a02", "\u1a03", "\u1a04", "\u1a05", "\u1a06", "\u1a09", "\u1a0a", "\u1a33", "\u1a34", "\u1a35", "\u1a36", "\u1a37", "\u1a38", "\u1a3b", "\u1a3c", "\u1a3d", "\u1a3e", "\u1a47", "\u1a51", "\u1a52", "\u1a53", "\u1a8a", "\u1a8b", "\u1a8c", "\u1a8d", "\u1a8e", "\u1a8f", "\u1a91", "\u1a92", "\u1a93", "\u1a94", "\u1a95", "\u1a96", "\u1a98", "\u1c38", "\u1c39", "\u1c3a", "\u1c3b", "\u1c3c", "\u1c3d", "\u1c3f", "\u1c92", "\u1c93", "\u1c94", "\u1c95", "\u1c96", "\u1c97", "\u1c98", "\u1c99", "\u1c9a", "\u1c9b", "\u1c9c", "\u1c9d", "\u1c9e", "\u1c9f", "\u1ca0", "\u1ca1", "\u1ca2", "\u1ca3", "\u1ca4", "\u1ca5", "\u1ca6", "\u1ca7", "\u1caa", "\u1cab", "\u1cac", "\u1cad", "\u1cae", "\u1caf", "\u1cb0", "\u1cb2", "\u1cb3", "\u1cb5", "\u1cb6", "\u1d31", "\u1d32", "\u1d33", "\u1d34", "\u1d35", "\u1d36", "\u1d3a", "\u1d3c", "\u1d3d", "\u1d3f", "\u1d40", "\u1d41", "\u1d42", "\u1d43", "\u1d44", "\u1d45", "\u1d47", "\u6af4", "\ubc9d", "\ubc9e", "\ud167", "\ud17b", "\ud17e", "\ud17f", "\ud180", "\ud181", "\ud182", "\ud1aa", "\ud1ab", "\ud1ac", "\ud1ad", "\ud243", "\ud244", "\ue004", "\ue00a", "\ue00b", "\ue00c", "\ue00d", "\ue00e", "\ue00f", "\ue01b", "\ue01c", "\ue01d", "\ue01e", "\ue01f", "\ue02a", "\ue8d0", "\ue8d1", "\ue8d2", "\ue8d3", "\ue8d4", "\ue8d5", "\ue8d6", "\ue944", "\ue945", "\ue946", "\ue947", "\ue948", "\ue949", "\ue94a", "\u01bb", "\u01c0", "\u01c1", "\u01c2", "\u01c3", "\u0294", "\u063b", "\u063c", "\u063d", "\u063e", "\u063f", "\u0672", "\u0673", "\u0674", "\u0675", "\u0676", "\u0677", "\u0678", "\u067a", "\u067b", "\u067f", "\u0682", "\u0683", "\u068b", "\u068c", "\u068d", "\u068e", "\u0690", "\u0692", "\u0694", "\u0697", "\u0699", "\u069b", "\u069c", "\u069d", "\u069e", "\u069f", "\u06a0", "\u06a1", "\u06a2", "\u06a3", "\u06a4", "\u06a5", "\u06a6", "\u06a7", "\u06a8", "\u06ac", "\u06ae", "\u06b0", "\u06b2", "\u06b4", "\u06b6", "\u06b7", "\u06b8", "\u06b9", "\u06bd", "\u06bf", "\u06c0", "\u06c2", "\u06c3", "\u06c4", "\u06c5", "\u06c9", "\u06ca", "\u06cf", "\u06d1", "\u06fb", "\u0713", "\u0714", "\u0715", "\u0716", "\u0717", "\u0718", "\u0719", "\u071a", "\u071b", "\u071c", "\u071d", "\u071e", "\u071f", "\u0720", "\u0721", "\u0722", "\u0723", "\u0724", "\u0725", "\u0726", "\u0727", "\u0728", "\u0729", "\u072a", "\u072b", "\u072c", "\u072d", "\u072e", "\u074e", "\u074f", "\u0750", "\u0751", "\u0752", "\u0753", "\u0754", "\u0755", "\u0756", "\u0757", "\u0758", "\u0759", "\u075a", "\u075b", "\u075c", "\u075d", "\u075e", "\u075f", "\u0760", "\u0761", "\u0762", "\u0763", "\u0764", "\u0765", "\u0766", "\u0767", "\u0768", "\u0769", "\u076a", "\u076b", "\u076c", "\u076d", "\u076e", "\u076f", "\u0770", "\u0771", "\u0772", "\u0773", "\u0774", "\u0775", "\u0776", "\u0777", "\u0778", "\u0779", "\u077a", "\u077b", "\u077c", "\u077d", "\u077e", "\u077f", "\u0781", "\u078f", "\u0792", "\u0798", "\u0799", "\u079a", "\u079b", "\u079c", "\u079d", "\u079e", "\u079f", "\u07a0", "\u07a1", "\u07a2", "\u07a3", "\u07a4", "\u07cb", "\u07cc", "\u07cd", "\u07ce", "\u07cf", "\u07d0", "\u07d1", "\u07d2", "\u07d3", "\u07d4", "\u07d5", "\u07d6", "\u07d7", "\u07d8", "\u07d9", "\u07da", "\u07db", "\u07dc", "\u07dd", "\u07de", "\u07df", "\u07e0", "\u07e1", "\u07e2", "\u07e3", "\u07e4", "\u07e5", "\u07e6", "\u07e7", "\u07e8", "\u07e9", "\u0801", "\u0802", "\u0803", "\u0804", "\u0805", "\u0806", "\u0807", "\u0808", "\u0809", "\u080a", "\u080b", "\u080c", "\u080d", "\u080e", "\u080f", "\u0810", "\u0811", "\u0812", "\u0813", "\u0814", "\u0841", "\u0842", "\u0843", "\u0844", "\u0845", "\u0846", "\u0847", "\u0848", "\u0849", "\u084a", "\u084b", "\u084c", "\u084d", "\u084e", "\u084f", "\u0850", "\u0851", "\u0852", "\u0853", "\u0854", "\u0855", "\u0856", "\u0857", "\u0860", "\u0861", "\u0862", "\u0863", "\u0864", "\u0865", "\u0866", "\u0867", "\u0868", "\u0869", "\u086a", "\u08a1", "\u08a2", "\u08a3", "\u08a4", "\u08a5", "\u08a6", "\u08a7", "\u08a8", "\u08a9", "\u08aa", "\u08ab", "\u08ac", "\u08ad", "\u08ae", "\u08af", "\u08b0", "\u08b1", "\u08b3", "\u08b4", "\u08b6", "\u08b7", "\u08b8", "\u08b9", "\u08ba", "\u08bb", "\u08bc", "\u08bd", "\u090b", "\u090c", "\u090d", "\u090e", "\u0912", "\u0929", "\u0931", "\u0934", "\u0959", "\u095a", "\u095b", "\u095c", "\u095d", "\u095e", "\u095f", "\u0960", "\u0972", "\u0973", "\u0974", "\u0975", "\u0976", "\u0977", "\u0978", "\u0979", "\u097a", "\u097b", "\u097c", "\u097d", "\u097e", "\u097f", "\u0988", "\u098b", "\u0994", "\u099d", "\u09a2", "\u09e0", "\u09fc", "\u0a14", "\u0a19", "\u0a1e", "\u0a5a", "\u0a73", "\u0a8a", "\u0a8b", "\u0a8c", "\u0a90", "\u0a94", "\u0a99", "\u0af9", "\u0b08", "\u0b0a", "\u0b0b", "\u0b14", "\u0b1d", "\u0b60", "\u0b94", "\u0bb6", "\u0bb7", "\u0c0b", "\u0c14", "\u0c18", "\u0c19", "\u0c1d", "\u0c1e", "\u0c22", "\u0c31", "\u0c34", "\u0c5a", "\u0c80", "\u0c8b", "\u0c94", "\u0c99", "\u0c9d", "\u0ca2", "\u0cb1", "\u0d0a", "\u0d0b", "\u0d18", "\u0d1b", "\u0d1d", "\u0d20", "\u0d22", "\u0d29", "\u0d54", "\u0d55", "\u0d56", "\u0d5f", "\u0d88", "\u0d8c", "\u0d8d", "\u0d8e", "\u0d8f", "\u0d90", "\u0d91", "\u0d92", "\u0d93", "\u0d95", "\u0d9d", "\u0d9e", "\u0da0", "\u0da1", "\u0da3", "\u0da4", "\u0da5", "\u0da6", "\u0da8", "\u0daa", "\u0dac", "\u0dae", "\u0db5", "\u0db9", "\u0ede", "\u0f43", "\u0f4b", "\u0f4d", "\u0f4e", "\u0f52", "\u0f57", "\u0f5c", "\u0f65", "\u0f69", "\u0f6a", "\u0f6b", "\u0f89", "\u0f8a", "\u0f8b", "\u1003", "\u1006", "\u1008", "\u1009", "\u100b", "\u100c", "\u100d", "\u100e", "\u100f", "\u1011", "\u1020", "\u1022", "\u1023", "\u1024", "\u1025", "\u1026", "\u1028", "\u1029", "\u1051", "\u1052", "\u1053", "\u1054", "\u105b", "\u105c", "\u106f", "\u1076", "\u1077", "\u1078", "\u1079", "\u107a", "\u107b", "\u107c", "\u107d", "\u107e", "\u10f7", "\u10f8", "\u10f9", "\u10fd", "\u10fe", "\u10ff", "\u1103", "\u1104", "\u1105", "\u1106", "\u1107", "\u1108", "\u1109", "\u110a", "\u110b", "\u110c", "\u110d", "\u110e", "\u110f", "\u1110", "\u1111", "\u1112", "\u1113", "\u1114", "\u1115", "\u1116", "\u1117", "\u1118", "\u1119", "\u111a", "\u111b", "\u111c", "\u111d", "\u111e", "\u111f", "\u1120", "\u1121", "\u1122", "\u1123", "\u1124", "\u1125", "\u1126", "\u1135", "\u1136", "\u1137", "\u1138", "\u1139", "\u113a", "\u113b", "\u113c", "\u113d", "\u113e", "\u113f", "\u1140", "\u1141", "\u1142", "\u1143", "\u1144", "\u1145", "\u1146", "\u1147", "\u1148", "\u1149", "\u114a", "\u114b", "\u114c", "\u114d", "\u114e", "\u114f", "\u1150", "\u1151", "\u1152", "\u1153", "\u1154", "\u1155", "\u1156", "\u1157", "\u1158", "\u1159", "\u115a", "\u115b", "\u115c", "\u115d", "\u115e", "\u115f", "\u1160", "\u1161", "\u1162", "\u1163", "\u1164", "\u1165", "\u1166", "\u1167", "\u1168", "\u1169", "\u116a", "\u116b", "\u116c", "\u116d", "\u116e", "\u116f", "\u1170", "\u1171", "\u1172", "\u1174", "\u1175", "\u1176", "\u1177", "\u1178", "\u1179", "\u117a", "\u117b", "\u117c", "\u117d", "\u117e", "\u117f", "\u1183", "\u1184", "\u1185", "\u1186", "\u1187", "\u1188", "\u1189", "\u118a", "\u118b", "\u118c", "\u118d", "\u118e", "\u118f", "\u1190", "\u1191", "\u1192", "\u1193", "\u1194", "\u1195", "\u1196", "\u1197", "\u1198", "\u1199", "\u119a", "\u119b", "\u119c", "\u119d", "\u119e", "\u119f", "\u11a0", "\u11a1", "\u11a2", "\u11a3", "\u11a4", "\u11a5", "\u11a6", "\u11a7", "\u11a8", "\u11a9", "\u11aa", "\u11ab", "\u11ac", "\u11ad", "\u11ae", "\u11af", "\u11b0", "\u11b1", "\u11b2", "\u11c1", "\u11c2", "\u11c3", "\u11c4", "\u11c5", "\u11c6", "\u11c7", "\u11c8", "\u11c9", "\u11cd", "\u11ce", "\u11cf", "\u11d0", "\u11d1", "\u11d2", "\u11d3", "\u11d4", "\u11d5", "\u11d6", "\u11d7", "\u11d8", "\u11d9", "\u11da", "\u11db", "\u11dc", "\u11dd", "\u11de", "\u11df", "\u11e0", "\u11e1", "\u11e2", "\u11e3", "\u11e4", "\u11e5", "\u11e6", "\u11e7", "\u11e8", "\u11e9", "\u11ea", "\u11eb", "\u11ec", "\u11ed", "\u11ee", "\u11ef", "\u11f0", "\u11f1", "\u11f2", "\u11f3", "\u11f4", "\u11f5", "\u11f6", "\u11f7", "\u11f8", "\u11f9", "\u11fa", "\u11fb", "\u11fc", "\u11fd", "\u11fe", "\u11ff", "\u1200", "\u1201", "\u1202", "\u1203", "\u1204", "\u1206", "\u1207", "\u1209", "\u120a", "\u120b", "\u120c", "\u120e", "\u1210", "\u1212", "\u1213", "\u1214", "\u1215", "\u1216", "\u1217", "\u1218", "\u1219", "\u121a", "\u121c", "\u121e", "\u121f", "\u1220", "\u1221", "\u1222", "\u1223", "\u1224", "\u1225", "\u1226", "\u1227", "\u1228", "\u1229", "\u122a", "\u1238", "\u1239", "\u123a", "\u123b", "\u123c", "\u123d", "\u123f", "\u1241", "\u1242", "\u1243", "\u1244", "\u1245", "\u1246", "\u1247", "\u124b", "\u124c", "\u1251", "\u1252", "\u1253", "\u1254", "\u1255", "\u125b", "\u125c", "\u1261", "\u1262", "\u1264", "\u1266", "\u1267", "\u1268", "\u1269", "\u126a", "\u126b", "\u126c", "\u126d", "\u126e", "\u126f", "\u1271", "\u1272", "\u1273", "\u1274", "\u1276", "\u1277", "\u1278", "\u1279", "\u127a", "\u127b", "\u127c", "\u127d", "\u127e", "\u127f", "\u1280", "\u1281", "\u1282", "\u1283", "\u1284", "\u1285", "\u1286", "\u1287", "\u128b", "\u128c", "\u1291", "\u1292", "\u1293", "\u1294", "\u1296", "\u1297", "\u1298", "\u1299", "\u129a", "\u129b", "\u129c", "\u129d", "\u129e", "\u129f", "\u12a1", "\u12a2", "\u12a3", "\u12a4", "\u12a6", "\u12a7", "\u12a9", "\u12aa", "\u12ab", "\u12ac", "\u12ad", "\u12ae", "\u12af", "\u12b3", "\u12b4", "\u12b9", "\u12ba", "\u12bb", "\u12bc", "\u12bd", "\u12c3", "\u12c4", "\u12c9", "\u12ca", "\u12cb", "\u12cc", "\u12cd", "\u12ce", "\u12cf", "\u12d0", "\u12d1", "\u12d2", "\u12d3", "\u12d4", "\u12d5", "\u12d9", "\u12da", "\u12db", "\u12dc", "\u12dd", "\u12de", "\u12eb", "\u12ec", "\u12ee", "\u12ef", "\u12f0", "\u12f1", "\u12f2", "\u12f4", "\u12f5", "\u12f6", "\u12f7", "\u12f8", "\u12f9", "\u12fa", "\u12fb", "\u12fc", "\u12fd", "\u12fe", "\u12ff", "\u1304", "\u1305", "\u1306", "\u1307", "\u1308", "\u1309", "\u130a", "\u130b", "\u130c", "\u130e", "\u130f", "\u1313", "\u1314", "\u1319", "\u131a", "\u131b", "\u131c", "\u131d", "\u131e", "\u131f", "\u1320", "\u1321", "\u1322", "\u1323", "\u1324", "\u1325", "\u1326", "\u1327", "\u1328", "\u1329", "\u132a", "\u132b", "\u132c", "\u132d", "\u132e", "\u132f", "\u1330", "\u1331", "\u1332", "\u1333", "\u1334", "\u1335", "\u1336", "\u1337", "\u1338", "\u1339", "\u133a", "\u133b", "\u1345", "\u1346", "\u1349", "\u134a", "\u134e", "\u134f", "\u1350", "\u1351", "\u1352", "\u1353", "\u1354", "\u1355", "\u1356", "\u1358", "\u1359", "\u1381", "\u1382", "\u1383", "\u1384", "\u1385", "\u1386", "\u1387", "\u1388", "\u1389", "\u138a", "\u138b", "\u138c", "\u138d", "\u138e", "\u1402", "\u1403", "\u1404", "\u1405", "\u1406", "\u1407", "\u1408", "\u1409", "\u140a", "\u140b", "\u140c", "\u140d", "\u140e", "\u140f", "\u1410", "\u1411", "\u1412", "\u1413", "\u1414", "\u1415", "\u1416", "\u1417", "\u1418", "\u1419", "\u141a", "\u141b", "\u141c", "\u141d", "\u141e", "\u141f", "\u1420", "\u1421", "\u1422", "\u1423", "\u1424", "\u1425", "\u1426", "\u1427", "\u1428", "\u1429", "\u142a", "\u142b", "\u142c", "\u142d", "\u142e", "\u142f", "\u1430", "\u1431", "\u1432", "\u1433", "\u1434", "\u1447", "\u1448", "\u1449", "\u144a", "\u144b", "\u144c", "\u144d", "\u144e", "\u144f", "\u1450", "\u1451", "\u1452", "\u1453", "\u1454", "\u1455", "\u1456", "\u1457", "\u1458", "\u1459", "\u145a", "\u145b", "\u145c", "\u145d", "\u145e", "\u145f", "\u1460", "\u1461", "\u1462", "\u1463", "\u1464", "\u1465", "\u1466", "\u1467", "\u1468", "\u1469", "\u146a", "\u146b", "\u146c", "\u146d", "\u146e", "\u146f", "\u1470", "\u1471", "\u1472", "\u1473", "\u1474", "\u1475", "\u1476", "\u1477", "\u1478", "\u1479", "\u147a", "\u147b", "\u147c", "\u147d", "\u147e", "\u147f", "\u1480", "\u1481", "\u1482", "\u1483", "\u1484", "\u1485", "\u1486", "\u1487", "\u1488", "\u1489", "\u148a", "\u148b", "\u148c", "\u148d", "\u148e", "\u148f", "\u1490", "\u1491", "\u1492", "\u1493", "\u1494", "\u1495", "\u1496", "\u1497", "\u1498", "\u1499", "\u149a", "\u149b", "\u149c", "\u149d", "\u149e", "\u149f", "\u14a0", "\u14a1", "\u14a2", "\u14a3", "\u14a4", "\u14a5", "\u14a6", "\u14a7", "\u14a8", "\u14a9", "\u14aa", "\u14ab", "\u14ac", "\u14ad", "\u14ae", "\u14af", "\u14c4", "\u14c5", "\u14c6", "\u14c7", "\u14c8", "\u14c9", "\u14ca", "\u14cb", "\u14cc", "\u14cd", "\u14ce", "\u14cf", "\u14d0", "\u14d1", "\u14d2", "\u14d3", "\u14d4", "\u14d5", "\u14d6", "\u14d7", "\u14d8", "\u14d9", "\u14da", "\u14db", "\u14dc", "\u14dd", "\u14de", "\u14df", "\u14e0", "\u14e1", "\u14e2", "\u14e3", "\u14e4", "\u14e5", "\u14e6", "\u14e7", "\u14e8", "\u14e9", "\u14ea", "\u14eb", "\u14ec", "\u14ed", "\u14ee", "\u14ef", "\u14f0", "\u14f1", "\u14f2", "\u14f3", "\u14f4", "\u14f5", "\u14f6", "\u14f7", "\u14f8", "\u14f9", "\u14fa", "\u14fb", "\u14fc", "\u14fd", "\u14fe", "\u14ff", "\u1500", "\u1501", "\u1502", "\u1503", "\u1504", "\u1505", "\u1506", "\u1507", "\u1508", "\u1509", "\u150a", "\u150b", "\u150c", "\u150d", "\u150e", "\u150f", "\u1510", "\u1511", "\u1512", "\u1513", "\u1514", "\u1515", "\u1516", "\u1517", "\u1518", "\u1519", "\u151a", "\u151b", "\u151c", "\u151d", "\u151e", "\u151f", "\u1520", "\u1521", "\u1522", "\u1523", "\u1524", "\u1525", "\u1526", "\u1527", "\u1528", "\u1529", "\u152a", "\u152b", "\u152c", "\u152d", "\u152e", "\u152f", "\u1530", "\u1531", "\u1532", "\u1533", "\u1534", "\u1535", "\u1536", "\u1537", "\u1538", "\u1539", "\u153a", "\u153b", "\u153c", "\u153d", "\u153e", "\u153f", "\u1540", "\u1541", "\u1542", "\u1543", "\u1544", "\u1545", "\u1546", "\u1547", "\u1548", "\u1549", "\u154a", "\u154b", "\u154c", "\u154d", "\u154e", "\u154f", "\u1550", "\u1551", "\u1552", "\u1553", "\u1554", "\u1555", "\u1556", "\u1557", "\u1558", "\u1559", "\u155a", "\u155b", "\u155c", "\u155d", "\u155e", "\u155f", "\u1560", "\u1561", "\u1562", "\u1563", "\u1564", "\u1565", "\u1566", "\u1567", "\u1568", "\u1569", "\u156a", "\u156b", "\u156c", "\u156d", "\u156e", "\u156f", "\u1570", "\u1571", "\u1572", "\u1573", "\u1574", "\u1575", "\u1576", "\u1577", "\u1578", "\u1579", "\u157a", "\u157b", "\u157c", "\u157d", "\u157e", "\u157f", "\u1580", "\u1581", "\u1582", "\u1583", "\u1584", "\u1585", "\u1586", "\u1587", "\u1588", "\u1589", "\u158a", "\u158b", "\u158c", "\u158d", "\u158e", "\u158f", "\u1590", "\u1591", "\u1592", "\u1593", "\u1594", "\u1595", "\u1596", "\u1597", "\u1598", "\u1599", "\u159a", "\u159b", "\u159c", "\u159d", "\u159e", "\u159f", "\u15a0", "\u15a1", "\u15a2", "\u15a3", "\u15a4", "\u15a5", "\u15a6", "\u15a7", "\u15a8", "\u15a9", "\u15aa", "\u15ab", "\u15ac", "\u15ad", "\u15ae", "\u15b6", "\u15b7", "\u15c1", "\u15c2", "\u15c3", "\u15c4", "\u15c5", "\u15c6", "\u15c7", "\u15c8", "\u15c9", "\u15ca", "\u15cb", "\u15cc", "\u15cd", "\u15ce", "\u15cf", "\u15d0", "\u15d1", "\u15d2", "\u15d3", "\u15d4", "\u15d5", "\u15d6", "\u15d7", "\u15d8", "\u15d9", "\u15da", "\u15db", "\u15de", "\u15df", "\u15e0", "\u15e1", "\u15e2", "\u15e3", "\u15e4", "\u15e5", "\u15e6", "\u15e7", "\u15e8", "\u15e9", "\u15ea", "\u15eb", "\u15ec", "\u15ed", "\u15ee", "\u15ef", "\u15f0", "\u15f1", "\u15f2", "\u15f3", "\u15f4", "\u15f5", "\u15f6", "\u15f7", "\u15f8", "\u15f9", "\u15fa", "\u15fb", "\u15fc", "\u15fd", "\u15fe", "\u15ff", "\u1600", "\u1601", "\u1602", "\u1603", "\u1604", "\u1605", "\u1606", "\u1607", "\u1608", "\u1609", "\u160a", "\u160b", "\u160c", "\u160d", "\u160e", "\u160f", "\u1610", "\u1611", "\u1612", "\u1613", "\u1614", "\u1615", "\u1616", "\u1617", "\u1618", "\u1619", "\u161a", "\u161b", "\u161c", "\u161d", "\u161e", "\u161f", "\u1620", "\u1621", "\u1622", "\u1623", "\u1624", "\u1625", "\u1626", "\u1627", "\u1628", "\u1629", "\u162a", "\u162b", "\u162c", "\u162d", "\u162e", "\u162f", "\u1641", "\u1642", "\u1643", "\u1644", "\u1645", "\u1646", "\u1647", "\u1648", "\u1649", "\u164a", "\u164b", "\u164c", "\u164d", "\u164e", "\u164f", "\u1650", "\u1651", "\u1652", "\u1653", "\u1654", "\u1655", "\u1656", "\u1657", "\u1658", "\u1659", "\u165a", "\u165b", "\u165c", "\u165d", "\u165e", "\u165f", "\u1660", "\u1661", "\u1662", "\u1663", "\u1664", "\u1665", "\u1666", "\u1667", "\u1668", "\u1669", "\u166a", "\u166b", "\u1670", "\u1671", "\u1672", "\u1673", "\u1674", "\u1675", "\u1676", "\u1677", "\u1678", "\u1679", "\u167a", "\u167b", "\u167c", "\u167d", "\u167e", "\u1682", "\u1683", "\u1684", "\u1685", "\u1686", "\u1687", "\u1688", "\u1689", "\u168a", "\u168b", "\u168c", "\u168d", "\u168e", "\u168f", "\u1690", "\u1691", "\u1692", "\u1693", "\u1694", "\u1695", "\u1696", "\u1697", "\u1698", "\u1699", "\u16a1", "\u16a2", "\u16a3", "\u16a4", "\u16a5", "\u16a6", "\u16a7", "\u16a8", "\u16a9", "\u16aa", "\u16b8", "\u16b9", "\u16ba", "\u16bb", "\u16bc", "\u16bd", "\u16be", "\u16bf", "\u16c0", "\u16c1", "\u16c2", "\u16c3", "\u16c4", "\u16c5", "\u16c6", "\u16c7", "\u16c8", "\u16c9", "\u16ca", "\u16cb", "\u16cc", "\u16cd", "\u16ce", "\u16cf", "\u16d0", "\u16d1", "\u16d2", "\u16d3", "\u16d4", "\u16d5", "\u16d6", "\u16d7", "\u16d8", "\u16d9", "\u16da", "\u16db", "\u16dc", "\u16dd", "\u16de", "\u16df", "\u16e0", "\u16e1", "\u16e2", "\u16e3", "\u16e4", "\u16e5", "\u16e6", "\u16e7", "\u16e8", "\u16e9", "\u16f1", "\u16f2", "\u16f3", "\u16f4", "\u16f5", "\u16f6", "\u16f7", "\u1701", "\u1702", "\u1703", "\u1704", "\u1705", "\u1706", "\u1707", "\u1708", "\u1709", "\u170a", "\u170b", "\u170f", "\u1710", "\u172c", "\u172d", "\u172e", "\u172f", "\u1730", "\u1741", "\u1742", "\u1743", "\u1744", "\u1745", "\u1746", "\u1747", "\u1748", "\u1749", "\u174a", "\u174b", "\u174c", "\u174d", "\u174e", "\u174f", "\u1750", "\u1761", "\u1762", "\u1763", "\u1764", "\u1765", "\u1766", "\u1767", "\u1768", "\u1769", "\u176a", "\u176b", "\u176f", "\u1783", "\u1787", "\u1788", "\u178b", "\u178c", "\u178d", "\u178e", "\u1795", "\u179d", "\u179e", "\u17a1", "\u17a3", "\u17a4", "\u17a5", "\u17a6", "\u17a8", "\u17a9", "\u17aa", "\u17ab", "\u17ac", "\u17ad", "\u17ae", "\u17af", "\u17b0", "\u17b1", "\u17b2", "\u1821", "\u1822", "\u1823", "\u1824", "\u1825", "\u1826", "\u1827", "\u1828", "\u1829", "\u182a", "\u182b", "\u182c", "\u182d", "\u182e", "\u182f", "\u1830", "\u1831", "\u1832", "\u1833", "\u1834", "\u1835", "\u1836", "\u1837", "\u1838", "\u1839", "\u183a", "\u183b", "\u183c", "\u183d", "\u183e", "\u183f", "\u1840", "\u1841", "\u1842", "\u1844", "\u1845", "\u1846", "\u1847", "\u1848", "\u1849", "\u184a", "\u184b", "\u184c", "\u184d", "\u184e", "\u184f", "\u1850", "\u1851", "\u1852", "\u1853", "\u1854", "\u1855", "\u1856", "\u1857", "\u1858", "\u1859", "\u185a", "\u185b", "\u185c", "\u185d", "\u185e", "\u185f", "\u1860", "\u1861", "\u1862", "\u1863", "\u1864", "\u1865", "\u1866", "\u1867", "\u1868", "\u1869", "\u186a", "\u186b", "\u186c", "\u186d", "\u186e", "\u186f", "\u1870", "\u1871", "\u1872", "\u1873", "\u1874", "\u1875", "\u1876", "\u1881", "\u1882", "\u1883", "\u1884", "\u1887", "\u1888", "\u1889", "\u188a", "\u188b", "\u188c", "\u188d", "\u188e", "\u188f", "\u1890", "\u1891", "\u1892", "\u1893", "\u1894", "\u1895", "\u1896", "\u1897", "\u1898", "\u1899", "\u189a", "\u189b", "\u189c", "\u189d", "\u189e", "\u189f", "\u18a0", "\u18a1", "\u18a2", "\u18a3", "\u18a4", "\u18a5", "\u18a6", "\u18a7", "\u18b1", "\u18b2", "\u18b3", "\u18b4", "\u18b5", "\u18b6", "\u18b7", "\u18b8", "\u18b9", "\u18ba", "\u18bb", "\u18bc", "\u18bd", "\u18be", "\u18bf", "\u18c0", "\u18c1", "\u18c2", "\u18c3", "\u18c4", "\u18c5", "\u18c6", "\u18c7", "\u18c8", "\u18c9", "\u18ca", "\u18cb", "\u18cc", "\u18cd", "\u18ce", "\u18cf", "\u18d0", "\u18d1", "\u18d2", "\u18d3", "\u18d4", "\u18d5", "\u18d6", "\u18d7", "\u18d8", "\u18d9", "\u18da", "\u18db", "\u18dc", "\u18dd", "\u18de", "\u18df", "\u18e0", "\u18e1", "\u18e2", "\u18e3", "\u18e4", "\u18e5", "\u18e6", "\u18e7", "\u18e8", "\u18e9", "\u18ea", "\u18eb", "\u18ec", "\u18ed", "\u18ee", "\u18ef", "\u18f0", "\u18f1", "\u18f2", "\u18f3", "\u18f4", "\u1901", "\u1902", "\u1903", "\u1904", "\u1905", "\u1906", "\u1907", "\u1908", "\u1909", "\u190a", "\u190b", "\u190c", "\u190d", "\u190e", "\u190f", "\u1910", "\u1911", "\u1912", "\u1913", "\u1914", "\u1915", "\u1916", "\u1917", "\u1918", "\u1919", "\u191a", "\u191b", "\u191c", "\u191d", "\u1951", "\u1952", "\u1953", "\u1954", "\u1955", "\u1956", "\u1957", "\u1958", "\u1959", "\u195a", "\u195b", "\u195c", "\u195d", "\u195e", "\u195f", "\u1960", "\u1961", "\u1962", "\u1963", "\u1964", "\u1965", "\u1966", "\u1967", "\u1968", "\u1969", "\u196a", "\u196b", "\u196c", "\u1971", "\u1972", "\u1973", "\u1981", "\u1982", "\u1983", "\u1984", "\u1985", "\u1986", "\u1987", "\u1988", "\u1989", "\u198a", "\u198b", "\u198c", "\u198d", "\u198e", "\u198f", "\u1990", "\u1991", "\u1992", "\u1993", "\u1994", "\u1995", "\u1996", "\u1997", "\u1998", "\u1999", "\u199a", "\u199b", "\u199c", "\u199d", "\u199e", "\u199f", "\u19a0", "\u19a1", "\u19a2", "\u19a3", "\u19a4", "\u19a5", "\u19a6", "\u19a7", "\u19a8", "\u19a9", "\u19aa", "\u19b1", "\u19b2", "\u19b3", "\u19b4", "\u19b5", "\u19b6", "\u19b7", "\u19b8", "\u19b9", "\u19ba", "\u19bb", "\u19bc", "\u19bd", "\u19be", "\u19bf", "\u19c0", "\u19c2", "\u19c3", "\u19c4", "\u19c5", "\u19c6", "\u19c8", "\u1a0b", "\u1a0c", "\u1a0d", "\u1a0e", "\u1a0f", "\u1a10", "\u1a11", "\u1a12", "\u1a13", "\u1a14", "\u1a15", "\u1a21", "\u1a22", "\u1a23", "\u1a24", "\u1a25", "\u1a26", "\u1a27", "\u1a28", "\u1a29", "\u1a2a", "\u1a2b", "\u1a2c", "\u1a2d", "\u1a2e", "\u1a2f", "\u1a30", "\u1a31", "\u1a32", "\u1a3a", "\u1a3f", "\u1a40", "\u1a41", "\u1a42", "\u1a43", "\u1a44", "\u1a45", "\u1a46", "\u1a48", "\u1a49", "\u1a4a", "\u1a4b", "\u1a4c", "\u1a4d", "\u1a4e", "\u1a4f", "\u1a50", "\u1b06", "\u1b07", "\u1b08", "\u1b09", "\u1b0a", "\u1b0b", "\u1b0c", "\u1b0d", "\u1b0e", "\u1b0f", "\u1b10", "\u1b11", "\u1b12", "\u1b13", "\u1b14", "\u1b15", "\u1b16", "\u1b17", "\u1b18", "\u1b19", "\u1b1a", "\u1b1b", "\u1b1c", "\u1b1d", "\u1b1e", "\u1b1f", "\u1b20", "\u1b21", "\u1b22", "\u1b23", "\u1b24", "\u1b25", "\u1b26", "\u1b27", "\u1b28", "\u1b29", "\u1b2a", "\u1b2b", "\u1b2c", "\u1b2d", "\u1b2e", "\u1b2f", "\u1b30", "\u1b31", "\u1b32", "\u1b46", "\u1b47", "\u1b48", "\u1b49", "\u1b4a", "\u1b84", "\u1b85", "\u1b86", "\u1b87", "\u1b88", "\u1b89", "\u1b8a", "\u1b8b", "\u1b8c", "\u1b8d", "\u1b8e", "\u1b8f", "\u1b90", "\u1b91", "\u1b92", "\u1b93", "\u1b94", "\u1b95", "\u1b96", "\u1b97", "\u1b98", "\u1b99", "\u1b9a", "\u1b9b", "\u1b9c", "\u1b9d", "\u1b9e", "\u1b9f", "\u1bbb", "\u1bbc", "\u1bbd", "\u1bbe", "\u1bbf", "\u1bc0", "\u1bc1", "\u1bc2", "\u1bc3", "\u1bc4", "\u1bc5", "\u1bc6", "\u1bc7", "\u1bc8", "\u1bc9", "\u1bca", "\u1bcb", "\u1bcc", "\u1bcd", "\u1bce", "\u1bcf", "\u1bd0", "\u1bd1", "\u1bd2", "\u1bd3", "\u1bd4", "\u1bd5", "\u1bd6", "\u1bd7", "\u1bd8", "\u1bd9", "\u1bda", "\u1bdb", "\u1bdc", "\u1bdd", "\u1bde", "\u1bdf", "\u1be0", "\u1be1", "\u1be2", "\u1be3", "\u1be4", "\u1c01", "\u1c02", "\u1c03", "\u1c04", "\u1c05", "\u1c06", "\u1c07", "\u1c08", "\u1c09", "\u1c0a", "\u1c0b", "\u1c0c", "\u1c0d", "\u1c0e", "\u1c0f", "\u1c10", "\u1c11", "\u1c12", "\u1c13", "\u1c14", "\u1c15", "\u1c16", "\u1c17", "\u1c18", "\u1c19", "\u1c1a", "\u1c1b", "\u1c1c", "\u1c1d", "\u1c1e", "\u1c1f", "\u1c20", "\u1c21", "\u1c22", "\u1c4e", "\u1c5b", "\u1c5c", "\u1c5d", "\u1c5e", "\u1c5f", "\u1c60", "\u1c61", "\u1c62", "\u1c63", "\u1c64", "\u1c65", "\u1c66", "\u1c67", "\u1c68", "\u1c69", "\u1c6a", "\u1c6b", "\u1c6c", "\u1c6d", "\u1c6e", "\u1c6f", "\u1c70", "\u1c71", "\u1c72", "\u1c73", "\u1c74", "\u1c75", "\u1c76", "\u1c77", "\u1cea", "\u1ceb", "\u1cef", "\u1cf0", "\u2d32", "\u2d35", "\u2d36", "\u2d38", "\u2d3b", "\u2d3c", "\u2d3e", "\u2d3f", "\u2d40", "\u2d41", "\u2d42", "\u2d43", "\u2d46", "\u2d47", "\u2d48", "\u2d4b", "\u2d4c", "\u2d50", "\u2d51", "\u2d52", "\u2d57", "\u2d58", "\u2d5d", "\u2d5e", "\u2d60", "\u2d64", "\u2d65", "\u2d66", "\u2d81", "\u2d82", "\u2d83", "\u2d84", "\u2d85", "\u2d86", "\u2d87", "\u2d88", "\u2d89", "\u2d8a", "\u2d8b", "\u2d8c", "\u2d8d", "\u2d8e", "\u2d8f", "\u2d90", "\u2d91", "\u2d92", "\u2d93", "\u2d94", "\u2d95", "\u2da1", "\u2da2", "\u2da3", "\u2da4", "\u2da5", "\u2da9", "\u2daa", "\u2dab", "\u2dac", "\u2dad", "\u2db1", "\u2db2", "\u2db3", "\u2db4", "\u2db5", "\u2db9", "\u2dba", "\u2dbb", "\u2dbc", "\u2dbd", "\u2dc1", "\u2dc2", "\u2dc3", "\u2dc4", "\u2dc5", "\u2dc9", "\u2dca", "\u2dcb", "\u2dcc", "\u2dcd", "\u2dd1", "\u2dd2", "\u2dd3", "\u2dd4", "\u2dd5", "\u2dd9", "\u2dda", "\u2ddb", "\u2ddc", "\u2ddd", "\u3050", "\u3052", "\u3054", "\u3056", "\u305a", "\u305c", "\u305e", "\u3062", "\u3065", "\u306c", "\u306d", "\u3072", "\u3074", "\u3075", "\u3076", "\u3077", "\u307a", "\u307b", "\u307c", "\u307d", "\u3084", "\u3086", "\u3090", "\u3091", "\u3094", "\u30ac", "\u30b2", "\u30bc", "\u30be", "\u30c2", "\u30c4", "\u30c5", "\u30cc", "\u30ce", "\u30cf", "\u30d2", "\u30e4", "\u30e8", "\u30f0", "\u30f1", "\u30f2", "\u30f4", "\u30f7", "\u30f8", "\u30f9", "\u3106", "\u3107", "\u3108", "\u3109", "\u310a", "\u310b", "\u310c", "\u310d", "\u310e", "\u310f", "\u3111", "\u3112", "\u3113", "\u3114", "\u3115", "\u3116", "\u3117", "\u3118", "\u3119", "\u311a", "\u311b", "\u311c", "\u311d", "\u311e", "\u311f", "\u3120", "\u3121", "\u3122", "\u3123", "\u3124", "\u3125", "\u3126", "\u3127", "\u3128", "\u3129", "\u312a", "\u312b", "\u312c", "\u312e", "\u3132", "\u3133", "\u3134", "\u3135", "\u3136", "\u3137", "\u3138", "\u3139", "\u313a", "\u313b", "\u313c", "\u313d", "\u313e", "\u313f", "\u3140", "\u3141", "\u3142", "\u3143", "\u3144", "\u3145", "\u3146", "\u3147", "\u3148", "\u3149", "\u314a", "\u314b", "\u314c", "\u314d", "\u314e", "\u314f", "\u3150", "\u3151", "\u3152", "\u3153", "\u3154", "\u3155", "\u3156", "\u3157", "\u3158", "\u3159", "\u315a", "\u315b", "\u315c", "\u315d", "\u315e", "\u315f", "\u3160", "\u3161", "\u3162", "\u3163", "\u3164", "\u3165", "\u3166", "\u3167", "\u3168", "\u3169", "\u316a", "\u316b", "\u316c", "\u316d", "\u316e", "\u316f", "\u3170", "\u3171", "\u3172", "\u3173", "\u3174", "\u3175", "\u3176", "\u3177", "\u3178", "\u3179", "\u317a", "\u317b", "\u317c", "\u317d", "\u317e", "\u317f", "\u3180", "\u3181", "\u3182", "\u3183", "\u3184", "\u3185", "\u3186", "\u3187", "\u3188", "\u3189", "\u318a", "\u318b", "\u318c", "\u318d", "\u31a1", "\u31a2", "\u31a3", "\u31a4", "\u31a5", "\u31a6", "\u31a7", "\u31a8", "\u31a9", "\u31aa", "\u31ab", "\u31ac", "\u31ad", "\u31ae", "\u31af", "\u31b0", "\u31b1", "\u31b2", "\u31b3", "\u31b4", "\u31b5", "\u31b6", "\u31b7", "\u31b8", "\u31b9", "\u9fea", "\ua001", "\ua002", "\ua003", "\ua004", "\ua005", "\ua006", "\ua007", "\ua008", "\ua009", "\ua00a", "\ua00b", "\ua00c", "\ua00d", "\ua00e", "\ua00f", "\ua010", "\ua011", "\ua012", "\ua013", "\ua014", "\ua016", "\ua017", "\ua018", "\ua019", "\ua01a", "\ua01b", "\ua01c", "\ua01d", "\ua01e", "\ua01f", "\ua020", "\ua021", "\ua022", "\ua023", "\ua024", "\ua025", "\ua026", "\ua027", "\ua028", "\ua029", "\ua02a", "\ua02b", "\ua02c", "\ua02d", "\ua02e", "\ua02f", "\ua030", "\ua031", "\ua032", "\ua033", "\ua034", "\ua035", "\ua036", "\ua037", "\ua038", "\ua039", "\ua03a", "\ua03b", "\ua03c", "\ua03d", "\ua03e", "\ua03f", "\ua040", "\ua041", "\ua042", "\ua043", "\ua044", "\ua045", "\ua046", "\ua047", "\ua048", "\ua049", "\ua04a", "\ua04b", "\ua04c", "\ua04d", "\ua04e", "\ua04f", "\ua050", "\ua051", "\ua052", "\ua053", "\ua054", "\ua055", "\ua056", "\ua057", "\ua058", "\ua059", "\ua05a", "\ua05b", "\ua05c", "\ua05d", "\ua05e", "\ua05f", "\ua060", "\ua061", "\ua062", "\ua063", "\ua064", "\ua065", "\ua066", "\ua067", "\ua068", "\ua069", "\ua06a", "\ua06b", "\ua06c", "\ua06d", "\ua06e", "\ua06f", "\ua070", "\ua071", "\ua072", "\ua073", "\ua074", "\ua075", "\ua076", "\ua077", "\ua078", "\ua079", "\ua07a", "\ua07b", "\ua07c", "\ua07d", "\ua07e", "\ua07f", "\ua080", "\ua081", "\ua082", "\ua083", "\ua084", "\ua085", "\ua086", "\ua087", "\ua088", "\ua089", "\ua08a", "\ua08b", "\ua08c", "\ua08d", "\ua08e", "\ua08f", "\ua090", "\ua091", "\ua092", "\ua093", "\ua094", "\ua095", "\ua096", "\ua097", "\ua098", "\ua099", "\ua09a", "\ua09b", "\ua09c", "\ua09d", "\ua09e", "\ua09f", "\ua0a0", "\ua0a1", "\ua0a2", "\ua0a3", "\ua0a4", "\ua0a5", "\ua0a6", "\ua0a7", "\ua0a8", "\ua0a9", "\ua0aa", "\ua0ab", "\ua0ac", "\ua0ad", "\ua0ae", "\ua0af", "\ua0b0", "\ua0b1", "\ua0b2", "\ua0b3", "\ua0b4", "\ua0b5", "\ua0b6", "\ua0b7", "\ua0b8", "\ua0b9", "\ua0ba", "\ua0bb", "\ua0bc", "\ua0bd", "\ua0be", "\ua0bf", "\ua0c0", "\ua0c1", "\ua0c2", "\ua0c3", "\ua0c4", "\ua0c5", "\ua0c6", "\ua0c7", "\ua0c8", "\ua0c9", "\ua0ca", "\ua0cb", "\ua0cc", "\ua0cd", "\ua0ce", "\ua0cf", "\ua0d0", "\ua0d1", "\ua0d2", "\ua0d3", "\ua0d4", "\ua0d5", "\ua0d6", "\ua0d7", "\ua0d8", "\ua0d9", "\ua0da", "\ua0db", "\ua0dc", "\ua0dd", "\ua0de", "\ua0df", "\ua0e0", "\ua0e1", "\ua0e2", "\ua0e3", "\ua0e4", "\ua0e5", "\ua0e6", "\ua0e7", "\ua0e8", "\ua0e9", "\ua0ea", "\ua0eb", "\ua0ec", "\ua0ed", "\ua0ee", "\ua0ef", "\ua0f0", "\ua0f1", "\ua0f2", "\ua0f3", "\ua0f4", "\ua0f5", "\ua0f6", "\ua0f7", "\ua0f8", "\ua0f9", "\ua0fa", "\ua0fb", "\ua0fc", "\ua0fd", "\ua0fe", "\ua0ff", "\ua100", "\ua101", "\ua102", "\ua103", "\ua104", "\ua105", "\ua106", "\ua107", "\ua108", "\ua109", "\ua10a", "\ua10b", "\ua10c", "\ua10d", "\ua10e", "\ua10f", "\ua110", "\ua111", "\ua112", "\ua113", "\ua114", "\ua115", "\ua116", "\ua117", "\ua118", "\ua119", "\ua11a", "\ua11b", "\ua11c", "\ua11d", "\ua11e", "\ua11f", "\ua120", "\ua121", "\ua122", "\ua123", "\ua124", "\ua125", "\ua126", "\ua127", "\ua128", "\ua129", "\ua12a", "\ua12b", "\ua12c", "\ua12d", "\ua12e", "\ua12f", "\ua130", "\ua131", "\ua132", "\ua133", "\ua134", "\ua135", "\ua136", "\ua137", "\ua138", "\ua139", "\ua13a", "\ua13b", "\ua13c", "\ua13d", "\ua13e", "\ua13f", "\ua140", "\ua141", "\ua142", "\ua143", "\ua144", "\ua145", "\ua146", "\ua147", "\ua148", "\ua149", "\ua14a", "\ua14b", "\ua14c", "\ua14d", "\ua14e", "\ua14f", "\ua150", "\ua151", "\ua152", "\ua153", "\ua154", "\ua155", "\ua156", "\ua157", "\ua158", "\ua159", "\ua15a", "\ua15b", "\ua15c", "\ua15d", "\ua15e", "\ua15f", "\ua160", "\ua161", "\ua162", "\ua163", "\ua164", "\ua165", "\ua166", "\ua167", "\ua168", "\ua169", "\ua16a", "\ua16b", "\ua16c", "\ua16d", "\ua16e", "\ua16f", "\ua170", "\ua171", "\ua172", "\ua173", "\ua174", "\ua175", "\ua176", "\ua177", "\ua178", "\ua179", "\ua17a", "\ua17b", "\ua17c", "\ua17d", "\ua17e", "\ua17f", "\ua180", "\ua181", "\ua182", "\ua183", "\ua184", "\ua185", "\ua186", "\ua187", "\ua188", "\ua189", "\ua18a", "\ua18b", "\ua18c", "\ua18d", "\ua18e", "\ua18f", "\ua190", "\ua191", "\ua192", "\ua193", "\ua194", "\ua195", "\ua196", "\ua197", "\ua198", "\ua199", "\ua19a", "\ua19b", "\ua19c", "\ua19d", "\ua19e", "\ua19f", "\ua1a0", "\ua1a1", "\ua1a2", "\ua1a3", "\ua1a4", "\ua1a5", "\ua1a6", "\ua1a7", "\ua1a8", "\ua1a9", "\ua1aa", "\ua1ab", "\ua1ac", "\ua1ad", "\ua1ae", "\ua1af", "\ua1b0", "\ua1b1", "\ua1b2", "\ua1b3", "\ua1b4", "\ua1b5", "\ua1b6", "\ua1b7", "\ua1b8", "\ua1b9", "\ua1ba", "\ua1bb", "\ua1bc", "\ua1bd", "\ua1be", "\ua1bf", "\ua1c0", "\ua1c1", "\ua1c2", "\ua1c3", "\ua1c4", "\ua1c5", "\ua1c6", "\ua1c7", "\ua1c8", "\ua1c9", "\ua1ca", "\ua1cb", "\ua1cc", "\ua1cd", "\ua1ce", "\ua1cf", "\ua1d0", "\ua1d1", "\ua1d2", "\ua1d3", "\ua1d4", "\ua1d5", "\ua1d6", "\ua1d7", "\ua1d8", "\ua1d9", "\ua1da", "\ua1db", "\ua1dc", "\ua1dd", "\ua1de", "\ua1df", "\ua1e0", "\ua1e1", "\ua1e2", "\ua1e3", "\ua1e4", "\ua1e5", "\ua1e6", "\ua1e7", "\ua1e8", "\ua1e9", "\ua1ea", "\ua1eb", "\ua1ec", "\ua1ed", "\ua1ee", "\ua1ef", "\ua1f0", "\ua1f1", "\ua1f2", "\ua1f3", "\ua1f4", "\ua1f5", "\ua1f6", "\ua1f7", "\ua1f8", "\ua1f9", "\ua1fa", "\ua1fb", "\ua1fc", "\ua1fd", "\ua1fe", "\ua1ff", "\ua200", "\ua201", "\ua202", "\ua203", "\ua204", "\ua205", "\ua206", "\ua207", "\ua208", "\ua209", "\ua20a", "\ua20b", "\ua20c", "\ua20d", "\ua20e", "\ua20f", "\ua210", "\ua211", "\ua212", "\ua213", "\ua214", "\ua215", "\ua216", "\ua217", "\ua218", "\ua219", "\ua21a", "\ua21b", "\ua21c", "\ua21d", "\ua21e", "\ua21f", "\ua220", "\ua221", "\ua222", "\ua223", "\ua224", "\ua225", "\ua226", "\ua227", "\ua228", "\ua229", "\ua22a", "\ua22b", "\ua22c", "\ua22d", "\ua22e", "\ua22f", "\ua230", "\ua231", "\ua232", "\ua233", "\ua234", "\ua235", "\ua236", "\ua237", "\ua238", "\ua239", "\ua23a", "\ua23b", "\ua23c", "\ua23d", "\ua23e", "\ua23f", "\ua240", "\ua241", "\ua242", "\ua243", "\ua244", "\ua245", "\ua246", "\ua247", "\ua248", "\ua249", "\ua24a", "\ua24b", "\ua24c", "\ua24d", "\ua24e", "\ua24f", "\ua250", "\ua251", "\ua252", "\ua253", "\ua254", "\ua255", "\ua256", "\ua257", "\ua258", "\ua259", "\ua25a", "\ua25b", "\ua25c", "\ua25d", "\ua25e", "\ua25f", "\ua260", "\ua261", "\ua262", "\ua263", "\ua264", "\ua265", "\ua266", "\ua267", "\ua268", "\ua269", "\ua26a", "\ua26b", "\ua26c", "\ua26d", "\ua26e", "\ua26f", "\ua270", "\ua271", "\ua272", "\ua273", "\ua274", "\ua275", "\ua276", "\ua277", "\ua278", "\ua279", "\ua27a", "\ua27b", "\ua27c", "\ua27d", "\ua27e", "\ua27f", "\ua280", "\ua281", "\ua282", "\ua283", "\ua284", "\ua285", "\ua286", "\ua287", "\ua288", "\ua289", "\ua28a", "\ua28b", "\ua28c", "\ua28d", "\ua28e", "\ua28f", "\ua290", "\ua291", "\ua292", "\ua293", "\ua294", "\ua295", "\ua296", "\ua297", "\ua298", "\ua299", "\ua29a", "\ua29b", "\ua29c", "\ua29d", "\ua29e", "\ua29f", "\ua2a0", "\ua2a1", "\ua2a2", "\ua2a3", "\ua2a4", "\ua2a5", "\ua2a6", "\ua2a7", "\ua2a8", "\ua2a9", "\ua2aa", "\ua2ab", "\ua2ac", "\ua2ad", "\ua2ae", "\ua2af", "\ua2b0", "\ua2b1", "\ua2b2", "\ua2b3", "\ua2b4", "\ua2b5", "\ua2b6", "\ua2b7", "\ua2b8", "\ua2b9", "\ua2ba", "\ua2bb", "\ua2bc", "\ua2bd", "\ua2be", "\ua2bf", "\ua2c0", "\ua2c1", "\ua2c2", "\ua2c3", "\ua2c4", "\ua2c5", "\ua2c6", "\ua2c7", "\ua2c8", "\ua2c9", "\ua2ca", "\ua2cb", "\ua2cc", "\ua2cd", "\ua2ce", "\ua2cf", "\ua2d0", "\ua2d1", "\ua2d2", "\ua2d3", "\ua2d4", "\ua2d5", "\ua2d6", "\ua2d7", "\ua2d8", "\ua2d9", "\ua2da", "\ua2db", "\ua2dc", "\ua2dd", "\ua2de", "\ua2df", "\ua2e0", "\ua2e1", "\ua2e2", "\ua2e3", "\ua2e4", "\ua2e5", "\ua2e6", "\ua2e7", "\ua2e8", "\ua2e9", "\ua2ea", "\ua2eb", "\ua2ec", "\ua2ed", "\ua2ee", "\ua2ef", "\ua2f0", "\ua2f1", "\ua2f2", "\ua2f3", "\ua2f4", "\ua2f5", "\ua2f6", "\ua2f7", "\ua2f8", "\ua2f9", "\ua2fa", "\ua2fb", "\ua2fc", "\ua2fd", "\ua2fe", "\ua2ff", "\ua300", "\ua301", "\ua302", "\ua303", "\ua304", "\ua305", "\ua306", "\ua307", "\ua308", "\ua309", "\ua30a", "\ua30b", "\ua30c", "\ua30d", "\ua30e", "\ua30f", "\ua310", "\ua311", "\ua312", "\ua313", "\ua314", "\ua315", "\ua316", "\ua317", "\ua318", "\ua319", "\ua31a", "\ua31b", "\ua31c", "\ua31d", "\ua31e", "\ua31f", "\ua320", "\ua321", "\ua322", "\ua323", "\ua324", "\ua325", "\ua326", "\ua327", "\ua328", "\ua329", "\ua32a", "\ua32b", "\ua32c", "\ua32d", "\ua32e", "\ua32f", "\ua330", "\ua331", "\ua332", "\ua333", "\ua334", "\ua335", "\ua336", "\ua337", "\ua338", "\ua339", "\ua33a", "\ua33b", "\ua33c", "\ua33d", "\ua33e", "\ua33f", "\ua340", "\ua341", "\ua342", "\ua343", "\ua344", "\ua345", "\ua346", "\ua347", "\ua348", "\ua349", "\ua34a", "\ua34b", "\ua34c", "\ua34d", "\ua34e", "\ua34f", "\ua350", "\ua351", "\ua352", "\ua353", "\ua354", "\ua355", "\ua356", "\ua357", "\ua358", "\ua359", "\ua35a", "\ua35b", "\ua35c", "\ua35d", "\ua35e", "\ua35f", "\ua360", "\ua361", "\ua362", "\ua363", "\ua364", "\ua365", "\ua366", "\ua367", "\ua368", "\ua369", "\ua36a", "\ua36b", "\ua36c", "\ua36d", "\ua36e", "\ua36f", "\ua370", "\ua371", "\ua372", "\ua373", "\ua374", "\ua375", "\ua376", "\ua377", "\ua378", "\ua379", "\ua37a", "\ua37b", "\ua37c", "\ua37d", "\ua37e", "\ua37f", "\ua380", "\ua381", "\ua382", "\ua383", "\ua384", "\ua385", "\ua386", "\ua387", "\ua388", "\ua389", "\ua38a", "\ua38b", "\ua38c", "\ua38d", "\ua38e", "\ua38f", "\ua390", "\ua391", "\ua392", "\ua393", "\ua394", "\ua395", "\ua396", "\ua397", "\ua398", "\ua399", "\ua39a", "\ua39b", "\ua39c", "\ua39d", "\ua39e", "\ua39f", "\ua3a0", "\ua3a1", "\ua3a2", "\ua3a3", "\ua3a4", "\ua3a5", "\ua3a6", "\ua3a7", "\ua3a8", "\ua3a9", "\ua3aa", "\ua3ab", "\ua3ac", "\ua3ad", "\ua3ae", "\ua3af", "\ua3b0", "\ua3b1", "\ua3b2", "\ua3b3", "\ua3b4", "\ua3b5", "\ua3b6", "\ua3b7", "\ua3b8", "\ua3b9", "\ua3ba", "\ua3bb", "\ua3bc", "\ua3bd", "\ua3be", "\ua3bf", "\ua3c0", "\ua3c1", "\ua3c2", "\ua3c3", "\ua3c4", "\ua3c5", "\ua3c6", "\ua3c7", "\ua3c8", "\ua3c9", "\ua3ca", "\ua3cb", "\ua3cc", "\ua3cd", "\ua3ce", "\ua3cf", "\ua3d0", "\ua3d1", "\ua3d2", "\ua3d3", "\ua3d4", "\ua3d5", "\ua3d6", "\ua3d7", "\ua3d8", "\ua3d9", "\ua3da", "\ua3db", "\ua3dc", "\ua3dd", "\ua3de", "\ua3df", "\ua3e0", "\ua3e1", "\ua3e2", "\ua3e3", "\ua3e4", "\ua3e5", "\ua3e6", "\ua3e7", "\ua3e8", "\ua3e9", "\ua3ea", "\ua3eb", "\ua3ec", "\ua3ed", "\ua3ee", "\ua3ef", "\ua3f0", "\ua3f1", "\ua3f2", "\ua3f3", "\ua3f4", "\ua3f5", "\ua3f6", "\ua3f7", "\ua3f8", "\ua3f9", "\ua3fa", "\ua3fb", "\ua3fc", "\ua3fd", "\ua3fe", "\ua3ff", "\ua400", "\ua401", "\ua402", "\ua403", "\ua404", "\ua405", "\ua406", "\ua407", "\ua408", "\ua409", "\ua40a", "\ua40b", "\ua40c", "\ua40d", "\ua40e", "\ua40f", "\ua410", "\ua411", "\ua412", "\ua413", "\ua414", "\ua415", "\ua416", "\ua417", "\ua418", "\ua419", "\ua41a", "\ua41b", "\ua41c", "\ua41d", "\ua41e", "\ua41f", "\ua420", "\ua421", "\ua422", "\ua423", "\ua424", "\ua425", "\ua426", "\ua427", "\ua428", "\ua429", "\ua42a", "\ua42b", "\ua42c", "\ua42d", "\ua42e", "\ua42f", "\ua430", "\ua431", "\ua432", "\ua433", "\ua434", "\ua435", "\ua436", "\ua437", "\ua438", "\ua439", "\ua43a", "\ua43b", "\ua43c", "\ua43d", "\ua43e", "\ua43f", "\ua440", "\ua441", "\ua442", "\ua443", "\ua444", "\ua445", "\ua446", "\ua447", "\ua448", "\ua449", "\ua44a", "\ua44b", "\ua44c", "\ua44d", "\ua44e", "\ua44f", "\ua450", "\ua451", "\ua452", "\ua453", "\ua454", "\ua455", "\ua456", "\ua457", "\ua458", "\ua459", "\ua45a", "\ua45b", "\ua45c", "\ua45d", "\ua45e", "\ua45f", "\ua460", "\ua461", "\ua462", "\ua463", "\ua464", "\ua465", "\ua466", "\ua467", "\ua468", "\ua469", "\ua46a", "\ua46b", "\ua46c", "\ua46d", "\ua46e", "\ua46f", "\ua470", "\ua471", "\ua472", "\ua473", "\ua474", "\ua475", "\ua476", "\ua477", "\ua478", "\ua479", "\ua47a", "\ua47b", "\ua47c", "\ua47d", "\ua47e", "\ua47f", "\ua480", "\ua481", "\ua482", "\ua483", "\ua484", "\ua485", "\ua486", "\ua487", "\ua488", "\ua489", "\ua48a", "\ua48b", "\ua4d1", "\ua4d2", "\ua4d3", "\ua4d4", "\ua4d5", "\ua4d6", "\ua4d7", "\ua4d8", "\ua4d9", "\ua4da", "\ua4db", "\ua4dc", "\ua4dd", "\ua4de", "\ua4df", "\ua4e0", "\ua4e1", "\ua4e2", "\ua4e3", "\ua4e4", "\ua4e5", "\ua4e6", "\ua4e7", "\ua4e8", "\ua4e9", "\ua4ea", "\ua4eb", "\ua4ec", "\ua4ed", "\ua4ee", "\ua4ef", "\ua4f0", "\ua4f1", "\ua4f2", "\ua4f3", "\ua4f4", "\ua4f5", "\ua4f6", "\ua4f7", "\ua501", "\ua502", "\ua503", "\ua504", "\ua505", "\ua506", "\ua507", "\ua508", "\ua509", "\ua50a", "\ua50b", "\ua50c", "\ua50d", "\ua50e", "\ua50f", "\ua510", "\ua511", "\ua512", "\ua513", "\ua514", "\ua515", "\ua516", "\ua517", "\ua518", "\ua519", "\ua51a", "\ua51b", "\ua51c", "\ua51d", "\ua51e", "\ua51f", "\ua520", "\ua521", "\ua522", "\ua523", "\ua524", "\ua525", "\ua526", "\ua527", "\ua528", "\ua529", "\ua52a", "\ua52b", "\ua52c", "\ua52d", "\ua52e", "\ua52f", "\ua530", "\ua531", "\ua532", "\ua533", "\ua534", "\ua535", "\ua536", "\ua537", "\ua538", "\ua539", "\ua53a", "\ua53b", "\ua53c", "\ua53d", "\ua53e", "\ua53f", "\ua540", "\ua541", "\ua542", "\ua543", "\ua544", "\ua545", "\ua546", "\ua547", "\ua548", "\ua549", "\ua54a", "\ua54b", "\ua54c", "\ua54d", "\ua54e", "\ua54f", "\ua550", "\ua551", "\ua552", "\ua553", "\ua554", "\ua555", "\ua556", "\ua557", "\ua558", "\ua559", "\ua55a", "\ua55b", "\ua55c", "\ua55d", "\ua55e", "\ua55f", "\ua560", "\ua561", "\ua562", "\ua563", "\ua564", "\ua565", "\ua566", "\ua567", "\ua568", "\ua569", "\ua56a", "\ua56b", "\ua56c", "\ua56d", "\ua56e", "\ua56f", "\ua570", "\ua571", "\ua572", "\ua573", "\ua574", "\ua575", "\ua576", "\ua577", "\ua578", "\ua579", "\ua57a", "\ua57b", "\ua57c", "\ua57d", "\ua57e", "\ua57f", "\ua580", "\ua581", "\ua582", "\ua583", "\ua584", "\ua585", "\ua586", "\ua587", "\ua588", "\ua589", "\ua58a", "\ua58b", "\ua58c", "\ua58d", "\ua58e", "\ua58f", "\ua590", "\ua591", "\ua592", "\ua593", "\ua594", "\ua595", "\ua596", "\ua597", "\ua598", "\ua599", "\ua59a", "\ua59b", "\ua59c", "\ua59d", "\ua59e", "\ua59f", "\ua5a0", "\ua5a1", "\ua5a2", "\ua5a3", "\ua5a4", "\ua5a5", "\ua5a6", "\ua5a7", "\ua5a8", "\ua5a9", "\ua5aa", "\ua5ab", "\ua5ac", "\ua5ad", "\ua5ae", "\ua5af", "\ua5b0", "\ua5b1", "\ua5b2", "\ua5b3", "\ua5b4", "\ua5b5", "\ua5b6", "\ua5b7", "\ua5b8", "\ua5b9", "\ua5ba", "\ua5bb", "\ua5bc", "\ua5bd", "\ua5be", "\ua5bf", "\ua5c0", "\ua5c1", "\ua5c2", "\ua5c3", "\ua5c4", "\ua5c5", "\ua5c6", "\ua5c7", "\ua5c8", "\ua5c9", "\ua5ca", "\ua5cb", "\ua5cc", "\ua5cd", "\ua5ce", "\ua5cf", "\ua5d0", "\ua5d1", "\ua5d2", "\ua5d3", "\ua5d4", "\ua5d5", "\ua5d6", "\ua5d7", "\ua5d8", "\ua5d9", "\ua5da", "\ua5db", "\ua5dc", "\ua5dd", "\ua5de", "\ua5df", "\ua5e0", "\ua5e1", "\ua5e2", "\ua5e3", "\ua5e4", "\ua5e5", "\ua5e6", "\ua5e7", "\ua5e8", "\ua5e9", "\ua5ea", "\ua5eb", "\ua5ec", "\ua5ed", "\ua5ee", "\ua5ef", "\ua5f0", "\ua5f1", "\ua5f2", "\ua5f3", "\ua5f4", "\ua5f5", "\ua5f6", "\ua5f7", "\ua5f8", "\ua5f9", "\ua5fa", "\ua5fb", "\ua5fc", "\ua5fd", "\ua5fe", "\ua5ff", "\ua600", "\ua601", "\ua602", "\ua603", "\ua604", "\ua605", "\ua606", "\ua607", "\ua608", "\ua609", "\ua60a", "\ua60b", "\ua611", "\ua612", "\ua613", "\ua614", "\ua615", "\ua616", "\ua617", "\ua618", "\ua619", "\ua61a", "\ua61b", "\ua61c", "\ua61d", "\ua61e", "\ua6a1", "\ua6a2", "\ua6a3", "\ua6a4", "\ua6a5", "\ua6a6", "\ua6a7", "\ua6a8", "\ua6a9", "\ua6aa", "\ua6ab", "\ua6ac", "\ua6ad", "\ua6ae", "\ua6af", "\ua6b0", "\ua6b1", "\ua6b2", "\ua6b3", "\ua6b4", "\ua6b5", "\ua6b6", "\ua6b7", "\ua6b8", "\ua6b9", "\ua6ba", "\ua6bb", "\ua6bc", "\ua6bd", "\ua6be", "\ua6bf", "\ua6c0", "\ua6c1", "\ua6c2", "\ua6c3", "\ua6c4", "\ua6c5", "\ua6c6", "\ua6c7", "\ua6c8", "\ua6c9", "\ua6ca", "\ua6cb", "\ua6cc", "\ua6cd", "\ua6ce", "\ua6cf", "\ua6d0", "\ua6d1", "\ua6d2", "\ua6d3", "\ua6d4", "\ua6d5", "\ua6d6", "\ua6d7", "\ua6d8", "\ua6d9", "\ua6da", "\ua6db", "\ua6dc", "\ua6dd", "\ua6de", "\ua6df", "\ua6e0", "\ua6e1", "\ua6e2", "\ua6e3", "\ua6e4", "\ua6e5", "\ua78f", "\ua7fb", "\ua7fc", "\ua7fd", "\ua7fe", "\ua7ff", "\ua800", "\ua804", "\ua808", "\ua809", "\ua80d", "\ua80e", "\ua80f", "\ua810", "\ua811", "\ua812", "\ua813", "\ua814", "\ua815", "\ua816", "\ua817", "\ua818", "\ua819", "\ua81a", "\ua81b", "\ua81c", "\ua81d", "\ua81e", "\ua81f", "\ua820", "\ua821", "\ua841", "\ua842", "\ua843", "\ua844", "\ua845", "\ua846", "\ua847", "\ua848", "\ua849", "\ua84a", "\ua84b", "\ua84c", "\ua84d", "\ua84e", "\ua84f", "\ua850", "\ua851", "\ua852", "\ua853", "\ua854", "\ua855", "\ua856", "\ua857", "\ua858", "\ua859", "\ua85a", "\ua85b", "\ua85c", "\ua85d", "\ua85e", "\ua85f", "\ua860", "\ua861", "\ua862", "\ua863", "\ua864", "\ua865", "\ua866", "\ua867", "\ua868", "\ua869", "\ua86a", "\ua86b", "\ua86c", "\ua86d", "\ua86e", "\ua86f", "\ua870", "\ua871", "\ua872", "\ua883", "\ua884", "\ua885", "\ua886", "\ua887", "\ua888", "\ua889", "\ua88a", "\ua88b", "\ua88c", "\ua88d", "\ua88e", "\ua88f", "\ua890", "\ua891", "\ua892", "\ua893", "\ua894", "\ua895", "\ua896", "\ua897", "\ua898", "\ua899", "\ua89a", "\ua89b", "\ua89c", "\ua89d", "\ua89e", "\ua89f", "\ua8a0", "\ua8a1", "\ua8a2", "\ua8a3", "\ua8a4", "\ua8a5", "\ua8a6", "\ua8a7", "\ua8a8", "\ua8a9", "\ua8aa", "\ua8ab", "\ua8ac", "\ua8ad", "\ua8ae", "\ua8af", "\ua8b0", "\ua8b1", "\ua8b2", "\ua8f3", "\ua8f4", "\ua8f5", "\ua8f6", "\ua8fd", "\ua90b", "\ua90c", "\ua90d", "\ua90e", "\ua90f", "\ua910", "\ua911", "\ua912", "\ua913", "\ua914", "\ua915", "\ua916", "\ua917", "\ua918", "\ua919", "\ua91a", "\ua91b", "\ua91c", "\ua91d", "\ua91e", "\ua91f", "\ua920", "\ua921", "\ua922", "\ua923", "\ua924", "\ua931", "\ua932", "\ua933", "\ua934", "\ua935", "\ua936", "\ua937", "\ua938", "\ua939", "\ua93a", "\ua93b", "\ua93c", "\ua93d", "\ua93e", "\ua93f", "\ua940", "\ua941", "\ua942", "\ua943", "\ua944", "\ua945", "\ua961", "\ua962", "\ua963", "\ua964", "\ua965", "\ua966", "\ua967", "\ua968", "\ua969", "\ua96a", "\ua96b", "\ua96c", "\ua96d", "\ua96e", "\ua96f", "\ua970", "\ua971", "\ua972", "\ua973", "\ua974", "\ua975", "\ua976", "\ua977", "\ua978", "\ua979", "\ua97a", "\ua97b", "\ua985", "\ua986", "\ua987", "\ua988", "\ua989", "\ua98a", "\ua98b", "\ua98c", "\ua98d", "\ua98e", "\ua98f", "\ua990", "\ua991", "\ua992", "\ua993", "\ua994", "\ua995", "\ua996", "\ua997", "\ua998", "\ua999", "\ua99a", "\ua99b", "\ua99c", "\ua99d", "\ua99e", "\ua99f", "\ua9a0", "\ua9a1", "\ua9a2", "\ua9a3", "\ua9a4", "\ua9a5", "\ua9a6", "\ua9a7", "\ua9a8", "\ua9a9", "\ua9aa", "\ua9ab", "\ua9ac", "\ua9ad", "\ua9ae", "\ua9af", "\ua9b0", "\ua9b1", "\ua9e1", "\ua9e2", "\ua9e3", "\ua9e7", "\ua9e8", "\ua9e9", "\ua9ea", "\ua9eb", "\ua9ec", "\ua9ed", "\ua9ee", "\ua9fb", "\ua9fc", "\ua9fd", "\uaa01", "\uaa02", "\uaa03", "\uaa04", "\uaa05", "\uaa06", "\uaa07", "\uaa08", "\uaa09", "\uaa0a", "\uaa0b", "\uaa0c", "\uaa0d", "\uaa0e", "\uaa0f", "\uaa10", "\uaa11", "\uaa12", "\uaa13", "\uaa14", "\uaa15", "\uaa16", "\uaa17", "\uaa18", "\uaa19", "\uaa1a", "\uaa1b", "\uaa1c", "\uaa1d", "\uaa1e", "\uaa1f", "\uaa20", "\uaa21", "\uaa22", "\uaa23", "\uaa24", "\uaa25", "\uaa26", "\uaa27", "\uaa41", "\uaa45", "\uaa46", "\uaa47", "\uaa48", "\uaa49", "\uaa4a", "\uaa61", "\uaa62", "\uaa63", "\uaa64", "\uaa65", "\uaa66", "\uaa67", "\uaa68", "\uaa69", "\uaa6a", "\uaa6b", "\uaa6c", "\uaa6d", "\uaa6e", "\uaa6f", "\uaa71", "\uaa72", "\uaa73", "\uaa74", "\uaa75", "\uaa7f", "\uaa80", "\uaa81", "\uaa82", "\uaa83", "\uaa84", "\uaa85", "\uaa86", "\uaa87", "\uaa88", "\uaa89", "\uaa8a", "\uaa8b", "\uaa8c", "\uaa8d", "\uaa8e", "\uaa8f", "\uaa90", "\uaa91", "\uaa92", "\uaa93", "\uaa94", "\uaa95", "\uaa96", "\uaa97", "\uaa98", "\uaa99", "\uaa9a", "\uaa9b", "\uaa9c", "\uaa9d", "\uaa9e", "\uaa9f", "\uaaa0", "\uaaa1", "\uaaa2", "\uaaa3", "\uaaa4", "\uaaa5", "\uaaa6", "\uaaa7", "\uaaa8", "\uaaa9", "\uaaaa", "\uaaab", "\uaaac", "\uaaad", "\uaaae", "\uaaba", "\uaabb", "\uaabc", "\uaadc", "\uaae1", "\uaae2", "\uaae3", "\uaae4", "\uaae5", "\uaae6", "\uaae7", "\uaae8", "\uaae9", "\uab02", "\uab03", "\uab04", "\uab05", "\uab0a", "\uab0b", "\uab0c", "\uab0d", "\uab12", "\uab13", "\uab14", "\uab15", "\uab21", "\uab22", "\uab23", "\uab24", "\uab25", "\uab29", "\uab2a", "\uab2b", "\uab2c", "\uab2d", "\uabc1", "\uabc2", "\uabc3", "\uabc4", "\uabc5", "\uabc6", "\uabc7", "\uabc8", "\uabc9", "\uabca", "\uabcb", "\uabcc", "\uabcd", "\uabce", "\uabcf", "\uabd0", "\uabd1", "\uabd2", "\uabd3", "\uabd4", "\uabd5", "\uabd6", "\uabd7", "\uabd8", "\uabd9", "\uabda", "\uabdb", "\uabdc", "\uabdd", "\uabde", "\uabdf", "\uabe0", "\uabe1", "\ud7b1", "\ud7b2", "\ud7b3", "\ud7b4", "\ud7b5", "\ud7b6", "\ud7b7", "\ud7b8", "\ud7b9", "\ud7ba", "\ud7bb", "\ud7bc", "\ud7bd", "\ud7be", "\ud7bf", "\ud7c0", "\ud7c1", "\ud7c2", "\ud7c3", "\ud7c4", "\ud7c5", "\ud7cc", "\ud7cd", "\ud7ce", "\ud7cf", "\ud7d0", "\ud7d1", "\ud7d2", "\ud7d3", "\ud7d4", "\ud7d5", "\ud7d6", "\ud7d7", "\ud7d8", "\ud7d9", "\ud7da", "\ud7db", "\ud7dc", "\ud7dd", "\ud7de", "\ud7df", "\ud7e0", "\ud7e1", "\ud7e2", "\ud7e3", "\ud7e4", "\ud7e5", "\ud7e6", "\ud7e7", "\ud7e8", "\ud7e9", "\ud7ea", "\ud7eb", "\ud7ec", "\ud7ed", "\ud7ee", "\ud7ef", "\ud7f0", "\ud7f1", "\ud7f2", "\ud7f3", "\ud7f4", "\ud7f5", "\ud7f6", "\ud7f7", "\ud7f8", "\ud7f9", "\ud7fa", "\uf90f", "\uf910", "\uf911", "\uf912", "\uf913", "\uf915", "\uf916", "\uf917", "\uf918", "\uf92a", "\uf92b", "\uf934", "\uf935", "\uf936", "\uf937", "\uf938", "\uf93a", "\uf93b", "\uf93c", "\uf93d", "\uf93e", "\uf93f", "\uf940", "\uf941", "\uf942", "\uf943", "\uf94b", "\uf94c", "\uf94d", "\uf94e", "\uf94f", "\uf950", "\uf951", "\uf953", "\uf954", "\uf955", "\uf956", "\uf957", "\ufa2e", "\ufa2f", "\ufa30", "\ufa31", "\ufa32", "\ufa33", "\ufa34", "\ufa35", "\ufa36", "\ufa37", "\ufa38", "\ufa39", "\ufa3a", "\ufa3b", "\ufa3c", "\ufa3d", "\ufa3e", "\ufa3f", "\ufa40", "\ufa41", "\ufa42", "\ufa43", "\ufa44", "\ufa45", "\ufa46", "\ufa47", "\ufa48", "\ufa49", "\ufa4a", "\ufa4b", "\ufa4c", "\ufa4d", "\ufa4e", "\ufa4f", "\ufa50", "\ufa51", "\ufa52", "\ufa53", "\ufa54", "\ufa55", "\ufa56", "\ufa57", "\ufa58", "\ufa59", "\ufa5a", "\ufa5b", "\ufa5c", "\ufa5d", "\ufa5e", "\ufa5f", "\ufa60", "\ufa61", "\ufa62", "\ufa63", "\ufa64", "\ufa65", "\ufa66", "\ufa67", "\ufa68", "\ufa69", "\ufa6a", "\ufa6b", "\ufa6c", "\ufa71", "\ufa72", "\ufa73", "\ufa74", "\ufa75", "\ufa76", "\ufa77", "\ufa78", "\ufa79", "\ufa7a", "\ufa7b", "\ufa7c", "\ufa7d", "\ufa7e", "\ufa7f", "\ufa80", "\ufa81", "\ufa82", "\ufa83", "\ufa84", "\ufa85", "\ufa86", "\ufa87", "\ufa88", "\ufa89", "\ufa8a", "\ufa8b", "\ufa8c", "\ufa8d", "\ufa8e", "\ufa8f", "\ufa90", "\ufa91", "\ufa92", "\ufa93", "\ufa94", "\ufa95", "\ufa96", "\ufa97", "\ufa98", "\ufa99", "\ufa9a", "\ufa9b", "\ufa9c", "\ufa9d", "\ufa9e", "\ufa9f", "\ufaa0", "\ufaa1", "\ufaa2", "\ufaa3", "\ufaa4", "\ufaa5", "\ufaa6", "\ufaa7", "\ufaa8", "\ufaa9", "\ufaaa", "\ufaab", "\ufaac", "\ufaad", "\ufaae", "\ufaaf", "\ufab0", "\ufab1", "\ufab2", "\ufab3", "\ufab4", "\ufab5", "\ufab6", "\ufab7", "\ufab8", "\ufab9", "\ufaba", "\ufabb", "\ufabc", "\ufabd", "\ufabe", "\ufabf", "\ufac0", "\ufac1", "\ufac2", "\ufac3", "\ufac4", "\ufac5", "\ufac6", "\ufac7", "\ufac8", "\ufac9", "\ufaca", "\ufacb", "\ufacc", "\ufacd", "\uface", "\ufacf", "\ufad0", "\ufad1", "\ufad2", "\ufad3", "\ufad4", "\ufad5", "\ufad6", "\ufad7", "\ufad8", "\ufb20", "\ufb21", "\ufb22", "\ufb23", "\ufb24", "\ufb25", "\ufb26", "\ufb27", "\ufb2b", "\ufb2c", "\ufb2d", "\ufb2e", "\ufb2f", "\ufb30", "\ufb31", "\ufb32", "\ufb33", "\ufb34", "\ufb35", "\ufb39", "\ufb3a", "\ufb3b", "\ufb47", "\ufb48", "\ufb49", "\ufb4a", "\ufb4b", "\ufb4c", "\ufb4d", "\ufb4e", "\ufb4f", "\ufb50", "\ufb51", "\ufb52", "\ufb53", "\ufb54", "\ufb55", "\ufb56", "\ufb57", "\ufb58", "\ufb59", "\ufb5a", "\ufb5b", "\ufb5c", "\ufb5d", "\ufb5e", "\ufb5f", "\ufb60", "\ufb61", "\ufb62", "\ufb63", "\ufb64", "\ufb65", "\ufb66", "\ufb67", "\ufb68", "\ufb69", "\ufb6a", "\ufb6b", "\ufb6c", "\ufb6d", "\ufb6e", "\ufb6f", "\ufb70", "\ufb71", "\ufb72", "\ufb73", "\ufb74", "\ufb75", "\ufb76", "\ufb77", "\ufb78", "\ufb79", "\ufb7a", "\ufb7b", "\ufb7c", "\ufb7d", "\ufb7e", "\ufb7f", "\ufb80", "\ufb81", "\ufb82", "\ufb83", "\ufb84", "\ufb85", "\ufb86", "\ufb87", "\ufb88", "\ufb89", "\ufb8a", "\ufb8b", "\ufb8c", "\ufb8d", "\ufb8e", "\ufb8f", "\ufb90", "\ufb91", "\ufb92", "\ufb93", "\ufb94", "\ufb95", "\ufb96", "\ufb97", "\ufb98", "\ufb99", "\ufb9a", "\ufb9b", "\ufb9c", "\ufb9d", "\ufb9e", "\ufb9f", "\ufba0", "\ufba1", "\ufba2", "\ufba3", "\ufba4", "\ufba5", "\ufba6", "\ufba7", "\ufba8", "\ufba9", "\ufbaa", "\ufbab", "\ufbac", "\ufbad", "\ufbae", "\ufbaf", "\ufbb0", "\ufbd4", "\ufbd5", "\ufbd6", "\ufbd7", "\ufbd8", "\ufbd9", "\ufbda", "\ufbdb", "\ufbdc", "\ufbdd", "\ufbde", "\ufbdf", "\ufbe0", "\ufbe1", "\ufbe2", "\ufbe3", "\ufbe4", "\ufbe5", "\ufbe6", "\ufbe7", "\ufbe8", "\ufbe9", "\ufbea", "\ufbeb", "\ufbec", "\ufbed", "\ufbee", "\ufbef", "\ufbf0", "\ufbf1", "\ufbf2", "\ufbf3", "\ufbf4", "\ufbf5", "\ufbf6", "\ufbf7", "\ufbf8", "\ufbf9", "\ufbfa", "\ufbfb", "\ufbfc", "\ufbfd", "\ufbfe", "\ufbff", "\ufc00", "\ufc01", "\ufc02", "\ufc03", "\ufc04", "\ufc05", "\ufc06", "\ufc07", "\ufc08", "\ufc09", "\ufc0a", "\ufc0b", "\ufc0c", "\ufc0d", "\ufc0e", "\ufc0f", "\ufc10", "\ufc11", "\ufc12", "\ufc13", "\ufc14", "\ufc15", "\ufc16", "\ufc17", "\ufc18", "\ufc19", "\ufc1a", "\ufc1b", "\ufc1c", "\ufc1d", "\ufc1e", "\ufc1f", "\ufc20", "\ufc21", "\ufc22", "\ufc23", "\ufc24", "\ufc25", "\ufc26", "\ufc27", "\ufc28", "\ufc29", "\ufc2a", "\ufc2b", "\ufc2c", "\ufc2d", "\ufc2e", "\ufc2f", "\ufc30", "\ufc31", "\ufc32", "\ufc33", "\ufc34", "\ufc35", "\ufc36", "\ufc37", "\ufc38", "\ufc39", "\ufc3a", "\ufc3b", "\ufc3c", "\ufc3d", "\ufc3e", "\ufc3f", "\ufc40", "\ufc41", "\ufc42", "\ufc43", "\ufc44", "\ufc45", "\ufc46", "\ufc47", "\ufc48", "\ufc49", "\ufc4a", "\ufc4b", "\ufc4c", "\ufc4d", "\ufc4e", "\ufc4f", "\ufc50", "\ufc51", "\ufc52", "\ufc53", "\ufc54", "\ufc55", "\ufc56", "\ufc57", "\ufc58", "\ufc59", "\ufc5a", "\ufc5b", "\ufc5c", "\ufc5d", "\ufc5e", "\ufc5f", "\ufc60", "\ufc61", "\ufc62", "\ufc63", "\ufc64", "\ufc65", "\ufc66", "\ufc67", "\ufc68", "\ufc69", "\ufc6a", "\ufc6b", "\ufc6c", "\ufc6d", "\ufc6e", "\ufc6f", "\ufc70", "\ufc71", "\ufc72", "\ufc73", "\ufc74", "\ufc75", "\ufc76", "\ufc77", "\ufc78", "\ufc79", "\ufc7a", "\ufc7b", "\ufc7c", "\ufc7d", "\ufc7e", "\ufc7f", "\ufc80", "\ufc81", "\ufc82", "\ufc83", "\ufc84", "\ufc85", "\ufc86", "\ufc87", "\ufc88", "\ufc89", "\ufc8a", "\ufc8b", "\ufc8c", "\ufc8d", "\ufc8e", "\ufc8f", "\ufc90", "\ufc91", "\ufc92", "\ufc93", "\ufc94", "\ufc95", "\ufc96", "\ufc97", "\ufc98", "\ufc99", "\ufc9a", "\ufc9b", "\ufc9c", "\ufc9d", "\ufc9e", "\ufc9f", "\ufca0", "\ufca1", "\ufca2", "\ufca3", "\ufca4", "\ufca5", "\ufca6", "\ufca7", "\ufca8", "\ufca9", "\ufcaa", "\ufcab", "\ufcac", "\ufcad", "\ufcae", "\ufcaf", "\ufcb0", "\ufcb1", "\ufcb2", "\ufcb3", "\ufcb4", "\ufcb5", "\ufcb6", "\ufcb7", "\ufcb8", "\ufcb9", "\ufcba", "\ufcbb", "\ufcbc", "\ufcbd", "\ufcbe", "\ufcbf", "\ufcc0", "\ufcc1", "\ufcc2", "\ufcc3", "\ufcc4", "\ufcc5", "\ufcc6", "\ufcc7", "\ufcc8", "\ufcc9", "\ufcca", "\ufccb", "\ufccc", "\ufccd", "\ufcce", "\ufccf", "\ufcd0", "\ufcd1", "\ufcd2", "\ufcd3", "\ufcd4", "\ufcd5", "\ufcd6", "\ufcd7", "\ufcd8", "\ufcd9", "\ufcda", "\ufcdb", "\ufcdc", "\ufcdd", "\ufcde", "\ufcdf", "\ufce0", "\ufce1", "\ufce2", "\ufce3", "\ufce4", "\ufce5", "\ufce6", "\ufce7", "\ufce8", "\ufce9", "\ufcea", "\ufceb", "\ufcec", "\ufced", "\ufcee", "\ufcef", "\ufcf0", "\ufcf1", "\ufcf2", "\ufcf3", "\ufcf4", "\ufcf5", "\ufcf6", "\ufcf7", "\ufcf8", "\ufcf9", "\ufcfa", "\ufcfb", "\ufcfc", "\ufcfd", "\ufcfe", "\ufcff", "\ufd00", "\ufd01", "\ufd02", "\ufd03", "\ufd04", "\ufd05", "\ufd06", "\ufd07", "\ufd08", "\ufd09", "\ufd0a", "\ufd0b", "\ufd0c", "\ufd0d", "\ufd0e", "\ufd0f", "\ufd10", "\ufd11", "\ufd12", "\ufd13", "\ufd14", "\ufd15", "\ufd16", "\ufd17", "\ufd18", "\ufd19", "\ufd1a", "\ufd1b", "\ufd1c", "\ufd1d", "\ufd1e", "\ufd1f", "\ufd20", "\ufd21", "\ufd22", "\ufd23", "\ufd24", "\ufd25", "\ufd26", "\ufd27", "\ufd28", "\ufd29", "\ufd2a", "\ufd2b", "\ufd2c", "\ufd2d", "\ufd2e", "\ufd2f", "\ufd30", "\ufd31", "\ufd32", "\ufd33", "\ufd34", "\ufd35", "\ufd36", "\ufd37", "\ufd38", "\ufd39", "\ufd3a", "\ufd3b", "\ufd3c", "\ufd51", "\ufd52", "\ufd53", "\ufd54", "\ufd55", "\ufd56", "\ufd57", "\ufd58", "\ufd59", "\ufd5a", "\ufd5b", "\ufd5c", "\ufd5d", "\ufd5e", "\ufd5f", "\ufd60", "\ufd61", "\ufd62", "\ufd63", "\ufd64", "\ufd65", "\ufd66", "\ufd67", "\ufd68", "\ufd69", "\ufd6a", "\ufd6b", "\ufd6c", "\ufd6d", "\ufd6e", "\ufd6f", "\ufd70", "\ufd71", "\ufd72", "\ufd73", "\ufd74", "\ufd75", "\ufd76", "\ufd77", "\ufd78", "\ufd79", "\ufd7a", "\ufd7b", "\ufd7c", "\ufd7d", "\ufd7e", "\ufd7f", "\ufd80", "\ufd81", "\ufd82", "\ufd83", "\ufd84", "\ufd85", "\ufd86", "\ufd87", "\ufd88", "\ufd89", "\ufd8a", "\ufd8b", "\ufd8c", "\ufd8d", "\ufd8e", "\ufd93", "\ufd94", "\ufd95", "\ufd96", "\ufd97", "\ufd98", "\ufd99", "\ufd9a", "\ufd9b", "\ufd9c", "\ufd9d", "\ufd9e", "\ufd9f", "\ufda0", "\ufda1", "\ufda2", "\ufda3", "\ufda4", "\ufda5", "\ufda6", "\ufda7", "\ufda8", "\ufda9", "\ufdaa", "\ufdab", "\ufdac", "\ufdad", "\ufdae", "\ufdaf", "\ufdb0", "\ufdb1", "\ufdb2", "\ufdb3", "\ufdb4", "\ufdb5", "\ufdb6", "\ufdb7", "\ufdb8", "\ufdb9", "\ufdba", "\ufdbb", "\ufdbc", "\ufdbd", "\ufdbe", "\ufdbf", "\ufdc0", "\ufdc1", "\ufdc2", "\ufdc3", "\ufdc4", "\ufdc5", "\ufdc6", "\ufdf1", "\ufdf2", "\ufdf3", "\ufdf4", "\ufdf5", "\ufdf6", "\ufdf7", "\ufdf8", "\ufdf9", "\ufdfa", "\ufe72", "\ufe73", "\ufe78", "\ufe7a", "\ufe7c", "\ufe7e", "\ufe86", "\ufe87", "\ufe89", "\ufe8c", "\ufe90", "\ufe92", "\ufe94", "\ufe96", "\ufe98", "\ufe9a", "\ufe9c", "\ufe9e", "\ufea0", "\ufea2", "\ufea4", "\ufea6", "\ufea8", "\ufeaa", "\ufeac", "\ufeae", "\ufeb0", "\ufeb2", "\ufeb4", "\ufeb6", "\ufeb8", "\ufeba", "\ufebc", "\ufebe", "\ufec0", "\ufec2", "\ufec3", "\ufec4", "\ufec6", "\ufec8", "\ufed2", "\ufed4", "\ufed6", "\ufed8", "\ufeda", "\ufedc", "\ufede", "\ufee0", "\ufee2", "\ufee4", "\ufee6", "\ufee8", "\ufeea", "\ufeee", "\ufef4", "\uff71", "\uff72", "\uff73", "\uff74", "\uff75", "\uff76", "\uff77", "\uff78", "\uff79", "\uff7b", "\uff7c", "\uff7d", "\uff7e", "\uff7f", "\uff80", "\uff82", "\uff83", "\uff84", "\uff85", "\uff87", "\uff88", "\uff89", "\uff8b", "\uff8c", "\uff8d", "\uff8e", "\uff8f", "\uff90", "\uff91", "\uff92", "\uff93", "\uff94", "\uff95", "\uff96", "\uff97", "\uff98", "\uff99", "\uff9a", "\uff9b", "\uff9c", "\uffa0", "\uffa1", "\uffa2", "\uffa3", "\uffa4", "\uffa5", "\uffa6", "\uffa7", "\uffa8", "\uffa9", "\uffaa", "\uffab", "\uffac", "\uffad", "\uffae", "\uffaf", "\uffb0", "\uffb1", "\uffb2", "\uffb3", "\uffb4", "\uffb5", "\uffb6", "\uffb7", "\uffb8", "\uffb9", "\uffba", "\uffbb", "\uffbc", "\uffbd", "\uffc3", "\uffc4", "\uffc5", "\uffc6", "\uffcb", "\uffcc", "\uffcd", "\uffce", "\uffd3", "\uffd4", "\uffd5", "\uffd6", "\uffdb", "\u02b0", "\u02b1", "\u02b2", "\u02b3", "\u02b4", "\u02b5", "\u02b6", "\u02b7", "\u02b8", "\u02b9", "\u02ba", "\u02bb", "\u02bd", "\u02c0", "\u02c2", "\u02c3", "\u02c4", "\u02c5", "\u02c8", "\u02cc", "\u02ce", "\u02cf", "\u0375", "\u0380", "\u0381", "\u0382", "\u0383", "\u038b", "\u038d", "\u03a2", "\u0482", "\u0488", "\u0524", "\u0525", "\u0526", "\u0527", "\u0530", "\u0557", "\u0558", "\u055f", "\u0560", "\u0600", "\u0601", "\u0602", "\u0603", "\u0604", "\u0605", "\u0606", "\u0607", "\u0608", "\u0609", "\u060a", "\u060b", "\u060d", "\u060e", "\u060f", "\u061c", "\u061d", "\u061e", "\u066b", "\u066c", "\u066d", "\u06d4", "\u06de", "\u06e9", "\u06fd", "\u06fe", "\u0700", "\u0701", "\u0702", "\u0703", "\u0704", "\u0705", "\u0706", "\u0707", "\u0708", "\u0709", "\u070a", "\u070b", "\u070c", "\u070d", "\u070e", "\u070f", "\u074b", "\u074c", "\u082e", "\u082f", "\u0830", "\u0831", "\u0832", "\u0833", "\u0834", "\u0835", "\u0837", "\u0838", "\u083c", "\u083f", "\u086b", "\u086c", "\u086d", "\u086e", "\u086f", "\u0870", "\u0871", "\u0872", "\u0873", "\u0874", "\u0875", "\u0876", "\u0880", "\u0881", "\u0882", "\u0883", "\u0884", "\u0885", "\u0886", "\u0887", "\u0888", "\u0889", "\u088a", "\u088b", "\u088c", "\u088d", "\u088e", "\u088f", "\u0890", "\u0891", "\u0892", "\u0893", "\u0894", "\u0895", "\u0896", "\u0897", "\u0898", "\u0899", "\u089a", "\u089b", "\u089c", "\u089d", "\u089e", "\u08e2", "\u0984", "\u098d", "\u098e", "\u0991", "\u0992", "\u09a9", "\u09b1", "\u09b3", "\u09b4", "\u09b5", "\u0a00", "\u0a11", "\u0a12", "\u0a29", "\u0a31", "\u0a60", "\u0a61", "\u0a62", "\u0a63", "\u0a64", "\u0a65", "\u0a76", "\u0a77", "\u0a78", "\u0a79", "\u0a7a", "\u0a7b", "\u0a7c", "\u0a80", "\u0a84", "\u0a8e", "\u0a92", "\u0ac6", "\u0aca", "\u0ace", "\u0acf", "\u0ad1", "\u0ad2", "\u0ad3", "\u0ad4", "\u0ad5", "\u0ad6", "\u0ad7", "\u0ad8", "\u0ad9", "\u0ada", "\u0adb", "\u0adc", "\u0add", "\u0ade", "\u0adf", "\u0ae4", "\u0b00", "\u0b04", "\u0b0d", "\u0b0e", "\u0b11", "\u0b12", "\u0b29", "\u0b31", "\u0b34", "\u0b45", "\u0b46", "\u0b49", "\u0b4a", "\u0b4e", "\u0b4f", "\u0b50", "\u0b51", "\u0b52", "\u0b53", "\u0b54", "\u0b55", "\u0b64", "\u0b65", "\u0b6b", "\u0b6d", "\u0b70", "\u0b72", "\u0b80", "\u0b81", "\u0b84", "\u0b8b", "\u0b8c", "\u0b8d", "\u0b91", "\u0c04", "\u0c0d", "\u0c11", "\u0c29", "\u0c3a", "\u0c3b", "\u0c3c", "\u0c45", "\u1090", "\u1091", "\u1092", "\u1093", "\u1094", "\u1095", "\u1096", "\u1097", "\u1098", "\u1099", "\u109e", "\u109f", "\u128f", "\u12b1", "\u12b6", "\u12b7", "\u12bf", "\u12c1", "\u12c6", "\u12c7", "\u12d7", "\u1316", "\u1317", "\u1360", "\u1361", "\u1400", "\u169b", "\u169c", "\u169d", "\u169e", "\u169f", "\u170d", "\u1715", "\u1716", "\u1717", "\u1718", "\u1719", "\u18ff", "\u1a1c", "\u1a1d", "\u1a1e", "\u1a1f", "\u1a5f", "\u1a7d", "\u1a7e", "\u1a80", "\u1a81", "\u1a82", "\u1a83", "\u1a86", "\u1a87", "\u1a88", "\u1ac0", "\u1ac1", "\u1ac2", "\u1ac3", "\u1ac4", "\u1ac5", "\u1ac6", "\u1ac7", "\u1ac8", "\u1ac9", "\u1aca", "\u1acb", "\u1acc", "\u1acd", "\u1ace", "\u1acf", "\u1ad0", "\u1ad1", "\u1ad2", "\u1ad3", "\u1ad4", "\u1ad5", "\u1ad6", "\u1ad7", "\u1ad8", "\u1ad9", "\u1ada", "\u1adb", "\u1adc", "\u1add", "\u1ade", "\u1adf", "\u1ae0", "\u1ae1", "\u1ae2", "\u1ae3", "\u1ae4", "\u1ae5", "\u1ae6", "\u1ae7", "\u1ae8", "\u1ae9", "\u1aea", "\u1aeb", "\u1aec", "\u1aed", "\u1aee", "\u1aef", "\u1af0", "\u1af1", "\u1af2", "\u1af3", "\u1af4", "\u1af5", "\u1af6", "\u1af7", "\u1af8", "\u1c78", "\u1c79", "\u1c7a", "\u1c7b", "\u1c7c", "\u1c7e", "\u1c7f", "\u1c80", "\u1c81", "\u1c82", "\u1c83", "\u1c84", "\u1c85", "\u1c86", "\u1c87", "\u1c88", "\u1c89", "\u1c8a", "\u1c8b", "\u1c8c", "\u1c8d", "\u1c8e", "\u1c8f", "\u1d2c", "\u1d2d", "\u1d2e", "\u1d2f", "\u1d30", "\u1d46", "\u2011", "\u2012", "\u201b", "\u201f", "\u2023", "\u2024", "\u202b", "\u202d", "\u202e", "\u2036", "\u2037", "\u2038", "\u203c", "\u203d", "\u2042", "\u2045", "\u2046", "\u2047", "\u2048", "\u2049", "\u204a", "\u204b", "\u204c", "\u204d", "\u204e", "\u2050", "\u2051", "\u2052", "\u2053", "\u2055", "\u2056", "\u2058", "\u2059", "\u205a", "\u205b", "\u205c", "\u205d", "\u205e", "\u2064", "\u2065", "\u2066", "\u2067", "\u2068", "\u2069", "\u206a", "\u206b", "\u206c", "\u206d", "\u206e", "\u206f", "\u2072", "\u2073", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079", "\u207a", "\u207b", "\u207c", "\u207d", "\u207e", "\u2080", "\u2085", "\u2086", "\u2087", "\u2088", "\u2089", "\u208a", "\u208b", "\u208c", "\u208d", "\u208e", "\u208f", "\u2091", "\u2092", "\u2093", "\u2094", "\u2095", "\u2096", "\u2097", "\u2098", "\u2099", "\u209a", "\u209b", "\u209d", "\u209e", "\u209f", "\u20a0", "\u20a1", "\u20a2", "\u20a3", "\u20a5", "\u20a6", "\u20a8", "\u20ae", "\u20b0", "\u20b1", "\u20b2", "\u20b3", "\u20b4", "\u20b5", "\u20b6", "\u20b7", "\u20b8", "\u20b9", "\u20ba", "\u20bb", "\u20bc", "\u20be", "\u20bf", "\u20c0", "\u20c1", "\u20c2", "\u20c3", "\u20c4", "\u20c5", "\u20c6", "\u20c7", "\u20c8", "\u20c9", "\u20ca", "\u20cb", "\u20cc", "\u20cd", "\u20ce", "\u20cf", "\u20dd", "\u20de", "\u20df", "\u20e0", "\u20e2", "\u20e3", "\u20e4", "\u20f1", "\u20f2", "\u20f3", "\u20f4", "\u20f5", "\u20f6", "\u20f7", "\u20f8", "\u20f9", "\u20fa", "\u20fb", "\u20fc", "\u20fd", "\u20fe", "\u20ff", "\u2100", "\u2101", "\u2104", "\u2106", "\u2108", "\u2114", "\u211f", "\u2120", "\u2123", "\u2125", "\u212e", "\u213a", "\u213b", "\u2140", "\u2141", "\u2142", "\u2143", "\u2144", "\u214a", "\u214b", "\u214c", "\u214d", "\u214f", "\u2150", "\u2151", "\u2152", "\u215f", "\u2180", "\u2181", "\u2182", "\u2185", "\u2186", "\u2187", "\u2189", "\u218a", "\u218b", "\u218c", "\u218d", "\u218e", "\u219c", "\u21a8", "\u21af", "\u21b4", "\u21dc", "\u21de", "\u21df", "\u21e0", "\u21e1", "\u21e2", "\u21e3", "\u21e6", "\u21e8", "\u21e9", "\u21ea", "\u21eb", "\u21ec", "\u21ed", "\u21ee", "\u21ef", "\u21f0", "\u21f1", "\u21f2", "\u21f3", "\u21f4", "\u21f6", "\u21f7", "\u21f8", "\u21f9", "\u21fa", "\u21fb", "\u21fc", "\u220a", "\u220d", "\u220e", "\u221b", "\u221c", "\u2239", "\u2258", "\u225b", "\u225d", "\u225e", "\u2263", "\u228c", "\u229c", "\u22a6", "\u22b1", "\u22bc", "\u22dc", "\u22dd", "\u22e4", "\u22e5", "\u22f8", "\u22ff", "\u2300", "\u2301", "\u2307", "\u2311", "\u2314", "\u2317", "\u2319", "\u231a", "\u2324", "\u2326", "\u2327", "\u2328", "\u232b", "\u232c", "\u232f", "\u2330", "\u2331", "\u2332", "\u2333", "\u2334", "\u2335", "\u2338", "\u233a", "\u233b", "\u233c", "\u233e", "\u2341", "\u2342", "\u2343", "\u2344", "\u2345", "\u2346", "\u2347", "\u2348", "\u234a", "\u234c", "\u234d", "\u234f", "\u2350", "\u2351", "\u2353", "\u2354", "\u2356", "\u2357", "\u2358", "\u2359", "\u235a", "\u235b", "\u235c", "\u235e", "\u2360", "\u2361", "\u2362", "\u2364", "\u2365", "\u2366", "\u2367", "\u2368", "\u2369", "\u236b", "\u236d", "\u236e", "\u236f", "\u2370", "\u2375", "\u2376", "\u2378", "\u2379", "\u237a", "\u237b", "\u237d", "\u237e", "\u237f", "\u2380", "\u2382", "\u2383", "\u2384", "\u2385", "\u2386", "\u2387", "\u2388", "\u2389", "\u238a", "\u238b", "\u238d", "\u238e", "\u238f", "\u2390", "\u2391", "\u2392", "\u2393", "\u2394", "\u2395", "\u2396", "\u2397", "\u2398", "\u2480", "\u2481", "\u2482", "\u2483", "\u2484", "\u2485", "\u2486", "\u2487", "\u2489", "\u248a", "\u248b", "\u248c", "\u248d", "\u248e", "\u248f", "\u2490", "\u2491", "\u2492", "\u2493", "\u2494", "\u2495", "\u2496", "\u2497", "\u2498", "\u2499", "\u249a", "\u249b", "\u249d", "\u249e", "\u249f", "\u24a0", "\u24a1", "\u24a2", "\u24a3", "\u24a4", "\u24a5", "\u24a6", "\u24a7", "\u24a8", "\u24a9", "\u24aa", "\u24ab", "\u24ac", "\u24ad", "\u24ae", "\u24af", "\u24b0", "\u24b1", "\u24b2", "\u24b3", "\u24b4", "\u24b5", "\u24ea", "\u24eb", "\u24ec", "\u24ed", "\u24ee", "\u24ef", "\u24f0", "\u24f1", "\u24f2", "\u24f3", "\u24f4", "\u24f5", "\u24f6", "\u24f7", "\u24f8", "\u24f9", "\u24fa", "\u24fb", "\u24fc", "\u24fd", "\u24fe", "\u24ff", "\u2504", "\u2505", "\u2506", "\u2507", "\u2508", "\u2509", "\u250a", "\u250b", "\u3004", "\u3018", "\u3019", "\u301a", "\u301b", "\u301c", "\u3020", "\u3022", "\u3023", "\u3024", "\u3025", "\u3026", "\u3027", "\u3028", "\u3030", "\u3032", "\u3033", "\u3034", "\u3036", "\u3037", "\u3039", "\u303a", "\u303d", "\u303f", "\u3040", "\u3097", "\u3098", "\u30a0", "\u3100", "\u3101", "\u3102", "\u3103", "\u3104", "\u312f", "\u3130", "\u318f", "\u3190", "\u3191", "\u3192", "\u3193", "\u3194", "\u3195", "\u3196", "\u3197", "\u3198", "\u3199", "\u319a", "\u319b", "\u319c", "\u319d", "\u319e", "\u319f", "\u31bb", "\u31bc", "\u31bd", "\u31be", "\u31bf", "\u31c1", "\u31c2", "\u31c3", "\u31c4", "\u31d0", "\u31d1", "\u31d2", "\u31d3", "\u31d4", "\u31d5", "\u31d6", "\u31d7", "\u31d8", "\u31d9", "\u31da", "\u31db", "\u31dc", "\u31dd", "\u31de", "\u31df", "\u31e0", "\u31e1", "\u31e2", "\u31e3", "\u31e4", "\u31e5", "\u31e6", "\u31e7", "\u31e8", "\u31e9", "\u31ea", "\u31eb", "\u31ec", "\u31ed", "\u31ee", "\u31ef", "\u3201", "\u3202", "\u3203", "\u3204", "\u3205", "\u3206", "\u3207", "\u3208", "\u3209", "\u320a", "\u320b", "\u320c", "\u320d", "\u320e", "\u320f", "\u3210", "\u3211", "\u3212", "\u3213", "\u3214", "\u3215", "\u3216", "\u3217", "\u3218", "\u3219", "\u321a", "\u321b", "\u321d", "\u321e", "\u321f", "\u3221", "\u3222", "\u3223", "\u3224", "\u3225", "\u3226", "\u3227", "\u3228", "\u3229", "\u322a", "\u322b", "\u322c", "\u322d", "\u322e", "\u322f", "\u3230", "\u3233", "\u3234", "\u3235", "\u3236", "\u3237", "\u3238", "\u323a", "\u323b", "\u323c", "\u323d", "\u323e", "\u323f", "\u3240", "\u3241", "\u3242", "\u3243", "\u3244", "\u3245", "\u3246", "\u3247", "\u3248", "\u3249", "\u324a", "\u324b", "\u324c", "\u324d", "\u324e", "\u324f", "\u3250", "\u3251", "\u3252", "\u3253", "\u3254", "\u3255", "\u3256", "\u3257", "\u3258", "\u3259", "\u325a", "\u325b", "\u325c", "\u325d", "\u325e", "\u325f", "\u3261", "\u3262", "\u3263", "\u3264", "\u3265", "\u3266", "\u3267", "\u3268", "\u3269", "\u326a", "\u326b", "\u326c", "\u326d", "\u326e", "\u326f", "\u3270", "\u3271", "\u3272", "\u3273", "\u3274", "\u3275", "\u3276", "\u3277", "\u3278", "\u3279", "\u327a", "\u327b", "\u327c", "\u327d", "\u327e", "\u3280", "\u3281", "\u3282", "\u3283", "\u3284", "\u3285", "\u3286", "\u3287", "\u3288", "\u3289", "\u328a", "\u328b", "\u328c", "\u328d", "\u328e", "\u328f", "\u3290", "\u3291", "\u3292", "\u3293", "\u3294", "\u3295", "\u3296", "\u3297", "\u3298", "\u3299", "\u329a", "\u329b", "\u329c", "\u329d", "\u329e", "\u329f", "\u32a0", "\u32a1", "\u32a2", "\u32a5", "\u32a6", "\u32a7", "\u32a8", "\u32a9", "\u32aa", "\u32ab", "\u32ac", "\u32ad", "\u32ae", "\u32af", "\u32b0", "\u32b1", "\u32b2", "\u32b3", "\u32b4", "\u32b5", "\u32b6", "\u32b7", "\u32b8", "\u32b9", "\u32ba", "\u32bb", "\u32bc", "\u32bd", "\u32be", "\u32bf", "\u32c0", "\u32c1", "\u32c2", "\u32c3", "\u32c4", "\u32c5", "\u32c6", "\u32c7", "\u32c8", "\u32c9", "\u32ca", "\u32cb", "\u32cc", "\u32cd", "\u32ce", "\u32cf", "\u32d0", "\u32d1", "\u32d2", "\u32d3", "\u32d4", "\u32d5", "\u32d6", "\u32d7", "\u32d8", "\u32d9", "\u32da", "\u32db", "\u32dc", "\u32dd", "\u32de", "\u32df", "\u32e0", "\u32e1", "\u32e2", "\u32e3", "\u32e4", "\u32e5", "\u32e6", "\u32e7", "\u32e8", "\u32e9", "\u32ea", "\u32eb", "\u32ec", "\u32ed", "\u32ee", "\u32ef", "\u32f0", "\u32f1", "\u32f2", "\u32f3", "\u32f4", "\u32f5", "\u32f6", "\u32f7", "\u32f8", "\u32f9", "\u32fa", "\u32fb", "\u32fc", "\u32fd", "\u32fe", "\u32ff", "\u3300", "\u3301", "\u3302", "\u3304", "\u3305", "\u3306", "\u3307", "\u3308", "\u3309", "\u330a", "\u330b", "\u330c", "\u330e", "\u330f", "\u3310", "\u3311", "\u3312", "\u3313", "\u3315", "\u3316", "\u3317", "\u3319", "\u331a", "\u331b", "\u331c", "\u331d", "\u331e", "\u331f", "\u3320", "\u3321", "\u3324", "\u3325", "\u3328", "\u3329", "\u332a", "\u332c", "\u332d", "\u332e", "\u332f", "\u3330", "\u3331", "\u3332", "\u3333", "\u3334", "\u3335", "\u3337", "\u3338", "\u3339", "\u333a", "\u333c", "\u333d", "\u333e", "\u333f", "\u3340", "\u3341", "\u3342", "\u3343", "\u3344", "\u3345", "\u3346", "\u3347", "\u3348", "\u334b", "\u334c", "\u334e", "\u334f", "\u3350", "\u3352", "\u3353", "\u3354", "\u3355", "\u3356", "\u3358", "\u3359", "\u335a", "\u335b", "\u335c", "\u335d", "\u335e", "\u335f", "\u3360", "\u3361", "\u3362", "\u3363", "\u3364", "\u3365", "\u3366", "\u3367", "\u3368", "\u3369", "\u336a", "\u336b", "\u336c", "\u336d", "\u336e", "\u336f", "\u3370", "\u3371", "\u3372", "\u3373", "\u3374", "\u3375", "\u3376", "\u3377", "\u3378", "\u3379", "\u337a", "\u337f", "\u3381", "\u3382", "\u3383", "\u3384", "\u3385", "\u3386", "\u3387", "\u3391", "\u3392", "\u3393", "\u3394", "\u339a", "\u339b", "\u339f", "\u33a0", "\u33a2", "\u33b1", "\u33b2", "\u33b3", "\u33b4", "\u33b5", "\u33b6", "\u33b7", "\u33b8", "\u33b9", "\u33bb", "\u33bc", "\u33bd", "\u33be", "\u33bf", "\u33cb", "\u33cc", "\u33d4", "\u33d7", "\u33d9", "\u33da", "\u33de", "\u33df", "\u33e0", "\u33e1", "\u33e2", "\u33e3", "\u33e4", "\u33e5", "\u33e6", "\u33e7", "\u33e8", "\u33e9", "\u33ea", "\u33eb", "\u33ec", "\u33ed", "\u33ee", "\u33ef", "\u33f0", "\u33f1", "\u33f2", "\u33f3", "\u33f4", "\u33f5", "\u33f6", "\u33f7", "\u33f8", "\u33f9", "\u33fa", "\u33fb", "\u33fc", "\u33fd", "\u33fe", "\u33ff", "\u3401", "\u3402", "\u3403", "\u3404", "\u3405", "\u3406", "\u3407", "\u3408", "\u3409", "\u340a", "\u340b", "\u340c", "\u340d", "\u340e", "\u340f", "\u3410", "\u3411", "\u3412", "\u3413", "\u3414", "\u3415", "\u3416", "\u3417", "\u3418", "\u3419", "\u341a", "\u341b", "\u341c", "\u341d", "\u341e", "\u341f", "\u3420", "\u3421", "\u3422", "\u3423", "\u3424", "\u3425", "\u3426", "\u3427", "\u3428", "\u3429", "\u342a", "\u342b", "\u342c", "\u342d", "\u342e", "\u4400", "\u4403", "\u4404", "\u4405", "\u4406", "\u4407", "\u4408", "\u4409", "\u440a", "\u440b", "\u440c", "\u440d", "\u440e", "\u440f", "\u4410", "\u4411", "\u4412", "\u4414", "\u4415", "\u4416", "\u4417", "\u4418", "\u4419", "\u441a", "\u441b", "\u441c", "\u441d", "\u441e", "\u441f", "\u4420", "\u4421", "\u4422", "\u4423", "\u4424", "\u4426", "\u4427", "\u4428", "\u4429", "\u442a", "\u442b", "\u442c", "\u442e", "\u442f", "\u4430", "\u4431", "\u4432", "\u4433", "\u4434", "\u4435", "\u4436", "\u4437", "\u4438", "\u4439", "\u443a", "\u443b", "\u443c", "\u443d", "\u443e", "\u443f", "\u4440", "\u4441", "\u4442", "\u4443", "\u4444", "\u4445", "\u4446", "\u4447", "\u4448", "\u4449", "\u444a", "\u444b", "\u444c", "\u444d", "\u444e", "\u444f", "\u4450", "\u4451", "\u4452", "\u4453", "\u4454", "\u4455", "\u4456", "\u4457", "\u4458", "\u4459", "\u445a", "\u445b", "\u445c", "\u445d", "\u445e", "\u445f", "\u4460", "\u4461", "\u4462", "\u4463", "\u4464", "\u4465", "\u4466", "\u4467", "\u4468", "\u4469", "\u446a", "\u446b", "\u446c", "\u446d", "\u446e", "\u446f", "\u4470", "\u4471", "\u4472", "\u4473", "\u4474", "\u4475", "\u4476", "\u4477", "\u4478", "\u4479", "\u447b", "\u447c", "\u447d", "\u447e", "\u447f", "\u4480", "\u4481", "\u4482", "\u4483", "\u4484", "\u4485", "\u4486", "\u4487", "\u4488", "\u4489", "\u448a", "\u448b", "\u448c", "\u448d", "\u448e", "\u4490", "\u4492", "\u4493", "\u4494", "\u4495", "\u4496", "\u4497", "\u4498", "\u4499", "\u449a", "\u449b", "\u449c", "\u449d", "\u449e", "\u44a1", "\u44a3", "\u44a4", "\u44a5", "\u44a6", "\u44a7", "\u44a8", "\u44a9", "\u44aa", "\u44ab", "\u44ac", "\u44ad", "\u44ae", "\u44af", "\u44b1", "\u44b2", "\u44b3", "\u44b4", "\u44b5", "\u44b6", "\u44b8", "\u44b9", "\u44ba", "\u44bb", "\u44bc", "\u44be", "\u44bf", "\u44c1", "\u44c2", "\u44c4", "\u44c6", "\u44c7", "\u44c8", "\u44c9", "\u44ca", "\u44cb", "\u44cc", "\u44cd", "\u44cf", "\u44d0", "\u44d1", "\u44d2", "\u44d3", "\u44d4", "\u44d5", "\u44d7", "\u44d8", "\u44d9", "\u44da", "\u44db", "\u44dc", "\u44e0", "\u44e2", "\u44e3", "\u44e5", "\u44e6", "\u44e7", "\u44e8", "\u44ed", "\u44ee", "\u44ef", "\u44f0", "\u44f1", "\u44f2", "\u44f3", "\u44f5", "\u44f6", "\u44f7", "\u44f8", "\u44f9", "\u44fa", "\u44fb", "\u44fc", "\u44fd", "\u44fe", "\u44ff", "\u4500", "\u4501", "\u4502", "\u4505", "\u4506", "\u4507", "\u4508", "\u450a", "\u450c", "\u450d", "\u450e", "\u450f", "\u4510", "\u4511", "\u4512", "\u4513", "\u4514", "\u4515", "\u4517", "\u4518", "\u4519", "\u451a", "\u451c", "\u451e", "\u451f", "\u4520", "\u4521", "\u4522", "\u4523", "\u4524", "\u4525", "\u4526", "\u4528", "\u4529", "\u452a", "\u452b", "\u452c", "\u452d", "\u452f", "\u4530", "\u4531", "\u4532", "\u4534", "\u4535", "\u4537", "\u4538", "\u4539", "\u453a", "\u453c", "\u453e", "\u4540", "\u4541", "\u4542", "\u4544", "\u4545", "\u4546", "\u4547", "\u4548", "\u4549", "\u454a", "\u454b", "\u454c", "\u454d", "\u454e", "\u454f", "\u4550", "\u4553", "\u4554", "\u4556", "\u4557", "\u4559", "\u455a", "\u455b", "\u455d", "\u455e", "\u455f", "\u4560", "\u4563", "\u4564", "\u4565", "\u4566", "\u4567", "\u4568", "\u4569", "\u456b", "\u456c", "\u456e", "\u456f", "\u4570", "\u4571", "\u4572", "\u4573", "\u4574", "\u4575", "\u4576", "\u4579", "\u457a", "\u457b", "\u457c", "\u457d", "\u457e", "\u457f", "\u4580", "\u4581", "\u4582", "\u4583", "\u4584", "\u4586", "\u4587", "\u4588", "\u4589", "\u458a", "\u458b", "\u458c", "\u458d", "\u458e", "\u458f", "\u4590", "\u4591", "\u4592", "\u4593", "\u4594", "\u4595", "\u4596", "\u4597", "\u4598", "\u4599", "\u459a", "\u459b", "\u459c", "\u459d", "\u459e", "\u459f", "\u45a0", "\u45a1", "\u45a2", "\u45a3", "\u45a4", "\u45a5", "\u45a7", "\u45a8", "\u45a9", "\u45aa", "\u45ab", "\u45ac", "\u45ad", "\u45ae", "\u45af", "\u45b0", "\u45b1", "\u45b2", "\u45b4", "\u45b5", "\u45b6", "\u45b7", "\u45b8", "\u45b9", "\u45ba", "\u45bb", "\u45bc", "\u45bd", "\u45be", "\u45bf", "\u45c0", "\u45c1", "\u45c2", "\u45c3", "\u45c4", "\u45c5", "\u45c6", "\u45c7", "\u45c8", "\u45c9", "\u45ca", "\u45cb", "\u45cc", "\u45cd", "\u45ce", "\u45cf", "\u45d0", "\u45d1", "\u45d2", "\u45d3", "\u45d4", "\u45d5", "\u45d6", "\u45d7", "\u45d8", "\u45d9", "\u45db", "\u45dc", "\u45dd", "\u45de", "\u45df", "\u45e0", "\u45e1", "\u45e2", "\u45e3", "\u45e4", "\u45e5", "\u45e6", "\u45e7", "\u45e8", "\u45eb", "\u45ec", "\u45ed", "\u45ee", "\u45ef", "\u45f0", "\u45f1", "\u45f2", "\u45f3", "\u45f4", "\u45f5", "\u45f6", "\u45f7", "\u45f8", "\u45f9", "\u45fa", "\u45fb", "\u45fc", "\u45fd", "\u45fe", "\u45ff", "\u4600", "\u4601", "\u4602", "\u4604", "\u4605", "\u4607", "\u4608", "\u4609", "\u460a", "\u460b", "\u460c", "\u460d", "\u460e", "\u4610", "\u4611", "\u4612", "\u4613", "\u4614", "\u4616", "\u4618", "\u4619", "\u461a", "\u461b", "\u461c", "\u461d", "\u461e", "\u461f", "\u4620", "\u4621", "\u4622", "\u4623", "\u4624", "\u4625", "\u4626", "\u4627", "\u4628", "\u4629", "\u462a", "\u462b", "\u462c", "\u462d", "\u462e", "\u462f", "\u4630", "\u4631", "\u4632", "\u4633", "\u4634", "\u4635", "\u4636", "\u4637", "\u4638", "\u4639", "\u463a", "\u463b", "\u463c", "\u463d", "\u463e", "\u463f", "\u4640", "\u4641", "\u4642", "\u4643", "\u4644", "\u4645", "\u4646", "\u6823", "\u6824", "\u685a", "\u6870", "\u6873", "\u688e", "\u6899", "\u689e", "\u68be", "\u68bf", "\u691d", "\u691e", "\u6929", "\u692b", "\u6947", "\u694d", "\u6950", "\u698f", "\u69da", "\u69e3", "\u6a0e", "\u6a10", "\u6a42", "\u6ad2", "\u6ad7", "\u6ae3", "\u6ae6", "\u6ae9", "\u6aed", "\u6b01", "\u6b0d", "\u6b0e", "\u6b14", "\u6b15", "\u6b1c", "\u6b29", "\u6b2a", "\u6b2e", "\u6b6c", "\u6b71", "\u6f1d", "\u8834", "\u8847", "\u8850", "\u88a6", "\u88a9", "\u88b3", "\u88ea", "\u88ed", "\u8908", "\u893f", "\u8948", "\u894a", "\u894e", "\u8955", "\u8968", "\u8978", "\u898c", "\u898e", "\u8992", "\u8999", "\u89a8", "\u89ab", "\u89b1", "\u89b8", "\u89bb", "\u89f5", "\u8a06", "\u8a09", "\u8a0b", "\u8a0d", "\u8a19", "\u8a1a", "\u8a21", "\u8a28", "\u8a2e", "\u8a32", "\u8a42", "\u8a4b", "\u8a5a", "\u8a64", "\u8a6a", "\u8a6f", "\u8a78", "\u8a7d", "\u8a88", "\u8a8e", "\u8a9b", "\u8a9d", "\u8aa2", "\u8ab1", "\u8ab5", "\u8ac1", "\u8ace", "\u8ad0", "\u8ae3", "\u8ae5", "\u8ae9", "\ub006", "\ub007", "\ub008", "\ub009", "\ub00a", "\ub00b", "\ub016", "\ub017", "\ub018", "\ub019", "\ub01a", "\ub01b", "\ub01f", "\ub020", "\ub021", "\ub022", "\ub023", "\ub024", "\ub025", "\ub026", "\ub027", "\ub02a", "\ub02b", "\ub02c", "\ub02d", "\ub02e", "\ub02f", "\ub030", "\ub031", "\ub032", "\ub033", "\ub034", "\ub035", "\ub036", "\ub037", "\ub038", "\ub039", "\ub03a", "\ub03b", "\ub03c", "\ub03d", "\ub03e", "\ub03f", "\ub040", "\ub041", "\ub042", "\ub043", "\ub05f", "\ub060", "\ub061", "\ub062", "\ub063", "\ub064", "\ub065", "\ub066", "\ub067", "\ub068", "\ub069", "\ub06a", "\ub06b", "\ub06c", "\ub06d", "\ub06e", "\ub06f", "\ub070", "\ub071", "\ub072", "\ub073", "\ub074", "\ub075", "\ub076", "\ub077", "\ub078", "\ub079", "\ub07a", "\ub07b", "\ub086", "\ub087", "\ub088", "\ub089", "\ub08a", "\ub08b", "\ub093", "\ub094", "\ub095", "\ub096", "\ub097", "\ub0ad", "\ub0ae", "\ub0af", "\ub0be", "\ub0bf", "\ub0c0", "\ub0c1", "\ub0c2", "\ub0c3", "\ub0cb", "\ub0cc", "\ub0cd", "\ub0ce", "\ub0cf", "\ub0da", "\ub0db", "\ub0dc", "\ub0dd", "\ub0de", "\ub0df", "\ub0e7", "\ub0e8", "\ub0e9", "\ub0ea", "\ub0eb", "\ub0ec", "\ub0ed", "\ub0ee", "\ub0ef", "\ub0f0", "\ub0f2", "\ub0f3", "\ub0f4", "\ub0f5", "\ub0f6", "\ub0f7", "\ub0f8", "\ub0f9", "\ub0fa", "\ub0fb", "\ub0fc", "\ub0fd", "\ub0fe", "\ub0ff", "\ub100", "\ub101", "\ub102", "\ub103", "\ub104", "\ub105", "\ub106", "\ub107", "\ub170", "\ub171", "\ub172", "\ub173", "\ub174", "\ub175", "\ub176", "\ub177", "\ub184", "\ub185", "\ub186", "\ub187", "\ub19f", "\ub1a0", "\ub1a1", "\ub1a2", "\ub1a3", "\ub1a4", "\ub1a5", "\ub1a6", "\ub1a7", "\ub1aa", "\ub1ab", "\ub1ac", "\ub1ad", "\ub1ae", "\ub1af", "\ub1b0", "\ub1b1", "\ub1b2", "\ub1b3", "\ub1b4", "\ub1b5", "\ub1b6", "\ub1b7", "\ub1b8", "\ub1ba", "\ub1bb", "\ub1bc", "\ub1bd", "\ub1be", "\ub1bf", "\ub1c0", "\ub1c1", "\ub1c2", "\ub1c3", "\ub1c4", "\ub1c5", "\ub1c6", "\ub1c7", "\ub1c8", "\ub1c9", "\ub1ca", "\ub1cb", "\ub1d7", "\ub1d8", "\ub1d9", "\ub1da", "\ub1db", "\ub1e1", "\ub1e2", "\ub1e3", "\ub1e4", "\ub1e5", "\ub1e6", "\ub1e7", "\ub1f2", "\ub1f3", "\ub1f4", "\ub1f5", "\ub1f6", "\ub1f7", "\ub1f8", "\ub1ff", "\ub200", "\ub201", "\ub202", "\ub203", "\ub20e", "\ub20f", "\ub210", "\ub211", "\ub212", "\ub213", "\ub21b", "\ub21c", "\ub21d", "\ub21e", "\ub21f", "\ub222", "\ub223", "\ub224", "\ub225", "\ub226", "\ub227", "\ub228", "\ub229", "\ub22a", "\ub22b", "\ub22c", "\ub22d", "\ub22e", "\ub22f", "\ub230", "\ub231", "\ub232", "\ub233", "\ub236", "\ub237", "\ub238", "\ub239", "\ub23a", "\ub23b", "\ub23e", "\ub23f", "\ub240", "\ub241", "\ub242", "\ub243", "\ub244", "\ub245", "\ub246", "\ub247", "\ub248", "\ub249", "\ub24a", "\ub24b", "\ub24c", "\ub24d", "\ub24e", "\ub24f", "\ub250", "\ub251", "\ub252", "\ub253", "\ub254", "\ub255", "\ub256", "\ub257", "\ub262", "\ub263", "\ub264", "\ub265", "\ub266", "\ub267", "\ub26b", "\ub26c", "\ub26d", "\ub26e", "\ub270", "\ub271", "\ub272", "\ub273", "\ub277", "\ub278", "\ub279", "\ub27a", "\ub27b", "\ub27e", "\ub27f", "\ub280", "\ub281", "\ub282", "\ub283", "\ub28b", "\ub28c", "\ub28d", "\ub28e", "\ub29c", "\ub29d", "\ub29e", "\ub29f", "\ub2b9", "\ub2ba", "\ub2bb", "\ub2bc", "\ub2bd", "\ub2be", "\ub2bf", "\ub2c0", "\ub2c1", "\ub2c2", "\ub2c3", "\ub2c4", "\ub2c5", "\ub2c6", "\ub2c7", "\ub2d4", "\ub2d5", "\ub2d6", "\ub2d7", "\ub2ed", "\ub2ee", "\ub2ef", "\ub2f8", "\ub2fa", "\ub2fb", "\ubc04", "\ubc05", "\ubc06", "\ubc07", "\ubc15", "\ubc17", "\ubc1d", "\ubc1e", "\ubc1f", "\ubc3a", "\ubc3b", "\ubc3c", "\ubc3d", "\ubc3e", "\ubc3f", "\ubc52", "\ubc53", "\ubc54", "\ubc55", "\ubc56", "\ubc57", "\ubc58", "\ubc59", "\ubc5f", "\ubc60", "\ubc61", "\ubc62", "\ubc63", "\ubc64", "\ubc65", "\ubc66", "\ubc67", "\ubc68", "\ubc69", "\ubc6a", "\ubc70", "\ubc71", "\ubc72", "\ubc73", "\ubc74", "\ubc75", "\ubc76", "\ubc77", "\ubc78", "\ubc79", "\ubc7a", "\ubc7b", "\ubc7c", "\ubc80", "\ubc81", "\ubc82", "\ubc83", "\ubc90", "\ubc91", "\ubc92", "\ubc93", "\ue800", "\ue802", "\ue803", "\ue804", "\ue805", "\ue806", "\ue807", "\ue808", "\ue809", "\ue80a", "\ue80b", "\ue80c", "\ue80d", "\ue80e", "\ue80f", "\ue811", "\ue812", "\ue813", "\ue814", "\ue815", "\ue819", "\ue81a", "\ue81b", "\ue81c", "\ue81d", "\ue81f", "\ue820", "\ue821", "\ue822", "\ue823", "\ue824", "\ue825", "\ue827", "\ue828", "\ue829", "\ue82a", "\ue82d", "\ue82e", "\ue82f", "\ue830", "\ue833", "\ue834", "\ue835", "\ue836", "\ue837", "\ue838", "\ue839", "\ue83a", "\ue83c", "\ue83d", "\ue83e", "\ue83f", "\ue840", "\ue841", "\ue842", "\ue844", "\ue845", "\ue846", "\ue847", "\ue848", "\ue849", "\ue84a", "\ue84b", "\ue84c", "\ue84d", "\ue84e", "\ue84f", "\ue850", "\ue851", "\ue852", "\ue853", "\ue856", "\ue857", "\ue858", "\ue859", "\ue85a", "\ue85b", "\ue85c", "\ue85d", "\ue85e", "\ue85f", "\ue860", "\ue861", "\ue862", "\ue863", "\ue865", "\ue866", "\ue867", "\ue868", "\ue869", "\ue86a", "\ue86b", "\ue86c", "\ue86d", "\ue86e", "\ue86f", "\ue870", "\ue871", "\ue872", "\ue873", "\ue874", "\ue875", "\ue876", "\ue877", "\ue878", "\ue879", "\ue87a", "\ue87b", "\ue87c", "\ue87d", "\ue87e", "\ue87f", "\ue880", "\ue881", "\ue882", "\ue883", "\ue884", "\ue885", "\ue886", "\ue887", "\ue888", "\ue889", "\ue88a", "\ue88b", "\ue88c", "\ue88d", "\ue88e", "\ue88f", "\ue890", "\ue891", "\ue892", "\ue893", "\ue894", "\ue895", "\ue896", "\ue897", "\ue898", "\ue899", "\ue89a", "\ue89b", "\ue89c", "\ue89d", "\ue89e", "\ue89f", "\ue8a0", "\ue8a1", "\ue8a2", "\ue8a3", "\ue8a4", "\ue8a5", "\ue8a6", "\ue8a7", "\ue8a8", "\ue8a9", "\ue8aa", "\ue8ab", "\ue8ac", "\ue8ad", "\ue8ae", "\ue8af", "\ue8b0", "\ue8b1", "\ue8b2", "\ue8b3", "\ue8b4", "\ue8b5", "\ue8b6", "\ue8b7", "\ue8b8", "\ue8b9", "\ue8ba", "\ue8bb", "\ue8bc", "\ue8bd", "\ue8be", "\ue8bf", "\ue8c0", "\ue8c1", "\ue8c2", "\ue8c3", "\ue8c4", "\uee00", "\uee01", "\uee02", "\uee03", "\uee05", "\uee06", "\uee07", "\uee08", "\uee09", "\uee0a", "\uee0b", "\uee0c", "\uee0d", "\uee0e", "\uee0f", "\uee10", "\uee11", "\uee12", "\uee13", "\uee14", "\uee15", "\uee16", "\uee17", "\uee18", "\uee19", "\uee1a", "\uee1b", "\uee1c", "\uee1d", "\uee1e", "\uee1f", "\uee21", "\uee22", "\uee24", "\uee27", "\uee29", "\uee2a", "\uee2b", "\uee2c", "\uee2d", "\uee2e", "\uee2f", "\uee30", "\uee31", "\uee32", "\uee34", "\uee35", "\uee36", "\uee37", "\uee39", "\uee3b", "\uee42", "\uee47", "\uee49", "\uee4b", "\uee4d", "\uee4e", "\uee4f", "\uee51", "\uee52", "\uee54", "\uee57", "\uee59", "\uee5b", "\uee5d", "\uee5f", "\uee61", "\uee62", "\uee64", "\uee67", "\uee68", "\uee69", "\uee6a", "\uee6c", "\uee6d", "\uee6e", "\uee6f", "\uee70", "\uee71", "\uee72", "\uee74", "\uee75", "\uee76", "\uee77", "\uee79", "\uee7a", "\uee7b", "\uee7c", "\uee7e", "\uee80", "\uee81", "\uee82", "\uee83", "\uee84", "\uee85", "\uee86", "\uee87", "\uee88", "\uee89", "\uee8b", "\uee8c", "\uee8d", "\uee8e", "\uee8f", "\uee90", "\uee91", "\uee92", "\uee93", "\uee94", "\uee95", "\uee96", "\uee97", "\uee98", "\uee99", "\uee9a", "\uee9b", "\ueea1", "\ueea2", "\ueea3", "\ueea5", "\ueea6", "\ueea7", "\ueea8", "\ueea9", "\ueeab", "\ueeac", "\ueead", "\ueeae", "\ueeaf", "\ueeb0", "\ueeb1", "\ueeb2", "\ueeb3", "\ueeb4", "\ueeb5", "\ueeb6", "\ueeb7", "\ueeb8", "\ueeb9", "\ueeba", "\ueebb", "\ua700", "\ub734", "\ub740", "\ub820", "\uceb0", "\uebe0", "\uf800", "\uf801", "\uf802", "\uf803", "\uf804", "\uf805", "\uf806", "\uf807", "\uf808", "\uf809", "\uf80a", "\uf80b", "\uf80c", "\uf80d", "\uf80e", "\uf80f", "\uf810", "\uf811", "\uf812", "\uf813", "\uf814", "\uf815", "\uf816", "\uf817", "\uf818", "\uf819", "\uf81a", "\uf81b", "\uf81c", "\uf81d", "\uf81e", "\uf81f", "\uf820", "\uf821", "\uf822", "\uf823", "\uf824", "\uf825", "\uf826", "\uf827", "\uf828", "\uf829", "\uf82a", "\uf82b", "\uf82c", "\uf82d", "\uf82e", "\uf82f", "\uf830", "\uf831", "\uf832", "\uf833", "\uf834", "\uf835", "\uf836", "\uf837", "\uf838", "\uf839", "\uf83a", "\uf83b", "\uf83c", "\uf83d", "\uf83e", "\uf83f", "\uf840", "\uf841", "\uf842", "\uf843", "\uf844", "\uf845", "\uf846", "\uf847", "\uf848", "\uf849", "\uf84a", "\uf84b", "\uf84c", "\uf84d", "\uf84e", "\uf84f", "\uf850", "\uf851", "\uf852", "\uf853", "\uf854", "\uf855", "\uf856", "\uf857", "\uf858", "\uf859", "\uf85a", "\uf85b", "\uf85c", "\uf85d", "\uf85e", "\uf85f", "\uf860", "\uf861", "\uf862", "\uf863", "\uf864", "\uf865", "\uf866", "\uf867", "\uf868", "\uf869", "\uf86a", "\uf86b", "\uf86c", "\uf86d", "\uf86e", "\uf86f", "\uf870", "\uf871", "\uf872", "\uf873", "\uf874", "\uf875", "\uf876", "\uf877", "\uf878", "\uf879", "\uf87a", "\uf87b", "\uf87c", "\uf87d", "\uf87e", "\uf87f", "\uf880", "\uf881", "\uf882", "\uf883", "\uf89a", "\uf89b", "\uf89c", "\uf89d", "\uf89e", "\uf89f", "\uf8a0", "\uf8a1", "\uf8a2", "\uf8a3", "\uf8a4", "\uf8a5", "\uf8a6", "\uf8a7", "\uf8a8", "\uf8a9", "\uf8aa", "\uf8ab", "\uf8ac", "\uf8ad", "\uf8ae", "\uf8af", "\uf8b0", "\uf8b1", "\uf8b2", "\uf8b3", "\uf8b4", "\uf8b5", "\uf8b6", "\uf8b7", "\uf8b8", "\uf8b9", "\uf8ba", "\uf8bb", "\uf8bc", "\uf8bd", "\uf8be", "\uf8bf", "\uf8c0", "\uf8c1", "\uf8c2", "\uf8c3", "\uf8c4", "\uf8c5", "\uf8c6", "\uf8c7", "\uf8c8", "\uf8c9", "\uf8ca", "\uf8cb", "\uf8cc", "\uf8cd", "\uf8ce", "\uf8cf", "\uf8d0", "\uf8d1", "\uf8d2", "\uf8d3", "\uf8d4", "\uf8d5", "\uf8d6", "\uf8d7", "\uf8d8", "\uf8d9", "\uf8da", "\uf8db", "\uf8dc", "\uf8dd", "\uf8de", "\uf8df", "\uf8e0", "\uf8e1", "\uf8e2", "\uf8e3", "\uf8e4", "\uf8e5", "\uf8e6", "\uf8e7", "\uf8e8", "\uf8e9", "\uf8ea", "\uf8eb", "\uf8ec", "\uf8ed", "\uf8ee", "\uf8ef", "\uf8f0", "\uf8f1", "\uf8f2", "\uf8f3", "\uf8fd", "\uf8fe", "\u16ef", "\u16f0", "\ua6e6", "\ua6e7", "\ua6e8", "\ua6e9", "\ua6ea", "\ua6eb", "\ua6ec", "\ua6ed", "\ua6ee", "\u2401", "\u2402", "\u2403", "\u2404", "\u2405", "\u2406", "\u2407", "\u2408", "\u2409", "\u240a", "\u240b", "\u240c", "\u240e", "\u240f", "\u2410", "\u2411", "\u2412", "\u2413", "\u2414", "\u2415", "\u2416", "\u2417", "\u2418", "\u2419", "\u241a", "\u241b", "\u241c", "\u241d", "\u241e", "\u241f", "\u2420", "\u2422", "\u2425", "\u2426", "\u2427", "\u2428", "\u2429", "\u242a", "\u242b", "\u242c", "\u242d", "\u242e", "\u242f", "\u2430", "\u2431", "\u2432", "\u2433", "\u2434", "\u2435", "\u2436", "\u2437", "\u2438", "\u2439", "\u243a", "\u243b", "\u243c", "\u243d", "\u243e", "\u243f", "\u2440", "\u2441", "\u2442", "\u2443", "\u2444", "\u2445", "\u2446", "\u2447", "\u2448", "\u2449", "\u244a", "\u244b", "\u244c", "\u244d", "\u244e", "\u244f", "\u2450", "\u2451", "\u2452", "\u2453", "\u2454", "\u2455", "\u2456", "\u2457", "\u2458", "\u2459", "\u245a", "\u245b", "\u245c", "\u245d", "\u245e", "\u245f", "\u2461", "\u2462", "\u2463", "\u2464", "\u2465", "\u2466", "\u2467", "\u2468", "\u2469", "\u246a", "\u246b", "\u246c", "\u246d", "\u246e", "\u02e1", "\u02e2", "\u02e3", "\u1843", "\u1d37", "\u1d38", "\u1d39", "\u1d3b", "\u1d3e", "\u1d48", "\u1d49", "\u1d4a", "\u1d4b", "\u1d4c", "\u1d4d", "\u1d4e", "\u1d4f", "\u1d50", "\u1d51", "\u1d52", "\u1d53", "\u1d54", "\u1d55", "\u1d56", "\u1d57", "\u1d58", "\u1d59", "\u1d5a", "\u1d5b", "\u1d5c", "\u1d5d", "\u1d5e", "\u1d5f", "\u1d60", "\u1d61", "\u1d78", "\u1d9b", "\u1d9c", "\u1d9d", "\u1d9e", "\u1d9f", "\u1da0", "\u1da1", "\u1da2", "\u1da3", "\u1da4", "\u1da5", "\u1da6", "\u1da7", "\u1da8", "\u1da9", "\u1daa", "\u1dab", "\u1dac", "\u1dad", "\u1dae", "\u1daf", "\u1db0", "\u1db1", "\u1db2", "\u1db3", "\u1db4", "\u1db5", "\u1db6", "\u1db7", "\u1db8", "\u1db9", "\u1dba", "\u1dbb", "\u1dbc", "\u1dbd", "\u1dbe", "\u2c7d", "\ua015", "\ua4f8", "\ua4f9", "\ua4fa", "\ua4fb", "\ua4fc", "\ua69c", "\ua718", "\ua719", "\ua71a", "\ua71b", "\ua71c", "\ua71d", "\ua71e", "\ua770", "\ua7f8", "\ua7f9", "\uaa70", "\uaaf3", "\uab5d", "\uab5e", "\uff9e", "\uff9f", "\u6f98", "\u6f99", "\u6f9b", "\u07c1", "\u07c2", "\u07c3", "\u07c4", "\u07c5", "\u07c6", "\u07c7", "\u07c8", "\u07c9", "\u0c67", "\u0c6a", "\u0c6b", "\u0c6c", "\u0c6d", "\u0c6e", "\u0d67", "\u0d68", "\u0d6a", "\u0d6b", "\u0d6c", "\u0d6d", "\u0d6e", "\u0de7", "\u0de8", "\u0de9", "\u0dea", "\u0deb", "\u0dec", "\u0ded", "\u0dee", "\u1811", "\u1812", "\u1813", "\u1814", "\u1815", "\u1816", "\u1817", "\u1818", "\u1947", "\u1948", "\u1949", "\u194a", "\u194b", "\u194c", "\u194d", "\u194e", "\u194f", "\u19d1", "\u19d2", "\u19d3", "\u19d4", "\u19d5", "\u19d6", "\u19d7", "\u19d8", "\u1a84", "\u1a85", "\u1b51", "\u1b52", "\u1b53", "\u1b54", "\u1b55", "\u1b56", "\u1b57", "\u1b58", "\u1bb0", "\u1bb1", "\u1bb2", "\u1bb3", "\u1bb4", "\u1bb5", "\u1bb6", "\u1bb7", "\u1bb8", "\u1bb9", "\u1c41", "\u1c42", "\u1c43", "\u1c44", "\u1c45", "\u1c46", "\u1c47", "\u1c48", "\u1c50", "\u1c51", "\u1c52", "\u1c53", "\u1c54", "\u1c55", "\u1c56", "\u1c57", "\u1c58", "\u1c59", "\ua620", "\ua621", "\ua622", "\ua623", "\ua624", "\ua625", "\ua626", "\ua627", "\ua628", "\ua629", "\ua8d1", "\ua8d2", "\ua8d3", "\ua8d4", "\ua8d5", "\ua8d6", "\ua8d7", "\ua8d8", "\ua901", "\ua902", "\ua903", "\ua904", "\ua905", "\ua906", "\ua907", "\ua908", "\ua909", "\ua9d0", "\ua9d1", "\ua9d2", "\ua9d3", "\ua9d4", "\ua9d5", "\ua9d6", "\ua9d7", "\ua9d8", "\ua9f0", "\ua9f1", "\ua9f2", "\ua9f3", "\ua9f4", "\ua9f5", "\ua9f6", "\ua9f7", "\ua9f8", "\ua9f9", "\uaa51", "\uaa52", "\uaa53", "\uaa54", "\uaa55", "\uaa56", "\uaa57", "\uaa58", "\uabf1", "\uabf2", "\uabf3", "\uabf4", "\uabf5", "\uabf6", "\uabf7", "\uabf8", "\uff12", "\uff13", "\uff14", "\uff15", "\uff16", "\uff17", "\u1735", "\u1736", "\u1737", "\u1738", "\u1739", "\ud7fc", "\ud7fd", "\ud7fe", "\ue950", "\ue951", "\ue952", "\ue953", "\ue954", "\ue955", "\ue956", "\ue957", "\ue958", "\ue959", "\u0528", "\u052a", "\u052c", "\u052e", "\u13a1", "\u13a2", "\u13a3", "\u13a4", "\u13a5", "\u13a6", "\u13a7", "\u13a8", "\u13a9", "\u13aa", "\u13ab", "\u13ac", "\u13ad", "\u13ae", "\u13af", "\u13b0", "\u13b1", "\u13b2", "\u13b3", "\u13b4", "\u13b5", "\u13b6", "\u13b7", "\u13b8", "\u13b9", "\u13ba", "\u13bb", "\u13bc", "\u13bd", "\u13be", "\u13bf", "\u13c0", "\u13c1", "\u13c2", "\u13c3", "\u13c4", "\u13c5", "\u13c6", "\u13c7", "\u13c8", "\u13c9", "\u13ca", "\u13cb", "\u13cc", "\u13cd", "\u13ce", "\u13cf", "\u13d0", "\u13d1", "\u13d2", "\u13d3", "\u13d4", "\u13d5", "\u13d6", "\u13d7", "\u13d8", "\u13d9", "\u13da", "\u13db", "\u13dc", "\u13dd", "\u13de", "\u13df", "\u13e0", "\u13e1", "\u13e2", "\u13e3", "\u13e4", "\u13e5", "\u13e6", "\u13e7", "\u13e8", "\u13e9", "\u13ea", "\u13eb", "\u13ec", "\u13ed", "\u13ee", "\u13ef", "\u13f0", "\u13f1", "\u13f2", "\u13f3", "\u13f5", "\u2c70", "\u2c7e", "\u2c7f", "\u2ced", "\ua660", "\ua698", "\ua69a", "\ua78d", "\ua792", "\ua796", "\ua798", "\ua79a", "\ua79c", "\ua79e", "\ua7a0", "\ua7a2", "\ua7a4", "\ua7a6", "\ua7a8", "\ua7aa", "\ua7ab", "\ua7ac", "\ua7ae", "\ua7b2", "\ua7b3", "\ua7b4", "\ua7b6", "\u0c84", "\u0c8d", "\u0c91", "\u0ca9", "\u18ab", "\u18ac", "\u18ad", "\u18ae", "\u18af", "\ud403", "\ud404", "\ud405", "\ud406", "\ud407", "\ud40a", "\ud40b", "\ud40c", "\ud40d", "\ud40e", "\ud40f", "\ud410", "\ud411", "\ud412", "\ud413", "\ud414", "\ud415", "\ud416", "\ud418", "\ud419", "\ud434", "\ud435", "\ud436", "\ud437", "\ud439", "\ud43a", "\ud43b", "\ud43c", "\ud43d", "\ud43e", "\ud43f", "\ud446", "\ud447", "\ud448", "\ud449", "\ud44a", "\ud44b", "\ud44c", "\ud44d", "\ud468", "\ud469", "\ud46a", "\ud46b", "\ud46c", "\ud474", "\ud475", "\ud476", "\ud477", "\ud49c", "\ud49f", "\ud4a2", "\ud4a5", "\ud4a6", "\ud4ab", "\ud4ac", "\ud4ae", "\ud4af", "\ud4b0", "\ud4b1", "\ud4b2", "\ud4b3", "\ud4b4", "\ud4b5", "\ud4d7", "\ud4d8", "\ud4d9", "\ud4da", "\ud4db", "\ud4e1", "\ud4e2", "\ud4e3", "\ud4e4", "\ud4e5", "\ud4e6", "\ud4e7", "\ud50e", "\ud50f", "\ud510", "\ud511", "\ud512", "\ud513", "\ud519", "\ud51a", "\ud51b", "\ud51c", "\ud546", "\ud54a", "\ud54b", "\ud56f", "\ud570", "\ud571", "\ud572", "\ud573", "\ud57e", "\ud57f", "\ud580", "\ud581", "\ud582", "\ud583", "\ud5a0", "\ud5a1", "\ud5a2", "\ud5a3", "\ud5a4", "\ud5a9", "\ud5aa", "\ud5ab", "\ud5ac", "\ud5ad", "\ud5ae", "\ud5af", "\ud5b0", "\ud5b1", "\ud5b2", "\ud5b3", "\ud5b4", "\ud5b5", "\ud5b6", "\ud5b7", "\ud5b8", "\ud5b9", "\ud5d4", "\ud5d5", "\ud5d6", "\ud5d7", "\ud5df", "\ud5e0", "\ud5e1", "\ud5e2", "\ud5e3", "\ud60a", "\ud60b", "\ud60c", "\ud60d", "\ud60e", "\ud60f", "\ud617", "\ud618", "\ud619", "\ud61a", "\ud61b", "\ud676", "\ud677", "\ud678", "\ud679", "\ud67a", "\ud67b", "\ud67c", "\ud67d", "\ud67e", "\ud67f", "\ud680", "\ud687", "\ud688", "\ud689", "\ud6b2", "\ud6b3", "\ud6b4", "\ud6b5", "\ud6b6", "\ud6b7", "\ud6b8", "\ud6bd", "\ud6be", "\ud6bf", "\ud6c0", "\ud6ea", "\ud6eb", "\ud6ec", "\ud6ed", "\ud6f7", "\ud6f8", "\ud6f9", "\ud6fa", "\ud722", "\ud723", "\ud724", "\ud725", "\ud726", "\ud727", "\ud72f", "\ud730", "\ud731", "\ud732", "\ud733", "\ud75b", "\ud75c", "\ud75d", "\ud75e", "\ud792", "\ud793", "\ud794", "\ud795", "\ud796", "\ud797", "\ud79f", "\ud7a0", "\ud7a1", "\ud7a2", "\ud7a4", "\ud7a5", "\ud7a6", "\ud7a7", "\ud7a8", "\ud7ca", "\ue90d", "\ue90e", "\ue90f", "\ue910", "\ue911", "\ue912", "\ue913", "\ue914", "\ue915", "\ue916", "\ue917", "\ue918", "\ue919", "\ue91a", "\ue91b", "\ue91c", "\ue91d", "\ue91e", "\ue91f", "\ue920", "\ue921", "\u0529", "\u052b", "\u052d", "\u13f8", "\u13f9", "\u13fa", "\u13fb", "\u13fc", "\u13fd", "\u2cec", "\ua661", "\ua699", "\ua69b", "\ua791", "\ua793", "\ua794", "\ua795", "\ua797", "\ua799", "\ua79b", "\ua79d", "\ua79f", "\ua7a1", "\ua7a3", "\ua7a5", "\ua7a7", "\ua7a9", "\ua7b5", "\ua7b7", "\ua7fa", "\uab31", "\uab32", "\uab33", "\uab34", "\uab35", "\uab36", "\uab37", "\uab38", "\uab39", "\uab3a", "\uab3b", "\uab3c", "\uab3d", "\uab3e", "\uab3f", "\uab40", "\uab41", "\uab42", "\uab43", "\uab44", "\uab45", "\uab46", "\uab47", "\uab48", "\uab49", "\uab4a", "\uab4b", "\uab4c", "\uab4d", "\uab4e", "\uab4f", "\uab50", "\uab51", "\uab52", "\uab53", "\uab54", "\uab55", "\uab56", "\uab57", "\uab58", "\uab59", "\uab60", "\uab61", "\uab62", "\uab63", "\uab70", "\uab71", "\uab72", "\uab73", "\uab74", "\uab75", "\uab76", "\uab77", "\uab78", "\uab79", "\uab7a", "\uab7b", "\uab7c", "\uab7d", "\uab7e", "\uab7f", "\uab80", "\uab81", "\uab82", "\uab83", "\uab84", "\uab85", "\uab86", "\uab87", "\uab88", "\uab89", "\uab8a", "\uab8b", "\uab8c", "\uab8d", "\uab8e", "\uab8f", "\uab90", "\uab91", "\uab92", "\uab93", "\uab94", "\uab95", "\uab96", "\uab97", "\uab98", "\uab99", "\uab9a", "\uab9b", "\uab9c", "\uab9d", "\uab9e", "\uab9f", "\uaba0", "\uaba1", "\uaba2", "\uaba3", "\uaba4", "\uaba5", "\uaba6", "\uaba7", "\uaba8", "\uaba9", "\uabaa", "\uabab", "\uabac", "\uabad", "\uabae", "\uabaf", "\uabb0", "\uabb1", "\uabb2", "\uabb3", "\uabb4", "\uabb5", "\uabb6", "\uabb7", "\uabb8", "\uabb9", "\uabba", "\uabbb", "\uabbc", "\uabbd", "\uabbe", "\uabbf", "\u0cc5", "\u0cc9", "\u0cce", "\u0ccf", "\u0cd0", "\u0cd1", "\u0cd2", "\u0cd3", "\u0cd4", "\u0cd7", "\u0cd8", "\u0cd9", "\u0cda", "\u0cdb", "\u0cdc", "\u0cdd", "\u0cdf", "\u0ce4", "\u0ce5", "\u0cf0", "\ud41a", "\ud41b", "\ud41c", "\ud41f", "\ud420", "\ud421", "\ud422", "\ud423", "\ud424", "\ud425", "\ud426", "\ud427", "\ud428", "\ud429", "\ud42a", "\ud42b", "\ud42c", "\ud42d", "\ud42e", "\ud42f", "\ud430", "\ud431", "\ud432", "\ud433", "\ud44e", "\ud44f", "\ud450", "\ud451", "\ud452", "\ud453", "\ud456", "\ud457", "\ud458", "\ud459", "\ud45a", "\ud45b", "\ud466", "\ud467", "\ud484", "\ud485", "\ud486", "\ud487", "\ud48f", "\ud490", "\ud491", "\ud492", "\ud493", "\ud496", "\ud497", "\ud498", "\ud499", "\ud49a", "\ud49b", "\ud4b6", "\ud4b7", "\ud4b8", "\ud4bb", "\ud4bd", "\ud4be", "\ud4bf", "\ud4c0", "\ud4c1", "\ud4c2", "\ud4c3", "\ud4c5", "\ud4c6", "\ud4c7", "\ud4c8", "\ud4c9", "\ud4ca", "\ud4cb", "\ud4f2", "\ud4f3", "\ud4f4", "\ud4f5", "\ud4f6", "\ud4f7", "\ud4ff", "\ud500", "\ud501", "\ud502", "\ud503", "\ud51f", "\ud520", "\ud521", "\ud522", "\ud523", "\ud524", "\ud525", "\ud526", "\ud527", "\ud528", "\ud529", "\ud52a", "\ud52b", "\ud52c", "\ud52d", "\ud52e", "\ud52f", "\ud530", "\ud531", "\ud532", "\ud533", "\ud534", "\ud535", "\ud536", "\ud537", "\ud553", "\ud554", "\ud555", "\ud556", "\ud557", "\ud592", "\ud593", "\ud594", "\ud595", "\ud596", "\ud597", "\ud598", "\ud599", "\ud59a", "\ud59b", "\ud59c", "\ud59d", "\ud59e", "\ud59f", "\ud5ba", "\ud5bb", "\ud5bc", "\ud5bd", "\ud5be", "\ud5bf", "\ud5c0", "\ud5c1", "\ud5c2", "\ud5c3", "\ud5c4", "\ud5c5", "\ud5c6", "\ud5c7", "\ud5f0", "\ud5f1", "\ud5f2", "\ud5f3", "\ud5fb", "\ud5fc", "\ud5fd", "\ud5fe", "\ud5ff", "\ud626", "\ud627", "\ud628", "\ud629", "\ud62a", "\ud62b", "\ud62c", "\ud62f", "\ud630", "\ud631", "\ud632", "\ud633", "\ud634", "\ud635", "\ud636", "\ud637", "\ud65e", "\ud65f", "\ud660", "\ud661", "\ud663", "\ud664", "\ud665", "\ud666", "\ud66b", "\ud66c", "\ud66d", "\ud66e", "\ud66f", "\ud68a", "\ud68b", "\ud696", "\ud697", "\ud698", "\ud699", "\ud69a", "\ud69b", "\ud69c", "\ud6a3", "\ud6a4", "\ud6a5", "\ud6c2", "\ud6c3", "\ud6dc", "\ud6dd", "\ud6de", "\ud6df", "\ud706", "\ud707", "\ud708", "\ud709", "\ud70a", "\ud70b", "\ud70c", "\ud70d", "\ud70e", "\ud70f", "\ud710", "\ud73e", "\ud73f", "\ud740", "\ud741", "\ud742", "\ud743", "\ud74b", "\ud74c", "\ud74d", "\ud74e", "\ud776", "\ud777", "\ud778", "\ud779", "\ud77a", "\ud77b", "\ud783", "\ud784", "\ud785", "\ud786", "\ud787", "\ud7aa", "\ud7ab", "\ud7ac", "\ud7ad", "\ud7ae", "\ud7af", "\ud7c7", "\ud7c8", "\ud7c9", "\ue922", "\ue923", "\ue924", "\ue925", "\ue926", "\ue927", "\ue928", "\ue929", "\ue92a", "\ue92b", "\ue92c", "\ue92d", "\ue92e", "\ue92f", "\ue930", "\ue931", "\ue932", "\ue933", "\ue934", "\ue935", "\ue936", "\ue937", "\ue938", "\ue939", "\ue93a", "\ue93b", "\ue93c", "\ue93d", "\ue93e", "\ue93f", "\ue940", "\ue941", "\ue942", "\ue943", "\ud83d\ude04", "\u2add", "\ua7b9", "\ua7bb", "\ua7bd", "\ua7bf", "\ua7c3", "\ua7c8", "\ua7ca", "\ua7f6", "\u980b", "\ud84a\udc4a", "\ud84a\udc44", "\ud84c\udfd5", "\u3b9d", "\u4018", "\ud854\ude49", "\ud857\udcd0", "\ud85f\uded3", "\ud801\udcd8", "\ud801\udcd9", "\ud801\udcda", "\ud801\udcdb", "\ud801\udcdc", "\ud801\udcdd", "\ud801\udcde", "\ud801\udcdf", "\ud801\udce0", "\ud801\udce1", "\ud801\udce2", "\ud801\udce3", "\ud801\udce4", "\ud801\udce5", "\ud801\udce6", "\ud801\udce7", "\ud801\udce8", "\ud801\udce9", "\ud801\udcea", "\ud801\udceb", "\ud801\udcec", "\ud801\udced", "\ud801\udcee", "\ud801\udcef", "\ud801\udcf0", "\ud801\udcf1", "\ud801\udcf2", "\ud801\udcf3", "\ud801\udcf4", "\ud801\udcf5", "\ud801\udcf6", "\ud801\udcf7", "\ud801\udcf8", "\ud801\udcf9", "\ud801\udcfa", "\ud801\udcfb", "\ud803\udcc0", "\ud803\udcc1", "\ud803\udcc2", "\ud803\udcc3", "\ud803\udcc4", "\ud803\udcc5", "\ud803\udcc6", "\ud803\udcc7", "\ud803\udcc8", "\ud803\udcc9", "\ud803\udcca", "\ud803\udccb", "\ud803\udccc", "\ud803\udccd", "\ud803\udcce", "\ud803\udccf", "\ud803\udcd0", "\ud803\udcd1", "\ud803\udcd2", "\ud803\udcd3", "\ud803\udcd4", "\ud803\udcd5", "\ud803\udcd6", "\ud803\udcd7", "\ud803\udcd8", "\ud803\udcd9", "\ud803\udcda", "\ud803\udcdb", "\ud803\udcdc", "\ud803\udcdd", "\ud803\udcde", "\ud803\udcdf", "\ud803\udce0", "\ud803\udce1", "\ud803\udce2", "\ud803\udce3", "\ud803\udce4", "\ud803\udce5", "\ud803\udce6", "\ud803\udce7", "\ud803\udce8", "\ud803\udce9", "\ud803\udcea", "\ud803\udceb", "\ud803\udcec", "\ud803\udced", "\ud803\udcee", "\ud803\udcef", "\ud803\udcf0", "\ud803\udcf1", "\ud803\udcf2", "\ud806\udcc0", "\ud806\udcc1", "\ud806\udcc2", "\ud806\udcc3", "\ud806\udcc4", "\ud806\udcc5", "\ud806\udcc6", "\ud806\udcc7", "\ud806\udcc8", "\ud806\udcc9", "\ud806\udcca", "\ud806\udccb", "\ud806\udccc", "\ud806\udccd", "\ud806\udcce", "\ud806\udccf", "\ud806\udcd0", "\ud806\udcd1", "\ud806\udcd2", "\ud806\udcd3", "\ud806\udcd4", "\ud806\udcd5", "\ud806\udcd6", "\ud806\udcd7", "\ud806\udcd8", "\ud806\udcd9", "\ud806\udcda", "\ud806\udcdb", "\ud806\udcdc", "\ud806\udcdd", "\ud806\udcde", "\ud806\udcdf", "\ud81b\ude60", "\ud81b\ude61", "\ud81b\ude62", "\ud81b\ude63", "\ud81b\ude64", "\ud81b\ude65", "\ud81b\ude66", "\ud81b\ude67", "\ud81b\ude68", "\ud81b\ude69", "\ud81b\ude6a", "\ud81b\ude6b", "\ud81b\ude6c", "\ud81b\ude6d", "\ud81b\ude6e", "\ud81b\ude6f", "\ud81b\ude70", "\ud81b\ude71", "\ud81b\ude72", "\ud81b\ude73", "\ud81b\ude74", "\ud81b\ude75", "\ud81b\ude76", "\ud81b\ude77", "\ud81b\ude78", "\ud81b\ude79", "\ud81b\ude7a", "\ud81b\ude7b", "\ud81b\ude7c", "\ud81b\ude7d", "\ud81b\ude7e", "\ud81b\ude7f", "\ud834\udd57", "\ud834\udd65", "\ud834\udd58", "\ud834\udd6e", "\ud834\udd6f", "\ud834\udd70", "\ud834\udd71", "\ud834\udd72", "\ud834\uddb9", "\ud834\uddba", "\ud83a\udd22", "\ud83a\udd23", "\ud83a\udd24", "\ud83a\udd25", "\ud83a\udd26", "\ud83a\udd27", "\ud83a\udd28", "\ud83a\udd29", "\ud83a\udd2a", "\ud83a\udd2b", "\ud83a\udd2c", "\ud83a\udd2d", "\ud83a\udd2e", "\ud83a\udd2f", "\ud83a\udd30", "\ud83a\udd31", "\ud83a\udd32", "\ud83a\udd33", "\ud83a\udd34", "\ud83a\udd35", "\ud83a\udd36", "\ud83a\udd37", "\ud83a\udd38", "\ud83a\udd39", "\ud83a\udd3a", "\ud83a\udd3b", "\ud83a\udd3c", "\ud83a\udd3d", "\ud83a\udd3e", "\ud83a\udd3f", "\ud83a\udd40", "\ud83a\udd41", "\ud83a\udd42", "\ud83a\udd43", "\ud840\udd22", "\u349e", "\ud841\ude3a", "\ud841\udd1c", "\u34b9", "\ud841\udd4b", "\ud864\udddf", "\u3515", "\ud842\ude2c", "\ud842\udf63", "\u5717", "\u5651", "\ud845\udce4", "\ud845\udea8", "\ud845\udeea", "\u36ee", "\ud846\uddc8", "\ud846\udf18", "\u3781", "\ud847\udde4", "\ud847\udde6", "\u382f", "\u3862", "\ud848\udd83", "\u387c", "\ud868\udf92", "\ud848\udf31", "\u38c7", "\ud84c\udeb8", "\ud858\uddda", "\u38e3", "\u393a", "\u391c", "\ud849\uded4", "\u625d", "\ud84a\udf0c", "\ud84a\udff1", "\u3a2e", "\u647e", "\u3a6c", "\ud84c\udc0a", "\u3b08", "\u3ae4", "\ud84c\udfc3", "\u3b49", "\ud84d\udc6d", "\ud84d\udea3", "\ud84e\udca7", "\u3c4e", "\ud84e\ude8d", "\ud847\udd0b", "\ud84f\udcbc", "\ud84f\udd1e", "\u3d33", "\ud84f\uded1", "\ud84f\udf5e", "\ud84f\udf8e", "\u3d96", "\ud841\udd25", "\ud850\ude63", "\ud851\ude08", "\ud851\udf35", "\ud852\udc14", "\u3eac", "\u3f1b", "\ud853\udc36", "\ud853\udc92", "\ud848\udd9f", "\ud853\udfa1", "\ud854\udc44", "\u3ffc", "\u4008", "\ud854\udcf3", "\ud854\udcf2", "\ud854\udd19", "\ud854\udd33", "\u4046", "\u4096", "\ud855\udc1d", "\u40e3", "\ud855\ude26", "\ud855\ude9a", "\ud855\udec5", "\u412f", "\ud856\udd7c", "\ud856\udea7", "\u4202", "\ud856\udfab", "\u4227", "\ud857\udc80", "\u42a0", "\u7ce3", "\ud857\udf86", "\u4301", "\u7e02", "\u4334", "\ud858\ude28", "\ud858\ude47", "\u4359", "\ud858\uded9", "\ud858\udf3e", "\ud859\udcda", "\ud859\udd23", "\ud859\udda8", "\ud84c\udf5f", "\u43d5", "\ud859\udfa7", "\ud859\udfb5", "\ud84c\udf93", "\ud84c\udf9c", "\ud85a\udf3c", "\ud85b\udc36", "\ud85b\udd6b", "\ud85b\udcd5", "\ud85c\udfca", "\ud85b\udf2c", "\ud85b\udfb1", "\ud85d\ude67", "\u34bb", "\ud85e\udcae", "\ud85e\udd66", "\u46be", "\u46c7", "\ud85f\udca8", "\ud85f\udf2f", "\ud842\udc04", "\ud842\udcde", "\ud861\uddd2", "\ud861\udded", "\ud861\udf2e", "\ud862\udffa", "\u4995", "\ud863\udd77", "\u49e6", "\ud864\udd45", "\ud864\ude1a", "\u4a6e", "\u4a76", "\ud865\udc0a", "\u4ab2", "\ud865\udc96", "\ud865\uddb6", "\u4b33", "\u4bce", "\ud866\udf30", "\u4cce", "\ud868\udcce", "\u4cf8", "\ud868\udd05", "\ud868\ude0e", "\ud868\ude91", "\u4d56", "\u9f05", "\ud869\ude00", "\u25a2", "\u25c9", "\u2840", "\u2844", "\u2846", "\u2847", "\u28c7", "\u28e7", "\u28f7", "\u28ff", "\u25f7", "\u25f6", "\u25f5", "\u25f4", "\u25d2", "\u25d3", "\u23ba", "\u23bb", "\u23bc", "\u23bd", "\u28fe", "\u28ef", "\u28df", "\u287f", "\u28bf", "\u28fb", "\u28fd", "\u2582", "\u2583", "\u2585", "\u2586", "\u2587", "\u25d4", "\u25d5", "\ud83d\udcbb", "\uac15" ]
			isBinCharTest.append(chr(10))
			isBinCharTest.append('/r')
			isBinCharTest.append('/n')
	def isBin( self, path ):
 
 
 
		try:
			head = vc.HD.headTXT(path)
		except Exception as e:
			return True

		if not len(head):
			return False
		elif head[0] == '#':
			return False

		# print(head)
		# print(head[0])
		# sys.exit()

		# try:
		# import mimetypes
		# mime = str(mimetypes.guess_type(path)).lower()
		# if 'text' in mime:
		#    return False
		# else:
		#    return True

		# except Exception as e:
		global isBinCharTest

		self.isBinChar()

		for c in head:
			if not c in isBinCharTest:
				_printME_('error',c)
				return True
		return False
	def isText( self, path ):
 
 
 
		if self.isBin(path):
			return False
		else:
			return True

	def isCrypt( self, filepath ):
 
 
 
		if vc.HD.head(filepath).startswith( '41 45 53 02 00 00 1B' ):
			return True
		else:
			return False

	def isGz( self, filepath ):
 
 
 
		if vc.HD.head(filepath).startswith( '1F 8B 08 08' ):
			return True
		else:
			return False

	def isBz2( self, filepath ):
 
 
 
		if vc.HD.head(filepath).startswith( '42 5A 68' ):
			return True
		else:
			return False




hex_header_chars = [ "A", "C", "S", "D", "b", "p", "l", "i", "s", "t", "\u0000", "\u0014", "\u0001", "\u0002", "0", "7", "\u007f", "E", "L", "F", "\u00a1", "\u00b2", "\u00cd", "4", "\u0004", "\u0005", "\u00ac", "\u00ed", "K", "W", "J", "\u0088", "\u00f0", "'", "\u00d1", " ", "\u00aa", "Z", "3", "o", "<", "\u00c3", "\u00d4", "\u00ef", "\u00bb", "\u00bf", "\u00fe", "\u00ff", "e", "g", "n", "\u00e4", "\u0096", "\u00c9", "\u00db", "\u00d6", "\u0007", "\u001a", "\u0010", "M", "f", "y", "\u0018", "R", "I", "z", "\u00bc", "\u00af", "\u001c", "B", "Q", "V", "r", ".", "O", "N", "X", "a", "d", "\u00ab", "\u00d0", "\u00cf", "\u0011", "\u00e0", "\u00b1", "\u00e1", "U", ":", ",", "\u0003", "P", "\u0080", "\u0012", "!", "#", "\u0090", "\b", "\t", "`", "\u00ea", "*", "&", "u", "\u008e", "H", "\u008a", "T", "2", "h", "c", "(", "\u00b5", "\u00a2", "\u00b0", "\u00b3", "\u00a5", "_", "[", "m", "\u00ca", "\u00ba", "\u00be", "+", "1", "\u00e8", "\u00e9", "\u00eb", "\u00dc", "w", "v", "\u00a9", "\r", "G", "6", "\u0006", "\u0015", "\u00d2", "\u00fd", "\u00ad", "\u00de", "x", "\n", "9", "\u0093", "\u00a7", "-", "\u00ec", "\u00c1", "]", "{", "@", "\u00c5", "\u00d3", "\u00c6", "%", "5", "\"", "k", "?", "8", "\u0099", "\u001f", "\u008b", "\u0091", "\u00e3", "\u00a8", "\u0089", "\u00d8", "\u000e", "\f", "j", "\u00e2", "\u00c8", ">", "=", "\u000f", "\u00df", "\u00a3", "\u0082", "\\", "\u008c", "\u000b", "/", "\u00a0", "\u001d", "\u001e", "~", "\u0085", "\u0086", "\u009e", "\u00bd", "\u008f", "\u00da", "\u00ee", "\u00a4", "$", ")", "\u0095", "\u0084", "Y", "\u009d", "\u00b4", "\u0081", "\u009c", "\u00cb", "\u008d", "\u0013", "\u00d7", "\u009a", "}" ]
visibleChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


class FIG:

	def __init__( self ):
		self.imp_table = {}
		self.importlib = None
		self.bashrc_spent = []

	def load( self ):
		folder_alt = '(profile)Downloads'
		folder_alt = vc.PATHS.path(folder_alt.replace( '(profile)', v.home + os.sep ))

		



		self.folder_IDs = {
								'{C12F266D-71B9-40D2-98B9-424B42D2DBAC}': v.host,
								'{6FAB5628-94A1-410A-82D1-1D42A2A11750}': v.home,
								'{D53E69A0-5663-4D19-B0A8-817F0AECBF9C}': v.appsFolder,
								'{BCAE64F2-C911-4F04-AF8C-DFE052E60973}': folder_alt,
								'{A8693D4B-8A80-898F-83F0-E806D2F36800}': v.bash['widgets'],

		}
		self.bm_default = """ii|/mnt/d/tech/hosts/VULCAN/indexes
vi|/mnt/d/tech/hosts/VULCAN/indexes
iv|/mnt/d/tech/hosts/VULCAN/indexes
hh|/mnt/d/tech/hosts
mi|/mnt/d/tech/hosts/MSI/indexes
im|/mnt/d/tech/hosts/MSI/indexes
pp|{A8693D4B-8A80-898F-83F0-E806D2F36800}/programs
p|{6FAB5628-94A1-410A-82D1-1D42A2A11750}
ppp|/mnt/d/programs
git|/mnt/d/widgets/git
b|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/bash
bash|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/bash
livepp|/mnt/d/programs
l.pp|/mnt/d/programs
l.b|/mnt/d/widgets/bash
l.bash|/mnt/d/widgets/bash
l.py|/mnt/d/widgets/python
l.ttt|/mnt/d/widgets/databank/tables
l.db|/mnt/d/widgets/databank/tables
live.pp|/mnt/d/programs
pp.live|/mnt/d/programs
live.py|/mnt/d/widgets/python
py.live|/mnt/d/widgets/python
live.i|/mnt/d/tech/hosts/VULCAN/indexes
i.live|/mnt/d/tech/hosts/VULCAN/indexes
h|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}
i|{A8693D4B-8A80-898F-83F0-E806D2F36800}/hosts/VULCAN/indexes
tt|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/tables
ttt|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/databank/tables
py|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/python
ent|/mnt/d/entertainment/movies
pr|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects
key|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys
keys|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys
key.p|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys/p
k.p|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys/p
kp|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys/p
k|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/keys
config|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/config
ta|/mnt/d/techApps
sh.stuff|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
stuff.sh|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
sh|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sh-stuff
sshfs|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/sshfs_test
b.live|/mnt/d/widgets/bash
bash.live|/mnt/d/widgets/bash
.rt|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt
pr.live|/mnt/d/tech/hosts/VULCAN/projects
h.live|/mnt/d/tech/hosts/VULCAN
ovpn|{A8693D4B-8A80-898F-83F0-E806D2F36800}/{C12F266D-71B9-40D2-98B9-424B42D2DBAC}/projects/ovpn
ovpn.live|/mnt/d/tech/hosts/VULCAN/projects/ovpn
bash.test|/mnt/d/tech/hosts/VULCAN/projects/bash
pp.l|/mnt/d/programs
py.l|/mnt/d/widgets/python
i.l|/mnt/d/tech/hosts/VULCAN/indexes
b.l|/mnt/d/widgets/bash
bash.l|/mnt/d/widgets/bash
pr.l|/mnt/d/tech/hosts/VULCAN/projects
h.l|/mnt/d/tech/hosts/VULCAN
ovpn.l|/mnt/d/tech/hosts/VULCAN/projects/ovpn
bm|{A8693D4B-8A80-898F-83F0-E806D2F36800}/widgets/python/_rightThumb/_bookmarks
tool.live|/mnt/d/widgets/bash/install/py
tool|/mnt/d/widgets/bash/install/py
tt-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile/tables
p-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile
rt-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt
pr-|{6FAB5628-94A1-410A-82D1-1D42A2A11750}/.rt/profile/projects"""
		pass


	def path_clean( self, path ):
		path = path.replace( chr(92), os.sep )
		path = path.replace( chr(47), os.sep )
		path = path.replace( os.sep+os.sep, os.sep )
		return path

	def path_resolve( self, path ):
		path = self.path_clean(path)
		for k in self.folder_IDs:
			# if k in path:
			#   print('r',k,path)
			path = path.replace( k, self.folder_IDs[k] )
		path = self.path_clean(path)
		return path

	def path_secure( self, path ):
		path = self.path_clean(path)
		for k in self.folder_IDs:
			# if self.folder_IDs[k] in path:
			#   print('s',k,path,self.folder_IDs[k])
			# else:
			#   print('e',self.folder_IDs[k])

			path = path.replace( self.folder_IDs[k], k )
		path = self.path_clean(path)
		return path






	def save_bashrc( self, code, bashrc_manual=None, b='E45D09D22184', e='AEC80B4D3338', be='## {xXx} ##' ):

		root_bashrc_check = [
								'/root/.bashrc',
								# '/etc/bash.bashrc',
		]


		
		if not v.isWin:


			tmpFile = v.temp+'/who.txt'
			os.system("whoami>"+tmpFile)
			username = 'user'
			if os.path.isfile(tmpFile):
				username = vc.HD.getText( tmpFile, clean=2,raw=True ).replace('\n','')
			


			
			if not bashrc_manual is None:
				# print('specified', bashrc_manual)
				bashrc_path = bashrc_manual
			elif bashrc_manual is None:

				# if not username == 'root':
				bashrc_path = os.getenv('HOME') + os.sep + '.bashrc'
				
				if username == 'root':
					self.save_bashrc( code, bashrc_path, b, e, be )
					self.save_bashrc( code, root_bashrc_check[0] )
					for i,root_test in enumerate(root_bashrc_check):
						if i:
							if os.path.isfile(root_test):
								self.save_bashrc( code, root_test, b, e, be )
					sys.exit()
			if bashrc_path in self.bashrc_spent:
				return None


			self.bashrc_spent.append(bashrc_path)
			_printME_( 'whoami:', username )
			# print( 'running:',bashrc_path )
			bashrc = vc.HD.getText( bashrc_path, raw=True )
			
			s = be.replace( 'xXx', b )
			e = be.replace( 'xXx', e )
			if bashrc is None:
				bashrc = ''
			if not s in bashrc:
				bashrc += '\n\n'
				bashrc += s
				bashrc += '\n\n'
				bashrc += e
				bashrc += '\n\n'


			alias = []
			for item in code.split('\n'):
				# item = _str.cleanBE(item,' ')
				alias.append(item)

			active=False
			wasActive=False
			new_bashrc = []
			# new_bashrc = ''
			for line in bashrc.split('\n'):
				if s in line:
					active=True


				if not active:

					if 'h' in switches.values('Installer') or 'h' in switches.values('.bashrc-Default'):
						if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
							new_bashrc.append(line)
							# new_bashrc += line + '\n'
						else:
							new_bashrc.append('# '+line)
							# new_bashrc += '# '+line + '\n'
					else:
						new_bashrc.append(line)
						# new_bashrc += line + '\n'



				if e in line:
					new_bashrc.append(s)
					# new_bashrc += s + '\n'
					for a in alias:
						new_bashrc.append(a)
						# new_bashrc += a + '\n'

					new_bashrc.append(e)
					# new_bashrc += e + '\n'
					active=False
					wasActive=True


			vc.HD.saveText( '\n'.join(new_bashrc), bashrc_path )
			cp(  [bashrc_path, 'updated'], 'cyan'  )


	def bashrc( self, subject=None, settings=[] ):
		if 'installer.py2' in 'installer.py ':
			nn = '2'
		else:
			nn = '3'
		nn = '3'
		for seti in settings:
			if len(seti) == 2 and seti[0] == 'v' and seti[1] in '0123456789':
				nn = seti[1]
		loader()
		v.bashrc_default = False

		file = ''
		if subject is None:
			v.bashrc_default = True
			nt = 'def'
			if 'installer.py2' in 'installer.py ':
				add = A.vfiles.file('.bashrc.full')['data']
				add += A.vfiles.file('.bashrc.mini')['data']
				if not 'h' in switches.values('Installer') and not 'h' in switches.values('.bashrc-Default'):
					newFile=''
					for line in add.split('\n'):
						if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
							newFile+=line+'\n'
						else:
							newFile+='# '+line+'\n'
							
					add=newFile
				file += add
			else:
				add = A.vfiles.file('.bashrc.mini')['data']
				add += A.vfiles.file('.bashrc.full')['data']
				if not 'h' in switches.values('Installer') and not 'h' in switches.values('.bashrc-Default'):
					newFile=''
					for line in add.split('\n'):
						if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
							newFile+=line+'\n'
						else:
							newFile+='# '+line+'\n'
					add=newFile
				file += add
			
		else:
			if subject == 'mini':

				file = self.bash_vars(p=0)
			add = A.vfiles.file('.bashrc.'+subject)['data']
			if not 'h' in switches.values('Installer') and not 'h' in switches.values('.bashrc-Default'):
				newFile=''
				for line in add.split('\n'):
					if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
						newFile+=line+'\n'
					else:
						newFile+='# '+line+'\n'
				add=newFile
			file += add
			nt = subject
		save = True

		for seti in settings:
			if 'auto' in seti:
				add = A.vfiles.file('.bashrc-auto')['data']
				if not 'h' in switches.values('Installer') and not 'h' in switches.values('.bashrc-Default'):
					newFile=''
					for line in add.split('\n'):
						if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
							newFile+=line+'\n'
						else:
							newFile+='# '+line+'\n'
					add=newFile
				file += add

			if 'strip' in seti:
				file = file.replace( '$( $widgets/install/installer.py -bash.vars )', self.bash_vars(p=0) )
			if 'print' in seti:
				save = False
			if 'home' in seti:
				file += '\n\ncd $HOME\n\n'
			if 'clear' in seti:
				file += '\n\nclear\n\n'


		add = A.vfiles.file('.bashrc-all')['data']
		if not 'h' in switches.values('Installer') and not 'h' in switches.values('.bashrc-Default'):
			newFile=''
			for line in add.split('\n'):
				if not 'HISTSIZE' in line and not 'HISTFILESIZE' in line:
					newFile+=line+'\n'
				else:
					newFile+='# '+line+'\n'
			add=newFile
		file += add

		file = file.replace( '.20F543'+'59E924', '' )
		file = file.replace( '20F543'+'59E924', '' )
		# file = file.replace( '20F543'+'59E924', nn+'.'+nt )

		file += '\n'
		file += 'alias k="$widgets/widgets/python/keychain.py -rc ";\n'
		file += 'alias pc="$widgets/widgets/python/pc.py -rc ";\n'
		file += 'alias color="$widgets/widgets/python/pipe-color.py -color ";\n'
		file += '\n'

		# print( file )







		if save:
			self.save_bashrc( file )
		else:
			_printME_(file)

	def home( self ):
 
 
 
		global v
		if v.home is None:
			temp = None
			try:
				temp = os.getenv('XDG_CURRENT_DESKTOP')
				if type(temp) == str and len(temp) > 2:
					v.gui = True
			except Exception as e:
				pass
			if temp is None:
				try:
					temp = os.getenv('GDMSESSION')
					if type(temp) == str and len(temp) > 2:
						v.gui = True
				except Exception as e:
					pass
				



			pass
			if v.isWin:
				v.home = os.getenv('USERPROFILE')
			elif not v.isWin:

				try:
					v.home = os.getenv('HOME')
				except Exception as e:
					try:
						from pathlib import Path
						v.home = str(Path.home())
					except Exception as e:
						v.home = '~'

		v.home = vc.PATHS.path(v.home)
		v.rt = v.home +os.sep+ '.rt'
		v.rtc = v.rt +os.sep+ 'config'
		v.config = v.rt +os.sep+ '.config.hash'
		v.config_py = v.rtc +os.sep+ '.py'
		v.f.mkdir( v.rt )
		# v.f.mkdir( v.rtc )
		return v.home

	def var_clean( self ):

		done=False
		while not done:
			err=False
			for k in v.bash:
				if not self.var_test(v.bash[k]):
					err=True
					del v.bash[k]
					break
			if not err:
				done=True

	def var_test( self, var ):
		if os.path.isfile(var):
			return True
		if os.path.isdir(var):
			return True

		if not os.sep in var:
			import subprocess
			try:
				result=subprocess.check_output([  'which', var ])
				result=str( result ,'iso-8859-1')
				if len(result) > 3:
					return True
			except Exception as e:
				pass
		return False
	def bash_vars( self, p=1 ):
 
 
		global v
		self.home()
		# print( v.home )
		def _bash_DEF_():
			v.bash['widgets'] = vc.PATHS.path(__file__).split(os.sep+'install')[0]
			for key in v.bash_defaults.keys():
				if not key in v.bash:
					v.bash[key] = v.bash_defaults[key].replace('[widgets]',v.bash['widgets'])
		items = []
		_printME_(v.config)
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		# else:
		#     _bash_DEF_()
		#     vc.HD.saveTableSimp( v.bash, v.config )



		# print(v.bash_defaults)
		# print( type(v.bash_defaults) )
		# sys.exit()
		
		_bash_DEF_()
		if not v.isWin:
			if not v.gui:
				for key in v.bash_defaults_no_gui.keys():
					v.bash[key] = v.bash_defaults_no_gui[key]


		self.v_bash_order()
		# if 'PY' in v.bash and not v.bash['PY'] and 'PY' in v.bash_defaults:
		#   v.bash['PY'] = v.bash_defaults['PY']

		# if 'widgets' in v.bash and not v.bash['widgets'] and 'widgets' in v.bash_defaults:
		#   v.bash['widgets'] = v.bash_defaults['widgets']
		
		# if 'code_editor' in v.bash and not v.bash['code_editor'] and 'code_editor' in v.bash_defaults:
		#   v.bash['code_editor'] = v.bash_defaults['code_editor']
		if not 'widgets' in v.bash:
			v.bash['widgets'] = vc.PATHS.path(__file__).split(os.sep+'install')[0]
		
		if v.isWin:
			v.bash['p'] = v.bash['widgets'] + '\\widgets\\batch\\p.bat'
		else:
			v.bash['p'] = v.bash['widgets'] + '/widgets/bash/nav/p.sh'
		v.bash['p'] = v.bash['p'].replace('/',os.sep)

		for k in v.bash:
			if os.sep in v.bash[k]:
				v.bash[k] = vc.PATHS.path(v.bash[k])
				if v.isWin:
					if not k in ['widgets']:
						v.bash[k] = '"'+v.bash[k]+'"'
					else:
						v.bash[k] = v.bash[k]
		
		# if v.isWin:
		#   v.bash['widgets'] = v.bash['widgets'][0]
		for k in v.bash:
			# if not k == 'widgets':
			if '/opt/rightthumb-widgets-v0' in v.bash[k]:
				v.bash[k] = v.bash[k].replace( '/opt/rightthumb-widgets-v0', v.bash['widgets'] )

		self.v_bash_order()



		items.append('\n')
		for key in v.bash:
			if key:
				if v.bash[key] and not key == 'CAT' and not key == 'SHELL':
					if v.isWin:
						items.append( 'set '+cl(key)+'='+v.bash[key]+'\n' )
					else:
						items.append( 'export '+cl(key)+'='+v.bash[key]+'\n' )
		items.append('\n')
		export = ''.join(items)
		if v.isWin:
			ext='bat'
			export=export.replace('\\\\','\\')
		else:
			ext='sh'
		_printME_( export )
		self.home()
		if not 'wprofile' in v.bash:
			v.bash['wprofile']=v.home+os.sep+'.rt'+os.sep+'profile'
		if not 'code_editor' in v.bash: v.bash['code_editor']='nano'
		if not 'code_editor2' in v.bash: v.bash['code_editor2']='C:\\Program Files\\Sublime Text\\sublime_text.exe'

		v.f.mkdir(v.bash['wprofile']+os.sep+'vars')
		vc.HD.saveText( export, v.bash['wprofile']+os.sep+'vars'+os.sep+'config.'+ext )
		if p:
			if v.isWin:
				comment=':'

			else:
				comment='#'
			
			if not os.path.isfile(v.bash['wprofile']+os.sep+'vars'+os.sep+'config.'+ext):
				color='yellow'
				me=0
			else:
				me=os.stat( v.bash['wprofile']+os.sep+'vars'+os.sep+'config.'+ext ).st_size
				if me > 5:
					color='green'
				else:
					color='cyan'
			cp([comment,vc.DIR.formatSize(me),v.bash['wprofile']+os.sep+'vars'+os.sep+'config.'+ext],color)

			# if True:
			if not os.path.isfile(v.bash['wprofile']+os.sep+'vars'+os.sep+'personal.'+ext):
				vc.HD.saveText( export, v.bash['wprofile']+os.sep+'vars'+os.sep+'personal.'+ext )
				color='yellow'
				me=0
			else:
				me=os.stat( v.bash['wprofile']+os.sep+'vars'+os.sep+'personal.'+ext ).st_size
				if me > 5:
					color='green'
				else:
					color='cyan'


			cp([comment,vc.DIR.formatSize(me),v.bash['wprofile']+os.sep+'vars'+os.sep+'personal.'+ext],color)
			if not os.path.isfile(v.home+os.sep+'.rt'+os.sep+'.config.hash'):
				color='yellow'
				me=0
			else:
				me=os.stat( v.home+os.sep+'.rt'+os.sep+'.config.hash' ).st_size
				if me > 5:
					color='green'
				else:
					color='cyan'
			cp([comment,vc.DIR.formatSize(me),v.home+os.sep+'.rt'+os.sep+'.config.hash'],color)
			# print(color)
		# print()
		# print('suggestion:')
		# print('    echo "alias crontab=\'EDITOR=nano /usr/bin/crontab\'" >> ~/.bashrc')
		# print()

		vc.HD.saveTableSimp( v.bash, v.config )
		return export



	def v_bash_order( self ):
		vVv = vc.PATHS.clean4os( v.vVv )
		bash_defaults = vc.PATHS.clean4os( v.bash_defaults )

		if not 'widgets' in v.bash:
			v.bash['widgets'] = vc.PATHS.path(__file__).split(os.sep+'install')[0]

		for k in vVv:
			if not k in v.bash:
				v.bash[k] = vVv[k]

		for k in bash_defaults:
			if not k in v.bash:
				v.bash[k] = bash_defaults[k]

		for k in v.bash:
			if not k == 'widgets':
				v.bash[k] = v.bash[k].replace( '/opt/rightthumb-widgets-v0', v.bash['widgets'] )
 
		table = {}
		# if v.isWin:
		#   if 'widgets' in v.bash:
		#       v.bash['widgets'] = v.bash['widgets'][0]+':'
		for key in v.bash_defaults:
			if key in v.bash:
				table[key] = v.bash[key]
		for key in v.bash:
			if not key in table:
				table[key] = v.bash[key]
		v.bash = table
		
		for key in v.bash:
			for key2 in v.bash:
				if '['+key2+']' in v.bash[key]:
					v.bash[key] = v.bash[key].replace( '['+key2+']', v.bash[key2] )

		for key in v.bash:
			if '\\' in v.bash[key] and not '\\\\' in v.bash[key]:
				v.bash[key]=v.bash[key].replace( '\\', '\\\\' )

		if not 'wprofile' in v.bash:
			v.bash['wprofile']=v.home+os.sep+'.rt'+os.sep+'profile'
		v.bash['w']=v.bash['widgets']
		v.bash['ww']=v.bash['widgets']+os.sep+'widgets'
		for k in v.bash:
			v.bash[k]=v.bash[k].replace('"','')
			v.bash[k]=v.bash[k].replace(os.sep+os.sep,os.sep)
			v.bash[k]=v.bash[k].replace(os.sep+os.sep,os.sep)
			if ' ' in v.bash[k]:
				v.bash[k]='"'+v.bash[k]+'"'

		done = False
		while not done:
			done=True
			for k in v.bash:
				if os.sep in k or '-' in k or ' ' in k or v.bash[k] == '' :
					done=False
					del v.bash[k]
					break
		
		if 'profile' in v.bash:
			del v.bash['profile']

		for k in v.bash:
			if '[profile]' in v.bash[k]:
				if 'wprofile' in v.bash:
					v.bash[k]=v.bash[k].replace( '[profile]', v.bash['wprofile'] )

			if '[home]' in v.bash[k]:
				v.bash[k]=v.bash[k].replace( '[home]', v.home )
				
		self.var_clean()









	def imp( self, subject, testing=False ):
		try:
			v.bash['PY']
		except Exception as e:
			vc.FIG.bash_vars(p=0)
 
		if self.importlib is None:
			try:
				import importlib
			except Exception as e:

				file = ''
				if 'installer.py2' in 'installer.py ':
					file += '#!'+v.bash['PY2']
				else:
					file += '#!'+v.bash['PY']
				file += '\n'
				file += 'import '+subject+' as subject'
				file += '\n'
				vc.HD.saveText( v.home+os.sep+'.rt'+os.sep+'config_helper.py', path )
				time.sleep(.05)
				import config_helper
				return config_helper.subject

				return None
			self.importlib = importlib
			if testing:
				_printME_('\n\n\t\timport importlib\n\n')

		if not subject in self.imp_table:

			try:
				self.imp_table[subject] = self.importlib.import_module(subject)
				if testing:
					_printME_( 'imp.DID' )
				return self.imp_table[subject]
			except Exception as e:
				cp( 'missing '+subject, 'red' )
				if testing:
					_printME_( 'imp.NO' )
				return None
		if testing:
			_printME_( 'imp.YES' )
		return self.imp_table[subject]

	def uuid( self ):
 
 
 
		UUID = self.imp('uuid')
		return str(UUID.uuid4())

	def settings( self, subjects, a='a678-71e9', d=None, to='71e9-a678' ):
 
 
 
		if not a == 'a678-71e9':
			for subject in subjects:
				if a == setting( subject, to, d ):
					return True
			return False
		else:
			for subject in subjects:
				setting( subject, to, d )


	setting_table = {}
	def setting( self, subject, to='71e9-a678', d=None ):
 
 
 
		global setting_table

		if not to == '71e9-a678':
			setting_table[subject] = to

		if not subject in setting_table:
			return d
		
		return setting_table[subject]





def printDic( data, p=1 ):
	table = []
	for key in data:
		string = spaces(2)+'"' + key + '": "' + data[key] + '"'
		table.append(string)
	text = ''
	text += '{\n'
	text += ',\n'.join( table )
	text += '\n}'
	if p:
		_printME_(text)
	return text 

def pp(path):
	vc.FIG.home()
	path = path.replace( v.home, '~' )
	return path





def createDestinationFolders( folder, isFile=False, p=False ):


	

	thisSlash = os.sep
	slash = os.sep



	if isFile:

		f = folder.split(thisSlash)
		f.pop()
		folder = thisSlash.join( f )



	if os.path.isdir( folder ):
		return folder

	try:
		os.mkdir( folder )
		if p:
			_printME_( folder )
		return folder
	except Exception as e:
		pass

	parts = folder.split( slash )
	
	if not os.path.isdir( parts[0]+slash ):
		return folder
		# cp( 'Error: Destination drive does not exist', 'red' )

	newParts = []

	for p in parts:

		newParts.append( p )
		f = slash.join( newParts )
		exist = os.path.isdir( f )
		if not exist:
			try:
				os.mkdir( f )
			except Exception as e:
				pass
				# cp( [ 'Error: creating folder', f ], 'red' )
	return folder


class HEAD:

	def __init__( self ): pass;
 
 
 

	def bashFileHeader( self, path ):
 
 
 
		if v.isWin:
			return None
		if not os.path.isfile(path):
			return None
		vc.HD.chmod(path)
		newFile = ''
		fileChanged = False
		vc.HD.chmod(path)
		if vc.HD.headTXT(path).startswith('#!'):

			file = vc.HD.getText(path)
			if 'cat' in file[0] and not 'bash' in file[0]:
				newFile += '#!'+v.bash['CAT'] + '\n'
				if not newFile == file[0]:
					fileChanged = True
			elif 'python' in file[0] and not 'bash' in file[0]:
				pyVer=3
				if '3' in file[0]:
					fv = 3
				else:
					fv = 2

				p3 = '#!'+v.bash['PY'] + '\n'
				p2 = '#!'+v.bash['PY2'] + '\n'
				if 'installer.py2' in 'installer.py ':
					# print('ifa2 true')
					pyVer=2
					# newFile += '#!'+v.bash['PY2'] + '\n'
				else:
					if '2' in file[0]:
						pyVer=2
						# print('if2 true')
						# newFile += '#!'+v.bash['PY2'] + '\n'
					# else:
						# print('else3')
						# newFile += '#!'+v.bash['PY'] + '\n'
				if fv == 3:
					cp(['fv3',path],'cyan')
					newFile += p3
				else:
					cp(['fv2    ',path],'cyan')
					newFile += p2

				
				if not newFile == file[0]:

					fileChanged = True
			elif v.bash['SHELL'] and '#!/bin/bash' in file[0] and not v.bash['SHELL'] == v.bash_defaults['SHELL']:
				newFile += '#!'+v.bash['SHELL'] + '\n'
				if not newFile == file[0]:
					fileChanged = True
			if not len(newFile):
				newFile += file[0]
			
			pre = newFile
			newFile += ''.join(file[1:])
			if fileChanged:
				if ( 'python' in file[0] or 'python' in pre ) and ( '3' in file[0] and '2' in pre ):
					pass 
				else:
					cp( pp(path), 'yellow' )
					cp( ['from: ', file[0].replace( '\n', '' ).replace( chr(10), '' )], 'cyan' )
					cp( [' to: ', pre.replace( '\n', '' ).replace( chr(10), '' )], 'cyan' )
					# print(newFile)
					newFile = newFile.replace( chr(10), '\n' )
					newFile = newFile.replace( chr(27), '' )
					newFile = newFile.replace( '\r', '' )
					vc.HD.saveText( newFile, path )
		else:
			if path.endswith('.py'):
				file = vc.HD.getText(path)
				newFile += '#!'+v.bash['PY'] + '\n'
				newFile += ''.join(file)
				newFile = newFile.replace( chr(10), '\n' )
				newFile = newFile.replace( chr(27), '' )
				newFile = newFile.replace( '\r', '' )
				vc.HD.saveText( newFile, path )
			if path.endswith('.sh'):
				file = vc.HD.getText(path)
				newFile += '#!'+v.bash['SHELL'] + '\n'
				newFile += ''.join(file)
				newFile = newFile.replace( chr(10), '\n' )
				newFile = newFile.replace( chr(27), '' )
				newFile = newFile.replace( '\r', '' )
				vc.HD.saveText( newFile, path )
		pass
		vc.HD.chmod(path)




	def getFolderBH( self, folder ):
 
 
 
		if not os.path.isdir(folder):
			return None
		try:
			dirList = os.listdir(folder)
		except Exception as e:
			return None
		# i = 0
		for item in dirList:
			path = folder + os.sep + item
			if os.path.isfile(path):
				shouldProcess = True


				if shouldProcess:
					self.bashFileHeader(path)

			if os.path.isdir(path):
				if switches.isActive('Header-Fix-Folder-Recursive'):
					try:
						self.getFolderBH(path)
					except Exception as e:
						pass
	def asciiHeaderRun( self, header, p=1 ):
 
 
 
		global hex_header_chars
		global visibleChar
		hexHeader = []
		txtHeader = []
		txtSuffix = '.'
		txtSuffix = ''
		for hx in header.split(' '):
			x = ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])
			if x in visibleChar or x in hex_header_chars:
				if not x == '\r' and not x == '\n':
					if not x == '\r' and not x == '\n':
						if x in visibleChar:
							txtHeader.append( x )
						else:
							txtHeader.append( ' ' )
				if len(hexHeader) == 6:
					hexHeader.append( txtSuffix )
				elif len(hexHeader) < 6:
					hexHeader.append( hx )
			else:
				break
		if len( hexHeader ):
			return { 'ascii': ''.join(txtHeader), 'hex': ' '.join(hexHeader) }
		else:
			return { 'ascii': '', 'hex': '' }


class EXT:
	def __init__( self ): pass;
 
 
 

	def getFolderEXT( self, folder ):
 
 
 
		if not os.path.isdir(folder):
			return None
		try:
			dirList = os.listdir(folder)
		except Exception as e:
			return None
		# i = 0
		for item in dirList:
			path = folder + os.sep + item
			if os.path.isfile(path):
				shouldProcess = True


				if shouldProcess:
					self.fileEXT(path)

			if os.path.isdir(path):
				if switches.isActive('Folder-Extensions-Recursive'):
					try:
						self.getFolderEXT(path)
					except Exception as e:
						pass

	def fileEXT( self, path ):
 
 
 
		path = path.lower()
		parts = path.split(os.sep)
		parts.reverse()
		file = parts.pop(0)

		subject = self.getExt(file)
		if not subject in v.ext:
			v.ext[subject] = 0
		v.ext[subject] += 1
		# if not subject == '.py':
		# print( subject, file )

	def getExt( self, file ):
 
 
 
		parts = file.split('.')
		parts.pop(0)
		parts.reverse()
		split_ends = []
		for p in parts:
			if len(p) <= 4:
				split_ends.append(p)
			else:
				break
		split_ends.reverse()
		if not split_ends:
			subject = '-'

		subject = '.' + '.'.join(split_ends)
		for cl in v.folder_ext_wipe_pre.split(','):
			if cl in subject:
				xz = subject.split(cl)
				xz.pop(0)
				subject = cl
				for xy in xz:
					subject += xy
		for cl in v.folder_ext_final_suffix.split(','):
			if subject.endswith(cl):
				subject = cl
		return subject

class ONLINE:
	def __init__( self ):
		self.onStatus=0
		self.ip='0.0.0.0'
 
		
 

	def page( self, url ):
 
 
 
		requests = vc.FIG.imp('requests')
		if requests is None:
			return ''
		try:
			page = requests.get(url)
			page_code = str(page.text)
			self.onStatus=True
		except Exception as e:
			self.onStatus=False
			page_code=''
		page_code = page_code.replace( chr(10), '\n' )
		page_code = page_code.replace( chr(27), '' )
		page_code = page_code.replace( '\r', '' )
		return page_code


	def status( self ):
 
		loader()
 
		requests = vc.FIG.imp('requests')
		if requests is None:
			self.onStatus = None
			return self.onStatus

		url = 'http://tools.rightthumb.com/ip.php'
		if type(self.onStatus) == bool:
			return self.onStatus
		page_code = self.page(url)
		if not self.onStatus:
			return self.onStatus
		page_code = page_code.replace( '\n', '' )
		page_code = page_code.replace( ' ', '' )
		if len(page_code) > 6 and len(page_code) < 16:
			self.ip = page_code
			self.onStatus = True
		else:
			self.onStatus = False
		# print(self.ip)
		# print(self.onStatus)
		return self.onStatus



	def download_updates( self ):
 
 
 
		requests = vc.FIG.imp('requests')
		# print('here')
		vc.FIG.bash_vars(p=0)
		if not os.path.isdir(v.home +os.sep+ '.rt'):
			os.mkdir(v.home +os.sep+ '.rt')

		

		if self.status():
			cp( ['status:', self.onStatus], 'green' )
		else:
			cp( ['status:', self.onStatus], 'red' )
		if self.status():

			files = []
			files.append({ 'label': 'tool', 'path': v.home +os.sep+ '.rt' +os.sep+ 'tool', 'pre-exist': False })
			files.append({ 'label': 'tool.sh', 'path': v.home +os.sep+ '.rt' +os.sep+ 'tool.sh', 'pre-exist': False })
			files.append({ 'label': 'help.txt', 'path': v.home +os.sep+ '.rt' +os.sep+ 'help.txt', 'pre-exist': False })
			# rec = { 'label': 'bashrc.py', 'path': v.bash['widgets'] + '/widgets/python/bashrc.py', 'pre-exist': True }
			# rec['path'] = rec['path'].replace( '/', os.sep )
			# files.append(rec)
			rec = { 'label': 'load-vars.sh', 'path': v.bash['widgets'] + '/widgets/bash/load-vars.sh', 'pre-exist': True }
			rec['path'] = rec['path'].replace( '/', os.sep )
			files.append(rec)


			for rec in files:
				p = rec['path']
				l = rec['label']

				shouldProcess = False
				if not rec['pre-exist']:
					shouldProcess = True
				else:
					if os.path.isfile(rec['path']):
						shouldProcess = True
				if shouldProcess:
					
					if os.path.isfile(p):
						os.unlink(p)
					if not os.path.isfile( p ):
						_printME_()
						cp( [ 'downloading:', l ], 'yellow' )
						url = 'http://reph.us/tools/'+l
						page = requests.get(url)
						page_code = str(page.text)
						page_code = page_code.replace( chr(10), '\n' )
						page_code = page_code.replace( chr(27), '' )
						page_code = page_code.replace( '\r', '' )
						vc.HD.saveText( page_code, p )
						cp( [ 'saved:', p ], 'yellow' )
				else:
					_printME_(rec)

	download = download_updates
	
	# def reqPage( url ):
	#   page = requests.get(url)
	#   page_code = str(page.text)
	#   page_code = page_code.replace( chr(10), '\n' )
	#   page_code = page_code.replace( chr(27), '' )
	#   page_code = page_code.replace( '\r', '' )
	#   return page_code


class virtualFiles:
	def __init__( self ):
 
 
 
		self.files = {}
	def file( self, path, data=None, meta={} ):


 
 
 
		if data is None:
			if path in self.files:
				return self.files[path]
			elif not path in self.files:
				return self.myFile( path )
		elif not data is None:
			self.files[path] = { 'data': data, 'meta': meta }
			return self.files[path]

	def myFile( self, path ):
 
		c3po = vc.HD.getText( '/etc/hostname', raw=True, clean=2 )
		_printME_(c3po)
		c3po=c3po.split('.')[0]
		_printME_(c3po)
 


		if path == '.bashrc-auto':
			data = """

# echo 000-001

## .bashrc-auto
# 82977d555926
export env_='false'

# exit if scp or similar 4f8c
if [[ "$FORCE_BASHRC" != "true" ]]; then
  if [ -z "$PS1" ]; then
	return
  fi
fi


if test -f "$HOME/.bashrc-"; then
	source "$HOME/.bashrc-";
fi
if test -f "$HOME/.bashrc."; then
	source "$HOME/.bashrc.";
fi


# echo 000-002

if [ -z "$Session_ID" ]; then
  export Session_ID=$(date +%s)
fi

################# #################
alias beep.="play -nq -t alsa synth 1 sine 440"
################# ################# #################
# echo 000-003
[ -z "$pterm" ] && clear

		"""
			return self.file( path, data, { 'status': 'virtual' } )
		if path == '.bashrc-all':
			data = """
# echo 000-004
## .bashrc-all
# exit if scp or similar 4f8c
if [[ "$FORCE_BASHRC" != "true" ]]; then
  if [ -z "$PS1" ]; then
	return
  fi
fi
if test -f "$HOME/.bashrc-"; then
	source "$HOME/.bashrc-";
fi
if test -f "$HOME/.bashrc."; then
	source "$HOME/.bashrc.";
fi
# echo 000-005
if [ -z "$Session_ID" ]; then
  export Session_ID=$(date +%s)
fi
force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
	if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
	else
	color_prompt=
	fi
fi

EMOJIS=(THE_EMOJIS_GO_HERE)
prompt_symbol=${EMOJIS[$RANDOM % ${#EMOJIS[@]}]};
# echo 000-006



if [ -f /mnt/.chroot ]; then
	host_prefix="chroot: "
else
	host_prefix=""
fi
if [ "$color_prompt" = yes ]; then
	prompt_color='\\[\033[;32m\\]'
	info_color='\\[\033[1;34m\\]'
	if [ "$EUID" -eq 0 ]; then # Change prompt colors for root user
	prompt_color='\\[\033[;94m\\]'
	info_color='\\[\033[1;31m\\]'
	fi
	PS1=$prompt_color'\n┌──${debian_chroot:+($debian_chroot)──}($host_prefix'$info_color'\\u${prompt_symbol}\\h'$prompt_color')-[\\[\033[0;1m\\] \\w '$prompt_color'].20F54359E924\n'$prompt_color'└─'$info_color'\\$\\[\033[0m\\] '
else
	PS1='\n┌── (\\u${prompt_symbol}\\h)──[ \\w ].20F54359E924\\n└─── $ '
fi


unset color_prompt force_color_prompt
[ -z "$pterm" ] && clear

			"""
			data = data.replace( 'THE_EMOJIS_GO_HERE', v.emojis )
			return self.file( path, data, { 'status': 'virtual' } )
		if path == '.bashrc.mini':
			data = """
# bash -x
# echo 000-026
## .bashrc.mini


export START_TIME=$(date +%s.%N)

get_time_difference2() {
	local end_time=$(date +%s.%N)
	local elapsed_time=$(awk -v start=$START_TIME -v end=$end_time 'BEGIN { printf "%.9f", end - start }')
	echo "Time elapsed: $elapsed_time seconds"
}

get_time_difference() {
	local current_time=$(date +%s.%N)
	local elapsed_time=$(awk -v start=$START_TIME -v end=$current_time 'BEGIN { printf "%.9f", end - start }')
	echo "Time elapsed since last run: $elapsed_time seconds"
	START_TIME=$current_time # Update START_TIME for the next run
}

# echo 000-007
# exit if scp or similar 4f8c
if [[ "$FORCE_BASHRC" != "true" ]]; then
  if [ -z "$PS1" ]; then
	return
  fi
fi
if [ -z "$Session_ID" ]; then
  export Session_ID=$(date +%s)
fi
# echo 000-027
################# ################# ################# #################
[ ! -d $HOME/.rt ] && mkdir $HOME/.rt
[ ! -d $HOME/.rt/profile ] && mkdir $HOME/.rt/profile
[ ! -d $HOME/.rt/profile/temp ] && mkdir $HOME/.rt/profile/temp
touch $HOME/.rt/profile/temp/temp.exp
# chmod -R 777 $HOME/.rt/
# chmod 777 $HOME/.rt/profile/temp/temp.exp
################# ################# ################# #################
# echo 000-008
source $HOME/.rt/profile/vars/config.sh
touch $HOME/.rt/profile/vars/personal.sh
if [ -f "$HOME/.rt/profile/vars/personal.sh" ]; then
source $HOME/.rt/profile/vars/personal.sh
fi

source /opt/rightthumb-widgets-v0/widgets/bash/rc/mini.sh


# PROMPT_COMMAND='echo -ne "\\033]0;$( whoami ) $prompt_symbol """+c3po+""" \\007"'
export HISTSIZE=100000
export HISTFILESIZE=100000
# get_time_difference
# echo 000-028
[ -z "$pterm" ] && clear

			"""
			return self.file( path, data, { 'status': 'virtual' } )

		if path == '.bashrc.full':
			data = """
#9483b053a84b
# echo 000-019
## .bashrc.full
# exit if scp or similar 4f8c
if [[ "$FORCE_BASHRC" != "true" ]]; then
  if [ -z "$PS1" ]; then
	return
  fi
fi


if command -v python3.11 >/dev/null; then
	alias python3='python3.11'
	alias pip3='pip3.11'
fi



if [ -z "$Session_ID" ]; then
  export Session_ID=$(date +%s)
fi
# chmod -R 777 $HOME/.rt/
# echo 000-009
################# ################# ################# #################

source $HOME/.rt/profile/vars/config.sh
source $HOME/.rt/profile/vars/personal.sh

# echo 000-010

# echo 000-020

# get_time_difference
config="$wprofile/config"
unixID="$config/.unix_id"



if [ ! -e $config ]; then
	echo "0 no config"
	mkdir $config;
else
	unixID1=$(md5sum <<< "$(sed -n '1p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID2=$(md5sum <<< "$(sed -n '2p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID3=$(md5sum <<< "$(sed -n '3p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID4=$(md5sum <<< "$(sed -n '4p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID5=$(md5sum <<< "$(sed -n '5p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID6=$(md5sum <<< "$(sed -n '6p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID7=$(md5sum <<< "$(sed -n '7p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID8=$(md5sum <<< "$(sed -n '8p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID9=$(md5sum <<< "$(sed -n '9p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
	unixID10=$(md5sum <<< "$(sed -n '10p' < $unixID)$(cat /etc/machine-id)" | awk '{print $1}')
fi
# get_time_difference
if [ ! -e $unixID ]; then
	touch $unixID
fi


export p="sh $widgets/widgets/bash/nav/p.sh"
export bb="sh $widgets/widgets/bash/nav/bb.sh"
export b="sh $widgets/widgets/bash/nav/b.sh"
export m="sh $widgets/widgets/bash/nav/m.sh"
export cdf="sh $widgets/widgets/bash/cdf.sh"
export config
export widgets


# echo 000-021




export HISTSIZE=100000
export HISTFILESIZE=100000





export EDITOR='nano'
# export VISUAL='program'

# get_time_difference

alias rms='python3 $ww/python/secure-delete-file.py -f '

# PROMPT_COMMAND='echo -ne "\\033]0;$( whoami ) $prompt_symbol """+c3po+""" \\007"'
export HISTSIZE=100000
export HISTFILESIZE=100000

# echo 000-022
# if [ -z ${TERM} ]; then TERM=dumb; fi

# echo 000-011

alias myip='curl ifconfig.co/'
 

# export Session_ID=$(date +%s)





once_file=$HOME/.bashrc.once
once_file2=$HOME/.bashrc.once.log
if test -f "$once_file"; then
	source $once_file
	echo ___ >> $once_file2
	echo date >> $once_file2
	cat $once_file >> $once_file2
	rm $once_file

fi
personal_file=$HOME/.bashrc.always
if test -f "$personal_file"; then
	source $personal_file
fi
personal_file_print=$HOME/.bashrc.always.print
if test -f "$personal_file_print"; then
	echo ''
	$p print_color -line -color Background.green
	cat $personal_file_print
	$p print_color -line -color Background.green
	echo ''
fi
# echo 000-023
once_file_print=$HOME/.bashrc.once.print
if test -f "$once_file_print"; then
	echo ''
	$p print_color -line -color Background.green
	cat $once_file_print
	$p print_color -line -color Background.green
	echo ''
	rm $once_file_print
fi
if [ -f "$HOME/bashrc.sh" ]; then
source $HOME/bashrc.sh
fi

# get_time_difference
# echo 000-012

# if [ ! -f "$HOME/.files-rrr" ]; then
# 	echo "status" > $HOME/.files-rrr.
# 	if [ ! -d "/tmp/p_files-rrr" ]; then
# 		mkdir /tmp/p_files-rrr
# 	fi
# 	$p files -folder /var/empty -rrr > /dev/null 2>&1
# fi

# echo 000-024


alias .deb="sudo dpkg -i "

function o() {
	if [ -z "$1" ]; then
		$p file-open -backup secure -alias last
	else
		$p file-open -backup secure -alias "$@"
	fi
}

# get_time_difference
export isgui=false
g() {
	export isgui=true
	echo "isgui=true"
}
# echo 000-013
dl.mp4t() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp4t <URL>"
		return 1
	fi

	# Download the best video and audio streams with specific extensions
	youtube-dlc -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' "$url" &
}
# echo 000-025
dl.mp3t() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp3t <URL>"
		return 1
	fi

	# Download audio in MP3 format
	youtube-dlc -x --audio-format mp3 "$url" &
}
load() {
	source "$widgets/widgets/bash/vps-bashrc_extended.sh"
	# source "$widgets/widgets/bash/vps-bashrc_extended.sh" &> /dev/null
}
loada() {
	source "$widgets/widgets/bash/vps-bashrc_aliases.sh" &> /dev/null
}
# echo 000-014

####### wsl cron start
# Define the path to the marker file
marker_file="$HOME/.cron_started"

function has_file_been_modified_recently() {
	local file="$1"
	local hours="${2:-4}"  # Default to 4 hours
	local file_modification_time
	file_modification_time=$(stat -c %Y "$file" 2>/dev/null || echo 0)
	local current_time
	current_time=$(date +%s)
	local time_diff
	time_diff=$((current_time - file_modification_time))
	
	# Calculate the threshold time in seconds (N hours ago)
	local threshold=$((hours * 3600))
	
	# Check if the file has been modified in the last N hours
	[ "$time_diff" -le "$threshold" ]
}

if ! has_file_been_modified_recently "$marker_file" 5; then
	if [ -d "/mnt/c/Users/" ]; then
		sudo service cron start > /dev/null 2>&1 & 
		touch "$marker_file"
	fi
fi
alias cron.="sudo service cron start"
####### wsl cron end

source $widgets/widgets/bash/rc/full.sh


# echo 000-015
alias size.fi="du -h  "
alias size.f="du -sh "
alias size.d="df -h"
alias sizeFo="du -sh "
alias sizeDrive="df -h"
alias s.fi="du -h "
alias s.f="du -sh "
alias s.fo="du -sh "
alias s.d="df -h"
alias s.fo="du -sh "
alias s.fl="du -shL "

alias clip="xsel --clipboard"
alias pa="xsel --clipboard"
alias pa.="xsel --clipboard"
alias pa.="xsel --clipboard"
alias cp.="$p -copy"
alias aaa="works"
alias code.="/snap/bin/code"
alias lns="readlink -f "

alias dmg.="bash $widgets/widgets/bash/dmg.sh"
# alias java.="bash $widgets/widgets/bash/java.sh"
# alias java.dmg="bash $widgets/widgets/bash/java-mac-dmg.sh"
# alias java.pkg="bash $widgets/widgets/bash/java-mac-pkg.sh"
# alias java.exe="bash $widgets/widgets/bash/java-win-exe.sh"
# alias java.msi="bash $widgets/widgets/bash/java-win-msi.sh"
# alias java.deb="bash $widgets/widgets/bash/java-linux-deb.sh"
# alias java.rpm="bash $widgets/widgets/bash/java-linux-rpm.sh"
alias whitelist="bash $widgets/widgets/bash/whitelist.sh"
alias whitelist.r="bash $widgets/widgets/bash/whitelist-remove.sh"
alias whitelist.="bash $widgets/widgets/bash/vps-whitelistAuto.sh"
alias whitelist.a="bash $widgets/widgets/bash/vps-whitelistAuto.sh"
alias block="bash $widgets/widgets/bash/blocklist.sh"
alias block.r="bash $widgets/widgets/bash/blocklist-remove.sh"
export PATH=$PATH:$widgets/widgets/bash:$widgets/widgets/python

# echo 000-016

# # pyEnvironment - START
# file="$widgets/widgets/bash/load_pyEnvironment.sh"
# folder="$HOME/.pyEnvironment"

# if [ -f "$file" ]; then
#     source "$file"
# fi

# if [ -d "$folder" ]; then
#     :
# fi
# # testing
# # python3 -c "from Crypto.Cipher import Blowfish; print('Blowfish is available')"
# # instead run: setup-force.sh
# # pyEnvironment - END



function git_add_modified_files() {
	if [ -z "$1" ]; then
		$widgets/widgets/python/files.py  - minecraft.py vps- + *.py *.sh *.bat *.md *.ad *.ps1 -or  --c -ago 10h | p line --c -make "git add {}" | p execute
	else
		$widgets/widgets/python/files.py  - minecraft.py vps- + *.py *.sh *.bat *.md *.ad *.ps1 -or --c -ago "$1" | p line --c -make "git add {}" | p execute
	fi
}
generate_and_push() {
	tmpf=$(mktemp)
	$widgets/widgets/python/genuuid.py -e > "$tmpf"
	uuid=$(cat "$tmpf")
	git commit -m "$uuid"
	git push --force
	rm "$tmpf"
}
# echo 000-017
alias git.files="git_add_modified_files"
alias git.cp="generate_and_push"

alias burn="kill -9 $$"
alias est="date +%Z; sudo timedatectl set-timezone America/New_York; date +%Z"

alias zip.="$widgets/widgets/bash/micro_zip.sh"
alias zip.l="$widgets/widgets/bash/micro_zip_list.sh"
alias unzip.="$widgets/widgets/bash/micro_unzip.sh"
alias unzip.="$widgets/widgets/bash/micro_unzip.sh"
alias fi.cnt="find . -type f | wc -l"
alias fi.c="find . -type f | wc -l"
alias fo.cnt="find . -type d | wc -l"
alias fo.c="find . -type d | wc -l"
alias imgText="$widgets/widgets/bash/tesseract_image.sh"
alias imgt="$widgets/widgets/bash/tesseract_image.sh"
alias imgtxt="$widgets/widgets/bash/tesseract_image.sh"
alias it="$widgets/widgets/bash/tesseract_image.sh"
alias movieTablet="$widgets/widgets/bash/movie_tablet.sh"
alias moviePhone="$widgets/widgets/bash/movie_phone.sh"

alias pip3.="pip3 install --upgrade --no-cache-dir --break-system-packages"
alias flushdns="sudo systemctl restart systemd-resolved"
alias set.="(set -o posix; set)"
# echo 000-018

tmux_exec_bg() {
	if [ "$#" -ne 2 ]; then
		echo "Usage: tmux_exec_bg <session-name> <command>"
		return 1
	fi

	local session="$1"
	local cmd="$2"

	tmux new-session -d -s "$session" "$cmd"
}

tmux_exec_fg() {
	if [ "$#" -ne 2 ]; then
		echo "Usage: tmux_exec_fg <session-name> <command>"
		return 1
	fi

	local session="$1"
	local cmd="$2"

	tmux new-session -s "$session" "$cmd"
}


# pa | p line + alias --c | p line -p = 0 --c | p line -p " " 1
#####################################################################
# TMUX Session Management
alias tr="tmux_exec_fg"            # Run a command in a new TMUX session, in the forground
alias trb="tmux_exec_bg"           # Run a command in a new TMUX session, in the background
alias tn="tmux new-session -s"     # Create a new TMUX session
alias td="tmux detach"             # Detach from the current session
alias tl="tmux list-sessions"      # List all TMUX sessions
alias tls="tmux ls"                # Same as tl, optional to keep both
alias ta="tmux attach-session -t"  # Attach to an existing session
alias tk="tmux kill-session -t"    # Kill a specific TMUX session
alias tsrv="tmux kill-server"      # Kill the TMUX server
alias tkill="tmux list-sessions | grep -v attached | cut -d: -f1 | xargs -I {} tmux kill-session -t {}"  # Kill all unattached sessions

# TMUX Window and Pane Management
alias tsh="tmux split-window -h"   # Split the current pane horizontally
alias tsv="tmux split-window -v"   # Split the current pane vertically
alias tsp="tmux select-pane -t"    # Select a specific pane
alias tsw="tmux select-window -t"  # Select a specific window
alias tsl="tmux select-layout"     # Select a predefined layout for the current window

# TMUX Interaction
alias tsk="tmux send-keys -t"      # Send keys to a specific pane, simulating keyboard input
  # Example usage: tmux send-keys -t mysession:0.1 'ls -l' C-m
  # C-m is the Enter key.
  # https://sds.sh/tmux-send_key-examples
	
# TMUX Template Management
alias t4="source $widgets/widgets/bash/tmux/templates/4_Square.sh"
alias tq="source $widgets/widgets/bash/tmux/templates/Quadrants.sh"
alias ts="source $widgets/widgets/bash/tmux/templates/Single.sh"
alias t1="source $widgets/widgets/bash/tmux/templates/Single.sh"
alias ths="source $widgets/widgets/bash/tmux/templates/Horizontal_Stripes.sh"
alias t13="source $widgets/widgets/bash/tmux/templates/One_Three.sh"
alias ttop="source $widgets/widgets/bash/tmux/templates/Top_Large_Pane_with_Three_Columns_Below.sh"
alias tt="source $widgets/widgets/bash/tmux/templates/Top_Large_Pane_with_Three_Columns_Below.sh"
#####################################################################
#####################################################################


export Bash="$widgets/widgets/bash"
export BASH="$widgets/widgets/bash"
export B="$widgets/widgets/bash"

alias drive.s="find / -type f -size"
alias drive.s.10g="find / -type f -size +10737418240"
alias drive.s.1g="find / -type f -size +1073741824"

_title() {
	echo -ne "\033]0;$1\007"
}

alias shell="source $widgets/widgets/bash/shell.sh"
alias ovpn="source $widgets/widgets/bash/openvpn_manager.sh"
alias ovpn.="source $widgets/widgets/bash/openvpn_manager.sh"
alias ...ssh="rm -rf $HOME/.ssh/*; ssh-keygen -t rsa -b 4096"
alias ..ssh..="$widgets/widgets/bash/srv/MISC/ssh.sh"


if [ -f "${stmp}/pin_ask" ]; then
	source $widgets/widgets/bash/pin.sh
fi

alias o="source $widgets/widgets/bash/nav/o.sh"
alias fileCount="python3 $widgets/widgets/python/fileCount.py"
alias fC="python3 $widgets/widgets/python/fileCount.py"

alias iso="source $widgets/widgets/bash/iso_img_bin_nrg_mdf__info.sh"
alias pst="source $widgets/widgets/bash/pst.sh"


alias p="$p"




alias d='$widgets/widgets/bash/nav/d.sh'
alias rr="sudo su root"

if [ ! -d "$h/widgets/python" ]; then
	mkdir "$h/widgets/python"
fi

export mp="bash $widgets/widgets/bash/nav/mp.sh"
alias mp="$mp"

alias dt="ssh -L 59001:localhost:5901 -C -N -l scott"

dtdt() {
	ssh -L 59001:localhost:5901 -C -N -l scott "$1" &
}

mp4() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp4t <URL>"
		return 1
	fi

	# Download the best video and audio streams with specific extensions
	youtube-dlc -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' "$url" &
}

mp3() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp3t <URL>"
		return 1
	fi

	# Download audio in MP3 format
	youtube-dlc -x --audio-format mp3 "$url" &
}

alias dt.="dtdt"
alias dt.k="kill -9 $(lsof -ti :59001)"
alias k="kill -9"
alias ai="$p ai -prompt"
alias ai.t="$p ai -prompt what is the tmux shortcut for"

alias tmux.="curl -s https://sds.sh/tmux-aliases | $p line --c +"
alias tmux..="curl -s https://sds.sh/tmux-aliases | $p line --c "

alias ..b='cd /opt ; cd rightthumb-widgets-v0 ; m w ; cd install/ ; m in ; cd .. ; cd widgets/ ; m ww ; cd python/ ; m py ; cd .. ; cd bash/ ; m b ; m bash ; cd 101; m 101; cd ..; cd .. ; cd databank/ ; m db ; cd tables/ ; m ttt ; cd ; cd .rt ; m rt ; cd profile/ ; m h ; cd tables/ ; m tt ; cd .. ; cd config/ ; m config ; m c ; cd .. ; cd projects/ ; m pr ; cd'

alias on.run='while true; do $p on; sleep 1; done'
alias on.fi="$widgets/widgets/bash/on.fi.sh"
alias on.fo="$widgets/widgets/bash/on.fo.sh"
alias on="$widgets/widgets/bash/on.sh"
alias listZip="$widgets/widgets/bash/list_zip.sh"

export Session_ID_Suffix=${Session_ID:4:5}

alias sync.="$widgets/widgets/bash/srv/sync.sh"

sshssh() {
	local who=${2:-scott}
	ssh-copy-id -i ~/.ssh/id_rsa.pub "$who@$1.sds.sh"
}

alias bb.="bleachbit --clean system.cache"
alias bleachbit.="bleachbit --clean system.cache"
alias ssh...='rm -rf ~/.ssh; ssh-keygen -t rsa'
alias x.="exit"




#####################################################################
mp4() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp4t <URL>"
		return 1
	fi

	# Download the best video and audio streams with specific extensions
	youtube-dlc -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' "$url" &
}

mp3() {
	local url="$1"

	# Check if a URL was provided
	if [ -z "$url" ]; then
		echo "Usage: dl.mp3t <URL>"
		return 1
	fi

	# Download audio in MP3 format
	youtube-dlc -x --audio-format mp3 "$url" &
}
#####################################################################



up_date() {
	echo "🔍 Detecting system and package manager..."

	has_sudo() {
		command -v sudo >/dev/null 2>&1 && sudo -n true 2>/dev/null
	}

	if command -v apt-get >/dev/null 2>&1; then
		echo "📦 APT (Debian/Ubuntu)"
		sudo apt-get update -y && sudo apt-get upgrade -y

	elif command -v pacman >/dev/null 2>&1; then
		echo "📦 pacman (Arch, Manjaro, MSYS2)"
		if has_sudo; then
			echo "🔐 Running with sudo"
			sudo pacman -Syu --noconfirm
		else
			echo "⚠️ sudo not available — running pacman without it"
			pacman -Syu --noconfirm
		fi

	elif command -v dnf >/dev/null 2>&1; then
		echo "📦 DNF (Fedora/Alma/RHEL)"
		sudo dnf upgrade --refresh -y
		if command -v yum >/dev/null 2>&1; then
			echo "📦 Also running YUM (compatibility layer)"
			sudo yum update -y
		fi

	elif command -v yum >/dev/null 2>&1; then
		echo "📦 YUM (Older RHEL/CentOS)"
		sudo yum update -y

	elif command -v zypper >/dev/null 2>&1; then
		echo "📦 zypper (openSUSE)"
		sudo zypper refresh && sudo zypper update -y

	elif command -v apk >/dev/null 2>&1; then
		echo "📦 apk (Alpine Linux)"
		sudo apk update && sudo apk upgrade

	elif command -v xbps-install >/dev/null 2>&1; then
		echo "📦 xbps (Void Linux)"
		sudo xbps-install -Syu

	elif command -v emerge >/dev/null 2>&1; then
		echo "📦 emerge (Gentoo)"
		sudo emerge --sync && sudo emerge -avuDN @world

	elif command -v nix-env >/dev/null 2>&1; then
		echo "📦 Nix (NixOS)"
		nix-channel --update && nix-env -u '*'

	elif command -v brew >/dev/null 2>&1; then
		echo "🍏 Homebrew (macOS/Linuxbrew)"
		brew update && brew upgrade

	elif command -v pkg >/dev/null 2>&1 && uname | grep -qi "bsd"; then
		echo "📦 pkg (FreeBSD)"
		sudo pkg update && sudo pkg upgrade -y

	elif command -v flatpak >/dev/null 2>&1; then
		echo "📦 flatpak"
		flatpak update -y

	else
		echo "❌ No supported package manager found."
		return 1
	fi

	if command -v snap >/dev/null 2>&1; then
		echo "📦 snap"
		sudo snap refresh
	fi

	echo "✅ Update complete."
}
#####################################################################
run_bash_url() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: bash.. <URL> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "$first_arg" | bash -s -- "$@"
}
alias b..="run_bash_url"
alias bash..="run_bash_url"

run_python_url() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: py.. <URL> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "$first_arg" | python3 - "$@"
}
alias py..="run_python_url"
alias p..="run_python_url"



run_python_url_sds() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: py. <alias> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "https://u.sds.sh/$first_arg" | python3 - "$@"
}
alias py.="run_python_url_sds"
alias p.="run_python_url_sds"

run_bash_url_sds() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: bash. <alias> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "https://u.sds.sh/$first_arg" | bash -s -- "$@"
}
alias bash.="run_bash_url_sds"
alias b.="run_bash_url_sds"



run_python_url_shell_sds() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: py.. <alias> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "https://shell.sds.sh/?f=py/$first_arg" | python3 - "$@"
}
alias py.sds="run_python_url_shell_sds"
alias p.sds="run_python_url_shell_sds"
alias py.s="run_python_url_shell_sds"
alias p.s="run_python_url_shell_sds"

run_bash_url_shell_sds() {
	if [ "$#" -lt 1 ]; then
		echo "Usage: bash.. <alias> [arg1 arg2 ...]"
		return 1
	fi
	first_arg="$1"
	shift
	curl -s -L -k "https://shell.sds.sh/?f=sh/$first_arg" | bash -s -- "$@"
}
alias bash.sds="run_bash_url_shell_sds"
alias b.sds="run_bash_url_shell_sds"
alias bash.s="run_bash_url_shell_sds"
alias b.s="run_bash_url_shell_sds"
#####################################################################

alias fi.en="p cryptFile -vault -r -en -f "
alias fi.de="p cryptFile -vault -r -de -f "




alias aes="p aes"
alias if.="p Import-Module-Functions -i"



alias php='/usr/local/bin/php'
alias wp="php /usr/local/bin/wp.phar"
alias dex="p search-indexDB-files -db"
alias dex="$p search-indexDB-files -db"
export dex="$p search-indexDB-files -db"
alias dex.="p indexDB-files"
alias sqlite="sqlite3"

alias sshp="echo 'ssh -L 59001:localhost:5901 -C -N -l scott teth.sds.sh'"

sshr() {
	local host="$1"

	if [[ -z "$host" ]]; then
		echo "Usage: remove_ssh_known_host <hostname or IP>"
		return 1
	fi

	# Remove entry from known_hosts
	ssh-keygen -R "$host"

	# Optional: Remove any hashed entries (if hashed SSH keys are used)
	sed -i.bak "/^|1|/d" ~/.ssh/known_hosts

	echo "Removed $host from ~/.ssh/known_hosts."
}



alias rc.="curl -s -o $HOME/.bashrc_sds -L -k https://u.sds.sh/bashrc; chmod +x $HOME/.bashrc_sds; source $HOME/.bashrc_sds"


alias file="$widgets/widgets/bash/vps-file-documentation.sh"


tess() {
	local imagePath="$1"
	local imagePath2="${imagePath%.*}_converted.png"

	convert -density 300 "$imagePath" -units PixelsPerInch "$imagePath2"
	tesseract "$imagePath2" stdout
}


alias _figlet='$ww/bash/_figlet.sh'
alias _figlet_='$ww/bash/_figlet_.sh'
alias _cowsay='$ww/bash/_cowsay.sh'


alias dex='python3 $ww/python/search-indexDB-files.py'
alias dex.='python3 $ww/python/indexDB-files.py'
alias mem="free -h"


alias .bash="bash --norc --noprofile"

alias exec='$widgets/widgets/bash/vps-______________execute_on_all_servers.sh'

alias f='$widgets/widgets/bash/nav/c.sh'


alias ob="p script-helper -i"
alias obb="p script-helper -t r:_.al -i"

alias vps-="/usr/bin/python3 $widgets/widgets/python/files.py + vps- -folders /opt/rightthumb-widgets-v0/"

export Session_ID=$(date +%s)



url() {
  if [ -z "$1" ]; then
	echo "Usage: smartpath_remote <argument>"
	return 1
  fi

  ssh root@teth.sds.sh "/bin/python3 $widgets/widgets/python/smartpath.py -f \"$1\""
}

if test -f "$HOME/.bashrc-"; then
	source "$HOME/.bashrc-";
fi
if test -f "$HOME/.bashrc."; then
	source "$HOME/.bashrc.";
fi

if test -f "/home/.bashrc."; then
	source "/home/.bashrc.";
fi

alias px="python3"

alias social="p vps-scan-social-media"


alias ui='$widgets/widgets/bash/universal-install.sh'

alias wget-s="wget -q -O - "

alias pacman.="pacman -Sy --noconfirm"



alias Ssh="ssh-copy-id -i ~/.ssh/id_rsa.pub "

MC() {
	python3 $ww/python/line.py -make "$@" 
}

MX() {
	python3 $ww/python/line.py -make "$@" | python3 $ww/python/execute.py
}

clean_yaml() {
	cat "$1" | tr -d '\r\033' | sed 's/^\xEF\xBB\xBF//' > "$1.cleaned" && mv "$1.cleaned" "$1"
}


get_content_type() {
	local url="$1"
	if [ -z "$url" ]; then
		echo "Usage: get_content_type <URL>"
		return 1
	fi
	curl -s -D - -o /dev/null -L "$url" | grep -i '^Content-Type:' | cut -d';' -f1 | sed 's/^[Cc]ontent-[Tt]ype: //'
}


alias curl..="get_content_type"



alias .mx='MX'
alias .mc='MC'

alias ..cat="/usr/bin/python3 $widgets/widgets/python/cat.py"
alias ..c="/usr/bin/python3 $widgets/widgets/python/cat.py"
alias .cat="/usr/bin/python3 $widgets/widgets/python/cat.py -f"
alias .c="/usr/bin/python3 $widgets/widgets/python/cat.py -f"
alias j='sh $widgets/widgets/bash/nav/p.sh'

alias up.date="up_date"

# source $widgets/widgets/bash/rc/full.sh
# source $widgets/widgets/bash/rc/full.sh
# source $widgets/widgets/bash/rc/full.sh

alias 101="python3 $ww/python/file.py -folder $ww/bash/101 -a"

alias who.f="stat -c '%A %U %G %u %g %n'"

alias os="cat /etc/os-release"
alias curl-="curl -sLk"
alias curl.="curl -sLk"


## p tag-cycle ## dos2unix

[ -z "$pterm" ] && clear

alias pid="ps aux | grep "

alias name.="sudo hostnamectl set-hostname "
alias name..="sudo nano /etc/hosts"

alias host.="sudo hostnamectl set-hostname "
alias host..="sudo nano /etc/hosts"

# alias pp="realpath -- "
alias pp="$p pp -f"

alias bg.="cat $widgets/widgets/bash/background.txt"

# get_time_difference
alias chats="$p gptChats"





alias dig.="dig +short "




schema() {
	local db="${1:-index.db}"
	sqlite3 "$db" .schema
}

alias gpt="p gpt -p "


alias .rc.="source $HOME/.bashrc"
alias ..rc="source $HOME/.bashrc"
alias brc="source $HOME/.bashrc"
alias ref="source $HOME/.bashrc"

alias ccat="$p cat -f "
alias o.a="$p file-open -ap -a "
alias resolve="$p resolveIDs3 "

export COLORTERM=truecolor
export TERM=xterm-256color
alias del="rm -rf"
alias move="mv"



# top: 9483b053a84b
# a3bc42ec51e9

			"""
			# echo "alias rr='sudo su root'" >> ~/.bashrc
			return self.file( path, data, { 'status': 'virtual' } )
			


class Bookmarks:
	def __init__( self ):
		self.table = {}
	def b( self, alias ):
		self.load()
		if alias in self.table['labels']:
			path = self.table['labels'][alias]
			path = vc.FIG.path_resolve(path)
			path = path.replace( os.sep+os.sep, os.sep )
			path = vc.PATHS.path(path)
			return 
		return ''

	def m( self, alias, path=None ):
		self.load()
		if path is None:
			path = os.getcwd()
		else:

			path = vc.FIG.path_resolve(path)


		if os.path.isdir(path) or os.path.isfile(path):
			cp( [ alias, '=', path ], 'cyan' )
			path = path.replace( os.sep+os.sep, os.sep )
			path = vc.PATHS.path(path)
			path = vc.FIG.path_secure(path)
			# print(path)
			self.table['labels'][alias] = path
			if not path in self.table['paths']:
				self.table['paths'][path] = []
			self.table['paths'][path].append(alias)
			# vc.EXIT.onExit( self.save, 'bm-save' )
			self.save()
		
	def load( self ):
		if not self.table:
			self.table = vc.HD.getTable( 'bookmarks.index' )
		if not self.table:
			self.table = {
							'labels': {},
							'paths': {},
			}

	def save( self ):
		vc.HD.saveTable( self.table, 'bookmarks.index' )


		# vc.FIG.save_bashrc( code, b='455B6DCC5737', e='6198DDC12140' )


# 

		# cp( [ 'saved:', 'bookmarks.index' ], 'cyan' )

	def structure( self ):
 
 
 
		folders = [
						v.home +os.sep+ '.rt',
						v.home +os.sep+ '.rt' +os.sep+ 'profile',
						v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'tables',
						v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'temp',
						v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'projects',
						v.home +os.sep+ '.rt' +os.sep+ 'profile' +os.sep+ 'vars',
		]
		for folder in folders:
			v.f.mkdir(folder)
		pass



class DATE:
	def __init__( self ): pass;
 
 
 

	tz = str(time.strftime("%z")).replace(':','')

	def epoch( self, stamp ):
 
 
 
		return str(datetime.datetime.fromtimestamp(stamp).strftime('%c'))

	def friendlyDate2( self, theDate ):
 
 
 
		fd = self.friendlyDate( theDate )
		if type(fd) == str and len(fd):
			fd = fd[:-3][2:]
			# if fd.startswith('21-'):
			# fd = fd[3:]
		return fd


	def friendlyDate( self, theDate ):
 
 
 
		try:
			return self.resolveEpoch( float(theDate) )
		except Exception as e:
			try:
				return self.resolveEpoch( self.autoDate( str(theDate) ) )
			except Exception as e:
				return vc.Color.red + 'error: self.friendlyDate()' + vc.Color.end
				# return colorThis( [ 'error: self.friendlyDate()' ], 'red' )
				# return 'error: self.friendlyDate()'

	def friendlyDateTouch( self, theDate ):
 
 
 
		xyz = self.friendlyDate(theDate)
		# 2020-12-29 07:40:16
		partsA = xyz.split(' ')
		a = partsA[0].replace('-', '')
		partsB = partsA[1].split(':')
		a = a + partsB[0] + partsB[1] 
		return int(a)
	def resolveEpoch( self, string, test=1, showPrint=False, showPrintTry=False, onlyEpoch=True, delim='-', falseBlank=False ):
 
 
 
		# onlyEpoch = True, False, 'day' 

		auto = self.autoDate( string )
		if not type( auto ) == bool:
			string = auto


		rData = False

		try:
			float( string )
		except Exception as e:
			test = 0

		word = string
		if test == 1:

			if showPrintTry:
				_printME_( 'try:', 1 )
			try:
				if showPrint:
					_printME_( 'success:', 1 )
				result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
				epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
				rData = [ result, epoch ]
			except Exception as e:
				pass
				rData = self.resolveEpoch( string, 2, showPrint, showPrintTry, onlyEpoch, delim )
		

		if test == 2:

			if showPrintTry:
				_printME_( 'try:', 2 )
			try:
				if showPrint:
					_printME_( 'success:', 2 )
				result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(word)/1000.))) + ' } } '
				epoch = str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(word)/1000.)))
				rData = [ result, epoch ]
			except Exception as e:
				pass
				rData = self.resolveEpoch( string, 3, showPrint, showPrintTry, onlyEpoch, delim )



		if test == 3:

			if showPrintTry:
				_printME_( 'try:', 3 )
			try:
				if showPrint:
					_printME_( 'success:', 3 )
				result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)/1000.)) + ' } } '
				epoch = str(datetime.datetime.fromtimestamp(float(word)/1000.))
				rData = [ result, epoch ]
			except Exception as e:
				pass
				rData = self.resolveEpoch( string, 4, showPrint, showPrintTry, onlyEpoch, delim )


		if test == 4:

			if showPrintTry:
				_printME_( 'try:', 4 )
			try:
				if showPrint:
					_printME_( 'success:', 4 )
				result = ' { { ' + str(time.ctime(float(word))) + ' } } '
				epoch = str(time.ctime(float(word)))
				rData = [ result, epoch ]
			except Exception as e:
				pass
				rData = self.resolveEpoch( string, 5, showPrint, showPrintTry, onlyEpoch, delim )



		if test == 5:

			if showPrintTry:
				_printME_( 'try:', 5 )
			try:
				if showPrint:
					_printME_( 'success:', 5 )
				result = ' { { ' + str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(word)/1000.))) + ' } } '
				epoch = str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(word)/1000.)))
				rData = [ result, epoch ]
			except Exception as e:
				pass
				rData = self.resolveEpoch( string, 6, showPrint, showPrintTry, onlyEpoch, delim )

		if test == 6:

			if showPrintTry:
				_printME_( 'try:', 6 )
			try:
				if showPrint:
					_printME_( 'success:', 6 )
				result = ' { { ' + str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S')) + ' } } '
				epoch = str(datetime.datetime.fromtimestamp(float(word)).strftime('%Y-%m-%d %H:%M:%S'))
				rData = [ result, epoch ]
			except Exception as e:
				pass

		if not type( rData ) == bool:
			if not type( onlyEpoch ) == bool:
				rData = rData[1].split(' ')[0].replace( '-', delim )
			elif onlyEpoch == True:
				rData = rData[1].replace( '-', delim )
			else:
				rData[1] = rData[1].replace( '-', delim )

		if falseBlank and type( rData ) == bool:
			rData = ''
		return rData



	def formatDate( self, date ):
 
 
 
		theDate = datetime.datetime.fromtimestamp( float(date) ).strftime('%Y.%m.%d-%H.%M-%S')
		# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
		theDate = str(theDate)
		return theDate

	def epoch2TextTimestamp( self, date ):
 
 
 
		date = str( date )
		try:
			theDate = self.formatDate( date )
		except Exception as e:
			if not '.' in date and len( date ) > 10:
				nDate = int( date )
				date = nDate / 1000
			theDate = datetime.datetime.fromtimestamp( float(date) ).strftime('%Y.%m.%d-%H.%M-%S')
			# theDate = datetime.datetime.fromtimestamp( int(date) ).strftime('%Y-%m-%d %H:%M:%S')
		theDate = str(theDate)
		return theDate


	def date2epoch( self, theDate, delim='-' ):
 
 
 
		theDate = str(theDate)
		theDate = theDate.replace(delim,'-')
		fdtl = theDate.split(delim)
		try:
			stmp = datetime.date(int(fdtl[0]), int(fdtl[1]), int(fdtl[2]))
			result = float(time.mktime(stmp.timetuple()))
		except Exception as e:
			try:
				stmp = datetime.date(int(fdtl[2]), int(fdtl[0]), int(fdtl[1]))
				result = float(time.mktime(stmp.timetuple()))
			except Exception as e:
				result = False
		
		# stmp = datetime.datetime.strptime(theDate, '%Y-%m-%d')
		return result




	def hasYear( self, data ):
 
 
 
		foundYear = False
		for x in vc.STR.singlDelim( data ).split('-'):
			if vc.STR.isInt( x ) and len( x ) == 4:
				if int( x ) > 1000:
					foundYear = True
		return foundYear


	def hasWeekday( self, data ):
 
 
 
		data = str( data )
		data = data.lower()
		setA = 'sun mon tue wed thu fri sat'.split(' ')
		setB = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.lower().split(' ')

		result = False
		for i,test in enumerate(setA):
			if setA[i] in data or setB[i] in data:
				result = True
		return result

	def hasTextMonth( self, data ):
 
 
 
		data = str( data )
		data = data.lower()
		setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
		setB = 'January February March April May June July August September October November December'.lower().split(' ')

		result = False
		for i,test in enumerate(setA):
			if setA[i] in data or setB[i] in data:
				result = True
		return result

	def isWeekday( self, data ):
 
 
 
		data = str( data )
		data = data.lower()
		setA = 'sun mon tue wed thu fri sat'.split(' ')
		setB = 'Sunday Monday Tuesday Wednesday Thursday Friday Saturday'.lower().split(' ')

		result = False
		for i,test in enumerate(setA):
			if data == setA[i] or data == setB[i]:
				result = True
		return result


	def isMonth( self, data ):
 
 
 
		data = str( data )
		data = data.lower()
		setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
		setB = 'January February March April May June July August September October November December'.lower().split(' ')

		result = False
		for i,test in enumerate(setA):
			if data == setA[i] or data == setB[i]:
				result = True
		return result

	def month2Number( self, data ):
 
 
 
		data = str( data )
		data = data.lower()
		setA = 'jan feb mar apr may jun jul aug sep oct nov dec'.split(' ')
		setB = 'January February March April May June July August September October November December'.lower().split(' ')

		result = False
		for i,test in enumerate(setA):
			if data == setA[i] or data == setB[i]:
				result = i+1
		return vc.STR.padZero(result)

	def removeDayOfWeek( self, data, delim='-' ):
 
 
 
		data = str( data )
		if self.hasWeekday( data ):
			result = ''
			for row in data.split(delim):
				if not self.isWeekday( row ):
					result += row + delim
			data = vc.STR.removeDuplicates( result, delim )
			data = vc.STR.stripDelimBE( data, delim )


		return data
	def isYear( self, data ):
 
 
 
		result = False
		data = str(data)
		if vc.STR.isInt( data ) and len( data ) == 4:
			result = True
		return result
	def validDay( self, data ):
 
 
 
		result = False
		data = str(data)
		if vc.STR.isInt( data ):
			if int( data ) < 32:
				result = True
		return result

	def cleanDate( self, data, delim='-' ):
 
 
 
		data = str(data)
		if delim in data:

			y = False
			m = False
			d = False
			sData = data.split(delim)
			if self.isMonth( sData[0] ):
				m = self.month2Number( sData[0] )
				if self.isYear( sData[1] ):
					y = sData[1]
					if self.validDay( sData[2] ):
						d = sData[2]
					
				if self.isYear( sData[2] ):
					y = sData[2]
					if self.validDay( sData[1] ):
						d = sData[1]
			if self.isMonth( sData[1] ):
				m = self.month2Number( sData[1] )

				if self.isYear( sData[0] ):
					y = sData[0]
					if self.validDay( sData[2] ):
						d = sData[2]
					
				if self.isYear( sData[2] ):
					y = sData[2]
					if self.validDay( sData[0] ):
						d = sData[0]
			if not type( y ) == bool and not type( m ) == bool and not type( d ) == bool:
				sData[0] = y
				sData[1] = m
				sData[2] = d
				result = ''
				for row in sData:
					result += row + delim
				data = vc.STR.removeDuplicates( result, delim )
				data = vc.STR.stripDelimBE( data, delim )
		return data



	def address24Hr( self, data, hr, delim='-' ):
 
 
 
		data = str(data)
		if hr == 12:
			sData = data.split(delim)
			if len( sData ) == 5 or len( sData ) == 4:
				result = ''
				for i,row in enumerate(sData):
					if i == 3 and vc.STR.isInt( row ):
						row = str( int( row ) + 12 )
					result += row + delim
				data = vc.STR.removeDuplicates( result, delim )
				data = vc.STR.stripDelimBE( data, delim )
		return data


	def autoDate( self, data, theFormat=False, fail=False ):
 
 
 
		if type(data) == float:
			return data
		try:
			if 'T' in data:
				data = data.replace( 'T', ' ' )
		except Exception as e:
			pass
			# print( data )
		try:
			if '+' in data:
				data = data.split('+')[0]
		except Exception as e:
			pass

		try:
			float(data)
			return False
		except Exception as e:
			pass

		originalData = data
		data = str( data )
		if not vc.STR.hasInt( data ):
			if fail:
				_printME_( 'Error: not a date', 0 )
				sys.exit()
			data = False
		data = vc.STR.singlDelim( data )
		data = data.lower()
		data = data.replace( 't', '-' )
		data = data.replace( 'at', '-' )
		hr = 24
		if 'pm' in data:
			hr = 12
		data = data.replace( 'am', '' ).replace( 'am', '' )
		data = vc.STR.removeDuplicates( data )
		data = vc.STR.stripDelimBE( data )
		data = self.removeDayOfWeek( data )
		data = self.cleanDate( data )
		delims = vc.STR.findDelims( data )
		
		# print(data)
		if type( theFormat ) == bool and not vc.STR.hasAlpha( data ):
			if len( delims ) == 0:
				if not vc.STR.isEpoch( data ):
					if fail:
						_printME_( 'Error: not a date', 1 )
						sys.exit()
					data = False
				else:
					data = str( int( data ) / 1000 )
			elif vc.STR.isEpoch( data ):
				data
				
			else:
				if not self.hasYear( data ):
					if fail:
						_printME_( 'Error: not a date', 2 )
						sys.exit()
					data = False
				else:
					if len( delims ) == 2:
						# print('here')
						data = self.date2epoch( data, delims[0] )
						if fail and type(data) == bool:
							_printME_( 'Error: not a date', 3 )
							sys.exit()

					elif len( delims ) == 5:
						sData = data.split('-')
						try:
							test = datetime.datetime.strptime( self.address24Hr( data, hr ), '%Y-%m-%d-%H-%M-%S' )
							data = test.timestamp()
						except Exception as e:
							if fail:
								_printME_( 'Error: not a date', 4 )
								sys.exit()
							data = False
					elif len( delims ) == 4:
						sData = data.split('-')
						try:
							test = datetime.datetime.strptime( self.address24Hr( data, hr ), '%Y-%m-%d-%H-%M' )
							data = test.timestamp()
						except Exception as e:
							if fail:
								_printME_( 'Error: not a date', 5 )
								sys.exit()
							data = False
					else:
						if fail:
							_printME_( 'Error: not a date', 6 )
							sys.exit()
						data = False

		if not type( data ) == bool:
			if vc.STR.isFloat( data ):
				data = float( data )

		return data 



	def isDate( self, theDate, record={}, tz=None ):
 
 
 

		if not tz is None and not len(tz):
			tz = None


		local_tz = str(time.strftime("%z")).replace(':','')

		hasTZ = False
		if type(theDate) == str and len(theDate) > 11:
			if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
				hasTZ = theDate[-6:].replace(':','')

		if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
			if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
				hasTZ = theDate[-5:].replace(':','')








		epoch = self.autoDate(theDate)


		if not type(hasTZ) == bool:
			if not hasTZ == local_tz:
				epoch = self.tzconvert( epoch, hasTZ, local_tz )

		if not tz is None and not local_tz == tz:
			epoch = self.tzconvert( epoch, local_tz, tz )
			local_tz = tz


			if '/' in tz:

				arrow = vc.FIG.imp('arrow')
				utc = arrow.utcnow()
				theDate = str(utc.to(tz))
				hasTZ = False
				if type(theDate) == str and len(theDate) > 11:
					if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
						hasTZ = theDate[-6:].replace(':','')

				if type(theDate) == str and len(theDate) > 11 and type(hasTZ) == bool:
					if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
						hasTZ = theDate[-5:].replace(':','')
				local_tz = hasTZ


		if not epoch:
			return record
		pandas = vc.FIG.imp('pandas')


		
		record['epoch'] = epoch
		record['sdate'] = self.friendlyDate2( epoch )
		record['date'] = self.friendlyDate( epoch ).split(' ')[0]
		record['time'] = self.friendlyDate2( epoch ).split(' ')[1]
		record['fdate'] = self.friendlyDate( epoch )
		record['month'] = self.getMonthFromEpoch( epoch )
		record['year'] = self.getYearFromEpoch( epoch )
		record['woy'] = self.getWeekAndYear( epoch )
		record['dow'] = self.getDOWromEpochText( epoch )
		record['ago'] = self.dateDiffText( epoch )
		record['days'] = self.daysDiff( epoch, time.time() )
		record['tz'] = local_tz
		
		try:
			import _rightThumb._stardate as _sd
			record['stardate'] = _sd.gen( epoch )
		except Exception as e:
			pass

		dt = record['fdate'].split(' ')[0].split('-')
		try:
			record['quarter'] = str(record['year']) +'.'+ str(pandas.Timestamp(datetime.date( int(dt[0]) , int(dt[1]), int(dt[2]))).quarter)
		except Exception as e:
			pass

		return record


	def daysDiff( self, one, two ):
 
 
 
		oneA = self.autoDate( one )
		twoB = self.autoDate( two )
		g = 1
		if two > one:
			g = 2

		if one == two:
			return 0
		elif one > two:
			one = self.friendlyDate( oneA ).split(' ')[0]
			two = self.friendlyDate( twoB ).split(' ')[0]
		else:
			one = self.friendlyDate( twoB ).split(' ')[0]
			two = self.friendlyDate( oneA ).split(' ')[0]


		# print( '090', one, two )

		oneB = one.split('-')
		twoB = two.split('-')
		date = vc.FIG.imp('datetime.date')
		
		d0 = date(int(oneB[0]), int(oneB[1]), int(oneB[2]))
		# print( '080', twoB )
		d1 = date(int(twoB[0]), int(twoB[1]), int(twoB[2]))
		delta = d1 - d0
		dd = delta.days
		if g == 1:
			dd = abs(dd)
		return dd



	def getWeekAndYear( self, theDate ):
 
 
 
		y = self.getYearFromEpoch(theDate)
		w = self.getWOYFromEpoch(theDate)
		if w < 10:
			w = '0'+str(w)
		else:
			w = str(w)
		return str(y) +'.'+ w

	def getMonthFromEpoch( self, theDate ):
 
 
 
		return str( self.getYearFromEpoch(theDate) ) + '.' + str(self.formatDateMonth(theDate))


	def getYearFromEpoch( self, theDate ):
 
 
 
		return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[0]

	def getWOYFromEpoch( self, theDate ):
 
 
 
		return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[1]

	def getDOWromEpoch( self, theDate ):
 
 
 
		return datetime.datetime.fromtimestamp( int(theDate) ).isocalendar()[2]

	def getDOWromEpochText( self, theDate ):
 
 
 
		return self.dowConvert(self.getDOWromEpoch(theDate))
	def dowConvert( self, dow ):
 
 
 
		result = ''
		if dow == 1:
			result = 'Monday'
		if dow == 2:
			result = 'Tuesday'
		if dow == 3:
			result = 'Wednesday'
		if dow == 4:
			result = 'Thursday'
		if dow == 5:
			result = 'Friday'
		if dow == 6:
			result = 'Saturday'
		if dow == 7:
			result = 'Sunday'
		return result




	def formatDate( self, theDate ):
 
 
 
		result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%Y-%m-%d %H:%M:%S')
		result = str(result)
		return result
	def formatDateYear( self, theDate ):
 
 
 
		result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%Y')
		# result = str(result)
		return result
	def formatDateDay( self, theDate ):
 
 
 
		result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%d')
		# result = str(result)
		return result
	def formatDateMonth( self, theDate ):
 
 
 
		result = datetime.datetime.fromtimestamp( int(theDate) ).strftime('%m')
		result = str(result)
		return result



	def dateDiffText( self, theDate ):
 
 
 

		# print( theDate )

		y=0
		m=0
		w=0

		# theDate = autoDate( theDate )
		epoch = time.time()
		# woy = getWOY( theDate )

		days = int( str( (time.time() - theDate)/86400 ).split('.')[0] )

		msDiff = epoch - theDate

		if msDiff <= 86402:
			return 'today'

		# days = abs(daysDiff( theDate, epoch ))
		
		if theDate < epoch:
			end = '<'
		else:
			end = '>'

		if days == 0:
			return 'today'
		elif theDate < epoch:
			if days == 1:
				return 'yesterday'
			elif days < 7:
				return 'this week'
		elif theDate > epoch:
			if days == 1:
				return 'tommorow'
			elif days < 7:
				return 'next week'

		if days >= 365:
			tmp = float(days / 365)
			y = int(str(tmp).split('.')[0])
			days = days - ( y*365 )
		if days >= 30:
			tmp = float(days / 30)
			m = int(str(tmp).split('.')[0])
			days = days - ( m*30 )
		if days >= 7:
			tmp = float(days / 7)
			w = int(str(tmp).split('.')[0])
			days = days - ( w*7 )

		result = []
		if y:
			result.append( str(y)+'y' )
		if m:
			result.append( str(m)+'m' )
		if w:
			result.append( str(w)+'w' )
		result.append( end )
		return ' '.join( result )

	def daysDiff( self, one, two ):
 
 
 

		# print(one, two)
		# print(type(one), type(two))

		if one == two:
			return 0
		elif one > two:
			one2 = datetime.datetime.fromtimestamp( int(one) )
			two2 = datetime.datetime.fromtimestamp( int(two) )
		else:
			two2 = datetime.datetime.fromtimestamp( int(one) )
			one2 = datetime.datetime.fromtimestamp( int(two) )



		delta = one2 - two2
		return delta.days


	def tzconvert( self, epoch, tz_src, tz_to ):
 
 
 


		pytz = vc.FIG.imp('pytz')
		arrow = vc.FIG.imp('arrow')

		tz_src = tz_src.replace(':','')
		tz_to = tz_to.replace(':','')

		if '/' in tz_src:
			utc = arrow.utcnow()
			theDate = str(utc.to(tz_src))
			if type(theDate) == str and len(theDate) > 11:
				if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
					tz_src = theDate[-6:].replace(':','')

			if type(theDate) == str and len(theDate) > 11 and type(tz_src) == bool:
				if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
					tz_src = theDate[-5:].replace(':','')




		if '/' in tz_to:
			utc = arrow.utcnow()
			theDate = str(utc.to(tz_to))
			if type(theDate) == str and len(theDate) > 11:
				if theDate[-6:].startswith('+') or theDate[-6:].startswith('-'):
					tz_to = theDate[-6:].replace(':','')

			if type(theDate) == str and len(theDate) > 11 and type(tz_to) == bool:
				if theDate[-5:].startswith('+') or theDate[-5:].startswith('-'):
					tz_to = theDate[-5:].replace(':','')




		if tz_src == tz_to:
			return epoch
		source_date = datetime.datetime.fromtimestamp( epoch )
		source_time_zone = pytz.timezone( self.index[tz_src]['name'] )
		source_date_with_timezone = source_time_zone.localize(source_date)
		target_time_zone = pytz.timezone( self.index[tz_to]['name'] )
		target_date_with_timezone = source_date_with_timezone.astimezone(target_time_zone)
		out = time.mktime(target_date_with_timezone.timetuple())
		return out

	index = {
		"+0000": {
			"country": "CI",
			"name": "Africa/Abidjan",
			"offset": "+00:00",
			"offset2": "+0000",
			"status": "Canonical",
			"py": True
		},
		"+0300": {
			"country": "ET",
			"name": "Africa/Addis_Ababa",
			"offset": "+03:00",
			"offset2": "+0300",
			"status": "Alias",
			"py": True
		},
		"+0100": {
			"country": "DZ",
			"name": "Africa/Algiers",
			"offset": "+01:00",
			"offset2": "+0100",
			"status": "Canonical",
			"py": True
		},
		"+0200": {
			"country": "MW",
			"name": "Africa/Blantyre",
			"offset": "+02:00",
			"offset2": "+0200",
			"status": "Alias",
			"py": True
		},
		"-1000": {
			"country": "US",
			"name": "America/Adak",
			"offset": "-10:00",
			"offset2": "-1000",
			"status": "Canonical",
			"py": True
		},
		"-0900": {
			"country": "US",
			"name": "America/Anchorage",
			"offset": "-09:00",
			"offset2": "-0900",
			"status": "Canonical",
			"py": True
		},
		"-0400": {
			"country": "AI",
			"name": "America/Anguilla",
			"offset": "-04:00",
			"offset2": "-0400",
			"status": "Alias",
			"py": True
		},
		"-0300": {
			"country": "BR",
			"name": "America/Araguaina",
			"offset": "-03:00",
			"offset2": "-0300",
			"status": "Canonical",
			"py": True
		},
		"-0500": {
			"country": "CA",
			"name": "America/Atikokan",
			"offset": "-05:00",
			"offset2": "-0500",
			"status": "Canonical",
			"py": True
		},
		"-0600": {
			"country": "MX",
			"name": "America/Bahia_Banderas",
			"offset": "-06:00",
			"offset2": "-0600",
			"status": "Canonical",
			"py": True
		},
		"-0700": {
			"country": "US",
			"name": "America/Boise",
			"offset": "-07:00",
			"offset2": "-0700",
			"status": "Canonical",
			"py": True
		},
		"-0800": {
			"country": "MX",
			"name": "America/Ensenada",
			"offset": "-08:00",
			"offset2": "-0800",
			"status": "Deprecated",
			"py": True
		},
		"-0200": {
			"country": "BR",
			"name": "America/Noronha",
			"offset": "-02:00",
			"offset2": "-0200",
			"status": "Canonical",
			"py": True
		},
		"-0100": {
			"country": "GL",
			"name": "America/Scoresbysund",
			"offset": "-01:00",
			"offset2": "-0100",
			"status": "Canonical",
			"py": True
		},
		"-0330": {
			"country": "CA",
			"name": "America/St_Johns",
			"offset": "-03:30",
			"offset2": "-0330",
			"status": "Canonical",
			"py": True
		},
		"+1100": {
			"country": "AQ",
			"name": "Antarctica/Casey",
			"offset": "+11:00",
			"offset2": "+1100",
			"status": "Canonical",
			"py": True
		},
		"+0700": {
			"country": "AQ",
			"name": "Antarctica/Davis",
			"offset": "+07:00",
			"offset2": "+0700",
			"status": "Canonical",
			"py": True
		},
		"+1000": {
			"country": "AQ",
			"name": "Antarctica/DumontDUrville",
			"offset": "+10:00",
			"offset2": "+1000",
			"status": "Canonical",
			"py": True
		},
		"+0500": {
			"country": "AQ",
			"name": "Antarctica/Mawson",
			"offset": "+05:00",
			"offset2": "+0500",
			"status": "Canonical",
			"py": True
		},
		"+1200": {
			"country": "AQ",
			"name": "Antarctica/McMurdo",
			"offset": "+12:00",
			"offset2": "+1200",
			"status": "Alias",
			"py": True
		},
		"+0600": {
			"country": "AQ",
			"name": "Antarctica/Vostok",
			"offset": "+06:00",
			"offset2": "+0600",
			"status": "Canonical",
			"py": True
		},
		"+0400": {
			"country": "AZ",
			"name": "Asia/Baku",
			"offset": "+04:00",
			"offset2": "+0400",
			"status": "Canonical",
			"py": True
		},
		"+0800": {
			"country": "BN",
			"name": "Asia/Brunei",
			"offset": "+08:00",
			"offset2": "+0800",
			"status": "Canonical",
			"py": True
		},
		"+0530": {
			"country": "IN",
			"name": "Asia/Calcutta",
			"offset": "+05:30",
			"offset2": "+0530",
			"status": "Deprecated",
			"py": True
		},
		"+0900": {
			"country": "RU",
			"name": "Asia/Chita",
			"offset": "+09:00",
			"offset2": "+0900",
			"status": "Canonical",
			"py": True
		},
		"+0430": {
			"country": "AF",
			"name": "Asia/Kabul",
			"offset": "+04:30",
			"offset2": "+0430",
			"status": "Canonical",
			"py": True
		},
		"+0545": {
			"country": "NP",
			"name": "Asia/Kathmandu",
			"offset": "+05:45",
			"offset2": "+0545",
			"status": "Canonical",
			"py": True
		},
		"+0630": {
			"country": "MM",
			"name": "Asia/Rangoon",
			"offset": "+06:30",
			"offset2": "+0630",
			"status": "Deprecated",
			"py": True
		},
		"+0330": {
			"country": "IR",
			"name": "Asia/Tehran",
			"offset": "+03:30",
			"offset2": "+0330",
			"status": "Canonical",
			"py": True
		},
		"+0930": {
			"country": "AU",
			"name": "Australia/Adelaide",
			"offset": "+09:30",
			"offset2": "+0930",
			"status": "Canonical",
			"py": True
		},
		"+0845": {
			"country": "AU",
			"name": "Australia/Eucla",
			"offset": "+08:45",
			"offset2": "+0845",
			"status": "Canonical",
			"py": True
		},
		"+1030": {
			"country": "AU",
			"name": "Australia/LHI",
			"offset": "+10:30",
			"offset2": "+1030",
			"status": "Deprecated",
			"py": True
		},
		"-1100": {
			"country": "",
			"name": "Etc/GMT+11",
			"offset": "-11:00",
			"offset2": "-1100",
			"status": "Canonical",
			"py": True
		},
		"-1200": {
			"country": "",
			"name": "Etc/GMT+12",
			"offset": "-12:00",
			"offset2": "-1200",
			"status": "Canonical",
			"py": True
		},
		"+1300": {
			"country": "",
			"name": "Etc/GMT-13",
			"offset": "+13:00",
			"offset2": "+1300",
			"status": "Canonical",
			"py": True
		},
		"+1400": {
			"country": "",
			"name": "Etc/GMT-14",
			"offset": "+14:00",
			"offset2": "+1400",
			"status": "Canonical",
			"py": True
		},
		"+1245": {
			"country": "NZ",
			"name": "NZ-CHAT",
			"offset": "+12:45",
			"offset2": "+1245",
			"status": "Deprecated",
			"py": True
		},
		"-0930": {
			"country": "PF",
			"name": "Pacific/Marquesas",
			"offset": "-09:30",
			"offset2": "-0930",
			"status": "Canonical",
			"py": True
		}
	}



# class DATE













class DIR:
	def __init__( self ): pass;
 
 
 
	def info( self, path ):
 
 
 
		path = os.path.abspath(path)
		info = {
					"path": path,
					"name": None,
					"folder": None,
					"bytes": os.stat( path ).st_size,
					"size": None,
					"date_created": None,
					"date_modified": None,
					"date_accessed": None,
					"ext": None,
					"ce": os.path.getctime( path ),
					"me": os.path.getmtime( path ),
					"ae": os.path.getatime( path ),
		}
		parts = path.split(os.sep)
		parts.reverse()
		info['name'] = parts.pop(0)
		parts.reverse()
		info['folder'] = os.sep.join( parts )
		info['size'] = self.formatSize( info['bytes'] )
		info['date_created'] = vc.DATE.epoch( info['ce'] )
		info['date_modified'] = vc.DATE.epoch( info['me'] )
		info['date_accessed'] = vc.DATE.epoch( info['ae'] )
		info['ext'] = vc.EXT.getExt(info['name'])





	def md5( self, path ):
 
 
 
		import hashlib
		hash_md5 = hashlib.md5()
		with open(path, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()
		return hash_md5.hexdigest()


	def formatSize( self, size ):
 
 
 
		try:
			size = int(size)
		except Exception as e:
			size = float(size)
		result = ''
		if size == None:
			result = ''
		elif size < 1024:
			result = str(size) + ' B'
		elif size >= 1024 and size < 1048576:
			num = round(size / 1024, 2)
			result = str(num) + ' KB'
		elif size >= 1048576 and size < 1073741824:
			num = round(size / 1048576, 2)
			result = str(num) + ' MB'
		elif size >= 1073741824 and size < 1099511627776 :
			num = round(size / 1073741824, 2)
			result = str(num) + ' GB'
		elif size >= 1099511627776 and size < 1125899906842624 :
			num = round(size / 1099511627776, 2)
			result = str(num) + ' TB'
		elif size >= 1125899906842624 and size < 1152921504606847000 :
			num = round(size / 1125899906842624, 2)
			result = str(num) + ' PB'
		elif size >= 1152921504606847000 and size < 1180591620717411303424 :
			num = round(size / 1152921504606847000, 2)
			result = str(num) + ' EB'
		elif size >= 1180591620717411303424 and size < 1208925819614629174706176 :
			num = round(size / 1180591620717411303424, 2)
			result = str(num) + ' ZB'
		else:
			num = round(size / 1208925819614629174706176, 2)
			result = str(num) + ' YB'
		# 1152921504606846976

		# if size < 1:
		# result = ''
		return result

	def unFormatSize( self, size ):
 
 
 
		size = str(size)
		size = size.upper()
		factor = ''
		# 1152921504606846976
		if False:
			pass
		elif 'YB' in size:
			factor = 1208925819614629174706176
		elif 'ZB' in size:
			factor = 1180591620717411303424
		elif 'EB' in size:
			factor = 1152921504606847000
		elif 'PB' in size:
			factor = 1125899906842624
		elif 'TB' in size:
			factor = 1099511627776
		elif 'GB' in size:
			factor = 1073741824
		elif 'MB' in size:
			factor = 1048576
		elif 'KB' in size:
			factor = 1024
		else:
			factor = 1
		size = size.replace('X','')
		size = size.replace('Y','')
		size = size.replace('Z','')
		size = size.replace('E','')
		size = size.replace('P','')
		size = size.replace('T','')
		size = size.replace('B','')
		size = size.replace('M','')
		size = size.replace('K','')
		size = size.replace('G','')
		size = float(size)
		if str(size).endswith('.0'):
			size = int(size)

		result = round(size * factor,0)
		# print( size, factor )
		# result = size * factor
		return result


class Files_Folders:
	def __init__( self ):
 
 
 
		self.files = {}
		self.folders = {}
	def getFolders( self, folders=[], r=False, parent=None ):

		loader()

		if type(folders) == str:
			folders = [folders]
		if not folders:
			folders.append( os.getcwd() )
		for folder in folders:
			if os.path.isdir(folder):
				if parent is None:
					parent = folder

				try:
					dirList = os.listdir(folder)
				except Exception as e:
					return None
				# i = 0
				for item in dirList:
					path = folder + os.sep + item
					b = path.replace( parent, '' )[1:]
					b = b.replace( os.getcwd(), '' )
					tested = showLine(b)
					if os.path.isfile(path):
						if tested or showLine(path):
							self.files[path] = b
					elif os.path.isdir(path):
						if tested or showLine(path):
							self.folders[path] = b
						if r:
							self.getFolders( path, r, parent )








class PATHS:
	def __init__( self ): pass;
 
 
 
	def clean4os( self, table ):
 
 
 
		data = {}
		for key in table:
			data[key] = table[key].replace( '/', os.sep )
			for bk in v.bash:
				if '['+bk+']' in data[key]:
					data[key] = data[key].replace( '['+bk+']', v.bash[bk] )
		for key in data:
			for bk in data:
				if '['+bk+']' in data[key]:
					data[key] = data[key].replace( '['+bk+']', data[bk] )
			data[key] = self.path( data[key] )
		
		return data

	def path( self, p, ab=True, pop=False, file=False ):
		# os = vc.FIG.imp('os')
		# os = imp('os')
		# print(p)
		p = p.replace( chr(92), os.sep )
		p = p.replace( chr(47), os.sep )
		p = p.replace( os.sep+os.sep, os.sep )
		if os.path.isfile(p) or os.path.isdir(p):
			pass
		else:
			return p
		if not p:
			return p
		while os.sep+os.sep in p:
			p = p.replace(os.sep+os.sep,os.sep)
		if ab:
			try:
				p = os.path.abspath(p)
			except Exception as e:
				pass
			try:
				p = os.path._getfinalpathname(p).lstrip(r'\?')
			except Exception as e:
				pass
		if type(p) == str and p[1] == ':':
			p = p[0].upper() + p[1:]
		if type(p) == str and ( pop or file ):
			parts = p.split(os.sep)
			parts.reverse()
			f = parts.pop(0)
			parts.reverse()
			p = str(os.sep).join(parts)
			if file:
				p = f
		return p


	def print_paths( self, subjects=[] ):

		if not subjects:
			subjects = [os.getcwd()]


		for subject in subjects:
			try:
				subject = vc.PATHS.path(subject)
				subby = subject.replace(os.getcwd(),'')
				if subby and not subby == subject:
					if v.isWin and subby.startswith(os.sep):
						subby = subby[1:]
					if not v.isWin and subby.startswith(os.sep):
						subby = '.'+subby

					_printME_(subby)
				_printME_( subject )

				if v.isWin:
					_printME_( subject.replace( '\\', '\\\\' ) )
					git_path = subject
					git_path = git_path.replace( '\\', '/' )
					git_path = git_path.replace( ':', '' )
					git_path = '/' + git_path
					_printME_( git_path )

					wsl = '/mnt/'+ git_path[1].lower() + git_path[2:]
					_printME_( wsl )
					




				_printME_( self.path2url( subject ) )

				if vc.FIG.path_secure( subject ).startswith('{'):
					_printME_( vc.FIG.path_secure( subject ) )

				
		

			except Exception as e:
				pass
	def path2url( self, path ):
		pathlib = vc.FIG.imp('pathlib')
		if pathlib is None:
			return ''
		return pathlib.Path(os.path.abspath(path)).as_uri()


class EXIT:
	def __init__( self ):
		self.on_exit_subjects = {}
 
 
 
	def onExit( self, script, subject=None ):
		if subject is None:
			subject = uuid()
		self.on_exit_subjects[subject] = script

	def isExit( self ):
		for subject in self.on_exit_subjects:
			self.on_exit_subjects[subject]()





class STR:
	def __init__( self ):
		self.upperChar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.lowerChar = 'abcdefghijklmnopqrstuvwxyz'
		self.alphaChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.printable = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
		self.printable2 = self.printable
		self.alphanumeric = ' 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.safeChar = self.printable
		self.visibleChar = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		self.notFilenameSafe = '/\\?%*:|"<>'
		self.ciData = ([ '_;192A;_',   ',' ], [ '_;192B;_',   ':' ], [ ';;', ',' ], [ ';c', ',' ],  [ ';_', '-' ], [ ';-', '-' ],  [ ';p;',        '%' ], [ ';p', '%' ], [ ';.', ':' ], [ ";;'",        os.sep+'"' ],  [ os.sep+'n',        '\n' ], [ ';n', '\n' ], [ ';return',    '\n' ], [ ';t', '\t' ],  [ ";'", '"' ], [ ';q;',        '"' ], [ '"\'"',       "'" ], [ 'null00',     '"",' ], [ '"\'", "\'"', "','" ],  [ '[star]',     '*' ], [ '[a]',        '*' ], [ '[s]',        '$' ], [ '[eq]',       '=' ], [ ';opar;',     '[' ], [ '[pipe]',     '|' ], [ '[p]',     '|' ], [ '[htmlopen]', '<' ], [ '[htmlclose]','>' ], [ '[gtr]',      '>' ], [ '[lss]',      '<' ], [ ';6', '^' ], [ ';+', '+' ],  [ '+--+c',  '--c' ],  [ '[semi]', ';' ],  [ '[caret]',    '^' ]  )


 
	def ci(self,string): 
		for cx in self.ciData:
			if cx[0] in string:
				# print( 'HERE', cx )
				string = string.replace( cx[0], cx[1] )
		
		string = string.replace( ';d;', __.theDelim )
		string = string.replace( ';delim;', __.theDelim )
		string = string.replace( ';thedelim;', __.theDelim )
		string = string.replace( ';theDelim;', __.theDelim )
		return string

	def hasAlpha( self, data ):
 
 
 
		data = str( data )
		d = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		result = False
		for c in data:
			if c in d:
				result = True
		return result

	def hasInt( self, data ):
 
 
 
		data = str( data )
		d = '0123456789'
		result = False
		for c in data:
			if c in d:
				result = True
		return result

	def isInt( self, data ):
 
 
 
		data = str( data )
		d = '0123456789'
		result = True
		for c in data:
			if not c in d:
				result = False
		return result

	def isFloat( self, data ):
 
 
 
		data = str( data )
		result = True
		if self.isInt( data ):
			result = False
		else:
			try:
				float( data )
			except Exception as e:
				result = False

		return result



	def isEpoch( self, data ):
 
 
 
		result = True
		try:
			vc.DATE.epoch2TextTimestamp( data )
		except Exception as e:
			result = False
		return result




	def padZero( self, data, pad=2 ):
 
 
 
		data = str(data)
		l = len(data)
		if not l == pad:
			x = l
			pre = ''
			while not x == pad:
				pre += '0'
				x += 1
			data = pre + data
		return data

	def findDelims( self, data ):
 
 
 
		data = str( data )
		d = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		delims = []
		for c in data:
			if not c in d:
				delims.append(c)
		return delims

	def singlDelim( self, data, newDelim='-' ):
 
 
 
		data = str( data )
		for x in self.findDelims( data ):
			data = data.replace( x, newDelim )
		return data
		
	def stripDelimBE( self, data, delim='-' ):
 
 
 
		data = str( data )
		delim = str( delim )
		if data.startswith(delim):
			data = data[1:]
		if data.endswith(delim):
			data = data[:-1]
		return data

	def removeDuplicates( self, data, subject='-' ):
 
 
 
		data = str( data )
		subject = str( subject )
		dup = subject + subject
		if dup in data:
			done = False
			while not done:
				data = data.replace( dup, subject )
				if not dup in data:
					done = True
		return data


	slash = 0
	if platform.system() == 'Windows':
		slash = chr(92)
	else:
		slash = chr(47)

	import re




	def printClean( self, text ):
 
 
 
		text = str(text)
		fix = []
		for x in text:
			if x in self.printable:
				fix.append(x)
		return ''.join(fix)

	def minimalistClean( self, row ):
 
 
 
		result = ''
		for x in row:
			if not x in self.printable:
				result+=' '
			else:
				result+=x
		result = self.replaceDuplicate( result, ' ' )
		result = self.cleanBE( result, ' ' )
		return result




	def hasAlpha( self, row ):
 
 
 
		row = str(row)
		for r in row:
			for a in self.alphaChar:
				if r == a:
					return True
		return False

	def totalClean( self, row ):
 
 
 
		row = row.replace( '\n', '' )
		row = row.replace( '\r', '' )
		row = self.replaceDuplicate( row, ' ' )
		row = self.replaceDuplicate( row, '\t' )
		row = self.cleanBE( row, ' ' )
		row = self.cleanBE( row, '\t' )
		return row



	def filenameSafe( self, data ):
 
 
 

		PERMITTED_CHARS = self.printable
		data = str( data )

		result = ''
		for d in data:
			if d in PERMITTED_CHARS and not d in self.notFilenameSafe:
				result += d
			else:
				result += ' '
		result = self.replaceDuplicate( result, ' ' )
		result = self.cleanBE( result, ' ' )
		return result



	def hasVisible( self, data ):
 
 
 
		for char in data:
			if char in self.visibleChar:
				return True
		return False

	def removeUnsave( self, data ):
 
 
 
		result = ''
		for char in data:
			if char in self.safeChar:
				result += char
		return result

	def spaceba( self, string, what ):
 
 
 
		if what in string:
			string = string.replace( ' '+what, what )
			string = string.replace( what+' ', what )
		return string


	def makePrintable( self, string, replaceWith=' ', appropriate=False ):
 
 
 
		if type(appropriate) == bool:
			appropriate = self.printable
		result = ''

		for char in string:
			if char in appropriate:
				result += char
			else:
				result += replaceWith
		result = self.replaceDuplicate( result, replaceWith )
		result = self.cleanBE( result, replaceWith )
		return result

	def namespace( self, app, data ):
 
 
 
		string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._'
		data = self.makePrintable( data, replaceWith=' ', appropriate=string )
		result = False
		# print( type( app ) )
		for row in data.split(' '):
			if row.startswith( str(app)+'.' ):
				result = row
		# try:
		# except Exception as e:
		# return app, result

		return result

	# import MySQLdb

	############################################### ###############################################

	LATIN_1_CHARS = (
		( '\xe2\x80\x99', "'" ),
		( '\xc3\xa9', 'e' ),
		( '\xe2\x80\x90', '-' ),
		( '\xe2\x80\x91', '-' ),
		( '\xe2\x80\x92', '-' ),
		( '\xe2\x80\x93', '-' ),
		( '\xe2\x80\x94', '-' ),
		( '\xe2\x80\x94', '-' ),
		( '\xe2\x80\x98', "'" ),
		( '\xe2\x80\x9b', "'" ),
		( '\xe2\x80\x9c', '"' ),
		( '\xe2\x80\x9c', '"' ),
		( '\xe2\x80\x9d', '"' ),
		( '\xe2\x80\x9e', '"' ),
		( '\xe2\x80\x9f', '"' ),
		( '\xe2\x80\xa6', '.' ),
		( '\xe2\x80\xb2', "'" ),
		( '\xe2\x80\xb3', "'" ),
		( '\xe2\x80\xb4', "'" ),
		( '\xe2\x80\xb5', "'" ),
		( '\xe2\x80\xb6', "'" ),
		( '\xe2\x80\xb7', "'" ),
		( '\xe2\x81\xba', "+" ),
		( '\xe2\x81\xbb', "-" ),
		( '\xe2\x81\xbc', "=" ),
		( '\xe2\x81\xbd', "( " ),
		( '\xb3', '' ),
		( '\xe2\x81\xbe', ")" )
	)

	def xChar( self, data ):
 
 
 
		char = 'abcdefghijklmnopqrstuvwxyz0123456789'

		for x in char:
			for y in char:
				data = data.replace( self.slash+'x' + x + y, ' ' )
		
		data = self.replaceDuplicate( data, ' ' )
		data = self.cleanBE( data, ' ' )

		return data


	def clean_latin1( self, data ):
 
 
 
		# data = str( data )
		data = data.encode('latin1', 'ignore')
		data = data.decode('latin1')
		# Source: https://gist.github.com/tushortz/9fbde5d023c0a0204333267840b592f9
		# data = data.encode('utf-8')
		# try:
		# pass
		# # return data.encode('latin1')
		# # return data.encode('utf-8')
		# data = data.decode('iso-8859-1')
		# except UnicodeDecodeError:
		# pass
		for _hex, _char in self.LATIN_1_CHARS:
			data = data.replace( _hex, _char )
		# return data.encode('utf8')
		# return data.encode('latin1')
		data = data.replace( 'Alien\\xb3', 'Alien 3' )
		if self.slash+'x' in data:
			data = self.xChar( data )
		return data

	def cleanChar( self, data ):
 
 
 
		# data = str( data )
		
		# Source: https://stackoverflow.com/questions/6539881/python-converting-from-iso-8859-1-latin1-to-utf-8

		# data = data.encode('ascii', 'ignore') 
		# data = data.decode('latin1').encode('utf8').rstrip()
		# data = data.decode('utf8').encode('latin1', 'ignore') 
		# data = str( data )
		# data = str( data )
		data = self.clean_latin1( data )
		# data = data.encode('ascii', 'ignore')
		data = data.encode('latin1', 'ignore')
		# data = data.decode('latin1').encode('utf8')
		# data = data.decode('utf8').encode('latin1', 'ignore') 
		data = data.decode('latin1')
		# data = str( data )
		return data

	############################################### ###############################################

	def stripNonAlphaNumaric( self, data, also='' ):
 
 
 
		PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' + also
		data = str( data )

		result = ''
		for d in data:
			if d in PERMITTED_CHARS:
				result += d
			else:
				result += ' '
		result = self.replaceDuplicate( result, ' ' )
		result = self.cleanBE( result, ' ' )
		return result


	def autoFloatInt( self, data ):
 
 
 
		if self.isInt( data ):
			return int( data )
		if self.isFloat( data ):
			return float( data )
		return data

	def isInt( self, data ):
 
 
 
		data = str( data )
		d = '0123456789'
		result = True
		for c in data:
			if not c in d:
				result = False
		return result

	def isFloat( self, data ):
 
 
 
		data = str( data )
		result = True
		if self.isInt( data ):
			result = False
		else:
			try:
				float( data )
			except Exception as e:
				result = False

		return result

	def removeNonNumber( self, string ):
 
 
 
		PERMITTED_CHARS = '0123456789'
		string = str(string)

		result = ''

		for cha in string:
			if cha in PERMITTED_CHARS:
				result += cha
		return result

	def removeNonAlpha( self, string ):
 
 
 
		PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		string = str(string)

		result = ''

		for cha in string:
			if cha in PERMITTED_CHARS:
				result += cha
		return result

	def removeNonAlpha2( self, string ):
 
 
 
		PERMITTED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
		string = str(string)

		result = ''

		for cha in string:
			if cha in PERMITTED_CHARS:
				result += cha
		return result

	def padZeros( self, string, count ):
 
 
 
		string = str(string)

		diff = count - len(string)
		pre = ''
		for x in range(1,diff+1):
			pre += '0'
		result = pre + string
		return result


	def replaceAll( self, string, rWhat, rWith ):
 
 
 
		tmp = '{C9DCAA81-3B8A-68E9-E4CF-A405E2199CB9}'


		done=False
		string = str(string)
		while done == False:
			if string.count(str(rWhat)) > 0:
				string = string.replace(str(rWhat),tmp)
			else:
				done=True


		done=False
		string = str(string)
		while done == False:
			if string.count(str(rWhat)) > 0:
				string = string.replace(str(rWhat),tmp)
			else:
				done=True



		done=False
		while done == False:
			if string.count(tmp) > 0:
				string = string.replace(tmp,str(rWith))
			else:
				done=True

		string = string.replace(tmp,str(rWith))
		return string
	# def replaceAll(string,rWhat,rWith):
	# if not rWhat == rWith:
	#    done=False
	#    while done == False:
	#        if string.count(rWhat) > 0:
	#            string = string.replace(rWhat,rWith)
	#        else:
	#            done=True
	# return string

	def removeAll( self, string, rWhat ):
 
 
 
		rWith = ''
		return self.replaceAll(string,rWhat,rWith)

	def replaceDuplicate( self, string, rWhat ):
 
 
 
		rWith = rWhat
		rWhat = str(rWhat) + str(rWhat)
		string = self.replaceAll(string,rWhat,rWith)
		for x in range(10):
			string = string.replace( rWhat, rWith )
		return string

	def cleanBE( self, string, rWhat ):
 
 
 
		string = self.cleanEnd(string,rWhat)
		string = self.cleanFirst(string,rWhat)
		return string
	def cleanEnd( self, string, rWhat ):
 
 
 
		string = str(string)
		rWhat = str(rWhat)
		# string = self.replaceDuplicate(string,rWhat)
		string += '*?*'
		string = string.replace(rWhat + '*?*', '')
		string = string.replace('*?*', '')
		if string.endswith(rWhat):
			string = self.cleanEnd(string,rWhat)

		return string

	def cleanEnd2( self, string, rWhat ):
 
 
 
		string = str(string)
		rWhat = str(rWhat)
		string = self.totalStrip3(string)
		string = self.cleanSpecial(string)
		string = self.replaceDuplicate(string,rWhat)
		string += '*?*'
		string = string.replace(rWhat + '*?*', '')
		string = string.replace('*?*', '')
		return string

	def cleanLast( self, string, rWhat ):
 
 
 
		return self.cleanEnd(string,rWhat)

	def cleanFirst( self, string, rWhat ):
 
 
 
		string = str(string)
		rWhat = str(rWhat)
		# string = self.replaceDuplicate(string,rWhat)
		string = '*?*' + str(string)
		string = string.replace('*?*' + rWhat, '')
		string = string.replace('*?*', '')
		if string.startswith(rWhat):
			string = self.cleanFirst(string,rWhat)
		return string

	def cleanAll( self, string, rWhat, rWith ):
 
 
 
		done=False
		while done == False:
			if string.count(rWhat) > 0:
				string = string.replace(rWhat,rWith)
			else:
				done=True
		return string

	def cleanSpecial( self, line, special1=False ):
 
 
 
		line = str(line)
		if not special1:
			line = self.replaceAll(str(line),self.slash,'--/--')
			try:
				pass
				line = line.encode('latin-1')
				line = self.replaceAll(line,self.slash+'t',' ')
				line = self.replaceAll(line,self.slash+'xa0',' ')
				line = self.replaceAll(line,self.slash+'xe9',"'")
				line = self.replaceDuplicate(line,' ')
				line = self.cleanFirst(line,' ')
				line = self.cleanLast(line,' ')
			except Exception as e:
				try:
					line = line.encode('utf-8')
					pass
				except Exception as e:
					pass
		else:
			line = self.replaceAll(line,'\u0092',"'")
		try:
			line = line.replace('…','.')
		except Exception as e:
			pass
		i = 0
		skip = False
		string = ''
		for char in str(line):
			# print(item)
			char = str(char)
			if char == self.slash:
				i = 0
				skip = True
			if skip == True:
				if i == 4:
					i = 0
					skip = False
				else:
					i += 1
			if skip == False:
				string += char
			else:
				string += ' '

		# line = string
		if not special1:
			line = self.replaceAll(str(line),'--/--',self.slash)
			# line = self.replaceAll(str(line),'_-_',',')
			line = self.replaceDuplicate(str(line), ' ')
			line = self.cleanEnd(str(line),'"')
			line = self.cleanEnd(str(line),"'")
			line = self.cleanEnd(str(line),' ')
			line = self.cleanFirst(str(line),"b'")
			line = self.cleanFirst(str(line),'b"')
			line = self.cleanFirst(str(line),'.')
			# line = line.replace(' ',' ')
		return line

	def cleanSpecial2( self, line, special1=False ):
 
 
 
		line = str(line)
		def cleanup(line):
			line = self.replaceAll(line,self.slash+'t',' ')
			line = self.replaceAll(line,self.slash+'xc3',' ')
			
			line = self.replaceAll(line,self.slash+'xb1',' ')
			line = self.replaceAll(line,self.slash+'xf3',' ')
			line = self.replaceAll(line,self.slash+'xf6',' ')
			line = self.replaceAll(line,self.slash+'xe4',' ')

			line = self.replaceAll(line,self.slash+'xa0',' ')
			line = self.replaceAll(line,self.slash+'xe9',"'")
			line = self.replaceAll(line,self.slash+'xe2\\x80\\x93','-')
			line = self.replaceAll(line,self.slash+'\\xe2\\\\x80\\\\x93','-')
		if not special1:
			line = self.replaceAll(str(line),self.slash,'--/--')
			try:
				pass
				try:
					line = cleanup(line)
					line = line.decode('utf-8','ignore')
				except Exception as e:
					pass
				try:
					line = cleanup(line)
					line = line.encode('utf-8').decode('utf-8')
				except Exception as e:
					pass
				try:
					line = cleanup(line)
					line = line.encode('latin-1')
				except Exception as e:
					pass
				try:
					line = cleanup(line)
					line = line.encode('latin-1').decode('latin-1')
				except Exception as e:
					pass
				try:
					line = cleanup(line)
				except Exception as e:
					pass



				line = self.replaceDuplicate(line,' ')
				line = self.cleanFirst(line,' ')
				line = self.cleanLast(line,' ')
			except Exception as e:
				try:
					line = line.encode('utf-8')
					pass
				except Exception as e:
					pass
		else:
			line = self.replaceAll(line,'\u0092',"'")
		try:
			line = line.replace('…','.')
		except Exception as e:
			pass
		i = 0
		skip = False
		string = ''
		for char in str(line):
			# print(item)
			char = str(char)
			if char == self.slash:
				i = 0
				skip = True
			if skip == True:
				if i == 4:
					i = 0
					skip = False
				else:
					i += 1
			if skip == False:
				string += char
			else:
				string += ' '

		# line = string
		if not special1:
			line = self.replaceAll(str(line),'--/--',self.slash)
			# line = self.replaceAll(str(line),'_-_',',')
			line = self.replaceDuplicate(str(line), ' ')
			line = self.cleanEnd(str(line),'"')
			line = self.cleanEnd(str(line),"'")
			line = self.cleanEnd(str(line),' ')
			line = self.cleanFirst(str(line),"b'")
			line = self.cleanFirst(str(line),'b"')
			line = self.cleanFirst(str(line),'.')
			# line = line.replace(' ',' ')
		return line

	def totalStrip( self, line ):
 
 
 
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._,-@:'#\""
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def alpha( self, line ):
 
 
 
		PERMITTED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'"
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def totalStrip2( self, line ):
 
 
 
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-" 
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def totalStrip3( self, line ):
 
 
 
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-," 
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def totalStrip4( self, line ):
 
 
 
		PERMITTED_CHARS = "0123456789" 
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def totalStrip5( self, line ):
 
 
 
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._,-@:'#\"()"
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ''
		# line = section + ']'
		# line = line.replace(' ]','')
		# line = line.replace(']','')
		return line
	def totalStrip6( self, line ):
 
 
 
		line = self.removeAll(line,'\n')
		line = self.removeAll(line,'\r')
		line = self.characterClean(line)
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._,-@:'#\"()"
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def totalStrip9( self, line ):
 
 
 
		line = self.removeAll(line,'\n')
		line = self.removeAll(line,'\r')
		line = self.underscore(line)
		# line = self.cleanupString(line)
		# line = self.cleanSpecial2(line)
		# line = self.characterClean(line)
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
		section = ''
		for cha in line:
			if cha in PERMITTED_CHARS:
				section += cha
			else:
				section += ' '
		line = section
		line = self.cleanBE(line,' ')
		line = self.replaceDuplicate(line,' ')
		return line
	def underscore( self, line ):
 
 
 
		# http://www.fileformat.info/
		line = line.replace('\u005F',' ')
		line = line.replace('\uFF3F',' ')
		line = line.replace('\u2017',' ')
		line = line.replace('\u203E',' ')
		line = line.replace('\u0332',' ')
		line = line.replace('_',' ')
		return line

	def totalStrip7( self, line ):
 
 
 
		line = self.removeAll(line,'\n')
		line = self.removeAll(line,'\r')
		line = self.underscore(line)
		# line = self.cleanupString(line)
		# line = self.cleanSpecial2(line)
		# line = self.characterClean(line)
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ."
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section
		line = self.cleanBE(line,' ')
		line = self.replaceDuplicate(line,' ')
		return line
	def onlyDigits( self, line ):
 
 
 
		line = self.removeAll(line,'\n')
		line = self.removeAll(line,'\r')
		line = self.characterClean(line)
		PERMITTED_CHARS = "0123456789-"
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def onlyDigits2( self, line ):
 
 
 
		line = str( line )
		line = line.replace( '–', '-' )
		PERMITTED_CHARS = '0123456789-'
		result = ''
		for char in line:
			if char in PERMITTED_CHARS:
				result += char
		return result
	def totalStrip8( self, line ):
 
 
 
		line = self.removeAll(line,'\n')
		line = self.removeAll(line,'\r')
		line = self.characterClean(line)
		PERMITTED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ._,-@:'#\"()"
		section = ''
		for word in line.split(' '):
			section += ''.join(c for c in word if c in PERMITTED_CHARS)
			section += ' '
		line = section + ']'
		line = line.replace(' ]','')
		line = line.replace(']','')
		return line
	def cleanupString0( self, string ):
 
 
 
		string = self.replaceAll(string,'\n',' ')
		string = self.replaceDuplicate(string,' ')
		string = self.cleanLast(string,' ')
		string = self.cleanFirst(string,' ')
		string = self.cleanSpecial(string)
		string = self.cleanFirst(string,' ')
		return string
	def cleanupString( self, string, beforeAfter=True ):
 
 
 
		string = self.replaceAll(string,'\n',' ')
		string = self.replaceAll(string,'\t',' ')
		string = self.replaceDuplicate(string,' ')
		string = self.cleanLast(string,' ')
		string = self.cleanFirst(string,' ')
		string = self.cleanSpecial(string)
		string = self.cleanFirst(string,' ')
		string = string.replace(self.slash+'xe2\\x80\\x93','-')
		string = string.replace(self.slash+'\\xe2\\\\x80\\\\x93','-')
		if beforeAfter:
			string = string.split('(')[0]
		else:
			string = string.split('(')[1]
		string = string.split('/')[0]
		return string

	def characterClean( self, string ):
 
 
 
		string = string.replace('\xe2\x80\x9c','"').replace('\xe2\x80\x9d','"').replace('\xe2\x80\x99',"'").replace(self.slash+'xe2\\x80\\x93','-')
		# string = string.encode('latin-1')
		return string

	def basic( self, string ):
 
 
 
		# pattern = re.compile('([^\s\w]|_)+')
		pattern = re.compile(r'([^\s\w]|_)+')
		string = pattern.sub('', string)
		string = self.replaceDuplicate(string,' ')
		string = self.cleanFirst(string,' ')
		string = self.cleanLast(string,' ')

		return string

	def charFix( self, string ):
 
 
 
		for ch in self.charFixData:
			chs = ch[1].split(',')
			for c in chs:
				string = string.replace( self.slash+c, ch[0] )
		return string

	charFixData = ['','x00'],
	['','x01'],
	['','x02'],
	['','x03'],
	['','x04'],
	['','x05'],
	['','x06'],
	['','x07'],
	['','x08'],
	['','x09'],
	['','x0a'],
	['','x0b'],
	['','x0c'],
	['','x0d'],
	['','x0e'],
	['','x0f'],
	['','x10'],
	['','x11'],
	['','x12'],
	['','x13'],
	['','x14'],
	['','x15'],
	['','x16'],
	['','x17'],
	['','x18'],
	['','x19'],
	['','x1a'],
	['','x1b'],
	['','x1c'],
	['','x1d'],
	['','x1e'],
	['','x1f'],
	['','x20'],
	['!','x21'],
	[''','x22'],
	['#','x23'],
	['$','x24'],
	['%','x25'],
	['&','x26'],
	[''','x27'],
	['(','x28'],
	[')','x29'],
	['*','x2a'],
	['+','x2b'],
	[',','x2c'],
	['-','x2d'],
	['.','x2e'],
	['/','x2f'],
	['0','x30'],
	['1','x31'],
	['2','x32'],
	['3','x33'],
	['4','x34'],
	['5','x35'],
	['6','x36'],
	['7','x37'],
	['8','x38'],
	['9','x39'],
	[':','x3a'],
	[';','x3b'],
	['<','x3c'],
	['=','x3d'],
	['>','x3e'],
	['?','x3f'],
	['@','x40'],
	['A','x41'],
	['B','x42'],
	['C','x43'],
	['D','x44'],
	['E','x45'],
	['F','x46'],
	['G','x47'],
	['H','x48'],
	['I','x49'],
	['J','x4a'],
	['K','x4b'],
	['L','x4c'],
	['M','x4d'],
	['N','x4e'],
	['O','x4f'],
	['P','x50'],
	['Q','x51'],
	['R','x52'],
	['S','x53'],
	['T','x54'],
	['U','x55'],
	['V','x56'],
	['W','x57'],
	['X','x58'],
	['Y','x59'],
	['Z','x5a'],
	['[','x5b'],
	['','x5c'],
	[']','x5d'],
	['^','x5e'],
	['_','x5f'],
	['`','x60'],
	['a','x61'],
	['b','x62'],
	['c','x63'],
	['d','x64'],
	['e','x65'],
	['f','x66'],
	['g','x67'],
	['h','x68'],
	['i','x69'],
	['j','x6a'],
	['k','x6b'],
	['l','x6c'],
	['m','x6d'],
	['n','x6e'],
	['o','x6f'],
	['p','x70'],
	['q','x71'],
	['r','x72'],
	['s','x73'],
	['t','x74'],
	['u','x75'],
	['v','x76'],
	['w','x77'],
	['x','x78'],
	['y','x79'],
	['z','x7a'],
	['{','x7b'],
	['|','x7c'],
	['}','x7d'],
	['~','x7e'],
	['','x7f'],
	['','xc2,x80'],
	['','xc2,x81'],
	['','xc2,x82'],
	['','xc2,x83'],
	['','xc2,x84'],
	['','xc2,x85'],
	['','xc2,x86'],
	['','xc2,x87'],
	['','xc2,x88'],
	['','xc2,x89'],
	['','xc2,x8a'],
	['','xc2,x8b'],
	['','xc2,x8c'],
	['','xc2,x8d'],
	['','xc2,x8e'],
	['','xc2,x8f'],
	['','xc2,x90'],
	['','xc2,x91'],
	['','xc2,x92'],
	['','xc2,x93'],
	['','xc2,x94'],
	['','xc2,x95'],
	['','xc2,x96'],
	['','xc2,x97'],
	['','xc2,x98'],
	['','xc2,x99'],
	['','xc2,x9a'],
	['','xc2,x9b'],
	['','xc2,x9c'],
	['','xc2,x9d'],
	['','xc2,x9e'],
	['','xc2,x9f'],
	['','xc2,xa0'],
	['','xc2,xa1'],
	['','xc2,xa2'],
	['','xc2,xa3'],
	['-','xc2,xa4'],
	['','xc2,xa5'],
	['','xc2,xa6'],
	['','xc2,xa7'],
	['','xc2,xa8'],
	['(C)','xc2,xa9'],
	['-','xc2,xaa'],
	['-','xc2,xab'],
	['-','xc2,xac'],
	['-','xc2,xad'],
	['-','xc2,xae'],
	['-','xc2,xaf'],
	['-','xc2,xb0'],
	['','xc2,xb1'],
	['','xc2,xb2'],
	['','xc2,xb3'],
	['´','xc2,xb4'],
	['','xc2,xb5'],
	['','xc2,xb6'],
	['-','xc2,xb7'],
	['','xc2,xb8'],
	['','xc2,xb9'],
	['-','xc2,xba'],
	['-','xc2,xbb'],
	[' 1/4','xc2,xbc'],
	[' 1/2','xc2,xbd'],
	[' 3/4','xc2,xbe'],
	['','xc2,xbf'],
	['','xc3,x80'],
	['','xc3,x81'],
	['','xc3,x82'],
	['','xc3,x83'],
	['','xc3,x84'],
	['','xc3,x85'],
	['','xc3,x86'],
	['','xc3,x87'],
	['','xc3,x88'],
	['','xc3,x89'],
	['','xc3,x8a'],
	['','xc3,x8b'],
	['','xc3,x8c'],
	['','xc3,x8d'],
	['','xc3,x8e'],
	['','xc3,x8f'],
	['','xc3,x90'],
	['','xc3,x91'],
	['','xc3,x92'],
	['','xc3,x93'],
	['','xc3,x94'],
	['','xc3,x95'],
	['','xc3,x96'],
	['x','xc3,x97'],
	['','xc3,x98'],
	['','xc3,x99'],
	['','xc3,x9a'],
	['','xc3,x9b'],
	['','xc3,x9c'],
	['','xc3,x9d'],
	['','xc3,x9e'],
	['','xc3,x9f'],
	['','xc3,xa0'],
	['','xc3,xa1'],
	['','xc3,xa2'],
	['','xc3,xa3'],
	['','xc3,xa4'],
	['','xc3,xa5'],
	['','xc3,xa6'],
	['','xc3,xa7'],
	['','xc3,xa8'],
	['','xc3,xa9'],
	['','xc3,xaa'],
	['','xc3,xab'],
	['','xc3,xac'],
	['','xc3,xad'],
	['','xc3,xae'],
	['','xc3,xaf'],
	['','xc3,xb0'],
	['','xc3,xb1'],
	['','xc3,xb2'],
	['','xc3,xb3'],
	['','xc3,xb4'],
	['','xc3,xb5'],
	['','xc3,xb6'],
	['÷','xc3,xb7'],
	['','xc3,xb8'],
	['','xc3,xb9'],
	['','xc3,xba'],
	['','xc3,xbb'],
	['','xc3,xbc'],
	['','xc3,xbd'],
	['','xc3,xbe'],
	['','xc3,xbf']

# class STR:



class TableView:

	def __init__(self,name,table,fields,sort):
		self.name = name
		self.fields = fields
		self.sort = sort
		self.table = table
		# print(self.name)


TableProfile_Config = {}
class Table:

	def __init__( self, name, asset=[], group_space=True, tab='' ):
		global switches
		global _dir
		

		self.group_space = group_space
		self.name = name
		self.asset = asset
		self.fields = []
		self.views = []
		self.spaces = {}
		self.maxNameLength = 35
		if switches.isActive('Long'):
			try:
				self.maxNameLength = int(switches.value('Long'))
			except Exception as e:
				self.maxNameLength = 35
		self.columnTab = spaces(3)
		self.groupSeparator = '_'
		self.tableProfile = []
		self.tableProfileDefaultAlignment = 'left'
		self.tableProfileDefaultAlignmentHeader = ''
		self.tableProfileDefaultAlignmentChanged = False
		self.tableProfileDefaultAlignment = False
		self.tableProfileDefaultSupersedes = False
		self.views = []
		self.universalSpacing = False

		self.wrapTableKey = 'Da529801Ef674997B9f3382B3eD2b93F'
		self.backup = dot()
		self.backup.asset = asset.copy()
		self.aggregate_processed = False
		self.isWrap = False
		self.hasAggregate = False
		self.hasGroups = False
		self.backup.fields = {}
		self.backup.allfields = {}
		self.backup.NGfields = {}
		self.groupID_KEY = genUUID()
		if len( self.asset ):
			for r in self.asset:
				for k in r:
					if not k in self.backup.fields:
						self.backup.fields[k] = 1
						self.backup.allfields[ tfc(k) ] = k
						self.backup.NGfields[ tfc(k) ] = k


		self.tab_color = ''
		if type(tab) == list:
			self.tab_color = tab[1]
			tab = tab[0]

		tabH = ''
		i=0
		while not i == len(tab):
			i+=1
			tabH+=' '

		self.tab = { 'header': tabH, 'table': tab }

	def registerView(self,name,fields,sort = ''):
		self.views.append(TableView(name,self.name,fields,sort))

	def printView(self,name):
		global switches
		i=0
		for tp in self.views:
			# print()
			# for x in dir(self.views[i]):
			#   print(x)

			if self.views[i].name == name:
				# print('found')
				switches.fieldSet('Sort','active',True)
				switches.fieldSet('Sort','value',str(self.views[i].sort))
				# print(switches.value('Sort'))
				# try:
					
				# except Exception as e:
				#   pass
				# print('name:',name)
				self.print(self.views[i].fields)
			i += 1

	# def trigger(self,field,script,includes):
	#   self.views.append({'name': field, 'script_trigger': script , 'includes': includes })


	def nameLength(self,string,suffix):
		result = ''
		toLong = False
		if switches.isActive('Length'):
			result = self.nameLengthFix(string,switches.value('Length'),'')
		else:
			try:
				i = 0
				for L in string:
					if i <= self.maxNameLength:
						result += L
					else:
						toLong = True
					i += 1
				if toLong == True:
					result += '...'
					if len(suffix) > 0:
						result += spaces(2)+'.' + suffix
			except Exception as e:
				result = string
		return result

	def nameLengthFix(self,string,change,suffix):
		result = ''
		toLong = False
		change = change.lower()
		old = self.maxNameLength
		if 'x' in change:
			change = change.replace('x','')
			newLength = self.maxNameLength * int(change)
		else:
			newLength = self.maxNameLength + int(change)
		try:
			i = 0
			for L in string:
				if i <= newLength:
					result += L
				else:
					toLong = True
				i += 1
			if toLong == True:
				result += '...'
				if len(suffix) > 0:
					result += spaces(2)+'.' + suffix
		except Exception as e:
			result = string
		return result

	def tabGetMaxSpace(self,name):
		global errors
		global switches
		rows = self.asset
		spacer = 1
		# print('*** ' + name)
		size = len(name) + spacer
		
		# print(name,00)
		# rows[0][name]
		try:
			pass
			if name in rows[0]:
				rows[0][name]
			else:
				# print(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
				eval(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
		except Exception as e:
			errors.append({'id': 9, 'function': 'tabGetMaxSpace()', 'cnt': 1, 'location': 'rows[0][name]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
			printBold('Error:','red')
			printBold('\tBad column input.')
			_printME_(9)
			_printME_(name)
			_printME_(  'rows[0]["' + '"]["'.join(name.split('.')) + '"]'  )
			printVarSimple(rows[0])
			printBold('record sample','red')
			os._exit(0)
		# print(name)
		for item in rows:
			shorten = True
			if switches.isActive('Long') == True:
				shorten = False
				if switches.isActive('ShortenColumn') == True:
					shortenColumn = switches.value('ShortenColumn')
					for sc in shortenColumn.split(','):
						if sc == name:
							shorten = True
			
			if name in item:
				thisData = item[name]
			elif name.split('.')[0] in item:
				thisData = eval(  'item["' + '"]["'.join(name.split('.')) + '"]'  )


			if shorten == True and not switches.isActive('Length'):
				try:
					text = self.nameLength( str(self.scriptTriggerField(name,thisData)) ,'')
				except Exception as e:
					text = self.nameLength(str(thisData),'')
			else:
				if switches.isActive('Length'):
					# print('asdf')
					# sys.exit()
					try:
						
						text = self.nameLengthFix(  str(self.scriptTriggerField(name,thisData)) ,switches.value('Length'),'')
					except Exception as e:
						text = self.nameLengthFix(str(thisData),switches.value('Length'),'')
				else:
					# sys.exit()
					# if type(thisData) == int or type(thisData) == float:
					#     text = thisData
					# else:
					try:
						text = self.scriptTriggerField(name,thisData)
					except Exception as e:
						text = thisData
							
			
			itemSize = len(str(text)) + spacer
			if itemSize > size:
				size = itemSize
			# print(item)
		return size

	def addSpace(self,string,max):
		dif = int(max) - len(string)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def addSpace2(self,max):
		dif = int(max)
		build = ''
		for x in range(dif):
			build = build + ' '
		return build
	def scriptTriggerField(self,field,value):
		i = 0
		for s in self.tableProfile:
			try:
				if self.tableProfile[i]['includes'] == True:
					if ',' in self.tableProfile[i]['name']:
						found = False
						for n in self.tableProfile[i]['name'].split(','):
							if n in field:
								found = True
						if found:
							value = self.tableProfile[i]['script_trigger'](value)
					else:
						if self.tableProfile[i]['name'] in field:
							value = self.tableProfile[i]['script_trigger'](value)
				else:
					if field == self.tableProfile[i]['name']:
						value = self.tableProfile[i]['script_trigger'](value)
			except Exception as e:
				pass
			i += 1
		return value
	def triggerExecute(self,field,value):
		i = 0
		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i]['trigger'](value)
				except Exception as e:
					pass
			else:
				if type(value) == int:
					value = addComma( str(value) )
			i += 1
		return value

	def fieldProfileSet(self,field,propertyName,value):
		field = field.lower()
		if field == '*' and propertyName == 'alignment':
			self.tableProfileDefaultAlignment = value
			self.tableProfileDefaultAlignmentChanged = True
		if field == '_header_' and propertyName == 'alignment':
			self.tableProfileDefaultAlignmentHeader = value
		else:
			if ',' in field:
				for n in field.split(','):
					self.fieldProfileSet(n,propertyName,value)

			found = False
			i = 0
			for s in self.tableProfile:
				if self.tableProfile[i]['name'] == field:
					found = True
					self.tableProfile[i][propertyName] = value
				i += 1

			if not found:
				item = len(self.tableProfile)
				self.tableProfile.append({'name': field, propertyName: value})

	def fieldProfileGet(self,field,propertyName,isHeader = False):
		# print('ran')
		field = field.lower()
		i = 0
		value = ''
		if isHeader and '_header_' in TableProfile_Config.keys() and propertyName in TableProfile_Config['_header_'].keys():
			return TableProfile_Config['_header_'][propertyName]
		elif not isHeader and field in TableProfile_Config.keys() and propertyName in TableProfile_Config[field].keys():
			return TableProfile_Config[field][propertyName]
		elif '*' in TableProfile_Config.keys() and propertyName in TableProfile_Config['*'].keys():
			return TableProfile_Config['*'][propertyName]

		if propertyName == 'alignment':
			value = self.tableProfileDefaultAlignment

		for s in self.tableProfile:
			if self.tableProfile[i]['name'] == field:
				try:
					value = self.tableProfile[i][propertyName]
				except Exception as e:
					pass
			i += 1


		if self.tableProfileDefaultAlignmentChanged and self.tableProfileDefaultSupersedes:
			value = self.tableProfileDefaultAlignment
		if isHeader and len(self.tableProfileDefaultAlignmentHeader) > 0:
			value = self.tableProfileDefaultAlignmentHeader

		elif isHeader:
			value = 'center'
		if propertyName == 'alignment' and value == '':
			value = 'left'
		return value
	def showColumn(self,column,i,columnHeaderLength):
		# print(column)
		global errors
		global lastGroup
		global switches
		def test(one,two):
			# print(one,two)
			if (one) == (two):
				return True
			else:
				return False
		groupByList = self.groupByList
		rows = self.asset
		# print(rows)

		columnList = column
		if column in rows[i]:
			value = str(self.triggerExecute(column,rows[i][column]))
		elif column.split('.')[0] in rows[i]:
			value = str(self.triggerExecute(column,  eval(  'rows[i]["' + '"]["'.join(column.split('.')) + '"]'  )  ) )

		# value = rows[i][column]
		# print(column,value)
		value = value.replace('\n','')
		# value = self.scriptTriggerField(column,rows[i][column])
		try:
			pass
		except Exception as e:
			pass

		shorten = True
		if switches.isActive('Long') == True:
			shorten = False
			if switches.isActive('ShortenColumn') == True:
				shortenColumn = switches.value('ShortenColumn')
				for sc in shortenColumn.split(','):
					if sc == column:
						shorten = True
		text = str(value)
		if shorten == True:
			text = self.nameLength(str(value),'')
		else:
			text = str(value)


		groupBy = switches.value('GroupBy')
		try:
			tabFix = self.spaces[column]
		except Exception as e:
			# errors.append({'id': 10, 'function': 'showColumn()', 'cnt': 1, 'location': 'tabFix = spaces[column]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}, {'name': 'i', 'value': i}], 'error': e})
			tabFix = self.tabGetMaxSpace(column)
			self.spaces[column] = tabFix

		if switches.isActive('GroupBy') == True:
			for gb in groupBy.split(','):
				gb = str(gb)
				if column == gb:
					# print('- -',last,text)
					if not test(groupByList[gb],text) == True:
						if groupBy.split(',')[0] == column:
							pass
							if self.group_space:
								_printME_(self.groupLine(columnList,columnHeaderLength))
							if not self.isExtraRecord:
								for g in groupBy.split(','):
									groupByList[g] = ''
						else:
							pass
							if self.group_space:
								_printME_('')
						

						if not self.isExtraRecord:
							groupByList[gb] = text
						else:
							if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
								text = ''

						# else:
						#   print(text)
					else:
						pass
						
						if len(self.isExtraRecord_000x):
							self.isExtraRecord_0001[ self.isExtraRecord_000x.split('-')[0] ] = 1
						text = ''
						
		alignment = self.fieldProfileGet(column,'alignment')
		# print(alignment)
		# if alignment == 'left':
		result = text + self.addSpace(text,tabFix)
		if alignment == 'left':
			result = text + self.addSpace(text,tabFix)
		if alignment == 'right':
			result = self.addSpace(text,tabFix) + text
		if alignment == 'center':
			totalSpace = int(tabFix) - len(text)
			if totalSpace > 0:
				if totalSpace % 2 == 0:
					div2 = totalSpace/2
					theLeft = div2
					theRight = div2
				else:
					divTMP = totalSpace - 1
					div2 = divTMP/2
					theLeft = div2 + 1
					theRight = div2
			else:
				theLeft = 0
				theRight = 0
			result = self.addSpace2(theLeft) + text + self.addSpace2(theRight)
			# print(column,theLeft,theRight,'0' + result + '0')
			# print(totalSpace,theLeft,theRight)
		#   result = theLeft + text + theRight
		return result

	def groupLine(self,columnList,columnHeaderLength):
		columnNumber = len(columnList.split(','))
		loop = 0
		result = ''
		while loop < columnHeaderLength + (columnNumber * 4):
			result += self.groupSeparator
			loop += 1
		return result

	def showColumnHeader(self,column):
		# rows = self.asset
		result = ''
		if type(self.universalSpacing) == dict:
			self.spaces = self.universalSpacing
		for c in column.split(','):
			try:
				tabFix = self.spaces[c]
			except Exception as e:
				# errors.append({'id': 11, 'function': 'showColumn()', 'cnt': 2, 'location': 'tabFix = spaces[c]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'column', 'value': column}], 'error': e})
				tabFix = self.tabGetMaxSpace(c)
				self.spaces[c] = tabFix
				# print(tabFix)
			# x
			# alignment = 'center'
			alignment = self.fieldProfileGet(c,'alignment',isHeader=True)
			if alignment == '':
				########## Default Alignment ##########
				alignment = 'right'


			if alignment == 'center':
				totalSpace = int(tabFix) - len(c)
				if totalSpace > 0:
					if totalSpace % 2 == 0:
						div2 = totalSpace/2
						theLeft = div2
						theRight = div2
					else:
						divTMP = totalSpace - 1
						div2 = divTMP/2
						theLeft = div2 + 1
						theRight = div2
				else:
					theLeft = 0
					theRight = 0
				result += self.addSpace2(theLeft) + c.replace('_',' ').upper() + self.addSpace2(theRight) + self.columnTab
			if alignment == 'left':
				result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
			if alignment == 'right':
				result += self.addSpace(c,tabFix) + c.replace('_',' ').upper() + self.columnTab
			# else:
				# result += c.replace('_',' ').upper() + self.addSpace(c,tabFix) + self.columnTab
		result += '\n'
		return '\n'+result

	def findColumName( self, column ):
		for k in self.asset[0].keys():
			if k.lower() == column.lower():
				return k
		for k in self.asset[0].keys():
			if k.lower() == column.split('.')[0].lower():
				return column




	def prefixSize( self ):
		pre = ''
		for x in self.tab['table']+loopPrint(__.table_prefix_padding):
			if x == '\t':
				pre += spaces(4)
			else:
				pre += x
		return len(pre)


	def wrapTable( self, cols=None ):
		# return None

		if not __.terminal.width:
			return None

		cols = __.terminal.width
		cols -= 8
		spaces = []
		theKeys = []
		for c in self.spaces:
			theKeys.append(c)
			spaces.append({ 'c': c, 's': self.spaces[c] })

		spaces = sorted(spaces, key=lambda d: (d['s']))
		spaces.reverse()

		fieldsToShorten = []

		if not len(switches.value('WrapTable')):
			fieldsToShorten.append( spaces[0]['c'] )
			if len( self.spaces.keys() ) > 1:
				diff = percentageDiffIntAuto( spaces[0]['s'], spaces[1]['s'] )
				if diff >= 50:
					fieldsToShorten.append( spaces[1]['c'] )
				# print( 'diff:', diff )

				if len( self.spaces.keys() ) > 2:
					diff = percentageDiffIntAuto( spaces[0]['s'], spaces[2]['s'] )
					if diff >= 50:
						fieldsToShorten.append( spaces[2]['c'] )
					# print( 'diff:', diff )
		elif len(switches.value('WrapTable')):
			done = False
			if len(switches.values('WrapTable')) == 1:
				done = False
				wrapBy = switches.value('WrapTable')
				if wrapBy in self.asset[0].keys():
					done = True
				if not done:
					if formatColumns(wrapBy) in self.asset[0].keys():
						wrapBy = formatColumns(wrapBy)
						done = True

				if not done:
					wrapBy = 0
					try:
						wrapBy = int(switches.value('WrapTable'))
					except Exception as e:
						wrapBy = 0
					if wrapBy > 0:
						done = True
			elif len(switches.values('WrapTable')) > 1:
				wrapBy = []
				for xx in switches.values('WrapTable'):
					y = formatColumns(xx)
					if y in self.asset[0].keys():
						wrapBy.append(y)
						done = True

			if done:
				if type(wrapBy) == str:
					fieldsToShorten.append( wrapBy )
				if type(wrapBy) == list:
					for yy in wrapBy:
						fieldsToShorten.append( yy )
				if type(wrapBy) == int:
					for isp, itx in enumerate(spaces):
						fieldsToShorten.append( itx['c'] )
						
						if isp+1 == wrapBy:
							break

				# print(type(wrapBy))
				# print(wrapBy)
				# sys.exit()

					


		# print(fieldsToShorten)
		# sys.exit()

		maxLen = self.maxNameLength
		total = self.prefixSize()
		for c in self.spaces:
			total += self.spaces[c]
			total += len(self.columnTab)
		
		tempSpaces = self.spaces.copy()
		for c in tempSpaces:
			if tempSpaces[c] > maxLen:
				if not c in fieldsToShorten:
					fieldsToShorten.append(c)

		while total > cols:
			hasGrtMax = False

			for fs in fieldsToShorten:
				if tempSpaces[fs] > maxLen:
					hasGrtMax = True
					tempSpaces[fs] -=1
			if not hasGrtMax:
				for fs in fieldsToShorten:
					tempSpaces[fs] -=1

			total = self.prefixSize()
			for c in tempSpaces:
				total += tempSpaces[c]
				total += len(self.columnTab)
		


		# percentageDiffIntAuto
		# printVarSimple( self.spaces )
		# print( '---------' )
		# printVarSimple( tempSpaces )
		# for x in spaces:
		#   print(x)

		wrapTableKey = self.wrapTableKey
		
		counter = 0
		global fields
		fields.register( wrapTableKey+'-b', 'val', 4, m=4 )
		fields.register( wrapTableKey, 'val', 7, m=12 )
		test = fields.padZeros( wrapTableKey, 'val', 5 )
		test = fields.padZeros( wrapTableKey+'-b', 'val', 5 )
		letters = {}
		

		# print(letterSet)
		# sys.exit()
		def letterBoost( i ):
			if not str(i) in letters:
				letters[str(i)] = 'a'
		

		recordsToAdd = []
		for i,record in enumerate(self.asset):
			letters[ str(i) ] = 'a'
			recordKey = 1
			

			this_key = fields.padZeros( wrapTableKey, 'val', i+1 )
			this_key_B = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )

			
			self.asset[i][wrapTableKey+'-sort'] = this_key+'-'+this_key_B
			rec = {}
			rec_last = {}
			for c in tempSpaces:

				if c in record and len( str(record[c]) ) > tempSpaces[c]:
					# rec[c] = {}
					recordKey = 1
					# cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					# # print(cs)
					# if not cs in rec:
					#   rec[cs] = {}
					# if not c in rec[cs]:
					#   rec[cs][c] = ''
					
					rec_parts = autoWrapText( str(record[c]), length=tempSpaces[c] )

					# print('_________________________________________')
					# print()
					# print(record[c])
					# print()
					# print(rec_parts)
					# print()
					# print('_________________________________________')
					rp = ''
					last_rp = ''
					for rp in rec_parts:
						if len(rp) and not last_rp == rp:
							last_rp = rp
							cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
							recordKey += 1
							if not cs in rec:
								rec[cs] = {}
							if not cs in rec_last:
								rec_last[cs] = {}
							# if not c in rec[cs]:
								# rec[cs][c] = ''
							
							# if c in rec_last[cs]:
							#   if 
							rec[cs][c] = rp
					rp = ''

					# for x in record[c]:
					#   rec[cs][c] += x
					#   if len( rec[cs][c] ) > tempSpaces[c]:
					#       recordKey += 1
					#       cs = fields.padZeros( wrapTableKey+'-b', 'val', recordKey )
					#       # print(cs)
					#       if not cs in rec:
					#           rec[cs] = {}
					#       if not c in rec[cs]:
					#           rec[cs][c] = ''
					# printVarSimple(rec)
					# sys.exit()
			if rec:
				for iii,xXx in enumerate(rec):
					if xXx == '0001':
						for c in rec[xXx]:
							self.asset[i][c] = rec[xXx][c]
					else:
						# print(xXx)
						rec[xXx][wrapTableKey+'-sort'] = this_key +'-'+ xXx
						recordsToAdd.append(rec[xXx])
					# print(rec[x])
				# print(rec)

		for rec in recordsToAdd:
			self.asset.append(rec)
			# print(rec)
		# sys.exit()
		self.spaces = {}


		groupBy = switches.values('GroupBy')
		last = {}
		for gb in groupBy:
			last[gb] = '{7270D97A-CC1D-4365-9545-87CA34F2F026}'



		for i,record in enumerate(self.asset):
			ks = list(record.keys())
			for k in theKeys:
				if not k in ks:
					self.asset[i][k] = ''
			for k in theKeys:
				if not k in self.spaces:
					self.spaces[k] = 0
				if len(str(record[k])) > self.spaces[k]:
					self.spaces[k] = len(str(record[k]))


		# for i,record in enumerate(self.asset):
		#   for gb in groupBy:
		#       if gb in self.asset[i]:
		#           if self.asset[i][gb] == last[gb]:
		#               self.asset[i][gb] = ''
		#           else:
		#               last[gb] = self.asset[i][gb]
		self.asset = sorted(self.asset, key=lambda d: (d[wrapTableKey+'-sort']))


		# for x in self.asset:
		#   print()
		#   print(x)
		#   print()




		# for i,record in enumerate(self.asset):
		#   print( record[wrapTableKey+'-sort'] )
		# sys.exit()
		# print(self.asset)
		# for x in self.asset:
		#   print()
		#   print(x)
		#   print()
		# sys.exit()
		
		self.print(
					column=self.print_backup['column'],
					fieldLengths=self.print_backup['fieldLengths'],
					pc=self.print_backup['pc'],
					printColumns=self.print_backup['printColumns'],
					force=True
		)




	def aggregateRecord( self, i ):
		# print()
		
		for c in self.aggregates.columns:
			if not c in self.asset[i]:
				self.asset[i][c] = ''

		for seg in self.aggregates.segments:
			if seg['status']:
				record = self.aggregate_record_process( i, seg['i'] )


	def aggregateTop( self, s ):
		ss = str(s)
		if self.aggregates.index[ss]['rent'] >= 0:
			return self.aggregateTop(self.aggregates.index[ss]['rent'])
		else:
			return self.aggregates.index[ss]


	def aggregateItemValue( self, v, f ):
		if not 'params' in v:
			v['params'] = {}
		if not 'fields' in v:
			v['fields'] = {}
		if not 'data' in v:
			v['data'] = []

		# print( self.aggregate_backtrack )

		if 'data' in f:
			v['data'].append( f['data'] )
		if 'fields' in f:
			if not 'fields' in v:
				v['fields'] = {}
			for k in f['fields']:
				v['fields'][k] = f['fields'][k]
		elif 'params' in f:
			if not 'params' in v:
				v['params'] = {}
			for k in f['params']:
				v['params'][k] = f['params'][k]
		return v

	def aggregate_record_process_group( self, i, s ):
		ss = str(s)
		seg = self.aggregates.index[ss]
		if 'variable' in seg['l']:
			alpha = seg['l']
			if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				txtParts = seg['txt'].split('?')
				grp = txtParts[0]+'?'
				fld = txtParts[1]
				lbl = txtParts[2]
				if not lbl in self.aggregates.group_storage:
					self.aggregates.group_storage[lbl] = 0


				data = self.aggregate_record_process( i, seg['val'] )
				child = self.aggregates.index[ str(seg['val']) ]
				do = None
				if 'function' in child['l']:
					do = child['txt']
					done = False
					if do == 'max':
						done = True;
						try:
							if data['data'] > self.aggregates.group_storage[lbl]:
								self.aggregates.group_storage[lbl] = data['data']
						except Exception as e: cp('Error: group max variable', 'red');

					if do == 'add':
						done = True;
						try:
							self.aggregates.group_storage[lbl] += data['data']
						except Exception as e: cp('Error: group add variable', 'red');
					
					# if not done:
					#   self.aggregates.group_storage[lbl] = data['data']

				pass


				
				pass

				if i in self.aggregates.groups[fld]['e']:
					if __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 3:
						self.asset[  self.aggregates.groups[fld]['e'][i]  ][lbl] = addComma( self.aggregates.group_storage[lbl] )
					else:
						if tfc(lbl) in self.backup.NGfields:
							if not str(i) in self.aggregates.agroupsADD:
								self.aggregates.agroupsADD[ str(i) ] = {}
							self.aggregates.agroupsADD[ str(i) ][lbl] = self.aggregates.group_storage[lbl]
						else:
							self.asset[i][lbl] = addComma( self.aggregates.group_storage[lbl] )
					if not __.aggregate.group_prefixes[  seg['txt'].lower().split('?')[0]+'?'  ] == 2:
						self.aggregates.group_storage[lbl] = 0
			


		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print( list( self.asset[0].keys() ) )
		#   sys.exit()


	def aggregate_record_process( self, i, s ):

		ss = str(s)
		if True:
			seg = self.aggregates.index[ss]
			# print(seg)
			
			# self.aggregate_backtrack = { 'i': i, 's': s, 'seg': seg }


			if 'alpha' in seg['l'] and 'arg' in seg['l'] :
				simple_keys = {}
				for key in list(self.asset[i].keys()):
					simple_keys[ tfc(key) ] = key
				if tfc(formatColumns( seg['txt'] )) in simple_keys:
					vXv = simple_keys[tfc(formatColumns( seg['txt'] ))]
					return { 'fields': { vXv: self.asset[i][vXv] }, 'data': self.asset[i][vXv] }

				elif formatColumns( seg['txt'] ) in self.asset[i]:
					return { 'fields': { formatColumns( seg['txt'] ): self.asset[i][formatColumns( seg['txt'] )] }, 'data': self.asset[i][formatColumns( seg['txt'] )] }
				return { 'params': { seg['txt']: 1 } }



			if 'variable' in seg['l']:
				alpha = seg['l']
				isOF = False
				data = self.aggregate_record_process( i, seg['val'] )
				if '?' in seg['txt'] and  seg['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes:
					isOF = True
					if '?' in seg['txt'] and seg['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
						return None
					if seg['txt'].startswith('eot?'):
						if not seg['txt'] in self.aggregates.storage:
							self.aggregates.storage[ seg['txt'] ] = {}
						if not alpha in self.aggregates.storage[seg['txt']]:
							self.aggregates.storage[seg['txt']][alpha] = {}
							self.aggregates.storage[seg['txt']][alpha]['data'] = 0
							self.aggregates.storage[seg['txt']][alpha]['settings'] = {}
					if seg['txt'].startswith('eof?'):
						# print( seg['txt'] ); sys.exit();
						if not seg['txt'] in __.aggregate.eof.storage:
							__.aggregate.eof.storage[ seg['txt'] ] = {}
						if not alpha in __.aggregate.eof.storage[seg['txt']]:
							__.aggregate.eof.storage[seg['txt']][alpha] = {}
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = 0
							__.aggregate.eof.storage[seg['txt']][alpha]['settings'] = {}
					
					
					# print(isOF, seg['txt'])

				
					child = self.aggregates.index[ str(seg['val']) ]
					do = None
					if 'function' in child['l']:
						do = child['txt']


					if seg['txt'].startswith('eot?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > self.aggregates.storage[seg['txt']][alpha]['data']:
									self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								self.aggregates.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');

						
						if not done:
							self.aggregates.storage[seg['txt']][alpha]['data'] = data['data']
							
					elif seg['txt'].startswith('eof?'):
						done = False
						if do == 'max':
							done = True;
							try:
								if data['data'] > __.aggregate.eof.storage[seg['txt']][alpha]['data']:
									__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
							except Exception as e: cp('Error: max variable', 'red');

						if do == 'add':
							done = True;
							try:
								__.aggregate.eof.storage[seg['txt']][alpha]['data'] += data['data']
							except Exception as e: cp('Error: add variable', 'red');
						
						if not done:
							__.aggregate.eof.storage[seg['txt']][alpha]['data'] = data['data']
				
				else:
					# print( i, seg['txt'], data['data'] )
					self.asset[i][seg['txt']] = data['data']

					

					return data
				return { 'data': '' }
			if 'function' in seg['l']:
				###########################################################################################################
				if seg['txt'] == 'trigger':
					pass

				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'add':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result += float( d )
								except Exception as e: pass;
						else:
							try:
								result += float( v['data'] )
							except Exception as e: pass;
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'int':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						nX = []
						if type(v['data']) == list:
							for d in v['data']:
								for cn in str(d):
									if cn in '0123456789.':
										nX.append(cn)
						else:
							for cn in str(v['data']):
								if cn in '0123456789.':
									nX.append(cn)
					result = float(''.join(nX))
					if str(result).endswith('.0'):
						result = int(result)
					# print(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'len':
					result = 0; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								# print( 'len-d:', d )
								result += len( str( d ) )
						else:
							# print( 'len-vd:', v['data'] )
							result += len( str( v['data'] ) )
					# print( 'len-v', v )
					if str(result).endswith('.0'):
						result = int(result)
					return { 'data': result }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'max':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for d in v['data']:
						if '?date' in v['params']:
							try:
								ad = autoDate( d )
							except Exception as e: ad = 0;
							result.append(ad)
						else:
							try:
								ad = float( d )
							except Exception as e: ad = 0;
							result.append(ad)
					result.sort()
					result.reverse()

					return { 'data': result[0] }


				if seg['txt'] == 'config':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						try:
							eval( '__.aggregate.config'+suffix  )
						except Exception as e:
							exec( '__.aggregate.config'+suffix+' = { }'  )
					# printVarSimple(__.aggregate.config)
					# sys.exit()

				pass
				if seg['txt'] == 'format':
					result = []; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f ); 
					for par in v['params']:
						result.append(par)
					suffix = ''
					for par in result:
						suff = "['"+par+"']"
						suffix += suff
						# print( 'suffix:', suffix )
						try:
							eval( '__.aggregate.format'+suffix  )
						except Exception as e:
							exec( '__.aggregate.format'+suffix+' = { }'  )



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'isDate':
					result = None; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = autoDate( d )
								except Exception as e: pass;
						else:
							try:
								result = autoDate( v['data'] )
							except Exception as e: pass;
					
					if not result is None:
						try:
							global _dir
						except Exception as e:
							pass
						if _dir is None:
							import _rightThumb._dir as _dir
						# print( result )
						# self.asset[i]['month'] = _dir.getMonthFromEpoch( result )
						# self.asset[i]['year'] = _dir.getYearFromEpoch( result )
						# self.asset[i]['woy'] = _dir.getWeekAndYear( result )
						# self.asset[i]['dow'] = _dir.getDOWromEpochText( result )
						# self.asset[i]['ago'] = _dir.dateDiffText( result )
						self.asset[i] = isDate( result, self.asset[i] )
						
						# month year woy dow ago
						

						month = _dir.getMonthFromEpoch
						# year = _dir.getYearFromEpoch
						# woy = _dir.getWOYFromEpoch
						# dow = _dir.getDOWromEpochText
						# ago = _dir.dateDiffText
					return { 'data': None }



				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				if seg['txt'] == 'file':
					result = ''; v = {};
					for s in seg['args']:
						f = self.aggregate_record_process( i, s ); v = self.aggregateItemValue( v, f );
					if 'data' in v:
						if type(v['data']) == list:
							for d in v['data']:
								try:
									result = d
								except Exception as e: pass;
						else:
							try:
								result = v['data']
							except Exception as e: pass;


					# global _dir
					if _dir is None:
						import _rightThumb._dir as _dir
					# info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					# print( info )
					try:
						info = _dir.info( _str.cleanBE( result, ' ' ).replace( '\t', '' ) )
					except Exception as e:
						info = {
									"path": "",
									"name_": "",
									"name": "",
									"folder": "",
									"bytes": 0,
									"size": "",
									"date_created_raw": 0,
									"date_modified_raw": 0,
									"date_created": "",
									"date_modified": "",
									"type": "File",
									"typesort": 1,
									"ext": "txt",
									"week_of_year": "",
									"week_of_year_": 0,
									"day_of_the_week": "",
									"month": "",
									"friendly_week": "",
									"friendly_month": "",
									"md5": "",
									"year": 2021,
									"accessed_raw": 0,
									"date_accessed": "",
									"ce": 0,
									"me": 0,
									"ae": 0,
									"meta": {},
									"ago": "",
									"header": "",
									"error": 0
								}
					
					for k in info:
						if not k in self.asset[i]:
							self.asset[i][k] = info[k]

					return { 'data': result }




				# { 'fields': {  'field': 123, 'data': 123 } }  { 'params': {  'param': 1  } }
				###########################################################################################################



	def aggregateBuild( self ):
		if self.aggregate_processed:
			return None
		
		self.aggregate_processed = True


		a = ' '.join( switches.values('Aggregate') )
		# print( a )

		
		self.aggregates = dot()

		
		self.aggregates.storage = {}
		self.aggregates.group_storage = {}
		# self.aggregates.segments = __.code.process( a, addString=[['alphaParam','?']] )
		# self.aggregates.segments = __.aggregate.data.records
		self.aggregates.segments = __.aggregate.obj.build( self.name, addSwitch=True )

		self.aggregates.index = {}

		self.aggregates.groups = {}
		self.aggregates.agroups = {}
		self.aggregates.agroupsADD = {}
		self.aggregates.columns = []
		for rec in self.aggregates.segments:
			self.aggregates.index[ str(rec['i']) ] = rec
			if rec['status'] and rec['l'] == 'variable':
				# if not rec['txt'].startswith('eot?'):
				# if not rec['txt'].startswith('eot?') and not rec['txt'].startswith('eof?') and not rec['txt'].startswith('eog?') and  not rec['txt'].startswith('bog?') and  not rec['txt'].lower().startswith('eoga?'):
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					self.aggregates.columns.append( rec['txt'] )
					if not rec['txt'] in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = rec['txt']
						self.backup.NGfields[ rec['txt'] ] = rec['txt']
		for rec in self.aggregates.segments:
			if rec['status'] and rec['l'] == 'variable':
				if not '?' in rec['txt'] or ( '?' in rec['txt'] and not rec['txt'].lower().split('?')[0]+'?' in __.aggregate.prefixes):
					pass
				elif '?' in rec['txt'] and rec['txt'].lower().split('?')[0]+'?' in __.aggregate.group_prefixes:
				# elif 'g?' in rec['txt']:
					self.aggregates.agroups[ rec['i'] ] = rec
					
					try:
						gc = rec['txt'].split('?')[2]

					except Exception as e:
						cp( 'Error: aggregates, group split', 'red' )
						sys.exit()
					else:
						self.aggregates.columns.append( gc )
					if not gc in self.backup.allfields:
						self.backup.allfields[ rec['txt'] ] = gc

		# self.hasGroups

		pass
		# print( self.aggregates.columns )
		# sys.exit()



		# sys.exit()
		# for x in segments:
		#   if x['status']:
		#       cp( x, 'green' )
		#   else:
		#       cp( x, 'cyan' )
		#       # print( x )

		for i,record in enumerate(self.asset):
			self.aggregateRecord( i )


		# sys.exit()
		__.aggregate.storage = self.aggregates.storage
		return self.aggregates.columns


	def aggregateRecordGroups( self, i ):
		# print()

		for seg in self.aggregates.segments:
			if seg['status']:
				# record = self.aggregate_record_process_group( i, seg['i'] )
				try:
					record = self.aggregate_record_process_group( i, seg['i'] )
				except Exception as e:
					cp( 'Error: aggregate, group error', 'red' )
					cp( '\t expected:', 'yellow' )
					cp( '\t\t eog?level?group-len=add(len)', 'green' )
					_printME_()
					cp( [ 'Specifically:', e ], 'red' )
					_printME_()
					sys.exit()




	def aggregateGroup( self ):
		# NOTE: reprocess after aggregates added        
		for ix in self.aggregates.agroups:
			seg = self.aggregates.agroups[ix]
			q = seg['txt'].split('?')
			subject = q[1]
			# print( self.asset[0].keys() )
			# print(subject); sys.exit();
			if subject in self.asset[0] and not subject in self.aggregates.groups:
				self.aggregates.groups[subject] = {}
				self.aggregates.groups[subject]['b'] = {}
				self.aggregates.groups[subject]['e'] = {}
				lastQ = ''
				lastID = -1
				for i,record in enumerate(self.asset):
					# print(subject)
					if subject in record:
						# print( record[subject] )
						if not record[subject] == lastQ:
							if not lastID == -1:
								self.aggregates.groups[subject]['b'][lastID] = i
								self.aggregates.groups[subject]['e'][i] = lastID
							lastQ = record[subject]
							lastID = i
				self.aggregates.groups[subject]['b'][lastID] = len(self.asset)-1
				self.aggregates.groups[subject]['e'][len(self.asset)-1] = lastID

		# if self.aggregates.groups:
		#   printVarSimple(self.aggregates.groups)
		#   print( list( self.asset[0].keys() ) )
		#   sys.exit()

	def aggregate( self, script ):
		self.hasAggregate = True
		__.aggregate.obj.code( script, label=self.name )

	def aggregateBuildGroup( self ):
		self.aggregateGroup()
		for i,record in enumerate(self.asset):
			self.aggregateRecordGroups( i )

		if self.aggregates.agroupsADD:
			

			fields.register( self.groupID_KEY, 'val', 7, m=6 )
			test = fields.padZeros( self.groupID_KEY, 'val', 5 )
			newRecords = []
			for i,record in enumerate(self.asset):
				ii = str(i)
				ix = fields.padZeros( self.groupID_KEY, 'val', i )
				record[ self.groupID_KEY ] = ix + '-A'
				newRecords.append(record)
				if ii in self.aggregates.agroupsADD:
					rec = self.aggregates.agroupsADD[ii]
					rec[ self.groupID_KEY ] = ix + '-B'
					for k in self.backup.allfields:
						if not self.backup.allfields[k] in rec:
							rec[ self.backup.allfields[k] ] = ''
					newRecords.append(rec)
			self.asset = newRecords
	def print( self, column, fieldLengths=False, pc=None, printColumns=True, force=False ):


		if not type(self.asset) == list or len(self.asset) == 0:
			_printME_('Null Set')
			sys.exit()




		if not force:
			if not switches.isActive('Help'):
				if switches.isActive('Column'):
					column = switches.value('Column')
			
				if switches.isActive('Sort'):
					self.asset = self.sort()
				elif switches.isActive('GroupBy'):
					
					switches.fieldSet('Sort','active',True)
					switches.fieldSet('Sort','value',switches.value('GroupBy'))
					self.asset = self.sort()

			pass
			__.aggregate.storage = {}
			__.aggregate.config = {}
			__.aggregate.format = {}
			__.aggregate.prefix = self.tab['table']+loopPrint(__.table_prefix_padding)
			if switches.isActive('Aggregate') or self.hasAggregate:
				aggregate_columns = self.aggregateBuild()
				if type(aggregate_columns) == list:
					columns = column.split(',')
					for ac in aggregate_columns:
						if not ac in columns:
							columns.append(ac)
					column = ','.join(columns)
				__.aggregate.columns = columns

				shouldSortAgain = False
				if switches.isActive('Sort'):
					for sxy in switches.values('Sort'):
						if sxy in aggregate_columns:
							shouldSortAgain = True

					if shouldSortAgain:
						self.asset = self.sort()
				self.aggregateBuildGroup()
				for i,record in enumerate(self.asset):
					for c in record:
						nw = __.aggregate.obj.format( c, record[c] )
						if not nw == record[c]:
							self.asset[i][c] = nw
			pass
			for i,record in enumerate( self.asset ):
				for k in record:
					if record[k] is None:
						self.asset[i][k] = ''




		self.isExtraRecord = False
		if force:
			self.isWrap = True
		self.print_backup = {
								'column': column,
								'fieldLengths': fieldLengths,
								'pc': pc,
								'printColumns': printColumns,
		}
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''
		# print('here',column)
		if not pc is None:
			printColumns = pc
		self.groupByTrigger()
		if type(fieldLengths) == dict:
			self.universalSpacing = fieldLengths
		# print(column)
		# print(self.assets)
		# rows = self.asset
		if not type(self.asset) == list or len(self.asset) == 0:
			_printME_('Null Set')
			sys.exit()
		global errors
		global switchDefault
		column = column.lower()
		columnSearch = column
		column = ''
		for cs in columnSearch.split(','):
			try:
				column += self.findColumName(cs.split('=')[0]) + ','
			except Exception as e:
				column += cs + ','
				# print( 'Error: print column', cs )
				# sys.exit()
			# print(cs.split('=')[0])
		column = _str.cleanBE(column,',')
		# print(column)
		newData = []
		oldData = []
		if ':' in column or '=' in columnSearch:
			oldData = self.asset
		if ':' in column:
			depth = []
			flat = []
			for c in column.split(','):
				if not ':' in c:
					flat.append(c)
				else:
					try:
						found = False
						i=0
						for dp in depth:
							if depth[i]['parent'] == c.split(':')[0]:
								found = True
								dpID = i
							i+=1
					except Exception as e:
						found = False
					if found:
						depth[dpID]['children'].append(c.split(':')[1])
					else:
						depth.append({'parent': c.split(':')[0],'children': [c.split(':')[1]]})
			
			i = 0
			for data in self.asset:
				r = {}
				for f in flat:
					r[f] = data[f]
				x = []
				hasRecords = False
				for dp in depth:
					if len(data[dp['parent']]) > 0:
						hasRecords = True
						for dpi in data[dp['parent']]:
							y = {}
							hasData = False
							for dpic in dp['children']:
								try:
									if len(str(dpi[dpic])) > 1:
										hasData = True
								except Exception as e:
									pass
								try:
									y[str(dp['parent']) + ':' + str(dpic)] = dpi[dpic]
								except Exception as e:
									pass
							for f in flat:
								y[f] = r[f]
							if hasData:
								newData.append(y)
				if not hasRecords:
					for dpi in data[dp['parent']]:
						for dpic in dp['children']:
							r[str(dp['parent']) + ':' + str(dpic)] = ''
					newData.append(r)
				i+=1
			self.asset = newData
			# print(newData)
			# print('dasfdasdfasdfadsf')


		newData = []
		if '=' in columnSearch:
			for data in self.asset:
				rowInclude = True
				for c in columnSearch.split(','):
					if rowInclude:
						if '=' in c:
							cc = c.split('=')
							string = data[cc[0]]
							string = _str.cleanBE(string.lower(),' ')
							cc[1] = _str.cleanBE(cc[1],' ')
							try:
								dataYes = _str.cleanBE(cc[1].split('-')[0],' ')
							except Exception as e:
								dataYes = ''
							try:
								dataNo = _str.cleanBE(cc[1].split('-')[1],' ')
							except Exception as e:
								dataNo = ''
							if len(dataYes) > 0:
								# print('IS')
								# print(dataYes)
								length = 0

								for s in dataYes.split(' '):
									if rowInclude:
										rowInclude = False
										if len(s) > 0:
											length += 1
											# print(string)
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
													rowInclude = True
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													# print(s,string)
													cnt += 1
													rowInclude = True
											elif s in string:
												cnt += 1
												rowInclude = True
								# print(length,cnt)
								# if length == cnt:
								# if cnt > 0:
									# rowInclude = True
										# if switches.isActive('PlusOr') == True:
										#   if cnt > 0:
										#       rowInclude = True
							if len(dataNo) > 0 and rowInclude:
								# print('ISNOT')
								rowInclude = True
								try:
									for s in dataNo.split(' '):
										if len(s) > 0:
											s = s.lower()
											cnt = 0
											if len(s) > 1 and s[0] == '*':
												s = s.replace('*','')
												if string.endswith(s):
													cnt += 1
											elif len(s) > 1 and s[-1] == '*':
												s = s.replace('*','')
												if string.startswith(s):
													cnt += 1
											elif not string.find(vc.STR.ci(s)) == -1:
												cnt += 1
											# if not string.find(vc.STR.ci(s)) == -1:
											if cnt > 0:
												rowInclude = False
												break
								except Exception as e:
									pass
				if rowInclude:
					newData.append(data)
			self.asset = newData
			# print(self.asset)





		# if not len(groupByList):


		# if not column == False:
			# switches.fieldSet('Column','value',column)
			# column = switches.value('Column')

		# print('-',column)
		columnHeader = self.showColumnHeader(column)
		columnHeaderLength = len(columnHeader)
		# print(columnHeader)


		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass



		if not force and not switches.isActive('NoWrapTable'):

			if __.terminal.width:
				maxSize = 0
				i=0
				for item in self.asset:
					result = ''
					for c in column.split(','):
						try:
							result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
						except Exception as e:
							pass
					# print(result)
					maxSize = len(result)+self.prefixSize()
					i+=1


				# print( maxSize )
				if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
					self.wrapTable(__.terminal.width)
					# print( 'error' )
					# sys.exit()
					return None


		pass
		self.groupByList = {}
		try:
			for gb in switches.value('GroupBy').split(','):
				self.groupByList[str(gb)] = ''
		except Exception as e:
			pass


		if printColumns:
			columnHeader = self.tab['table']+loopPrint(__.table_prefix_padding) + columnHeader.replace( '\n', '' )
			_printME_()
			printBold( columnHeader )
			# printBold( columnHeader, prefix=self.tab['header'] )
			_printME_()
		i = 0
		# print(self.asset)
		self.isExtraRecord_0001 = {}
		self.isExtraRecord_000x = ''

		for item in self.asset:
			# print(item)
			result = ''
			for c in column.split(','):
				try:
					pass
					# result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					pass
				# print(result)
				self.isExtraRecord = False
				
				
				# if self.wrapTableKey+'-sort' in item:
					# print(  item[self.wrapTableKey+'-sort']  )
					# print(    )

				if self.wrapTableKey+'-sort' in item:
					self.isExtraRecord_000x = item[self.wrapTableKey+'-sort']

				if self.wrapTableKey+'-sort' in item and not item[self.wrapTableKey+'-sort'].endswith('-0001'):
					self.isExtraRecord = True
				try:
					pass
					result += self.showColumn(c,i,columnHeaderLength) + self.columnTab
				except Exception as e:
					errors.append({'id': 12, 'function': '_printME_()', 'cnt': 1, 'location': "result += showColumn(rows,c,i) + os.sep+'t'", 'vars': [{'name': 'folder', 'value': 'folder'}, {'name': 'column', 'value': column}], 'error': e})
					printBold('Error:','red')
					printBold('\tBad column input.')
					_printME_(12)
					_printME_(c)
					_printME_(12)
					os._exit(0)
			# print(_str.totalStrip5(result)) #TESTING
			
			maxSize = len(result)+self.prefixSize()
			if maxSize > __.terminal.width and not switches.isActive('NoWrapTable'):
				ToDo = " result = ''"+spaces(3)
				ToDo = ' for sult in self.wrapTable2(i):'+spaces(2)
				ToDo = '     result += sult'+spaces(2)
			else:
				ToDo = ' the below if will be under this else '

			if len(result) > 0:
				# print(result)
				shouldPrint = True
				if self.isExtraRecord_000x.split('-')[0] in self.isExtraRecord_0001:
					testResult = result
					testResult = testResult.replace( ' ', '' ).replace( '\t', '' )
					if not len(testResult):
						shouldPrint = False
				# if self.isExtraRecord:
				#   print( self.isExtraRecord )

				if shouldPrint:
					if self.groupID_KEY in item and item[self.groupID_KEY].endswith('-B'):
						cp( [ self.tab['table']+loopPrint(__.table_prefix_padding) + result ], 'BackgroundGrey.blue' )
					else:
						colorizeRow( result, prefix=self.tab['table']+loopPrint(__.table_prefix_padding), prefixColor=self.tab_color, haltColorShift=self.isExtraRecord )
			i += 1
			if 'expected_input_example' in column and 'switch' in column and  switchDefault == i:
				if '??' in __.switch_skimmer.active:
					sys.exit()
				pass
				_printME_('')
		# if len(oldData) > 0:
		#   self.asset = oldData
		self.asset = self.backup.asset.copy()
		self.aggregate_processed = False
		# print( 'recovered' )


		footer = {}
		aSettings = {}
		for k in __.aggregate.storage:
			if k.startswith('eot?'):
				f = k[len('eot?'):]
				for y in __.aggregate.storage[k]:
					for sv in __.aggregate.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.storage[k][y]['settings']:
						__.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					theKey = f 
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eot?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?fl' in special:
						theKey = f + ' '+ y
					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y


					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = friendlyDate( __.aggregate.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.storage[k][y]['data'] = addComma( __.aggregate.storage[k][y]['data'] )
					# # print(  )
					# footer[ theKey ] = __.aggregate.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.storage[k][y]['data'] )
		if footer:
			_printME_()
			# print()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( spaces(2) )
			cp( footer_txt, 'cyan' ) 
			# print( __.aggregate.config )
			_printME_()
					# print( f, y, __.aggregate.storage[k][y]['data'] )
			# print( k )
			# sys.exit()

	def sort(self,fields=''):# sortThis
		rows = self.asset

		if not len(self.asset):
			return None

		if self.wrapTableKey+'-sort' in self.asset[0]:
			return rows
		

		global errors
		global switches
		# self.sort = name
		tempFields = []
		delim = ':'
		if fields == '':
			name = switches.value('Sort')
		else:
			name = fields
		name = name.replace(':',delim)
		# if not name:
		sortBy = {}
		sortList = name.split(',')
		sortList.reverse()

		### Check for bad sort input
		for item in sortList:
			item = item
			try:
				if item.count(delim) > 0:
					sb = item.split(delim)[1]
				else:
					sb = item
			except Exception as e:
				errors.append({'id': 16, 'function': 'sortThis()', 'cnt': 1, 'location': 'rows[0][sb]', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})

		# itemgetter = __.imp('operator.itemgetter')
		for item in sortList:
			try:
				direction = item.split(delim)[0]
				sb = self.findColumName(item.split(delim)[1])
				if 'a' in direction:
				# if direction.find('a') == 0:
					self.asset = sorted(self.asset, key=itemgetter(sb))
				else:
					self.asset = sorted(self.asset, key=itemgetter(sb), reverse=True)
			except Exception as e:
				try:
					pass
					self.asset = sorted(self.asset, key=itemgetter(self.findColumName(item)))
				except Exception as e:
					errors.append({'id': 17, 'function': 'sortThis()', 'cnt': 2, 'location': 'rows = sorted(rows, key=itemgetter(sb))', 'vars': [{'name': 'rows', 'value': 'nope to that, to big'}, {'name': 'name', 'value': name}], 'error': e})
				
			uuid = __.imp('uuid')
			sortBy[item] = str(uuid.uuid4())
			tempFields.append( sortBy[item] )
			i = 0
			for row in self.asset:
				self.asset[i][sortBy[item]] = i
				i += 1

		# rows = sorted(rows, key=lambda d: (-d['typesort'], d['ext'], d['name']))

		sortCode = 'rows = sorted(rows, key=lambda d: ('
		for item in sortList:
			sortCode += "d['" + str(sortBy[item]) + "'],"
		sortCode = sortCode[:-1]
		sortCode += '))'
		exec(sortCode)
		if len( tempFields ):
			# print( tempFields )
			for ix,r in enumerate(rows):
				for tmp in tempFields:
					try:
						del rows[ix][tmp]
					except Exception as e:
						pass
		return self.asset

	def countThis(self):
		rows = self.asset
		i = 0
		for x in self.asset:
			i += 1
		return i

	def file(self,file):
		self.file = file

	def save(self,theFile = '',tableTemp = True,printThis = True):
		theFile=theFile.replace(os.sep+os.sep,os.sep)

		if os.sep in theFile:
			parts = theFile.split(os.sep)
			parts.reverse()
			parts.pop(0)
			parts.reverse()
			v.f.mkdir(os.sep.join(parts))

		HD.chmod(theFile)
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = str(self.file)
		self.file = theFile
		# print(theFile)
	# def saveTable(rows,theFile,tableTemp = True,printThis = True):
		# defaults to myTables
		if tableTemp == True:
			file0 = str(v.tables) + str(os.sep) + str(theFile)
		else:
			file0 = v.temp + os.sep + theFile
		dataDump = simplejson.dumps(self.asset, indent=4, sort_keys=True)
		f = open(file0,'w')
		f.write(str(dataDump))
		f.close()
		HD.chmod(theFile)
		if printThis:
			_printME_('Saved: ' + file0)
	def get(self,theFile = '',tableTemp = True,printThis = False):
		simplejson = __.imp('simplejson')
		if theFile == '':
			theFile = self.file
		self.file = theFile
		# defaults to myTables
		if tableTemp == True:
			file0 = v.tables + os.sep + theFile
		else:
			file0 = v.temp + os.sep + theFile
		if printThis:
			_printME_('Loaded: ' + file0)
		if os.path.isfile(file0) == True:
			with open(file0,'r', encoding="latin-1") as json_file:
				json_data = simplejson.load(json_file)
				# json_data = simplejson.load(json_file, object_pairs_hook=OrderedDict)
		else:
			json_data = []
		self.asset = json_data
		return json_data

	def assets(self):
		return self.asset

	def set(self,asset):
		self.asset = asset
		return self.asset

	def groupByTrigger( self ):
		try:
			if switches.isActive('GroupBy') and len(self.asset):
				newValues = []
				keys = []
				for key in self.asset[0].keys():
					keys.append( key )
				for val in switches.value('GroupBy').split( ',' ):
					for key in keys:
						if key.lower() == val.lower():
							newValues.append( key )
				if len(newValues):
					switches.fieldSet( 'GroupBy', 'value', ','.join(newValues) )
		except Exception as e:
			pass



class Tables:

	def __init__(self):
		self.tables = []
		self.index = {}
		self.maxNameLength = 35
		self.columnTab = '\t'
		self.groupSeparator = '_'
		self.group_space = False



	def aggregate( self, name=None, code=None ):
		if code is None:
			return None
		if name is None:
			name = self.tables[ len(self.tables)-1 ].name
		
		self.tables[ self.index[name] ].aggregate( code )


	def r_printME_( self, asset, columns, name=None, n=None, sc=True ):
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		if sc and switches.isActive('Column'):
			columns = switches.value('Column')
		self.print( name, columns )



	def rsort( self, asset, columns, name=None, n=None ):
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		self.register( name, asset )
		return self.returnSorted( name,columns,asset )
		# return self.sort( name, columns )


	def register( self, name=None, asset = [], group_space=True, tab='',    gs=None, t=None, n=None ):
		global TableProfile_Config
		if not n is None:
			name = n
		if name is None:
			name = genUUID()
		if not __.table_b_print:
			for i,record in enumerate(asset):
				for field in record.keys():
					if str( record[field] ) == 'b':
						asset[i][field] = ''


		found = False
		thisID = False
		if not gs is None:
			group_space = gs
		elif 'ALLTABLES' in TableProfile_Config.keys() and 'GroupSpaces' in TableProfile_Config['ALLTABLES'].keys():
			group_space = TableProfile_Config['ALLTABLES']['GroupSpaces']
		else:
			group_space = switches.isActive('GroupSpaces')
		if not t is None:
			tab = t
		for i,t in enumerate(self.tables):
			if t.name == name:
				thisID = i
				found = True
				self.tables[i].maxNameLength = self.maxNameLength
				if len(asset) > 0:
					self.tables[i].set(asset)
		if found:
			self.tables.pop( thisID )
			found = False

		if not found:
			self.tables.append(Table( name, asset, group_space, tab ))
			self.tables[ len( self.tables )-1 ].maxNameLength = self.maxNameLength
			self.index[name] = len( self.tables )-1
		return name

	def trigger(self,name,field,script,includes = False):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].trigger(field,script,includes)
			i += 1

	def registerView(self,table,name,fields,sort):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].registerView(name,fields,sort)
			i += 1

	def fieldProfileSet(self,table,field,propertyName,value):
		i = 0
		found = False
		for t in self.tables:
			if t.name == table:
				found = True
				self.tables[i].fieldProfileSet(field,propertyName,value)
			i += 1
		if not found:
			self.tables.append(Table(table,[]))
			i = 0
			for t in self.tables:
				if t.name == table:
					self.tables[i].fieldProfileSet(field,propertyName,value)
				i += 1

	def print(self,name,fields,fieldLengths=False, pc=None, printColumns=True ):
		global switches
		if not ',' in fields:
			pc = False

		xXx = switches.records('dic_on-off-v')
		if 'Sort' in xXx['on']:
			sortBy = xXx['values']['Sort']
			self.sort( name, ','.join( sortBy ) )
			# print( sortBy )
			# sys.exit()
		if not pc is None:
			printColumns = pc
		# print(name,fields)
		sI = None
		i = 0
		for t in self.tables:
			if t.name == name:
				if len(self.tables[i].asset) > 0:
					if not ',' in fields:
						printColumns = False
					self.tables[i].print(fields,fieldLengths,printColumns=printColumns)
					sI = i
				else:
					_printME_('Null Set')
			i += 1
		if switches.isActive('FieldTotal'):
			fieldTotals = {}
			for field in switches.values('FieldTotal'):
				fieldTotals[field] = { 'actual': None, 'total': 0 }
				for rec in self.tables[sI].asset:
					for key in rec.keys():
						if check_field_match( key, field ):
							fieldTotals[field]['actual'] = key
							thisFieldA = str(rec[key])
							thisFieldB = []
							for char in thisFieldA:
								if char in '0123456789':
									thisFieldB.append(char)
							thisFieldC = int(''.join(thisFieldB))
							fieldTotals[field]['total'] += thisFieldC
			_printME_()
			_printME_()
			for field in fieldTotals:
				_printME_( addComma(fieldTotals[field]['total']),'\t', fieldTotals[field]['actual'] )




	def sort(self,name,fields):
		fields = fields.replace('.',':')
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
			i += 1

	def returnSorted(self,name,fields,asset = []):
		fields = fields.replace('.',':')
		if len(asset) > 0:
			self.register(name,asset)

		result = []
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].sort(fields)
				result = self.tables[i].asset
			i += 1
		return result
	def view(self,table,name):
		i = 0
		for t in self.tables:
			if t.name == table:
				try:
					self.tables[i].printView(name)
				except Exception as e:
					pass
			i += 1

	def save(self,table,theFile = '',tableTemp = True,printThis = True):
		theFile=theFile.replace(os.sep+os.sep,os.sep)

		if os.sep in theFile:
			parts = theFile.split(os.sep)
			parts.reverse()
			parts.pop(0)
			parts.reverse()
			v.f.mkdir(os.sep.join(parts))

		HD.chmod(theFile)
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].save(theFile,tableTemp,printThis)
			i += 1
		HD.chmod(theFile)

	def get(self,table,theFile = '',tableTemp = True,printThis = False):
		theFile=theFile.replace(os.sep+os.sep,os.sep)
		theFile = str(theFile)
		if not theFile == '' and not '.json' in theFile:
			theFile = theFile + '.json'
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].get(theFile,tableTemp,printThis)
			i += 1

	def asset(self,table):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].assets()
			i += 1

	def file(self,table,theFile):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].file(theFile)
			i += 1

	def set(self,table,asset):
		i = 0
		for t in self.tables:
			if t.name == table:
				return self.tables[i].set(asset)
			i += 1

	def alignmentMasterSupersedes(self,table,value):
		i = 0
		for t in self.tables:
			if t.name == table:
				self.tables[i].tableProfileDefaultSupersedes = value
			i += 1
		
	def getLength(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		total = 0
		for r in result.keys():
			total += result[r]
			total += 5
		# print(result)
		return total

	def getFieldLengths(self,name,fields):
		i = 0
		for t in self.tables:
			if t.name == name:
				self.tables[i].showColumnHeader(fields)
				result = self.tables[i].spaces
			i += 1
		###### How it works:
		# totalColumnWidth = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   spaces = tables.getLength(m['table'],'type,field,max,min,average')
		#   if spaces > totalColumnWidth:
		#       totalColumnWidth = spaces


		# fieldLengths = 0
		# for m in self.meta['data']:
		#   tables.register(m['table'],m['fields'])
		#   data = tables.getFieldLengths(m['table'],'type,field,max,min,average')
		#   if not type(fieldLengths) == dict:
		#       fieldLengths = data
		#   for name in fieldLengths.keys():
		#       if data[name] > fieldLengths[name]:
		#           fieldLengths[name] = data[name]



		# for m in self.meta['data']:
		#   genLine(totalColumnWidth,'=')
		#   print('Table:\t',m['table'])
		#   print('Parent:\t',m['parent'])
		#   print('Records:',m['count'])
		#   print()
		#   tables.register(m['table'],m['fields'])
		#   tables.fieldProfileSet(m['table'],'*','alignment','center')
		#   tables.print(m['table'],'type,field,max,min,average',fieldLengths)

		#   genLine(totalColumnWidth,'=')
		# print()
		# print('Records:',self.meta['records'])
		# print()
		# print('Errors:')
		# for e in self.meta['errors']:
		#   print('\t',e)

		return result



	def eof( self ):
		try:
			__.aggregate.eof.storage
		except Exception as e:
			shouldPrint = False
		else:
			shouldPrint = True

		if not __.aggregate.eof.storage:
			shouldPrint = False

		if shouldPrint:
			_printME_()
			_printME_()

			linePrint()

			# print()
			# printVarSimple( __.aggregate.eof.storage )


		footer = {}
		aSettings = {}

		for k in __.aggregate.eof.storage:
			if k.startswith('eof?'):
				f = k[len('eof?'):]
				for y in __.aggregate.eof.storage[k]:
					for sv in __.aggregate.eof.storage[k][y]['settings']:
						aSettings[sv] = __.aggregate.eof.storage[k][y]['settings'][sv]

					if '?date' in __.aggregate.eof.storage[k][y]['settings']:
						__.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					theKey = f +' '+ y
					special = {}

					kk = k
					var = 'var'
					if 'var' in __.aggregate.config:
						var = 'var'
					if '?var' in __.aggregate.config:
						var = '?var'
					if 'var?' in __.aggregate.config:
						var = 'var?'

					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
					kk = '?all'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'all?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]

					kk = 'eof?'
					if var in __.aggregate.config and kk in __.aggregate.config[var]:
						for spK in __.aggregate.config[var][kk]:
							special[spK] = __.aggregate.config[var][kk][spK]
						

					if '?first' in special:
						theKey = f
					elif '?second' in special:
						theKey = y

					# print( 'format:', __.aggregate.format )
					# print( 'k y:', k, y  )

					# for fo in __.aggregate.format:
					#   if fo == k or fo == y:
					#       if '?date' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = friendlyDate( __.aggregate.eof.storage[k][y]['data'] )
					#       if '?comma' in __.aggregate.format[fo]:
					#           __.aggregate.eof.storage[k][y]['data'] = addComma( __.aggregate.eof.storage[k][y]['data'] )



					# # print(  )
					# footer[ theKey ] = __.aggregate.eof.storage[k][y]['data']
					footer[ theKey ] = __.aggregate.obj.format( [k,y], __.aggregate.eof.storage[k][y]['data'] )
		if footer:
			_printME_()
			# print()
			footer_txt = []
			footer_txt.append( __.aggregate.prefix )

			for k in footer:
				footer_txt.append( k+':' ) 
				footer_txt.append( footer[k] ) 
				footer_txt.append( spaces(2) )
			cp( footer_txt, 'cyan' ) 
			# print( __.aggregate.config )
			_printME_()
					# print( f, y, __.aggregate.storage[k][y]['data'] )
			# print( k )




 
 


def dics( items ):
	table = {}
	for item in items:
		for key in item:
			table[key] = item[key]
	return table


####################################################################################################################################



class _md5:
	def __init__( self ): pass;
		
	def md5File( self, fname ):
		if os.path.isfile(fname):
			hashlib = vc.FIG.imp('hashlib')
			hashData = hashlib.md5()
			with open(fname, "rb") as f:
				for chunk in iter(lambda: f.read(4096), b""):
					hashData.update(chunk)
			return hashData.hexdigest()
		else:
			_printME_('Error: md5 no file')
			sys.exit()

	def sha256File( self, fname ):
		hashlib = vc.FIG.imp('hashlib')
		if os.path.isfile(fname):
			hashData = hashlib.sha256()
			with open(fname, "rb") as f:
				for chunk in iter(lambda: f.read(4096), b""):
					hashData.update(chunk)
			return hashData.hexdigest()
		else:
			_printME_('Error: md5 no file')
			sys.exit()


	def file( self, fname, h='md5' ):
		hashlib = vc.FIG.imp('hashlib')
		if os.path.isfile(fname):
			hashes = [
						'md5',
						'sha1',
						'sha224',
						'sha256',
						'sha384',
						'sha512',
						'sha3_224',
						'sha3_256',
						'sha3_384',
						'sha3_512',
			]
			if not h in hashes:
				_printME_( 'Error: hash type not valid' )
				_printME_( '\t Try:', ' , '.join( hashes ) )
				sys.exit()
			if h == 'md5':
				hashData = hashlib.md5()
			if h == 'sha1':
				hashData = hashlib.sha1()
			if h == 'sha224':
				hashData = hashlib.sha224()
			if h == 'sha256':
				hashData = hashlib.sha256()
			if h == 'sha384':
				hashData = hashlib.sha384()
			if h == 'sha3_224':
				hashData = hashlib.sha3_224()
			if h == 'sha3_256':
				hashData = hashlib.sha3_256()
			if h == 'sha3_384':
				hashData = hashlib.sha3_384()
			if h == 'sha3_512':
				hashData = hashlib.sha3_512()
			if h == 'sha512':
				hashData = hashlib.sha512()


			with open(fname, "rb") as f:
				for chunk in iter(lambda: f.read(4096), b""):
					hashData.update(chunk)
			return hashData.hexdigest()
		else:
			_printME_('Error: not a file')
			sys.exit()


	def string( self, chunk, h='md5' ):
		hashlib = vc.FIG.imp('hashlib')
		hashes = [
					'md5',
					'sha1',
					'sha224',
					'sha256',
					'sha384',
					'sha512',
					'sha3_224',
					'sha3_256',
					'sha3_384',
					'sha3_512',
		]
		if not h in hashes:
			_printME_( 'Error: hash type not valid' )
			_printME_( '\t Try:', ' , '.join( hashes ) )
			sys.exit()
		if h == 'md5':
			hashData = hashlib.md5()
		if h == 'sha1':
			hashData = hashlib.sha1()
		if h == 'sha224':
			hashData = hashlib.sha224()
		if h == 'sha256':
			hashData = hashlib.sha256()
		if h == 'sha384':
			hashData = hashlib.sha384()
		if h == 'sha3_224':
			hashData = hashlib.sha3_224()
		if h == 'sha3_256':
			hashData = hashlib.sha3_256()
		if h == 'sha3_384':
			hashData = hashlib.sha3_384()
		if h == 'sha3_512':
			hashData = hashlib.sha3_512()
		if h == 'sha512':
			hashData = hashlib.sha512()

		pass
		hashData.update(bytes(chunk, 'utf-8'))
		return hashData.hexdigest()



	def bin( self, data, h='md5' ):
		hashlib = vc.FIG.imp('hashlib')
		hashes = [
					'md5',
					'sha1',
					'sha224',
					'sha256',
					'sha384',
					'sha512',
					'sha3_224',
					'sha3_256',
					'sha3_384',
					'sha3_512',
		]
		if not h in hashes:
			_printME_( 'Error: hash type not valid' )
			_printME_( '\t Try:', ' , '.join( hashes ) )
			sys.exit()
		if h == 'md5':
			hashData = hashlib.md5()
		if h == 'sha1':
			hashData = hashlib.sha1()
		if h == 'sha224':
			hashData = hashlib.sha224()
		if h == 'sha256':
			hashData = hashlib.sha256()
		if h == 'sha384':
			hashData = hashlib.sha384()
		if h == 'sha3_224':
			hashData = hashlib.sha3_224()
		if h == 'sha3_256':
			hashData = hashlib.sha3_256()
		if h == 'sha3_384':
			hashData = hashlib.sha3_384()
		if h == 'sha3_512':
			hashData = hashlib.sha3_512()
		if h == 'sha512':
			hashData = hashlib.sha512()

		pass
		hashData.update(data)
		return hashData.hexdigest()


	def md5Bin( self, data ):
		hashlib = vc.FIG.imp('hashlib')
		hashData = hashlib.md5()
		hashData.update(data)
		return hashData.hexdigest()

	def md5( self, chunk ):
		hashlib = vc.FIG.imp('hashlib')
		hashData = hashlib.md5()
		hashData.update(bytes(chunk, 'utf-8'))
		return hashData.hexdigest()
				
	def md52GUID( self, string, brackets ):
		string = string.upper()
		result = ''
		result += str(string[0:8])
		result += str('-')
		result += str(string[8:12])
		result += str('-')
		result += str(string[12:16])
		result += str('-')
		result += str(string[16:20])
		result += str('-')
		result += str(string[20:32])
		if brackets == True:
			result = '{' + result + '}'
		return result





####################################################################################################################################
def setPipeData( data, clean=True ):
	result = []
	if len(data) > 0:
		if not clean:
			return data
		for pd in data:
			if clean:
				pd = pd.replace('\n','')
				pd = pd.replace('\r','')
				if not pd == '':
					result.append(pd)
			else:
				result.append(pd)
	return result

####################################################################################################################################









# C3PO_4life.4


####################################################################################################################################





'''
cat D:\\tech\\hosts\\VULCAN\\programs\\python\\validate-tool.py + _. - __. 
'''

os.sep = os.sep
class Validator:
	def __init__( self ):
		pass
	def register( self, asset, language, project=None ):
		if not project is None:
			__.objectPath=project
		self.logistics=vc.HD.getTable( 'auditCodeBase.index' )
		self.asset=asset
		self.language=language
		self.stringDelim='-B248-'
		self.inlineComments=[]
		self.multilineComments=[]
		self.locationTable=[]
		self.relevantTable={ 'char': [], 'multi': [], 'records': [] }
		self.tickets={}
		self.omitRanges=[]
		self.idCache=[]
		self.idOmitCache=[]
	def dump(self):
		self.projectFile
		pickle=vc.FIG.imp('pickle')
		if not pickle is None:
			with open( objFile()  , 'wb') as objSelf:
				pickle.dump(self, objSelf, pickle.HIGHEST_PROTOCOL )
			cp( 'Saved: ' + objFile(), 'green' )
	def auditOmit( self ):
		result=''
		for i in self.idOmitCache:
			char=self.asset[i]
			result +=char
		_printME_( result )
	def printPos( self, start, end, p=True ):
		if p:
			_printME_( 'diff:', end-start )
			_printME_( '__________________________' )
		theEnd=len(self.asset) -(  end )
		payload=self.asset[ start :-theEnd ]
		if p:
			_printME_( 'payload:' )
			cp( payload )
			_printME_( '__________________________' )
		return payload
	def process( self ):
		self.idCache=[]
		a=len(self.asset)
		i=0
		while not a==len(self.idCache):
			self.idCache.append( i )
			i+=1
		
		self.buildRelevantTable( comment=True )
		self.buildLocationTable()
		self.omitTickets()
		self.buildIDCache()
		self.buildRelevantTable( quote=True )
		self.buildLocationTable()
		self.omitTickets()
		self.buildIDCache()
		self.buildRelevantTable()
		self.buildLocationTable()
		_printME_( 'closed:', len(self.locationTable) )
		vc.HD.saveTable( self.tickets, 'auditCodeBase_errors.json' )
		self.dump()
	def createIndex( self, asset, language='global', skipLoad=False, simple=False, A=None, B=None, C=None, addString=None ):
		self.addString=addString
		if A is None and B is None and C is None:
			self.index_process='A'
		elif not B is None:
			self.index_process='B'
		elif not A is None:
			self.index_process='A'
		elif not C is None:
			self.index_process='C'
		self.isSimple=simple
		self.logistics={'characters': [{'id': 0, 'char': '[', 'print': '[', 'database': [], 'profiles': [{'language': 'global', 'groupID': 0, 'tags': ['list'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': True, 'hasClose': True}]}, {'id': 1, 'char': ']', 'print': ']', 'database': [], 'profiles': [{'language': 'global', 'groupID': 0, 'tags': ['list'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 2, 'char': '(', 'print': '(', 'database': [], 'profiles': [{'language': 'global', 'groupID': 1, 'tags': ['parentheses'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': True, 'hasClose': True}]}, {'id': 3, 'char': ')', 'print': ')', 'database': [], 'profiles': [{'language': 'global', 'groupID': 1, 'tags': ['parentheses'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 4, 'char': '{', 'print': '{', 'database': [], 'profiles': [{'language': 'global', 'groupID': 2, 'tags': ['dict'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': True, 'hasClose': True}]}, {'id': 5, 'char': '}', 'print': '}', 'database': [], 'profiles': [{'language': 'global', 'groupID': 2, 'tags': ['dict'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 6, 'char': '/', 'print': '/', 'database': [], 'profiles': [{'language': 'javascript', 'groupID': 4, 'tags': ['inline comment'], 'set': [6], 'escape': [], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}, {'language': 'javascript', 'groupID': 3, 'tags': ['comment'], 'set': [7], 'escape': [], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}, {'language': 'global', 'groupID': False, 'tags': ['regex'], 'set': [], 'escape': [18], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}]}, {'id': 7, 'char': '*', 'print': '*', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript', 'groupID': 3, 'tags': ['comment'], 'set': [6], 'escape': [], 'rules': [], 'nest': False, 'isOpen': False, 'hasClose': False}]}, {'id': 8, 'char': '\n', 'print': '\\n', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['carriage', 'end', 'return'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'global', 'groupID': 4, 'tags': ['carriage', 'end', 'return'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 9, 'char': ' ', 'print': ' ', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['whitespace'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 10, 'char': '\t', 'print': '\\t', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['tab'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript', 'groupID': False, 'tags': ['whitespace'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 11, 'char': "'", 'print': "'", 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['quote'], 'set': [], 'escape': [18], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}, {'language': 'python', 'groupID': False, 'tags': ['quote'], 'set': [11, 11], 'escape': [18], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}]}, {'id': 12, 'char': '"', 'print': '"', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['quote'], 'set': [], 'escape': [18], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': True}, {'language': 'python', 'groupID': False, 'tags': ['quote'], 'rules': [], 'nest': False, 'set': [12, 12], 'escape': [], 'isOpen': True, 'hasClose': True}]}, {'id': 13, 'char': '=', 'print': '=', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['equals'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 14, 'char': ';', 'print': ';', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript', 'groupID': False, 'tags': ['end'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 15, 'char': ':', 'print': ':', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript_Archive', 'groupID': 5, 'tags': ['nsField'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': True, 'hasClose': False}]}, {'id': 16, 'char': '#', 'print': '#', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'python', 'groupID': False, 'tags': ['inline comment'], 'set': [], 'escape': [], 'rules': [], 'nest': False, 'isOpen': True, 'hasClose': False}]}, {'id': 17, 'char': ',', 'print': ',', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': ['delimiter'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript', 'groupID': 5, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 18, 'char': '\\', 'print': '\\', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'javascript', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 19, 'char': '<', 'print': '<', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'java', 'groupID': 6, 'tags': ['angle'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 20, 'char': '>', 'print': '>', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}, {'language': 'java', 'groupID': 6, 'tags': ['angle'], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 21, 'char': '.', 'print': '.', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}, {'id': 22, 'char': '+', 'print': '+', 'database': [], 'profiles': [{'language': 'global', 'groupID': False, 'tags': [], 'set': [], 'escape': [], 'rules': [], 'nest': True, 'isOpen': False, 'hasClose': False}]}], 'action': [{'id': 0, 'description': 'namespace', 'language': 'javascript', 'patterns': [{'type': 'text', 'strict': 0, 'test': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.'}, {'type': 'text', 'strict': 1, 'test': '='}, {'type': 'index', 'strict': 1, 'test': '{'}], 'specific': False, 'caseStrict': False, 'start': True, 'type': [3], 'rules': ['validate namespace']}], 'type': [{'id': 0, 'name': 'function'}, {'id': 1, 'name': 'class'}, {'id': 2, 'name': 'label'}, {'id': 3, 'name': 'variable'}, {'id': 4, 'name': 'command'}], 'rules': [{'id': 0, 'language': 'javascript', 'tags': 'namespace,validate', 'description': 'validate namespace', 'loop': True, 'rules': [], 'patterns': [{'type': 'text', 'strict': 0, 'test': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.', 'rules': []}, {'type': 'text', 'strict': 1, 'test': ':', 'rules': []}, {'type': 'scan', 'strict': 1, 'test': 'namespace variable', 'rules': []}, {'type': 'text', 'strict': 5, 'test': ',', 'rules': []}]}, {'id': 1, 'language': 'javascript', 'tags': 'namespace,variable,quote', 'description': 'namespace variable', 'loop': False, 'rules': [], 'patterns': [{'type': 'index', 'strict': 1, 'test': '"', 'rules': []}]}, {'id': 2, 'language': 'javascript', 'tags': 'namespace,variable,quote', 'description': 'namespace variable', 'loop': False, 'rules': [], 'patterns': [{'type': 'index', 'strict': 1, 'test': "'", 'rules': []}]}, {'id': 3, 'language': 'javascript', 'tags': 'namespace,variable,braces', 'description': 'namespace variable', 'loop': False, 'rules': ['validate namespace'], 'patterns': [{'type': 'index', 'strict': 1, 'test': '{', 'rules': []}]}, {'id': 4, 'language': 'javascript', 'tags': 'namespace,variable,bracket', 'description': 'namespace variable', 'loop': False, 'rules': ['validate bracket'], 'patterns': [{'type': 'index', 'strict': 1, 'test': '[', 'rules': []}]}, {'id': 5, 'language': 'javascript', 'tags': 'namespace,variable,bracket', 'description': 'namespace variable', 'loop': False, 'rules': ['validate bracket'], 'patterns': [{'type': 'index', 'strict': 1, 'test': '[', 'rules': []}]}, {'id': 6, 'language': 'javascript', 'tags': 'namespace,variable,function', 'description': 'namespace variable', 'loop': False, 'rules': ['validate bracket'], 'patterns': [{'type': 'text', 'strict': 1, 'test': 'function', 'rules': []}, {'type': 'index', 'strict': 1, 'test': '(', 'rules': []}, {'type': 'index', 'strict': 1, 'test': '{', 'rules': []}]}, {'id': 7, 'language': 'javascript', 'tags': 'namespace,variable,number', 'description': 'namespace variable', 'loop': False, 'rules': [], 'patterns': [{'type': 'text', 'strict': 0, 'test': '0123456789.', 'rules': []}, {'type': 'text', 'strict': 1, 'test': ',', 'rules': []}]}, {'id': 8, 'language': 'javascript', 'tags': 'scan,namespace', 'description': 'scan', 'loop': False, 'rules': [], 'patterns': [{'type': 'text', 'strict': 0, 'test': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.', 'rules': []}, {'type': 'text', 'strict': 1, 'test': '=', 'rules': []}, {'type': 'index', 'strict': 1, 'test': '{', 'rules': ['validate namespace']}]}]}
		self.backupLoaded={ 'attempted': False, 'indexes': False, 'validaton': False, 'profile': False }
		if not len( asset ):
			_printME_( 'No Data' )
			return []
		self.asset=asset
		self.language=language
		self.skipLoad=skipLoad
		self.individualIndexes=[]
		self.flat={}
		self.omitIndex=[]
		self.indexes={ 'char': [], 'group': [], }
		self.validaton={}
		self.profile={}
		self.MD5=vc.md5.md5( self.asset )
		self.projectFile='auditCodeBase_MD5_' + self.MD5 + '_PROJECT.json'
		__.validator_Project=self.MD5
		try:
			self.rlID
		except Exception as e:
			self.rls={}
			self.rlID=0
			
		
		
		
		
		if not self.skipLoad:
			self.loadProject()
			
			
		
		if not self.backupLoaded['indexes']:
			self.buildIndexes()
			self.saveProject()
		
		return self.indexes
	def filePath( self ):
		_printME_( self.projectFile.replace( 'PROJECT', 'indexes' ) )
		_printME_( self.projectFile.replace( 'PROJECT', 'validaton' ) )
	def lookupChars( self ):
		_printME_( '"', ord('"') )
		_printME_()
		for i,char in enumerate(self.asset):
			_printME_( char, ord( char ) )
		sys.exit()
	def colorPrint_old( self ):
		
		
		
		
		pass
		indexes={}
		colors=[
					[ '//', 'blue,darkcyan' ],
					[ '/*', 'blue,darkcyan' ],
					[ '*/', 'blue,darkcyan' ],
					[ '{', 'green' ],
					[ '}', 'green' ],
					[ '[', 'yellow' ],
					[ ']', 'yellow' ],
					[ '"', 'cyan,darkcyan' ],
					[ "'", 'cyan,darkcyan' ],
					
					
					[ ":", 'red' ],
					[ "=", 'red' ],
					[ ",", 'purple' ],
					[ ";", 'darkcyan' ],
					[ "(", 'Background.red' ],
					[ ")", 'Background.red' ],
				]
		pass
		for color in colors:
			theColors=[]
			if ',' in color[1]:
				theColors=color[1].split(',')
			else:
				theColors.append( color[1] )
			cID=self.query( color[0], justIDs=True, isChar=True )
			gID=self.query( color[0], justIDs=True, isGroup=True )
			self.indexes['char'][ cID ]['color']=theColors[0]
			if not gID is None:
				if ',' in color[1]:
					self.indexes['group'][ gID ]['color']=theColors[1]
				else:
					self.indexes['group'][ gID ]['color']=theColors[0]
		
		posColor=[]
		for i,char in enumerate(self.asset):
			setColor=None
			for color in colors:
				
				
				cIndexes=self.query( color[0], justIndex=False, isChar=True )
				gIndexes=self.query( color[0], justIndex=False, isGroup=True )
				
				
				
				if not gIndexes is None and not gIndexes['nestable']:
					
					if i in gIndexes['inner']:
						setColor=gIndexes['color']
				if setColor is None and i in cIndexes['index']:
					setColor=cIndexes['color']
			
			if setColor is None:
				pass
				_printME_( char, end='' )
			else:
				
				
				
				_printME_( cp( char, color=setColor, shouldPrint=False ), end='' )
				
		pass

	def dicFix( self, f,var, add ):
		_printME_(type(var),type(add))
		table = {}
		table2 = {}
		if type(var) == dict:
			for k in var:
				table2[k] = var[k]

		if type(add) == dict:
			for k in add:
				table[k] = add[k]
			return table
		return add

		if type(table2) == dict:
			table2[f] = table
			return table2
		if not type(add) == dict:
			table2[f] = table
			return table2
		return table



		if type(var) == dict and type(add) == dict:
			for k in table:
				table2[k] = table[k]
			return table2

		else:
			table2[f] = table
			return table2

	def genJson_rec( self, dic ):

		# print('dic',type(dic), dic, )
		n = {}
		for k in dic:
			n[k] = dic[k]
		self.json_records.append(n)


	def genJson( self ):
		self.json_records = []
		def getData(o,c,f=None, p=[],v={}, l=None, spent=[], rec=[], top=True, li=[]):
			# print(0,o)

			# print(o,spent)
			# o+=1
			# c-=1
			oo = o
			cc = c
			# print(o,c, spent)

			while oo < c :
				if oo in spent:
					oo+=1
				spent.append(oo)
				# print(oo)
				if oo in self.identity['location']['open']:
					
					cc = self.identity['location']['open'][oo]
					txt=self.assetSnipet( oo, cc )
					txtl=txt.lower()
					txtq=txt.replace('"','')
					
					# print(txt)
					if txt.startswith('['):
						if not f is None:
							# print(7,txt)
							txt4=self.assetSnipet( oo, cc )
							# print(6,txt4)
							# z1 = vc.HD.process_code(txt)
							z2 = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=[], top=True, li=[])
							v[f] = z2
							# print( '-' )
							# print( 'z1', z1 )
							# print( 'z2', z2 )
							# print( '-' )
							# v[f] = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=True, li=li)
							# v[f] = self.dicFix(f,v,getData(oo,cc,f=None, p=[],v=v, l=None, spent=spent, rec=rec, top=True, li=li))
							# v = self.dicFix(f,v,getData(oo,cc,f=None, p=[],v=v, l=None, spent=spent, rec=rec, top=True, li=li))
						else:
							vx = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=False, li=li)
							# print('vx',vx)
						f = None
						# rec.append(vx)
						# print('vx',vx)
					elif txt.startswith('{'):
						if not f is None:
							# print(8,txt,f)
							# z1 = vc.HD.process_code(txt)
							z2 = getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=True, li=li)
							v[f] = z2
							# print( '-' )
							# print( 'z1', z1 )
							# print( 'z2', z2 )
							# print( '-' )
							# v = self.dicFix(f,v,getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=True, li=li))
							# v[f] = self.dicFix(f,v,getData(oo,cc,f=None, p=[],v={}, l=None, spent=spent, rec=rec, top=True, li=li))
						else:
							vy = getData( oo, cc, None, p, {}, l, spent, rec, False, li )
							self.genJson_rec(vy)
						# vy = getData( oo+1, cc-1, None, p, v, l, spent, rec, False )
						# rec.append(vy)
						f = None
						# print('vy',vy, rec)
					elif txt and txt[0] in '"':
						li.append(txtq)

						if self.asset[o] == '{':
							if f is None:
								f = txtq
								p.append(f)
								# print('f',txtq)
							else:
								v[f] = txtq
								# print(f,txtq)
								f = None


					elif txt and txt[0] in '0123456789.-':
						if '.' in txt:
							xx = float(txt)
						else:
							xx = int(txt)
						# print(self.asset[o],txt)
						li.append(xx)
						v[f] = xx
						# print(f,txt)
						f = None

					elif txtl.lower().startswith('true'):
						li.append(True)
						v[f] = True
						# print(f,True)
						f = None
					elif txtl.lower().startswith('false'):
						li.append(False)
						# print(f,False)
						v[f] = False
						f = None
					oo = cc


				oo+=1
				# break
			if top:
				if self.asset[o] == '[':
					if self.json_records:
						return self.json_records
					else:
						return li
						# print('end',li,self.json_records)
				else:
					if len(self.json_records) > 1:
						return self.json_records
					if self.json_records:
						return self.json_records[0]
					return v
			# print('r',self.asset[o])
			if self.asset[o] == '[':
				return li
			return v
			if self.asset[o] == '{':
				return v




		o = 0
		c = len(self.asset)-1

		ss = getData(o,c)
		# print(self.json_records)
		# print(ss)
		return ss

		# self.identity['location']['open'][o]
		# self.identity['identity'][o]

		# for o,c in enumerate(self.asset):
		#   if o in self.identity['location']['open']:
		#       c = self.identity['location']['open'][o]
		#       txt=self.assetSnipet( o, c )
		#       print(txt)

		# table = {}
		# last=''
		# for i,o in enumerate(self.identity['identity']):
		#   c=self.identity['location']['open'][o]
		#   txt=self.assetSnipet( o, c )
		#   print(txt)
		#   if '"' in txt:
		#       txt = txt.replace('"','')
		#   elif txt[0] in '0136456789.-':
		#       if '.' in txt:
		#           txt = float(txt)
		#       else:
		#           txt = int(txt)
		#   elif 'false' in txt.lower():
		#       txt = False
		#   elif 'true' in txt.lower():
		#       txt = True

		#   ii=i+1
		#   if ii % 2 == 0:
		#       # print( 4, a )
		#       table[last] = txt
		#   else:
		#       last=txt
		# pv(table)
		# return table

		# # for k in self.indexes:
		# #     print(k)

		# print( self.indexes['char'] )
		# print( self.indexes['individual'] )

		# print( self.indexes['group'] )
		# for rec in self.indexes['group']:
		#   print( rec['label'] )

	def colorPrint( self ):
		
		
		
		
		pass
		indexes={}
		colors={
					'all': {
								'alphaLower': {  'c': 'cyan', 'b': None, 'attr': 'bold'  },
								'alpha': {  'c': 'cyan', 'b': None, 'attr': 'bold'  },
								'alphaNumeric': {  'c': 'cyan', 'b': None, 'attr': 'bold'  },
								'alphaUpper': {  'c': 'cyan', 'b': None, 'attr': 'bold'  },
								'number': {  'c': 'white', 'b': None, 'attr': 'bold'  },
								'float': {  'c': 'white', 'b': None, 'attr': 'bold'  },
								
								
								'bool': {  'c': 'magenta', 'b': None, 'attr': 'bold'  },
					},
					'parts': {
								'quote': [{  'c': 'cyan', 'b': None, 'attr': None  },{  'c': 'cyan', 'b': None, 'attr': 'bold'  }],
								'regex': [{  'c': 'red', 'b': None, 'attr': None  },{  'c': 'red', 'b': None, 'attr': 'bold'  }],
								'inline comment': [{  'c': 'red', 'b': None, 'attr': 'bold'  },{  'c': 'green', 'b': None, 'attr': None  }],
								'comment': [{  'c': 'red', 'b': None, 'attr': 'bold'  },{  'c': 'green', 'b': None, 'attr': None  }],
					},
					'ends': {
								'dict': {  'c': 'green', 'b': None, 'attr': 'bold'  },
								'list': {  'c': 'yellow', 'b': None, 'attr': 'bold'  },
								'parentheses': {  'c': 'yellow', 'b': None, 'attr': None  },
								
					},
					'chars': {
								',': {  'c': 'cyan', 'b': None, 'attr': 'dark'  },
								'+': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'=': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								':': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'!': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'?': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								';': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'|': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'%': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'&': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'@': {  'c': 'red', 'b': None, 'attr': 'bold'  },
								'$': {  'c': 'red', 'b': None, 'attr': 'bold'  },
					},
		}
		items=[
					"alpha",
					"alphaLower",
					"alphaNumeric",
					"alphaUpper",
					"number",
					"float",
					"comment",
					"inline comment",
					
					"bool",
					
					"quote",
					"regex"
					"dict",
					"list",
					"parentheses",
		]
		action={}
		actionLenClose={}
		actionLenOpen={}
		for aID in self.action:
			for x in items:
				if x in self.action[aID]['tags']:
					if not self.action[aID]['close']['label'] is None and len(self.action[aID]['close']['label']) > 1:
						action[x]=aID
						actionLenClose[x]=len(self.action[aID]['close']['label'])
					if len(self.action[aID]['open']['label']) > 1:
						actionLenOpen[x]=len(self.action[aID]['open']['label'])
		pass
		
		
		
		
		
		close={}
		pass
		o=0
		end=len(self.asset)
		while not o==end:
			if o in self.identity['identity'] or o in close:
				if o in self.identity['identity']:
					ident=self.identity['identity'][o]
				elif o in close:
					ident=self.identity['identity'][close[o]]
				if ident in colors['all']:
					dent=colors['all'][ident]
					c=self.identity['location']['open'][o]
					if ident in actionLenClose:
						c-=1
						c+=actionLenClose[ident]
					txt=self.assetSnipet( o, c )
					
					
					_printME_( nothing( txt, c=dent['c'], b=dent['b'], attr=dent['attr'], p=0 ), end='' )
					
					o=c
				elif ident in colors['parts']:
					dent=colors['parts'][ident]
					oo=o
					oc=o
					c=self.identity['location']['open'][o]
					cc=c
					ooo=1
					ccc=1
					if ident in actionLenOpen:
						ooo=actionLenOpen[ident]
						oc-=1
						oc+=ooo
					if ident in actionLenClose:
						ccc=actionLenClose[ident]
						cc-=1
						cc+=ccc
					io=o + ooo
					ic=c - ccc
					txt=self.assetSnipet( o, oc )
					_printME_( nothing( txt, c=dent[0]['c'], b=dent[0]['b'], attr=dent[0]['attr'], p=0 ), end='' )
					txt=self.assetSnipet( io, ic )
					_printME_( nothing( txt, c=dent[1]['c'], b=dent[1]['b'], attr=dent[1]['attr'], p=0 ), end='' )
					
					if not ic==c-1:
						icc=ic
						while not icc==c-1:
							icc+=1
							_printME_( self.asset[icc], end='' )
					txt=self.assetSnipet( c, cc )
					_printME_( nothing( txt, c=dent[0]['c'], b=dent[0]['b'], attr=dent[0]['attr'], p=0 ), end='' )
					o=cc
				elif ident in colors['ends']:
					dent=colors['ends'][ident]
					if o in self.identity['location']['open']:
						c=self.identity['location']['open'][o]
						close[c]=o
						oo=o
						oc=o
						ooo=1
						if ident in actionLenOpen:
							ooo=actionLenOpen[ident]
							oc-=1
							oc+=ooo
						io=o + ooo
						txt=self.assetSnipet( o, oc )
						_printME_( nothing( txt, c=dent['c'], b=dent['b'], attr=dent['attr'], p=0 ), end='' )
						o-=1
						o+=ooo
					elif o in close:
						c=o
						cc=c
						ccc=1
						if ident in actionLenClose:
							ccc=actionLenClose[ident]
							cc-=1
							cc+=ccc
						ic=c - ccc
						txt=self.assetSnipet( c, cc )
						_printME_( nothing( txt, c=dent['c'], b=dent['b'], attr=dent['attr'], p=0 ), end='' )
						o-=1
						o+=ccc
				else:
					_printME_( self.asset[o], end='' )
			elif self.asset[o] in colors['chars']:
				dent=colors['chars'][ self.asset[o] ]
				_printME_( nothing( self.asset[o], c=dent['c'], b=dent['b'], attr=dent['attr'], p=0 ), end='' )
			else:
				_printME_( self.asset[o], end='' )
			o+=1
		_printME_()
		return None
		sys.exit()
		ident=[]
		for x in self.identity['identity']:
			y=self.identity['identity'][x]
			if not y in ident:
				ident.append(y)
		printVar( ident )
		sys.exit()
		self.identity['location']['open'][o]
		self.identity['identity'][o]
		for i,char in enumerate(self.asset):
			if setColor is None:
				pass
				_printME_( char, end='' )
			else:
				
				
				
				_printME_( cp( char, color=setColor, shouldPrint=False ), end='' )
	def query( self, label=None, special=None, iID=None, gID=None, cID=None, rID=None, pID=None, oc='open,close', tag=None, pos=None, justIDs=None, isOpen=None, justIndex=False, isChar=False, isGroup=False, quoteComment=False ):
		
		locationLabel=None
		if quoteComment:
			records=[]
			for i,item in enumerate(self.indexes['group']):
				add=False
				for t in item['tags']:
					if 'quote' in t:
						add=True
					if 'comment' in t:
						add=True
				if add:
					records.append( i )
			return records
		elif not label is None and not justIndex and isChar and not isGroup and justIDs:
			locationLabel='01'
			theID=self.itemLabel( label, 'char' )
			if theID is None:
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return theID
		elif not label is None and not justIndex and not isChar and isGroup and justIDs:
			locationLabel='02'
			theID=self.itemLabel( label, 'group' )
			if theID is None:
				return None
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return theID
		elif not label is None and justIndex and isChar and not isGroup:
			locationLabel='03'
			
			theID=self.itemLabel( label, 'char' )
			if theID is None:
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			result=self.indexes['char'][ theID ]['index']
			
			if result is None:
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return result
		elif not label is None and not justIndex and isChar and not isGroup:
			locationLabel='04'
			theID=self.itemLabel( label, 'char' )
			if theID is None:
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			result=self.indexes['char'][ theID ]
			
			if result is None:
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			return result
		elif not label is None and not justIndex and not isChar and isGroup:
			locationLabel='05'
			theID=self.itemLabel( label, 'group' )
			if theID is None:
				return None
				cp( [ 'Query Error:', locationLabel, label ] )
				sys.exit()
			result=self.indexes['group'][ theID ]
			
			if result is None:
				cp( label, 'red' )
				sys.exit()
			return result
		elif not justIDs is None:
			if not label is None and special is None:
				info={ 'gID': None, 'iID': None }
				for i,item in enumerate(self.indexes['group']):
					if item['label']==label:
						info['gID']=i
				for i,item in enumerate(self.indexes['char']):
					if item['label']==label:
						info['iID']=i
				return info
			elif not tag is None and special is None and ',' in tag:
				
				records=[]
				for i,item in enumerate(self.indexes['group']):
					add=False
					for t in item['tags']:
						found=0
						for test in tag.split( ',' ):
							if test in t:
								found +=1
						if found==len( tag.split( ',' ) ):
							add=True
					if add:
						records.append( i )
				return records
			elif not tag is None and not special is None and ',' in tag and 'all' in special:
				
				records=[]
				for i,item in enumerate(self.indexes['group']):
					add=False
					for t in item['tags']:
						found=0
						for test in tag.split( ',' ):
							if test in t:
								add=True
					if add:
						records.append( i )
				return records
			elif not tag is None and special is None:
				records=[]
				for i,item in enumerate(self.indexes['group']):
					for t in item['tags']:
						if t==tag:
							records.append( i )
				return records
			elif not tag is None and not special is None and type(special)==str and 'includes' in special and not ':' in special:
				records=[]
				for i,item in enumerate(self.indexes['group']):
					if tag in item['tags']:
						records.append( i )
				return records
			elif not tag is None and not special is None and type(special)==str and 'exclude' in special and not ':' in special:
				records=[]
				for i,item in enumerate(self.indexes['group']):
					added=False
					for tagX in item['tags']:
						for exclude in tag.split(','):
							if not exclude in tagX:
								if not added:
									added=True
									records.append( i )
				return records
		return None
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
					
					
					
					
					
					
					
					
					
					
					
					
						
		
		
		
		
		
		
		
		
		
		
		
	
		
	
	
	
	
	
	
	
	
	
	def loadProject( self ):
		self.backupLoaded['attempted']=True
		self.backupLoaded['validaton']
		if not self.skipLoad:
			projectFile_indexes=vc.HD.getTable( self.projectFile.replace( 'PROJECT', 'indexes' ), 1 )
			projectFile_validaton=vc.HD.getTable( self.projectFile.replace( 'PROJECT', 'validaton' ), 1 )
			projectFile_profile=vc.HD.getTable( self.projectFile.replace( 'PROJECT', 'profile' ), 1 )
			self.identity=vc.HD.getTable( self.projectFile.replace( 'PROJECT', 'identity' ), 1 )
			if not len(projectFile_indexes):
				self.backupLoaded['indexes']=False
			else:
				self.backupLoaded['indexes']=True
				self.indexes=projectFile_indexes
			if not len(projectFile_validaton):
				self.backupLoaded['validaton']=False
			else:
				self.backupLoaded['validaton']=True
				self.validaton=projectFile_validaton
			if not len(projectFile_profile):
				self.backupLoaded['profile']=False
			else:
				self.backupLoaded['profile']=True
				self.profile=projectFile_profile
	def saveProject( self ):
		vc.HD.saveTable( self.indexes, self.projectFile.replace( 'PROJECT', 'indexes' ) )
		if self.profile:
			vc.HD.saveTable( self.profile, self.projectFile.replace( 'PROJECT', 'profile' ) )
		
		try:
			vc.HD.saveTable( self.identity, self.projectFile.replace( 'PROJECT', 'identity' ) )
		except Exception as e:
			pass
		
	def buildActionQueue( self, xID ):
		
		
		if not xID in self.buildActionQueueSpent:
			self.buildActionQueueSpent.append( xID )
			self.action[ self.action_queue ]=self.indexes['group'][xID]
			self.action[ self.action_queue ]['scanID']=0
			
			self.posTable[ self.action[ self.action_queue ]['open']['label'] ]=[]
			self.scanID[ str(self.action_queue)+'escape' ]=0
			self.scanID[ self.action_queue ]=0
			self.scanID[ str(self.action_queue) + 'open']=0
			self.scanID[ str(self.action_queue) + 'close']=0
			self.theNestID[ self.action_queue ]=0
			self.scanEscapeActive[ self.action_queue ]=None
			
			self.scanIsOpen[ self.action_queue ]=False
			self.action_queue +=1
		else:
			_printME_( 'Omited Dupicate', xID )
		
	def buildCarriageIndex( self ):
		
		self.carriageIndex={
						'index': [],
						'line': [],
						'label': ''
		}
		line=0
		self.carriageIndex['index'].append( 0 )
		for i,char in enumerate(self.asset):
			self.carriageIndex['line'].append( line )
			if char=='\n':
				line +=1
				self.carriageIndex['index'].append( i )
	def getLine( self, pos ):
		
		
		
		
		try:
			return self.carriageIndex['line'][pos]
		except Exception as e:
			return self.indexes['carriageIndex']['line'][pos]
	
	def getLinePos( self, line ):
		return self.indexes['carriageIndex']['index'][line]
	def getLineStartEnd( self, line ):
		pos=self.getLinePos( line )
		try:
			end=self.getLinePos( line+1 )
		except Exception as e:
			end=len( self.asset )-1
		return { 'start': pos, 'end': end }
	def buildIndividualIndexes( self, char ):
		shouldAdd=True
		for x in self.indexes['char']:
			if x['label']==char:
				shouldAdd=False
		if shouldAdd:
			self.flat[char]=[]
			
			
			
			
			
			
			
			
			
			
			
	def buildIndexes( self ):
		
		self.buildIndexStructure()
		self.buildCarriageIndex()
		self.action_queue=0
		self.action={}
		self.table={}
		self.tableID={}
		self.posTable={}
		self.scanID={}
		self.theNestID={}
		self.scanIsOpen={}
		self.scanEscapeActive={}
		self.buildActionQueueSpent=[]
			
			
			
			
			
		self.buildIndividualIndexes( ':' )
		self.buildIndividualIndexes( ',' )
		self.buildIndividualIndexes( '=' )
		self.buildIndividualIndexes( ';' )
		self.buildIndividualIndexes( os.sep )
		self.indexes['individual']=list( self.flat.keys() )
		
		
		
		
		
		
		
		
		
		
		
		for xID in self.query( tag='inline,comment', justIDs=True ):
			
			self.buildActionQueue( xID )
		
		
		for xID in self.query( tag='comment', justIDs=True ):
			self.buildActionQueue( xID )
		for xID in self.query( tag='comment', justIDs=True, special='exclude' ):
			self.buildActionQueue( xID )
		
		
		
		
		
		
		
		
		self.allClosed=[]
		self.identity={
								'location': {
												'open': {},
												'close': {},
												'action': {},
								},
								'identity': {},
								'validation': {},
								'oc': [],
								'dic': [],
								'dicType': {},
								'fn': [],
								'list': [],
								'par': [],
		}
		if self.index_process=='A':
			self.buildIndexes_Process_A()
		elif self.index_process=='B':
			self.buildIndexes_Process_B()
		elif self.index_process=='C':
			self.buildIndexes_Process_C()
	def buildIndexes_Process_A( self ):
		isSimple=self.isSimple
		nestable={
					'status': False,
					'close': None,
		}
		
		
		nestTickets={}
		auditIsClose={}
		loopCheck=0
		testA=0
		testB=0
		testC=0
		testD=0
		testE=0
		loopLen=len( self.action.keys() ) 
		savedIn=[]
		nestAudit={
						'firstRun': True,
						'id': 0,
						'spent': [],
		}
		
		
		
		scanChars=[]
		scanChars.append( ' ' )
		scanChars.append( '\n' )
		scanChars.append( '\t' )
		
		identification={
							'all': '-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							'notFirst': '-:',
							'scan': [
											'0123456789',
											'.0123456789',
											'abcdefghijklmnopqrstuvwxyz',
											'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							],
							'label': [
											'number',
											'float',
											'alphaLower',
											'alphaUpper',
											'alpha',
											'alphaNumeric',
							],
							'id': None,
							'active': False,
							'start': None,
							'max': None,
		}
		identification['max']=len( identification['scan'] )-1
		
		
		
		
		
		
		
		
		
		
		def genLabel( aID ):
			
			
			tempLabel='_'.join(  self.action[ aID ]['tags']  )
			return tempLabel
			tempLabel=self.action[ aID ]['open']['label']
			if not self.action[ aID ]['close']['label'] is None:
				tempLabel+=self.stringDelim+self.action[ aID ]['close']['label']
			return tempLabel
		for record in self.logistics['characters']:
			scanChars.append( record['char'] )
		scanChars=set(scanChars)
		startTime=time.time()
		for i,char in enumerate(self.asset):
			loopCheck +=1
			aID=0
			saved=False
			nestAudit['firstRun']=True
			allClosed=True
			factor=False
			if True:
				while not aID==( loopLen ):
					if not saved or False:
						if self.action[ aID ]['close']['label'] is None:
							pass
						aIDxx=str(aID) + 'escape'
						if not self.scanEscapeActive[ aID ] is None and not self.scanEscapeActive[ aID ]==i:
							self.scanEscapeActive[ aID ]=None
						if len( self.action[ aID ]['escape'] ):
							if self.action[ aID ]['escape'][ self.scanID[ aIDxx ] ]==char:
								self.scanID[ aIDxx ] +=1
							else:
								self.scanID[ aIDxx ]=0
							if self.scanID[ aIDxx ]==len(self.action[ aID ]['escape']):
								self.scanEscapeActive[ aID ]=i+1
								factor=True
								self.scanID[ aIDxx ]=0
						if self.scanEscapeActive[ aID ] is None or not self.scanEscapeActive[ aID ]==i:
							if self.action[ aID ]['close']['label'] is None:
								if self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ]==char:
									self.scanID[ str(aID)+'open' ] +=1
								else:
									self.scanID[ str(aID)+'open' ]=0
									if False and aID==1:
										cp( '00 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
								
								if self.scanID[ str(aID)+'open' ]==len(self.action[ aID ]['open']['label']):
									self.scanID[ str(aID)+'open' ]=0
									factor=True
									if False and aID==1:
										cp( '01 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
									if not nestable['status'] or(not nestable['close'] is None and nestable['close']==self.action[ aID ]['open']['label'] and nestable['close']==char):
										
	
	
										if not self.scanIsOpen[ aID ] and not nestable['status']:
											if not self.action[ aID ]['nestable']:
												nestable['status']=True
												nestAudit['id']+=1
												nestable['close']=self.action[ aID ]['open']['label']
											self.theNestID[ aID ] +=1
											saved=True
											if self.theNestID[ aID ] > 1:
												cp( 'error', 'red' )
											nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=True
											self.scanIsOpen[ aID ]=True
											if not isSimple:
												try:
													
													
													
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 0 )
												except Exception as e:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=[]
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 1 )
											self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=i
										
										elif self.scanIsOpen[ aID ]:
											self.identity['location']['close'][ i ]=self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
											self.identity['location']['open'][  self.identity['location']['close'][ i ]  ]=i
											self.identity['identity'][  self.identity['location']['close'][ i ] ]=genLabel(aID)
											if not isSimple:
												if not self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ][0]['start']==i-len(self.action[ aID ]['open']['label'])+1:
													nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=False
													saved=True
													nestable['status']=False
													nestable['close']=None
													self.scanIsOpen[ aID ]=False
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 2 )
													self.theNestID[ aID ] -=1
							else:
	
								if not nestable['status']:
									if False and i==5:
										sys.exit()
									if False and aID==1:
										_printME_( '\t', i, aID, self.scanID[ str(aID)+'open' ], self.action[ aID ]['open']['label'] )
									if self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ]==char:
										self.scanID[ str(aID)+'open' ] +=1
										if False and aID==1:
											_printME_( i, aID, 'Found:', self.action[ aID ]['open']['label'], self.scanID[ str(aID)+'open' ], self.asset[i+1] )
									else:
										if False and aID==1:
											_printME_( i, aID, 'Not Found:', self.action[ aID ]['open']['label'], self.scanID[ str(aID)+'open' ], self.asset[i], self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ]-1 ],self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] )
											_printME_(  self.asset[i], self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] )
											_printME_(  "'"+self.asset[i]+"'", "'"+self.action[ aID ]['open']['label'][ self.scanID[ str(aID)+'open' ] ] +"'" )
										self.scanID[ str(aID)+'open' ]=0
										if False and aID==1:
											cp( '02 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
									if self.scanID[ str(aID)+'open' ]==len(self.action[ aID ]['open']['label']):
										self.scanID[ str(aID)+'open' ]=0
										factor=True
										if False and aID==1:
											cp( '03 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
										if not nestable['status'] :
											self.theNestID[ aID ] +=1
											self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=i
											saved=True
											nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=True
											if not self.action[ aID ]['nestable']:
												nestable['status']=True
												nestAudit['id']+=1
												nestable['close']=self.action[ aID ]['open']['label']
											self.identity['location']['close'][ i ]=self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
											self.identity['location']['open'][  self.identity['location']['close'][ i ]  ]=i
											self.identity['identity'][  self.identity['location']['close'][ i ] ]=genLabel(aID)
											if not isSimple:
												try:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 3 )
												except Exception as e:
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=[]
													self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['open']['label'] , 'start': i-len(self.action[ aID ]['open']['label'])+1, 'end': i, 'id': i, 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 4 )
											
											if not self.action[ aID ]['nestable']:
												nestable['status']=True
												nestAudit['id']+=1
												nestable['close']=self.action[ aID ]['close']['label']
									pass
	
								pass
								if '\n'==self.action[ aID ]['close']['label'] :
									if char==self.action[ aID ]['close']['label']:
										if not nestable['status'] or(not nestable['close'] is None and nestable['close']==self.action[ aID ]['close']['label']):
											try:
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ]-1 ) ]
											except Exception as e:
												isClose=False
												
											else:
												if nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ]-1 ) ]:
													isClose=True
												else:
													isClose=False
											if isClose or True:
												
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=False
												try:
													if not isSimple:
														self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['close']['label'] , 'start': i-len(self.action[ aID ]['close']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													savedIn.append( 5 )
													self.identity['location']['close'][ i ]=self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
													self.identity['location']['open'][  self.identity['location']['close'][ i ] ]=i
													self.identity['identity'][  self.identity['location']['close'][ i ] ]=genLabel(aID)
												except Exception as e:
													pass
												else:
													saved=True
													self.theNestID[ aID ] -=1
													nestable['status']=False
													nestable['close']=None
								else:
									if self.action[ aID ]['close']['label'][ self.scanID[ str(aID)+'close' ] ]==char:
										
										self.scanID[ str(aID)+'close' ] +=1
									else:
										self.scanID[ str(aID)+'close' ]=0
										if False and aID==1:
											cp( '04 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
									if self.scanID[ str(aID)+'close' ]==len(self.action[ aID ]['close']['label']):
										self.scanID[ str(aID)+'close' ]=0
										factor=True
										if False and aID==1:
											cp( '05 ' +str(i)+ self.action[ aID ]['open']['label'], 'green' )
										if not nestable['status'] or(not nestable['close'] is None and nestable['close']==self.action[ aID ]['close']['label']):
											try:
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]
											except Exception as e:
												isClose=False
												
											else:
												if nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]:
													isClose=True
												else:
													isClose=False
												nestTickets[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=False
												try:
													if not isSimple:
														if not self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ][0]['start']==i-len(self.action[ aID ]['close']['label'])+1:
															self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ].append({ 'label': self.action[ aID ]['close']['label'] , 'start': i-len(self.action[ aID ]['close']['label'])+1, 'end': i, 'id': self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ], 'n': self.theNestID[ aID ], 'line': self.getLine(i) })
													self.identity['location']['close'][ i ]=self.tableID[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]-len(self.action[ aID ]['open']['label'])+1
													self.identity['location']['open'][  self.identity['location']['close'][ i ] ]=i
													self.identity['identity'][  self.identity['location']['close'][ i ] ]=genLabel(aID)
												except Exception as e:
													pass
												else:
													savedIn.append( 6 )
													saved=True
													self.theNestID[ aID ] -=1
													nestable['status']=False
													nestable['close']=None
										else:
											pass
						pass
						if not nestable['status']:
							for key in self.flat.keys():
								if key==char:
									self.flat[key].append( i )
						pass
						if not nestable['status']:
							for iiChar in self.individualIndexes:
								if char==self.indexes['char'][iiChar]['label']:
									self.indexes['char'][iiChar]['total']+=1
									self.indexes['char'][iiChar]['index'].append( i )
									self.indexes['char'][iiChar]['line'].append( self.getLine(i) )
					pass
					if self.theNestID[ aID ]:
						allClosed=False
					
					aID +=1
				pass
				if not nestable['status']:
					pass
					if not char in identification['all'] and identification['active']:
						
						thisLabel=identification['label'][  identification['id']  ]
						txx=i-1-identification['start']
						if txx==4 or txx==3:
							sample=self.assetSnipet( identification['start'], i-1 )
							
							if sample=='true' or sample=='True' or sample=='false' or sample=='False' or sample=='TRUE' or sample=='FALSE':
								thisLabel='bool'
						
						
						
						
						self.identity['location']['close'][ i-1 ]=identification['start']
						self.identity['location']['open'][  self.identity['location']['close'][ i-1 ] ]=i-1
						self.identity['identity'][  self.identity['location']['close'][ i-1 ] ]=thisLabel
						identification['active']=False
						identification['id']=None
						identification['start']=None
					
					elif char in identification['all'] and not identification['active']:
						if not char in identification['notFirst']:
							identification['start']=i
							identification['id']=0
							identification['active']=True
							
							while not char in identification['scan'][  identification['id']  ]:
								identification['id']+=1
					elif char in identification['all'] and identification['active']:
						while not char in identification['scan'][  identification['id']  ]:
							identification['id']+=1
					
					
					
					pass
				pass
					
			pass
			if allClosed:
				self.allClosed.append( i )
		
		
		if not isSimple:
			self.dataRestructure()
		self.duration=time.time()-startTime
	def buildIndexes_Process_B( self ):
		
		identification={
							'all': '-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							'notFirst': '-:',
							'scan': [
											'0123456789',
											'.0123456789',
											'abcdefghijklmnopqrstuvwxyz',
											'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							],
							'label': [
											'number',
											'float',
											'alphaLower',
											'alphaUpper',
											'alpha',
											'alphaNumeric',
							],
							'id': None,
							'active': False,
							'start': None,
							'max': None,
		}
		
		identification['max']=len( identification['scan'] )-1
		if not self.addString is None:
			if type(self.addString)==list:
				for addString in self.addString:
					if len(addString)==2:
						identification['scan'].append(identification['scan'][5]+addString[1])
						identification['label'].append(addString[0])
		all_alpha_text=[]
		for xYz in identification['scan']:
			for xYz_char in xYz:
				if not xYz_char in all_alpha_text:
					all_alpha_text.append(xYz_char)
		identification['all']=''.join(all_alpha_text)
		
		
		
		
		
		
		
		
		
		
		
		
		def genLabel( aID ):
			
			
			tempLabel='_'.join(  self.action[ aID ]['tags']  )
			return tempLabel
			tempLabel=self.action[ aID ]['open']['label']
			if not self.action[ aID ]['close']['label'] is None:
				tempLabel+=self.stringDelim+self.action[ aID ]['close']['label']
			return tempLabel
		
		
		self.characters_max_length=0
		action_count_temp={}
		self.action_index={}
		for aID in self.action:
			self.action[aID]['open']['not']=None
			self.action[aID]['close']['not']=None
		for aID in self.action:
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ]={}
				action_count_temp[  o[0]  ]={ 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }
			if not c is None:
				self.action_index[  c[0]  ]={}
				action_count_temp[  c[0]  ]={ 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				if len(o) > self.characters_max_length:
					self.characters_max_length=len(o)
				self.action_index[  o[0]  ][ len(o) ]={}
			if not c is None:
				if len(c) > self.characters_max_length:
					self.characters_max_length=len(c)
				self.action_index[  c[0]  ][ len(c) ]={}
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ][ len(o) ][ o ]=i
			if not c is None:
				self.action_index[  c[0]  ][ len(c) ][ c ]=i
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				action_count_temp[  o[0]  ]['cnt']+=1
				if len(o) > action_count_temp[  o[0]  ]['max']:
					action_count_temp[  o[0]  ]['max']=len(o)
				action_count_temp[  o[0]  ]['chars']['start'][o]={}
			if not c is None:
				action_count_temp[  c[0]  ]['cnt']+=1
				if len(c) > action_count_temp[  c[0]  ]['max']:
					action_count_temp[  c[0]  ]['max']=len(c)
				action_count_temp[  c[0]  ]['chars']['start'][c]={}
		self.action_multi={ 'cnt': {}, 'max': {} }
		for x in action_count_temp:
			if action_count_temp[x]['max'] > 1:
				self.action_multi['max'][x]=action_count_temp[x]
			if action_count_temp[x]['cnt'] > 1:
				self.action_multi['cnt'][x]=action_count_temp[x]
		
		
		
		
		
		
		
		
		
		
		
		
						
		
		
		
		
		
		
		
		
		
		
		for i,aID in enumerate(self.action):
			for ix,aIDx in enumerate(self.action):
				if not aID==aIDx:
					if self.action[aID]['open']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['open']['label']
						b=self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg']={}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)]={}
							self.action[aID]['open']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end']={}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)]={}
							self.action[aID]['open']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid']={}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)]={}
							self.action[aID]['open']['not']['mid'][len(b)][b]={}
					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['close']['label']
						b=self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg']={}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)]={}
							self.action[aID]['close']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end']={}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)]={}
							self.action[aID]['close']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid']={}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)]={}
							self.action[aID]['close']['not']['mid'][len(b)][b]={}
		
					if not self.action[aID]['open']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['open']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['open']['label']
						b=self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg']={}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)]={}
							self.action[aID]['open']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end']={}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)]={}
							self.action[aID]['open']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid']={}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)]={}
							self.action[aID]['open']['not']['mid'][len(b)][b]={}
					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['open']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['close']['label']
						b=self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg']={}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)]={}
							self.action[aID]['close']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end']={}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)]={}
							self.action[aID]['close']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid']={}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)]={}
							self.action[aID]['close']['not']['mid'][len(b)][b]={}
		def d4_peek( ix, length ):
			txt=''
			while not len(txt)==length:
				try:
					txt +=self.asset[ix]
				except Exception as e:
					txt +=' '
				ix+=1
			return txt
		def d4_peek( ix, length ):
			txt=''
			while not len(txt)==length:
				try:
					txt +=self.asset[ix]
				except Exception as e:
					txt +=' '
				ix+=1
			return txt
		def d4_peekB( ix, length, char ):
			txt=[]
			for x in char:
				txt.append(x)
			txt.reverse()
			ix-=1
			while not len(txt)==length:
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix-=1
			txt.reverse()
			return ''.join(txt)
		def d8_peek_in(  ix, char, charX, sject  ):
			
			x=charX.index(char)
			txt=[]
			yx=0
			bix=ix
			while not yx==x:
				yx+=1
				try:
					txt.append( self.asset[ bix-yx ] )
				except Exception as e:
					txt.append( ' ' )
				
			txt.reverse()
			yy=x+len(char)-1
			xy=len(charX)-1
			for y in char:
				ix+=1
				txt.append(y)
			while not len(txt) >=len(charX):
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix+=1
			return ''.join(txt)
		def escapeIsActive(i,escape):
			txt=''
			bix=i-1
			while self.asset[bix]==escape:
				txt+=self.asset[bix]
				bix-=1
			if len(txt) % 2==0:
				return False
			else:
				return True
		def d20( i, char  ):
			aID=None
			if char in self.action_index:
				
				ai=self.action_index[char]
				if len( ai )==1 and 1 in ai:
					aID=ai[1][char]
				else:
					mx=self.characters_max_length
					while mx > 0 and aID is None:
						if aID is None:
							if mx in ai:
								char=d4_peek( i, mx )
								if char in ai[mx]:
									aID=ai[mx][char]
									checkValid=True
									
									for item in ['open']:
										runTHIS=True
										
										
										
										if runTHIS:
											if not self.action[aID][item]['label'] is None:
												if self.action[aID][item]['label']==char:
													if not self.action[aID][item]['not'] is None:
														for sject in self.action[aID][item]['not']:
															if not self.action[aID][item]['not'][sject] is None:
																
																mxNOT=self.characters_max_length
																while mxNOT > 0:
																	if mxNOT in self.action[aID][item]['not'][sject]:
																		
																		if sject=='beg':
																			if d4_peek( i, mxNOT ) in self.action[aID][item]['not'][sject][mxNOT]:
																				checkValid=False
																			if d4_peekB( i, mxNOT, char ) in self.action[aID][item]['not'][sject][mxNOT]:
																				checkValid=False
																		elif sject=='end':
																			charX=d4_peekB( i, mxNOT, char )
																			if charX in self.action[aID][item]['not'][sject][mxNOT]:
																				checkValid=False
																		elif sject=='mid':
																			for charX in self.action[aID][item]['not'][sject][mxNOT]:
																				if not d8_peek_in( i, char, charX, sject ):
																					checkValid=False
																	mxNOT-=1
									
									if checkValid:
										break
									else:
										if not self.nestable['status']:
											aID=None
										else:
											break
						mx-=1
			
			if not aID is None:
				if not self.nestable['status']:
					isValid=True
				elif self.nestable['close']==aID:
					
					
					
					
					isValid=True
				else:
					isValid=False
				if isValid:
					if 'regex' in self.action[aID]['tags']:
						if not self.nestable['status']:
							the_last_char=[
										'(',
										'=',
										':',
										'[',
									]
							if not self.the_last_char in the_last_char:
								isValid=False
				if isValid:
						escape=self.action[aID]['escape']
						if escape:
							if not i==0:
								if self.asset[i-1]==escape:
									if escapeIsActive(i,escape):
										isValid=False
						
				
				
				if isValid:
					if self.nestable['close']==aID or char==self.action[aID]['close']['label']:
						if self.theNestID[ aID ] > 0:
							end=i
							start=self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]
							self.identity['location']['close'][ end ]=start
							self.identity['location']['open'][  start ]=end
							self.identity['identity'][  start ]=genLabel(aID)
							self.identity['location']['action'][  start ]=aID
							startLen=len( self.action[aID]['open']['label'] )
							
							if not startLen==1:
							
							
								ocI=start+1
								ocEnd=ocI + startLen - 1
								ran=False
								while not ocI==ocEnd:
									ran=True
									self.identity['oc'].append( ocI )
									ocI+=1
								
							if not self.action[aID]['close']['label'] is None:
								endLen=len( self.action[aID]['close']['label'] )
								if endLen==1:
									self.identity['oc'].append( i )
								else:
									ocI=i
									ocEnd=ocI + endLen 
									while not ocI==ocEnd:
										self.identity['oc'].append( ocI )
										ocI+=1
							self.theNestID[ aID ]-=1
							self.nestable['close']=None
							self.nestable['status']=False
					else:
						self.theNestID[ aID ]+=1
						self.table[ str(aID) +'X'+ str( self.theNestID[ aID ] ) ]=i
						if not self.action[aID]['nestable']:
							self.nestable['close']=aID
							self.nestable['status']=True
						
						
						
		
		
		
		
		
		
		self.nestable={
							'status': False,
							'close': None,
		}
		
		startTime=time.time()
		self.the_last_char=''
		for i,char in enumerate(self.asset):
			x=d20( i, char )
				
			if not self.nestable['status']:
				if not char==' ' and not char=='\t' and not char=='\n':
					self.the_last_char=char
				pass
				if not char in identification['all'] and identification['active']:
					
					thisLabel=identification['label'][  identification['id']  ]
					txx=i-1-identification['start']
					if txx==4 or txx==3:
						sample=self.assetSnipet( identification['start'], i-1 )
						
						if sample=='true' or sample=='True' or sample=='false' or sample=='False' or sample=='TRUE' or sample=='FALSE':
							thisLabel='bool'
					
					
					
					
					self.identity['location']['close'][ i-1 ]=identification['start']
					self.identity['location']['open'][  self.identity['location']['close'][ i-1 ] ]=i-1
					self.identity['identity'][  self.identity['location']['close'][ i-1 ] ]=thisLabel
					identification['active']=False
					identification['id']=None
					identification['start']=None
				
				elif char in identification['all'] and not identification['active']:
					if not char in identification['notFirst']:
						identification['start']=i
						identification['id']=0
						identification['active']=True
						
						while not char in identification['scan'][  identification['id']  ]:
							identification['id']+=1
				elif char in identification['all'] and identification['active']:
					while not char in identification['scan'][  identification['id']  ]:
						identification['id']+=1
				
				
				
				pass
			pass
		
		self.duration=time.time()-startTime
		errors=[]
		for x in self.theNestID:
			if self.theNestID[x] > 0:
				yyy=self.table[ str(x) +'X'+ str( self.theNestID[ x ] ) ]
				
				errors.append( yyy )
		
		if errors:
			_printME_()
			_printME_()
			_printME_()
			cp( [  'CODE NOT VALID:'  ] )
			cp( [  '\tfound', len(errors), 'errors'  ], 'yellow' )
			for x in errors:
				y={  'char': self.asset[x], 'line': self.getLine(x) }
				nothing( [  '\t\t\t', y  ], 'yellow' )
			_printME_()
			_printME_()
			_printME_()
			return None
			sys.exit()
		
		del self.nestable
	def post_C( self ):
		self.the_validation_process()
		
	def buildIndexes_Process_C( self ):
		self.buildIndexes_Process_B()
		self.post_C()
		return None
		
		identification={
							'all': '-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							'notFirst': '-:',
							'scan': [
											'0123456789',
											'.0123456789',
											'abcdefghijklmnopqrstuvwxyz',
											'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
											'-:._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
							],
							'label': [
											'number',
											'float',
											'alphaLower',
											'alphaUpper',
											'alpha',
											'alphanumeric',
							],
							'id': None,
							'active': False,
							'start': None,
							'max': None,
		}
		self.TMP_lastSub=None
		identification['max']=len( identification['scan'] )-1
		
		
		
		
		
		
		
		
		
		
		def genLabel( aID ):
			
			
			tempLabel='_'.join(  self.action[ aID ]['tags']  )
			return tempLabel
			tempLabel=self.action[ aID ]['open']['label']
			if not self.action[ aID ]['close']['label'] is None:
				tempLabel+=self.stringDelim+self.action[ aID ]['close']['label']
			return tempLabel
		
		
		self.characters_max_length=0
		action_count_temp={}
		self.action_index={}
		for aID in self.action:
			self.action[aID]['open']['not']=None
			self.action[aID]['close']['not']=None
		for aID in self.action:
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ]={}
				action_count_temp[  o[0]  ]={ 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }
			if not c is None:
				self.action_index[  c[0]  ]={}
				action_count_temp[  c[0]  ]={ 'max': 0, 'cnt': 0, 'chars': {'start':{},'end':{},'middle':{}} }
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				if len(o) > self.characters_max_length:
					self.characters_max_length=len(o)
				self.action_index[  o[0]  ][ len(o) ]={}
			if not c is None:
				if len(c) > self.characters_max_length:
					self.characters_max_length=len(c)
				self.action_index[  c[0]  ][ len(c) ]={}
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				self.action_index[  o[0]  ][ len(o) ][ o ]=i
			if not c is None:
				self.action_index[  c[0]  ][ len(c) ][ c ]=i
		for i,aID in enumerate(self.action):
			o=self.action[aID]['open']['label']
			c=self.action[aID]['close']['label']
			if not o is None:
				action_count_temp[  o[0]  ]['cnt']+=1
				if len(o) > action_count_temp[  o[0]  ]['max']:
					action_count_temp[  o[0]  ]['max']=len(o)
				action_count_temp[  o[0]  ]['chars']['start'][o]={}
			if not c is None:
				action_count_temp[  c[0]  ]['cnt']+=1
				if len(c) > action_count_temp[  c[0]  ]['max']:
					action_count_temp[  c[0]  ]['max']=len(c)
				action_count_temp[  c[0]  ]['chars']['start'][c]={}
		self.action_multi={ 'cnt': {}, 'max': {} }
		for x in action_count_temp:
			if action_count_temp[x]['max'] > 1:
				self.action_multi['max'][x]=action_count_temp[x]
			if action_count_temp[x]['cnt'] > 1:
				self.action_multi['cnt'][x]=action_count_temp[x]
		
		
		
		
		
		
		
		
		
		
		
		
						
		
		
		
		
		
		
		
		
		
		
		for i,aID in enumerate(self.action):
			for ix,aIDx in enumerate(self.action):
				if not aID==aIDx:
					if self.action[aID]['open']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['open']['label']
						b=self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg']={}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)]={}
							self.action[aID]['open']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end']={}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)]={}
							self.action[aID]['open']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid']={}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)]={}
							self.action[aID]['open']['not']['mid'][len(b)][b]={}
					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['close']['label']
						b=self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg']={}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)]={}
							self.action[aID]['close']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end']={}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)]={}
							self.action[aID]['close']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid']={}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)]={}
							self.action[aID]['close']['not']['mid'][len(b)][b]={}
		
					if not self.action[aID]['open']['label'] is None and not self.action[aIDx]['close']['label'] is None and self.action[aID]['open']['label'] in self.action[aIDx]['close']['label']:
						if self.action[aID]['open']['not'] is None:
							self.action[aID]['open']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['open']['label']
						b=self.action[aIDx]['close']['label']
						if b.startswith( a ):
							if self.action[aID]['open']['not']['beg'] is None:
								self.action[aID]['open']['not']['beg']={}
							if not len(b) in self.action[aID]['open']['not']['beg']:
								self.action[aID]['open']['not']['beg'][len(b)]={}
							self.action[aID]['open']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['open']['not']['end'] is None:
								self.action[aID]['open']['not']['end']={}
							if not len(b) in self.action[aID]['open']['not']['end']:
								self.action[aID]['open']['not']['end'][len(b)]={}
							self.action[aID]['open']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['open']['not']['mid'] is None:
								self.action[aID]['open']['not']['mid']={}
							if not len(b) in self.action[aID]['open']['not']['mid']:
								self.action[aID]['open']['not']['mid'][len(b)]={}
							self.action[aID]['open']['not']['mid'][len(b)][b]={}
					if not self.action[aID]['close']['label'] is None and not self.action[aIDx]['open']['label'] is None and self.action[aID]['close']['label'] in self.action[aIDx]['open']['label']:
						if self.action[aID]['close']['not'] is None:
							self.action[aID]['close']['not']={'beg':None,'end':None,'mid':None }
						a=self.action[aID]['close']['label']
						b=self.action[aIDx]['open']['label']
						if b.startswith( a ):
							if self.action[aID]['close']['not']['beg'] is None:
								self.action[aID]['close']['not']['beg']={}
							if not len(b) in self.action[aID]['close']['not']['beg']:
								self.action[aID]['close']['not']['beg'][len(b)]={}
							self.action[aID]['close']['not']['beg'][len(b)][b]={}
						elif b.endswith( a ):
							if self.action[aID]['close']['not']['end'] is None:
								self.action[aID]['close']['not']['end']={}
							if not len(b) in self.action[aID]['close']['not']['end']:
								self.action[aID]['close']['not']['end'][len(b)]={}
							self.action[aID]['close']['not']['end'][len(b)][b]={}
						else:
							if self.action[aID]['close']['not']['mid'] is None:
								self.action[aID]['close']['not']['mid']={}
							if not len(b) in self.action[aID]['close']['not']['mid']:
								self.action[aID]['close']['not']['mid'][len(b)]={}
							self.action[aID]['close']['not']['mid'][len(b)][b]={}
		def d4_peek( ix, length ):
			txt=''
			while not len(txt)==length:
				try:
					txt +=self.asset[ix]
				except Exception as e:
					txt +=' '
				ix+=1
			return txt
		def d4_peek( ix, length ):
			txt=''
			while not len(txt)==length:
				try:
					txt +=self.asset[ix]
				except Exception as e:
					txt +=' '
				ix+=1
			return txt
		def d4_peekB( ix, length, char ):
			txt=[]
			for x in char:
				txt.append(x)
			txt.reverse()
			ix-=1
			while not len(txt)==length:
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix-=1
			txt.reverse()
			return ''.join(txt)
		def d8_peek_in(  ix, char, charX, sject  ):
			
			x=charX.index(char)
			txt=[]
			yx=0
			bix=ix
			while not yx==x:
				yx+=1
				try:
					txt.append( self.asset[ bix-yx ] )
				except Exception as e:
					txt.append( ' ' )
				
			txt.reverse()
			yy=x+len(char)-1
			xy=len(charX)-1
			for y in char:
				ix+=1
				txt.append(y)
			while not len(txt) >=len(charX):
				try:
					txt.append( self.asset[ix] )
				except Exception as e:
					txt.append( ' ' )
				ix+=1
			return ''.join(txt)
		def escapeIsActive(i,escape):
			txt=''
			bix=i-1
			while self.asset[bix]==escape:
				txt+=self.asset[bix]
				bix-=1
			if len(txt) % 2==0:
				return False
			else:
				return True
		def d20( i, char  ):
			aID=None
			if char in self.action_index:
				
				ai=self.action_index[char]
				if len( ai )==1 and 1 in ai:
					aID=ai[1][char]
				else:
					mx=self.characters_max_length
					while mx > 0 and aID is None:
						if aID is None:
							if mx in ai:
								char=d4_peek( i, mx )
								if char in ai[mx]:
									aID=ai[mx][char]
									checkValid=True
									
									for item in ['open']:
										if not self.action[aID][item]['label'] is None:
											if self.action[aID][item]['label']==char:
												if not self.action[aID][item]['not'] is None:
													for sject in self.action[aID][item]['not']:
														if not self.action[aID][item]['not'][sject] is None:
															
															mxNOT=self.characters_max_length
															while mxNOT > 0:
																if mxNOT in self.action[aID][item]['not'][sject]:
																	
																	if sject=='beg':
																		if d4_peek( i, mxNOT ) in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid=False
																		if d4_peekB( i, mxNOT, char ) in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid=False
																	elif sject=='end':
																		charX=d4_peekB( i, mxNOT, char )
																		if charX in self.action[aID][item]['not'][sject][mxNOT]:
																			checkValid=False
																	elif sject=='mid':
																		for charX in self.action[aID][item]['not'][sject][mxNOT]:
																			if not d8_peek_in( i, char, charX, sject ):
																				checkValid=False
																mxNOT-=1
									
									if checkValid:
										break
									else:
										if not self.nestable['status']:
											aID=None
										else:
											break
						mx-=1
			
			if not aID is None:
				if not self.nestable['status']:
					isValid=True
				elif self.nestable['close']==aID:
					isValid=True
				else:
					isValid=False
				if isValid:
					if 'regex' in self.action[aID]['tags']:
						if not self.nestable['status']:
							the_last_char=[
										'(',
										'=',
										':',
										'[',
									]
							if not self.the_last_char in the_last_char:
								isValid=False
				if isValid:
						escape=self.action[aID]['escape']
						if escape:
							if not i==0:
								if self.asset[i-1]==escape:
									if escapeIsActive(i,escape):
										isValid=False
						
				
				
				if isValid:
					if self.nestable['close']==aID or char==self.action[aID]['close']['label']:
						if self.theNestID[ aID ] > 0:
							thisItem=str(aID) +'X'+ str( self.theNestID[ aID ] )
							theEnd=i-len(self.action[ aID ]['open']['label'])+1+len(self.action[ aID ]['open']['label'])-1
							theStart=self.table[ thisItem ]
							self.identity['location']['close'][ theEnd ]=theStart
							self.identity['location']['open'][  self.identity['location']['close'][ theEnd ] ]=theEnd
							self.identity['identity'][  self.identity['location']['close'][ theEnd ] ]=genLabel(aID)
							d10_close( char, theStart, theEnd, thisItem )
							self.theNestID[ aID ]-=1
							self.nestable['close']=None
							self.nestable['status']=False
					else:
						self.theNestID[ aID ]+=1
						thisItem=str(aID) +'X'+ str( self.theNestID[ aID ] )
						self.table[ thisItem ]=i
						if not self.action[aID]['nestable']:
							self.nestable['close']=aID
							self.nestable['status']=True
						
						d10_open( i, char, thisItem )
						
						
						
		
		
		
		
		
		
		self.relevant_OC=['(', '{','[']
		def d10_open( i, char, thisItem ):
			
			self.components['preLast'][thisItem]=self.components['last']
			self.components['last']=thisItem
			self.components['char'][thisItem]=char
			self.components['hasLabel'][thisItem]=False
			self.components['builder'][thisItem]=[]
			self.components['sub'][thisItem]=[]
			
			self.components['lastLabel'][ thisItem ]=[]
			
			
		def d10_close( char, theStart, theEnd, thisItem=None ):
			if thisItem is None:
				thisItem=self.components['last']
				if not thisItem in self.components['sub']:
					self.components['sub'][ thisItem ]=[]
				self.components['sub'][ thisItem  ].append(theStart)
				self.TMP_lastSub=theStart
			else:
				if char in '}':
					d10_softClose( thisItem )
				
				self.components['last']=self.components['preLast'][thisItem]
			
				if not self.components['last'] in self.components['sub']:
					self.components['sub'][ self.components['last'] ]=[]
				
				if self.TMP_lastSub in self.identity['location']['open']:
					lsO=self.TMP_lastSub
					lsC=self.identity['location']['open'][ lsO ]
					if theStart > lsO and theStart < lsC:
						pass
					else:
						self.components['sub'][ self.components['last']  ].append(theStart)
				self.TMP_lastSub=theStart
			
			
			
				
					
					
					
					
			
					
					
			if not self.components['char'][ thisItem ] is None and self.components['char'][ thisItem ] in '{[(' :
				self.identity['validation'][theStart]=self.components['builder'][thisItem]
				self.components['builder'][thisItem]=[]
			
		def d10_char(i,char):
			thisItemP=self.components['preLast'][self.components['last']]
			thisItem=self.components['last']
			if self.components['char'][ thisItem ]=='{':
				if char==self.breaks['label']:
					self.components['lastLabel'][ thisItem ]=self.components['sub'][ thisItem ]
					self.components['hasLabel'][ thisItem ]=True
					self.components['sub'][ thisItem  ]=[]
				elif char==self.breaks['mini']:
					d10_softClose( thisItem )
			
		def d10_softClose( thisItem ):
			
			try:
				vbs={ 'label': self.components['lastLabel'][ thisItem ], 'values': self.components['sub'][ thisItem  ] }
			except Exception as e:
				_printME_( thisItem, self.components['char'][thisItem] )
				sys.exit()
			asdf=False
			if asdf:
				_printME_()
				_printME_(thisItem, vbs)
			for x in self.components['lastLabel'][ thisItem ]:
				if x in self.identity['location']['open']:
					txt=self.assetSnipet( x, self.identity['location']['open'][x] )
				else:
					txt=self.asset[x]
				if asdf:
					_printME_( '\t LABEL', txt )
			for x in self.components['sub'][ thisItem  ]:
				if x in self.identity['location']['open']:
					txt=self.assetSnipet( x, self.identity['location']['open'][x] )
				else:
					txt=self.asset[x]
				if asdf:
					_printME_( '\t VALUE', txt )
			self.components['sub'][ thisItem  ]=[]
			self.components['builder'][ thisItem ].append(vbs)
		self.breaks={
								'label': ':',
								'mini': ',',
								'hard': ';',
								'soft': '\n',
		}
		relevantChars=[]
		for x in self.breaks:
			relevantChars.append( self.breaks[x] )
		
		self.components={
								'parts': {},
								'sub': {},
								'builder': {},
								'group': {},
								'char': {},
								'variable': {},
								'preLast': {},
								'last': 0,
								'hasLabel': {},
								'lastLabel': {},
								'dicType': {},
		}
		self.components['sub'][0]=[]
		self.components['char'][0]=None
		self.components['preLast'][0]=0
		self.components['preLast']['None']=0
		self.components['char']['None']=''
		self.components['builder'][0]=[]
		self.nestable={
							'status': False,
							'close': None,
		}
		
		startTime=time.time()
		self.the_last_char=''
		for i,char in enumerate(self.asset):
			x=d20( i, char )
			if not char==' ' and not char=='\t' and not char=='\n':
				self.the_last_char=char
				
			if not self.nestable['status']:
				pass
				if not char in identification['all'] and identification['active']:
					
					thisLabel=identification['label'][  identification['id']  ]
					txx=i-1-identification['start']
					if txx==4 or txx==3:
						sample=self.assetSnipet( identification['start'], i-1 )
						
						
						
						if sample=='true' or sample=='True' or sample=='false' or sample=='False' or sample=='TRUE' or sample=='FALSE':
							thisLabel='bool'
					
					
					
					
					self.identity['location']['close'][ i-1 ]=identification['start']
					self.identity['location']['open'][  self.identity['location']['close'][ i-1 ] ]=i-1
					self.identity['identity'][  self.identity['location']['close'][ i-1 ] ]=thisLabel
					d10_close( char, identification['start'], i-1 )
					identification['active']=False
					identification['id']=None
					identification['start']=None
				
				elif char in identification['all'] and not identification['active']:
					if not char in identification['notFirst']:
						identification['start']=i
						identification['id']=0
						identification['active']=True
						
						while not char in identification['scan'][  identification['id']  ]:
							identification['id']+=1
				elif char in identification['all'] and identification['active']:
					while not char in identification['scan'][  identification['id']  ]:
						identification['id']+=1
				
				
				
				pass
			pass
			if not self.nestable['status']:
				if char in relevantChars:
					d10_char( i, char )
				elif not char in self.action_index and not char in identification['all'] and not char==' ' and not char=='\t' and not char=='\n':
					if not self.components['last'] in self.components['sub']:
						self.components['sub'][ self.components['last']  ]=[]
					
					self.components['sub'][ self.components['last']  ].append(i)
					self.TMP_lastSub=i
			
		
		self.duration=time.time()-startTime
		errors=[]
		for x in self.theNestID:
			if self.theNestID[x] > 0:
				yyy=self.table[ str(x) +'X'+ str( self.theNestID[ x ] ) ]
				
				errors.append( yyy )
		
		if errors:
			_printME_()
			_printME_()
			_printME_()
			cp( [  'FILE NOT VALID:'  ] )
			cp( [  '\tfound', len(errors), 'errors'  ], 'yellow' )
			for x in errors:
				y={  'char': self.asset[x], 'line': self.getLine(x) }
				nothing( [  '\t\t\t', y  ], 'yellow' )
			_printME_()
			_printME_()
			_printME_()
			return None
			sys.exit()
		
		del self.nestable
	def getLabel( self, subject, string=False ):
		try:
			self.stringDelim
		except Exception as e:
			self.stringDelim='-B248-'
		if type(subject)==str:
			r=subject.split(self.stringDelim)
			if string:
				return ''.join(r)
			return r
		elif type(subject)==int:
			return self.getLabel(  self.identity['identity'][subject], string  )
	def preValidate( self, start=None, end=None ):
		special={
						'\n': { 'tags': ['close'] },
						';': { 'tags': ['close'] },
						'=': { 'tags': ['eq'] },
						',': { 'tags': ['delimiter'] },
						'-': { 'tags': ['math'] },
						'+': { 'tags': ['math','add'] },
						'/': { 'tags': ['math'] },
						'*': { 'tags': ['math'] },
		}
		whitespace=[ ' ', '\t', '\n' ]
		if start is None:
			i=-1
		else:
			i=start
		if end is None:
			end=len(self.asset)
		end-=1
		done=False
		result=[]
		last=None
		lastSet=[]
		var=None
		isEqual=False
		label=None
		delimiters=0
		variables={}
		while not  done:
			i+=1
			if i==end:
				done=True
			if not done:
				try:
					char=self.asset[i]
				except Exception as e:
					done=True
			if not done:
				
				if not i in self.identity['identity'] and not i in self.identity['oc']:
					
					if char in special:
						
						
						if 'close' in special[char]['tags']:
							if not label is None:
								y=[]
								for x in lastSet:
									y.append(str(x))
								variables[ ','.join(y) ]=lastSet
								result.append( { 'label': label, 'values': lastSet } )
							elif len(lastSet):
								result.append( lastSet )
							lastSet=[]
							label=None
						elif 'eq' in special[char]['tags']:
							
							
							label=lastSet
							
							lastSet=[]
						else:
							lastSet.append( i )
					elif char in whitespace:
						pass
					else:
						lastSet.append(i)
				elif not i in self.identity['oc']:
					o=i
					c=self.identity['location']['open'][o]
					lastSet.append(i)
					i=c
		if len(lastSet):
			if not label is None:
				result.append( { 'label': label, 'values': lastSet } )
				label=None
			else:
				result.append(lastSet)
		return result
	def the_validation_process_variables_dic( self, o, parents=[] ):
		c=self.identity['location']['open'][o]
		txt=self.assetSnipet( o, c )
		
		
		test=self.validateDic(o,c)
		_printME_( 'validateDic:', test )
		for rec in test:
			
			
			
			
			
			
			
			
			
			self.the_validation_process_items( rec[0], parents, prefix='\t', color='yellow' )
			
			self.the_validation_process_items( rec[1], parents+[rec[0]], prefix='\t\t', color='green' )
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
	def the_validation_process_items( self, values, parents=[], prefix=None, color=None ):
		if type(values)==int:
			values=[values]
		for o in values:
			self.the_validation_process_item( o, parents, prefix, color )
	def the_validation_process_item( self, o, parents=[], prefix=None, color=None ):
		if self.asset[o]=='{': 
			done=False
			oi=o+1
			what={  'fn': None, 'dic': None  }
			while not done:
				if oi==self.identity['location']['open'][o]:
					done=True
				if oi > len(self.asset)-1:
					done=True
				if not done:
					
					if self.asset[oi]==':':
						done=True
						what['dic']=True
					if oi in self.identity['location']['open']:
						oi=self.identity['location']['open'][oi]
					oi+=1
			if what['dic'] is None:
				what['fn']=True
				what['dic']=False
			if what['dic']:
				self.identity['dicType'][o]='dic'
				
				self.the_validation_process_variables_dic( o, parents=parents )
			else:
				self.identity['dicType'][o]='fn'
			cp( self.identity['dicType'][o] )
		elif self.asset[o]=='(': 
			_printME_( '(' )
		elif self.asset[o]=='[': 
			_printME_( '[' )
		else:
			closeLen=''
			if type(o)==int:
				if o in self.identity['location']['open']:
					c=self.identity['location']['open'][o]
					l=self.identity['identity'][o]
					if True:
						try:
							aID=self.identity['location']['action'][o]
							closeLen=len(self.action[aID]['close']['label'])
							c=c-1+closeLen
							if self.action[aID]['close']['label']=='\n':
								c -=1
						except Exception as e:
							pass
					
					
					
					txt=self.assetSnipet( o, c )
				else:
					l=''
					txt=self.asset[o]
				prefix=''
				pix=0
				while not pix==len(parents):
					pix+=1
					prefix+='\t'
				if not prefix is None and not color is None:
					_printME_( prefix, o, cp( txt, color, p=0 ), l, closeLen )
				else:
					_printME_( o, cp( txt, 'yellow', p=0 ), l, closeLen )
			else:
				_printME_( type(i) )
				_printME_( str(i) )
	def the_validation_process( self, start=None, end=None ):
		result=self.preValidate()
		
		_printME_(  )
		_printME_( '____' )
		_printME_(  )
		for group in result:
			_printME_(  )
			if type(group)==dict:
				_printME_( group )
				
				self.the_validation_process_items( group['values'], group['label'] )
			elif type(group)==list:
				self.the_validation_process_items( group )
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	def validateDic( self, oo, cc ):
		field=':'
		each=','
		i=oo
		done=False
		result=[]
		lastField=None
		lastValue=[]
		pastField=False
		
		
		while not  done:
			if i==cc: done=True;
			i+=1
			if i==cc: done=True;
			
			
			if not done:
				try:
					char=self.asset[i]
				except Exception as e:
					done=True
			if not done:
				
				if not i in self.identity['identity'] and not i in self.identity['oc']:
				
					
					if char==field and pastField:
						cp( 'Error' )
					if char==field:
						pastField=True
					elif char==each:
						result.append( [lastField, lastValue] )
						lastField=None
						lastValue=[]
						pastField=False
					elif char==' ' or char=='\t' or char=='\n':
						pass
					else:
						lastValue.append(i)
				elif not i in self.identity['oc']:
					if lastField is None:
						lastField=i
					elif pastField:
						lastValue.append(i)
					else:
						cp( 'Error' )
					
					
					o=i
					try:
						c=self.identity['location']['open'][i]
					except Exception as e:
						_printME_( 'Error:', self.asset[i] )
					i=c
					
					
		if len(lastValue):
			result.append( [lastField, lastValue] )
		
		return result
	def dataRestructure( self ):
		self.indexes['allClosed']=self.allClosed
		self.indexes['carriageIndex']=self.carriageIndex
		actionIndex={}
		loopLen=len( self.action.keys() ) 
		aID=0
		while not aID==( loopLen ):
			actionIndex[ self.action[ aID ]['open']['label'] ]=aID
			
			if not self.action[ aID ]['close']['label'] is None:
				actionIndex[ self.action[ aID ]['close']['label'] ]=aID
			aID+=1
		
		for key in self.flat.keys():
			charIndexes={
							'total': len(self.flat[key]),
							'index': self.flat[key],
							'start': self.flat[key],
							'end': 1,
							'line': [],
							'label': key
			}
			for i in self.flat[key]:
				charIndexes['line'].append( self.getLine(i) )
			self.indexes['char'].append( charIndexes )
		cleanKeys={}
		for key in self.table.keys():
			for x in self.table[ key ]:
				try:
					cleanKeys[x['id']].append( x )
				except Exception as e:
					cleanKeys[x['id']]=[]
					cleanKeys[x['id']].append( x )
				
				
		pass
		for key in cleanKeys.keys():
			if not len( cleanKeys[key] )==2:
				cp( 'Validation Fail: ' + str(cleanKeys[key]), 'red' )
				sys.exit()
		
		
		omit=[
					'[',
					"'",
					'(',
					'//',
					'"',
					'{',
				]
		
		
		
		
		
		
		
		
		self.noIndex=[]
		self.genitemLabelIndexes()
		
		
		for i,key in enumerate(cleanKeys.keys()):
			if True:
			
				theChar=cleanKeys[key][0]['label']
				char0ID=self.itemLabel( cleanKeys[key][0]['label'], 'char' )
				char1ID=self.itemLabel( cleanKeys[key][1]['label'], 'char' )
				groupID=self.itemLabel( cleanKeys[key][0]['label']+cleanKeys[key][1]['label'], 'group' )
				if groupID is None:
					groupID=self.itemLabel( cleanKeys[key][0]['label'], 'group' )
				if char0ID is None:
					printVar( cleanKeys[key] )
					cp( 'Error: char0ID is None', 'red' )
				if char1ID is None:
					printVar( cleanKeys[key] )
					cp( 'Error: char1ID is None', 'red' )
				if groupID is None:
					printVar( cleanKeys[key] )
					cp( 'Error: groupID is None', 'red' )
				
				
				
				start=cleanKeys[key][0]['start']
				xLen=1
				try:
					xLen=len( cleanKeys[key][0]['label'] )
				except Exception as e:
					pass
				end=cleanKeys[key][0]['start'] + xLen
				
				xPos=[]
				x=start
				if start==end:
					xPos.append( start )
				else:
					while not x==end:
						xPos.append( x )
						x+=1
				aStart=start
				aEnd=end
				aLen=xLen
				aPos=xPos
				
				
				start=cleanKeys[key][1]['start']
				xLen=1
				try:
					xLen=len( cleanKeys[key][1]['label'] )
				except Exception as e:
					pass
				end=cleanKeys[key][1]['start'] + xLen
				
				xPos=[]
				x=start
				if start==end:
					xPos.append( start )
				else:
					while not x==end:
						xPos.append( x )
						x+=1
				bStart=start
				bEnd=end
				bLen=xLen
				bPos=xPos
				
				outer=[]
				inner=[]
				x=aStart
				while not x==bEnd:
					outer.append( x )
					x+=1
				
				x=aEnd
				
				if x < bStart:
					while not x==bStart:
						inner.append( x )
						x+=1
				
				
				pass
				
				
				
				self.indexes['char'][char0ID]['total']+=1
				self.indexes['char'][char0ID]['line'].append( cleanKeys[key][0]['line'] )
				self.indexes['char'][char0ID]['end']=aLen
				self.indexes['char'][char0ID]['start'].append( aStart )
				for x in aPos:
					self.indexes['char'][char0ID]['index'].append( x )
				
				self.indexes['char'][char1ID]['total']+=1
				self.indexes['char'][char1ID]['line'].append( cleanKeys[key][1]['line'] )
				self.indexes['char'][char1ID]['end']=bLen
				self.indexes['char'][char1ID]['start'].append( bStart )
				
				for x in bPos:
					self.indexes['char'][char1ID]['index'].append( x )
				
				self.indexes['group'][groupID]['total']+=1
				self.indexes['group'][groupID]['oc'].append({ 'open': aStart, 'close': bStart })
				for x in inner:
					self.indexes['group'][groupID]['inner'].append( x )
				try:
					for x in outer:
						self.indexes['group'][groupID]['index'].append( x )
				except Exception as e:
					_printME_( outer, self.indexes['group'][groupID]['index'] )
				
				pass
				
				
					
				
		
		pass
		self.indexes['totals']={}
		self.indexes['totals']['total']=len( cleanKeys.keys() )
		self.indexes['totals']['group']={}
		self.indexes['totals']['char']={}
		for record in self.indexes['group']:
			self.indexes['totals']['group'][ record['label'] ]=record['total']
		for record in self.indexes['char']:
			self.indexes['totals']['char'][ record['label'] ]=record['total']
		pass
		self.indexes['language']=self.language
		self.genitemLabelIndexes()
		
	def genitemLabelIndexes( self ):
		self.indexes['IDs']={}
		self.indexes['IDs']['char']={}
		self.indexes['IDs']['group']={}
		
		for i,record in enumerate(self.indexes['char']):
			self.indexes['IDs']['char'][ self.genLabel( i, 'char' ) ]=i
		for i,record in enumerate(self.indexes['group']):
			self.indexes['group'][i]['open']['iID']=self.itemLabel( self.indexes['group'][i]['open']['label'], 'char' )
			self.indexes['IDs']['group'][ self.genLabel( i, 'group' ) ]=i
			
			openID=self.genLabel( i, 'group', 'open' )
			if not openID is None:
				self.indexes['IDs']['group'][ openID ]=i
			closeID=self.genLabel( i, 'group', 'close' )
			if not closeID is None:
				self.indexes['IDs']['group'][ closeID ]=i
				self.indexes['group'][i]['close']['iID']=self.itemLabel( self.indexes['group'][i]['close']['label'], 'char' )
	def testIndexs( self ):
		
		
		
		for record in self.indexes['char']:
			_printME_()
			_printME_()
			cp( record['label'] )
			cp( len(record['index']), 'green' )
			chars=[]
			for x in record['index']:
				chars.append( self.asset[x] )
			cp( ''.join(chars), 'cyan' )
	def buildValidationActionQueue( self, xID ):
		self.action[ self.action_queue ]=self.logistics['action'][xID]
		for i,record in enumerate(self.action[ self.action_queue ]['test']):
			if record['type']=='text' and record['strict']==1:
				self.action[ self.action_queue ]['test'][i]['data']=record['data'].lower()
		self.action[ self.action_queue ]['active']=True
		self.action[ self.action_queue ]['testLen']=len( self.action[ self.action_queue ]['test'] )
		
		self.scanID[ self.action_queue ]=0
		self.testID[ self.action_queue ]=0
		self.action_queue +=1
	def multiLanguageValidation( self ):
		if self.backupLoaded['validaton']:
			_printME_( 'Validation Loaded' )
			sys.exit()
		self.scanID={}
		self.testID={}
		self.action={}
		self.action_queue=0
		self.table={}
		quoteComment=self.query( quoteComment=True )
		omitIndex=[]
		for x in quoteComment:
			for i in self.indexes['group'][x]['index']:
				omitIndex.append( i )
		for xID,record in enumerate(self.logistics['action']):
			if record['language']=='global' or record['language']==self.language:
				self.buildValidationActionQueue( xID )
				
		assetLen=len(self.asset)-1
		whitespace=[]
		whitespace.append( ' ' )
		
		for i,char in enumerate(self.asset):
			if not i in omitIndex:
				aID=0
				while not aID==( loopLen ):
					self.action
					if self.action[ aID ]['active']:
						testPass=False
						rulePass=False
						if char in whitespace:
							isWhitespace=True
						else:
							isWhitespace=False
						if self.action[ aID ]['active'][self.testID]['type']=='text':
							if self.action[ aID ]['active'][self.testID]['strict']:
								if self.action[ aID ]['active'][self.testID]['strict']==1:
									theChar=char.lower()
								else:
									theChar=char
								if self.action[ aID ]['active'][self.testID]['data'][ self.scanID[ str(aID) ] ]==theChar:
									self.scanID[ str(aID) ] +=1
								else:
									self.scanID[ str(aID) ]=0
								if self.scanID[ str(aID) ]==len(self.action[ aID ]['active'][self.testID]['data']):
									self.scanID[ str(aID) ]=0
									testPass=True
							else:
								pass
						if testPass:
							self.action[ self.action_queue ]['testLen']
							rulePass=True
					aID+=1
	
	def reactivateActionItems( self ):
		aID=0
		while not aID==( loopLen ):
			self.action[aID]['active']=True
			aID+=1
	def javascriptNamespace( self ):
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		commentIndex=[]
		xIDs=self.query( tag='comment,inline comment', justIDs=True, special='all' )
		for x in xIDs:
			for i in self.indexes['group'][x]['index']:
				commentIndex.append( i )
		equal=self.indexes['char'][ self.query( '=', justIDs=True, isChar=True ) ]
		braces=self.indexes['char'][ self.query( '{', justIDs=True, isChar=True ) ]
		
		items=set(equal['index']) & set(self.indexes['allClosed'])
		lines=[]
		for x in items:
			lines.append( self.getLine( x ) )
		flaggedLines=set(lines) & set( braces['line'] )
		
		namespaceRecords=[]
		x=self.indexes['carriageIndex'].keys()
		car=[]
		
		for x in self.indexes['carriageIndex']['index']:
			car.append( x )
		self.genitemLabelIndexes()
		for line in flaggedLines:
			data=self.assetSnipetLine( line )
			pos=data['text'].index( '{' )+data['start']
			groupID=self.itemLabel( '{}', 'group' )
			record=self.indexes['group'][groupID]
			oc=list(filter(lambda data: data['open']==pos, record['oc']))
			ns=data['text'].split('=')[0]
			ns=ns.replace( ' ', '' ).replace( '\n', '' )
			namespaceRecords.append({ 'ns': ns, 'open': oc[0]['open'], 'close': oc[0]['close'] })
		for i,ns in enumerate(namespaceRecords):
			if not i:
				
				validaton=self.runRules( {'open': ns['open']+1, "close": ns['close']-1}, 'validate namespace' )
				_printME_( text )
				
		
	def runRules( self, on, run, returnFirst=False, shouldLoop=False, scanStart=None, scanEnd=None ):
		self.rlID +=1
		rID=self.rlID
		startOn=0
		self.rls[rID]={
							'action': {},
							'scanID': {},
							'testID': {},
							'rulePass': {},
							'pattern': {},
							'data': {},
		}
		if type( on )==dict:
			asset=self.assetSnipet( on['open'], on['close'] )
			startOn=on['open']
		elif type( on )==str:
			asset=on
		elif type( on )==list:
			startOn=on[0]['open']
			asset=self.assetSnipet( on[0]['open']+1, on[0]['close']-1 )
		
		rulesIDs=[]
		if type( run )==str:
			for i,record in enumerate(self.logistics['rules']):
				if record['description']==run:
					if record['language']=='global' or record['language']==self.language:
						rulesIDs.append( i )
		elif type( run )==list:
			for rl in run:
				if type( rl )==int:
					for i,record in enumerate(self.logistics['rules']):
						if record['id']==rl:
							if record['language']=='global' or record['language']==self.language:
								rulesIDs.append( i )
				elif type( rl )==str:
					for i,record in enumerate(self.logistics['rules']):
						if record['description']==rl:
							if record['language']=='global' or record['language']==self.language:
								rulesIDs.append( i )
		elif type( run )==int:
			for i,record in enumerate(self.logistics['rules']):
				if record['id']==run:
					if record['language']=='global' or record['language']==self.language:
						rulesIDs.append( i )
		def buildRuleActionQueue( self, i, rID, theRule ):
			
			self.rls[rID]['action'][ i ]=theRule
			for ii,record in enumerate(self.rls[rID]['action'][ i ]['patterns']):
				if record['type']=='text' and record['strict']==1:
					self.rls[rID]['action'][ i ]['patterns'][ii]['test']=record['test'].lower()
			self.rls[rID]['action'][ i ]['active']=True
			self.rls[rID]['action'][ i ]['testLen']=len( self.rls[rID]['action'][ i ]['patterns'] )
			
			self.rls[rID]['scanID'][ i ]=0
			self.rls[rID]['testID'][ i ]=0
			self.rls[rID]['rulePass'][ i ]=False
			self.rls[rID]['pattern'][ i ]=False
			self.rls[rID]['data'][ i ]=[]
		omitIndex=[]
		for xID in self.query( tag='comment,inline comment', justIDs=True, special='all' ):
			for x in self.indexes['group'][xID]['index']:
				omitIndex.append( x )
			
		scanID={}
		testID={}
		action={}
		action_queue=0
		table={}
		for i,iX in enumerate(rulesIDs):
			buildRuleActionQueue( self, i, rID, self.logistics['rules'][iX] )
		
		
		
		loopLen=len( self.rls[rID]['action'].keys() )
		
		assetLen=len(asset)-1
		ws=[]
		ws.append( ' ' )
		ws.append( '\n' )
		
		
		
		skippedWS=False
		records=[]
		loopCount=0
		loopICount=0
		data={}
		i=0
		if not scanStart is None:
			i=scanStart
			startOn=scanStart
		if not scanEnd is None:
			assetLen=scanEnd
		text=self.assetSnipet( startOn, assetLen, asset )
		cp( text, 'purple' )
		while not i==assetLen:
			
			loopICount+=1
			ii=i
			if not startOn+i in omitIndex:
				if asset[i] in ws:
					skippedWS=True
				else:
					
					
					aID=0
					allFail=True
					while not aID==loopLen:
						
						
						cp( self.rls[rID]['action'][aID], 'Color.yellow' )
						
						pass
						if self.rls[rID]['action'][aID]['active']:
							loopCount+=1
							
							testID=self.rls[rID]['testID'][aID]
							
							if self.rls[rID]['action'][aID]['patterns'][testID]['strict']==1:
								theChar=asset[i].lower()
							else:
								theChar=asset[i]
							
							_printME_( '___ A', self.rls[rID]['action'][aID]['patterns'][testID]['type'], aID, testID, loopCount, loopICount, i, asset[i] )
							
							if self.rls[rID]['action'][aID]['patterns'][testID]['type']=='text':
								
								if self.rls[rID]['action'][aID]['patterns'][testID]['strict']:
									if self.rls[rID]['action'][aID]['patterns'][testID]['test'][ self.rls[rID]['scanID'][aID] ]==theChar:
										self.rls[rID]['scanID'][aID] +=1
									else:
										self.rls[rID]['scanID'][aID]=0
										self.rls[rID]['action'][aID]['active']=False
										_printME_( 'Fail 01', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
										
										self.rls[rID]['data'][aID]=[]
									if self.rls[rID]['scanID'][aID]==len(self.rls[rID]['action'][aID]['patterns'][testID]['test']):
										
										self.rls[rID]['pattern'][aID]=True
										
								else:
									
									if asset[i] in self.rls[rID]['action'][aID]['patterns'][testID]['test']:
										self.rls[rID]['scanID'][aID] +=1
										
									elif self.rls[rID]['scanID'][aID]:
										
										
										if self.rls[rID]['scanID'][aID]:
											self.rls[rID]['pattern'][aID]=True
											i-=1
											cp( 'back', 'red' )
										else:
											self.rls[rID]['scanID'][aID]=0
											self.rls[rID]['action'][aID]['active']=False
											_printME_( 'Fail 02', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
											
											self.rls[rID]['data'][aID]=[]
									else:
										_printME_( 'asdf test' )
							elif self.rls[rID]['action'][aID]['patterns'][testID]['type']=='index':
								_printME_( 'index HERE' )
								if self.rls[rID]['action'][aID]['patterns'][testID]['test'][ self.rls[rID]['scanID'][aID] ]==theChar:
									self.rls[rID]['scanID'][aID] +=1
								else:
									self.rls[rID]['scanID'][aID]=0
									self.rls[rID]['action'][aID]['active']=False
									_printME_( 'Fail 03', self.rls[rID]['testID'][aID],'-', asset[i], theChar )
									
									
									self.rls[rID]['data'][aID]=[]
								if self.rls[rID]['scanID'][aID]==len(self.rls[rID]['action'][aID]['patterns'][testID]['test']):
									_printME_( 'works' )
									self.rls[rID]['pattern'][aID]=True
									
							elif self.rls[rID]['action'][aID]['patterns'][testID]['type']=='scan':
								
								cp( '\nSTARTING SCAN\n', 'cyan' )
								_printME_( i+1, asset[i], startOn, asset[ i+startOn ] )
								scan=self.runRules( self.asset, self.rls[rID]['action'][aID]['patterns'][testID]['test'], returnFirst=True, scanStart=i+startOn, scanEnd=None )
								cp( '\nSCAN COMPLETE\n', 'darkcyan' )
								_printME_( scan )
								self.rls[rID]['pattern'][aID]=True
							if self.rls[rID]['pattern'][aID]:
								
								cp( [ self.rls[rID]['action'][aID]['tags'], testID ], 'white' )
								cp( [ 'pattern', asset[ii] ], 'green' )
								if self.rls[rID]['action'][aID]['patterns'][testID]['type']=='text':
									_printME_( 'pattern text' )
									text=self.assetSnipet( i-self.rls[rID]['scanID'][aID], i, asset )
									cp( [ 'text:', text ], 'cyan' )
									self.rls[rID]['data'][aID].append({ 'id': self.rls[rID]['action'][aID]['id'], 'pattern': testID, 'data': text })
								
								elif False and self.rls[rID]['action'][aID]['patterns'][testID]['type']=='index':
									_printME_( 'pattern index' )
									
									oc=list(filter(lambda data: data['open']==startOn+i, self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc']))
									try:
										pass
									except Exception as e:
										printVar( self.rls[rID]['action'][aID] )
										
										
									
									
									
									
									
									
									
									
									self.rls[rID]['data'][aID].append({ 'id': self.rls[rID]['action'][aID]['id'], 'pattern': testID, 'data': oc })
									
									text=self.assetSnipet( oc[0]['open'], oc[0]['close'], asset )
									cp( [ 'text:', text ], 'cyan' )
									_printME_( text )
									_printME_( rID, self.rlID, i, startOn+i, asset[i], oc, self.itemLabel( asset[i], 'group' ), self.indexes['group'][ self.itemLabel( asset[i], 'group' ) ]['oc'] )
									_printME_( oc[0]['close'] )
									i=oc[0]['close'] + 1
								elif self.rls[rID]['action'][aID]['patterns'][testID]['type']=='scan':
									text=self.assetSnipet( oc[0]['open'], oc[0]['close'], self.asset )
									cp( [ 'text:', text ], 'cyan' )
									pass
									
								if len( self.rls[rID]['action'][aID]['patterns'][testID]['rules'] ) and not self.rls[rID]['action'][aID]['patterns'][testID]['type']=='scan':
									
									
									cp( '\nSTARTING RULES\n', 'cyan' )
									scan=self.runRules( self.asset, self.rls[rID]['action'][aID]['patterns'][testID]['rules'], returnFirst=True, scanStart=oc[0]['open'], scanEnd=oc[0]['close'] )
									
								if returnFirst:
									records.append( self.rls[rID]['data'][aID] )
									return records
								
								self.rls[rID]['scanID'][aID]=0
								
								if self.rls[rID]['testID'][aID]==len(self.rls[rID]['action'][aID]['patterns'])-1:
									self.rls[rID]['testID'][aID]=0
									cp( 'Zero Test', 'green' )
									self.rls[rID]['rulePass'][aID]=True
								else:
									self.rls[rID]['testID'][aID]+=1
									testID=self.rls[rID]['testID'][aID]
									
							if self.rls[rID]['action'][aID]['loop']:
								self.rls[rID]['action'][aID]['active']=True
							elif self.rls[rID]['rulePass'][aID]:
								records.append( self.rls[rID]['data'][aID] )
								
								if returnFirst:
									return records
								self.rls[rID]['data'][aID]=[]
								if shouldLoop:
									aIDx=0
									while not aIDx==loopLen:
										self.rls[rID]['action'][aIDx]['active']=True
										aIDx+=1
								
							
							_printME_( '___ B', self.rls[rID]['action'][aID]['patterns'][testID]['type'], aID, testID, loopCount, loopICount, i, asset[i] )
							
						pass
						
						
						
						
						
						
						if self.rls[rID]['action'][aID]['active']:
							allFail=False
						aID+=1
						pass
						
					pass
					skippedWS=False
					if allFail:
						_printME_( testID )
						cp( [ 'All Fail', scanStart ], 'red' )
						return records
			pass
			i+=1
		cp( 'All Pass', 'green' )
		return records
	def assetSnipetLine( self, line ):
		pos=self.getLineStartEnd( line )
		snippet=self.assetSnipet( pos['start'], pos['end'] )
		return { 'start': pos['start'], 'end': pos['end'], 'text': snippet }
	def assetSnipet( self, start, end, asset='' ):
		end+=1
		if not asset:
			asset=self.asset
		result=''
		x=start
		if start==end:
			return asset[start]
		while not x==end:
			try:
				result +=asset[x]
			except Exception as e:
				_printME_( asset )
				cp( [ len(asset), start, end, 'self.assetSnipet' ], 'red' )
				return None
				
				
			x+=1
		return result
	def assetSnipetClean( self, start, end, asset='' ):
		if not len( self.omitIndex ):
			self.genOmit()
		end+=1
		if not asset:
			asset=self.asset
		result=''
		x=start
		while not x==end:
			if not x in self.omitIndex:
				result +=asset[x]
			x+=1
		return result
	def genOmit( self ):
		if not len( self.omitIndex ):
			self.omitIndex=[]
			
			
			for i,record in enumerate(self.indexes['group']):
				should=0
				for tag in record['tags']:
					if 'comment' in tag or 'quote' in tag:
						should=1
				if should:
					for ix in record['index']:
						self.omitIndex.append( ix )
	def itemLabel( self, index, what ):
		try:
			return self.indexes['IDs'][what][index]
		except Exception as e:
			pass
			
			
			
			
			
		
		return None
			
	def genLabel( self, i, what, oc=None ):
		test={}
		label=None
		if oc is None:
			try:
				test[ self.indexes[what][i]['label'] ]=None
				label=self.indexes[what][i]['label']
			except Exception as e:
				label=i
				self.noIndex.append({ 'index': i, 'label': self.indexes[what][i]['label'] })
			return label
		else:
			try:
				if 'open' in oc:
					label=self.indexes[what][i]['open']['label']
				else:
					if self.indexes[what][i]['close']['label'] is None:
						label=None
					else:
						label=self.indexes[what][i]['close']['label']
			except Exception as e:
				cp( 'Error: noIndex', 'red' )
				sys.exit()
				
				
				
			
			return label
	def auditTable( self ):
		
		try:
			self.table.keys()
		except Exception as e:
			
			return False
		cleanKeys={}
		for key in self.table.keys():
			for x in self.table[ key ]:
				try:
					cleanKeys[x['id']].append( x )
				except Exception as e:
					cleanKeys[x['id']]=[]
					cleanKeys[x['id']].append( x )
				
				
		test=[0,1]
		if 0 in test:
			theTotals={}
			for key in cleanKeys.keys():
				try:
					theTotals[ str(len(cleanKeys[key])) ] +=1
				except Exception as e:
					theTotals[ str(len(cleanKeys[key])) ]=1
			for key in theTotals.keys():
				_printME_( key, theTotals[key] )
		if 1 in test:
			for key in cleanKeys.keys():
				if not len( cleanKeys[key] )==2:
					cp( '_________________________________________', 'red' )
					_printME_( 'line:', cp(str(cleanKeys[key][0]['line']), 'green')  )
					_printME_( len( cleanKeys[key] ), cleanKeys[key] )
					self.printPos( cleanKeys[key][0]['start']-20, cleanKeys[key][0]['start']+20 )
		
		if 2 in test:
			for key in cleanKeys.keys():
				if len( cleanKeys[key] )==2 and cleanKeys[key][0]['label']=="'":
					_printME_( 'line:', cp(str(cleanKeys[key][0]['line']), 'green')  )
					self.printPos( cleanKeys[key][0]['start'], cleanKeys[key][1]['end'] )
	def buildIndexes2( self ):
		self.index_structure={ 
									'char': { 
												'line': [],
												'index': [],
												'end': [],
												'label': '',
											},
									'group': { 
												'open': {
															'label': '',
															'rID': None,
															'iID': None,
															'pIDs': [],
												},
												'close': {
															'label': '',
															'rID': None,
															'iID': None,
															'pIDs': [],
												},
												'tags': [],
												'index': [],
												'inner': [],
												'groups': [],
												'nestable': None,
												'escape': None,
												'label': '',
											}
							}
		self.indexes={ 'char': [], 'group': [], }
		carriage={
						'index': [],
						'line': [],
						'label': ''
		}
		line=0
		for i,char in enumerate(self.asset):
			carriage['line'].append( line )
			if char=='\n':
				line +=1
				carriage['index'].append( i )
		
		self.buildIndexStructure()
		lookForSingle=[]
		lookForMulti=[]
		who={}
		end={}
		table={}
		scan={}
		i={}
		for i,record in enumerate(self.indexes['char']):
			scan[record['label']]=0
			table[record['label']]=[]
			end[record['label']]=[]
			if len( record['label'] )==1:
				lookForSingle.append( record['label'] )
			else:
				lookForMulti.append( record['label'] )
		
		for i,char in enumerate(self.asset):
			for single in lookForSingle:
				table[single].append( i )
			for multi in lookForMulti:
				if multi[ scan[multi] ]==char:
					scan[multi] +=1
				else:
					scan[multi]=0
				if scan[multi]==len(multi):
					end[multi].append( i )
					table[multi].append( i-len(multi)-1 )
					scan[multi]=0
		
		
		
		
		
		
		_printME_( 'done' )
		sys.exit()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		indexes=self.indexes
		for i,record in enumerate(indexes['group']):
			if 'comment' in record['tags']:
				done=False
				i=0
				endAdd=len( record['open']['label'] )-1
				openID=record['open']['iID']
				try:
					closeID=record['close']['iID']
					pass
				except Exception as e:
					printVar( record )
					sys.exit()
				index=[]
				end=[]
				line=[]
				while not done:
					if not openID is None and not indexes['char'][ openID ]['index']:
						pos=self.asset.find( record['open']['label'] )
						posEnd=pos + endAdd
						if not pos==-1:
							index.append( pos )
							end.append( posEnd )
						else:
							done=True
							
				self.indexes['char'][ openID ]['index']=index
				self.indexes['char'][ openID ]['end']=end
				
				if not record['close']['label'] is None:
					endAdd=len( record['close']['label'] )-1
					index=[]
					end=[]
					line=[]
					while not done:
						if not closeID is None and not indexes['char'][ closeID ]['index']:
							pos=self.asset.find( record['close']['label'] )
							posEnd=pos + endAdd
							if not pos==-1:
								index.append( pos )
								end.append( posEnd )
							else:
								done=True
								
					self.indexes['char'][ openID ]['index']=index
					self.indexes['char'][ openID ]['end']=end
				
				
				
				
				
				
				
				
				
				
						
		printVar( self.indexes )
		
		
	def inIndex( self, label=None, iID=None, gID=None, rID=None, pID=None, tag=None, oc='open,close', cg='char,group' ):
		oc=oc.lower()
		if not iID is None:
			try:
				self.indexes['char'][iID]
			except NameError:
				return False
			else:
				return True
		if not label is None and not pID is None and not gID is None:
			if not self.inIndex( label=label ):
				_printME_( 'Error: test for label first' )
				sys.exit()
			if not self.inIndex( gID=gID ):
				_printME_( 'Error: test for gID first' )
				sys.exit()
				if pID in self.indexes['group'][gID]['open']['pIDs']:
					return True
		if not label is None and not pID is None:
			if not self.inIndex( label=label ):
				_printME_( 'Error: test for label first' )
				sys.exit()
				for item in self.indexes['group']:
					if item['label']==label:
						if 'open' in oc:
							if pID in item['open']['profiles']:
								return True
						if 'close' in oc:
							if pID in item['close']['profiles']:
								return True
		elif not rID is None and not gID is None:
			if not self.inIndex( gID=gID ):
				_printME_( 'Error: test for gID first' )
				sys.exit()
			if 'open' in oc:
				if self.indexes['group'][gID]['open']['rID']==rID:
					return True
			if 'close' in oc:
				if self.indexes['group'][gID]['close']['rID']==rID:
					return True
		elif not rID is None:
			for char in self.indexes['group']:
				if 'open' in oc:
					if char['open']['rID']==rID:
						return True
				if 'close' in oc:
					if char['close']['rID']==rID:
						return True
		elif not gID is None:
			try:
				self.indexes['group'][gID]
			except NameError:
				return False
			else:
				return True
		elif not label is None:
			if 'group' in cg:
				for item in self.indexes['group']:
					if item['label']==label:
						return True
			if 'char' in cg:
				for item in self.indexes['char']:
					if item['label']==label:
						return True
		elif not tag is None:
			for char in self.indexes['group']:
				if char['label']==label:
					if tag in char['tags']:
						return True
		return False
	def buildIndexStructure( self, comment=False, quote=False ):
		for rID,record in enumerate(self.logistics['characters']):
			for pID,profile in enumerate(record['profiles']):
				if profile['language']==self.language or profile['language']=='global':
					if profile['isOpen']:
						indexes={ 
										'open': {
													'label': '',
													'rID': None,
													'iID': None,
													'pIDs': [],
										},
										'close': {
													'label': '',
													'rID': None,
													'iID': None,
													'pIDs': [],
										},
										'total': 0,
										'tags': [],
										'oc': [],
										'index': [],
										'inner': [],
										'groups': [],
										'nestable': None,
										'escape': None,
										'label': '',
						}
						charIndexes={
										'total': 0,
										'index': [],
										'start': [],
										'end': 1,
										'line': [],
										'label': ''
						}
						charIndexesC={
										'total': 0,
										'index': [],
										'start': [],
										'end': 1,
										'line': [],
										'label': ''
						}
						indexes['open']={}
						indexes['close']={}
						indexes['open']['pIDs']=[]
						indexes['close']['pIDs']=[]
						indexes['close']['label']=None
						charIndexes['label']=record['char']
						indexes['label']=record['char']
						indexes['open']['label']=record['char']
						indexes['open']['rID']=rID
						indexes['open']['pIDs'].append( pID )
						indexes['tags']=profile['tags']
						indexes['nestable']=profile['nest']
						indexes['escape']=''
						for charID in profile['escape']:
							indexes['escape'] +=self.charById( charID )['char']
							
						for charID in profile['set']:
							char=self.charById( charID )['char']
							charIndexes['label'] +=char
							indexes['label'] +=char
							indexes['open']['label'] +=char
						if not type(profile['groupID'])==bool:
							pass
							for rIDc,recordC in enumerate(self.logistics['characters']):
								for pIDc,profileC in enumerate(recordC['profiles']):
									if not type(profileC['groupID'])==bool and profileC['groupID']==profile['groupID'] and not profileC['isOpen']:
										charIndexesC['label']=recordC['char']
										indexes['label'] +=recordC['char']
										indexes['close']['label']=recordC['char']
										indexes['close']['rID']=rIDc
										indexes['close']['pIDs'].append( pIDc )
										
										for charID in profileC['set']:
											char=self.charById( charID )['char']
											charIndexesC['label'] +=char
											indexes['label'] +=char
											indexes['close']['label'] +=char
						
						pass
						self.addRecords( indexes, charIndexes, charIndexesC )
	
							
							
 
	def addRecords( self, indexes, charIndexes, charIndexesC ):
		if not self.inIndex( label=indexes['open']['label'] ):
			
			
			
			self.indexes['char'].append( charIndexes )
			xID=self.query( label=indexes['open']['label'], justIDs=True )
			indexes['open']['iID']=xID['iID']
			if not indexes['close']['label'] is None:
				if not self.inIndex( label=indexes['close']['label'] ):
					self.indexes['char'].append( charIndexesC )
				xID=self.query( label=indexes['close']['label'], justIDs=True )
				indexes['close']['iID']=xID['iID']
			self.indexes['group'].append( indexes )
		else:
			xID=self.query( label=indexes['label'], justIDs=True )
			if not xID['gID'] is None and not self.inIndex( gID=xID['gID'], pID=pID, oc='open' ):
				self.indexes['group'][xID['gID']]['open']['pIDs'].append( pID )
				for tag in indexes['tags']:
					self.indexes['goup'][xID['gID']]['tags'].append( tag )
			if not self.inIndex( gID=xID['gID'], pID=pIDc, oc='close' ):
				self.indexes['goup'][xID['gID']]['close']['pIDs'].append( pIDc )
			if not self.inIndex( label=indexes['close']['label'] ):
				pass
		pass
		
		
		if not indexes['close']['label'] is None:
			if not self.inIndex( label=indexes['close']['label'] ):
				self.indexes['char'].append( charIndexesC )
		if not self.inIndex( label=indexes['open']['label'] ):
			self.indexes['char'].append( charIndexes )
		pass
	def omitTickets( self ):
		self.omitRanges=[]
		closed=0
		for i,ticket in enumerate(self.locationTable):
			if not ticket['isOpen']:
				self.omitRanges.append({ 'start': ticket['start'], 'end': ticket['end'], })
				closed+=1
		_printME_( 'closed:', closed )
	def buildLocationTable( self ):
		relevantTable=self.relevantTable
		end=len(self.asset)-1
		self.tickets={
							'open': {},
							'closeOn': {},
							'scanningFor': { 'char': [], 'multi': [] },
							'records': [],
							'closed': 0,
		}
		zNoNestActive=''
		for relevant in self.relevantTable['char']:
			self.tickets['open'][relevant]=0
		for i in self.idCache:
			char=self.asset[i]
			if True:
				if not len(zNoNestActive) and char in self.relevantTable['char']:
					shouldProcess=False
					record=False
					for check in self.relevantTable['records']:
						if check['char']==char:
							hasSet=False
							for lan in check['profiles']:
								if len(lan['set']):
									xx=i
									for theID in lan['set']:
										xx+=1
										if not xx > end:
											if self.asset[xx]==self.charById( theID )['char']:
												hasSet=True
												recordSet=lan
												shouldProcess=True
												break
								else:
									record=lan
									shouldProcess=True
							if hasSet:
								record=recordSet
							break
					if shouldProcess:
						if len( record['escape'] ):
							xx=i
							record['escape'].reverse()
							for eID in record['escape']:
								xx-=1
								if xx > 0:
									if self.asset[xx]==self.charById( eID )['char']:
										shouldProcess=False
					if shouldProcess:
						lan=record
						if type(lan['groupID'])==bool:
							close={ 'char': char , 'lan': lan }
						else:
							close=self.charByGroupIdClose( lan['groupID'] )
						if type(close)==bool:
							_printME_( 'Error: line 292... ish' )
							sys.exit()
						if not close['char'] in self.tickets['scanningFor']['char']:
							self.tickets['scanningFor']['char'].append( close['char'] )
						if len(close['lan']['set']):
							if not close['char']==self.tickets['scanningFor']['multi']:
								self.tickets['scanningFor']['multi'].append( close['char'] )
						self.tickets['records'].append({  
															'start': i,
															'end': False,
															'isOpen': True,
															'closeOn': self.tickets['open'][char],
															'char': char,
															'lan': close['lan'],
															'closeChar': close['char']
														})
						pass
						self.tickets['open'][char] +=1
						if not record['nest']:
							zNoNestActive=close['char']
				if char in self.tickets['scanningFor']['char']:
					shouldProcess=True
					cID=None
					for ic,check in enumerate(self.tickets['records']):
						if check['isOpen'] and check['start'] < i  and check['closeChar']==char and check['closeOn']==(self.tickets['open'][ check['char'] ]-1):
						
						
							cID=ic
							if len( check['lan']['escape'] ):
								xx=i
								check['lan']['escape'].reverse()
								for eID in check['lan']['escape']:
									xx-=1
									if xx > 0:
										if self.asset[xx]==self.charById( eID )['char']:
											shouldProcess=False
					if not cID is None:
						groupLength=1
						if char in self.tickets['scanningFor']['multi']:
							found=False
							if self.tickets['records'][cID]['closeChar']==char:
								xx=i
								for theID in self.tickets['records'][cID]['lan']['set']:
									xx+=1
									if not xx > end:
										if self.asset[xx]==self.charById( theID )['char']:
											groupLength+=1
											found=True
							if not found:
								shouldProcess=False
					if shouldProcess and not cID is None:
						zNoNestActive=''
						self.tickets['open'][self.tickets['records'][cID]['char']] -=1
						self.tickets['closed']+=1
						self.tickets['records'][cID]['end']=i
						self.tickets['records'][cID]['isOpen']=False
						self.locationTable.append( self.tickets['records'][cID] )
						self.tickets['records'].pop( cID )
	def findCloseByChar( self, char ):
		
		for record in self.logistics['characters']:
			if record['char']==char:
				for lan in record['profiles']:
					if lan['language']==self.language or lan['language']=='global':
						if lan['isOpen']:
							if not type(lan['groupID'])==bool:
								return self.charByGroupIdClose( lan['groupID'] )
							else:
								return { 'char': record['char'] , 'lan': lan }
							
		return False
	def charByGroupIdClose( self, groupID ):
		
		found=False
		for i,record in enumerate(self.logistics['characters']):
			for lan in record['profiles']:
				if lan['groupID']==groupID and not lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
		return False
	def charByGroupIdOpen( self, groupID ):
		
		for record in self.logistics['characters']:
			for lan in record['profiles']:
				if lan['groupID']==groupID and lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
					
		return False
	def inCommentRange( self, i ):
		for omit in self.omitRanges:
			if i >=omit['start'] and i <=omit['end']:
				return True
		return False
	def buildRelevantTable( self, comment=False, quote=False ):
		self.relevantTable={ 'char': [], 'multi': [], 'records': [] }
		if not comment and not quote:
			for record in self.logistics['characters']:
				isRelevant=False
				profiles=[]
				for lan in record['profiles']:
					if lan['language']==self.language or lan['language']=='global':
						tagList=[]
						if lan['isOpen']:
							isRelevant=True
							profiles.append( lan )
							if len(lan['set']):
								pass
				if isRelevant:  
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )
		elif comment:
			for record in self.logistics['characters']:
				isRelevant=False
				profiles=[]
				for lan in record['profiles']:
					if lan['language']==self.language:
						isComment=False
						tagList=[]
						for tag in lan['tags']:
							if 'comment' in tag:
								isRelevant=True
								profiles.append( lan )
				if isRelevant:  
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )
		elif quote:
			for record in self.logistics['characters']:
				isRelevant=False
				profiles=[]
				for lan in record['profiles']:
					if lan['language']==self.language or lan['language']=='global':
						isComment=False
						tagList=[]
						for tag in lan['tags']:
							if 'quote' in tag:
								isRelevant=True
								profiles.append( lan )
				if isRelevant:  
					self.relevantTable['records'].append({ 'char': record['char'] , 'profiles': profiles })
					self.relevantTable['char'].append( record['char'] )
	def shouldScan( self, char ):
		record=charByChar( char )
	def charByChar( self, char ):
		
		for record in self.logistics['characters']:
			if record['char']==char:
				return record   
		return False
	def buildMultilineComments( self ):
		
		for record in self.logistics['characters']:
			charSet=record['char']
			theOpen=record['char']
			for lan in record['profiles']:
				if lan['language']==self.language:
					isComment=False
					tagList=[]
					if lan['isOpen'] and 'comment' in lan['tags'] :
						_printME_( lan['tags'] )
						tagList.append( 'comment' )
						isComment=True
						theClose=''
						if type(lan['set'])==list and len( lan['set'] ):
							for setID in lan['set']:
								if type(setID)==int:
									nextChar=self.charById( setID )['char']
									if type( nextChar )==str:
										theOpen +=nextChar
						if not type(lan['groupID'])==bool:
							groupInfo=self.charByGroupIdClose( lan['groupID'] )
							if not type(groupInfo)==bool:
								theClose +=groupInfo['char']
								if len( groupInfo['lan']['set'] ):
									for groupSetId in groupInfo['lan']['set']:
										if type(groupSetId)==int:
											nextChar=self.charById( groupSetId )['char']
											if type( nextChar )==str:
												theClose +=nextChar
						if isComment and True:
							self.multilineComments.append({ 'open': theOpen, 'close': theClose })
	def charByGroupId( self, groupID ):
		
		for record in self.logistics['characters']:
			for lan in record['profiles']:
				if lan['groupID']==groupID and not lan['isOpen']:
					return { 'char': record['char'] , 'lan': lan }
					
		return False
	def buildInlineComments( self ):
		
		for record in self.logistics['characters']:
			charSet=record['char']
			comment=record['char']
			for lan in record['profiles']:
				if lan['language']==self.language:
					isComment=False
					tagList=[]
					isInline=False
					for tag in lan['tags'] :
						if lan['isOpen'] and 'inline' in tag:
							isInline=True
							tagList.append( tag )
					if isInline:
						isComment=True
						if type(lan['set'])==list and len( lan['set'] ):
							for setID in lan['set']:
								if type(setID)==int:
									nextChar=self.charById( setID )['char']
									if type( nextChar )==str:
										comment +=nextChar
					if isComment and True:
						self.inlineComments.append( comment )
		
	def charById( self, setID ):
		
		for record in self.logistics['characters']:
			if record['id']==setID:
				return record
		return False
	def cleanInlineComments( self ):
		pass
		
		
		
		
		
		
		
		
		
	def cleanMultilineComments( self ):
		pass
		
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
			
			
			
	def jsNameSpace_2019( self ):
		
		
		self.namespaceFunctions=[]
		gi=None
		for i,record in enumerate(self.indexes['group']):
			if record['label']=='{}':
				gi=i
				break
		ci=None
		for i,record in enumerate(self.indexes['char']):
			
			if record['label']=='{':
				ci=i
				break
		functions=[]
		lastNS=''
		documentation=[]
		docIndex=[]
		self.genOmit()
		
		
		
		
		
		
		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line']=self.getLine( oc['open'] )
			oc['linePos']=self.getLinePos( oc['line'] )
			code=self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs=None
			code=code=self.assetSnipet( oc['open'], oc['close'] )
			if 'doc2b' in code:
				thisIs='documentation'
				documentation.append( oc )
				docIndex.append( oc['open'] )
		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line']=self.getLine( oc['open'] )
			oc['linePos']=self.getLinePos( oc['line'] )
			code=self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs=None
			if '=' in code:
				ns=code.split('=')[0]
				ns=ns.replace( ' ', '' )
				ns=ns.replace( '\t', '' )
				lastNS=ns
				thisIs='var'
				
			if 'function' in code.lower() and ':' in code.lower() and '(' in code.lower():
				thisIs='function'
				ns=code.split(':')[0]
				ns=ns.replace( ' ', '' )
				ns=ns.replace( '\t', '' )
				fullNS=lastNS + '.' + ns
				oc['ns']=fullNS
				functions.append( oc )
				code=code=self.assetSnipetClean( oc['open'], oc['close'] )
				terms=self.findTerms( code )
				for t in terms:
					pass
					
				oc['documentation']=[]
				for doci,doc in enumerate(documentation):
					if doc['open'] > oc['open'] and doc['open'] < oc['close']:
						oc['documentation'].append( doci )
		self.profile['documentation']=documentation
		self.profile['functions']=functions
		self.saveProject()
		return self.profile
	def jsNameSpace( self ):
		if self.backupLoaded['profile']:
			return self.profile
		self.namespaceFunctions=[]
		gi=None
		for i,record in enumerate(self.indexes['group']):
			if record['label']=='{}':
				gi=i
				break
		ci=None
		for i,record in enumerate(self.indexes['char']):
			
			if record['label']=='{':
				ci=i
				break
		functions=[]
		lastNS=''
		documentation=[]
		docIndex=[]
		self.genOmit()
		
		
		
		
		
		
		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line']=self.getLine( oc['open'] )
			oc['linePos']=self.getLinePos( oc['line'] )
			code=self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs=None
			code=code=self.assetSnipet( oc['open'], oc['close'] )
			if 'doc2b' in code:
				thisIs='documentation'
				documentation.append( oc )
				docIndex.append( oc['open'] )
		
		
		
		top=[]
		for i,oc in enumerate(self.indexes['group'][gi]['oc']):
			oc['line']=self.getLine( oc['open'] )
			oc['linePos']=self.getLinePos( oc['line'] )
			if not oc['open'] in self.indexes['group'][gi]['inner']:
				top.append( oc )
		for oc in top:
			code=self.assetSnipet( oc['linePos']+1, oc['open'] )
			thisIs=None
			if '=' in code:
				ns=code.split('=')[0]
				ns=ns.replace( ' ', '' )
				ns=ns.replace( '\t', '' )
				lastNS=ns
				thisIs='var'
				
				
				
				
				for i,ocX in enumerate(self.indexes['group'][gi]['oc']):
					if ocX['open'] > oc['open'] and ocX['close'] < oc['close']:
						codeX=self.assetSnipet( ocX['linePos']+1, ocX['open'] )
						if 'function' in codeX.lower() and ':' in codeX.lower() and '(' in codeX.lower():
							thisIs='function'
							ns=codeX.split(':')[0]
							ns=ns.replace( ' ', '' )
							ns=ns.replace( '\t', '' )
							fullNS=lastNS + '.' + ns
							ocX['ns']=fullNS
							functions.append( ocX )
							
							
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		self.profile['functions']=functions
		self.saveProject()
		return self.profile
	def findTerms( self, code ):
		data=''
		for char in code:
			if not char in _str.alphaChar+'._-':
				data +=' '
			else:
				data +=char
		data=_str.replaceDuplicate( data, ' ' )
		data=_str.cleanBE( data, ' ' )
		return data.split(' ')
	def findTerms_has_issues( self, code ):
		result=[]
		for line in code.split('\n'):
			data=''
			for char in code:
				if not char in _str.alphaChar+'._-':
					data +=' '
				else:
					data +=char
			data=_str.replaceDuplicate( data, ' ' )
			data=_str.cleanBE( data, ' ' )
			result.append( data.split(' ') )
		return result
	def jsNameSpace_Old( self ):
		self.namespaceFunctions=[]
		theFileRows=[]
		lineIDX=[]
		for i,line in enumerate(self.asset.split('\n')):
			line=_str.cleanBE( line, ' ' )
			
			if len( line ) and not line.startswith('//'):
				if not '//' in line and not '}'in line :
					theFileRows.append( line )
					lineIDX.append( i )
					
		namespaceList=[]
		lineID=[]
		for i,line in enumerate(theFileRows):
			if not 'this.' in line and not 'prototype' in line and not '.v.' in line and '.' in line and '=' in line and '{' in line and not '==' in line and not line.startswith('for ') and not line.startswith('var ') and not line.startswith('$') and not '(' in line and not '[' in line:
				namespaceList.append( line )
				lineID.append( lineIDX[i] )
				
				
		namespaceFunctions=[]
		for i,ns in enumerate(namespaceList):
			
			pos=self.asset.find( ns )
			end=len(self.asset) -( pos + len(ns)+1 )
			string=self.asset[pos:-end]
				
			bOpen=1
			bClose=0
			closeingChar=False
			nsX=ns.replace( ' ', '' )
			
			namespaceRecord={ 'ns': nsX[:-2],  'raw': ns, 'start': pos }
			self.namespaceFunctions.append( namespaceRecord )
		pass
		ns=self.namespaceFunctions
		idList=[]
		for i,record in enumerate(ns):
			ix=self.findStringInAsset( record['ns']+'={' )
			if ix:
				ns[i]['charID']=ix
				idList.append( ix )
				
		testTable=[]
		for record in self.locationTable:
			if record['char']=='{':
				testTable.append( record )
		relevant=[]
		xx=0
		for test in testTable:
			if test['start'] in idList:
				xx +=1
				relevant.append( test )
		for i,record in enumerate(ns):
			for ticket in relevant:
				try:
					if ns[i]['charID']==ticket['start']:
						ns[i]['record']=ticket
				except Exception as e:
					printVar( ns[i] )
					
		self.namespaceFunctions=ns
		return self.namespaceFunctions
	def link_jsNameSpace_to_function_payloads( self ):
		self.jsNameSpace()
		
		fnList=[]
		for i,ns in enumerate(self.namespaceFunctions):
			fn=[]
			try:
				code=self.findCode( ns['record']['start'], ns['record']['end'] )
				for ln in code.split('\n'):
					if ':' in ln and '(' in ln and ')' in ln and '{' in ln and 'function' in ln and not 'push(' in ln:
						f=ns['ns']+'.'+ln.split(':')[0].replace(' ','')
						fn.append( f )
						fnList.append( f )
						
				self.namespaceFunctions[i]['functions']=fn
			except Exception as e:
				pass
			
		xref={}
		for i,ns in enumerate(self.namespaceFunctions):
			code=self.findCode( ns['record']['start'], ns['record']['end'] )
			
			xref[i]=[]
			for fnx in fnList:
				if fnx in code:
					xref[i].append( fnx )
		for i in xref.keys():
			cp( self.namespaceFunctions[i]['ns'] )
			for x in xref[i]:
				_printME_( '\t', x )
	# def quickTest( self ):
	#   dataSample=vc.HD.getTable( 'auditCodeBase_js_field_tmp.json', 1 )
	#   self.tableAudit=_profile.records.audit( 'tableAudit', dataSample )
		
	#   printVar( self.tableAudit )
		
		
		
		
	def findX(self, key, dictionary):
		for k, v in dictionary.iteritems():
			if k==key:
				yield v
			elif isinstance(v, dict):
				for result in find(key, v):
					yield result
			elif isinstance(v, list):
				for d in v:
					if isinstance(d, dict):
						for result in find(key, d):
							yield result
	def findStringInAsset( self, string ):
		test=0
		i=0
		while not i==len(self.asset)-1:
			char=self.asset[i]
			if not char==' ':
				if string[test]==char:
					test +=1
				else:
					test=0
				if test==len(string):
					return i
			i+=1
		return False
	def buildIDCache( self ):
		self.idCache=[]
		self.idOmitCache=[]
		a=len(self.asset)
		i=0
		while not i==a:
			if not self.inCommentRange( i ):
				self.idCache.append( i )
			else:
				self.idOmitCache.append( i )
			i +=1
		if not( len(self.idOmitCache) + len(self.idCache) )==len(self.asset):
			_printME_( 'Error xy' )
	def findCode( self, start, end ):
		return self.asset[ start :-( len(self.asset) - end ) ]
	def buildCarriageReturnTable( self ):
		self.carriageReturnTable=[]
		self.carriageReturnTable.append( 0 )
		
		for i in self.idCache:
			char=self.asset[i]
			if char=='\n':
				
				self.carriageReturnTable.append( i )
		
		
		
	def noComment( self ):
		commentRecords=self.query( tag='comment', justIDs=True )
		_printME_( commentRecords )
		sys.exit()
def loadProject( project=None ):
	
	global validator
	result=None
	if not project is None:
		__.validator_Project=project
	pickle=vc.FIG.imp('pickle')
	if pickle is None:
		return ''
	try:
		with open( objFile() , 'rb') as objThis:
			result=pickle.load(objThis)
	except Exception as e:
		pass
	if not result is None:
		validator=result
	cp( 'Loaded: ' + objFile(), 'green' )
	return result
def objFile():
	return __.objectPath.replace( 'MD5', __.validator_Project )
def action(path=None):
	data=vc.HD.getText( switches.values('Files')[fi], raw=True );

# import _rightThumb._profileVariables as _profile
class simpleCode:
	def __init__( self, code=None, addString=None ):
		global validator
		self._code=None
		self.addString=addString
		self.code=''
		if not code is None:
			self.code=code
	def cleanup( self ):
		self.code=_str.cleanBE( self.code, ' ' )
		self.code=_str.replaceDuplicate( self.code, ' ' )
	def process( self, code, clean=False, addString=None ):
		if not addString is None:
			self.addString=addString
		self.segments=[]
		self.code=code
		if clean:
			self.cleanup()
		self.identityCode()
		self.build()
		return self.segments
		
		
	def identityCode( self ):
		status=validator.createIndex( self.code, 'javascript', skipLoad=True, simple=False, A=False, B=True, C=False, addString=self.addString )
		return validator.identity
	def build(self):
		
		
		def build_item(i,im):
			segments=[]
			while not i==im:
				if i in validator.identity['location']['open']:
					o=i
					c=validator.identity['location']['open'][o]
					l=validator.getLabel( o, string=True )
					s=validator.assetSnipet( o, c )
					
					if validator.identity['location']['open'][o]:
						segments.append({ 'o':o,'c':c,'l':l,'txt':s })
				else:
					pass
					
					
					
					
					
					
					
					
					
				i+=1
			return segments
		im=len(self.code)-1
		i=0
		
		self.segments=self.segments + build_item(i,im)
		
		segments=[]
		for i,seg in enumerate(self.segments):
			record={}
			record['i']=i
			record['status']=1
			for k in seg:
				record[k]=seg[k]
			segments.append(record)
		self.segments=segments
		if not len(self.segments):
			return None
		self.index={}
		for i,seg in enumerate(self.segments):
			self.index[ seg['o'] ]=i
		
		
		para=[]
		for i,seg in enumerate(self.segments):
			if seg['l']=='parentheses':
				if seg['o']==0:
					para.append({ 'i': i, 'status': 1 })
				else:
					para.append({ 'i': i, 'status': 0 })
		
		for ip,pax in enumerate(para):
			pa=self.segments[ pax['i'] ]
			if not pax['status']:
				for i,seg in enumerate(self.segments):
					if seg['c']==pa['o']-1:
						self.segments[i]['l']='function'
						self.segments[i]['p']=pax['i']
						self.segments[ pax['i'] ]['status']=0
						para[ip]['status']=1
		openPara=False
		for ip,pax in enumerate(para):
			pa=self.segments[ pax['i'] ]
			if not pax['status']:
				openPara=True
		if openPara:
			for ip,pax in enumerate(para):
				pa=self.segments[ pax['i'] ]
				o=pa['o']
				probable=-1
				probableID=None
				if not pax['status']:
					for i,seg in enumerate(self.segments):
						if seg['c'] < o and seg['c'] > probable and 'alpha' in seg['l']:
							probable=seg['c']
							probableID=i
				if not probableID is None:
					para[ip]['status']=1
					self.segments[probableID]['l']='function'
					self.segments[probableID]['p']=pax['i']
					self.segments[ pax['i'] ]['status']=0
		for i,seg in enumerate(self.segments):
			if 'function' in seg['l']  and 'p' in seg:
				self.segments[i]['args']=[]
				o=self.segments[ seg['p'] ]['o']
				c=self.segments[ seg['p'] ]['c']
				for ix,segx in enumerate(self.segments):
					if segx['o'] > o and segx['o'] < c: 
						if segx['c'] > o and segx['c'] < c:
							
							if not 'arg' in self.segments[ix]['l']:
								self.segments[ix]['l'] +=',arg'
							if 'function' in self.segments[ix]['l']:
								fe=self.functionEnd(ix)
								if type(fe)==int:
									o=fe
							self.segments[ix]['status']=0
							self.segments[i]['args'].append(ix)
		eq=[]
		for i,x in enumerate(self.code):
			if x=='=':
				eq.append({ 'i': i, 'status': 0 })
		for ip,pax in enumerate(eq):
			
			o=pax['i']
			
			
			probable=None
			probableID=None
			if not pax['status']:
				closest=[]
				for i,seg in enumerate(self.segments):
					if seg['c'] < o and probable is None and 'alpha' in seg['l']:
						probable=seg['c']
						probableID=i
						
						
					if not probable is None and seg['c'] < o and seg['c'] > probable and 'alpha' in seg['l']:
						
						
						probable=seg['c']
						probableID=i
			if not probableID is None:
				eq[ip]['status']=1
				lastProbable=probableID
				self.segments[probableID]['l']='variable'
				self.segments[probableID]['val']=-1
				probable=None
				probableID=None
				for i,seg in enumerate(self.segments):
					if seg['c'] > o and probable is None :
						
						probable=seg['c']
						probableID=i
					if not probable is None and seg['c'] > o and seg['c'] < probable :
						
						probable=seg['c']
						probableID=i
				if not probableID is None:
					self.segments[lastProbable]['val']=probableID
					self.segments[probableID]['status']=0
		
		
		for i,seg in enumerate(self.segments):
			
			if seg['status']:
				self.children(i)
		
		
		return None
	def children( self, i, p=None ):
		if p is None:
			self.segments[i]['rent']=-1
		if not p is None:
			self.segments[i]['rent']=p
		seg=self.segments[i]
		if 'function' in seg['l']:
			self.children( seg['p'], i )
			for arg in seg['args']:
				self.children( arg, i )
		if 'alpha' in seg['l']:
			return None
		if 'parentheses' in seg['l']:
			return None
		if 'variable' in seg['l']:
			self.children( seg['val'], i )
		return None
		
		
	def functionEnd( self, i ):
		l=self.segments[i]['l']
		if 'function' in l:
			return self.segments[ self.segments[i]['p'] ]['c']
__.code=simpleCode()





####################################################################################################################################


class PY3TO2:
	def __init__( self ):
		pass
	def spaceOut( self, line ):
		ln = ''
		for char in line:
			if char in vc.STR.alphanumeric+'._':
				ln += char
			else:
				ln += ' '
		return ln

	def cleanMe( self, line, subject=' ' ):
		ii = 0
		while line.endswith(subject):
			line = line[:-1]
			if ii > 100:
				break
			ii += 1
		ii = 0
		while line.startswith(subject):
			line = line[1:]
			if ii > 100:
				break
			ii += 1
		ii = 0
		while subject+subject in line:
			line = line.replace( subject+subject, subject )
			if ii > 100:
				break
			ii += 1
		return line

	def process( self, line ):
		line = line.replace( 'def '+' ', 'def ' )
		line = line.replace( 'def '+' ', 'def ' )
		line = line.replace( 'def '+' ', 'def ' )
		line = line.replace( 'def '+' ', 'def ' )
		line = line.replace( chr(27), '' )
		line = line.replace( chr(10), '' )
		line = line.replace( '\n', '' )
		line = line.replace( '\r', '' )
		line = line.replace( '  ', '\t' )
		lx = self.spaceOut(' '+line+' ')
		if not '.print(' in line and ' print ' in lx and not ' def ' in lx and not "'print" and not '"print' and 'print(' in line:
			line = line.replace( '_printME_(', 'print ' )
			line = self.cleanMe( line, ' ' )
			if line.endswith(')'):
				line = line[:-1]
			# print( line )

		line = line.replace( 'except '+'Exception, e:', 'except e:' )
		line = line.replace( 'except '+'Exception, ee:', 'except ee:' )
		line = line.replace( 'except '+'Exception, error:', 'except error:' )
		line = line.replace( 'def '+'_printME_(', 'def print2(' )
		line = line.replace( 'self'+'.print(', 'self.print2(' )
		line = line.replace( '#!/usr/bin'+'/python3', '#!/usr/bin'+'/python2' )
		line = line.replace( 'ð', '' )
		line = line.replace( '\xf0', '' )
		
		# line = line.replace( 'installer.py ', 'installer.py2 ' )

		line = line.replace( 'installer.py ', 'installer.py2 ' )
		line = line.replace( '$widgets/install/installer.py ', 'installer.py2 ' )


		line = line.replace( 'def print(', 'def print2(' )
		line = line.replace( '.print(', '.print2(' )
		if 'print' in line and 'end' in line and '=' in line:
			while ' '+' ' in line:
				line = line.replace( ' '+' ', ' ' )
			line = line.replace( ' =', '=' )
			line = line.replace( '= ', '=' )

			line = line.replace( 'end'+'=""', '' )
			line = line.replace( "end"+"=''", '' )
			line = self.cleanMe( line, ' ' )
			line = self.cleanMe( line, ',' )
			line = self.cleanMe( line, ' ' )
		line = line.replace( "str(decoded"+".decode('utf-8'))", 'str(decoded)' )
		if 'alias ' in line:
			line = line.replace( 'tool ', 'tool2 ' )

		newline = ''
		for c in line:
			if c in vc.STR.printable2:
				newline+=c

		return newline

	def convert( self, f, t=[] ):
		loader()
		file = ''
		if v.pipe:
			data = v.pipe
		if t:
			if type(t) == list:
				tx = []
				for x in t:
					tx.append( vc.PATHS.path( x ) )
				t = tx
			if type(t) == str:
				t  = vc.PATHS.path( t )
		if f:
			if type(f) == list:
				for x in f:
					self.convert(x,t)
				return None
			f  = vc.PATHS.path( f )
			fi = vc.PATHS.path( f, ab=False, file=True )
			fo = vc.PATHS.path( f, ab=False, pop=True )
			if not t:
				if not '.' in fi:
					fi += '2'
				if not '.py' in fi:
					fi = fi.replace('.py','2.py')
				t = fo +os.sep+ fi
		if f:
			data = vc.HD.getText( f )



		for i,line in enumerate( data ):
			if not i:
				file+='#!/usr/bin/python2\n'
				# print( '#!/usr/bin/python2' )
			else:
				line = self.process(line)+'\n'
				file+=line
				# print(line)
		if t:
			if type(t) is list:
				for x in t:
					vc.HD.saveText( file, x )
					cp( [ 'Saved:', x ], 'cyan' )
			else:
				vc.HD.saveText( file, t )
				cp( [ 'Saved:', t ], 'cyan' )

		else:
			_printME_(file)


def print_help():
	cp( 'help', 'yellow' )
	# os.system('cls')
	_printME_('')

	try:
		_printME_('Version: \t', cp( v.appInfo['version'], 'cyan', p=0 ) + '\n')
		configured = True
	except Exception as e:
		configured = False

	try:
		_printME_('Description: \t', v.appInfo['description'] + '\n')
		configured = True
	except Exception as e:
		configured = False

	try:
		if len(v.appInfo['prerequisite']) > 0:
			_printME_('Prerequisite:')
			for prereq in v.appInfo['prerequisite']:
				_printME_('\t' + prereq)
			_printME_('\n')
	except Exception as e:
		pass
	if configured:
		if len(v.appInfo['examples']) > 0:
			_printME_('Examples:')
			for ex in v.appInfo['examples']:
				_printME_('\t' + ex)
			_printME_('\n')
		if len(v.appInfo['columns']) > 0:
			_printME_('Columns and abbreviations:')
			result = ''
			for col in v.appInfo['columns']:
				result += col['name'] + '(' + col['abbreviation'] + '), '
			result = result[:-2]
			_printME_('\t' + result + '\n')
			# print('\n')
	switches.print()

	pass
	if 'a' in switches.values('Help') or 'all' in switches.values('Help'):
		_printME_('ALL:')
		for sw in switches.switches:
			_printME_( '\t', 't ', switches.switches[sw].switch.split(',')[0] )
			# for x in switches.switches[sw]:
			# print(x)
			# sys.exit()
	sys.exit()

####################################################################################################################################



####################################################################################################################################


























class LS:
	def __init__( self ): pass;
 
 



 
 

class BASHRC:
	def __init__( self ): pass;
 
 
 

class HASH:
	def __init__( self ): pass;
 
 
 






# C3PO_4life.4
########################################################################################
# switches.register('Help','--h')
switches.register('Help','?,??,-h,--h,/?,-?,/h,help,/help,-help,--help')
switches.register('---------','---------')
switches.register('Plus','+')
switches.register('Minus','-')
switches.register('PlusOr', '-or')
switches.register('PlusClose', '+close', '90%')
switches.register('PlusDuplicate', '+dup,+duplicate', '90%')
switches.register('StrictCase', '-strictcase')

switches.register('Column', '-c,-column', 'size, name')
switches.register('Sort','-s,-sort', 'Asc:type, Desc:ext')
switches.register('GroupBy', '-g,-group,-groupby', 'ext, month')
switches.register('WrapTable', '-wrap', 'n p  OR  2  OR  path')
switches.register('NoWrapTable', '-nowrap')
switches.register('FieldTotal', '-fieldtotal', 'mem_usage')
switches.register('Aggregate', '-aggregate', '" eof-field-len= add(len(version),len(backup)); config(var,eof,isFirst); "')
switches.register('GroupSpaces', '-gs,-space,-groupspaces')
switches.register('TableProfile', '-tp,-table',' *;c *;l  h;l header;left  size;l,gs')
switches.register('Long', '-l,-long')
switches.register('Short', '-sc,-short')
switches.register('Length', '-length','x3')
switches.register('--------','---------')
########################################################################################
# START
switches.register('Installer','-install')
switches.register('JSON-to-Var','-j2v,-json2var')
switches.register('Test-Import','-i,-imp,-import,-t')
switches.register('TEST','-test')

switches.register('SH-Files','-sh.f,-sh.fi,-sh.file,-sh.files')
switches.register('SH-Folders','-sh.fo,-sh.folder,-sh.folders')
switches.register('SH-Folder-Recursive','-sh.fo.r,-sh.folder.r')
# switches.register('SH-Auto-File','-sh.auto')

switches.register('Clean','--c')

switches.register('Header-Fix-File','-h.f,-h.fi,-header.fix.file')
switches.register('Header-Fix-Folder','-h.fo,-header.fix.folder')
switches.register('Header-Fix-Folder-Recursive','-h.fo.r,-header.fix.folder.r')

switches.register('Header-Read','-header.read')
switches.register('Bash-Vars','-bash.vars')

switches.register('Config-Alias','-config.alias')
switches.register('Config-Python','-config.py,-config.python')
switches.register('Config-Editor','-config.editor')
switches.register('Config-Skip-Keychain','-config.skip')
switches.register('Config-Python2','-config.py2,-config.python2')
switches.register('Config-Path','-config.path,-config.widgets,-config.drive,-config.tech')
# switches.register('Config-Editor','-config.editor')
switches.register('Config-Add','-config.add')
switches.register('Config-Remove','-config.remove')
switches.register('Config-Print','-config,-config.print')
switches.register('Config-Clean','-config.clean')

switches.register('Folder-Extensions','-ext.folder')
switches.register('Folder-Extensions-Recursive','-ext.folder.r')

switches.register('Download-Tool-Updates','-dl')

switches.register('URL-Requests','-url.get')
switches.register('URL-Requests-Save','-url.save')
switches.register('URL-WGET','-wget.url')

switches.register('App-m','-app.m')
switches.register('App-b','-app.b')
switches.register('App-bm-gen','-app.bm.gen,-app.bm.default')

switches.register('App-d','-app.d')

# switches.register('App-bashrc','-app.bashrc')
switches.register('App-ls','-app.ls')
switches.register('App-ago','-app.ago')
switches.register('App-which','-app.which')

switches.register('App-file','-app.file')
switches.register('App-files','-app.files')
switches.register('App-folder','-app.folder')
switches.register('App-folders','-app.folders')
switches.register('App-f-depth','-app.f.depth')

switches.register('App-Paths','-app.paths')
switches.register('App-Line','-app.line')
# switches.register('App-Line-Number','-app.line.n')

switches.register('Status-Online','-is.online,-ip,-online-is.o,-online,-o')

switches.register('is-Crypt','-is.crypt')
switches.register('is-Tar','-is.tar')
switches.register('is-Date','-is.date')

switches.register('.bashrc-Mini','-rc.m,-rc.mini,-bashrc.mini')
switches.register('.bashrc-Full','-rc.f,-rc.full,-bashrc.full,-bashrc')
switches.register('.bashrc-Default','-rc.d,-rc.def,-bashrc.def,-bashrc.default')
switches.register('File-Valid','-file.valid')

switches.register('File-3to2-3','-3to2.3')
switches.register('File-3to2-2','-3to2.2')

switches.register('Setting-PIPE-Clean','-setting.pipe.clean')
switches.register('Setting-PIPE-Print','-setting.pipe.print')

switches.register('Server-Utility-Port-PS','-u.p,-u.p.l,-util.port,-util.port.list')
switches.register('Server-Utility-Port-PS-Kill','-u.p.k,-util.port.kill')

switches.register('Folders-servers','-folders.servers')


switches.process()


pv=printVar
vp=printVar

# C3PO_4life.2



















# C3PO_4life.3

def action():

	sws = switches.statuses()
	if not sws.active:
		print_help()
	
	if switches.isActive('Installer'):
		vc.FIG.home()
		v.bash['widgets'] = vc.PATHS.path(__file__).split(os.sep+'install')[0]
		vc.FIG.v_bash_order()
		if not os.getcwd().endswith(os.sep+'install'):
			cp( 'Error, Please run from install folder', 'red' )
			sys.exit()
		vc.FIG.home()
		vc.FIG.v_bash_order()
		v.f.mkdir(v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'tables')
		v.f.mkdir(v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'temp')
		v.f.mkdir(v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'vars')
		vc.HD.saveText( '"', v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'vars'+os.sep+'quote.txt' )
		vc.HD.saveText( '%', v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'vars'+os.sep+'percentage.txt' )
		vc.HD.saveText( vc.FIG.uuid(), v.home+os.sep+'.rt'+os.sep+'profile'+os.sep+'vars'+os.sep+'instanceID.sys' )
		insta=vc.PATHS.path(__file__)
		# tool=v.home+os.sep+'.rt'+os.sep+'tool.py'
		tool=v.home+os.sep+'.rt'+os.sep+'tool'
		if os.path.isfile(tool):
			os.unlink(tool)
		from shutil import copyfile
		copyfile(insta,tool)


		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		v.bash['python'] = v.bash['ww']+os.sep+'python'
		v.bash['PY'] = sys.executable
		if v.isWin:
			v.bash['pip'] = os.path.dirname(sys.executable)+os.sep+'Scripts'+os.sep+'pip.exe'
			v.bash['pip3'] = os.path.dirname(sys.executable)+os.sep+'Scripts'+os.sep+'pip.exe'

		
		# else:
		#   if not 'widgets' in v.bash:
		#       v.bash['widgets'] = input( 'path? ' )


		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		vc.FIG.bash_vars()
		vc.FIG.bashrc(settings=['strip'])
		if v.isWin:
			cc_bat='''@echo off
call "%userprofile%\\.rt\\profile\\vars\\config.bat"
rem call "%widgets%\\widgets\\batch\\resetVars.bat"
call "%widgets%\\widgets\\batch\\c.bat" %1 
			'''
			# vc.HD.saveText( cc_bat, v.home+os.sep+'rt.bat' )
			vc.HD.saveText( cc_bat, v.home+os.sep+'rr.bat' )
			vc.HD.saveText( cc_bat, v.home+os.sep+'cc.bat' )
			A.ff.getFolders( v.bash['widgets']+'\\widgets\\powershell', r=False )
			_printME_()
			_printME_()
			_printME_()
			template='Set-Variable -Name "!VAR!" -Value "!PATH!" -Visibility Public'
			# template='New-Variable -Name "!VAR!" -Value "!PATH!" -Visibility Public'
			powershellVars=''
			for k in v.bash:
				vary=v.bash[k]
				vary=vary.replace('\\\\','\\')
				vary=vary.replace('"','')
				powershellVars+=template.replace('!VAR!',k).replace('!PATH!',vary)+'\n'
			# powershellVars+='Clear-Variable -Name "widgets"\n'
			for k in v.bash:
				vary=v.bash[k]
				vary=vary.replace('\\\\','\\')
				if '"' in vary:
					powershellVars+='$'+k+'='+vary+'\n'
				else:
					powershellVars+='$'+k+'="'+vary+'"\n'
			powershellVars+='Set-Variable -Name "widgets" -Value $tech_drive\n'
			powershellVars+='$widgets=$tech_drive\n'
			# powershellVars+='echo $widgets\n'
			# powershellVars+='echo $tech_drive\n'

			if os.path.isdir(v.home+'\\OneDrive\\Documents\\WindowsPowerShell'):
				too=v.home+'\\Documents\\'
				if not os.path.isfile(too+'backup.rt'):
					v.f.mkdir(too+'backup.rt')
				for path in A.ff.files:
					to=too+vc.PATHS.path(path,file=True)
					theFile = vc.HD.getText( path, raw=True )
					if os.path.isfile(to):
						me=str(os.path.getmtime( to ))
						bkPath=too+'backup.rt'+os.sep+me+'-'+vc.PATHS.path(to,file=True)
						vc.HD.saveText( theFile, bkPath )

					theFile = theFile.replace('# 3DF20E1B1A8A',powershellVars)
					vc.HD.saveText( theFile, to )
				cp( [ ':','installed powershell tools', v.home+'\\OneDrive\\Documents\\WindowsPowerShell' ], 'green' )
				_printME_( ':','which python3;     now works in powershell, widgets, etc' )
			elif os.path.isdir(v.home+'\\Documents\\WindowsPowerShell'):
				too=v.home+'\\Documents\\WindowsPowerShell\\'
				if not os.path.isfile(too+'backup.rt'):
					v.f.mkdir(too+'backup.rt')
				for path in A.ff.files:
					to=too+vc.PATHS.path(path,file=True)
					theFile = vc.HD.getText( path, raw=True )
					if os.path.isfile(to):
						me=str(os.path.getmtime( to ))
						bkPath=too+'backup.rt'+os.sep+me+'-'+vc.PATHS.path(to,file=True)
						vc.HD.saveText( theFile, bkPath )
					theFile = theFile.replace('# 3DF20E1B1A8A',powershellVars)
					vc.HD.saveText( theFile, to )
				cp( [ ':','installed powershell tools', v.home+'\\Documents\\WindowsPowerShell' ], 'green' )
				_printME_( ':','which python3;     now works in powershell, widgets, etc' )
		if os.path.isfile(v.home+os.sep+'.rt'+os.sep+'.config.hash'):
			try:
				os.system(v.bash['code_editor'] +' '+ v.home+os.sep+'.rt'+os.sep+'.config.hash')
			except Exception as e:
				pass
		if not v.isWin:
			switches.updateSwitchField( 'SH-Folder-Recursive', 'active', True )
			vc.SH.getFolderSH(v.bash['ww'])
		# pv(v.bash)

		# 'Installer'
		return None

	if switches.isActive('Setting-PIPE-Print'):
		for x in v.pipe:
			_printME_(x)
		if switches.values('Setting-PIPE-Print'):
			return None

	if switches.isActive('Header-Read'):
		for path in switches.values('Header-Read'):
			isB = vc.IS.isBin(path)
			if isB:
				w = 'bin'
			else:
				w = 'text'
			cp( [ w ], 'cyan' )

			if not isB:
				head = vc.HD.headTXT(path,32)
				phead = ''
				for x in head:
					# print(x,ord(x))
					if x == '/n' or x == chr(10) or x == '\r':
						break
					phead+=x
				_printME_(phead)
			else:
				head = vc.HD.head(path)
				# x = ''.join([chr(int(''.join(c), 16)) for c in zip(head[0::2],head[1::2])])
				resolved = vc.HD.asciiHeaderRun( head )
				_printME_( resolved['hex'] )
				_printME_( resolved['ascii'] )
				# print( isB )

		return None
	if switches.isActive('SH-Folders') or switches.isActive('SH-Folder-Recursive'):
		if switches.isActive('SH-Folders'):
			items = switches.values('SH-Folders')
		if switches.isActive('SH-Folder-Recursive'):
			items = switches.values('SH-Folder-Recursive')
		if not items:
			items.append(os.getcwd())
		for folder in items:
			vc.SH.getFolderSH(folder)
	if switches.isActive('SH-Files'):
		for path in switches.values('SH-Files'):
			try:
				path = os.path.abspath(path)
			except Exception as e:
				pass
			# print(path)
			vc.SH.processSHfile(path)
			
	if switches.isActive('Test-Import'):
		for imp in switches.values('Test-Import'):
			testImport(imp)
		return None
	if switches.isActive('JSON-to-Var'):
		if switches.values('JSON-to-Var') == []:
			asdf = """
example: ~/.rt/.config.hash

{
	"widgets": "/home/ximlickficfp/cloud/files",
	"PY": "/home/ximlickficfp/.local/bin/python3",
	"code_editor": "code-oss"
}
				"""
			pass
			_printME_(asdf)


		else: 
			items = []
			for file in switches.values('JSON-to-Var'):
				if os.path.isfile(file):
					table = vc.HD.getTableSimp( file )
					items.append('\n')
					for key in table:
						if table[key] and not key == 'CAT' and not key == 'SHELL':
							if v.isWin:

								items.append( 'set '+cl(key)+'='+table[key]+'\n' )
							else:
								items.append( 'export '+cl(key)+'='+table[key]+'\n' )
					items.append('\n')
					_printME_( ''.join(items) )
		return None
	if switches.isActive('Header-Fix'):
		vc.FIG.home()
		_printME_( v.home )
		return None
	if switches.isActive('Bash-Vars'):
		vc.FIG.bash_vars()
		return None
	if switches.isActive('Config-Alias'):
		vc.FIG.home()
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		if v.pipe:
			v.bash['hAlias'] = ''.join(v.pipe)
		else:
			v.bash['hAlias'] = switches.values('Config-Alias')[0]
		
		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	if switches.isActive('Config-Skip-Keychain'):
		vc.FIG.home()
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		v.bash['skip_chain'] = 'true'
		vc.FIG.v_bash_order()
		if 'r' in switches.values('Config-Skip-Keychain'):
			del v.bash['skip_chain']
		if 'remove' in switches.values('Config-Skip-Keychain'):
			del v.bash['skip_chain']
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		elif os.path.isfile(v.config):
			os.unlink(v.config)
			
		if not os.path.isfile(v.config):
			_printME_( {} )
			return None

		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	if switches.isActive('Config-Editor'):
		vc.FIG.home()
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		if v.pipe:
			v.bash['code_editor'] = ''.join(v.pipe)
			# v.bash['n'] = ''.join(v.pipe)
		else:
			v.bash['code_editor'] = ' '.join(switches.values('Config-Editor'))
			# v.bash['n'] = ' '.join(switches.values('Config-Editor'))
		if 'n' in v.bash:
			del v.bash['n']
		if 'n2' in v.bash:
			del v.bash['n2']
		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None
	if switches.isActive('Config-Python'):
		vc.FIG.home()
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		if v.pipe:
			v.bash['PY'] = ''.join(v.pipe)
		else:
			v.bash['PY'] = ' '.join(switches.values('Config-Python'))

		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	if switches.isActive('Config-Python2'):
		vc.FIG.home()
		
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		if v.pipe:
			v.bash['PY2'] = ''.join(v.pipe)
		else:
			v.bash['PY2'] = ' '.join(switches.values('Config-Python2'))
		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	if switches.isActive('Config-Path'):
		vc.FIG.home()
		
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		if v.pipe:
			v.bash['widgets'] = ''.join(v.pipe)
		else:
			v.bash['widgets'] = ' '.join(switches.values('Config-Path'))
		vc.FIG.v_bash_order()
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	# if switches.isActive('Config-Editor'):
	#   vc.FIG.home()
		
	#   if os.path.isfile( v.config ):
	#       v.bash = vc.HD.getTableSimp( v.config )
	#   if v.pipe:
	#       v.bash['code_editor'] = ''.join(v.pipe)
	#       v.bash['n'] = ''.join(v.pipe)
	#   else:
	#       v.bash['code_editor'] = ' '.join(switches.values('Config-Editor'))
	#       v.bash['n'] = ' '.join(switches.values('Config-Editor'))
	#   vc.FIG.v_bash_order()
	#   if v.bash:
	#       vc.HD.saveTableSimp( v.bash, v.config )
	#   test = vc.HD.getText( v.config, raw=True )
	#   print( test )
	#   if os.path.isfile(v.config):
	#       cp( pp(v.config) , 'cyan' )
	#   else:
	#       cp( pp(v.config) , 'red' )
	#   return None

	if switches.isActive('Config-Add'):
		vc.FIG.home()
		
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		for add in switches.values('Config-Add'):
			if ':' in add:
				add = add.replace(':',';')
			parts = add.split(';')
			if len(parts) > 1:
				v.bash[parts[0]] = parts[1]
		# print(v.bash)
		vc.FIG.v_bash_order()
		# print(v.bash)
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None


	if switches.isActive('Config-Remove'):
		vc.FIG.home()
		
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		for remove in switches.values('Config-Remove'):
			if remove in v.bash:
				del v.bash[remove]
		vc.FIG.v_bash_order()
		if not v.bash and os.path.isfile(v.config):
			os.unlink( v.config )

		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		if os.path.isfile(v.config):
			test = vc.HD.getText( v.config, raw=True )
			_printME_( test )
		else:
			_printME_('{}')
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None

	if switches.isActive('Config-Print'):
		vc.FIG.home()

		cp( 'example:', 'yellow' )
		printDic( v.bash_defaults )

		_printME_('________________________')
		cp( 'config file:', 'yellow' )
		if os.path.isfile(v.config):
			test = vc.HD.getText( v.config, raw=True )
			_printME_( test )
		else:
			_printME_('{}')
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		_printME_('________________________')
		
		cp( 'live:', 'yellow' )
		vc.FIG.bash_vars(p=0)
		printDic( v.bash )
		return None


	if switches.isActive('Config-Clean'):
		# print('here')
		vc.FIG.home()
		
		if os.path.isfile( v.config ):
			v.bash = vc.HD.getTableSimp( v.config )
		# print(v.bash)
		vc.FIG.v_bash_order()
		# print(v.bash)
		if v.bash:
			vc.HD.saveTableSimp( v.bash, v.config )
		test = vc.HD.getText( v.config, raw=True )
		_printME_( test )
		if os.path.isfile(v.config):
			cp( pp(v.config) , 'cyan' )
		else:
			cp( pp(v.config) , 'red' )
		return None


	if switches.isActive('Header-Fix-File'):
		vc.FIG.bash_vars(p=0)
		for path in switches.values('Header-Fix-File'):
			vc.HEAD.bashFileHeader(path)
		return None

	if switches.isActive('Header-Fix-Folder') or switches.isActive('Header-Fix-Folder-Recursive'):
		vc.FIG.bash_vars(p=0)
		if switches.isActive('Header-Fix-Folder'):
			items = switches.values('Header-Fix-Folder')
		if switches.isActive('Header-Fix-Folder-Recursive'):
			items = switches.values('Header-Fix-Folder-Recursive')
		if not items:
			items.append(os.getcwd())
		for path in items:
			vc.HEAD.getFolderBH(path)
		return None

	if switches.isActive('Folder-Extensions') or switches.isActive('Folder-Extensions-Recursive'):
		try:
			from operator import itemgetter
		except Exception as e:
			_printME_( 'missing operator' )
		vc.FIG.bash_vars(p=0)
		if switches.isActive('Folder-Extensions'):
			items = switches.values('Folder-Extensions')
		if switches.isActive('Folder-Extensions-Recursive'):
			items = switches.values('Folder-Extensions-Recursive')
		if not items:
			items.append(os.getcwd())
		v.ext = {}
		for path in items:
			vc.EXT.getFolderEXT(path)
		exData = []
		for key in v.ext:
			exData.append({ 'ext': key, 'cnt': v.ext[key]})
		v.exData = sorted(exData, key=itemgetter('cnt'))
		for rec in v.exData:
			_printME_( rec['ext'], rec['cnt'] )
		return v.exData

	if switches.isActive('Download-Tool-Updates'):
		vc.ONLINE.download_updates()
		return None

	if switches.isActive('URL-Requests'):
		url = switches.values('URL-Requests')[0]
		page_code = vc.ONLINE.page(url)
		if not switches.isActive('URL-Requests-Save'):
			_printME_( page_code )
		if switches.isActive('URL-Requests-Save'):
			vc.HD.saveText( page_code, switches.values('URL-Requests-Save')[0] )
		return None

	if switches.isActive('URL-WGET') and switches.isActive('URL-WGET-Save'):
		try:
			import wget
		except Exception as e:
			_printME_('missing wget')
			return None
		url = switches.values('URL-WGET')[0]
		s = switches.values('URL-WGET_Save')[0]
		wget.download(url, s)
		return None

	if switches.isActive('App-file'):
		items = switches.values('App-file')
		if not items:
			items.append(os.getcwd())
		A.ff.getFolders( items, r=False )
		for file in A.ff.files:
			cp( file, 'cyan')
		return None
	if switches.isActive('App-files'):
		items = switches.values('App-files')
		if not items:
			items.append(os.getcwd())
		A.ff.getFolders( items, r=True )
		for file in A.ff.files:
			cp( file, 'cyan')
		return None
	if switches.isActive('App-folder'):
		items = switches.values('App-folder')
		if not items:
			items.append(os.getcwd())
		A.ff.getFolders( items, r=False )
		for folder in A.ff.folders:
			cp( folder, 'cyan')
		return None

	if switches.isActive('App-folders'):
		items = switches.values('App-folders')
		if not items:
			items.append(os.getcwd())
		A.ff.getFolders( items, r=True )
		for folder in A.ff.folders:
			cp( folder, 'cyan')
		return None
	if switches.isActive('App-d'):
		items = switches.values('App-folders')
		if not items:
			items.append(os.getcwd())
		A.ff.getFolders( items, r=False )
		cp( 'Files:', 'yellow' )
		for f in A.ff.files:
			ft = A.ff.files[f]
			if len(ft):
				cp( [ '\t', ft ], 'cyan' )
		_printME_()
		cp( 'Folders:', 'yellow' )
		for f in A.ff.folders:
			ft = A.ff.folders[f]
			if len(ft):
				cp( [ '\t', ft ], 'cyan' )

		# for folder in A.ff.folders:
		# cp( folder, 'cyan')
		return None
	if switches.isActive('Status-Online'):
		s = vc.ONLINE.status()
		if type(s) == bool:
			if s:
				prn = cp( 'online', 'green', p=0 ) +': '+ cp( vc.ONLINE.ip, 'yellow', p=0 )
				_printME_(prn)
			else:
				cp( 'offline', 'red' )
		else:
			if s is None:
				cp( 'no requests library', 'red' )
		return None


	if switches.isActive('is-Crypt'):
		items = switches.values('is-Crypt')
		c = 'red'
		for item in items:
			if vc.IS.isCrypt(item):
				prn = 'Y'
				c = 'green'
			else:
				prn = 'N'
				c = 'red'
			prn += ', '+item
			cp(prn,c)
		return None
	if switches.isActive('is-Tar'):
		items = switches.values('is-Tar')
		c = 'red'
		for item in items:
			if vc.IS.isGz(item) or vc.IS.isBz2(item):
				prn = 'Y'
				c = 'green'
			else:
				prn = 'N'
				c = 'red'
			prn += ', '+item
			cp(prn,c)
		return None


	if switches.isActive('is-Date'):
		items = switches.values('is-Date')
		if not items:
			items.append(time.time())
		for item in items:
			d = vc.DATE.isDate( item )
			pv(d)
		return None


	if switches.isActive('.bashrc-Mini'):
		vc.FIG.bashrc('mini',settings=switches.values('.bashrc-Mini'))
		vc.FIG.bash_vars()
		return None

	if switches.isActive('.bashrc-Default'):
		vc.FIG.bashrc(settings=switches.values('.bashrc-Default'))
		vc.FIG.bash_vars()
		return None

	if switches.isActive('.bashrc-Full'):
		vc.FIG.bashrc('full',settings=switches.values('.bashrc-Full'))
		vc.FIG.bash_vars()
		return None

	if switches.isActive('File-Valid'):
		for path in switches.values('File-Valid'):
			records = vc.HD.json(path)
			_printME_(records)
		return None


	if switches.isActive('App-m'):
		_bm = Bookmarks()
		for a in switches.values('App-m'):
			_bm.m(a)
		return None

	if switches.isActive('App-b'):
		_bm = Bookmarks()
		for a in switches.values('App-m'):
			b = _bm.b(a)
			_printME_(b)
		return None

	if switches.isActive('App-bm-gen'):
		_bm = Bookmarks()

		for item in vc.FIG.bm_default.split('\n'):
			a = item.split('|')[0]
			p = item.split('|')[1]
			_bm.m(a,p)
		return None


	if switches.isActive('App-Paths'):
		items = switches.values('App-Paths')
		if not items:
			items.append(os.getcwd())
		vc.PATHS.print_paths( items )
		return None

	if switches.isActive('File-3to2-3') or switches.isActive('File-3to2-2'):
		_3to2 = PY3TO2()
		_3to2.convert( switches.values('File-3to2-3'), switches.values('File-3to2-2') )
		return None

	if switches.isActive('App-Line'):
		for i,line in enumerate(v.pipe):
			if showLine(line):
				if switches.isActive('Clean'):
					_printME_(line)
				else:
					pad = len(str(v.pipe))
					_printME_(vc.STR.padZero( i, pad ),line)
		return None

	if switches.isActive('Server-Utility-Port-PS-Kill'):
		result = 'error'
		order = 'A'
		subjects = []
		for s in switches.values('Server-Utility-Port-PS-Kill'):
			
			if s == 'b':
				order = 'B'
			else:
				subjects.append(s)

		if not subjects and not order is None:
			subjects.append(order)
			order = None

		if order == 'A':
			if subdo('which fuser'):
				for subject in subjects:
					result = subdo('fuser -k xXx/tcp'.replace( 'xXx', subject ),p=2)
			elif subdo('which lsof'):
				for subject in subjects:
					result = subdo('kill -9 $(lsof -t -i:xXx)'.replace( 'xXx', subject ),p=2)
			else:
				e( 'missing: fuser and lsof' )
		elif order == 'B':
			if subdo('which lsof'):
				for subject in subjects:
					result = subdo('kill -9 $(lsof -t -i:xXx)'.replace( 'xXx', subject ),p=2)
			elif subdo('which fuser'):
				for subject in subjects:
					result = subdo('fuser -k xXx/tcp'.replace( 'xXx', subject ),p=2)
			else:
				e( 'missing: fuser and lsof' )

		return None


	if switches.isActive('Server-Utility-Port-PS'):
		result = 'error'
		order = 'A'
		subjects = []
		for s in switches.values('Server-Utility-Port-PS'):
			
			if s == 'b':
				order = 'B'
			else:
				subjects.append(s)

		if not subjects and not order is None:
			subjects.append(order)
			order = None

		if order == 'A':
			if subdo('which fuser'):
				for subject in subjects:
					result = subdo('fuser xXx/tcp'.replace( 'xXx', subject ),p=2)
			elif subdo('which lsof'):
					result = subdo('lsof -i:xXx'.replace( 'xXx', subject ),p=2)
			else:
				e( 'missing: fuser and lsof' )
		elif order == 'B':
			if subdo('which lsof'):
					result = subdo('lsof -i:xXx'.replace( 'xXx', subject ),p=2)
			elif subdo('which fuser'):
				for subject in subjects:
					result = subdo('fuser xXx/tcp'.replace( 'xXx', subject ),p=2)
			else:
				e( 'missing: fuser and lsof' )

		return None

	if switches.isActive('Folders-servers'):
		folders = """
/opt/rightthumb-widgets-v0/widgets/servers/socket
/opt/rightthumb-widgets-v0/widgets/servers/socket/linux
/opt/rightthumb-widgets-v0/widgets/servers/socket/smb
/opt/rightthumb-widgets-v0/widgets/servers/web
/opt/rightthumb-widgets-v0/widgets/servers/web/alphabet
/opt/rightthumb-widgets-v0/widgets/servers/web/alphabet/assets
/opt/rightthumb-widgets-v0/widgets/servers/web/alphabet/assets/js
/opt/rightthumb-widgets-v0/widgets/servers/web/alphabet/Docs
/opt/rightthumb-widgets-v0/widgets/servers/web/crud
/opt/rightthumb-widgets-v0/widgets/servers/web/DnD
/opt/rightthumb-widgets-v0/widgets/servers/web/js.devexpress
/opt/rightthumb-widgets-v0/widgets/servers/web/largeJsonTest
/opt/rightthumb-widgets-v0/widgets/servers/web/shell
/opt/rightthumb-widgets-v0/widgets/servers/web/vps
		"""
		vc.FIG.bash_vars(p=0)
		for line in folders.split('\n'):
			line = line.replace( ' ', '' )
			line = vc.STR.cleanBE( line, ' ' )
			line = vc.STR.cleanBE( line, '\r' )
			line = vc.STR.cleanBE( line, '\t' )
			if line:
				line = line.replace( '/opt/rightthumb-widgets-v0', v.bash['widgets'] )
				line = line.replace( '/', os.sep )
				v.f.mkdir(line)
		return None

	if switches.isActive('NEXT'):
		return None





tables = Tables()
if __name__ == '__main__':
	loader()
	action()
	vc.EXIT.isExit()

# wget https://bootstrap.pypa.io/pip/2.7/get-pip.py

# C3PO_4life.0

# genJson
# save_bashrc

# '.bashrc.full'
# '.bashrc-all'
# '.bashrc-auto'
# A.vfiles.file('.bashrc.full')['data']

# vc.PATHS.path
# vc.FIG.save_bashrc( code, o='455B6DCC5737', c='6198DDC12140' )
# self.isActive('Help')
# bin'
# alias t2="installer.py2";
# bashFileHeader
# sys.executable
# del v.bash['profile']

# vc.FIG.bash_vars(p=0)
# 'Installer'

# /etc/bash.bashrc
# unalias v
# unalias v

# it exit if scp or similar 4f8c
## .bashrc.mini
# bashrc bof 82977d555926
# bashrc eof a3bc42ec51e9