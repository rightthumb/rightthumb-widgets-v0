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
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://efm.cx/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
__.setting('require-list',['Pipe','Files'])
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

def label(line):
	line=line.strip()
	while '  ' in line: line=line.replace('  ',' ')
	lab=''
	for c in line.split(' ')[1]:
		if c in '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': lab+=c
		else: break
	return lab

def whitespace(line):
	ws=''
	for c in line:
		if c in ' \t': ws+=c
		else: break
	return ws

def process(path):
	_.pr(path)
	_file_open.action(path)
	# sys.exit()
	file=_.getText(path,raw=True).replace('\r','')
	while '\t' in file: file=file.replace('\t','    ')
	while '    ' in file: file=file.replace('    ','\t')
	lines=file.split('\n')
	Parent={}
	counters={
				'class': 0,
				'def': 0,
				'def-def': 0,
				'class-def': 0,
				'def-all': 0,
	}
	_lines_=[]
	i=0
	active=False
	for line in lines:
		i+=1
		inject=False
		if line.strip().startswith('class ') and ':' in line:
			Parent={'class':label(line)}
			counters['class']+=1
		elif line.strip().startswith('def ') and ':' in line:
			Def=label(line)
			ws=whitespace(line)
			if not ws: Parent={'def':label(line)}
			counters['def-all']+=1

			# counters
			if ws:
				if 'def' in Parent: counters['def-def']+=1
				elif 'class' in Parent: counters['class-def']+=1
			if not ws: counters['def']+=1


			# print
			if ws:
				if 'def' in Parent: _.pr('d',Parent['def'],Def,c='cyan')
				elif 'class' in Parent: _.pr('c',Parent['class'],Def,c='darkcyan')
			if not ws: _.pr(Def,c='green')


			# inject tracer
			if ws:
				if 'def' in Parent: am=['d',Parent['def'],Def]
				elif 'class' in Parent: am=['c',Parent['class'],Def]
			if not ws: am=[Def]
			
			if not ws and Def == 'registerSwitches':
				active=True
			elif active:
				inject_0 = str(i)+',"'+' '.join(am)+'"'
				inject_1 = '\t'+ws+'_.pr('+inject_0+',c="red")'
				inject=True


		_lines_.append(line)
		if inject:
			_lines_.append(inject_1)
			i+=1

	pass
	_.saveText(_lines_,path)

			# if not ws: print(Def)
	print()
	# _.pr('Totals:',c='Background.blue')
	_.printDicFields(counters,'Totals')


def action():
	for path in _.isData(r=0):
		if path.endswith('.py'):
			process(path)
	

_file_open = _.regImp( __.appReg, 'file-open' )
_file_open.switch('Backup')

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

