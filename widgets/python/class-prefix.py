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
	_.switches.register( 'JustClean', '-jc,-clean' )

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
	'file': 'class-prefix.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'gen class prefix in temp file',
	'categories': [
						'class',
						'prefix',
						'code',
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
						_.hp('p class-prefix -f D:\tech\hosts\VULCAN\programs\python\date-class-prefix.py '),
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
		lastClass=''
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
			if line.startswith('\tif ') or line.startswith('\telif ') or line.startswith('\telse:') :
				lastIsIf = True

			if line.startswith('\tglobal '):
				# _.pr('000')
				ln = spaceOut(line)
				if ' global ' in ln:
					# _.pr('001')
					lx = cleanMe( line, ' ' )
					lx = cleanMe( lx, '\n' )
					try:
						lastGlobal = lx.split(' ')[1]
					except Exception as e:
						lastGlobal = ''
					if len(lastGlobal):
						# _.pr( '002', lastGlobal )
						myGlobalsAll.append(lastGlobal)
			if line.startswith('\tdef '):
				myGlobals = []
				lastIsIf = False
				lx = line.split('\tdef ')[1]
				ln = spaceOut(lx)
				lastDef = ln.split(' ')[1]
			elif line.startswith('\t\t'):
				ln = spaceOut(line)
				# if 'global ' in ln:
					# _.pr('100')
				if ' global ' in ln:
					# _.pr('110')
					lx = cleanMe( ln, ' ' )
					# lx = cleanMe( lx, '\n' )
					try:
						lastGlobal = lx.split(' ')[1]
					except Exception as e:
						lastGlobal = ''
					if len(lastGlobal) and not lastGlobal == 'global':
						# _.pr( '111', lastGlobal )
						myGlobals.append(lastGlobal)



				if not lastIsIf:
					ln = spaceOut(line)
					for cd in table[lastClass]:
						if cd:
							if ' '+cd+' ' in ln:
								line = line.replace( cd+'(', lastClass+'.'+cd+'(' )
					for cd in tablev[lastClass]:
						if cd:
							if ' '+cd+' ' in ln:
								line = line.replace( cd, lastClass+'.'+cd )
					

			pass
			ln = spaceOut(line)
			for cd in tabd:
				if cd:
					if ' '+cd+' ' in ln:
						line = line.replace( cd+'(', tabd[cd]+'.'+cd+'(' )
						line = classy( line, tabd[cd] )
			if not lastIsIf:
				for cd in tabv:
					if cd:
						if ' '+cd+' ' in ln:
							_.pr( '200', cd, myGlobalsAll, myGlobals )
							if cd in myGlobalsAll or cd in myGlobals:
								_.pr( '222', cd )
								line = line.replace( cd, tabv[cd]+'.'+cd )
								line = classy( line, tabv[cd] )





			line = classy( line, lastClass )
			ii = 0
			while line.endswith(' '):
				line = line[:-1]
				if ii > 100:
					break
				ii += 1

			newfile += line



		_.saveText( newfile, path )
		pass

def process2(path):
	file = _.getText( path, raw=True, clean=1 )
	_.saveText( file, path )
	file = _.getText( path, c=2 )
	_.saveText( file, path )
	_.cp( [ 'cleaned:', path ], 'cyan' )

def action():
	for i,path in enumerate( _.isData(r=1) ):
		ask = ''
		ask=input(' overwrite? ')
		if ask == 'y':
			if _.switches.isActive('JustClean'):
				process2(path)
			else:
				process(path)
		else:
			_.pr('skipped')

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()