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
	'file': 'joplin-md2json.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'convert Joplin .md ( RAW ) export to .json',
	'categories': [
						'joplin',
						'md',
						'raw',
						'json',
						'convert',
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

level = 0
records = {}
def action():
	global records
	records = { 'parents': [], 'files': {}, 'folders': {} }
	folder = os.getcwd()
	for item in os.listdir(folder):
		path = folder +os.sep+ item
		if path.endswith('.md') and os.path.isfile(path):
			lines = _.getText(path,raw=True).split('\n')
			lines.reverse()
			data = []
			end = []
			blank = False
			for line in lines:
				if line == '':
					blank = True
				if not blank:
					end.append(line)
				else:
					data.append(line)
			end.reverse()
			data.reverse()
			meta = {}
			data = '\n'.join(data)
			data = _str.cleanBE( data, '\n' )
			meta['title'] = ''
			meta['data'] = ''
			for i,lin in enumerate(data.split('\n')):
				if not i:
					meta['title'] = lin
				else:
					meta['data'] += lin+'\n'
			meta['data'] = _str.cleanBE( meta['data'], '\n' )


			for line in end:
				meta[ line.split(':')[0] ] = _str.cleanBE( line.split(':')[1], ' ' )

			if 'parent_id' in meta:
				if meta['parent_id'] == '':
					records['parents'].append(meta['id'])
					# _.pv(meta)
					# sys.exit()
					# _.pr(meta['data'])
				else:
					if not meta['parent_id'] in records['folders']:
						records['folders'][meta['parent_id']] = []
					records['folders'][meta['parent_id']].append(meta['id'])



			# meta['title'] = meta['data']
			records['files'][meta['id']] = meta
			# _.pr(records)
			# _.pv(records)
			# _.pr(meta['data'])
			# sys.exit()
	_.saveTable2(records, folder +os.sep+ 'joplin-database.json')
	for rec in records['parents']:
		xx = records['files'][rec]['title']
		if not xx == '?':
			processFolder(rec)
	_.pr()
	_.cp(folder +os.sep+ 'joplin-database.json','green')
spent=[]
def processFolder(rec):
	global records
	global level
	if not rec in spent:
		spent.append(rec)
		xx = records['files'][rec]['title']
		t = records['files'][rec]['type_']
		try:
			todo = records['files'][rec]['is_todo']
		except Exception as e:
			todo = '0'
		if len(xx) > 2 and not xx.startswith('Z0'):
			if t == '2' or t == '5':
				_.pr( pre(),  _.cp(xx,'yellow',p=0), _.cp(rec,'purple',p=0) )
			elif todo == '0':
				_.pr( pre(),  _.cp(xx,'green',p=0), _.cp(rec,'purple',p=0) )
			else:
				_.pr( pre(),  _.cp(xx,'red',p=0), _.cp(rec,'purple',p=0) )
			if rec in records['folders']:
				level += 1
				for recF in records['folders'][rec]:
				#     _.pr( pre(), records['files'][recF]['data'].split('\n')[0] )
				# sys.exit()
					processFolder(recF)
				level -= 1

def pre():
	global level
	result = ''
	i=0
	while not i==level:
		i+=1
		result+='  '
	return result



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()