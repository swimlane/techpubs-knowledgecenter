Install Into an Offline Existing Kubernetes Cluster
############===

Prepare the SPI Kubectl Add-on
##############--

#. Download the SPI kubectl add-on for the OS version of your jumpbox:

#. Untar the file:

#. Rename the kots binary to kubectl-kots:

#. Move the kubectl-kots binary into your PATH so that it can be
   recognized by kubectl (e.g. /usr/local/bin/)

Install the SPI Using the Kubectl Add-on
####################

#. Choose the namespace that you will install the Swimlane Platform
   Installer and Swimlane Platform into. This guide will refer to this
   namespace as your-namespace.

#. | Download the offline installer package to your jumpbox:

   https://get.swimlane.io/existing-cluster/install/offline-package

#. Copy the offline installer package to the jumpbox.

#. Upload the SPI container images to your private registry to prepare
   for installation into the Kubernetes cluster:

#. Install the SPI pods:

#. When the install is complete it will automatically proxy the SPI UI
   to http://localhost:8800.

#. Enter the password you specified during the install process.

#. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click Upload license.

#. After the license is uploaded it will prompt you to confirm the
   private docker image registry settings.

#. After the Swimlane platform images are pushed to the private docker
   image registry it will take you to the config page to configure the
   Swimlane platform. See the `Configure the Swimlane Platform for an
   Existing Cluster
   Install <configure-the-swimlane-platform-for-an-existing-cluster-install.htm>`__
   topic to configure and deploy Swimlane.
