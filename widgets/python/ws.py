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
	_.switches.register( 'Text', '-t,-text' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files' )

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
	'file': 'ws.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'returns word dic of word stems',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'meta',
						'listener',
						'meta listener',
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
						_.hp('p ws -t scientific information systematic process testing '),
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


processWordStem = None
def wordStem(word):
	global processWordStem
	if processWordStem is None:
		from nltk.stem import PorterStemmer
		processWordStem = PorterStemmer()
	return processWordStem.stem(word)


added=False
def stim(word):
	global c3po
	global added
	if word in c3po: return c3po[word];
	c3po[word]=wordStem(word)
	added=True
	return c3po[word]

def clean_D():
	global added
	global c3po
	c3={}
	for k in c3po:
		if not k==c3po[k]:
			c3[k]=c3po[k]
		else:
			added=True
	c3po=c3
def action():
	load()
	global c3po
	global added
	if _.switches.isActive('Text'):
		data = ' '.join(_.switches.values('Text'))
	elif _.isData():
		data = ' '.join(_.isData())
	data=_str.do('.sh',data)
	data = data.replace('\n',' ')
	data=_str.do('dup',data,' ')
	data=_str.do('be',data,' ')

	# clean_D()

	for word in data.split(' '): stim(word);
	if added: _.saveTableDB(c3po,'app-word-stems.index');

	_.pr( simplejson.dumps(c3po, indent=4, sort_keys=False) )

simplejson = __.imp('simplejson')


def load():
	global c3po
	c3po = _.getTableDB( 'app-word-stems.index' )


########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




