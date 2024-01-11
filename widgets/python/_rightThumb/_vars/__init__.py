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

#b)--> legacy registration system
config_hash_default = {
							'register.php': 'http://tools.rightthumb.com/register.php',
							'ip.php': 'http://tools.rightthumb.com/ip.php',
}
#n)--> DISABLED
__register_php=False
__ip_php=False
#e)--> legacy registration system

import _rightThumb._construct as __
import _rightThumb._string as _str
from pathlib import Path
import os
import sys
import platform
import time
simplejson = None
class dot:
	def __init__( self ):
		pass
config_default = dot()
config_default.cloud = dot()
config_default.cloud.ssh = dot()
config_default.cloud.ssh.password = 'v2SUI1UMn7Q2xF3DJmoJZuB+rgBesCSA'
config_default_dic = {}
config_default_dic['cloud-ssh-pass'] = config_default.cloud.ssh.password
configFile_data = {}
def dics(*arg):
	dic = {}
	for table in arg:
		for k in table:
			dic[k] = table[k]
	return dic


def path_fix(path):
	path=path.replace('/',os.sep).replace('\\',os.sep)
	path=_str.do('dup',path,os.sep)
	return path

def configFile( item=None, value=None, p=True ):
	global simplejson
	try:
		global configFile_data
		if item is None:
			if p:
				if not simplejson is None:
					import simplejson
				dataDump = simplejson.dumps(configFile_data, indent=4, sort_keys=False)
				_.pr(dataDump)
			return configFile_data
		if value is None:
			if item in configFile_data:
				return configFile_data[item]
			else:
				_.pr( 'Error: configFile', item, 'value not set' )
		elif not value is None:
			configFile_data[item] = value
			return value
	except Exception as e:
		pass
# import _rightThumb._base3 as _
# import md5
# _v.generateFunctionLogFilename( filename )
# _v.myDatabases
# _v.bookmarkFormat
# _v.myTables
# _v.myAppsJs
# _v.chromedriver
# _v.myTemp+slash+
# base_import
# import_delim
# base_versions
# baseFolderVersions
def genUUID(x=False):
	import uuid
	string = uuid.uuid4()
	string = str(string)
	if x:
		string = string.upper()
	else:
		string = '{' + string.upper() + '}'
	if x:
		try:
			random
		except Exception as e:
			import random
		string = string.replace('-','')
		x = []
		for y in string:
			ran = random.randint(0,20)
			if ran % 2 == 0:
				x.append( y.lower() )
			else:
				x.append( y.upper() )
		string = ''.join(x)
	return string
# unixID
folderID_tech      = '{A8693D4B-8A80-898F-83F0-E806D2F36800}'
folderID_profile   = '{6FAB5628-94A1-410A-82D1-1D42A2A11750}'
folderID_host      = '{C12F266D-71B9-40D2-98B9-424B42D2DBAC}'
folderID_techApps  = '{D53E69A0-5663-4D19-B0A8-817F0AECBF9C}'
folderID_alt       = '{BCAE64F2-C911-4F04-AF8C-DFE052E60973}'
folder_alt = '(profile)Downloads'
windowsSlash = chr(92)
unixSlash = chr(47)
slashes = {
				'w': windowsSlash,
				
				'o': unixSlash,
				
				'u': unixSlash,
				'l': unixSlash,
				
				'a': unixSlash,
				'm': unixSlash,
				'd': unixSlash,
				
				'windows': windowsSlash,
				
				'other': unixSlash,
				'unix': unixSlash,
				'linux': unixSlash,
				
				'apple': unixSlash,
				'mac': unixSlash,
				'macOS': unixSlash,
				'darwin': unixSlash,
}
s = slashes
if __.isWin:
	slash = slashes['windows']
	dDim = ':'
elif not __.isWin:
	slash = slashes['unix']
	dDim = ''
import_delim = 'VX'
base_import = 'import _rightThumb._base'+import_delim+' as _'
base_template = '_base'+import_delim+'_init_example.py'
base_file = '_rightThumb'+slash+'_base'+import_delim+slash+'__init__.py'
py_examples = 'py_base'+import_delim+'_examples.json'
def base_versions():
	data = []
	data.append('')
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for x in range(0,10):
		data.append( str(x) )
		for y in alpha:
			data.append( str(x)+y )
	# print('_v.base_versions',data)
	return data
def cmdSetVar( n, v ):
	os.environ[n.upper()] = v
def cmdGetVar( n ):
	return os.getenv( n.upper() )

if __.isWin:
	profileTMP = cmdGetVar('userprofile') + slash+'_AppShareTemp'
elif not __.isWin:
	profileTMP = cmdGetVar('HOME') + slash+'_AppShareTemp'

home = ''
if __.isWin:
	home = cmdGetVar('USERPROFILE')
if not __.isWin:
	try:
		home = cmdGetVar('HOME')
	except Exception as e:
		pass
	if not home:
		try:
			home = str(Path.home())
		except Exception as e:
			pass
	if not home:
		if not __.isWin:
			home = '~'
# _.pr( 'home:',home )
if __.isWin:
	computername = os.getenv('COMPUTERNAME')
	userprofile = os.getenv('USERPROFILE')
elif not __.isWin:
	import socket
	computername = socket.gethostname()
	userprofile = os.getenv('HOME')
# user = os.getlogin()
downloads = userprofile + slash+'Downloads'
computername2 = computername.replace(' ','_')
# inputScriptDriveFile = php_drive.txt
td = dot() 
td.a = dot()
td.b = dot()
td.c = dot()

configFile( '.path', home  +os.sep+'.rt'+os.sep+  '.path' )
configFile( '.config.hash', home +os.sep+'.rt'+os.sep+ '.config.hash' )

# _.pr('techDrive',techDrive)
configFile( '.path', home  +os.sep+'.rt'+os.sep+  '.path' )
configFile( '.config.hash', home +os.sep+'.rt'+os.sep+ '.config.hash' )
if os.path.isfile( configFile('.path') ):
	techDrive_test = open( configFile('.path')  , 'r').read().replace('\n','').replace('\r','').replace('\t','')
	if os.path.isdir(techDrive_test):
		techDrive = techDrive_test
	del techDrive_test
config_hash = {}
if os.path.isfile( configFile('.config.hash') ):
	config_hash = __.getTable( configFile('.config.hash') )
	for k in config_hash_default:
		if not k in config_hash: config_hash[k]=config_hash_default[k];
	if 'w' in config_hash:
		if __.isWin:
			techDrive = config_hash['w']
			# techDrive = techDrive.replace(':','')
		if not __.isWin:
			if os.path.isdir(config_hash['w']):
				techDrive = config_hash['w']
	if 'path' in config_hash:
		if __.isWin:
			techDrive = config_hash['path']
			# techDrive = techDrive.replace(':','')
		if not __.isWin:
			if os.path.isdir(config_hash['path']):
				techDrive = config_hash['path']

me = os.path.abspath(__file__)
mep = me.split(os.sep)
mep.reverse()
mep.pop(0)
mep.pop(0)
mep.pop(0)
mep.pop(0)
mep.pop(0)
mep.reverse()
techDrive = os.sep.join(mep)
del me
del mep
config_default.path = techDrive
config_default_dic['w'] = techDrive
config_default_dic['widgets'] = techDrive
config_default_dic['tech_drive'] = techDrive
config_default_dic['techDrive'] = techDrive
config_default_dic['path'] = techDrive
try:
	configFile( '.host', techDrive+'/.host' )
except Exception as e:
	pass
try:
	if not __.isWin:
		if not os.path.isfile(configFile('.host')):
			open( configFile('.host') ,'w', encoding='utf-8').write( computername2 )
except Exception as e:
	pass
techDrive = techDrive.replace('\t','')
techDrive = techDrive.replace('\r','')
techDrive = techDrive.replace('\n','')
techDrive = _str.cleanBE(techDrive,' ')
if techDrive.endswith(os.sep):
	techDrive = techDrive[:-1]
techDrive = _str.cleanBE(techDrive,' ')
td.path = techDrive
drive=techDrive

if __.isWin:
	# fileName = home + slash+'.tk421'
	fileName = home + slash+'.tk421'
	# if not os.path.isfile( fileName ):
	#     open(fileName,'w', encoding='utf-8').write('C:\\.rightthumb-widgets')
	# techDrive = open( fileName, 'r' ).read()
	# techDrive = techDrive
	# _.pr('techDrive',techDrive)
	if '\n' in techDrive or '\r' in techDrive:
		if os.path.isfile( fileName ):
			techDrive = techDrive.replace('\n','').replace('\r','')
			techDrive = techDrive.replace('\n','').replace('\r','')
			techDrive = techDrive.replace('\n','').replace('\r','')
			open(fileName,'w', encoding='utf-8').write( techDrive )
w=techDrive
# elif not __.isWin:
#     techDrive = '/opt/RightThumb'
#     try:
#         if not os.path.isdir(techDrive):
#             os.mkdir(techDrive)
#     except Exception as e:
#         if os.path.isdir('/home/ximlickficfp/cloud/files'):
#             techDrive = '/home/ximlickficfp/cloud/files'
	# fileName = home + slash+'.tk421'
	# fileNameHost = home + slash+'.ncc1701'
	# fileName = fileName.replace( slashes['windows'], slash )
	# if not os.path.isfile( fileNameHost ):
	#     open(fileNameHost,'w', encoding='utf-8').write(computername)
	# if not os.path.isfile( fileName ):
	#     open(fileName,'w', encoding='utf-8').write(home)
	# techDrive = open( fileName, 'r' ).read()
def ddDim(xyz):
	return xyz
	global dDim
	if not dDim:
		return xyz
	if not dDim in xyz:
		return xyz+dDim
techFolder =  ddDim(techDrive)
# _.pr('techFolder:',techFolder)
# sys.exit()
appsFolder =  ddDim(techDrive) +slash+'techApps'
archive7z =  ddDim(techDrive) +slash+'archive_7z_files'
widgets = techFolder
programs=widgets
pp  = techFolder + slash+'widgets'
w   = techFolder 
ww  = techFolder +slash+ 'widgets'
ads = ww +slash+ 'ads'
appProfiles = widgets+os.sep+'widgets'+ slash+'python'+slash+'profiles'
compiled = widgets+os.sep+'widgets'+ slash+'compiled'
documentation = widgets+os.sep+'widgets'+ slash+'documentation'
project = widgets+os.sep+'widgets'+ slash+'project'
updates = project + slash+'updates'
images = techFolder + slash+'widgets'+slash+'project'+slash+'img'+slash
# log_config = techFolder + slash+'widgets'+slash+'project'+slash+'log_config'+slash+'log_data.js'
log_config = techFolder + slash+'widgets'+slash+'html'+slash+'projects'+slash+'log_config'+slash+'log_data.js'
# log_config_html = techFolder + slash+'widgets'+slash+'project'+slash+'log_config'+slash+'index.htm'
log_config_html = techFolder + slash+'widgets'+slash+'html'+slash+'projects'+slash+'log_config'+slash+'index.htm'
dance = images + 'dance.gif'
gears = images + 'gears.gif'
life=home +os.sep+'.rt'+os.sep+'profile'+os.sep+'life'+os.sep
rtp=home +os.sep+'.rt'+os.sep+'profile'+os.sep
rt=home +os.sep+'.rt'



if __.isWin:
	# sublime = '"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"'
	sublime = '"C:\\Program Files\\Microsoft VS Code\\Code.exe"'
elif not __.isWin:
	if os.path.isfile('/opt/sublime/sublime_text'):
		sublime = '/opt/sublime/sublime_text'
	elif os.path.isfile('/usr/bin/sublime_text'):
		sublime = '/usr/bin/sublime_text'
	elif os.path.isfile('/usr/bin/code-oss'):
		sublime = '/usr/bin/code-oss'
	else:
		sublime = '/usr/bin/nano'
# _v.sublime
# scriptsFolder =  techFolder + slash+'scripts'
# thisHost =  'hosts' + slash + computername2
# myHome =  techFolder + slash+'hosts' + slash + computername2
myHome =  home+os.sep+'.rt'+os.sep+'profile'
# _.pr('myHome',myHome)
thisHost =  myHome
# myHome =  home +slash+ 'profile'
# thisHost =  myHome
dataFolder = techFolder + slash+'data'
myIndexes = myHome + slash+'indexes'
quickIndex = myIndexes + slash+'0A{465C1A34-D22F-184E-F713-F8E5149E212D}'
myTables = myHome + slash+'tables'
duckDuckGo = myTables + slash+'DuckDuckGo'
relevant_folders = myTables + slash+'relevantFolders.txt'
myWebApp = myHome + slash+'/widgets/servers/web/crud'
myBackup = myHome + slash+'backup'
myLogs = myHome + slash+'logs'
myConfig = myHome + slash+'config'
unixID_path = myConfig + slash + '.unix_id'
vault_path = myConfig + slash + '.vault'



configFile( '.ip.hash', myConfig + slash + '.ip.hash' )
configFile( '.ip', myConfig + slash + '.ip' )
# unix_editor_path = myConfig + slash + '.editor'
if os.path.isfile( myConfig + os.sep + '.terminal-copy' ):
	terminal_copy = True
else:
	terminal_copy = False
isTerminal = True
isGUI = False
try:
	if len( os.getenv('HOMEXDG_CURRENT_DESKTOP') ) > 1:
		isGUI = True
		isTerminal = False
except Exception as e:
	pass
try:
	if len( os.getenv('GDMSESSION') ) > 1:
		isGUI = True
		isTerminal = False
except Exception as e:
	pass
configFile( '.distro', myConfig + slash + '.distro' )
configFile( '.alias', myConfig + slash + '.alias' )
 
host_alias = computername2
if os.path.isfile(configFile('.alias')):
	host_alias = open( configFile('.alias'), 'r' ).read()
if host_alias.startswith('client_ '):
	isClient = True
else:
	isClient = False
if __.isWin:
	unix_editor_path = home + slash+'.tk421_editor'
else:
	unix_editor_path = techDrive + slash+'.editor'
	unix_editor_path_sufix = techDrive + slash+'.editor.sufix'
	# _.pr(unix_editor_path)
if not __.isWin:
	unix_editor_edit = ''
	if os.path.isfile(unix_editor_path_sufix):
		unix_editor_edit = open( unix_editor_path_sufix, 'r' ).read()
	if os.path.isfile(unix_editor_path):
		unix_editor = open( unix_editor_path, 'r' ).read()
	else:
		find_unix_editor = [
				'/snap/bin/subl',
				'/usr/bin/sublime_text',
				'/usr/bin/subl',
				'/opt/sublime/subl',
				'/opt/sublime/sublime_text',
				'/usr/bin/code-oss',
				'/usr/share/code/code',
				'/usr/share/code',
				'/usr/bin/code/code',
				'/usr/bin/code',
				"/usr/bin/brackets",
				'/usr/bin/bluefish',
				'/usr/bin/notepad++',
				"/usr/bin/acme",
				"/usr/bin/akelpad",
				"/usr/bin/alphatk",
				"/usr/bin/arachnophilia",
				"/usr/bin/bbedit",
				"/usr/bin/bbedit",
				"/usr/bin/codewright",
				"/usr/bin/crimson",
				"/usr/bin/cudatext",
				"/usr/bin/cygnused",
				"/usr/bin/eddie",
				"/usr/bin/emeditor",
				"/usr/bin/epsilon",
				"/usr/bin/featherpad",
				"/usr/bin/golded",
				"/usr/bin/html_kit",
				"/usr/bin/hxd",
				"/usr/bin/jedit",
				"/usr/bin/jove",
				"/usr/bin/juffed",
				"/usr/bin/kedit",
				"/usr/bin/kile",
				"/usr/bin/komodo",
				"/usr/bin/lapis",
				"/usr/bin/leafpad",
				"/usr/bin/leo",
				"/usr/bin/mcedit",
				"/usr/bin/metapad",
				"/usr/bin/microemacs",
				"/usr/bin/mousepad",
				"/usr/bin/multi-edit",
				"/usr/bin/nedit",
				"/usr/bin/notepad",
				"/usr/bin/notepad2",
				"/usr/bin/notetab",
				"/usr/bin/pe",
				"/usr/bin/pluma",
				"/usr/bin/polyedit",
				"/usr/bin/pfe",
				"/usr/bin/pspad",
				"/usr/bin/q10",
				"/usr/bin/rj",
				"/usr/bin/sam",
				"/usr/bin/scite",
				"/usr/bin/simpletext",
				"/usr/bin/slickedit",
				"/usr/bin/smultron",
				"/usr/bin/subethaedit",
				"/usr/bin/hydra",
				"/usr/bin/teachtext",
				"/usr/bin/ted",
				"/usr/bin/tex-edit",
				"/usr/bin/textpad",
				"/usr/bin/wildedit",
				"/usr/bin/texniccenter",
				"/usr/bin/texshop",
				"/usr/bin/textedit",
				"/usr/bin/textmate",
				"/usr/bin/textwrangler",
				"/usr/bin/topstyle",
				"/usr/bin/ultraedit",
				"/usr/bin/ulysses",
				"/usr/bin/vedit",
				"/usr/bin/winedt",
				"/usr/bin/x11",
				"/usr/bin/xedit",
				"/usr/bin/yudit",
				'/usr/bin/vscode',
				'/usr/bin/lighttable',
				'/usr/bin/gedit',
				'/usr/bin/kakoune',
				'/usr/bin/brackets ',
				
				'/usr/bin/limetext ',
				'/usr/bin/leafpad ',
				
				'/usr/bin/atom',
				'/usr/bin/pico',
				'/usr/bin/nano',
				'/usr/bin/kwrite',
				'/usr/bin/kate',
				'/usr/bin/geany',
				'/usr/bin/medit',
				'/usr/bin/neovim',
				'/usr/bin/jed',
				'/usr/bin/micro',
				'/usr/bin/gvim',
				'/usr/bin/vim',
				'/usr/bin/vi'
		]
		try:
			for tep in find_unix_editor:
				if os.path.isfile(tep):
					unix_editor = tep
					open(unix_editor_path,'w', encoding='utf-8').write( tep )
					break
		except Exception as e:
			pass
if __.isWin: sublime = '"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"'
unixID = None
unixIDs = []
unixID_NEW = False
def gen_unixIDs():
	global unixID
	global unixIDs
	global unixID_NEW
	if os.path.isfile(unixID_path):
		try:
			f = open(unixID_path, 'r', encoding='utf-8')
			unixIDs = []
			for x in f.readlines():
				unixIDs.append(x.replace('\n',''))
			unixID = unixIDs[0]
			f.close()
		except Exception as e:
			pass
	else:
		unixID = genUUID(x=True)
		unixIDs = unixID+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)+'\n'+genUUID(x=True)
		unixID_NEW = True
	return unixIDs
gen_unixIDs()
if not '/bash/' in __file__:
	try:
		if '-' in unixIDs[8]:
			os.unlink(unixID_path)
			if os.path.isfile(vault_path):
				os.unlink(vault_path)
			gen_unixIDs()
	except Exception as e:
		if os.path.isfile(unixID_path):
			os.unlink(unixID_path)
		if os.path.isfile(vault_path):
			os.unlink(vault_path)
		gen_unixIDs()
research = techFolder + slash+'widgets'+slash+'databank'
myDatabank = research
keys = techFolder + slash+'widgets'+slash+'keys'
data = research
databank = research
python = {
			'crypt': {
						'en': widgets+os.sep+'widgets'+ slash+'python'+slash+'crypt'+slash+'en',
						'de': widgets+os.sep+'widgets'+ slash+'python'+slash+'crypt'+slash+'de',
			},
			'imploded': {
						'windows': widgets+os.sep+'widgets'+ slash+'python'+slash+'imploded'+slash+'unity',
						'unix': widgets+os.sep+'widgets'+ slash+'python'+slash+'imploded'+slash+'unity',
						'this': None,
			},
			'src': {
						'windows': widgets+os.sep+'widgets'+ slash+'python'+slash+'src'+slash+'unity',
						'unix': widgets+os.sep+'widgets'+ slash+'python'+slash+'src'+slash+'unity',
						'this': None,
			},
			'compiled': {
						'windows': widgets+os.sep+'widgets'+ slash+'python'+slash+'compiled'+slash+'unity',
						'unix': widgets+os.sep+'widgets'+ slash+'python'+slash+'compiled'+slash+'unity',
						'this': None,
			},
			'burn': {
						'windows': widgets+os.sep+'widgets'+ slash+'python'+slash+'burn'+slash+'unity',
						'unix': widgets+os.sep+'widgets'+ slash+'python'+slash+'burn'+slash+'unity',
						'this': None,
			},
}

py = widgets+os.sep+'widgets'+ slash+'python'

  
folder_alt = folder_alt.replace( '(profile)', userprofile + slash )
UNC = { 'en': {}, 'de': {} }
UNC['de'][folderID_techApps] = appsFolder
UNC['de'][folderID_host] = myHome
UNC['de'][folderID_tech] = techFolder
UNC['de'][folderID_profile] = userprofile
UNC['de'][folderID_alt] = folder_alt
UNC['en'][appsFolder] = folderID_techApps
UNC['en'][myHome] = folderID_host
UNC['en'][techFolder] = folderID_tech
UNC['en'][userprofile] = folderID_profile
UNC['en'][folder_alt] = folderID_alt
UNC['en']['alt'] = folderID_alt
dbTables = databank + slash+'tables'
tablesDB = dbTables
databases = databank + slash+'databases'
db = databank 
dbs = databank + slash+'databases'
dbdbs = databank + slash+'databases'
myBatch = myHome + slash+'widgets'+slash+'batch'
myTXT = myBackup + slash+'txt'
myBIN = myBackup + slash+'bin'
webapp = techFolder +os.sep+ os.sep.join( 'widgets/servers/web/crud'.split('/') )

library = techFolder + slash+'widgets'+slash+'library'
myDatabases = myHome + slash+'databases'
myVars = myHome + slash+'vars'
terminal = myHome + slash+'vars'+slash+'terminal'+slash
try:
	terminal_variables = terminal+os.getenv('Session_ID')
	# terminal_variables = terminal+os.environ['Session_ID']
	tvy=terminal_variables+'.yml'
	# print('has Session_ID')
except:
	pass
	# print('no Session_ID')
	

myNotes = myHome + slash+'notes'
umlJson = myHome + slash+'json-uml-tree'+slash+'data.js'
umlHtml = myHome + slash+'json-uml-tree'+slash+'index.htm'
androidMaster = 'android_apps_master.json'
androidMasterFull = myTables + slash + androidMaster
myApps = techFolder + slash+'widgets'
ipsum = myApps + slash+'project'+slash+'ipsum.txt'
myAppsJs = myApps + slash+'javascript'
myAppsBatch = myApps + slash+'batch'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'2.46'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'73.0.3683.68'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'74.0.3729.6'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'75.0.3770.90'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'76.0.3809.25'+slash+'chromedriver.exe'
if __.isWin:
	# D:\.rightthumb-widgets\widgets\exe\ChromeDriver\80.0.3987.16\chromedriver.exe
	chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'80.0.3987.16'+slash+'chromedriver.exe'
	geckodriver = myApps + slash+'exe'+slash+'gecko'+slash+'0.24.0'+slash+'geckodriver.exe'
	chromePortable = appsFolder + slash+'chrome-win'+slash+'chrome.exe'
elif platform.system() == 'Linux':
	chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'linux'+slash+'chromedriver'
	chromePortable = chromedriver
elif platform.system() == 'Darwin':
	chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'darwin'+slash+'chromedriver'
	chromePortable = chromedriver
stmp = myHome + slash+'temp'
rtstmp = home +slash+'.rt'+slash+ 'profile'+slash+'temp'
chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'80.0.3987.16'+slash+'chromedriver.exe'
exif_temp = stmp + slash+'exif'
json_temp = stmp + slash+'_temp.json'
txt_temp = stmp + slash+'_temp.txt'
text_temp = stmp + slash+'_temp.txt'
html_temp = stmp + slash+'_temp.htm'
# D:\tech\hosts\MSI\temp\_temp.htm
pips = stmp + slash+'pips.txt'
tmpbat = stmp + slash+'44E28BDF-8269-EEAE-D1DC-9B05B63E5F93.bat'
tempFile = stmp + slash+'{c84ebb36-d978-4fdb-a928-1d906f89df25}'
tmpf = stmp + slash+'{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}'
tmpf0 = stmp + slash+'{B820137A-79B8-45E3-BCBD-A6CAC50892D0}'
tmpf1 = stmp + slash+'{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}'
tmpf2 = stmp + slash+'{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}'
tmpf3 = stmp + slash+'{F139D191-FA1A-44D5-855C-7E5141B30E0D}'
tmpf4 = stmp + slash+'{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}'
tmpf5 = stmp + slash+'{201D82D6-2DC0-4552-A598-54F5481399A1}'
tmpf6 = stmp + slash+'{26B3B9C6-0A59-432A-9386-D432B53001CB}'
tmpf7 = stmp + slash+'{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}'
tmpf8 = stmp + slash+'{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}'
tmpf9 = stmp + slash+'{DF1D4EBC-838E-419C-9C58-943C1767391A}'
contextTemp = stmp + slash+'{21E8D046-A855-EE9B-B772-9EECBD922D87}'
myTemp = stmp
# indexFolder = indexRoot + slash + computername + slash+'index'+slash
myBookmarks = myHome + slash+'bookmarks'
bookmarkFormat = myBookmarks + slash+'BM-ALIASHERE.txt'
myTickets = myHome + slash+'tickets'
# bookmarksFolder = techFolder + slash+'scripts'+slash+'script-bookmarks'+slash+'MSI'+slash
fileBackupLogData = []
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@['+slash+']^_`{|}~ \t\n\r\x0b\x0c'
safeChar = printable
cryptoKeyPad = '{D0A25D57-37B9-4DCA-A290-F7F5D2B4E869-ED89EEC8-FC42-4E36-B57A-BD2756F58071-1358EA50-2BED-4533-99C7-4D90BB450D7F-40A9A7E8-6AF5-4C32-9062-F975CDF12209}'
myLogs = myHome + slash+'logs'
myAppLogs = myHome + slash+'logs'+slash+'apps'

def tv(var=None,val='a80cc434'):
	global terminal_variables
	global tvy
	vs = __.getYML(tvy)
	if var is None:
		return vs
	elif val=='a80cc434':
		if var in vs:
			return vs[var]
		else:
			return ''
	else:
		if val is None:
			if var in vs:
				del vs[var]
		else:
			vs[var]=str(val)
		__.saveYML(vs,tvy)
		script=[]
		if __.isWin:
			tvx=terminal_variables+'.bat'
			for v in vs: script.append('SET '+v+'='+vs[v])
		else:
			# for v in vs: os.environ[v]=vs[v]
			import subprocess
			tvx=terminal_variables+'.sh'
			script.append('#!/bin/bash')
			for v in vs: script.append('export '+v+'="'+vs[v]+'"')
		__.saveText('\n'.join(script), tvx )
		if not __.isWin: os.chmod( tvx, 0o777 )

def cloud_path( path ):
	global techDrive
	global slash
	global techFolder
	global slashes
	paths = []
	if not __.isWin:
		x = os.getenv('HOME') + slash + 'tech' + slash
		paths.append(x)
	x = techFolder+slash
	if not x in paths:
		paths.append(x)
	x = 'D:\\tech\\'
	if not x in paths:
		paths.append(x)
	x = techDrive
	if not x in paths:
		paths.append(x)
	found = False
	newPath = path
	for test in paths:
		if test.lower() in path.lower():
			found = True
			if not test in path:
				for subject in _.caseUnspecific( path, test ):
					newPath = newPath.replace( subject, '' )
			else:
				newPath = newPath.replace( test, '' )
	if found:
		if __.isWin:
			newPath = newPath.replace(  slashes['w'], slashes['u']  )
		newPath = '/'+newPath
		newPath = newPath.replace( '//', '/' )
		newPath = newPath.replace( '//', '/' )
		newPath = newPath.replace( '//', '/' )
		_.pr(newPath)
		return newPath
	_.pr(path)
	return path
def projectData( project ):
	global slash
	global databank
	pf = slash.join(  project.split('.')  )
	p = databank+slash+'projects'+slash+pf+slash
	dir_check_create(p)
	return p
def session():
	return os.getenv('Session_ID')
def autoUNC( path, alt=False, o=None, crypt=None ):
	global windowsSlash
	global unixSlash
	global slash
	global UNC
	found = False
	if crypt is None:
		for key in UNC['de'].keys():
			if key in path:
				found = True
				path = path.replace( key, UNC['de'][key] )
		if not found:
			for key in UNC['en'].keys():
				if key in path:
					found = True
					path = path.replace( key, UNC['en'][key] )
		if not found and alt:
			if ':' in path:
				path = UNC['en']['alt'] + path.split(':')[1]
	
	elif not crypt is None:
		if 'en' in crypt:
			if not found:
				for key in UNC['en'].keys():
					if key in path:
						found = True
						path = path.replace( key, UNC['en'][key] )
			if not found and alt:
				if ':' in path:
					path = UNC['en']['alt'] + path.split(':')[1]
		elif 'de' in crypt:
			for key in UNC['de'].keys():
				if key in path:
					found = True
					path = path.replace( key, UNC['de'][key] )
	if not o is None:
		if 'w' in o.lower():
			path = path.replace( unixSlash, windowsSlash )
		else:
			path = path.replace( windowsSlash, unixSlash )
	return path
def theUSB():
	pass
def create_default_profile():
	pass

def popFile( path ):
	global slash
	parts = path.split( slash )
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	folder = slash.join(parts)
	return folder
def popFileDir( path ):
	try: dir_check_create(popFile(path));
	except Exception as e: return False;
	return True
	
def dir_structure():
	global slash
	global appProfiles
	global compiled
	global databank
	global databases
	global dbTables
	global documentation
	global duckDuckGo
	global library
	global myAppLogs
	global myBackup
	global myBIN
	global myBookmarks
	global myConfig
	global myDatabank
	global myDatabases
	global myIndexes
	global myLogs
	global myNotes
	global myTables
	global myTickets
	global myTXT
	global myVars
	global myWebApp
	global profileTMP
	global widgets
	global project
	# global python
	global stmp
	global techDrive
	global thisHost
	global umlHtml
	global umlJson
	global updates
	global myHome
	global py
	global terminal
	dir_check_create( py )
	home_created = dir_check_create( myHome )
	dir_check_create( myIndexes )
	dir_check_create( myTables )
	dir_check_create( myWebApp )
	dir_check_create( myBackup )
	dir_check_create( myDatabases )
	dir_check_create( myVars )
	dir_check_create( terminal )
	dir_check_create( myNotes )
	dir_check_create( myLogs )
	dir_check_create( myConfig )
	dir_check_create( myDatabank )
	
	dir_check_create( umlJson )
	dir_check_create( umlHtml )
	dir_check_create( stmp )
	dir_check_create( myBookmarks )
	dir_check_create( myTickets )
	dir_check_create( myLogs )
	dir_check_create( myAppLogs )
	dir_check_create( myTXT )
	dir_check_create( myBIN )
	dir_check_create( profileTMP )
	
	dir_check_create( duckDuckGo )
	dir_check_create( library )
	dir_check_create( databank )
	dir_check_create( databank+slash+'indexes' )
	dir_check_create( databank+slash+'indexes'+slash+'queries' )
	dir_check_create( databank+slash+'indexes'+slash+'databases' )
	dir_check_create( databank+slash+'indexes'+slash+'tag_stems' )
	dir_check_create( databank+slash+'vault' )
	dir_check_create( databank+slash+'profiles' )
	dir_check_create( databank+slash+'profiles'+slash+'folders' )
	dir_check_create( databank+slash+'db' )
	dir_check_create( databank+slash+'temp' )
	dir_check_create( databank+slash+'projects' )
	# dir_check_create( databank+slash+'query_cache' )
	dir_check_create( widgets )
	dir_check_create( documentation )
	dir_check_create( project )
	dir_check_create( updates )
	dir_check_create( appProfiles )
	dir_check_create( compiled )
	# dir_check_create( thisHost + slash+'{}' )
	dir_check_create( thisHost+slash+'config' )
	dir_check_create( thisHost+slash+'WebApp' )
	dir_check_create( thisHost+slash+'archive' )
	dir_check_create( thisHost+slash+'backup' )
	dir_check_create( thisHost+slash+'bookmarks' )
	dir_check_create( thisHost+slash+'databases' )
	dir_check_create( thisHost+slash+'indexes' )
	# dir_check_create( thisHost+slash+'info' )
	dir_check_create( thisHost+slash+'logs' )
	dir_check_create( thisHost+slash+'notes' )
	# dir_check_create( thisHost+slash+'playground' )
	dir_check_create( thisHost+slash+'widgets' )
	dir_check_create( thisHost+slash+'projects' )
	# dir_check_create( thisHost+slash+'scripts' )
	dir_check_create( thisHost+slash+'tables' )
	dir_check_create( thisHost+slash+'temp' )
	dir_check_create( thisHost+slash+'tickets' )
	dir_check_create( thisHost+slash+'txt' )
	dir_check_create( thisHost+slash+'json-uml-tree' )
	dir_check_create( thisHost+slash+'vars' )
	dir_check_create( thisHost+slash+'tables'+slash+'imdb' )
	dir_check_create( thisHost+slash+'tables'+slash+'txt' )
	dir_check_create( thisHost+slash+'tables'+slash+'applogs' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'{}' )
	# type %tmpf1% | p line --c -make "dir_check_create( widgets+os.sep+'widgets'+slash+'{}' )"
	dir_check_create( widgets+os.sep+'widgets'+slash+'batch' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'c++' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'compiled' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'data' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'databank' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'documentation' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'exe' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'extensions' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'hack' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'html' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'javascript' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'keys' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'php' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'powershell' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'project' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'python' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'vbs' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'webApp' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'java' )
	# dir_check_create( widgets+os.sep+'widgets'+slash+'git' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'cron' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'sessions'+slash+'waiting' )
	dir_check_create( widgets+os.sep+'widgets'+slash+'sessions'+slash+'active' )
	# dir_check_create( techDrive+slash+'techApps' )
	# dir_check_create( techDrive + slash+'techApps\\_installers' )
	# dir_check_create( techDrive + slash+'techApps\\_stand_alone' )
	# dir_check_create( techDrive + slash+'techApps\\tools' )
	# dir_check_create( techDrive + slash+'techApps\\one\\two\\three' )
	dir_check_create( dbTables )
	dir_check_create( databases )

	if home_created:
		create_default_profile()
def createDestinationFolders( folder, o=None, isFile=False, p=False, f=None, pop=False ):
	if pop: isFile=True
	if not f is None: isFile=f
	_pr=p
	folder=path_fix(folder)
	global techDrive
	global slashes
	global slash
	global UNC
	# _.pr(folder)
	if os.path.isdir(folder): return None;
	
	thisSlash = slash
	for key in UNC['de'].keys():
		if key in folder:
			folder = folder.replace( key, UNC['de'][key] )
	if os.path.isdir(folder): return None;
	# _.pr(folder)
	if not __.isWin:
		isUnix = True
	else:
		isUnix = False
	if not o is None:
		if not 'w' in o.lower():
			isUnix = True
		else:
			isUnix = False
	if isUnix:
		thisSlash = slashes['unix']
		if ':' in folder:
			folder = techDrive + slash + folder.split(':')[1]
	if isFile:
		f = folder.split(thisSlash)
		f.reverse()
		f.pop(0)
		f.reverse()
		folder = thisSlash.join( f )
	if os.path.isdir( folder ):
		return folder
	try:
		os.mkdir(  folder )
		if _pr:
			_.pr( folder )
		return folder
	except Exception as e:
		pass
	parts = folder.split( slash )
	# print('here')
	
	# ??????
	# if not os.path.isdir( parts[0] ):
	#     return folder
	# ??????

		# _.colorThis( 'Error: Destination drive does not exist', 'red' )
	newParts = []
	for p in parts:
		newParts.append( p )
		f = slash.join( newParts )
		exist = os.path.isdir( f )
		if not exist:
			if _pr: print(f)
			try:
				os.mkdir( f )
			except Exception as e:
				pass
				# _.colorThis( [ 'Error: creating folder', f ], 'red' )
	return folder
def dir_check_create( folder ):
	folder=path_fix(folder)
	# _.pr(folder)
	return createDestinationFolders( folder )
	global dDim
	global slash
	global slashes
	global techDrive
	global techFolder
	global appsFolder
	if not __.isWin:
		folder = folder.replace( slashes['windows'], slash )
		folder = folder.replace( ':', '' )
		techDrive = techDrive.replace( slashes['windows'], slash )
		techDrive = techDrive.replace( ':', '' )
	# if techDrive in folder:
	#     folder = techDrive+dDim+slash+folder
	# _.pr(folder)
	# _.pr( folder )
	if os.path.isdir( folder ):
		# _.pr( folder )
		return False
	try:
		os.mkdir( folder )
		return True
	except Exception as e:
		pass
	t = None
	if appsFolder in folder:
		t = appsFolder
	elif techFolder in folder:
		t = techFolder
	if t is None:
		return None
	fld = folder.replace( t+slash, '' )
	parts = fld.split( slash )
	# parts.pop(0)
	newParts = []
	for p in parts:
		newParts.append( p )
		f = slash.join( newParts )
		f = t+slash+f
		# if not techDrive in f:
		#     f = techDrive+dDim+slash+f
		# _.pr(f)
		exist = os.path.isdir( f )
		# _.pr( 'exist:', exist, f, '\r\n' )
		if not exist:
			try:
				os.mkdir( f )
			except Exception as e:
				pass
				# _.pr( 'Error:', f )
	return True
def dir_check_create2( theFolder ):
	theFolder=path_fix(theFolder)
	global slashes
	global slash
	if not __.isWin:
		theFolder = theFolder.replace( slashes['windows'], slash )
	if not os.path.exists( theFolder ):
		try:
			os.mkdir( theFolder )
		except Exception as e:
			pass
def appLogs():
	global myLogs
	global myAppLogs
	if not os.path.isdir( myLogs ):
		os.mkdir( myLogs )
	if not os.path.isdir( myAppLogs ):
		os.mkdir( myAppLogs )
	return myAppLogs
def ticketPath( ticket ):
	global myTickets
	global slash
	dirList = os.listdir(myTickets)
	i = 0
	for item in dirList:
		path = myTickets + slash + item
		if os.path.isfile(path) and item.lower().endswith('.txt'):
			if item.lower().startswith('closed-') or item.lower().startswith('open-'):
				idx = item.lower().replace( 'closed-', '' ).replace( 'open-', '' ).replace( '.txt', '' )
				if idx == ticket:
					return path
	return False
def fileBackupLog():
	global fileBackupLogData
	if len(fileBackupLogData) == 0:
		fileBackupLogData = getTable('fileBackup.json')
	return fileBackupLogData
def generateFunctionLogFilename( filename ):
	global myTXT
	global py
	file = os.path.abspath( filename )
	# _.pr( file )
	f = file
	if myTXT in file:
		for record in fileBackupLog():
			if record['backup'] == file:
				f = record['file']
				break
	fb = f.replace( py, '' ).replace( '.py', '' )
	fb = fb.replace( slash, '_' )
	fbr = 'audit_'+fb + '_raw.json'
	fbf = 'audit_'+fb + '_functions.json'
	# _.pr( fbf )
	return fbf

def getTable( theFile, tableTemp=False, printThis=False ):
	theFile=path_fix(theFile)
	global simplejson
	if not simplejson is None:
		import simplejson
	global myTables
	global slash
	global stmp
	if os.sep in theFile:
		file0 = theFile
	else:
		if not type( tableTemp ) == bool:
			if tableTemp == 'split':
				file0 = myTables + slash+'tablesets'+slash + theFile
		else:
			if tableTemp == True:
				file0 = stmp + slash + theFile
			else:
				file0 = myTables + slash + theFile
	if printThis:
		_.pr('Loaded: ' + file0)
	if os.path.isfile(file0) == True:
		with open(file0,'r', encoding="latin-1") as json_file:
			json_data = simplejson.load(json_file)
		return json_data
	else:
		return __.data_default(file=theFile,default=[]).default()

def app7z():
	if not __.isWin:
		if not os.path.isfile('/usr/bin/7z'):
			ask=''
			# get = 'sudo apt-get install p7zip-full'
			ask=input( ' not installed.. install ? ' )
			if not 'y' in ask.lower():
				sys.exit()
			os.system( 'sudo apt-get install p7zip-full' )
		return '/usr/bin/7z'
	else:
		# app7z0 = "c:\\Program Files (x86)\\7-Zip\\7z.exe"
		app7z0 = "C:\\Program Files\\7-Zip\\7z.exe"
		app7z1 = appsFolder + "\\7-Zip\\7z.exe"
		app = ""
		if os.path.isfile(app7z0):
			app = app7z0
		elif os.path.isfile(app7z1):
			app = app7z1
		else:
			print('Error: no 7z')
			sys.exit()
		app = '"' + app + '"'
	return app
def getUserProfile():
# machineID = _v.getMachineID()
	os.system("echo %userprofile% >" + tempFile)
	output = open( tempFile, 'r' ).read()
	try:
		os.remove(tempFile)
	except Exception as e:
		pass
	output = output.replace('\n','')
	output = output.replace('\r','')
	output = _str.cleanBE( output, ' ' )
	return output
def md5(string,_id=False,mini=False):
	import _rightThumb._md5 as _md5
	MD5 = _md5.md5(string)
	if _id: MD5 = _md5.md52GUID(MD5,True)
	elif mini:
		a = MD5[:3]
		b = MD5[3:7]
		MD5 = f'{a}-{b}'
	return MD5
def machine():
	import uuid
	return md5(  str(uuid.UUID(int=uuid.getnode()))  ,mini=True)



# /etc/machine-id
# uuid.UUID(int=uuid.getnode())
	
def getMachineID():
# machineID = _v.getMachineID()
	import uuid
	import _rightThumb._md5 as _md5
	global tempFile
	if __.isWin:
		os.system("wmic useraccount where (name='administrator' and domain='%computername%') get name,sid | find \"admin\" >" + tempFile)
		output = open( tempFile, 'r' ).read()
		try:
			os.remove(tempFile)
		except Exception as e:
			pass
		output = _str.replaceAll(output, ' ','')
		output = _str.totalStrip(output)
		output = output.replace('administrator','')
		# _.pr('getMachineID',output)
		# sys.exit()
		md5 = _md5.md5(output)
		guid = _md5.md52GUID(md5,True)
		return guid
	else:
		global unixID
		return unixID
		
def getDriveID(driveLetter):
	global slash
	global dDim
	idFile = ddDim(driveLetter) +slash+'drive.id.sys'
	# _.pr(idFile)
	result = False
	if os.path.isfile(idFile) == True:
		driveID = open( idFile, 'r' ).read()
		driveID = driveID.replace(' ','')
		driveID = driveID.replace('\n','')
		driveID = driveID.replace('\r','')
		result = driveID
	return result
def sanitizeFolder( id_path ):
	global folderID_tech
	global folderID_profile
	global folderID_host
	global techFolder
	global thisHost
	global slash
	id_path = __.path(id_path)
	if id_path is None:
		return None
	id_path = id_path.replace( techFolder, folderID_tech )
	if __.isWin:
		id_path = id_path.replace( os.environ['USERPROFILE'], folderID_profile )
	elif not __.isWin:
		id_path = id_path.replace( os.environ['HOME'], folderID_profile )
	
	id_path = id_path.replace( thisHost, folderID_host )
	id_path = id_path.replace( slash, '/' ).replace( '//', '/' ).replace( '//', '/' ).replace( '//', '/' ).replace( '//', '/' ).replace( '//', '/' )
	return id_path
def resolveFolderIDs( id_path ):
	if id_path is None:
		return None
	global folderID_tech
	global folderID_profile
	global folderID_host
	global techFolder
	global thisHost
	global slash
	if id_path is None:
		return None
	id_path = id_path.replace( folderID_tech, techFolder )
	if __.isWin:
		id_path = id_path.replace( folderID_profile, os.environ['USERPROFILE'] )
	else:
		id_path = id_path.replace( folderID_profile, os.environ['HOME'] )
	
	id_path = id_path.replace( folderID_host, thisHost )
	# id_path = id_path.replace( folderID_tech, techFolder )
	# if __.isWin:
	#     id_path = id_path.replace( os.environ['USERPROFILE'], folderID_profile )
	# elif not __.isWin:
	#     id_path = id_path.replace( os.environ['HOME'], folderID_profile )
	
	# id_path = id_path.replace( folderID_host, thisHost )
	# if not __.isWin:
	id_path = id_path.replace( '4FD4030911', slash )
	id_path = id_path.replace( '/', slash )
	id_path = id_path.replace( '\\', slash )
	return id_path
	return __.path(id_path)
def filePath(path):
	return 'file://' + os.path.realpath(path)
def notepad():
	global slash
	global myVars
	f = open(myVars + slash+'notepad.txt' , 'r', encoding='latin-1')
	lines = f.readlines()
	f.close()
	result = lines[0].replace('\n','')
	return result
def myCrypto( data=False, encrypt=True, decrypt=False ):
	global cryptoKeyPad
	import _rightThumb._encryptString as _blowfish
	if type( data ) == bool:
		data = cryptoKeyPad
	if decrypt or not encrypt:
		return _blowfish.decrypt( data, password=True )
	else:
		return _blowfish.encrypt( data, password=True )
def scrampleIDs(ids):
	if len(ids) == 38 and ids[0] == '{' and ids[-1] == '}' and len(ids.split('-')) == 5:
		result = ''
		
		i=0
		for char in ids:
			if i == 1:
				result += ids[36]
			elif i == 2:
				result += ids[35]
			elif i == 8:
				result += ids[20]
			elif i == 36:
				result += ids[1]
			elif i == 35:
				result += ids[2]
			elif i == 20:
				result += ids[8]
			elif i == 10:
				result += ids[15]
			elif i == 11:
				result += ids[16]
			elif i == 12:
				result += ids[17]
			elif i == 13:
				result += ids[18]
			elif i == 15:
				result += ids[10]
			elif i == 16:
				result += ids[11]
			elif i == 17:
				result += ids[12]
			elif i == 18:
				result += ids[13]
			else:
				result += char
			i+=1
	else:
		result = ids
	return result
def installationCheck():
	global techFolder
	fileName = techFolder + slash+'scripts\\instanceID.sys'
	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write( genUUID() )
def batch_files():
	# epyi vars -file batch_c
	# epyi vars -file batch_cc
	# epyi vars -file batch_timestamp
	# epyi vars -file batch_theUSB
	global batch_files_installed
	try:
		batch_files_installed
	except Exception as e:
		batch_files_installed = False
		
	if not batch_files_installed:
		batch_files_installed = True
		global home
		global widgets
		global slash
		## OLD_INSTALLER
		# if __.isWin:
		#     if not os.path.isfile( widgets+os.sep+'widgets'+ slash+'batch\\c.bat' ):
		#         from _rightThumb._vars import batch_c
		#         batch_c.GENERATE_FILE(widgets)
		#     if not os.path.isfile( home + slash+'cc.bat' ):
		#         from _rightThumb._vars import batch_cc
		#         batch_cc.GENERATE_FILE(home)
		#     if not os.path.isfile( widgets+os.sep+'widgets'+ slash+'batch\\timestamp.bat' ):
		#         from _rightThumb._vars import batch_timestamp
		#         batch_timestamp.GENERATE_FILE(widgets)
		#     if not os.path.isfile( widgets+os.sep+'widgets'+ slash+'batch\\theUSB.bat' ):
		#         from _rightThumb._vars import batch_theUSB
		#         batch_theUSB.GENERATE_FILE(widgets)
if not __.autoCreationConfiguration['created']['_vars']:
	dir_structure()
	batch_files()
	__.autoCreationConfiguration['created']['_vars'] +=1
	# autoCreationConfiguration_folders = False
try:
	if unixID_NEW:
		f = open(unixID_path,'w', encoding='utf-8')
		f.write(unixIDs)
		f.close()
except Exception as e:
	pass
ip = 'offline'
ip_old = None
def ipGet(force=False):
	global ip_old
	global ip
	global host_alias
	global unixIDs
	global config_hash
	global __ip_php
	global __register_php
	if not __ip_php: return '0.0.0.0'
	if not __register_php: return '0.0.0.0'
	
	

	get_ip = False
	hasImported = False
	if not os.path.isfile(configFile('.ip')):
		from lxml import html
		import requests
		import urllib
		hasImported = True
		f = {
				'alias': host_alias,
				'ids': '-'.join(unixIDs),
				'os':str(platform.platform())
		}
		if os.path.isfile( configFile('.distro') ):
			f['distro'] = open( configFile('.distro'), 'r' ).read()
		url = config_hash['register.php']+'?'+urllib.parse.urlencode(f)
		# _.pr(url)
		try:
			ip = html.fromstring(requests.get( url  ).content).text_content()
			open(configFile('.ip'),'w', encoding='utf-8').write( ip )
		except Exception as e:
			ip = 'offline'
		get_ip = True
	else:
		cache_time = os.path.getmtime(configFile('.ip'))
		cache_age = time.time() - cache_time
		if cache_age > 14400:
			get_ip = True
	# _.pr(get_ip)
	if not get_ip and not force:
		# ip = open( configFile('.ip'), 'r' ).read()
		ip = open(configFile('.ip'), 'r', encoding='utf-8').readlines()[0]
		# _.pr(ip,'here',configFile('.ip'))
		ip = _str.totalStrip(ip)
	elif get_ip or force:
		if not hasImported:
			from lxml import html
			import requests
		ip_old = open(configFile('.ip'), 'r', encoding='utf-8').readlines()[0]
		try:
			ip = html.fromstring(requests.get(config_hash['ip.php']+'?id='+unixIDs[8]).content).text_content()
			open(configFile('.ip'),'w', encoding='utf-8').write( ip )
		except Exception as e:
			ip = 'offline'
	# import urllib
	# ip = urllib.request.urlopen( 'http://tools.rightthumb.com/ip.php?' ).read()
	# ip = str(ip,'iso-8859-1')
	if ip_old is None:
		ip_old = ip
	if not ip_old == ip:
		ip_hash = __.getTable( configFile('.ip.hash') )
		if not ip in ip_hash:
			ip_hash[ip] = {}
		ip_hash[ip][time.time()] = {}
		__.saveTable( ip_hash, configFile('.ip.hash') )
	
	return ip
if not os.path.isdir( myConfig ):
	dir_check_create( myConfig )
	dir_structure()
	gen_unixIDs()
if not '/bash/' in __file__:
	try:
		ipGet()
	except Exception as e:
		pass
		# _.pr( 'Error: IP' )
def table(t):
	global myTables
	global slash
	return myTables + slash + t
def tableDB(t):
	global tablesDB
	global slash
	return tablesDB + slash + t
def tableAlt(t,h='MSI'):
	global myHome
	global slash
	parts = myHome.split(slash)
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	fo = slash.join( parts ) +slash+ h +slash+ 'tables'
	if os.path.isdir(fo):
		fo = os.path.abspath(fo)
	fi = fo+slash+ t
	return fi
def tableAlts(t,omit=True):
	global myHome
	global slash
	parts = myHome.split(slash)
	parts.reverse()
	current = parts.pop(0)
	parts.reverse()
	folder = slash.join( parts )
	# _.pr( folder )
	# sys.exit()
	result = []
	for ho in os.listdir(folder):
		shouldInclude = True
		if omit and ho == current:
			shouldInclude = False
		if shouldInclude:
			fo =  folder+slash+ ho +slash+ 'tables'
			if os.path.isdir(fo):
				fo = os.path.abspath(fo)
				fi = fo+slash+ t
				if os.path.isfile(fi):
					result.append(fi)
	return result





# popFileDir(path)
# _.pr('end')
def config( subject='?' ):
	global myConfig
	global config_file
	global config_hash
	global config_default
	if config_file is None:
		config_file = {}
		try:
			if os.path.isfile(myConfig +os.sep+ '.config.hash'):
				config_file = __.getTable( myConfig +os.sep+ '.config.hash' )
				if 'cloud-ssh-pass' in config_file:
					config_default.cloud.ssh.password = config_file['cloud-ssh-pass']
		except Exception as e:
			pass
	cData = dics( config_hash, config_file, config_default_dic )

	if subject == '?':
		return config_default
	if subject in cData:
		return cData[subject]
	return None


try:
	if not os.path.isfile(myConfig+os.sep+'construct.settings'):
		with open(   myConfig+os.sep+'construct.settings',    'w' ) as f:
			pass
except Exception as e:
	_.pr( 'unable to touch:', myConfig+os.sep+'construct.settings' )

def settings_load():
	global myConfig
	if os.stat( myConfig+os.sep+'construct.settings' ).st_size:
		table = getTable(myConfig+os.sep+'construct.settings')
		for k in table:
			__.settings_table[k] = table[k]

def fpath(path): return resolveFolderIDs(path.replace('\\',os.sep).replace('/',os.sep))


figpath=home +os.sep+'.rt'+os.sep+ '.config.hash'

path = __.path
mkdir=createDestinationFolders
# default_powershell = 'echo test | py $p\\app.py'
default_powershell = ''
config_file = None

hp=myHome
hi=myIndexes
hc=myConfig
ht=myTables
hb=myBackup

bk=myBackup
tt=myTables

pp = techFolder + slash+'widgets'
w = techFolder 
ww = techFolder + slash+'widgets'

t   = techDrive
tt  = myTables
ttt = dbTables
p   = home
pp = widgets
ta = appsFolder



if not os.path.isdir(myConfig):
	dir_structure()
# dir_check_create
# thisHost
## OLD_INSTALLER
myAppsPy=py
wprofile = myHome
doc_sep = '__________________________________________________________________________________'
meta=config_hash
# print(life); sys.exit();


keychainPath=home +os.sep+'.rt'+os.sep+ '.keychain'
keychain=''
if os.path.isfile(keychainPath):
	keychain=__.getText(keychainPath)
fn=dot()
fn.path=dot()
fn.path.fix=fpath
fn.path.res=resolveFolderIDs
fn.path.san=sanitizeFolder
fn.path.resolve=resolveFolderIDs
fn.path.sanitize=sanitizeFolder
fn.path.path=__.path
fn.path.pop=popFile
fn.path.mpop=popFileDir
applog=myAppLogs
fig=config_hash
if __.isWin:
	user = cmdGetVar('username')
else:
	user = cmdGetVar('USER')

# return __.path(id_path)
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'80.0.3987.16'+slash+'chromedriver.exe'
# chromedriver = 'D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\74.0.3729.6\\chromedriver.exe'
# chromedriver = 'D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\109.0.5414.25\\chromedriver.exe'
# chromedriver = 'D:\\.rightthumb-widgets\\widgets\\exe\\ChromeDriver\\109.0.5414.25\\chromedriver.exe'
chromedriver = 'D:\\techApps\\chrome-win\\chrome.exe'
chromePortable = 'D:\\techApps\\chrome-win\\chrome.exe'