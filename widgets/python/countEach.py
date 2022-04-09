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
__.registeredApps.append(focus())


import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	pass
	# _.switches.register('Input', '-i,-input','file.txt')
	_.switches.register('Files', '-f,-file,-files','file.txt')
	_.switches.register('SkipFirst', '-first,-skip')
	_.switches.register('CleanBE', '-clean')
	_.switches.register('NoCount', '--c')
	

_.autoBackupData = False


_.appInfo[focus()] = {
	'file': 'countEach.py',
	'description': 'Count Occurances in pipe data',
	'categories': [
						'pipe',
						'pattern',
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
						'type %tmpf0% | p countEach',
						'',
						'p countEach -f %tmpf0% + \\ -clean \\ - dns winsock crypt Tcp',
						'',
						'type %tmpf8% | p line + : - http --c | p simpleList -split " " n -remove : "," -case lower -stems tiktok | p simpleList | p countEach',
						'',
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
	__.constructRegistration(_.appInfo[__.appReg]['file'],__.appReg)
	appSwitches()

	_.myFileLocation_Print = False
	_.switches.trigger('Files',_.myFileLocations)
	# _.switches.trigger('Files',_.inRelevantFolder)
	

	# _.switches.trigger('Watched', _.txt2Date)
	# _.switches.trigger('Input',_.formatColumns)
	# _.switches.trigger('Franchise',_.triggerSpace)
	
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


_.appData[__.appReg]['pipe'] = False
if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg )

_.postLoad( __file__ )

########################################################################################
# p = _.getText( _v.pips, raw=True, clean=True ).split('\n')
# os.system('"' + do + '"')
########################################################################################
# START

def action():

	_.fields.register( 'cnt', 'val', 7, m=4 )
	test = _.fields.padZeros( 'cnt', 'val', 5 )

	if _.switches.isActive('Files'):
			tmpFiles = []
			for file in _.switches.values('Files'):
				if os.path.isfile( file ):
					for row in _.getText( file, raw=True, clean=2 ).split('\n'):
						tmpFiles.append( row )
			_.setPipeData( tmpFiles, focus() )

	if type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pr( 'Error: no input' )
		sys.exit()

	dic = []
	_.pipeCleaner(2)
	# _.pr( _.appData[__.appReg]['pipe'] )
	# if len(_.appData[__.appReg]['pipe']) == 1:
	# 	_.pr()
	# 	_.pr(  '  1      ', _.appData[__.appReg]['pipe'][0]  )
	for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
		row = row.replace( '\n', '' )
		row = row.replace( '\r', '' )
		original = row
		row = row.lower()
		row = _str.clean_latin1( row )
		row = _str.replaceDuplicate( row,' ' )
		row = _str.cleanBE( row,' ' )
		
		if _.switches.isActive( 'CleanBE' ) and len( _.switches.values( 'CleanBE' ) ) :
			for clean in _.switches.values( 'CleanBE' ):
				row = _str.cleanBE( row, clean )
				original = _str.cleanBE( original, clean )


		if len( row ):
			# _.pr('here')
			dic.append({ 'original': original, 'sortable': row })

	data = _.tables.returnSorted( 'data', 'a.sortable', dic )
	if not len(data):
		last = { 'original': '', 'sortable': '' }
	else:
		last = { 'original': data[0]['original'], 'sortable': data[0]['sortable'] }
	count = 0
	result = []
	groupCNT = 0
	# _.printVarSimple(data)
	counter = {}
	spent = {}
	for record in data:
		count += 1
		if not record['sortable'] in counter:
			counter[record['sortable']] = 0
		counter[record['sortable']] +=1

		if not record['sortable'] == last['sortable']:
			if _.switches.isActive('SkipFirst'):
				if len(last['sortable']) > 0:
					result.append({ 'cnt': count, 'record': last })
					spent[last['sortable']] = 1
			else:
				result.append({'cnt': count, 'record': last})
				spent[last['sortable']] = 1
			count = 0
		last = record
	# _.pr(data[ len(data)-1 ]['sortable'])
	# _.pr(data[ len(data)-1 ]['sortable'] in spent)
	# _.printVarSimple(result)
	# _.pr( spent.keys() )

	if not data[ len(data)-1 ]['sortable'] in spent:
		# _.pr( data[ len(data)-1 ] )
		# _.pr( spent[data[ len(data)-1 ]['sortable']] )
		result.append({'cnt': counter[data[ len(data)-1 ]['sortable']]  , 'record': data[ len(data)-1 ]})
	result0 = _.sort(result,'cnt')

	# _.printVarSimple(result0)
	if not _.switches.isActive( 'NoCount' ):
		for data in result0:
			if _.showLine( data['record']['original'] ):
				# _.pr( 'here:', data )
				if len(data['record']['original']):
					# _.pr('',data['cnt'],'\t\t',data['record']['original'])
					# _.pr('',data['cnt'],'\t',data['record']['original'])
					_.pr('',  _.fields.padZeros( 'cnt', 'val', data['cnt'], space=True )  ,'\t',data['record']['original'])
					groupCNT+=1
	else:
		for data in result0:
			if _.showLine( data['record']['original'] ):
				_.pr(data['record']['original'])


	_.colorThis(  [ '\n','  ','groups:', _.addComma( groupCNT ) ], 'yellow'  )
	_.colorThis(  [ '  ','  items:', _.addComma( len(_.appData[__.appReg]['pipe']) ) ], 'yellow'  )


# def load():
# 	global data
# 	data = _.getTable( 'table.json' )
# data = []
########################################################################################
if __name__ == '__main__':
	action()







