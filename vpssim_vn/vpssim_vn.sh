#!/bin/sh
if [ $(id -u) != "0" ]; then
    printf "Co loi: Ban phai dang nhap bang user root!\n"
    exit
fi
if [ -f /var/cpanel/cpanel.config ]; then
echo "Server cua ban da cai san WHM/Cpanel, neu ban muon dung VPSSIM"
echo "Hay cai moi lai he dieu hanh, khuyen dung centos6 - 64bit"
echo "Chao tam biet !"
exit
fi

if [ -f /etc/psa/.psa.shadow ]; then
echo "Server cua ban da cai san Plesk, neu ban muon dung VPSSIM"
echo "Hay cai moi lai he dieu hanh, khuyen dung centos6 - 64bit"
echo "Chao tam biet !"
exit
fi

if [ -f /etc/init.d/directadmin ]; then
echo "Server cua ban da cai san DirectAdmin, neu ban muon dung VPSSIM"
echo "Hay cai moi lai he dieu hanh, khuyen dung centos6 - 64bit"
echo "Chao tam biet !"
exit
fi

if [ -f /etc/init.d/webmin ]; then
echo "Server cua ban da cai san webmin, neu ban muon dung VPSSIM"
echo "Hay cai moi lai he dieu hanh, khuyen dung centos6 - 64bit"
echo "Chao tam biet !"
exit
fi

if [ -f /home/vpssim.conf ]; then
clear
echo "========================================================================="
echo "========================================================================="
echo "Server/VPS cua ban da cai san VPSSIM"
echo "Hay su dung lenh vpssim de truy cap VPSSIM menu"
echo "Chao tam biet !"
echo "========================================================================="
echo "========================================================================="
rm -rf install*
exit
fi

if [ -f /etc/yum.repos.d/epel.repo ]; then
sudo sed -i "s/mirrorlist=https/mirrorlist=http/" /etc/yum.repos.d/epel.repo
fi
wget -q http://vpssim.com/script/vpssim/calc -O /bin/calc && chmod +x /bin/calc
yum -y install psmisc bc gawk gcc
yum -y -q install virt-what unzip sudo net-tools iproute iproute2 curl deltarpm yum-utils
clear 
rm -rf /root/vpssim-setup 
wget -q https://hostingaz.vn/script/vpssim/centos$(rpm -q --qf "%{VERSION}" $(rpm -q --whatprovides redhat-release))/vpssim-setup && chmod +x vpssim-setup && clear && ./vpssim-setup

 
