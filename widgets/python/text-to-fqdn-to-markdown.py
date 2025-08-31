import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	_.switches.register( 'NoCache', '-no,-nocache,-live,-lookup' )
	_.switches.register( 'NoCopy', '-nocopy' )
	_.switches.register( 'NoIP', '-noip' )
	_.switches.register( 'NoMarkdown', '-nomd' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'text-to-fqdn-to-markdown.py',
	'description': ['Server List: Text to FQDN to Markdown IP FQDN list','142.251.35.238 google.com','20.231.239.246 microsoft.com'],
	'categories': [
						'fqdn',
						'srv',
						'server list',
						'tool',
						'ip',
				],
	'examples': [
						_.hp('p text-to-fqdn-to-markdown'),
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
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start


import re
import socket


def convert_fqdn_to_markdown(text):
	spent = []
	# Regular expression to match FQDNs (e.g., subdomain.domain.tld)
	fqdn_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
	fqdns = re.findall(fqdn_pattern, text)
	
	# Dictionary to cache resolved IP addresses to avoid repeated lookups
	ip_cache = _.getTable('text-to-fqdn-to-markdown.index')
	markdown_list = []
	
	for fqdn in fqdns:
		if fqdn in spent:
			continue
		spent.append(fqdn)
		if _.switches.isActive('NoIP'): continue
		if fqdn not in ip_cache:
			try:
				# Resolve FQDN to IP address
				ip_address = socket.gethostbyname(fqdn)
				ip_cache[fqdn] = ip_address
			except socket.gaierror:
				# Skip FQDNs that cannot be resolved
				ip_cache[fqdn] = None

		# Add to Markdown list if the IP was resolved successfully
		if ip_cache[fqdn]:
			if _.switches.isActive('NoMarkdown'):
				markdown_list.append(f"{ip_cache[fqdn]} {fqdn}")
			else:
				markdown_list.append(f"- {ip_cache[fqdn]} {fqdn}")
			
	if _.switches.isActive('NoMarkdown') and _.switches.isActive('NoIP'):
		return "\n".join(spent)
	elif _.switches.isActive('NoIP'):
		for fqdn in fqdns:
			markdown_list.append(f"- {fqdn}")

	_.saveTable(ip_cache,'text-to-fqdn-to-markdown.index',p=0)
	# Join the list into a single string separated by newline characters
	return "\n".join(markdown_list)





def action():
	data = '\n'.join(_.isData(r=1))
	result = convert_fqdn_to_markdown(data)
	_copy = _.regImp( __.appReg, '-copy' )
	try:
		_copy.imp.copy( result )
	except:
		_.pr( result )


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__);