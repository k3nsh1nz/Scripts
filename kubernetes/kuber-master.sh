#!/bin/bash
# author __k__

#disable firewall centos 7
systemctl stop firewalld
systemctl disable firewalld

# Install NTP and make sure it is enabled and running:
yum -y install ntp
systemctl start ntpd
systemctl enable ntpd

#Install etcd and Kubernetes through yum:
yum -y install etcd kubernetes

# Configure etcd listen all IP
sed -i 's/ETCD_LISTEN_CLIENT_URLS=\"http:\/\/localhost:2379\"/ETCD_LISTEN_CLIENT_URLS=\"http:\/\/0.0.0.0:2379\"/g' /etc/etcd/etcd.conf
 
# Configure Kubernetes API server
sed -i 's/KUBE_API_ADDRESS=\"--insecure-bind-address=127.0.0.1\"/KUBE_API_ADDRESS=\"--address=0.0.0.0\"/g' /etc/kubernetes/apiserver
sed -i 's/# KUBELET_PORT/KUBELET_PORT/g' /etc/kubernetes/apiserver
sed -i 's/# KUBE_API_PORT/KUBE_API_PORT/g' /etc/kubernetes/apiserver
# KUBE_ADMISSION_CONTROL="--admission_control=NamespaceLifecycle,NamespaceExists,LimitRanger,SecurityContextDeny,ResourceQuota"

# Start and enable etcd, kube-apiserver, kube-controller-manager and kube-scheduler
for SERVICES in etcd kube-apiserver kube-controller-manager kube-scheduler; do
    systemctl restart $SERVICES
    systemctl enable $SERVICES
    systemctl status $SERVICES 
done

#Define flannel network configuration in etcd
etcdctl mk /atomic.io/network/config '{"Network":"172.17.0.0/16"}'
