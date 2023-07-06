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
	# _.switches.register( 'Database', '-db' )
	_.switches.register( 'Table', '-table' )
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', isRequired=True, description='Files' )


# _.autoBackupData = False
_.autoBackupData = __.autoCreationConfiguration['backup']
__.myFileLocations_SKIP_VALIDATION = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ls2db_cloud.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Create mogoDB collection (on cloud) based on ls.py save file ',
	'categories': [
						'tool',
						'mogoDB',
						'file',
						'ls',
						'cloud',
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
						'p ls2db_cloud -table programming  -f programming.json',
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
	__.appReg = focus()
	for i,filename in enumerate(_.isData( focus=focus() )):
		# _.pr(filename)
		# sys.exit()
		# _.pr(filename)
		# sys.exit()
		file = _.getTable2( filename )

		encrypted_connection_string = '6h0zPeDVhqMH0yIMRnOeA9NjJajbGY0HOqo4LnRgeZbx0hnInPE46WXkcl4Qu2BJFIdpCY3MCbjFeAIYLamP+aDmiFPoKsKQm5cBqVc+OfqShFLKPptf1djYtgygBlKbrG/N/H59bmhfWi5s3oQAgXEj9w6cKp2ay2QYdHkSIFDHQDJ1si3fmGg9dR1UuYpjVDi812VXYQm2/4Wgpw/CxBPTQG9zgMYjbmjEgVoI6HoyeOoEDI2r/lxpbDbsoP7mRQWwnwGZtTpbo4F/EcRavnqUJ6HUe3TLcQeF6ywFN+wHHePOrmMOlZ13Y4Qo4OSfkEGtUl+0X9Q='
		# _.pr(_blowfish.decrypt( encrypted_connection_string, _vault.key() ))
		client = pymongo.MongoClient(  _blowfish.decrypt( encrypted_connection_string, _vault.key() )  )

		db = client[  'ls2mdb'  ]
		table = db[ _.switches.values('Table')[0] ]
		try:
			table.drop()
		except Exception as e:
			pass


		keys2del = ['stat']
		for i,record in enumerate(file['data']):
			# if not i:
				# for key in record.keys():
					# if type(record[key]) == float:
					#     keys2del.append(key)
						
			for x in keys2del:
				del file['data'][i][x]
			# _.printVarSimple( file['data'][i] )
			# sys.exit()



		x = table.insert_many(file['data'])
		# _.pr(x.inserted_ids)
		_.colorThis(  [  '\n\t', "Records:", _.addComma(len(file['data']))  ], 'yellow'  )


import _rightThumb._encryptString as _blowfish
import _rightThumb._vault as _vault
import pymongo


########################################################################################
if __name__ == '__main__':
	action()







