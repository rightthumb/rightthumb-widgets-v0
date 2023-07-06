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

##################################################


def appSwitches():
	pass
	_.switches.register( 'Query', '-q,-query' )
	_.switches.register( 'ResultCount', '-c,-count' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'NoPrint', '-noprint' )
	_.switches.register( 'NoAsk', '-noask' )



	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'google.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'search google',
	'categories': [
						'google',
						'web',
						'internet',
						'search',
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
						'p google -q amanda tapping',
						''
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
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
	_.switches.trigger( 'Files',_.myFileLocations )
	
	
	
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
# __.appRegPipe
########################################################################################
# START

# import google
# google.LICENSE_KEY = '4fbf124ec3255efed6b95f2685a95c93e557823f'
# google.LICENSE_KEY = 'AIzaSyB2soQ6-tsUOYN2E2bRfyCCv82Css_2bPY'

try: 
	from googlesearch import search
except ImportError:  
	_.pr("No module named 'google' found") 


# for x in dir( search ):
#     _.pr( x )
# sys.exit()

def action():
	_.updateLine( 'Searching google.com                     ' )
	# for x in dir( google.standard_search.GoogleResult ):
		# _.pr( x )
	# data = google.doGoogleSearch('python')
	# google.standard_search.search = 'python'
	# data = 
	# _.pr( data )
	query = ' '.join( _.switches.values('Query') )
	# _.switches.value('Query').replace( ',', ' ' )
	# query = _.ci( query )

	saveFile = _str.stripNonAlphaNumaric( query, also=' _-' )
	saveFile = saveFile.replace( ' ', '_' )
	# saveFile = _str.replaceAll( saveFile, ' ', '_' )
	saveFile = _str.cleanBE( saveFile, ' ' )

	if _.switches.isActive('ResultCount'):
		stop = int( _.switches.values('ResultCount')[0] )
	else:
		stop = 5

	saveFile = 'google_search__' + saveFile + '__count_' + str(stop) + '__.json'

	data = _.getTable( saveFile )

	if len( data ):
		srcSave = 1
	else:
		srcSave = 0
		data = []
	
	if not srcSave:

		# for j in search(query, tld="co.in", num=10, stop=1, pause=2):
		for j in search( query, tld='com', num=10, stop=stop ):
			data.append( j )

		_.saveTable( data, saveFile, p=0 )

	_.updateLine( '                                                ' )
	result = {}
	for i,j in enumerate(data):
		x = str(i+1)
		if i+1 < 10:
			x = '  '+ str(i+1)
		elif i+1 < 100:
			x = ' '+ str(i+1)
		if _.showLine(j):
			result[x] = j



	if not _.switches.isActive('NoPrint'):
		if not _.switches.isActive('Clean'):
			_.pr()
			if not srcSave:
				_.colorThis( [  '', '(', 'live', ')'  ], 'darkcyan' )
			else:
				_.colorThis( [  '', '(', 'archive', ')'  ], 'darkcyan' )


		_.pr()
		for key in result:
			_.pr( key, result[key] )


		if not _.switches.isActive('NoAsk'):
			# _.pv( result )
			_copy = _.regImp( __.appReg, '-copy' )
			_.pr()
			ask = input( '  id?: ' )
			if len(ask):
				i = int(ask)
				if i+1 < 10:
					x = '  '+ str(i)
				elif i+1 < 100:
					x = ' '+ str(i)
				try:
					_copy.imp.copy( result[x] )
				except Exception as e:
					_.cp( [ 'Error: did not copy', 'red' ] )
					_.cp( [ 'Error: did not copy', 'red' ] )
				else:
					_.cp( [ 'copied' ], 'green' )

			

	
	return data


########################################################################################
if __name__ == '__main__':
	action()







