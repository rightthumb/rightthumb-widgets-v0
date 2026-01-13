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

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt',  isRequired=True, description='Files' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'compareDice.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'DND class compare stats',
	'categories': [
						'dnd',
						'charecter',
						'class',
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
						'p compareDice -file cleric.json sorcerer.json wizard.json',
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


def process( database, record ):
	global dice

	if not database in dice:
		dice[database] = {}

	if not record['type'] in dice[database]:
		dice[database][record['type']] = {}

	if not record['level'] in dice[database][record['type']]:
		dice[database][record['type']][record['level']] = {}

	for die in record['dice'].split(' '):
		if len(die):
			d = die.split('d')
			try:
				d[1]
			except Exception as e:
				_.pr(d)
				sys.exit()
			if not d[1] in dice[database][record['type']][record['level']]:
				dice[database][record['type']][record['level']][d[1]] = []
			dice[database][record['type']][record['level']][d[1]].append( die )
			dice[database][record['type']][record['level']][d[1]].sort()



def processCompareLevel( database, record ):
	global dice


	if not record['type'] in dice:
		dice[record['type']] = {}

	if not record['level'] in dice[record['type']]:
		dice[record['type']][record['level']] = {}

	if not database in dice[record['type']][record['level']]:
		dice[record['type']][record['level']][database] = {}

	for die in record['dice'].split(' '):
		if len(die):
			d = die.split('d')
			try:
				d[1]
			except Exception as e:
				_.pr(d)
				sys.exit()
			if not d[1] in dice[record['type']][record['level']][database]:
				dice[record['type']][record['level']][database][d[1]] = {'t': 0, 'c': {}, 'd': [] }

			if not d[0] in dice[record['type']][record['level']][database][d[1]]['c']:
				dice[record['type']][record['level']][database][d[1]]['c'][d[0]] = 0
			dice[record['type']][record['level']][database][d[1]]['c'][d[0]] +=1

			dice[record['type']][record['level']][database][d[1]]['d'].append( die )
			dice[record['type']][record['level']][database][d[1]]['d'].sort()
			dice[record['type']][record['level']][database][d[1]]['t']+=1

def processCompareLevel( database, record ):
	global dice
	global diceSum


	if not record['type'] in dice:
		dice[record['type']] = {}

	if not record['level'] in dice[record['type']]:
		dice[record['type']][record['level']] = {}

	if not database in dice[record['type']][record['level']]:
		dice[record['type']][record['level']][database] = {}

	for die in record['dice'].split(' '):
		if len(die):
			d = die.split('d')
			try:
				d[1]
			except Exception as e:
				_.pr(d)
				sys.exit()
			if not d[1] in dice[record['type']][record['level']][database]:
				dice[record['type']][record['level']][database][d[1]] = {'t': 0, 'c': {}, 'd': [] }

			if not d[0] in dice[record['type']][record['level']][database][d[1]]['c']:
				dice[record['type']][record['level']][database][d[1]]['c'][d[0]] = 0
			dice[record['type']][record['level']][database][d[1]]['c'][d[0]] +=1

			dice[record['type']][record['level']][database][d[1]]['d'].append( die )
			dice[record['type']][record['level']][database][d[1]]['d'].sort()
			dice[record['type']][record['level']][database][d[1]]['t']+=1

def processCompareStatsD( database, record ):
	global dice
	global files
	global diceSum

	if not record['type'] in diceSum:
		diceSum[record['type']] = {}
	if not database in diceSum[record['type']]:
		diceSum[record['type']][database] = 0

	if not record['type'] in dice:
		dice[record['type']] = {}

	if not record['level'] in dice[record['type']]:
		dice[record['type']][record['level']] = {}

	if not database in dice[record['type']][record['level']]:
		dice[record['type']][record['level']][database] = 0
	for db in files:
		if not db in dice[record['type']][record['level']]:
			dice[record['type']][record['level']][db] = 0
	maxDice = 0
	for die in record['dice'].split(' '):
		if len(die):
			d = die.split('d')
			try:
				d[1]
			except Exception as e:
				_.pr(d)
				sys.exit()

			i=0
			try:
				dx = int(d[0])
			except Exception as e:
				dx = 1
			dy = 0
			try:
				dy = int(d[1])
			except Exception as e:
				pass
				# _.pr( d[1] )
			
			thisDice=0
			while not i == dx:
				thisDice += dy
				i+=1
			if thisDice > maxDice:
				maxDice = thisDice
					
	
	dice[record['type']][record['level']][database] += maxDice
	diceSum[record['type']][database] += maxDice



def action():
	global data
	global dice
	global files
	global diceSum

	load()

	for database in data:
		files.append(database['name'])
	for database in data:
		for record in database['records']:
			processCompareStatsD( database['name'], record )

	_.printVar( dice )
	_.printVar( diceSum )

def load():
	global data
	data = []
	for filename in _.switches.values('Files'):

		data.append({
						'name': filename.replace('.json',''),
						'records': _.getTableDB(filename),
			})


data = []
dice = {}
diceSum = {}
files = []

########################################################################################
if __name__ == '__main__':
	action()