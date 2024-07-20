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
# import simplejson as json
# import shutil

import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str

_.switches.register('Songs', '-songs')
_.switches.register('Song', '-song')

_.appInfo=    {
	'file': 'done.py',
	'description': 'Changes the world',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

_.appInfo['examples'].append('p done -song 19')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})


_.switches.process()


# pipeData = ''

# if not sys.stdin.isatty():
#     pipeData = sys.stdin.readlines()
#     try:
#         if pipeData[0][0].isalnum() == False:
#             pipeData[0] = pipeData[0][1:]
#     except Exception as e:
#         pass

########################################################################################
def action():


	if not 'ta' in _v.fig:
		return False
	else:
		_v.fig['mp3'] = _v.fig['ta']+'mp3\\'
	

	songs = []
	# songs.append("tapeatalk_records"+_v.slash+"Time lord treachery.mp3")
	songs.append("Katherine Jenkins"+_v.slash+"2011 - Daydream"+_v.slash+"13. Abigail's Song (Bonus Track).mp3")
	songs.append("Ludovico Einaudi"+_v.slash+"Ludovico Einaudi - Nuvole Bianche.mp3")
	songs.append("Andrea Bocelli"+_v.slash+"Romanza - Andrea - Bocelli - Say Goodbye.mp3.mp3")
	songs.append("Jewel"+_v.slash+"Misc"+_v.slash+"(Jewel) - Foolish Games.mp3")
	songs.append("Less Than Jake"+_v.slash+"Hello Rockview"+_v.slash+"01. Last One Out of Liberty City.mp3")
	songs.append("louis_armstrong_-_somewhere_over_the_rainbow.mp3")
	songs.append("My Chemical Romance"+_v.slash+"My Chemical Romance - Im Not Okay (I Promise) (1).mp3")
	songs.append("Saved"+_v.slash+"George Strait - All My Ex's Live In Texas.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Soft"+_v.slash+"3. Today.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Soft"+_v.slash+"13. Luna.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Soft"+_v.slash+"2. Tonight, Tonight.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Soft"+_v.slash+"14. For Martha.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Hard"+_v.slash+"6. Disarm.mp3")
	songs.append("Smashing Pumpkins"+_v.slash+"Hard"+_v.slash+"4. Hummer.mp3")
	songs.append("The Cranberries"+_v.slash+"Cranberries - Linger.mp3")
	songs.append("The Cranberries"+_v.slash+"The Cranberries - Zombie.mp3")
	songs.append("Slick Shoes"+_v.slash+"Rusty"+_v.slash+"Slick Shoes - Cliche.mp3")
	songs.append("Slick Shoes"+_v.slash+"Rusty"+_v.slash+"Slick Shoes - Feeble.mp3")
	songs.append("Metalica"+_v.slash+"Fuel - Metallica [HD] [1080p].mp3")
	songs.append("Metalica"+_v.slash+"Metallica - Fade to Black.mp3")
	songs.append("Metalica"+_v.slash+"Metallica - Sad But True [Official Music Video].mp3")
	songs.append("Metalica"+_v.slash+"Metallica - The Unforgiven (Video).mp3")



	# mplayer = 'C:"+_v.slash+"Program Files (x86)"+_v.slash+"Windows Media Player"+_v.slash+"wmplayer.exe'
	# mplayer = _v.techDrive + ':"+_v.slash+"techApps"+_v.slash+"VLCPortable"+_v.slash+"VLCPortable.exe'
	mplayer = _v.techDrive + ':'+_v.slash+'techApps'+_v.slash+'XMPlayPortable'+_v.slash+'XMPlayPortable.exe'
	# if not os.path.isfile( mplayer ):
	#     mplayer = _v.techDrive + ':"+_v.slash+"techApps"+_v.slash+"VLCPortable"+_v.slash+"VLCPortable.exe'
	
	# mFolder = 'D:"+_v.slash+"_Scott"+_v.slash+"S_Music'
	mFolder = _v.appsFolder+_v.slash+'MP3'
	print(mFolder)
	# if not os.path.isdir( mFolder ):
	#     mFolder = _v.techDrive + ':"+_v.slash+"techApps"+_v.slash+"MP3'

	play = False

	if not _.switches.isActive('Songs') and not _.switches.isActive('Song'):
		play = True
		song =  _v.fig['mp3']+songs[18]

	if _.switches.isActive('Songs'):
		i = 0
		for s in songs:
			print(i, '\t', s)
			i += 1

	if _.switches.isActive('Song'):
		play = True
		song =  _v.fig['mp3']+songs[int(_.switches.value('Song'))]



	if play:
		theSong = mFolder + _v.slash + song
		
		theSong = "D:\\techApps\\MP3\\Metalica\\Fuel - Metallica [HD] [1080p].mp3"

		mplayerQ = '"' + mplayer + '"'
		theSongQ = '"' + theSong + '"'

		# print( 'start ' + mplayerQ + ' ' + theSongQ )
		# sys.exit()
		
		os.system('start ' + mplayerQ + ' ' + theSongQ)
	# print(mplayerQ)
########################################################################################
if __name__ == '__main__':
	action()





