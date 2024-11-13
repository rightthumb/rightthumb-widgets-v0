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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
	# _blowfish.genPassword('string')


_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
##################################################
import glob
##################################################

def appSwitches():
	pass
	_.switches.register( 'Folder', '-folder', 'D:\\_Scott\\S_Documents\\Sites\\RightThumb\\projects\\john\\js' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='One or more javascript file' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='' )


	_.switches.documentation( 'Plus', { 
										'description': 'glob. example: *.js'
									} )
	"""
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.isRequired_or_List = ['Pipe','Files','Plus']


_.appInfo[focus()] = {
	'file': 'auditJavascriptFileNamespaceAndProcessManagement.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Audit the namespace and process management in file or list of files and how it is used in a website',
	'categories': [
						'javascript',
						'web',
						'www',
						'audit',
						'namespace',
						'js',
						'.js',
				],
	'relatedapps': [
						'_rightThumb._auditCodeBase',
						'',
						'p auditCodeBase_locationTable',
						'',
						'',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p auditJavascriptFileNamespaceAndProcessManagement -f ',
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})



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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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



		# _.pr( closeingChar )
def process():
	global allFiles
	
	# p inFunc -i D:\tech\programs\python\_rightThumb\_auditCodeBase\__init__.py

	test = 7

	if test == 0:
		_code.imp.validator.register( allFiles, 'javascript' )
		_code.imp.validator.process()

	if test == 1:
		_code.imp.loadProject()
		namespace = _code.imp.validator.link_jsNameSpace_to_function_payloads()

	if test == 2:
		index = _code.imp.validator.createIndex( allFiles, 'javascript' )
		index = _code.imp.validator.auditTable()
		# _.printVar( index )

		# auditJavascriptFileNamespaceAndProcessManagement


	if test == 3:
		_code.imp.loadProject()
		# _code.imp.validator.printPos( 810, 841+1 )
		# _code.imp.validator.printPos( 184518, 184520 )
		_code.imp.validator.printPos( 13620, 13630 )
		# _code.imp.validator.printPos( 174, 184520 )

	if test == 4:
		index = _code.imp.validator.createIndex( allFiles, 'javascript' )
		# _.pr( index )
		# _.printVar( index )
		_code.imp.validator.colorPrint()


	if test == 5:

		_.pr( allFiles )

	if test == 6:
		index = _code.imp.validator.createIndex( allFiles, 'javascript' )
		_code.imp.validator.readCode()

	if test == 7:
		start = time.time()
		index = _code.imp.validator.createIndex( allFiles, 'javascript' )
		# index = _code.imp.validator.createIndex( allFiles, 'javascript', skipLoad=True )

		data = _code.imp.validator.jsNameSpace()
		for record in data['functions']:
			# test = _code.imp.validator.printPos( record['linePos'] , record['open'], p=0 )
			# _.pr( test )
			_.pr( record['ns'] )
		end = time.time()
		# _.pr( 'time:', end-start )

		# _code.imp.validator.jsNameSpace_Old()
		# _code.imp.validator.javascriptNamespace()
		# _code.imp.validator.link_jsNameSpace_to_function_payloads()


	# _code.imp.validator.auditOmit()

	# namespace = _code.imp.validator.quickTest()


	# namespace = _code.imp.validator.jsNameSpace()

	# # _.printVar( namespace )

	# for ns in namespace:
	#     if ns['ns'] == 'family.talk.adherence':
	#         _.printVar( ns )
	#         _code.imp.validator.printPos( ns['record']['start'], ns['record']['end'] )



	# _code.imp.validator.findStringInAsset( 'family.v.shouldRun=' )


	# _code.imp.validator.printPos( 2624, 19264+1 )
	# _code.imp.validator.printPos( 2624, 19264+1 )
	# _code.imp.validator.printPos( 2150, 2415 )
	# _code.imp.validator.jsNameSpace()



def acquire( row ):
	global allFiles
	file = _.getText( row, raw=True )
	allFiles += file + '\n'



def action():

	# indexes = _.getTable( 'auditCodeBase_projectMD5_0b00f62a91a78c45e0ced77793a1b19e.json' )

	# _.printVar( indexes['totals'] )
	# sys.exit()


	load()

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner()
		# _.printVar(_.appData)
		for i,row in enumerate(_.appData[__.appReg]['pipe']):
			acquire( row )
		process()



def load():
	if _.switches.isActive('Plus'):
		if _.switches.isActive('Folder'):
			folder = _.switches.values('Folder')[0]
		else:
			folder = os.getcwd()
		files = os.listdir( folder )
		selection = []
		for file in files:
			if _.showLine( file ):
				selection.append( file )

		_.setPipeData( selection, __.appReg )



allFiles = ''
data = []
########################################################################################
if __name__ == '__main__':
	action()







