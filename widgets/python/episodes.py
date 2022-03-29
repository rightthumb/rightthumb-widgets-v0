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
	pass
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

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
	# 'app': '7facG-jo0Cxk',
	'file': 'episodes.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'creates folder and files for episode documentation',
		# _.ail(1,'subject')+
		# _.aib('one')+
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
						_.hp('ee stargate atlantis | p episodes'),
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

data='''
2004-2009 Stargate: Atlantis

        Seasons:  5


  SEASON         ID       DATE               TITLE

  Season: 01     1:1      2004-07-16         Rising
                 1:2      2004-07-23         Hide and Seek
                 1:3      2004-07-30         Thirty Eight Minutes
                 1:4      2004-08-06         Suspicion
                 1:5      2004-08-13         Childhood's End
                 1:6      2004-08-20         Poisoning the Well
                 1:7      2004-08-27         Underground
                 1:8      2004-09-10         Home
                 1:9      2004-09-17         The Storm
                 1:10     2005-01-21         The Eye
                 1:11     2005-01-28         The Defiant One
                 1:12     2005-02-04         Hot Zone
                 1:13     2005-02-11         Sanctuary
                 1:14     2005-02-18         Before I Sleep
                 1:15     2005-02-25         The Brotherhood
                 1:16     2005-03-04         Letters from Pegasus
                 1:17     2005-03-11         The Gift
                 1:18     2005-03-18         The Siege: Part 1
                 1:19     2005-03-25         The Siege: Part 2
  Season: 02     2:1      2005-07-15         The Siege: Part 3
                 2:2      2005-07-22         The Intruder
                 2:3      2005-07-29         Runner
                 2:4      2005-08-05         Duet
                 2:5      2005-08-12         Condemned
                 2:6      2005-08-19         Trinity
                 2:7      2005-08-26         Instinct
                 2:8      2005-09-09         Conversion
                 2:9      2005-09-23         Aurora
                 2:10     2005-09-23         The Lost Boys
                 2:11     2006-01-06         The Hive
                 2:12     2006-01-13         Epiphany
                 2:13     2006-01-20         Critical Mass
                 2:14     2006-01-27         Grace Under Pressure
                 2:15     2006-02-03         The Tower
                 2:16     2006-02-10         The Long Goodbye
                 2:17     2006-02-17         Coup D'etat
                 2:18     2006-02-24         Michael
                 2:19     2006-03-03         Inferno
                 2:20     2006-03-10         Allies
  Season: 03     3:1      2006-07-14         No Man's Land
                 3:2      2006-07-21         Misbegotten
                 3:3      2006-07-28         Irresistible
                 3:4      2006-08-04         Sateda
                 3:5      2006-08-11         Progeny
                 3:6      2006-08-18         The Real World
                 3:7      2006-08-25         Common Ground
                 3:8      2006-09-08         McKay and Mrs. Miller
                 3:9      2006-09-15         Phantoms
                 3:10     2006-09-22         The Return: Part 1
                 3:11     2007-04-13         The Return: Part 2
                 3:12     2007-04-20         Echoes
                 3:13     2007-04-27         Irresponsible
                 3:14     2007-05-04         Tao of Rodney
                 3:15     2007-05-11         The Game
                 3:16     2007-05-18         The Ark
                 3:17     2007-06-01         Sunday
                 3:18     2007-06-08         Submersion
                 3:19     2007-06-15         Vengeance
                 3:20     2007-06-22         First Strike
  Season: 04     4:1      2007-09-28         Adrift
                 4:2      2007-10-05         Lifeline
                 4:3      2007-10-12         Reunion
                 4:4      2007-10-19         Doppelganger
                 4:5      2007-10-26         Travelers
                 4:6      2007-11-02         Tabula Rasa
                 4:7      2007-11-09         Missing
                 4:8      2007-11-16         The Seer
                 4:9      2007-11-30         Miller's Crossing
                 4:10     2007-12-07         This Mortal Coil
                 4:11     2008-01-04         Be All My Sins Remember'd
                 4:12     2008-01-11         Spoils of War
                 4:13     2008-01-18         Quarantine
                 4:14     2008-01-25         Harmony
                 4:15     2008-02-01         Outcast
                 4:16     2008-02-08         Trio
                 4:17     2008-02-15         Midway
                 4:18     2008-02-22         The Kindred: Part 1
                 4:19     2008-02-29         The Kindred: Part 2
                 4:20     2008-03-07         The Last Man
  Season: 05     5:1      2008-07-11         Search and Rescue
                 5:2      2008-07-18         The Seed
                 5:3      2008-07-25         Broken Ties
                 5:4      2008-08-01         The Daedalus Variations
                 5:5      2008-08-15         Ghost in the Machine
                 5:6      2008-08-22         The Shrine
                 5:7      2008-09-05         Whispers
                 5:8      2008-09-12         The Queen
                 5:9      2008-09-19         Tracker
                 5:10     2008-09-26         First Contact
                 5:11     2008-10-10         The Lost Tribe
                 5:12     2008-10-17         Outsiders
                 5:13     2008-10-24         Inquisition
                 5:14     2008-11-07         The Prodigal
                 5:15     2008-11-14         Remnants
                 5:16     2008-11-21         Brain Storm
                 5:17     2008-12-05         Infection
                 5:18     2008-12-12         Identity
                 5:19     2008-12-19         Vegas
                 5:20     2009-01-09         Enemy at the Gate

 99 episodes


isCanceled: True

'''

# test[1:]
# test[:-1]

# test[-1]

def sections(line):
	line = clean(line)

	parts = []
	while len(clean(line)):
		line = clean(line)
		sub = line.split(' ')[0]
		line = line[ len(sub) : ]
		parts.append(sub)
	if len(parts) > 3 and parts[0][0] in '0123456789':
		a = parts[0]
		parts = parts[1:]
		b = parts[0]
		parts = parts[1:]
		c = ' '.join( parts )
		parts=[]
		parts.append(a)
		parts.append(b)
		parts.append(c)

	if len(parts) == 3:
		ep = parts[0]
		par = ep.split('.')
		if len(par) < 2:
			return ''
		if len(par[1]) == 1:
			ep = par[0]+'.0'+par[1]
		parts[0] = ep
	return parts

	# ep = line.split(' ')[0]
	# line = line[ len(ep) : ]
	# line = clean(line)
	# da = line.split(' ')[0]

	# epb = ep
	# par = ep.split('.')
	# if len(par) < 2:
	# 	return ''
	# if len(par[1]) == 1:
	# 	ep = par[0]+'.0'+par[1]
	
	# line = ep + line[ len(epb)+1 : ]

def clean(string):
	string = string.replace( '\r', '' )
	string = string.replace( '\t', '    ' )
	string = _str.do( 'be', string, '\n' )
	string = _str.do( 'be', string, '\t' )
	string = _str.do( 'be', string, ' ' )
	return string

def process(line):
	line = clean(line)
	if 'Season: ' in line:
		line = '  '+line
		s = line.split('  ')[1]
		line = line.replace( s, '' )
	line = line.replace( ':', '.' )
	parts = sections(line)
	# line = str(parts)
	try:
		line = parts[0] + '    '+parts[1]+'    '+parts[2]
	except Exception as e:
		line = ''
	line = _str.do('file', line)

	return line
def action():
	global folder
	# global data

	data = '\n'.join( _.isData(r=1) )


	data = clean(data)

	lines = data.split('\n')


	while not len(clean(lines[0])):
		lines = lines[1:]

	while lines[-1] == clean(lines[-1]):
		lines = lines[:-1]

	show = lines[0]
	show = _str.do('file', show, 1)
	files = []
	started=False
	for line in lines:
		if 'Season: 01' in line:
			started = True

		if started:
			line = process(line)
			if line:
				files.append(line)
	pass
	fo = folder +os.sep+ show
	if not os.path.isdir(fo):
		_v.mkdir(fo)

	for file in files:
		path = fo+os.sep+file
		if not os.path.isfile(path):
			_.saveText( '', path )


folder = 'C:\\Users\\Scott\\.rt\\profile\\projects\\ent'

	

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





