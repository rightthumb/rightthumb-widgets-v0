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
	_.switches.register( 'Database', '-db' )
	_.switches.register( 'Table', '-table' )
	_.switches.register( 'Query', '-q,-query' )
	_.switches.register( 'Mode', '-mode', ' table OR json' )
	_.switches.register( 'AND', '-and' )
	_.switches.register( 'OR', '-or' )
	_.switches.register( 'Fields', '-field,-fields' )
	_.switches.register( 'Clean', '--c' )


# _.autoBackupData = False
_.autoBackupData = __.autoCreationConfiguration['backup']
__.myFileLocations_SKIP_VALIDATION = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = [ 'Query' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ls2db_cloud_query.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Query mogoDB collection  ',
	'categories': [
						'tool',
						'mogoDB',
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
						'p ls2db_cloud_query',
						'',
						'',
						'',
						'',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "{\'name\': \'ls.py\'}" ',
						'',
						# 'p ls2db_cloud_query -db ls2mdb -table programming -q name: *.py, ls* ; folder: programs ',
						'',
						# 'p ls2db_cloud_query -db ls2mdb -table programming -q name: *.py -field path',
						'',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "ext: \'py\' ; path: *ls.py" -field path',
						# '',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "ext: \'py\' ; path: *ls.py" -field path -or',
						'',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "name: ls*"  -field path',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "name: ls* ; ext: \'py\'" -field path',
						'',
						'',
						' p ls2db_cloud_query -db ls2mdb -table programming -q "folder: *programs*" -field path',
						'',
						'',
						'p ls2db_cloud_query -db ls2mdb -table programming -q "folder: *programs* ; ext: \'py\' ; name: ls*" -field path',
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

indexed_fields_hash = {}
indexed_fields_checked = False
def indexed_fields(client):
	global indexed_fields_hash
	global indexed_fields_checked
	if indexed_fields_checked:
		return indexed_fields_hash
	indexed_fields_checked = True
	if not  list(client.list_database_names()):
		return indexed_fields_hash
	if not 'my_indexes' in client['collection_management'].list_collection_names():
		return indexed_fields_hash

	for record in client['collection_management']['my_indexes'].find({}):
		db = record['db']
		table = record['table']
		field = record['field']
		if not db in indexed_fields_hash:
			should_index = True
			indexed_fields_hash[db] = {}
			indexed_fields_hash[db][table] = {}
			indexed_fields_hash[db][table][field] = {}
		elif not table in indexed_fields_hash[db]:
			indexed_fields_hash[db][table] = {}
			indexed_fields_hash[db][table][field] = {}
			should_index = True
		elif not field in indexed_fields_hash[db][table]:
			indexed_fields_hash[db][table][field] = {}

	return indexed_fields_hash
		# _.pr(record)

def index_field( client, db, table, field ):
	global indexed_fields_hash
	global indexed_fields_checked
	if not indexed_fields_checked:
		indexed_fields(client)

	should_index = False
	if not db in indexed_fields_hash:
		should_index = True
		indexed_fields_hash[db] = {}
		indexed_fields_hash[db][table] = {}
		indexed_fields_hash[db][table][field] = {}
	elif not table in indexed_fields_hash[db]:
		indexed_fields_hash[db][table] = {}
		indexed_fields_hash[db][table][field] = {}
		should_index = True
	elif not field in indexed_fields_hash[db][table]:
		indexed_fields_hash[db][table][field] = {}
		should_index = True
	# should_index = True
	if should_index:
		resp = client[db][table].create_index([ (field, 1) ])
		_.pr( 'indexing result:', resp )

		client['collection_management']['my_indexes'].insert_one({
				'db': db,
				'table': table,
				'field': field
			})


def action():

	encrypted_connection_string = '6h0zPeDVhqMH0yIMRnOeA9NjJajbGY0HOqo4LnRgeZbx0hnInPE46WXkcl4Qu2BJFIdpCY3MCbjFeAIYLamP+aDmiFPoKsKQm5cBqVc+OfqShFLKPptf1djYtgygBlKbrG/N/H59bmhfWi5s3oQAgXEj9w6cKp2ay2QYdHkSIFDHQDJ1si3fmGg9dR1UuYpjVDi812VXYQm2/4Wgpw/CxBPTQG9zgMYjbmjEgVoI6HoyeOoEDI2r/lxpbDbsoP7mRQWwnwGZtTpbo4F/EcRavnqUJ6HUe3TLcQeF6ywFN+wHHePOrmMOlZ13Y4Qo4OSfkEGtUl+0X9Q='
	# _.pr(_blowfish.decrypt( encrypted_connection_string, _vault.key() ))
	client = pymongo.MongoClient(  _blowfish.decrypt( encrypted_connection_string, _vault.key() )  )

	theDB = 'ls2mdb'
	if _.switches.isActive('Database'):
		theDB = _.switches.values('Database')[0]

	global indexed_fields_hash
	indexed_fields(client)
	# _.printVarSimple( indexed_fields_hash )
	if not _.switches.isActive('Database') and not _.switches.isActive('Table'):

		omit = [ 'collection_management', 'admin', 'local' ]
		omit.pop(0)
		for x in client.list_database_names():
			if not x in omit:
				mydb = client[x]
				_.colorThis( x, 'green' )
				for coll in mydb.list_collection_names():
					my_collection = client[x][coll]
					# one = dir(client[x][coll])

					_.pr( 
						'\t',
						_.colorThis( coll, 'yellow', p=0 ),
						' | ',
						_.colorThis( _.addComma( my_collection.count_documents({}) ), 'cyan', p=0 ),
						)
					try:
						theKeys = list(client[x][coll].find_one().keys())
						# _.pr( theKeys )
						for fy in theKeys:
							_.colorThis( [ '\t\t', fy ], 'white' )
						# _.pr(client[x][coll].find_one())
					except Exception as e:
						pass


		sys.exit()

	db = client[  theDB  ]
	table = db[ _.switches.values('Table')[0] ]


	# myquery = { "address": "Park Lane 38" }
	# preQ = ' '.join(     _.switches.values('Query')     ).replace( "'", '"' )

	preQ = ' '.join(     _.switches.values('Query')     )
	if '{' in preQ:
		mydoc = table.find(  eval( preQ )  )
	else:
		mydoc = table.find(  eval( generate( client, theDB, _.switches.values('Table')[0] ) )  )
		# mydoc = eval(  )

	isSingle = False
	if _.switches.isActive('Fields') and len(_.switches.values('Fields')) == 1:
		isSingle = True
	records = []
	for x in mydoc:

		record = {}

		keys = list(x.keys())
		if _.switches.isActive('Fields'):
			keys = _.switches.values('Fields')
		for key in keys:
			if not '.' in str(type(x[key])):
				if key in x:
					record[key] = x[key]
					if isSingle:
						_.pr( record[key] )

		records.append(record)
	if not isSingle:
		if not len( records ):
			_.colorThis( 'No records', 'yellow' )
		else:

			if not _.switches.isActive('Mode') or _.switches.value('Mode').lower() == 'json':
				_.printVarSimple( records )
			elif _.switches.value('Mode').lower() == 'table' or 't' in _.switches.value('Mode').lower():
				_.tables.register( 'data', records )

				if _.switches.isActive('Fields'):
					_.tables.print( 'data', ','.join( _.switches.values('Fields') ) )
				else:
					_.tables.print( 'data', list(records[0].keys()) )


def generate( client, db, table):
	a = """  { "$and": [ RECORDS ] }  """
	o = """  { "$or": [ RECORDS ] }  """

	iz = """{"FIELD": "STRING" } """
	# c = """{"$text":{"$search": "*STRING*"}}"""
	c = """{"FIELD":{"$regex": ".*STRING.*"}}"""
	# c = """{"FIELD":{"$regex": "/^STRING/"}}"""
	# c = """{"FIELD":{"$regex": "^STRING$"}}"""
	# c = """{"FIELD":{"$regex": "*.STRING.*"}}"""
	s = """{"FIELD":{"$regex": "^STRING"}}"""
	e = """{"FIELD":{"$regex": "STRING$"}}"""
	# e = """ {"FIELD":{"$regex": "*STRING", "$options":"i"} } """

	parts = []
	qq = ' '.join( _.switches.values('Query') ).split(';')
	for q in qq:
		field = _str.cleanBE(q.split(':')[0],' ')
		index_field( client, db, table, field )
		for x in q.split(':')[1].split(','):
			x = _str.cleanBE( x, ' ' )
			if False:
				pass
			elif x.endswith('*') and x.startswith('*'):
				parts.append(   c.replace( 'FIELD', field ).replace( 'STRING', x.replace('*','') )   )
			elif x.endswith('*'):
				parts.append(   s.replace( 'FIELD', field ).replace( 'STRING', x.replace('*','') )   )
			elif x.startswith('*'):
				parts.append(   e.replace( 'FIELD', field ).replace( 'STRING', x.replace('*','') )   )
			elif x.startswith("'") and x.endswith("'"):
				parts.append(   iz.replace( 'FIELD', field ).replace( 'STRING', x.replace("'",'') )   )
			else:
				parts.append(   c.replace( 'FIELD', field ).replace( 'STRING', x )   )
	result = ''
	if len( parts ) == 0:
		_.colorThis( 'Error: EFCA | Empty Query' )
		sys.exit()
	elif len( parts ) == 1:
		result = parts[0]
	elif len( parts ) > 1:
		if _.switches.isActive('ADD') or (  not _.switches.isActive('ADD') and not _.switches.isActive('OR')  ):
			result = a.replace( 'RECORDS', '\n\t'+ ',\n\t'.join(  parts  ) +'\n' )
		elif _.switches.isActive('OR'):
			result = o.replace( 'RECORDS', '\n'+ ',\n'.join(  parts  ) +'\n' )

		else:
			_.colorThis( 'Error: AE1D | generic problem' )
			sys.exit()
	if not _.switches.isActive('Clean'):
		_.pr('\n\n')
		_.printVarSimpleSTR( result )
		_.pr('\n\n')
		# _.printVarSimple( eval(result) )

	# sys.exit()
	return result
	# field = q.pop(0)



	# c = """ {"FIELD":{"$regex":".*STRING.*"} } """



	if len(q) == 2:
		_.pr(q)


	sys.exit()


fields_to_index = []

import _rightThumb._encryptString as _blowfish
import _rightThumb._vault as _vault
import pymongo
import simplejson as json


########################################################################################
if __name__ == '__main__':
	action()







