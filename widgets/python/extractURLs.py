import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'thisApp.py',
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
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
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import re

def extract_urls(text):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(
        r'http[s]?://'                      # Start with http:// or https://
        r'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|'  # Match domain
        r'(?:%[0-9a-fA-F][0-9a-fA-F]))+'    # Match percent-encoded characters
    )
    
    # Find all matches in the text
    urls = url_pattern.findall(text)
    
    return urls


def extract_relevant(url,string):
	if string in url:
		parts = url.split(string)
		url = parts[0]
	return url


def action():
	text = '\n'.join(_.isData(r=1))
	for url in extract_urls(text):
		url = url.replace("'",'')
		# url = url.rstrip('/')
		url = url.rstrip(',')
		url = url.rstrip(';')
		url = url.rstrip(':')
		
		url = url.replace('\\','')
		url = url.replace('"','')
		url = url.replace(')','')
		url = url.replace(']','')
		url = extract_relevant(url,'.replace(')
		url = extract_relevant(url,'.decode(')
		url = extract_relevant(url,'+urllib.')
		url = extract_relevant(url,'+tag.get')
		url = extract_relevant(url,'+_.switches.')
		url = extract_relevant(url,'+sub.')
		url = url.replace('https://','\nhttps://')
		url = url.replace('http://','\nhttp://')
		url = url.strip()
		# url = extract_relevant(url,'')
		if 'head>' in url:
			continue
		for u in url.split('\n'):
			u = u.rstrip('//www.,')
			if len(u) > len('https://'):
				if _.showLine(u):
					_.pr(u)



########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);