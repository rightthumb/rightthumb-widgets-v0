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

import _rightThumb._construct as __
import _rightThumb._string as _str
from pathlib import Path
import os
import sys
import platform
import time
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
def configFile( item=None, value=None, p=True ):
	try:
		global configFile_data
		if item is None:
			if p:
				import simplejson as json
				dataDump = json.dumps(configFile_data, indent=4, sort_keys=False)
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
if __.isWin:
	# fileName = home + slash+'.tk421'
	fileName = home + slash+'.tk421'
	if not os.path.isfile( fileName ):
		open(fileName,'w', encoding='utf-8').write('C')
	techDrive = open( fileName, 'r' ).read()
	techDrive = _str.totalStrip(techDrive)
	if '\n' in techDrive or '\r' in techDrive:
		techDrive = techDrive.replace('\n','').replace('\r','')
		open(fileName,'w', encoding='utf-8').write( techDrive )
elif not __.isWin:
	techDrive = '/opt/RightThumb'
	try:
		if not os.path.isdir(techDrive):
			os.mkdir(techDrive)
	except Exception as e:
		if os.path.isdir('/home/ximlickficfp/cloud/files'):
			techDrive = '/home/ximlickficfp/cloud/files'
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
	if 'tech_drive' in config_hash:
		if __.isWin:
			techDrive = config_hash['tech_drive']
			techDrive = techDrive.replace(':','')
		if not __.isWin:
			if os.path.isdir(config_hash['tech_drive']):
				techDrive = config_hash['tech_drive']
	if 'path' in config_hash:
		if __.isWin:
			techDrive = config_hash['path']
			techDrive = techDrive.replace(':','')
		if not __.isWin:
			if os.path.isdir(config_hash['path']):
				techDrive = config_hash['path']
config_default.path = techDrive
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
	# fileName = home + slash+'.tk421'
	# fileNameHost = home + slash+'.ncc1701'
	# fileName = fileName.replace( slashes['windows'], slash )
	# if not os.path.isfile( fileNameHost ):
	#     open(fileNameHost,'w', encoding='utf-8').write(computername)
	# if not os.path.isfile( fileName ):
	#     open(fileName,'w', encoding='utf-8').write(home)
	# techDrive = open( fileName, 'r' ).read()
def ddDim(xyz):
	global dDim
	if not dDim:
		return xyz
	if not dDim in xyz:
		return xyz+dDim
# baseFolder = dDim+slash+'tech'+slash+'programs'+slash+'python'+slash+'_rightThumb'+slash+'_base3'
# baseFolderVersions = dDim+slash+'tech'+slash+'programs'+slash+'python'+slash+'_rightThumb'+slash+'_base' + import_delim
techFolder =  ddDim(techDrive)+slash+'tech'
# _.pr('techFolder:',techFolder)
# sys.exit()
appsFolder =  ddDim(techDrive) +slash+'techApps'
archive7z =  ddDim(techDrive) +slash+'tech'+slash+'archive_7z_files'
programs = techFolder + slash+'programs'
pp = techFolder + slash+'programs'
appProfiles = programs + slash+'python'+slash+'profiles'
compiled = programs + slash+'compiled'
documentation = programs + slash+'documentation'
project = programs + slash+'project'
updates = project + slash+'updates'
images = techFolder + slash+'programs'+slash+'project'+slash+'img'+slash
# log_config = techFolder + slash+'programs'+slash+'project'+slash+'log_config'+slash+'log_data.js'
log_config = techFolder + slash+'programs'+slash+'html'+slash+'projects'+slash+'log_config'+slash+'log_data.js'
# log_config_html = techFolder + slash+'programs'+slash+'project'+slash+'log_config'+slash+'index.htm'
log_config_html = techFolder + slash+'programs'+slash+'html'+slash+'projects'+slash+'log_config'+slash+'index.htm'
dance = images + 'dance.gif'
gears = images + 'gears.gif'
if __.isWin:
	sublime = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
elif not __.isWin:
	if os.path.isfile('/opt/sublime/sublime_text'):
		sublime = '/opt/sublime/sublime_text'
	elif os.path.isfile('/usr/bin/sublime_text'):
		sublime = '/usr/bin/sublime_text'
	elif os.path.isfile('/usr/bin/code-oss'):
		sublime = '/usr/bin/code-oss'
# _v.sublime
# scriptsFolder =  techFolder + slash+'scripts'
# thisHost =  'hosts' + slash + computername2
myHome =  techFolder + slash+'hosts' + slash + computername2
thisHost =  myHome
# myHome =  home +slash+ 'profile'
# thisHost =  myHome
hostDefault =  'hosts' + slash+'{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}'
dataFolder = techFolder + slash+'data'
myIndexes = myHome + slash+'indexes'
quickIndex = myIndexes + slash+'0A{465C1A34-D22F-184E-F713-F8E5149E212D}'
myTables = myHome + slash+'tables'
duckDuckGo = myTables + slash+'DuckDuckGo'
relevant_folders = myTables + slash+'relevantFolders.txt'
myWebApp = myHome + slash+'/tech/programs/servers/web/crud'
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
		for tep in find_unix_editor:
			if os.path.isfile(tep):
				unix_editor = tep
				open(unix_editor_path,'w', encoding='utf-8').write( tep )
				break
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
research = techFolder + slash+'programs'+slash+'databank'
myDatabank = research
keys = techFolder + slash+'programs'+slash+'keys'
data = research
databank = research
python = {
			'crypt': {
						'en': programs + slash+'python'+slash+'crypt'+slash+'en',
						'de': programs + slash+'python'+slash+'crypt'+slash+'de',
			},
			'imploded': {
						'windows': programs + slash+'python'+slash+'imploded'+slash+'unity',
						'unix': programs + slash+'python'+slash+'imploded'+slash+'unity',
						'this': None,
			},
			'src': {
						'windows': programs + slash+'python'+slash+'src'+slash+'unity',
						'unix': programs + slash+'python'+slash+'src'+slash+'unity',
						'this': None,
			},
			'compiled': {
						'windows': programs + slash+'python'+slash+'compiled'+slash+'unity',
						'unix': programs + slash+'python'+slash+'compiled'+slash+'unity',
						'this': None,
			},
			'burn': {
						'windows': programs + slash+'python'+slash+'burn'+slash+'unity',
						'unix': programs + slash+'python'+slash+'burn'+slash+'unity',
						'this': None,
			},
}
if __.isWin:
	python['src']['this'] = python['src']['windows']
	python['imploded']['this'] = python['imploded']['windows']
	python['compiled']['this'] = python['compiled']['windows']
	python['burn']['this'] = python['burn']['windows']
elif not __.isWin:
	python['src']['this'] = python['src']['unix']
	python['imploded']['this'] = python['imploded']['unix']
	python['compiled']['this'] = python['compiled']['unix']
	python['burn']['this'] = python['burn']['unix']
py = programs + slash+'python'+slash+'src'+slash+'unity'
"""
python['crypt']['en']
python['crypt']['de']
python['imploded']['windows']
python['imploded']['unix']
	
python['src']['windows']
python['src']['unix']
python['compiled']['windows']
python['compiled']['unix']
python['burn']['windows']
python['burn']['unix']
"""
  
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
db = databank + slash+'databases'
dbs = databank + slash+'databases'
dbdbs = databank + slash+'databases'
myBatch = myHome + slash+'programs'+slash+'batch'
myTXT = myBackup + slash+'txt'
myBIN = myBackup + slash+'bin'
webapp = techFolder +os.sep+ os.sep.join( 'tech/programs/servers/web/crud'.split('/') )

library = techFolder + slash+'programs'+slash+'library'
myDatabases = myHome + slash+'databases'
myVars = myHome + slash+'vars'
myNotes = myHome + slash+'notes'
umlJson = myHome + slash+'uml_from_json'+slash+'data.js'
umlHtml = myHome + slash+'uml_from_json'+slash+'index.htm'
androidMaster = 'android_apps_master.json'
androidMasterFull = myTables + slash + androidMaster
myApps = techFolder + slash+'programs'
ipsum = myApps + slash+'project'+slash+'ipsum.txt'
myAppsPy = python['src']['windows']
myAppsJs = myApps + slash+'javascript'
myAppsBatch = myApps + slash+'batch'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'2.46'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'73.0.3683.68'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'74.0.3729.6'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'75.0.3770.90'+slash+'chromedriver.exe'
# chromedriver = myApps + slash+'exe'+slash+'ChromeDriver'+slash+'76.0.3809.25'+slash+'chromedriver.exe'
if __.isWin:
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

exif_temp = stmp + slash+'exif'
json_temp = stmp + slash+'_temp.json'
txt_temp = stmp + slash+'_temp.txt'
text_temp = stmp + slash+'_temp.txt'
html_temp = stmp + slash+'_temp.htm'
# D:\tech\hosts\MSI\temp\_temp.htm
pips = stmp + slash+'pips.txt'
tmpbat = stmp + slash+'44E28BDF-8269-EEAE-D1DC-9B05B63E5F93.bat'
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
tempFile = tmpf
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
	# global slash
	# global hostDefault
	# global myBookmarks
	# if os.path.isdir( hostDefault ):
	#     for file in os.listdir( hostDefault + slash+'bookmarks' ):
		# hostDefault =  'hosts' + slash+'{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}'
		# myBookmarks = myHome + slash+'bookmarks'
def popFile( path ):
	global slash
	parts = path.split( slash )
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	folder = slash.join(parts)
	return folder
def popFileDir( path ):
	global slash
	parts = path.split( slash )
	parts.reverse()
	parts.pop(0)
	parts.reverse()
	folder = slash.join(parts)
	try:
		dir_check_create(folder)
	except Exception as e:
		return False
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
	global programs
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
	dir_check_create( py )
	home_created = dir_check_create( myHome )
	dir_check_create( myIndexes )
	dir_check_create( myTables )
	dir_check_create( myWebApp )
	dir_check_create( myBackup )
	dir_check_create( myDatabases )
	dir_check_create( myVars )
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
	dir_check_create( programs )
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
	dir_check_create( thisHost+slash+'info' )
	dir_check_create( thisHost+slash+'logs' )
	dir_check_create( thisHost+slash+'notes' )
	dir_check_create( thisHost+slash+'playground' )
	dir_check_create( thisHost+slash+'programs' )
	dir_check_create( thisHost+slash+'projects' )
	dir_check_create( thisHost+slash+'scripts' )
	dir_check_create( thisHost+slash+'tables' )
	dir_check_create( thisHost+slash+'temp' )
	dir_check_create( thisHost+slash+'tickets' )
	dir_check_create( thisHost+slash+'txt' )
	dir_check_create( thisHost+slash+'uml_from_json' )
	dir_check_create( thisHost+slash+'vars' )
	dir_check_create( thisHost+slash+'tables'+slash+'imdb' )
	dir_check_create( thisHost+slash+'tables'+slash+'txt' )
	dir_check_create( thisHost+slash+'tables'+slash+'applogs' )
	# dir_check_create( programs+slash+'{}' )
	# type %tmpf1% | p line --c -make "dir_check_create( programs+slash+'{}' )"
	dir_check_create( programs+slash+'batch' )
	dir_check_create( programs+slash+'c++' )
	dir_check_create( programs+slash+'compiled' )
	# dir_check_create( programs+slash+'data' )
	dir_check_create( programs+slash+'databank' )
	dir_check_create( programs+slash+'documentation' )
	dir_check_create( programs+slash+'exe' )
	dir_check_create( programs+slash+'extensions' )
	# dir_check_create( programs+slash+'hack' )
	dir_check_create( programs+slash+'html' )
	dir_check_create( programs+slash+'javascript' )
	dir_check_create( programs+slash+'keys' )
	dir_check_create( programs+slash+'php' )
	dir_check_create( programs+slash+'powershell' )
	dir_check_create( programs+slash+'project' )
	dir_check_create( programs+slash+'python' )
	dir_check_create( programs+slash+'vbs' )
	dir_check_create( programs+slash+'webApp' )
	dir_check_create( programs+slash+'java' )
	dir_check_create( programs+slash+'git' )
	dir_check_create( programs+slash+'cron' )
	dir_check_create( programs+slash+'sessions'+slash+'waiting' )
	dir_check_create( programs+slash+'sessions'+slash+'active' )
	dir_check_create( techDrive+slash+'techApps' )
	# dir_check_create( techDrive + slash+'techApps\\_installers' )
	# dir_check_create( techDrive + slash+'techApps\\_stand_alone' )
	# dir_check_create( techDrive + slash+'techApps\\tools' )
	# dir_check_create( techDrive + slash+'techApps\\one\\two\\three' )
	dir_check_create( dbTables )
	dir_check_create( databases )
	# dir_check_create( python['crypt']['en'] )
	# dir_check_create( python['crypt']['de'] )
	# dir_check_create( python['imploded']['windows'] )
	# dir_check_create( python['imploded']['unix'] )
	
	# dir_check_create( python['src']['windows'] )
	# dir_check_create( python['src']['unix'] )
	# dir_check_create( python['compiled']['windows'] )
	# dir_check_create( python['compiled']['unix'] )
	# dir_check_create( python['burn']['windows'] )
	# dir_check_create( python['burn']['unix'] )
	if home_created:
		create_default_profile()
def createDestinationFolders( folder, o=None, isFile=False, p=False ):
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
		f.pop()
		folder = thisSlash.join( f )
	if os.path.isdir( folder ):
		return folder
	try:
		os.mkdir(  folder )
		if p:
			_.pr( folder )
		return folder
	except Exception as e:
		pass
	parts = folder.split( slash )
	
	if not os.path.isdir( parts[0]+slash ):
		return folder
		# _.colorThis( 'Error: Destination drive does not exist', 'red' )
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
				# _.colorThis( [ 'Error: creating folder', f ], 'red' )
	return folder
def dir_check_create( folder ):
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
	global myAppsPy
	global slash
	file = os.path.abspath( filename )
	# _.pr( file )
	f = file
	if myTXT in file:
		for record in fileBackupLog():
			if record['backup'] == file:
				f = record['file']
				break
	fb = f.replace( myAppsPy, '' ).replace( '.py', '' )
	fb = fb.replace( slash, '_' )
	fbr = 'audit_'+fb + '_raw.json'
	fbf = 'audit_'+fb + '_functions.json'
	# _.pr( fbf )
	return fbf
def getTable( theFile, tableTemp=False, printThis=False ):
	import simplejson as json
	global myTables
	global slash
	global stmp
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
			json_data = json.load(json_file)
			# json_data = json.load(json_file, object_pairs_hook=OrderedDict)
	else:
		json_data = []
	return json_data
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
		app7z0 = "c:\\Program Files (x86)\\7-Zip\\7z.exe"
		app7z1 = appsFolder + "\\7-Zip\\7z.exe"
		app = ""
		if os.path.isfile(app7z0):
			app = app7z0
		elif os.path.isfile(app7z1):
			app = app7z1
		else:
			_.pr('Error: no 7z')
			sys.exit()
		app = '"' + app + '"'
	return app
def getUserProfile():
# machineID = _v.getMachineID()
	os.system("echo %userprofile% >" + tempFile)
	output = open( tempFile, 'r' ).read()
	os.remove(tempFile)
	output = output.replace('\n','')
	output = output.replace('\r','')
	output = _str.cleanBE( output, ' ' )
	return output
def getMachineID():
# machineID = _v.getMachineID()
	import _rightThumb._md5 as _md5
	global tempFile
	if __.isWin:
		os.system("wmic useraccount where (name='administrator' and domain='%computername%') get name,sid | find \"admin\" >" + tempFile)
		output = open( tempFile, 'r' ).read()
		os.remove(tempFile)
		output = _str.replaceAll(output, ' ','')
		output = _str.totalStrip(output)
		output = output.replace('administrator','')
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
	id_path = id_path.replace( slash, '/' )    
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
	elif not __.isWin:
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
		global programs
		global slash
		if __.isWin:
			if not os.path.isfile( programs + slash+'batch\\c.bat' ):
				from _rightThumb._vars import batch_c
				batch_c.GENERATE_FILE(programs)
			if not os.path.isfile( home + slash+'cc.bat' ):
				from _rightThumb._vars import batch_cc
				batch_cc.GENERATE_FILE(home)
			if not os.path.isfile( programs + slash+'batch\\timestamp.bat' ):
				from _rightThumb._vars import batch_timestamp
				batch_timestamp.GENERATE_FILE(programs)
			if not os.path.isfile( programs + slash+'batch\\theUSB.bat' ):
				from _rightThumb._vars import batch_theUSB
				batch_theUSB.GENERATE_FILE(programs)
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
		url = 'http://tools.rightthumb.com/register.php?'+urllib.parse.urlencode(f)
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
			ip = html.fromstring(requests.get('http://tools.rightthumb.com/ip.php?id='+unixIDs[8]).content).text_content()
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
path = __.path
mkdir = createDestinationFolders
default_powershell = 'echo test | py $p\\app.py'
# popFileDir(path)
# _.pr('end')
config_file = None
def config( subject='?' ):
	global mymyConfig
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
t   = techDrive
tt  = myTables
ttt = dbTables
p   = home
pp = programs
ta = appsFolder
if not os.path.isdir(myConfig):
	dir_structure()
# dir_check_create
# thisHost


