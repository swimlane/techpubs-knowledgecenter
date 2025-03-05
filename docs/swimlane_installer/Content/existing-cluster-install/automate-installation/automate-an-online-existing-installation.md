Automate an Online Existing Installation
##########

This topic provides steps for automating an online Swimlane installation
into an existing Kubernetes cluster.

Other Requirements
########--

To automate this process the following files are needed:

-  Swimlane Platform Installer (SPI) license file (ends with `.yaml`)
-  Swimlane license file (ends with `.lic`)

SPI Kubectl Add-on Installation
##############---

In order to automate a Swimlane installation in to an existing cluster,
the SPI Kubectl Add-on must be downloaded and correctly setup on a
system with access to the cluster:

For Linux, download and untar the binary file:

curl -sSL -O https://get.swimlane.io/existing-cluster/install/linux tar
-zxvf linux mv kots /usr/local/bin/kubectl-kots

For OSX, download and untar the binary file:

curl -sSL -Ohttps://get.swimlane.io/existing-cluster/install/osx tar
-zxvf osx mv kots /usr/local/bin/kubectl-kots

Swimlane Installation and Deployment
##################

After the SPI Kubectl Add-on has been installed, install Swimlane with
the following command:

kubectl kots install swimlane-platform \\ --namespace <Namespace> \\
--shared-password <SPI Admin Console Password> \\ --license-file <SPI
License>.yaml \\ --port-forward=false \\ --config-values <SPI Config
File>.yaml

Creating an SPI Config File
##################~~~

The `<SPI Config File>.yaml` file is a YAML-formatted file that
outlines the specifications of a Swimlane deployment. You can get the
.yaml file from a previously configured installation of SPI or by
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

To create the file manually, review the configurable options available
in the `Existing Cluster SPI <existing-cluster-spi-config-file.htm>`__.

Here is a basic version of the config file that you can use for an
initial single-node configuration:

apiVersion: kots.io/v1beta1 kind: ConfigValues metadata:
creationTimestamp: null name: <Swimlane Namespace> spec: values: is_ha:
value: "0" mongo_admin_user_password: value: <Base64 encoded string>
mongo_admin_user_password_confirm: value: <Base64 encoded string>
mongo_swimlane_user_password: value: <Base64 encoded string>
mongo_swimlane_user_password_confirm: value: <Base64 encoded string>
swimlane_database_encrypt_key: value: <Base64 encoded string>
swimlane_database_encrypt_key_confirm: value: <Base64 encoded string>
swimlane_enable_ingress: value: "1" swimlane_hostname: value: <Swimlane
Hostname> swimlane_ingress_annotations: value: \|- <Insert ingress
annotations here> <Insert ingress annotations here>
swimlane_storage_class: value: <Storage Class Name>

Swimlane Initial Login
##########--

It will take a few minutes for Swimlane to initialize all of the
required components. However, automation can effectively 'wait' for a
ready state by waiting for a ready status from different parts of the
deployment. There are multiple ways to accomplish this wait period, the
following code block is just one example:

kubectl wait -l statefulset.kubernetes.io/pod-name=swimlane-sw-mongo-0
--for=condition=ready pod --namespace <Swimlane Namespace>
--timeout=240s export SW_API=$(kubectl get po -n <NameSpace>
--no-headers -o custom-columns=":metadata.name" \| grep -i api) kubectl
wait --for=condition=ready pod $SW_API -n <NameSpace> --timeout=240s

Next, continue with the Swimlane install by creating the initial
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
"license" :<Generated JSON Data>, "adminUserName":"<Admin Username>",
"adminEmail":"<Admin Email>"}'
