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
	_.switches.register( 'String', '-t,-txt,-text,-string,-strings' )
	_.switches.register( 'Files', '-f,-file,-files', isPipe='name' )
	_.switches.register( 'Parts', '-p', '3' )




_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'length.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Find length of things',
	'categories': [
						'tool',
						'length',
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
						'p length -string auditJavascriptFileNamespaceAndProcessManagement a2plcpnl0385.prod.iad2.secureserver -s d.l',
						'',
	],
	'columns': [
					{ 'name': 'subject', 'abbreviation': 's,string,n,name,f,file' },
					{ 'name': 'length', 'abbreviation': 'l,r,rows' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
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
	# _.switches.trigger( 'Files', _.myFileLocations )
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


import _rightThumb._mimetype as _mime
import _rightThumb._dir as _dir

def isText(file):
	return _mime.isText(file)

def whatIsIt(file):
	if isText(file):
		result = 'Text'
	else:
		result = 'Binary'

	return result

def process( row ):
	if _.switches.isActive('Files') and _.switches.isActive('String'):
		if os.path.isfile( row ):
			if whatIsIt(row) == 'Binary':
				return _dir.info( row )['bytes']
			else:
				subject = _.getText( row, raw=1 )
		else:
			return 'Not a File'
	elif _.switches.isActive('Files') and not _.switches.isActive('String'):
		if os.path.isfile( row ):
			if whatIsIt(row) == 'Binary':
				return _dir.info( row )['bytes']
			else:
				subject = _.getText( row )
		else:
			return 'Not a File'
	elif not _.switches.isActive('Files') and _.switches.isActive('String'):
		subject = row
	return str(len( subject ))

def label( row ):

	if _.switches.isActive('Files') and _.switches.isActive('String'):
		subject = 'characters'
		if not os.path.isfile( row ):
			return 'Not a File'
		if whatIsIt(row) == 'Binary':
			subject = 'bytes'
	elif _.switches.isActive('Files') and not _.switches.isActive('String'):
		subject = 'lines'
		if not os.path.isfile( row ):
			return 'Not a File'
		if whatIsIt(row) == 'Binary':
			subject = 'bytes'
	elif not _.switches.isActive('Files') and _.switches.isActive('String'):
		subject = 'characters'
	return subject

def action():
	load()

	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		table = []
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):

			if _.switches.isActive('Parts'):
				_.pr( len(row) )
				a = int(   str(len(row)/int(_.switches.value('Parts'))).split('.')[0]   )
				_.pr(a)
				line = ''
				for i,x in enumerate(row):
					line += x
					n=i+1
					if n % a == 0:
						line += ' '

				_.pr( line )


			elif not _.switches.isActive('Parts'):
				l = label(row)
				if 'not' in l.lower():
					c = 'red'
				else:
					c = 'yellow'
				if l == 'bytes':
					c = 'bold'
				table.append({
								'subject':   _.colorThis( row, 'yellow', p=0 ),
								'length':   _.colorThis( _.addComma(process(row)), 'green', p=0 ),
								'label':   _.colorThis( l, c, p=0 )
							})
				# table.append({
				#                 'subject':   row,
				#                   'length':   process(row),
				#                   'label':   label(row),
				#             })

			pass
			_.fields.asset( 'length', table )
			_.pr()
			for record in table:
				row = '\t'
				row += _.fields.value( 'length', 'length',   record['length'], right=1   )
				row += '  '
				row += _.fields.value( 'length', 'label',   record['label']   )
				row += '\t'
				row += _.fields.value( 'length', 'subject',   record['subject'], right=1   )
				_.pr( row )
			_.pr()



def load():
	global data
	if type( _.appData[__.appReg]['pipe'] ) == bool:
		if _.switches.isActive('String'):
			_.appData[__.appReg]['pipe'] = _.switches.values('String')
		if _.switches.isActive('Files'):
			_.appData[__.appReg]['pipe'] = _.switches.values('Files')
	else:
		if not _.switches.isActive('Files') and not _.switches.isActive('String'):
			if os.path.isfile(  _.appData[__.appReg]['pipe'][0]  ):
				_.switches.fieldSet( 'Files', 'active', True )
			else:
				_.switches.fieldSet( 'String', 'active', True )
			



"""
	if _.switches.isActive('String'):

		table = []
		for string in _.switches.values('String'):
			table.append({ 'string': string, 'length': len(string) })
		if _.switches.isActive('Sort'):
			table = _.tables.returnSorted( 'strings', _.switches.value('Sort'), table )
		_.fields.asset( 'strings', table )
		_.pr()
		for record in table:
			row = '\t'
			row += _.fields.value( 'strings', 'string', record['string'], right=1 )
			row += '\t'
			row += _.fields.value( 'strings', 'length', record['length'] )
			_.pr( row )
		_.pr()
"""


		# for string in _.switches.values('String'):
		#     table.append({ 'string':   _.colorThis( string, 'yellow', p=0 )   , 'length':   _.colorThis( len(string), 'green', p=0 )   })
		# _.pr()
		# _.fields.asset( 'strings', table )
		# _.pr()
		# for record in table:
		#     row = '\t'
		#     row += _.fields.value( 'strings', 'string',   _.colorThis( record['string'], 'yellow', p=0 )   )
		#     row += '\t'
		#     row += _.fields.value( 'strings', 'length',   _.colorThis( record['length'], 'green', p=0 )   )
		#     _.pr( row )
		# _.pr()


########################################################################################
if __name__ == '__main__':
	action()