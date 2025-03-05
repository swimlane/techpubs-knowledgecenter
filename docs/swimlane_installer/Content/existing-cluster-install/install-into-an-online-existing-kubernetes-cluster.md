Install Into an Online Existing Kubernetes Cluster
############==

Prepare the SPI Kubectl Add-on
##############--

#. Download the SPI kubectl add-on for the OS version where you run
   kubectl commands from:

#. Untar the file:

   tar zxf kots\_<OS version>.tar.gz

#. Rename the kots binary to kubectl-kots: mv kots kubectl-kots

#. Move the kubectl-kots binary into your PATH so that it can be
   recognized by kubectl (e.g. /usr/local/bin/)

Install the SPI Using the Kubectl Add-on
####################

#. Choose the namespace that you will install the Swimlane Platform
   Installer and Swimlane Platform into. These instructions refer to
   this namespace as your-namespace.

#. First, run:

#. When the install is complete it automatically proxies the SPI UI to
   http://localhost:8800.

#. Enter the password you specified during the install process.

#. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click Upload license.

#. Next, see the `Configure the Swimlane Platform for an Existing
   Cluster
   Install <configure-the-swimlane-platform-for-an-existing-cluster-install.htm>`__
   topic to configure and deploy Swimlane.
