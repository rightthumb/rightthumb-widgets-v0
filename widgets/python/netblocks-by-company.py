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

##################################################
import sys, time
##################################################
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################

def sw():
	_.switches.register( 'Company', '-co,-company' )
	_.switches.register( 'URL', '-url' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files' )
	_.switches.register( 'Keys', '-keys' )
	pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'netblocks-by-company.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
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
						_.hp('p netblocks-by-company -file file.txt'),
						_.linePrint(label='simple',p=0),
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

def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#n)--> start

from functools import reduce

def deep_get(dictionary, keys, default=None):
	return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)
scanner_result = []

def scanner(data,fields):
	global scanner_result
	if type(fields) == str: fields = [fields]
	if type(data) == list:
		for k in data:
			if type(k) == list: return scanner(k,fields)
			elif type(k) == dict:
				for f in fields:
					if f in list(k.keys()):
						scanner_result.append(k[f])
	return scanner_result

def ipRange2cidr(start,end):
	startip = ipaddress.IPv4Address(start)
	endip = ipaddress.IPv4Address(end)
	return [ipaddr for ipaddr in ipaddress.summarize_address_range(startip, endip)]


def get_cidr_ranges(txt):
	while '\n\n' in txt: txt = txt.replace('\n\n','\n')
	table = simplejson.loads(txt)
	# print(table)
	# data = deep_get(table,'primaryKey')
	data = scanner(table,'primaryKey')
	# print(data)
	results = []
	for d in data:
		if ':' in d:
			results.append(d)
			# print(d)
		elif '.' in d and ' - ' in d:
			IPs = d.split(' - ')
			try:
				for cidr in ipRange2cidr(IPs[0],IPs[1]):
					# print(cidr)
					results.append(str(cidr))
			except Exception as e: pass
	return results

def print_company(co,ranges):
	_.pr(co,c='green')
	for cidr in ranges:
		_.pr('\t',cidr,c='yellow')


def action():
	if _.switches.isActive('Company'):
		netco = {}
		netco = _.getTableDB('netblocks-by-company.index')
		delete = []
		for co in netco:
			if not netco[co]: delete.append(co)
			# elif '123.124.132.0/27' in netco[co]: delete.append(co)
		for co in delete:
			del netco[co]

		for co in _.switches.values('Company'):
			if co in netco:
				print_company(co,netco[co])
			else:
				txt=str(requests.get( 'https://wq.apnic.net/query?searchtext='+co).content,'iso-8859-1')
				ranges = get_cidr_ranges(txt)
				if ranges:
					netco[co] = ranges
				ranges = []
				print_company(co,ranges)
			time.sleep(2)
		_.saveTableDB(netco,'netblocks-by-company.index')
		return None
	elif _.switches.isActive('URL'):
		txt=str(requests.get( _.switches.values('URL')[0]).content,'iso-8859-1')
		# print(inpoot)
		# sys.exit()
	else:
		txt = '\n'.join( _.isData(r=0) ).replace('\r','')
	



simplejson = __.imp('simplejson')
requests = __.imp('requests')
import ipaddress
##################################################
######################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
