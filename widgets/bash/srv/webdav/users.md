# webdav users

## add

~~~sh
htpasswd -c /etc/apache2/webdav.users username
systemctl restart apache2
~~~

## delete user

~~~sh
htpasswd -D /etc/apache2/webdav.users username
systemctl restart apache2
~~~

## reset password

~~~sh
htpasswd -b /etc/apache2/webdav.users username password
systemctl restart apache2
~~~

[setup](https://chat.openai.com/c/8de05e26-e5e3-4363-9d03-dd4186b30580)
