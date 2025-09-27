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

import time,signal,sys,platform
tz = str(time.strftime("%z")).replace(':','')
# signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

try:
	importlib
except Exception as e:
	importlib = None





releaseAcquiredData = True

table_b_print = False

switch_raw = []



thisOS = platform.system()
theOS = thisOS
OS = theOS
windowsSlash = chr(92)
unixSlash = chr(47)

if thisOS == 'Windows':
	slash = windowsSlash
	isWin  = True
else:
	slash = unixSlash
	isWin  = False

class dot:
	def __init__( self ):
		pass

v = dot()

LOOP = {}

def pathList( *paths ):
	os = imp('os')
	result = os.sep.join(paths)
	result = result.replace( '/', os.sep )
	result = result.replace( '\\', os.sep )
	result = result.replace( os.sep+os.sep, os.sep )
	result = result.replace( os.sep+os.sep, os.sep )
	result = result.replace( 'tech'+os.sep+'tech', 'tech' )
	return result

def p( *text, w='' ):
	texXxt = []
	for x in text:
		texXxt.append(str(x))
	txt = ' '.join( texXxt )
	
	if w:
		os = imp('os')
		if os.path.isfile(w):
			file1 = open( w , 'a' )
			file1.write( txt+'\n' )
			file1.close()
		else:
			file1 = open( w , 'w' )
			file1.write( txt+'\n' )
			file1.close()
	print(txt)


def xit():
	sys.exit()

specifications = {}
did_table = {}
def uuid():
	UUID = imp('uuid')
	return str(UUID.uuid4())

def settings( subjects, a='a678-71e9', d=None, to='71e9-a678' ):
	if not a == 'a678-71e9':
		for subject in subjects:
			if a == setting( subject, to, d ):
				return True
		return False
	else:
		for subject in subjects:
			setting( subject, to, d )


setting_table = {}
def setting( subject, to='71e9-a678', d=None ):
	global setting_table

	if not to == '71e9-a678':
		setting_table[subject] = to

	if not subject in setting_table:
		return d
	
	return setting_table[subject]


imp_table = {}
def imp( subject, imp_table_testing=False ):
	global imp_table
	global importlib
	if importlib is None:
		import importlib
		if imp_table_testing:
			print('\n\n\t\timport importlib\n\n')

	if not subject in imp_table:
		try:
			imp_table_tmp
		except Exception as e:
			pass
		else:
			del imp_table_tmp



		try:
			imp_table[subject] = importlib.import_module(subject)
			if imp_table_testing:
				print( 'imp.DID' )
			return imp_table[subject]
		except Exception as e:
			if imp_table_testing:
				print( 'imp.NO' )
			return None
	if imp_table_testing:
		print( 'imp.YES' )
	return imp_table[subject]



on_exit_subjects = {}
def onExit(script,subject=None):
	global on_exit_subjects
	if subject is None:
		subject = uuid()
	on_exit_subjects[subject] = script

def isExit():
	global on_exit_subjects
	for subject in on_exit_subjects:
		on_exit_subjects[subject]()


def path( p, ab=True, pop=False, file=False ):
	# os = vc.FIG.imp('os')
	os = imp('os')
	if not p:
		return p
	# print(p)
	p = p.replace( chr(92), os.sep )
	p = p.replace( chr(47), os.sep )
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

def file( p ):
	os = imp('os')
	p = p.replace( chr(92), os.sep )
	p = p.replace( chr(47), os.sep )
	if not os.sep in p:
		return p
	parts = p.split(os.sep)
	parts.reverse()
	f = parts.pop(0)
	return f

class data_default:
	# __.data_default(file=theFile,default=[])
	def __init__( self, file, default ):
		self.dics = 'index,indexes,dex,ls,hash,hashes,tables,logs,lists,indices,meta,setting,settings'
		self.lists = 'table,cache,log,list'
		self.file = file
		self.default_result = default
	def default( self ):
		for x in self.dics.split(','):
			if self.file.lower().endswith( '.'+x ):
				return {}
		for x in self.lists.split(','):
			if self.file.lower().endswith( '.'+x ):
				return []
		return self.default_result

def getTable( file ):
	os = imp('os')
	json = imp('simplejson')

	if os.path.isfile(file):
		with open(file,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
	else:
		json_data = data_default(file=file,default=[]).default()
	return json_data

def saveTable( data, file, sk=False ):
	json = imp('simplejson')
	dataDump = json.dumps(data, indent=4, sort_keys=sk)

	f = open(file,'w')
	f.write(str(dataDump))
	f.close()


pre_error = False
class Table_Aggregates:
	def __init__( self ):
		self.triggers = {}
	def trigger( self, label, script ):
		self.triggers[label] = script
	def run( self, label, data ):
		return self.triggers[label](data)
table_aggregates = Table_Aggregates()


payloadCache = None
varFoldersCheck = False
myFileLocations_SKIP_VALIDATION = False




autoCreationConfiguration = {
							'backup': True,
							'logs': True,
							'folders': True,
							'created': { '_vars': 0 },
}
"""
__.autoCreationConfiguration['backup']
__.autoCreationConfiguration['logs']
__.autoCreationConfiguration['folders']
"""

# import importlib
try:
	startTime
except Exception as e:
	startTime = time.time()
	
trigger_isPipe = False
isRequired_Pipe = False
isRequired_Pipe_or_File = False
isRequired_or_List = None
isRequired_index = {}
switchList = []
appRegPipe = None
cls_process_switches_help = False

storyboard = []
# __.sbd( fn=sys._getframe().f_code.co_name, d='' )
def sbd( location=1, line=0, fn='', d='' ):
	# add to auto documentation
	global storyboard
	global switchList
	function = fn
	activeSwitches = ''
	inactiveSwitches = ''
	documentation = n

	storyboard.append({ 'timestamp': time.time(), 'function': function, 'active': activeSwitches, 'inactive': inactiveSwitches })


def triggerTest( data ):
	return 'test'

def clearFocus( name, file ):
	global slash
	f = file.split(slash)
	if name == '__main__':
		x = '__' + f[len(f)-1].replace('.py','') + '__'
	else:
		x = f[len(f)-1].replace('.py','')
	return x

def thisApp( file ):
	global slash
	f = file.split(slash)
	x = f[len(f)-1].replace('.py','')
	return x





# delimReg = '_'
delimReg = '_-_'

appReg = ''

registeredApps = []
registeredAppsAll = []

threadQueue = {}

def constructRegistration( file, dba ):
	global registeredAppsAll
	shouldAdd = True
	for ra in registeredAppsAll:
		if ra['dba'] == dba:
			shouldAdd = False
	if shouldAdd:
		registeredAppsAll.append({ 'file': file, 'dba': dba })

def constructApps():
	global registeredAppsAll
	for appreg in registeredAppsAll:
		print(appreg)

def appName( appReg, parentApp='', childApp='' ):
	global delimReg
	global isRequired_index
	if not parentApp == '':
		appReg = appReg + delimReg + parentApp
	if not childApp == '':
		appReg = parentApp + delimReg + appReg
	isRequired_index[appReg] = []
	return appReg

def structure():
	result = []
	global registeredAppsAll
	for raa in registeredAppsAll:
		if type(raa) == dict:
			result.append(raa)
			# print(raa)
	return result

theDelim = '|||'
appInfoScan = False # appInfo.py



# import blank
# blank.focus(focus())
# _.load()
# blank.registerSwitches()
# _.switches.process()
# _.switches.fieldSet('Input','active',True)
# _.switches.fieldSet('Input','value','one')

# _.appInfo[blank.focus(focus())] = _.appInfo[blank.focus()]
# _.appData[blank.focus(focus())] = _.appData[blank.focus()]
# __.constructRegistration(_.appInfo[blank.focus(focus())]['file'],blank.focus(focus()))





















