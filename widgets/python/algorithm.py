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
	_.switches.register( 'Algorithm', '-a,-algorithm' )
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

def action():

	# for path in :

	for algor in _.switches.values('Algorithm'):
		# print(algor)
		# sys.exit()
		time.sleep(1)
		_copy = _.regImp( __.appReg, '-copy' )
		# _paste = _.regImp( __.appReg, '-paste' )
		# clip = _paste.imp.paste()
		clip = '\n'.join(_.isData(r=0))
		clip=clip.replace('\t','')
		clip=clip.replace('\r','\n')
		result = []
		for cl in clip.split('\n'):
			if algor == 'vps-function-result-skimmer--01':     #algor)-->   vps-function-result-skimmer--01
				if 'Function' in cl:
					cl=cl.split('Function ')[1]
					cl=cl.replace(' ','')
					cl=cl.split('(')[0]
					result.append( cl )
			elif algor == 'vps-function-result-skimmer--02':     #algor)-->   vps-function-result-skimmer--01
				shouldAdd = True
				cl=cl.strip()
				if cl.startswith("\\' "): cl=cl.split("\\' ")[1]
				# if cl.startswith('Add '): shouldAdd=False
				if cl.startswith('from '): shouldAdd=False
				# if cl.startswith('Desc '): shouldAdd=False
				if shouldAdd:
					result.append( cl )
			pass

		if algor == 'vps-function-result-skimmer--01':
			# output = 'p cat -f '+ ' '.join(_.switches.values('Files')) +'   --c -or +    ' + ' '.join(result) + '     | p line --c + =   | call p algorithm -a vps-function-result-skimmer--01  -f '+ ' '.join(_.switches.values('Files')) +' | p execute --c'
			output = 'p cat -f '+ ' '.join(_.switches.values('Files')) +'   --c -or +    ' + ' '.join(result) + '     | p line --c + =   | call p algorithm -a vps-function-result-skimmer--02  -f '+ ' '.join(_.switches.values('Files')) +' '
			# _.pr(output)
			# os=__.imp('os.system')
			# os.system(output)
			# subprocess=__.imp('subprocess.getoutput')
			import subprocess
			run=subprocess.getoutput(output)
			# run=subprocess.getoutput(output.split('| p line')[0])
			_.pr(run)
			# _copy.imp.copy( output, p=False, clean=True )
			# _copy.imp.copy( output )
		if algor == 'vps-function-result-skimmer--02':
			# output = _paste.imp.paste()
			# _copy.imp.copy( clip )
			_.pr( '\n'.join(result) )



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
