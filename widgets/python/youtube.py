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
	_.switches.register( 'URLS', '-u,-url,-urls', 'https://www.youtube.com/watch?v=NGFToiLtXrod' )
	_.switches.register( 'AddNumber', '-n,-number,-cnt' )


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'youtube.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Downloads youtube video',
	'categories': [
						'youtube',
						'download',
						'internet',
				],
	'relatedapps': [
						# 'p another -file file.txt',
						'type  %tmpf2% | p youtubeSearch -official -song +close',
						'type %tmpf2% | a.playlist',
						'',
						'ymp3 "https://www.youtube.com/watch?v=8p4sXJ1UMRU" 01',
						'yAudio "https://www.youtube.com/watch?v=NGFToiLtXrod" & autoMP3 "cant_take_my_eyes_off_you"',
						'',
						'youtube https://www.youtube.com/watch?v=cGa3zFRqDn4',
						'youtube -F https://www.youtube.com/watch?v=cGa3zFRqDn4',
						'',
						'D:\\tech\\programs\\exe\\exe\\youtube-dl.exe  --help | + url',
						'youtube-dl -f best https://www.youtube.com/watch?v=hM68yc5nQyk',
						'youtube-dl -x --audio-format mp3 -f bestaudio https://www.youtube.com/watch?v=NGFToiLtXro',
						'youtube-dl --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=NGFToiLtXro',
						'youtube-dl --update',
						'',
						'h > %tmpf7% & type %tmpf7% | p patternInFolder -split "v=" 1 + youtube',
						'h > %tmpf7% & type %tmpf7% | p patternInFolder -split "v=" 1 + youtube | p line + youtube-dl watch - ">" --c',
						'',
						'youtube-dl -f bestaudio https://www.youtube.com/watch?v=hM68yc5nQyk',
						'ffmpeg -i "video.mp4" -codec:a libmp3lame -qscale:a 2 "output.mp3"',
						'',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p youtube -url https://www.youtube.com/watch?v=8p4sXJ1UMRU ',
						'',
						'type %tmpf1% | | p youtube -n ',
						'',
						'type %tmpf2% | p youtubeSearch -official -song +close -offset 0 | p youtube -n',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
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
# __.appRegPipe
########################################################################################
# START

def process( i, url ):
	if _.switches.isActive('AddNumber'):
		do = 'ymp3 "THE_URL" ' + _.fields.padZeros( 'cnt', 'val', i )
		# do = 'yAudio "THE_URL" & ppause & autoMP3 ' + _.fields.padZeros( 'cnt', 'val', i )
	else:
		do = 'ymp3 "THE_URL"'
		# do = 'yAudio "THE_URL" & autoMP3'
	do = do.replace( 'THE_URL', url )
	# do='yt-dlp --extract-audio --audio-format mp3 '+url
	os.system( '"' + do + '"' )

def action():
	_.fields.register( 'cnt', 'val', 7, m=2 )
	if _.switches.isActive('URLS'):
		if type( _.appData[__.appReg]['pipe'] ) == bool:
			_.appData[__.appReg]['pipe'] = _.switches.values('URLS')
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		cnt = 0
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			found = False
			url = None
			for x in row.split(' '):
				if 'http' in x   and ( 'youtube.com' in x or 'youtu.be' in x   ):
					url = x
			if not url is None:
				cnt+=1
				process( cnt, url )


# ymp3 "https://www.youtube.com/watch?v=8p4sXJ1UMRU" 01
# p pop_last   -string "01 Can't Take My Eyes off You - Frankie Valli and The 4 Seasons- delete this     .mp3" -p ;- .

########################################################################################
if __name__ == '__main__':
	action()






