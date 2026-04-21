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

# import os
import sys
import time
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._encryptString as _blowfish
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Add', '-add')
	_.switches.register('Remove', '-remove')
	
	



_.appInfo[focus()] = {
	'file': 'dicTable.py',
	'description': 'Manage  dictionary table',
	'categories': [
						'research',
						'dictionary manipulation',
				],
	'relatedapps': [],
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appData[focus()] = {
	'start': time.time(),
	'uuid': '',
	'audit': [],
	'pipe': [],
	}

_.appInfo[focus()]['examples'].append('p dicTable -i dic_noun.json -add jane ')
_.appInfo[focus()]['examples'].append('p dicTable -i dic_noun.json -remove to ')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('\tdic_pronoun.json')
_.appInfo[focus()]['examples'].append('\tdic_noun.json')
_.appInfo[focus()]['examples'].append('\tdic_verb.json')
_.appInfo[focus()]['examples'].append('\tdic_adj.json')
_.appInfo[focus()]['examples'].append('\tdic_adv.json')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('\tdic_omit.json')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('\tdic_all.json')







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

	# _.switches.trigger('Input',_.myFileLocations)
		# trigger settings
	_.myFileLocation_Print = False

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	
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


########################################################################################
########################################################################################
# START

def inTable( word ):
	global data
	try:
		for test in data.keys():
			if test == word:
				return True
	except Exception as e:
		pass
	return False

def action():
	global data
	global file

	if _.switches.isActive('Add'):
		word = _.switches.value('Add').lower()
		if not inTable( word ):
			try:
				data[word] = 1
			except Exception as e:
				data = {}
				data[word] = 1
			_.saveTable( data, file )

	if _.switches.isActive('Remove'):
		word = _.switches.value('Remove').lower()
		if inTable( word ):
			newData = {}
			for test in data.keys():
				if not test == word:
					newData[test] = 1

			_.saveTable( newData, file )
if __name__ == '__main__':
	if _.switches.isActive('Input'):
		file = _.switches.value('Input')
	else:
		_.pr()
		_.pr( 'Expected:' )
		_.pr('\tp dicTable -i dic_noun.json -add jane ')
		_.pr('\tp dicTable -i dic_noun.json -remove to ')
		sys.exit()
	data = _.getTable( file )
########################################################################################
if __name__ == '__main__':
	action()