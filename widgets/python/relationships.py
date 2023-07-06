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
##################################################

def appSwitches():
	pass
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Project', '-project', 'DnD.5e', isRequired=True )
	_.switches.register( 'Label', '-label', isRequired=True )
	_.switches.register( 'Fields', '-field,-fields' )
	_.switches.register( 'Ask', '-ask' )

	# _.switches.register( 'Search', '-search' )
	# _.switches.register( 'One', '-one' )
	# _.switches.register( 'Spaces', '-space,-spaces,-spaceing,-spacing', '0 fields' )
	# _.switches.register( 'Lines', '-lines' )
	# _.switches.register( 'Required', '-r,-required' )


__.fieldSettings = {  'primary': None, 'secondary': None, 'omit': []  }
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

def field_trigger(data):
	if '[' in data:
		data = data.replace( '[', '' )
		data = data.replace( ']', '' )
		__.fieldSettings['primary'] = data
	if '(' in data:
		data = data.replace( '(', '' )
		data = data.replace( ')', '' )
		__.fieldSettings['secondary'] = data
	return data



_.appInfo[focus()] = {
	'file': 'traverse.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Traverse a JSON file',
	'categories': [
						'traverse',
						'JSON',
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

						'p relationships -project DnD.5e  -fields classes.i.index class.index index  + cleric -label class',
						'p relationships -project DnD.5e  -list  + elf -label race',
						'',
						'n D:\\_Scott\\S_Documents\\Projects\\DND\\Research\\cmd.txt',
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
	# _.switches.trigger( 'Search', search_trigger )
	_.switches.trigger( 'Fields', field_trigger )
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	
	
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


def isINT( i, txt=False ):
	if type(i) == str:
		if len(i):
			isInt = True
			for x in i:
				if not x in '0123456789':
					isInt = False
			if isInt:
				if txt:
					return 'i'
				return int(i)
	return i




def start(thisFILE):
	if _.switches.isActive('Fields'):
		if len( _.switches.values('Fields') ) == 1:
			_.switches.fieldSet( 'Spaces', 'active', True )
			_.switches.fieldSet( 'Spaces', 'values', ['0'] )

	__.fieldSettings['omit'] = []
	global data

	if _.switches.isActive('Plus'):
		paths = []
		IDs = []
		for x in _.traverse( data, config={'inDicI':_.switches.value('Plus').replace(',',' ').lower()})['inDicI']:
			IDs.append(int(x[0]))
			# _.pr(isINT(x[0]))
			p = []
			for i,y in enumerate(x):
				# p.append( y )
				if i:
					p.append( isINT( y, txt=True ) )
			# paths.append(p)
			px = '.'.join(p)
			if not px in paths:
				paths.append(px)
				# _.pr(px)
			# _.pr(  )

		# _.pr( thisFILE, IDs )
		if len(paths):
			label = _.fileLabel(thisFILE)
			__.databases[  label  ] = data
			# _.printTest(f)
			_.pr()
			_.colorThis(  label, 'yellow' )
			fullPaths = []
			for x in paths:
				# _.pr( '\t', x )

				py = []
				py.append(label)
				py.append(x)
				pz = ':'.join(py)
				# addOption( pz )
				_.pr( '\t',pz )
				fullPaths.append( pz )


			pass
			_.pr()
			xXx = 'y'
			subjects = []
			if _.switches.isActive('Ask') and not _.switches.isActive('Fields'):
				while not xXx == 'x' and not xXx == '':
					xXx = input(' : ')
					if len( xXx) and xXx in fullPaths:
						subjects.append( xXx )
						__.chosen.append( xXx )

			elif _.switches.isActive('Fields'):
				found = False
				for fld in _.switches.values('Fields'):
					if not found:
						for xXx in fullPaths:
							if fld.lower() in xXx.lower():
								found=True
								subjects.append( xXx )
								__.chosen.append( xXx )

			_.pr()
			_.pr(subjects)
			_.pr()
			_.pr()
			_.pr()

def traverse( data, path ):
	global trav
	p = path.split('.')
	p.reverse()
	subject = p.pop()
	if subject == 'i':
		_.pr( 'Error' )
	# _.pr( subject )
	# _.pr( data[subject] )
	# _.pr( data[subject] )
	try:
		if type( data[subject] ) == str:
			trav.append( data[subject] )
		elif type( data[subject] ) == list:
			p.pop()
			p.reverse()
			path = '.'.join(p)
			for x in data[subject]:
				traverse( x, path )
		elif type( data[subject] ) == dict:
			path = '.'.join(p)
			traverse( data[subject], path )
	except Exception as e:
		_.colorThis( subject, 'red' )
		_.colorThis( data, 'red' )
		# sys.exit()

def processPath( xXx ):
	global trav
	global index

	db = xXx.split(':')[0]
	path = xXx.split(':')[1]
	index[ db ] = {
						'IDs': {},
						'items': {},
	}
	_.pr()
	_.pr()
	_.pr(db)

	for i,row in enumerate( __.databases[db] ):
		trav = []
		traverse( row, path )
		if len(trav):
			_.pr( '\t', trav )
			for x in trav:
				if not i in index[ db ]['IDs']:
					index[ db ]['IDs'][i] = {}
				if not x in index[ db ]['IDs'][i]:
					index[ db ]['IDs'][i][x] = {}
				if not x in index[ db ]['items']:
					index[ db ]['items'][ x ] = []
				if not i in index[ db ]['items'][ x ]:
					index[ db ]['items'][ x ].append(i)


trav = []
index = {}
def action():
	__.databases = {}
	__.chosen = []
	# if _.switches.isActive('Search'):
	#     _.pr( 'search active' )
	#     _.pr( _.switches.value('Search') )
	#     _.pr( _.switches.values('Search') )

	global data
	global fileFirst
	# for i,row in enumerate(_.isData(r=1)):
	for row in _.getTablesProject( '.'.join( _.switches.values('Project') ) ):

		try:
			data = _.getTable( row )
			start(thisFILE=row)
		except Exception as e:
			_.colorThis( [ 'Error: FILE' ], 'red' )
	
	_.pr()
	_.pr()
	_.colorThis('=============================================================================================================', 'green' )
	_.pr()
	_.pr()
	if len( __.chosen ):
		global index

		index_path = '.'.join( _.switches.values('Project') ) + '.relationships.registration'
		# index_file = '_'.join( _.switches.values('Label') ) + '.json'
		index_file = 'relationships.index'

		dex = _.getTableProject( index_path, index_file )

		dex[  '_'.join( _.switches.values('Label') )  ] = __.chosen

		_.saveTableProject( index_path, dex, index_file )

		for xXx in __.chosen:
			processPath( xXx )

		index_path = '.'.join( _.switches.values('Project') ) + '.relationships.indices'
		index_file = '_'.join( _.switches.values('Label') ) + '.index'
		_.saveTableProject( index_path, index, index_file )

"""
		p relationships -project DnD.5e  -fields classes.i.index class.index index  + cleric -label class
		p relationships -project DnD.5e   + elf -label race  -ask
		p relationships -project DnD.5e   + Pseudodragon -label monster  -ask
"""

########################################################################################
if __name__ == '__main__':
	action()







