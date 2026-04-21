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
	_.switches.register( 'Encrypt', '-en' )

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
	'file': 'foobar.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'fake word generator',
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


def encrypt(text,r=False):
	random=_.imp('random.randrange')
	n=''
	for c in text:
		n+=str(ord(c))
	# _.pr(n)
	def seek(): return random.randrange(5, 12);
	k=seek()
	w=''
	for i,c in enumerate(n):
		if i == k:
			k=i+seek()
			w+=' '
		w+=c
	# _.pr(w)
	def _en(w5):
		z=''
		for part in w5.split(' '):
			z+=_nID.mini.gen(int(part))
			z+=' '
		return z
	a=_en(w)
	w2a=list(w)
	w2a.reverse()
	b=_en(''.join(w2a))
	return a, b    

	_.pr(z)



def action():
	text='test'
	if _.switches.isActive('Encrypt'):
		text=' '.join(_.switches.values('Encrypt'))

	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	[ _.pr('\n',w3) for w3 in encrypt(text) ]
	


def load():
	if _.switches.isActive('Password'):
		_nID.mini.password( _.switches.values('Password')[0] )
	else:
		# _nID.mini.password( _keychain.imp.key('nID') )
		_nID.mini.password( _.appID_nID_password() )
	

import _rightThumb._nID as _nID
_keychain = _.regImp( __.appReg, 'keychain' )

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()