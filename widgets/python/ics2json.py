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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'Save', '-save' )

	pass

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
	'file': 'ics2json.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'convert ics to json',
	'categories': [
						'ics',
						'json',
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
						_.hp('p ics2json -url '),
						_.hp('p ics2json -f C:\\Users\\Scott\\Downloads\\basic.ics '),
						_.hp('p ics2json -f C:\\Users\\Scott\\Downloads\\basic.ics -save cal-dirty.json '),
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


def skim(txt):
	scan = _clean.imp.app.scan.process( txt )
	if not 'email' in scan:
		scan['email'] = []
	if not 'phone' in scan:
		scan['phone'] = []
	return scan

def date_fix(dt):
	if ':' in dt:
		dt = dt.split(':')[1]
	if len(dt) == 15:
		n = ''
		for ic, di in enumerate(dt):
			n+=di
			if ic == 3:
				n += '-'
			if ic == 5:
				n += '-'
			if ic == 10:
				n += ':'
			if ic == 12:
				n += ':'
		dt = n
	if len(dt) == 8:
		n = ''
		for ic, di in enumerate(dt):
			n+=di
			if ic == 3:
				n += '-'
			if ic == 5:
				n += '-'
		dt = n
	dt = _.friendlyDate( _.autoDate( dt ) )
	return dt
def attendee(rec):
	b = -1
	e = -1
	active = False
	lines = rec.split('\n')
	for i,line in enumerate(lines):
		if active and line[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and not line.startswith('ATTENDEE'):
			active = False
			e = i
		if not active and line.startswith('ATTENDEE'):
			b = i
			active = True
	if not b:
		return None
	emails = skim( '\n'.join(lines[b:e]).replace('ATTENDEE',',ATTENDEE').replace(' ','').replace('\n',''))['email']
	return { 'b': b, 'e': e, 'emails': emails, 'raw': '\n'.join(lines[b:e])}

def dic_order(dic):
	new = {}
	for k in 'UID DTSTART DTEND ORGANIZER ATTENDEE CREATED LAST-MODIFIED DESCRIPTION LOCATION'.split(' '):
		if k in dic:
			new[k] = dic[k]
	for k in dic:
		if not k in new:
			new[k] = dic[k]
	if 'DTSTART' in new:
		new['DTSTART'] = date_fix(new['DTSTART'])
		new['epoch'] = _.autoDate(new['DTSTART'])
	if 'DTEND' in new:
		new['DTEND'] = date_fix(new['DTEND'])
	if 'DTSTAMP' in new:
		new['DTSTAMP'] = date_fix(new['DTSTAMP'])
	if 'RECURRENCE-ID' in new:
		new['RECURRENCE-ID'] = date_fix(new['RECURRENCE-ID'])
	if 'CREATED' in new:
		new['CREATED'] = date_fix(new['CREATED'])
	if 'LAST-MODIFIED' in new:
		new['LAST-MODIFIED'] = date_fix(new['LAST-MODIFIED'])
	for k in new:
		if type(new[k]) == str:
			new[k] = new[k].replace('\\n','\n')
			new[k] = new[k].replace('\\','')
	n = {}
	for k in new:
		n[ k.lower() ] = new[k]

	return n

def action():
	# should be   Single-Task   OR   Imply-Architecture-Functions   OR   CLASSES!!
	load()
	global data
	output = []
	for i,rec in enumerate( records ):
		rec = rec.replace( '\n ', '' )
		dic = {}
		dic['ATTENDEE'] = []
		# _.pr('_______________')
		att = attendee(rec)
		if not att is None:
			rec = rec.replace( att['raw'], '' )
			dic['ATTENDEE'] = ', '.join(att['emails'])
		# _.pv(att)11
		for line in rec.split('\n'):
			if line.startswith('UID:'):
				dic['UID'] = line.replace( 'UID:', '' )
			if line.startswith('LOCATION:'):
				dic['LOCATION'] = line.replace( 'LOCATION:', '' )
			elif line.startswith('DESCRIPTION:'):
				dic['DESCRIPTION'] = line.replace( 'DESCRIPTION:', '' )
			elif line.startswith('DTSTART;VALUE=DATE:'):
				dic['DTSTART'] = line.replace( 'DTSTART;VALUE=DATE:', '' )
			elif line.startswith('DTEND;VALUE=DATE:'):
				dic['DTEND'] = line.replace( 'DTEND;VALUE=DATE:', '' )
			elif line.startswith('DTSTART;TZID='):
				dic['DTSTART'] = line.replace( 'DTSTART;TZID=', '' )
			elif line.startswith('DTEND;TZID='):
				dic['DTEND'] = line.replace( 'DTEND;TZID=', '' )
			elif line.startswith('CREATED:'):
				dic['CREATED'] = line.replace( 'CREATED:', '' )
			elif line.startswith('DTSTART:'):
				dic['DTSTART'] = line.replace( 'DTSTART:', '' )
			elif line.startswith('DTEND:'):
				dic['DTEND'] = line.replace( 'DTEND:', '' )
			elif line.startswith('DTSTAMP:'):
				dic['DTSTAMP'] = line.replace( 'DTSTAMP:', '' )
			elif line.startswith('RRULE:'):
				dic['RRULE'] = line.replace( 'RRULE:', '' )
			elif line.startswith('EXDATE:'):
				dic['EXDATE'] = line.replace( 'EXDATE:', '' )
			elif line.startswith('EXDATE;'):
				dic['EXDATE'] = line.replace( 'EXDATE;', '' )
			elif line.startswith('ORGANIZER:'):
				dic['ORGANIZER'] = line.replace( 'ORGANIZER:', '' )
			elif line.startswith('ORGANIZER;'):
				dic['ORGANIZER'] = line.replace( 'ORGANIZER;', '' )
			elif line.startswith('LAST-MODIFIED:'):
				dic['LAST-MODIFIED'] = line.replace( 'LAST-MODIFIED:', '' )
			elif line.startswith('SEQUENCE:'):
				dic['SEQUENCE'] = line.replace( 'SEQUENCE:', '' )
			elif line.startswith('STATUS:'):
				dic['STATUS'] = line.replace( 'STATUS:', '' )
			elif line.startswith('SUMMARY:'):
				dic['SUMMARY'] = line.replace( 'SUMMARY:', '' )
			elif line.startswith('TRANSP:'):
				dic['TRANSP'] = line.replace( 'TRANSP:', '' )
			elif line.startswith('X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:'):
				dic['X-APPLE-TRAVEL-ADVISORY-BEHAVIOR'] = line.replace( 'X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:', '' )
			elif line.startswith('BEGIN:'):
				dic['BEGIN'] = line.replace( 'BEGIN:', '' )
			elif line.startswith('ACTION:'):
				dic['ACTION'] = line.replace( 'ACTION:', '' )
			elif line.startswith('TRIGGER:'):
				dic['TRIGGER'] = line.replace( 'TRIGGER:', '' )
			elif line.startswith('X-WR-ALARMUID:'):
				dic['X-WR-ALARMUID'] = line.replace( 'X-WR-ALARMUID:', '' )
			elif line.startswith('X-WR-ALARMUID:'):
				dic['X-WR-ALARMUID'] = line.replace( 'X-WR-ALARMUID:', '' )
			elif line.startswith('ACKNOWLEDGED:'):
				dic['ACKNOWLEDGED'] = line.replace( 'ACKNOWLEDGED:', '' )
			elif line.startswith('RECURRENCE-ID;'):
				dic['RECURRENCE-ID'] = line.replace( 'RECURRENCE-ID;', '' )
			elif line.startswith('END:VEVENT'):
				pass
			elif line.startswith('UID:'):
				pass
			elif line.startswith('X-APPLE-STRUCTURED-LOCATION'):
				pass
			else:
				pass
				# _.pr(line)
		# _.pr(rec)
		dic['DTSTART'] = dic['DTSTART'].replace('America/New_York:','')
		dic['DTEND'] = dic['DTEND'].replace('America/New_York:','')
		dic = dic_order(dic)
		output.append(dic)
		# _.pr( dic['DTSTART'] )
		# _.pv(dic)
		# sys.exit()
	pass 
	if _.switches.isActive('Save'):
		_.saveTable2( output, _.switches.values('Save')[0] )



def load():
	global records
	if _.switches.isActive('Files'):
		data = _.getText( _.switches.values('Files')[0], raw=True )
	if _.switches.isActive('URL'):
		import requests
		if not _.switches.values('URL'):
			import _rightThumb._vault as _vault
			u = 'vckSOow6eQUAdfgBNjAgs7p02TY7X0rUUx3ZaQP3B6E8QI82GUjfckDR2CRWFaZP+OjzAZnQiZCILEUkMpqxG16y3VF+BOnQ4txJnKPLLM5oZ2FEKzRBig2T6MDDtA4Chw0uZYhxvlGoiqQl3/PD/nxUh/JjgOFQw2SB2F6GPKLLihZATFhng6BAcGGf6heDVi/Eg0JHKT4='
			url = _vault.s.de(u)
		else:
			url = _.switches.values('URL')[0]
		# data = str(requests.get( _.switches.values('URL')[0] ).content,'iso-8859-1').split('\n')
		data = str(requests.get( url ).content,'iso-8859-1')
	data = data.replace('\r','').split('\n')
	records = []
	active = False
	for line in data:
		if line == 'BEGIN:VEVENT':
			active = True
			record = []
		if active:
			record.append(line)

		if line == 'END:VEVENT':
			records.append( '\n'.join( record ) )
			active = False

_clean = _.regImp( __.appReg, 'record-cleaner' )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





