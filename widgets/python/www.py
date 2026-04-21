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
	pass
	# _.switches.register( 'Text', '-t,-text,-txt' )
	_.switches.register( 'Source', '-s,-source' )
	_.switches.register( 'URL', '-url', 'https://www.google.com/', isRequired=True )
	_.switches.register( 'Cookies', '-cookie,-cookies', 'name::scott' )
	_.switches.register( 'JSON', '-json,-JSON' )
	_.switches.register( 'People', '-people' )
	_.switches.register( 'Record-IDs', '-r,-recs,-records' )
	_.switches.register( 'Headers-Impersonate', '-h,-head,-headers,-i,-imp,-impersonate', 'win' )
	_.switches.register( 'Dump-Headers', '-h,-head,-header,-headers' )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'www.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'download url src or page text',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'www',
						'url',
						'source',
						'web copy',
				],
	'usage': [
						# 'epy another',
						# 'e nmap',
						# '',
	],
	'relatedapps': [
						'p cat -f %tmpf0% + 40 - http 165 urls single total starting',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p www -url https://www.eyeformeta.com/'),
						_.hp('p www -url https://eyeformeta.com/apps/terminal/cookie.php -cookies name::scott status::epic'),
						_.hp('p www -json -url "https://gis.hcpafl.org/CommonServices/property/search/AdvancedSearch?zip=33606&pagesize=40&page={}" -people -recs 1-1000 > %tmpf0%'),
						_.hp('p www -json -url "https://gis.hcpafl.org/CommonServices/property/search/AdvancedSearch?zip=33548&pagesize=40&page={}" -people -recs 1-1000 > %tmpf0%'),
						_.hp('p www -url https://eyeformeta.com/apps/misc/agent.php -h win'),
						_.hp('p www -url https://eyeformeta.com/apps/misc/agent.php -impersonate windows'),
						_.hp('p www -url https://eyeformeta.com/apps/misc/server.php -json'),
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


########################################################################################
# START

def url_port(url):
	url=url.replace(' ','')
	if not url.endswith('/'):
		url=url+'/'
	try:
		domain=url.split('//')[1].split('/')[0]
		if ':' in domain:
			return int(domain.split(':')[1])
	except Exception as e:
		return 80
	return 80
def _cleaner_(data):
	for encodeing in 'ISO-8859-1 UTF-8 Windows-1251 Windows-1252 GB2312 Shift GBK EUC-KR ISO-8859-9 Windows-1254 EUC-JP Big5'.lower().split(' '):
		try: return _str.do('.sh',str(data,encodeing))
		except Exception as e:
			try:
				return _str.do('.sh',str(data))
			except Exception as e:
				return str(data)

def json_code(data):
	simplejson=__.imp('simplejson')
	return simplejson.loads(_cleaner_(data))
url_count=0
def get_url(url,cookies):
	global url_count
	url_count+=1
	# _.pr(url,c='yellow')
	time.sleep(.2)
	headers=None
	if _.switches.isActive('Headers-Impersonate'):
		if 'win' in _.switches.value('Headers-Impersonate'):
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
							"KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}
	if headers is None:
		headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
						"KHTML, like Gecko) Version/4.0 Safari/534.30"}
	response=requests.get(url, headers=headers,cookies=cookies)
	if _.switches.isActive('Dump-Headers'):
		_.pr(dict(response.headers), pvs=1)
		sys.exit()
	return response.content

url_id_at=None

def url_next(url,_range):
	global url_id_at
	global url_count
	_.linePrint(c='green')
	_.linePrint(c='green')
	_.pr(time.time())
	_.pr('urls:',url_count)

	if url_id_at is None:
		url_id_at=_range['s']
		_.pr('starting:',url_id_at)
	else:
		url_id_at+=1
	if _.switches.isActive('Record-IDs') and _.switches.value('Record-IDs'):
		if url_id_at >= _range['e']:
			_.pr('hit threshold:',url_id_at,c='red')
			sys.exit()
	newURL=url.replace('{}',str(url_id_at))

	_.pr(newURL,c='purple')
	_.linePrint(c='green')
	return newURL


def action():
	url=_.switches.value('URL')
	port=url_port(url)
	# html = urlopen(url).read()
	cookies={
		# 'c3po': 'r2d2'
	}
	if _.switches.isActive('Cookies'):
		# _.pr('cookie')
		for cookie in _.switches.values('Cookies'):
			if '::' in cookie:
				name  = cookie.split('::')[0]
				value = cookie.split('::')[1]
				cookies[name]=value
	if _.switches.isActive('Record-IDs'):
		if _.switches.value('Record-IDs') and '-' in _.switches.value('Record-IDs'):
			v=_.switches.value('Record-IDs')
			_range={
					's': int( v.split('-')[0] ),
					'e': int( v.split('-')[1] ),
			}
		
		while True:
			primary_url(url_next(url,_range),cookies)
	else:
		primary_url(url,cookies)
def primary_url(url,cookies):

	# if not _.switches.isActive('Text'):
	if 0 and _.switches.isActive('Source'):
		page=__.url( url, text=_.switches.isActive('Text') )
		_.pr(page)
		return None



	webpage = get_url(url,cookies)
	# print(11)
	if _.switches.isActive('JSON'):
		# print(22)
		code=json_code(webpage)
		if not _.switches.isActive('People'):
			_.pr(code,pvs=1)
			return code
		_.pr('page:',len(code),c='darkcyan')
		ii=0
		single=0
		total=0
		for rec_prop in code:
			ii+=1
			# if ii > 2: break
			if 'owner' in rec_prop:
				while '; ' in rec_prop['owner']:
					rec_prop['owner']=rec_prop['owner'].replace('; ',';')
				while ' ;' in rec_prop['owner']:
					rec_prop['owner']=rec_prop['owner'].replace(' ;',';')
				pass
				for owner in rec_prop['owner'].split(';'):
					url2='https://gis.hcpafl.org/CommonServices/property/search/AdvancedSearch?owner=NAME&pagesize=1&page=1'
					if owner:
						url2=url2.replace( 'NAME', owner.replace(' ','+') ).replace("'",'')
						webpage = get_url(url2,cookies)
						recs_people=json_code(webpage)
						total+=1
						# _.pr(recs_people,pvs=1)
						if len(recs_people) == 1:
							single+=1
						elif len(recs_people) > 1:
							_.linePrint(c='green')
							_.pr(url,c='green')
							_.pr(url2,c='yellow')
							_.pr('valid:',len(recs_people),c='cyan')
							_.linePrint(c='green')
						# _.pr(recs_people,pvs=1)

		if single == total:
			_.pr('  single prop:',single,c='darkcyan')
		else:
			_.pr('  single prop:',single,c='darkcyan')
			_.pr(' total people:',total,c='darkcyan')
					
	if _.switches.isActive('JSON'):
		return None
	# print(webpage)
	soup = BeautifulSoup(webpage,features="lxml")

	for script in soup(["script", "style"]):
		script.decompose()
	# delete out tags


	strips = list(soup.stripped_strings)
	_.linePrint()
	_.pr( '\n'.join(strips) )
	# _.pr(strips[:5])

# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

# import urlopen
from bs4 import BeautifulSoup
requests=__.imp('requests.get')

# started page 9
# p www -json -url "https://gis.hcpafl.org/CommonServices/property/search/AdvancedSearch?zip=33606&pagesize=40&page={}" -people -recs 11-1000 >> %tmpf0%

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




