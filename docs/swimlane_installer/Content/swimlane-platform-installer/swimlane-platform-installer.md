- _swimlane-platform-installer:

Swimlane Platform Installer Guide
########=

The Swimlane Platform Installer (SPI) is an administrative console where
you can access and manage your Swimlane instance. It is also where you
will go to access upgrades to new Swimlane releases, as well as any
updates to the installer itself. The installer consists of an
Application tab where you manage your application, version history,
configuration settings, as well as a Cluster Management tab and a
Snapshots tab.

|image1|

Cluster Management is where you view, drain, and add nodes to your
instance. Follow the installation steps based on how you are managing
your clusters.

+################--+################--+
| Cluster Type                     | Description                      |
+########==+########==+
| `Embedded <.                     | Install Docker, Kubernetes, and  |
| ./embedded-cluster-install/embed | the components required for a    |
| ded-cluster-installation.htm>`__ | working cluster onto your        |
|                                  | servers. Swimlane is then        |
|                                  | installed into that Kubernetes   |
|                                  | cluster, referred to here as an  |
|                                  | embedded cluster.                |
+################--+################--+
| `Existing <.                     | Install Swimlane into an         |
| ./existing-cluster-install/exist | existing Kubernetes cluster.     |
| ing-cluster-installation.htm>`__ |                                  |
+################--+################--+

You then use Snapshots to backup and restore your instance of Swimlane.

Important Information!
##########--

As of the 10.6.0 release of the Swimlane platform, Swimlane no longer
supports the Swimlane Linux Toolkit Installer. Contact your Swimlane
support representative to discuss your migration path to Swimlane with
the Swimlane Platform Installer (SPI).

As of the 10.8.0 release, Swimlane no longer supports Helm.

- |image1| image:: ../Resources/Images/Installer_Header.png

- toctree::
   :titlesonly:
   :caption: Children:

   /Content/embedded-cluster-install/embedded-cluster-installation
   /Content/existing-cluster-install/existing-cluster-installation
   /Content/troubleshooting-guide/troubleshooting-guide
