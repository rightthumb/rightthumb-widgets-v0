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
	'file': 'taboo.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'taboo game',
	'categories': [
						'game',
						'taboo',
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
						_.hp('p taboo'),
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



def action():
	load()
	global data

	_.fields.register( 'project', 'name', '111111111111111111111' )
	total = 0
	for i,card in enumerate(data):
		if card['level'] == 0:
			total+=1
	# _.pv(data[0])


	# for i,card in enumerate(data):
	#     data[i]['level']=0
	# _.saveTableDB( data, 'taboo.json' )
	# sys.exit()
	#     _.clear()
	#     _.fields.register( 'project', 'name', card['subject'] )
	#     for mit in card['omit']:
	#         _.fields.register( 'project', 'name', mit )

	# _.pr( len(  _.fields.value( 'project', 'name', 'test', center=True )  ) );sys.exit();
	i=-1
	isBack=False
	while True:
		i+=1
		try:
			card = data[i]
		except Exception as e:
			sys.exit()
		try:
			level = data[i]['level']
		except Exception as e:
			level = 0
		if _.switches.isActive('Plus'):
			isBack=True
		if isBack or (  ( level == 0 ) and _.showLine(card['subject'])  ):
			_.clear()
			_.cp('|'+ _.fields.value( 'project', 'name', card['subject'], center=True )+'|', 'Background.green' )
			for mit in card['omit']:
				_.cp('|'+_.fields.value( 'project', 'name', mit, center=True )+'|', 'Background.red' )
			# _.pr( 'q(quit), b(back)' )
			
			# _.pr()
			# _.pr()
			_.pr( _.fields.value( 'project', 'name', str(i+1)+' of '+str(total)+', '+str(len(data)), center=True ) )
			_.pr( _.fields.value( 'project', 'name', '(q)uit (b)ack', center=True ) )
			isBack=False
			wait=input('lvl: ')
			if wait.lower()=='q' or wait.lower()=='x':
				sys.exit()
			
			if wait.lower()=='b':
				isBack=True
				i-=2
			elif len(wait):
				try:
					data[i]['level'] = int(wait)
					_.saveTableDB( data, 'taboo.json' )
				except Exception as e:
					pass
		# {
		#     "subject": "drama",
		#     "omit": [
		#         "genre",
		#         "queen",
		#         "soap",
		#         "movie",
		#         "book"
		#     ]
		# }

		# Background.green
		# Background.red

		# _.fields.register( 'project', 'name', value )

		# _.fields.value( 'project', 'name', value )

def load():
	global data
	data = _.getTableDB( 'taboo.json' )
	random.shuffle(data)

import random

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





