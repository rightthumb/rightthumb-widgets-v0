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
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################

# from lxml import html
# import requests
# import cssselect

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	_.switches.register('Alpha', '-alpha')
	_.switches.register('Unique', '-u,-unique')
	_.switches.register('MinLength', '-min','2')
	_.switches.register('Stemming', '-stem')
	_.switches.register('PartsOfSpeech', '-speech')
	_.switches.register('Clean', '--c')
	



_.appInfo[focus()] = {
	'file': 'words.py',
	'description': 'Output individual words',
	'categories': [
						'research',
						'text manipulation',
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

_.appInfo[focus()]['examples'].append('p words -i %tmpf0% | p sortthis | p counteach ')
_.appInfo[focus()]['examples'].append('type %tmpf0% | p words | p sortthis | p counteach ')

# _.appInfo[focus()]['columns'].append({'name': 'name', 'abbreviation': 'n'})





def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:
		_.argvProcess = True
		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()
	_.defaultScriptTriggers()
	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
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

def setPipeData(data):
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in data:
			pd = pd.replace('\n','')
			if not pd == '':
				_.appData[__.appReg]['pipe'].append(pd)

def pipeCleaner():
	if len( _.appData[__.appReg]['pipe'] ):
		if type( _.appData[__.appReg]['pipe'][0] ) == str:
			if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
				_.appData[__.appReg]['pipe'][0] = _.appData[__.appReg]['pipe'][0][1:]
			for i,pipeData in enumerate(_.appData[__.appReg]['pipe']):
				_.appData[__.appReg]['pipe'][i] = _.appData[__.appReg]['pipe'][i].replace('\n','')




_.appData[__.appReg]['pipe'] = False
if not sys.stdin.isatty():
	setPipeData( sys.stdin.readlines() )
	# _.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################################

# def processFolder(folder, qID):
# __.queueLastActivity = time.time()
# __.projectData[focus()][__.pdID[focus()]].append( obj )
# _.threads.add( 'test', testFunction, [{'two':item}], kwargs=True )
# _.threads.add( 'process_folder', processFolder, [ path ] )
# _.threads.spent( qID, sys.getsizeof( 'obj') )
					################
# _.threads.add( 'test', trigger=complete, triggerArg={'hello','test'}, loaded=False )
# _.threads.add( 'test', trigger=complete, triggerArg=({'two': 'hi'}), loaded=False ) # kwargs 
# _.threads.maxThreadsSafe = 250
# _.threads.report = True
# _.threads.projectDataFileSQL = db
# _.threads.auditPrint = False

##################

# _.appData[focus()]['uuid'] = {  'app': _.appInfo[focus()]['file'], 'project': 'app_instance' }
# _.appInfo[focus()]['instance'] = _.genUUID()
# # _.appData[focus()]['audit'].append( { 'start': True, 'note': '', 'entire': True, 'function': sys._getframe().f_code.co_name, 'app': _.appInfo[focus()]['file'], 'timestamp': time.time(), 'uuid': '' } );

# _dir.sqlCreateTable( db, deleteDBFirst=True, close=True )
# obj = _dir.fileInfo( path, sql=True )
# _.pr(   _dir.fileInfo( _.switches.value('Input') )['size']   )

# _.saveLog('queue')
# _.saveLog('audit')

########################################################################

# os.path.isfile(files)
# os.system('cls')

# _.switches.isActive('_File_')
# global

# _.appInfo[focus()]['categories']

# #######################################
# uuidProject = { 'input': _.switches.value('Input'), 'note': 'sample' }
# _.appData[__.appReg]['uuid'] = {  'app': _.appInfo[__.appReg]['file'], 'project': uuidProject }
# _.genUUID(project='')
# _.genUUID('temp file')
# _.genUUID({'file':'app.py'})
# #######################################
# import blank
# blank.focus(focus())
# blank.registerSwitches()
# _.switches.fieldSet('Input','active','one')
# _.switches.fieldSet('Input','value','one')
# focus()
# #######################################

# _.switches.fieldSet('_File_','active',True)

# _.switches.dumpSwitches(includeBlank=False)

# _.tables.register('childClassItems',childItems)
# _.tables.fieldProfileSet('Auto','timestamp','trigger',_.float2Date)
# _.tables.print('childClassItems','name')

# backupLog = _.tables.returnSorted( 'backupLog', 'd.timestamp', _.getTable('fileBackup.json') )

# _mime.isText(file)
# _mime.isBinary(file)

# books = _.getText(_v.myTables + '\\bible_books.csv')
# _.saveText(convertedFile,'file.txt')

# json = _.getTable('base64Key.json')
# _.saveTable(jsonFile,'file.json')
# _.saveTable( jsonFile, 'file.json', printThis=True )

# _.showLine(item)
# _.showLine( string, plus = '', minus = '', plusOr = False )

# if not type(_.appData[__.appReg]['pipe']) == str:
# os.system('"' + do + '"')

########################################################################################
# START
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize
def action():
	data = []
	speech = {}
	index = {}
	count = {}

	newSpeech = {}
	newSpeechParts = {}
	count_percentage = {}
	raw = []
	
	omit = _.getTable( 'dic_omit.json' )
	if _.switches.isActive('Stemming'):
		_.switches.fieldSet( 'Unique', 'active', True )
		_.switches.fieldSet( 'Alpha', 'active', True )
		if not _.switches.isActive('MinLength'):
			_.switches.fieldSet( 'MinLength', 'active', True )
			_.switches.fieldSet( 'MinLength', 'value', 2 )

	if _.switches.isActive('Input'):
		tmp = []
		for f in _.switches.value('Input').split(','):
			for row in _.getText( f ):
				tmp.append( row )
		setPipeData( tmp )
		del tmp

	if not type( _.appData[__.appReg]['pipe'] ) == bool:


		if _.switches.isActive('PartsOfSpeech'):
			import nltk
			from nltk.stem import PorterStemmer
			from nltk.tokenize import word_tokenize
			ps = PorterStemmer()

			for row in _.appData[__.appReg]['pipe']:
				row = row.replace( '"', ' ' )
				row = _str.stripNonAlphaNumaric( row )

				tex = word_tokenize(row)
				for token in tex:
					subject_speech = nltk.pos_tag([token])

					# _.pr( subject_speech[0][0] )
					# sys.exit()
		
					


					keep = True
					for x in subject_speech[0][0]:
						if not x in _str.alphaChar:
							keep = False


					if keep:
						if _.switches.isActive('MinLength'):
							if not len(subject_speech[0][0]) >= int(_.switches.value('MinLength')):
								keep = False
					if keep:
						theStem = ps.stem( subject_speech[0][0] )


						# sys.exit()
						try:
							speech[ theStem +'_'+ subject_speech[0][1] ] += 1
						except Exception as e:
							speech[ theStem +'_'+ subject_speech[0][1] ] = 1

	






		for row in _.appData[__.appReg]['pipe']:
			row = row.replace( '"', ' ' )
			row = _str.stripNonAlphaNumaric( row )
			row = row.lower()
			for w in row.split(' '):
				keep = True
				if _.switches.isActive('Alpha'):
					good = True
					for x in w:
						if not x in _str.alphaChar:
							good = False

					if not good:
						keep = False

				if keep and len(w):

					if _.switches.isActive('MinLength'):
						if not len(w) >= int(_.switches.value('MinLength')):
							keep = False

					if keep:
						if w in omit.keys():
							keep = False

					if keep:
						data.append( w )

	
	raw = data

	if _.switches.isActive('Unique'):
		data = list(set(data))

	if not _.switches.isActive('Stemming'):
		for w in data:
			_.pr(w)
		if not _.switches.isActive('Clean'):
			_.colorThis( [ '\n', len(data), 'words' ], 'yellow' )
		return data

	else:
		from nltk.stem import PorterStemmer
		from nltk.tokenize import word_tokenize
		
		ps = PorterStemmer() 
		
		# choose some words to be stemmed 
		words = raw
		
		# index = {}
		# count = {}
		for w in words:
			theStem = ps.stem(w)
			index[w] = theStem
			if theStem in count.keys():
				count[theStem] += 1
			else:
				count[theStem] = 1



		newSpeech = {}
		newSpeechParts = {}
		for k in sorted(speech):
			newSpeech[k] = speech[k]
			newSpeechParts[ k.split('_')[0] ] = []
		for k in sorted(speech):
			newSpeechParts[ k.split('_')[0] ].append( k.split('_')[1] )
			
		if not _.switches.isActive('Clean'):
			_.printVar1( index )
			_.printVar1( count )
			_.printVar1( newSpeech )
			# _.printVar1( newSpeechParts )


		



		count_percentage = {}
		for k in count.keys():
			count_percentage[k] = _.percentageDiffInt( count[k] , len(raw) )

			# 
		return { 'words': data, 'stems': count, 'speech': newSpeech, 'parts': newSpeechParts, 'words_cnt': len(raw), 'words_cnt_unique': len(data), 'percentage': count_percentage }
		pass


# words
########################################################################################
if __name__ == '__main__':
	action()






