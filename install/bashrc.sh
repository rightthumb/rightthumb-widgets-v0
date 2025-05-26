#!/bin/bash

# source /opt/rightthumb-widgets-v0/install/source.sh

## {E45D09D22184} ##



################# ################# ################# #################
[ ! -d $HOME/.rt ] && mkdir $HOME/.rt
[ ! -d $HOME/.rt/profile ] && mkdir $HOME/.rt/profile
[ ! -d $HOME/.rt/profile/temp ] && mkdir $HOME/.rt/profile/temp
touch $HOME/.rt/profile/temp/temp.exp
chmod 777 -R $HOME/.rt/
chmod 777 $HOME/.rt/profile/temp/temp.exp
################# ################# ################# #################

source $HOME/.rt/profile/vars/config.sh
source $HOME/.rt/profile/vars/personal.sh


################# ################# ################# #################
alias get.t.sh="wget http://reph.us/tools/file.php?file=tool.sh -O $HOME/.rt/tool.sh";
alias get.t="wget http://reph.us/tools/file.php?file=tool -O installer.py; $PY $widgets/install/installer.py -h.f installer.py;";
alias get.t2="wget http://reph.us/tools/file.php?file=tool2 -O installer.py2; $PY installer.py2 -h.f installer.py2;";
alias get.h="wget http://reph.us/tools/file.php?file=help.txt -O $HOME/.rt/help.txt; $PY installer.py2 -h.f $HOME/.rt/help.txt;";

################# ################# #################
alias m="$widgets/install/installer.py -app.m";
alias b="$widgets/install/installer.py -app.b";
alias d="$widgets/install/installer.py -app.d";
################# ################# #################
alias p.ls="$widgets/install/installer.py -app.ls";
alias p.bashrc="$widgets/install/installer.py -app.bashrc";
alias p.which="$widgets/install/installer.py -app.which";
alias p.ago="$widgets/install/installer.py -app.ago";

alias p.file="$widgets/install/installer.py -app.file";
alias p.files="$widgets/install/installer.py -app.files";
alias p.folder="$widgets/install/installer.py -app.folder";
alias p.folders="$widgets/install/installer.py -app.folders";

alias p.paths="$widgets/install/installer.py -app.paths";
alias t.p="$widgets/install/installer.py -app.paths";

alias p.shClean="$widgets/install/installer.py -sh.file";
alias p.shClean.r="$widgets/install/installer.py -sh.folder.r";

alias s.p.shClean="sudo $widgets/install/installer.py -sh.file";
alias s.p.shClean.r="sudo $widgets/install/installer.py -sh.folder.r";

alias bash.vars="$widgets/install/installer.py -bash.vars";
alias t.dl="$widgets/install/installer.py -dl";
alias t.url.get="$widgets/install/installer.py -url.get";
alias t.wget.url="$widgets/install/installer.py -wget.url";
alias t.online="$widgets/install/installer.py -is.online";
alias t.o="$widgets/install/installer.py -is.online";
alias t.ip="$widgets/install/installer.py -is.online";

alias t.rc.mini="$widgets/install/installer.py -bashrc.mini";
alias t.rc.full="$widgets/install/installer.py -bashrc.full";
alias t.rc.def="$widgets/install/installer.py -bashrc.def";
alias t.valid="$widgets/install/installer.py -file.valid";
alias t.pi="$widgets/install/installer.py -setting.pipe.print x";
alias t.pipe="$widgets/install/installer.py -setting.pipe.print x";
alias t.p="$widgets/install/installer.py -setting.pipe.print x";
alias t.pipe.clean="$widgets/install/installer.py -setting.pipe.clean";
alias t.p.clean="$widgets/install/installer.py -setting.pipe.clean";
alias t.pi.c="$widgets/install/installer.py -setting.pipe.clean";
alias t.p.c="$widgets/install/installer.py -setting.pipe.clean";
alias line="$widgets/install/installer.py -app.line";

alias file.header="$widgets/install/installer.py -header.fix.file";
alias file.header.fix="$widgets/install/installer.py -header.fix.file";
alias file.header.read="$widgets/install/installer.py -header.read";

alias sh.fi="$widgets/install/installer.py -sh.file";
alias sh.fo="$widgets/install/installer.py -sh.folder";
alias sh.fo.r="$widgets/install/installer.py -sh.folder.r";

alias h.fi="$widgets/install/installer.py -header.fix.file";
alias h.fo="$widgets/install/installer.py -header.fix.folder";
alias h.fo.r="$widgets/install/installer.py -header.fix.folder.r";


alias t="$widgets/install/installer.py ";
alias s.t="sudo $widgets/install/installer.py ";
alias tool="$widgets/install/installer.py ";
alias s.tool="sudo $widgets/install/installer.py ";

alias t3="installer.py";
alias s.t3="sudo installer.py";

alias t2="installer.py2";
alias s.t2="sudo installer.py2";
alias tool2="installer.py2";
alias s.tool2="sudo installer.py2";

alias t.sh="$HOME/.rt/tool.sh";
alias s.t.sh="sudo $HOME/.rt/tool.sh";
alias c="clear";
alias vps.new="ssh-keygen -f $HOME/.ssh/known_hosts -R 'vps.rightthumb.com';ssh-keygen -f $HOME/.ssh/known_hosts -R '45.35.203.103';";
alias vps2.new="ssh-keygen -f '/home/scott/.ssh/known_hosts' -R 'vps2.rightthumb.com';ssh-keygen -f '/home/scott/.ssh/known_hosts' -R '45.35.203.104';";




export HISTSIZE=100000
export HISTFILESIZE=100000



chmod 777 -R $HOME/.rt/

################# ################# ################# #################

source $HOME/.rt/profile/vars/config.sh
source $HOME/.rt/profile/vars/personal.sh

################# ################# ################# #################
alias get.t.sh="wget http://reph.us/tools/file.php?file=tool.sh -O $HOME/.rt/tool.sh";
alias get.t="wget http://reph.us/tools/file.php?file=tool -O installer.py; $PY $widgets/install/installer.py -h.f installer.py;";
alias get.t2="wget http://reph.us/tools/file.php?file=tool2 -O installer.py2; $PY installer.py2 -h.f installer.py2;";
alias get.h="wget http://reph.us/tools/file.php?file=help.txt -O $HOME/.rt/help.txt; $PY installer.py2 -h.f $HOME/.rt/help.txt;";



alias s.p="sudo $widgets/widgets/bash/nav/p.sh"
alias s.pp="sudo $widgets/widgets/bash/nav/pp.sh"
alias p.sudo="sudo $widgets/widgets/bash/nav/p.sh"
alias pp.sudo="sudo $widgets/widgets/bash/nav/pp.sh"
alias p="$widgets/widgets/bash/nav/p.sh"
alias pp="$widgets/widgets/bash/nav/pp.sh"
alias b="$widgets/widgets/bash/nav/b.sh"
alias bb="$widgets/widgets/bash/nav/bb.sh"
alias m="$widgets/widgets/bash/nav/m.sh"
alias d="$widgets/widgets/bash/nav/d.sh"
alias bs="$widgets/widgets/bash/nav/bs.sh"

alias n="$widgets/widgets/bash/nav/n.sh"
alias e="$widgets/widgets/bash/nav/e.sh"
alias epy="$widgets/widgets/bash/nav/epy.sh"
alias epyi="$widgets/widgets/bash/nav/epyi.sh"

alias s.n="sudo $widgets/widgets/bash/nav/n.sh"
alias s.e="sudo $widgets/widgets/bash/nav/e.sh"
alias s.epy="sudo $widgets/widgets/bash/nav/epy.sh"
alias s.epyi="sudo $widgets/widgets/bash/nav/epyi.sh"


alias x="$widgets/widgets/bash/nav/x.sh"

alias bashFix="chmod 777 $widgets/widgets/bash/*.sh"

alias dirx="$widgets/widgets/bash/nav/dirX.sh"

alias p0="$widgets/widgets/bash/nav/p0.sh"
alias pu="$widgets/widgets/bash/nav/p0.sh"
alias p00="$widgets/widgets/bash/nav/p00.sh"
alias pw="$widgets/widgets/bash/nav/p00.sh"
alias v="$widgets/widgets/bash/nav/v.sh"


alias c="$widgets/widgets/bash/nav/c.sh"
alias epyiBuild="$widgets/widgets/bash/nav/epyiBuild.sh"
alias hack="$widgets/widgets/bash/hack.sh"
alias newpage="$widgets/widgets/bash/newpage.sh"



export stmp="$wprofile/temp"
export tmpf0="$wprofile/temp/{B820137A-79B8-45E3-BCBD-A6CAC50892D0}"
export tmpf1="$wprofile/temp/{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}"
export tmpf2="$wprofile/temp/{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}"
export tmpf3="$wprofile/temp/{F139D191-FA1A-44D5-855C-7E5141B30E0D}"
export tmpf4="$wprofile/temp/{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}"
export tmpf5="$wprofile/temp/{201D82D6-2DC0-4552-A598-54F5481399A1}"
export tmpf6="$wprofile/temp/{26B3B9C6-0A59-432A-9386-D432B53001CB}"
export tmpf7="$wprofile/temp/{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}"
export tmpf8="$wprofile/temp/{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}"
export tmpf9="$wprofile/temp/{DF1D4EBC-838E-419C-9C58-943C1767391A}"




config="$wprofile/config"
unixID="$config/.unix_id"



if [ ! -e $config ]; then
		echo "0 no config"
		mkdir $config;
else

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

if [ ! -e $unixID ]; then
		touch $unixID
fi

alias vnc.toggle="$widgets/widgets/bash/nav/p.sh toggle_comment -f /etc/vnc.conf -label vnc"
alias vnc.off='vncserver-stop'
alias vnc.on="$widgets/widgets/bash/dt/vnc-on.sh"

alias fix="chmod -R 777 $widgets"
alias fixme="sudo chmod -R 777 $widgets"
alias sudofix="sudo chmod -R 777 $widgets"
alias fixme.root="sudo chmod -R 777 $widgets"
alias fixme.sudo="sudo chmod -R 777 $widgets"
alias fixme.su="sudo chmod -R 777 $widgets"
alias s.fixme="sudo chmod -R 777 $widgets"

alias register_terminal="$widgets/widgets/bash/register_terminal.sh"

notes_folder="$widgets/widgets/bash/notes"
notes_file="$notes_folder/RT-SCRAP-$unixID7.txt"

alias cat.scrap="cat $notes_file"


alias scrap="$widgets/widgets/bash/scrap.sh"
alias notes="$widgets/widgets/bash/scrap.sh"
alias ent='p imdb -ent '
alias ee='p imdb -live -case -ep -ent '

alias uuid.m='p genuuid -strip -short'
alias uuid.mini='p genuuid -strip -short'
alias uuid.s='p genuuid -strip'
alias uuid='p genuuid'
alias uuids='p genuuid -cnt 10'
alias n.rc='n ~/.bashrc'

export p="bash $widgets/widgets/bash/nav/p.sh"
export config
export widgets

alias ls.g="p ls -c g s n -s g -g g";
alias ls.d='p ls -ago 2d -c ago name -g ago -sort md'
alias ls.='p ls -c ago name -g ago -sort md -ago '

alias cloud='p cloud -sync'

alias ls.p='p ls -s md -g ago --c -nocolor -c path'
alias a.cp='p copyTool'
alias scrap.seg='echo  "_________________ _________________ _________________ _________________"'
alias scrap.seg2='echo "################# ################# ################# #################"'

alias cdf="$widgets/widgets/bash/cdf.sh"
alias copy="xsel --clipboard --input"
alias paste="xsel --clipboard --output"
alias cloud.fix="sudo $widgets/widgets/bash/nav/p.sh cloud -sync"
alias cloud.fix.dl="sudo $widgets/widgets/bash/nav/p.sh cloud -sync -download"
alias cloud.sync.dl="$widgets/widgets/bash/nav/p.sh cloud -sync -download"
alias cloud.sync="$widgets/widgets/bash/nav/p.sh cloud -sync"
alias c.s="sudo $widgets/widgets/bash/nav/p.sh cloud -sync"
alias c.s.dl="sudo $widgets/widgets/bash/nav/p.sh cloud -sync -download"
alias c.s.="$widgets/widgets/bash/nav/p.sh cloud -sync"
alias c.s.dl.="$widgets/widgets/bash/nav/p.sh cloud -sync -download"


alias py="python3"


export HISTSIZE=100000
export HISTFILESIZE=100000


alias up.date="echo "update"; sudo apt-get update; echo "upgrade"; sudo apt-get upgrade;"

alias bbb="p hasAlias"
alias app="p searchAppRegistrationInfo"

alias tool="installer.py"
alias tool.sh="$HOME/.rt/tool.sh"
alias s.tool="sudo installer.py"
alias s.tool.sh="sudo $HOME/.rt/tool.sh"
alias load.fix="$widgets/install/installer.py -sh.file $widgets/widgets/bash/load-vars.sh"

alias listening2="lsof -i -P -n | grep LISTEN"
alias listening="netstat -l | p simpleLine + listen - listening"
alias fw.y="sudo ufw allow "
alias fw.n="sudo ufw deny "

alias watch.vnc="$widgets/widgets/bash/vnc_watch.sh> /dev/null 2>&1 & "



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
		prompt_color='\[\]'
		info_color='\[\]'
		if [ "$EUID" -eq 0 ]; then # Change prompt colors for root user
		prompt_color='\[\]'
		info_color='\[\]'
		fi
		PS1=$prompt_color'┌──${debian_chroot:+($debian_chroot)──}('$info_color'\u${prompt_symbol}\h'$prompt_color')-[\[\]\w'$prompt_color'].3.def
'$prompt_color'└─'$info_color'\$\[\] '
else
		PS1='┌── (\u${prompt_symbol}\h)──[\w].3.def\n└─── $ '
fi
unset color_prompt force_color_prompt


alias k="$widgets/widgets/python/keychain.py -rc ";
alias pc="$widgets/widgets/python/pc.py -rc ";


## {AEC80B4D3338} ##