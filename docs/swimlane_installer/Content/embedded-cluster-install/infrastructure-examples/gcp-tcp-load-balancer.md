GCP TCP Load Balancer
#####=

This topic explains how to use an GCP TCP Load Balancer (Layer 4) for
your Swimlane deployment.

Architecture Diagram
##########

|image1|

Create an Unmanaged Instance Group
################--

To create an `unmanaged instance
group <https://cloud.google.com/compute/docs/instance-groups?hl=en>`__:

-  Set a name for the Instance Group
-  Set the region and the zone to where the Swimlane VM instances live
-  Set the network to where the Swimlane VM instances live
-  Add your first Swimlane primary in the VM instances drop-down

Create a TCP Load Balancer:
############---

To create a `TCP load
balancer <https://cloud.google.com/load-balancing/docs/network>`__:

-  For Internet facing or internal only set `From Internet to my VMs`

-  For Multiple regions or single region set `Single region only`

-  For Backend type set `Backend Service`

-  Create a Backend Configuration

   -  Set the region to where the Swimlane instances live
   -  Select your Instance Group that contains the first Swimlane SPI VM
   -  Under the health check drop-down select an existing health check
      or `Create another health check`

      -  Set a name for the health check
      -  Set the protocol to `TCP`
      -  Set the port to `6443`
      -  Unless needed per your organization's requirements, leave the
         defaults for the remaining settings

-  Create a Frontend Configuration

   -  Set the Network Service Tier per your requirements

   -  Create a new reserved IP address or use an existing one

   -  Set Ports to `Multiple`

   -  Set the port to `6443,8800,443,80`

   -  Create the load balancer

   -  After Swimlane has been installed on the additional nodes they
      need to be added to this target group.

Notes
###~

After the initial install is done, you will need to join any additional
primaries to the Swimlane cluster before adding them to the Instance
Group in use by your load balancer to ensure the join script runs
successfully. If you want a multi-zonal deployment, you can create
additional Unmanaged Instance Groups and put your other Swimlane
primaries in them.

Adding Backend Configuration for NodePort services
########################--

Due to GCP's workaround for hairpinning, traffic may blackhole when
attempting to access NodePorts through the load balancer. This is
because GCP automatically routes traffic destined for the load balancer
to the loopback address of the VM the request was forwarded to, and
kube-proxy does not listen on localhost. To workaround this and
successfully access NodePorts through the load balancer, you will need
to create an alias for the primary network interface that resolves to
the load balancer's IP address e.g.,
`ifconfig eth0:0 <lb-ip> netmask 255.255.255.255 up` on each node in
the Swimlane cluster. To persist these changes you will need to add them
to your network interfaces configuration file.

Firewall Rules
######--

For GCP Load Balancers, ingress port access is defined in the Firewall
section of your GCP Project's VPC Network. For more information about
the port requirements see the External Access section of the `System
Requirements for an Embedded Cluster
Installation <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Swimlane Configuration
##########--

Be sure to enable the `Enable the Ingress Controller` option on the
Swimlane Platform Installer UI config tab.

- |image1| image:: ../../Resources/Images/gcp-tcp-load-balancer-diagram.png
