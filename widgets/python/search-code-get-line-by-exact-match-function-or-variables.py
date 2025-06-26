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
	# _.switches.register( 'Input', '-i' )
	pass
	
	
	cowsay -f dragon "Run for cover, I feel a sneeze coming on."
	
	
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])
_.appInfo[focus()] = {
	
	'file': 'thisApp.py',
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
def triggers():
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Duration', _.timeFuture )
_.l.conf('clean-pipe',True)
_.l.sw.register( triggers, sw )
	
		
		
		
		
		
	
		
	
		
		
	
		
		
def action():
	load(); global c3po;
	
	for subject in _.isData(r=0): _.pr(subject)
def load():
	global c3po
	c3po = _.getTable( 'table' )
	
	_.pt(c3po)
if __name__ == '__main__':
	action()
	__.isExit()