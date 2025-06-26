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
	_.switches.register( 'Time', '-time' )
	_.switches.register( 'Print', '-print' )
	_.switches.register( 'Make', '-make', '' )
	_.switches.register( 'Count', '-cnt,-count', '4' )
	_.switches.register( 'Lists', '-lists', 'a,b,c d,e,f "g g, h h"' )
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='data', description='Files' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'permutations.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Permutations of small lists',
	'categories': [
						'tool',
						'build',
						'make',
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
						'p permutations -lists a,b,c d,e,f "g g, h h" -make " one {0} two {1} three {2} "',
						'',
						'p permutations -lists grey,red,green,yellow,blue,magenta,cyan,white grey,red,green,yellow,blue,magenta,cyan,white -make " pp new_color_test -fore {0} -back {1} "',
						'',
						'p permutations -lists  C,D,H,S  A,2,3,4,5,6,7,8,9,10,J,Q,K -make "{0}{1}" | p simpleList -flat',
						'p permutations -lists  C,D,H,S  A,2,3,4,5,6,7,8,9,10,J,Q,K -make "{1}{0}" | p simpleList -flat',
						'',
						'p permutations -count 2 -lists AC,2C,3C,4C,5C,6C,7C,8C,9C,10C,JC,QC,KC,AD,2D,3D,4D,5D,6D,7D,8D,9D,10D,JD,QD,KD,AH,2H,3H,4H,5H,6H,7H,8H,9H,10H,JH,QH,KH,AS,2S,3S,4S,5S,6S,7S,8S,9S,10S,JS,QS,KS',
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

#     grey,red,green,yellow,blue,magenta,cyan,white;grey,red,green,yellow,blue,magenta,cyan,white

def build( data ):
	if not data:
		return ''
	return "['"+"']['".join(data)+"']"

def process(lvl=0,parents=[],last=False):
	global permutations
	global highest
	global tables

	# _.pr( len(tables) )
	# sys.exit()
	try:
		for x in tables[lvl]:
			p = parents+[x]
			if not x in eval('permutations'+build(parents)):
				exec('permutations'+build(p)+'={ }')
			# _.pr(last, highest,lvl)
			
			# if last and highest==lvl:
			
			# _.pr(  len(tables) , lvl  )

			if len(tables)-1 == lvl:
				if not _.switches.isActive('Time'):
					m = ' '.join(  _.switches.values('Make')  )
					for i,z in enumerate(p):
						m = m.replace( '{'+str(i)+'}', _.color(z,'yellow',attr='bold',p=0) )
					_.pr(m)
			if len(tables) > lvl-1:
				process( lvl+1, p, last=last )
			if lvl>highest:
				highest=lvl
	except Exception as e:
		pass
		# _.pr( 'lvl',lvl )


def action():
	start=time.time()

	if _.switches.isActive('Count'):
		import _rightThumb._pID as _pID
		c = ','.join( _.switches.values('Lists') )

		y = _pID.mini.pattern( c, ',' )
		start=time.time()
		table = _pID.mini.buildPatterns(   int(  _.switches.value('Count')  ), duplicates=False   )

		# y = _pID.mini.resolve( x[0] )
		# x = _pID.mini.gen( n )
		if not _.switches.isActive('Print'):
			_.pr( time.time()-start )
			_.pr( 'code:', len(_pID.mini.code) )
			_.pr( 'table:',len(table) )
			_.pr( 'skipped:',_pID.mini.skip_count )

		# for x in _pID.mini.skip_table:
		#     _.pr(x)
		# input( ' : ' )
		if _.switches.isActive('Print'):
			for x in table:
				_.pr(x)
		# sys.exit()


	global permutations
	global tables
	permutations = {}
	l = ';'.join( _.switches.values('Lists') )
	tables = []
	spent = []
	for x in l.split(';'):
		x = _str.cleanBE( x, ' ' )
		table = []
		for y in  x.split(','):
			y = _str.cleanBE( y, ' ' )
			table.append(y)
		tables.append(table)
	if not _.switches.isActive('Count'):
		process()
	if _.switches.isActive('Time'):
		_.pr( '\ntime:', time.time()-start )

			
highest=0
 


########################################################################################
if __name__ == '__main__':
	action()







