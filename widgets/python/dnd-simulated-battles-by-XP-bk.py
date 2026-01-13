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

##################################################
import os, sys, time
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
	_.switches.register( 'XP-Start', '-start' )
	_.switches.register( 'XP-End', '-end' )

	_.switches.register( 'Hit-Dice', '-dice', 'd10' )
	_.switches.register( 'Hit-Dice-Mod', '-dice.mod', '9' )
	_.switches.register( 'Hit-Dice-Plus', '-dice.plus', '19' )
	
	_.switches.register( 'Damage-120', '-120', '1d8 LOW TO HIGH' )
	_.switches.register( 'Damage-60', '-60', '1d8 LOW TO HIGH' )
	_.switches.register( 'Damage-Melee', '-melee', '1d8 LOW TO HIGH' )



	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'dnd-simulated-battles-by-XP.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Simulated battles',
	'categories': [
						'dnd',
						'simulations',
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
						_.hp('p dnd-simulated-battles-by-XP -start 5000 -end 120000 -120 1d12 -60 2d10 -melee 3d8 -dice d6  -dice.mod 9 -dice.plus 18'),
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )    
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START

XP_LEVEL =     [
		{
			"XP": "0",
			"Level": "1",
			"Prof": "+2"
		},
		{
			"XP": "300",
			"Level": "2",
			"Prof": "+2"
		},
		{
			"XP": "900",
			"Level": "3",
			"Prof": "+2"
		},
		{
			"XP": "2,700",
			"Level": "4",
			"Prof": "+2"
		},
		{
			"XP": "6,500",
			"Level": "5",
			"Prof": "+3"
		},
		{
			"XP": "14,000",
			"Level": "6",
			"Prof": "+3"
		},
		{
			"XP": "23,000",
			"Level": "7",
			"Prof": "+3"
		},
		{
			"XP": "34,000",
			"Level": "8",
			"Prof": "+3"
		},
		{
			"XP": "48,000",
			"Level": "9",
			"Prof": "+4"
		},
		{
			"XP": "64,000",
			"Level": "10",
			"Prof": "+4"
		},
		{
			"XP": "85,000",
			"Level": "11",
			"Prof": "+4"
		},
		{
			"XP": "100,000",
			"Level": "12",
			"Prof": "+4"
		},
		{
			"XP": "120,000",
			"Level": "13",
			"Prof": "+5"
		},
		{
			"XP": "140,000",
			"Level": "14",
			"Prof": "+5"
		},
		{
			"XP": "165,000",
			"Level": "15",
			"Prof": "+5"
		},
		{
			"XP": "195,000",
			"Level": "16",
			"Prof": "+5"
		},
		{
			"XP": "225,000",
			"Level": "17",
			"Prof": "+6"
		},
		{
			"XP": "265,000",
			"Level": "18",
			"Prof": "+6"
		},
		{
			"XP": "305,000",
			"Level": "19",
			"Prof": "+6"
		},
		{
			"XP": "355,000",
			"Level": "20",
			"Prof": "+6"
		}
	]

for i,rec in enumerate(XP_LEVEL):
	XP_LEVEL[i]['Level'] = int(rec['Level'])
	XP_LEVEL[i]['XP'] = int(rec['XP'].replace(',',''))
	XP_LEVEL[i]['Prof'] = int(rec['Prof'].replace('+',''))
# XP_LEVEL.reverse()




def levelXP():
	global XP
	global XP_LEVEL
	# _.pv(XP_LEVEL)
	for rec in XP_LEVEL:
		if XP < rec['XP']:
			return rec['Level']-1


def healthXP():

	HP_DICE = int(_.switches.value('Hit-Dice').lower().split('d')[1])
	HP_DICE_X = int(_.switches.value('Hit-Dice').lower().split('d')[0])
	times = levelXP()
	# sub = HP_DICE*(HP_DICE_X+times)
	sub = HP_DICE*(levelXP())
	# _.pr('healthXP',HP_DICE,levelXP())
	if _.switches.isActive('Hit-Dice-Mod'):
		sub += int(_.switches.value('Hit-Dice-Mod'))


	if _.switches.isActive('Hit-Dice-Plus'):
		sub += int(_.switches.value('Hit-Dice-Plus'))

	return sub




def roll(dice,cnt):
	total = 0
	i=0
	while not i == cnt:
		i+=1
		total += random.randint(1,dice)

	return total

def genMobs():
	mobs = [
			{ 'npc': 1, 'type': 'orc', 'ac': 13, 'health': 15, 'Damage-120': [] , 'Damage-60': ['1d4'], 'Damage-Melee': ['1d4','1d6'] },
			{ 'npc': 1, 'type': 'kobold', 'ac': 12, 'health': 5, 'Damage-120': [] , 'Damage-60': ['1d4'], 'Damage-Melee': ['1d4','1d6'] },
			{ 'npc': 1, 'type': 'oger', 'ac': 11, 'health': 59, 'Damage-120': [] , 'Damage-60': [], 'Damage-Melee': ['1d4','1d6','1d10'] },
	]

	cnt = random.randint(1,5)
	myMob = mobs[ random.randint(0,len(mobs)-1) ]

	if myMob['health'] > 16:
		cnt = 1

	allMobs = []
	i=0
	while not i == cnt:
		i+=1
		allMobs.append( myMob )

	if __.printing:
		_.pr( '__________________________________________________', cnt, 'MOBS' )


	return allMobs

rollDamage_LAST = -2 

def rollDamage( options, npc, yer ):
	global rollDamage_LAST

	if yer == rollDamage_LAST:
		return 0

	if not options:
		rollDamage_LAST = yer
		return 0

	if npc:
		di = options[ random.randint(0,len(options)-1) ].lower()
	else:
		di = options[ len(options)-1 ].lower()

	result = roll(  dice=  int( di.split('d')[1] )  ,   cnt=int( di.split('d')[0] )   )
	if not npc:
		dic={
				'result':result,
				'di':di,
				'yer':yer,
				'last':rollDamage_LAST,
				'npc':npc,
		}
		# _.pr( 'rollDamage', dic  )
	rollDamage_LAST = yer
	return result


# test = [{'a':0},{'a':1},{'a':2}]

BATTLE_ID = 0

def battle():
	global HEALTH
	global BATTLE_ID
	global XP
	global XP_PER

	
	

	BATTLE_ID+=1
	if __.printing:
		_.pr('\n\n\nBATTLE_ID:',BATTLE_ID)
	


	distance = 120
	mobs = genMobs()
	player =  { 'npc': 0, 'type': 'player', 'ac': 12, 'health': HEALTH, 'Damage-120': _.switches.values('Damage-120') , 'Damage-60': _.switches.values('Damage-60'), 'Damage-Melee': _.switches.values('Damage-Melee') }


	ROUND = 0

	while len(mobs) and HEALTH:
		ROUND+=1        

		# PLAYER MOVE X2 Because of Ronan AND Shade
		mi = random.randint(0,len(mobs)-1)
		ac = roll(dice=20,cnt=1)
		if ac >= mobs[mi]['ac']:
			if distance > 60:
				damage = rollDamage( options=player['Damage-120'], npc=1, yer=-10 )
			elif distance > 15:
				damage = rollDamage( options=player['Damage-60'], npc=1, yer=-10 )
			else:
				damage = rollDamage( options=player['Damage-Melee'], npc=1, yer=-10 )
			# _.pr("mobs[mi]['health']",mobs[mi]['health'],,ROUND)
			mobs[mi]['health'] = mobs[mi]['health'] - damage
			if mobs[mi]['health'] < 1:
				# XP += XP_PER
				if __.printing:
					_.cp( [ 'NPC DEAD:', mobs[mi] ], 'green' )
				mobs.pop(mi)
				if not len(mobs):
					return None
		# PLAYER MOVE X2 Because of Ronan AND Shade
		mi = random.randint(0,len(mobs)-1)
		ac = roll(dice=20,cnt=1)
		if ac >= mobs[mi]['ac']:
			if distance > 60:
				damage = rollDamage( options=player['Damage-120'], npc=1, yer=-11 )
			elif distance > 15:
				damage = rollDamage( options=player['Damage-60'], npc=1, yer=-11 )
			else:
				damage = rollDamage( options=player['Damage-Melee'], npc=1, yer=-11 )
			mobs[mi]['health'] = mobs[mi]['health'] - damage
			# _.pr("mobs[mi]['health']",mobs[mi]['health'],ROUND)
			if mobs[mi]['health'] < 1:
				# XP += XP_PER
				if __.printing:
					_.cp( [ 'NPC DEAD:', mobs[mi] ], 'green' )
				mobs.pop(mi)
				if not len(mobs):
					return None

		mob_health=[]
		for i,mob in enumerate(mobs):
			mob_health.append( mob['health'] )

		pass
		spent=[]
		for i,mob in enumerate(mobs):
			ac = roll(dice=20,cnt=1)
			if ac >= player['ac']:
				# _.pr('ac',ac)



				spent.append(i)
				damage=mobs_fight(distance,mob,i)
				if damage:
					old=HEALTH
					HEALTH -= damage
					dic = {
								'old': old,
								'HEALTH': HEALTH,
								'mobs': mob_health,
								'R': ROUND,
					}
					if __.printing:
						_.pr('HEALTH',dic)
					player['health'] = HEALTH
					
					if HEALTH < 1:
						healing_potion()

						# _.pr( 'PLAYER DEAD:', player )
						# _.pr( 'KILLED BY:', mob )
						# _.e('DEAD')



		distance -= 30






def mobs_fight(distance,mob,yer):
	if distance > 60:
		damage = rollDamage( options=mob['Damage-120'], npc=0, yer=yer )
	elif distance > 15:
		damage = rollDamage( options=mob['Damage-60'], npc=0, yer=yer )
	else:
		damage = rollDamage( options=mob['Damage-Melee'], npc=0, yer=yer )
	return damage





def rest():
	global HEALTH
	global LAST_FULL_HEALTH
	global healing_RING
	healing_RING = False
	OLD_HEALTH = HEALTH
	MAX = healthXP()
	if not LAST_FULL_HEALTH == MAX:
		HEALTH +=  MAX - LAST_FULL_HEALTH


	HEALTH + levelXP()

	if __.printing:
		_.cp( [ 'REST', { 'old': OLD_HEALTH, 'new': HEALTH } ], 'yellow' )
	HEALTH = MAX

def healing_potion():
	global HEALTH
	global POTIONS_USED
	global healing_RING
	if not healing_RING:
		healing_RING=True
	HEALTH += healing_RING
	while HEALTH < 5:
		POTIONS_USED+=1
		HEALTH += roll(dice=4,cnt=2)+2



def action():
	global POTIONS_USED_LIST
	POTIONS_USED_LIST = []

	ip = 100
	did = 0
	while not did == ip:
		did+=1
		simulation_of_years()

	_.pr()
	_.linePrint(txt=' ',p=1)
	_.pr()
	_.pr('Potions average of',_.addComma(ip)+':',Average(POTIONS_USED_LIST))

def Average(lst):
	return sum(lst) / len(lst)

def simulation_of_years():
	global POTIONS_USED_LIST
	global XP
	global HEALTH
	global XP_PER
	global LAST_FULL_HEALTH
	global healing_RING
	global POTIONS_USED






	POTIONS_USED = 0
	XP = int(_.switches.value('XP-Start'))
	
	HP_END = int(_.switches.value('XP-End'))
	LAST_FULL_HEALTH = healthXP()
	HEALTH = healthXP()

	# _.pr('starting-health',HEALTH, 'Level:',levelXP())
	
	# sys.exit()


	while not XP >= HP_END:
		battle()
		XP+=XP_PER
		rest()

	# _.pr('POTIONS_USED:',POTIONS_USED)
	POTIONS_USED_LIST.append(POTIONS_USED)
	# _.pr('ending-health',HEALTH, 'Level:',levelXP())


__.printing=0


import random
_.pr()

XP_PER = 500


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()