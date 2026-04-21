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


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': '5e.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'dungeons and dragons databases',
	'categories': [
						'dnd',
						'dungeons and dragons',
						'5e',
						'd&d',
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
						'p 5e',
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
	__.myFileLocations_SKIP_VALIDATION = False
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START



def action():
	load()

	# global Ability_Scores
	# global Classes
	# global Conditions
	# global Damage_Types
	# global Equipment_Categories
	# global Equipment
	# global Features
	# global Languages
	# global Levels
	# global Magic_Schools
	# global Monsters
	# global Proficiencies
	# global Races
	# global Skills
	# global Spellcasting
	global Spells
	# global StartingEquipment
	# global Subclasses
	# global Subraces
	# global Traits
	# global Weapon_Properties

	test = _.traverse( Spells, config={'inDicI':'cleric'})
	# spent = []
	found = []
	for x in test['inDicI']:
		found.append( int(x[0]) )
		# _.pr(x)
		# if not str(x) in spent:
			# spent.append(str(x))
	# _.pr(test)

	# what = 'for x in Spells: for y in x["classes"]: _.pr(y["name"]);'
	# what = '[[y["name"] for y in x["classes"]] for x in Spells]'
	# [[ if 'cleric' in y["name"]:_.pr(y["name"]) for y in x["classes"]] for x in Spells]
	# exec (what)

	# for x in test['inDic']:
	#     base = 'Spells'
	#     for y in x:



	# sys.exit()

	for i,r in enumerate(Spells):
		if i in found:
			test = _.traverse( r, config={'find_field':'level'})
			level = None
			try:
				level = _.traverse_dic_research['return']
			except Exception as e:
				pass
			_.pr('levellevellevellevellevellevellevel', level)
			_.pr()
			_.pr()
			_.pr( r['name'] )
			_.pr( '\t','level:', r['level'] )
			_.pr( '\t','school:', r['school']['name'] )

			_.pr( '\t', 'classes:' )
			for s in r['classes']:
				_.pr( '\t\t', s['name'] )

			_.pr( '\t', 'subclasses:' )
			for s in r['subclasses']:
				_.pr( '\t\t', s['name'] )

			if 'damage' in r:

				if 'damage_at_character_level' in r['damage']:
					_.pr( '\t', 'damage_at_character_level:', r['damage']['damage_at_character_level'] )

		# _.pr(r)
		# _.pr( list(r.keys()) )



def load():

	# global Ability_Scores
	# global Classes
	# global Conditions
	# global Damage_Types
	# global Equipment_Categories
	# global Equipment
	# global Features
	# global Languages
	# global Levels
	# global Magic_Schools
	# global Monsters
	# global Proficiencies
	# global Races
	# global Skills
	# global Spellcasting
	global Spells
	# global StartingEquipment
	# global Subclasses
	# global Subraces
	# global Traits
	# global Weapon_Properties

	# Ability_Scores = _.getTableDB( '5e-SRD-Ability-Scores.json' )
	# Classes = _.getTableDB( '5e-SRD-Classes.json' )
	# Conditions = _.getTableDB( '5e-SRD-Conditions.json' )
	# Damage_Types = _.getTableDB( '5e-SRD-Damage-Types.json' )
	# Equipment_Categories = _.getTableDB( '5e-SRD-Equipment-Categories.json' )
	# Equipment = _.getTableDB( '5e-SRD-Equipment.json' )
	# Features = _.getTableDB( '5e-SRD-Features.json' )
	# Languages = _.getTableDB( '5e-SRD-Languages.json' )
	# Levels = _.getTableDB( '5e-SRD-Levels.json' )
	# Magic_Schools = _.getTableDB( '5e-SRD-Magic-Schools.json' )
	# Monsters = _.getTableDB( '5e-SRD-Monsters.json' )
	# Proficiencies = _.getTableDB( '5e-SRD-Proficiencies.json' )
	# Races = _.getTableDB( '5e-SRD-Races.json' )
	# Skills = _.getTableDB( '5e-SRD-Skills.json' )
	# Spellcasting = _.getTableDB( '5e-SRD-Spellcasting.json' )
	Spells = _.getTableDB( '5e-SRD-Spells.json' )
	# StartingEquipment = _.getTableDB( '5e-SRD-StartingEquipment.json' )
	# Subclasses = _.getTableDB( '5e-SRD-Subclasses.json' )
	# Subraces = _.getTableDB( '5e-SRD-Subraces.json' )
	# Traits = _.getTableDB( '5e-SRD-Traits.json' )
	# Weapon_Properties = _.getTableDB( '5e-SRD-Weapon-Properties.json' )

"""
5e-SRD-Ability-Scores.json
5e-SRD-Classes.json
5e-SRD-Conditions.json
5e-SRD-Damage-Types.json
5e-SRD-Equipment-Categories.json
5e-SRD-Equipment.json
5e-SRD-Features.json
5e-SRD-Languages.json
5e-SRD-Levels.json
5e-SRD-Magic-Schools.json
5e-SRD-Monsters.json
5e-SRD-Proficiencies.json
5e-SRD-Races.json
5e-SRD-Skills.json
5e-SRD-Spellcasting.json
5e-SRD-Spells.json
5e-SRD-StartingEquipment.json
5e-SRD-Subclasses.json
5e-SRD-Subraces.json
5e-SRD-Traits.json
5e-SRD-Weapon-Properties.json
"""



########################################################################################
if __name__ == '__main__':
	action()