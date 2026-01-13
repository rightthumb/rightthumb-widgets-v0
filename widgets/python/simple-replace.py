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

##################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
# - Scott Taylor Reph (rightthumb.com)
##################################################
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
	_.switches.register( 'Clip', '-clip' )
	_.switches.register( 'Folders', '-folder,-folders' )
	_.switches.register( 'Recursive', '-r' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt',  description='Files' )

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
	'file': 'simple-replace.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'simple replace from pipe or clipboard',
	'categories': [
						'simple',
						'replace',
						'clip',
						'pipe',
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
						_.hp('p simple-replace -f c.bat -clip '),
						_.hp('p simple-replace -f D:\\.rightthumb-widgets\\widgets\\python\\_rightThumb\\_vars\\__init__.py -clip '),
						_.hp('p simple-replace -clip -folder '),
						_.hp('p simple-replace -clip -folder '),
						_.hp('p simple-replace -f %tool% '),
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START

def getFolder(folder):
	global files
	if os.path.isdir(folder):
		for item in os.listdir( folder ):
			path=folder+os.sep+item
			if os.path.isfile(path):
				files.append(path)
			elif os.path.isdir(path) and _.switches.isActive('Recursive'):
				try:
					getFolder(path)
				except Exception as e:
					pass



def process(path):
	# _.pr(path)
	if not _.showLine(path):
		return None
	else:
		global index
		global printed_replace
		file=_.getText(path,raw=True)
		original=file
		for v in index:
			if not printed_replace:
				_.pr(v,index[v])
			file = file.replace(v,index[v])
		printed_replace=True
		
		if not original==file:
			backup_file(path)
			_.saveText(file,path)
			# _.cp(path,'yellow')
def action():
	global index

	if _.switches.isActive('Clip'):
		_paste = _.regImp( __.appReg, '-paste' )
		text=_paste.imp.paste()
	else:
		text='\n'.join(_.isData())
	text=text.replace('\r','')
	text=_str.cleanBE(text,'\n')
	if text:
		# _.pr(text)
		while '\n\n\n' in text:
			text=text.replace('\n\n\n','\n\n')
		# _.pr(text)
		data=text.split('\n\n')
		# _.pr(data)
		index={}
		for dt in data:
			y=dt.split('\n')
			if len(y) > 1:
				y[0]=_str.cleanBE(y[0],' ')
				y[0]=_str.cleanBE(y[0],'\t')
				y[1]=_str.cleanBE(y[1],' ')
				y[1]=_str.cleanBE(y[1],'\t')
				index[y[0]]=y[1]
		# _.pv(index)
		# sys.exit()
		for path in _.switches.values('Files'):
			process(path)
		if _.switches.isActive('Folders'):
			folders=_.switches.values('Folders')
			if not len(_.switches.value('Folders')):
				folders=[os.getcwd()]
			# _.pr(folders)
			global files
			files=[]
			for folder in folders:
				getFolder(folder)
			for path in files:
				process(path)
printed_replace=False
fileBackup = _.regImp( focus(), 'fileBackup' )
fileBackup.switch( 'Silent' )
fileBackup.switch( 'Flag', 'imdb' )
fileBackup.switch( 'isRunOnce' )
fileBackup.switch( 'DoNotSchedule' )
def backup_file(path):
	fileBackup.switch( 'Input', path )
	fb = fileBackup.action()
	# _.cp( [ fb, path ], 'Background.green' )
	_.cp( [ fb ], 'cyan' )


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







