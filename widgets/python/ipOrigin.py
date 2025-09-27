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

# import os
import sys
# import simplejson as json
import _rightThumb._base1 as _
import _rightThumb._vars as _v
import _rightThumb._string as _str
from netaddr import IPAddress
import socket,struct

from lxml import html
import requests
import cssselect


_.switches.register('Countries', '-countries,-test')
_.switches.register('IP', '-ip')
_.switches.register('All', '-all')

# _.appInfo=    {
#     'file': 'origin.py',
#     'description': 'Manages drives and indexes',
#     'prerequisite': [],
#     'examples': [],
#     'columns': [],
#     }

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
_.switches.process()

# _.tableProfile.append({
#     'field': 'timestamp', 
#     'script_trigger_external': _.float2Date
#     })

# if _.switches.isActive('File') == False:
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
#     xRefList = _.sort(xRefList, 'new')
#     _.tables.register('Auto',_.switch)
#     _.tables.print('Auto','name,switch,expected_input_example')
	# _.saveTable(rows,theFile,tableTemp = True,printThis = True)
	# theTable = _.getTable(theFile,tableTemp = True,printThis = False)


########################################################################################

def netmask_to_cidr(netmask):
	'''
	:param netmask: netmask ip addr (eg: 255.255.255.0)
	:return: equivalent cidr number to given netmask ip (eg: 24)
	'''
	return sum([bin(int(x)).count('1') for x in netmask.split('.')])

def makeMask(n):
	"return a mask of n bits as a long integer"
	return (2<<n-1) - 1

def dottedQuadToNum(ip):
	"convert decimal dotted quad string to long integer"
	return struct.unpack('L',socket.inet_aton(ip))[0]

def networkMask(ip,bits):
	"Convert a network address to a long integer" 
	return dottedQuadToNum(ip) & makeMask(bits)

def addressInNetwork(ip, net):
   import socket,struct
   ipaddr = int(''.join([ '%02x' % int(x) for x in ip.split('.') ]), 16)
   netstr, bits = net.split('/')
   netaddr = int(''.join([ '%02x' % int(x) for x in netstr.split('.') ]), 16)
   mask = (0xffffffff << (32 - int(bits))) & 0xffffffff
   return (ipaddr & mask) == (netaddr & mask)

def pageData(theUrl,lookupWhat):
	page = requests.get(theUrl)
	tree = html.fromstring(page.content)
	data = tree.cssselect(lookupWhat)
	result = []
	for d in data:
		result.append(d.text_content())
	return result

########################################################################################
def action():
	countries = _.getTable('countries_ips.json')
	if _.switches.isActive('Countries') == True:
		c = []
		for country in countries:
			if _.showLine(country['name']):
				c.append({'count': len(country['ip']), 'name': country['name']})
		if _.switches.isActive('Sort'):
			c = _.sort(c, _.switches.value('Sort'))
		if _.switches.isActive('Column'):
			_.tables.register('Auto',c)
			_.tables.print('Auto','Column')
		else:
			pass
			_.tables.register('Auto',c)
			_.tables.print('Auto','name,count')
	if _.switches.isActive('IP') == True:
		for country in countries:
			for ip in country['ip']:
				sIP = _.switches.value('IP').split('.')
				cIP = ip['network'].split('.')
				network = ip['network']
				subnet = ip['subnet']
				# print(ip['network'])
				if cIP[0] == sIP[0]:
					ip = _.switches.value('IP')
					# print(ip)
					# print(cIP)
					# print(network)
					# print((country['name']))
					cidr = netmask_to_cidr(subnet)
					net = network + '/' + str(cidr)
					# print(net)
					# print( networkMask(network,cidr))
					try:
						if addressInNetwork( ip, net ):
							print('\nlocal archive:')
							print('\t',(country['name']))
					except Exception as e:
						pass
		try:
			theUrl = 'http://whois.arin.net/rest/nets;q=' + _.switches.value('IP') + '?showDetails=true&showARIN=false'
			profile = pageData(theUrl,'orgRef')
			company = pageData(profile[0],'name')
			print('\narin:')
			print('\t',company[0])
			print('\t',company[1])
		except Exception as e:
			raise e
########################################################################################
if __name__ == '__main__':
	action()