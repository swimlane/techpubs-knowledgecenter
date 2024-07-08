Offline Embedded Cluster Install
================================

If you need to do an offline installation of Turbine with the Turbine
Platform Installer, you will need the offline installer package, and an
airgap bundle. The airgap bundle works with the Installer to allow an
offline install.

Airgap installs require a jumpbox that has access to:

-  the internet
-  the airgapped network
-  a browser, from which you can access the Turbine Platform Installer

Before you begin, copy the offline installer package to the jumpbox and
then to each node in the cluster.

To perform an offline install with the Turbine Platform Installer:

#. Copy the offline installer package to the instance that will become
   the first cluster master node and untar the package with the
   following command:

2. Next, run this install command:

3.  Once install completes, save the URL and password that the install
    generates. In addition, copy the add master node command to use to
    add additional masters.

4.  Copy the offline installer package to an additional master node.

5.  Untar the offline installer package.

6.  Run the add master node command that you copied in step 3, above.

7.  Repeat steps 4 through 6 above until all nodes have been installed.

8.  | Next, run this command to make sure each node is ready:

    kubectl get nodes

9.  Copy the airgap bundle to the jumpbox.

10. In a Chrome browser, enter the URL and password for the Turbine
    Platform Installer UI (from the original install command). Upload
    your .yaml license file and proceed until you are prompted to upload
    the airgap bundle.

11. Upload the airgap bundle.

After the airgap bundle is uploaded and processed, see the `Configure
the Turbine Platform for an Embedded Cluster
Install <configure-the-turbine-platform-for-an-embedded-cluster-install.htm>`__
topic to configure and deploy Turbine.
