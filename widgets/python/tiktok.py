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
	_.switches.register( 'Files', '-f,-file,-files','%tiktok%', isPipe=True, isRequired=True, description='Files' )
	_.switches.register( 'Records', '-records' )
	_.switches.register( 'Labels', '-labels' )
	_.switches.register( 'Count', '-cnt,-count' )
	_.switches.register( 'Done', '-done' )
	_.switches.register( 'Organize', '-organize' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'tiktok.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'tiktok notes tool',
	'categories': [
						'tiktok',
						'notes',
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
						'type %tiktok% | p tiktok ',
						'type %tiktok% | p tiktok + tech',
						'type %tiktok% | p tiktok + tech -records',
						'',
						'type %tiktok% | p tiktok -done',
						'',
						'type %tiktok% | p tiktok -organize',
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START

def process(row):
	global complete
	global data
	global last
	global lastRow
	if ':' in row and not 'http' in row.lower():
		last = row
	else:
		if 'tiktok' in row and 'http' in row.lower():
			if not last in data:
				data[last] = []
			data[last].append(row)
		else:
			# if True:
			# if len(row):
			if not len(row) and lastRow == '':
				pass
			else:
				if not last in complete:
					complete[last] = []
				complete[last].append(row)
				lastRow = row
	# _.pr(row)

def wordStem(word):
	global processWordStem
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	return processWordStem.stem(word)


def wordsBuild(key):
	global omit
	global words
	keyX = key.split(':')[0].lower()
	
	keyY = ''
	for p in keyX:
		if p in _str.alphaChar+'_- ':
			keyY += p

	keyY = keyY.replace( '\t', ' ' )
	keyY = _str.replaceDuplicate( keyY, ' ' )
	keyY = _str.cleanBE( keyY, ' ' )


	for part in keyY.split(' '):
		stem = wordStem(part)
		stem = stem.replace(' ','')
		if not stem in omit and len(stem) and len(stem) > 1:
			
			if not stem in words:
				words[stem] = []
			words[stem].append(key)

def action():
	global complete
	global data
	global words
	if platform.system() == 'Windows':
		os.system('CLS')
	else:
		os.system('clear')
	load()
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		# _.pipeCleaner(0)
		# _.printVar( _.appData )
		file = ''.join( _.appData[__.appReg]['pipe'] )
		for i,row in enumerate( file.split('\n') ):
			process(row)



	if _.switches.isActive('Done'):

		for key in complete:
			if _.showLine(key):
				_.colorThis(  [  '\n', key  ], 'yellow'  )
				for text in complete[key]:
					hasEstrogen = False
					for x in _.internet_domains(text):
						hasEstrogen = True
						text = text.replace( x, _.colorThis( x, 'green', p=0 ) )
					if True:
						text = text.replace( ' x ', _.colorThis( ' x ', 'cyan', p=0 ) )
						text = text.replace( ' o ', _.colorThis( ' o ', 'purple', p=0 ) )
					_.wrapText(  '    '+ text, scan=[ 'Progesterone','Estrogen' ], bold='green'  )
					# _.colorThis(  [  '\t', url  ], 'green'  )

		sys.exit()

	if _.switches.isActive('Labels'):
		for key in data:
			if _.showLine(key):
				_.pr( key )
		sys.exit()



	if _.switches.isActive('Count') or not _.switches.isActive('Plus'):
		for key in data:
			wordsBuild(key)

		table = []
		for i,key in enumerate(words):
			records = 0
			for x in words[key]:
				records += len( data[x] )
			table.append({ 'id': i, 'length': len( words[key] ), 'stem': key, 'keys': words[key], 'records': records })

	if _.switches.isActive('Count'):
		cnt = int( _.switches.value('Count') )
		i=0
		for record in table:
			if record['records'] == cnt:
				i+=1
				_.pr()
				_.pr()
				_.pr(i)
				_.colorThis(  [  record['stem']  ], 'yellow'  )
				for key in record['keys']:
					_.colorThis(  [  '\t', key, ' '.join( data[key] )  ], 'green'  )


		sys.exit()



	if not _.switches.isActive('Plus'):



		theTable = _.tables.returnSorted( 'table', 'd.records', table )

		if _.switches.isActive('Organize'):

			spent = []
			for rec in theTable:
				first = True
				# _.colorThis(  [  '\n', rec['stem']  ], 'cyan'  )
				for key in rec['keys']:
					if not key in spent:
						spent.append(key)
						if first:
							first = False
							_.colorThis(  [  '\n___\n'  ], 'red'  )
						_.colorThis(  [  '\n\t', key  ], 'yellow'  )
						for url in data[key]:
							_.colorThis(  [  '\t\t', url  ], 'green'  )

			# sys.exit()


		_.tables.print( 'table', 'records,stem' )
	elif _.switches.isActive('Plus'):
		if not _.switches.isActive('Records'):
			for key in data:
				if _.showLine(key):
					_.colorThis( key.replace(':',''), 'yellow' )
		elif _.switches.isActive('Records'):
			for key in data:
				if _.showLine(key):
					_.pr()
					_.pr()
					_.colorThis( key.replace(':',''), 'yellow' )
					for x in data[key]:
						_.colorThis( [  '\t', x  ], 'green' )



def load():
	global omit
	omit = list( _.getTableDB( 'dic_omit.json' ).keys() )


omit = None
data = {}
last = ''
lastRow = ''
words = {}
processWordStem = None
complete = {}


########################################################################################
if __name__ == '__main__':
	action()







