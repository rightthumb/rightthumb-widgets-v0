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

import os
import sys
import time
# import platform
##################################################
import _rightThumb._construct as __
appDBA = __.clearFocus( __name__, __file__ )
__.appReg = appDBA
def focus( parentApp='', childApp='', reg=True ):
	global appDBA
	f = __.appName( appDBA, parentApp, childApp )
	if reg:
		__.appReg = f
	return f
__.registeredApps.append( focus() )
import _rightThumb._base3 as _
_.load()
##################################################
import _rightThumb._vars as _v
import _rightThumb._string as _str
##################################################

def appSwitches():
	_.switches.register( 'Label', '-l,-label,-lable', 'cloud-ssh-pass' )
	_.switches.register( 'Password', '-password' )
	_.switches.register( 'Clipboard', '-clip' )
	_.switches.register( 'ChangePassword', '-change' )
	_.switches.register( 'Add', '-a,-add' )
	_.switches.register( 'Get', '-g,-get' )
	_.switches.register( 'Print', '-p,-print' )
	_.switches.register( 'Alias', '-alias' )
	# _.switches.register( 'AddAlias', '-addalias' )
	_.switches.register( 'Temp', '-temp', '8' )
	_.switches.register( 'JustPrint', '-jp', 'r' )
	_.switches.register( '.bashrc-Aliases', '-ap,-rc', 'r' )
	_.switches.register( 'Backup', '-b,-backup' )


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
__.switch_raw = []
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'keychain.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'manage passwords',
	'categories': [
						'keys',
						'keychain',
						'passwords',
						'pass',
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
						'p keychain -get -label dt',
						'p keychain -add -label joplin-token -clip',
						'p keychain -add -label joplin-token --pa',
						_.linePrint(label='simple',p=0,c='yellow'),
						'p keychain -label rightthumb@yavin.m-eta.app   -add   -alias rt',
						'p keychain -get -label rt',
						'',
						'p keychain -label theName   -add    -clip',
						'p keychain -label theName   -add   -alias  tn',
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



def registerSwitches( argvProcessForce=False ):
	global appDBA
	if not __.appReg == appDBA and appDBA in __.appReg:

		if not __name__ == '__main__':
			_.argvProcess = argvProcessForce
		else:
			_.argvProcess = True

		_.load()
		_.appInfo[__.appReg] = _.appInfo[appDBA]
		_.appData[__.appReg] = _.appData[appDBA]
	__.constructRegistration( _.appInfo[__.appReg]['file'],__.appReg )
	appSwitches()

	_.myFileLocation_Print = False
	__.myFileLocations_SKIP_VALIDATION = False
	_.switches.trigger( 'Files', _.myFileLocations, vs=True )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	# _.switches.trigger( 'Files',_.inRelevantFolder )
	
	
	_.defaultScriptTriggers()
	_.switches.process()


if not __name__ == '__main__':
	_.argvProcess = False
else:
	_.argvProcess = True

registerSwitches()


def fieldSet( switchName, switchField, switchValue, theFocus=False ):
	if not type( theFocus ) == bool:
		theFocus = theFocus
	_.switches.fieldSet( switchName, switchField, switchValue, theFocus )


if __name__ == '__main__':
	if not sys.stdin.isatty():
		_.setPipeData( sys.stdin.readlines(), __.appReg, clean=True )


_.postLoad( __file__ )

########################################################################################
# START


def add():
	global table
	global label
	global aliases
	password = None

	if _.switches.isActive('Alias'):
		for alias in _.switches.values('Alias'):
			aliases[alias] = label
		_.saveTableDB( aliases, 'keychain-aliases.hash' )
		return None

	if _.switches.isActive('Clipboard'):
		password = _copy.imp.paste()
	if _.switches.isActive('Password'):
		password = _.switches.values('Password')[0]
	try:
		table[label] = _vault.imp.s.en( password )
	except: _.e( 'Login error' )
	# if 'eof' in table: del table['eof']; table['eof']='';
	_.saveTableDB( table, 'keychain.hash' )



def possibly_wait():
	if  _.switches.isActive('Temp'):
		# _.pr('Temp')
		loops = 15
		if len( _.switches.value('Temp') ):
			loops = int( _.switches.value('Temp') )

		while loops:
			_.updateLine( 'waiting: '+str(loops) )
			loops -= 1
			if not loops:
				_.updateLine( '                  ' )
				_.updateLine( '\r' )
				break
			time.sleep(1)
			_.updateLine( '                  ' )

		_copy.imp.copy( '', p=0  )
__.keychain_copy=True
def get(theLabel=None,cp=True):
	__.keychain_copy=cp
	load()
	global table
	global label
	global aliases
	if not theLabel is None:
		label = theLabel

	password = ''
	# _.pr('label',label)
	if label in table:
		try:
			password = _vault.imp.s.de(table[label])
		except: _.e( 'Login error' )

		if theLabel is None and not _.switches.isActive('JustReturn'):
			if _.switches.isActive('JustPrint'):
				if 'r' == _.switches.value('JustPrint'):
					_.pr(password+'\r')
				else:
					_.pr(password)
				return password
			if __.keychain_copy and len(password):
				_copy.imp.copy( password, p=_.v.p  )
		
		if __.keychain_copy and len(password):
			if not _.switches.isActive('Print'):
				_.pr('copied:',label,c='green')
			possibly_wait()
		return password
	elif label in aliases:
		try:
			password = _vault.imp.s.de(table[aliases[label]])
		except: _.e( 'Login error' )
		if theLabel is None and not _.switches.isActive('JustReturn'):
			if _.switches.isActive('JustPrint'):
				if 'r' == _.switches.value('JustPrint'):
					_.pr(password+'\r')
				else:
					_.pr(password)
				return password
			_copy.imp.copy( password, p=_.v.p  )
		if len(password):
			if not _.switches.isActive('Print'):
				_.pr('copied:',label,c='green')
		possibly_wait()
		return password
	else:
		return None
	

def changePassword():
	global table

	for label in table:
		try:
			table[label] = _vault.imp.s.de(table[label])
		except: _.e( 'Login error' )

	_logout = _.regImp( __.appReg, 'logout' )
	_logout.action()

	for label in table:
		try:
			table[label] = _vault.imp.s.en(table[label])
		except: _.e( 'Login error' )
	# if 'eof' in table: del table['eof']; table['eof']='';
	_.saveTableDB( table, 'keychain.hash' )

def addAlias():
	global table
	global label
	global aliases
	if _.switches.isActive('Alias'):
		for alias in _.switches.values('Alias'):
			aliases[alias] = label
		_.saveTableDB( aliases, 'keychain-aliases.hash' )

def bashrc_aliases():
	aliases = """
################# ################# #################
alias exp.gen="$tech_drive/tech/programs/python/src/unity/expect-gen.py -p "
alias exp.geny="$tech_drive/tech/programs/python/src/unity/expect-gen.py -p -y "
alias pr.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label p.r -jp -get )"
alias pr.e="exp.gen;pr.do"
alias p9.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label p.9 -jp -get )"
alias pv.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label vault -jp -get )"
alias pv.e="exp.gen;pv.do"
#################
alias vps.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label vps.scott -jp -get )"
alias vps.e="exp.gen;vps.do"
alias vps.ey="exp.geny;vps.do"
alias vps.el="echo su root | vps.e"
#################
alias reph.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label reph.l -jp -get )"
alias reph.e="exp.gen;reph.do"
alias reph.ey="exp.geny;reph.do"
alias reph.el="echo su root | reph.e"
#################
alias web.do="$HOME/.rt/profile/temp/temp.exp $( $tech_drive/tech/programs/python/src/unity/keychain.py -label web.l -jp -get )"
alias web.e="exp.gen;web.do"
alias web.ey="exp.geny;web.do"
alias web.el="echo su root | web.e"
################# #################
alias ssh.1="echo 'ssh -R 8888:localhost:22 -C -N -l scott vps.rightthumb.com' | vps.e";
alias ssh.2="echo 'ssh -R 8888:localhost:22 -C -N -l scott vps.rightthumb.com' | vps.e";
alias ssh.3="echo 'ssh scott@localhost -p 8080' | vps.e";
alias ssh.3b="echo 'ssh rephs@localhost -p 8080' | vps.e";
#################
alias vps.l="p keychain -label vps.l  -get -temp 10"
alias web.l="p keychain -label web.l  -get -temp 10"
alias reph.l="p keychain -label reph.l  -get -temp 10"
#################
alias vps.socket="echo 'ssh -R 65432:localhost:65432 -C -N -l scott vps.rightthumb.com' | vps.e";
################# #################
alias reph.ssh.p="echo 'ssh thisreph@reph.us'";
alias vps.ssh.p="echo 'ssh scott@vps.rightthumb.com'";
alias web.ssh.p="echo 'ssh ximlickficfp@tools.rightthumb.com'";
################# #################
alias reph.ssh.y="echo 'ssh thisreph@reph.us' | reph.ey";
alias vps.ssh.y="echo 'ssh scott@vps.rightthumb.com' | vps.ey";
alias web.ssh.y="echo 'ssh ximlickficfp@tools.rightthumb.com' | web.ey";
#################
alias reph.ssh="echo 'ssh thisreph@reph.us' | reph.e";
alias vps.ssh="echo 'ssh scott@vps.rightthumb.com' | vps.e";
alias web.ssh="echo 'ssh ximlickficfp@tools.rightthumb.com' | web.e";
################# #################
alias beep.="play -nq -t alsa synth 1 sine 440"
################# ################# #################
alias vps.sync.sh="$HOME/.rt/tool -sh.folder /mnt/d/tech/programs/webApps/vps/"
alias vps.sync="echo scp /mnt/d/tech/programs/servers/web/vps/* root@vps.rightthumb.com:/opt/lampp/htdocs/|vps.e"
alias vps.sync.get="echo scp root@vps.rightthumb.com:/opt/lampp/htdocs/ /mnt/d/tech/programs/servers/web/vps/* |vps.e"
alias vps.www="echo    'ssh -L 8080:localhost:80 -C -N -l scott vps.rightthumb.com'    |  s.vps.e"
export vpswww="sudo ssh -L 80:localhost:80 -C -N -l scott vps.rightthumb.com"
alias vps.dt="echo    'ssh -L 59000:localhost:5900 -C -N -l scott vps.rightthumb.com'    |  vps.e"
alias vps.dt2="echo    'ssh -L 59001:localhost:5901 -C -N -l scott vps.rightthumb.com'    |  vps.e"
alias vps.k="echo $( p keychain -get -label vps.k )"
alias kk="echo $( p keychain -get -label login-test )"

	"""
	_.pr( aliases )

def action():
	if _.switches.isActive('Paste-isData'): _.switches.fieldSet( 'Clipboard', 'active', True )
	if _.switches.isActive('.bashrc-Aliases'):
		bashrc_aliases()
		return None

	load()
	if _.switches.isActive('Add'):
		add()

	if _.switches.isActive('Get'):
		get()

	if _.switches.isActive('ChangePassword'):
		changePassword()

	if _.switches.isActive('AddAlias'):
		addAlias()

def load():
	global table
	global label
	global aliases
	def _bk_(yml,save):
		if os.path.isfile(save):
			_.deFi(save,ext=False)
			time.sleep(.3)
			bk=_.getText(save,raw=True,clean=2).split('\n')
		else:
			bk=[]
		bk.append('___')
		bk.append(_.friendlyDate(__.startTime))
		for line in yml.split('\n'):
			if not line in bk:
				bk.append(line)
		_.saveText(bk,save)
		time.sleep(.1)
		bk=_.getText(save,raw=True,clean=2).split('\n')
		time.sleep(.1)
		_.saveText(bk,save)
		time.sleep(.3)
		_.enFi(save,ext=False)
	if table is None:
		table = _.getTableDB( 'keychain.hash' )
		aliases = _.getTableDB( 'keychain-aliases.hash' )
		if _.switches.isActive('Backup'):
			backup={}
			for k in table:
				try:
					backup[k]=_vault.imp.s.de(table[k])
				except: _.e( 'Login error' )
			yml=_.toYML(backup)

			save = _v.tt+os.sep+'keychain.crypt'
			save2 = _v.tt+os.sep+'keychain'+'-'+_.friendlyDate(__.startTime).split(' ')[0]+'.crypt'
			_bk_(yml,save)
			# try: _bk_(yml,save)
			# except: _bk_(yml,save2)


			return None
		_.v.p = _.switches.isActive('Print')
		label = _.switches.value('Label')
		if _.switches.isActive('Label'):
			if not label:
				_.e( 'missing label' )
		# _.pr('label:',label)
		# _.vp(table)
		# sys.exit()
table = None
key = get

_copy = _.regImp( __.appReg, '-copy' )
# _copy.imp.copy(  )
# _copy.imp.paste(  )


_vault = _.regImp( __.appReg, '_rightThumb._vault' )
# _vault.imp.s.de(  )


# _keychain = _.regImp( __.appReg, 'keychain' )
# _keychain.imp.key('')

########################################################################################
if __name__ == '__main__':
	action()
	_.tables.eof()