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
# import sys

# if not sys.stdin.isatty():
#     LINES = [line.strip() for line in sys.stdin if line.strip()]
# else:
#     LINES = []
##################################################
class Meta_Namespace():
	def __init__( self ):
		pass
dot=Meta_Namespace
fn=Meta_Namespace()
switch_skimmer = Meta_Namespace()
switch_skimmer.scan = {}
##################################################
switchTableSpentPrint = []
##################################################
# App Help Menu Switch Grouping
SwitchGroup_Help = Meta_Namespace()
SwitchGroup_Help.Delim = ''
SwitchGroup_Help.Group = '>'
SwitchGroup_Help.SubGroup = '>' # if this len 1: SwitchGroupDepth +=1
SwitchGroup_Help.Group_After = ' | \u25BD Group \u25BD '
SwitchGroup_Help.SubGroup_After = ' | \u25BD SubGroup cnt\u25BD '
SwitchGroup_Help.NoGroup_After = '  \u25BD Switches \u25BD '
SwitchGroup_Help.NoGroup = '-'
SwitchGroup_Help.PostLabel = '  '
SwitchesModifier = Meta_Namespace()
SwitchesModifier.Trigger = {}
SwitchesModifier.PrintActive = True
appInfoAcquiredData = { 'app': '', 'focus': '', 'data': None }

# HasSwitchSubGroup search for in framework

##################################################



import sys
from io import StringIO

if not sys.stdin.isatty():
	stdin_data = sys.stdin.read()
	sys.stdin = StringIO(stdin_data)  # Replace with in-memory stream
	# PIPE = [line for line in sys.stdin if line]
	PIPE = [line.rstrip() for line in sys.stdin]
	sys.stdin.seek(0)  # Reset pointer for reuse
else:
	PIPE = []






##################################################
ForcePipe = False
import sys
if '--pipe' in sys.argv:
	if not sys.stdin.isatty():
		ForcePipe = sys.stdin.read()
		if type(ForcePipe) == str:
			ForcePipe = ForcePipe.split('\n')
		

##################################################

# earthy_tones oceanic pastel warm_bold autumn midnight
# spring earthy_tones oceanic pastel warm_bold autumn
# midnight spring2 volcano frosty desert forest rainbow
# mystic industrial rustic sci_fi victorian retro
isData_Switches = {}
CodeTheme = 'retro'

##################################################
def isGui():
	import platform
	if platform.system() == "Windows":
		return True
	else:
		display_var = os.getenv('DISPLAY')
		if display_var:
			return True
	return False
##################################################
def Form(form):
	from _rightThumb._forms import genForm
	results = genForm(form)
	return results
#################################################
prFn  = None
def pr( *args, **kwargs ):
	global prFn
	if prFn is None:
		from _rightThumb._base3 import print_
		prFn = print_
	return prFn( *args, **kwargs )
#################################################
startTraceRecords = []
def startTrace(search='widgets'):
	global startTraceRecordsSearch
	startTraceRecordsSearch = search

	import sys
	def trace_calls(frame, event, arg):
		if event == 'call':
			global startTraceRecordsSearch
			global startTraceRecords
			code = frame.f_code
			func_name = code.co_name
			func_line_no = frame.f_lineno
			filename = code.co_filename
			if not startTraceRecordsSearch:
				startTraceRecords.append({'function':func_name,'line':func_line_no,'file':filename})
			elif type(startTraceRecordsSearch) == str and startTraceRecordsSearch.strip() and startTraceRecordsSearch in func_name:
				startTraceRecords.append({'function':func_name,'line':func_line_no,'file':filename})

				# print(f'Calling function: {func_name} in {filename}:{func_line_no}')
		return trace_calls

	sys.settrace(trace_calls)

def endTrace(functions=None,a=False):
	sys.settrace(None)
	table = {}
	for record in startTraceRecords:
		shouldPrint = True
		if functions is not None:
			shouldPrint = False
			for file in functions:
				if record['file'].endswith(file):
					for function in functions[file]:
						if record['function'] == function:
							shouldPrint = True
		if shouldPrint:
			if a:
				print(f'{record["function"]} in {record["file"]}:{record["line"]}')
			else:
				if not record['file'] in table:
					table[record['file']] = {}
				if not record['function'] in table[record['file']]:
					table[record['file']][record['function']] = 0
				if table[record['file']][record['function']] == 0:
					print(f'{record["function"]} in {record["file"]}:{record["line"]}')
#################################################

import sys
import json
class SwitchManager:
	def __init__(self, command=None, Switches=None, Triggers=None):
		if isinstance(command, int):
			command = sys.argv[command:]
		elif isinstance(command, str):
			command = command.replace('  ', ' ').split(' ')
		elif not command:
			command = sys.argv

		self.command = command
		self.app = command[0]
		self.args = command[1:]

		if Switches is None:
			Switches = {}
		if Triggers is None:
			Triggers = {}

		self.triggers = {**Triggers}
		self.switchesRegister = self._flatten_switches(Switches)
		self.used = {}
		self._Values = {}
		self.usage = {}
		self.instances = {}

		self.flag_to_key = {}
		for key, val in self.switchesRegister.items():
			self.used[key] = False
			self._Values[key] = []
			if isinstance(val, str):
				val = val.strip().replace('  ', ' ').replace(' ', ',')
				self.switchesRegister[key] = val
			for flag in self.switchesRegister[key].split(','):
				self.flag_to_key[flag] = key

		self.parse()

	def _flatten_switches(self, switches):
		flat = {}
		for group_or_key, val in switches.items():
			if isinstance(val, dict):
				flat.update(val)
			else:
				flat[group_or_key] = val
		return flat

	def _clean_quotes(self, value):
		if not isinstance(value, str):
			return value
		for quote in ["'", '"']:
			if value.startswith(quote * 2) and value.endswith(quote * 2):
				value = value[2:-2]
			elif value.startswith(quote) and value.endswith(quote):
				value = value[1:-1]
		return value

	def parse(self):
		current_switch = None
		current_key = None
		i = 0

		while i < len(self.args):
			arg = self.args[i]

			# Handle --flag=value format
			if arg.startswith('--') and '=' in arg:
				flag, val = arg.split('=', 1)
				key = self.flag_to_key.get(flag)
				if key:
					current_key = key
					current_switch = flag
					self._register_usage(key, current_switch)
					values = val.split(',')
					for v in values:
						value = self.triggers[key](v) if key in self.triggers else v
						value = self._clean_quotes(value)
						self._Values[key].append(value)
						self.instances[key][current_switch].append(value)

			# Handle standalone flags like -pulldown or -m
			elif arg in self.flag_to_key:
				key = self.flag_to_key[arg]
				current_key = key
				current_switch = arg
				self._register_usage(key, current_switch)
				if self._Values[key] == []:
					self._Values[key] = True

			# Handle values passed after a flag
			elif current_key and current_switch:
				if self._Values[current_key] is True:
					self._Values[current_key] = []
				value = self.triggers[current_key](arg) if current_key in self.triggers else arg
				value = self._clean_quotes(value)
				self._Values[current_key].append(value)
				self.instances[current_key][current_switch].append(value)

			# Orphan value (no active flag) — ignored, or could log
			else:
				pass

			i += 1


	def _register_usage(self, key, flag):
		self.used[key] = True
		if key not in self.instances:
			self.instances[key] = {}
		if flag not in self.instances[key]:
			self.instances[key][flag] = []
		if key not in self.usage:
			self.usage[key] = []
		if flag not in self.usage[key]:
			self.usage[key].append(flag)

	def isActive(self, name):
		return self.used.get(name, False)

	def values(self, name):
		val = self._Values.get(name, [])
		if val is True:
			return []
		return val

	def value(self, name):
		vals = self.values(name)
		if len(vals) == 1:
			return vals[0]
		return ','.join(vals)

	def Values(self, name, instance=None):
		if name not in self.instances:
			return []
		if instance is not None:
			return self.instances[name].get(instance, [])
		return self.values(name)

	def strip(self):
		return [item for item in self.command if item not in self.flag_to_key]

	def validate(self):
		print('___________\nApp:')
		print(self.app)
		print('___________\nUsed:')
		print(json.dumps(self.used, indent=4))
		print('___________\nValues:')
		print(json.dumps(self._Values, indent=4))
		print('___________\nUsage:')
		print(json.dumps(self.usage, indent=4))
		print('___________\nInstances:')
		print(json.dumps(self.instances, indent=4))

	def dump(self):
		return {
			'command': self.command,
			'app': self.app,
			'used': self.used,
			'values': self._Values,
			'usage': self.usage,
			'instances': self.instances
		}


Switches = SwitchManager
#################################################




preSwitches = []
site_url=None
autoCreationConfiguration = {
							'backup': True,
							'logs': True,
							'folders': True,
							'created': { '_vars': 0 },
}

settings_table = {
					#t)--> edit: 1661227949.7667239
					'receipt-log': True,
					'receipt-file': True,
					'default-switches': True,
}
UnixCopy = 'xsel'
truePath = False
truePath = True
isHeaders = {
	# IS(path, 'gz')
	'gzip': '1F 8B 08 08',
	'docx': [
		'50 4B 03 04',
		'50 4B 05 06',
	],
	'isCrypt': '41 45 53 02 00 00 1B',
	'gz': '1F 8B 08 08',
	'bz2': '42 5A 68',
}
import time,signal,sys,platform
tz = str(time.strftime("%z")).replace(':','')
try:
	signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
except:
	sys.exit(0)

banner=None
def _local_(do): print('not registered')


def name(path):
	path=path(path)
	par=path.split(os.sep)
	par.reverse()
	app=par[0]
	fo=par[1]
	root=par[2]
	app=app.replace('.py','')
	if app == '__init__': app=root+'.'+fo
	return app



def settings( subjects, d=None, val='71e9-a678' ):
	results = []
	for subject in subjects:
		results.append(  setting( subject, val, d )  )
	return results

def setting( subject, val='71e9-a678', d=None, default=None ):
	global settings_table

	if not default is None:
		d = default

	if not val == '71e9-a678':
		settings_table[subject] = val

	if not subject in settings_table:
		return d
	
	return settings_table[subject]


releaseAcquiredData = True

table_b_print = True

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

v = Meta_Namespace()

LOOP = {}

def pathList( *paths ):
	# os = imp('os')
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
		# os = imp('os')
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












# import os
# import sys
# import importlib

# Helper function to dynamically import modules using dot notation
def dots(path):
	def _dots_(pth):
		try:
			exec(pth)
			return True
		except Exception:
			return False

	parts = path.split('.')
	exec(f'global {parts[0]}')
	
	if _dots_(path):
		return eval(parts[0])

	pre, temp_path = [], []
	for i, segment in enumerate(parts):
		pre = temp_path.copy()
		temp_path.append(segment)
		namespace_prefix = '.'.join(pre)
		current_path = '.'.join(temp_path)

		if i == len(parts) - 1:
			# Import the final segment from the package
			exec(f'from {namespace_prefix} import {parts[-1]}')
			assignment = f'{path} = {parts[-1]}'
		else:
			# Create a dynamic namespace if it doesn't exist
			assignment = f'{current_path} = Meta_Namespace()'

		if not _dots_(current_path):
			exec(assignment)
			if i == len(parts) - 1:
				return eval(parts[0])


# Import helpers
imp_table = {}

def imp(subject, imp_table_testing=False):
	try:
		return imp_run(subject, imp_table_testing)
	except ImportError:
		imp_install(subject)
		try:
			return imp_run(subject, imp_table_testing)
		except ImportError:
			imp_run2(subject)

# Install missing packages using pip
def imp_install(mod):
	mod = mod.split('.')[0]
	
	package_mapping = {
		'all': {},
		'win': {
			'magic': 'python-magic-bin==0.4.14',
		},
		'linux': {
			'magic': 'python-magic',
		},
	}

	# Check platform-specific package mapping
	if sys.platform == 'win32' and mod in package_mapping['win']:
		mod = package_mapping['win'][mod]
	elif sys.platform != 'win32' and mod in package_mapping['linux']:
		mod = package_mapping['linux'][mod]

	# Install the package
	os.system(f'pip install {mod} >nul 2>&1')

# Run secondary import
def imp_run2(subject):
	global importlib
	global imp_table
	if importlib is None:
		import importlib
	exec(f'import {subject}')
	imp_table[subject] = eval(subject)

# Main import runner
def imp_run(subject, imp_table_testing=False):
	global importlib
	if '.' in subject and '_rightThumb' not in subject:
		return dots(subject)

	global imp_table
	if subject in imp_table:
		return imp_table[subject]

	if importlib is None:
		import importlib

	try:
		imp_table[subject] = importlib.import_module(subject)
		if imp_table_testing:
			print('Module imported successfully:', subject)
		return imp_table[subject]
	except ImportError:
		if imp_table_testing:
			print('Failed to import module:', subject)
		return None

















# def dots(path):
# 	def _dots_(pth):
# 		try: exec(pth); return True;
# 		except Exception as e: return False;
# 	rts=path.split('.'); exec('global '+rts[0]);
# 	if _dots_(path): return eval(rts[0])
# 	pre=[]; thp=[];
# 	for i,seg in enumerate(rts):
# 		pre=thp.copy(); thp.append(seg); npre='.'.join(pre); npath='.'.join(thp)
# 		if i == len(rts)-1:
# 			exec('from 1 import 2'.replace('1',npre).replace('2',rts[-1]))
# 			f='3=2'.replace('1',npre).replace('2',rts[-1]).replace('3',path)
# 		else: f='1=Meta_Namespace()'.replace('1',npath);

# 		if not _dots_(npath):
# 			exec(f)
# 			if i == len(rts)-1: return eval(rts[0]);


try:
	importlib
except Exception as e:
	importlib = None
# imp_table = {}
# def imp( subject, imp_table_testing=False ):
# 	try:
# 		return imp_run( subject, imp_table_testing )
# 	except:
# 		imp_install(subject)
# 		try:
# 			return imp_run( subject, imp_table_testing )
# 		except:
# 			try:
# 				imp_run2( subject )
# 			except:
# 				print('unable to import:',subject)

# def imp_install(mod):
# 	mod = mod.split('.')[0]
# 	try:
# 		exec('import os')
# 	except Exception as e:
# 		raise e
# 	# print()
# 	# print('__.imp_install('+mod+')')
# 	# print()
# 	if '.' in mod: mod = mod.split('.')[0]

# 	dic = {
# 			'all': {},
# 			'win': {},
# 			'linux': {},
# 	}

# 	dic['win']['magic'] = 'python-magic-bin==0.4.14'
# 	dic['linux']['magic'] = 'python-magic'

# 	if       sys.platform == 'win32' and mod in dic['win']: mod = dic['win'][mod]
# 	elif not sys.platform == 'win32' and mod in dic['linux']: mod = dic['linux'][mod]
# 	elif mod in dic['linux']: mod = dic['all'][mod]


# 	if mod in dic: mod=dic[mod]

# 	os.system('pip3 install '+mod+' >nul 2>&1')
	
# 	# if sys.platform == 'win32':
# 	#     # os.system('pip3 install python-magic-bin==0.4.14')
# 	#     os.system('pip3 install '+mod+' >nul 2>&1')
# 	# else:

# 	#     def _pipy_(mod):
# 	#         mod0=mod
# 	#         try:
# 	#             import pip
# 	#             if '=' in mod: mod = mod.split('=')[0]
# 	#             pip.main(['install', mod])
# 	#         except: print('pip3 install '+mod0)
# 	#     import subprocess
# 	#     if len(subprocess.getoutput('sudo cat /etc/sudoers').split('\n')) > 3:
# 	#         try: os.system('sudo pip3 install '+mod+'  > /dev/null 2>&1')
# 	#         except: _pipy_(mod)
# 	#     else:
# 	#         try: os.system('pip3 install '+mod+'  > /dev/null 2>&1')
# 	#         except:_pipy_(mod)




# def imp_run2( subject ):
# 	global imp_table
# 	global importlib
# 	if importlib is None:
# 		import importlib
# 	exec( 'import '+subject )
# 	imp_table[subject] = eval(subject)

# def imp_run( subject, imp_table_testing=False ):
# 	# print(subject); sys.exit();
# 	if '.' in subject and not '_rightThumb' in subject: return dots(subject);
# 	global imp_table
# 	# if subject in imp_table: return imp_table[subject]
# 	global importlib
# 	if importlib is None:
# 		import importlib
# 		if imp_table_testing:
# 			print('\n\n\t\timport importlib\n\n')

# 	if not subject in imp_table:
# 		try:
# 			imp_table_tmp
# 		except Exception as e:
# 			pass
# 		else:
# 			del imp_table_tmp

# 		imp_table[subject] = importlib.import_module(subject)
# 		if imp_table_testing:
# 			print( 'imp.DID' )
# 		return imp_table[subject]

# 		# try:
# 		#     imp_table[subject] = importlib.import_module(subject)
# 		#     if imp_table_testing:
# 		#         print( 'imp.DID' )
# 		#     return imp_table[subject]
# 		# except Exception as e:
# 		#     if imp_table_testing:
# 		#         print( 'imp.NO' )
# 		#     return None
# 	if imp_table_testing:
# 		print( 'imp.YES' )
# 	return imp_table[subject]



on_exit_subjects = {}
def onExit(script,subject=None):
	global on_exit_subjects
	if subject is None:
		subject = uuid()
	on_exit_subjects[subject] = script
decompress_log = []
def isExit(fromKill=False):
	global on_exit_subjects
	global decompress_log
	for path in decompress_log:
		compress(path)

	for subject in on_exit_subjects:
		on_exit_subjects[subject]()
	if fromKill and not type(fromKill) == str:
		return True
	KILL()

def compress(path):
	os=imp('os.rename')
	os=imp('os.unlink')
	import gzip
	import shutil
	if IS(path,'gzip'): return False
	path = path(path)
	compressed_file_path = path
	original_file_path = path+'_temp'
	os.rename(path, original_file_path)
	with open(original_file_path, 'rb') as original_file:
		with gzip.open(compressed_file_path, 'wb') as compressed_file:
			shutil.copyfileobj(original_file, compressed_file)
	print(f"File compressed and saved to {compressed_file_path}")
	os.unlink(original_file_path)
def IS(path,check=1):
	path = path.strip()
	if not os.path.isfile(path): return False
	path = path2(path)
	global isHeaders
	if check in isHeaders.keys():
		check = isHeaders[check]
	header=" ".join(['{:02X}'.format(byte) for byte in     open( path, 'rb' ).read(32)    ])
	if check == 1: return header
	if type(check) == str:
		if header.startswith(check): return True
	elif type(check) == list:
		for c in check:
			if header.startswith(c): return True
	
	return False
def path( p, ab=True, pop=False, file=False, slash=None, folder=None, relative=False, fi=None, fo=None, fix=True, ln=None, r=None  ):
	if not r is None:
		relative = r
	os=imp('os.path.isfile')
	if relative:
		if not type(relative) == str:
			relative = os.getcwd()
		if relative.endswith('\\') or relative.endswith('/'):
			relative = relative[:-1]
		
		p = p.strip()
		if p.startswith(relative):
			p = p[len(relative)+1:]
		return p
	if not os.path.isfile(p) and not os.path.isdir(p): p = p.strip()
	if not os.path.isfile(p) and not os.path.isdir(p):
		if pop or folder:
			parts = p.split(os.sep)
			parts.pop(-1)
			p = os.sep.join(parts)
		if file:
			parts = p.split(os.sep)
			p = parts.pop(-1)
		return p
	os=imp('os.sep')
	p=p.replace(os.sep+os.sep,os.sep)
	if isWin or not pop: return _path_( p, ab, pop, file, slash, folder, fi, fo, fix, ln )
	# os=imp('os.path.abspath')
	# try: p1 = os.path.abspath(p)
	# except: pass
	os=imp('os.path.realpath')
	try: p1 = os.path.realpath(p)
	except: pass
	p2 = _path_( p, ab, pop, file, slash, folder, fi, fo, fix, ln )
	if p1 == p2:
		parts = p1.split(os.sep)
		parts.pop(-1)
		return os.sep.join(parts)
	return p1
path2=path
def _path_( p, ab=True, pop=False, file=False, slash=None, folder=None, fi=None, fo=None, fix=True, ln=None ):
	
	p_bk=p
	# fix used in fileBackup.py

	if not fo is None: folder=fo;
	if not folder is None: pop=folder;
	if not fi is None: file=fi;


	# os = vc.FIG.imp('os')
	# os = imp('os')
	os=imp('os.sep')
	try: os.path.abspath
	except Exception as e: os=imp('os.path.abspath')
	try: os.path.isfile
	except Exception as e: os=imp('os.path.isfile')
	try: os.path.isdir
	except Exception as e: os=imp('os.path.isdir')

	global isWin
	if not isWin:
		if p.startswith('/'):
			if   os.path.isdir(p): return p
			elif os.path.isfile(p): return p

	if ab:
		if os.path.isfile(p) or os.path.isdir(p):
			try: p = os.path.abspath(p)
			except: pass

	if fix and not os.path.isfile(p) and not os.path.isdir(p) and not os.sep in p and p:
		p = os.getcwd() +os.sep+ p
		return p



	if slash is None:
		slash = os.sep
	if not p:
		return p.replace(os.sep+os.sep,os.sep)
	# print(p)
	p = p.replace( chr(92), slash )
	p = p.replace( chr(47), slash )
	while slash+slash in p:
		p = p.replace(slash+slash,slash)
	if ab:
		if os.path.isfile(p) or os.path.isdir(p):
			try:
				p = os.path.abspath(p)
			except Exception as e:
				pass
	if isWin or (not ln is None and ln):
		global truePath
		if truePath:
			try:
				os=imp('os.path._getfinalpathname')
				p = os.path._getfinalpathname(p).lstrip(r'\?')
			except: pass
	try:
		if p_bk[1] == ':' and not p[1] == ':': p = p_bk
		if type(p) == str and len(p)>1 and p[1] == ':':
			p = p[0].upper() + p[1:]
	except: pass
	if type(p) == str and ( pop or file ):

		if type(pop) == int:
			i=0
			while not i == pop:
				i+=1
				p = path( p, pop=True, slash=slash )
				# print(p)
			if file:
				p = path( p, file=True, slash=slash )
			return p.replace(os.sep+os.sep,os.sep)
		parts = p.split(slash)
		parts.reverse()
		f = parts.pop(0)
		parts.reverse()
		p = str(slash).join(parts)
		if file:
			p = f
	return p.replace(os.sep+os.sep,os.sep)

def file( p ):
	# os = imp('os')
	p = p.replace( chr(92), os.sep )
	p = p.replace( chr(47), os.sep )
	if not os.sep in p:
		return p
	parts = p.split(os.sep)
	parts.reverse()
	f = parts.pop(0)
	return f


def fromYML(text):
	if os.path.isfile(text):
		text=getText(text)
	elif not '\n' in text and text.count(os.sep):
		return {}
	try:
		import yaml
		return yaml.safe_load(text.replace('\t','    '))
	except Exception as e:
		table = {}
		lines = text.split('\n')
		for line in lines:
			if ':' in line:
				key, value = line.split(':', 1)
				table[key.strip()] = value.strip()
			return table
def toYML(dic,path=None):
	text =  imp('yaml').dump( dic, sort_keys=False )
	if path is None:
		return text
	else:
		mkdir(path,isFile=True)
		f = open(path,'w')
		f.write(str(text))
		f.close()

getYML=fromYML
saveYML=toYML

def yamlSimp(text):
	return fromYML(text)


def get_first_char(filename):
	with open(filename, 'r') as file: first_char = file.read(1)
	return first_char

def getText(filename):
	with open(filename, 'r') as file: content = file.read()
	return content
def saveText(text, path):
	mkdir(path,isFile=True)
	try:
		with open(path, 'w') as file:
			file.write(text)
	except IOError:
		print("An error occurred while saving the text to the file.")


get_file_content=saveText


def mkdir(path,isFile=False,pop=False):
	if pop: isFile=True
	if isFile:
		os=imp('os.path.dirname')
		path = os.path.dirname(path)
	os=imp('os.path.abspath')
	os=imp('os.path.exists')
	absolute_path = os.path.abspath(path)
	if not os.path.exists(absolute_path):
		os.makedirs(absolute_path)
	return absolute_path

def getTable( file, simple=False ):
	os = imp('os.path.isfile')
	if not get_first_char(file) == '{' and  not get_first_char(file) == '[':
		if simple:
			return yamlSimp(file)
		return yamlSimp(saveText(file))
	
	
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		print('no json')
	if os.path.isfile(file):
		with open(file,'r', encoding="latin-1") as json_file:
			json_data = json.load(json_file)
	else:
		json_data = data_default(file=file,default=[]).default()
	return json_data

def saveTable( data, file, sk=False ):
	try:
		import simplejson
		json = simplejson
	except:
		pass
	try:
		import json
	except ImportError:
		print('no json')
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


# payloadCache = None
varFoldersCheck = False
myFileLocations_SKIP_VALIDATION = False




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
	startTime2 = int(str(startTime).split('.')[0])

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
	appInfoAcquiredData['app'] = x
	return x

def thisApp( file ):
	global slash
	f = file.split(slash)
	x = f[len(f)-1].replace('.py','')
	return x


def wsl(fi):
	subject = fi
	git_path = subject
	while '\\' in git_path:
		git_path = git_path.replace( '\\', '/' )
	print(git_path)
	git_path = git_path.replace( ':', '' )
	git_path = '/' + git_path
	wsl5 = '/mnt/'+ git_path[1].lower() + git_path[2:]
	wsl5=wsl5.replace(' ','\\ ')
	return wsl5


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
	appInfoAcquiredData['focus'] = appReg
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


class data_default:
	# __.data_default(file=theFile,default=[])
	def __init__( self, file, default ):
		self.dics = 'yml yaml i index indexes dex ls hash hashes tables logs lists indices meta setting settings dic s fig conf cnf'
		self.lists = 't tbl table cache log list lists l json config'
		while '  ' in self.dics:  self.dics  = self.dics.replace('  ',' ')
		while '  ' in self.lists: self.lists = self.lists.replace('  ',' ')
		self.file = file
		self.default_result = default
	def default( self ):

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.json' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.json' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.yml' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.yml' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x+'.yaml' ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x+'.yaml' ):
				return []

		for x in self.dics.split(' '):
			if self.file.lower().endswith( '.'+x ):
				return {}
		for x in self.lists.split(' '):
			if self.file.lower().endswith( '.'+x ):
				return []
		return self.default_result
# return __.data_default(file=theFile,default=[]).default()


class file_headers:
	# __.data_default(file=theFile,default=[])
	def __init__( self, path, default='' ):
		self.watermark = '''
## {R2D2919B742E} ##
###########################################################################
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
	- Scott Taylor Reph, RightThumb.com
###########################################################################
## {C3P0D40fAe8B} ##

'''.replace('\r','')
		self.path = path
		self.headers = {
							'functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'_functions.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'_fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'fn.php':  {'url':'https://apps.eyeformeta.com/templates/html/functions.php.txt'},
							'.folder.meta':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.h'},
							'.folder.meta.b':  {'url':'https://apps.eyeformeta.com/templates/html/.folder.meta.b'},
							'.txt': '__________________________________________________________________________________\n',
							'.sh': '#!/bin/bash\n',
							'.py': '#!/usr/bin/python3\n',
							'.bat': '@echo off\n',
							'.html': {'url':'https://apps.eyeformeta.com/templates/html/0.htm'},
							'.htm':  {'url':'https://apps.eyeformeta.com/templates/html/1.htm'},
							'.php':  {'url':'https://apps.eyeformeta.com/templates/html/0.php.txt'},
		}
		self.comment = {
							# '.js': '//',
							'.sh': '#',
							'.py': '#',
							'.bat': 'rem',
		}
		# self.nospace=['.sh']
		self.nospace=[]
		self.default_result = default
	def add_watermark(self,code):
		for ext in self.comment:
			if self.path.endswith(ext):
				for line in self.watermark.split('\n'):
					if len( line.replace(' ','').replace('\t','') ):
						code+=self.comment[ext]+' '+line+'\n'
					else:
						code+='\n'
		for ext in self.nospace:
			if self.path.endswith(ext):
				import _rightThumb._string as _str
				code = code.replace('\r','')
				code = _str.cleanBE(code,' ')
				code = _str.cleanBE(code,'\n')
				code = _str.replaceDuplicate(code,'\n')
				code = _str.cleanBE(code,'\n')
				code = _str.cleanBE(code,' ')
				code+='\n'

		return code.replace('\r','')


	def default( self ):
		for ext in self.headers:
			if self.path.endswith(ext):
				if type(self.headers[ext]) == dict:
					try:
						import requests
						page = requests.get(self.headers[ext]['url'])
						return page.content.decode("utf-8").replace('\r','')
					except Exception as e:
						return self.add_watermark(self.default_result)
						
				return self.add_watermark(self.headers[ext])
		return self.add_watermark(self.default_result)
# __.file_headers(path).default()


setting('myFileLocations-skip-validation',False)
setting('require-pipe',False)
setting('require-pipe||file',False)
setting('pre-error',False)
setting('switch-raw',[])
setting('require-list',[])
setting('receipt-log',True)
setting('receipt-file',True)
setting('fileBackup-secure_file',False)

#--> todo#> create app to scan to fix this situation below


# import os

def url( URL, data={}, d=None, raw=False, r=None,txt=None,text=None,t=None, dic=None, get=None ):
	headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
						"KHTML, like Gecko) Version/4.0 Safari/534.30"}
	if not txt is None: t=txt;
	if not text is None: t=text;
	import _rightThumb._string as _str

	if not r is None: raw=r;
	if not d is None: data=d;
	def _url_(data): return _str.do('.sh',data);
	# if not json is None and json:
	#     page=imp('requests.get').json(URL, headers=headers)
	#     return page
	if not get is None and get:

		page=imp('requests.get').get(URL, headers=headers)
		if raw: return page;
		if not t is None and t:
			result=page.text
		else:
			result=page.content
		for encodeing in 'UTF-8 ISO-8859-1 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
			try: return _url_(str(result,encodeing));
			except Exception as e: pass;
		return _url_(str(result))



	if not dic is None and dic:
		_dic={
			"href": "https://www.google.com/search?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
			"origin": "https://www.google.com",
			"domain": "google.com",
			"host": "www.google.com",
			"protocol": "https",
			"folder": "",
			"path": "google.com/search",
			"port": "443",
			"param": "?q=python+url+breakdown+port&rlz=1C1RXQR_enUS929US929&sxsrf=ALiCzsYDllCEJyfUu1VElV9U9f23zWE4PQ%3A1656037461579&ei=VSC1Yon9IsygkPIPwdGI-AM&ved=0ahUKEwjJ-4alhMX4AhVMEEQIHcEoAj8Q4dUDCA4&uact=5&oq=python+url+breakdown+port&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIICCEQHhAWEB06BwgAEEcQsAM6CggAEOQCELADGAE6BggAEB4QFjoICAAQHhAPEBY6BQgAEIYDOgUIIRCrAkoECEEYAEoECEYYAVBzWKsKYMMMaAFwAXgAgAFtiAHjA5IBAzQuMZgBAKABAcgBDcABAdoBBggBEAEYCQ&sclient=gws-wiz",
			"params": {},
			"username": "",
			"password": ""
		}

		return _dic



	page=imp('requests.post').post(URL, data = data)
	if raw: return page;
	if not t is None and t:
		result=page.text
	else:
		result=page.content
	for encodeing in 'ISO-8859-1 UTF-8 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
		try: return _url_(str(result,encodeing));
		except Exception as e: pass;
	return _url_(str(result))
page=url

print_=print
def getText2( theFile, raw=False, clean=False,  e=0, c=0 ):
	try: _str;
	except Exception as e:
		try: import _rightThumb._string as _str;
		except Exception as e: pass;
	os=imp('os.path.getmtime')
	if os.path.isfile(theFile): vv.opened_file_me[theFile] = os.path.getmtime( theFile );
	# HD.chmod(theFile)
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
	else:
		if not e:
			return None
		print_('(getText) Error: No File')
		sys.exit()
	if raw:
		txt = ''.join( lines )
		# txt = txt.replace( _v.slash+'n', '\n' )

		if clean:
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		if clean == 2:
			txt = txt.replace( '\t', ' ' )
			txt = _str.replaceDuplicate( txt, ' ' )
			while '\n \n' in txt:
				txt = txt.replace( '\n \n', '\n' )
			txt = _str.replaceDuplicate( txt, '\n' )
			txt = _str.cleanBE( txt, '\n' )
		return txt
	elif c > 0:
		if c > 1:
			txt = ''.join( lines )
			TXT = ''
			txt = txt.replace( "'\"\"\"'", '' )
			if '"""' in txt:
				for i,item in enumerate(txt.split('"""')):
					if i % 2 == 0:
						TXT+=item
			elif not '"""' in txt:
				TXT = txt
			while '    ' in TXT:
				TXT = TXT.replace( '    ', '\t' )
			while ' (' in TXT:
				TXT = TXT.replace( ' (', '(' )
			while ' =' in TXT:
				TXT = TXT.replace( ' =', '=' )
			while '= ' in TXT:
				TXT = TXT.replace( '= ', '=' )
			while 'def  ' in TXT:
				TXT = TXT.replace( 'def  ', 'def ' )
			while 'class  ' in TXT:
				TXT = TXT.replace( 'class  ', 'class ' )
			lines = TXT.split('\n')

		newLines = []
		for i,row in enumerate(lines):
			# row = row.replace('\n','')
			row = row.replace('\r','')
			
			if not c > 1:
				newLines.append(row)
			else:
				row = row.split('#')[0]
				test = row
				# while test.startswith(' ') or test.startswith('\t'):
				#   test = _str.cleanBE( test, ' ' )
				#   test = _str.cleanBE( test, '\t' )
				if not test.startswith('#') and len(test):
					newLines.append(row)


			


		return newLines

	elif clean:
		# lines = _str.replaceDuplicate( lines, '\n' )
		# lines = _str.cleanBE( lines, '\n' )
		for i,row in enumerate(lines):
			row = row.replace( '\n', '' )
			row = row.replace( '\r', '' )
			if type(clean) == int:
				row = row.replace( '\t', ' ' )
				row = _str.replaceDuplicate( row, ' ' )
				row = _str.cleanBE( row, ' ' )
			if clean == 3:
				row = ' ' + row + ' '

			# print_( row )
			lines[i] = row
		return lines
	else:
		return lines
try:
	os = imp('os.system')
	os = imp('os.sep')
	os = imp('os.listdir')
	os = imp('os.getcwd')
	os = imp('os.path.abspath')
	os = imp('os.path.isfile')
	os = imp('os.path.isdir')
	os = imp('os.name')
	os = imp('os.stat')
	sys = imp('sys.exit')
except:
	import os
	import sys





import sys

class VariableManager:
	def __init__(self):
		self.values = {}
		self.triggers = {}
		self.triggersAll = {}
		self.aliases = {}
		self.globals = {}

	def setGlobal(self, name):
		if name in self.aliases:
			name = self.aliases[name]
		self.globals[name] = True

	def g(self, name):
		self.setGlobal(name)

	def append(self, name, value, p=None, c=None, h=None, pp=True):
		return self.set(name, value, append=True, p=p, c=c, h=h, pp=pp)

	def appendIf(self, name, value, p=None, c=None, h=None, pp=True):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			if self.triggers[name](value):
				return self.set(name, value, append=True, p=p, c=c, h=h, pp=pp)
			else:
				return False
		else:
			return None

	def ai(self, name, value, p=None, c=None, h=None, pp=True):
		return self.appendIf(name, value, p=p, c=c, h=h, pp=pp)

	def setIf(self, name, value, p=None, c=None, h=None, pp=True):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			if self.triggers[name](value):
				return self.set(name, value, p=p, c=c, h=h, pp=pp)
			else:
				return False
		else:
			return None

	def If(self, name, value, p=None, c=None, h=None, pp=True):
		return self.setIf(name, value, p=p, c=c, h=h, pp=pp)

	def runTrigger(self, name, value):
		if name in self.aliases:
			name = self.aliases[name]
		if name in self.triggers:
			return self.triggers[name](value)

	def Trigger(self, name, value): return self.runTrigger(name, value)
	def t(self, name, value): return self.runTrigger(name, value)
	def run(self, name, value): return self.runTrigger(name, value)
	def check(self, name, value): return self.runTrigger(name, value)

	def set(self, name, value, append=False, a=None, p=None, c=None, h=None, pp=True):
		if a is not None:
			append = a
		if name in self.aliases:
			name = self.aliases[name]
		if append:
			if name not in self.values:
				self.values[name] = []
			self.values[name].append(value)
			if name in self.globals:
				setattr(self, name, self.values[name])  # Replaces exec
		else:
			self.values[name] = value
			if name in self.globals:
				setattr(self, name, value)  # Replaces exec
		if name in self.triggersAll:
			self.triggersAll[name](self.values[name])
		if name in self.triggers:
			self.triggers[name](value)
		for alias, actual_name in self.aliases.items():
			if actual_name == name:
				if name in self.globals:
					setattr(self, alias, self.values[name])  # Replaces exec
		if p:
			if not pp:
				return pr(value, c=c, h=h, p=pp)  # Using placeholder pr function
			else:
				pr(value, c=c, h=h)
		return self.values[name]

	def alias(self, name, *aliases):
		for a in aliases:
			if a in self.values:
				print(self.values)
				pr('Error: Alias already exists in values:', name, c='red')
				KILL()
			self.aliases[a] = name

	def value(self, name):
		if name in self.aliases:
			name = self.aliases[name]
		return self.values.get(name, None)

	def get(self, name): return self.value(name)
	def val(self, name): return self.value(name)

	def trigger(self, name, script, all=False):
		if name in self.aliases:
			name = self.aliases[name]
		if all:
			self.triggersAll[name] = script
		else:
			self.triggers[name] = script

# Placeholder `pr()` function (replace with your actual implementation)
# def pr(value, c=None, h=None, p=True):
#     print(f"{c.upper() if c else ''} {value}")


# appInfoAcquiredData  app focus data

def vmTrigger_payloadCache(value):
	global appInfoAcquiredData
	appInfoAcquiredData['data'] = value

VM = VariableManager
Store = VariableManager
Vars = VariableManager
store = VariableManager()
store.set('payloadCache', None)
store.alias('payloadCache', 'data','payload','records')
store.trigger('payloadCache', vmTrigger_payloadCache, all=True)


def KILL():
	isExit(fromKill=True)
	os = imp('os._exit')
	os._exit(1)