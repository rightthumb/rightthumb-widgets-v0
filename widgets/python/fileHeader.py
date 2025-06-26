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
import platform
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


import _rightThumb._dir as _dir
import _rightThumb._mimetype as _mime
	
##################################################

def appSwitches():
	pass
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name', description='Files' )
	_.switches.register( 'Clean', '--c' )

	_.switches.register( 'ResolveErrors', '-err' )
	_.switches.register( 'JustHeader', '-jh' )
	_.switches.register( 'NoExtension', '-noext' )
	_.switches.register( 'Add', '-add' )
	_.switches.register( 'Rename', '-rename' )
	_.switches.register( 'FullHeader', '-fh,-fullheader' )



	
_.autoBackupData = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'fileHeader.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Read the header. Can show header. Can tell you what the file is.',
	'categories': [
						'file',
						'file header',
						'header',
						'tool',
						'research',
						'troubleshoot',
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
						'p fileHeader -f 8F11__cc.bin ',
						'p fileHeader -f "{4267C3A6-2322-4FA6-A10D-4665279CCD68}" -noext ',
						'',
						'p harResearch -f www.google.com.har -field encoding base64 | p harResearch -f www.google.com.har -save base64',
						'p file -bin --c | p fileheader -noext -rename jpg png svg gif ico',
						'',
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
	# _.switches.trigger( 'Files', _.myFileLocations  )
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Folder',_.myFolderLocations )
	
	
	
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

def process( filepath ):
	file = open( filepath, 'rb' ).read(32)
	hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])

	if _.switches.isActive('JustHeader'):
		return hex_bytes

	if _v.slash in filepath:
		x = filepath.split(_v.slash)
		x.reverse()
		f = x[0]
		ext = _dir.getExtension( f )
	else:
		ext = _dir.getExtension( filepath )

	results = []
	for record in data:
		if hex_bytes.startswith( record['signature'] ):
			shouldRun = True
			if not _.switches.isActive('NoExtension') and not record['extension'].lower() == ext.lower():
				shouldRun = False
			if _.switches.isActive('Rename'):
				shouldRun = True
			if shouldRun:
				# record['header'] = hex_bytes
				results.append( record )
				if not _.switches.isActive('NoExtension'):
					return record
	pass
	if len( results ):
		return results

	if _mime.isText(filepath):
		record = {
					'extension': 'TXT',
					'description': 'Plain Text',
					'signature': '',
					'header': hex_bytes,
		}
		return record


	return hex_bytes
def addSig(sig):
	if not _.switches.isActive('Add'):
		return None
	if _.switches.isActive('Rename'):
		return None
	if _.switches.isActive('Clean'):
		return None

	theSignature=input( 'add?: ' )

	if len(theSignature) and sig['signature'].startswith(theSignature):
		_.pr()
		for record in data:
			if theSignature == record['signature'] or record['signature'].startswith(theSignature):
				_.pr( '\t', record['signature'], '\t', record['description'] )
		_.pr()
		theExtension=input( 'extension: ' )
		theExtension = theExtension.replace('.','')
		if len(theExtension):
			theExtension=theExtension.upper()
			theDescription=input( 'description: ' )
			if len(theDescription):
				data.append({
								"extension": theExtension,
								"signature": theSignature,
								"description": theDescription,
								"src": "manually added"
							})
				_.saveTableDB( data, 'hex_headers.json' )
				_.colorThis( 'Added', 'green' )
def action():
	global data
	global err
	load()

	if not _.switches.isActive('ResolveErrors'):

		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner(0)
			# _.printVar( _.appData )
			# for i,row in enumerate( _.appData[__.appReg]['pipe'] ):
			for i,row in enumerate(_.pp()):
				if not os.path.isfile(row):
					_.colorThis(  ['Not a file:',row], 'red' )
					# sys.exit()
				if os.path.isfile(row):
					info = process( row )
					if _.switches.isActive('Add'):
						_.pr( info )
						if type(info) == list:
							for record in info:
								_.printVarSimple(record)
							_.switches.fieldSet( 'JustHeader', 'active', True )
							info = process( row )
						elif type(info) == str:
							for record in data:
								if info.startswith(record['signature']):
									_.pr( '\t?\t', record['description'] )
						addSig(info)
						return None


					if _.switches.isActive('JustHeader'):
						asciiH = asciiHeader(info)
						# _.pr( info )
						_.pr()
						_.pr( _.colorPrint( row, 'cyan', p=0 ), asciiH )
						_.pr()
					else:

						if type(info) == str:
							if not _.switches.isActive('Clean'):
								_.pr()
								_.pr( row, 'Unknown', info )
								for record in data:
									if info.startswith(record['signature']):
										_.pr( '\t?\t', record['description'] )
								addSig(info)


							p = os.path.abspath( row )

							found = False
							for rec in err:
								if rec['path'].lower() == p.lower():
									found = True

							if not found:
								d = {
										'ext': _dir.getExtension( row ),
										'path': os.path.abspath( row )
								}
								# _.printVar( d )
								err.append({ 'header': info, 'dir': d, 'path': d['path'] })
								# _.saveTable( err, 'hex_headers_errors.json', p=0 )


						elif type(info) == dict:
							record = {
										'file': row,
										'extension': info['extension'],
										'description': info['description'],
							}
							if not _.switches.isActive('Clean'):
								if not _.switches.isActive('Rename'):

									_.linePrint( 'header', [
																row,
																info['extension'],
																info['description'],
																info['signature'],
															] )

									_.pr()
									_.colorThis( _.linePrint( 'header', add=10, p=0 ), 'red' )
									_.colorThis( [ _.lp(), row ], 'cyan' )
									_.colorThis( [ _.lp(), info['extension'] ] , 'cyan' )
									_.colorThis( [ _.lp(), info['description'] ], 'yellow' )
									_.pr( _.lp(), asciiHeader(info['signature']) )
									_.colorThis( _.linePrint( 'header', add=10, p=0 ), 'red' )
									
									# _.printVarSimple( info )
								elif _.switches.isActive('Rename'):
									if not row.endswith('.'+info['extension'].lower()) and not row.endswith('.'+info['extension'].upper()):
										os.rename( row, row+'.'+info['extension'].lower() )
										_.colorThis( [ row+'.'+info['extension'].lower() ], 'green' )
									# _.pr( info )
						elif type(info) == list:
								if not _.switches.isActive('Rename'):
									_.pr()
									_.pr( row )
									for inf in info:
										_.pr( '\t', inf['extension'], inf['description'] )
								elif _.switches.isActive('Rename'):
									theExtensions = []
									found = None
									for inf in info:
										theExtensions.append( inf['extension'].lower() )
										if inf['extension'].lower() in _.switches.values('Rename'):
											found = inf['extension'].lower()
									
									if found is None and len(theExtensions):
										found = theExtensions[0]
									if not found is None:
										if not row.endswith('.'+found.lower()) and not row.endswith('.'+found.upper()):
											os.rename( row, row+'.'+found )
											_.colorThis( [ row+'.'+found ], 'green' )



	_.saveTable( err, 'hex_headers_errors.json', p=0 )

	if _.switches.isActive('ResolveErrors'):

		_.pr( 'Errors:', len(err) )

		# sig = {}

		# for record in data:
		#     x = len( record['signature'].split(' ') )+1
		#     try:
		#         sig[x] += 1
		#     except Exception as e:
		#         sig[x] = 1

		# _.printVar( sig )
		
		'''
				{
					"2": 35,
					"3": 55,
					"4": 33,
					"5": 176,
					"6": 33,
					"7": 27,
					"8": 15,
					"9": 146,
					"10": 1,
					"11": 1,
					"12": 1,

					"15": 2,
					"17": 4,
					
					"20": 3,
					"22": 1
					"35": 1,
					"51": 1,
				}
		'''

		records = {}
		for i,rec in enumerate(err):
			rec['index'] = i
			h = headerParts( rec['header'], 3 )
			e = rec['dir']['ext'].lower()
			if not h is None:
				n = e + ' - ' + h
				# _.printTest( n )

				try:
					records[n].append( rec )
				except Exception as e:
					records[n] = []
					records[n].append( rec )

		pass

		add = []
		remove = []

		for n in records.keys():
			i=3
			good = True
			done = False
			if len( records[n] ) > 3:

				while not done:
					i+=1
					for rec in records[n]:
						h = headerParts( rec['header'], i )
						if h is None:
							good = False
						else:    
							if not rec['header'].startswith( h ):
								good = False

					if not good:
						done = True
				i-=1
				h = headerParts( records[n][0]['header'], i )
				if platform.system() == 'Windows':
					os.system('cls')
				else:
					os.system('clear')
				newRecord =     {
									"extension": n.split(' ')[0],
									"signature": h,
									"description": "",
									"src": "auto"
								}


				# { 'signature': h, 'ext': n.split(' ')[0] }
				_.pr()
				_.pr()
				_.pr()
				_.pr()
				_.pr( newRecord )
				_.pr()
				_.pr( 'records:', len(records[n]) )
				_.pr()



				for rec in records[n]:
					_.pr( rec['path'] )
				# _.printVar( records[n][0]['dir'] )
				# add.append()
			
				_.pr()
				_.pr()
				_.pr()
				_.pr()
				description = 'y'
				description = input( 'Description: ' )
				if not description.lower() == 'x':


					description = _str.replaceDuplicate( description, ' ' )
					description = _str.cleanBE( description, ' ' )

					newRecord['description'] = description

					data.append(newRecord)
					for rec in records[n]:
						remove.append( rec['index'] )


					pass
					remove.sort()
					remove.reverse()
					# _.pr( remove )
					# _.pr( 'Signature:', h )

					for r in remove:
						err.pop(r)

					_.saveTable( err, 'hex_headers_errors.json' )
					_.saveTableDB( data, 'hex_headers.json' )
					sys.exit()

######################################################################################################
		pass

		# sys.exit()



		os.system('cls')
		_.pr()
		_.pr()

		_.pr( 'Done' )
		pause=input('pause')


		records = {}
		for i,rec in enumerate(err):
			rec['index'] = i
			h = headerParts( rec['header'], 3 )
			e = rec['dir']['ext'].lower()
			if not h is None:
				n = h
				# _.printTest( n )

				try:
					records[n].append( rec )
				except Exception as e:
					records[n] = []
					records[n].append( rec )

		pass

		add = []
		remove = []

		for n in records.keys():
			i=3
			good = True
			done = False
			if len( records[n] ) > 3:

				while not done:
					i+=1
					for rec in records[n]:
						h = headerParts( rec['header'], i )
						if h is None:
							good = False
						else:    
							if not rec['header'].startswith( h ):
								good = False

					if not good:
						done = True
				i-=1
				h = headerParts( records[n][0]['header'], i )
				os.system('cls')
				newRecord =     {
									"extension": '',
									"signature": h,
									"description": "",
									"src": "auto"
								}


				# { 'signature': h, 'ext': n.split(' ')[0] }
				_.pr()
				_.pr()
				_.pr()
				_.pr()
				_.pr( newRecord )
				_.pr()
				_.pr( 'records:', len(records[n]) )
				_.pr()



				for rec in records[n]:
					_.pr( rec['path'] )
				# _.printVar( records[n][0]['dir'] )
				# add.append()
			
				_.pr()
				_.pr()
				_.pr()
				_.pr()
				description = 'y'
				description = input( 'Description: ' )
				if not description.lower() == 'x':


					description = _str.replaceDuplicate( description, ' ' )
					description = _str.cleanBE( description, ' ' )

					newRecord['description'] = description

					data.append(newRecord)
					for rec in records[n]:
						remove.append( rec['index'] )


					pass
					remove.sort()
					remove.reverse()
					# _.pr( remove )
					# _.pr( 'Signature:', h )

					for r in remove:
						err.pop(r)

					_.saveTable( err, 'hex_headers_errors.json' )
					_.saveTableDB( data, 'hex_headers.json' )
					sys.exit()



		pass
		remove.sort()
		remove.reverse()
		_.pr( remove )

		for r in remove:
			err.pop(r)

		_.saveTable( err, 'hex_headers_errors.json' )
		_.saveTableDB( data, 'hex_headers.json' )



		# for i,record in enumerate(data):
		#     data[i]['src'] = 'filesignatures.net'
		# _.saveTable( data, 'hex_headers.json' )

def asciiHeader( header, p=1 ):
	try:
		return asciiHeaderRun( header, p )
	except Exception as e:
		return header

hex_header_chars = None
def asciiHeaderRun( header, p=1 ):
	global hex_header_chars
	if hex_header_chars is None:
		hex_header_chars = _.getTableDB( 'hex_header_chars.json' )
	hexHeader = []
	txtHeader = []
	for hx in header.split(' '):
		x = ''.join([chr(int(''.join(c), 16)) for c in zip(hx[0::2],hx[1::2])])
		if x in _str.visibleChar or x in hex_header_chars:
			if not x == '\r' and not x == '\n':
				if x in _str.visibleChar:
					txtHeader.append( x )
				else:
					txtHeader.append( ' ' )
				# txtHeader.append( x )
			if _.switches.isActive('FullHeader'):
				hexHeader.append( hx )
			elif not _.switches.isActive('FullHeader'):
				if len(hexHeader) == 6:
					hexHeader.append( '...' )
				elif len(hexHeader) < 6:
					hexHeader.append( hx )
		else:
			break
	if len( hexHeader ):
		if p:
			return _.colorThis( 'ASCII: ', 'cyan', p=0 ) + _.colorThis( ''.join(txtHeader), 'green', p=0 ) + '\t' +  _.colorThis( 'HEX: ', 'cyan', p=0 ) + _.colorThis( ' '.join(hexHeader), 'yellow', p=0 )
		else:
			return { 'ascii': ''.join(txtHeader), 'hex': ' '.join(hexHeader) }
	else:
		return header



def headerParts( header, cnt ):

	h = header.split(' ')
	r=[]
	i=0
	while i < cnt:
		
		try:
			r.append( h[i] )
		except Exception as e:
			return None

		i+=1

	return ' '.join(r)



def load():
	global data
	global err
	data = _.getTableDB( 'hex_headers.json' )
	err = _.getTable( 'hex_headers_errors.json' )


data = []
err = []
########################################################################################
if __name__ == '__main__':
	action()







