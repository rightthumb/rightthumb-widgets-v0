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
	_.switches.register( 'Good', '-good' )
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'MoveIndexes', '-move' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'clean_bm.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Remove bookmarks that no longer exist',
	'categories': [
						'clean',
						'bm',
						'bookmarks',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'create bookmark to current folder',
						'    p m -a test',
						'list all bookmarks',
						'    p bookmarks',
						'quick generate bookmarks if blank',
						'   p bm-dirty | bash',
						'remove all bookmarks that no longer exist',
						'    p clean-bm -good -save',
						'bookmark location',
						'    p b -a ww',
						# '',
						# 'old not sure what it does',
						# '    p cleanBookmarks -?',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p clean_bm',
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



def action():

	# if not os.path.isfile(  _v.dbTables  +_v.slash+ 'bookmarks.index'  ):
	#     _.colorThis( [ '' ] )

	# _.pr( _v.thisHost )
	# sys.exit()

	# folderID_host folderID_techApps folderID_alt

	load()
	global data

	index = {
				'labels': {},
				'paths': {},
	}


	# paths labels
	if True:
		for subject in data['labels'].keys():

			for y in _.caseUnspecific(  data['labels'][subject]  ,  'c:\\tech'  ):

				_.pr()
				_.colorThis( data['labels'][subject], 'cyan' )
				data['labels'][subject] = data['labels'][subject].replace( y, _v.folderID_tech )
				_.colorThis( data['labels'][subject], 'cyan' )
				_.pr()
			
			for y in _.caseUnspecific(  data['labels'][subject]  ,  'C:\\Users\\Scott'  ):
				_.pr()
				_.colorThis( data['labels'][subject], 'cyan' )
				data['labels'][subject] = data['labels'][subject].replace( y, _v.folderID_profile )
				_.colorThis( data['labels'][subject], 'cyan' )
				_.pr()

			for y in _.caseUnspecific(  data['labels'][subject]  ,  'hosts\\VULCAN'  ):
				_.pr()
				_.colorThis( data['labels'][subject], 'cyan' )
				data['labels'][subject] = data['labels'][subject].replace( y, _v.folderID_host )
				_.colorThis( data['labels'][subject], 'cyan' )
				_.pr()



			if 'c:\\tech' in data['labels'][subject].lower():
				data['labels'][subject] = data['labels'][subject].replace(  )
			if not os.path.isdir( _v.resolveFolderIDs(data['labels'][subject]) ):
				if not _.switches.isActive('Good'):
					_.colorThis( [ _v.resolveFolderIDs(data['labels'][subject]) ], 'red' )
				# del data['labels'][subject]
			else:
				index['labels'][subject] = data['labels'][subject]
				if _.switches.isActive('Good'):
					_.colorThis( [ _v.resolveFolderIDs(data['labels'][subject]) ], 'green' )

	if True:
		for subject in data['paths'].keys():


			subjectNEW = subject
			for y in _.caseUnspecific(  subject  ,  'c:\\tech'  ):
				subjectNEW = subject.replace( y, _v.folderID_tech )
			
			for y in _.caseUnspecific(  subject  ,  'C:\\Users\\Scott'  ):
				subjectNEW = subject.replace( y, _v.folderID_profile )

			for y in _.caseUnspecific(  subject  ,  'hosts\\VULCAN'  ):
				subjectNEW = subject.replace( y, _v.folderID_profile )

			temp = None
			if not subject == subjectNEW:
				_.pr()
				_.colorThis( subject, 'cyan' )
				_.colorThis( subjectNEW, 'cyan' )
				_.pr()
				if not os.path.isdir( _v.resolveFolderIDs(subjectNEW) ):
					if not _.switches.isActive('Good'):
						_.colorThis( [ _v.resolveFolderIDs(subjectNEW) ], 'red' )
					# del data['paths'][subject]
				else:
					index['paths'][subjectNEW] = data['paths'][subject]
					if _.switches.isActive('Good'):
						_.colorThis( [ _v.resolveFolderIDs(subjectNEW) ], 'green' )


			else:
				if not os.path.isdir( _v.resolveFolderIDs(subject) ):
					if not _.switches.isActive('Good'):
						_.colorThis( [ _v.resolveFolderIDs(subject) ], 'red' )
					# del data['paths'][subject]
				else:
					index['paths'][subject] = data['paths'][subject]
					if _.switches.isActive('Good'):
						_.colorThis( [ _v.resolveFolderIDs(subject) ], 'green' )


	if _.switches.isActive('Save'):
		if os.path.isfile(  _v.dbTables  +_v.slash+ 'bookmarks.index'  ):
			_.saveTableDB( index, 'bookmarks.index' )
		elif os.path.isfile(  _v.myTables  +_v.slash+ 'bookmarks.index'  ):
			_.saveTable( index, 'bookmarks.index' )

		_.colorThis(  [ '\n','Saved' ] , 'yellow' )
	else:
		if not _.switches.isActive('MoveIndexes'):
			_.colorThis(  [ '\n','Not saved' ] , 'yellow' )


	if _.switches.isActive('MoveIndexes'):
		found = False
		if os.path.isfile(  _v.dbTables  +_v.slash+ 'bookmarks.index'  ):
			if not os.path.isfile(  _v.myTables  +_v.slash+ 'bookmarks.index'  ):
				found = True
				shutil.move(   _v.dbTables  +_v.slash+ 'bookmarks.index'   ,   _v.myTables  +_v.slash+ 'bookmarks.index'   )
			else:
				found = True
				_.colorThis(  [ '\n','Already moved:', 'bookmarks.index', 'copy in databank and myTables' ] , 'red' )

			_.colorThis(  [ '\n','Moved:', 'bookmarks.index' ] , 'yellow' )
		if os.path.isfile(  _v.dbTables  +_v.slash+ 'bookmarks.logs'  ):
			found = True
			shutil.move(   _v.dbTables  +_v.slash+ 'bookmarks.logs'   ,   _v.myTables  +_v.slash+ 'bookmarks.logs'   )
			_.colorThis(  [ '\n','Moved:', 'bookmarks.logs' ] , 'yellow' )
		if not found:
			if os.path.isfile(  _v.myTables  +_v.slash+ 'bookmarks.index'  ):
				_.colorThis(  [ '\n','Already moved:', 'bookmarks.index' ] , 'yellow' )

			if os.path.isfile(  _v.myTables  +_v.slash+ 'bookmarks.logs'  ):
				_.colorThis(  [ '\n','Already moved:', 'bookmarks.logs' ] , 'yellow' )



def load():
	global data
	if os.path.isfile(  _v.dbTables  +_v.slash+ 'bookmarks.index'  ):
		data = _.getTableDB( 'bookmarks.index' )
	elif os.path.isfile(  _v.myTables  +_v.slash+ 'bookmarks.index'  ):
		data = _.getTable( 'bookmarks.index' )
	else:
		_.colorThis(  [ ' Error: bookmarks.index is missing ' ], 'red'  )
		sys.exit()

import shutil



########################################################################################
if __name__ == '__main__':
	action()