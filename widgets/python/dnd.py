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


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	_.switches.register( 'All', '-all' )
	_.switches.register( 'ID', '-id', '12' )
	_.switches.register( 'PrepData', '-prep' )
	# _.switches.register( 'Selected', '-ss,-select,-selected', '5 4 0 6 19 14 10 18 15 28 34 36 39' )
	_.switches.register( 'Selected', '-ss,-select,-selected', '  10 15 22 34    14 18 19 20 28 36 39 41 51' )
	_.switches.register( 'Unselected', '-us,-unselect,-unselected', ' 5 7 9    10 15 22 34 ' )
	_.switches.register( 'ToggleSelected', '-t,-toggle' )
	_.switches.register( 'GroupSpaces', '-gs' )
	_.switches.register( 'CastSpell', '-cast,-spell' )
	_.switches.register( 'ResetSpellSlots', '-rs,-resetslots,-resetspell,-resetspells' )
	_.switches.register( 'RemoveCantrips', '-rc,-nc,-nocantrips' )
	_.switches.register( 'JustCantrips', '-jc,-justcantrips' )
	_.switches.register( 'History', '-h,-history' )
	_.switches.register( 'Ago', '-ago' )
	_.switches.register( 'CastLevel', '-level' )

	_.switches.register( 'GameGroup', '-ggroup', 'Church' )
	_.switches.register( 'GameCampaign', '-gcamp', 'The Heroes of Eisendell' )
	_.switches.register( 'GamePlayer', '-gplayer', 'Scott Reph' )
	_.switches.register( 'GameCharacter', '-gchar', 'Kolvar' )
	_.switches.register( 'CharacterIndex', '-gindex', 'Kolvar,cKolvar,Church,Scott,Eisendell' )
	_.switches.register( 'CharacterLevel', '-charLevel', '1' )
	_.switches.register( 'CharacterClass', '-class,-charClass', 'cleric' )
	_.switches.register( 'AddGameCharacter', '-add' )
	# _.switches.register( 'CharacterDefault', '-default', 'Kolvar' )
	_.switches.register( 'Character', '-char', 'Kolvar' )
	_.switches.register( 'WhatCharacter', '-?char,-char?' )
	# _.switches.register( 'BuildSpells', '-build' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'cleric.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': [
						'Interact with DnD database of cleric spells',
						'Manage daily spell slot usage',
						'Document history of spells',
	],
	'categories': [
						'dnd',
						'cleric',
						'spells',
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
						'p dnd -prep',
						'p dnd -selected 14 18 19 20 28 36 39 41 51    10 15 22 34',
						'p dnd -t 10 15 22 34 ',
						'p dnd ',
						'',
						'p dnd -ss ',
						'',
						'',
						'p dnd -ss + heal',
						'p dnd -ss + help',
						'p dnd -ss + hurt',
						'p dnd -all ',
						'p dnd -all + hurt ',
						'p dnd -id 80',
						'',
						'',
						['p dnd -c t sel l n -g t sel','red'],
						'',
						['p dnd -c sel t i n l de r du  -g sel t','red'],
						'',
						'p dnd -c selected type name level damage-effect range duration  -g selected type',
						'',
						'',

						'',
						'',
						'',
						'p dnd -history',
						'p dnd -history -ago 1w',
						'p dnd -history -ago 1w one',
						'',
						'',
						['p dnd -ss -c TYPE LEVEL NAME DICE -g type','red'],
						'',
						'',
						'p dnd -column selected type i level name damage-effect range duration attack-save dice school time components',
						'',
	],
	'columns': [
						{ 'name': 'i', 'abbreviation': 'id' },
						{ 'name': 'name', 'abbreviation': 'n' },
						{ 'name': 'level', 'abbreviation': 'l' },
						{ 'name': 'time', 'abbreviation': 'e' },
						{ 'name': 'range', 'abbreviation': 'r' },
						{ 'name': 'components', 'abbreviation': 'c' },
						{ 'name': 'duration', 'abbreviation': 'du' },
						{ 'name': 'damage-effect', 'abbreviation': 'de' },
						{ 'name': 'school', 'abbreviation': 's' },
						{ 'name': 'description', 'abbreviation': 'd' },
						{ 'name': 'attack-save', 'abbreviation': 'a' },
						{ 'name': 'type', 'abbreviation': 't' },
						{ 'name': 'selected', 'abbreviation': 'sel' },
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


# _.appInfo[focus()]['columns'].append( {'name': 'i', 'abbreviation': 'id'} )
# _.appInfo[focus()]['columns'].append( {'name': 'level', 'abbreviation': 'l'} )
# _.appInfo[focus()]['columns'].append( {'name': 'time', 'abbreviation': 'e'} )
# _.appInfo[focus()]['columns'].append( {'name': 'range', 'abbreviation': 'r'} )
# _.appInfo[focus()]['columns'].append( {'name': 'components', 'abbreviation': 'c'} )
# _.appInfo[focus()]['columns'].append( {'name': 'duration', 'abbreviation': 'du'} )
# _.appInfo[focus()]['columns'].append( {'name': 'damage-effect', 'abbreviation': 'de'} )
# _.appInfo[focus()]['columns'].append( {'name': 'school', 'abbreviation': 's'} )
# _.appInfo[focus()]['columns'].append( {'name': 'description', 'abbreviation': 'd'} )
# _.appInfo[focus()]['columns'].append( {'name': 'attack-save', 'abbreviation': 'a'} )
# _.appInfo[focus()]['columns'].append( {'name': 'type', 'abbreviation': 't'} )

def levelTrigger( data ):
	relevant = [
					'Cantrip',
					'1st',
					'2nd',
					'3rd',
					'4th',
					'5th',
					'6th',
					'7th',
					'8th',
					'9th'
	]
	for x in relevant:
		if data in x:
			return x
	return data

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
	_.switches.trigger( 'CastLevel', levelTrigger )
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
# __.appRegPipe
########################################################################################
# START

def prepData():
	global data
	global character
	global selection_record_text_yes
	global selection_record_text_no
	scan=['d4','d6','d8','d10','d12','d20','d100']
	# from bs4 import BeautifulSoup

	for i,record in enumerate(data):
		data[i]['dice'] = ''
		dice = []
		for word in record['description'].split(' '):
			for sn in scan:
				if sn.lower() in word.lower():
					di = _str.stripNonAlphaNumaric(word).replace(' ','')
					if not di in dice:
						dice.append( di )
		data[i]['dice'] = ' '.join( dice )


		data[i]['type'] = ''
		if record['level'] == 'Cantrip':
			data[i]['selected'] = selection_record_text_yes
		else:
			data[i]['selected'] = selection_record_text_no
		# soup = BeautifulSoup(data[i]['html'], 'lxml')
		# data[i]['description'] = soup.body.text.replace( '\n', '\n\n' )
		# data[i]['description'] = soup.body.get_text('\n')
		# del data[i]['html']



	for i,record in enumerate(data):
		found = 0
		if 'damage' in data[i]['description']:
			found+=1
		if 'd8' in data[i]['description']:
			found+=1
		if 'd4' in data[i]['description']:
			found+=1
		if 'd6' in data[i]['description']:
			found+=1
		if 'd10' in data[i]['description']:
			found+=1
		if 'Ranged' in data[i]['attack-save']:
			found+=1
		if 'Force' in data[i]['damage-effect']:
			found+=1
		if 'Melee' in data[i]['attack-save']:
			found+=1
		if 'Acid' in data[i]['damage-effect']:
			found+=1

		if found > 1:
			# _.pr( i, record['level'], record['name'] )
			if not data[i]['attack-save'] == '':
				data[i]['type'] = 'hurt'



	for i,record in enumerate(data):
		if 'heal' in data[i]['description'].lower() or 'heal' in data[i]['name'].lower() or 'heal' in data[i]['damage-effect'].lower()  or 'protect' in data[i]['description'].lower() :
			# _.pr( i, record['level'], record['name'] )
			data[i]['type'] = 'heal'



	for i,record in enumerate(data):
		data[i]['damage-effect'] = data[i]['damage-effect'].replace( ' (...)', '' )



	for i,record in enumerate(data):
		if record['type'] == '':
			data[i]['type'] = 'help'


	for i,record in enumerate(data):
		data[i]['i'] = i


	# _.saveTableDB( data, 'cleric.json' )
	_.saveTableProject( __.thisProjectPath, data, 'spells.json' )



def history():
	global spell_history

	# _.pr(time.time());sys.exit();

	if _.switches.isActive('Ago') and len(_.switches.values('Ago')) > 1 and _.switches.values('Ago')[1] == 'one':
		one = True
	else:
		one = False

	spent = False
	lastDay = ''
	today = _.friendlyDate( time.time() ).split(' ')[0]
	for i,record in enumerate(spell_history):
		day = _.friendlyDate( record['epoch'] ).split(' ')[0]
		clock = _.justTime( record['epoch'] )
		diff = _.dateDiff( day, today )
		shouldRun = True

		if _.switches.isActive('Ago'):
			
				
			if record['epoch'] < _.switches.values('Ago')[0]:
				shouldRun = False


		if shouldRun:
			if not day == lastDay:
				if spent: return None;
				if one: spent = True;
					
				_.pr()
				_.pr()
				plur = 's'
				if diff == 1:
					plur = ''
				lastDay = day
				_.colorThis( [  day, '\t', diff, 'day'+plur  ], 'yellow' )
			
			_.pr()
			theLevel = record['level']
			if theLevel is None:
				theLevel = '___________________________________________________'
			_.colorThis( [  '\t', clock  ], 'blue' )
			_.colorThis( [  '\t\t', theLevel  ], 'red' )
			_.colorThis( [  '\t\t\t', record['name']  ], 'cyan' )
			_.colorThis( [  '\t\t\t\t', record['notes']  ], 'green' )



def charSpellSlots():
	global character
	theLevels = _.getTableProject( 'DnD.sheet', 'level-spells.index' )
	return theLevels[ str( character['level'] ) ]

def action():





	global data
	global selection_record_text_no
	global selection_record_text_yes
	global selection_record_text_no_used
	global spell_slots
	global spell_history
	global character

	load()

	if _.switches.isActive('History'):
		history()
		return None


	if not _.switches.isActive('ID'):
		if platform.system() == 'Windows':
			os.system('cls')
		else:
			os.system('clear')


	selected_past_IDs = []
	selected_IDs = []
	selected_IDs_All = []
	records = []

	


	spell_slots_max = charSpellSlots()

	maxSpells = spell_slots_max['spells']

	"""
	spell_slots_max = {
					'Cantrip': '*',
					'1st': 4,
					'2nd': 3,
					'3rd': 2,
	}
	"""

	if type(spell_slots) == list or type(spell_slots) == dict and len(list(spell_slots.keys())) == 0:
		spell_slots = {}
		for k in spell_slots_max.keys():
			spell_slots[k] = 0


	if _.switches.isActive('ResetSpellSlots'):
		spell_history.append({  'id': None, 'name': 'REST', 'epoch': time.time(), 'notes': '', 'level': None })
		spell_slots = {}
		_.saveTableDB( spell_slots, 'spell_slots.json' )
		_.saveTableProject( __.thisProjectPath, spell_slots, 'spell_slots.json' )
		_.saveTableProject( __.thisProjectPath, spell_history, 'history.json' )
	if _.switches.isActive('CastSpell') and len( _.switches.values('CastSpell') ):

		if type(spell_slots) == list or type(spell_slots) == dict and len(list(spell_slots.keys())) == 0:
			spell_slots = {}
			for k in spell_slots_max.keys():
				spell_slots[k] = 0

		cp = ''
		notes = []
		for i,x in enumerate(_.switches.values('CastSpell')) :
			if not i:
				cp = x
			else:
				notes.append( x )

		for i,record in enumerate(data):
			if str(record['i']) == cp:
				theLevel = record['level']
				if _.switches.isActive('CastLevel'):
					theLevel = _.switches.value('CastLevel')
				spell_history.append({  'id': record['i'], 'name': record['name'], 'epoch': time.time(), 'notes': ' '.join(notes), 'level': theLevel })
				if not _.switches.isActive('CastLevel'):
					spell_slots[ record['level'] ] += 1
				else:
					spell_slots[ _.switches.value('CastLevel') ] += 1


		_.saveTableProject( __.thisProjectPath, spell_history, 'history.json' )
		_.saveTableProject( __.thisProjectPath, spell_slots, 'spell_slots.json' )
 

	if _.switches.isActive('ToggleSelected'):
		# _.pr( type( _.switches.values('ToggleSelected') ) )
		# for x in _.switches.values('ToggleSelected'):
		#   _.pr( x, type(x) )
		# sys.exit()
		for i,record in enumerate(data):
			# _.pr( record['i'], type(record['i']) )
			try:
				if str(record['i']) in _.switches.values('ToggleSelected'):
					pass
			except Exception as e:
				_.pr( record )
				sys.exit()
			if str(record['i']) in _.switches.values('ToggleSelected'):
				if  record['selected'] == selection_record_text_yes:
					data[i]['selected'] = selection_record_text_no_used
				else:
					data[i]['selected'] = selection_record_text_yes 



		# _.saveTableDB( data, 'cleric.json' )
		_.saveTableProject( __.thisProjectPath, data, 'spells.json' )

	for i,record in enumerate(data):
		if '*' in record['selected']:
			selected_past_IDs.append( str(record['i']) )
		if record['selected'] == selection_record_text_yes:
			selected_IDs_All.append( str(record['i']) )
		if record['selected'] == selection_record_text_yes and not record['level'] == 'Cantrip':
			selected_IDs.append( str(record['i']) )

	if len( selected_IDs ) > maxSpells:
		_.colorThis(  [ '\nTotal:', len( selected_IDs ) ], 'red'  )
		_.colorThis(  [ '\tMax Spells:', maxSpells ], 'red'  )
		_.colorThis(  [ '\tRemove:', len( selected_IDs ) - maxSpells ], 'red'  )
	else:
		_.colorThis(  [ '\nTotal:', len( selected_IDs ), '\tWith Cantrips:', len(selected_IDs_All) ], 'green'  )
		if not len( selected_IDs ) == maxSpells:
			_.colorThis(  [ '\tNot enough spells, Add:', maxSpells - len( selected_IDs ) ], 'red'  )
	
	_.colorThis(  [ '\n\t\t  My Spells:', ' '.join(selected_IDs) ], 'yellow'  )
	_.colorThis(  [ '\n\t\tPast Spells:', ' '.join(selected_past_IDs) ], 'blue'  )
	_.pr()
	_.pr()



	_.colorThis(  [ 'Spell Slots:' ], 'yellow'  )

	_.pr()
	_.colorThis(  [ '\tUsed:' ], 'bold'  )
	
	if spell_slots == {}:
		for slot in spell_slots_max.keys():
			if not slot in __.spell_slots_omit:
				spell_slots[slot] = 0


	for slot in spell_slots_max.keys():
		if not slot in __.spell_slots_omit:
			_.colorThis(  [ '\t\t', spell_slots[slot], slot ], 'cyan'  )
		
	_.pr()
	_.colorThis(  [ '\tLeft:' ], 'bold'  )
	for slot in spell_slots_max.keys():
		# _.pr( slot )
		if not slot in __.spell_slots_omit:
			if type(spell_slots_max[slot]) == str:
				pass
			else:
				# _.pr( type(spell_slots_max[slot]), spell_slots[slot] )
				diff = spell_slots_max[slot] - spell_slots[slot]

				if diff == 0:
					_.colorThis(  [ '\t\t', diff, slot ], 'red'  )
				elif diff > 0:
					_.colorThis(  [ '\t\t', diff, slot ], 'green'  )
				else:
					_.colorThis(  [ '\t\t', diff, slot ], 'red'  )

		
	
	_.pr()
	_.pr()

	if _.switches.isActive('All'):

		relevant = [
						'Cantrip',
						'1st',
						'2nd',
						'3rd',
						'4th',
						'5th',
						'6th',
						'7th',
						'8th',
						'9th'
		]
	else:

		relevant = list( spell_slots_max.keys() )

		# relevant = [
		#                 'Cantrip',
		#                 '1st',
		#                 '2nd',
		#                 '3rd',
		#                 # '4th',
		#                 # '5th',
		#                 # '6th',
		#                 # '7th',
		#                 # '8th',
		#                 # '9th'
		# ]



	if _.switches.isActive('PrepData'):
		prepData()


	elif _.switches.isActive('ID'):
		for i,record in enumerate(data):
			if str(i) == _.switches.value('ID'):
				description = record['description']
				del record['description']
				del record['html']
				_.pr()
				_.printVarSimple2( record )
				_.pr()

				_.wrapText(  description,  scan=['d4','d6','d8','d10','d12','d20','d100']  )
				



	elif _.switches.isActive('Plus') and _.switches.value('Plus') == 'heal' or _.switches.value('Plus') == 'help' or _.switches.value('Plus') == 'hurt':
		
		for i,record in enumerate(data):
			if _.showLine( record['type'] ):
				records.append(record)


	elif _.switches.isActive('Selected') and not _.switches.value('Selected') == '':
		for i,record in enumerate(data):
			if record['level'] == 'Cantrip':
				data[i]['selected'] = selection_record_text_yes
			else:
				if str(i) in _.switches.values('Selected'):
					data[i]['selected'] = selection_record_text_yes


		# _.saveTableDB( data, 'cleric.json' )
		_.saveTableProject( __.thisProjectPath, data, 'spells.json' )


	elif _.switches.isActive('Unselected') and not _.switches.value('Unselected') == '':
		for i,record in enumerate(data):
			if str(i) in _.switches.values('Unselected'):
				if not record['level'] == 'Cantrip':
					data[i]['selected'] = selection_record_text_no_used

		# _.saveTableDB( data, 'cleric.json' )
		_.saveTableProject( __.thisProjectPath, data, 'spells.json' )


	else:
		# _.switches.dumpSwitches(includeBlank=False)
		for i,record in enumerate(data):
			if _.showLine( record['name'] +' '+ record['description'] +' '+ record['damage-effect'] ):
				records.append(record)
				pass
			# if _.showLine( record['name'] ) or _.showLine( record['description'] ):
				
					
	

	if len(records):

		newRecords = []

		selected = False
		unselected = False

		if _.switches.isActive('Selected') and _.switches.value('Selected') == '':
			selected = True
		if _.switches.isActive('Unselected') and _.switches.value('Unselected') == '':
			unselected = True

		for i,record in enumerate(records):
			if record['level'] in relevant:
				shouldAdd = True
				if selected and record['selected'] == '':
					shouldAdd = False
				if unselected and not record['selected'] == '':
					shouldAdd = False
				if shouldAdd:
					newRecords.append(record)



		if len(newRecords):
			if _.switches.isActive('RemoveCantrips'):
				newRecords_X = []
				for i,record in enumerate(newRecords):
					if not record['level'] == 'Cantrip':
						newRecords_X.append( record )
				newRecords = newRecords_X
			if _.switches.isActive('JustCantrips'):
				newRecords_X = []
				for i,record in enumerate(newRecords):
					if record['level'] == 'Cantrip':
						newRecords_X.append( record )
				newRecords = newRecords_X

			if _.switches.isActive('Selected') and _.switches.value('Selected') == '':

				newRecords_X = []
				# for i,record in enumerate(newRecords):
				for i,record in enumerate(records):
					if 'cantrip' in data[i]['level'].lower():
						# _.pr(data[i]['level'], data[i]['name'])
						newRecords_X.append( record )

					elif data[i]['selected'] == selection_record_text_yes:
						newRecords_X.append( record )
				newRecords = newRecords_X

			group_space = _.switches.isActive('GroupSpaces')

			_.tables.register( 'data', newRecords, gs=group_space )
			_.tables.fieldProfileSet('data','selected','alignment','center')
			_.tables.fieldProfileSet('data','level','alignment','right')
			if _.switches.isActive('Column'):
				_.tables.print( 'data', _.switches.value('Column') )
			else:
				_.switches.fieldSet( 'GroupBy', 'active', True )
				# _.switches.fieldSet( 'GroupBy', 'value', 'selected,type,level' )
				_.switches.fieldSet( 'GroupBy', 'value', 'selected,type,level' )
				_.switches.fieldSet( 'Sort', 'active', True )
				# _.switches.fieldSet( 'Sort', 'value', 'd.selected,type' )
				# _.switches.fieldSet( 'Sort', 'value', 'selected,type,level' )
				_.switches.fieldSet( 'Sort', 'value', 'selected,type,level,damage-effect' )
				# _.tables.print( 'data', 'i,level,selected,name,type' )
				_.tables.print( 'data', 'selected,type,i,level,name,damage-effect,range,duration,attack-save,dice' )

def loadCharacter(char):
	__.thisProjectPath = __.thisProjectPathBase
	__.thisProjectPath = __.thisProjectPath.replace( 'theGroup', char['group'] )
	__.thisProjectPath = __.thisProjectPath.replace( 'theCampaign', char['campaign'] )
	__.thisProjectPath = __.thisProjectPath.replace( 'theClass', char['class'] )
	__.thisProjectPath = __.thisProjectPath.replace( 'thePlayer', char['player'] )
	__.thisProjectPath = __.thisProjectPath.replace( 'theCharacter', char['character'] )
	if _.switches.isActive('WhatCharacter'):
		_.pr( __.thisProjectPath )
		sys.exit()


def load():
	global data
	global spell_slots
	global spell_history
	global character
	character = None
	__.thisProjectPathBase = 'DnD.configurations.groups.theGroup.campaigns.theCampaign.players.theClass.thePlayer.characters.theCharacter'



	# GameGroup GameCampaign GamePlayer GameCharacter  CharacterIndex AddGameCharacter  CharacterLevel CharacterDefault
	# default_character = {
	#                         'group': 'Church',
	#                         'campaign': 'The Heroes of Eisendell',
	#                         'player': 'Scott Reph',
	#                         'character': 'Kolvar',
	#                         'indices': 'Kolvar,cKolvar,Church,Scott,Eisendell',
	# }
	# default_character = 'Kolvar'
	character_data = _.getTableProject( 'DnD.configurations.characters', 'characters.json' )
	character_index = _.getTableProject( 'DnD.configurations.characters', 'characters.index' )
	


	if _.switches.isActive('AddGameCharacter'):
		try:
			character = {
									'character': '_'.join( _.switches.values('GameCharacter') ),
									'level': int( _.switches.values('CharacterLevel')[0] ),
									'class': '_'.join( _.switches.values('CharacterClass') ),
									'player': '_'.join( _.switches.values('GamePlayer') ),
									'indices': ','.join( _.switches.values('CharacterIndex') ).split(','),
									'group': '_'.join( _.switches.values('GameGroup') ),
									'campaign': '_'.join( _.switches.values('GameCampaign') ),
			}

			loadCharacter(character)

			i = len(character_data)

			for x in character['indices']:
				character_index[x] = i
				character_index[x.lower()] = i
				_.pr()

			character_data.append(character)
			spell_history = []
			spell_slots = {}
			for k in charSpellSlots().keys():
				if not k in __.spell_slots_omit:
					spell_slots[k]=0




			# data = _.getTableDB( character['class']+'.json' )
			# data = _.getTableProject( __.thisProjectPath, 'spells.json' )


			_.saveTableProject( __.thisProjectPath, spell_slots, 'spell_slots.json' )

			spell_history.append({  'id': None, 'name': 'NEW Character', 'epoch': time.time(), 'notes': '', 'level': None })
			_.saveTableProject( __.thisProjectPath, spell_history, 'history.json' )
			# spell_history = _.getTableProject( __.thisProjectPath, 'history.json' )
			_.saveTableProject( 'DnD.configurations.characters', [character['indices'][0]], 'characters.default' )
			_.saveTableProject( 'DnD.configurations.characters', character_data, 'characters.json' )
			_.saveTableProject( 'DnD.configurations.characters', character_index, 'characters.index' )
			pass
		except Exception as e:
			_.colorThis( 'Error: character create FAILED', 'red' )
			sys.exit()
			pass


		pass
	if _.switches.isActive('Character'):
		try:
			default = '_'.join( _.switches.values('Character') )
			character = character_data[  character_index[ default ]  ]

		except Exception as e:
			_.colorThis( 'Error: character does not exist', 'red' )
			sys.exit()
		_.saveTableProject( 'DnD.configurations.characters', [default], 'characters.default' )

	if character is None:
		try:
			default = _.getTableProject( 'DnD.configurations.characters', 'characters.default' )
			# _.pr(default)
			default = default[0]
			character = character_data[  character_index[ default ]  ]
		except Exception as e:
			_.colorThis( 'Error: character does not exist', 'red' )
			sys.exit()

	if character is None:
		_.colorThis( 'Error: character does not exist', 'red' )
		sys.exit()

	loadCharacter(character)
	# _.pr( 'character:', character )

	# _.printVarSimple(character)
	# sys.exit()



	if _.switches.isActive('PrepData'):
		# str strength
		# dex dexterity
		# con constitution
		# int intelligence
		# wis wisdom
		# cha charisma
		savingThrows = {
					'strength': 'str',
					'dexterity': 'dex',
					'constitution': 'con',
					'intelligence': 'int',
					'wisdom': 'wis',
					'charisma': 'cha',
		}
		Spells = _.getTableProject( 'DnD.dndspellslist', 'spells.json' )
		mySpells = []
		for i,spell in enumerate(Spells):
			if character['class'] in spell['availableClasses']:
				attach_save_list = []
				attach_save = ''
				for atts in spell['savingThrows']:
					attach_save_list.append( savingThrows[atts] )
				if len(attach_save_list):
					attach_save = ', '.join(attach_save_list)
				spell['attack-save'] = attach_save

				if not spell['level']:
					spell['level'] = 'Cantrip'
				else:
					spell['level'] = str(spell['level'])

				spell['components'] = ', '.join( spell['components'] )
				spell['damage-effect'] = ', '.join( spell['damageTypes'] )
				mySpells.append(spell)
			

		_.saveTableProject( __.thisProjectPath, mySpells, 'spells.json' )



	data = _.getTableProject( __.thisProjectPath, 'spells.json' )
	spell_slots = _.getTableProject( __.thisProjectPath, 'spell_slots.json' )
	spell_history = _.getTableProject( __.thisProjectPath, 'history.json' )


	# Spells = _.getTableProject( 'DnD.5e', 'Spells.json' )


	# Ability-Scores.json
	# Classes.json
	# Conditions.json
	# Damage-Types.json
	# Equipment-Categories.json
	# Equipment.json
	# Features.json
	# Languages.json
	# Levels.json
	# Magic-Schools.json
	# Monsters.json
	# Proficiencies.json
	# Races.json
	# Skills.json
	# Spellcasting.json
	# Spells.json
	# StartingEquipment.json
	# Subclasses.json
	# Subraces.json
	# Traits.json
	# Weapon-Properties.json



# i
# name
# level
# time
# range
# components
# duration
# school
# attack-save
# damage-effect
# description
# type

# p cleric -prep
# p cleric -selected 14 18 19 28 34 36 39 41
# p cleric -t 10 15 22
# p cleric -t 10 15 22
# p cleric


# *******************************
# https://www.dndbeyond.com/spells?filter-class=2&filter-search=
# b dnd
# n spell_hack.js
# *******************************

# 706 # for i,record in enumerate(newRecords):

__.spell_slots_omit = ['spells']
selection_record_text_yes = 'YES'
selection_record_text_no = 'NO'
selection_record_text_no_used = '* NO *'
data = []

########################################################################################
if __name__ == '__main__':
	action()