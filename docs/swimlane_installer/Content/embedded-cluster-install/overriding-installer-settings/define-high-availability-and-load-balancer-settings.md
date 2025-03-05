Define High Availability and Load Balancer Settings
############===

In order to deploy Swimlane with High Availability, the `ha` flag must
be used during the initial installation.

This can also be set by adding `HACluster: true` (under the kubernetes
spec) to the installer-override.yaml patch file `spec:` section.

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: kubernetes: HACluster: true

During initial installation, the Swimlane Platform Installer will prompt
you to set a Load Balancer Address.

This can also be set by adding
`loadBalancerAddress: "<Load Balancer FQDN or IP>:6443"` (under the
kubernetes spec) to the installer-override.yaml patch file `spec:`
section.

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: kubernetes: loadBalancerAddress: "<Load Balancer FQDN or
IP>:6443"

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
