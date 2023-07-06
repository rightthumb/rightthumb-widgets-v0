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
	pass
	_.switches.register( 'Max', '-max' )
	# _.switches.register( 'Slots', '-slots' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data', description='Files' )
	_.switches.register( 'Clean', '--c' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'closest.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Compare distance of different strings',
	'categories': [
						'tool',
						'compare',
						'file',
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
						'type dx.all-20.2.5-clean.js | p closest + startDayHour currentView -or',
						'',
						'type dx.all-20.2.5-clean.js | p closest + startDayHour currentView -or -slots 100',
						'',
						'default max lines 10',
						# 'default slots 100',
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
	_.switches.trigger( 'Files', _.myFileLocations )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START

def manageSlots( n ):
	global slots
	global default
	global spent

	# _.pr(n)

	for s in slots:
		if slots[s] == default:
			if not n in spent:
				spent.append(n)
				slots[s] = n
				return None
	for s in slots:
		if n < slots[s]:
			if not n in spent:
				spent.append(n)
				slots[s] = n
				return None

def clean(x):
	x = _str.cleanBE(x,' ')
	x = _str.cleanBE(x,'\t')
	x = x.replace( '\r', '' )
	x = x.replace( '\n', '' )
	for z in _.switches.values('Plus'):
		for y in _.caseUnspecific(x,z):
			x = x.replace(y, _.colorThis( y, 'green', p=0 ))

	return x

def action():
	# _.colorThis( '', 's' )
	_.switches.fieldSet( 'PlusOr', 'active', True )
	global slots
	global default

	dex = {}
	windex = {}
	table = []
	last = ''
	default = 999999999999999999999999999999
	diff = default
	slotCnt = 10000
	if _.switches.isActive('Slots'):
		slotCnt = int(_.switches.value('Slots'))

	# for x in range(0,slotCnt):
	#     _.pr(x)
	# sys.exit()
	_.pr( 'Processing...', end='\r' )
	for x in range(0,slotCnt):
		slots[x] = default
	for i,row in enumerate(_.isData(r=1,pipeClean=False)):
		if _.showLine( row ):
			cnt = 0
			for x in _.switches.values('Plus'):
				if x.lower() in row.lower():
					cnt+=1
			if cnt == len(_.switches.values('Plus')):
				single = True
			else:
				single = False
			for x in _.switches.values('Plus'):
				if x.lower() in row.lower():
					if not x == last:
						li = -1
						if single:
							dx = 0
							li = i
						else:
							try:
								li = windex[last]
							except Exception as e:
								li = -1
							if not li == -1:
								dx = i - li
						if not li == -1:
							manageSlots( dx )
							if dx < diff:
								diff = dx
							if not dx in dex:
								dex[dx] = {}

							dex[ dx ][ li ] = i

					table.append(i)
					windex[x] = i
					last = x
		# _.pr(row)
	_.pr( '                                                        ', end='\r' )
	if diff == default:
		_.colorThis( 'not found', 'red' )
	else:
		if _.switches.isActive('Max'):
			m = int( _.switches.value('Max') )
		else:
			m = 10
		tbl = []
		# for s in slots:
		#     if not slots[s] == default:
		#         if slots[s] <= m:
		#             tbl.append(slots[s])
		for t in dex:
			if t <= m:
				tbl.append(t)
		tbl.sort()
		cnt = 0
		for t in tbl:
			_.colorThis( t, 'blue' )
			for d in dex[t]:
				_.colorThis( [ '\t', d, dex[t][d] ], 'cyan' )
				cnt+=1
				if not _.switches.isActive('Clean'):
					if d == dex[t][d]:
						_.pr( '\t\t', clean( _.isData(pipeClean=False)[d] ) )
					else:
						x = d
						while not x == dex[t][d]+1:
							_.pr( '\t\t', clean( _.isData(pipeClean=False)[x] ) )
							x+=1
		_.colorThis( [ '\n','',  cnt ], 'yellow' )


		# _.printVarSimple(slots)



spent = []

slots = {}


########################################################################################
if __name__ == '__main__':
	action()







