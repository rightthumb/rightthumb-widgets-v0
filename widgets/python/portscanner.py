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
import socket

def appSwitches():
	_.switches.register( 'CIDR', '-cidr', '192.168.254.57/24' )
	_.switches.register( 'IPs', '-ip,-ips,-h,-host,-hosts', '192.168.254.1-254' )
	# _.switches.register( 'ThreadPrint', '-tp' )
	_.switches.register( 'Resolve', '-r,-resolve' )
	_.switches.register( 'Top', '-top', '20  OR 200 udp' )
	_.switches.register( 'Categories', '-cat,-category,-categories', 'ms OR microsoft' )
	_.switches.register( 'AllPorts', '-all' )
	_.switches.register( 'Max', '-max','800' )
	_.switches.register( 'Ports', '-port,-ports',' 9100 139 ' )
	_.switches.register( 'Save', '-save',' scan-tbcn-2021.04.csv ' )
	_.switches.register( 'DisplayFilter', '-filter','ports' )
	_.switches.register( 'HelpPortDescription', '-hp,-pd','53, 110, 80, 22, 21, 443, 995, 993, 143, 3306' )
	_.switches.register( 'Ridiculous', '-rd,-ridiculous' )
	_.switches.register( 'UDP', '-udp' )

	# _.switches.register( 'Quick', '-q' )

def hostname_to_ip(data):
	if not data[0] in '0123456789':
		try:
			data = socket.gethostbyname(data)
		except Exception as e:
			_.cp([e,'\n',data],'red')
			pass
	return data


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
	'file': 'portscanner.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'port scanner',
	'categories': [
						'network',
						'tool',
						'port',
						'scan',
						'ping',
						'resolve',
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
						'p portscanner -top 20  -ip 45.35.203.103 ',
						'p portscanner -top 200 -ip 45.35.203.103  ',
						'',
						'p portscanner -ip 192.168.254.57',
						'p portscanner -ip 192.168.254.1-x',
						'p portscanner -ip 192.168.254.1-254',
						'p portscanner -cidr 192.168.254.57/24',
						'p portscanner -cidr 192.168.254.57/24 ',
						'p portscanner -cidr 192.168.254.57/24 -top 20 -r',
						'p portscanner -cidr 192.168.254.57/24 -top 10 -r',
						'p portscanner -cidr 192.168.254.57/24 -top 200 udp -r',
						'p portscanner -cidr 192.168.254.57/24 -top 200 tcp -r',
						'p portscanner -cidr 192.168.254.57/24 -top 200 tcp -r -max 800',
						'',
						'',
						'p portscanner -cidr 192.168.254.57/24 -top 20 -r -save scan-home-2021.04.csv scan-home-2021.04.table',
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
	_.switches.trigger( 'IPs', hostname_to_ip )
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

def PC(ports):
	ports = ports.replace(' ','').replace(',,',',').split(',')
	ports.sort()
	return ports
# _.pr('ran 0', time.time() - __.test_epoch )

def testA():
	_.pr('ran A', time.time() - __.test_epoch )

def testB():
	# time.sleep( 5 )
	_.pr('ran B', time.time() - __.test_epoch )

def testC():
	# time.sleep( 5 )
	_.pr('ran C', time.time() - __.test_epoch )







# import subprocess
import platform
 
def ping_ip(current_ip_address):
		try:
			output = subprocess.check_output("ping -{} 4 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
			if 'unreachable' in output:
				return False
			else:
				return True
		except Exception:
				return False
 







def resolve_address(address=None):
	global IP_Table
	# _.pr(resolve_address)
	if address is None:
		_.pr( 'missing address' )
		return None
	# _.pr( address )
	# host = ping(address, count=4, interval=1, timeout=2, source=None, privileged=True)

	# host = pyping.ping( address )

	# host = do_one( address, 2 )



	# return_code = subprocess.run(["ping", "-c", "1", "-n","4", "-q", address],
 #                                 stdout=subprocess.DEVNULL,
 #                                 stderr=subprocess.DEVNULL)


	# return_code = ping_ip(address)




	the_mac = get_mac_address(ip=address, network_request=True)
	# _.pr(the_mac)

	# _.pr(return_code,address)
	scan = False
	if _.switches.isActive('Top') or _.switches.isActive('Categories') or _.switches.isActive('AllPorts') or _.switches.isActive('Ports'):
		if _.switches.isActive('Resolve') and the_mac:
			scan = True
		elif not _.switches.isActive('Resolve'):
			scan = True
	
	if the_mac:
		# _.pr( 'scan:', scan )
		THE_IP_DIC( a=address, m=the_mac )
		get_name(address)

	if scan:
		__.asyn.register( name=address, category='scan', fn=scan_address, a=address, timeout=1 )

	
		# _.pr( the_mac, name )




	# _.pr( host.packets_received, type(host.packets_received) )
	
	# for x in dir(return_code):
	#     _.pr(x)
	# sys.exit()

	# _.pr( host.__dict__['_packets_received'] )

	# sys.exit()
	# _.pr(host.packets_received,address)
	# if host.__dict__['_packets_received']:
		# IP_Table[address] = host.__dict__['_packets_received']
		# _.pr(1)
	# else:
		# _.pr(0)

def THE_IP_DIC( a=None, m=None, n=None, v=None, p=None ):
	global IP_Table
	if not a in IP_Table:
		IP_Table[a] = { 'address': '', 'mac': '', 'name': '', 'vendor': '', 'ports': '', 'p': {} }
	
	if not a is None:
		IP_Table[a]['address'] = a
	if not m is None:
		IP_Table[a]['mac'] = m
	if not n is None:
		IP_Table[a]['name'] = n
	if not v is None:
		IP_Table[a]['vendor'] = v
	if not p is None:
		if not p in IP_Table[a]['p']:
			IP_Table[a]['p'][p] = 1
		IP_Table[a]['ports'] = ', '.join(  list(  IP_Table[a]['p'].keys()  )  )

	return IP_Table[a]



def get_name(address):
	global IP_Table
	run = False
	if not address in IP_Table:
		run = True
	if address in IP_Table and not IP_Table[address]['name']:
		run = True
	# _.pr('run',run)
	name = ''
	try:
		name = socket.getfqdn(address)
	except Exception as e:
		pass
	# _.pr('name',name)
	if name:
		THE_IP_DIC( a=address, n=name )
		# _.pr(x)

	

def resolution_results():
	# _.pr( 'Report:' )
	global IP_Table
	global mac_vendor_table

	# _.pr( 400 )
	IP_Table = _.dic_key_sort2(IP_Table,ip=True)
	# _.pr( 401 )



	records = []

	# _.pr( 401 )
	for address in IP_Table:

		vend = ''
		m = IP_Table[address]['mac'].replace(':','').replace('-','').upper()[:6]
		if m in mac_vendor_table:
			vend = mac_vendor_table[m]

		# get_name(address)
		rec = THE_IP_DIC(a=address,v=vend)
		del rec['p']
		records.append( dic_cleaner(rec) )
		


	_.pr()
	if _.switches.isActive('DisplayFilter'):
		recs = []
		if 'port' in _.switches.value('DisplayFilter').lower():
			for rec in records:
				# _.pr( type(rec['ports']), rec['ports'])
				if len(rec['ports']):
					recs.append(dic_cleaner(rec))
			records = recs
	_.tables.register( 'IPS', records )
	_.tables.print( 'IPS', 'address,name,vendor,mac,ports' )
	_.pr()
	if not len(records) == len(IP_Table):
		_.cp(  [ '\n', '', len(records),'of',len(IP_Table) ], 'yellow'  )
	else:
		_.cp(  [ '\n', '', len(IP_Table) ], 'yellow'  )

	if _.switches.isActive('Save') and len(_.switches.value('Save')):
		for save in _.switches.values('Save'):
			if save.endswith('.csv'):
				# _.saveCSV( records, save, printThis=True )
				_.csv2( records, save, printThis=True )
			else:
				_.saveTable2( records, save, printThis=True )



def processIPs():
	global IP_Table
	if _.switches.isActive('Top') or _.switches.isActive('Categories') or _.switches.isActive('AllPorts') or _.switches.isActive('Ports'):
		scan = True
	else:
		scan = False


	if _.switches.isActive('CIDR'):
		for network in _.switches.values('CIDR'):
			# _.pr(network)
			# sys.exit()
			try:
				for ip in IPNetwork( network )[1:-1]:
					ip = str(ip)
					# _.pr(ip)
					# resolve_address(ip)
					# sys.exit()
					__.asyn.register( name=ip, category='resolve', fn=resolve_address, a=ip )
					# if scan:
					#     if not _.switches.isActive('Resolve'):
					#         __.asyn.register( name=ip, category='scan', fn=scan_address, a=ip )
					#     elif ip in IP_Table:
					#         __.asyn.register( name=ip, category='scan', fn=scan_address, a=ip )

			except Exception as e:
				_.cp(  [ 'Error: cidr', network ], 'red'  )
			



	elif not  _.switches.isActive('CIDR'):
		for IPs in _.switches.values('IPs'):
			if not '-' in IPs and IPs.count('.') == 3:
				# _.pr('here')
				# _.pr('here')
				# resolve_address(ip)
				__.asyn.register( name=IPs, category='resolve', fn=resolve_address, a=IPs )
				# if scan:
				#     if not _.switches.isActive('Resolve'):
				#         __.asyn.register( name=IPs, category='scan', fn=scan_address, a=IPs )
				#     elif IPs in IP_Table:
				#         __.asyn.register( name=IPs, category='scan', fn=scan_address, a=IPs )
			elif '-' in IPs and IPs.count('.') == 3:
				ips = IPs.split('-')[0]
				r = IPs.split('-')[1]
				if r == 'x':
					r = '254'
				for x in range( int(ips.split('.')[3]), int(r)+1 ):
					ip = ips.split('.')[0] +'.'+ ips.split('.')[1] +'.'+ ips.split('.')[2] +'.'+ str(x)
					__.asyn.register( name=ip, category='resolve', fn=resolve_address, a=ip )
					# if scan:
					#     if not _.switches.isActive('Resolve'):
					#         __.asyn.register( name=ip, category='scan', fn=scan_address, a=ip )
					#     elif ip in IP_Table:
					#         __.asyn.register( name=ip, category='scan', fn=scan_address, a=ip )
					# _.pr(ip)


def scan_address(address):
	# _.pr('scan_address:', address)
	'''
	'''
	global spent_ports
	if _.switches.isActive('Top') or _.switches.isActive('Categories') or _.switches.isActive('AllPorts') or _.switches.isActive('Ports'):
		scan = True
	else:
		scan = False
	if scan:
		# _.pr(' HERE A ')
		ports = []
		if _.switches.isActive('Ports'):
			ports = _.switches.values('Ports')
		elif _.switches.isActive('Top'):
			# _.pr(' HERE B ')
			if _.switches.value('Top') == '':
				ports = __.ports_hash['top']
			elif _.switches.value('Top') == '20':
				ports = __.ports_hash['20']
			elif _.switches.values('Top')[0] == '200':
				if not len(_.switches.values('Top')) > 1:
					ports = __.ports_hash['200']['tcp']
				elif 't' in  _.switches.values('Top')[1].lower():
					ports = __.ports_hash['200']['tcp']
				elif 'u' in  _.switches.values('Top')[1].lower():
					ports = __.ports_hash['200']['udp']
					_.switches.fieldSet( 'UDP', 'active', True )
			else:
				# _.pr(' HERE C ')
				if int(  _.switches.values('Top')[0]  ) > len(__.ports_hash['top']):
					ports = __.ports_hash['top']
				else:
					ports = __.ports_hash['top'][: int(  _.switches.values('Top')[0]  ) ]
				# _.pr(' HERE D ')
			pass
		
		# _.pr(' HERE xXx ')
		if not address in spent_ports:
			spent_ports[address] = {}
		# _.pr(ports)
		selected_ports = []
		for port in ports:
			if len(port):
				port = port.replace( ' ', '' )
				if not '-' in port:
					if int(port) < __.ephemeral:
						if not port in spent_ports[address]:
							spent_ports[address][port] = 1
							selected_ports.append(int(port))
							# __.asyn.register( name=address+port, category='ports', fn=scan_port, k=[address, port], timeout=3 )
				elif '-' in port:
					for p in range( int(port.split('-')[0]),  int(port.split('-')[1])+1 ):
						if p < __.ephemeral:
							if not str(p) in spent_ports[address]:
								spent_ports[address][str(p)] = 1
								selected_ports.append(int(p))
								# __.asyn.register( name=address+str(p), category='ports', fn=scan_port, k=[address, p], timeout=3 )
		selected_ports.sort()
		for port in selected_ports:
			__.asyn.register( name=address+str(port), category='ports', fn=scan_port, k=[address, port], timeout=3 )




		# elif _.switches.isActive('Categories'):
		# elif _.switches.isActive('AllPorts'):



def action():
	if _.switches.isActive('Ridiculous'):
		_.switches.fieldSet( 'Max', 'active', True )
		_.switches.fieldSet( 'Max', 'value', '800' )
		_.switches.fieldSet( 'Max', 'values', ['800'] )

		_.switches.fieldSet( 'Resolve', 'active', True )
		
		_.switches.fieldSet( 'Top', 'active', True )
		_.switches.fieldSet( 'Top', 'value', '200,tcp' )
		_.switches.fieldSet( 'Top', 'values', ['200','tcp'] )
		# __.ports_hash['200']['tcp']=PC('1-65535')


	load()
	# if _.switches.isActive('Ridiculous'): __.ports_hash['200']['tcp']=PC('1-65535')

	_.switches.fieldSet( 'Long', 'active', True )


	if _.switches.isActive('HelpPortDescription'):
		index = _.getTableDB( 'Ports_Complete_List_Index.json' )
		for p in _.switches.values('HelpPortDescription'):
			p = p.replace(',','')
			if p in index:
				rec = index[p]
				tcp = False
				udp = False
				if 'TCP' in rec and not rec['TCP'] == 'No':
					tcp = True
				if 'UDP' in rec and not rec['UDP'] == 'No':
					udp = True
				tcp_udp = ''
				if tcp:
					tcp_udp += ' '+_.cp('TCP','green',p=0)+' '
				else:
					tcp_udp += ' '+_.cp('TCP','red',p=0)+' '
				if udp:
					tcp_udp += ' '+_.cp('UDP','green',p=0)+' '
				else:
					tcp_udp += ' '+_.cp('UDP','red',p=0)+' '
				_.pr()
				_.pr(p)
				_.pr(tcp_udp)
				des = _.autoWrapText(rec['Description'],prefix=' ')
				if type(des) == str:
					des = [des]
				for line in des:
					_.pr(line)
				_.pr()
				# _.pv(rec)
		
		return None

	# scan_port( '192.168.254.57', '1' )
	# scan_port( '192.168.254.57', '80' )
	# scan_port( '192.168.254.57', '139' )
	# scan_port( '192.168.254.57', '9100' )
	# sys.exit()

	# global data
	
	# if not _.switches.isActive('Top') and not _.switches.isActive('Categories') and not _.switches.isActive('AllPorts'):
	#     _.switches.fieldSet( 'Resolve', 'active', True )

	__.asyn.cp( 'resolve', 1 )
	__.asyn.cp( 'ip', 2 )
	__.asyn.cp( 'name', 3 )
	__.asyn.cp( 'scan', 4 )
	__.asyn.cp( 'ports', 5 )

	# if _.switches.isActive('ThreadPrint'):
	__.asyn.print = 1

	__.asyn.max = 600
	if _.switches.isActive('Max'):
		__.asyn.max = int( _.switches.value('Max') )



	# if _.switches.isActive('Resolve'):
	__.asyn.atExit( category=None, name=None, fn=resolution_results )


	processIPs()
	
	# __.asyn.register( fn=testB )
	# __.asyn.register( fn=testC )



def load():
	global mac_vendor_table

	mac_vendor_table = _.getTableDB( 'mac-vendors.hash' )
	# with open( _v.myDatabank+_v.slash+'tables'+_v.slash+'mac-vendors.txt' , mode='rb') as f:
	#     for l in ( f.read()).splitlines():
	#         prefix, vendor = l.split(b":", 1)
	#         mac_vendor_table[prefix.upper()] = vendor
	# _.saveTableDB( mac_vendor_table, 'mac-vendors.hash' )

	# test = '123456789'
	# _.pr( test[:6] )
	# _.printVarSimple( mac_vendor_table )
	# sys.exit()

# myDatabank

	
def report_fix_test():
	IP_Table = {'localhost': 1, '192.168.254.30': 1, '192.168.254.62': 1, '192.168.254.75': 1, '192.168.254.78': 1, '192.168.254.82': 1, '192.168.254.86': 1, '192.168.254.97': 1, '192.168.254.95': 1, '192.168.254.64': 1, '192.168.254.66': 1, '192.168.254.73': 1, '192.168.254.74': 1, '192.168.254.81': 1, '192.168.254.87': 1, '192.168.254.60': 1, '192.168.254.61': 1, '192.168.254.68': 1, '192.168.254.71': 1, '192.168.254.72': 1, '192.168.254.88': 1, '192.168.254.90': 1, '192.168.254.93': 1, '192.168.254.94': 1, '192.168.254.99': 1, '192.168.254.65': 1, '192.168.254.69': 1, '192.168.254.77': 1, '192.168.254.80': 1, '192.168.254.85': 1, '192.168.254.91': 1, '192.168.254.89': 1, '192.168.254.92': 1, '192.168.254.96': 1, '192.168.254.59': 1, '192.168.254.70': 1, '192.168.254.79': 1, '192.168.254.84': 1, '192.168.254.83': 1, '192.168.254.100': 1, '192.168.254.98': 1, '192.168.254.63': 1, '192.168.254.67': 1, '192.168.254.76': 1, '192.168.254.38': 1, '192.168.254.5': 1, '192.168.254.51': 1, '192.168.254.12': 1, '192.168.254.15': 1, '192.168.254.26': 1, '192.168.254.18': 1, '192.168.254.29': 1, '192.168.254.28': 1, '192.168.254.20': 1, '192.168.254.45': 1, '192.168.254.7': 1, '192.168.254.46': 1, '192.168.254.44': 1, '192.168.254.2': 1, '192.168.254.10': 1, '192.168.254.31': 1, '192.168.254.35': 1, '192.168.254.52': 1, '192.168.254.25': 1, '192.168.254.53': 1, '192.168.254.17': 1, '192.168.254.55': 1, '192.168.254.6': 1, '192.168.254.22': 1, '192.168.254.27': 1, '192.168.254.34': 1, '192.168.254.47': 1, '192.168.254.1': 1, '192.168.254.32': 1, '192.168.254.16': 1, '192.168.254.13': 1, '192.168.254.3': 1, '192.168.254.40': 1, '192.168.254.9': 1, '192.168.254.54': 1, '192.168.254.8': 1, '192.168.254.36': 1, '192.168.254.33': 1, '192.168.254.23': 1, '192.168.254.58': 1, '192.168.254.49': 1, '192.168.254.21': 1, '192.168.254.56': 1, '192.168.254.39': 1, '192.168.254.19': 1, '192.168.254.57': 1, '192.168.254.41': 1, '192.168.254.50': 1, '192.168.254.43': 1, '192.168.254.14': 1, '192.168.254.42': 1, '192.168.254.24': 1, '192.168.254.37': 1, '192.168.254.11': 1, '192.168.254.48': 1, '192.168.254.4': 1, '192.168.254.254': 1}

	# _.pr(IP_Table)
	IP_Table = _.dic_key_sort2(IP_Table,ip=True)
	# _.pr(IP_Table)

	for ip in IP_Table:
		_.pr( ip )


	_.pr( '', len(IP_Table)  )



def check_port_udp(host, port):
	# https://stackoverflow.com/questions/42867192/python-check-udp-port-open
	import socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(2)
	try:
		s.sendto('ping'.encode(), (host, port))
		s.recvfrom(1024)
	except socket.timeout:
		s.close()
		return 0
	s.close()
	return 1


def scan_port( ip, port ):
	# _.pr( ip, port )
	port = int(port)
	if port >= __.ephemeral:
		return None

	global data
	if not type(port) == int:
		try:
			port = int(port)
		except Exception as e:
			pass
	if not type(port) == int:
		return None

	# Create a new socket
	if _.switches.isActive('UDP'):
		# if check_port_udp(ip,port):
		#     THE_IP_DIC( a=ip, p=str(port) )
		connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	else:
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# _.pr( connection.gettimeout() )
	# sys.exit()
	connection.settimeout(2)
	# _.pr( connection.connect_ex((ip, port)), port )


	# Print if the port is open
	result = connection.connect_ex((ip, port))
	# _.pr( result, port )

	# for x in dir(result):
	#     _.pr(x)

	try:
		connection.close()
	except Exception as e:
		pass




	if not result:
		THE_IP_DIC( a=ip, p=str(port) )
		# _.pr( 'not result:', port )
	# else:
		# _.pr( 'result:', port )
		# _.pr('[+] %s:%d/TCP Open' % (ip, port) )
		# _.pr('[+] %s:%d/TCP Open' % (ip, port) , data[str(port)]['Description'] )

spent_ports = {}
__.ports_hash = {
					'top': PC(' 27018,2701,27017, 9100,80, 20-23,25,53,110-111,135-139,143,443,445,993,995,1723,3306,3389,5900,8080,   1701, 500, 4500 ,554,   50, 51,67, 68,69,80,119,123,161, 162,389,989, 990, 7,19,20-21,22,23,25,42,43,49,53,67-68,69,70,79,80,88,102,110,113,119,123,135,137-139,143,161-162,177,179,201,264,318,381-383,389,411-412,443,445,464,465,497,500,512,513,514,515,520,521,540,554,546-547,560,563,587,591,593,631,636,639,646,691,860,873,902,989-990,993,995,1025,1026-1029,1080,1080,1194,1214,1241,1311,1337,1433-1434,1512,1589,1701,1723,1725,1741,1755,1812-1813,1863,1985,2000,2002,2049,2082-2083,2100,2222,2302,2483-2484,2745,2967,3050,3074,3124,3127,3128,3222,3260,3306,3389,3689,3690,3724,3784-3785,4333,4444,4664,4672,4899,5000,5001,5001,5004-5005,5050,5060,5190,5222-5223,5432,5500,5554,5631-5632,5800,5900,6000-6001,6112,6129,6257,6346-6347,6500,6566,6588,6665-6669,6679,6697,6699,6881-6999,6891-6901,6970,7212,7648-7649,8000,8080,8086-8087,8118,8200,8500,8767,8866,9100,9101-9103,9119,9800,9898,9988,9999,10000,10113-10116,11371,12035-12036,12345,13720-13721,14567,15118,19226,19638,20000,24800,25999,27015,27374,28960,31337,33434, 1,3,7,9,13,17,19,21-23,25-26,37,53,79-82,88,100,106,110-111,113,119,135,139,143-144,179,199,254-255,280,311,389,427,443-445,464-465,497,513-515,543-544,548,554,587,593,625,631,636,646,787,808,873,902,990,993,995,1000,1022,1024-1033,1035-1041,1044,1048-1050,1053-1054,1056,1058-1059,1064-1066,1069,1071,1074,1080,1110,1234,1433,1494,1521,1720,1723,1755,1761,1801,1900,1935,1998,2000-2003,2005,2049,2103,2105,2107,2121,2161,2301,2383,2401,2601,2717,2869,2967,3000-3001,3128,3268,3306,3389,3689-3690,3703,3986,4000-4001,4045,4899,5000-5001,5003,5009,5050-5051,5060,5101,5120,5190,5357,5432,5555,5631,5666,5800,5900-5901,6000-6002,6004,6112,6646,6666,7000,7070,7937-7938,8000,8002,8008-8010,8031,8080-8081,8443,8888,9000-9001,9090,9100,9102,9999-10001,10010,32768,32771,49152-49157,50000, 7,9,13,17,19,21-23,37,42,49,53,67-69,80,88,111,120,123,135-139,158,161-162,177,192,199,389,407,427,443,445,464,497,500,514-515,517-518,520,593,623,626,631,664,683,800,989-990,996-999,1001,1008,1019,1021-1034,1036,1038-1039,1041,1043-1045,1049,1068,1419,1433-1434,1645-1646,1701,1718-1719,1782,1812-1813,1885,1900,2000,2002,2048-2049,2148,2222-2223,2967,3052,3130,3283,3389,3456,3659,3703,4000,4045,4444,4500,4672,5000-5001,5060,5093,5351,5353,5355,5500,5632,6000-6001,6346,7938,9200,9876,10000,10080,11487,16680,17185,19283,19682,20031,22986,27892,30718,31337,32768-32773,32815,33281,33354,34555,34861-34862,37444,39213,41524,44968,49152-49154,49156,49158-49159,49162-49163,49165-49166,49168,49171-49172,49179-49182,49184-49196,49199-49202,49205,49208-49211,58002,65024'),
					'20': PC('5000,9100,80, 21-23,25,53,110-111,135-139,143,443,445,993,995,1723,3306,3389,5900,8080,1701,27017,5432,783,953,579,323,579,2087'),
					'30': PC('5000,9100,80, 21-23,25,53,110-111,135-139,143,443,445,993,995,1723,3306,3389,5900,8080,1701,27017,5432,783,953,579,323,579,2087'),
					'200': {
						'tcp': PC('9100,1,3,7,9,13,17,19,21-23,25-26,37,53,79-82,88,100,106,110-111,113,119,135,139,143-144,179,199,254-255,280,311,389,427,443-445,464-465,497,513-515,543-544,548,554,587,593,625,631,636,646,787,808,873,902,990,993,995,1000,1022,1024-1033,1035-1041,1044,1048-1050,1053-1054,1056,1058-1059,1064-1066,1069,1071,1074,1080,1110,1234,1433,1494,1521,1720,1723,1755,1761,1801,1900,1935,1998,2000-2003,2005,2049,2103,2105,2107,2121,2161,2301,2383,2401,2601,2717,2869,2967,3000-3001,3128,3268,3306,3389,3689-3690,3703,3986,4000-4001,4045,4899,5000-5001,5003,5009,5050-5051,5060,5101,5120,5190,5357,5432,5555,5631,5666,5800,5900-5901,6000-6002,6004,6112,6646,6666,7000,7070,7937-7938,8000,8002,8008-8010,8031,8080-8081,8443,8888,9000-9001,9090,9100,9102,9999-10001,10010,32768,32771,49152-49157,50000'),
						'udp': PC('7,9,13,17,19,21-23,37,42,49,53,67-69,80,88,111,120,123,135-139,158,161-162,177,192,199,389,407,427,443,445,464,497,500,514-515,517-518,520,593,623,626,631,664,683,800,989-990,996-999,1001,1008,1019,1021-1034,1036,1038-1039,1041,1043-1045,1049,1068,1419,1433-1434,1645-1646,1701,1718-1719,1782,1812-1813,1885,1900,2000,2002,2048-2049,2148,2222-2223,2967,3052,3130,3283,3389,3456,3659,3703,4000,4045,4444,4500,4672,5000-5001,5060,5093,5351,5353,5355,5500,5632,6000-6001,6346,7938,9200,9876,10000,10080,11487,16680,17185,19283,19682,20031,22986,27892,30718,31337,32768-32773,32815,33281,33354,34555,34861-34862,37444,39213,41524,44968,49152-49154,49156,49158-49159,49162-49163,49165-49166,49168,49171-49172,49179-49182,8888,49184-49196,49199-49202,49205,49208-49211,58002,65024'),
					}


}



# __.ports_hash['top']=PC('1-65535')
# __.ports_hash['top']=PC('0, 1, 2, 3, 5, 7, 9, 9, 11, 13, 15, 17, 18, 19, 20, 21, 22, 23, 25, 27, 28, 29, 31, 33, 37, 38, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71–74, 76, 78, 79, 80, 81, 82, 82, 83, 84, 85, 86, 88, 89, 90, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 113, 113, 115, 117, 118, 119, 123, 126, 135, 135, 137, 138, 139, 143, 151, 152, 153, 156, 158, 161, 162, 165, 169, 170, 177, 179, 180, 194, 199, 201, 209, 210, 213, 218, 220, 225–241, 249–255, 259, 262, 264, 280, 300, 308, 311, 312, 318, 319, 320, 350, 351, 356, 366, 369, 370, 370, 371, 376, 383, 384, 387, 388, 389, 399, 401, 427, 433, 434, 443, 444, 445, 445, 464, 465, 465, 465, 475, 476–490, 491, 497, 500, 502, 504, 510, 512, 512, 513, 513, 514, 514, 515, 517, 518, 520, 520, 521, 524, 525, 530, 532, 533, 540, 542, 543, 544, 546, 547, 548, 550, 554, 556, 560, 561, 563, 564, 585, 587, 591, 593, 601, 604, 623, 625, 631, 631, 635, 636, 639, 641, 643, 646, 647, 648, 651, 653, 654, 655, 657, 660, 666, 666, 674, 688, 690, 691, 694, 695, 698, 700, 701, 702, 706, 711, 712, 749, 750, 751, 752, 753, 753, 754, 754, 760, 782, 783, 800, 802, 808, 829, 830, 831, 832, 833, 843, 847, 848, 853, 853, 860, 861, 862, 873, 888, 888, 897, 898, 902, 903, 953, 981, 987, 987, 988, 989, 990, 991, 992, 993, 994, 995, 1010, 1011–1020, 1023, 1023')
if _.switches.isActive('Ridiculous'): __.ports_hash['200']['tcp']=PC('20-23,25-26,37,53,67-69,70,79-84,85,88,90,99-111,113,119,123,135,137-139,143-144,161,179,199,389,427,443-445,465,500,512-515,520,523,548,554,587,593,631,636,646,873,902,989-990,993,995,1023-1031,1080,1110,1194,1234,1311,1433,1434,1521,1604,1701,1720-1723,1755,1812-1813,1900,2000-2001,2049,2100,2121,2222,2301,2375-2376,2483-2484,2600-2601,2745,2967,3050,3128,3260,3306,3333,3389,3689,3986,4443,4500,4662,4899,5000-5001,5037,5050-5051,5060-5061,5101,5222-5223,5353,5432,5500,5555-5556,5631-5632,5800,5900-5901,5984,5985-5986,6000-6006,6112,6129,6257,6379,6443,6502,6660-6669,6679,6697,6881,6969-7000,7070,7100,7200,7547,7680,7777-7778,8000-8010,8022,8080-8083,8088-8090,8180,8222,8333,8443,8500,8600,8649,8888,9000-9010,9042,9060,9090-9100,9152,9200-9201,9300-9301,9418,9443,9555,9999,10000-10001,10010,10050-10051,10082,10243,11211,12000,12345,13720-13721,14567,15000,16080,17235,18006,18067,18077,18091,18101,18182,20000,30718,32768-32771,33389,37777,40000,49152-49161,49163,49165,49167,49175-49176,49400,49999')
# if _.switches.isActive('Ridiculous'): __.ports_hash['200']['tcp']=PC('1-49152')
# if _.switches.isActive('Ridiculous'): __.ports_hash['200']['tcp']=PC('1-65535')

IP_Table = {}

__.ephemeral = 49152

__.test_epoch = time.time()
_async = _.regImp( __.appReg, '_rightThumb._asynchronous' )
# from icmplib import ping
# import pyping
# import ping
# for x in dir(ping):
#     _.pr(x)
# sys.exit()

import subprocess
from getmac import get_mac_address

if _.switches.isActive('CIDR'):
	from netaddr import IPNetwork


def dic_cleaner(rec):
	if 'address' in rec and 'name' in rec:
		if rec['name'] == rec['address']: rec['name']=''
	return rec


########################################################################################
if __name__ == '__main__':
	action()
	# report_fix_test()