#!/bin/bash
#

echo "Enter Kubernetes master IP:"
read IP_MASTER
echo "Enter Kubernetes node IP:"
read IP_MINION

#disable firewall centos 7
systemctl stop firewalld
systemctl disable firewalld

# Install NTP and make sure it is enabled and running:
yum -y install ntp
systemctl start ntpd
systemctl enable ntpd

# Install flannel and Kubernetes using yum:
yum -y install flannel kubernetes

# Configure etcd server for flannel service
sed -i "s/FLANNEL_ETCD=\"http:\/\/127.0.0.1:2379\"/FLANNEL_ETCD=\"http:\/\/$IP_MASTER:2379\"/g" /etc/sysconfig/flanneld

# Configure Kubernetes connect to Kubernetes master API
sed -i "s/KUBE_MASTER=\"--master=http:\/\/127.0.0.1:8080\"/KUBE_MASTER=\"--master=http:\/\/$IP_MASTER:8080\"/g" /etc/kubernetes/config

# Configure kubelet service
sed -i 's/KUBELET_ADDRESS=\"--address=127.0.0.1\"/KUBELET_ADDRESS=\"--address=0.0.0.0\"/g' /etc/kubernetes/kubelet
sed -i 's/# KUBELET_PORT=/KUBELET_PORT=/g' /etc/kubernetes/kubelet
sed -i "s/KUBELET_HOSTNAME=\"--hostname-override=127.0.0.1\"/KUBELET_HOSTNAME=\"--hostname_override=$IP_MINION\"/g" /etc/kubernetes/kubelet
sed -i "s/KUBELET_API_SERVER=\"--api-servers=http:\/\/127.0.0.1:8080\"/KUBELET_API_SERVER=\"--api_servers=http:\/\/$IP_MASTER:8080\"/g" /etc/kubernetes/kubelet

# Start and enable kube-proxy, kubelet, docker and flanneld services
for SERVICES in kube-proxy kubelet docker flanneld; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES 
done
