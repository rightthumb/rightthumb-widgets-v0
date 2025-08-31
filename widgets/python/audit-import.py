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

import os
import sys
import time
# import platform
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
	_.switches.register( 'Import', '-i,-imp,-import', 'vars', isRequired=True )
	_.switches.register( 'Child', '-child', 'classic' )
	_.switches.register( 'AppCount', '-apps' )

	_.switches.register( 'Prefix', '-p,-pre,-prefix', '_v' )

	_.switches.register( 'Print', '-print', 'classes variables functions  OR  v 6' )
	_.switches.register( 'Good', '-good', '6' )
	_.switches.register( 'Bad', '-bad', '6' )


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

_.appInfo[focus()] = {
	'file': 'audit-import.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Check all python apps to see how an import is used',
	'categories': [
						'audit',
						'import',
						'python',
						'apps',
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
						'b py',
						"""p f -in *.py + _rightThumb._base  -jn | p f + "if __name__ == '__main__';." - # -jn  | p appInfo""",
	],
	'examples': [
						'p audit-import -i vars -pre _v',
						'',
						'p audit-import -i drive -pre _drive -child classic',
						'',
						'p audit-import -i temp-test -pre _t',
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


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START



def processImport():
	global pre
	global imp
	global table
	table = _.dot()
	table.variables = {}
	table.classes = {}
	table.functions = {}
	IMP = ' \n '.join(imp)
	IMPY = ''
	for ch in IMP:
		if ch in '._0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			IMPY += ch
		else:
			IMPY += ' '+ch+' '

	# xxx = IMPY.count('folderID_tech')
	# _.pr(xxx)
	# sys.exit()
	table.usage = _.dot()
	table.usage.app = _.dot()
	table.usage.i = _.dot()

	# _.pr( imp )
	# for line in imp:
	#     line = line.replace( ' ', '•' )
	#     _.pr(line)

	pass
	isClass = False
	lClass = ''
	functions = []
	for line in imp:
		# if line.startswith('class '):
		#     # _.pr(line)

		if line.startswith('class ') and not line == 'class dot:' and not line == 'class DOT:' and not line == 'class Dot:':
			# _.pr(line)
			isClass = True
			lClass = line.split('class ')[1].split('(')[0].split(':')[0].split(' ')[0]
			lClass = _str.cleanBE( lClass, '\t' )
			table.classes[lClass] = {
										'i': 0,
										'apps': {},
										'variable': None,
										'children': {},
			}

		# if not line.startswith('\t') and len(line) and line:
			

		if not line.startswith('\t') and not line.startswith('def ') and '=' in line and not '+=' in line and not '.' in line  and not '==' in line and not line.startswith('if ') :
			isClass = False
			cl = line.split('=')[0].split('[')[0].split(' ')[0]
			cl = _str.cleanBE( cl, '\t' )
			var = line.split('=')[1].split('[')[0].split(' ')[0]
			if var in functions:
				table.functions[cl] = {
																'i': 0,
																'apps': {},
				}
			else:
				ixi = IMPY.count(cl)-1
				iii = IMP.count('global '+cl)-1
				iii = IMP.count('global '+cl)-1
				iYi = IMP.count(cl+'.')-1
				if iii > ixi:
					ixi = iii
				if iYi > ixi:
					ixi = iYi
				# _.pr(ixi, cl)
				table.variables[cl] = {
															'i': ixi,
															'apps': {},
				}

		elif line.startswith('def '):
			isClass = False
			cl = line.split('def ')[1].split('(')[0].split(' ')[0]
			cl = _str.cleanBE( cl, '\t' )
			# table.functions[cl] = {
			functions.append(cl)
			table.functions[cl] = {
															'i': 0,
															'apps': {},
			}
		
		if isClass:
			if line.startswith('\tdef '):
				# _.pr(line)
				cl = line.split('\tdef ')[1].split('(')[0].split(' ')[0]
				cl = _str.cleanBE( cl, '\t' )
				if not cl == '__init__':
					table.classes[lClass]['children'][cl] = {
																'i': 0,
																'apps': {},
					}


	pass
	for line in imp:
		# _.pr(line)
		for k in table.classes:
			x = '='+k+'('
			# _.pr(x)
			if x in line:
				line = line.replace('\t','')
				line = line.replace(' ','')
				v = line.split(x)[0]
				# if not '.' in v:
				#     v = pre+'.'+v
				if not v.startswith('self.') and not '(' in v:
					v = v.replace('..','.')
					v = v.replace('_._','_.')
					table.classes[k]['variable'] = v
					# _.cp( v, 'green' )
				# _.pr( k, v )
	# _.vp( table.classes )
	# _.pr( '\n'.join( list(table.classes.keys()) ) )


def scanAppRegistration():
	global appCount
	global pre
	appRegLog = _.getTableDB( 'appRegistration.hash' )
	IMP = _.switches.values('Import')[0]
	for key in appRegLog:
		record = appRegLog[key]
		appCount += 1

		a = key


		# _.pr(a)
		for rec in record['file_profile']['imports']:
			im = rec['app']
			if im == '_rightThumb._'+IMP:
				# _.pr(im)
				if 'instances' in rec:
					if rec['instances']:
						# _.pr( list(rec['instances'].keys())[0] )
						pre = list(rec['instances'].keys())[0].split('.')[0]
						# _.pr(pre)
						# _.pr('here')
						# _.pv(table.classes)
						# _.pv(table.functions)
						# _.pv(table.variables)
						for k in table.classes:
							if table.classes[k]['variable']:
								vv = table.classes[k]['variable']
								for child in table.classes[k]['children']:
									item = pre +'.'+ vv +'.'+child + '('
									if item in rec['instances']:
										# _.pr(item)
										table.classes[k]['children'][child]['i'] += 1
										table.classes[k]['children'][child]['apps'][a] = rec['instances'][item]
										table.classes[k]['i'] += rec['instances'][item]
										pass

						for k in table.functions:
							# item = pre +'.'+ k + '('
							item = pre +'.'+ k+'('
							# _.pr(item)
							for oOo in rec['instances']:

								if item[:-1] == oOo or item in oOo:
									if item in rec['instances']:
										table.functions[k]['i'] += 1
										table.functions[k]['apps'][a] = rec['instances'][item]
										# table.functions[k]['i'] += rec['instances'][item]
									# _.pr(oOo)

						for k in table.variables:
							# item = pre +'.'+ k + '('
							item = pre +'.'+ k
							for oOo in rec['instances']:
								if item in oOo:
									if item in rec['instances']:
										table.variables[k]['i'] += 1
										table.variables[k]['apps'][a] = rec['instances'][item]
										# table.functions[k]['i'] += rec['instances'][item]
									# _.pr(oOo)

def isInt(n):
	x = '0123456789'
	result = True
	for nn in n:
		if not nn in x:
			result = False
	return result


def action():
	load()
	global imp
	global impy
	global table
	global appCount
	global pre

	appCount = 0
	scanAppRegistration()

	dump = {
				'classes': table.classes,
				'functions': table.functions,
				'variables': table.variables,
	}


	isBad = True

	do = _.dot()
	do.classes   = 0
	do.functions = 0
	do.variables = 0


	if _.switches.isActive('Bad'):
		if _.switches.value('Bad'):
			n = int( _.switches.value('Bad') )
			do.classes   = n
			do.functions = n
			do.variables = n


	if _.switches.isActive('Good'):

		do.classes   = 1
		do.functions = 1
		do.variables = 1

		isBad = False
		if _.switches.value('Good'):
			n = int( _.switches.value('Good') )
			do.classes   = n
			do.functions = n
			do.variables = n


	if _.switches.isActive('Print'):
		do.classes   = None
		do.functions = None
		do.variables = None


		for p in _.switches.values('Print'):
			last = ''
			p = p.lower()
			if p.startswith('c'):
				last = 'c'
				do.classes = 0
			elif p.startswith('f'):
				last = 'f'
				do.functions = 0
			elif p.startswith('v'):
				last = 'v'
				do.variables
			elif isInt(p):
				if last == 'c':
					do.classes = int(p)
				elif last == 'f':
					do.functions = int(p)
				elif last == 'v':
					do.variables = int(p)
	pass
	# pree = pre
	# pre+='.'
	pre = ''
	if _.switches.isActive('Prefix'):
		pre = _.switches.values('Prefix')[0]
	if len(pre) and not pre.endswith('.'):
		pre += '.'
	if not do.variables is None:
		_.cp( 'Variables', 'yellow' )
		for k in table.variables:
			if isBad:
				if table.variables[k]['i'] <= do.variables:
					_.cp( [ '\t', table.variables[k]['i'], pre+k ], 'cyan' )
			else:
				if table.variables[k]['i'] >= do.variables:
					_.cp( [ '\t', table.variables[k]['i'], pre+k ], 'cyan' )
				

	if not do.functions is None:
		_.cp( 'Functions', 'yellow' )
		for k in table.functions:
			if isBad:
				if table.functions[k]['i'] <= do.functions:
					_.cp( [ '\t', table.functions[k]['i'], pre+k ], 'cyan' )
					# _.pr( table.functions[k]['i'], pre+k )
			else:
				if table.functions[k]['i'] >= do.functions:
					_.cp( [ '\t', table.functions[k]['i'], pre+k ], 'cyan' )

	if not do.classes is None:
		_.cp( 'Classes', 'yellow' )
		for k in table.classes:
			for child in table.classes[k]['children']:
				go = False
				if isBad:
					if table.classes[k]['children'][child]['i'] <= do.classes:
						go = True
				else:
					if table.classes[k]['children'][child]['i'] >= do.classes:
						go = True
				if go:
					if table.classes[k]['variable'] is None:
						vVv = k
					else:
						vVv = table.classes[k]['variable']
					if not len(pre):
						ppre = ''
					else:
						if not vVv.startswith(pre):
							ppre = pre
						else:
							ppre = ''
					_.cp( [ '\t', table.classes[k]['children'][child]['i'], ppre+vVv+'.'+child ], 'cyan' )
					# _.pr( table.classes[k]['i'], pre+table.classes[k]['variable']+'.'+child )
			





	# _.saveTableDB( dump, 'audit-import-'+_.switches.values('Import')[0]+'.json' )
	# for k in table.classes:
	#     if table.classes[k]['i']:
	#         newChildren = {}
	#         for child in table.classes[k]['children']:
	#             if table.classes[k]['children'][child]['i']:
	#                 newChildren[child] = table.classes[k]['children'][child]
	#         table.classes[k]['children'] = newChildren


	# for k in table.classes:
	#     if table.classes[k]['i']:
	#         pass
	#         _.vp( table.classes[k] )

	# _.vp(table.classes)
	# _.vp(table.variables)
	# _.vp(table.functions)
	# test = {}
	# for k in table.classes:
	#     if table.classes[k]['i']:
	#         test[k] = table.classes[k]


	# _.vp(test)
	# IMPY = '\n'.join( imp )
	# _.pr(IMPY)
	# for k in table.variables:
	#     if table.variables[k]['i'] < 1:
	#         _.pr( 0, k )
			# ixi = impy.lower().count(k.lower())
			# table.variables[k]['i'] = ixi
			# if table.variables[k]['i'] < 1:
			#     # _.pr()
			#     # _.pr()

			#     # _.pr(table.variables[k]['i'], k)
			#     # for x in k:
			#     #     _.pr( ord(x), chr(ord(x)) )
			#     # _.pr()
			#     # _.pr()
			# test[k] = table.variables[k]
			# _.vp( table.variables[k] )


	# test = {}
	# for k in table.functions:
	#     if table.functions[k]['i']:
	#         test[k] = table.functions[k]
	# _.vp( test )

	if _.switches.isActive('AppCount'):
		_.pr( 'apps:', appCount )

def load():
	global imp
	global impy
	global pre

	pre = _.switches.value('Prefix')

	s   = os.sep
	i   = _.switches.values('Import')[0]
	c   = '__init__.py'
	if _.switches.isActive('Child'):
		c = _.switches.values('Child')[0]
		if not c.endswith('.py'):
			c += '.py'
	
	if not os.path.isdir( _v.py +s+ '_rightThumb' +s+ '_'+i ):
		_.e( 'no import folder' )


	imp = _.getText( _v.py +s+ '_rightThumb' +s+ '_'+i +s+ c, c=2 )
	impy = _.getText( _v.py +s+ '_rightThumb' +s+ '_'+i +s+ c, raw=True )
	processImport()



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()







