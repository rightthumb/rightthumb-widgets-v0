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
	_.switches.register( 'Dirty', '-dirty' )
	_.switches.register( 'Split', '-split', 'sp sep win' )
	_.switches.register( 'SameLine', '-line' )
	_.switches.register( 'PrintScrap', '-print,-scrap' )
	_.switches.register( 'AddChars', '-a,-add,-char,-chars' )
	_.switches.register( 'Clean', '--c' )

	pass

def sc(string):
	string = _str.replaceDuplicate(string,' ')
	string = _str.cleanBE(string,' ')
	return string


SPLIT = {
		sc('cn sc colon semi'): ';',
		sc('c comma'): ',',
		sc('d dash'): '-',
		sc('sp space'): ' ',
		sc('s sl sep os.sep slash'): os.sep,
		sc('w win iswin'): '\\',
		sc('l linux'): '/',
		sc('t tab'): '\t',
		sc('q qq'): '"',
		sc('sq'): "'",
}

def split_trigger(data):
	global SPLIT
	for k in SPLIT:
		for a in k.split(' '):
			if a == data.lower():
				return SPLIT[k]
	return data

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
	'file': 'pipe-split.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'pipe skimmer',
	'categories': [
						'skim',
						'search',
						'pipe',
						'screen',
						'troubleshoot',
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
						_.hp('echo %path% | p pipe-split -split ;'),
						_.hp(''),
						_.hp('py vps- | p pipe-split -split " " + 7GzGHN'),
						_.hp(''),
						_.hp('p file -folder py | p pipe-split -split sp sep + 7GzGHN'),
						_.hp(''),
						_.hp('p file -folder py | p pipe-split -split sep .  + 7GzGHN'),
						_.hp(''),
						_.hp('b e'),
						_.hp('p files + *.php *.sh -or -has .py exec -print | p pipe-split -dirty + .py'),
						_.hp('p files + *.php *.sh -or -has .py exec -print | p pipe-split -dirty + .py -print'),
						_.hp('p files + *.php *.sh -or -has .py exec -print | p pipe-split -dirty + .py -a / \\'),
						_.hp(''),
						_.hp('p files + *.php *.sh   *.py   -or -has .py exec -print | p pipe-split -dirty + .py -a / \\'),
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
	_.switches.trigger( 'Split', split_trigger )

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

def splitter(data,split):
	# _.pr(data,split)
	results = []
	for i,row in enumerate( data ):
		if _.showLine(row):
			for subject in row.split(split):
				if _.showLine(subject):
					results.append(subject)
	return results
def action():
	result = _.isData(r=1)
	# _.pr(result)
	if _.switches.isActive('Dirty'):
		dirty={}
		file=''
		for ch in '\n'.join(result):
			if ch in '._-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n'+_.switches.value('AddChars'):
				file+=ch
			else:
				file+=' '
		file=_str.do('all',file,'  ',' ')
		file=_str.do('be',file,' ')
		if _.switches.isActive('PrintScrap'):
			_.pr(file)
		for line in file.split('\n'):
			for kik in line.split(' '):
				if _.showLine(kik):
					if not kik in dirty:
						dirty[kik]=0
					dirty[kik]+=1
		if not _.switches.isActive('Clean'):
			_.cp( _.linePrint(p=0), 'cyan' )
			_.pv(dirty)
			_.cp( _.linePrint(p=0), 'cyan' )
		for k in dirty:
			_.pr(k)
		if not _.switches.isActive('Clean'):
			_.cp( _.linePrint(p=0), 'cyan' )
		return None


	if not _.switches.isActive('Split') or not len(_.switches.value('Split')):
		global SPLIT
		_.cp( _.linePrint(p=0), 'green' )
		_.cp( 'split trigger', 'yellow' )
		_.pv(SPLIT)
		_.cp( _.linePrint(p=0), 'green' )
		_.e('-split required')
	# _.pr(_.switches.values('Split'))
	for split in _.switches.values('Split'):
		# _.pr('split',split)
		result=splitter(result,split)
		# _.pr('result',result)
	for row in result:
		_.pr(row)



def load():
	global data
	data = _.getTable( 'table' )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





