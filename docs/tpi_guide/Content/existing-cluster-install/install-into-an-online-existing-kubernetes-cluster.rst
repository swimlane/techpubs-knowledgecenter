Install Into an Online Existing Kubernetes Cluster
==================================================

Prepare the Turbine Installer Kubectl Add-on
--------------------------------------------

#. Download the Turbine Installer kubectl add-on for the OS version
   where you run kubectl commands from:

#. Untar the file:

#. Rename the kots binary to kubectl-kots and move the kubectl-kots
   binary into your PATH so that it can be recognized by kubectl (e.g.
   /usr/local/bin/):

Install the Turbine Installer Using the Kubectl Add-on
------------------------------------------------------

#. Choose the namespace that you will install the Turbine Installer and
   Turbine Platform into. These instructions refer to this namespace as
   ``your-namespace``.

#. First, run:

   kubectl kots install turbine --namespace your-namespace

   ````

   This automatically creates the namespace specified if it does not
   exist.

   | If the KUBECONFIG environment variable is not set you will need to
     add the following to the install command above so that it can
     authenticate to your cluster:

   --kubeconfig /path/to/kube/config

#. When the install is complete it automatically proxies the Turbine
   Installer UI to ``http://localhost:8800``.

#. Enter the password you specified during the install process.

#. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click **Upload license**.

#. Next, see the `Configure the Turbine Platform for an Existing Cluster
   Install <OLD_configure-the-turbine-platform-for-an-existing-cluster-install.htm>`__
   topic to configure and deploy Turbine.
