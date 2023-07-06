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

#b)--> load
import sys, time
#n)--> rightThumb.com widgets
import _rightThumb._construct as __
appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;
def focus(parentApp='',childApp='',reg=True):
	global appDBA;f=__.appName(appDBA,parentApp,childApp);
	if reg:__.appReg=f;
	return f
import _rightThumb._base3 as _
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA)
_.load()
#n)--> common(loaded in other things so might as well)
_v = __.imp('_rightThumb._vars')
_str = __.imp('_rightThumb._string')
#e)--> load

def sw():
	pass
	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files' )
	#e)--> examples

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
	'file': 'find-fn-function-def.py',
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
						_.hp('p find-fn-function-def -file file.py'),
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
		# if _.switches.isActive('Test'): test(); return None;
		# result=[]; result=[ _.pr(line) for i, line, bi in _.numerate( _.isData(r=0) )]
		# bk=[];[  bk.append(rec['backup']) for rec in backupLog if path == rec['file']]; bk=bk[-1];
		# a=(1 if True else 0) <--# 
		#!)--> m=[[row[i] for row in matrix] for i in range(4)]

	#n)--> python globals
		# for k in globals(): print(k, eval(k) )

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
counter=0
os=__.imp('os.sep')

def clean(text):
	while '  ' in text: text=text.replace('  ',' ')
	while text.startswith(' '): text[1:]
	while text.endsswith(' '): text[:-1]
	return text

def inject(path,fn,spaces):
	fna=''
	for f in fn:
		if f in '0_123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
			fna+=f
		else:
			fna+=' '
	global counter
	counter+=1
	app=__.name(path)
	i=0
	space_the_final_frontier=''
	while not i == spaces:
		i+=1
		space_the_final_frontier+=' '
	space_the_final_frontier+='    '
	space_the_final_frontier+="print('"+app+"',"+str(counter)+")"
	return space_the_final_frontier

def process(path):

	_bk.switch( 'Input', path ); bkfi = _bk.action();
	_.pr(bkfi,c='darkcyan')
	file=_.getText(path,raw=True).split('\n')
	while '\t' in file: file=file.replace('\t','    ')
	lines=[]
	for i, line in enumerate(file):
		hasComment=False
		if '#' in line:
			hasComment=True
			original=line

			com=line.split('#')
			line=com[0]
			if not line: lines.append(original); continue;
			comment=line[len(line):len(original)]
		lines.append(file[i])
		if ' def ' in ' '+liner:
			spaces=0
			test=file[i]
			while test.startswith(' '):
				spaces+=1
				test=test[1:]
			lines.append(inject(path,file[i]spaces))


	_.saveText(lines,path)


def action():
	# load(); global c3po;

	#--> iterate
	for path in _.isData(r=0):
		process(path)
		

# def load():
#     global c3po
#     c3po = _.getTable( 'table' )
#     #--> print table
#     _.pt(c3po)

_bk = _.regImp( focus(), 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', focus() ); _bk.switch( 'DoNotSchedule' )

########################################################################################
if __name__ == '__main__':
	action()
	__.isExit()






