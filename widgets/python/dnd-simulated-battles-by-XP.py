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
try:
	import winsound
except Exception as e:
	pass
##################################################

def appSwitches():
	pass
	# _.switches.register( 'XP-Start', '-start' )
	# _.switches.register( 'XP-End', '-end' )

	# _.switches.register( 'Hit-Dice', '-dice', 'd10' )
	# _.switches.register( 'Hit-Dice-Mod', '-dice.mod', '9' )
	# _.switches.register( 'Hit-Dice-Plus', '-dice.plus', '19' )
	
	# _.switches.register( 'Damage-120', '-120', '1d8 LOW TO HIGH' )
	# _.switches.register( 'Damage-60', '-60', '1d8 LOW TO HIGH' )
	# _.switches.register( 'Damage-Melee', '-melee', '1d8 LOW TO HIGH' )



	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )
	### EXAMPLE: END

#   finds the file in probable locations
#   and 
#       if  _.autoBackupData = True
#       and __.releaseAcquiredData = True
#           GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#       you can run apps on usb at a clients office
#           when you get home run: p app -loadepoch epoch 
#               backed up
#                   pipe
#                   files
#                   tables
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
						_.hp('p dnd-simulated-battles-by-XP'),
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
#                                                   if platform.system() == 'Windows':
########################################################################################
# START



class BEEPS:
	def __init__( self ):
		###
		# Notes Config
		###

		# Set delay tempo
		self.tempo = 0.15
		# tempo = 1

		# Setup Notes
		self.notes = {}
		self.notes["pause"] = 0
		self.notes["c"] = 1
		self.notes["c#"] = 2
		self.notes["d"] = 3
		self.notes["d#"] = 4
		self.notes["e"] = 5
		self.notes["f"] = 6
		self.notes["f#"] = 7
		self.notes["g"] = 8
		self.notes["g#"] = 9
		self.notes["a"] = 10
		self.notes["a#"] = 11
		self.notes["b"] = 12

		# Note Types
		self.note_types = {}
		self.note_types["sixteenth"] = 50
		self.note_types["eigth"] = 100
		self.note_types["dotted_eigth"] = 150
		self.note_types["quarter"] = 200
		self.note_types["half"] = 400
		self.note_types["whole"] = 800
		self.note_types["triplet"] = 60
	def play_note( self, octave, note, note_type ):
		"""Play a note at a certain octave by calculating the frequency of the sound it would represent on the motherboard's speaker."""

		# Match the note and note type to the dictionaries
		note = self.notes[note]
		note_type = self.note_types[note_type]

		# Chill for a bit if it's a pause
		if not note:
			time.sleep(note_type/1000)
			return

		# Calculate C for the provided octave
		frequency = 32.7032 * (2**octave)

		# Calculate the frequency of the given note
		frequency *= 1.059463094**note

		# Beep it up
		try:
			winsound.Beep(int(frequency), note_type)
			# Delay after the beep so it doesn't all run together
			time.sleep(self.tempo)
		except Exception as e:
			pass

	def simple_beep(self):
		oct = 3
		self.play_note(oct, 'g', 'half')

	def simple_beep2(self):
		oct = 3
		self.play_note(oct, 'e', 'half')



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
	global XP_LEVEL
	# _.pv(XP_LEVEL)
	last = {'XP':0,'Level':0,'Prof':0}
	for rec in XP_LEVEL:
		if _.g.mm:
			_.g.m[_.g.i]['prof']=0
			if _.g.m[_.g.i]['xp'] < rec['XP']:
				_.g.m[_.g.i]['level'] = last['Level']
				_.g.m[_.g.i]['prof'] = last['Prof']
				return last['Level']
		else:
			if _.g.p[_.g.i]['xp'] < rec['XP']:
				_.g.p[_.g.i]['level'] = last['Level']
				_.g.p[_.g.i]['prof'] = last['Prof']
				return last['Level']
		last = rec


def healthXP():
	if _.g.mm:
		HP_DICE = int(_.g.m[_.g.i]['hp']['dice'].lower().split('d')[1])
		times = levelXP()
		# _.pr( HP_DICE, levelXP() )
		sub = HP_DICE*(levelXP())
		if 'bo' in _.g.m[_.g.i]['hp']:
			sub += int(_.g.m[_.g.i]['hp']['bo'])
	else:
		HP_DICE = int(_.g.p[_.g.i]['hp']['dice'].lower().split('d')[1])
		times = levelXP()
		# _.pr('healthXP',_.g.p[_.g.i]['name'],HP_DICE,levelXP())
		sub = HP_DICE*(levelXP())
		if 'bo' in _.g.p[_.g.i]['hp']:
			sub += int(_.g.p[_.g.i]['hp']['bo'])
	return sub



def roll(dice=20,cnt=1):
	total = 0
	i=0
	while not i == cnt:
		i+=1
		total += random.randint(1,dice)

	return total

def genMobs():
	mobs = [
			# 15
			{ 'name': _.miniUUID(), 'npc': 1, 'race': 'orc', 'ac': 13, 'xp': 100, 'prof': 0, 
				'hp': { 'val': 15, 'dice': 'd8', 'bo': 0, },
				'stats': {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10 },
				'damage': [
						# {'r':60, 'd': 'throwing-knife','di':'1d4','s':'dex','DC':10},
						{'r':15, 'd': 'club','di':'1d4','s':'dex','DC':10},
					] },
			# 5
			{ 'name': _.miniUUID(), 'npc': 1, 'race': 'kobold', 'ac': 12, 'xp': 100, 'prof': 0, 
				'hp': { 'val': 5, 'dice': 'd6', 'bo': 0, },
				'stats': {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10 },
				'damage': [
						{'r':15, 'd': 'throwing-knife','di':'1d4','s':'dex','DC':10},
					] },
			# { 'name': _.miniUUID(), 'npc': 1, 'race': 'oger', 'ac': 11, 'xp': 100, 'prof': 0, 
			#   'hp': { 'val': 59, 'dice': 'd10', 'bo': 0, },
			#   'stats': {'str': 10, 'dex': 10, 'con': 10, 'int': 10, 'wis': 10, 'cha': 10 },
			#   'damage': [
			#           {'r':15, 'd': 'blunt-object','di':'1d4','s':'dex','DC':10},
			#           {'r':15, 'd': 'blunt-object','di':'1d6','s':'dex','DC':10},
			#           {'r':15, 'd': 'blunt-object','di':'1d10','s':'dex','DC':10},
			#       ] },
	]

	cnt = random.randint(1,2)
	cnt=1
	myMob = mobs[ random.randint(0,len(mobs)-1) ]


	if myMob['hp']['val'] > 16:
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

def rollDamage( dam, ii, yeti ):
	result = 0
	di = dam['di']
	if ',' in dam['di']:
		di = dam['di'].split(',')[0]
		b = int(dam['di'].split(',')[1])
		i = 0
		while not i == b:
			i+=1
			result += roll(  dice=  int( di.split('d')[1] )  ,   cnt=int( di.split('d')[0] )   )
	else:
		result += roll(  dice=  int( di.split('d')[1] )  ,   cnt=int( di.split('d')[0] )   )
	# _.pr( result, ii, yeti )
	return result



# test = [{'a':0},{'a':1},{'a':2}]

BATTLE_ID = 0
ROUND_ID = 0
battle_notes = {}
battle_notes['rounds'] = []
battle_notes['mini'] = []
battle_notes['npc'] = []
def battle():
	global BATTLE_ID
	global ROUND_ID
	global battle_notes
	BATTLE_ID+=1
	battle_notes['mini'].append({ 'battle': str(BATTLE_ID)})
	if __.printing:
		_.pr('\n\n\nBATTLE_ID:',BATTLE_ID)
	
	_.g.m = genMobs()
	_.g.mm = True
	npc = {}
	npcd = {}
	for i,rec in enumerate(_.g.m):
		_.g.m[i]['name'] = _.miniUUID()
		Min = _.g.p[0]['xp']-200
		if Min < 0:
			Min = 0
		npc[_.g.m[i]['name']] = 0
		npcd[_.g.m[i]['name']] = 0
		_.g.m[i]['xp'] = random.randint( Min ,  _.g.p[0]['xp']+200 )
		_.g.i = i
		_.g.m[i]['save'] = {}
		healthXP()
		for st in _.g.m[i]['stats']:
			_.g.m[i]['stats'][st] = roll(20)
			_.g.m[i]['save'][st] = _.g.m[i]['prof']
	battle_notes['mobs'] = _.g.m
	_.g.mm = False



	distance = 120

	ROUND = 0
	
	battle_notes['mini'].append({ 'mob-cnt': str(len(_.g.m))})
	global tryQuit
	tryQuit=False
	while len(_.g.m):
		ROUND+=1
		ROUND_ID+=1
		battle_round(distance,ROUND,npc,npcd)
		if not tryQuit:
			distance -= 30
		if distance < 0:
			distance = 10
		if distance > 120:
			battle_notes['round'].append({ 'ran away': 'HA HA HA!!'})
			battle_notes['mini'].append({ 'ran away': 'HA HA HA!!'})
			battle_notes['npc'].append({ 'ran away': 'HA HA HA!!'})
			_.pr('ran away')
			break
	return ROUND

def battle_round(distance,R,npc,npcd):
	turn=0
	global tryQuit
	global BATTLE_ID
	global battle_notes
	if distance > 120:
		return None
	_.g.mm = False
	battle_notes['mini'].append({ 'round': str(R)})
	battle_notes['rounds'].append({'BEGIN':'   '+str(BATTLE_ID)+'   '+ str(R) +'   '+'###########################################################################################'})
	battle_notes['rounds'].append({'distance': distance })
	for i,rec in enumerate(_.g.p):
		_.g.i = i

		if not _.g.p[i]['mage-armor']:
			_.g.p[i]['mage-armor'] = True
			_.g.p[i]['hp']['val']+=_.g.p[i]['mage-armor-val']
		else:
			mi = random.randint(0,len(_.g.m)-1)
			ac = roll(20)
			turn+=1
			battle_notes['rounds'].append({'turn':turn})
			battle_notes['rounds'].append({'player':_.g.p[i]['name']})
			battle_notes['rounds'].append({'player-hp':_.g.p[i]['hp']['val']})
			battle_notes['rounds'].append({'opponent':mi})
			battle_notes['rounds'].append({'opponent-hp':_.g.m[mi]['hp']['val']})
			if ac >= _.g.m[mi]['ac']:
				battle_notes['rounds'].append({'ac':True})
			else:
				battle_notes['rounds'].append({'ac':False})
			if ac >= _.g.m[mi]['ac']:
				dams = []
				for dam in _.g.m[mi]['damage']:
					if dam['r'] >= distance:
						dams.append(dam)
				
				battle_notes['rounds'].append({'weapon-options':len(dams)})
				if len(dams):
					hit = True
					di = random.randint( 0, len(dams)-1 )
					battle_notes['rounds'].append({'weapon': str(dams[di])})
					if 'DC' in dams[di]:
						if dams[di]['DC'] < roll(20) + _.g.m[mi]['prof']:
							battle_notes['rounds'].append({'save':True})
							hit = False
						else:
							battle_notes['rounds'].append({'save':False})

					battle_notes['rounds'].append({'hit':hit})
					if hit:
						damage = rollDamage( dams[di], i, 0 )
						npc[_.g.m[mi]['name']]+=1
						battle_notes['rounds'].append({'damage':damage})
						battle_notes['npc'].append({_.g.m[mi]['name']+str(mi)+'-damage':damage})
						battle_notes['rounds'].append({'hp-before':_.g.m[mi]['hp']['val']})
						battle_notes['npc'].append({_.g.m[mi]['name']+str(mi)+'-hp-before':_.g.m[mi]['hp']['val']})
						_.g.m[mi]['hp']['val'] -= damage
						battle_notes['npc'].append({_.g.m[mi]['name']+str(mi)+'-hp-after':_.g.m[mi]['hp']['val']})
						battle_notes['rounds'].append({'hp-after':_.g.m[mi]['hp']['val']})
						if _.g.m[mi]['hp']['val'] < 15:
							tryQuit=True
							distance+=30
						if _.g.m[mi]['hp']['val'] < 1:
							n = _.g.m[mi]['name']
							battle_notes['npc'].append({_.g.m[mi]['name']+str(mi)+'-NPC-DEAD': npc[_.g.m[mi]['name']] })
							battle_notes['rounds'].append({'NPC-DEAD ++++++++++++++++++++++++++++++++++++++++++++++++++++++++':mi})
							if __.printing:
								_.cp( [ 'NPC DEAD:', _.g.m[mi] ], 'green' )
							# _.g.m.pop(mi)
							utter = []
							for l2,spoo in enumerate(_.g.m):
								if not spoo['name'] == n:
									utter.append(spoo)
							_.g.m = utter
							del utter
							npcd[n]+=1
							battle_notes['npc'].append({n+str(mi)+'-DELETED': npcd[n] })

							if not len(_.g.m):
								return None


	_.g.mm = True
	for i,rec in enumerate(_.g.m):
		_.g.i = i

		mi = random.randint(0,len(_.g.p)-1)
		ac = roll(20)
		turn+=1
		battle_notes['rounds'].append({'turn':turn})
		battle_notes['rounds'].append({'player':_.g.m[i]['race']})
		battle_notes['rounds'].append({'player-hp':_.g.m[i]['hp']['val']})
		battle_notes['rounds'].append({'opponent':_.g.p[mi]['name']})
		battle_notes['rounds'].append({'opponent-hp':_.g.p[mi]['hp']['val']})
		if ac >= _.g.p[mi]['ac']:
			battle_notes['rounds'].append({'ac':True})
		else:
			battle_notes['rounds'].append({'ac':False})
		if ac >= _.g.p[mi]['ac']:
			dams = []
			for dam in _.g.p[mi]['damage']:
				if dam['r'] >= distance:
					dams.append(dam)
			
			battle_notes['rounds'].append({'weapon-options':len(dams)})
			if len(dams):
				hit = True
				di = random.randint( 0, len(dams)-1 )
				battle_notes['rounds'].append({'weapon':str(dams[di])})
				if 'DC' in dams[di]:
					if dams[di]['DC'] < roll(20) + _.g.p[mi]['prof']:
						battle_notes['rounds'].append({'save':True})
						hit = False
					else:
						battle_notes['rounds'].append({'save':False})

				battle_notes['rounds'].append({'hit':hit})
				if hit:
					damage = rollDamage( dams[di], i, 0 )
					battle_notes['rounds'].append({'damage':damage})
					battle_notes['mini'].append({_.g.p[mi]['name']+'-damage':damage})
					battle_notes['rounds'].append({'hp-before':_.g.p[mi]['hp']['val']})

					if 'player-shield' in _.g.p[mi]:
						sh = _.g.p[mi]['player-shield']['id']
						good_idea = True
						if _.g.p[sh]['hp']['val'] < 15:
							good_idea = False
							if _.g.p[mi]['hp']['val'] < _.g.p[sh]['hp']['val']:
								good_idea = True

						if not good_idea:
							battle_notes['rounds'].append({'player-shield': 'not good idea'})
							battle_notes['mini'].append({_.g.p[mi]['name']+'-player-shield':'not good idea'})
						if good_idea:
							if 1 == random.randint(1,_.g.p[mi]['player-shield']['prob']):
								battle_notes['rounds'].append({'player-shield': 'failed'})
								battle_notes['mini'].append({_.g.p[mi]['name']+'-player-shield':'failed'})
							else:
								battle_notes['rounds'].append({'player-shield': 'worked'})
								battle_notes['mini'].append({_.g.p[mi]['name']+'-player-shield':'worked'})
								mi = _.g.p[mi]['player-shield']['id']


					battle_notes['mini'].append({_.g.p[mi]['name']+'-hp-before':_.g.p[mi]['hp']['val']})
					_.g.p[mi]['hp']['val'] -= damage
					battle_notes['mini'].append({_.g.p[mi]['name']+'-hp-after':_.g.p[mi]['hp']['val']})
					battle_notes['rounds'].append({'hp-after':_.g.p[mi]['hp']['val']})
					if _.g.p[mi]['hp']['val'] < 10:
						_.g.i = mi
						battle_notes['rounds'].append({'potion':'_________________________________________________________________'})
						battle_notes['rounds'].append({'healing-hp-before':_.g.p[mi]['hp']['val']})
						battle_notes['mini'].append({_.g.p[mi]['name']+'-healing-hp-before':_.g.p[mi]['hp']['val']})
						healing_potion()
						battle_notes['mini'].append({_.g.p[mi]['name']+'-healing-hp-after':_.g.p[mi]['hp']['val']})
						_.g.i = i
						battle_notes['rounds'].append({'healing-hp-after':_.g.p[mi]['hp']['val']})
	_.g.mm = False

	# for i,rec in enumerate(_.g.m):
	#   _.g.i = i

	#   mi = random.randint(0,len(_.g.p)-1)
	#   ac = roll(20)
	#   if ac >= _.g.p[mi]['ac']:
	#       dams = []
	#       for dam in _.g.p[mi]['damage']:
	#           if dam['r'] >= distance:
	#               dams.append(dam)
			
	#       if len(dams):
	#           hit = True
	#           di = random.randint( 0, len(dams)-1 )
	#           if 'DC' in dams[di]:
	#               if dams[di]['DC'] < roll(20) + _.g.p[mi]['save'][dams[di]['s']]:
	#                   hit = False

	#           if hit:
	#               damage = rollDamage( dams[di], i, 1 )
	#               o=_.g.p[mi]['hp']['val']
	#               _.g.p[mi]['hp']['val'] -= damage
	#               # _.pr(o,_.g.p[mi]['hp']['val'])
	#               if _.g.p[mi]['hp']['val'] < 1:
	#                   _.g.i = mi
	#                   healing_potion()
	_.g.mm = False



def rest():
	val = int(str(_.g.p[_.g.i]['hp']['val']))
	battle_notes['rounds'].append({ 'REST': '-------------------------------------------------------------------------------' })
	battle_notes['rounds'].append({ 'player': _.g.p[_.g.i]['name'] })
	battle_notes['rounds'].append({ 'hp-before': _.g.p[_.g.i]['hp']['val'] })
	battle_notes['mini'].append({_.g.p[_.g.i]['name']+'-REST-hp-before':val})
	global healing_RING
	healing_RING = False
	MAX = healthXP()
	if not _.g.p[_.g.i]['hp']['max']  == MAX:
		battle_notes['rounds'].append({ 'LEVEL-UP': '****************************************' })
		val +=  MAX - _.g.p[_.g.i]['hp']['max']
		levelChar()
	val += levelXP()

	_.g.p[_.g.i]['hp']['max'] = MAX
	if 'mage-armor' in _.g.p[_.g.i]:
		_.g.p[_.g.i]['mage-armor'] = False
	battle_notes['rounds'].append({ 'hp-after': val })
	# val = MAX
	if val > MAX:
		val = MAX
	battle_notes['mini'].append({_.g.p[_.g.i]['name']+'-REST-hp-after':val})
	_.g.p[_.g.i]['hp']['val'] = int(str(val))



def healing_potion():
	global healing_RING

	if not healing_RING:
		healing_RING=True
		_.g.p[_.g.i]['hp']['val'] += roll(20)+10
		return None
	while _.g.p[_.g.i]['hp']['val'] < 5:
		_.g.p[_.g.i]['potions']+=1
		_.g.p[_.g.i]['hp']['val'] += roll(dice=10,cnt=2)+2



def Average(lst):
	return sum(lst) / len(lst)
healing_RING=False

def levelChar():
	levelXP()
	if _.g.mm:
		for st in _.g.m[_.g.i]['stats']:
			_.g.m[_.g.i]['save'][st] = _.g.m[_.g.i]['prof'] + _.g.m[_.g.i]['bonus'][st]
			_.g.m[_.g.i]['mods'][st] = _.g.m[_.g.i]['prof']

		for i,dam in enumerate(_.g.m[_.g.i]['damage']):
			if 'dc' in dam:
				if type(dam['dc']) == int:
					_.g.m[_.g.i]['damage']['DC'] = dam['dc']
				elif type(dam['dc']) == str:
					# 8+str+prof
					dam['dc'] = dam['dc'].lower()
					t = 0
					for par in dam['dc'].split('+'):
						if par[0] in '0123456789':
							t += int(par)
						elif par in _.g.m[_.g.i]['stats']:
							t+=_.g.m[_.g.i]['stats'][par]
						elif par == 'prof':
							t+=_.g.m[_.g.i]['prof']
	else:
		for st in _.g.p[_.g.i]['stats']:
			_.g.p[_.g.i]['save'][st] = _.g.p[_.g.i]['prof'] + _.g.p[_.g.i]['bonus'][st]
			_.g.p[_.g.i]['mods'][st] = _.g.p[_.g.i]['prof']

		if 'mage-armor' in _.g.p[_.g.i]:
			_.g.p[_.g.i]['mage-armor-val'] = 13 + _.g.p[_.g.i]['save']['dex']



		for i,dam in enumerate(_.g.p[_.g.i]['damage']):
			if 'dc' in dam:
				if type(dam['dc']) == int:
					_.g.p[_.g.i]['damage']['DC'] = dam['dc']
				elif type(dam['dc']) == str:
					# 8+str+prof
					dam['dc'] = dam['dc'].lower()
					t = 0
					for par in dam['dc'].split('+'):
						if par[0] in '0123456789':
							t += int(par)
						elif par in _.g.p[_.g.i]['stats']:
							t+=_.g.p[_.g.i]['stats'][par]
						elif par == 'prof':
							t+=_.g.p[_.g.i]['prof']

 

def action():
	global BATTLE_ID
	global ROUND_ID
	global games
	games = []

	ip = 99999
	ip = 100
	ip = 1
	did = 0
	while not did == ip:
		did+=1
		simulation_of_years()

	_.pr()
	_.linePrint(txt=' ',p=1)
	_.pr()
	for i,rec in enumerate(_.g.p):
		_.pr(_.g.p[i]['name'],'Potions average of',_.addComma(ip)+':',Average(_.g.p[i]['potions-avg']))

	_.pr( 'battles:',_.addComma(BATTLE_ID) )
	_.pr( 'rounds:',_.addComma(ROUND_ID) )

def simulation_of_years():
	global XP_PER
	global games
	_.g.mm = False

	game = {
				'start': {},
				'end': {},
				'battles': [],
	}
	for i,rec in enumerate(_.g.p):
		_.g.i=i
		_.g.p[i]['potions'] = 0
		_.g.p[i]['xp'] = int(str(_.g.p[i]['xp-b']))
		_.g.p[i]['hp']['max']  = int(str(healthXP()))
		_.g.p[i]['hp']['val'] = int(str(_.g.p[i]['hp']['max']))
		levelChar()
		dic = copy.deepcopy(_.g.p[i])
		game['start'][dic['name']] = dic
		# _.pv(dic)
		# sys.exit()
		



	HP_END = _.g.p[_.g.i]['xp-e']

	# _.pr('starting-health',_.g.p[_.g.i]['hp'], 'Level:',levelXP())
	
	# sys.exit()
	# 0C8CC579
	battle_avg=[]
	i=1
	global BATTLE_ID
	global battle_notes
	while not _.g.p[_.g.i]['xp'] >= HP_END:
		i=i+1

		if 1 == random.randint(1,4):
			bats = random.randint(1,3)
		else:
			bats = 1
		# bats=1
		# if not bats == 1:
		#     _.pr('bats',bats)
		bty = 0
		if 1 == random.randint(1,5):
			bats=0

		while not bty == bats:
			bty+=1
			b = { 'i': i,'rounds': battle(), 'id': BATTLE_ID, 'notes': battle_notes }; game['battles'].append(b); battle_avg.append( b['rounds'] );

		for ii,rec in enumerate(_.g.p):
			_.g.i=ii
			_.g.p[ii]['xp']+=XP_PER
			_.g.p[ii]['level']=levelXP()
			rest()
		# break
	game['battle_avg'] = Average(battle_avg)
	game['loops'] = i



	# _.pr(battle_notes['rounds'])
	# _.pv(battle_notes['rounds'])
	
	battle_notes_text = ''
	for bat in battle_notes['mini']:
		line = str(list(bat.keys())[0]) +':  '+ str(bat[ list(bat.keys())[0] ])
		# _.pr(line)
		line += '\n'
		battle_notes_text+=line



	
	for i,rec in enumerate(_.g.p):
		_.g.i = i
		_.g.p[i]['potions-avg'].append(_.g.p[i]['potions'])
		# _.pr(_.g.p[i]['name'])

		n = _.g.p[i]['name']
		game['end'][n] = _.g.p[i]
		game['mini'] = {
					'start': {
								'hp':    game['start'][n]['hp']['max'],
								'level': game['start'][n]['level'],
								'xp':    game['start'][n]['xp'],
					},
					'end': {
								'hp':    game['end'][n]['hp']['max'],
								'level': game['end'][n]['level'],
								'xp':    game['end'][n]['xp'],
								'potions':    game['end'][n]['potions'],
					},
		}
		_.pv(game['mini'])

	# _.pr( 'battle_avg:', game['battle_avg'] )
	games.append( game )
	# Timer( 0, _beep.simple_beep ).start()

	# _.saveTable(battle_notes['rounds'],'dnd-simulated-battles-by-XP.json')


# from threading import Timer



_.g = _.dot()

_.g.p = []
_.g.m = []

_.g.i = 0
_.g.mm = False

import random
# _.pr()

XP_PER = 500


_.g.p = [
						{
							'id': 0,
							'name': 'Sulnaar',
							'race': 'Dragonborn',
							'class': 'Sorcerer',
							'ac': 14,
							'damage': [
											{'r': 15, 'd': 'ax','di':'2d8','s':'dex','dc': '8+str+prof'},
											{'r':60, 'd': 'xbow-x2','di':'1d10,2'},
											{'r':120, 'd': 'fire','di':'1d12'},

										],
							'stats': {'str': 19, 'dex': 13, 'con': 14, 'int': 10, 'wis': 12, 'cha': 16 },
							'bonus': {'str': 0, 'dex': 0, 'con': 2, 'int': 0, 'wis': 0, 'cha': 2 },
							'save': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
							'mods': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
							'hp': { 'val': 0, 'dice': 'd6', 'bo': 0, 'max': 0},
							'mage-armor': False,
							'prof': 0,
							'xp': 5000,
							'xp-b': 5000,
							'xp-e': 120000,
							'potions': 0,
							'potions-avg': [],
							'player-shield': {'id':1,'prob':2},
						},
						{
							'id': 1,
							'name': 'Shade',
							'race': 'Mimic',
							'class': 'Sorcerer',
							'ac': 14,
							'damage': [
											{'r': 15, 'd': 'ax','di':'2d8','s':'dex','dc': '8+str+prof'},
											{'r':60, 'd': 'xbow-x2','di':'1d10,2'},
											{'r':120, 'd': 'fire','di':'1d12'},

										],
							'stats': {'str': 17, 'dex': 12, 'con': 15, 'int': 5, 'wis': 13, 'cha': 8 },
							'bonus': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
							'save': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
							'mods': {'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 },
							'hp': { 'val': 0, 'dice': 'd8', 'bo': 18, 'max': 0 },
							'mage-armor': False,
							'prof': 0,
							'xp': 5000,
							'xp-b': 5000,
							'xp-e': 120000,
							'potions': 0,
							'potions-avg': [],
						},
					]


_beep=BEEPS()

__.printing=0
import copy

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()


# battle_notes['mini']
# battle_notes['npc']
# simulation_of_years
# 0C8CC579
# healing_RING