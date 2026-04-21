import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	_.switches.register('Domain', '-domain,-d', description='Domain name(s)')
	_.switches.register('Check', '-check', description='Check availability')
	_.switches.register('Buy', '-buy', description='Buy the domain')
	_.switches.register('Years', '-years', description='Years to register (default=1)')
	_.switches.register('Privacy', '-privacy', description='Enable WHOIS privacy')
	_.switches.register('List', '-list', description='List all domains in account')
	_.switches.register('DNS', '-dns', description='List DNS records')
	_.switches.register('Record', '-record', description='Add DNS record')
	_.switches.register('Type', '-type', description='DNS record type (A, CNAME, etc.)')
	_.switches.register('Host', '-host', description='DNS record hostname (subdomain)')
	_.switches.register('Value', '-value', description='DNS record content')
	_.switches.register('SetNS', '-setns', description='Set nameservers')
	_.switches.register('NS', '-ns', description='Comma-separated nameservers')
	_.switches.register('APIKey', '-apikey', description='Override Porkbun API key')
	_.switches.register('APISecret', '-secret', description='Override Porkbun API secret')
_._default_settings_()



_.appInfo[focus()] = {
	'file': 'porkbun.py',
	'description': 'Porkbun Domain Management App',
	'categories': [
						'domain',
						'porkbun',
						'',
				],
	'examples': [
						_.hp('p porkbun -list'),
						_.hp('p porkbun -domain test1234cool.com -check'),
						_.hp('p porkbun -domain test1234cool.com -buy -years 1 -privacy'),
						_.hp('p porkbun -domain mysite.com -dns'),
						_.hp('p porkbun -domain mysite.com -record -type A -host www -value 1.2.3.4'),
						_.hp(''),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

import sys
import requests # type: ignore



_.porkbun = {
	'api_key': _v.fig['porkbunKey'],
	'api_secret': _v.fig['porkbunSecret'],
	'url': 'https://api.porkbun.com/api/json/v3'
}



def api(endpoint, payload=None, domain=None):
	if payload is None:
		payload = {}
	payload['apikey'] = _.switches.value('APIKey') if _.switches.isActive('APIKey') else _.porkbun['api_key']
	payload['secretapikey'] = _.switches.value('APISecret') if _.switches.isActive('APISecret') else _.porkbun['api_secret']

	if domain:
		url = f"{_.porkbun['url']}/{endpoint}/{domain}"
	else:
		url = f"{_.porkbun['url']}/{endpoint}"

	print(f"[DEBUG] POST → {url}")
	r = requests.post(url, json=payload)
	try:
		return r.json()
	except:
		return {'status': 'ERROR', 'response': r.text}

def list_domains():
	result = api('domain/listAll', {})
	_.pv(result)

def check_availability(domain):
	result = api('domain/checkDomain', {}, domain)
	_.pv(result)

def buy_domain(domain, years=1, privacy=True):
	payload = {
		'domain': domain,
		'years': str(years),
		'privacy': 'true' if privacy else 'false',
		'renewAuto': 'true'
	}
	result = api('order/create', payload)
	_.pv(result)

def list_dns(domain):
	result = api('dns/retrieve', {}, domain)
	_.pv(result)

def add_dns_record(domain, type_, host, value, ttl=600):
	payload = {
		'name': host,
		'type': type_,
		'content': value,
		'ttl': str(ttl)
	}
	result = api('dns/create', payload, domain)
	_.pv(result)

def set_nameservers(domain, nameservers):
	payload = {
		'ns': [ns.strip() for ns in nameservers]
	}
	result = api('domain/updateNs', payload, domain)
	_.pv(result)

def action():
	if _.switches.isActive('List'):
		list_domains()

	if _.switches.isActive('Check') and _.switches.isActive('Domain'):
		for domain in _.switches.values('Domain'):
			check_availability(domain)

	if _.switches.isActive('Buy') and _.switches.isActive('Domain'):
		years = int(_.switches.value('Years')) if _.switches.isActive('Years') else 1
		privacy = _.switches.isActive('Privacy')
		for domain in _.switches.values('Domain'):
			buy_domain(domain, years, privacy)

	if _.switches.isActive('DNS') and _.switches.isActive('Domain'):
		for domain in _.switches.values('Domain'):
			list_dns(domain)

	if _.switches.isActive('Record') and _.switches.isActive('Domain'):
		domain = _.switches.value('Domain')
		type_ = _.switches.value('Type')
		host = _.switches.value('Host')
		value = _.switches.value('Value')
		add_dns_record(domain, type_, host, value)

	if _.switches.isActive('SetNS') and _.switches.isActive('Domain') and _.switches.isActive('NS'):
		nameservers = _.switches.values('NS')
		for domain in _.switches.values('Domain'):
			set_nameservers(domain, nameservers)


########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)