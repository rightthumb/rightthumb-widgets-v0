#!/bin/bash
################# ################# ################# #################
Md5() {
	local input

	if [[ -n "$1" ]]; then
		input="$1"
	else
		echo -n " > "
		read -s input
		echo
	fi

	if command -v md5sum >/dev/null 2>&1; then
		printf "%s" "$input" | md5sum | awk '{print $1}'
	elif command -v md5 >/dev/null 2>&1; then
		printf "%s" "$input" | md5 | awk '{print $NF}'
	else
		echo "No md5sum or md5 command found"
		return 1
	fi
}
################# ################# ################# #################
alias get.t.sh="wget http://reph.us/tools/file.php?file=tool.sh -O $HOME/.rt/tool.sh";
alias get.t="wget http://reph.us/tools/file.php?file=tool -O installer.py; $PY $widgets/install/installer.py -h.f installer.py;";
alias get.t2="wget http://reph.us/tools/file.php?file=tool2 -O installer.py2; $PY installer.py2 -h.f installer.py2;";
alias get.h="wget http://reph.us/tools/file.php?file=help.txt -O $HOME/.rt/help.txt; $PY installer.py2 -h.f $HOME/.rt/help.txt;";

op() {
	if [ -z "$1" ]; then
		echo "❌ Usage: run_py_app <app_name> [args...]"
		return 1
	fi

	app="$1"
	shift
	python3.11 "/opt/rightthumb-widgets-v0/widgets/python/${app}.py" "$@"
}


alias s.p="sudo $widgets/widgets/bash/nav/p.sh"
alias s.pp="sudo $widgets/widgets/bash/nav/pp.sh"
alias p.sudo="sudo $widgets/widgets/bash/nav/p.sh"
alias pp.sudo="sudo $widgets/widgets/bash/nav/pp.sh"
# alias p="$widgets/widgets/bash/nav/p.sh"
function p() {
	source "$widgets/widgets/bash/nav/p.sh"
}

# alias pp="$widgets/widgets/bash/nav/pp.sh"
alias b="$widgets/widgets/bash/nav/b.sh"
alias bb="$widgets/widgets/bash/nav/bb.sh"
alias m="$widgets/widgets/bash/nav/m.sh"
alias d="$widgets/widgets/bash/nav/d.sh"
alias bs="$widgets/widgets/bash/nav/bs.sh"

alias n="$widgets/widgets/bash/nav/n.sh"
# alias e="$widgets/widgets/bash/nav/e.sh"
alias epy="$widgets/widgets/bash/nav/epy.sh"
alias epyi="$widgets/widgets/bash/nav/epyi.sh"

alias s.n="sudo $widgets/widgets/bash/nav/n.sh"
alias s.e="sudo $widgets/widgets/bash/nav/e.sh"
alias s.epy="sudo $widgets/widgets/bash/nav/epy.sh"
alias s.epyi="sudo $widgets/widgets/bash/nav/epyi.sh"

alias .d="$widgets/widgets/bash/nav/day.sh"
alias .day="$widgets/widgets/bash/nav/day.sh"


alias x="$widgets/widgets/bash/nav/x.sh"

alias bashFix="chmod 777 $widgets/widgets/bash/*.sh"

alias dirx="$widgets/widgets/bash/nav/dirX.sh"

alias p0="$widgets/widgets/bash/nav/p0.sh"
alias pu="$widgets/widgets/bash/nav/p0.sh"
alias p00="$widgets/widgets/bash/nav/p00.sh"
alias pw="$widgets/widgets/bash/nav/p00.sh"


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

alias cat.scrap="$p cat -f $notes_file"


alias scrap="$widgets/widgets/bash/scrap.sh"
alias notes="$widgets/widgets/bash/scrap.sh"
alias ent='python3 $ww/python/imdb.py -ent '
alias ee='python3 $ww/python/imdb.py -live -case -ep -ent '

alias uuid.m='python3 $ww/python/genuuid -strip -short'
alias uuid.mini='python3 $ww/python/genuuid -strip -short'
alias uuid.s='python3 $ww/python/genuuid -strip'
alias uuid='python3 $ww/python/genuuid.py'
alias uuids='python3 $ww/python/genuuid -cnt 10'
alias n.rc='n ~/.bashrc'

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



alias py="$widgets/widgets/bash/py.sh"
alias up.date='echo "update"; sudo apt-get update -y; echo "upgrade"; sudo apt-get upgrade -y;'

alias bbb='python3 $ww/python/hasAlias.py'
alias app='python3 $ww/python/searchAppRegistrationInfo.py'

alias tool="installer.py"
alias tool.sh="$HOME/.rt/tool.sh"
alias s.tool="sudo installer.py"
alias s.tool.sh="sudo $HOME/.rt/tool.sh"
alias load.fix="$widgets/install/installer.py -sh.file $widgets/widgets/bash/load-vars.sh"

alias listening2="lsof -i -P -n | grep LISTEN"
alias listening="netstat -l | p simpleLine + listen - listening"
alias fw.y="sudo ufw allow "
alias fw.n="sudo ufw deny "



alias .py-pip="$widgets/bash/quick-setup.sh";

alias ssh...="rm -rf ~/.ssh; ssh-keygen -t rsa"
alias .ssh.="ssh-keygen -t rsa"




alias grep.r="grep -R -l"

# alias cd/="cd /"
alias x.="exit"
alias cd..="cd .."
alias pi='ping -c 5'
alias fastping='ping -c 100 -s.2'
alias fping='ping -c 100 -s.2'
alias ports.='netstat -tulanp'
alias ports='ports. | grep 127.'
alias who.='grep $(curl ifconfig.me)'




#--> start#> git clone this project
alias .git="git clone https://github.com/rightthumb/rightthumb-widgets-v0"
# alias .git.="mkdir -p "/opt/__rightthumb-widgets-v0/"; rsync -av --include '*/' --include 'vps-*' --exclude '*' /opt/rightthumb-widgets-v0/ /opt/__rightthumb-widgets-v0/;cd /opt ; rm -rf rightthumb-widgets-v0 ; git clone https://github.com/rightthumb/rightthumb-widgets-v0 ; rsync -av ./__rightthumb-widgets-v0/* /opt/rightthumb-widgets-v0/; cd rightthumb-widgets-v0 ; chmod -R 777 . ; p shClean -folder . -r"




_git_restore() {
	local widgets="/opt/rightthumb-widgets-v0"
	local backup="/opt/__rightthumb-widgets-v0"

	echo "♻️  Restoring vps-* files from backup..."

	if [ ! -d "$backup" ]; then
		echo "❌ Backup folder not found: $backup"
		return 1
	fi

	if [ ! -d "$widgets" ]; then
		echo "⚠️  Target folder not found: $widgets — creating it..."
		mkdir -p "$widgets"
	fi

	rsync -av --include '*/' --include 'vps-*' --exclude '*' "$backup/" "$widgets/"

	echo "✅ Restore complete"
}





_git_() {
	local widgets="/opt/rightthumb-widgets-v0"
	local backup="/opt/__rightthumb-widgets-v0"

	echo "🔁 Starting .git. refresh..."

	# Create backup directory if it doesn't exist
	mkdir -p "$backup"

	# Backup from $widgets if it exists
	if [ -d "$widgets" ]; then
		echo "📦 Backing up vps-* files from $widgets"
		rsync -av --include '*/' --include 'vps-*' --exclude '*' "$widgets/" "$backup/"
	else
		echo "⚠️  Warning: $widgets does not exist. Skipping backup."
	fi

	# Clone fresh repo
	cd /opt || return 1
	echo "🌐 Cloning rightthumb-widgets-v0 from GitHub..."
	rm -rf "$widgets"
	git clone https://github.com/rightthumb/rightthumb-widgets-v0 "$widgets"

	# Restore backed up files if backup exists
	if [ -d "$backup" ]; then
		echo "♻️  Restoring files from backup $backup"
		rsync -av "$backup/" "$widgets/"
	fi

	# Fix permissions
	chmod -R 777 "$widgets"

	# Final cleanup
	cd "$widgets" || return 1
	# echo "🧹 Running p shClean -folder . -r"
	# p shClean -folder . -r

	echo "✅ .git. update complete"
}


alias .v.="_git_restore"
alias .git.="_git_"
alias Git="echo https://github.com/rightthumb/rightthumb-widgets-v0"

#-->   end#> git clone this project

alias pp.='python3 $ww/python/paths.py'
# alias pp='python3 $ww/python/paths.py -f '


alias mkdir.fi='python3 $ww/python/mkdir.py -files '
alias mkdir.fo='python3 $ww/python/mkdir.py -folders '
alias mkdir.='python3 $ww/python/mkdir.py'
alias f='python3 $ww/python/-file.py'


echo '' > $stmp/.gp
alias .gp=" pwd > $stmp/.gp ; cd $ww ; git reset --hard ; git pull ; sudo chmod 777 -R . ; python3 $ww/install/installer.py -rc.d h  ; cd $( cat $stmp/.gp )"


alias .u..='python3 $ww/python/site.py -mkdir -nopass -u -f '
alias .u.='python3 $ww/python/site.py  -nopass -u -f '


alias u..='python3 $ww/python/site.py -mkdir -u -f '
alias u.='python3 $ww/python/site.py -u -f'
alias d.='python3 $ww/python/site.py -d -f'

alias in.='cat ~/.bashrc > ~/.bashrc.bk ; echo "" > ~/.bashrc ; rm $widgets/install/installer.py ; wget https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/install/installer.py -O $widgets/install/installer.py ; chmod 777 $widgets/install/installer.py ; python3 $widgets/install/installer.py -rc.d h'
alias in.s='sudo cat ~/.bashrc > ~/.bashrc.bk ; echo "" > ~/.bashrc ; rm $widgets/install/installer.py ; wget https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/main/install/installer.py -O $widgets/install/installer.py ; chmod 777 $widgets/install/installer.py ; sudo python3 $widgets/install/installer.py -rc.d h'

alias ..b='cd /opt ; cd rightthumb-widgets-v0 ; m w ; cd install/ ; m in ; cd .. ; cd widgets/ ; m ww ; cd python/ ; m py ; cd .. ; cd bash/ ; m b ; m bash ; cd .. ; cd databank/ ; m db ; cd tables/ ; m ttt ; cd ; cd .rt ; m rt ; cd profile/ ; m h ; cd tables/ ; m tt ; cd .. ; cd config/ ; m config ; m c ; cd .. ; cd projects/ ; m pr ; cd'
alias ...b='cd rightthumb-widgets-v0 ; m w ; cd install/ ; m in ; cd .. ; cd widgets/ ; m ww ; cd python/ ; m py ; cd .. ; cd bash/ ; m b ; m bash ; cd .. ; cd databank/ ; m db ; cd tables/ ; m ttt ; cd ; cd .rt ; m rt ; cd profile/ ; m h ; cd tables/ ; m tt ; cd .. ; cd config/ ; m config ; m c ; cd .. ; cd projects/ ; m pr ; cd'

alias watch.vnc="$widgets/widgets/bash/vnc_watch.sh> /dev/null 2>&1 & "

alias bl='python3 $ww/python/blank-file -f '
alias wget.txt='wget -q -O - '
alias wgett='wget -q -O - '


alias rr='sudo su root'

alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'



alias wget.='wget -qO - '
alias curl.h='curl -s -D - -o '
alias curl.h.='curl -I -L '
alias curl.h..='curl -L -v -s -o /dev/null '

alias .h='nano ~/.bash_history'
alias .h.sh='nano ~/.bash_history'
alias .h.='nano ~/.python_history'
alias .h.py='nano ~/.python_history'
alias .b='nano ~/.bashrc'
alias ..h='$p cat -f ~/.bash_history'
alias ..h.sh='$p cat -f ~/.bash_history'
alias ..h.='$p cat -f ~/.python_history'
alias ..h.py='$p cat -f ~/.python_history'
alias cat..='$p cat -f ~/.bashrc'
alias cat..='$p cat -f ~/.bashrc'
alias .rc='$p cat -f ~/.bashrc'
alias ls='ls --color=auto'
alias ll='ls -la'

alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

alias sha1='openssl sha1'
alias hh='history'
alias h='$p cat -f ~/.bash_history'

alias now='date +"%T"'
alias nowtime=now
alias nowdate='date +"%Y-%m-%d"'




# Stop after sending count ECHO_REQUEST packets #
alias ping='ping -c 5'
# Do not wait interval 1 second, go fast #
alias fastping='ping -c 100 -s.2'

## shortcut  for iptables and pass it via sudo#
alias ipt='sudo /sbin/iptables'



# display all rules #
alias iptlist='sudo /sbin/iptables -L -n -v --line-numbers'
alias iptlistin='sudo /sbin/iptables -L INPUT -n -v --line-numbers'
alias iptlistout='sudo /sbin/iptables -L OUTPUT -n -v --line-numbers'
alias iptlistfw='sudo /sbin/iptables -L FORWARD -n -v --line-numbers'
alias firewall=iptlist



#################################
#             misc              #
alias l="$widgets/widgets/bash/l.sh"
#################################


# get web server headers #
alias header='curl -I'
 
# find out if remote server supports gzip / mod_deflate or not #
alias headerc='curl -I --compress'



# # do not delete / or prompt if deleting more than 3 files at a time #
# alias rm='rm -I --preserve-root'
 
# # confirmation #
# alias mv='mv -i'
# alias cp='cp -i'
# alias ln='ln -i'
 
# # Parenting changing perms on / #
# alias chown='chown --preserve-root'
# alias chmod='chmod --preserve-root'
# alias chgrp='chgrp --preserve-root'


## pass options to free ##
alias meminfo='free -m -l -t'
 
## get top process eating memory
alias psmem='ps auxf | sort -nr -k 4'
alias psmem10='ps auxf | sort -nr -k 4 | head -10'
 
## get top process eating cpu ##
alias pscpu='ps auxf | sort -nr -k 3'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
 
## Get server cpu info ##
alias cpuinfo='lscpu'
 
## older system use /proc/cpuinfo ##
##alias cpuinfo='less /proc/cpuinfo' ##
 
## get GPU ram on desktop / laptop##
alias gpumeminfo='grep -i --color memory /var/log/Xorg.0.log'

alias .6='cd ../../../../../..'
alias .5='cd ../../../../..'
alias .4='cd ../../../..'
alias .3='cd ../../..'
alias .2='cd ../..'
alias .1='cd ..'
alias ..='cd ..'

alias 2icon="$widgets/widgets/bash/tools/2icon.sh ";
alias 2ico="$widgets/widgets/bash/tools/2icon.sh ";

alias crypt="$ww/bash/crypt.sh"



alias rotate="$widgets/widgets/bash/rotate.sh"

alias linkFo="$widgets/widgets/bash/linkFo.sh"
alias fig="$widgets/widgets/bash/_figlet.sh"
alias _figlet="$widgets/widgets/bash/_figlet.sh"
alias cow="$widgets/widgets/bash/_cowsay.sh"
alias cows="$widgets/widgets/bash/_cowsay.sh"
alias figs="$widgets/widgets/bash/_figlet.sh"

alias cl="$p shClean -f"
alias loadBK="$widgets/widgets/bash/loadBK.sh"
alias exref="$p imdb -xref -ent"
alias text="$p vps-srv-7facG-twilio-send"
alias textme="$p vps-srv-7facG-twilio-send -to 8136901260 -body "

alias foSize='python3 $ww/python/folderSizeTotals.py'
alias z='python3 $ww/python/folderSizeTotals.py'
alias dl.mp3="youtube-dlc -x --audio-format mp3 "
alias dl.mp3.="sudo youtube-dlc -x --audio-format mp3 "
alias dl.vid="youtube-dlc -f best "
alias dl.vid.="sudo youtube-dlc -f best "
alias dl.video="youtube-dlc -f best "
alias dl.video.="sudo youtube-dlc -f best "
alias dl.mp4="youtube-dlc -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' "
alias dl.mp4.="sudo youtube-dlc -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]' "
alias yt.dl="sudo wget https://github.com/blackjack4494/yt-dlc/releases/latest/download/youtube-dlc -O /usr/local/bin/youtube-dlc ; sudo chmod a+rx /usr/local/bin/youtube-dlc"




xd5() {
	local input="$1"

	if [[ -z "$input" ]]; then
		echo -n "Enter: "

		# Custom star-printing password reader
		input=""
		while IFS= read -r -s -n1 char; do
			# Enter key ends input
			[[ $char == $'\0' || $char == $'\n' ]] && break
			# Backspace handling
			if [[ $char == $'\177' ]]; then
				if [ -n "$input" ]; then
					input="${input%?}"
					echo -ne "\b \b"
				fi
			else
				input+="$char"
				echo -n "*"
			fi
		done
		echo
	fi

	if [[ -f "$input" ]]; then
		# It's a file
		if command -v md5sum >/dev/null 2>&1; then
			export xd5=$(md5sum "$input" | awk '{print $1}')
		elif command -v md5 >/dev/null 2>&1; then
			export xd5=$(md5 -q "$input")
		else
			echo "No md5 tool found." >&2
			return 1
		fi
	else
		# It's a string
		if command -v md5sum >/dev/null 2>&1; then
			export xd5=$(echo -n "$input" | md5sum | awk '{print $1}')
		elif command -v md5 >/dev/null 2>&1; then
			export xd5=$(echo -n "$input" | md5 | awk '{print $NF}')
		else
			echo "No md5 tool found." >&2
			return 1
		fi
	fi
	alias vp="export vault_pin=$xd5"
}



alias url="$widgets/widgets/bash/url.sh"
alias u="$widgets/widgets/bash/url.sh"
alias uploadFolder="$widgets/widgets/bash/uploadFolder.sh"
alias uploadFo="$widgets/widgets/bash/uploadFolder.sh"
alias upFo="$widgets/widgets/bash/uploadFolder.sh"
alias uf="$widgets/widgets/bash/uploadFolder.sh"
alias loadBK="$widgets/widgets/bash/loadBK.sh"
alias foBackup="$widgets/widgets/bash/foBackup.sh"

alias fa="$p file-open  -backup -alias "
alias zip.="zip -9 -r "
alias zipp="zip -9 -r "
alias zzip="zip -9 -r "

alias vpn.="curl -sSL https://git.io/vpn | bash"



alias ai="$p vps-ai-sds -p"

alias size.fi="$p ls -f "
alias size.f="du -sh "
alias size.d="df -h"
alias sizeFo="du -sh "
alias sizeDrive="df -h"


alias ls.g='python3 $ww/python/ls.py -c g s n -s g -g g';
alias ls.d='python3 $ww/python/ls.py -ago 2d -c ago name -g ago -sort md'
alias ls.='python3 $ww/python/ls.py -c ago name -g ago -sort md -ago '

alias cloud='python3 $ww/python/cloud.py -sync'

alias ls.p=='python3 $ww/python/ls.py -s md -g ago --c -nocolor -c path'
alias a.cp=='python3 $ww/python/copyTool.py'
alias scrap.seg='echo  "_________________ _________________ _________________ _________________"'
alias scrap.seg2='echo "################# ################# ################# #################"'