#!/bin/bash

# The IP address to be unblocked
ip=$1;

# Unblock the IP with CSF (ConfigServer Security & Firewall) if installed
if which csf >/dev/null; then
  csf -dr $ip;
  echo "csf -dr $ip"
  ufw reload
fi

# Unblock the IP using iptables
if which iptables >/dev/null; then
  iptables -D INPUT -s $ip -p tcp --dport 22 -j DROP;
  echo "iptables -D INPUT -s $ip -p tcp --dport 22 -j DROP"
fi

# Unblock the IP in various configuration files if the /etc/virtual/ directory exists
if [ -d "/etc/virtual/" ]; then
  _fi1=(
	"/etc/virtual/blacklist_domains"
	"/etc/virtual/blacklist_from"
	"/etc/virtual/blacklist_hosts_ip"
	"/etc/virtual/blacklist_hosts"
	"/etc/virtual/blacklist_senders"
  )
  for fi1 in "${_fi1[@]}"; do
	sed -i "/$ip/d" ${fi1}
	echo "sed -i '/$ip/d' ${fi1}"
  done
fi

# Unblock the IP in /etc/hosts.deny if the file exists
_fi2=(
  "/etc/hosts.deny"
)
for fi2 in "${_fi2[@]}"; do
  if [ -f "${fi2}" ]; then
	sudo sed -i "/ALL: $ip/d" ${fi2}
	echo "sudo sed -i '/ALL: $ip/d' ${fi2}"
  fi
done

# Unblock the IP in DirectAdmin IP blacklist if the directory exists
if [ -d "/usr/local/directadmin/data/admin/" ]; then
  _fi3=(
	"/usr/local/directadmin/data/admin/ip_blacklist"
  )
  for fi3 in "${_fi3[@]}"; do
	sed -i "/$ip/d" ${fi3}
	echo "sed -i '/$ip/d' ${fi3}"
  done
fi

echo "Unblocking $ip completed."