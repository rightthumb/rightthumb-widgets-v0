# mount webdav

~~~sh
sudo apt-get install davfs2
sudo mkdir -p /mnt/webdav
sudo mount -t davfs https://server.com/webdav/ /mnt/webdav
~~~

~~~sh
sudo umount /mnt/webdav
~~~
