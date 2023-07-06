import sys
sys.path.append("D:\\.rightthumb-widgets\\widgets\\python")


import sys, time
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;

def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')

def sw():
	pass
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])

_.appInfo[focus()] = {
	'file': '_rightThumb.files',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'usage': [
	],
	'relatedapps': [
	],
	'prerequisite': [
	],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [
	],
	'notes': [
	],
}

_.appData[focus()] = {
		'start': __.startTime,
		'uuid': '',
		'audit': [],
		'pipe': False,
		'data': {
					'field': {'sent': [], 'received': [] }, 
					'table': {'sent': [], 'received': [] },
		},
	}

def triggers(): pass

# _.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

try: db
except: db=None

def load():
	global db
	if db==None: db=_.getTableDB('extensions.json')





#n)--> testing
load()

# for k in db:
#     kk=list(k.keys())[0]
#     _.pr(kk,c='yellow')
#     for rec in k[kk]:
#         for ext in rec['extension'].split(', '):
#             exto=ext
#             ext=ext.lower()
#             if not ext.startswith('.'):
#                 ext='.'+ext
#             _.pr('\t',ext,c='cyan')


for k in db:
	kk=list(k.keys())[0]
	for rec in k[kk]:
		for ext in rec['extension'].split(', '):
			exto=ext
			ext=ext.lower()
			if not ext.startswith('.'):
				ext='.'+ext
			if ext.count('.') > 1:
				_.pr(ext,c='cyan')





# a.fi


