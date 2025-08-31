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
	### EXAMPLE: START
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	_.switches.register( 'File', '-f,-file,-files','file.txt', description='Files' )
	### EXAMPLE: END


_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'popFile.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'folder of selected file',
	'categories': [
						'folder',
						'file',
						'tool',
						'nav',
						'navigate',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						'p cdf',
						'',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p popFile -f "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"',
						'p cdf -f "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"',
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
	### EXAMPLE: START
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	### EXAMPLE: END
	
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
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
########################################################################################
# START

def httpCheck(path):
	if path.startswith('https:') or path.startswith('http:'):
		url=path
		url=url.replace('https://www.','https://')
		if '?' in url: url=url.split('?')[0]
		sites=_.getTable('site-locations.list')
		for mPath in sites:
			if os.path.isfile(mPath):
				p = __.path(mPath,pop=True)
				if _.getText( mPath, raw=True ).strip().startswith('{'): meta = _.getTable2( mPath )
				else: meta = _.getYML( mPath )
				if 'url' in meta:
					u = meta['url'].replace('https://www.','https://')
					if url.startswith(u):
						x=url[len(u):].replace('/',os.sep)
						y=p+os.sep+x
						if os.path.isdir(y):
							test='index.php index.htm index.html'.split(' ')
							for t in test:
								yt=str(y+os.sep+t).replace(os.sep+os.sep,os.sep)
								if os.path.isfile(yt):
									y=yt
						y=y.replace(os.sep+os.sep,os.sep)
						if os.path.isfile(y):
							path=y
	return path


def action():
	# files=_.isData()
	# if _.switches.isActive('Files'):
	files=_.switches.values('File')
	for i,path in enumerate(files):
		# print(path);sys.exit()
		path=httpCheck(path)
		_.pr( __.path(path,pop=True) )



########################################################################################
if __name__ == '__main__':
	action()







