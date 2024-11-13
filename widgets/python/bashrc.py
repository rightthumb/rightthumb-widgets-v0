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
	pass


_.autoBackupData = __.autoCreationConfiguration['backup']
__.releaseAcquiredData = __.autoCreationConfiguration['logs']
__.myFileLocations_SKIP_VALIDATION = False
__.isRequired_Pipe = False
__.isRequired_Pipe_or_File = False
__.pre_error = False
# __.switch_raw = [ 'Delim' ]
# __.isRequired_or_List = ['Pipe','Files','Plus']

_.appInfo[focus()] = {
	'file': 'bashrc.py',
	'liveAppName': __.thisApp( __file__ ),
	'description': 'edit bashrc',
	'categories': [
						'bashrc',
						'linux',
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
						'p thisApp -file file.txt',
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
	_.switches.trigger( 'Files', _.myFileLocations )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'URL', _.urlTrigger )
	_.switches.trigger( 'Ago', _.timeAgo )
	_.switches.trigger( 'Duration', _.timeFuture )
	
	
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



def action( bashrc_manual=None ):

	global spent

	root_bashrc_check = [
							'/root/.bashrc',
							'/etc/bash.bashrc',
	]


	global code
	if not _.isWin:


		tmpFile = _v.stmp+'/who.txt'
		os.system("whoami>"+tmpFile)
		username = 'user'
		if os.path.isfile(tmpFile):
			username = _.getText( tmpFile, clean=2,raw=True ).replace('\n','')
		


		
		if not bashrc_manual is None:
			# _.pr('specified', bashrc_manual)
			bashrc_path = bashrc_manual
		elif bashrc_manual is None:

			# if not username == 'root':
			bashrc_path = os.getenv('HOME') + _v.slash + '.bashrc'
			
			if username == 'root':
				action( bashrc_path )
				action( root_bashrc_check[0] )
				for i,root_test in enumerate(root_bashrc_check):
					if i:
						if os.path.isfile(root_test):
							action( root_test )
				sys.exit()
		if bashrc_path in spent:
			return None


		spent.append(bashrc_path)
		_.pr( 'whoami:', username )
		# _.pr( 'running:',bashrc_path )
		bashrc = _.getText( bashrc_path, raw=True )
		s = '## {E45D09D22184} ##'
		e = '## {AEC80B4D3338} ##'
		if bashrc is None:
			bashrc = ''
		if not s in bashrc:
			bashrc += '\n\n'
			bashrc += s
			bashrc += '\n\n'
			bashrc += e
			bashrc += '\n\n'


		alias = []
		for item in code.split('\n'):
			# item = _str.cleanBE(item,' ')
			alias.append(item)

		active=False
		wasActive=False
		new_bashrc = ''
		for line in bashrc.split('\n'):
			if s in line:
				active=True


			if not active:
				new_bashrc += line + '\n'

			if e in line:
				new_bashrc += s + '\n'
				for a in alias:
					new_bashrc += a + '\n'

				new_bashrc += e + '\n'
				active=False
				wasActive=True


		_.saveText( new_bashrc, bashrc_path )
		_.colorThis(  [bashrc_path, 'updated'], 'cyan'  )

spent = []

code = """

chmod 777 -R $HOME/.rt/

############################################################################

$( $HOME/.rt/tool -bash.vars )

############################################################################








####################################

alias p.ls="$HOME/.rt/tool -app.ls";
alias p.bashrc="$HOME/.rt/tool -app.bashrc";
alias p.which="$HOME/.rt/tool -app.which";
alias p.ago="$HOME/.rt/tool -app.ago";

alias p.file="$HOME/.rt/tool -app.file";
alias p.files="$HOME/.rt/tool -app.files";
alias p.folder="$HOME/.rt/tool -app.folder";
alias p.folders="$HOME/.rt/tool -app.folders";

alias p.paths="$HOME/.rt/tool -app.paths";
alias t.p="$HOME/.rt/tool -app.paths";

alias p.shClean="$HOME/.rt/tool -sh.file";
alias p.shClean.r="$HOME/.rt/tool -sh.folder.r";

alias s.p.shClean="sudo $HOME/.rt/tool -sh.file";
alias s.p.shClean.r="sudo $HOME/.rt/tool -sh.folder.r";

alias bash.vars="$HOME/.rt/tool -bash.vars";
alias t.dl="$HOME/.rt/tool -dl";
alias t.url.get="$HOME/.rt/tool -url.get";
alias t.wget.url="$HOME/.rt/tool -wget.url";
alias t.online="$HOME/.rt/tool -is.online";
alias t.o="$HOME/.rt/tool -is.online";
alias t.ip="$HOME/.rt/tool -is.online";

alias t.bashrc.mini="$HOME/.rt/tool -bashrc.mini";
alias t.bashrc.full="$HOME/.rt/tool -bashrc.full";
alias t.valid="$HOME/.rt/tool -file.valid";
alias t.pipe="$HOME/.rt/tool -setting.pipe.print x";
alias t.p="$HOME/.rt/tool -setting.pipe.print x";
alias t.pipe.clean="$HOME/.rt/tool -setting.pipe.clean";
alias t.p.clean="$HOME/.rt/tool -setting.pipe.clean";
alias line="$HOME/.rt/tool -app.line";



alias t="$HOME/.rt/tool ";
alias s.t="sudo $HOME/.rt/tool ";
alias tool="$HOME/.rt/tool ";
alias s.tool="sudo $HOME/.rt/tool ";

alias t3="$HOME/.rt/tool";
alias s.t3="sudo $HOME/.rt/tool";

alias t2="$HOME/.rt/tool2";
alias s.t2="sudo $HOME/.rt/tool2";
alias tool2="$HOME/.rt/tool2";
alias s.tool2="sudo $HOME/.rt/tool2";

alias t.sh="$HOME/.rt/tool.sh";
alias s.t.sh="sudo $HOME/.rt/tool.sh";
alias c="clear";

alias ssh.p="ssh -R 8888:localhost:1 -C -N -l scott vps.rightthumb.com";
alias ssh.pp="ssh -R 8888:localhost:5900 -C -N -l scott vps.rightthumb.com";
alias ssh.dt="ssh -L 59000:localhost:8888 -C -N -l scott vps.rightthumb.com";
alias ssh.1="ssh -R 8888:localhost:22 -C -N -l scott vps.rightthumb.com";
alias ssh.2="ssh -L 8080:localhost:8888 -C -N -l scott vps.rightthumb.com";
alias ssh.3="ssh scott@localhost -p 8080";

alias ssh.r="ssh -R 8888:localhost:22 -C -N -l scott vps.rightthumb.com";
alias ssh.l="ssh -L 8080:localhost:8888 -C -N -l scott vps.rightthumb.com";
alias ssh.s="ssh scott@localhost -p 8080";
alias ssh.reph="ssh rephs@localhost -p 8080";
alias ssh.root="ssh root@localhost -p 8080";
####################################





alias s.p="sudo $tech_drive/tech/programs/bash/nav/p.sh"
alias s.pp="sudo $tech_drive/tech/programs/bash/nav/pp.sh"
alias p.sudo="sudo $tech_drive/tech/programs/bash/nav/p.sh"
alias pp.sudo="sudo $tech_drive/tech/programs/bash/nav/pp.sh"
alias p="$tech_drive/tech/programs/bash/nav/p.sh"
alias pp="$tech_drive/tech/programs/bash/nav/pp.sh"
alias b="$tech_drive/tech/programs/bash/nav/b.sh"
alias bb="$tech_drive/tech/programs/bash/nav/bb.sh"
alias m="$tech_drive/tech/programs/bash/nav/m.sh"
alias d="$tech_drive/tech/programs/bash/nav/d.sh"
alias bs="$tech_drive/tech/programs/bash/nav/bs.sh"

alias n="$tech_drive/tech/programs/bash/nav/n.sh"
alias e="$tech_drive/tech/programs/bash/nav/e.sh"
alias epy="$tech_drive/tech/programs/bash/nav/epy.sh"
alias epyi="$tech_drive/tech/programs/bash/nav/epyi.sh"

alias s.n="sudo $tech_drive/tech/programs/bash/nav/n.sh"
alias s.e="sudo $tech_drive/tech/programs/bash/nav/e.sh"
alias s.epy="sudo $tech_drive/tech/programs/bash/nav/epy.sh"
alias s.epyi="sudo $tech_drive/tech/programs/bash/nav/epyi.sh"


alias x="$tech_drive/tech/programs/bash/nav/x.sh"

alias bashFix="chmod 777 $tech_drive/tech/programs/bash/*.sh"

alias dirx="$tech_drive/tech/programs/bash/nav/dirX.sh"

alias p0="$tech_drive/tech/programs/bash/nav/p0.sh"
alias pu="$tech_drive/tech/programs/bash/nav/p0.sh"
alias p00="$tech_drive/tech/programs/bash/nav/p00.sh"
alias pw="$tech_drive/tech/programs/bash/nav/p00.sh"
alias v="$tech_drive/tech/programs/bash/nav/v.sh"


alias c="$tech_drive/tech/programs/bash/nav/c.sh"
alias epyiBuild="$tech_drive/tech/programs/bash/nav/epyiBuild.sh"
alias hack="$tech_drive/tech/programs/bash/hack.sh"
alias newpage="$tech_drive/tech/programs/bash/newpage.sh"



export stmp="$tech_drive/tech/hosts/$(hostname)/temp"
export tmpf0="$tech_drive/tech/hosts/$(hostname)/temp/{B820137A-79B8-45E3-BCBD-A6CAC50892D0}"
export tmpf1="$tech_drive/tech/hosts/$(hostname)/temp/{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}"
export tmpf2="$tech_drive/tech/hosts/$(hostname)/temp/{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}"
export tmpf3="$tech_drive/tech/hosts/$(hostname)/temp/{F139D191-FA1A-44D5-855C-7E5141B30E0D}"
export tmpf4="$tech_drive/tech/hosts/$(hostname)/temp/{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}"
export tmpf5="$tech_drive/tech/hosts/$(hostname)/temp/{201D82D6-2DC0-4552-A598-54F5481399A1}"
export tmpf6="$tech_drive/tech/hosts/$(hostname)/temp/{26B3B9C6-0A59-432A-9386-D432B53001CB}"
export tmpf7="$tech_drive/tech/hosts/$(hostname)/temp/{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}"
export tmpf8="$tech_drive/tech/hosts/$(hostname)/temp/{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}"
export tmpf9="$tech_drive/tech/hosts/$(hostname)/temp/{DF1D4EBC-838E-419C-9C58-943C1767391A}"




# echo "a"
config="$tech_drive/tech/hosts/$(hostname)/config"
# echo "b"
unixID="$config/.unix_id"



if [[ ! -e $config ]]; then
	echo "0 no config"
	# echo " c000 ";
	mkdir $config;
else

# echo "c"
	

	unixID1=$( sed -n '1p' < $unixID )
	unixID2=$( sed -n '2p' < $unixID )
	unixID3=$( sed -n '3p' < $unixID )
	unixID4=$( sed -n '4p' < $unixID )
	unixID5=$( sed -n '5p' < $unixID )
	unixID6=$( sed -n '6p' < $unixID )
	unixID7=$( sed -n '7p' < $unixID )
	unixID8=$( sed -n '8p' < $unixID )
	unixID9=$( sed -n '9p' < $unixID )
	unixID10=$( sed -n '10p' < $unixID )




fi

if [[ ! -e $unixID ]]; then
	touch $unixID
fi



alias vnc.toggle="$tech_drive/tech/programs/bash/nav/p.sh toggle_comment -f /etc/vnc.conf -label vnc"
alias vnc.off='vncserver-stop'
alias vnc.on="$tech_drive/tech/programs/bash/dt/vnc-on.sh"



alias fix="chmod -R 777 $tech_drive"
alias fixme="sudo chmod -R 777 $tech_drive"
alias sudofix="sudo chmod -R 777 $tech_drive"
alias fixme.root="sudo chmod -R 777 $tech_drive"
alias fixme.sudo="sudo chmod -R 777 $tech_drive"
alias fixme.su="sudo chmod -R 777 $tech_drive"
alias s.fixme="sudo chmod -R 777 $tech_drive"

alias register_terminal="$tech_drive/tech/programs/bash/register_terminal.sh"

notes_folder="$tech_drive/tech/programs/bash/notes"
notes_file="$notes_folder/RT-SCRAP-$unixID7.txt"

alias cat.scrap="cat $notes_file"


alias scrap="$tech_drive/tech/programs/bash/scrap.sh"
alias notes="$tech_drive/tech/programs/bash/scrap.sh"
alias ent='p imdb -ent '
#alias entep='p imdb -live -case -ep -ent '
alias ee='p imdb -live -case -ep -ent '

alias uuid='p genuuid'
alias uuids='p genuuid -cnt 10'
alias n.rc='n ~/.bashrc'

tech_drive="$tech_drive"
p="bash $tech_drive/tech/programs/bash/nav/p.sh"




export config

export tech_drive
export p

alias ls.d='p ls -ago 2d -c ago name -g ago  -sort md'
alias ls.='p ls  -c ago name -g ago  -sort md -ago  '
alias watch.vnc="$tech_drive/tech/programs/bash/vnc_watch.sh> /dev/null 2>&1 & "

alias cloud='p cloud -sync'

alias ls.p='p ls -s md -g ago --c  -nocolor  -c path'
alias a.cp='p copyTool'
alias scrap.seg='echo "_________________ _________________ _________________ _________________"'

alias cdf="$tech_drive/tech/programs/bash/cdf.sh"
alias copy="xsel --clipboard --input"
alias paste="xsel --clipboard --output"
alias cloud.fix="sudo $tech_drive/tech/programs/bash/nav/p.sh cloud -sync"
alias cloud.fix.dl="sudo $tech_drive/tech/programs/bash/nav/p.sh cloud -sync -download"
alias cloud.sync.dl="$tech_drive/tech/programs/bash/nav/p.sh cloud -sync -download"
alias cloud.sync="$tech_drive/tech/programs/bash/nav/p.sh cloud -sync"
alias c.s="sudo $tech_drive/tech/programs/bash/nav/p.sh cloud -sync"
alias c.s.dl="sudo $tech_drive/tech/programs/bash/nav/p.sh cloud -sync -download"

alias a.tools.vps="p -copy -subject tools vps | p cryptString -de -clip -temp 8"
alias a.tools.vps.scott="p -copy -subject tools vps.scott | p cryptString -de -clip -temp 8"
alias a.tools.vps.scott.dt="p -copy -subject tools vps.scott.desktop"
alias a.tools.vps.scott.dt.ssh="p -copy -subject tools vps.scott.desktop"
alias a.tools.vps.scott.dt.l="p -copy -subject tools vps.scott.desktop.login | p cryptString -de -clip -temp 8"
alias a.tools.vps.scott.dt.id="p -copy -subject tools vps.scott.desktop.id"
alias py="python3"


export HISTSIZE=100000
export HISTFILESIZE=100000

# export PS1='${debian_chroot:+($debian_chroot)}\\[\033[01;32m\\]\\u@\\h\\[\033[00m\\]: '

force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
	if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	color_prompt=yes
	else
	color_prompt=
	fi
fi

EMOJIS=(🧻 🧪 💀 🦆 🦉 🥓 🦄 🦀 🖕 🍣 🍤 🍥 🍡 🥃 🥞 🐕 👾 🐉 🐓 🐋 🐌 🐢 👽 👿 🥑 🐡 🐗 💐 🏹 🎨 🐔 🐛 🎯 🌯 📷 🛶 🥕 🍒 🍸 🍳 🐲 🎣 🐟 🦅 👀 🐸 🤞 💪 💾 👻 🐊 🍔 🌭 🍀 🕓 🦊 🍟 🥝 🖕 🐒 🥞 🐼 📎 🐧 💩 🍕 🍍 🦏 🍗 🌈 🐳 🦑 🚀 🙈 🙊 🙉 🌮 🥒 🐅 🐯 🍉 🚽 🍅 👅 🎩 🍷)
prompt_symbol=${EMOJIS[$RANDOM % ${#EMOJIS[@]}]};


if [ "$color_prompt" = yes ]; then
	prompt_color='\\[\033[;32m\\]'
	info_color='\\[\033[1;34m\\]'
	#prompt_symbol=㉿
	if [ "$EUID" -eq 0 ]; then # Change prompt colors for root user
	prompt_color='\\[\033[;94m\\]'
	info_color='\\[\033[1;31m\\]'
	#prompt_symbol=💀
	fi
	PS1=$prompt_color'┌──${debian_chroot:+($debian_chroot)──}('$info_color'\\u${prompt_symbol}\\h'$prompt_color')-[\\[\033[0;1m\\]\\w'$prompt_color']\n'$prompt_color'└─'$info_color'\\$\\[\033[0m\\] '
else
	# PS1='${debian_chroot:+($debian_chroot)}\\u@\\h:\\w\\$ '
	PS1='┌── (\\u${prompt_symbol}\\h)──[\\w] \\n└─── $ '
fi
unset color_prompt force_color_prompt


# sudo apt install fonts-emojione

# sudo apt     --purge remove mplayer
# sudo apt-get --purge remove mplayer

alias up.date="echo "update"; sudo apt-get update; echo "upgrade"; sudo apt-get upgrade;"



	# if [ "${#XDG_CURRENT_DESKTOP}" -lt 2 -a "${#GDMSESSION}" -lt 2 ]; then
	#     touch "$config/.isTerminal"
	#             if [[  -e "$config/.editor.pre" ]]; then




alias vps.ssh="echo 'ssh -L 59000:localhost:5901 -C -N -l scott vps.rightthumb.com' "
alias vps.l="p -copy -subject tools vps.scott.desktop.login | p cryptString -de -clip -temp 8"
alias vps.sshx="p -copy -subject tools vps.scott | p cryptString -de -clip ; ssh -L 59000:localhost:5901 -C -N -l scott vps.rightthumb.com "

alias web.ssh="echo 'ssh ximlickficfp@tools.rightthumb.com'"
alias web.l="p -copy -subject tools ssh | p cryptString -de -clip -temp 8"
alias web.sshx="p -copy -subject tools ssh  | p cryptString -de -clip ; ssh ximlickficfp@tools.rightthumb.com"

alias bbb="p hasAlias"
alias app="p searchAppRegistrationInfo"

alias tool="$HOME/.rt/tool"
alias tool.sh="$HOME/.rt/tool.sh"
alias s.tool="sudo $HOME/.rt/tool"
alias s.tool.sh="sudo $HOME/.rt/tool.sh"
alias load.fix="$HOME/.rt/tool -sh.file $tech_drive/tech/programs/bash/load-vars.sh"
alias t="$HOME/.rt/tool"
alias t.sh="$HOME/.rt/tool.sh"
alias s.t="sudo $HOME/.rt/tool"
alias s.t.sh="sudo $HOME/.rt/tool"
alias listening2="lsof -i -P -n | grep LISTEN"
alias listening="netstat -l | p simpleLine + listen - listening"
alias fw.y="sudo ufw allow "
alias fw.n="sudo ufw deny "

cd $HOME


"""

# export PATH=$PATH:/place/with/the/file

# alias cdf=" cd $(p popFile -f $1) "


########################################################################################
if __name__ == '__main__':
	action()






