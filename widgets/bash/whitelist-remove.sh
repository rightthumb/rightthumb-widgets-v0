#!/bin/bash

ip=$1;

if which csf >/dev/null; then
  csf -a $ip;
  echo "csf -a $ip"
  ufw reload
fi

if which iptables >/dev/null; then
  iptables -I INPUT -s $ip -p tcp --dport 22 -j ACCEPT;
  echo "iptables -I INPUT -s $ip -p tcp --dport 22 -j ACCEPT;"
fi

if [ -d "/etc/virtual/" ]; then
  _fi1=(
	"/etc/virtual/whitelist_domains"
	"/etc/virtual/whitelist_from"
	"/etc/virtual/whitelist_hosts_ip"
	"/etc/virtual/whitelist_hosts"
	"/etc/virtual/whitelist_senders"
  )
  for fi1 in "${_fi1[@]}"; do
	echo $ip >> ${fi1}
	echo "echo $ip >> ${fi1}"
  done
fi

_fi2=(
  "/etc/hosts.allow"
)
for fi2 in "${_fi2[@]}"; do
  if [ -f "${fi2}" ]; then
	echo "ALL: $ip" | sudo tee -a ${fi2}
	echo "echo 'ALL: $ip' | sudo tee -a ${fi2}"
  fi
done

if [ -d "/usr/local/directadmin/data/admin/" ]; then
  _fi3=(
	"/usr/local/directadmin/data/admin/ip_whitelist"
  )
  for fi3 in "${_fi3[@]}"; do
	echo $ip >> ${fi3}
  done
fi