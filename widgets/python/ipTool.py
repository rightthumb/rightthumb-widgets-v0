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
# import simplejson as json
# from threading import Timer


##################################################
# construct registration

import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
# appDBA = __name__
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

# from lxml import html
# import requests
# import cssselect
# import sqlite3

##################################################


def appSwitches():
	pass 
	_.switches.register( 'IPAddress', '-ip' )
	_.switches.register( 'cidr', '-cidr' )
	_.switches.register( 'SubnetMask', '-mask,-netmask,-subnetmask' )
	_.switches.register( 'List', '-list' )
	_.switches.register( 'Clean', '--c' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe=True, isRequired=True, description='Files' )
	# _.switches.register( 'Files', '-f,-file,-files','file.txt', isPipe='name,data,clean', description='Files' )


	"""
	_.switches.documentation( 'Test', { 
										'examples': [
														'',
													],

										'required': [],
										'related': [],
										'isRequired': False,
									} )
	"""


_.autoBackupData = True
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'ip.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'IP tool',
	'categories': [
						'ip',
						'tool',
						'convert',
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
						'p ip -cidr -netmask 255.255.255.0',
						'p ip -cidr 24 -mask',
						'p ip -cidr 24 -netmask',
						'p ip -cidr 24 -subnetmask',
						'',
						'p ipTool -ip 192.168.1.0 -netmask 255.255.255.0',
						'p ipTool -cidr 192.168.0/24',
						'p ipTool -cidr 192.168.1.0/24 -list',
						'p ipTool -ip 192.168.1.0 -subnetmask 255.255.255.0 -list',
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

# _.appInfo[focus()]['examples'].append( 'p thisApp -file file.txt' )

# _.appInfo[focus()]['columns'].append( {'name': 'name', 'abbreviation': 'n'} )



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
	
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	# _.switches.trigger( 'Watched', _.txt2Date )
	# _.switches.trigger( 'Input',_.formatColumns )
	# _.switches.trigger( 'Franchise',_.triggerSpace )
	
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
# data = _.tables.returnSorted( 'data', 'd.timestamp', data )
# _.switches.fieldSet( 'Long', 'active', True )
# _.tables.register( 'data', table )
# _.tables.print( 'data', 'name' )
# p = _.getText( _v.pips, raw=True, clean=True ).split( '\n' )
# os.system( '"' + do + '"' )
# _.setPipeData( os.listdir( os.getcwd() ), focus() )
# _.showLine( item )
#     if os.path.isdir( row ):
#     if os.path.isfile( row ):
# __.appRegPipe
########################################################################################
# START


import socket
import struct
from netaddr import IPNetwork



def cidr_to_netmask(cidr):
	cidr = int(cidr)
	mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
	return (str( (0xff000000 & mask) >> 24)   + '.' +
			str( (0x00ff0000 & mask) >> 16)   + '.' +
			str( (0x0000ff00 & mask) >> 8)    + '.' +
			str( (0x000000ff & mask)))

def cidr_to_netmask_network(cidr):
	network, net_bits = cidr.split('/')
	host_bits = 32 - int(net_bits)
	netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
	return network, netmask


def addressInNetwork(ip, net):
	# import socket,struct
	ipaddr = int(''.join([ '%02x' % int(x) for x in ip.split('.') ]), 16)
	netstr, bits = net.split('/')
	netaddr = int(''.join([ '%02x' % int(x) for x in netstr.split('.') ]), 16)
	mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
	return (ipaddr & mask) == (netaddr & mask)



def action():
	load()

	clean = _.switches.isActive('Clean')
	if len(_.switches.all()) == 2 and _.switches.isActive('cidr') and _.switches.isActive('SubnetMask') and not len(_.switches.value('cidr')) and len(_.switches.value('SubnetMask')) :
		# from netaddr import IPAddress
		# cidr = IPAddress(  _.switches.value('GenerateCidr')  ).netmask_bits()

		cidr = sum(bin(int(x)).count('1') for x in _.switches.value('SubnetMask').split('.'))
		if not clean:
			_.pr( cidr )
		return cidr
	elif len(_.switches.all()) == 2 and _.switches.isActive('cidr') and _.switches.isActive('SubnetMask') and len(_.switches.value('cidr')) and  len(_.switches.value('cidr')) < 4 and not len(_.switches.value('SubnetMask')) :
		netmask = cidr_to_netmask(_.switches.value('cidr'))
		if not clean:
			_.pr(netmask)
		return netmask

	elif len(_.switches.all()) == 1 and _.switches.isActive('cidr') and  _.switches.isActive('cidr') and _.switches.value('cidr').count('.') == 3  and _.switches.value('cidr').count('/') == 1:
		network = cidr_to_netmask_network(_.switches.value('cidr'))
		i=0
		for ip in IPNetwork(_.switches.value('cidr')):
			i+=1
		if not clean:
			_.pr( '\n'.join( network ) )
			_.pr( 'IPs:', i )
		return network
	elif len(_.switches.all()) == 2 and _.switches.isActive('List') and _.switches.isActive('cidr') and  _.switches.isActive('cidr') and _.switches.value('cidr').count('.') == 3  and _.switches.value('cidr').count('/') == 1:
		IPs = []
		for ip in IPNetwork(_.switches.value('cidr')):
			IPs.append( ip )
			if not clean:
				_.pr(ip)
		return IPs
	elif len(_.switches.all()) == 3 and _.switches.isActive('List') and _.switches.isActive('IPAddress') and  _.switches.isActive('SubnetMask'):
		cidr = sum(bin(int(x)).count('1') for x in _.switches.value('SubnetMask').split('.'))
		IPs = []
		i=0
		for ip in IPNetwork( _.switches.value('IPAddress')+'/'+str(cidr) ):
			i+=1
			IPs.append( ip )
			if not clean:
				_.pr(ip)
		if not clean:
			_.pr( 'IPs:', i )
		return IPs
	elif len(_.switches.all()) == 2 and _.switches.isActive('IPAddress') and  _.switches.isActive('SubnetMask'):
		cidr = sum(bin(int(x)).count('1') for x in _.switches.value('SubnetMask').split('.'))
		netmask = cidr_to_netmask(cidr)
		IPs = []
		i=0
		for ip in IPNetwork( _.switches.value('IPAddress')+'/'+str(cidr) ):
			i+=1
			IPs.append( ip )
		if not clean:
			_.pr( _.switches.value('IPAddress')+'/'+str(cidr) )
			_.pr( 'IPs:', i )
			if not netmask == _.switches.value('SubnetMask'):
				_.pr()
				_.pr( 'Fixed:', netmask )
		return IPs
	pass



def load():
	pass

########################################################################################
if __name__ == '__main__':
	action()