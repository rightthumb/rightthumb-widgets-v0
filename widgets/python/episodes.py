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
						'imdb',
						'show',
						'episodes',
						'ent',
						'entertainment',
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
	if len(parts) > 4 and parts[0][0] in '0123456789':
		a = parts[0]
		parts = parts[1:]
		b = parts[0]
		parts = parts[1:]
		c = parts[0]
		parts = parts[1:]
		d = ' '.join( parts )
		parts=[]
		parts.append(a)
		parts.append(b)
		parts.append(c)
		parts.append(d)

	# _.pr(parts)
	if len(parts) == 4:
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
	#     return ''
	# if len(par[1]) == 1:
	#     ep = par[0]+'.0'+par[1]
	
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
		line = parts[0] + '    '+parts[1]+'    '+parts[2]+'    '+parts[3]
	except Exception as e:
		line = ''
	line = _str.do('file', line)
	if not '-' in parts[1]:
		return ''

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


# folder = 'C:\\Users\\Scott\\.rt\\profile\\projects\\ent'
folder = _v.home + '/.rt/profile/projects/ent'.replace('/',os.sep)
_.pr(folder)
	

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()