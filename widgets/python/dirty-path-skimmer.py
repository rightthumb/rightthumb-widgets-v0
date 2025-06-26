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
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files' )
	pass
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
	'file': 'dirty-path-skimmer.py',
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
						_.hp('p dirty-path-skimmer -file file.txt'),
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
#n)--> start

def clean(text):
	while '  ' in text: text=text.replace('  ',' ')
	while text.startswith(' '): text[1:]
	while text.endswith(' '): text[:-1]
	return text


def skim(data):
	# for file in data.split('\n'):
	# print(0)
	file=data
	file = file.replace( '"', ' ' )
	file = file.replace( "'", ' ' )
	file=clean(file)
	# print(file)
	_file=''
	testing = '0 12 +-_./\\:3456789abcdefghijklmnop%$qrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'+'''!#$%&'()+,-./:;=?@[\\]^_`{}~ ®··èéìò'''
	for ch in file:
		if ch in testing:
			_file+=ch
		else:
			_file+='|'
	# print(_file)
	for scrap in _file.split('|'):
		scrap=scrap.strip()
		# print(1)
		good=True
		while '  ' in scrap: scrap=scrap.replace('  ',' ')
		if " " in scrap and (not "'" in scrap and not '"' in scrap ):
			for tmp in scrap.split(' '):
				if good and( '\\'  in tmp or '/' in tmp ):
					# print(tmp)
					scrap=tmp
		not_included = [
							'set /p ',
							'^',
							'if not exist',
							'if exist',
		]
		for xXx in not_included:
			if xXx in scrap.lower(): good=False
		if '=' in scrap.lower():

			while '= ' in scrap: scrap=scrap.replace('= ','=')
			while ' =' in scrap: scrap=scrap.replace(' =','=')
			scrap = scrap.split('=')[1]
		scrap=scrap.strip()
		if len(scrap) < 4: good=False
		if good and( '\\'  in scrap or '/' in scrap ): _.pr(scrap)
		# elif scrap: _.pr(scrap)




def action():
	global c3po
	c3po=[]
	_.isData(r=0)
	if type(_.isData()) == list: data = '\n'.join(_.isData())
	else: data = _.isData()

	# if type(data) == list: data = '\n'.join(data)
	skim( data )
	sys.exit()


########################################################################################
if __name__ == '__main__':
	action()
	_.isExit(__file__)
