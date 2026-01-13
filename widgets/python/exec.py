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
	_.switches.register( 'Root', '-r,-root' )
	_.switches.register( 'Scott', '-scott' )
	_.switches.register( 'AllUsers', '-u,-a,-allusers' )
	_.switches.register( 'RootScott', '-rs,-rootscott' )
	_.switches.register( 'Clean', '--c' )
	# _.switches.register( 'URL', '-u,-url,-urls', 'https://etc.ac/', isData='raw' )
	#e)--> examples
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )

# __.setting('require-list',['Files,Plus','File,Has']) # todo
# __.setting('require-list',['Pipe','Files'])
__.setting('receipt-log',True)
__.setting('receipt-file',True)
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
						_.hp(''),
						_.hp('copy:'),
						_.hp('/opt/rightthumb-widgets-v0/widgets/bash/genKeys.sh >> /opt/genKeys.log'),
						_.hp('curl -s https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/install/installer.py > /opt/rightthumb-widgets-v0/install/installer.py;  echo '' > ~/.bashrc ; python3 /opt/rightthumb-widgets-v0/install/installer.py -rc.d h ; m loading-bookmarks'),
						_.hp(''),
						_.linePrint(label='simple',p=0),
						_.hp('p vps-exec -root'),
						_.hp('p vps-exec -scott'),
						_.hp('p vps-exec -rs'),
						_.hp('|           ^ -rootscott'),
						_.hp('p vps-exec -u'),
						_.hp('|           ^ -allusers'),
						'',
	],
	'columns': [
					# { 'name': 'name', 'abbreviation': 'n' },
# columns used for
# 	- abbreviation in switches
#		- ex: -column n s
#			- instead of: -column name size
#		- ex: -sort n
#		- ex: -group n
# 	- sort is used for things like size sort by bytes
# 	- responsiveness to terminal width
# 		- order is important
# 		- most important on top
		
		# this is used for personal usage to programmatically generate columns
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

import re

def escape_pw(pw):
	return re.sub(r'([^\w])', r'\\\1', pw)
def implodeCMD(command):
	return command.replace("\n", " \\n ")
def escape_for_double_quotes(command):
	# First, escape all backslashes.
	command = command.replace("\\", "\\\\")
	# Then, escape dollar signs, backticks, and double quotes.
	command = command.replace("$", "\\$")
	command = command.replace("`", "\\`")
	command = command.replace('"', '\\"')
	return command
os=__.imp('os.system')
def action():
	accounts=''
	if _.switches.isActive('Root'):
		accounts='root'
		loginsFile=_v.rt+os.sep+'logins-root.json'
	elif _.switches.isActive('AllUsers'):
		accounts='all users'
		loginsFile=_v.rt+os.sep+'logins.json'
	elif _.switches.isActive('Scott'):
		accounts='scott'
		loginsFile=_v.rt+os.sep+'logins-scott.json'
	elif _.switches.isActive('RootScott'):
		accounts='root and scott'
		loginsFile=_v.rt+os.sep+'logins-main.json'
	else:
		_.e('No user selected','-allusers, -root, -scott')
	if not os.path.isfile(loginsFile):
		_.e('missing logins file',loginsFile)
	logins=_.getTable2(loginsFile)
	# _.pv(logins)
	command=escape_for_double_quotes(implodeCMD( '\n'.join(_.pp()) )).strip()
	# _.pr(command,c='cyan')
	_.cr(command)
	run=input(f'Execute this on as {accounts}?: ')
	for login in logins:
		user=login['login']
		pw=escape_pw(_vault.imp.s.de(login['password']))
		pwf=_.password_filter(pw)
		if _.isWin:
			pre='wsl '
		else:
			pre=''
		if 'y' in run.lower():
			cmdf=f'''{pre} sshpass -p "{pwf}" ssh  -f  {user} "{command}" '''
			cmd=f'''{pre} sshpass -p "{pw}" ssh  -f  {user} "{command}" '''
			if not _.switches.isActive('Clean'):
				cmd += ' > nul 2>&1'
			_.cr(user)
			# _.cr(cmdf)
			# os.system(cmd)

			process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

			for line in iter(process.stdout.readline, b''):
			    print(line.decode('utf-8').rstrip())

			process.stdout.close()
			process.wait()



import subprocess
_vault = _.regImp( __.appReg, '_rightThumb._vault' )
# _vault.imp.s.de(  )

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