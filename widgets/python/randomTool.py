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
	_.switches.register( 'Between', '-b', '10-20 6' )
	_.switches.register( 'Case', '-case' )
	_.switches.register( 'Int', '-int' )
	_.switches.register( 'Text', '-text' )
	_.switches.register( 'Around', '-around', ' 0000.000 OR probability 100000' )
	_.switches.register( 'ProbRandom', '-prob', '1-10   OR   1-10 100000   OR   1-100000 --c' )
	_.switches.register( 'Variance', '-var,-variance' )

	_.switches.register( 'Clean', '--c' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'randomTool.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Randomize stuff',
	'categories': [
						'random',
						'randomize',
						'tool',
						'case',
						'order',
						'true false',
						'true',
						'false',
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
						'p randomTool -case {6AB92DF0-EB27-4370-AE66-E946E54DD411}',
						'',
						'random date:',
						'\tp randomTool -around 1616349556.9732485',
						'\tp randomTool -around 1616349556.9732485 | p line --c -make "p ago -epoch {}" | p execute',
						'\tp ago | p fileLine -line 1 | p line --c -make "p randomTool -around {}" | p execute --c | p line --c -make "p ago -epoch {}" | p execute',
						'',
						'p randomTool -around 100 -prob 100',
						'p randomTool -prob 1-100000 --c',
						'p randomTool -prob 1-10',
						'',
						'p randomTool -around probability 100000',
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

import random

def true_false(fix=2):

	global randomTrueFalseLast
	global randomTrueFalseCount
	global randomTrueFalseSame
	try:
		randomTrueFalseLast
	except Exception as e:
		randomTrueFalseLast = True
		randomTrueFalseSame = 0
		randomTrueFalseCount = 0

	ran = random.randint(1,101)
	result = ran % 2 == 0
	i = 0
	while i < fix:
		i+=1
		if result == randomTrueFalseLast:
			ran = random.randint(100,200)
			result = ran % 2 == 0

	if result == randomTrueFalseLast:
		randomTrueFalseSame += 1
	randomTrueFalseCount += 1
	randomTrueFalseLast = result
	return result
def case(string):
	

	result = ''
	for ch in string:
		if ch.isalnum():
			try:
				int(ch)
			except Exception as e:
				ran = random.randint(1,101)
				test = ran % 2 == 0
				if true_false():
					ch = ch.lower()
				else:
					ch = ch.upper()
		result += ch
	return result


def percentage( part, whole, i=1 ):
	if i:
		return int(100 * float(part)/float(whole))
	else:
		return (100 * float(part)/float(whole))

def tf():
	# n = '0'
	# for x in str(uuid.uuid4()):
	#     if x in '0123456789':
	#         n+=x
	# nn = int(n)
	if (  random.randint(100,200)   % 2) == 0:
	# if (  nn   % 2) == 0:
		return True
	else:
		return False
	
import uuid
def around( string, place_value_strict=False ):
	ee = ''
	if '.' in string:
		ee = '.' + str(int_zero(  string.split('.')[1]  ))
		# ee='.1000'
		string = string.split('.')[0]
	val = int(string)
	# _.pr(val)
	pL = 1
	# sB = percentage( 500, val, i=0 )
	variance = 5
	if _.switches.isActive('Variance'):
		if len( _.switches.value(Variance) ):
			variance = int( _.switches.value(Variance) )

		if len( _.switches.values(Variance) ) > 1:
			maxVarianceLoops = int( _.switches.values(Variance)[1] )
	
	maxVarianceLoops = 1000
	

	sB = percent_of( val, 5 )
	tx = sB
	# _.pr(sB)

	vLoop = 0
	while tf() and vLoop < maxVarianceLoops:
		vLoop+=1
		tx+=sB
		pL+=1


	# _.pr(pL,sB,tx)

	s = val - tx
	e = val + tx
	ran=0
	ran = random.randint(s,e)
	if len(ee):
		if ee.endswith('0'):
			ex = ee

			while ex.endswith('0'):
				ex = ex.replace( '.', '.0' )
				ex = ex[:len(ex) - 1]

			return float(str(ran)+ex)
			# return float(str(ran)+ee.replace('.','.0'))
		else:
			return float(str(ran)+ee)

	return ran
	# _.pr( ran, ' | ', s, '-', e )

def percent_of( n, p ):

	return int((  n * p ) / 100)

	nn = n
	while True:
		nn-=1
		pp = percentage( nn, n )
		# _.pr( 'po', n, p, '-', nn, pp )
		if pp <= p:
			return nn

def around_probability():

	do=10000
	if len(  _.switches.values('Around')  ) > 1:
		do = int( _.switches.values('Around')[1] )

	i=0
	x = {}
	_.pr( _.addComma(do) )
	while not i==do:
		i+=1
		t=0
		while tf():
			t+=1
		if not str(t) in x:
			x[str(t)] = 0
		x[str(t)]+=1
	x = _.dic_key_sort( x, n=1 )
	_.printVarSimple(x)
	
	for y in x.keys():
		_.pr( y, percentage( x[y], do, i=0 ) )


def around_probability_real():
	a = _.switches.value('Around')
	do=10
	if len(  _.switches.value('ProbRandom')  ) > 0:
		do = int( _.switches.values('ProbRandom')[0] )

	i=0
	x = {}
	_.pr( _.addComma(do) )
	while not i==do:
		i+=1
		t = around( a )
		if not str(t) in x:
			x[str(t)] = 0
		x[str(t)]+=1
	x = _.dic_key_sort( x, n=1 )
	_.printVarSimple(x)

def prob_random():
	if len(  _.switches.values('ProbRandom')  ) == 0 or not '-' in _.switches.values('ProbRandom')[0]:
		_.colorThis( 'Error: expected   1-10   OR   1-10 100000' )
		sys.exit()
	do=10000
	if len(  _.switches.values('ProbRandom')  ) > 1:
		do = int( _.switches.values('ProbRandom')[1] )

	sw = _.switches.values('ProbRandom')[0].split('-')
	s = int(sw[0])
	e = int(sw[1])

	i=0
	x = {}
	_.pr( _.addComma(do) )



	while not i==do:
		i+=1
		t=0
		t = random.randint(s,e)
		if not str(t) in x:
			x[str(t)] = 0
		x[str(t)]+=1
	x = _.dic_key_sort( x, n=1 )
	if not _.switches.isActive('Clean'):
		_.printVarSimple(x)
	p = []
	for y in x.keys():
		pp = percentage( x[y], do, i=0 )
		p.append(pp)
		if not _.switches.isActive('Clean'):
			_.pr( y, pp )
	_.pr()
	_.pr( Average(p) )
def Average(lst): 
	return sum(lst) / len(lst)

def int_zero(s, e=None):
	# s = str(s)
	# e = str(e)
	if e is None:
		lint = []
		lint.append( '1' )
		for i,x in enumerate(s):
			if i:
				lint.append( '0' )
		start = int( ''.join(lint) )

		lint = []
		for i,x in enumerate(s):
			lint.append( '9' )
		end = int( ''.join(lint) )
		ran = random.randint(start,end)
	elif not e is None:
		start = int( s )
		end = int( e )
		ran = random.randint(start,end)
	return ran

def action():
	if _.switches.isActive('Between'):
		if len(_.switches.values('Between')) == 1: 
			x = random.randint(int(_.switches.values('Between')[0].split('-')[0]), int(_.switches.values('Between')[0].split('-')[1]))
			_.pr(x)
		else:
			i=0
			e=int(_.switches.values('Between')[1])
			while not i == e:
				i+=1
				x = random.randint(int(_.switches.values('Between')[0].split('-')[0]), int(_.switches.values('Between')[0].split('-')[1]))
				_.pr(x)    
		return None

	# _.pr( percent_of( 100, 5 ) )
	# _.pr( percent_of( 1616348027, 5 ) )
	# sys.exit()
	if _.switches.isActive('ProbRandom'):
		if _.switches.isActive('Around'):
			around_probability_real()
		else:
			prob_random()
		sys.exit()
	if _.switches.isActive('Around'):
		if 'prob' in _.switches.value('Around').lower():
			around_probability()
		else:
			a = around( _.switches.value('Around') )
			_.pr( a )
		sys.exit()
	if _.switches.isActive('Case'):
		for x in _.switches.values('Case'):
			_.pr( case( x ) )

	if _.switches.isActive('Int'):
		if len( _.switches.value('Int') ):
			e = None
			s = _.switches.values('Int')[0]
			if len(_.switches.values('Int')) == 2:
				e = _.switches.values('Int')[1]

			ran = int_zero( s, e )

		elif not len( _.switches.value('Int') ):
			ran = random.randint(1,1000001)
		_.pr( ran )

	if _.switches.isActive('Text'):
		for x in _.switches.values('Text'):
			data = []
			for i,row in enumerate( x ):
				data.append({ 'sort': _.genUUID(), 'data': row })

			records = _.tables.returnSorted( 'data', 'd.sort', data )
			new = []
			for x in records:
				new.append( x['data'] )
			_.pr( ''.join(new) )



########################################################################################
if __name__ == '__main__':
	action()







