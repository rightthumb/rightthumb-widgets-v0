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
# import platform
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
	_.switches.register( 'Games', '-games' )
	_.switches.register( 'Players', '-players' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'war.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'plays the card game war',
	'categories': [
						'cards',
						'game',
						'war',
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
						'p war',
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
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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

values = {
			'2': 2,
			'3': 3,
			'4': 4,
			'5': 5,
			'6': 6,
			'7': 7,
			'8': 8,
			'9': 9,
			'10': 10,
			'J': 11,
			'Q': 12,
			'K': 13,
			'A': 14,
}

# def test( data ):
#     global values
#     tmp = []

#     for i,c in enumerate(data):
#         tmp.append({ 'card': c, 'val': values[c[:-1]], 'player': i+1 })
#     sortedDeck = _.tables.returnSorted( 'data', 'd.val', tmp )
#     return sortedDeck
	# _.pr( sortedDeck )
	# sys.exit()
	# aa = a[:-1]
	# bb = b[:-1]

	# if values[aa] > values[bb]:
	#     return 1
	# elif values[aa] < values[bb]:
	#     return 2
	# elif values[aa] == values[bb]:
	#     return 3
	# else:
	#     return 4


def shuffle( deck ):
	tmp = []
	for c in deck:
		tmp.append({ 'card': c, 'key': _.genUUID() })
	sortedDeck = _.tables.returnSorted( 'data', 'd.key', tmp )
	newDeck = []
	for cx in sortedDeck:
		newDeck.append(cx['card'])
	return newDeck

hands = {}


def play():
	global loopCheck
	global hands
	global lost
	winner = False
	while not winner:
		loopCheck += 1
		if loopCheck > 100000:
			for p in hands:
				if not p in lost:
					if len(hands[p]):
						_.pr( '?', p, len(hands[p]), hands[p] )
			# _.pr( 'TIE' )
			_.colorThis( 'DRAW', 'green' )
			winner = True
		cnt = 0
		for p in hands:
			if not p in lost:
				if not len(hands[p]):
					lost.append(p)
					_.colorThis( [p, 'lost'], 'red' )
				else:
					cnt+=1
		if cnt == 1:

			for p in hands:
				if not p in lost:
					if len(hands[p]):
						_.colorThis( ['winner:', p], 'green' )
						# _.pr( 'winner:', p )
						winner = True
		if cnt == 0:
			lost.reverse()
			_.pr( 'Loosing TIE:', lost[0], lost[1] )
			winner = True
		if not cnt == 1 and not cnt == 0:
			hand()

		

def hand():
	global total_hands
	global lost
	global hands
	global war_cards
	global values
	global warLEVEL
	war_cards = []
	h = []
	total_hands['hands']+=1
	total_hands['total']+=1
	for i,p in enumerate(hands):
		if not p in lost:
			c = hands[p].pop(0)
			h.append( { 'card': c , 'val': values[c[:-1]], 'player': i+1 } )

	result = _.tables.returnSorted( 'data', 'd.val', h )

	# result = test( h )
	if len( result ) == 1:
		return None

	if result[0]['val'] == result[1]['val']:
		mx = result[0]['val']
		battling = []
		for cx in result:
			if cx['val'] == mx:
				if len(hands[cx['player']]):
					battling.append( cx['player'] )
		warLEVEL['level'] = 0
		# warLEVEL = { 'level': 0, 'totals':{}, 'game':{}, 'max': 0 }
		winner = war( battling )
		if warLEVEL['level']:
			if not warLEVEL['level'] in warLEVEL['totals']:
				warLEVEL['totals'][ warLEVEL['level'] ] = 0
			if not warLEVEL['level'] in warLEVEL['game']:
				warLEVEL['game'][ warLEVEL['level'] ] = 0
			warLEVEL['totals'][ warLEVEL['level'] ]+=1
			warLEVEL['game'][ warLEVEL['level'] ]+=1
			if warLEVEL['level'] > warLEVEL['max']:
				__.maxDepthGame = __.currentGame
				warLEVEL['max'] = warLEVEL['level']
		# if not 
		if not winner is None:
			for x in war_cards:
				hands[winner].append(x)

	else:
		winner = result[0]['player']
	
	# winner = result[0]['player']
	if not winner is None:
		for cx in result:
			hands[winner].append( cx['card'] )
	# _.pr( result )
	# sys.exit()

def war( battling ):
	global total_wars
	global hands
	global war_cards
	global lost
	global warLEVEL

	
	# for p in battling:
	#     _.pr( p, len(hands[p]) )
	cg = {}
	for p in battling:
		cg[p] = []
	noCards = []
	for p in battling:
		try:
			cg[p].append(hands[p].pop(0))
		except Exception as e:
			if not p in noCards:
				noCards.append(p)
		try:
			cg[p].append(hands[p].pop(0))
		except Exception as e:
			if not p in noCards:
				noCards.append(p)
		try:
			cg[p].append(hands[p].pop(0))
		except Exception as e:
			if not p in noCards:
				noCards.append(p)
		try:
			cg[p].append(hands[p].pop(0))
		except Exception as e:
			if not p in noCards:
				noCards.append(p)
		cg[p].reverse()


	for i,p in enumerate(cg):
		for x in cg[p]:
			war_cards.append(x)

	h = []
	for i,p in enumerate(cg):
		if not p in noCards:
			h.append( { 'card': cg[p][0], 'val': values[cg[p][0][:-1]], 'player': p } )

	result = _.tables.returnSorted( 'test', 'd.val', h )
	if len(result) > 1:
		
		total_wars['war']+=1
		total_wars['total_war']+=1
		if warLEVEL['level'] == 0:
			_.colorThis( [warLEVEL['level']+1, 'battling:', battling, result], 'white' )
		elif warLEVEL['level'] == 1:
			_.colorThis( [warLEVEL['level']+1, 'battling:', battling, result], 'yellow' )
		elif warLEVEL['level'] == 2:
			_.colorThis( [warLEVEL['level']+1, 'battling:', battling, result], 'purple' )
		elif warLEVEL['level'] == 3:
			_.colorThis( [warLEVEL['level']+1, 'battling:', battling, result], 'cyan' )
		elif warLEVEL['level'] > 3:
			_.colorThis( [warLEVEL['level']+1, 'battling:', battling, result], 'green' )

		# _.pr()
	
	if len(result) == 0:
		for p in battling:
			lost.append(p)
			_.colorThis( [p, 'lost'], 'red' )
		return None
		_.colorThis(  'Error: b23', 'red'  )
		_.pr(  )
	elif len(result) == 1:
		for p in battling:
			if not p == result[0]['player']:
				lost.append(p)
				_.colorThis( [p, 'lost'], 'red' )

		return result[0]['player']
	else:
		warLEVEL['level'] +=1
	if not result[0]['val'] == result[1]['val']:
		return result[0]['player']
	elif result[0]['val'] == result[1]['val']:
		total_wars['multi'] += 1
		total_wars['total_multi'] += 1
		# _.colorThis( 'multi - war:', 'purple' )
		mx = result[0]['val']
		nBattling = []
		for cx in result:
			if cx['val'] == mx:
				if not cx['player'] in noCards:
					nBattling.append( cx['player'] )
		if len(nBattling) == 0:
			for p in battling:
				_.colorThis( [p, 'lost'], 'red' )
				lost.append(p)
			return None
				# _.pr( p, len(hands[p]) )
			# _.colorThis( [ 'Error', battling, cg, war_cards ], 'red' )
		if len(nBattling) == 1:
			for p in battling:
				if not p == nBattling[0]:
					lost.append(p)
					_.colorThis( [p, 'lost'], 'red' )
			return nBattling[0]
		# _.pr(nBattling)
		return war( nBattling )



def newGame():
	_.pr()
	_.pr()
	_.pr()
	_.pr()
	global players
	global hands
	global loopCheck
	global lost
	global total_wars
	global total_hands
	global warLEVEL

	__.currentGame +=1
	_.colorThis(  ['GAME:', __.currentGame], 'cyan'  )
	# _.pr(  )

	total_wars['war'] = 0
	total_wars['multi'] = 0
	total_hands['hands'] = 0
	warLEVEL['game'] = {}
	lost = []
	loopCheck = 0
	hands = {}
	deck = shuffle( 'AC,2C,3C,4C,5C,6C,7C,8C,9C,10C,JC,QC,KC,AD,2D,3D,4D,5D,6D,7D,8D,9D,10D,JD,QD,KD,AH,2H,3H,4H,5H,6H,7H,8H,9H,10H,JH,QH,KH,AS,2S,3S,4S,5S,6S,7S,8S,9S,10S,JS,QS,KS'.split(',') )
	# _.pr( deck )

	# players = 8
	for p in range(1,players+1):
		hands[p] = []
	#     pass
	p = 1
	for c in deck:
		try:
			hands[p].append( c )
		except Exception as e:
			p=1
			hands[p].append( c )
		p+=1
		if p > players:
			p = 1
	# for p in hands:
	#     _.pr( p, len(hands[p]) )
	play()
	# _.pr( 'wars:', total_wars['war'] )
	# _.pr( 'multi-wars:', total_wars['multi'] )
	totals = {}
	wtotal = 0
	# total_wars = 0
	for k in sorted(warLEVEL['game'].keys()):
		totals[k] = warLEVEL['game'][k]
		wtotal += totals[k]

	_.pr( 'hands:', total_hands['hands'])
	_.pr( 'depths of war:', totals)
	_.pr( 'Total wars:', wtotal )


def action(total_games=1):
	global total_wars
	global players
	global total_hands
	global warLEVEL

	__.currentGame = 0
	__.maxDepthGame = 0

	# warLEVEL = { 'level': 0, 'totals':{}, 'game':{}, 'max': 0 }
	if _.switches.isActive('Games'):
		total_games = int( _.switches.value('Games') )

	players = 2
	if _.switches.isActive('Players'):
		players = int( _.switches.value('Players') )


	games = 0
	while not games == total_games:
		games+=1
		newGame()

	_.pr()
	_.pr()
	_.pr()
	# _.pr( 'total wars:', total_wars['total_war'] )
	# _.pr( 'total multi-wars:', total_wars['total_multi'] )
	_.pr( 'players:', players )
	_.pr( 'games:', _.addComma(total_games) )
	_.pr( 'hands:', _.addComma(total_hands['total']))
	totals = {}
	wtotal = 0
	for k in sorted(warLEVEL['totals'].keys()):
		totals[k] = warLEVEL['totals'][k]
		wtotal += totals[k]
	_.pr( 'depths of war:', totals)
	_.pr( 'max depths of war:', warLEVEL['max'])
	_.pr( 'Total wars:', _.addComma(wtotal) )
	_.pr( 'Max Depth GAME:', __.maxDepthGame )
	
	# total_wars = { 'war':0,'multi':0,'total_war':0,'total_multi'0 }



total_hands = { 'hands': 0, 'total': 0 }
total_wars = { 'war':0,'multi':0,'total_war':0,'total_multi':0 }
lost = []
war_cards = []
players = 2
loopCheck = 0

# next step
warLEVEL = { 'level': 0, 'totals':{}, 'game':{}, 'max': 0 }
########################################################################################
if __name__ == '__main__':
	action()







