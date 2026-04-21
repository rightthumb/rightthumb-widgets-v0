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
	_.switches.register( 'ColorPrint', '-color', 'cyan This is a test' )
	_.switches.register( 'Replace', '-replace', '"\'haystack\' \'needle\' \'new\'"' )
	_.switches.register( 'NoPrint', '--c' )
	_.switches.register( 'isFile', '-fi' )
	# _.switches.register( 'Path-Cleaner', '-path' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='name', description='Files' )
	_.switches.register( 'Single-File', '-singlefile' )

	_.switches.register('JQ-Filter', '-jq-filter')
	_.switches.register('JQ-Map', '-jq-map')
	_.switches.register('JQ-Reduce', '-jq-reduce')
	_.switches.register('JQ-Select', '-jq-select')
	_.switches.register('JQ-Keys', '-jq-keys')
	_.switches.register('JQ-Values', '-jq-values')
	_.switches.register('File-Contains', '-fc,--file-contains', 'FolderPath')

	_.switches.register('Input-Multipurpose', '-i', 'file or string')
	_.switches.register('Execute-Framework-Function', '-fn', '(`auto: _. __. _v. _str.` ) ex: -i 1w -fn _.ago -t r:_.fd | ex:  -fn _.md  -i file.txt || (--c) (-t _.fd ) (fd = friendlyDate)')

	_.switches.register( 'Triggers-And-Settings', '-t', '`na;i;r`  `na=not auto (auto is file stuff, float to date etc), i=input, r=result(default is r)`ex: -t na:isFile | -t na (no auto result trigger) | -t _.fd | -i 1w -fn _.ago -t _.fd' )
	_.switches.register("Strip-/'", '-sq')
	_.switches.register("ReadSwitch", '-rs,-cron', 'crontab -l | p script-helper -rs')
	# _.switches.register( 'Triggers-And-Settings', '-t', '`i=input, r=result(default is r)`ex: -t _.fd | -t r:_.friendlyDate  |  i:_.isFileAdvanced;r:_.friendlyDate (i=input, r=result `i` by itself skips default _.isFile trigger r: runs trigger on result)' )
	

_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	# 'app': '7facG-jo0Cxk',
	'file': 'script-heplper.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'usage in .bat .sh etc',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'programming',
						'script',
						'code',
						'',
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
						_.hp('p script-helper -replace "\'C:\\\\Users\\\\Scott\\\\OneDrive\\\\Pictures\\\\terminal-wallpaper\\\\\' \'\\\\\\\\\' \'\\\\\'"'),
						_.hp(''),
						_.hp('.bat'),
						_.hp('    call p script-helper -replace "\'%b%\' \'/\' \'\\\\\'" > %tmpf%'),
						_.hp('    SET /p b=<%tmpf%'),
						_.hp(''),
						_.hp('p script-helper -jq-reduce -f filename.json'),
						_.hp('p script-helper -jq-select -f filename.json'),
						_.hp('p script-helper -jq-keys -f filename.json'),
						_.hp('p script-helper -jq-values -f filename.json'),
						_.hp(''),
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
# START

import json
import simplejson

def jq_filter(json_obj, key):
	"""
	Filter JSON objects by a specific key.
	
	Parameters:
	json_obj (list/dict): The JSON data.
	key (str): The key to filter by.
	
	Returns:
	list: A list of values corresponding to the given key.
	"""
	if isinstance(json_obj, dict):
		return [json_obj.get(key)]
	elif isinstance(json_obj, list):
		return [item.get(key) for item in json_obj if key in item]
	return []

def jq_map(json_obj, func):
	"""
	Apply a function to each item in the JSON array.
	
	Parameters:
	json_obj (list): The JSON array.
	func (function): A function to apply to each item.
	
	Returns:
	list: A list of results after applying the function.
	"""
	if isinstance(json_obj, list):
		return [func(item) for item in json_obj]
	return []

def jq_reduce(json_obj, func, initial):
	"""
	Reduce a JSON array to a single value using a function.
	
	Parameters:
	json_obj (list): The JSON array.
	func (function): A function to apply for reduction.
	initial: The initial value for reduction.
	
	Returns:
	The result of reduction.
	"""
	if isinstance(json_obj, list):
		from functools import reduce
		return reduce(func, json_obj, initial)
	return initial

def jq_select(json_obj, condition):
	"""
	Select items from a JSON array that match a condition.
	
	Parameters:
	json_obj (list): The JSON array.
	condition (function): A function that returns True for items to select.
	
	Returns:
	list: A list of items that match the condition.
	"""
	if isinstance(json_obj, list):
		return [item for item in json_obj if condition(item)]
	return []

def jq_keys(json_obj):
	"""
	Get all keys in a JSON object.
	
	Parameters:
	json_obj (dict): The JSON object.
	
	Returns:
	list: A list of keys in the JSON object.
	"""
	if isinstance(json_obj, dict):
		return list(json_obj.keys())
	elif isinstance(json_obj, list):
		return [list(item.keys()) for item in json_obj if isinstance(item, dict)]
	return []

def jq_values(json_obj):
	"""
	Get all values in a JSON object.
	
	Parameters:
	json_obj (dict): The JSON object.
	
	Returns:
	list: A list of values in the JSON object.
	"""
	if isinstance(json_obj, dict):
		return list(json_obj.values())
	elif isinstance(json_obj, list):
		return [list(item.values()) for item in json_obj if isinstance(item, dict)]
	return []

def load_json_file(filename):
	with open(filename, 'r') as file:
		return simplejson.load(file)

import os


## New Input Function Trigger stuff    <- START
## New Input Function Trigger stuff    <- START
def blank(arg):
	return arg
def fnLoad(rr):
	toTest = '_. __. _v. _str.'
	toTest = toTest.strip()
	while '  ' in toTest: toTest = toTest.replace('  ',' ')
	test = toTest.split(' ')
	test.insert(0,'')
	fn = blank
	for i,t in enumerate(test):
		try:
			fn = eval(t+rr)
			# print(t+rr)
			break
		except Exception as e:
			pass
	return fn

def autoTrigger(data):

	test = {
		'float': '_.friendlyDate',
	}

	# clean space delim functions
	for k in test.keys():
		test[k] = test[k].strip()
		while '  ' in test[k]: test[k] = test[k].replace('  ',' ')


	dataType = str(type(data)).split("'")[1]
	if not dataType in test: return data


	for i,t in enumerate( test[dataType].split(' ') ):
		try:
			fn = eval(t)
			data = fn(data)
			break
		except Exception as e:
			pass
	return data

def pr1(arg):
	# print('arg',arg)
	global aSettings
	if 'r' in aSettings:
		fn = fnLoad(aSettings['r'])
		# eval(aSettings['r'])
		# print('|'+aSettings['r']+'|')
		# fn = _.friendlyDate
		result = fn(arg)
		if type(result) == list:
			_.pr(line=1,c='green')
			_.pr(arg,c='yellow')
			_.pr()
			for r in result:
				_.pr(r,c='cyan')
			
		else:
			if not 'na' in aSettings:
				# ogResult = result
				result = autoTrigger(result)
				# if not ogResult == result:
				# 	_.pr(ogResult,c='yellow')
			_.pr(result,c='cyan')
	else:
		_.pr(arg,c='yellow')
	if _.linePr:
		_.pr(line=1,c='green')
aSettings = {}
## New Input Function Trigger stuff    <- END
## New Input Function Trigger stuff    <- END

def action():
	if _.switches.isActive("ReadSwitch"):
		for line in _.isData(2):
			if line.strip().startswith('#'):
				_.pr()
				_.pr(line=1,c='green')
				_.pr()
			if '*' in line:
				_.pr()
				_.pr()
			line = line.replace(' -','\n    -')
			_.pr(line)
		return
	if _.switches.isActive("Strip-/'"):
		for line in _.isData():
			if _.showLine(line):
				line = line.replace("\\'","'")
				_.pr(line)
	
		return None
	

	if _.switches.isActive('ColorPrint'):
		val = _.switches.values('ColorPrint')
		color = val[0]
		val.pop(0)
		toPrint = ' '.join(val)
		_.pr(toPrint, c=color)
		return


	## New Input Function Trigger stuff    <- START
	## New Input Function Trigger stuff    <- START
	global aSettings
	# Execute-Framework-Function  Input-Multipurpose
	if _.switches.isActive('Triggers-And-Settings'):
		default = 'r'
		stringKeys = [
			'na',
		]
		keys = [
			'na',
			'i',
			'r',
		]
		dic = {
			# 'nt': 'No-Trigger',
		}
		for aa in _.switches.values('Triggers-And-Settings'):
			aa = aa.replace(' ','')
			for a in aa.split(';'):
				sub = a.split(':')
				sub[0] = sub[0]
					
				if len(sub) == 1:
					if sub[0] in keys:
						if sub[0] in stringKeys:
							aSettings[ sub[0] ] = ''
						else:	
							aSettings[ sub[0] ] = True
					else:
						if sub[0].lower() in dic:
							aSettings[ default ] = dic[sub[0].lower()]
						else:
							aSettings[ default ] = sub[0]

				else:
					aSettings[ sub[0] ] = sub[1]
					if sub[1].lower() in dic:
						aSettings[ sub[0] ] = dic[sub[1].lower()]
					
				# if a in dic:
				# 	aSettings[ dic[a] ] = True
				# else:
				# 	aSettings[a] = True
	# print(aSettings)
	if _.switches.isActive('Input-Multipurpose') and not _.switches.isActive('Execute-Framework-Function'):
		for im in _.switches.values('Input-Multipurpose'):
			im = _.ci( im )
			if not 'i' in aSettings:
				if 'na' in aSettings:
					if not'isFile' in aSettings['na']: im = _.isFile( im )
				else:
					im = _.isFile(im)
			elif type(aSettings['i']) == bool: pass
			elif aSettings['i'] == 'nt': pass
			else:
				tr = fnLoad(aSettings['i'])
				im = tr(im)
			pr1(im)
		return im


	if _.switches.isActive('Execute-Framework-Function'):
		fn = fnLoad(_.switches.value('Execute-Framework-Function'))
		if _.switches.isActive('Input-Multipurpose'):
			for im in _.switches.values('Input-Multipurpose'):
				if not 'No-Trigger' in aSettings:
					im = _.ci( im )
					if not 'i' in aSettings:
						if 'na' in aSettings:
							if not'isFile' in aSettings['na']: im = _.isFile( im )
						else:
							im = _.isFile(im)
					elif type(aSettings['i']) == bool: pass
					elif aSettings['i'] == 'nt': pass
					else:
						tr = fnLoad(aSettings['i'])
						im = tr(im)
				ogIm = im
				result = fn(im)
				if not ogIm == result:
					if not _.switches.isActive('NoPrint'):
						_.pr(line=1,c='green')
						_.pr(ogIm,c='yellow')
						_.pr()

				if not _.switches.isActive('NoPrint'):
					pr1(result)
		else:
			result = fn()
			if not _.switches.isActive('NoPrint'):
				pr1(result)
		return result
		
	if _.switches.isActive('File-Contains'):
		values = _.switches.values('File-Contains')
		for i,v in enumerate(values):
			values[i] = v.strip().lower()
		val = ' '.join(values)
		
		valid = False
		for path in _.switches.values('Files'):
			file = _.getText( path, raw=True )
			# print(file)
			if not values:
				if len(file.strip()) > 0:
					valid = True
					break
			elif 'path' in val and 'fo':
				for line in file.split('\n'):
					line = line.strip()
					# print(line)
					if os.path.isdir(line):
						valid = True
						break
		if valid:
			print('yes')
		else:
			print('no')
		return valid
	
	## New Input Function Trigger stuff    <- END
	## New Input Function Trigger stuff    <- END











	if _.switches.isActive('JQ-Filter'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			key = _.switches.value('JQ-Filter')
			result = jq_filter(json_data, key)
			_.pr(simplejson.dumps(result, indent=4))
			return

	if _.switches.isActive('JQ-Map'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			result = jq_map(json_data, lambda x: x.get('age'))
			_.pr(simplejson.dumps(result, indent=4))
			return

	if _.switches.isActive('JQ-Reduce'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			result = jq_reduce(json_data, lambda acc, x: acc + x.get('status', 0), 0)
			_.pr(result)
			return

	if _.switches.isActive('JQ-Select'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			result = jq_select(json_data, lambda x: x.get('status', 0) == 2)
			_.pr(simplejson.dumps(result, indent=4))
			return

	if _.switches.isActive('JQ-Keys'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			result = jq_keys(json_data)
			_.pr(simplejson.dumps(result, indent=4))
			return

	if _.switches.isActive('JQ-Values'):
		files = _.switches.values('Files')
		for file in files:
			json_data = load_json_file(file)
			result = jq_values(json_data)
			_.pr(simplejson.dumps(result, indent=4))
			return




	if _.switches.isActive('Files') or _.isData():

		if _.switches.isActive('Single-File'):
			path = ' '.join( _.switches.values('Files') )
			path = __.path(  path  )
			_.pr( path )
			return None
			
		for path in _.isData():
			path = __.path(  path  )
			_.pr( path )


		return None


	# indexes
	# relevant_OC
	# inIndex
	#--> replace string fix {:replace:}
	if _.switches.isActive('Replace'):
		dump =' '.join(_.switches.values('Replace'))
		# _.pr(dump)
		_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
		_code.imp.validator.register( dump, 'javascript' )
		status = _code.imp.validator.createIndex( dump, 'javascript', skipLoad=True, simple=False, B=True )

		Q = []
		i=-1
		for ii,x in enumerate(_code.imp.validator.identity['identity']):
			i+=1
			o = x
			c = _code.imp.validator.identity['location']['open'][o]
			l = _code.imp.validator.getLabel( o, string=True )
			text=_code.imp.validator.assetSnipet( o, c )
			text=text[1:]
			text=text[:-1]
			Q.append(text)
			# _.pr(i,text)
		pass
		a=Q[0]
		b=Q[1]
		c=Q[2]
		if _.switches.isActive('isFile'):
			path=a
			a=_.getText(a,raw=True)
		if b=='\\\\':
			b='\\'
		if c=='\\\\':
			c='\\'
		if b=='\\\\\\\\':
			b='\\\\'
		if c=='\\\\\\\\':
			c='\\\\'



		i=0
		while b in a:
			i+=1; a=a.replace(b,c);
			if i>1000: break;
		if not _.switches.isActive('NoPrint'):
			_.pr(a)
		if _.switches.isActive('isFile'):
			_.saveText( a, path )
		return a
	_.e('use a switch\n p script-heplper ?? c')



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





