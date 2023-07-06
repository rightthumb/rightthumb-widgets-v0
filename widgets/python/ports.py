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
	pass
	_.switches.register( 'Ports', '-p,-port,-ports',  isPipe='name' )
	_.switches.register( 'All', '-all' )
	_.switches.register( 'Clean', '--c' )
	_.switches.register( 'Test', '-test' )
	_.switches.register( 'PortScan', '-scan' )
	_.switches.register( 'Ephemeral', '-e,-eph,-ephemeral', 'yes OR no OR y OR n OR t OR f OR true OR false' )
	_.switches.register( 'NetBrute', '-nb,-netbrute' )




_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.sort_name_trigger_override = [  ['']  ]

# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ports.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Lookup info about network ports',
	'categories': [
						'network',
						'networking',
						'resource',
						'research',
						'tool',
						'port',
						'ports',
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
						'p ports -ports 1433 110 25 73',
						'p ports -ports 1433 110 25 73 -all',
						'',
						'type %tmpf0% | p ports',
						'',
						'p ports + system',
						'',
						'p ports + imap',
						'p ports + pop',
						'p ports + smtp',
						'',
						'p ports + database',
						'',
						'p ports + system -tp *;l --c | p cmd2Table -print | p printTable -c tcp udp port description -g tcp udp -s TCP udp -long',
						'',
						['p ports + pop smtp imap mail -or','red'],
						'',
						'p ports + trojjan +close 90%',
						'',
						'',
						'b ttt',
						'p ports -all  > ports-raw.txt',
						'p ports -all -ephemeral > ports-raw-with-ephemeral.txt',
						'',
						'',
						'type %tmpf0% | p ports -nb',
						'type %tmpf0% | p ports -netbrute -all',
						'type %tmpf0% | p ports -nb -e',
						'type %tmpf0% | p ports -nb -ephemeral',
						'type %tmpf0% | p ports -nb + 80',
						'type %tmpf0% | p ports -nb + 139 445',
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
					# { 'name': 'Port', 'abbreviation': 'p', 'sort': 'port_sort' },
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
		_.setPipeData( sys.stdin.readlines(), __.appReg )


_.postLoad( __file__ )

########################################################################################
# START


import socket


def port_scan():
	global data
	

	ip = _.switches.value('PortScan')

	# scan_port( ip, 135 )
	# sys.exit()

	for port in data.keys():
		if not 'Ephemeral' in data[port]['IANA_Status'] and not 'Ephemeral' in data[port]['Description']:
		
			if not port == 'Port':
				# _.pr(port)
				scan_port( ip, port )
				try:
					scan_port( ip, port )
				except Exception as e:
					pass
					# _.pr( 'port error:', port )


spent = []
def scan_port( ip, port ):
	global data
	global spent
	if not type(port) == int:
		try:
			port = int(port)
		except Exception as e:
			pass
	if not type(port) == int:
		return None

	if not port in spent:
		spent.append(port)
		# Create a new socket
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# _.pr( tcp.gettimeout() )
		# sys.exit()
		tcp.settimeout(.02)
		# _.pr( tcp.connect_ex((ip, port)), port )


		# Print if the port is open
		result = tcp.connect_ex((ip, port))
		# _.pr( result, port )
		if not result:
			_.pr( port )
			# _.pr('[+] %s:%d/TCP Open' % (ip, port) )
			# _.pr('[+] %s:%d/TCP Open' % (ip, port) , data[str(port)]['Description'] )
			tcp.close()

		# try:
				
		# except Exception:
		#     pass


	# a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# location = ( ip, port )
	# result_of_check = a_socket.connect_ex(location)

	# if result_of_check == 0:
	#    _.pr( 'Yes\t', port )
	#    # _.pr( port )
	# # else:
	# #    _.pr( 'No \t', port )
	#    # _.pr("Port is not open")
	# # OUTPUT
	# # Port is not open

	# a_socket.close()





def processPortRow(row):
	global data
	global ipsPorts
	ip = _str.cleanBE(  row.split( '#' )[0]  ,' ')
	port = row.split( '#' )[1]
	
	if not ip in ipsPorts:
		ipsPorts[ip] = {}

	if not port in ipsPorts[ip]:
		ipsPorts[ip][port] = {}
	# if port not in data:
	# else:
	#     ipsPorts[ip][port] = data[port]
	#     # _.pr()
		# if _.switches.isActive('All'):
		#     _.pr(port)
		#     _.printVarSimple( data[port] )
		# else:
		#     _.pr( '  ', _.cp( port, 'yellow', p=0 ), _.cp( data[port]['Description'], 'cyan', p=0 ) )

		# _.pr()

def ip_port_report():
	global data
	global ipsPorts

	# ipsPorts = _.dic_key_sort2(ipsPorts, ip=False)
	# _.printVarSimple( ipsPorts )
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	# _.pr()
	ipsPorts = _.dic_key_sort2(ipsPorts, ip=True)
	# _.printVarSimple( ipsPorts )
	# sys.exit()

	if not _.switches.isActive('Plus'):
		for ip in ipsPorts:
			_.cp( ip, 'green' )

			ipsPorts[ip] = _.dic_key_sort2( ipsPorts[ip], n=True )
			# _.pr(ipsPorts[ip])

			for port in ipsPorts[ip]:
				if port in data:

					if _.switches.isActive('All'):
						_.pr(port)
						_.printVarSimple( data[port] )
					else:
						_.pr( '  ', _.cp( port, 'yellow', p=0 ), _.cp( data[port]['Description'], 'cyan', p=0 ) )
				else:
					# printRed = False
					try:
						if int(port) < 49152:
							printRed = True
						elif int(port) >= 49152:
							printRed = False

					except Exception as e:
						printRed = True
		
					if printRed:
						_.pr( '  ', _.cp( port, 'red', p=0 ), _.cp( 'not found', 'red', p=0 ) )
					else:
						_.pr( '  ', _.cp( port, 'yellow', p=0 ), _.cp( 'Ephemeral', 'cyan', p=0 ) )
	elif _.switches.isActive('Plus'):
		for ip in ipsPorts:
			printed = False
			for plus in _.switches.values('Plus'):
				if plus in ipsPorts[ip]:
					if not printed:
						printed = True
						_.pr( ip )



ipsPorts = {}
def action():
	global data
	global ephemeral
	global ipsPorts
	load()


	if _.switches.isActive('NetBrute'):
		try:
			research = _.appData[__.appReg]['pipe']
		except Exception as e:
			research = False

		if type(research) == list:

			for row in research:
				if len(row) and '#' in row:
					processPortRow(row) 

			ip_port_report()

		sys.exit()


	if _.switches.isActive('All') and not _.switches.isActive('PortScan'):


		for port in data:
			try:
				if int(port) > 0:
					_.pr( port )
			except Exception as e:
				pass

		sys.exit()

		# _.switches.fieldSet( 'Sort', 'active', True )
		# _.switches.fieldSet( 'Sort', 'value', 'port_sort' )
		# _.switches.fieldSet( 'Long', 'active', True )
		# _.tables.register( 'data', records )
		# _.tables.print( 'data', 'Port,TCP,UDP,Description' )


	# if type( _.appData[__.appReg]['pipe'] ) == list:
	#     for port in _.appData[__.appReg]['pipe']:
	#         if port in 
	
	
	if _.switches.isActive('PortScan'):
		port_scan()
		sys.exit()

	if not _.switches.isActive('Plus'):
		if not type( _.appData[__.appReg]['pipe'] ) == bool:
			_.pipeCleaner(0)
			research = _.appData[__.appReg]['pipe']
		else:
			research = _.switches.values('Ports')

		for search in research:
			search = search.replace(' ', '')
			if search in data.keys():
				if _.switches.isActive('All'):
					_.pr( data[search] )
				else:
					tcp_udp = []
					if 'y' in data[search]['TCP'].lower():
						tcp_udp.append( 'TCP' )
					if 'y' in data[search]['UDP'].lower():
						tcp_udp.append( 'UDP' )
					text = _.colorThis( ','.join(tcp_udp), 'green', p=0 )
					text += '\t'
					text += _.colorThis( data[search]['Description'], 'yellow', p=0 )
					_.pr( text )
			else:
				_.colorThis( [ 'Port '+search+' not found' ], 'red' )

	elif _.switches.isActive('Plus'):
		records = []
		total = 0
		totalAll = 0
		_.fields.register( 'ports', 'val', 7, m=15 )
		for record in data:
			totalAll = countPorts( record['Port'], totalAll )
			if _.showLine( record['Description'] ):
				tcp_udp = []
				if 'y' in record['TCP'].lower():
					tcp_udp.append( 'TCP' )
				if 'y' in record['UDP'].lower():
					tcp_udp.append( 'UDP' )
				record['port_sort'] = _.fields.padZeros( 'ports', 'val', record['Port'].split('-')[0] )
				record['tcp_udp'] = ','.join(tcp_udp)
				records.append( record )
				total = countPorts( record['Port'], total )

		# _.pr('totalAll',totalAll)
		if len(records):
			_.switches.fieldSet( 'Sort', 'active', True )
			_.switches.fieldSet( 'Sort', 'value', 'port_sort' )
			_.switches.fieldSet( 'Long', 'active', True )
			_.tables.register( 'data', records )
			_.tables.print( 'data', 'Port,TCP,UDP,Description' )
		
		if not _.switches.isActive('Clean'):
			theCount = [ {'data': _.addComma(len(records)), 'label':'Records'},{'data': _.addComma(total), 'label':'Ports'},{'data': _.addComma(len(data)), 'label':'Total Records'},{'data': _.addComma(totalAll), 'label':'Total Ports'},  ]
			_.fields.asset( 'totals', theCount )
			if len(records) == total:
				_.colorThis( [ '\n', '',  _.fields.value( 'totals', 'data', _.addComma(len(records)), right=1 )  , _.fields.value( 'totals', 'label', 'Ports' ) ], 'yellow' )
				# _.colorThis( [ '\n', '', _.addComma(len(records)), 'Ports' ], 'yellow' )
			else:
				# part = 
				_.colorThis( [ '\n', '',  _.fields.value( 'totals', 'data', _.addComma(len(records)), right=1 )  , _.fields.value( 'totals', 'label', 'Records' ) ], 'yellow' )
				_.colorThis( [ ' ',  _.fields.value( 'totals', 'data', _.addComma(total), right=1 )  , _.fields.value( 'totals', 'label', 'Ports' ) ], 'yellow' )
				# _.colorThis( [ ' ', _.addComma(total), '\t', 'Ports' ], 'yellow' )
			_.pr()
			_.colorThis( [  ' ',  _.fields.value( 'totals', 'data', _.addComma(len(data)), right=1 )  , _.fields.value( 'totals', 'label', 'Total Records' ) ], 'yellow' )
			_.colorThis( [  ' ',  _.fields.value( 'totals', 'data',  _.addComma(totalAll), right=1 )  , _.fields.value( 'totals', 'label', 'Total Ports' ) ], 'yellow' )
			# _.colorThis( [ '\n', '', _.addComma(len(data)), 'Total Records' ], 'yellow' )


def countPorts( ports, total=0 ):
	if not '-' in ports:
		total += 1
	else:
		parts = ports.split('-')
		port = int(parts[0])
		end = int(parts[1])
		while not port == end+1:
			total+=1
			port += 1
	return total
def generatePortsIndex():
	records = _.getCSV( _v.dbTables + _v.slash+'Ports_Complete_List.csv' )
	data = {}
	for record in records:
		if not '-' in record['Port']:
			data[ record['Port'] ] = record
		else:
			parts = record['Port'].split('-')
			port = int(parts[0])
			end = int(parts[1])
			# _.pr(parts)
			while not port == end+1:
				# _.pr( port )
				data[ str(port) ] = record
				port += 1
	_.saveTableDB( 'Ports_Complete_List_Index.json' )
	return data
			# sys.exit()
def load():
	global data
	global ephemeral

	ephemeral = False

	if _.switches.isActive('Ephemeral'):
		if _.switches.value('Ephemeral') == ''   or   't' in _.switches.value('Ephemeral').lower()   or   'y' in _.switches.value('Ephemeral').lower():
			ephemeral = True




	if not _.switches.isActive('Plus'):

		if not os.path.isfile( _v.dbTables + _v.slash+'Ports_Complete_List_Index.json' ):
			data = generatePortsIndex()
		else:
			data = _.getTableDB( 'Ports_Complete_List_Index.json' )

		dataB = {}
		for port in data:
			try:
				p = int(port)
				if p > 0:
					

					if ephemeral:
						dataB[ port ] = data[ port ]
					elif p < 49152:
						dataB[ port ] = data[ port ]
					
					if p == 80:
						data[ port ]['Description'] = 'http server'

					# else:
					#     _.pr( 'skipped:', port )


			except Exception as e:
				pass
		data = dataB
		del dataB
	

	elif _.switches.isActive('Plus'):
		data = _.getCSV( _v.dbTables + _v.slash+'Ports_Complete_List.csv' )

data = {}



########################################################################################
if __name__ == '__main__':
	action()







