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
# import sys, time
##################################################
import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');
##################################################

# app_navigator: switches
def sw():
	pass
	#b)--> examples
	_.switches.register( 'Title/One', '-1,-one,-t,-title' )
	_.switches.register( 'Message/Two', '-2,-two,-m,-message' )
	_.switches.register( 'Bullets/Three', '-3,-three,-b,-bullet,-bullets' )
	_.switches.register( 'AddDashToBullets', '--,-dash' )
		##  -->    p SwitchGroupsExamples   <--
	# #e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='glob,name,data,clean', description='Files', isRequired=False )

_._default_settings_()
# __.setting('omit-switch-triggers',['Ago'])
# __.setting('omit-functions',['myFolderLocations','aliasesFo'])
# if not 'Ago' in __.setting('omit-switch-triggers',d=[]): pass
# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
# __.setting('receipt-log',True)
# __.setting('receipt-file',True)
# __.setting('myFileLocations-skip-validation',False)
# __.setting('require-pipe',False)
# __.setting('require-pipe||file',False)
# __.setting('pre-error',False)
# __.setting('switch-raw',[])


_.appInfo[focus()] = {
	# 'app': '8facG-jo0Cxk',
	'file': 'DisplayError.py',
	'description': 'Used in shell scripts, batch files, etc to display an error message',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'Script Helper',
						'Batch Files',
						'Shell Scripts',
						'.sh',
						'.bat',
				],
	'examples': [
						_.hp('p DisplayError -1 Missing Required Files Switch'),
						_.hp('p DisplayError -1 Missing Required Files Switch -2 "ex: -file file.txt"'),
						_.hp('p DisplayError -1 Missing Required Switch -2 Files is required, -3 "ex: -file file.txt"'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
					# { 'name': '{1}', 'abbreviation': '{0}', 'sort': '{2}' },
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'DB', _.aliasesFi )
	# _.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
	# _.switches.trigger( 'URL', _.urlTrigger )
	# _.switches.trigger( 'Duration', _.timeFuture )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );

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

def action():
	if not _.switches.isActive('Title/One'):
		_.pr( 'Error: Title/One is required',c='red' )
		return None
		
	if not _.switches.isActive('Message/Two'):
		_.e( ' '.join(_.switches.values('Title/One')) )
		return None
	if not _.switches.isActive('Bullets/Three'):
		_.e( ' '.join(_.switches.values('Title/One')),   ' '.join(_.switches.values('Message/Two')) )
		return None
	else:
		dash = _.switches.isActive('AddDashToBullets')
		_.e( ' '.join(_.switches.values('Title/One')),   ' '.join(_.switches.values('Message/Two')), _.switches.values('Bullets/Three'), dash=dash )

	_.e(   '\n'.join(_.switches.values('Title/One')),      )
	_.switches.register( 'Title/One', '-1,-one,-sub,-subject' )
	_.switches.register( 'Message/Two', '-2,-two,-m,-message' )
	_.switches.register( 'Bullets/Three', '-3,-three,-b,-bullets' )

##################################################
#b)--> examples
# banner=_.Banner(dependencies)
# goss=banner.goss
# goss('-\t this app will sherlock tf out of any python app or python module')
#e)--> examples
##################################################
########################################################################################
# import requests # pip install requests
########################################################################################
if __name__ == '__main__':
	#b)--> examples

	# banner.pr()
	# if len(_.switches.all())==0: banner.gossip()
	
	#e)--> examples
	action(); _.isExit(__file__);
