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
	_.switches.register( 'Datetime/Epoch', '-epoch,-t,-dt' )
	_.switches.register( 'Percentage', '-p,-per,-percentage' )
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
	'file': 'how-much-time-is-left.py',
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
						_.hp('p how-much-time-is-left -epoch 1656220467.8824193 -p 22'),
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



def action():
	p=int(_.switches.value('Percentage'))
	epoch=_.autoDate( ' '.join(_.switches.values('Datetime/Epoch')) )
	if not epoch: return _.e('epoch')
	dd1=_.date_diff_dic(epoch,time.time())
	diff = time.time() - epoch
	cm=_.cross_multiplication({'a':p,'b':diff,'c':100,'d':'n',})
	# cm=cm/2
	# cm=cm/2
	base=time.time()
	base=epoch
	projected=_.isDate(base+cm)
	# _.pv(projected)
	# _.pr(cm)
	# _.pr( int((cm/60)) )
	# _.pr( int((cm/60)/60) )
	# _.pr(dd1)
	# _.pr(projected['text-datetime'])
	dd2=_.date_diff_dic( base+cm )
	_.pr(_.simpleDic(dd1))
	_.pr(_. simpleDic(dd2))

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()




