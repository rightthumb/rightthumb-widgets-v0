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
##################################################

def appSwitches():
	pass
	_.switches.register('Input', '-i,-input','file_profile;imports examples')
	_.switches.register('Test', '-test','0-4')

	# _.switches.register('Files', '-f,-file,-files','file.txt')
	# _.switches.register('Test', '-test', isRequired=True)


	"""
	_.switches.documentation( 'Test', { 
										'description': 'test switch',
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True


_.appInfo[focus()] = {
	'file': 'appRegDataTool.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search application registration information, specific fields',
	'categories': [
						'DEFAULT'
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
						'p appRegDataTool -i file_profile;imports examples',
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )


########################################################################################
# START



def action():
	global data
	global spent_list
	load()

	test = 2

	if _.switches.isActive( 'Test' ):
		test = int( _.switches.value( 'Test' ) )

	if _.switches.isActive( 'Input' ):
		test = 4

	if test == 0:
		for record in data:
			try:
				for imports in record['file_profile']['imports']:
					for example in imports['examples']:
						if not '_.' in example and not ' _' in example and not '_str' in example and not '=_' in example and not example.startswith('_'):
							# _.pr( example )
							thisExample = _str.namespace( imports['namespace'][0], example )
							if not thisExample in spent_list and not type(thisExample) == bool:
								spent_list.append( thisExample )
								_.pr( thisExample )
			except Exception as e:
				pass


	if test == 1:
		for record in data:
			try:
				for imports in record['file_profile']['imports']:
					if not imports['namespace'][0] in spent_list:
						_.pr( imports['namespace'][0] )
						spent_list.append( imports['namespace'][0] )
			except Exception as e:
				pass

	if test == 2:
		for record in data:
			for imports in record['file_profile']['imports']:
				for example in imports['examples']:
					thisExample = _str.namespace( imports['namespace'][0], example )
					if not thisExample in spent_list and not type(thisExample) == bool:
						spent_list.append( thisExample )
						_.pr( thisExample )


	if test == 3:
		for record in data:
			for app in record['relatedapps']:
				if not app in spent_list:
					spent_list.append( app )
					_.pr( app )

	if test == 4:
		global valueOffset
		for record in data:
			valueOffset=0
			generateQuery( record )


	if test == 5:
		for i,record in enumerate(data):
			for ii,imports in enumerate(record['file_profile']['imports']):
				if '_rightThumb' == data[i]['file_profile']['imports'][ii]['app']:
					data[i]['file_profile']['imports'][ii]['app'] = extractAppName( data[i]['file_profile']['imports'][ii]['raw'] )
					
					

				data[i]['file_profile']['imports'][ii]['namespace_tree'] = []
				for iii,example in enumerate(imports['examples']):
					namespace_tree = []
					thisExample = _str.namespace( imports['namespace'][0], example )
					if not thisExample in spent_list and not type(thisExample) == bool:
						spent_list.append( thisExample )
						_.pr( thisExample )
						if not thisExample in namespace_tree:
							namespace_tree.append( thisExample )
							data[i]['file_profile']['imports'][ii]['namespace_tree'].append( thisExample )
		_.saveTableDB( data, 'appRegistration.json' )



	_.pr()
	_.pr( '', len( spent_list ) )


def extractAppName( data ):
	for row in data.split(' '):
		if '_rightThumb' in row:
			return row
	return data

def generateQuery( data ):
	global valueOffset
	global spent_list
	fieldBase = "['THIS']"
	commandBase = 'data'
	isLast = False
	pastDone = False
	if len( _.switches.values( 'Input' ) ) == ( valueOffset+1 ):
		isLast = True
	if len( _.switches.values( 'Input' ) ) < ( valueOffset+1 ):
		pastDone = True

	if not pastDone:
		buildCommand = commandBase
		# _.pr( valueOffset )
		selectedValue = _.switches.values( 'Input' )[valueOffset].split(';')
		valueOffset+=1
		for key in selectedValue:
			buildCommand += fieldBase.replace( 'THIS', key )

		newData = eval( buildCommand )


			

		if type(newData) == list:
			for record in newData:
				if isLast:
					if not record in spent_list:
						spent_list.append( record )
						_.pr( '\t', record )
				else:
					if not isLast:
						generateQuery( record )
		else:
			if isLast:
				if not newData in spent_list:
					spent_list.append( newData )
					_.pr( '\t', newData )



def load():
	global data
	data = _.getTableDB( 'appRegistration.json' )

valueOffset = 0
data = []
spent_list = []
########################################################################################
if __name__ == '__main__':
	action()