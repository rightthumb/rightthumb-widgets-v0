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
	_.switches.register( 'File', '-f,-file' )
	_.switches.register( 'Subject', '-s,-subject' )
	_.switches.register( 'Log', '-log' )
	_.switches.register( 'Python', '-py' )
	# _.switches.register( 'Execute', '-exec' )
	_.switches.register( 'Me', '-me' )
	_.switches.register( 'Clear', '--c,-clear' )



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
	'file': 'tf.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'simple send and receive files',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'share',
						'file',
						'transfer',
						'upload',
						'download',
						'online',
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
						_.linePrint(label='simple',p=0),
						_.hp('p -paste | p tf -f py -log'),
						'''___
				python -m SimpleHTTPServer''',
						_.linePrint(label='simple',p=0),
						_.linePrint(label='simple',p=0),
						_.hp('p -paste | p tf -f import-fix -log'),
						'''___
				def _read_file(path): # 173 stickytape.__init__
					return open(path,encoding="utf-8").read()''',
						_.linePrint(label='simple',p=0),
						'''cat xfce4_de.sh | p tf
				curl https://tf.sds.sh/?py=tf.py --output tf.py ; chmod +x tf.py
				python3 tf.py  | bash''',
						_.linePrint(label='simple',p=0),
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

_.l.conf('clean-pipe',False)
_.l.sw.register( triggers, sw )

########################################################################################
# START

import requests

def action():
	subject = '0'
	url = _v.fig['tf-url']
	token = 'eol'
	data = ''
	pre = ''

	if _.switches.isActive('Clear'):
		response = requests.post(url, data={'token': token, 'subject': pre + subject, 'data': ''})
		data = response.content.decode(response.encoding or 'utf-8')
		return None
	if _.switches.isActive('Log'):
		pre = 'log-'
	
	if _.switches.isActive('Me') and _.switches.value('Me'):
		pre = 'me-' + _.isDate(time.time(), f='stript') + '-'
		subject = _v.user + '-AT-' + _v.computername + '-' + _.switches.value('Me')
	
	if _.switches.isActive('Python') and _.switches.value('Python'):
		pre = ''
		subject = _.switches.value('Python')
		response = requests.post(url+'?py=' + subject)
		data = response.content.decode(response.encoding or 'utf-8')
		_.pr(data)
		return data
	
	if _.switches.isActive('Subject') and _.switches.value('Subject'):
		subject = _.switches.value('Subject')
		response = requests.post(url, data={'token': token, 'subject': pre + subject})
		data = response.content.decode(response.encoding or 'utf-8')
		_.pr(data)
		return data

	if _.switches.isActive('File') and _.switches.value('File'):
		subject = _.switches.value('File')
	# print(_.isData()); sys.exit();
	if _.isData():
		response = requests.post(url, data={'token': token, 'subject': pre + subject, 'data': '\n'.join(_.isData())})
		data = response.content.decode(response.encoding or 'utf-8')
	else:
		response = requests.post(url, data={'token': token, 'subject': pre + subject})
		data = response.content.decode(response.encoding or 'utf-8')

	data = data.replace(chr(10), '\n')
	data = data.replace(chr(27), '')
	data = data.replace('\r', '')
	data = _str.do('sh', data)
	
	while '\t' in data:
		data = data.replace('\t', '    ')
	
	_.pr(data)


requests=__.imp('requests.post')
########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




