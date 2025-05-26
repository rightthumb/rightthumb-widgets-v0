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
	_.switches.register( 'File', '-f,-file' )
	# _.switches.register( 'Supporting', '-S,--s' )
	# _.switches.register( 'Table', '-table' )
	# _.switches.register( 'To', '-to' )
	# _.switches.register( 'Underscore', '-u' )
	# _.switches.register( 'Alpha', '-a' )
	pass


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
	'file': 'copy-fn-class.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'copy classes or functions to another python app',
	'categories': [
						'copy',
						'app',
						'python',
						'function',
						'fn',
						'class',
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
						_.hp('type D:\\tech\\hosts\\VULCAN\\projects\\copy-fn-class\\to-add.txt | p copy-fn-class -from D:\\tech\\programs\\python\\src\\unity\\_rightThumb\\_base3\\__init__.py -to _func.py'),
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Duration', _.timeFuture )
	
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


def find_supporting(file):
	spent=[]
	support=[]
	index = _.find_all( file, '(' )
	fns = _.find_all( file, 'def ' )
	index.reverse()
	for i in index:
		done=False
		ii = i
		function=[]
		while not done:
			ii-=1
			if not file[ii] in '._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
				done=True
			elif not file[ii] == ' ':
				function.append(file[ii])
		pass
		if not '.' in function:
			if not ii-len('def ')+1 in fns:
				function.reverse()
				fn = ''.join(function)
				if fn and not fn in ['childScript','__import__','abs','all','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']:
					if not fn in spent:
						spent.append(fn)
						support.append(fn)

	return {'list':support,'add':file}

process_fc=[]
def process(subject):
	global base
	add=''

	if not subject.startswith('class ') and not subject.startswith('def '):
		if 'class '+subject in table:
			subject = 'class '+subject
		elif 'def '+subject in table:
			subject = 'def '+subject
		else:
			return None
	sub=subject
	if not sub in table:
		return base
	else:
		addedFunctions.append(sub)
		process_fc.append(sub)
		# _.cp(['deleted:',sub],'green')
		s = table[sub]['start']-1
		e = table[sub]['end']-1
		for i,line in enumerate(base):
			if i >=s and i <= e:
				add += line

	base = base.replace( add,'' )
	toAdd=[]
	# if _.switches.isActive('Supporting'):
	if 1:
		support = find_supporting(base)
		for sup in support['list']:
			c = 'class '+sup
			f = 'def '+sup
			if c in table:
				# _.cp( ['supporting:',c], 'yellow' )
				toAdd.append(c)
			if f in table:
				toAdd.append(f)
				# _.cp( ['supporting:',f], 'yellow' )

		for ta in toAdd:
			# _.pr(ta)
			_.cp([ta],'red')
			# ask='n'
			# _.pr('delete supporting '+ta+':')
			# ask = input(': ')
			# if 'y' in ask.lower():
			#     process(ta)






def action():
	load()
	global base
	global process_fc
	focus()
	for i,subject in enumerate( _.isData(r=1) ):
		subject = _str.cleanBE(subject,' ')
		if subject:
			process(subject)
	for sub in process_fc:
		_.cp(['deleted:',sub],'cyan')
	_.saveText(base,_.switches.values('File')[0])
	_.cp(['Saved:',_.switches.values('File')[0]],'green')



def load():
	global table
	global base

	_inFunc = _.regImp( __.appReg, 'inFunc' )
	_inFunc.switch('Log')
	_inFunc.switch('Files',_.switches.values('File')[0])
	table = _inFunc.action().copy()
	base = _.getText( _.switches.values('File')[0], raw=True )
	

addVars=''
addedVars=[]
addedVarsCode=[]
addedFunctions=[]


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







