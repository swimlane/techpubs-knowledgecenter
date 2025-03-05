Automate Installation
#####=

These topics will walk you through `Automating an Online
Installation <automate-an-online-existing-installation.htm>`__ or
`Automating an Air-Gapped Existing Cluster
Installation <automate-an-air-gapped-existing-cluster-installation.htm>`__
of the Swimlane Platform Installer (SPI) into an existing Kubernetes
cluster.

Before attempting an automated installation, refer to the existing
cluster `system
requirements <../system-requirements-for-an-existing-cluster-install/system-requirements-for-an-existing-cluster-install.htm>`__
to ensure your systems' compliance. Also, for a thorough explanation of
the overall installation process, refer to the manual steps for an
online or offline installation.

Existing Cluster SPI Config File
################################

The automation of an SPI installation requires several files including a
valid `SPI Config
File <existing-cluster-spi-config-file.htm#creating-an-spi-config-file>`__
which defines specifics of the deployed SPI environment. This file is
based off of the options chosen when you `Configure the Swimlane
Platform <../configure-the-swimlane-platform-for-an-existing-cluster-install.htm>`__.
It is recommended to initially, manually deploy SPI, set up your desired
configuration in the SPI Config UI, and then download the resultant SPI
config file from there and modify that as opposed to building one from
scratch with these instructions. For an explanation of all the
configurable options in an SPI config file refer to the `Existing
Cluster SPI Config File <existing-cluster-spi-config-file.htm>`__ page.

- toctree::
   :titlesonly:
   :caption: Children:

   /Content/existing-cluster-install/automate-installation/automate-an-online-existing-installation
   /Content/existing-cluster-install/automate-installation/automate-an-air-gapped-existing-cluster-installation
   /Content/existing-cluster-install/automate-installation/existing-cluster-spi-config-file
