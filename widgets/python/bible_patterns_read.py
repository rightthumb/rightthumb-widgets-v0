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


	


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'bible_patterns_read.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Search the index for patterns',
	'categories': [
						'Bible',
						'research',
						'bible study',
						'study',
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
						'p bible_patterns_read + ps',
						'p bible_patterns_read + lam',
						''
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# __.appRegPipe
########################################################################################
# START


def newAbbreviations():
	global theBooks
	global booksRaw
	global sections

	for i,br in enumerate(booksRaw):
		br = br.replace('\n','').replace('.','')
		# _.pr( br )
		abbreviation = br.split(',')[1]
		n = {
				'book':        br.split(',')[0],
				'abbreviation':    br.split(',')[1],
				'minimal':    sections[str(i)]['abbreviation']
		}
		theBooks.append( n )

def action():
	global theBooks
	global data
	global patterns
	global theBible
	load()

	# for key in data.keys():
	#     _.pr( key, len( data[key] ) )

	# _.pr( len(_.appData[__.appReg]['pipe']) )

	for i,book in enumerate(theBooks):
		if _.showLine( book['book'] ):
			_.pr( i+1,'\t', book['book'] )


	myBook = None
	try:
		book=input(' Choose book:  ')
		book=int( book )-1
		myBook= theBooks[ book ]['abbreviation']
		chapter=input(' Chapter:  ')
		verse=input(' Verse:  ')
		for i,index in enumerate(data[ myBook+' '+chapter+':'+verse ]):
			_.pr( i,'\t',index.split('-')[1], '\t', index.split('-')[0] )
		pat=int(input(' Select:  '))
		for record in patterns[ data[ myBook+' '+chapter+':'+verse ][pat].split('-')[0] ]:
			_.pr()
			_.pr()
			_.pr()
			_.pr( record['verse'], '\t', _str.stripNonAlphaNumaric(  _str.replaceDuplicate( theBible[ int(record['id']) ].replace( '\t', '   ' ), '  ' ).split('  ')[4].replace( eCV(record['verse'])[0], '' ).replace( eCV(record['verse'])[1], '' )   ) )

	except Exception as e:
		pass

def eCV( ref ):
	parts = ref.split(' ')
	for x in parts:
		if ':' in x:
			return x.split(':')


def load():
	global data
	global theBooks
	global booksRaw
	global sections
	global patterns
	global theBible

	theBible = _.getText( 'b_av.txt', raw=1 ).split('\n')
	patterns = _.getTable2( 'bible_patterns_min_3.json' )
	sections = _.getTable('Bible_section_headers.json')
	booksRaw = _.getText(_v.myTables + _v.slash+'bible_books.csv')
	data = _.getTable2( 'bible_patterns_verses.json' )
	newAbbreviations()


theBooks = []
data = []
########################################################################################
if __name__ == '__main__':
	action()







