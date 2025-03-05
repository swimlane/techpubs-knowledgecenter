Azure Load Balancer
####===

This topic explains how to use an Azure Load Balancer (Layer 4) for your
Swimlane deployment.

Architecture Diagram
##########

|image1|

Load Balancer
######-

-  Create a `Public Azure Load
   Balancer <https://docs.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal>`__

__Important!__ `Type` must be set to `Public` because internal load
balancers do not support hairpinning.

Continue setup of the load balancer with the following settings:

-  `Resource Group` should be set according to your organization's
   standards
-  `Region` should match that of the Virtual Machines that Swimlane
   will be installed in
-  `Type` set to `Public`

   -  This has to be set to Public because Internal load balancers do
      not support hairpinning
   -  Access to the virtual machines should still be restricted by
      network security groups

-  `SKU` set to `Standard`
-  `Tier` set to\ `Regional`
-  `Public IP Address` can either be a new Public IP Address to use or
   select an existing one
-  `Availability Zone` set to `Zone-redundant`

Backend Pools
######-

-  Create the following Backend Pools:

   -  Port 443

      -  `Backend Pool Configuration` set to `NIC`
      -  `IP Version` set to `IPv4`
      -  `Virtual Machines`

         -  Add the first virtual machine that you'll be running the
            Swimlane Platform Installer on to the backend pool

            -  After Swimlane has been installed on the additional nodes
               they need to be added to this target group

   -  Port 8800

      -  `Backend Pool Configuration` set to `NIC`
      -  `IP Version` set to `IPv4`
      -  `Virtual Machines`

         -  Add the first virtual machine that you'll be running the
            Swimlane Platform Installer on to the backend pool

            -  After Swimlane has been installed on the additional nodes
               they need to be added to this target group

   -  Port 6443

      -  `Backend Pool Configuration` set to `NIC`
      -  `IP Version` set to `IPv4`
      -  `Virtual Machines`

         -  Add the first virtual machine that you'll be running the
            Swimlane Platform Installer on to the backend pool

            -  After Swimlane has been installed on the additional nodes
               they need to be added to this target group

   -  Optional - Port 80

      -  Used for the HTTP to HTTPS redirect and can be excluded if you
         only want HTTPS/443 to be available
      -  `Backend Pool Configuration` set to `NIC`
      -  `IP Version` set to `IPv4`
      -  `Virtual Machines`

         -  Add the first virtual machine that you'll be running the
            Swimlane Platform Installer on to the backend pool

            -  After Swimlane has been installed on the additional nodes
               they need to be added to this target group

Health Probes
######-

-  Create the following Health Probes:

   -  Port 443

      -  `Protocol` set to `TCP`
      -  `Port` set to `443`
      -  `Interval` and `Unhealthy Threshold` may vary based on your
         preferences for how quickly a virtual machine should become
         unhealthy in order to stop receiving traffic

   -  Port 8800

      -  `Protocol` set to `TCP`
      -  `Port` set to `8800`
      -  `Interval` and `Unhealthy Threshold` may vary based on your
         preferences for how quickly a virtual machine should become
         unhealthy in order to stop receiving traffic

   -  Port 6443

      -  `Protocol` set to `TCP`
      -  `Port` set to `6443`
      -  `Interval` and `Unhealthy Threshold` may vary based on your
         preferences for how quickly a virtual machine should become
         unhealthy in order to stop receiving traffic

   -  Optional - Port 80

      -  Used for the HTTP to HTTPS redirect and can be excluded if you
         only want HTTPS/443 to be available
      -  `Protocol` set to `TCP`
      -  `Port` set to `80`
      -  `Interval` and `Unhealthy Threshold` may vary based on your
         preferences for how quickly a virtual machine should become
         unhealthy in order to stop receiving traffic

Load Balancing Rules
##########

-  Create the following Load Balancing Rules:

   -  Port 443

      -  `IP Version` set to `IPv4`
      -  `Frontend IP Address` set to the IP that was chosen when the
         load balancer was created
      -  `Protocol` set to `TCP`
      -  `Port` set to `443`
      -  `Backend Port` set to `443`
      -  `Backend Pool` set to the `Port 443` backend pool created
         above
      -  `Health Probe` set to the `Port 443` health probe created
         above
      -  `Floating IP` set to `Disabled`
      -  `Outbound Source Network Address Translation` set to
         `Outbound and inbound use the same IP`

   -  Port 8800

      -  `IP Version` set to `IPv4`
      -  `Frontend IP Address` set to the IP that was chosen when the
         load balancer was created
      -  `Protocol` set to `TCP`
      -  `Port` set to `8800`
      -  `Backend Port` set to `8800`
      -  `Backend Pool` set to the `Port 8800` backend pool created
         above
      -  `Health Probe` set to the `Port 8800` health probe created
         above
      -  `Floating IP` set to `Disabled`
      -  `Outbound Source Network Address Translation` set to
         `Outbound and inbound use the same IP`

   -  Port 6443

      -  `IP Version` set to `IPv4`
      -  `Frontend IP Address` set to the IP that was chosen when the
         load balancer was created
      -  `Protocol` set to `TCP`
      -  `Port` set to `6443`
      -  `Backend Port` set to `6443`
      -  `Backend Pool` set to the `Port 6443` backend pool created
         above
      -  `Health Probe` set to the `Port 6443` health probe created
         above
      -  `Floating IP` set to `Disabled`
      -  `Outbound Source Network Address Translation` set to
         `Outbound and inbound use the same IP`

   -  Optional - Port 80

      -  `IP Version` set to `IPv4`
      -  `Frontend IP Address` set to the IP that was chosen when the
         load balancer was created
      -  `Protocol` set to `TCP`
      -  `Port` set to `80`
      -  `Backend Port` set to `80`
      -  `Backend Pool` set to the `Port 80` backend pool created
         above
      -  `Health Probe` set to the `Port 80` health probe created
         above
      -  `Floating IP` set to `Disabled`
      -  `Outbound Source Network Address Translation` set to
         `Outbound and inbound use the same IP`

Network Security Groups
##########---

For Azure Load Balancers, ingress port access is defined in the Network
Security groups used by the virtual machines and subnets. The port
requirements are available in the External Access section of the `System
Requirements for an Embedded Cluster
Installation <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Swimlane Configuration
##########--

Be sure to enable the `Enable the Ingress Controller` option on the
Swimlane Platform Installer UI config tab.

- |image1| image:: ../../Resources/Images/azure-load-balancer-diagram.png
