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
	#b)--> examples
	_.switches.register( 'URL', '-url' )
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
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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


# def action(): initial_url = _.switches.values('URL')[0]




import requests
import hashlib
import os
import json
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

# Function to calculate the MD5 hash of a URL
def calculate_md5(url):
	return hashlib.md5(url.encode()).hexdigest()

# Function to save the collected URLs to a JSON file with a hash index
def save_to_json(data, filename):
	with open(filename, 'w') as json_file:
		json.dump(data, json_file, indent=4)

# Function to load the collected URLs from the JSON file with the hash index
def load_from_json(filename):
	if os.path.exists(filename):
		with open(filename) as json_file:
			return json.load(json_file)
	return {}

# Function to extract all URLs from a given webpage
def extract_urls(url):
	try:
		response = requests.get(url, timeout=10)
		response.raise_for_status()
		soup = BeautifulSoup(response.content, 'html.parser')
		urls = set()
		for link in soup.find_all('a', href=True):
			href = link.get('href')
			# Filter out non-http(s) links and avoid navigating outside the initial domain
			if href and href.startswith(('http://', 'https://')) and urlparse(href).netloc == urlparse(url).netloc:
				urls.add(href)
		return urls
	except requests.RequestException:
		return set()

# Function to collect all URLs from a list of pages
def collect_urls_from_pages(pages):
	all_urls = set()
	visited_urls = set()  # To keep track of visited URLs
	with ThreadPoolExecutor(max_workers=15) as executor:
		# Start fetching URLs concurrently
		future_to_url = {executor.submit(extract_urls, page): page for page in pages}
		for future in concurrent.futures.as_completed(future_to_url):
			page = future_to_url[future]
			try:
				urls = future.result()
				print(f"Collected {len(urls)} URLs from {page}")
				all_urls.update(urls)
			except Exception as e:
				print(f"Failed to collect URLs from {page}: {e}")

			# Add the visited URL to the set
			visited_urls.add(page)

	# Filter out the URLs that have already been visited
	all_urls = all_urls - visited_urls
	return all_urls

def action():
	initial_url = _.switches.values('URL')[0]
	maxThreads = 15
	cache_filename = "url_cache.json"

	# Load the previously collected URLs from the JSON file
	url_cache = load_from_json(cache_filename)

	# Calculate the MD5 hash of the initial URL
	initial_url_hash = calculate_md5(initial_url)

	# Check if the initial URL is already in the cache
	if initial_url_hash in url_cache:
		print("URLs are already cached. Loading from cache...")
		initial_urls = url_cache[initial_url_hash]
	else:
		# Collect initial URLs from the starting page
		initial_urls = extract_urls(initial_url)
		# Save the initial URLs to the cache
		url_cache[initial_url_hash] = initial_urls
		save_to_json(url_cache, cache_filename)

	# Follow URLs from the starting page and collect more URLs
	all_collected_urls = collect_urls_from_pages(initial_urls)

	# Save all the collected URLs to the cache
	url_cache[initial_url_hash] = all_collected_urls
	save_to_json(url_cache, cache_filename)

	# Print all the collected URLs
	print(f"\nCollected {len(all_collected_urls)} URLs in total:")
	for url in all_collected_urls:
		print(url)










##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action()
	_.isExit(__file__)

