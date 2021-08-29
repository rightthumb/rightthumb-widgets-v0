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
	_.switches.register( 'Comment', '-comment', '\\# OR #' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Label', '-label' )



_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = [ 'Comment' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'toggle_comment.py',
	'liveAppName': __.thisApp( __file__ ),
 	'description': 'Toggle comment in config file',
	'categories': [
						'config',
						'tool',
						'toggle',
						'on',
						'off',
						'swap',
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
						'p thisApp -file file.txt',
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



def action():
	# if not _.isWin:

	escape = '#'
	if _.switches.isActive('Comment'):
		# escape = _.ci(_.switches.values('Comment')[0])
		escape = _.switches.values('Comment')[0]

	the_file_path = 'D:\\tech\\hosts\\VULCAN\\projects\\vnc\\vnc.config'

	for i,the_file_path in enumerate(_.isData(r=1)):
		print(the_file_path)

		if not os.path.isfile(the_file_path):
			print( 'The file:' )
			print( '          ',the_file_path )
			print( 'does not exist' )
		elif os.path.isfile(the_file_path):
			bashrc = _.getText( the_file_path, raw=True )
			s = '{A3D236DE}'
			the_new_file = ''
			found = False
			for ii,line in enumerate(bashrc.split('\n')):
				if s in line:
					label = 'default'
					table = {}
					if _.switches.isActive('Label'):
						table_file = _v.myConfig +_v.slash+ '.toggle_comment.hash'
						table = _.getTable2( table_file )
						label = _.switches.values('Label')[0]
					if not label in table:
						table[label] = {}
					found = True
					if line.startswith(escape):
						the_new_file += line[len(escape):] + '\n'

						if str(ii) in table[label]:
							del table[label][str(ii)]
						table[label][ii] = 1

						print('Now is ON')
					else:

						if str(ii) in table[label]:
							del table[label][str(ii)]
						table[label][ii] = 0

						print('Now is OFF')
						the_new_file += escape + line + '\n'
					
					if _.switches.isActive('Label'):
						_.saveTable2( table, table_file )

				else:
						the_new_file += line + '\n'


			if not found:
				print( 'Error: file is missing code', s )
			else:
				_.saveText( the_new_file, the_file_path )


# $locallhost = "no" #{A3D236DE


########################################################################################
if __name__ == '__main__':
	action()




