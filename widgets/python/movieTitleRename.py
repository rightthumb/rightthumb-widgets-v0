#!/usr/bin/python3
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
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'Size', '-size' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	


# _.autoBackupData = __.autoCreationConfiguration['backup']
_.autoBackupData = False
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'movieTitleRename.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate code to rename movies',
	'categories': [
						'rename',
						'file',
						'folder',
						'entertainment',
						'ent',
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
						'p folder --c | p movieTitleRename',
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
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



def removeStuff( line ):
	add = ''
	if '2160' in line:
		add = '(2160p)'
	elif '1080i' in line or '1080I' in line:
		add = '(1080i)'
	elif '1080p' in line or '1080P' in line or '1080' in line:
		add = '(1080p)'
	elif '720i' in line or '720I' in line:
		add = '(720i)'
	elif '720p' in line or '720P' in line or '720' in line:
		add = '(720p)'
	elif 'x264' in line.lower():
		add = '(x264)'
	elif 'bluray' in line.lower():
		add = '(BluRay)'
	elif 'dvd' in line.lower():
		add = '(dvd)'
	elif 'hd' in line.lower():
		add = '(HD)'
	if not _.switches.isActive('Size'):
		add = ''



	stuff = [

				'[',
				']',
				')',
				'(',
				'. .',
				'WEBRip',
				'AAC',
				'5.1',
				'YTS.MX',
				'YTS.LT',
				'512Kb',
				'2160p',
				'2160P',
				' MULTI ',
				' HDTV',
				'_track',
				'BluRay',
				'BluRay',
				'HDCLUB',
				'HDRip',
				'720p',
				'1080p',
				'1080P',
				'x264',
				'HD-TS',

				'WwW SeeHD PL',
				'WwW SeeHD',
				'NEW',
				'new',
				'New',
				'WEB-DL',
				'WEB-DLRip',
				'46Gb',
				'Rip 1  Line MegaPeer',
				'P TS',
				'E:\\MOVIES'+_v.slash,
				'dvdrip',
				'xvid',
				'kinokopilka',
				' www ',
				' dvdrip ',
				' Hmark ',
				' Dvdrip ',
				'Xvid',
				'Bgaudio',
				'Siso',
				'-',
				'"',
				'Dvdrip',
				'Brrip',
			]
	for s in stuff:
		line = line.replace(s,' ')
		line = line.replace(s.replace( ' ','' ),' ')
		line = line.replace(s.upper(),' ')
		line = line.replace(s.lower(),' ')
		line = line.replace(s.title(),' ')
	line = _str.cleanBE(line,' ')
	line = line.replace( '.20', ' 20' )
	line = line.replace( '.19', ' 19' )
	line = line.replace( '_', ' ' )
	line = _str.replaceDuplicate( line, ' ' )
	line = line.replace( '. .', '' )
	line = line.replace( ' .', '.' )
	line = _str.cleanBE(line,' ')
	global extensionList
	# print( extensionList )
	# sys.exit()
	hasExt = ''
	# print( extensionList )
	for xt in extensionList:
		if xt.upper() in line:
			hasExt = xt
		if xt in line:
			hasExt = xt
		line = line.replace( xt.upper(), xt )
		line = line.replace( ' '+xt, xt )
		if add:
			line = line.replace( xt, ' '+add+''+xt )
	line = line.replace( hasExt, '' )
	line = line.replace( '.', ' ' )
	line = _str.cleanBE(line,' ')
	line = line + '.'+hasExt
	line = line.replace( '..', '.' )
	if add and not hasExt:
		line = line + ' '+add
	line = _str.replaceDuplicate( line, ' ' )
	# line = line.replace( '  ', ' ' )
	line = _str.cleanBE(line,' ')
	return line


def action():
	extensionsDatabank()
	# _copy = _.regImp( __.appReg, '-copy' )
	# _copy.imp.copy(  )

	# _movieTitle = _.regImp( __.appReg, 'movieTitle' )
	# _movieTitle.switch( 'JustVar' )
	# import movieTitle

	for i,row in enumerate( _.isData(r=1) ):
		row = _str.cleanBE(row,' ')
		# _movieTitle.imp.pipeData = []
		# _movieTitle.imp.pipeData.append(row)
		# _movieTitle.action()
		# m = movieTitle.theTitle

		m = removeStuff(row)
		if _.switches.isActive('Test'):
			print()
			print(row)
			print(m)
			print()
		else:
			if _.isWin:
				print( 'rename '+ '"'+row+'"'  +'   '+ '"'+m+'"' )
			else:
				print( 'mv '+ '"'+row+'"'  +'   '+ '"'+m+'"' )



def extensionsDatabank():
	global extensionList
	extensionList = []
	_db = _.regImp( __.appReg, 'databank' )
	_db.switch( 'JustReturn' )
	_db.switch( 'Tables', [ 'file', 'extensions' ] )

	for index in ['video']:
		_db.switch( 'Plus', [index] )
		for i,x in enumerate(_db.do( 'action' )):
			x = x.replace('.','')
			if not x.startswith('.'):
				x = '.'+x
			if not x in extensionList:
				extensionList.append( x.lower() )



########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()




