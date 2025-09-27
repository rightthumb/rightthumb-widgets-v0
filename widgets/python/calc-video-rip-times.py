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
	'file': 'calc-video-rip-times.py',
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


########################################################################################
# START

def action():
	#--> min, architecture {:strict:}
	#--> trigger/callback  <w#
	#--> todo#> meta to scan for
	load()
	global c3po



	for i, line, bi in _.numerate( c3po.split('\n') ):
		#--> _.nindex(bi,h,n)  =  line.index(n)
		#--> new print function
		_.pr(i,bi)
	_.pr('ready',c='green')

def load():
	global c3po
	c3po=c3po.replace('\r','')
	c3po=c3po.replace('\t',' ')
	c3po=_str.do('dup',c3po,' ')
	c3po=_str.do('dup',c3po,'\n')
	c3po=_str.do('be',c3po,'\n')


c3po='''
piller-10-1.mp4     1653064301.7805753     1652565643.5936503
piller-01.mp4       1653064300.689178      1652569382.1872935
piller-02.mp4       1653064300.8467927     1652571932.9867163
piller-03.mp4       1653064300.9256144     1652575912.2651699
piller-04.mp4       1653064301.1949415     1652586879.2538848
piller-05.mp4       1653064301.2538414     1652590756.1769834
piller-07-1.mp4     1653064301.4065015     1652727065.45464
piller-07-2.mp4     1653064301.4972918     1652736472.8367777
piller-09.mp4       1653064301.601054      1652739620.837456
piller-11.mp4       1653064302.203765      1652745437.6103113
notes.txt           1653064300.6881814     1652933855.7653308
piller-12-1.mp4     1653411610.9753027     1653414030.1525514
piller-12-2.mp4     1653414591.24551       1653417061.6420698
piller-13.mp4       1653418227.1785357     1653421652.5366676
piller-14-1.mp4     1653425781.924607      1653427326.8276126
piller-14-2.mp4     1653431284.4555166     1653433506.3697827
piller-15.mp4       1653434768.55589       1653438276.036759
piller-16.mp4       1653449563.5948658     1653453375.228229
piller-17.mp4       1653454166.2115273     1653458478.9009638
piller-10-2.mp4     1653459805.1250346     1653461901.7615304
'''



########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()