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

import subprocess

#b)--> load
from _rightThumb._base3 import template; exec(  template.header()  ); exec(  template.setting()  );
#e)--> load
def sw():
	pass
	#b)--> examples
	_.switches.register( 'Do-Not-Open', '-noopen' )
	_.switches.register( 'Default-Print-Command', '-d,-default' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.py', isData='name', description='Files' )
	#e)--> examples
__.setting('require-list',['Pipe','Files'])
_.appInfo[focus()] = {
	'file': 'find-print.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p find-print -file file.py'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'created': None,
	'tested': 1658814211.728284,
}

#b)--> registration
template.info(focus()); exec(  template.triggers()  ); _.l.sw.register( triggers, sw ); _.l.conf('clean-pipe',False);
#e)--> registration

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
		# _bk = _.regImp( focus(), 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', 'APP' ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start

if _.switches.isActive('Default-Print-Command'): print_command = 'print('
else: print_command = 'print('

counter=40000
def inject(line):
	if line.strip().startswith('#'): return line
	global print_command
	if not print_command in line: return line
	for TEST in '.,_'.split(','):
		if TEST+print_command in line: return line
	global counter
	counter+=1
	line=line.replace(print_command,print_command+str(counter)+',')
	# pr(line)
	return line
spent=[]
def process(path):
	global spent
	if path in spent: return None
	spent.append(path)
	if not _.switches.isActive('Do-Not-Open'): subprocess.Popen([ _v.fig['code_editor'], __.path(path)])
	_bk.switch( 'Input', path ); bkfi = _bk.action();
	_.pr(bkfi,c='darkcyan')
	_.pr(path)
	file=_.getText(path,raw=True).split('\n')
	for i, line in enumerate(file):

		file[i]=inject(line)
	_.saveText(file,path)


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





