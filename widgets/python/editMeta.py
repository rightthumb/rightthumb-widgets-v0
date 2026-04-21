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
# import requests
# import mutagen
from PIL import Image
import piexif
# import exif
# from exif._image import Image
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
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeFrontEnd' )
# _browser = _.regImp( __.appReg, '_rightThumb._toolsScrapeDirect' )
# import _rightThumb._date as _date
# import _rightThumb._dir as _dir
	# _.printVar( _dir.fileInfo( path ) )
# import _rightThumb._md5 as _md5
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

##################################################

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass
	# _.switches.register('Input', '-i,-f,-file','file.txt')
	# activate trigger in registerSwitches 
	



_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT'
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
						'p thisApp -file file.txt',
						''
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

# _.appInfo[focus()]['examples'].append('p thisApp -file file.txt')

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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# os.system('"' + do + '"')
########################################################################################
# START




def action():
	file = 'D:\\_Scott\\S_Pictures\\test.jpg'
	file2 = 'D:\\_Scott\\S_Pictures\\test3.jpg'

	im = Image.open(file)
	exif_dict = piexif.load(im.info["exif"])
	exif_dict['test'] = 'works'
	exif_bytes = piexif.dump(exif_dict)
	im.save(file2, "jpeg", exif=exif_bytes)
	_.printVar( exif_dict )


# def load():
#     global data
#     data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()


############################################

# type E:\index_dad_laptop.txt | p line +  *.jpg > %tmpf0%
# type %tmpf0% | p line + 1998 - AppData > %tmpf1%
# type %tmpf0% | p line + 1999 - AppData >> laptop_pics.txt

# done

############################################

# p lists -f1 %tmpf2% -f2 %tmpf3% > %tmpf4%

# type drive_e* | p line --c + FileName | p line --c -p ;' 3 > %tmpf2%

# p dir -cache archive\drive.cache -c n > %tmpf3%

# dir /s/b e:\*.jpg | p dir4 -save D:\Picture_Project\drive_e2.cache

# D:\Picture_Project\drive.cache
# D:\Picture_Project\drive_e1.cache
# D:\Picture_Project\drive_e2.cache

# type drive_e* | p line --c + md5 | p line --c -p ;' 3 > %tmpf2%
# type drive.cache | p line --c + md5 | p line --c -p ;' 3 > %tmpf3%
# p lists -f1 %tmpf2% -f2 %tmpf3% > %tmpf4%
# n %tmpf4%

############################################

# type %tmpf0% | p exif -folder D:\Picture_Project

# b Picture_Project
# type drive_e* | p line --c + md5 | p line --c -p ;' 3 > MD5.txt
# cd data
# cd laptop
# type drive* | p line --c + md5 | p line --c -p ;' 3 > MD5.txt
# cd..
# cd desktop
# type drive* | p line --c + md5 | p line --c -p ;' 3 > MD5.txt



# D:\Picture_Project\data\desktop\MD5.txt
# D:\Picture_Project\data\laptop\MD5.txt
# D:\Picture_Project\data\MD5.txt
# D:\Picture_Project\MD5.txt


# p lists -f1 D:\Picture_Project\MD5.txt -f2 D:\Picture_Project\data\laptop\MD5.txt > %tmpf4%
# n %tmpf4%
# p lists -f1 D:\Picture_Project\MD5.txt -f2 D:\Picture_Project\data\desktop\MD5.txt > %tmpf5%
# n %tmpf5%


############################################