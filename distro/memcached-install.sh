#!/bin/bash
yum install -y memcached
chkconfig memcached on
service memcached start
#php 5.6
yum --enablerepo=remi,remi-php56 install -y php-pecl-memcached php-pecl-memcache

service php-fpm restart
service nginx restart
#fw
# memcached -d -p 11943 -u memcached -m 2048 -c 2048
iptables -A INPUT -m state --state NEW -m tcp -p tcp --dport 11211 -j ACCEPT
service iptables save
service iptables restart