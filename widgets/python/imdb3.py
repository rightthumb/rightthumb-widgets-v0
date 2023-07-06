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
import simplejson as json
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
import _rightThumb._imdb as _imdb
# import _rightThumb._dir as _dir
# import _rightThumb._md5 as _md5
# import _rightThumb._mimetype as _mime

##################################################


from operator import itemgetter

from lxml import html
import requests
import cssselect

import webbrowser
import time

import datetime
import arrow

import pickle

##################################################


def appSwitches():
	_.switches.register('Input', '-i,-f,-file','file.txt')
	



_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
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

_.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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
	# _.switches.trigger('Input',_.formatColumns)
	_.switches.process()



if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()





def fieldSet(switchName,switchField,switchValue):
	_.switches.fieldSet(switchName,switchField,switchValue)

def setPipeData(data): 
	# _.appData[__.appReg]['pipe'] = list(data)
	if len(data) > 0:
		_.appData[__.appReg]['pipe'] = []
		for pd in sys.stdin.readlines():
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




_.appData[__.appReg]['pipe'] = ''
if not sys.stdin.isatty():
	_.appData[__.appReg]['pipe'] = sys.stdin.readlines()
	# pipeCleaner()



########################################################################

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

########################################################################################
# START




def action():
	focus()
	__.pipeData = _.appData[__name__]['pipe']
	if type(__.pipeData) == list:
		if _.switches.isActive('Movie'):
			if _.switches.isActive('Score'):
				for theLabel in __.pipeData:
					if not theLabel in __.omitFromMovies:
						# _.pr('   -   ',theLabel)
						imdbID = googleID(theLabel,'movie')
						__.cinema.rating(imdbID)
	else:
		imdbID = _.switches.value('Case')
		if not len(imdbID) > 0:
			if _.switches.isActive('Movie'):
				imdbID = googleID(_.switches.value('Movie'),'movie')
			if _.switches.isActive('Person'):
				imdbID = googleID(_.switches.value('Person'),'person')
		if not len(imdbID) > 0:
			_.pr('Google Error')
			sys.exit()
		if _.switches.isActive('Episode'):
			__.cinema.seasons(imdbID)
			# __.cinema.inSeason(imdbID)
		elif _.switches.isActive('SeasonStarts'):
			ssv = _.switches.value('SeasonStarts')
			# _.pr(ssv)
			ssvp = ssv.split(',')
			if len(ssvp) == 1:
				__.cinema.seasonsStarts(imdbID,ssvp[0])
			if len(ssvp) == 2:
				__.cinema.seasonsStarts(imdbID,ssvp[0],ssvp[1])
		else:
			if 'nm' in imdbID:
				# __.people.register(imdbID, False)
				__.people.register(imdbID, True)
			if 'tt' in imdbID:
				# __.cinema.register(imdbID, False)
				__.cinema.register(imdbID, True)

			# __.people.dump()
			# __.cinema.dump()


def loadObject(file):
	result = None
	with open(file, 'rb') as objThis:
		result = pickle.load(objThis)
	return result
focus()
_.appData[__name__]['pipe'] = ''

if not sys.stdin.isatty():
	_.appData[__name__]['pipe'] = []
	for pd in sys.stdin.readlines():
		# _.pr(pd)
		pd = pd.replace('\n','')
		if not pd == '':
			# _.pr(pd)
			_.appData[__name__]['pipe'].append(pd)
	try:
		if not _.appData[__.appReg]['pipe'][0][0] in _str.safeChar:
			_.appData[__name__]['pipe'][0] = _.appData[__name__]['pipe'][0][1:]
	except Exception as e:
		pass

# def timestamp():
#     return time.time()


# _.pr(type(__.pipeData))

__.aliases = _.getTable('imdb_aliases.json')
# _.pr(__.aliases)
# test = input('pause')
__.omitFromMovies = []
__.omitFromMovies.append('Scotty\'S 4Th Birthday 7 16 84')




########################################################################################
if __name__ == '__main__':
	action()






