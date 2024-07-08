Install with Firewalld Enabled
==============================

By default, the installer requires that Firewalld is disabled before
continuing. If you need to leave Firewalld enabled you can add a flag
(under the firewalldConfig spec) to the installer-override.yaml patch
file ``spec:`` section.

For example:

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: firewalldConfig: bypassFirewalldWarning: true

Configuring Firewalld
---------------------

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
External Mongo ports) see below:

``kubectl get svc -o wide``

NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE SELECTOR gotenberg
ClusterIP 10.96.3.132 <none> 3500/TCP 21m service=gotenberg kotsadm
ClusterIP 10.96.1.169 <none> 3000/TCP 153m app=kotsadm kotsadm-postgres
ClusterIP 10.96.1.58 <none> 5432/TCP 153m app=kotsadm-postgres
kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 157m <none>
kurl-proxy-kotsadm NodePort 10.96.1.20 <none> 8800:8800/TCP 153m
app=kurl-proxy-kotsadm mongo ClusterIP None <none> 27017/TCP 21m
app=mongo,release=turbine mongo-0-external NodePort 10.96.1.49 <none>
27017:24361/TCP 7m45s statefulset.kubernetes.io/pod-name=mongo-0
mongo-1-external NodePort 10.96.0.76 <none> 27017:24964/TCP 6m29s
statefulset.kubernetes.io/pod-name=mongo-1 mongo-2-external NodePort
10.96.1.75 <none> 27017:22626/TCP 6m29s
statefulset.kubernetes.io/pod-name=mongo-2 postgresql-pgpool ClusterIP
10.96.0.97 <none> 5432/TCP 21m
app.kubernetes.io/component=pgpool,app.kubernetes.io/instance=turbine,app.kubernetes.io/name=postgresql-ha
postgresql-postgresql ClusterIP 10.96.2.67 <none> 5432/TCP 21m
app.kubernetes.io/component=postgresql,app.kubernetes.io/instance=turbine,app.kubernetes.io/name=postgresql-ha
postgresql-postgresql-headless ClusterIP None <none> 5432/TCP 21m
app.kubernetes.io/component=postgresql,app.kubernetes.io/instance=turbine,app.kubernetes.io/name=postgresql-ha
rabbitmq ClusterIP 10.96.1.133 <none>
5672/TCP,4369/TCP,25672/TCP,15672/TCP 21m
app.kubernetes.io/instance=turbine,app.kubernetes.io/name=rabbitmq
rabbitmq-headless ClusterIP None <none>
4369/TCP,5672/TCP,25672/TCP,15672/TCP 21m
app.kubernetes.io/instance=turbine,app.kubernetes.io/name=rabbitmq
swimlane-api ClusterIP 10.96.3.8 <none> 5000/TCP 21m
service=swimlane-api swimlane-reports ClusterIP 10.96.3.21 <none>
4000/TCP 21m service=swimlane-reports swimlane-web ClusterIP 10.96.0.173
<none> 443/TCP 21m service=swimlane-web turbine-agent ClusterIP None
<none> 10000/TCP 21m service=turbine-agent turbine-api ClusterIP
10.96.2.69 <none> 3000/TCP 21m service=turbine-api turbine-engine
ClusterIP 10.96.1.138 <none> 3000/TCP 21m service=turbine-engine
turbine-webhook-agent ClusterIP 10.96.2.47 <none> 3008/TCP 21m
service=turbine-webhook-agent turbine-websocketrelay ClusterIP
10.96.0.169 <none> 15670/TCP 21m service=turbine-websocketrelay

The ports from the example output above will be different for every
deployment. Run these commands to create firewall exceptions:

TCP ports 24361, 24964, 22626 have been assigned to our MongoDB service
for external access:

sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule
family="ipv4" port protocol="tcp" port="24361" accept' sudo firewall-cmd
--permanent --zone=public --add-rich-rule='rule family="ipv4" port
protocol="tcp" port="24964" accept' sudo firewall-cmd --permanent
--zone=public --add-rich-rule='rule family="ipv4" port protocol="tcp"
port="22626" accept'

Restart firewalld:

sudo firewall-cmd --reload

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
