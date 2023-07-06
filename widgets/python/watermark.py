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

import os, sys, time
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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', description='Files' )
	_.switches.register( 'Folders', '-folder,-folders' )
	_.switches.register( 'Recursive', '-folder,-folders' )

_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs'] 
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'watermark.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'add watermark to code',
	'categories': [
						'watermark',
						'code',
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
						_.hp('p thisApp -file file.txt'),
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

def process(path):
	comment=''
	if path.endswith('.py'):
		comment = '#'
	elif path.endswith('.sh'):
		comment = '#'
	elif path.endswith('.bat'):
		comment = 'rem'
	elif path.endswith('.js'):
		comment = '//'
	elif path.endswith('.php'):
		comment = '//'

	if len(comment) and os.path.isfile(path):
		global watermark
		watermark_lines = []
		for item in watermark.split('\n'):
			# item = _str.cleanBE(item,' ')
			watermark_lines.append(item)
		file=_.getText(path, raw=True)
		if file is None or not '\n' in file:
			return None
		s = '## {R2D291''9B742E} ##'
		e = '## {C3P0D4'+'0fAe8B} ##'
		if not s in file:
			new_file = ''
			for i,line in enumerate(file.split('\n')):
				if i == 1:
					new_file += '\n'
					new_file += comment+' '+s + '\n'
					for a in watermark_lines:
						new_file += comment+' '+ a + '\n'
					new_file += comment+' '+e + '\n'
					new_file += '\n'
				new_file += line + '\n'
			_.saveText( new_file, path )
			_.cp(path,'cyan')
			return None
			



		active=False
		wasActive=False
		new_file = ''
		for line in file.split('\n'):
			if s in line:
				active=True


			if not active:
				new_file += line + '\n'

			if e in line:
				new_file += comment+' '+s + '\n'
				for a in watermark_lines:
					new_file += comment+' '+a + '\n'

				new_file += comment+' '+e + '\n'
				active=False
				wasActive=True
		if not new_file == file:
			_.saveText( new_file, path )
			_.cp(path,'cyan')
			return None

def action():
	files=_.isData()
	if _.switches.isActive('Files'):
		for file in _.switches.values('Files'):
			files.append(file)
	if _.switches.isActive('Folders'):
		for folder in _.switches.values('Folders'):
			for fi in _.fo( folder, r=_.switches.isActive('Recursive')  ):
				files.append( fi )
	for path in files:
		if _.showLine(path):
			process(path)


watermark = '''###########################################################################
What if magic existed?
What if a place existed where your every thought and dream come to life.
There is only one catch: it has to be written down.
Such a place exists, it is called programming.
   - Scott Taylor Reph, RightThumb.com
###########################################################################'''

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




