import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register('Domain', '-d,-domain', 'example.com')
	_.switches.register('User', '-u,-user', 'cpuser')
	_.switches.register('Home', '-h,-home', '/home/cpuser')
	_.switches.register('IP', '-ip', '1.2.3.4')
	_.switches.register('Addon', '-addon')  # Flag to indicate addon domain
	_.switches.register('Subdomain', '-sub')  # Flag to indicate subdomain
	_.switches.register('Files', '-f,-fi,-file,-files', 'domains.txt')
	_.switches.register('JSON', '-j,-json', 'config.json')
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



COMMANDS = {
	# WHMAPI1 Commands
	'create-account': {
		'api': 'whmapi1',
		'func': 'createacct',
		'required': ['user', 'domain', 'password'],
	},
	'list-accounts': {
		'api': 'whmapi1',
		'func': 'listaccts',
		'required': [],
	},
	'suspend-account': {
		'api': 'whmapi1',
		'func': 'suspendacct',
		'required': ['user'],
	},
	'unsuspend-account': {
		'api': 'whmapi1',
		'func': 'unsuspendacct',
		'required': ['user'],
	},
	'terminate-account': {
		'api': 'whmapi1',
		'func': 'removeacct',
		'required': ['user'],
	},
	'change-password': {
		'api': 'whmapi1',
		'func': 'passwd',
		'required': ['user', 'password'],
	},
	'set-reseller': {
		'api': 'whmapi1',
		'func': 'setupreseller',
		'required': ['user'],
	},
	'list-packages': {
		'api': 'whmapi1',
		'func': 'listpkgs',
		'required': [],
	},
	'create-package': {
		'api': 'whmapi1',
		'func': 'addpkg',
		'required': ['name', 'quota', 'bandwidth'],
	},
	'delete-package': {
		'api': 'whmapi1',
		'func': 'killpkg',
		'required': ['name'],
	},
	'edit-package': {
		'api': 'whmapi1',
		'func': 'editpkg',
		'required': ['name'],
	},
	'get-dns-zone': {
		'api': 'whmapi1',
		'func': 'dumpzone',
		'required': ['domain'],
	},
	'edit-dns-zone': {
		'api': 'whmapi1',
		'func': 'editzonerecord',
		'required': ['domain', 'line', 'name', 'ttl', 'class', 'type', 'record'],
	},
	'add-dns-record': {
		'api': 'whmapi1',
		'func': 'addzonerecord',
		'required': ['domain', 'name', 'type', 'record'],
	},
	'delete-dns-record': {
		'api': 'whmapi1',
		'func': 'removezonerecord',
		'required': ['domain', 'line'],
	},
	'generate-ssl': {
		'api': 'whmapi1',
		'func': 'generatessl',
		'required': ['host', 'country', 'state', 'city', 'company', 'email'],
	},

	# UAPI Commands
	'create-addon': {
		'api': 'uapi',
		'module': 'Domain',
		'func': 'addaddondomain',
		'required': ['user', 'domain'],
	},
	'create-subdomain': {
		'api': 'uapi',
		'module': 'SubDomain',
		'func': 'addsubdomain',
		'required': ['user', 'domain', 'rootdomain'],
	},
	'delete-addon': {
		'api': 'uapi',
		'module': 'Domain',
		'func': 'deladdondomain',
		'required': ['user', 'domain'],
	},
	'list-email-accounts': {
		'api': 'uapi',
		'module': 'Email',
		'func': 'list_pops',
		'required': ['user'],
	},
	'create-email': {
		'api': 'uapi',
		'module': 'Email',
		'func': 'add_pop',
		'required': ['user', 'email', 'password', 'quota'],
	},
	'delete-email': {
		'api': 'uapi',
		'module': 'Email',
		'func': 'delete_pop',
		'required': ['user', 'email'],
	},
	'create-db': {
		'api': 'uapi',
		'module': 'Mysql',
		'func': 'create_database',
		'required': ['user', 'name'],
	},
	'create-db-user': {
		'api': 'uapi',
		'module': 'Mysql',
		'func': 'create_user',
		'required': ['user', 'name', 'password'],
	},
	'set-db-privs': {
		'api': 'uapi',
		'module': 'Mysql',
		'func': 'set_privileges_on_database',
		'required': ['user', 'user_name', 'database', 'privileges'],
	},
}






import argparse, subprocess, requests, json, os # type: ignore

WHM_CONFIG = {
	'host': _v.fig['whm-https'],
	'user': 'root',
	'token': _v.fig['whm'],
}

def whm_api(api, params={}):
	headers = {
		'Authorization': f"whm {WHM_CONFIG['user']}:{WHM_CONFIG['token']}"
	}
	url = f"{WHM_CONFIG['host']}/json-api/{api}?api.version=1"
	r = requests.get(url, headers=headers, params=params, verify=False)
	return r.json()

def uapi(user, module, func, args={}):
	headers = {
		'Authorization': f"whm {WHM_CONFIG['user']}:{WHM_CONFIG['token']}"
	}
	url = f"{WHM_CONFIG['host']}/execute/{module}/{func}"
	args['user'] = user
	r = requests.get(url, headers=headers, params=args, verify=False)
	return r.json()

def create_addon_domain(user, domain, subdomain=None, home=None):
	args = {
		'newdomain': domain,
		'dir': home or f'/home/{user}/public_html/{domain}/public_html',
		'subdomain': subdomain or domain.split('.')[0]
	}
	return uapi(user, 'Domain', 'addaddondomain', args)

def action():
	_.switches.process()

	if _.switches.isActive('Files'):
		for domain in _.switches.values('Files'):
			result = create_addon_domain(
				_.switches.value('User'),
				domain
			)
			_.pv(result)

	elif _.switches.isActive('Domain'):
		result = create_addon_domain(
			_.switches.value('User'),
			_.switches.value('Domain'),
			subdomain=None,
			home=_.switches.value('Home') if _.switches.isActive('Home') else None
		)
		_.pv(result)
	else:
		print('No domain specified.')

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)