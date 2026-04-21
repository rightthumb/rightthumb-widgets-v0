import os

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

import sys
import time
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus(__file__)
# appDBA = __name__
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append(focus())
import _rightThumb._base3 as _
_.load()

##################################################

# import _rightThumb._auditCodeBase as _code

import _rightThumb._vars as _v
import _rightThumb._string as _str
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': '_rightThumb._auditCodeBase.py',
	'description': 'Profiles code of multiple languages',
	'categories': [
						'import',
						'tool',
						'audit',
						'profile',
						'profiler',
						'code profiler',
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

_.appInfo[focus()]['examples'].append('')

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
	_.defaultScriptTriggers()
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	{
		'documentation': True,
		'tags': [

		]
	}

	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if _.appData[__.appReg]['pipe'][0][0].isalnum() == False:
		_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
	for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
		_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )



########################################################################################
########################################################################################
########################################################################################
# START

from _rightThumb._auditCodeBase import config
ins = config.instructions

def findNext( i, p ):
	global ins
	for struct in ins['characters']:
		if i == struct['id']:
			for d in struct['database']:
				if d > p:
					return d
	return False

def findLine( p ):
	global ins
	for struct in ins['characters']:
		if 8 == struct['id']:

			for line, d in enumerate(struct['database']):
				if d > p:
					return line+1
	return False

def findNextLineStart( p ):
	global ins
	for struct in ins['characters']:
		if 8 == struct['id']:

			for line, d in enumerate(struct['database']):
				if d > p:
					return d+1
	return False

def findLineStart( p ):
	global ins
	for struct in ins['characters']:
		if 8 == struct['id']:
			record = 'Error'
			for line, d in enumerate(struct['database']):
				if d > p:
					_.pr(d)
					record = line-1
					break
			
			pass
			if record == -1:
				_.pr(0)
			else:
				_.pr(struct['database'][record],record)

	return False

def loadCharInstructionsByChar( c ):
	global ins
	for struct in ins['characters']:
		if c == struct['char']:
			return struct
	return False

def loadCharInstructionsByID( i ):
	global ins
	for struct in ins['characters']:
		if i == struct['id']:
			return struct

	_.pr( 'charInstructions: Error' )
	sys.exit()

def isCharByID( i, c ):
	global ins
	for struct in ins['characters']:
		if i == struct['id']:
			if c == struct['char']:
				return struct
	return False

def loadRules( i ):
	global ins
	for struct in ins['rules']:
		if i == struct['id']:
			return struct
	_.pr( 'charInstructions: Error' )
	sys.exit()

def inDatabase( i, p ):
	global ins
	for struct in ins['characters']:
		if i == struct['id']:

			if p in struct['database']:
				return True
			else:
				return False
	_.pr( 'inDatabase: Error' )
	sys.exit()

def inDatabaseByCategory( cat, p, strict=True ):
	global code
	global ins
	for struct in ins['characters']:
		for ln in struct['languages']:
			if ln['code'] == 'global' or ln['code'] == code:
				if strict:
					if cat in ln['is']:
						if inDatabase( struct['id'], p ):
							return True
				else:
					for cis in ln['is']: 
						if cat in cis:
							if inDatabase( struct['id'], p ):
								return True

	return False

# inDatabaseByCategory( 'whitespace', 436 )
code = ''
def registerCodeType():
	global code
	f = _.switches.value('Input')
	f = f.lower()
	if f.endswith( '.json' ):
		code = 'json'
	elif f.endswith( '.py' ):
		code = 'python'
	elif f.endswith( '.js' ):
		code = 'javascript'

currentPos=0
actionPlan_count=0
actionPlan_count_raw=0

def dumpDocumentation():
	global documentation
	global currentPos
	global actionPlan_count
	global actionPlan_count_raw
	global omit
	global fileText
	_.pr()
	_.pr()
	_.pr('    START    ')
	_.pr()
	_.pr()
	_.pr(documentation)
	_.pr()
	_.pr()
	_.pr( 'pos:', currentPos )
	_.pr( 'line:', findLine(currentPos) )
	_.pr()
	_.pr( 'actionPlan_count:', actionPlan_count )
	_.pr( 'actionPlan_count_raw:', actionPlan_count_raw )
	_.pr()
	# _.pr('omit dump:')
	# _.pr(omit)
	_.pr()
	dmp = ''
	for o in omit:
		dmp += fileText[o]
	_.pr(dmp)
	_.pr()
	_.pr()
	_.pr('    END    ')
	_.pr()
	_.pr()



def processCharID( p, i=False, charRules=False ):
	global fileText
	global ins
	global code

	if not type( i ) == bool:
		charRules = loadCharInstructionsByID( i )

	if not '#' in fileText[p]:
		_.pr( 'processCharID:', fileText[p] )
	ran = False
	for rl in charRules['languages']:
		if rl['code'] == 'global' or rl['code'] == code:
			if rl['isOpen'] == 1 and rl['hasClose'] == 0 and type( groupID ) == bool:
				ran = True
				pt = p
				while not inDatabaseByCategory( 'end', pt ):
					pt+=1
				resolveRange( p, pt, noPrint=True, forceOmit=True,initiatedBy='processCharID' )
	if not ran:
		_.pr( 'not complete' )
		sys.exit()




def actionPlan( p ):
	global ins
	global fileText
	global labelText0
	global labelText1
	global code
	global omit
	global omitR
	global info
	global documentation
	global currentPos
	global actionPlan_count
	global actionPlan_count_raw
	actionPlan_count_raw+=1
	pt = p
	currentPos=0
	shouldSkip = False
	if inDatabaseByCategory( 'whitespace', p ):
		shouldSkip = True
	if inDatabaseByCategory( 'carage', p ):
		shouldSkip = True
	if inDatabaseByCategory( 'comment', p, strict=False ):
		_.pr(p)
		sys.exit()
		charRules = loadCharInstructionsByChar( fileText[p] )
		if not type( charRules ) == bool:
			e = processCharID( p, charRules=charRules )
			resolveRange( p, e, noPrint=True, forceOmit=True, initiatedBy='omit comment' )
			
		

	if p in omit:
		shouldSkip = True

	if not shouldSkip:
		actionPlan_count+=1

		pt = skipWhitespace( p )
		isAN = str(p) in labelText0
		isAN_NS = str(p) in labelText1
		ran = ''
		for path in ins['action']:
			# _.pr( path['code'] )
			# sys.exit()
			pathFail = False
			if path['code'] == 'global' or path['code'] == code:
				pt = skipWhitespace( pt )
				# _.pr( 'p:', p )
				for test in path['test']:
					pt = skipWhitespace( pt )
					pathFail = False
					if type( test ) == str:
						if path['specific']:
							ran += ' specific'
							for ct in test:
								if not fileText[pt] == ct:
									pathFail = True
								if inDatabaseByCategory( 'end', pt ):
									pt -= 1
									break
								pt += 1
							if pathFail:
								ran += ' pathFail'
							if not pathFail:
								_.pr( 'pass:', test )
								for r in path['rules']:
									ran += ' rules'
									omitR = []
									_.pr( 'STARTING RULE:', r, fileText[p], ';0 ln:',findLine(p) )
									ruleResult = testRule( p, r )
									if type(ruleResult) == int:
										_.pr( type( ruleResult ) )
										# _.pr( 'ruleResult:', ruleResult )
										documentation.append({ 'id': path['id'], 'record': resolveRange( p, ruleResult, initiatedBy='success' ) })
										return True
								_.pr( 'RULE FAIL' )
						else:
							ran += ' NOT specific'
							# not path['specific']

							if fileText[pt] in test:
								while fileText[pt] in test:
									if inDatabaseByCategory( 'end', pt ):
										pt -= 1
										break
									pt+=1
								_.pr( 'pass:', test )
								for r in path['rules']:
									ran += ' rules'
									omitR = []
									_.pr( 'STARTING RULE:', r, fileText[p], ';1 ln:',findLine(p) )
									ruleResult = testRule( p, r )
									if type(ruleResult) == int:
										_.pr( type( ruleResult ) )
										# _.pr( 'ruleResult:', ruleResult )
										documentation.append({ 'id': path['id'], 'record': resolveRange( p, ruleResult, initiatedBy='success' ) })
										return True
								ran += 'RULE FAIL'


	if not shouldSkip:
		_.pr( p,fileText[p], pt,fileText[pt],'\tline:', findLine(p), 'ran:', ran )
		resolveRange( p, pt, justPrint=True, initiatedBy='not shouldSkip' )
		dumpDocumentation()
		if not inDatabaseByCategory( 'comment', p, strict=False ):
			sys.exit()
		sys.exit()
	

def resolveRange( s, e, noPrint=False, justPrint=False, forceOmit=False, initiatedBy='' ):
	global fileText
	global omit
	ss = s
	# _.pr( 'resolveRange:', s, e )
	record = ''
	while not s == e:
		record += str(fileText[s])
		if inDatabaseByCategory( 'end', s ):
			break
		s+=1
	shouldOmit = False
	if not justPrint and not noPrint:
		shouldOmit = True
	if forceOmit:
		shouldOmit = True
	if shouldOmit:
		xx = ss
		yy = findNextLineStart( ss )
		while not xx == yy:
			if not xx in omit:
				omit.append(xx)
			xx+=1


	if not noPrint:
		_.pr( noPrint, justPrint, initiatedBy )
		_.pr( ss,e,'record:', record )
	return record

def testRule( p, r ):
	global fileText
	global labelText0
	global labelText1
	global omitR
	_.pr()
	_.pr('                                              start:',r)
	rules = loadRules( r )
	pt = skipWhitespace( p )

	for i,rule in enumerate(rules['pattern']):
		pt = skipWhitespace( pt )
		_.pr( 'pos:', pt )
		ruleFail = False
		if i in omitR:
			_.pr( 'skipped:', i )
		else:
			for test in rule['test']:
				if type( test ) == str:
					if rule['specific']:
						for ct in test:
							if not fileText[pt] == ct:
								ruleFail = True
								if rule['required']:
									_.pr( r, 'Hard Fail:0', test, fileText[pt], rules['code'] )
									resolveRange( p, pt, justPrint=True, initiatedBy='tr hf 0' )
									resetLine = findLineStart( p )
									_.pr('END resetLine')
									dumpDocumentation()
									return False
								else:
									omitR.append( i )
									_.pr( 'Soft Fail:0', test, fileText[pt], rules['code'] )
									# testRule( p, r )
							else:
								if inDatabaseByCategory( 'end', pt ):
									pt -= 1
									break
								pt += 1
							if not ruleFail:
								_.pr( 'pass:', test )
					else:
						if fileText[pt] in test:
							while fileText[pt] in test:
								if inDatabaseByCategory( 'end', pt ):
									pt -= 1
									break
								pt+=1
						else:
							ruleFail = True
							if rule['required']:
								_.pr( r, 'Hard Fail:1', test, fileText[pt], rules['code'] )
								resolveRange( p, pt, justPrint=True, initiatedBy='tr hf 1' )
								resetLine = findLineStart( p )
								_.pr('END resetLine')
								dumpDocumentation()
								return False
							else:
								omitR.append( i )
								_.pr( 'Soft Fail:1', test, fileText[pt], rules['code'] )
								# testRule( p, r )

				elif type( test ) == int:
					_.pr()
					_.pr('isInt',r,fileText[p],'; ln:',findLine(p) )
					charTest = isCharByID( test, fileText[p] )
					_.pr( type( charTest ) )
					_.pr()
					
				else:
					_.pr( type( test ) )
					_.pr( 'not string' )
	_.pr('end')
	# sys.exit()
	return pt

def skipWhitespace( p ):
	# _.pr( 'skipWhitespace: ran' )
	while inDatabaseByCategory( 'whitespace', p ):
		_.pr( str(fileText[p])+'** skipped ** ' )
		if inDatabaseByCategory( 'end', p ):
			break
		p+=1
	return p
		# _.pr( rule )

	# _.pr( rules )

# isWhitespace = inDatabaseByCategory( 'whitespace', p )
# isEnd = inDatabaseByCategory( 'end', p )


def action():
	global tickets
	global info
	global fileText
	global ins
	global code


	registerCodeType()






	filepath = os.path.abspath( _.switches.value('Input') )
	if not os.path.isfile( filepath ):
		_.pr( 'No File:', filepath )
		return False

	# _.pr( filepath )

	fileTable = _.getText( filepath )
	fileText = ''.join( fileTable )
	# _.pr( type( fileText ) )
	# _.pr( fileText )
	

	# create databases

	for i,ch in enumerate(fileText):
		for struct in ins['characters']:
			if ch == struct['char']:
				struct['database'].append( i )


	for i,ch in enumerate(fileText):
		actionPlan( i )

			





def findConsecutive( data, cnt ):
	pass

def reset():
	global tickets
	global info
	global fileText
	global code
	global ins
	global omit
	global documentation

	for i,struct in enumerate(ins['characters']):
		ins['characters'][i]['database'] = []

	tickets = []
	info = {}
	fileText = ''
	code = ''
	omit = []
	omitR = []
	documentation = []

documentation = []
omit = []
omitR = []
info = {}
fileText = ''
labelText0 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
labelText1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.'

########################################################################################
if __name__ == '__main__':
	action()















# for alpha numeric skip ahead and check if next is equals or parentheses

# if has close and not group it is self


# auditCodeBase
# blank20
# config

# instructions





























