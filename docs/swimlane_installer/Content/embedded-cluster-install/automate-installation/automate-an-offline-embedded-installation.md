Automate an Offline Embedded Installation
##########=

This topic provides automation steps for setting up an offline,
single-node Swimlane installation on embedded clusters.

Installation Preparation and Customization
####################--

Before you begin, review the `System Requirements for an Embedded
Cluster
Install <../system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__
to confirm your system's compliance. The Swimlane Platform Installer
(SPI) performs several checks in the initial phases of the installation
to ensure the underlying host is compatible with the application. To
bypass any applicable checks, an installer patch YAML file can be
applied at installation time to account for several of these settings.
Refer to `Overriding Installer
Settings <../overriding-installer-settings/overriding-installer-settings.htm>`__
for more options.

Installer Patch File Example
#####################

Here is an example installer patch file:

apiVersion: "cluster.kurl.sh/v1beta1" kind: "Installer" metadata: name:
"patch" spec: kubernetes: HACluster: true loadBalancerAddress: "<Load
Balancer FQDN or IP>:6443" firewalldConfig: disableFirewalld: true
selinuxConfig: disableSelinux: true

You also need the following files:

-  Swimlane Platform Installer license file (ends with `.yaml`)
-  Swimlane license file (ends with `.lic`)
-  Swimlane tar archive (ends with `.tar.gz`)
-  Swimlane airgap bundle (ends with `.airgap`)

Embedded Cluster Installation
##############-

Once you've accounted for any customizations and system checks, install
an embedded cluster by running the following command:

tar -zxvf <Swimlane Airgap Bundle>.tar.gz cat install.sh \| bash -s
installer-spec-file=<Path to Patch File>.yaml

Swimlane Installation and Deployment
##################

After the embedded Kubernetes cluster has been installed, install
Swimlane with the following command:

kubectl kots install swimlane-platform \\ --namespace default \\
--shared-password <SPI Admin Console Password> \\ --license-file <SPI
License File>.yaml \\ --port-forward=false \\ --config-values <SPI
Config File>.yaml \\ --airgap-bundle <Swimlane Airgap Bundle>.airgap

Creating an SPI Config File
##################~~~

The `<SPI Config File>.yaml` file is a YAML-formatted file that
outlines the specifications of a Swimlane deployment. You can get the
.yaml file from an previously configured installation of SPI or by
creating a new file manually.

To obtain a file from an previously configured SPI install, run the
following command from a system with access to the Kubernetes API and
the SPI Kubectl Add-on installed:

`kubectl kots download swimlane-platform -n <namespace>`

This command downloads a copy of the entire SPI deployment
specifications to a local folder named `swimlane-platform`.

The config file is located at
`./swimlane-platform/upstream/userdata/config.yaml` in the downloaded
folder.

To create the file manually, here are all configurable options available
in the `Embedded Cluster SPI <embedded-cluster-spi-config-file.htm>`__.

Here is a basic version of the config file that you can use for an
initial single-node configuration:

apiVersion: kots.io/v1beta1 kind: ConfigValues metadata:
creationTimestamp: null name: swimlane spec: values: is_ha: value: "0"
mongo_admin_user_password: value: <Base64 encoded string>
mongo_admin_user_password_confirm: value: <Base64 encoded string>
mongo_swimlane_user_password: value: <Base64 encoded string>
mongo_swimlane_user_password_confirm: value: <Base64 encoded string>
swimlane_database_encrypt_key: value: <Base64 encoded string>
swimlane_database_encrypt_key_confirm: value: <Base64 encoded string>
swimlane_enable_ingress: value: "1" swimlane_hostname: value: <Swimlane
Hostname>

Swimlane Initial Login
##########--

It takes a few minutes for Swimlane to initialize all of the required
components. However, automation can effectively 'wait' for a ready state
by waiting for a ready status from different parts of the deployment.
There are multiple ways to accomplish this wait period, the following
code block is just one example:

kubectl wait -l statefulset.kubernetes.io/pod-name=swimlane-sw-mongo-0
--for=condition=ready pod --namespace <Swimlane Namespace>
--timeout=240s export SW_API=$(kubectl get po -n <NameSpace>
--no-headers -o custom-columns=":metadata.name" \| grep -i api) kubectl
wait --for=condition=ready pod $SW_API -n <NameSpace> --timeout=240s

Next, continue with the Swimlane installation by creating the initial
administrative user.

Using your Swimlane license .lic file, first generate the necessary
license block for the API call with a curl command:

`curl -kLv -X POST https://<Swimlane URL>/api/settings/license/upload -H 'Content-Type: multipart/form-data' -F file=@<Swimlane License File>.lic`

Then, to create the initial administrative user, insert the returned
JSON into the following curl command:

curl -kLv -X POST https://<Swimlane URL>/api/settings/install \\
--header "Content-Type: application/json" \\ -d '{"mailSettings":{},
"password":"<Admin Password>","confirmPassword":"<Admin Password>",
"databaseEncryptionKey":"", "swimlaneUrl":"https://<Swimlane URL>",
"license" :<Generated JSON Data From Previous Step>,
"adminUserName":"<Admin Username>", "adminEmail":"<Admin Email>"}'
