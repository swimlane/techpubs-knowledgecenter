.. _turbine-platform-installer:

Turbine Platform Installer Guide
================================

| **Important!** This guide is for Turbine on-premise installs. If you
  are on 11.8.x, please refer to the `11.x Turbine Platform Installer
  Guide <https://docs.swimlane.com/turbine_installer_11/>`__.

The Turbine Platform Installer (TPI) is an administrative console where
you can access and manage your Turbine instance. It is also where you
will go to access upgrades to new Turbine releases, as well as any
updates to the installer itself. The installer consists of an
Application tab where you manage your application, version history,
configuration settings, as well as a Cluster Management tab and a
Snapshots tab.

|image1|

Cluster Management is where you view, drain, and add nodes to your
instance. Follow the installation steps based on how you are managing
your clusters.

+----------------------------------+----------------------------------+
| Cluster Type                     | Description                      |
+==================================+==================================+
| `Embedded <.                     | Install Docker, Kubernetes, and  |
| ./embedded-cluster-install/embed | the components required for a    |
| ded-cluster-installation.htm>`__ | working cluster onto your        |
|                                  | servers. Turbine is then         |
|                                  | installed into that Kubernetes   |
|                                  | cluster, referred to here as an  |
|                                  | embedded cluster.                |
+----------------------------------+----------------------------------+
| `Existing <.                     | Install Turbine into an existing |
| ./existing-cluster-install/exist | Kubernetes cluster.              |
| ing-cluster-installation.htm>`__ |                                  |
+----------------------------------+----------------------------------+

You can then use Snapshots to backup and restore your instance of
Turbine.

.. |image1| image:: ../Resources/Images/Installer_Header.png

.. toctree::
   :titlesonly:
   :caption: Related Topics

   /Content/embedded-cluster-install/embedded-cluster-installation
   /Content/existing-cluster-install/existing-cluster-installation
   /Content/troubleshooting-guide/troubleshooting-guide
