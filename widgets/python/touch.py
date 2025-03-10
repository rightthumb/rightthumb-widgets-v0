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
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Folders', '-folder,-folders' )
	_.switches.register( 'Recursive', '-r,-recursive' )
	_.switches.register( 'DoNotRun', '-no,-norun' )
	# _.switches.register( 'Epoch', '-epoch' )
	_.switches.register( 'Modified', '-m,-md,-me,-mod,-modified,-t,-ts,-dt,-when,-date,-datetime', 'now' )
	_.switches.register( 'Created', '-cd,-ce,-create,-created' )
	_.switches.register( 'Undo', '-undo,-del' )
	_.switches.register( 'Accessed', '-a,-ad,-ae,-access,-accessed' )
	_.switches.register( 'Meta', '-meta', '' )


# _.autoBackupData = __.autoCreationConfiguration['backup']
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.isRequired_or_List = ['Pipe','Files','Folders']

_.appInfo[focus()] = {
	'file': 'touch.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Similar to Linux touch',
	'categories': [
						'touch',
						'tool',
						'os',
						'file',
						'files',
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
						'p touch -f Long_Lat.csv',
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
	# _.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
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






def getFolder(folder):
	for item in os.listdir(folder):
		path = folder + _v.slash + item
		if os.path.isfile(path):
			_.appData[focus()]['pipe'].append(path)
			try:
				pass
			except Exception as e:
				raise e
		elif os.path.isdir(path):
			if _.switches.isActive('Recursive'):
				try:
					getFolder(path)
				except Exception as e:
					pass


		# _.pr(psA)
		# _.pr(psB)

def process( path ):
	_.pr()
	if not os.path.isfile(path):
		_v.popFileDir(path)
		with open(path, 'w') as fp: 
			pass
	path = os.path.abspath(path)




	if not _.switches.isActive('DoNotRun') and not _.switches.isActive('Undo'):
		now = time.time()
		stampM = now
		stampA = now
		default = True
		if _.switches.isActive('Created'):
			if _.switches.value('Created') == '':
				created_date = now
			elif _.switches.value('Created') == 'now':
				created_date = now
			elif _.isFloat( _.switches.value('Created') ):
				created_date = float(_.switches.value('Created'))
			else:
				created_date = _.autoDate(' '.join( _.switches.values('Created') ))
			# _.pr(created_date)
			_.changeC( path, created_date,   meta=_.switches.isActive('Meta')   ,p=1)
			if not default:
				# _.pr(stamp)
				_.changeM( path, stampM, stampA,   meta=_.switches.isActive('Meta')   ,p=1)
		if not _.switches.isActive('Modified'):
			stampM = _dir.info(path)['me']
		if _.switches.isActive('Modified'):
			default = False
			if _.switches.value('Modified') == '':
				# print(111)
				stampM = now
			elif _.switches.value('Modified') == 'now':
				# print(222)
				stampM = now
			elif _.isFloat( _.switches.value('Modified') ):
				# print(333)
				# print(111)
				stampM = float(_.switches.value('Modified'))
			else:
				# print(444)
				stampM = _.autoDate(' '.join( _.switches.values('Modified') ))
			stampA = stampM


		if _.switches.isActive('Accessed'):
			default = False
			if _.switches.value('Accessed') == '':
				stampA = now
			elif _.switches.value('Accessed') == 'now':
				stampA = now
			elif _.isFloat( _.switches.value('Accessed') ):
				stampA = float(_.switches.value('Accessed'))
			else:
				stampA = _.autoDate(' '.join( _.switches.values('Accessed') ))





		# if not path in _.nc.tables.data:
			# _.nc.tables.data[path] = _dir.info(path)
		

		else:
			# _.pr('here')
			_.changeM( path, stampM, stampA,   meta=_.switches.isActive('Meta')   ,p=1)
	elif _.switches.isActive('Undo'):
		if os.path.isfile(path):
			path = os.path.abspath(path)
			if path in _.nc.tables.data:
				info = _.nc.tables.data[path]
				live = _dir.info( path, meta=False )
				info['ce']
				info['me']
				info['ae']

				if not _.switches.isActive('Created') and not _.switches.isActive('Modified') and not _.switches.isActive('Accessed'):
					_.changeC( path, info['ce'] ,p=1)
					_.changeM( path, info['me'], info['ae'] ,p=1)
					
				else:
					if _.switches.isActive('Created'):
						_.changeC( path, info['ce'] ,p=1)

					if _.switches.isActive('Modified') and not _.switches.isActive('Accessed'):
						_.changeM( path, info['me'], info['ae'] ,p=1)

					elif _.switches.isActive('Accessed') and not _.switches.isActive('Modified'):
						_.changeM( path, live['me'], info['ae'] ,p=1)

					elif _.switches.isActive('Accessed') and _.switches.isActive('Modified'):
						_.changeM( path, info['me'], info['ae'] ,p=1)




				# _.printVarSimple( info )


	if _.switches.isActive('Meta') and _.switches.isActive('Undo'):
		if path in _.nc.tables.meta:
			if 'epoch' in _.nc.tables.meta[path]:
				if not _.switches.isActive('Created') and not _.switches.isActive('Modified') and not _.switches.isActive('Accessed'):
					del _.nc.tables.meta[path]['epoch']
				else:
					if _.switches.isActive('Created'):
						if 'ce' in _.nc.tables.meta[path]['epoch']:
							del _.nc.tables.meta[path]['epoch']['ce']

					if _.switches.isActive('Modified') and not _.switches.isActive('Accessed'):
						if 'ae' in _.nc.tables.meta[path]['epoch']:
							del _.nc.tables.meta[path]['epoch']['ae']

					if _.switches.isActive('Modified'):
						if 'me' in _.nc.tables.meta[path]['epoch']:
							del _.nc.tables.meta[path]['epoch']['me']

					if _.switches.isActive('Accessed'):
						if 'ae' in _.nc.tables.meta[path]['epoch']:
							del _.nc.tables.meta[path]['epoch']['ae']
							

		_.saveTable( _.nc.tables.meta, 'touch.meta', p=0 )

	_.pr( path )
	



def action():

	if _.switches.isActive('Modified'):
		md = _.switches.value('Modified')
		md = str(_.autoDate(md))
		_.switches.fieldSet( 'Modified', 'value', md )
		_.switches.fieldSet( 'Modified', 'values', [md] )
		# try:
		# 	md = float(md)
		# except:
		# 	md = _.

	for fi in _.switches.values('Files'):
		if not os.path.isfile(fi):
			_.saveText('',fi)


	# sys.exit()


	# if _.switches.isActive('Files') and not os.path.isfile(_.switches.values('Files')):

	if not _.switches.isActive('Modified'):
		_.switches.fieldSet( 'Modified', 'active', True )
		_.switches.fieldSet( 'Modified', 'value', 'now' )
		_.switches.fieldSet( 'Modified', 'values', ['now'] )

	if _.switches.isActive('Modified'):
		if not _.isFloat(_.switches.value('Modified')):
			x = len(_.switches.records('dic_on-off-v')['on'])
			if x <= 1:
				_.switches.fieldSet( 'Modified', 'active', True )
				_.switches.fieldSet( 'Modified', 'value', 'now' )
				_.switches.fieldSet( 'Modified', 'values', ['now'] )


	# _.pr(x)
	# sys.exit()

	_.nc.child( 'tables' )
	_.nc.tables.data = _.getTable( 'touch.index' )
	_.nc.tables.meta = _.getTable( 'touch.meta' )

	if not _.switches.isActive('Meta') and (  _.switches.isActive('Created') or _.switches.isActive('Undo')  ):
		_.changeC_START()
		# _.PowerShell_bashrc_name_break_fix()


	if _.switches.isActive('Folders'):
		_.appData[focus()]['pipe'] = []
		if not len( _.switches.value('Folders') ):
			getFolder(os.getcwd())
		else:
			for x in _.switches.values('Folders'):
				getFolder(x)

	for i,path in enumerate(_.isData(r=1)):
		process(path)
	if not _.switches.isActive('Meta') and (  _.switches.isActive('Created') or _.switches.isActive('Undo')  ):
		# _.PowerShell_bashrc_name_break()
		_.changeC_END()
	# _.saveTable( _.nc.tables.data, 'touch.index' )

	if _.switches.isActive('DoNotRun'):
		_.colorThis( 'Did not run', 'yellow' )

import datetime
import subprocess
import _rightThumb._dir as _dir


########################################################################################
if __name__ == '__main__':
	action()







