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
from email import message
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
	pass
	#b)--> examples
	_.switches.register( 'IP', '-ip,-domain', isData='raw', description='IP Address' )
	_.switches.register( 'Connected', '-h,-here,-connected' )
	_.switches.register( 'Kill', '-k,-kill' )
	_.switches.register( 'Clean', '--c' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name,data,clean', description='Files', isRequired=False )

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
	'file': 'thisApp.py',
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
						_.hp('p thisApp -file file.txt'),
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

def _local_(do): exec(do)

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )

########################################################################################
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# globals()['var']
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

	# netstat -a -n |- 0.0.0.0:0 |-- "*:*" |- UDP |- 127.0.0. |- [::] |- State




import ipaddress
import socket


def validate_ip(ip):
	try:
		ipaddress.ip_address(str(ip).strip())
		return True
	except Exception:
		return False


def resolve_domain(domain):
	try:
		return socket.gethostbyname(domain.strip())
	except Exception:
		return domain












def get_netblock_owner__0(data):
	simplejson = __.imp('simplejson')

	try:
		json_data = simplejson.loads(data) if isinstance(data, str) else data
	except Exception as e:
		print('JSON parse error:', e)
		return None
	
	messages = json_data.get('messages', False)
	if messages and 'credits balance' in str(messages):
		# for message in messages:
		# if 'error' in message.get('type', '').lower():
		# print('API error:', messages.get('message', 'Unknown error'))
		return _.pr('Out of API credits', c='red', p=0)
	elif messages:
		return  _.pr('API error: ' + messages.get('message', 'Unknown error'), c='red', p=0)

	inetnums = json_data.get('result', {}).get('inetnums', [])

	for inetnum in inetnums:
		org = inetnum.get('org')

		if isinstance(org, dict):
			name = org.get('name')
			if name:
				return name

		asn = inetnum.get('as')
		if isinstance(asn, dict):
			name = asn.get('name')
			if name:
				return name

		netname = inetnum.get('netname')
		if netname:
			return netname

		description = inetnum.get('description')
		if isinstance(description, list) and description:
			return ' '.join(description)
		if isinstance(description, str) and description:
			return description

	return None














def get_netblock_owner(data):
	simplejson = __.imp('simplejson')

	try:
		json_data = simplejson.loads(data) if isinstance(data, str) else data
	except Exception as e:
		print('JSON parse error:', e)
		return None

	messages = json_data.get('messages', False)

	if messages:
		msg_text = str(messages).lower()

		if 'credits balance' in msg_text:
			return _.pr('Out of API credits', c='red', p=0)

		if isinstance(messages, dict):
			return _.pr('API error: ' + messages.get('message', 'Unknown error'), c='red', p=0)

		if isinstance(messages, list) and messages:
			first_msg = messages[0]
			if isinstance(first_msg, dict):
				return _.pr('API error: ' + first_msg.get('message', 'Unknown error'), c='red', p=0)

		return _.pr('API error: ' + str(messages), c='red', p=0)

	# supports:
	# {"result": {"inetnums": [...]}}
	# and also {"inetnums": [...]}
	inetnums = (
		json_data.get('result', {}).get('inetnums')
		or json_data.get('inetnums')
		or []
	)

	# print(inetnums)

	for inetnum in inetnums:

		asn = inetnum.get('as')
		# print(asn)
		if isinstance(asn, dict):
			name = asn.get('name')
			if name:
				return name

		org = inetnum.get('org')
		if isinstance(org, dict):
			name = org.get('name')
			if name:
				return name



		netname = inetnum.get('netname')
		if netname:
			return netname

		description = inetnum.get('description')
		if isinstance(description, list) and description:
			return ' '.join(description)
		if isinstance(description, str) and description:
			return description

	return None

def get_whoisxml_key(debug=False):
	try:
		keys = _v.config('WhoisXMLids')
		key = keys[_v.config('WhoisXMLid')]
		if debug:
			print(key)
		return key
	except Exception:
		pass
	
	for key in ('whoisxmlapi', 'WhoisXML', 'WhoisXMLAPI'):
		try:
			value = _v.config(key)
			if value:
				return value
		except Exception:
			pass

	_.e(
		'Missing API key',
		'https://ip-netblocks.whoisxmlapi.com/api/documentation/making-requests'
	)


def fetch_url(url):
	import requests

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
		'Accept': 'application/json',
	}

	r = requests.get(url, headers=headers, timeout=10)

	return r.text




import platform
import subprocess




def connected_ip_pid_map():
	os_name = platform.system().lower()
	ip_pids = {}

	if 'windows' in os_name:
		cmd = ['netstat', '-a', '-n', '-o']
	else:
		cmd = ['netstat', '-tunap']

	try:
		raw = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, errors='ignore')
	except Exception as e:
		_.e('netstat failed', str(e))
		return ip_pids

	for line in raw.splitlines():
		line = line.strip()

		if not line:
			continue

		# Skip headers and unwanted stuff like your pipe filters:
		if (
			'0.0.0.0:0' in line
			or '*:*' in line
			or 'UDP' in line.upper()
			or '127.0.0.' in line
			or '[::]' in line
			or line.lower().startswith('proto')
			or 'state' in line.lower()
		):
			continue

		parts = line.split()

		remote = None
		pid = None

		if 'windows' in os_name:
			# Proto Local Foreign State PID
			# TCP 192.168.1.5:55555 1.2.3.4:443 ESTABLISHED 1234
			if len(parts) < 5:
				continue

			proto = parts[0].upper()
			if proto != 'TCP':
				continue

			remote = parts[2]
			state = parts[3]
			pid = parts[4]

			if state.upper() not in ('ESTABLISHED', 'CLOSE_WAIT', 'SYN_SENT'):
				continue

		else:
			# tcp 0 0 local:port remote:port ESTABLISHED pid/program
			if len(parts) < 6:
				continue

			proto = parts[0].upper()
			if not proto.startswith('TCP'):
				continue

			remote = parts[4]
			state = parts[5]

			if state.upper() not in ('ESTABLISHED', 'CLOSE_WAIT', 'SYN_SENT'):
				continue

			if len(parts) >= 7 and '/' in parts[6]:
				pid = parts[6].split('/', 1)[0]
			else:
				pid = None

		if not remote:
			continue

		# Remove IPv6 brackets and port
		remote = remote.strip()

		if remote.startswith('['):
			ip = remote.split(']')[0].strip('[]')
		else:
			ip = remote.rsplit(':', 1)[0]

		ip = ip.strip()

		if not validate_ip(ip):
			continue

		if ip.startswith('127.') or ip in ('0.0.0.0', '::1', '::'):
			continue

		if not pid or not str(pid).isdigit():
			continue

		ip_pids.setdefault(ip, [])
		if int(pid) not in ip_pids[ip]:
			ip_pids[ip].append(int(pid))

	return ip_pids



def kill_pid(pid):
	os_name = platform.system().lower()

	try:
		if 'windows' in os_name:
			subprocess.run(
				['taskkill', '/PID', str(pid), '/F'],
				check=False,
				capture_output=True,
				text=True
			)
		else:
			subprocess.run(
				['kill', '-9', str(pid)],
				check=False,
				capture_output=True,
				text=True
			)

		return True

	except Exception as e:
		print('Kill failed:', pid, e)
		return False















################################################################################

colors = {
	'ok': 'cyan',
	'bad': 'red',
	'flag': 'darkcyan'
}

labels = [
	{ 'Search': 'Microsoft', 'Abbrev': 'Microsoft', 'Color': colors['ok'] },
	{ 'Search': 'Apple', 'Abbrev': 'Apple', 'Color': colors['ok'] },
	{ 'Search': 'GitHub', 'Abbrev': 'GitHub', 'Color': colors['ok'] },
	{ 'Search': 'Google', 'Abbrev': 'Google', 'Color': colors['ok'] },
	{ 'Search': 'Amazon', 'Abbrev': 'Amazon', 'Color': colors['ok'] },
	{ 'Search': 'Cloudflare', 'Abbrev': 'Cloudflare', 'Color': colors['ok'] },
	{ 'Search': 'Akamai Technologies', 'Abbrev': 'Akamai', 'Color': colors['ok'] },
	{ 'Search': 'Internet Assigned Numbers Authority', 'Abbrev': 'LOCAL', 'Color': colors['flag'] },
]

suffixes = ['Inc.', 'LLC', 'Ltd.', 'Corporation', 'Corp.', 'Company', 'Co.']
prefixes = ['AS', 'ASN', 'Autonomous System']

def owner_cleaner(owner):
	global labels
	global suffixes
	global prefixes

	if not owner: return _.pr('UnknownC',c='red',p=0)
	
	# Remove common suffixes and prefixes
	for suffix in suffixes:
		owner = owner.replace(suffix, '').strip().strip(',').strip()

	for prefix in prefixes:
		if owner.startswith(prefix):
			owner = owner[len(prefix):].strip().strip(',').strip()

	

	for label in labels:
		if label['Search'].lower() in owner.lower():
			owner = label['Abbrev']
			if label.get('Color', False):
				owner = _.pr(owner,c=label['Color'],p=0)
			break

	
	return owner

################################################################################











from urllib.parse import urlencode

cache = _.getTable('netblock_cache.dex') or {}




def action():
	global cache
	debug = False
	data = _.isData(2)
	


	if _.switches.isActive('Connected'):
		ip_pids = connected_ip_pid_map()

		for IP, pids in ip_pids.items():
			owner = None
			if IP in cache:
				owner = cache[IP]
				if 'Unknown' in owner: owner = None
			try:
				api_key = get_whoisxml_key(debug=debug)

				params = urlencode({
					'apiKey': api_key,
					'ip': IP,
					'outputFormat': 'JSON',
				})

				url = 'https://ip-netblocks.whoisxmlapi.com/api/v2?' + params
				
				if not owner:
					result = fetch_url(url)
					if debug:
						print('URL:', url)  # Debug: print the URL being requested
						print('Raw Result:', result)  # Debug: print the raw result from the API
					try:
						owner = get_netblock_owner(result) or 'UnknownF'
						cache[IP] = owner
						_.saveTable(cache, 'netblock_cache.dex')
					except Exception as e:
						_.pr(IP, 'Error parsing result',str(e), c='red')
						continue
				
				owner = owner_cleaner(cache[IP])

				line = 'PIDs: ' + ','.join(map(str, pids)) + ' --> ' + IP + ' --> '  + ' --> ' + ( 'Owner: ' + owner  )

				if _.showLine(owner):
					print(line)

					if _.switches.isActive('Kill'):
						for pid in pids:
							_.pr('KILL:', pid, IP, owner,c='red')
							kill_pid(pid)

			except Exception as e:
				_.e(IP, str(e))
		return


	if not data:
		_.e('Missing -ip value')

	api_key = get_whoisxml_key(debug=debug)
	IPs = data




	for IP in IPs:
		# print(IP)
		owner = None
		if IP in cache:
			owner = cache[IP]
			# print(owner)
			if 'Unknown' in owner: owner = None


		original = IP
		IP = IP.strip()

		if not validate_ip(IP):
			IP = resolve_domain(IP)

		if not validate_ip(IP):
			_.e('Invalid IP/domain', original)
		try:
			url = (
				'https://ip-netblocks.whoisxmlapi.com/api/v2'
				+ '?apiKey=' + api_key
				+ '&ip=' + IP
			)
			if not owner:
				result = fetch_url(url)
				if debug:
					print('URL:', url)  # Debug: print the URL being requested
					print('Raw Result:', result)  # Debug: print the raw result from the API
				try:
					owner = get_netblock_owner(result)
					cache[IP] = owner
					_.saveTable(cache, 'netblock_cache.dex')
				except Exception as e:
					_.pr(IP, 'Error parsing result',str(e), c='red')
					continue
			
			
			owner = owner_cleaner(cache[IP])

			if _.switches.isActive('Clean'):
				print(cache[IP])
			else:
				if original != IP:
					print(original, '-->', IP, '-->', owner)
				else:
					print(IP, '-->', owner)

			if _.showLine(owner):
				# print(line)

				if _.switches.isActive('Kill'):
					for pid in pids:
						_.pr('KILL:', pid, IP, owner,c='red')
						kill_pid(pid)

		except Exception as e:
			
			_.pr(IP, str(e))

# 69f7f8bf-22c4-83ea-b805-a800c71d8e1f

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)