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
import platform

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


import _rightThumb._base3b as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'littleAlchemy.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'little alchemy cheat',
	'categories': [
						'little alchemy',
						'cheat',
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
						'p thisApp -file file.txt',
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
# START

def action():
	global hack
	global names
	global combinations
	load()


	ids = []
	for x in hack:
		found = False
		for k in names:
			if names[k] == x:
				found = True
				ids.append(int(k))
		if not found:
			_.colorThis( 'Error:', k, names[k] )


	# print( ids )
	# sys.exit()
	i=0
	for key in combinations.keys():
		# print( type(combinations[key]), combinations[key].keys() )
		if not int(key) in ids:
			found = 0
			for x in combinations[key][  list(combinations[key].keys())[0]  ]:
				# print(x)
				if x[0] in ids and x[1] in ids:
					i+=1

					found += 1
					print()
					if found == 1:
						print()
						_.colorThis( [ names[ str(key) ] ] , 'yellow' )
					_.colorThis( [ '\t', names[ str(x[0]) ] ] , 'green' )
					_.colorThis( [ '\t', names[ str(x[1]) ] ] , 'green' )
					# break
		# print()

	_.colorThis( [  '\n\n', i  ], 'red' )
		# if not len(record) == 3 and not len(record) == 2:
		#     print( (record) )

	# print( combinations.keys() )
	pass


def load():
	global hack
	global names
	global combinations
	hasError = False
	if not os.path.isfile( 'names.json' ):
		_.colorThis( [ 'Missing file: names.json' ], 'red' )
		hasError = True

	if not os.path.isfile( 'combinations.json' ):
		_.colorThis( [ 'Missing file: combinations.json' ], 'red' )
		hasError = True
	if hasError:
		sys.exit()

	names = _.getTable2( 'names.json' )
	combinations = _.getTable2( 'combinations.json' )
	hack = "hackData = []\n$('.elementName').each(function() {\n    hackData.push($(this).text());\n});\ncopy(hackData)"
	# hack = "hackData = []\n$('.elementName').each(function() {\n    hackData.push($(this).text());\n});\ncopy(hackData.join('\\n'))"
	
	if not os.path.isfile( 'littlealchemy_hack.js' ):
		ask = 'y'
	else:
		ask = input( 'Reset List ? :' )

	if 'y' in ask:
		_.saveText( hack, 'littlealchemy_hack.js' )
		hack = []
		do = 'start "EDIT" "notepad" "'+'littlealchemy_hack.js' +'"'
		os.system( '"' + do + '"' )
		pause=input( 'pause: ' )


	if platform.system() == 'Windows':
		do = 'cls'
	else:
		do = 'clear'
	os.system( '"' + do + '"' )
	print()
	print()

	txt = _.getText( 'littlealchemy_hack.js', raw=True, clean=2 )
	if 'hackData'.lower() in txt.lower():
		_.colorThis( [ 'Error: paste hack results in the text file' ], 'red' )
		sys.exit()


	hack = _.getTable2( 'littlealchemy_hack.js' )
# littlealchemy_images.json


hack = []
names = []
combinations = []
########################################################################################
if __name__ == '__main__':
	action()



# switches
# colorThis
# clearFocus
# load
# defaultScriptTriggers
# setPipeData
# postLoad
# showLine






