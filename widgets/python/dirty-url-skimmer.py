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
from _rightThumb._base3 import template; exec(  template.header()  ); exec(  template.setting()  );
#e)--> load

def sw():
	pass
	#b)--> examples
	_.switches.register( 'Domains', '-dom,-domain,-domains', 'min or minimal' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	#e)--> examples

_.appInfo[focus()] = {
	'file': 'dirty-url-skimmer.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p thisApp -file file.txt'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'created': None,
	'tested': 1658926278.0647678,
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


def skim0(data):
	test=''
	for ch in data:
		if ch in '@0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU-_VWX.YZ:/':
			test+=ch
		else:
			test+=' '
	while '  ' in test: test=test.replace('  ',' ')

	for crap in test.split(' '):
		if 'http:' in crap or 'https:' in crap:
			print(crap)

def skim(data):
	global extractor
	focus()
	urls = extractor.find_urls(data)
	for url in urls:
		if _.switches.isActive('Domains'):
			url = urlparse(url).netloc
			if 'min' in _.switches.value('Domains'):
				if url.count('.') > 1:
					par = url.split('.')
					par.reverse()
					ur=[par.pop(0),par.pop(0)]
					ur.reverse()
					url='.'.join(ur)

		_.pr(url)
	# print(urls)
	# print(type(urls))



def action():
	load(); global c3po;

	skim( '\n'.join( _.isData(r=0) ) )
	#--> iterate
	# for data in _.isData(r=0):

	

def load():
	global c3po
	c3po = _.getTable( 'table' )
	#--> print table
	_.pt(c3po)

focus()
import re
import urlextract
extractor = urlextract.URLExtract()
if _.switches.isActive('Domains'):
	from urllib.parse import urlparse



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