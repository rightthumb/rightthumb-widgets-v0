#!/bin/bash

# The IP address to be blocked
ip=$1;

# Block the IP with CSF (ConfigServer Security & Firewall) if installed
if which csf >/dev/null; then
  csf -d $ip;
  echo "csf -d $ip"
  ufw reload
fi

# Block the IP using iptables
if which firewall-cmd >/dev/null; then
  firewall-cmd --permanent --add-rich-rule="rule family=ipv4 destination address=$ip reject"
  firewall-cmd --reload
  echo "firewall-cmd --permanent --add-rich-rule=\"rule family=ipv4 destination address=$ip reject\""
else
  if which apt >/dev/null; then
	sudo apt update
	sudo apt install firewalld -y
  fi
  if which dnf >/dev/null; then
	sudo dnf install firewalld -y
  fi
  if which zypper >/dev/null; then
	sudo zypper install firewalld -y
  fi
  if which yum >/dev/null; then
	sudo yum install firewalld -y
  fi
  if which pacman >/dev/null; then
	sudo pacman -Syu firewalld --noconfirm
  fi
  if which apk >/dev/null; then
	sudo apk add firewalld
  fi
  sudo systemctl enable firewalld
  sudo systemctl start firewalld
  sudo systemctl status firewalld
  sudo firewall-cmd --permanent --add-service=ssh
  sudo firewall-cmd --reload

fi

if which firewall-cmd >/dev/null; then
  firewall-cmd --permanent --add-rich-rule="rule family=ipv4 destination address=$ip reject"
  firewall-cmd --reload
  echo "firewall-cmd --permanent --add-rich-rule=\"rule family=ipv4 destination address=$ip reject\""
fi

if which iptables >/dev/null; then
  iptables -I INPUT -s $ip -p tcp --dport 22 -j DROP;
  echo "iptables -I INPUT -s $ip -p tcp --dport 22 -j DROP"
fi

# Block the IP in various configuration files if the /etc/virtual/ directory exists
if [ -d "/etc/virtual/" ]; then
  _fi1=(
	"/etc/virtual/blacklist_domains"
	"/etc/virtual/blacklist_from"
	"/etc/virtual/blacklist_hosts_ip"
	"/etc/virtual/blacklist_hosts"
	"/etc/virtual/blacklist_senders"
  )
  for fi1 in "${_fi1[@]}"; do
	echo $ip >> ${fi1}
	echo "echo $ip >> ${fi1}"
  done
fi

# Block the IP in /etc/hosts.deny if the file exists
_fi2=(
  "/etc/hosts.deny"
)
for fi2 in "${_fi2[@]}"; do
  if [ -f "${fi2}" ]; then
	echo "ALL: $ip" | sudo tee -a ${fi2}
	echo "echo 'ALL: $ip' | sudo tee -a ${fi2}"
  fi
done

# Block the IP in DirectAdmin IP blacklist if the directory exists
if [ -d "/usr/local/directadmin/data/admin/" ]; then
  _fi3=(
	"/usr/local/directadmin/data/admin/ip_blacklist"
  )
  for fi3 in "${_fi3[@]}"; do
	echo $ip >> ${fi3}
  done
fi

echo "Blocking $ip completed."