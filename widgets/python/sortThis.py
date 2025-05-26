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

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-input','file.txt')
	# _.switches.register('Files', '-f,-file','file.txt')
	_.switches.register('Level', '-level')
	_.switches.register('Dic', '-dic')
	_.switches.register('Asc', '-asc')
	_.switches.register('Desc', '-desc')
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	

_.autoBackupData = False


_.appInfo[focus()] = {
	'file': 'sortThis.py',
	'description': 'Sort pipe data',
	'categories': [
						'pipe',
						'manipulate',
						'tool',
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
						'type out_file.txt | p inChar | p sortThis | p countEach',
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
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def action():
	# sorted(var, key=lambda v: (v.upper(), v[0].islower()))
	
		# _.pr( 'HERE' )
	newPipe = []
	dic = []
	for i,row in enumerate( _.myData() ):
		# _.pr(row)
		row = row.replace( '\n', '' )
		row = row.replace( '\r', '' )
		original = row
		if _.switches.isActive( 'Level' ) or _.switches.isActive( 'Dic' ):
			row = row.lower()
			row = _str.clean_latin1( row )
			row = _str.cleanBE(row,' ')
		if len( row ):
			newPipe.append( row )
			if _.switches.isActive( 'Level' ):
				dic.append({ 'original': original, 'sortable': row })
			else:
				dic.append({ 'sortable': row })

		pipeData = newPipe

	if _.switches.isActive( 'Desc' ):
		data = _.tables.returnSorted( 'data', 'd.sortable', dic )
	else:
		data = _.tables.returnSorted( 'data', 'a.sortable', dic )
	
	if _.switches.isActive( 'Dic' ):
		_.saveTable( data, 'sortThis_tmp.json' )
	else:
		for row in data:
			_.pr( row['sortable'] )

	# for d in sorted(pipeData, key=lambda v: (v.upper(), v[0].islower())):
	#     d = d.replace('\n','')
	#     d = d.replace('\r','')
	#     _.pr(d)



# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()







