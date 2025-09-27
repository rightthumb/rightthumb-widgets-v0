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
	_.switches.register( 'IP6', '-ip,-ip6', '2a03:2880:f141:82:face:b00c:0:25de' )
	pass
	#b)--> examples
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log')
__.setting('receipt-file')
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
__.setting('require-pipe||file',False)
__.setting('pre-error',False)
__.setting('switch-raw',[])



_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'thisApp.py',
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
#b)--> examples
#d)--> code hints to quickly get started
	#n)--> inline examples
		# any(ele in 'scott5' for ele in list('0123456789'))
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--#
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

	#n)--> webpage from url
		# for subject in _.caseUnspecific( line, needle ): line = line.replace( subject, _.colorThis( subject, 'green', p=0 ) )

	#n)--> webpage from url
		# requests=__.imp('requests.post')
		#!)--> data=str(requests.post(url,data={}).content,'iso-8859-1')

	#n)--> import and backup example
		# _bk = _.regImp( __.appReg, 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();

	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

import requests

def action():

	headers = {
					'csrftoken': '16rO9Z4cbtWQvsEWi8ILD9LCA1sIw4m+gEIszqWbCYBnJGGLPoBmO2s5VmjStlB0SmVMbnl6NzAzNXNuZ0tJeW44dWdicjQwQ2gxUEt3REhydzYxL0YxczBzND0=',
					'k': '6Lcu8d0ZAAAAAPcE9Lgl63NkYT3c1DwkG4U8qSkY',
					'Recaptcha': '6Lcu8d0ZAAAAAPcE9Lgl63NkYT3c1DwkG4U8qSkY',
					'referer': 'https://dnschecker.org/ipv6-whois-lookup.php',
					'csrftoken': '16rO9Z4cbtWQvsEWi8ILD9LCA1sIw4m+gEIszqWbCYBnJGGLPoBmO2s5VmjStlB0SmVMbnl6NzAzNXNuZ0tJeW44dWdicjQwQ2gxUEt3REhydzYxL0YxczBzND0=',
	}

	page=str(requests.post('https://dnschecker.org/ajax_files/ipv6_whois_lookup.php?upd=1582.890784287796', headers=headers, data = {'host': _.switches.values('IP6')[0] ,'gRToken':'03AIIukzgoqZdifUS9YMyt4kjy_X9B4Z7Aaa__1j0IzJ_gV2ZH2ElLz_3twAvUcxr0CY3m67-ufv5HDfWG2I592lkD_gRjKxWCU6qvweqKE0uszzxLwVbmwtjVhhzZ9tN6gujoFVNfTPF3NTzNZOG-y7mZo7HJ_J6AGCblQ9794P5JltY6wFQWaM4Et49iXC5_s1-Rgj4Ps6n27CELzQwg_Ww46LXg1M5-H6ZyU6pLXwjchIl0qZjJ79b82FYEviQicLGWIYN_UxLLx2xlWFujEvxFnHbb4NDh034pkeQyE0_XYCg20RmppicB3d6MWHIkeTuAjP995rrBhjh6mylKqwZoYS-er4m2Dbc7UgsSKh_0CJNXClL2ctEkQLtR1FhV9lNehjCzDooXfsxmLHh3fQntSuLbI2NCTlgf-4iuWQFSbcNFLtnFD4VEOfI_wlvSQUN3II3r8S78zjIypjw4zVuqmIuooYCHIkostF7aI4IObFGFKSvuhyBThzexcNet81BBjLTl-Ndx3nltWKjUpKIXzxpPyJBBhybVKvPLSjI3vZZAlgPpvjqrayu_ANbbGwUt8NbQp4TH'}).content,'iso-8859-1')

	print(page)

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################

########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()

	#e)--> examples
	action()
	_.isExit(__file__)