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
	_.switches.register( 'Indices', '-i,-index,-indexes,-indices,-f,-file,-files','file.index',  isRequired=True )


_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'word_stem_indices.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Query indices of saved word stems',
	'categories': [
						'word',
						'stem',
						'wordstem',
						'word_stem',
						'query',
						'index',
						'indices',
						'research',
						'project',
						'simpleList',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'p simpleList ?',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p word_stem_indices -i simpleList.tiktok + develop interviewer intelligence manager',
						'',
						'p word_stem_indices -i simpleList.tiktok',
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

processWordStem = None
index_of_word_stems = {}
def wordStem(word):
	global processWordStem
	global index_of_word_stems
	if processWordStem is None:
		import nltk
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		processWordStem = PorterStemmer()
	stem = processWordStem.stem(word)
	if not stem in index_of_word_stems:
		index_of_word_stems[stem] = {}
	index_of_word_stems[stem][word] = {}
	return stem

def action():
	table = []
	for file in _.switches.values('Indices'):
		original = file
		data = _.getTableProject( 'nltk.word_stems', file )
		if not data:
			if not '.index' in file:
				file += '.index'
			data = _.getTableProject( 'nltk.word_stems', file )
		if not data:
			_.colorThis(  [ 'No Data, try: simpleList.'+original ], 'red'  )
			sys.exit()
		if _.switches.isActive('Plus'):
			for search in _.switches.values('Plus'):
				search = wordStem(_.ci(search))
				q = None
				if search in data:
					q = search
				elif _.ci(search) in data:
					q = _.ci(search)
				elif wordStem(_.ci(search)) in data:
					q = wordStem(_.ci(search))
				elif wordStem(search) in data:
					q = wordStem(search)
				if not q is None:
					table.append({ 'index': file, 'stem': q, 'words': ', '.join(list( data[q].keys()  )) })
		else:
			for key in data:
				if len( data[key] ) > 1:
					table.append({ 'index': file, 'stem': key, 'words': ', '.join(list( data[key].keys()  )) })
	_.switches.fieldSet( 'GroupBy', 'active', True )
	_.switches.fieldSet( 'GroupBy', 'value', 'index' )
	_.switches.fieldSet( 'Sort', 'active', True )
	_.switches.fieldSet( 'Sort', 'value', 'index,stem' )
	_.tables.register( 'data', table )
	_.tables.print( 'data', 'index,stem,words' )

########################################################################################
if __name__ == '__main__':
	action()




