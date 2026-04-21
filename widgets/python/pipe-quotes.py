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
	# _.switches.register( 'Input', '-i' )
	# _.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=True )
	#e)--> examples

_.appInfo[focus()] = {
	'file': 'pipe-quotes.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'Changes the world',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp(' p files + *.py --c | p f3 + os.environ |  p pipe-quotes'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'created': None,
	'tested': 1658904289.9009602,
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

def process():
	text='\n'.join( _.isData(r=0) )
	validator._err_ = False
	index = validator.createIndex( text, 'javascript', skipLoad=True, simple=False, A=None, B=True, C=None )
	for k in validator.identity['location']['open']:
		quote = validator.assetSnipetClean(k,validator.identity['location']['open'][k])
		if quote.startswith('"') or quote.startswith("'"):
			quote=quote[:-1]; quote=quote[1:];
			if _.showLine(quote): _.pr(quote)
def action():
	try: process()
	except Exception as e: pass
	


	
_code = _.regImp( __.appReg, '_rightThumb._auditCodeBase' )
validator = _code.imp.Validator()





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