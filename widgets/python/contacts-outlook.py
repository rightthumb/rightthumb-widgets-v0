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
	_.switches.register( 'Save', '-save' )
	_.switches.register( 'Simple', '-simp,-simple' )
	_.switches.register( 'CrossRef', '-xref' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

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
	'file': 'contacts-csv.py',
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

def simple():
	global records
	global xref
	path=_.isData(r=1)[0]
	csv = _.csv(path)
	

	numbers = {}
	mobiles = {}
	mobiles2 = {}
	firsts = {}

	recs=[]
	for rec in csv:
		rcd={}
		rcd['name']=''
		rcd['first']=''
		rcd['last']=''
		rcd['phone']=''
		rcd['phones']=[]
		rcd['email']=''
		for k in rec:
			if 'name' in k.lower(): rcd['name'] = rec[k].strip()
			elif 'phone' in k.lower():
				rcd['phone'] = phone(rec[k].strip())
				if '\r' in rec[k]:
					for p in rec[k]:
						p=phone(p)
						if p: rcd['phones'].append(p)
			elif 'email' in k.lower(): rcd['email'] = rec[k].strip()
			elif 'address' in k.lower(): rcd['address'] = rec[k].strip()
			if ' ' in rcd['name']:
				n = rcd['name'].split(' ')
				rcd['first'] = n[0]
				rcd['last'] = n[-1]
		# _.pv(rcd); sys.exit();
		good=True
		if rcd['phone'] and rcd['phone'] in xref: good=False
		if rcd['phones']:
			for p in rcd['phones']:
				if p in xref: good=False
		if not rcd['phone']: good=False
			
		if good:
			records.append(rcd)
			del rcd['phones']
			recs.append(rcd)
			if rcd['phone'] and rcd['name']:
				mobiles2[rcd['phone']]=rcd['name']

	pass
	for rcd in records:
		if rcd['phone'] and rcd['name']:
			if rcd['first']:
				firsts[ rcd['first'].lower() ] = rcd['phone']

			numbers[rcd['name']]=rcd['phone']
			mobiles[rcd['phone']]=rcd['name']

	# _.pv(recs)
	# _.pv(records)
	# _.pv(mobiles)
	_.pr('simple',c='red')
	if _.switches.isActive('Save'):
		_.saveCSV(recs,'_import_.csv',h=1)
		_.saveYML2(mobiles,'mobile.yml')
		_.saveYML2(mobiles2,'_mobile_.yml')
		_.saveYML2(numbers,'numbers.yml')
		_.saveYML2(firsts,'firsts.yml')
		_.saveTable2(records,'contacts.json')

	return records

import re

def phone(number):
	number=str(number)
	number=number.lower()
	number=number.replace(',','x')
	number=number.replace(';','x')
	number=number.replace(' ','')
	number=number.replace('+','')
	number=number.replace('*','')
	number=number.replace('-','')
	number=number.replace('(','')
	number=number.replace(')','')
	number=number.replace('\r','')
	number=number.split('\n')[0]
	number=number.split('x')[0]
	n=re.sub('[^0-9]','', number)

	# for d in number:
	#     if d in '0123456789': n+=d
	if n.startswith('1'): n=n[1:]
	if len(n) < 10: return ''
	# if len(n) > 10: print(n,number)

	return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def fContact(rec,av,fields):
	fPhone = []
	fEmail = []
	rPhone = {}
	rEmail = {}
	ph=None
	em=None
	for k in rec:
		if 'Phone' in k:
			fPhone.append(k)
			rPhone[k]=rec[k]
		if 'Email' in k:
			fEmail.append(k)
			rEmail[k]=rec[k]
		f=rec[k].strip()
		if f: fields[k]=f
	if av['m'] in fields:
		ph=fields[av['m']]
	elif rPhone:
		for fP in fPhone:
			if fP in rPhone:
				ph=rPhone[fP]
				break

	if av['e'] in fields:
		em=fields[av['e']]
	elif rEmail:
		for fP in fEmail:
			if fP in rEmail:
				em=rEmail[fP]
				break
	
	if ph: ph = phone(ph)
	return ph,em

records = []
def process(path):
	global records
	global xref
	contacts = _.csv(path)
	abbrev = {
				'm': 'Mobile Phone',
				'f': 'First Name',
				'l': 'Last Name',
				'e': 'E-mail Address',
	}
	av=abbrev
	numbers = {}
	mobiles = {}
	firsts = {}
	for rec in contacts:
		for k in rec: rec[k]=rec[k].strip()
		fields = {}
		for k in rec:
			if 'Phone' in k:
				xref.append( phone(rec[k]) )
		ph,em = fContact(rec,av,fields)
		# _.pv(fPhone); _.pv(fields); sys.exit();
		if ph and '-' in ph:
			n=[]
			if rec[av['f']]: n.append(rec[av['f']])
			if rec[av['l']]: n.append(rec[av['l']])
			record = {
						'name': ' '.join(n),
						'first': rec[av['f']],
						'last': rec[av['l']],
						'phone': ph,
						'email': rec[av['e']],
			}
			
			records.append(record)
			if record['phone'] and record['name']:
				if record['first']:
					firsts[ record['first'].lower() ] = record['phone']

				numbers[record['name']]=record['phone']
				mobiles[record['phone']]=record['name']
			# _.pv(record)
			# sys.exit()
	pass
	# _.pv(mobiles)
	if _.switches.isActive('Save')   and   not _.switches.isActive('Simple'):
		_.saveYML2(mobiles,'mobile.yml')
		_.saveYML2(numbers,'numbers.yml')
		_.saveYML2(firsts,'firsts.yml')
		_.saveTable2(records,'contacts.json')

xref=[]
def action():
	if _.switches.isActive('Simple'):
		if _.switches.isActive('CrossRef'):
			for path in _.switches.values('CrossRef'):
				process(path)
		simple()
	else:
		for path in _.isData(r=0): process(path)


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