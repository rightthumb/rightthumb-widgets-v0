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
	_.switches.register( 'Sites', '-site,-sites,-d,-domain,-domains', 'eyeformeta.com rightthumb.com efm.cx thumb.cx etc.ac softwaredevelopment.solutions' )
	_.switches.register( 'Remove', '-r,-remove', 'relationshipideas.xyz' )
	_.switches.register( 'Template', '-t', 'allow deny access basic wordpress xsite api api2' )
	_.switches.register( 'Iter', '-it,-iter,-ip')
	_.switches.register( 'ListTemplates', '-lt' )
	
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
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
	'file': 'htaccess-builder.py',
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
						'p htpasswd -add -u sam',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p htaccess -sites softwaredevelopment.solutions sds.sh eyeformeta.com rightthumb.com biblicalheart.com m-eta.app efm.cx thumb.cx icosahedron.quest luketheawesomeone.com metaframe.work understand.quest vp-servers.com relationshipideas.xyz reph.vip'),
						_.hp('p htaccess -sites a.etc.ac a.sds.sh efm.cx etc.ac fo.etc.ac gatekeeper.thumb.cx git.etc.ac git.rightthumb.com js.etc.ac react.etc.ac s.etc.ac thumb.cx bible.biblicalheart.com biblicalheart.com d100.icosahedron.quest emloisevil.com icosahedron.quest luketheawesomeone.com luke.theprogramming.guru mostardently.relationshipideas.xyz relationshipideas.xyz ronanwins.com scott.theprogramming.guru xan.guru ai.sds.sh ai.softwaredevelopment.solutions apps.ai.softwaredevelopment.solutions a.sds.sh assets.softwaredevelopment.solutions billing.softwaredevelopment.solutions chrome.sds.sh chrome.softwaredevelopment.solutions config.softwaredevelopment.solutions ephemeral.softwaredevelopment.solutions heimdall.softwaredevelopment.solutions h.sds.sh orchards.softwaredevelopment.solutions sds.sh secure.softwaredevelopment.solutions s.sds.sh terminal.softwaredevelopment.solutions t.sds.sh'),
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


from urllib.parse import urlparse
import tldextract

def extract_domain(url):
	if not ':' in url: return url
	parsed_url = urlparse(url)
	return f"{parsed_url.scheme}://{parsed_url.netloc}"


def separate_domain_tld(domain):
	extracted = tldextract.extract(domain)
	domain_name = f"{extracted.subdomain}.{extracted.domain}"
	tld = extracted.suffix
	if domain_name.startswith('.'): domain_name=domain_name[1:]
	return domain_name, tld


def backup(path):
	appReg=__.appReg
	_bk = _.regImp( __.appReg, 'fileBackup' )
	_bk.switch( 'Silent' )
	_bk.switch( 'isPreOpen' )
	_bk.switch( 'Input', path )
	bkfi = _bk.action()
	__.appReg=appReg

def cl(text):
	text=text.strip()
	while '  ' in text: text.replace('  ',' ')
	return text

fqdn2ip = None

def resolveFqdn(string):
	import sys
	if not '-ip' in sys.argv and not '-ips' in sys.argv: return string
	global fqdn2ip
	if fqdn2ip is None:
		import sys, os
		sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'library', 'network')))
		from fqdn2ip import fqdn2ip # type: ignore

	try:
		return fqdn2ip(string)
	except:
		return string



def processIter(string):
	if not '-iter-' in string: return string
	if not _.switches.isActive('Iter'): return string
	lines = string.split('\n')
	new = []
	for i,line in enumerate(lines):
		if not '-iter-' in line:
			new.append(line)
			continue
		if '-iter-' in line:
			for it in _.switches.values('Iter'):
				if not it.strip(): continue
				it=resolveFqdn(it)
				# print(it,line,line.replace('-iter-', it))
				new.append( line.replace('-iter-', it) )
	return '\n'.join(new)




def action():
	global templates
	global documentation
	global alias
	if _.switches.isActive('ListTemplates'):
		for key in templates: _.pr(key)
		return None
	base=templates['base']
	sites=[]
	var={}
	vv=[]
	backup('.htaccess')
	if _.switches.isActive('Template'):
		if not len(_.switches.value('Template')): _.e('missing template','deny access basic')
		template = _.switches.values('Template')[0]
		if template in alias: template=alias[template]
		if not template in templates:  _.e('invalid template','deny access basic')
		contents = processIter(templates[template]).strip()
		_.saveText(contents,'.htaccess')
		_.pr(contents)
		if template in documentation:
			_.pr(line=1,c='yellow')
			_.pr(line=1,c='yellow')
			_.pr(documentation[template])
			_.pr(line=1,c='yellow')
			_.pr(line=1,c='yellow')
		return None
		
	if os.path.isfile('.htaccess'):
		ht=_.getText('.htaccess')
		for line in ht:
			line=cl(line)
			if line and line.startswith('SetEnv'): var[line]=0;vv.append(line);
	# print(vv); sys.exit();
	if os.path.isfile('.htaccess.site'): sites=_.getText('.htaccess.site',raw=True,clean=2).replace('\r','').strip().split('\n')
	if _.switches.isActive('Sites'):
		if not len(_.switches.values('Sites')):
			sites=_.pp()
		else:
			sites=_.switches.values('Sites')

	# for site in _.switches.values('Sites'): sites.append(site)

	remove=[]
	for site in _.switches.values('Remove'):
		site=site.lower()
		try: site=extract_domain(site)
		except: pass
		remove.append(site)

	# print(1,sites)
	items=[]
	for i,site in enumerate(sites):
		site=site.lower()
		sites[i]=sites[i].lower()
		try: sites[i]=extract_domain(site)
		except: pass
		site = sites[i]
	# print(1,sites)
	sites=list(set(sites))
	sit=[]
	for site in sites:
		if not site in remove and not ':' in site: sit.append(site)
	sites=sit
	# print(1,sites)
	for i,site in enumerate(sites):
		domain, tld = separate_domain_tld(site)
		items.append(domain+'\\'+'.'+tld)
	# print(1,sites)
	domains='|'.join(items)
	htaccess = base.replace('vVv',domains)
	_.saveText(sites,'.htaccess.site')
	if os.path.isfile('.htaccess'):
		_.saveText( _.getText('.htaccess',raw=True) ,'.htaccess-'+_.friendlyDate(_.mod('.htaccess')).split(' ')[0])
	if type(htaccess)==str: htaccess=htaccess.split('\n')

	for line in htaccess:
		line=cl(line)
		if line in var: var[line]=1
	vv.reverse()
	for v in vv:
		if not var[v]:
			htaccess.insert(0,v)

	for line in htaccess: print(line)
	_.saveText(htaccess,'.htaccess')
	backup('.htaccess')


documentation={}
documentation['get']='''
<?php
if (isset($_GET['__path'])) {
	$segments = explode('/', trim($_GET['__path'], '/'));
	$_GET['path'] = $segments;
	unset($_GET['__path']);
}

header('Content-Type: application/json');
echo json_encode($_GET, JSON_PRETTY_PRINT);

'''.strip()
	
	# rightthumb\\.com|eyeformeta\\.com
templates={}


templates['ip']='''
# Allow only specific IPs
<RequireAll>
    Require ip -iter-
</RequireAll>
'''.strip()

templates['get']='''
RewriteEngine On

# Skip real files and folders
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d

# Send everything to /path/index.php with a helper parameter
RewriteRule ^(.*)$ /index.php?__path=$1 [L,QSA]

'''.strip()
templates['public']='''
<IfModule mod_headers.c>
	Header Set Access-Control-Allow-Origin "*"
	Header Set Access-Control-Allow-Methods "GET, POST, OPTIONS"
	Header Set Access-Control-Allow-Headers "Content-Type, Authorization, X-Requested-With, XMLHttpRequest"
</IfModule>
'''
templates['xsite.']='''
# Enable CORS headers
<IfModule mod_headers.c>
	Header Set Access-Control-Allow-Origin "*"
	Header Set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"
	Header Set Access-Control-Allow-Headers "Content-Type, Authorization, X-Requested-With, XMLHttpRequest"
	Header Set Access-Control-Allow-Credentials "true"
</IfModule>

# Handle preflight requests
<IfModule mod_rewrite.c>
	RewriteEngine On
	RewriteCond %{REQUEST_METHOD} OPTIONS
	RewriteRule ^(.*)$ $1 [R=200,L]
</IfModule>

# Set CORS headers for specific files if needed (optional)
<FilesMatch "\.(js|css|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot)$">
	Header Set Access-Control-Allow-Origin "*"
</FilesMatch>
'''.strip()

templates['xsite-old']='''
# Enable Cross-Origin Resource Sharing (CORS)
<IfModule mod_headers.c>
	Header Set Access-Control-Allow-Origin "*"
	Header Set Access-Control-Allow-Methods "GET, POST, OPTIONS"
	Header Set Access-Control-Allow-Headers "*"
</IfModule>

# Ensure that preflight requests (OPTIONS) are handled correctly
RewriteEngine On
RewriteCond %{REQUEST_METHOD} OPTIONS
RewriteRule ^(.*)$ $1 [R=200,L]

# php -- BEGIN cPanel-generated handler, do not edit
# Set the “ea-php82” package as the default “PHP” programming language.
<IfModule mime_module>
  AddHandler application/x-httpd-ea-php82 .php .php8 .phtml
</IfModule>
# php -- END cPanel-generated handler, do not edit
'''.strip()

templates['xsite1']='''
<IfModule mod_headers.c>
	Header set Access-Control-Allow-Origin "*"
</IfModule>
'''.strip()

templates['xsite']='''
# Ensure mod_headers is available
<IfModule mod_headers.c>

	# Allow any origin to access resources (wildcard CORS)
	Header always set Access-Control-Allow-Origin "*"

	# Allow standard CORS methods
	Header always set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"

	# Allow common request headers
	Header always set Access-Control-Allow-Headers "Content-Type, Authorization, X-Requested-With, XMLHttpRequest"

	# Optional: Allow credentials (note: must not use '*' for origin in that case!)
	# Header always set Access-Control-Allow-Credentials "true"

	# Allow cache of CORS preflight
	Header always set Access-Control-Max-Age "1728000"

</IfModule>

# Ensure mod_rewrite is available
<IfModule mod_rewrite.c>
	RewriteEngine On

	# Handle OPTIONS preflight requests directly, without redirect
	RewriteCond %{REQUEST_METHOD} OPTIONS
	RewriteRule ^(.*)$ $1 [R=204,L]
</IfModule>

# Ensure all static assets also allow CORS (all file types)
<FilesMatch ".*\.(js|css|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot|otf|json|txt|xml|html|webp|mp3|mp4|avi|pdf)$">
	<IfModule mod_headers.c>
		Header always set Access-Control-Allow-Origin "*"
	</IfModule>
</FilesMatch>
'''.strip()
templates['wp']='''
# BEGIN WordPress
# The directives (lines) between "BEGIN WordPress" and "END WordPress" are
# dynamically generated, and should only be modified via WordPress filters.
# Any changes to the directives between these markers will be overwritten.
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>

# END WordPress

# php -- BEGIN cPanel-generated handler, do not edit
# Set the “ea-php82” package as the default “PHP” programming language.
<IfModule mime_module>
  AddHandler application/x-httpd-ea-php82 .php .php8 .phtml
</IfModule>
# php -- END cPanel-generated handler, do not edit
'''.strip()
templates['wordpress']='''

Options -Indexes
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress

'''.strip()
templates['base']='''
Header always set Access-Control-Allow-Methods "POST, GET, OPTIONS"
Header always set Access-Control-Allow-Headers "Content-Type"

Options -Indexes
<IfModule mime_module>
	AddHandler application/x-httpd-ea-php80 .php .php8 .phtml .srv.js .php.js
</IfModule>
#Rewrite everything to https
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

<IfModule mod_headers.c>
	SetEnvIf Origin "^http(s)?://(.+\\.)?(vVv)$" origin_is=$0
	Header always set Access-Control-Allow-Origin %{origin_is}e env=origin_is
</IfModule>
'''.strip()

templates['deny']='Deny from all'.strip()
templates['basic']='''

Options -Indexes
# php -- BEGIN cPanel-generated handler, do not edit
# Set the “ea-php80” package as the default “PHP” programming language.
<IfModule mime_module>
	AddHandler application/x-httpd-ea-php80 .php .php8 .phtml .js
</IfModule>
# php -- END cPanel-generated handler, do not edit
'''.strip()
templates['access']='''

Options -Indexes
<IfModule mod_headers.c>
		Header set Access-Control-Allow-Origin "*"
		Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
		Header set Access-Control-Allow-Headers "DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type"
</IfModule>
'''.strip()
templates['default']='''

Options -Indexes
<IfModule mime_module>
	AddHandler application/x-httpd-ea-php80 .php .php8 .phtml
</IfModule>
'''.strip()
templates['allow']='''
Order Allow,Deny
Allow from all
'''.strip()
templates['api2']='''
RewriteEngine On
RewriteCond %{HTTP:Authorization} .
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
'''.strip()
templates['api']='''
RewriteEngine On

# Pass the Authorization header through to PHP as an environment variable
RewriteCond %{HTTP:API} ^(.*)
RewriteRule .* - [E=SDS_API:%1]

# Pass the Ephemeral header through to PHP as an environment variable
RewriteCond %{HTTP:Ephemeral} ^(.*)
RewriteRule .* - [E=SDS_EPHEMERAL:%1]

# Pass the Ephemeral header through to PHP as an environment variable
RewriteCond %{HTTP:URL} ^(.*)
RewriteRule .* - [E=SDS_URL:%1]

<IfModule mod_headers.c>
	# CORS Headers
	Header set Access-Control-Allow-Origin "*"
	Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
	Header set Access-Control-Allow-Headers "DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type"
</IfModule>
'''.strip()

import os

alias = {
			# 'allow': 'access',
			'all': 'access',
}

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