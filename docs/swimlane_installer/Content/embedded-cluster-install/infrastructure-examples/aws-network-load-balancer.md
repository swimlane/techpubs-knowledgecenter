AWS Network Load Balancer
######=

This topic explains how to use an AWS Network Load Balancer (Layer 4)
for your Swimlane deployment.

Architecture Diagram
##########

|image1|

Target Groups
######-

-  Create the following `Target
   Groups: <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>`__

   -  Port 443

      -  `Type` set to `IP`
      -  `Protocol` set to `TCP`
      -  `Port` set to `443`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `TCP`
      -  `Health Check Port` set to `Traffic port`
      -  `Healthy Threshold`, `Unhealthy Threshold`, `Timeout`,
         and `Interval` may vary based on your preferences for how
         quickly an instance should become unhealthy in order to stop
         receiving traffic.
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `443`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

   -  Port 8800

      -  `Type` set to `IP`
      -  `Protocol` set to `TCP`
      -  `Port` set to `8800`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `TCP`
      -  `Health Check Port` set to `Traffic port`
      -  `Healthy Threshold`, `Unhealthy Threshold`, `Timeout`,
         and `Interval` may vary based on your preferences for how
         quickly an instance should become unhealthy in order to stop
         receiving traffic.
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `8800`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

   -  Port 6443

      -  `Type` set to `IP`
      -  `Protocol` set to `TCP`
      -  `Port` set to `6443`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `TCP`
      -  `Health Check Port` set to `Traffic port`
      -  `Healthy Threshold`, `Unhealthy Threshold`, `Timeout`,
         and `Interval` may vary based on your preferences for how
         quickly an instance should become unhealthy in order to stop
         receiving traffic.
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `6443`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

   -  Optional - Port 80

      -  Used for the HTTP to HTTPS redirect and can be excluded if you
         only want HTTPS/443 to be available
      -  `Type` set to `IP`
      -  `Protocol` set to `TCP`
      -  `Port` set to `80`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `TCP`
      -  `Health Check Port` set to `Traffic port`
      -  `Healthy Threshold`, `Unhealthy Threshold`, `Timeout`,
         and `Interval` may vary based on your preferences for how
         quickly an instance should become unhealthy in order to stop
         receiving traffic.
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `80`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

Load Balancer
######-

-  Create an `AWS Network Load
   Balancer <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html>`__

   -  `IP address type`

      -  Choose `ipv4`

   -  Add a `Listener`\ for each of the following ports:

      -  Port 443

         -  `Protocol` set to `TCP`
         -  `Port` set to `443`
         -  Configure it to forward traffic to the `Port 443` Target
            Group created above

      -  Port 8800

         -  `Protocol` set to `TCP`
         -  `Port` set to `8800`
         -  Configure it to forward traffic to the `Port 8800` Target
            Group created above

      -  Port 6443

         -  `Protocol` set to `TCP`
         -  `Port` set to `6443`
         -  Configure it to forward traffic to the `Port 6443` Target
            Group created above

      -  Optional - Port 80

         -  Used for the HTTP to HTTPS redirect and can be excluded if
            you only want HTTPS/443 to be available
         -  `Protocol` set to `TCP`
         -  `Port` set to `80`
         -  Configure it to forward traffic to the `Port 80` Target
            Group created above

   -  `Availability Zones`

      -  The Network Load Balancer's `VPC` should match that of the
         EC2 instances that Swimlane will be installed on
      -  The Network Load Balancer's `Availability Zones` should
         include each Availability Zone used by the EC2 instances that
         Swimlane will be installed on

Security Groups
######---

For AWS Network Load Balancers, ingress port access is defined in the
Security Group used by the EC2 instances. The port requirements are
available in the External Access section of the `System Requirements for
an Embedded Cluster
Installation <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Swimlane Configuration
##########--

Be sure to enable the `Enable the Ingress Controller` option on the
Swimlane Platform Installer UI config tab.

- |image1| image:: ../../Resources/Images/aws-network-load-balancer-diagram.png
