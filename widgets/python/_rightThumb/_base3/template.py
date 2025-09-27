
def header():
	return '''
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
# banner=_.Banner(thisApp)
# goss=banner.goss
# goss('-\t GOSSIP LABEL')
# goss('-\t\t BULLET1')
# goss('-\t\t\t SUB1')
##################################################
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
##################################################
'''
exec(header())
def triggers():
	return '''
def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
'''
def setting():
	return '''
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files','Plus'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])
'''
def appInfo(var):
	info = {
		'file': 'template.py',
		'created': '0000-00-00',
		'tested':  '0000-00-00',
		'description': 'Changes the world',
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
	pass
	if var['file'] == 'thisApp.py': var['file'] = var['liveAppName']

	for k in info:
		if not k in var: var[k] = info[k]
	return var

def appData(var):
	info = {
			'start': __.startTime,
			'uuid': '',
			'audit': [],
			'pipe': False,
			'data': {
						'field': {'sent': [], 'received': [] }, # { 'label': '', 'context': [],  }
						'table': {'sent': [], 'received': [] },
			},
		}

	for k in info:
		if not k in var: var[k] =  info[k]
	return var

def info(focus):
	if not focus in _.appData:_.appData[focus]={}
	_.appInfo[focus]=appInfo(_.appInfo[focus])

	try: _.appData
	except Exception as e: _.appData={}

	if not focus in _.appData:_.appData[focus]={}
	_.appData[focus]=appData(_.appData[focus])



