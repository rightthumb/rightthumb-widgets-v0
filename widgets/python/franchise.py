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
import _rightThumb._encryptString as _blowfish
##################################################

def appSwitches():
	_.switches.register('Franchise', '-f,-franchise')
	_.switches.register('Print', '-print')
	_.switches.register('Stats', '-stats,-stat')
	# _.switches.register('MustInclude', '-i,-include')
	# _.switches.register('RefineLists', '-list,-lists')
	
	_.switches.register('Alias', '-a,-alias')
	_.switches.register('RawPrint', '-rprint,-raw')

	_.switches.register('ListCount', '-l')
	_.switches.register('ListTypes', '-type', 'f m s tv')
	_.switches.register('ListTestOnly', '-test')
	_.switches.register('ListRAW', '-rawlist')


def ListTypes_trigger(data):
	if data == 'f':
		data = 'franchise'
	if data == 'm':
		data = 'movies'
	if data == 's':
		data = 'series'
	if data == 'tv':
		data = 'tv'
	return data       




_.appInfo[focus()] = {
	'file': 'franchise.py',
	'description': 'Entertainmain franchise management',
	'categories': [
						'auto',
						'entertainment',
						'movies',
						'research',
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

_.appInfo[focus()]['relatedapps'].append('pp getFranchiseKeys | p line -u')
_.appInfo[focus()]['relatedapps'].append('pp getFranchiseKeys | p line -u --c | p line --c -make " p franchise -f {} "')
_.appInfo[focus()]['relatedapps'].append('')
_.appInfo[focus()]['examples'].append('p franchise -f james_bond')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p franchise -f alien prometheus -a alien -type f -l 2')
_.appInfo[focus()]['examples'].append('p franchise -f hallmark!! ')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p franchise -f hallmark channel original -a hallmark -type m -l 5 -raw')
_.appInfo[focus()]['examples'].append('')

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
	_.switches.trigger('ListTypes',ListTypes_trigger)
	
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
# START

_franchise = _.regImp( __.appReg, '_rightThumb._franchise' )

def action():

	if _.switches.isActive('ListTestOnly'): _franchise.switch( 'ListTestOnly', _.switches.value('ListTestOnly') )
	if _.switches.isActive('ListRAW'): _franchise.switch( 'ListRAW', _.switches.value('ListRAW') )
	




	if _.switches.isActive('Franchise'):
		_franchise.switch( 'Franchise', _.switches.value('Franchise') )
		
	if _.switches.isActive('Alias'):
		_franchise.switch( 'Alias', _.switches.value('Alias') )
	
	if _.switches.isActive('ListCount'):
		_franchise.switch( 'ListCount', _.switches.value('ListCount') )

	if _.switches.isActive('ListTypes'):
		_franchise.switch( 'ListTypes', _.switches.value('ListTypes') )





	#n)--> THE ABOVE WAS JUST ADDED



	if _.switches.isActive('Print'):
		_franchise.switch( 'Franchise', _.switches.value('Franchise') )

		if _.switches.isActive('MustInclude'):
			_franchise.switch( 'MustInclude', _.switches.value('MustInclude') )

		if _.switches.isActive('RefineLists'):
			_franchise.switch( 'RefineLists', _.switches.value('RefineLists') )

		_.pr( len( __.franchises ) )
		_franchise.imp.printFranchise()
		sys.exit()



	
		
	if _.switches.isActive('Franchise'):
		_franchise.switch( 'Franchise', _.switches.value('Franchise') )
		
	if _.switches.isActive('Alias'):
		_franchise.switch( 'Alias', _.switches.value('Alias') )
	
	if _.switches.isActive('ListTestOnly'):
		_franchise.switch( 'ListTestOnly', _.switches.value('ListTestOnly') )
	

	if _.switches.isActive('ListCount'):
		_franchise.switch( 'ListCount', _.switches.value('ListCount') )

	if _.switches.isActive('ListTypes'):
		_franchise.switch( 'ListTypes', _.switches.value('ListTypes') )
	


	if _.switches.isActive('Stats'):
		_franchise.switch( 'Stats' )

	
	_franchise.imp.action()



# __.franchises = _.getTable( 'imdb_franchises_NEW.json' )
########################################################################################
if __name__ == '__main__':
	action()







