Define Custom Pod and Service Subnets
#########=

By default, the Swimlane Platform Installer uses 10.32.0.0/20 for
podCIDR and 10.96.0.0/22 for serviceCIDR. If these are in use in your
network and routable by the cluster nodes, the internal cluster IP
ranges will need to be overridden. However, the installer also includes
logic to find an available subnet automatically anywhere in the
10.0.0.0/8 network. As long as the excluded subnets appear in an IP
route it should find one without conflicts.

To override the defaults, you can add serviceCIDR (under the kubernetes
spec) and podCIDR (under the flannel spec) to the
installer-override.yaml patch file `spec:` section.

For example:

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: kubernetes: serviceCIDR: "<your custom subnet>" flannel:
podCIDR: "<your custom subnet>"

Alternatively, you can leave serviceCIDR blank, and set serviceCidrRange
to 22 or /22. Then at install time, the installer will try to discover a
/22 subnet to use, which does not overlap with any IP routes already
present on the host.

__Note:__ If you provide an invalid CIDR, you may run into issues with
the installer hanging during the installation process.

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
