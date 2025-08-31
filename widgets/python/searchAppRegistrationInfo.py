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
##################################################

def appSwitches():
	_.switches.register('Fields', '-f,-fields')
	_.switches.register('RemoveDefault', '-remove')
	_.switches.register('RequiredCategoriesCount', '-r,-require','2')
	_.switches.register('PrintRemoved', '-pr,-removed,-printremoved,-print')
	
	_.switches.register('NoCount', '--c')



_.appInfo[focus()] = {
	'file': 'searchAppRegistrationInfo.py',
	'description': 'Search for app registration information',
	'categories': [
						'research',
						'management',
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

_.appInfo[focus()]['prerequisite'].append('b py')
_.appInfo[focus()]['prerequisite'].append('p f -in *.py + _rightThumb._base -jn | p appInfo')
_.appInfo[focus()]['prerequisite'].append('')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + function')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + manipulation')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + thisApp.py')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + Changes the world')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + manipulation - text')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + text -fields c')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + manipulation -remove f d c')
_.appInfo[focus()]['examples'].append('p searchAppRegistrationInfo + text -or research -r 2')
_.appInfo[focus()]['examples'].append('')



_.appInfo[focus()]['columns'].append({'name': 'file', 'abbreviation': 'f'})
_.appInfo[focus()]['columns'].append({'name': 'description', 'abbreviation': 'd'})
_.appInfo[focus()]['columns'].append({'name': 'categories', 'abbreviation': 'c'})



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
	_.switches.trigger('RemoveDefault',_.formatColumns)
	_.switches.trigger('Fields',_.formatColumns)
	
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

def action():
	global data
	load()

	if not _.switches.isActive( 'NoCount' ):
		_.pr()

	rid = []
	if _.switches.isActive( 'RemoveDefault' ):
		rid = []
		if not len( _.switches.value( 'RemoveDefault' ) ):
			for i,record in enumerate(data):
				if record['file'] == 'thisApp.py':
					rid.append( i )
				elif record['description'] == 'Changes the world':
					rid.append( i )
				else:
					try:
						found = 0
						DEFAULT = False
						for row in record['categories']:
							if row == 'DEFAULT':
								DEFAULT = True
							if row == 'research' or row == 'text manipulation':
								found+=1
						if found == 2 or DEFAULT:
							rid.append( i )
					except Exception as e:
						pass
		else:
			if 'file' in _.switches.value( 'RemoveDefault' ).split( ',' ):
				for i,record in enumerate(data):
					if record['file'] == 'thisApp.py':
						rid.append( i )
			if 'description' in _.switches.value( 'RemoveDefault' ).split( ',' ):
				for i,record in enumerate(data):
					if record['description'] == 'Changes the world':
						rid.append( i )
			if 'categories' in _.switches.value( 'RemoveDefault' ).split( ',' ):
				try:
					found = 0
					for row in record['categories']:
						if row == 'research' or row == 'text manipulation':
							found+=1
					if found == 2:
						rid.append( i )
				except Exception as e:
					pass



	IDs = []
	if _.switches.isActive( 'Fields' ):
		if 'file' in _.switches.value( 'Fields' ).split( ',' ):
			for i,record in enumerate(data):
				if _.showLine( record['file'] ):
					IDs.append( i )
				elif _.showLine( record['live_file'] ):
					IDs.append( i )
		if 'description' in _.switches.value( 'Fields' ).split( ',' ):
			for i,record in enumerate(data):
				if _.showLine( record['description'] ):
					IDs.append( i )
		if 'categories' in _.switches.value( 'Fields' ).split( ',' ):
			for i,record in enumerate(data):
				try:
					len( record['categories'] )
					checkCat = True
				except Exception as e:
					checkCat = False
				if checkCat:
					found = 0
					for row in record['categories']:
						if _.showLine( row ):
							IDs.append( i )
			if _.switches.isActive( 'Minus' ):
				rid = []
				for i,record in enumerate(data):
					try:
						len( record['categories'] )
						checkCat = True
					except Exception as e:
						checkCat = False
					if checkCat:
						for row in record['categories']:
							for remove in _.switches.value( 'Minus' ).split( ',' ):
								if remove.lower() in row.lower():
									rid.append( i )

					

	else:
		for i,record in enumerate(data):
			# if type(record['description']) == str:
			#     if _.showLine( record['description'] ):
			#         IDs.append( i )
			# elif type(record['description']) == str:
			#     for description_xXx in record['description'] :
			#         if _.showLine( description_xXx ):
			#             IDs.append( i )

			# elif _.showLine( record['file'] ):
			#     IDs.append( i )
			# elif _.showLine( record['live_file'] ):
			#     IDs.append( i )
			# else:
			#     for row in record['categories']:
			#         if _.showLine( row ):
			#             IDs.append( i )





			if type(record['description']) == str:
				if _.showLine( record['description'] ):
					IDs.append( i )
			elif type(record['description']) == str:
				for description_xXx in record['description'] :
					if _.showLine( description_xXx ):
						IDs.append( i )

			if _.showLine( record['file'] ):
				IDs.append( i )
			if _.showLine( record['live_file'] ):
				IDs.append( i )

			for row in record['categories']:
				if _.showLine( row ):
					IDs.append( i )


	if _.switches.isActive( 'RequiredCategoriesCount' ):
		if len( _.switches.value( 'RequiredCategoriesCount' ) ):

			try:
				require = int( _.switches.value( 'RequiredCategoriesCount' ) )
			except Exception as e:
				require = 0

			if require:
				rid = []
				for i,record in enumerate(data):
					try:
						len( record['categories'] )
						checkCat = True
					except Exception as e:
						checkCat = False
					if checkCat:
						found = 0
						for row in record['categories']:
							if _.showLine( row ):
								found += 1

						if not found == require or not found > require:
							rid.append( i )



	rid = list(set(rid))
	IDs = list(set(IDs))
	pIDs = IDs
	if len( rid ):

		nIDs = []
		for ID in IDs:
			bad = False
			for r in rid:
				if ID == r:
					bad = True
			if not bad:
				nIDs.append( ID )
		IDs = nIDs
		diff = len(pIDs)-len(nIDs)

	for ID in IDs:
		_.pr( data[ID]['live_app'] )
	if _.switches.isActive( 'NoCount' ):
		sys.exit()
	_.pr()
	_.pr( '',len(IDs) )

	if len( rid ):
		_.pr( '', diff, '\tremoved' )
		_.pr()
		if _.switches.isActive( 'PrintRemoved' ):
			_.pr( 'Removed:' )
			_.pr()
			for ID in pIDs:
				bad = True
				for r in rid:
					if ID == r:
						bad = False
				if not bad:
					_.pr( '\t',data[ID]['live_file'] )
def load():
	global data
	data = _.getTableDB( 'appRegistration.json' )
data = []
########################################################################################
if __name__ == '__main__':
	action()







