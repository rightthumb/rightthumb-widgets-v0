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
	pass
	### EXAMPLE: START
	_.switches.register( 'Upload-Scp', '-u,-up,-upload' )
	_.switches.register( 'Download-Scp', '-dl,-down,-download' )
	_.switches.register( 'Test', '-t,-test' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt',  description='Files', isRequired=True )
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
	'file': 'vps-file.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage website files and open in url based on parentfolder meta',
	'categories': [
						'meta',
						'test',
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
						_.hp('p test -f default.js -test'),
						_.hp('p test -f default.js -up'),
						_.hp('p test -f default.js -dl'),
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
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	### EXAMPLE: START
	# _.default_switch_trigger('Plus', trigger_plus)
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

def process(path):
	meta = {}
	file = os.path.abspath(path)
	folder = __.path(path,pop=True)
	while not os.path.isfile( folder+os.sep+'.folder.meta' ):
		try:
			folder = __.path(folder,pop=True)
		except Exception as e:
			pass
	meta = _.getTable2( folder+os.sep+'.folder.meta' )
	_.pv(meta)
	

	# Upload-Scp Download-Scp Test
	ftp=None
	url=None
	for k in meta:
		for su in meta[k]:
			if su == 'full-path':
				ftp=meta[k]
				break
		if not ftp is None:
			break
	if 'url' in meta:
		url = file.replace( __.path(folder), meta['url'] ).replace('\\','/')
		if os.path.isdir(path):
			url += '/'
		print(url)
		if _.switches.isActive('Test'):
			try:
				import webbrowser
			except Exception as e:
				pass
			try:
				webbrowser.open(url, new=2)
			except Exception as e:
				_.e(e)

	scp='scp'
	if _.isWin:
		scp='"C:\\Program Files\\Git\\usr\\bin\\scp.exe"'

	if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
		if ftp is None or url is None:
			_.e('meta missing fields')
		s=ftp['server']
		f=ftp['full-path']
		u=ftp['user']
		fi = file.replace( __.path(folder), f ).replace('\\','/')
		if os.path.isdir(path):
			fi=__.path(fi,pop=True)
			fi += '/'
			path+=os.sep

	if _.switches.isActive('Upload-Scp'):
		do=f'{scp} {path}  {u}@{s}:{fi}'
	if _.switches.isActive('Download-Scp'):
		do=f'{scp} {u}@{s}:{fi} {path}'
	if _.switches.isActive('Upload-Scp') or _.switches.isActive('Download-Scp'):
		print(do)
		try:
			os.system( do )
		except Exception as e:
			_.e(e)

	
		

def action():
	if not _.switches.isActive('Test') and not _.switches.isActive('Upload-Scp') and not _.switches.isActive('Download-Scp'):
		_.switches.fieldSet( 'Test', 'active', True )
	for i,path in enumerate( _.switches.values('Files') ):
		process(path)



	

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()





