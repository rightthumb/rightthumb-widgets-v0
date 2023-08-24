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
	_.switches.register( 'Sites', '-site,-sites', 'eyeformeta.com rightthumb.com efm.cx thumb.cx etc.ac softwaredevelopment.solutions' )
	_.switches.register( 'Remove', '-r,-remove', 'relationshipideas.xyz' )
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
						# 'p another -file file.txt',
						# '',
	],
	'prerequisite': [
						# 'p another -file file.txt',
						# '',
	],
	'examples': [
						_.hp('p htaccess -sites eyeformeta.com rightthumb.com efm.cx thumb.cx etc.ac efm.cx alexandria.ninja biblicalheart.com emloisevil.com eyeformeta.com icosahedron.quest luketheawesomeone.com m-eta.app metaframe.work relationshipideas.xyz reph.vip rightthumb.com ronanwins.com stark-minecraft.com theprogramming.guru understand.quest vp-servers.com xan.guru'),
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

def action():
	global base
	sites=[]
	var={}
	vv=[]
	backup('.htaccess')
	if os.path.isfile('.htaccess'):
		ht=_.getText('.htaccess')
		for line in ht:
			line=cl(line)
			if line and line.startswith('SetEnv'): var[line]=0;vv.append(line);
	# print(vv); sys.exit();
	if os.path.isfile('.htaccess.site'): sites=_.getText('.htaccess.site',raw=True,clean=2).replace('\r','').strip().split('\n')
	for site in _.switches.values('Sites'): sites.append(site)

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



	
	# rightthumb\\.com|eyeformeta\\.com

base='''
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
'''
base=base.strip()
import os

BLOCK_ACCESS_TO_SELF_AND_CHILDRED='Deny from all'
SITE_ROOT='''
# php -- BEGIN cPanel-generated handler, do not edit
# Set the “ea-php80” package as the default “PHP” programming language.
<IfModule mime_module>
  AddHandler application/x-httpd-ea-php80 .php .php8 .phtml .js
</IfModule>
# php -- END cPanel-generated handler, do not edit
'''

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

