import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
	_.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='name' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt',  description='Files', isRequired=False )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'harTool.py',
	'description': 'List urls or specify a url and view the cached data',
	'categories': [
						'har',
						'web',
						'browser',
						'research',
				],
	'examples': [
						_.hp('p harTool '),
						_.hp('p harTool -url https://etc.ac/'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start


import json

def load_har_file(file_path):
	with open(file_path, 'r') as f:
		return json.load(f)

def extract_urls(har_data):
	urls = []
	for entry in har_data['log']['entries']:
		urls.append(entry['request']['url'])
	return urls

def get_cache_by_url(har_data, search_url):
	for entry in har_data['log']['entries']:
		request_url = entry['request']['url']
		if request_url == search_url:
			if 'response' in entry and 'content' in entry['response']:
				return entry['response']['content']['text'].replace('\r','').replace(chr(10), '\n').replace(chr(27), '')
			else:
				return "No cached data found for this URL."
	return "URL not found in HAR file."

def main(har_file, search_url=None):
	har_data = load_har_file(har_file)
	if search_url:
		cached_data = get_cache_by_url(har_data, search_url)
		# _.pr(f"Cached data for {search_url}:")
		_.pr(cached_data)
	else:
		urls = extract_urls(har_data)
		# print("List of URLs in the HAR file:")
		for url in urls:
			if _.showLine(url):
				_.pr(url)


def run(file,url=None,urls=[]):
	# print(file,url); return file
	har_file_path = file
	search_url = None
	if url:
		search_url = url
	if url and len(urls) > 1:
		_.pr(line=1,c='yellow')
		_.pr(url,c='cyan')
		_.pr()
	main(har_file_path, search_url)

def action():
	if not _.switches.isActive('Files'):
		_.e('No files specified')
	else:
		file = _.switches.values('Files')[0]
	urls = _.isData()
	# print(urls); return urls
	if not urls:
		run(file)
	else:
		for url in urls:
			run(file,url.strip(),urls)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);