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
	#b)--> examples
	_.switches.register( 'Field', '-field', 'address' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )
	_.switches.register( 'Save', '-save', 'save.csv' )

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

states = {
	'alabama': 'al',
	'alaska': 'ak',
	'arizona': 'az',
	'arkansas': 'ar',
	'california': 'ca',
	'colorado': 'co',
	'connecticut': 'ct',
	'delaware': 'de',
	'florida': 'fl',
	'georgia': 'ga',
	'hawaii': 'hi',
	'idaho': 'id',
	'illinois': 'il',
	'indiana': 'in',
	'iowa': 'ia',
	'kansas': 'ks',
	'kentucky': 'ky',
	'louisiana': 'la',
	'maine': 'me',
	'maryland': 'md',
	'massachusetts': 'ma',
	'michigan': 'mi',
	'minnesota': 'mn',
	'mississippi': 'ms',
	'missouri': 'mo',
	'montana': 'mt',
	'nebraska': 'ne',
	'nevada': 'nv',
	'new hampshire': 'nh',
	'new jersey': 'nj',
	'new mexico': 'nm',
	'new york': 'ny',
	'north carolina': 'nc',
	'north dakota': 'nd',
	'ohio': 'oh',
	'oklahoma': 'ok',
	'oregon': 'or',
	'pennsylvania': 'pa',
	'rhode island': 'ri',
	'south carolina': 'sc',
	'south dakota': 'sd',
	'tennessee': 'tn',
	'texas': 'tx',
	'utah': 'ut',
	'vermont': 'vt',
	'virginia': 'va',
	'washington': 'wa',
	'west virginia': 'wv',
	'wisconsin': 'wi',
	'wyoming': 'wy',
}


def split_address(address):
	try:
		return split_address2(address)
	except:
		return {
			'street': '',
			'city': '',
			'state': '',
			'zip': ''
		}
def split_address2(address):
	global states
	address_parts = address.split(',')
	if len(address_parts) != 3:
		raise ValueError("Invalid address format")
	
	street = address_parts[0].strip()
	city = address_parts[1].strip()
	state_zip = address_parts[2].strip().split(' ')

	if len(state_zip) != 2:
		raise ValueError("Invalid state and zip code format")
	
	state = state_zip[0].lower()
	zip_code = state_zip[1]

	if state in states:
		state_abbr = states[state]
	else:
		state_abbr=state

	return {
		'street': street,
		'city': city,
		'state': state_abbr,
		'zip': zip_code
	}





def action():
	fi = _.isData(r=1)[0]
	if _.getTextFirst(fi) == '[': records = _.getTable2(fi)
	else: records = _.csv(fi)
	if _.switches.isActive('Field'):
		field=_.switches.value('Field')
	else:
		field='address'
	for i,rec in enumerate(records):
		a=split_address(rec[field])
		for k in a: records[i][k] = a[k]


	_.saveCSV(records,_.switches.value('Save'))


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

