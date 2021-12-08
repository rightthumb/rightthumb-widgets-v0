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
	_.switches.register( 'Log', '-log' )
	_.switches.register( 'Client', '-client' )

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
# 	finds the file in probable locations
# 	and 
# 		if  _.autoBackupData = True
# 		and __.releaseAcquiredData = True
# 			GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
# 		you can run apps on usb at a clients office
# 			when you get home run: p app -loadepoch epoch 
# 				backed up
# 					pipe
# 					files
# 					tables
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
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
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
						_.hp('p thisApp -file file.txt'),
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
# 	if os.path.isdir( row ):
# 	if os.path.isfile( row ):
#	os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
# 													if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

FLAG = 'graphic.png?meta='
CLIENT = 'FLO20211206'
LOGS = ['/var/log/httpd/domains/eyeformeta.com.load.log']
SPENT_LINES = []
SPENT_LINES_PATH = '/home/admin/domains/eyeformeta.com/public_html/apps/email/skimmer/spent.list'
RECORDS = []
RECORDS_PATH = '/home/admin/domains/eyeformeta.com/public_html/apps/email/skimmer/records.json'

def action():
	global FLAG
	global CLIENT
	global LOGS
	global SPENT_LINES
	global SPENT_LINES_PATH
	global RECORDS
	global RECORDS_PATH

	FOUND_NEW = False

	if os.path.isfile(RECORDS_PATH):
		RECORDS = _.getTable2(RECORDS_PATH)

	if os.path.isfile(SPENT_LINES_PATH):
		SPENT_LINES = _.getText(SPENT_LINES_PATH)


	if _.switches.isActive('Client'):
		CLIENT = _.switches.values('Client')[0]
	# FLAG = FLAG.lower()
	CLIENT = CLIENT

	if _.switches.isActive('Log'):
		LOGS = _.switches.values('Log')



	for log in LOGS:
		# data = _.getText(log)
		data = ['''47.198.0.127 - - [06/Dec/2021:13:18:38 -0800] "GET /graphic.png?meta=FLO20211206-6CF079C0-7A3A-4067-9949-5560CA4E020A HTTP/2.0" 200 1108 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"''']
		for row in data:
			rec = {}
			# rowLo = row.lower()
			if FLAG in row and CLIENT in row:
				if not row in SPENT_LINES:
					FOUND_NEW = True
					SPENT_LINES.append(row)

					rec['line'] = row
					rec['ip'] = row.split(' ')[0]
					rec['date'] = ''
					rec['track'] = ''
					rec['agent'] = ''
					rec['cid'] = CLIENT
					on = False
					spent = False
					for x in row:
						if not spent and not on and x == '[':
							on = True
						elif on and x == ']':
							on = False
							spent = True
						elif on:
							rec['date'] += x

					qs = row.split('"')
					# for i,x in enumerate(qs):
					# 	print( i ,x )
					for x in qs[1].split(CLIENT+'-')[1]:
						if x in '-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
							rec['track'] += x 
						else:
							break
					rec['agent'] = qs[5]
					RECORDS.append(rec)

		if FOUND_NEW:
			pass
			# _.pv(RECORDS)
			_.saveTable2( RECORDS, RECORDS_PATH )
			_.saveText( SPENT_LINES, SPENT_LINES_PATH )













########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





