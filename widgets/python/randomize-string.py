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
	_.switches.register( 'Clipboard', '-clip' )
	_.switches.register( 'Text', '-text' )
	_.switches.register( 'Case', '-case' )
	_.switches.register( 'NoAutoQuote', '-noquote' )

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

def _local_(do): exec(do)

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
		# globals()['var']
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


import random

def randomize_case(s):
	return ''.join(random.choice([str.upper, str.lower])(c) for c in s)

def randomize_string(s):
	chars = list(s)
	random.shuffle(chars)
	randomized_s = ''.join(chars)
	return randomized_s



import re
import random
import string

def randomize_text(text):
	def randomize(match):
		domains = ['domain.com', 'domain.net', 'domain.org', 'domain.quest', 'domain.xyz', 'domain.guru', 'domain.cx', 'domain.ac', 'domain.work', 'domain.app', 'domain.vip', 'example.com', 'example.net', 'example.org', 'example.quest', 'example.xyz', 'example.guru', 'example.cx', 'example.ac', 'example.work', 'example.app', 'example.vip', 'site.com', 'site.net', 'site.org', 'site.quest', 'site.xyz', 'site.guru', 'site.cx', 'site.ac', 'site.work', 'site.app', 'site.vip']

		s = match.group(0)
		if re.match(r'[\'\"]\+?\d+[\'\"]', s):
			phone_number = s.strip('\'\"')
			area_code, rest = phone_number[:4], phone_number[4:]
			randomized_rest = ''.join(random.choice(string.digits) for _ in range(len(rest)))
			return f'"{area_code}{randomized_rest}"'
		elif re.match(r'[\'\"].+?@.+?[\'\"]', s):
			local, domain = s.strip('\'\"').split('@')
			domain = random.choice(domains)
			local = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(local)))
			return f'"{local}@{domain}"'
		else:
			randomized = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(s) - 2))
			return f'{s[0]}{randomized}{s[-1]}'

	pattern = r'[\'\"].+?[\'\"]'
	result = re.sub(pattern, randomize, text)
	return result



def action():
	if _.switches.isActive('Clipboard'):
		_copy = _.regImp( __.appReg, '-copy' )
		_paste = _.regImp( __.appReg, '-paste' )
		data  = _paste.imp.paste()
	elif _.switches.isActive('Text'):
		data = ' '.join(_.switches.values('Text'))

	ran=False
	if not _.switches.isActive('NoAutoQuote'):
		if '"' in data or "'" in data:
			ran=True
			result=randomize_text(data)
	if not ran:
		if _.switches.isActive('Case'):
			result = randomize_case(data)
		else:
			result = randomize_string(data)

	if _.switches.isActive('Clipboard'):
		_copy.imp.copy( result )
	else:
		print(result)


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

