Install with Firewalld Enabled
#######==

By default, the installer requires that Firewalld is disabled before
continuing. If you need to leave Firewalld enabled you can add a flag
(under the firewalldConfig spec) to the installer-override.yaml patch
file `spec:` section.

For example:

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: firewalldConfig: bypassFirewalldWarning: true

Configuring Firewalld
##########-

The required ports for cluster node communication need to be open in the
Firewalld config on each node in the cluster. For more information see
`System Requirements for an Embedded Cluster
Install <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Here is an example script for configuring Firewalld in CentOS 7/RHEL 7
environments:

#!/bin/bash echo 'net.ipv4.ip_forward = 1' \| tee -a /etc/sysctl.conf;
sysctl -p; firewall-cmd --permanent --zone=external --add-masquerade;
firewall-cmd --permanent --zone=trusted --add-interface=cni0; # SSH Port
firewall-cmd --permanent --zone=public --add-rich-rule=' rule
family="ipv4" port protocol="tcp" port="22" accept'; # HTTP Port
(optional - used to redirect to HTTPS) firewall-cmd --permanent
--zone=public --add-rich-rule=' rule family="ipv4" port protocol="tcp"
port="80" accept'; # HTTPS Port firewall-cmd --permanent --zone=public
--add-rich-rule=' rule family="ipv4" port protocol="tcp" port="443"
accept'; # Kubernetes etcd Port firewall-cmd --permanent --zone=public
--add-rich-rule=' rule family="ipv4" port protocol="tcp"
port="2379-2380" accept'; # Kubernetes API Port firewall-cmd --permanent
--zone=public --add-rich-rule=' rule family="ipv4" port protocol="tcp"
port="6443" accept'; # Flannel VXLAN Port firewall-cmd --permanent
--zone=public --add-rich-rule=' rule family="ipv4" port protocol="udp"
port="8472" accept'; # KOTS UI Port firewall-cmd --permanent
--zone=public --add-rich-rule=' rule family="ipv4" port protocol="tcp"
port="8800" accept'; # Kubernetes Component (kubelet, kube-scheduler,
kube-controller) Ports firewall-cmd --permanent --zone=public
--add-rich-rule=' rule family="ipv4" port protocol="tcp"
port="10250-10252" accept'; firewall-cmd --reload

If you wish to open additional ports after the Swimlane deployment (e.g.
Syslog Receiver, External Mongo ports) see below:

`kubectl get svc -o wide`

NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE SELECTOR kotsadm ClusterIP
10.96.3.36 <none> 3000/TCP 3d app=kotsadm kotsadm-postgres ClusterIP
10.96.3.188 <none> 5432/TCP 3d app=kotsadm-postgres kubernetes ClusterIP
10.96.0.1 <none> 443/TCP 3d1h <none> kurl-proxy-kotsadm NodePort
10.96.1.64 <none> 8800:8800/TCP 3d app=kurl-proxy-kotsadm sw-api
ClusterIP 10.96.2.47 <none> 5000/TCP 3d service=swimlane-api sw-web
ClusterIP 10.96.2.67 <none> 443/TCP 3d service=swimlane-web
swimlane-chrome ClusterIP 10.96.3.32 <none> 4444/TCP 3d
service=swimlane-chrome swimlane-sw-mongo ClusterIP None <none>
27017/TCP 3d app=sw-mongo,release=swimlane swimlane-sw-mongo-0-external
NodePort 10.96.0.224 <none> 27017:35246/TCP 3d
statefulset.kubernetes.io/pod-name=swimlane-sw-mongo-0
swimlane-sw-mongo-1-external NodePort 10.96.1.229 <none> 27017:6239/TCP
3d statefulset.kubernetes.io/pod-name=swimlane-sw-mongo-1
swimlane-sw-mongo-2-external NodePort 10.96.0.104 <none> 27017:36278/TCP
3d statefulset.kubernetes.io/pod-name=swimlane-sw-mongo-2
swimlane-syslog-receiver NodePort 10.96.2.119 <none> 514:42750/UDP 3d
service=swimlane-syslog-receiver

The ports from the example output above will be different for every
deployment. Run these commands to create firewall exceptions:

TCP ports 35246, 6239, 36278 have been assigned to our MongoDB service
for external access:

sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule
family="ipv4" port protocol="tcp" port="35246" accept' sudo firewall-cmd
--permanent --zone=public --add-rich-rule='rule family="ipv4" port
protocol="tcp" port="6239" accept' sudo firewall-cmd --permanent
--zone=public --add-rich-rule='rule family="ipv4" port protocol="tcp"
port="36278" accept'

UDP port 42750 has been assigned to our Swimlane Syslog Receiver
service:

sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule
family="ipv4" port protocol="udp" port="42750" accept'

Restart firewalld:

sudo firewall-cmd --reload

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
