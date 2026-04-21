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
	_.switches.register( 'Hex', '-h,-hex' )
	_.switches.register( 'Number', '-n,-c,-code,-codes' )
	_.switches.register( 'JSON', '-json' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
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
	'file': 'win-err.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'windows System Error Codes (0-499)'+
		_.aib('https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-'),
	'categories': [
						'DEFAULT',
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
						_.hp('p win-err -json'),
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
	# _.switches.trigger( 'Files',_.inRelevantFolder )    
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

def build_codes(codes_raw):
	raw=codes_raw.split('\n')
	def isEnd(i,raw):
		if i+3>len(raw):
			return True
		else:
			return False
	records={
				'n': {},
				'h': {},
				'l': [],
	}
	i=0
	while True:
		if isEnd(i,raw):
			break
		rec = {
				'e': raw[i],
				'n': raw[i+1].split(' ')[0],
				'h': raw[i+1].split(' ')[1].replace('(','').replace(')',''),
				'd': raw[i+2],
		}
		records['n'][ rec['n'] ]=len(records['l'])
		records['h'][ rec['h'] ]=len(records['l'])
		records['l'].append(rec)
		i+=3
	return records

def fh(string):
	return string.upper().replace('0X','0x')

def get(string):
	global codes
	if '0x' in string.lower():
		if fh(string) in codes['h']:
			return codes['l'][  codes['h'][fh(string)]  ]
		return {}
	elif string in codes['n']:
		return codes['l'][  codes['n'][fh(string)]  ]
	return {}




def action():
	load()
	global codes

	recs = []
	if _.switches.isActive('JSON'):
		_.pv(codes)
		return None
	if _.switches.isActive('Plus'):
		for rec in codes['l']:
			r=str(rec)
			r=rec['e']
			if _.showLine(r):
				_.pr( rec['n'], rec['e'] )
				# recs.append(rec)
		# _.pv(recs)
		return None


	if _.switches.isActive('Hex'):
		for s in _.switches.values('Hex'):
			recs.append(get(s))
	if _.switches.isActive('Number'):
		for s in _.switches.values('Number'):
			recs.append(get(s))

		_.pv(recs)

	# for i,rec in enumerate( codes ):
	#     _.pv(rec)
	#     sys.exit()



def load():
	global codes
	r=_v.ww+os.sep+'databank'+os.sep+'tables'+os.sep+'windows-system-error-codes-raw.txt'
	d=_v.ww+os.sep+'databank'+os.sep+'tables'+os.sep+'windows-system-error-codes.json'
	u='https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-'
	if 1 and os.path.isfile(d):
		codes=_.getTableDB('windows-system-error-codes.json')
	elif 1 and not os.path.isfile(d) and os.path.isfile(r):
		codes_raw = _.getText( r, raw=True,clean=2 )
		# _.pr(codes_raw)
		codes=build_codes(codes_raw)
		_.saveTableDB( codes, 'windows-system-error-codes.json' )
	else:

		try:
			import webbrowser
			webbrowser.open(u, new=2)
		except Exception as e:
			pass
		_.e([
				{ 'l': 'please save text errors', 'd': 0, 'c': 'Background.red' },
				0,
				u,
				{ 'l': "copy( document.querySelector('dl').innerText )", 'd': 1, 'c': 'cyan', 'n': 'todo' },
				{ 'l': r, 'd': 1, 'c': 'green', 'n': 'todo' },
			])
	# _.pv(codes)
	# sys.exit()



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






