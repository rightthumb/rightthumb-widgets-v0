# open vpn password notes

___

## notes

~~~sh
nano /etc/openvpn/server.conf
nano /etc/openvpn/psw-file
cat /etc/openvpn/psw-file
cat /opt/client_head.ovpn
nano /etc/openvpn/check_user.sh

sudo /usr/sbin/openvpn --config /etc/openvpn/server.conf

sudo systemctl status openvpn@server.service
sudo systemctl restart openvpn@server.service
sudo systemctl start openvpn@server.service
sudo systemctl stop openvpn@server.service

cat /opt/client_head.ovpn

~~~
