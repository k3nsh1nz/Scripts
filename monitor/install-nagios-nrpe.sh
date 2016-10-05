#!/bin/bash
yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel
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
#echo "nrpe            5666/tcp                 NRPE" >> /etc/services
#service xinetd restart  
