AWS Application Load Balancer
#######=

This topic explains how to use an AWS Application Load Balancer (Layer
7) for your Swimlane deployment. Two load balancers are required for
this deployment. The AWS Application Load Balancer (Layer 7) is used for
external access to the Swimlane platform and the Swimlane Platform
Installer. An additional AWS Network Load Balancer (Layer 4) is still
required for the internal cluster communication.

Architecture Diagram
##########

|image1|

Load Balancer for the Swimlane Platform and the Swimlane Platform Installer
####################################---

Target Groups
######-

-  Create the following `Target
   Group: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html>`__

   -  Port 4443

      -  `Type` set to `Instance`
      -  `Protocol` set to `HTTPS`
      -  `Port` set to `4443`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `HTTPS`
      -  `Health Check Port` set to `Traffic port`
      -  The `Health Check` settings `Healthy Threshold`,
         `Unhealthy Threshold`, `Timeout`, and `Interval` may vary
         based on your preferences for how quickly an instance should
         become unhealthy in order to stop receiving traffic.
      -  `Health Check Success codes` set to `200`
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `4443`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

   -  Port 8800

      -  `Type` set to `Instance`
      -  `Protocol` set to `HTTPS`
      -  `Port` set to `8800`
      -  `VPC` should match that of the EC2 instances that Swimlane
         will be installed on
      -  `Health Check protocol` set to `HTTPS`
      -  `Health Check Port` set to `Traffic port`
      -  The `Health Check` settings `Healthy Threshold`,
         `Unhealthy Threshold`, `Timeout`, and `Interval` may vary
         based on your preferences for how quickly an instance should
         become unhealthy in order to stop receiving traffic.
      -  `Health Check Success codes` set to `200`
      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `8800`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

Load Balancer
######-

-  Create an `AWS Application Load
   Balancer <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html>`__

   -  `IP address type`

      -  Choose `ipv4`

   -  Add a `Listener`\ for each of the following ports:

      -  Port 443

         -  `Protocol` set to `HTTPS`
         -  `Port` set to `443`
         -  Configure it to forward traffic to the `Port 4443` Target
            Group created above
         -  `Security Policy` set according to your security policies

            -  More information about `HTTPS
               Listeners <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html>`__
            -  `ELBSecurityPolicy-TLS-1-2-2017-01` or stronger is
               recommended

         -  `Default SSL certificate` set to the ACM, IAM, or imported
            certificate that you choose

            -  This certificate needs to be valid for the Swimlane
               Hostname you specify when configuring our application

      -  Port 8800

         -  `Protocol` set to `HTTPS`
         -  `Port` set to `8800`
         -  Configure it to forward traffic to the `Port 8800` Target
            Group created above
         -  `Security Policy` set according to your security policies

            -  More information about `HTTPS
               Listeners <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html>`__
            -  `ELBSecurityPolicy-TLS-1-2-2017-01` or stronger is
               recommended

         -  `Default SSL certificate` set to the ACM, IAM, or imported
            certificate that you choose

            -  This certificate needs to be valid for the Swimlane
               Hostname you specify when configuring our application

      -  Optional - Port 80

         -  Used for the HTTP to HTTPS redirect and can be excluded if
            you only want HTTPS/443 to be available
         -  `Protocol` set to `HTTP`
         -  `Port` set to `80`
         -  Configure it to `Redirect to` with the following settings

            -  `Protocol` set to `HTTPS`
            -  `Port` set to `443`
            -  Path settings set to `Original host, path, query`
            -  `Status Code` set to `301 - Permanently moved`

   -  `Availability Zones`

      -  The Application Load Balancer's `VPC` should match that of
         the EC2 instances that Swimlane will be installed on
      -  The Application Load Balancer's `Availability Zones` should
         include each Availability Zone used by the EC2 instances that
         Swimlane will be installed on

Security Groups
######---

For AWS Application Load Balancers, ingress port access is defined in
the Security Group assigned to the load balancer itself. For more
information about the port requirements see the External Access section
of the `System Requirements for an Embedded Cluster
Installation <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Load Balancer for internal cluster communication
########################

- _target-groups-1:

Target Groups
#########~

-  Create the following `Target
   Groups: <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html>`__

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

      -  Register the first instance that you'll be running the Swimlane
         Platform Installer on to the target group with `Port` set to
         `80`.

         -  After Swimlane has been installed on the additional nodes
            they need to be added to this target group.

- _load-balancer-1:

Load Balancer
#########~

-  Create an `AWS Network Load
   Balancer <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html>`__

   -  `IP address type`

      -  Choose `ipv4`

   -  Add a `Listener` for each of the following ports:

      -  Port 6443

         -  `Protocol` set to `TCP`
         -  `Port` set to `6443`
         -  Configure it to forward traffic to the `Port 6443` Target
            Group created above

   -  `Availability Zones`

      -  The Network Load Balancer's `VPC` should match that of the
         EC2 instances that Swimlane will be installed on
      -  The Network Load Balancer's `Availability Zones` should
         include each Availability Zone used by the EC2 instances that
         Swimlane will be installed on

- _security-groups-1:

Security Groups
#########~~~

For AWS Network Load Balancers, ingress port access is defined in the
Security Group used by the EC2 instances. The port requirements are
available in the External Access section of the `System Requirements for
an Embedded Cluster
Installation <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.

Swimlane Configuration
##########--

Be sure to enable the `Expose the Swimlane Web service externally`
option on the Swimlane Platform Installer UI config tab.

- |image1| image:: ../../Resources/Images/aws-application-load-balancer-diagram.png
