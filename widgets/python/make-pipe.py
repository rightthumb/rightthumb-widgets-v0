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
	_.switches.register( 'Zeros', '-z,-zero,-zeros' )
	_.switches.register( 'Spaces', '-sp,-space,-spaces' )
	_.switches.register( 'Text', '-t,-text,-make' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	### EXAMPLE: END

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
	'file': 'make-pipe.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'pipe make',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'pipe',
						'make',
						'generate',
						'code',
						'tool',
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
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )


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
########################################################################################
# START
cows='''flaming-sheep
apt
tux
sheep
ren
milk
dragon
vader-koala
bud-frogs
koala
elephant
snowman
moose
unipony
kangaroo
turkey
ghostbusters
cheese
turtle
eyes
pony-smaller
hellokitty
cower
three-eyes
www
elephant-in-snake
skeleton
moofasa
suse
luke-koala
unipony-smaller
mech-and-cow
daemon
stegosaurus
duck
fox
vader
cock
default
kiss
gnu
pony
calvin
bunny
kosh
stimpy'''.split('\n')
cow=-1
def have_a_cow():
	global cows
	global cow
	cow+=1
	try: cows[cow]
	except Exception as ee: cow = 0
	return cows[cow]


def action():
	cnt=0
	text = _.ci(' '.join( _.switches.values('Text') ))

	for i,row in enumerate( _.pp() ):
		if _.showLine(row):
			line = text.replace( '{{}}', row.replace(' ','_') )
			line = line.replace( '{}', row )
			if '{cow}' in line:
				line=line.replace('{cow}',have_a_cow())
			if '{n}' in line:
				cnt+=1
				if _.switches.isActive('Zeros'):
					line=line.replace('{n}',_.zeros3(cnt,len(_.myData())))
				elif _.switches.isActive('Spaces'):
					line=line.replace('{n}',_.zeros3(cnt,len(_.myData()),' '))
				else:
					line=line.replace('{n}',str(cnt))

			line = line.replace( '{}', row )
			_.pr(line)



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()