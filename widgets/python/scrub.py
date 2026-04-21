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
	pass
	### EXAMPLE: START
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	# _.switches.register( 'Subjects', '-subject,-subjects', isRequired=True )
	_.switches.register( 'Subjects', '-subject,-subjects' )
	### EXAMPLE: END


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
	'file': 'scrub.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'file scrubber',
	'categories': [
						'file',
						'scrub',
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
						_.hp('p scrub -f *'),
						_.hp('p scrub -f *.txt'),
						_.hp('p scrub -f file.txt'),
						_.hp('p scrub -f file1.txt file2.txt'),
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
### EXAMPLE: START
# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END


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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
### EXAMPLE: START
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.fieldProfileSet('data','timestamp','trigger',_.friendlyDate)
# _.tables.fieldProfileSet('data','phone,email,address','alignment','center')
# _.tables.print( 'data', 'name' )
# _.tables.print( 'data', ','.join(_.switches.values('Column')) )
# _.switches.isActive('Files')
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#   if os.path.isdir( row ):
#   if os.path.isfile( row ):
#   os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                   if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START


def process(path):
	global subjects
	lines = _.getText( path )



	for i,line in enumerate(lines):
		if 'tool.class' in subjects: 
			# _.pr('tool.class')
			if 'D.' in line and not '.D.' in line:
				line = line.replace( 'D.', 'oooooo.D.' )
			if 'HD.' in line and not '.HD.' in line:
				line = line.replace( 'HD.', 'oooooo.HD.' )
			if 'DIR.' in line and not '.DIR.' in line:
				line = line.replace( 'DIR.', 'oooooo.DIR.' )
			if 'IS.' in line and not '.IS.' in line:
				line = line.replace( 'IS.', 'oooooo.IS.' )
			if 'SH.' in line and not '.SH.' in line:
				line = line.replace( 'SH.', 'oooooo.SH.' )
			if 'FIG.' in line and not '.FIG.' in line:
				line = line.replace( 'FIG.', 'oooooo.FIG.' )
			if 'EXT.' in line and not '.EXT.' in line:
				line = line.replace( 'EXT.', 'oooooo.EXT.' )
			if 'LS.' in line and not '.LS.' in line:
				line = line.replace( 'LS.', 'oooooo.LS.' )
			if 'STR.' in line and not '.STR.' in line:
				line = line.replace( 'STR.', 'oooooo.STR.' )
			if 'HEAD.' in line and not '.HEAD.' in line:
				line = line.replace( 'HEAD.', 'oooooo.HEAD.' )
			if 'Color.' in line and not '.Color.' in line:
				line = line.replace( 'Color.', 'oooooo.Color.' )
			if 'ONLINE.' in line and not '.ONLINE.' in line:
				line = line.replace( 'ONLINE.', 'oooooo.ONLINE.' )
			if 'virtualFiles.' in line and not '.virtualFiles.' in line:
				line = line.replace( 'virtualFiles.', 'oooooo.virtualFiles.' )
			if 'DATE.' in line and not '.DATE.' in line:
				line = line.replace( 'DATE.', 'oooooo.DATE.' )
			if 'Files_Folders.' in line and not '.Files_Folders.' in line:
				line = line.replace( 'Files_Folders.', 'oooooo.Files_Folders.' )
			if 'PATHS.' in line and not '.PATHS.' in line:
				line = line.replace( 'PATHS.', 'oooooo.PATHS.' )
			if 'EXIT.' in line and not '.EXIT.' in line:
				line = line.replace( 'EXIT.', 'oooooo.EXIT.' )
			if 'BASHRC.' in line and not '.BASHRC.' in line:
				line = line.replace( 'BASHRC.', 'oooooo.BASHRC.' )
			if 'HASH.' in line and not '.HASH.' in line:
				line = line.replace( 'HASH.', 'oooooo.HASH.' )

		line = line.replace( 'oooooo.', 'vc.' )
		line = line.replace( '..', '.' )
		line = line.replace(chr(10),'')
		line = line.replace(chr(27),'')
		line = line.replace('\n','')
		line = line.replace('\r','')
		lines[i] = line

	_.saveText( lines, path )
	_.cp( path, 'cyan' )







def action():
	global subjects
	subjects = _.switches.values('Subjects')
	if not subjects:
		_.e( 'missing subject' )

	for i,path in enumerate( _.isData(r=1) ):
		if _mime.isText(path):
			process(path)


import _rightThumb._mimetype as _mime

# type %tmpf3% | p line --c -make "v.c.{} = {}()"
# type %tmpf3% | p line --c -make "file = file.replace( '{}.', 'v.c.{}.' )"


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






