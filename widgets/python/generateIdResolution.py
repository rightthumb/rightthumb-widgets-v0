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
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
import shutil

# {'name': 'File','switch': '-file', 'pos': None, 'active': False,'expected_input_example': None}

_.appInfo=    {
	'file': 'generateIdResolution.py',
	'description': 'Generate table of IDs and their resolved labels',
	'prerequisite': [],
	'examples': [],
	'columns': [],
	}

# _.appInfo['examples'].append('p drive -scan')

# _.appInfo['columns'].append({'name': 'name', 'abbreviation': 'n'})

# def formatColumns(columns):
#     result = ''
#     for c in columns.split(','):
#         for col in _.appInfo['columns']:
#             for a in col['abbreviation'].split(','):
#                 if a == c:
#                     c = col['name']
#         result += c + ','
#     result = result[:-1]
#     return result

# _.switches.trigger('Column',formatColumns)
# _.switches.process()

# _.tableProfile.append({
#     'field': 'timestamp', 
#     'script_trigger_external': _.float2Date
#     })

# if _.switches.isActive('Snapple') == False:
#     file = _.switches.value('File')
#     variable = _.getTable(file)
#     _.saveTable(xRefList,file)
#     line = _str.replaceAll(line,'  ',' ')
#     line = _str.cleanFirst(line,' ')
#     line = _str.cleanLast(line,' ')
#     line = _str.cleanSpecial(line)
#     line = _str.totalStrip(line)
#     line = _str.removeAll(line)
#     line = _str.replaceDuplicate(line,' ')
#     if _isSwitchActive('Sort'):
#         xRefList = _.sort(xRefList, _.switches.value('Sort'))
#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')
	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)



	# if _.showLine(string):
		# print(line)
########################################################################################

def processDriveLog( file, host='', local=True ):
	global resolution
	if local:
		driveTable = _.getTable(file)
	else:
		driveTable = _.getTable2(file)
	# print(driveTable)
	for drive in driveTable:
		if local:
			resolution.append({'name': drive['name'] , 'id': drive['id']})
		else:
			resolution.append({'name': drive['name'] + ' (' + host + ')', 'id': drive['id']})

	return resolution

def processUUIDLog( file, host='', local=True ):
	global resolution
	if local:
		uuid_log = _.getTable(file)
	else:
		uuid_log = _.getTable2(file)

	for row in uuid_log:
		try:
			len( row['project'] )
		except Exception as e:
			row['project'] = ''
		try:
			len( row['label'] )
		except Exception as e:
			row['label'] = ''
			
		if len( row['project'] ) and len( row['label'] ):
			n = row['app'].replace( '.py', '' )+': '+str(row['project'])+': '+str(row['label'])
		elif len( row['project'] ) and not len( row['label'] ):
			n = row['app'].replace( '.py', '' )+': '+str(row['project'])
			
		elif not len( row['project'] ) and len( row['label'] ):
			n = row['app'].replace( '.py', '' )+': '+str(row['label'])

		if local:
			resolution.append({'name': n, 'id': row['uuid']})
		else:
			resolution.append({'name': n + ' (' + host + ')', 'id': row['uuid']})

def action():
	global resolution
	

	resolution.append({'name': 'Default Profile', 'id': '{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}'})

	resolution.append({'name': 'Temp File', 'id': '{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}'})
	
	resolution.append({'name': 'Temp File 0', 'id': '{B820137A-79B8-45E3-BCBD-A6CAC50892D0}'})
	resolution.append({'name': 'Temp File 1', 'id': '{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}'})
	resolution.append({'name': 'Temp File 2', 'id': '{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}'})
	resolution.append({'name': 'Temp File 3', 'id': '{F139D191-FA1A-44D5-855C-7E5141B30E0D}'})
	resolution.append({'name': 'Temp File 4', 'id': '{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}'})
	resolution.append({'name': 'Temp File 5', 'id': '{201D82D6-2DC0-4552-A598-54F5481399A1}'})
	
	resolution.append({'name': 'Temp File 6', 'id': '{26B3B9C6-0A59-432A-9386-D432B53001CB}'})
	resolution.append({'name': 'Temp File 7', 'id': '{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}'})
	resolution.append({'name': 'Temp File 8', 'id': '{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}'})
	resolution.append({'name': 'Temp File 9', 'id': '{DF1D4EBC-838E-419C-9C58-943C1767391A}'})

	resolution.append({'name': 'Temp File L', 'id': '{79E8C4B0-2AAA-2083-B812-AD1B9283B30A}'})

	resolution.append({'name': 'Quick Index', 'id': '{3C2D3003A97C}'})

	resolution.append({'name': _v.techDrive + ':\\tech', 'id': '{A8693D4B-8A80-898F-83F0-E806D2F36800}'})
	resolution.append({'name': _v.getUserProfile() , 'id': '{6FAB5628-94A1-410A-82D1-1D42A2A11750}'})
	resolution.append({'name': _v.thisHost , 'id': '{C12F266D-71B9-40D2-98B9-424B42D2DBAC}'})
	# resolution.append({'name': '', 'id': ''})
	machineID = _v.getMachineID()
	resolution.append({'name': 'Machine ID', 'id': machineID})
	# print(machineID)
	file = 'indexTable_drives-' + machineID + '.json'
	# print(file)

	processDriveLog( file )

	processUUIDLog( 'uuid_log.json' )

	_.saveText( 'placeholder', _v.txt_temp )
	print(_v.txt_temp)

	# print(resolution)

	for item in os.listdir( _v.myIndexes ):
		if item.startswith( '0A{' ):
			resolution.append({'name': 'Quick Index', 'id': item})

	#####
	for l in 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(','):
		letter = l + ':'+_v.slash
		hosts = letter + 'tech\\hosts'
		if os.path.isdir( hosts ):
		

			for thisHost in os.listdir( hosts ):
				path = hosts + _v.slash + thisHost
				tables = path + _v.slash+'tables'
				indexes = path + _v.slash+'indexes'
				thisDrive = tables + _v.slash+'indexTable_drives-' + machineID + '.json'


				if not _v.myTables.lower() == tables and os.path.isdir( tables ):
					for itemX in os.listdir( tables ):
						do = 0
						if itemX.startswith( 'indexTable_drives-{' ):
							do = 1
						if itemX.startswith( 'uuid_log.json' ):
							do = 2
						

						
						
						# sys.exit()
						if os.path.isfile( thisDrive ):
							do = 0

						if do > 0:
							# print( thisDrive )
							file = tables + _v.slash + itemX
							dstf = _v.dataFolder + _v.slash+'IDs'+_v.slash + thisHost
							if not os.path.isdir( _v.dataFolder ):
								os.mkdir( _v.dataFolder )
							if not os.path.isdir( _v.dataFolder + _v.slash+'IDs' ):
								os.mkdir( _v.dataFolder + _v.slash+'IDs' )
							if not os.path.isdir( dstf ):
								os.mkdir( dstf )
							
							shutil.copy( file, dstf + _v.slash + itemX )

				if not _v.myTables.lower() == tables and os.path.isdir( indexes ):
					for itemX in os.listdir( indexes ):
						if itemX.startswith( '0A{' ):
							dstf = _v.dataFolder + _v.slash+'IDs'+_v.slash + thisHost
							if not os.path.isfile( thisDrive ):
								print( dstf + _v.slash + itemX )
								shutil.copy( _v.txt_temp, dstf + _v.slash + itemX )


	if os.path.isdir( _v.dataFolder + _v.slash+'IDs' ):
		for thisHost in os.listdir( _v.dataFolder + _v.slash+'IDs' ):
			tables = _v.dataFolder + _v.slash+'IDs'+_v.slash + thisHost
			for itemX in os.listdir( tables ):
				do = 0
				if itemX.startswith( 'indexTable_drives-{' ):
					do = 1
				if itemX == 'uuid_log.json':
					do = 2
				if itemX.startswith( '0A{' ):
					do = 3


				if do > 0:
					file = tables + _v.slash + itemX

					# print( file )
					if do == 2:
						processUUIDLog( file, host=thisHost, local=False )
					elif do == 1:
						processDriveLog( file, host=thisHost, local=False )
						machineIDx = itemX.split( '{' )[1].split( '}' )[0]
						resolution.append({'name': 'Machine ID ('+thisHost+')', 'id': machineIDx})
					elif do == 3:
						resolution.append({'name': 'Quick Index ('+thisHost+')', 'id': itemX})




							


# 

# 
	# sys.exit()
	resolutionIndex = {}
	for record in resolution:
		resolutionIndex[ record['id'] ] = record['name']

	for id_log in _v.tableAlts('idResolution.json'):
		print()
		print(id_log)
		print()
		for rec in _.getTable2(id_log):
			if not rec['id'] in resolutionIndex:
				print( '\tadded:', rec )
				resolution.append( rec )

	print()
	print()
	# sys.exit()
	for r in resolution:
		print(r['id'],r['name'])

	_.saveTable(resolution,'idResolution.json')
	resolutionIndex = {}
	for record in resolution:
		resolutionIndex[ record['id'] ] = record['name']
	_.saveTable(resolutionIndex,'registered-ids.index')

resolution = []

########################################################################################
if __name__ == '__main__':
	action()





