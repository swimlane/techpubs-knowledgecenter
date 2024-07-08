Install Turbine on an Embedded Kubernetes Cluster
=================================================

To install Turbine, you will first need to ensure that you have the
necessary server set up to host it.

See `System Requirements for an Embedded Cluster
Install <system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__
for information on what you need to install Turbine into an embedded
Kubernetes cluster.

Once you have the hardware accounted for, you can begin to install
Turbine.

Set Up Access to the Turbine Platform Installer
-----------------------------------------------

To begin installing Turbine with the Turbine Platform Installer, you
must first set up access to the administrative (admin) console.

To set up access to the Turbine Platform Installer:

#. From a command-line interface, log in as a privileged user to the
   system that will host your Turbine Instance.

#. Next, run:

3. Once you see the message ``Installation Complete`` copy and paste the
   URL following "Kotsadm:" and the subsequent password. Save the URL
   and password.

Access the Turbine Platform Installer Admin Console
---------------------------------------------------

Now you are ready to access the Turbine Platform Installer from a Chrome
browser.

To access the Turbine Platform Installer:

#. In a Chrome browser window, enter the URL you copied in step 3 above,
   appended with :8800.

2. On HTTPS for UI, enter the Fully Qualified Domain Name (FQDN) for the
   load balancer, and then click **Upload & Continue**.

3. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click **Upload license**.

4. Next, see the `Configure the Turbine Platform for an Embedded Cluster
   Install <configure-the-turbine-platform-for-an-embedded-cluster-install.htm>`__
   topic to configure and deploy Turbine.

5. To continue setting up additional nodes to create an HA cluster,
   continue to `Add Additional Nodes to Create an HA
   Cluster <add-additional-nodes-to-create-an-ha-cluster.htm>`__.
