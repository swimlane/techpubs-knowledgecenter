.. _install-into-an-offline-existing-kubernetes-cluster:

Air Gap Installation on an Existing Kubernetes Cluster
======================================================

This topic details the process of installing Turbine in an existing
Kubernetes cluster that is air-gapped. Air gap refers to a system that
resides in a private network, "air-gapped" from external networks or the
internet.

Swimlane provides the following:

-  The air gap bundle

-  A KOTS application license (.yaml)

-  A Swimlane license (.lic)

The airgap bundle contains the images and Kubernetes manifests for
Turbine. When it comes time to update your Turbine version, you will
need a new air gap bundle. Reach out to your Swimlane support
representative for access to the new bundle.

Before you begin you need:

-  The airgap bundle in a jumpbox that your Kubernetes cluster can pull
   from.

-  The KOTS kubectl addon version that is currently recommended by
   Swimlane.

-  A private image registry.

Verify your environment meets Turbine's `system
requirements <system-requirements-for-an-existing-cluster-install/system-requirements-for-an-existing-cluster-install.htm>`__.

Install KOTS Kubectl Add-on
---------------------------

#. The current recommended KOTS version is available through these
   links. Download the TPI kubectl add-on for the OS version of your
   jumpbox:

2. Untar the file:

#. Rename the ``kots`` binary to ``kubectl-kots``:

#. Move the ``kubectl-kots`` binary into your PATH so that it can be
   recognized by kubectl (e.g. /usr/local/bin/):

Install the Swimlane Application using KOTS
-------------------------------------------

#. Choose the namespace within which you will install the Swimlane
   Platform Installer (SPI) and Swimlane platform. These instructions
   will refer to this namespace as \`your-namespace\`.

#. Download the offline installer package to your jumpbox:

   https://get.swimlane.io/existing-cluster/install/offline-package

#. Copy the offline installer package to the jumpbox.

#. Upload the TPI container images to your private registry to prepare
   for installation into the Kubernetes cluster:

#. Install the TPI pods:

#. | If the KUBECONFIG environment variable is not set you will need to
     add the following to the install command above so that it can
     authenticate to your cluster:

   --kubeconfig /path/to/kube/config

#. When the install is complete it will automatically proxy the TPI UI
   to http://localhost:8800.

#. Enter the password you specified during the install process.

#. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click Upload license.

#. After the license is uploaded it will prompt you to confirm the
   private docker image registry settings.

#. After the Turbine platform images are pushed to the private Docker
   image registry, the Config page opens. This is where you configure
   the Turbine platform. See `Configure the Turbine Platform for an
   Existing Cluster
   Install <OLD_configure-the-turbine-platform-for-an-existing-cluster-install.htm>`__
   to configure and deploy Turbine.
