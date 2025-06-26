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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='glob', description='Files', isRequired=True )
	_.switches.register( 'Implode', '-i,-imp,-implode' )
	_.switches.register( 'Explode', '-e,-x,-explode' )
	_.switches.register( 'Add', '-add', 'name;scott py;python3' )
	_.switches.register( 'Clean1', '-cc' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Order', '-o,-order', 'name year  OR  n y' )
	_.switches.register( 'Alphabetical', '-alpha' )
	_.switches.register( 'Delete', '-del,-delete', 'testing' )
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
	'file': 'hash.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manipulate hash file',
	'categories': [
						'index',
						'hash',
						'hashtable',
						'table',
						'manipulate',
						'indent',
						'flatten',
						'flat',
						'explode',
						'format',
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
						'p hash -f file.json -implode -add name;scott -order name year',
						'',
						'p hash -f 2file.json -add name;scott year;2021 -implode',
						'p hash -f 2file.json ',
						'p hash -f 2file.json -add py;python3',
						'p hash -f 2file.json -i',
						'',
						'p hash -f 2file.json -alpha',
						'p hash -f 2file.json -order name year py',
						'',
						'p hash -f 2file.json -order p n',
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

	fileBackup = _.regImp( focus(), 'fileBackup' )
	fileBackup.switch( 'Silent' )
	fileBackup.switch( 'Flag', 'hash' )
	fileBackup.switch( 'isRunOnce' )
	fileBackup.switch( 'DoNotSchedule' )

	for i,file in enumerate( _.isData(r=1) ):
		if file == '?config':
			file = _v.home +os.sep+'.rt'+os.sep+ '.config.hash'
		if file == '??config':
			file = _v.myConfig + os.sep + '.config.hash'
		sort_keys  = False
		indentCode = True


		if not os.path.isfile(file):
			data = {}
		elif os.path.isfile(file):
			fileBackup.switch( 'Input', file )
			fb = fileBackup.action()
			# if not _.switches.isActive('Clean'):
			#     _.pr( fb )
			data = _.getTable2( file )
		if not type(data) == dict:
			_.cp( 'Error: not dic', 'red' )
			_.pr(data)
			return None
		if _.switches.isActive('Add'):
			for add in _.switches.values('Add'):
				item = add.split(';')
				# _.pr(item)
				data[ item[0] ] = item[1]
		if _.switches.isActive('Order'):
			newData = {}
			theOrder = _.switches.values('Order')
			for i,order in enumerate(theOrder):
				if not order in data:
					for k in data:
						if k.lower().startswith(order.lower()):
							theOrder[i] = k
							break
			for order in theOrder:
				if order in data:
					newData[order] = data[order]

			for k in data:
				if not k in _.switches.values('Order'):
					newData[k] = data[k]
			data = newData
		if _.switches.isActive('Alphabetical'):
			sort_keys = True
		if _.switches.isActive('Delete'):
			theOrder = _.switches.values('Delete')
			for i,order in enumerate(theOrder):
				if not order in data:
					for k in data:
						if k.lower().startswith(order.lower()):
							theOrder[i] = k
							break
			for d in theOrder:
				ask = input( 'Delete: '+d+'?  ' )
				if not ask.lower().startswith('n'):
					if d in data:
						del data[d]


		# if not _.switches.isActive('Clean'):
		#     _.pv(data)
		if _.switches.isActive('Implode'):
			indentCode = False
		if _.switches.isActive('Explode'):
			indentCode = True
		if data:
			_.saveTable2( data, file, sort_keys=sort_keys, indentCode=indentCode )
		elif os.path.isfile(file):
			os.unlink(file)
		if not os.path.isfile(file):
			_.e( 'does not exist', file )
		else:
			test = _.getText( file, raw=True )
			if not _.switches.isActive('Clean'):
				if not _.switches.isActive('Clean1'):
					_.pr()
				_.pr(test)
				if not _.switches.isActive('Clean1'):
					_.pr()
					_.pr(os.path.abspath(file))
					try:
						_.pr( fb )
					except Exception as e:
						pass




########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()







