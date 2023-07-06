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
	# _.switches.register( 'Table', '-table' )
	_.switches.register( 'From', '-from' )
	_.switches.register( 'To', '-to' )
	_.switches.register( 'Underscore', '-u' )
	_.switches.register( 'Alpha', '-a' )
	_.switches.register( 'Supporting', '-S,--s' )
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


def find_supporting(file,change):
	change = change.replace('def ','')
	change = change.replace('class ','')
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
			# test = ii-len('def ')
			# _.pr(test)
			# _.pr(fns)
			if not ii-len('def ')+1 in fns:
				function.reverse()
				fn = ''.join(function)
				if fn and not fn in ['childScript','__import__','abs','all','any','ascii','bin','bool','breakpoint','bytearray','bytes','callable','chr','classmethod','compile','complex','delattr','dict','dir','divmod','enumerate','eval','exec','filter','float','format','frozenset','getattr','globals','hasattr','hash','help','hex','id','input','int','isinstance','issubclass','iter','len','list','locals','map','max','memoryview','min','next','object','oct','open','ord','pow','print','property','range','repr','reversed','round','set','setattr','slice','sorted','staticmethod','str','sum','super','tuple','type','vars','zip']:
					if not fn in spent:
						spent.append(fn)
						# _.pr(fn)
						support.append(fn)
					# _.pr(fn,function)
					# new=''
					# i=-1
					# while not i == len(file)-1:
					#     i+=1
					#     ch = file[i]
					#     if i == ii+1:
					#         new+=change
					#         done2=None
					#         iii=i-1
					#         while not done2:
					#             iii+=1
					#             if file[iii] == '(':
					#                 done2=True
					#         i=iii-1

					#     new+=ch
					# file = new
		pass
		# sys.exit()
	pass
	return {'list':support,'add':file}

def nameUnder(subject):
	new = ''
	for i,s in enumerate(subject):
		if not i:
			new+=s.lower()
		else:
			if s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				n=False
				try:
					if subject[i+1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						n=True
				except Exception as e:
					pass
				try:
					if subject[i-1] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						n=True
				except Exception as e:
					pass
				try:
					if subject[i-1] == ' ':
						n=True
				except Exception as e:
					pass
				if not n:
					new+='_'+s.lower()
				else:
					new+=s
			else:
				new+=s
	return new

def nameUpper(subject):
	if not _.switches.isActive('Underscore'):
		return subject
	new = ''
	i=-1
	while not i == len(subject)-1:
		i+=1
		s = subject[i]
		if s == '_':
			ss = subject[i+1].upper()
			new+=ss
			i+=1
		else:
			new+=s
	return new

def process(subject):
	original = subject
	subject = _str.cleanBE(subject,' ')
	if not subject.startswith('def ') and not subject.startswith('class ') :
		subject = 'def '+subject
	altA = nameUnder(subject)
	altB = nameUpper(subject)
	# _.pr(subject,altA,altB)
	# global toTable
	global addedFunctions
	global addedVarsCode
	global addedVars
	global addVars
	global baseGlo
	global toGlo
	global table
	global base
	global to
	# if not _.switches.isActive('Underscore'):
	do = True
	if subject+' ' in to.replace(':',' :').replace('(',' ('):
		# _.pr('s in to',subject)
		do=False
	if altA in to.replace(':',' :').replace('(',' ('):
		# _.pr('A in to',altA)
		do=False
	if altB in to.replace(':',' :').replace('(',' ('):
		# _.pr('B in to',altB)
		do=False

	sub = None
	if original in table:
		sub = original
	if subject in table:
		sub = subject
	if altA in table:
		sub = altA
	if altB in table:
		sub = altB
	# if not do or sub is None:
	#     for k in table:
	#         if subject == k:
	#             sub = k
	#         if altA == k:
	#             sub = k
	#         if altB == k:
	#             sub = k

	if not do or sub is None and not sub in addedFunctions:
		# _.pv(table)
		should=False
		for k in table:
			if original == k:
				should=True
			if subject == k:
				should=True
			if altA == k:
				should=True
			if altB == k:
				should=True
			if should:
				pass
				# _.pr('should work B',sub,do,addedFunctions)


		return None

	suby = subject
	if original.startswith('class '):
		suby = sub
	if not original.startswith('class '):
		if _.switches.isActive('Underscore'):
			suby = altA
		if _.switches.isActive('Alpha'):
			suby = altB

	Glo=[]
	add=''
	if sub in table:
		addedFunctions.append(sub)
		# _.cp(['added:',sub,suby],'green')
		_.cp(['added:',sub],'green')
		s = table[sub]['start']-1
		e = table[sub]['end']-1
		add += '\n'
		for i,line in enumerate(base):
			if i >=s and i <= e:
				add += line
				if 'global ' in line:
					gg = line.split('global ')[1].replace('\n','')
					if not gg in addedVars:
						addedVars.append(gg)
					Glo.append( gg )
					_.cp(['global:',gg],'red')
		add += '\n'
	suby = subject
	if original.startswith('class '):
		suby = sub
	if not original.startswith('class '):
		if _.switches.isActive('Underscore'):
			suby = altA
			# add = add.replace(subject,altA)
			# add = add.replace(altB,altA)
		if _.switches.isActive('Alpha'):
			suby = altB
			# add = add.replace(subject,altB)
			# add = add.replace(altA,altB)
	if _.switches.isActive('Supporting'):
		support = find_supporting(add,suby)
		add = support['add']
		toAdd=[]
		for sup in support['list']:
			c = 'class '+sup
			f = 'def '+sup
			if c in table:
				_.cp( ['supporting:',c], 'yellow' )
				toAdd.append(c)
			if f in table:
				toAdd.append(f)
				_.cp( ['supporting:',f], 'yellow' )

	pass
	# addGlo = find_global(data)
	for g in Glo:
		if g in baseGlo and not g in addedVarsCode and not g in toGlo:
			addedVarsCode.append(g)
			addVars+=baseGlo[g]+'\n'
			_.cp(['supporting:',g],'purple')
	to+=add
	if _.switches.isActive('Supporting'):
		for ta in toAdd:
			process(ta)


def find_global(data):
	# if type(data) == str:
		# isStr=True
	#     data = data.split('\n')
	# else:
	#     isStr=False
	isStr=True
	glo = {}

	i=0
	while True:
		eol=_.vindex(data,i,n='\n')
		if not type(eol) == int:
			eol=len(data)-1
		if eol < 1:
			return glo

		line = _.rstr( data, i, eol )
		line2 = line
		# line = data[ i: eol ]
		# _.pr(i,eol,'line',line)
		pass
		if not '==' in line and not line.startswith(' ') and not line.startswith('\t') and '=' in line:
			# _.cp(line,'cyan')
			line = line.replace( '\n', '' )
			line = line.replace( ' =', '=' )
			line = line.replace( ' =', '=' )
			line = line.replace( ' =', '=' )
			line = line.replace( '= ', '=' )
			line = line.replace( '= ', '=' )
			line = line.replace( '= ', '=' )
			line = line.replace( '=', ' = ' )
			multi = False
			pre=''
			part=''
			ii=i
			started=False
			vi = False
			# _.pr(ii,eol)
			while not ii==eol:
				ii+=1
				ch=data[ii]
				if ch == '\n':
					break
				elif not started and ch == '=':
					started=True
				elif started:
					if ch in '[({"'+'"':
						vi=True
						ee = _.vindex( data, ii )[ii]
						if not type(ee) == int:
							ee = len(data)-1
						part = pre+_.rstr( data, i, ee )
						break
					else:
						# _.pr(pre)
						pre+=ch
			if not vi:
				part=line2

			glo[line.split(' ')[0]] = _str.cleanBE(_str.cleanBE(part,'\t'),' ')
			pass
		if eol >=len(data)-1:
			return glo
		pass
		i=eol+1

	# for line in data:

	return glo





def action():
	load()
	global to
	global addVars
	focus()
	# _.pr( _.isData() )
	for i,subject in enumerate( _.isData(r=1) ):
		subject = _str.cleanBE(subject,' ')
		if subject:
			process(subject)
	addVars+='\n\n'
	_.pr('addVars',addVars)
	_.saveText(to+addVars,_.switches.values('To')[0])
	_.cp(['Saved:',_.switches.values('To')[0]],'green')



def load():
	# global toTable
	global table
	global base
	global baseTXT
	global baseGlo
	global toGlo
	global to
	_inFunc = _.regImp( __.appReg, 'inFunc' )
	_inFunc.switch('Log')
	_inFunc.switch('Files',_.switches.values('From')[0])
	table = _inFunc.action().copy()
	
	# _inFunc.backupLog = []
	# _inFunc.data = []
	# _inFunc.process = []
	# _inFunc.log = []
	# _inFunc.ignoreLines=[]
	# _inFunc.md5Data=[]

	# _.pr('table',table)
	# # _inFunc = _.regImp( __.appReg, 'inFunc' )
	# _inFunc.switch('Log')
	# _inFunc.switch('Files',_.switches.values('To')[0])
	# toTable = _inFunc.action().copy()
	# # _.pr('toTable',toTable)
	# sys.exit()
	base = _.getText( _.switches.values('From')[0] )
	to = _.getText( _.switches.values('To')[0], raw=True )
	toGlo = find_global(to)
	baseGlo = find_global( ''.join(base) )
	_.pr('baseGlo',baseGlo)
	_.pr('##############################################################')
	for k in baseGlo:
		_.pr(baseGlo[k])
	_.pr('##############################################################')
	# _.pv(baseGlo)
	# _.pv(table)
	to+='\n\n############################################################## copy-fn-class\n\n'

addVars=''
addedVars=[]
addedVarsCode=[]
addedFunctions=[]


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







