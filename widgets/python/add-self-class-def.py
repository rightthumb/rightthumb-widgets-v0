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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )


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
	'file': 'add-self-class-def.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'add self to class def ',
	'categories': [
						'class',
						'self',
						'convert',
						'tool',
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
						_.hp('p add-self-class-def -f D:\\widgets\\python\\src\\unity\\py3to2.py '),
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
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=False )


_.postLoad( __file__ )

########################################################################################
# START



def spaceOut(line):
	ln = ''
	for char in line:
		if char in _str.alphanumeric+'._':
			ln += char
		else:
			ln += ' '
	return ln

def cleanMe(line,subject=' '):
	ii = 0
	while line.endswith(subject):
		line = line[:-1]
		if ii > 100:
			break
		ii += 1
	ii = 0
	while line.startswith(subject):
		line = line[1:]
		if ii > 100:
			break
		ii += 1
	ii = 0
	while subject+subject in line:
		line = line.replace( subject+subject, subject )
		if ii > 100:
			break
		ii += 1
	return line

def classy( line, lastClass ):
	line = line.replace( lastClass+'.'+lastClass+'.', lastClass+'.' )
	line = line.replace( lastClass+'.'+lastClass+'.', lastClass+'.' )
	line = line.replace( lastClass+'.'+lastClass+'.', lastClass+'.' )
	line = line.replace( lastClass+'.def ' , 'def ' )
	line = line.replace( 'def '+lastClass+'.' , 'def ' )
	line = line.replace( lastClass+'.if ' , 'if ' )
	if 'global '+lastClass+'.' in line:
		line = ''
	return line



def process(path):
	if os.path.isfile(path):
		path = os.path.abspath( path )

		file = _.getText( path )
		table = {}
		tablev = {}
		tabd = {}
		tabv = {}
		lastIsIf = False
		lastClass = ''
		for line in file:
			line = line.replace( '    ', '\t' )
			line = line.replace( '    ', '\t' )
			line = line.replace( '  ', ' ' )
			line = line.replace( '    ', '\t' )
			if line.startswith('class '):
				lastIsIf = False
				ln = spaceOut(line)
				# _.pr(ln)
				lastClass = ln.split(' ')[1]
				table[lastClass] = []
				tablev[lastClass] = []
				_.pr(lastClass)

			if line.startswith('\tif ') or line.startswith('\telif ') or line.startswith('\telse:') :
				lastIsIf = True
			if line.startswith('\tdef '):
				lastIsIf = False
				lx = line.split('\tdef ')[1]
				ln = spaceOut(lx)
				lastDef = ln.split(' ')[0]
				if lastClass:
					table[lastClass].append(lastDef)
					tabd[lastDef] = lastClass
					_.pr('\t',lastDef)
			if line.startswith('\t') and not line.startswith('\t\t') and '=' in line:
				lx = line.split('\t')[1]
				ln = spaceOut(lx)
				lastVar = ln.split(' ')[0]
				if lastClass:
					tablev[lastClass].append(lastVar)
					if not 'def' == lastVar and not 'if' == lastVar :
						tabv[lastVar] = lastClass
			if lastIsIf and line.startswith('\t\t') and not line.startswith('\t\t\t') and '=' in line:
				lw = line.replace( '\t\t', '\t' )
				lx = lw.split('\t')[1]
				ln = spaceOut(lx)
				lastVar = ln.split(' ')[0]
				if lastClass:
					tablev[lastClass].append(lastVar)
					if not 'def' == lastVar and not 'if' == lastVar :
						tabv[lastVar] = lastClass

		_.pr()
		_.pr()
		_.pr()
		newfile = ''
		myGlobals = []
		myGlobalsAll = []
		lastIsIf = False
		for line in file:
			line = line.replace( '    ', '\t' )
			line = line.replace( '    ', '\t' )
			line = line.replace( '  ', ' ' )
			line = line + ' '
			if line.startswith('class '):
				myGlobals = []
				lastIsIf = False
				ln = spaceOut(line)
				lastClass = ln.split(' ')[1]
				_.pr(lastClass)
			if line.startswith('\tif ') or line.startswith('\telif ') or line.startswith('\telse:') :
				lastIsIf = True

			if line.startswith('\tdef '):
				myGlobals = []
				lastIsIf = False
				lx = line.split('\tdef ')[1]
				ln = spaceOut(lx)
				lastDef = ln.split(' ')[1]
				suffix1 = line.split(':')
				if len(suffix1)>1:
					suffix = suffix1[1]
				else:
					suffix = ''
				dic = {
							'name': line.split('def ')[1].split('(')[0],
							'args': line.split('(')[1].split(')')[0],
							'suffix': suffix,
				}
				dic['args'] = dic['args'].replace( ',', ', ' )
				dic['args'] = dic['args'].replace( '  ', ' ' )
				dic['args'] = dic['args'].replace( '  ', ' ' )
				lx = line.replace(' ','')
				if 'self,' in lx or 'self)' in lx:
					line = '\tdef '+dic['name']+'( '+dic['args']+' ):'+dic['suffix']+''
				else:
					line = '\tdef '+dic['name']+'( self, '+dic['args']+' ):'+dic['suffix']+''
				line = line.replace( '  ', ' ' )
				line = line.replace( '  ', ' ' )
				line = line.replace( '  ', ' ' )
				line = line.replace( '  ', ' ' )
				line = line.replace( ', )', ' )' )

			if line.startswith('def') or not line.startswith('\t') and line.split('#')[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','') and not line.split('#')[0].replace(' ','').replace('\n','').replace('\t','').replace('\r','')[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
				lastClass = ''
			if line.startswith('\t\t'):
				if lastClass:
					line = line.replace( 'vc.'+lastClass+'.', 'self.' )
				# if lastClass and lastClass+'' in line:
				#   _.pr()
				#   _.pr('vc.'+lastClass+'.', line )
				#   _.pr()
				# # if 'vc.'+lastClass+'.' in line:
				#   _.pr('vc.'+lastClass+'.' )



			ii = 0
			while line.endswith(' '):
				line = line[:-1]
				if ii > 100:
					break
				ii += 1

			newfile += line



		_.saveText( newfile, path )
		_.cp(path,'cyan')
		pass


def action():

	for i,line in enumerate( _.isData(r=1) ):
		process(line)



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()