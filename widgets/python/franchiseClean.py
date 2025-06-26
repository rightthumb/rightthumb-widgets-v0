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

# _nd = _.regImp( __.appReg, 'fileNameDate' )
#     _nd.pipe( [databaseFile] )
#     _nd.do( 'action' )

# _textIndex = _.regImp( __.appReg, 'words' )
	# _textIndex.switch( 'Alpha' )
	# _textIndex.switch( 'Unique' )
	# _textIndex.switch( 'MinLength', 2 )
	# _textIndex.switch( 'Stemming' )
	# _textIndex.switch( 'PartsOfSpeech' )
	# _textIndex.switch( 'Clean' )
	# _textIndex.pipe( data )
#     index = _textIndex.do( 'action' )

# _bm = _.regImp( __.appReg, 'bookmarks' )
	# index = _bm.imp.index()
# _dirList = _.regImp( __.appReg, 'dirList' )
#     _dirList.switch( 'Files' )
#     _dirList.switch( 'Recursion' )
#     _dirList.switch( 'Binary' )
#     _dirList.switch( 'Path','D:\\Apps' )
#     files = _dirList.do( 'action' )

# import _rightThumb._profileVariables as _profile
#     profile = _profile.records.audit( 'name', asset )
# import _rightThumb._encryptString as _blowfish
	# _blowfish.genPassword()
	# _blowfish.genPassword( 'string' )
	# en = _blowfish.encrypt( string )
	# de = _blowfish.decrypt( en )
# import _rightThumb._encryptFile as _blowfish
#     _blowfish.encrypt( infilepath, outfilepath, key )
#     _blowfish.decrypt( infilepath, outfilepath, key )
# _browserX = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )

# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
#     _browser.imp.project.open( url )
#     code = _.getText( _v.myAppsJs + '\\Church_Directory.js' )
#     _browser.imp.project.jqueryInject()
#     _browser.imp.project.inject( code )
#     while not _browser.imp.project.injectReturn('return window.taskComplete;'): pass
#     data =_browser.imp.project.injectReturn( 'window.hack.acquire.payload()' )
#     _browser.imp.project.close()

# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _hash
#     .file .string .bin  ( data, h )
#     md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 shake_128 shake_256

# import _rightThumb._mimetype as _mime

# import _rightThumb._backupLog as _bkLog
# _bkLog = _.regImp( __.appReg, '_rightThumb._backupLog' )

# import _rightThumb._auditCodeBase as _code
# _code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
# _omit = _.regImp( __.appReg, 'omitTable' )
	# _omit.imp.inTable( 'the' )
# _inDic = _.regImp( __.appReg, 'inDic' )
	# _inDic.switch( 'All' )
	# _inDic.imp.testAll( 'fight' )
	# _inDic.imp.testOne( 'austen' )
# _file_folder = _.regImp( __.appReg, 'file_folder' )
#     _file_folder.switch( 'Save,Clean' )
#     _file_folder.switch( 'Compair,Clean' )
#     _file_folder.switch( 'Folder', '' )
# _fileNameDate = _.regImp( __.appReg, 'fileNameDate' )
#     _fileNameDate.imp.newName( filename )
#     _fileNameDate.imp.newName( filename, _dir.fileInfo( filename ) )
# _filePathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
	# _filePathPatterns.switch( 'NoPrint' )
	# _filePathPatterns.switch( 'Files', _.switches.value( 'Files' ) )
	# folderReport = _filePathPatterns.action()
# fileBackup = _.regImp( __.appReg, 'fileBackup' )
#     fileBackup.switch( 'Input', filename )
#     fileBackup.switch( 'Flag', 'pre replaceText' )
#     recoveryFile = fileBackup.do( 'action' )
# _folderContent = _.regImp( __.appReg, 'file' )
#     _folderContent.switch( 'Silent' )
#     _folderContent.switch( 'Folder', _v.myAppsBatch )
#     _folderContent.switch( 'NoExtension' )

#     _folderContent.switch( 'Recursive' )

#     _folderContent.switch( 'Text' )
#     _folderContent.switch( 'Binary' )
#     _folderContent.switch( 'Label', 'App: ' )
#     _folderContent.switch( 'Prefix', ';t' )
#     files = _folderContent.do( 'action' )['files']
#     folders = _folderContent.do( 'action' )['folders']
# _tickets = _.regImp( __.appReg, 'ticketTimeline' )
#     _tickets.switch( 'ReturnFiles' )
#     records = _tickets.do( 'records' )
##################################################

def appSwitches():
	pass
	_.switches.register( 'Franchise', '-f,-franchise', isRequired=True )
	_.switches.register( 'MustInclude', '-i,-include', isRequired=True )


	# _.switches.documentation( 'Test', { 
	#                                     'examples': [
	#                                                     '',
	#                                                 ],

	#                                     'required': [],
	#                                     'related': [],
	#                                     'isRequired': False,
	#                                 } )


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'franchiseClean.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Manage entertainment franchise databases',
	'categories': [
						'franchise',
						'entertainment',
						'movie',
						'movies',
						'tv',
						'tv shows',
						'shows',
						'movie drive',
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
						'p franchiseClean -f underworld -include date title',
						''
	],
	'columns': [
					{ 'name': 'date', 'abbreviation': 'd,y,year' },
					{ 'name': 'title', 'abbreviation': 't,n,l,name,label' },
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'MustInclude', _.formatColumns )
	
	
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START



def action():
	global franchises
	global labels
	load()

	_.switches.fieldSet( 'Plus', 'active', True )
	_.switches.fieldSet( 'Plus', 'value', _.switches.value('Franchise') )
	_.switches.fieldSet( 'Plus', 'values', _.switches.values('Franchise') )

	_.switches.fieldSet( 'Long', 'active', True )


	# if 'title' in _.switches.values('MustInclude'):
	#     _.pr( 'here' )

	# sys.exit()

# franchise
#     <class 'float'> date_acquired
#     <class 'float'> epoch
#     <class 'str'> date
#     <class 'str'> label
#     <class 'list'> aliases
#     <class 'list'> parts
#     <class 'list'> movieIDS
#     <class 'list'> peopleIDS
#     <class 'list'> movies
#     <class 'list'> list

# franchise['movies']
#     <class 'str'> imdbID
#     <class 'str'> year
#     <class 'str'> name
#     <class 'str'> link
#     <class 'int'> people

# for x in movie.keys(): _.pr( type(movie[x]), x );
	if platform.system() == 'Windows':
		os.system( 'cls' )
	else:
		os.system( 'clear' )
	_.pr()

	for i,franchise in enumerate(franchises):
		if _.showLine( franchise['label'] ) or _.showLine( str(franchise['aliases']) ):
			_.colorThis( [ '\n', franchise['label'] ], 'yellow' )
			# _.pr( franchise['movieIDS'] )
			# sys.exit()
			removeIDs_movies = []
			removeIDs_people = []
			for movie in franchise['movies']:
				if 'date' in _.switches.values('MustInclude') and movie['year'] == '':
					if not movie['imdbID'] in removeIDs_movies:
						removeIDs_movies.append( movie['imdbID'] )
				if 'title' in _.switches.values('MustInclude') and not _.showLine( movie['name'] ):
					if not movie['imdbID'] in removeIDs_movies:
						removeIDs_movies.append( movie['imdbID'] )
			if len(removeIDs_movies):

				newMovies = []
				newMoviesIDs = []
				delete_these_movies = []
				for movie in franchise['movieIDS']:
					if not movie in removeIDs_movies:
						newMoviesIDs.append(movie)

				for movie in franchise['movies']:
					if not movie['imdbID'] in removeIDs_movies:
						newMovies.append(movie)
					else:
						delete_these_movies.append( movie )

				franchises[i]['movieIDS'] = newMoviesIDs
				franchises[i]['movies'] = newMovies

				

				_.colorThis( [ '\nKeep:' ], 'green' )
				t = '    '
				t = ''
				_.tables.register( 'keep', newMovies, t=t )
				_.tables.print( 'keep', 'imdbID,year,name' )
				_.colorThis( [ '\nDelete:' ], 'red' )
				_.tables.register( 'delete', delete_these_movies, t=['del =>        ','red'] )
				_.tables.print( 'delete', 'imdbID,year,name' )


				pass
				if len(delete_these_movies) == 1:
					question = 'Remove this 1 item? '
				else:
					question = 'Remove these '+str(len(delete_these_movies))+' items? '

				ask = ''
				ask = input( '\n '+question )
				if 'y' in ask.lower():
					_.saveTable( franchises, 'imdb_franchises_NEW.json' )

				

				
def load():
	global franchises
	global labels
	franchises = _.getTable( 'imdb_franchises_NEW.json' )
	labels = _.getTable( 'imdb_franchise_display.json' )



labels = []
franchises = []

########################################################################################
if __name__ == '__main__':
	action()



0



