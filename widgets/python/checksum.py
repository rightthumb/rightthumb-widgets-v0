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



import _rightThumb._md5 as _hash
##################################################

def appSwitches():
	pass
	_.switches.register( 'Test', '-t,-test' )
	_.switches.register( 'Hash', '-h,-hash,-hashes', 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 ipfs' )
	
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Time', '-time' )



_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = True
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'checksum.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'generate all major checksums and/or check for match',
	'categories': [
						'checksum',
						'hash',
						'file',
						'tool',
						'audit',
						'check',
						'md5',
						'sha1',
						'sha224',
						'sha256',
						'sha384',
						'sha512',
						'sha3_224',
						'sha3_256',
						'sha3_384',
						'sha3_512',
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
						'p checksum -test bf367509c6bf77181517fd45a544e40ee21c1d63ad20b980ecf8009d91e19d3f  -h sha256 -f JetBrains.Rider-2020.1.1.exe',
						'',
						'p checksum -f unnamed.png',
						'p checksum -f unnamed.png -h md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512 ipfs',
						'p checksum -f unnamed.png -h md5 sha256 ',
						'',
						'p file + *.png --c | p checksum',
						'',
						'p file + *.png --c | p checksum -hashes md5 sha256',
						'',
						'p file + *.png --c | p checksum -hashes sha256 sha384 -test 80a466c320c6c23384298a00c8a1192195225a11d1bce68328cf37a6bce29aa9',
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


def hash_trigger( data ):
	if data.lower() == 'ipfs' or data.lower() == 'ipf':
		return 'sha256'
	return data


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
	_.switches.trigger( 'Hash', hash_trigger )
	
	
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



def process( file, h ):
	result = None
	start = time.time()
	try:
		result = _hash.file( file, h )
	except Exception as e:
		_.colorThis(  [ 'Error:', h, file ], 'red'  )
	end = time.time()
	diff = end - start
	if _.switches.isActive('Time'):
		_.pr( h, diff )
			
	return result
	
def action():
	focus()
	if _.switches.isActive('Files'):
		_.appData[__.appReg]['pipe'] = _.switches.values('Files')
	if type( _.appData[__.appReg]['pipe'] ) == bool and not _.switches.isActive('Files'):
		_.help()
		_.pr('Here')

	# _.pr( _.appData[__.appReg]['pipe'] )
	# sys.exit()
	hashes =     {
					"md5": "e400cf095a5ce8d540be1ffff5380829",
					"sha1": "1c451f944709ce0eea7e41c4df9b2fcf46fe1746",
					"sha224": "b57de62df4f94ed25df5654618621e386f361022118ca7a90ddb714b",
					"sha256": "80a466c320c6c23384298a00c8a1192195225a11d1bce68328cf37a6bce29aa9",
					"sha384": "9939b36161729307c6ef401b6222fcdfe0b86124c6b5f29a6b9ad2df7ddb1f415ab782382859c70fc67a5db8b183b483",
					"sha512": "04f243dfafd883821a0bd7db8ea80bcfef37f0f03daec35843faaff7268058d146cd6574fe1fea62919cbe9890f6e2ce7d050660719738f2c6f73b18398b8b7b",
					"sha3_224": "b925ee95c904ba118e247d9d4232a07a71412e51bb64e64d6353764d",
					"sha3_256": "37d000dbdcc6663eaf6582f39b0beb287690f899bc3b08a332116a892e2a3812",
					"sha3_384": "efa18dc132df94e78e59a6a6bccbcad55495c8b042a380442bbd2688e41ae94b1af179a94a5046f553707ac4026b7874",
					"sha3_512": "5b9fcfa37364d9ec0d85dba2c7d49ef97161d19ae7516eabbe5f419b8628898cb8f803c02f5abbd1b8ea4b60512a9c786d2684017fd85d4c190f25f3fdd47a9b"
				}


	if not _.switches.isActive('Hash') or not len(_.switches.value('Hash')):

		if _.switches.isActive('Test') and len(_.switches.value('Test')):
			testHashes = []
			for h in hashes.keys():
				if len( hashes[h] ) == len(_.switches.value('Test')):
					testHashes.append( h )
			if len(testHashes):    
				_.switches.fieldSet( 'Hash', 'active', True )
				_.switches.fieldSet( 'Hash', 'value', ','.join(testHashes) )
				_.switches.fieldSet( 'Hash', 'values', testHashes )
		else: # not test
			_.switches.fieldSet( 'Hash', 'active', True )
			_.switches.fieldSet( 'Hash', 'value', 'md5' )
			_.switches.fieldSet( 'Hash', 'values', ['md5'] )

	hash_dic = []
	for x in _.switches.values('Hash'):
		hash_dic.append({ 'hash': x, 'data': hashes[x] })

	_.fields.asset( 'hashes', hash_dic )
	

	records = []
	if not type( _.appData[__.appReg]['pipe'] ) == bool:
		_.pipeCleaner(0)
		# _.printVar( _.appData )
		if len( _.appData[__.appReg]['pipe'] ) > 1:
			multiFile = True
		else:
			multiFile = False
		
		if len( _.switches.values('Hash') ) > 1:
			multHash = True
		else:
			multHash = False

		
			
		
		for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			record_dic = {}
			if multHash:
				if not _.switches.isActive('Clean') and not _.switches.isActive('Test'):
					_.pr()
					_.pr()
					_.colorThis(   [ row ], 'green'   )
				for h in _.switches.values('Hash'):
					record = process( row, h )
					record_dic[h] = record
					records.append({ 'file': row, 'hashes': record_dic })
					hx = _.fields.value( 'hashes', 'hash', h, r=1 )
					if not _.switches.isActive('Clean') and not _.switches.isActive('Test'):
						# rx = _.fields.value( 'hashes', 'data',  )

						_.colorThis(   [ '\t', hx, '\t', record ], 'yellow'   )
					elif _.switches.isActive('Test'):
						if record.lower().replace( ' ', '' ) == _.switches.value('Test').lower().replace( ' ', '' ):
							_.colorThis(  [ 'Success:', hx, row ] , 'green'  )
							sys.exit()
						else:
							_.colorThis(  [ 'Failure:', hx, row ]  , 'red'  )


			if not multHash:

				for h in _.switches.values('Hash'):
					record = process( row, h )
					records = record


				if not _.switches.isActive('Clean') and not _.switches.isActive('Test'):
					if multiFile:
						_.colorThis(   [ record, row ], 'yellow'   )
					else:
						_.colorThis(   [ record ], 'yellow'   )


				elif _.switches.isActive('Test'):

					try:
						record
					except Exception as e:
						_.pr( 'Hash', _.switches.values('Hash') )
						sys.exit()

					if multiFile:
						if record.lower().replace( ' ', '' ) == _.switches.value('Test').lower().replace( ' ', '' ):
							_.colorThis(  [ 'success', row ] , 'green' )
						else:
							_.colorThis( [ 'failure', row ] , 'red' )
					if not multiFile:
						if record.lower().replace( ' ', '' ) == _.switches.value('Test').lower().replace( ' ', '' ):
							_.colorThis( 'success', 'green' )
						else:
							_.colorThis( 'failure', 'red' )


			pass
			# _.printVarSimple(temp)

	return records



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






