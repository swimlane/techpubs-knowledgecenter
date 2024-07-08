Air Gap Installation with kURL
==============================

This topic walks through the process of installing Turbine in an
air-gapped environment using kURL. Air gap refers to a system that
resides in a private network, air-gapped from external networks or the
internet. kURL is the Kubernetes installer used to initialize the
environment in Swimlane's embedded cluster installation option.

Swimlane provides the following:

-  The offline installer package
-  The air gap bundle
-  A KOTS application license (.yaml)
-  A Swimlane license (.lic)

The offline installer package contains the install script and all the
software dependencies, such as Kubernetes, to initialize the
environment. The airgap bundle contains the dependencies for the actual
Turbine application. When it comes time to update your Turbine version,
you will need a new installer package and airgap bundle. Reach out to
your Swimlane support representative for access to the new installer
package and airgap bundle.

On your end, you need:

-  a jumpbox with access to both the internet and the private network.
-  a set of VMs that will be the nodes of your Kubernetes cluster. They
   must meet Swimlane's `system
   requirements <system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__.
-  the four dependencies listed above from Swimlane.

Before you begin, copy the offline installer package to the jumpbox, and
then to each node in the cluster. Copy the airgap bundle to the jumpbox.

The goal is to initialize a Kubernetes cluster, usually with 3
control-plane nodes to create high availability (HA). Turbine can then
be installed on these control-plane nodes as a KOTS application. KOTS is
a kubectl plugin and admin console tool that allows the end user to
manage system settings without making direct changes to Kubernetes
resources.

The following steps walk through this process:

#. Untar the offline installer package on the first VM:

2. Move to the directory with the install script and run the install
   command:

3.  Once the installation completes, save the URL and password that the
    installation generates. In addition, copy the add master node
    command to use to add additional masters.

4.  Untar the offline installer package in the second VM.

5.  Run the master node join command that was output in step 2.

6.  Repeat steps 4 and 5 for the third and final VM.

7.  | Run this command to make sure each node has successfully joined
      the Kubernetes cluster:

8.  In a web browser, enter the URL and password for the Swimlane
    Platform Installer User Interface (UI). This is the password you got
    from the original install command. Upload your .yaml license file
    and proceed until you are prompted to upload the airgap bundle.

9.  Upload the airgap bundle from your jumpbox

10. See `Configure the Turbine Platform for an Embedded Cluster
    Install <configure-the-turbine-platform-for-an-embedded-cluster-install.htm>`__
    to configure and deploy Turbine.
