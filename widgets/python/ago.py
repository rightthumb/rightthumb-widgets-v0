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
	_.switches.register( 'Ago', '-ago', ' 2min 1h 1d 1w 1m 1y ' )
	_.switches.register( 'Future', '-fu,-future', ' 2min 1h 1d 1w 1m 1y ' )
	_.switches.register( 'Epoch', '-e,-epoch' )
	_.switches.register( 'Date', '-d,-date' )
	_.switches.register( 'WOY', '-woy' )
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'TimeZone', '-tz', '+0400  OR  US/Mountain  OR  all' )
	_.switches.register( 'Ordinal', '-ordinal' )
	_.switches.register( 'nID', '-nID' )
	_.switches.register( 'Fields', '-f,-field,-fields' )
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ago.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Ago epoch',
	'categories': [
						'time',
						'ago',
						'tool',
						'epoch',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						# 'p another -file file.txt',
						'p ago | p fileLine -line 1 | p line --c -make "p randomTool -around {}" | p execute --c | p line --c -make "p ago -epoch {}" | p execute',
						'',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						'p ago -ago 1y ',
						'',
						'p ago -ago +1m.+1w',
						'',
						'p ago -ago 1y 1y.1m.1w',
						'p ago -ago +1m.-4d',
						'',
						'p ago -ago 2020-01-19 2019-01-19',
						'p ago -ago 2020-01-19',
						'',
						'p ago -ago 1998-11-21',
						'p ago -ago 1980-07-16',
						'p ago -ago 1998-11-21 1980-07-16',
						'',
						'p ago -epoch 1606841831.3583136',
						'',
						'',
						'p ago -tz all + / | p line -p / 0 | p countEach',
						'',
						'p ago -date 2014-08-30T18:30:00+03:00',
						'p ago -date 2014-08-30T00:30:00+03:00',
						'p ago -date 2014-08-30T00:30:00+03:00 -tz America/New_York',
						'p ago -date 2014-08-30T00:30:00+03:00 -tz US/Eastern',
						'p ago -date 2014-08-30T18:30:00+03:00 -tz US/Mountain',
						'',
						'p ago -tz US/Mountain',
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


def epoch2float(data):
	return float(data)


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
	_.switches.trigger( 'Ago', _.Ago )
	_.switches.trigger( 'Duration', _.timeFuture )
	_.switches.trigger( 'Future', _.timeFuture )
	_.switches.trigger( 'Epoch', epoch2float )
	_.switches.trigger( 'Date', _.autoDate )
	
	
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

import datetime

def process():

	if _.switches.isActive('nID'):
		import _rightThumb._nID as _nID
		# _nID.mini.password( '1970' )
		_nID.mini.password( _keychain.imp.key('nID') )

		for o in _.switches.values('nID'):
			oo = str(_nID.mini.resolve( o ))
			t = ''
			# if len(oo) == 8:
			if len(oo) == 8 or len(oo) == 14:
				for i,c in enumerate(oo):
					if i == 4 or i == 6:
						t += '-'
					if i == 8:
						t += ' '
					if i == 10 or i == 12:
						t += ':'


					# _.pr(i,c)

					t += c
			else:
				t = int(oo)
				

			_.pr()
			_.printDicFields( _.isDate( t, tz=_.switches.value('TimeZone') ) )
			_.pr()
		return None

		
		_.printDicFields( _.isDate( oo, tz=_.switches.value('TimeZone') ) )
		return None
	if _.switches.isActive('Ordinal'):
		for o in _.switches.values('Ordinal'):
			oo = datetime.date.fromordinal(int(o))
			_.pr()
			_.printDicFields( _.isDate( oo, tz=_.switches.value('TimeZone') ) )
			_.pr()
		return None

	if _.switches.isActive('Test'):
		table = []
		now = time.time()
		i=0
		now = _.days_math( now, 100, '+' )
		while not i == 200:
			i+=1
			if i % 1 == 0:
				xyz = _.days_math( now, i, '-' )
				table.append({ 'diff': _.time_diff(xyz), 'date': _.friendlyDate(xyz), 'epoch': xyz })
		

		_.tables.register( 'data', table )

		if not _.switches.isActive('Sort'):
			_.switches.fieldSet( 'Sort', 'active', True )
			_.switches.fieldSet( 'Sort', 'value', 'epoch' )
			_.switches.fieldSet( 'Sort', 'values', ['epoch'] )

		if not _.switches.isActive('GroupBy'):
			_.switches.fieldSet( 'GroupBy', 'active', True )
			_.switches.fieldSet( 'GroupBy', 'value', 'diff' )
			_.switches.fieldSet( 'GroupBy', 'values', ['diff'] )

		if not _.switches.isActive('Column'):
			_.tables.print( 'data', 'diff,date,epoch' )
		else:
			_.tables.print( 'data', _.switches.value('Column') )




	elif _.switches.isActive('Date'):
		# _.pr( _.autoDate( _.switches.value('Date') ) )
		# _.pr( _.getWOY(_.switches.value('Date')) )
		# _.pr( _.time_diff( _.switches.value('Date') ) )
		# _.pr()
		# _.pr( _.daysDiff( _.autoDate(_.switches.value('Date')), time.time() ), 'days' )
		# _.pr()
		_.printDicFields( _.isDate( _.switches.value('Date'), tz=_.switches.value('TimeZone') ) )
		

	elif _.switches.isActive('Epoch'):
		# _.pr( _.friendlyDate(_.switches.value('Epoch')) )
		# _.pr( _.getWOY( _.switches.value('Epoch') ) )
		# _.pr( _.time_diff(_.switches.value('Epoch')) )

		_.printDicFields( _.isDate( float(_.switches.value('Epoch')), tz=_.switches.value('TimeZone') ) )
		


	elif _.switches.isActive('Future'):
		for i,future in enumerate(_.switches.values('Future')):
			_.printDicFields( _.isDate( _.switches.values('Future')[i], tz=_.switches.value('TimeZone') ) )
			_.pr('_________________________________________________________')
	elif _.switches.isActive('Ago'):

		if len(_.switches.values('Ago')) > 1:
			_.pr( _.dateDiffText(  _.switches.values('Ago')[0], _.switches.values('Ago')[1]  ) )
			_.pr('_______________')
			_.pr()
			
		for i,ago in enumerate(_.switches.values('Ago')):
			# _.pr( _.switches.values('Ago')[i] )
			# _.pr( (time.time() - _.switches.values('Ago')[i]) )
			# _.pr( _.friendlyDate(_.switches.values('Ago')[i]) )
			# _.pr( _.getWOY(_.switches.values('Ago')[i]) )
			# _.pr( _.time_diff(_.switches.values('Ago')[0]) )
			# _.pr()
			# _.pr()
			# _.pr( _.dateDiffText( _.switches.values('Ago')[i] ) )
			# _.pr()
			# _.pr( _.daysDiff( _.switches.values('Ago')[i], time.time() ), 'days' )
			# _.pr()
			_.printDicFields( _.isDate( _.switches.values('Ago')[i], tz=_.switches.value('TimeZone') ) )
			# _.pr()
			_.pr('_________________________________________________________')
		# _.pr( _.days_in_month( 5, 1980 ) )
		# # sys.exit()
		# _.pr()
		# _.pr( _.dateDiffDic(  time.time(), _.switches.value('Ago')  ) )

	elif _.switches.isActive('WOY'):
		d = _.woy2dates( _.switches.value('WOY') )
		f = _.woy2datesFriendly( _.switches.value('WOY') )
		_.pr( '      ', d[0], '  -  ', d[1] )
		_.pr( f[0], '  -  ', f[1] )
	else:
		epoch = time.time()
		# _.pr( 'Now' )
		# _.pr( epoch )
		# _.pr( _.friendlyDate(epoch) )
		# _.pr( _.getWOY(epoch) )
		# _.pr( _.time_diff(epoch) )
		# _.pr()
		_.printDicFields( _.isDate( epoch, tz=_.switches.value('TimeZone') ) )
		if False:
			_.pr()
			_.pr()
			_.pr()
			months = 2
			_.pr( months )
			xXx = _.monthMath( epoch, months, do='+' )
			_.pr( xXx )
			_.pr( _.friendlyDate(xXx) )
			_.pr( _.time_diff(xXx) )
			_.pr( _.monthsDiff( epoch, xXx ) )
			_.pr()
			# _.pr()
			xXx = _.monthMath( epoch, months, do='-' )
			_.pr( xXx )
			_.pr( _.friendlyDate(xXx) )
			_.pr( _.time_diff(xXx) )
			_.pr( _.monthsDiff( epoch, xXx ) )
			_.pr()
			_.pr()



def action():
	if _.switches.isActive('Fields'):
		fields = '''
				epoch
			ordinal
			text-date
			text-time
		text-datetime
				sdate
				strip
			stript
				date
				time
				fdate
				month
				year
				woy
				dow
				ago
				days
				tz
				iso
		crypt-date
		crypt-time
		crypt-epoch
				appID
		crypt-pass
			stardate
			quarter
		'''
		fields = fields.replace(' ','')
		fields = fields.replace('\t','')
		fields = _str.do( 'dup', fields, '\n' )
		fields = _str.do( 'be', fields, '\n' )
		f = fields.split('\n')
		# _.pv(f)
		# sys.exit()
		# return None
		pass
		if not _.switches.value('Fields'):
			return None

		# for field in f:
		for field in _.switches.values('Fields'):
			x=_.isDate(time.time(),f=field)
			# _.pr(field,x)
			_.pr(x)
			# _.cp( ,  )

		return None

	if _.switches.value('TimeZone') == 'all':
		import pytz
		for x in pytz.all_timezones:
			if _.showLine(x):
				_.pr(x)

		return None


	if True:
		process()
	else:
		try:
			process()
		except Exception as e:
			_.colorThis( [ 'Error: input' ], 'red' )



import datetime

import _rightThumb._dir as _dir
_keychain = _.regImp( __.appReg, 'keychain' )

########################################################################################
if __name__ == '__main__':
	action()