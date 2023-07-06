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

import os
import sys
import time
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

import _rightThumb._profileVariables as _profile
focus()
	# profile = _profile.records.audit( 'name', asset )
# import _rightThumb._md5 as _md5
##################################################

def appSwitches():
	pass
	_.switches.register( 'Source', '-src,-source' )
	_.switches.register( 'Destination', '-dst,-dest,-destination', isRequired=True )

	_.switches.register( 'MirrorPath', '-m,-mirror' )
	_.switches.register( 'NotRecursive', '-nr,-notrecursive' )

	_.switches.register( 'Text', '-t,-text,-txt' )
	_.switches.register( 'Binary', '-bin' )

	_.switches.register( 'Print', '-print' )

	_.switches.register( 'Report', '-report' )

	_.switches.register( 'Answer', '-answer', 'a' )

	_.switches.register( 'Fast_UpdateAtEnd', '-fast' )
	_.switches.register( 'Ago', '-ago' )
	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.isRequired_or_List = ['Pipe','Source']

_.appInfo[focus()] = {
	'file': 'copyTool.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Tool to make it easy to copy stuff',
	'categories': [
						'copy',
						'tool',
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
						'p dir3 -ago 1w -c p --c | p copyTool -dst n',
						'',
						'a.cp -src test -dst test',
						'',
						'a.cp -src test -dst n date tasks',
						'',
						'a.cp -src test -dst f sa',
						'a.cp -src test -dst f ta',
						'',
						'src shortcuts',
						'    pp program programs',
						'    tt tech',
						'    ta apps techapps',
						'    dl downloads',
						'    doc docs documents',
						'    dd desktop',
						'    pf programfiles "program files"',
						'    pfx pf86 pfx86 programfilesx86 programfiles86 "program files x86"',
						'',
						'',
						'dst shortcuts',
						'    in tainstallers installers',
						'    sa tasa standalone',
						'    ta apps techapps',
						'    nn note notes',
						'    test',
						'    mdt date today',
						'',
						'',
						[ 'p dir3 -ago 1w --c -c p | a.cp -dst test -m', 'red' ],
						'p dir3 -ago 1w --c -c p | a.cp -dst test',
						'',
						[ 'p files --c | a.cp -dst f ta personal -m', 'red' ],
						'',
						'',
						'',
						[':________________________________', 'white'],
						['UPDATE USB', 'white'],
						'',

						'theUSB print',
						['a.cp -m -src pp -dst %theusb% ', 'red' ],
						'e,12',
						'',
						['a.cp -m -src key1 -dst %theusb% ', 'red' ],
						'a',
						'',
						['a.cp -m -src key2 -dst %theusb% ', 'red' ],
						'a',
						'',
						['a.cp -m -src tapy3 -dst %theusb% ', 'red' ],
						'a',
						'',
						'a.cp -m -src ta -dst %theusb%',
						'',
						'a.cp -src ma -dst mad',
						'a',
						'',
						'a.cp -src ma -dst %theusb% mad',
						'a',
						'',
						'done',
						'',
						[':________________________________', 'white'],
						['UPDATE FROM USB', 'white'],
						'',
						['a.cp -m -src %theusb% pp -dst %scriptDrive% ', 'red' ],
						'a',
						'',
						['a.cp -m -src %theusb% tapy3 -dst %scriptDrive% ', 'red' ],
						'a',
						'',
						'a.cp -m -src %theusb% ta -dst ta ',
						'',
						'a.cp -src %theusb% mad -dst ma',
						'a',
						'',
						[':________________________________', 'white'],
						'',
						'findDriveLetter + my 256GB btn Sandisk BLK',
						# 'theDriveID + my 3T Backup Drive',
						# '  theDrive %theDriveID% error',
						# 'theDrive {A9BED46A-116D-47ED-BA20-6AE5CC408424}',
						' a.cp -src D:\\_Scott\\S_Documents\\Projects\\new_computer -dst %theDrive% e:\\new_computer',
						'a',
						'',
						'',
						'',
						'',
						'a.cp -src py?secureFiles.py -dst lpy',
						'a.cp -src py?bashrc.py -dst lpy',
						'',
	],



	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
	],
	'aliases': [
					# 'this',
					# 'app',
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


import _rightThumb._bookmarks as _bm
focus()
def source_destination_Trigger( data ):
	global _bm

	if not _v.slash in data:
		if '?' in data:
			test = _bm.Bookmarks( data.split('?')[0] ).get()
			if not test is None:
				return test + _v.slash + data.split('?')[1]

	test = _bm.Bookmarks( data ).get()

	if not test is None:
		return test

	test = data.lower()
	d = _v.techDrive
	if test == 'td':
		data = d
	# if test == 'mad':
		# data = _v.techFolder+_v.slash+'hosts'+_v.slash+'{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}'+_v.slash+'widgets'+_v.slash+'batch'
	elif test == 'hd':
		data = _v.hostDefault
	elif test == 'hh':
		data = _v.thisHost
	elif test == 'ma':
		data = _v.myBatch
	elif test == 'w' or test == 'widget' or test == 'widgets':
		data = _v.techFolder+_v.slash+'widgets'
	elif test == 'pp' or test == 'program' or test == 'programs':
		data = _v.techFolder+_v.slash+'widgets'
	elif test == 'tt' or test == 'tech':
		data = _v.techFolder
	elif test == 'key1':
		data = d+':\\techApps\\KeePass-1.28'
	elif test == 'key':
		data = d+':\\techApps\\KeePass-2.45'
	elif test == 'key2':
		data = d+':\\techApps\\KeePass-2.45'
	elif test == 'pyinst':
		data = d+':\\techApps\\Python_Installers'
	elif test == 'pyinst2':
		data = d+':\\techApps\\Python_Installers\\2'
	elif test == 'pyinst3':
		data = d+':\\techApps\\Python_Installers\\3'
	elif test == 'tests':
		data = 'D:\\tech\\hosts\\MSI\\playground\\usbAppsUpdate\\source'
	elif test == 'ta' or test == 'apps' or test == 'techapps':
		data = _v.appsFolder
	elif test == 'tapy' or test == 'pyexe' or test == 'techappspython':
		data = d+':\\techApps\\Python'
	elif test == 'tapy3' or test == 'pyexe3' or test == 'techappspython3':
		data = d+':\\techApps\\Python\\Python36-32'
	elif test == 'dl' or test == 'downloads':
		data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Downloads'
	elif test == 'doc' or test == 'docs' or test == 'documents':
		data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Documents'
	elif test == 'dd' or test == 'desk' or test == 'desktop':
		data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Desktop'
	elif test == 'pf' or test == 'programfiles' or test == 'program files':
		data = 'C\\Program Files'
	elif test == 'pfx' or test == 'pf86' or test == 'pfx86' or test == 'programfilesx86' or test == 'programfiles86' or test == 'program files x86':
		data = 'C:\\Program Files ( x86 )'

	elif test == 'h' or test == 'host' or test == 'hosts':
		data = _v.techFolder+_v.slash+'hosts'

	elif test == 'n' or test == 'note' or test == 'notes':
		data = _v.myNotes
	elif test == 'ta' or test == 'apps' or test == 'techapps':
		data = _v.appsFolder
	elif test == 'in' or test == 'tainstallers' or test == 'installers':
		data = _v.appsFolder +_v.slash+'_installers'
	elif test == 'sa' or test == 'tasa' or test == 'standalone':
		data = d+':\\techApps\\_stand_alone'
	if test == 'testd':
		data = 'D:\\tech\\hosts\\MSI\\playground\\usbAppsUpdate\\destination'
	if test == 'mdt' or test == 'date' or test == 'today':
		data = _.resolveEpoch( time.time() ).split( ' ' )[0].replace( '-', '.' )
	elif len( data ) == 1:
		data = data + ':'+_v.slash

	import _rightThumb._bookmarks as _bm
	bm = _bm.Bookmarks( data ).get()
	if not bm is None:
		data = bm
	if '?' in data:
		x = data.split('?')
		bm = _bm.Bookmarks( x[0] ).get()
		if not bm is None:
			data = bm +_v.slash+ x[1]

	return data



# def sourceTrigger( data ):
#     test = data.lower()
#     d = _v.techDrive
#     if test == 'p' or test == 'program' or test == 'widgets':
#         data = d+':\\tech\\programs'
#     elif test == 't' or test == 'tech':
#         data = d+':\\tech'
#     elif test == 'test':
#         data = 'D:\\tech\\hosts\\MSI\\playground\\usbAppsUpdate\\source'
#     elif test == 'ta' or test == 'apps' or test == 'techapps':
#         data = d+':\\techApps'
#     elif test == 'tapy' or test == 'pyexe' or test == 'techappspython':
#         data = d+':\\techApps\\Python'
#     elif test == 'tapy3' or test == 'pyexe3' or test == 'techappspython3':
#         data = d+':\\techApps\\Python\\Python36-32'
#     elif test == 'dl' or test == 'downloads':
#         data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Downloads'
#     elif test == 'doc' or test == 'docs' or test == 'documents':
#         data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Documents'
#     elif test == 'd' or test == 'desk' or test == 'desktop':
#         data = _v.cmdGetVar( 'userprofile' )+_v.slash+'Desktop'
#     elif test == 'pf' or test == 'programfiles' or test == 'program files':
#         data = 'C\\Program Files'
#     elif test == 'pfx' or test == 'pf86' or test == 'pfx86' or test == 'programfilesx86' or test == 'programfiles86' or test == 'program files x86':
#         data = 'C:\\Program Files ( x86 )'

#     return data

# def destinationTrigger( data ):
#     test = data.lower()
#     d = _v.techDrive
#     if test == 'n' or test == 'note' or test == 'notes':
#         data = _v.myNotes
#     elif test == 'ta' or test == 'apps' or test == 'techapps':
#         data = d+':\\techApps'
#     elif test == 'in' or test == 'tainstallers' or test == 'installers':
#         data = d+':\\techApps\\_installers'
#     elif test == 'sa' or test == 'tasa' or test == 'standalone':
#         data = d+':\\techApps\\_stand_alone'
#     if test == 'test':
#         data = 'D:\\tech\\hosts\\MSI\\playground\\usbAppsUpdate\\destination'
#     if test == 'mdt' or test == 'date' or test == 'today':
#         data = _.resolveEpoch( time.time() ).split( ' ' )[0].replace( '-', '.' )
#     elif len( data ) == 1:
#         data = data + ':'+_v.slash

#     return data



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


	_.switches.trigger( 'Source',source_destination_Trigger )
	_.switches.trigger( 'Destination',source_destination_Trigger )


	# _.switches.trigger( 'Source',sourceTrigger )
	# _.switches.trigger( 'Destination',destinationTrigger )


	

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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# __.appRegPipe
########################################################################################
# START

_dirList = _.regImp( __.appReg, 'dirList' )
_pathPatterns = _.regImp( __.appReg, 'filePathPatterns' )
focus()
from shutil import copyfile

def createDestinationFolders( folder ):
	if os.path.isdir( folder ):
		return True

	parts = folder.split( _v.slash )
	
	if not os.path.isdir( parts[0]+_v.slash ):
		_.colorThis( 'Error: Destination drive does not exist', 'red' )

	# drive = parts[0] + _v.slash
	# parts.reverse()
	# parts.pop()
	# parts.reverse()
	# _.pr( _v.slash.join( parts ) )

	newParts = []

	for p in parts:

		newParts.append( p )
		f = _v.slash.join( newParts )
		exist = os.path.isdir( f )
		if not exist:
			try:
				os.mkdir( f )
			except Exception as e:
				_.colorThis( [ 'Error: creating folder', f ], 'red' )


def createDestinationFoldersSrc( src, folders, destination ):
	for f in folders:
		p = f.replace( src+_v.slash, '' )
		d = destination + _v.slash + p
		createDestinationFolders( d )
		# _.pr( d )
		

def genFolders( src, folders ):
	result = []
	for f in folders:
		p = f.replace( src+_v.slash, '' )
		result.append( p )

	return result

def matchFolders( src, destination, toProcess ):
	global masterD
	tmpD = destination
	if not masterD in tmpD:
		tmpD = masterD
	destination = tmpD

	result = []
	result.append( { 's': src, 'd': destination } )
	for part in toProcess:
		s = src +_v.slash+ part
		d = destination +_v.slash+ part
		result.append( { 's': s, 'd': d } )
	return result

def getFiles( path ):
	files = []

	try:
		
		dirList = os.listdir( path )
	except Exception as e:
		return []

	for item in dirList:
		p = path + _v.slash + item
		if os.path.isfile( p ):
			if _.showLine( p ):
				files.append( p )
	return files

def destinationStructure( path ):
	global masterS
	global masterD

	if not len(masterS):
		_.colorThis( 'No Source', 'red' )
		return masterD 

	if os.path.isfile( path ):
		parts = path.split(_v.slash)
		file = _v.slash.join( parts )
		parts.pop()
		folder = _v.slash.join( parts )

	else:
		return None

	fop = folder.replace( masterS, '' )
	fip = file.replace( masterS, '' )
	# _.printTest( fip )
	dfo = masterD + '' + fop + _v.slash
	dfi = masterD + '' + fip
	createDestinationFolders( dfo )
	return dfi
	# _.printTest( 'HERE' )

	# 
	# sys.exit()


def destinationStructureGetFolder( s, d, path ):
	global masterDList
	global masterDListX

	if os.path.isfile( path ):
		parts = path.split(_v.slash)
		file = _v.slash.join( parts )
		parts.pop()
		folder = _v.slash.join( parts )



	fop = folder.replace( s, '' )
	fip = file.replace( s, '' )
	# _.printTest( fip )
	dfo = d + '' + fop 
	dfi = d + '' + fip


	if _.switches.isActive('MirrorPath'):
		dfi = _.switches.values('Destination')[0][0] + path[1:]
		x = dfi.split(_v.slash)
		x.pop()
		dfo = _v.slash.join( x )

	dfi = dfi.replace( _v.slash+_v.slash, _v.slash )
	dfo = dfo.replace( _v.slash+_v.slash, _v.slash )

	# _.pr( 'masterS:', masterS )
	# _.pr( '    dfo:', dfo )
	# _.pr( '    dfi:', dfi )
	# sys.exit()

	# _.pr()
	# _.pr( 'dfo:', dfo )
	# _.pr( 'dfi:', dfi )

	# sys.exit()
	if not d in masterDListX:
		masterDListX.append( d )
		masterDList.append( dfi )


	sMod_md = _.mod( path )
	shouldCopy = False
	if not os.path.isfile( dfi ):
		shouldCopy = True
	else:
		dMod = _.mod( dfi )
		sMod = sMod_md
		if sMod > dMod:
			shouldCopy = True
	if shouldCopy:
		if _.switches.isActive('Ago'):
			if not sMod_md > _.switches.value('Ago'):
				shouldCopy = False
	if shouldCopy:
		createDestinationFolders( dfo )

	else:
		dfi = None

	# _.pr()
	# _.pr( 'dfo:', dfo )
	# _.pr( 'dfi:', dfi )


	return dfi
	# _.printTest( 'HERE' )

	# 
	# sys.exit()



def destinationStructurePipe( path ):
	# global masterS
	global masterD
	global patterns
	global masterDList

	masterS = ''
	for record in patterns:
		if record['folder'] in path:
			parts = record['folder'].split( _v.slash )
			if _.switches.isActive('MirrorPath'):
				parts.pop()
			masterS = _v.slash.join( parts )



	if not len(masterS):
		_.colorThis( 'No Source: set to original', 'red' )
		return masterD 

	if os.path.isfile( path ):
		parts = path.split(_v.slash)
		file = _v.slash.join( parts )
		parts.pop()
		folder = _v.slash.join( parts )

	else:
		return None
	

	fop = folder.replace( masterS, '' )
	fip = file.replace( masterS, '' )
	# _.printTest( fip )
	dfo = masterD + '' + fop 
	dfi = masterD + '' + fip


	if _.switches.isActive('MirrorPath'):
		dfi = _.switches.values('Destination')[0][0] + path[1:]
		x = dfi.split(_v.slash)
		x.pop()
		dfo = _v.slash.join( x )

	dfi = dfi.replace( _v.slash+_v.slash, _v.slash )
	dfo = dfo.replace( _v.slash+_v.slash, _v.slash )

	# _.pr( 'masterS:', masterS )
	# _.pr( '    dfo:', dfo )
	# _.pr( '    dfi:', dfi )
	# sys.exit()


	# _.pr( 'dfo:', dfo )
	# _.pr( 'dfi:', dfi )

	# sys.exit()

	masterDList.append( dfi )

	shouldCopy = False
	if not os.path.isfile( dfi ):
		shouldCopy = True
	else:
		dMod = _.mod( dfi )
		sMod = _.mod( path )
		if sMod > dMod:
			shouldCopy = True
	if shouldCopy:
		createDestinationFolders( dfo )

	else:
		dfi = None


	return dfi
	# _.printTest( 'HERE' )

	# 
	# sys.exit()

def fileCopy( s, d ):
	global totals
	global copyReport
	# _.pr()
	# _.pr( '     Source:', s )
	# _.pr( 'Destination:', d )
	# return None
	if _.showLine( s ):
		# _.pr( s )
		shouldCopy = False
		if not os.path.isfile( d ):
			shouldCopy = True
		else:
			dMod = _.mod( d )
			sMod = _.mod( s )
			if sMod > dMod:
				shouldCopy = True
		if shouldCopy:
			try:
				result = copyfile( s, d )
			except Exception as e:
				result = 'Error'
			if result == d:
				didR = 'C'
				did = _.colorThis( 'C', 'green', p=0 )
			else:
				didR = 'E'
				did = _.colorThis( 'E', 'red', p=0 )
		else:
			didR = 'S'
			result = 'skipped'
			did = _.colorThis( 'S', 'yellow', p=0 )
		totals[ didR ] += 1
		if not _.switches.isActive('Fast_UpdateAtEnd'):
			_.updateLine(totals)
		copyReport['totals'][ didR ] += 1
		copyReport['records'][ didR ].append( s )
		
		if _.switches.isActive('Print'):
			_.pr( did, _.colorThis( s, 'cyan', p=0 ) )



		# _.pr( did, s )

#         # do = 'xcopy /d/y/c "' + s + '" "' + d + '">NUL'
#         do = 'xcopy /d/y/c/i/q "' + s + '" "' + d + '"'
#         _.printTest( do, x=0 )
#         # do = 'echo test'
#         try:
#             os.system( '"' + do + '"' )
# # copyfile
#         except Exception as e:
#             pass

def fileCopyX( s, d ):
	global totals
	global copyReport

	if _.showLine( s ):

		d = destinationStructurePipe( s )

		if not d is None:
			try:
				result = copyfile( s, d )
			except Exception as e:
				result = 'Error'
			if result == d:
				didR = 'C'
				did = _.colorThis( 'C', 'green', p=0 )
			else:
				didR = 'E'
				did = _.colorThis( 'E', 'red', p=0 )
		else:
			didR = 'S'
			result = 'skipped'
			did = _.colorThis( 'S', 'yellow', p=0 )
		totals[ didR ] += 1
		if not _.switches.isActive('Fast_UpdateAtEnd'):
			_.updateLine(totals)
		copyReport['totals'][ didR ] += 1
		copyReport['records'][ didR ].append( s )
		
		if _.switches.isActive('Print'):
			_.pr( did, _.colorThis( s, 'cyan', p=0 ) )


def fileCopyY( s, d, path ):
	global totals
	global copyReport


	if _.showLine( s ):

		d = destinationStructureGetFolder( s, d, path )
		# return None
		# _.pr( s, d, path )
		s = path


		if not d is None:
			try:
				result = copyfile( s, d )
			except Exception as e:
				result = 'Error'
			if result == d:
				didR = 'C'
				did = _.colorThis( 'C', 'green', p=0 )
			else:
				didR = 'E'
				did = _.colorThis( 'E', 'red', p=0 )
		else:
			didR = 'S'
			result = 'skipped'
			did = _.colorThis( 'S', 'yellow', p=0 )
		totals[ didR ] += 1
		if not _.switches.isActive('Fast_UpdateAtEnd'):
			_.updateLine(totals)
		copyReport['totals'][ didR ] += 1
		copyReport['records'][ didR ].append( s )
		
		if _.switches.isActive('Print'):
			_.pr( did, _.colorThis( s, 'cyan', p=0 ) )


def fileCopyX_old( s, d ):
	

	if _.showLine( s ):

		d = destinationStructurePipe( s )

		# createDestinationFolders( d )
		# _.pr( s )
		do = 'xcopy /d/y/c/i/q "' + s + '" "' + d + _v.slash+'">NUL 2>&1'
		
		# do = 'echo test'
		try:
			os.system( '"' + do + '"' )
			did = _.colorThis( 'C', 'yellow', p=0 )
		except Exception as e:
			did = _.colorThis( 'E', 'red', p=0 )
			
		_.pr( did, _.colorThis( s, 'cyan', p=0 ) )
def copyFolders( toCopy ):

	for record in toCopy:
		files = getFiles( record['s'] )

		if len( files ):
			for file in files:
				folderCopy( file, record['d'] )


def getFolder( s, d, folder ):
	takeAction = False
	if os.path.isdir(folder):
		try:
			dirList = os.listdir(folder)
			takeAction = True
		except Exception as e:
			takeAction = False
	if takeAction:
		
		for item in dirList:
			path = folder + _v.slash + item
			path = path.replace(_v.slash+_v.slash,_v.slash)
			if os.path.isfile(path):
				fileCopyY( s, d, path )
			if os.path.isdir(path):
				if os.path.isdir(path):
					try:
						getFolder( s, d, path )
					except Exception as e:
						pass
			# try:
			#         else:
			#             _.pr('error')


			# except Exception as e:
			#     pass



def process( s, d, fs ):
	# _.pr( s )
	# _.pr( d )
	# _.pr( fs )
	# sys.exit()
	toProcess = genFolders( s, fs )
	toCopy = matchFolders( s, d, toProcess )
	_.pr()
	_.pr( toProcess )
	_.pr()
	copyFolders( toCopy )

def processFiles( s, d, fs, a=0 ):
	global masterD
	global totals
	# _.pr( s )
	# _.pr( d )
	# _.pr( fs )
	# sys.exit()

	if a:
		_.colorThis( [ '\t',masterD ], 'cyan' )
	else:
		_.colorThis( [ '\t',masterD + _v.slash + fs[0].split(_v.slash)[ len( masterD.split(_v.slash) ) ] ], 'cyan' )

	for path in fs:
		d = destinationStructure( path )
		if not d is None:
			# _.pr()
			# _.printTest( 'Before fileCopy', x=0 )
			fileCopy( path, d )
			# _.printTest( 'After fileCopy', x=0 )
	_.pr()
	x = d.split(_v.slash)
	x.pop()

	_.pr()
	_.colorThis( [ '', _.addComma(totals['C']), '\tCopied' ], 'yellow' )
	# _.pr()
	_.colorThis( [ '', _.addComma(totals['S']), '\tAlready up to date' ], 'yellow' )
	# _.printVar( totals )
	# _.pr()
	_.colorThis( [ '', _.addComma(totals['E']), '\tErrors' ], 'yellow' )
	# _.colorThis( [ totals ], 'yellow' )

def folderSelection( s, d ):
	global masterD
	global hasCleared
	os.system( 'cls' )
	_.pr()
	_.pr( ' Folder:' )
	_.pr( '       ', s )
	# return False

	
	_dirList.switch( 'Recursion', delete=True )
	_dirList.switch( 'Folders' )
	_dirList.switch( 'Files', delete=True )
	_dirList.switch( 'Path', s )
	fs = _dirList.do( 'action' )

	if not _.switches.isActive('Answer'):
		_.pr()
		_.colorThis( 'Select what folders to backup:', 'yellow' )
		_.pr()
		options = []
		sections = []
		fs.sort()
		for i,folder in enumerate( fs ):
			options.append( str( i ) )
			cf = folder.replace( s+_v.slash, '' )
			_.colorThis( [ '\t', i, cf ], 'cyan' )
			sections.append( str(i) )
		_.pr()
		_.pr()
		_.pr()
		_.colorThis( [  'A = recursive ( all files and subfolder )'  ], 'yellow' )
		_.colorThis( [  'S = open a subfolder and list the folders'  ], 'yellow' )
		_.colorThis( [  'F = disables recursion and can specify a file'  ], 'yellow' )
		_.colorThis( [  'E = all except'  ], 'yellow' )
		_.colorThis( [  'B = back a folder'  ], 'yellow' )
		_.pr()
		_.colorThis( [  'Example: a or 0,1 of s,35 f,SanDisk.zip'  ], 'yellow' )
		_.pr()
		selection = input( ' Selection: ' )
	else:
		selection = ','.join( _.switches.values('Answer') )
	selection = selection.lower()
	selection = _str.cleanBE( selection,' ' )
	_.pr()
	os.system('cls')
	_.pr()
	_.colorThis( 'Copy Tool Results:', 'green' )
	_.pr()

	if selection.startswith( 'x' ):
		_.pr( 'Exit' )
		sys.exit()

	if 'b' in selection :
		sx = s.split(_v.slash)
		sx.pop()
		s = _v.slash.join(sx)

		dx = d.split(_v.slash)
		dx.pop()
		d = _v.slash.join(dx)

		return folderSelection( s, d )

	if 'e' in selection :
		selection = selection.replace( 'e', '' )
		selection = selection.replace( ' ', '' )
		selection = _str.replaceDuplicate(selection,',')
		selection = _str.cleanBE(selection,',')

		autoSelect = []
		for x in sections:
			found = False
			for y in selection.split(','):
				if y == x:
					found = True

			if not found:
				autoSelect.append( x )

		selection = ','.join( autoSelect )
		# _.pr( selection )
		# sys.exit()

	if 'a' in selection and not selection.startswith( 'f' ):
		# _dirList.switch( 'Recursion' )
		# _dirList.switch( 'Files' )
		# _dirList.switch( 'Folders', delete=True )
		# _dirList.switch( 'Path', s )
		# data = _dirList.do( 'action' )
		# processFiles( s, d, data, a=1 )
		
		getFolder( s, d, s )

		complete(printTotals=True)
		return False
	

	if 's' in selection and not selection.startswith( 'f' ):
		for i in selection.split( ',' ):
			if i in options:
				nfs = fs[int( i )]
				match = matchFolders( s, d, genFolders( s,[nfs] ) )
				folderSelection( match[1]['s'], match[1]['d'] )
		return False

	if 'b' in selection and not selection.startswith( 'f' ):
		tmpD = popLast( d )
		if not masterD in tmpD:
			tmpD = masterD
		folderSelection( popLast( s ), tmpD )
		return False
	if not _.switches.isActive( 'NotRecursive' ):
		if not selection.startswith( 'f' ):
			_dirList.switch( 'Recursion' )

	if len( selection.split( ',' ) ) > 1 and len( selection[1] ):
		shouldSet = False
		for x in selection:
			if x in _str.alphaChar:
				shouldSet = True
		if shouldSet:

			_.switches.fieldSet( 'Plus', 'active', True )
			_.switches.fieldSet( 'Plus', 'value', selection.split( ',' )[1] )
			_.switches.fieldSet( 'Plus', 'values', [selection.split( ',' )[1]] )



	_dirList.switch( 'Files' )
	_dirList.switch( 'Folders', delete=True )
	foldersToCopy = []
	ran = False
	for i in selection.split( ',' ):
		if i in options:
			ran = True
			nfs = fs[int( i )]

			match = matchFolders( s, d, genFolders( s,[nfs] ) )
			# _dirList.switch( 'Path', nfs )
			# data = _dirList.do( 'action' )
			# processFiles(  match[1]['s'], match[1]['d'],  data   )
			getFolder( match[1]['s'], match[1]['d'], match[1]['s'] )

	if ran:
		complete(printTotals=True)
	if not ran and selection.startswith( 'f' ):
		# _dirList.switch( 'Path', s )
		# data = _dirList.do( 'action' )
		# processFiles( s, d, data )
		getFolder( s, d, s )
		complete(printTotals=True)
	return False

def popLast( path ):
	p = path.split( _v.slash )
	p.pop()
	return _v.slash.join( p )



def complete(printTotals=False):
	global copyReport

	if not _.switches.isActive('Fast_UpdateAtEnd'):
		_.updateLine('                                                     ')
	_.pr()
	if printTotals:


		# masterDList

		_pathPatterns.switch( 'JustReturn' )
		_pathPatterns.pipe( masterDList )
		patterns = _pathPatterns.do( 'action' )


		try:
			for record in patterns:
				_.colorThis( [ record['folder'] ], 'cyan' )
		except Exception as e:
			pass


		_.pr()
		_.colorThis( [ '', _.addComma(totals['C']), '\tCopied' ], 'yellow' )
		_.colorThis( [ '', _.addComma(totals['S']), '\tAlready up to date' ], 'yellow' )
		_.colorThis( [ '', _.addComma(totals['E']), '\tErrors' ], 'yellow' )



	# copyReport = { 'totals': { 'C': 0, 'E': 0, 'S': 0,  }, 'records': { 'C': [], 'E': [], 'S': [],  } }

	_.pr( '____________________________________________________________________' )

	if copyReport['totals']['C']:
		_.pr()
		_.pr()
		_.colorThis( 'Copied:', 'green' )
		_.pr()

		for record in copyReport['records']['C']:
			_.colorThis( [ '\t', record ] , 'cyan' )
		_.pr()
		_.colorThis( [ '', copyReport['totals']['C'] ], 'cyan' )
		_.pr()

	if False:
		if copyReport['totals']['S']:
			_.pr()
			_.pr()
			_.colorThis( 'Already Had Updated Copy:', 'yellow' )
			_.pr()

			for record in copyReport['records']['S']:
				_.colorThis( [ '\t', record ], 'cyan' )
			_.pr()
			_.colorThis( [ '', copyReport['totals']['S'] ], 'yellow' )
			_.pr()



		if copyReport['totals']['E']:
			_.pr()
			_.pr()
			_.colorThis( 'Error:', 'yellow' )
			_.pr()

			for record in copyReport['records']['E']:
				_.colorThis( [ '\t', record ], 'red' )
			_.pr()
			_.colorThis( [ '', copyReport['totals']['E'] ], 'yellow' )
			_.pr()



	# _.printVar(  )

def action():
	focus()
	global masterD
	global masterS
	global masterDList

	if not _.switches.isActive('Source') and not _.switches.isActive('Destination'):
		focus()
		_.switches.help()
		sys.exit()


	s = ''
	if _.switches.isActive( 'Source' ):
		s = _.switches.values( 'Source' )[0]

		# when using same trigger
		dx = _.switches.values( 'Source' )
		if len( dx ) > 1:
			if dx[0].lower() == 'error':
				_.colorThis( [ 'Drive Not Connected' ], 'red' )
				sys.exit()
			if len( dx ) > 1 and len( dx[0] ) == 3 and dx[0][1:] == ':'+_v.slash:
				dx[0] = dx[0][:2]
				dx[1] = dx[1][3:]
			s = _v.slash.join( dx )
		else:
			s = _.switches.values( 'Source' )[0]

		if len(s) == 1:
			s+=':'+_v.slash

		if s.lower().startswith('error') == 'error':
			_.colorThis( [ 'Drive Not Connected' ], 'red' )
			sys.exit()
		# when using same trigger



	d = ''

	dx = _.switches.values( 'Destination' )
	if len( dx ) > 1:
		if dx[0].lower() == 'error'  or dx[0] == '0'  or dx[0] == 0  :
			_.colorThis( [ 'Drive Not Connected' ], 'red' )
			sys.exit()
		if len( dx ) > 1 and len( dx[0] ) == 3 and dx[0][1:] == ':'+_v.slash:
			dx[0] = dx[0][:2]
			dx[1] = dx[1][3:]
		d = _v.slash.join( dx )
	else:

		if _.switches.isActive( 'MirrorPath' ) and _.switches.isActive( 'Source' ):
			dtmp = _.switches.values( 'Destination' )[0]
			d = dtmp[0] + s[1:]
		else:
			d = _.switches.values( 'Destination' )[0]

	if len(d) == 1:
		d+=':'+_v.slash

	if d.lower().startswith('error') or d.startswith('0'):
		_.colorThis( [ 'Drive Not Connected' ], 'red' )
		sys.exit()
	if not _.switches.isActive('Answer'):
		_.pr( 'S:', s )
		_.pr( 'D:', d )
		pause=input(' : ')
	# sys.exit()

	if os.path.isfile(s):
		if os.path.isdir(d):
			if not d.endswith(_v.slash):
				d += _v.slash
			d += _.fileFolder(s)['file']
		folderTest = None
		try:
			folderTest = _.fileFolder(d)['folder']
		except Exception as e:
			folderTest = None
		
		if not os.path.isfile(d):
			if not folderTest is None and os.path.isdir(folderTest):
				this_has_been_tested_and_is_valid = True
			else:
				_.colorThis( [ 'Destination error: expected folder/file.ext' ], 'red' )
				sys.exit()
		copyfile( s, d )
		try:
			result = copyfile( s, d )
		except Exception as e:
			result = 'Error'
		if result == d:
			did = _.colorThis( 'C', 'green', p=0 )
		else:
			_.pr(result)
			did = _.colorThis( 'E', 'red', p=0 )
		_.pr(did)
		sys.exit()




	masterD = d
	masterS = s
	if not _.switches.isActive( 'Source' ):
		

		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			global patterns
			_.pipeCleaner(1)
			_pathPatterns.pipe( _.appData[__.appReg]['pipe'] )
			_pathPatterns.switch( 'JustReturn' )
			patterns = _pathPatterns.do( 'action' )

			for i,s in enumerate( _.appData[__.appReg]['pipe'] ):
				fileCopyX( s, d )

			_pathPatterns.switch( 'JustReturn' )
			_pathPatterns.pipe( masterDList )
			patterns = _pathPatterns.do( 'action' )


			try:
				for record in patterns:
					_.colorThis( [ record['folder'] ], 'cyan' )
			except Exception as e:
				pass



			_.pr()
			_.colorThis( [ '', _.addComma(totals['C']), '\tCopied' ], 'yellow' )
			_.colorThis( [ '', _.addComma(totals['S']), '\tAlready up to date' ], 'yellow' )
			_.colorThis( [ '', _.addComma(totals['E']), '\tErrors' ], 'yellow' )
			_.pr()
			complete()

		return False


	

	# _.pr( 'Source:', s )
	# _.pr( 'Destination:', d )

	# return False

	# _.pr( 'Source:', s )
	# _.pr( 'Destination:', d )


	# return False

	folderSelection( s, d )

	# _dirList.switch( 'Recursion' )
	# _dirList.switch( 'Recursion', delete=True )
	# createDestinationFoldersSrc( s, f, d )
	


totals = { 'C': 0, 'S': 0, 'E': 0  }
# add back
copyReport = { 'totals': { 'C': 0, 'S': 0, 'E': 0  }, 'records': { 'C': [], 'E': [], 'S': [],  } }
masterD = ''
masterS = ''
patterns = []
hasCleared = False
masterDList = []
masterDListX = []
# copyFoldersHere

# destinationTrigger

# usbAppsUpdate
# getFolder
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()







