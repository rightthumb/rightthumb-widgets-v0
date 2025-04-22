# mount webdav

~~~sh
sudo apt-get install davfs2
sudo mkdir -p /mnt/batuu
sudo mount -t davfs https://server.com/webdav/ /mnt/webdav
~~~

~~~sh
sudo umount /mnt/batuu
~~~

$ww/widgets/bash/srv/webdav/vps-auto_login.sh
