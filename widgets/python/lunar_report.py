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
	_.switches.register( 'Delta', '-delta' )

_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'lunar_report.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Lunar Report',
	'categories': [
						'report',
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
						'p lunar_report -delta 3',
						'p lunar_report -delta 2',
						'p lunar_report -delta 1',
						'p lunar_report -delta 0',
						'',
						'p lunar_report -delta 2.5',
						'',
						'p lunar_report -delta 36 hrs',
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
########################################################################################
# START


from datetime import datetime, timedelta

def dateAdd( theDate, addDays, epoch=True ):
	if addDays < 1:
		return theDate
	epoch = _.autoDate( theDate )

	# _.pr('epoch',epoch,theDate)
	# sys.exit()
	utc_time = datetime.utcfromtimestamp(epoch)
	future_time = utc_time + timedelta(addDays)
	if epoch:
		return _.autoDate( future_time )
	return future_time

def dateMinus( theDate, addDays, epoch=True ):
	if addDays < 1:
		return theDate
	epoch = _.autoDate( theDate )

	# _.pr('epoch',epoch,theDate)
	# sys.exit()
	utc_time = datetime.utcfromtimestamp(epoch)
	future_time = utc_time - timedelta(addDays)
	if epoch:
		return _.autoDate( future_time )
	return future_time
	# orig = datetime.datetime.fromtimestamp(epoch)
	# new = orig + datetime.timedelta(days=addDays)
	# return new.timestamp()
	
def epochAdd( epoch, add ):
	if not type(epoch) == float:
		epoch = _.autoDate(epoch)
	return epoch+((add*60)*60)

def epochMinus( epoch, add ):
	if not type(epoch) == float:
		epoch = _.autoDate(epoch)
	return epoch-((add*60)*60)

def process( start, end ):
	global theDates
	global theDiff
	if not type(start) == float:
		start = _.autoDate(start)
	if not type(end) == float:
		end = _.autoDate(end)
	# _.pr(start, end)
	diff = end - start
	theDiff = diff

	theDates.append({ 'start': start, 'end': end })

	# _.pr()
	# _.pr()
	# _.pr( _.friendlyDate(start) )
	# _.pr( _.friendlyDate(end) )
	# _.pr()
	# _.pr( 'diff', (diff/60), 'HRs'  )
	global log
	records = []
	for record in log:
		if record['timestamp'] > start and record['timestamp'] < end:
			records.append( record )
	return records

def epochHRs( a, b ):
	if a>b:
		start = b
		end = a
	else:
		start = a
		end = b
	diff = end - start
	return (diff/60)/60


def epochDays( a, b ):
	hrs = epochHRs( a, b )
	return hrs/24

def audit( search ):
	global lunar
	global delta
	global deltaType
	# if not type(delta) == int:
	#     delta = 1
	# if delta < 1:
	#     delta = 1

	records = []
	for record in lunar:
		# if 'Full Moon' in record['title']:
		
		if _.showLine( record['label'], search ):
			if len( record['date'] ) > 3:
				# day = _.friendlyDate( record['date'] ).split(' ')[0]
				day = record['date']
				if deltaType == 'day':
					if delta > 0:
						start = dateMinus( day, delta )
						end = dateAdd( day, delta )
					else:
						start = epochMinus( day, 12 )
						end = epochAdd( day, 12 )


				elif deltaType == 'hr':
					day = record['date']
					if delta > 0:
						start = epochMinus( day, delta )
						end = epochAdd( day, delta )
					else:
						start = epochMinus( day, 12 )
						end = epochAdd( day, 12 )


				report = process( start, end )
				for x in report:
					records.append( x )


	totals = {}
	grand = 0
	for record in records:
		grand+=1
		try:
			totals[ record['file'] ] += 1
		except Exception as e:
			totals[ record['file'] ] = 1
	return grand
	return grand, len(list(totals.keys()))



def action():
	global lunar
	global delta
	global theDiff
	global theDates
	
	load()


	# _.printVar( lunar )
	records = {
					'New Moon': audit( 'new,moon' ),
					'First Quarter': audit( 'first,quarter' ),
					'Full Moon': audit( 'full,moon' ),
					'Last Quarter': audit( 'last,quarter' ),
	}
	# _.printVar( records )

	count = []
	for key in records.keys():
		count.append( records[key] )
	count.sort()
	thresh = count[0]
	data = []
	for x in count:
		if thresh == x:
			data.append({ 'total': x, 'pDiff': 100 })
		else:
			data.append({ 'total': x, 'pDiff': _.pDiff( x, thresh, 'g' ) })

	report = []
	for key in records.keys():
		for dm in data:
			if dm['total'] == records[key]:
				report.append({ 'label': key, 'pDiff': int(dm['pDiff']) })
				
	
	report = _.tables.returnSorted( 'data', 'd.pDiff', report )
	_.fields.asset( 'data', report )
	
	_.pr()
	for record in report:
		line = _.colorThis( [  _.fields.value( 'data', 'label', record['label'], right=1 )  ], 'green', p=0 )
		line += '\t'
		line += _.colorThis( [ _.addComma(record['pDiff'])+'%' ], 'yellow', p=0 )
		_.pr( line )
	_.pr()
	_.colorThis( [ ' Days:', epochDays( theDates[0]['start'],theDates[0]['end'] ),'\tHrs:', epochHRs( theDates[0]['start'],theDates[0]['end'] ) ], 'blue' )
	_.pr( theDates[0] )


	# for record in theDates:
	#     diff = record['end'] - record['start']
	#     diffX = [diff,diff/60,(diff/60)/60]
	#     diffX = epochHRs(record['start'],record['end'])
	#     _.pr( _.friendlyDate(record['start']), _.friendlyDate(record['end']), diffX )

	# _.printVar( report )


	# pDiff


	# _.pr( lunar[0].keys() )

def load():
	global lunar
	global log
	global delta
	global deltaType

	if _.switches.isActive('Delta'):
		delta = float(_.switches.values('Delta')[0])
		if len( _.switches.values('Delta') ) > 1:
			if 'h' in _.switches.values('Delta')[1]:
				deltaType = 'hr'

	# lunar = _.getCSV( 'lunar_table.csv' )
	log = _.tables.returnSorted( 'data', 'd.timestamp', _.getTable('fileBackup.json') )
	lunar = []
	lunarYears = _.getTableDB( 'lunar_calendar.json' )
	for x in lunarYears['2018']:
		lunar.append(x)
	for x in lunarYears['2019']:
		lunar.append(x)
	for x in lunarYears['2020']:
		lunar.append(x)

theDates = []
theDiff = 0
deltaType = 'day'
delta = 1
log = []
lunar = []



# b lunar
"""


https://lunaf.com/lunar-calendar/2019/

window.open('http://www.pillerbeauty.com/js/jquery-1.11.3.js', 'new')


hackData = []
$('article').each(function() {
	var title = $(this).find('a').attr('title')
	var date = $(this).find('time').attr('datetime')
	hackData.push({ 'title': title, 'date': date });
});
console.log( hackData )

copy(hackData)
"""


########################################################################################
if __name__ == '__main__':
	action()