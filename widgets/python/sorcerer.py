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
	_.switches.register( 'Selected', '-ss,-select,-selected', '10 14 18 19 28 34 36 39' )
	_.switches.register( 'Unselected', '-us,-unselect,-unselected', '5 7 9' )
	_.switches.register( 'ToggleSelected', '-t,-toggle' )
	_.switches.register( 'GroupSpaces', '-gs' )
	_.switches.register( 'CastSpell', '-cast,-spell' )
	_.switches.register( 'ResetSpellSlots', '-rs,-resetslots,-resetspell,-resetspells' )
	_.switches.register( 'RemoveCantrips', '-rc,-nc,-nocantrips' )
	_.switches.register( 'JustCantrips', '-jc,-justcantrips' )
	_.switches.register( 'History', '-h,-history' )
	_.switches.register( 'Ago', '-ago' )
	



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'sorcerer.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': [
						'Interact with DnD database of sorcerer spells',
						'Manage daily spell slot usage',
						'Document history of spells',
	],
	'categories': [
						'dnd',
						'sorcerer',
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
						'p sorcerer -prep',
						'p sorcerer -selected 14 18 19 20 28 36 39 41    10 15 22 34',
						'p sorcerer -t 10 15 22 34 ',
						'p sorcerer ',
						'',
						'p sorcerer -ss ',
						'',
						'',
						'p sorcerer -ss + heal',
						'p sorcerer -ss + help',
						'p sorcerer -ss + hurt',
						'p sorcerer -all ',
						'p sorcerer -all + hurt ',
						'p sorcerer -id 80',
						'',
						'',
						['p sorcerer -c t sel l n -g t sel','red'],
						'',
						['p sorcerer -c sel t i n l de r du  -g sel t','red'],
						'',
						'p sorcerer -c selected type i name level damage-effect range duration dice -g selected type',
						'',
						'',
						'p sorcerer -prep',
						'p sorcerer -selected 14 18 19 20 28 36 39 41',
						'p sorcerer -t 10 15 22 34',
						'p sorcerer -t 10 15 22 34',
						'p sorcerer',
						'',
						'',
						'',
						'p sorcerer -history',
						'p sorcerer -history -ago 1w',
						'p sorcerer -history -ago 1w one',
						'',
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
# __.appRegPipe
########################################################################################
# START

def prepData():
	global data
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
		# if 'd12' in data[i]['description']:
		#     found+=1
		if 'damage' in data[i]['description']:
			found+=1
		# if 'd8' in data[i]['description']:
		#     found+=1
		# if 'd4' in data[i]['description']:
		#     found+=1
		# if 'd6' in data[i]['description']:
		#     found+=1
		# if 'd10' in data[i]['description']:
		#     found+=1
		if 'Ranged' in data[i]['attack-save']:
			found+=1
		if 'Force' in data[i]['damage-effect']:
			found+=1
		if 'Poison' in data[i]['damage-effect']:
			found+=1
		if 'Bludgeoning' in data[i]['damage-effect']:
			found+=1
		if 'Necrotic' in data[i]['damage-effect']:
			found+=1
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
		if 'Necrotic' in data[i]['damage-effect']:
			data[i]['type'] = 'hurt'
		if 'Warding' in data[i]['damage-effect']:
			data[i]['type'] = 'help'
		if 'Deafened' in data[i]['damage-effect']:
			data[i]['type'] = 'hurt'
		if 'Restrained' in data[i]['damage-effect']:
			data[i]['type'] = 'help'
		if 'Detection' in data[i]['damage-effect']:
			data[i]['type'] = 'help'
		if 'Teleportation' in data[i]['damage-effect']:
			data[i]['type'] = 'help'
		if 'Communication' in data[i]['damage-effect']:
			data[i]['type'] = 'help'
		if 'Control' in data[i]['damage-effect']:
			data[i]['type'] = 'help'


	for i,record in enumerate(data):
		if record['type'] == '':
			data[i]['type'] = 'help'


	for i,record in enumerate(data):
		data[i]['i'] = i


	_.saveTableDB( data, 'sorcerer.json' )



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
			_.colorThis( [  '\t', clock  ], 'blue' )
			_.colorThis( [  '\t\t', record['name']  ], 'cyan' )
			_.colorThis( [  '\t\t\t', record['notes']  ], 'green' )



def action():
	global data
	global selection_record_text_no
	global selection_record_text_yes
	global selection_record_text_no_used
	global spell_slots
	global spell_history
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

	# maxSpells = 8

	# spell_slots_max = {
	#                 'Cantrip': '*',
	#                 '1st': 4,
	#                 '2nd': 3,
	# }

	# if type(spell_slots) == list or type(spell_slots) == dict and len(list(spell_slots.keys())) == 0:
	#     spell_slots = {}
	#     for k in spell_slots_max.keys():
	#         spell_slots[k] = 0


	# if _.switches.isActive('ResetSpellSlots'):
	#     spell_slots = []
	#     _.saveTableDB( spell_slots, 'sorcerer_spell_book.json' )
	# if _.switches.isActive('CastSpell') and len( _.switches.values('CastSpell') ):

	#     if type(spell_slots) == list or type(spell_slots) == dict and len(list(spell_slots.keys())) == 0:
	#         spell_slots = {}
	#         for k in spell_slots_max.keys():
	#             spell_slots[k] = 0

	#     cp = ''
	#     notes = []
	#     for i,x in enumerate(_.switches.values('CastSpell')) :
	#         if not i:
	#             cp = x
	#         else:
	#             notes.append( x )

	#     for i,record in enumerate(data):
	#         if str(record['i']) == cp:
	#             spell_history.append({  'id': record['i'], 'name': record['name'], 'epoch': time.time(), 'notes': ' '.join(notes) })
	#             spell_slots[ record['level'] ] += 1


	#     _.saveTableDB( spell_history, 'sorcerer_spell_history.json' )
	#     _.saveTableDB( spell_slots, 'sorcerer_spell_book.json' )
 

	# if _.switches.isActive('ToggleSelected'):
	#     # _.pr( type( _.switches.values('ToggleSelected') ) )
	#     # for x in _.switches.values('ToggleSelected'):
	#     #     _.pr( x, type(x) )
	#     # sys.exit()
	#     for i,record in enumerate(data):
	#         # _.pr( record['i'], type(record['i']) )
	#         try:
	#             if str(record['i']) in _.switches.values('ToggleSelected'):
	#                 pass
	#         except Exception as e:
	#             _.pr( record )
	#             sys.exit()
	#         if str(record['i']) in _.switches.values('ToggleSelected'):
	#             if  record['selected'] == selection_record_text_yes:
	#                 data[i]['selected'] = selection_record_text_no_used
	#             else:
	#                 data[i]['selected'] = selection_record_text_yes 



	#     _.saveTableDB( data, 'sorcerer.json' )

	# for i,record in enumerate(data):
	#     if '*' in record['selected']:
	#         selected_past_IDs.append( str(record['i']) )
	#     if record['selected'] == selection_record_text_yes:
	#         selected_IDs_All.append( str(record['i']) )
	#     if record['selected'] == selection_record_text_yes and not record['level'] == 'Cantrip':
	#         selected_IDs.append( str(record['i']) )

	# if len( selected_IDs ) > maxSpells:
	#     _.colorThis(  [ '\nTotal:', len( selected_IDs ) ], 'red'  )
	#     _.colorThis(  [ '\tMax Spells:', maxSpells ], 'red'  )
	#     _.colorThis(  [ '\tRemove:', len( selected_IDs ) - maxSpells ], 'red'  )
	# else:
	#     _.colorThis(  [ '\nTotal:', len( selected_IDs ), '\tWith Cantrips:', len(selected_IDs_All) ], 'green'  )
	#     if not len( selected_IDs ) == maxSpells:
	#         _.colorThis(  [ '\tNot enough spells, Add:', maxSpells - len( selected_IDs ) ], 'red'  )
	
	# _.colorThis(  [ '\n\t\t  My Spells:', ' '.join(selected_IDs) ], 'yellow'  )
	# _.colorThis(  [ '\n\t\tPast Spells:', ' '.join(selected_past_IDs) ], 'blue'  )
	# _.pr()
	# _.pr()



	# _.colorThis(  [ 'Spell Slots:' ], 'yellow'  )

	# _.pr()
	# _.colorThis(  [ '\tUsed:' ], 'bold'  )
	# for slot in spell_slots_max.keys():
	#     _.colorThis(  [ '\t\t', spell_slots[slot], slot ], 'cyan'  )
		
	# _.pr()
	# _.colorThis(  [ '\tLeft:' ], 'bold'  )
	# for slot in spell_slots_max.keys():
	#     # _.pr( slot )
	#     if type(spell_slots_max[slot]) == str:
	#         pass
	#     else:
	#         # _.pr( type(spell_slots_max[slot]), spell_slots[slot] )
	#         diff = spell_slots_max[slot] - spell_slots[slot]
	#         if diff == 0:
	#             _.colorThis(  [ '\t\t', diff, slot ], 'cyan'  )
	#         elif diff > 0:
	#             _.colorThis(  [ '\t\t', diff, slot ], 'green'  )
	#         else:
	#             _.colorThis(  [ '\t\t', diff, slot ], 'red'  )

		
	
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

		relevant = [
						'Cantrip',
						'1st',
						# '2nd',
						# '3rd',
						# '4th',
						# '5th',
						# '6th',
						# '7th',
						# '8th',
						# '9th'
		]



	if _.switches.isActive('PrepData'):
		prepData()


	elif _.switches.isActive('ID'):
		for i,record in enumerate(data):
			if str(i) == _.switches.value('ID'):
				description = record['description']
				del record['description']
				del record['html']
				_.pr()
				_.printVarSimple( record )
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


		_.saveTableDB( data, 'sorcerer.json' )


	elif _.switches.isActive('Unselected') and not _.switches.value('Unselected') == '':
		for i,record in enumerate(data):
			if str(i) in _.switches.values('Unselected'):
				if not record['level'] == 'Cantrip':
					data[i]['selected'] = selection_record_text_no_used

		_.saveTableDB( data, 'sorcerer.json' )


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

			group_space = _.switches.isActive('GroupSpaces')

			# p sorcerer -c selected type i name level damage-effect range duration dice -g selected type
			_.tables.register( 'data', newRecords, gs=group_space )
			_.tables.fieldProfileSet('data','selected','alignment','center')
			_.tables.fieldProfileSet('data','level','alignment','right')
			if _.switches.isActive('Column'):
				_.tables.print( 'data', _.switches.value('Column') )
			else:
				_.switches.fieldSet( 'GroupBy', 'active', True )
				# _.switches.fieldSet( 'GroupBy', 'value', 'selected,type,level' )
				_.switches.fieldSet( 'GroupBy', 'value', 'selected,type' )
				_.switches.fieldSet( 'Sort', 'active', True )
				# _.switches.fieldSet( 'Sort', 'value', 'd.selected,type' )
				# _.switches.fieldSet( 'Sort', 'value', 'selected,type,level' )
				_.switches.fieldSet( 'Sort', 'value', 'selected,type,level,damage-effect' )
				# _.tables.print( 'data', 'i,level,selected,name,type' )
				_.tables.print( 'data', 'selected,type,i,name,level,damage-effect,range,duration,dice' )
				# _.tables.print( 'data', 'selected,type,i,level,name,damage-effect,range,duration,attack-save,dice' )



def load():
	global data
	global spell_slots
	global spell_history

	data = _.getTableDB( 'sorcerer.json' )
	spell_slots = _.getTableDB( 'sorcerer_spell_book.json' )
	spell_history = _.getTableDB( 'sorcerer_spell_history.json' )
	if _.switches.isActive('PrepData'):
		prepData()


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

# p sorcerer -prep
# p sorcerer -selected 14 18 19 28 34 36 39 41
# p sorcerer -t 10 15 22
# p sorcerer -t 10 15 22
# p sorcerer


# *******************************
# https://www.dndbeyond.com/spells?filter-class=2&filter-search=
# b dnd
# n spell_hack.js
# *******************************



selection_record_text_yes = 'YES'
selection_record_text_no = 'NO'
selection_record_text_no_used = '* NO *'
data = []

########################################################################################
if __name__ == '__main__':
	action()







