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
	_.switches.register( 'IP', '-ip' )
	pass
	### EXAMPLE: START
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	# _.switches.register( 'Files', '-f,-fi,-file,-files' )
	### EXAMPLE: END

# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('require-list',[])
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

_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )


########################################################################################
# START

def cl(string):
	string = str(string).replace('\n',' ')
	string = string.replace('\r',' ')
	string = _str.do('be',string,' ')
	string = _str.do('.sh',string)
	return string
ff=0

def key(search):
	global result
	if not search in research: return search;
	i=2
	while search+'-'+str(i) in result:
		i+=1
	return search+'-'+str(i)

def find(search,attrib=None):
	global tree
	global result
	tables = tree.cssselect(search)
	for table in tables:
		try:
			item = cl(table.text_content())
			if not attrib is None:
				attr=cl(str(table.attrib[attrib]))
				if len(attr): result[key(search+'-'+attrib)]=item;
			else:
				if len(item): result[key(search)]=item;
		except Exception as e:
			pass

def action():
	global result
	global tree
	if _.switches.isActive('IP'):
		# url='http://whois.arin.net/rest/nets;q=SEARCH?showDetails=true&showARIN=true'.replace('SEARCH',_.switches.value('IP'))
		url='https://eyeformeta.com/apps/networking/netblock.php?ip=SEARCH'.replace('SEARCH',_.switches.value('IP'))
		# print(url)
		# data=str(requests.post(url,data={}).content,'iso-8859-1'); print(data);
		page=requests.post(url,data={})
		tree = html.fromstring(page.content)
		for tree.cssselect(search)
		find('startAddress')
		find('endAddress')
		find('cidrLength')
		find('name')
		find('orgRef','name')
		_.pv(result)

result={}
requests=__.imp('requests.post')
from lxml import html


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()