# smb users

## add

~~~sh
sudo smbpasswd -a john
sudo systemctl restart smbd
~~~

## delete

~~~sh
sudo smbpasswd -x john
sudo systemctl restart smbd
~~~

## change password

~~~sh
sudo smbpasswd john
sudo systemctl restart smbd
~~~

## connection

~~~sh
smbclient //192.168.1.100/shared -U john
~~~
