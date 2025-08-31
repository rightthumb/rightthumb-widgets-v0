# dns notes

___

## folders

- `/var/named`
- `/etc/bind/zones/`

___

## /etc/bind/named.conf.local

~~~conf
zone "example.com" {
    type master;
    file "/etc/bind/zones/db.example.com"; # zone file path
};
zone "anotherdomain.com" {
    type master;
    file "/etc/bind/zones/db.anotherdomain.com"; # zone file path
};

~~~

___

## /etc/bind/zones/

~~~zones
$TTL    604800
@       IN      SOA     ns1.example.com. admin.example.com. (
                                   3         ; Serial
                              604800         ; Refresh
                               86400         ; Retry
                             2419200         ; Expire
                              604800 )       ; Negative Cache TTL
; Name servers
@       IN      NS      ns1.example.com.
@       IN      NS      ns2.example.com.

; A records for name servers
ns1     IN      A       192.0.2.1
ns2     IN      A       192.0.2.2

; A record for domain
@       IN      A       198.51.100.1
www     IN      A       198.51.100.1
~~~
