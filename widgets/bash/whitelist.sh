#!/bin/bash

# ## {R2D2919B742E} ##
# ###########################################################################
# What if magic existed?
# What if a place existed where your every thought and dream come to life.
# There is only one catch: it has to be written down.
# Such a place exists, it is called programming.
#    - Scott Taylor Reph, RightThumb.com
# ###########################################################################
# ## {C3P0D40fAe8B} ##

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
declare -A _fi1
_fi1=()
_fi1[${#_fi1[@]}]=/etc/virtual/whitelist_domains
_fi1[${#_fi1[@]}]=/etc/virtual/whitelist_from
_fi1[${#_fi1[@]}]=/etc/virtual/whitelist_hosts_ip
_fi1[${#_fi1[@]}]=/etc/virtual/whitelist_hosts
_fi1[${#_fi1[@]}]=/etc/virtual/whitelist_senders
for _fi1_ in "${_fi1[@]}"; do
echo $ip>>  ${_fi1_}
echo "echo $ip>>  ${_fi1_}"
done
fi

declare -A _fi2
_fi2=()
_fi2[${#_fi2[@]}]=/etc/hosts.allow
_fi2[${#_fi2[@]}]=
for _fi2_ in "${_fi2[@]}"
do
if [ -f "${_fi2_}" ]; then
echo $ip>>  ${_fi2_}
echo "echo $ip>>  ${_fi2_}"
fi
done

if [ -d "/usr/local/directadmin/data/admin/" ]; then
declare -A _fi3
_fi3=()
_fi3[${#_fi3[@]}]=/usr/local/directadmin/data/admin/ip_whitelist
for _fi3_ in "${_fi3[@]}"; do
echo $ip>>  ${_fi3_}
done
fi
