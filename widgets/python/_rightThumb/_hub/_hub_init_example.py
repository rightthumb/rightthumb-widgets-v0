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

from rightthumb import app
from rightthumb import func as _
reg = app.space(__name__, __file__)
reg.rent = app.register(reg)
app.rent = app.focus(reg.rent)
app.switches()
# app.tables()

def app_switches:

	pass
	### EXAMPLE: START
	# app.switch.reg( 'Input', '-i' )
	# app.switch.reg( 'Files', '-f,-file,-files','file.txt', isPipe='glob,name,data,clean', description='Files' )
	### EXAMPLE: END
app.autoBackupData = app.autoCreationConfiguration['backup']
app.releaseAcquiredData = app.autoCreationConfiguration['logs']
app.myFileLocations_SKIP_VALIDATION = False
app.isRequired_Pipe = False
app.isRequired_Pipe_or_File = False
app.pre_error = False
app.switch_raw = []
# app.switch_raw = [ 'Delim' ]
# app.isRequired_or_List = ['Pipe','Files','Plus']
# app.setting( 'app-switches-raw', [ 'Delim' ] )
reg.documentation = {
	'file': 'thisApp.py',
	'liveAppName': app.this_app( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
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
						app.hp('p thisApp -file file.txt'),
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

reg.data = {
		'start': app.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
					'table': {'sent': [], 'received': [] }, 
		},
	}
### EXAMPLE: START
# reg.documentation['examples'].append( 'p thisApp -file file.txt' )

# reg.documentation['columns'].append( {'name': 'name', 'abbreviation': 'n'} )
### EXAMPLE: END
def sw( argvProcessForce=False ):
	global appDBA
	if not app.appReg == appDBA and appDBA in app.appReg:

		if not __name__ == '__main__':
			app.argv_process = argvProcessForce
		else:
			app.argv_process = True

		app.load()
		app.appInfo[app.appReg] = app.appInfo[appDBA]
		app.appData[app.appReg] = app.appData[appDBA]
	app.construct_registration( app.appInfo[app.appReg]['file'],app.appReg )
	app_switches

	app.myFileLocation_Print = False
	app.switch.trigger( 'Files', app.myFileLocations, vs=True )
	app.switch.trigger( 'Folder', app.myFolderLocations )
	app.switch.trigger( 'URL', app.urlTrigger )
	app.switch.trigger( 'Ago', app.timeAgo )
	app.switch.trigger( 'Duration', app.timeFuture )
	### EXAMPLE: START
	# app.switch.trigger( 'Files',app.inRelevantFolder )    
	# app.switch.trigger( 'Watched', app.txt2Date )
	# app.switch.trigger( 'Input',app.formatColumns )
	# app.switch.trigger( 'Franchise',app.triggerSpace )
	### EXAMPLE: END
	
	app.defaultScriptTriggers()
	app.switch.process()
if not __name__ == '__main__':
	app.argv_process = False
else:
	app.argv_process = True

sw()
def field_set( switchName, switchField, switchValue, rent=False ):
	if not type( rent ) == bool:
		rent = rent
	app.switch.field_set( switchName, switchField, switchValue, rent )
if __name__ == '__main__':
	if not sys.stdin.isatty():
		app.set_pipe_data( sys.stdin.readlines(), app.appReg, clean=True )
app.post_load( __file__ )

########################################################################################
# START

def action():
	# should be   Single-Task   OR   Imply-Architecture-Functions   OR   CLASSES!!
	load()
	global data

	for i,row in enumerate( app.isData(r=1) ):
		print(row)

	if app.switch.isActive('Files'):
		file = app.switch.value('Files')
		files = app.switch.values('Files')

def load():
	global data
	data = app.getTable( 'table' )

########################################################################################
if __name__ == '__main__':
	action()
	app.isExit(diagram=False)



