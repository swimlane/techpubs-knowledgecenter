Install Into an Online OpenShift Cluster
##########

Prepare the SPI Kubectl Add-on
##############--

#. Download the SPI kubectl add-on for the OS version where you run
   kubectl commands from:

#. Untar the file: tar zxf kots_linux\_<OS version>.tar.gz

#. | Rename the kots binary to kubectl-kots:

   mv kots kubectl-kots

#. | Move the kubectl-kots binary into your PATH so that it can be
     recognized by kubectl (e.g. /usr/local/bin/)

   mv kubectl-kots /usr/local/bin/

Install the SPI Using the Kubectl Add-on
####################

#. Choose the namespace into which you are installing the Swimlane
   Platform Installer and Swimlane Platform. These instructions refer to
   this namespace as your-namespace.

#. Choose the service account that the Swimlane pods will run as. These
   instructions refer to this service account as service-account-name.

#. Create the namespace and service account with the correct OpenShift
   policy to run the Swimlane pods:

   kubectl create namespace your-namespace: oc create serviceaccount
   service-account-name -n your-namespace oc adm policy add-scc-to-user
   anyuid -z service-account-name -n your-namespace

#. Next, run:
   kubectl kots install swimlane-platform --namespace your-namespace

#. When the install is complete it automatically proxies the SPI UI to
   http://localhost:8800.

#. Enter the password you specified during the install process.

#. Next, you are prompted to upload your .yaml license file. Select or
   drag the file, and then click Upload license.

#. Next, see `Configure the Swimlane Platform for an Existing Cluster
   Install <configure-the-swimlane-platform-for-an-existing-cluster-install.htm>`__
   to configure and deploy Swimlane.

#. After Swimlane has been deployed, more steps are required to ensure
   that all Swimlane pods start successfully:

   The service account used by the Swimlane tools container requires an
   OpenShift policy be set in order to run. If you chose to have the
   service account used by the Swimlane Tools deployment automatically
   created then the service account name to specify to the command below
   will be swimlane-backup. If you chose to create your own service
   account, you will need to use the name of the service account you
   created for it.

   oc adm policy add-scc-to-user anyuid -z tools-service-account-name -n
   your-namespace
