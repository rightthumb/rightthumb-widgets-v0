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
	_.switches.register( 'Modules', '-m' )
	_.switches.register( 'Just-Versions', '-jv' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	
	#n)--> epyi base -file template
	
	#e)--> examples

_.appInfo[focus()] = {
	'file': 'py-module-version-by-date.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'read header of every download and see what date it is',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('p py-module-version-by-date -m elasticsearch_dsl -year 2016'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'created': None,
	'tested': 1658900582.441664,
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
		# _bk = _.regImp( focus(), 'fileBackup' ); _bk.switch( 'Silent' ); _bk.switch( 'isRunOnce' ); _bk.switch( 'Flag', focus() ); _bk.switch( 'DoNotSchedule' )
		# _bk.switch( 'Input', path ); bkfi = _bk.action();
	
	#n)--> inline
		# for rel in [ subject for subject in _.isData(r=0) if _.showLine(subject) ]: print(rel)

	#n)--> banner
		# banner=_.Banner(app); goss=banner.goss;
#e)--> examples
########################################################################################
#n)--> start


import subprocess
import requests
from bs4 import BeautifulSoup
 
# urls = 'https://www.geeksforgeeks.org/'

import sys
def build_date(line):

	# 0 last-modified:
	# 1 Wed,
	# 2 26
	# 3 Feb
	# 4 2020
	# 5 17:49:43
	# 6 GMT
	moi = {}
	for i, it in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split(' ')):
		ii=str(i+1)
		if len(ii)==1:ii='0'+ii
		moi[it]=ii
	par = line.split(' ')

	if len(par[2])==1:par[2]='0'+par[2]
	fDate=par[4]+'-'+moi[par[3]]+'-'+par[2]
	fTime=fDate+' '+par[5]
	return fDate
	# for i, it in enumerate(par):
	#     _.pr(i,it)
	# sys.exit()

def find_version(line):
	par=line.split('-')[1]
	txt=''
	for ch in par:
		if ch in '0123456789.':
			txt+=ch
		else:
			break
	txt=_str.do('be',txt,'.')
	return txt

def links(module):
	url = 'https://pypi.org/simple/'+module+'/'
	grab = requests.get(url)
	soup = BeautifulSoup(grab.text, 'html.parser')

	for link in soup.find_all("a"):
		data = link.get('href')

		ul = data.split('/')
		ul.reverse()
		fi = ul[0].split('#')[0]
		ver = find_version(fi)
		if _.switches.isActive('Just-Versions'):
			_.pr(ver,c='green')
		else:
			header = subprocess.getoutput('curl --head "'+data+'"')
			for line in header.split('\n'):
				if 'last-modified' in line:
					_.pr(build_date(line), fi)

	# print()
	# print(data)


def action():
	if not _.switches.isActive('Just-Versions'):
		if _.isWin:
			_.e('linux only, for now')

	if _.switches.isActive('Modules'):
		for module in _.switches.values('Modules'):
			links(module)

# https://pypi.org/project/elasticsearch-dsl/#history    


# https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/

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