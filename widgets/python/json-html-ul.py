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
	_.switches.register( 'Folders', '-f,-folder,-folders' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob,name,data,clean', description='Files' )
	### EXAMPLE: END

### EXAMPLE: START
# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
#     finds the file in probable locations
#     and 
#         if  _.autoBackupData = True
#         and __.releaseAcquiredData = True
#             GET EPOCH FROM: hosts/hostname/logs/apps/execution_receipt-app_name-epoch.json
#         you can run apps on usb at a clients office
#             when you get home run: p app -loadepoch epoch 
#                 backed up
#                     pipe
#                     files
#                     tables
### EXAMPLE: END
_.autoBackupData = __.setting('receipt-log')
__.releaseAcquiredData = __.setting('receipt-file')
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']
# __.setting( 'app-switches-raw', [ 'Delim' ] )


_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'liveAppName': __.thisApp( __file__ ),
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


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
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
#    os.path.abspath(path)
# __.appRegPipe    ( pipe data registerd focus(__.appReg) set by _.myFileLocations {if imported} , default is None )
# for i,row in enumerate(_.t( _.appData[__.appReg]['pipe'] )):
# for i,row in _.e( _.isData(r=1) ):
# date = _.friendlyDate( theDate )
# _.addComma()
#                                                     if platform.system() == 'Windows':
### EXAMPLE: END
########################################################################################
# START



def action():
	global records
	global code
	load()

	code += pre() + '<ul>\n'
	for rec in records['parents']:
		xx = records['files'][rec]['title']
		if not xx == '?':
			processFolderHTML(rec)
	code += pre() + '</ul>\n'
	# _.pr()
	_.pr(clean(code))
	# _.cp(folder +os.sep+ 'joplin-database.json','green')

def clean(data):
	result = ''
	for char in data:
		if char in _str.printable2:
			result += char
	return result

def what(rec):
	if rec in records['folders']:
		return 'folder'
	try:
		todo = records['files'][rec]['is_todo']
	except Exception as e:
		todo = '0'
	if not todo == '0':
		return 'todo'
	return 'note'

def processFolderHTML(rec):
	global records
	global level
	global code
	
	if not rec in spent:
		spent.append(rec)
		xx = records['files'][rec]['title']
		t = records['files'][rec]['type_']
		try:
			todo = records['files'][rec]['is_todo']
		except Exception as e:
			todo = '0'

		if rec in records['folders']:
			isFo = True
			f = len(records['folders'][rec])
		else:
			f = None
			isFo = False


		if len(xx) > 2 and not xx.startswith('Z0'):
			if not t == '5':
				if t == '2':
					code += li(xx,'folder',isFo,rec,t,f,todo)
				elif todo == '0':
					code += li(xx,'note',isFo,rec,t,f,todo)
				else:
					code += li(xx,'todo',isFo,rec,t,f,todo)
				if rec in records['folders']:
					level += 1
					code += pre() + '<ul id="'+rec+'" class="subby" style="display:none;">\n'
					for recF in records['folders'][rec]:
						if what(recF) == 'folder':
							processFolderHTML(recF)
					for recF in records['folders'][rec]:
						if what(recF) == 'todo':
							processFolderHTML(recF)
					for recF in records['folders'][rec]:
						if what(recF) == 'note':
							processFolderHTML(recF)
					code += pre() + '</ul>\n'
					level -= 1
				


def li(subject,classy,isFo,rec,t,f,todo):
	if _.switches.isActive('Folders') and not isFo:
		return ''
	# js = ' onclick="showHide(event)"'
	pre_check = '<input type="checkbox" id="'+rec+'" class="checklist"> '
	pre_folder = '<img src="folder.png"> '
	pre_note = '<img src="note.png"> '
	if not todo == '0':
		fix = pre_check
	elif isFo:
		fix = pre_folder
	else:
		fix = pre_note
	js = ' onclick="showHide(\''+rec+'\');"'
	JS = js
	if not isFo:
		JS = ''
	if f is None:
		ff = ''
	else:
		ff = ' ('+str(f)+')'

	return pre() + '<li '+JS+' kind="'+t+'">'+fix+'<span class="'+classy+'">'+subject+ff+'</span>'+'</li>\n'

def pre():
	global level
	result = ''
	i=0
	while not i==level:
		i+=1
		result+='    '
	return result



def load():
	global records
	global level
	global code
	global spent
	code = ''
	level = 1
	spent=[]
	records = { 'parents': [], 'files': {}, 'folders': {} }
	records = _.getTable2( 'joplin-database.json' )



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()