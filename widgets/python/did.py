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
	_.switches.register( 'Listen', '-l,-listen,-wait' )
	_.switches.register( 'Done', '-d,-done' )
	_.switches.register( 'Wait', '-w,-wait,-t', '15' )
	_.switches.register( 'Just-Beep', '-beep' )


# __.setting('require-list',['Files,Plus','File,Has']) # todo
__.setting('require-list',['Listen','Done'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'did.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'beep when whatever is done on whater device',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'notification',
						'beep',
						'task',
						'complete',
						'wait',
						'listen',
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
						_.hp('p did -listen install5'),
						_.hp('yes | sudo ./s.sh && p did -done install5'),
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


########################################################################################
# START
try: import _rightThumb._beep as _beep
except Exception as e: pass

def load():
	global v1
	global srv
	global sub
	global wait
	srv='https://eyeformeta.com/apps/terminal/status/'
	if _.switches.isActive('Listen'): sub = '_'.join(_.switches.values('Listen'))
	if _.switches.isActive('Done'): sub = '_'.join(_.switches.values('Done'))
	v0='?n='+sub+'&v=0'
	v1='?n='+sub+'&v=1'
	if _.switches.isActive('Listen'): __.url(srv+v0)
	wait=15
	if _.switches.isActive('Wait'): wait = int(_.switches.value('Wait'))



def action():

	if _.switches.isActive('Just-Beep'):
		_beep.mission_impossible()
		return None

	global v1
	global srv
	global sub
	global wait
	load()



	if _.switches.isActive('Done'):
		__.url(srv+v1)
		return None

	if _.switches.isActive('Listen'):
		status='0'
		while status=='0':
			_.waiting(wait)
			status=__.url(srv+sub)
		_beep.mission_impossible()
		return None



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




