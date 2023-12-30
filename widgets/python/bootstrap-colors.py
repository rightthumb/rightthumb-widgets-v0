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


def sw():
	_.switches.register( 'Root', '-root' )
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='name', description='Files', isRequired=False )

_._default_settings_()
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
	'file': 'thisApp.py',
	'description': 'Changes the world',
		# _.ail(1,'subject')+
		# _.aib('one')+
	'categories': [
						'DEFAULT',
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
	'aliases': [],
	'notes': [],
}
_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }
def triggers():
	_._default_triggers_()
	# _.switches.trigger( 'Files', _.myFileLocations, vs=True )
	# _.switches.trigger( 'Ago', _.timeAgo )
	# _.switches.trigger( 'Folder', _.myFolderLocations )
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

colors='''
#cce5ff
#533f03
#138496
#1b1e21
#fefefe
#1d2124
#86cfda
#f1b0b7
#000000
#34ce57
#b3b7bb
#d39e00
#545b62
#8fd19e
#0056b3
#ffeeba
#686868
#f5c6cb
#007bff
#b3d7ff
#040505
#19692c
#1c7430
#0f6674
#0069d9
#ffffff
#d4edda
#ececf6
#454d55
#7abaff
#495057
#abdde5
#e2e3e5
#16181b
#004085
#adb5bd
#23272b
#002752
#e0a800
#0c5460
#d6d8d9
#d1ecf1
#721c24
#f8f9fa
#95999c
#212529
#b9bbbe
#fbfcfc
#80bdff
#c82333
#bd2130
#383d41
#c8cbcf
#0b2e13
#1e7e34
#dee2e6
#117a8b
#c69500
#494f54
#202326
#491217
#856404
#121416
#b1dfbb
#fff3cd
#e4606d
#ed969e
#a71d2a
#dc3545
#bee5eb
#d6d8db
#6c757d
#e2e6ea
#155724
#dae0e5
#fcf8e3
#171a1d
#f7f7f7
#ebebeb
#c3e6cb
#d3d9df
#5a6268
#ba8b00
#e83e8c
#218838
#ffe8a1
#b21f2d
#f8d7da
#10707f
#28a745
#818182
#e9ecef
#ced4da
#ffc107
#0062cc
#cbd3da
#17a2b8
#343a40
#c6c8ca
#fdfdfe
#ffdf7e
#4e555b
#005cbf
#9fcdff
#062c33
#b8daff
'''.strip().split('\n')

def action():
	global colors
	i = 0
	dic={}
	rdic={}
	for color in colors:
		i+=1
		root = '--bootstrap-color-'+str(i)+': '+color+';'
		var = 'var(--bootstrap-color-'+str(i)+','+color+')'
		dic[color] = var
		rdic[color] = root
	if _.switches.isActive('Root'):
		print(':root {')
		for color in colors:
			print('    '+rdic[color])
		print('}')
	else:
		for path in _.myData():
			fi = _.getText2(path,'text')
			for color in colors:
				fi=fi.replace(color,dic[color])
			_.saveText(fi,path)




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
	action(); _.isExit(__file__);

