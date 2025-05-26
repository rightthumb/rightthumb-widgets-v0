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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data,clean', description='Files' )
	_.switches.register( 'Test', '-test' )


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
	'file': 'singleLine.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'single line. used in history management',
	'categories': [
						'history',
						'line',
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
						'p singleLine -f D:\\tech\\hosts\\VULCAN\\temp\\unclaimed_tickets_history\\history-10962.txt',
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




def genPatterns( ix ):
	global data
	patterns = {}

	for i,row in enumerate(data):
		if i >= ix-1:
			break
		if i >= 2:
			
			if not row in patterns:
				patterns[row] = {}
			if not data[i-1] in patterns[row]:
				patterns[row][data[i-1]] = {}
			if not data[i-2] in patterns[row][data[i-1]]:
				patterns[row][data[i-1]][data[i-2]] = {}

	return patterns




def testPattern( i ):
	global data
	global theLines
	global spent
	if not i:
		return True
	elif not data[i] in spent:
		return True
	else:

		if i >= 2:
			patternsX = {}
			patternsX = genPatterns(i)
			if not data[i] in patternsX:
				return True
			elif not data[i-1] in patternsX[data[i]]:
				return True
			# if not data[i-2] in patternsX[data[i]][data[i-1]]:
				# return True
			else:
				# _.pr(i, '\t x: \t',data[i], '\t\t' ,data[i-1] )
				return False
		# else:
		#     if i-1 in theLines[ data[i-1] ]:
		#         return False

	return True

def find_pattern():
	global data
	global theLines
	# _.pr(theLines,pvs=1)
	streaks_be={}
	last=[]
	lines=[]
	for i,line in enumerate(data):
		if line in theLines:
			groot=theLines[line]
			tester=_._2lists(lines,groot)
			# print('tester',tester)
			if not tester: lines.append(i)
			con=[]
			for la in last:
				for gro in groot:
					if la == gro-1:

						lala=la-1
						found=False
						while lala in streaks_be:
							found=True
							lala-=1
						if not found: lala=la
						else: lala+=1

						if not lala in streaks_be: streaks_be[lala]={}
						streaks_be[lala]=gro
			last=groot
	winner=None
	largest=0
	patterns={}
	index={}
	for b in streaks_be:
		e = streaks_be[b]
		ln = e - b
		if not ln in patterns: patterns[ln] = []
		patterns[ln].append(_.zeros3(b,len(data) ))
		index
	_patterns={}
	for i in sorted(patterns.keys()):
		_patterns[_.zeros3(i,len(data))]=patterns[i]
	patterns=_patterns

	# _streaks_be={}
	for b in streaks_be:
		e = streaks_be[b]
		ln = e - b
		if ln > largest:
			largest=ln
			winner=b
	_.pr(line=1,c='gray')
	_.pr(line=1,c='green')
	_.pr()
	_.pr('winner:',winner,c='cyan')
	_.pr('largest:',largest,c='cyan')
	_.pr()
	_.pr(patterns,pvs=1)
	sys.exit()
	_.pr()
	_.pr(line=1,c='green')
	_.pr()

	for i in lines:
		_.pr(data[i])
	_.pr(streaks_be,pvs=1)

def action():
	global data
	global theLines
	global spent

	method = 1
	if _.switches.isActive('Test'): method = -3000
	
	data = _.isData(r=1)

	for i,row in enumerate(data):
		try:
			if not row in theLines:
				theLines[ row ] = []
			theLines[ row ].append(i)
		except Exception as e: pass


	if method == -3000:
		pass
		find_pattern()
	
	elif method == 1:

		for i,row in enumerate(data):

			if False:
				if testPattern( i ):
					spent[row] = 1
					_.cp(  [i, 'Y', row], 'green'  )
				else:
					_.cp(  [i, 'N', row, '\t\t', data[i-1],'\t', data[i-2] ], 'red'  )

			else:
				if testPattern( i ):
					spent[row] = 1
					_.pr(row)
			



	elif method == 0:
		for i,row in enumerate(data):
			if not row in spent:
				spent[row] = 1
				_.pr(row)

spent = {}
data = []
theLines = {}



########################################################################################
if __name__ == '__main__':
	action()







