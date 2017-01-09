#!/bin/bash
yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel xinetd
useradd -u 1029 nagios
cd /usr/src
wget https://www.nagios-plugins.org/download/nagios-plugins-1.5.tar.gz
tar -xvf nagios-plugins-1.5.tar.gz
cd nagios-plugins-1.5
./configure
make
make install
chown nagios.nagios /usr/local/nagios
chown -R nagios.nagios /usr/local/nagios/libexec
cd /usr/src
wget http://liquidtelecom.dl.sourceforge.net/project/nagios/nrpe-2.x/nrpe-2.15/nrpe-2.15.tar.gz
tar -xzf nrpe-2.15.tar.gz
cd nrpe-2.15
./configure
make all
make install-plugin
make install-daemon
make install-daemon-config
make install-xinetd
echo "nrpe            5666/tcp                 NRPE" >> /etc/services
sed -i 's/127.0.0.1/172.16.2.232/g' /etc/xinetd.d/nrpe
service xinetd restart
echo "command[check_docker]=/usr/local/nagios/libexec/check_procs -c 1:50 -C dockerd" >> /usr/local/nagios/etc/nrpe.cfg
