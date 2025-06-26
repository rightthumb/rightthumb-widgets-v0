#!/usr/bin/python3
_hash_='''
	@@@  @@@      @@@@@@       @@@@@@      @@@  @@@  
	@@@  @@@     @@@@@@@@     @@@@@@@      @@@  @@@  
	@@!  @@@     @@!  @@@     !@@          @@!  @@@  
	!@!  @!@     !@!  @!@     !@!          !@!  @!@  
	@!@!@!@!     @!@!@!@!     !!@@!!       @!@!@!@!  
	!!!@!!!!     !!!@!!!!      !!@!!!      !!!@!!!!  
	!!:  !!!     !!:  !!!          !:!     !!:  !!!  
	:!:  !:!     :!:  !:!         !:!      :!:  !:!  
	::   :::     ::   :::     :::: ::      ::   :::  
	:   : :      :   : :     :: : :        :   : :  
'''

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
import sys, time, os
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
	_.switches.register( 'Files', '-f,-file,-files','file.txt', isData='name', description='Files' )
	_.switches.register( 'Hashes', '-h,-hash,-hashes', 'md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512')
	_.switches.register( 'Compare', '-c,-compare' )

	#b)--> examples
	# _.switches.register( 'Input', '-i' )
	#e)--> examples
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )

__.setting('require-list',['Pipe','Files'])
__.setting('require-pipe||file',True)
__.setting('receipt-log',False)
__.setting('receipt-file',False)
__.setting('myFileLocations-skip-validation',False)
__.setting('require-pipe',False)
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
#n)--> start


def action():
	if _.switches.isActive('Hashes'):
		hashes = _.switches.values('Hashes')
		if not hashes: hashes = ['md5']
		if hashes[0] == 'all': hashes='md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512'.split(' ')
		if hashes[0] in '123456789' or hashes[0] == '10':
			mx=int(hashes[0])
			_hashes='md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512'.split(' ')
			hashes=[]
			for ha in _hashes:
				if len(hashes) < mx: hashes.append(ha)
	else: hashes = ['md5']
	hashID={}
	if len(_.isData()) > 1:
		_.pr(line=1,c='yellow')
	for path in _.isData():
		
		index={}
		index['path']=path
		# _.pr(path)
		IDs={}
		all_hashes=[]
		for ha in hashes:
			ash = _hash.file( path, h=ha )
			index[ha]=ash
			if not ash in IDs:IDs[ash]=[]
			IDs[ash].append(path)
			all_hashes.append(ash)
			if not path in hashID: hashID[path]=0
			hashID[path]+=1

		_.pr(index,dic=1)
		if len(_.isData()) > 1:
			_.pr(line=1,c='yellow')

	if _.switches.isActive('Compare'):
		first=True
		firsts=[]
		for ash in IDs:
			if len(IDs[ash]) > 1:
				if first:
					first=False
					_.pr('Matches:')



import _rightThumb._md5 as _hash


##################################################
#b)--> examples
banner=_.Banner(_hash_)
goss=banner.goss
goss('-\t p hash -f file.exe')
goss('-\t p hash -f file.exe -h 4')
goss('-\t p hash -f file.exe -h sha256')
goss('-\t p hash -f file.exe -h md5 sha1 sha224 sha256 sha384 sha512 sha3_224 sha3_256 sha3_384 sha3_512')
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
