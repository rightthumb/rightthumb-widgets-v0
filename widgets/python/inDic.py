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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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
# import _rightThumb._encryptString as _blowfish
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-word,-test','weapon')
	_.switches.register('Print', '-print')
	_.switches.register('All', '-all')
	



_.appInfo[focus()] = {
	'file': 'inDic.py',
	'description': 'Searches in dictionaries',
	'categories': [
						'research',
						'dictionary',
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

_.appInfo[focus()]['examples'].append('p inDic -print -all -i the')
_.appInfo[focus()]['examples'].append('p franchiseParts | p line -u --c  | p inDic -all')

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
########################################################################################
# START
# import nltk
# from nltk.corpus import brown

def testNoun( word ):
	global noun
	for test in noun.keys():
		if test == word:
			return True
	return False

def testOne( word ):
	global adj
	global adv
	global verb
	global omit
	global noun
	global pronoun

	word = word.lower()

	for test in omit.keys():
		if test == word:
			return 'omit'
			_.pr( 'omit', test, word )
			break

	for test in pronoun.keys():
		if test == word:
			return 'pronoun'
			_.pr( 'pronoun', test, word )
			break

	for test in noun.keys():
		if test == word:
			return 'noun'
			_.pr( 'noun', test, word )
			break

	for test in verb.keys():
		if test == word:
			return 'verb'
			_.pr( 'verb', test, word )
			break


	for test in adv.keys():
		if test == word:
			return 'adv'
			_.pr( 'adv', test, word )
			break

	for test in adj.keys():
		if test == word:
			return 'adj'
			_.pr( 'adj', test, word )
			break


	try:
		if '.' in word:
			t = float(word)
		else:
			t = int(word)
		if str(t) == word:
			return 'number'

	except Exception as e:
		pass
	if word.endswith( 's' ):
		return testOne( word[:-1] )
	return 'unknown'


def testAll( word ):
	global adj
	global adv
	global verb
	global omit
	global noun
	global pronoun

	word = word.lower()
	result = ''
	found = False

	try:
		if '.' in word:
			t = float(word)
			result += 'number,float'
		else:
			t = int(word)
			result += 'number,int'
		if str(t) == word:
			found = True

	except Exception as e:
		pass

	for test in omit.keys():
		if test == word:
			found = True
			result += ',omit'
			break

	for test in pronoun.keys():
		if test == word:
			found = True
			result += ',pronoun'
			break

	for test in noun.keys():
		if test == word:
			found = True
			result += ',noun'
			break

	for test in verb.keys():
		if test == word:
			found = True
			result += ',verb'
			break


	for test in adv.keys():
		if test == word:
			found = True
			result += ',adv'
			break

	for test in adj.keys():
		if test == word:
			found = True
			result += ',adj'
			break



	if not found:
		if word.endswith( 's' ):
			return testAll( word[:-1] )    
		return 'unknown'
	if _.switches.isActive( 'Print' ):
		_.pr( str(word) + ':', result )
	result = _str.cleanBE( result, ',' )
	return result
	# else:
	#     _.pr( 'unknown' )



def action():
	if _.switches.isActive('Input'):
		word = _.switches.value('Input')
		word = word.lower()
		if _.switches.isActive( 'All' ):
			test = testAll( word )
		else:
			test = testOne( word )
		if test == 'unknown' and word.endswith('s'):
			if _.switches.isActive( 'All' ):
				test = testAll( word[:-1] )
			else:
				test = testOne( word[:-1] )
		record = { 'word': word, 'type': test }
		if _.switches.isActive( 'Print' ):
			_.pr( record )

		return test
		return record
		

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		data = []
		for word in _.appData[__.appReg]['pipe']:

			if _.switches.isActive( 'All' ):
				test = testAll( word )
			else:
				test = testOne( word )

			if test == 'unknown' and word.endswith('s'):
				if _.switches.isActive( 'All' ):
					test = testAll( word[:-1] )
				else:
					test = testOne( word[:-1] )

			if _.switches.isActive( 'All' ):
				record = { 'cnt': len(test.split(',')), 'type': test, 'word': word }
			else:
				record = { 'type': test, 'word': word }
			data.append( record )

		result = _.tables.returnSorted( 'data', 'a.type', data )

		for row in result:
			_.pr( row )



adj = _.getTable( 'dic_adj.json' )
adv = _.getTable( 'dic_adv.json' )
noun = _.getTable( 'dic_noun.json' )
verb = _.getTable( 'dic_verb.json' )
omit = _.getTable( 'dic_omit.json' )
pronoun = _.getTable( 'dic_pronoun.json' )

########################################################################################
if __name__ == '__main__':
	_.switches.fieldSet( 'Print', 'active', True )
	action()