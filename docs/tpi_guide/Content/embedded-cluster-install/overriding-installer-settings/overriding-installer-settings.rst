Overriding Installer Settings
=============================

Certain Turbine Platform Installer settings can be overridden at install
time to ensure proper installation and cluster operation.

Creating the Override Patch File
--------------------------------

Create the base patch file named ``override.yaml`` with the following
contents:

apiversion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name: ""
spec:

Adding Override Options to the Patch File
-----------------------------------------

Installer settings overrides are then added under the ``spec:`` section
of the ``override.yaml`` patch file. See the topics below for more
information about how to override available settings.

-  `Define High Availability and Load
   Balancer <define-high-availability-and-load-balancer-settings.htm>`__
-  `Define Custom Pod and Service
   Subnets <define-custom-pod-and-service-subnets.htm>`__
-  `Define Proxy Settings <define-proxy-settings.htm>`__
-  `Install with Firewalld
   Enabled <install-with-firewalld-enabled.htm>`__
-  `Install with SELinux Enabled <install-with-selinux-enabled.htm>`__

Using the Override Patch File
-----------------------------

| The patch file then needs to be specified as an argument to all
  install, upgrade, and node join commands to ensure the overrides are
  obeyed:

installer-spec-file=<Path to installer-override.yaml>

Install command example with the override patch file specified:

curl -sSL https://get.swimlane.io/turbine/install \| sudo bash -s ha
installer-spec-file=<Path to installer-override.yaml>

Join node command example with the override patch file specified:

curl -sSL https://kurl.sh/turbine/join.sh \| sudo bash -s \\
kubernetes-master-address=ip:port \\ kubeadm-token=token \\
kubeadm-token-ca-hash=sha256:hash \\ docker-registry-ip=ip \\
kubernetes-version=ip \\ cert-key=key \\ control-plane \\
installer-spec-file=<Path to installer-override.yaml>

.. toctree::
   :titlesonly:
   :caption: Related Topics

   /Content/embedded-cluster-install/overriding-installer-settings/define-high-availability-and-load-balancer-settings
   /Content/embedded-cluster-install/overriding-installer-settings/define-custom-pod-and-service-subnets
   /Content/embedded-cluster-install/overriding-installer-settings/define-proxy-settings
   /Content/embedded-cluster-install/overriding-installer-settings/install-with-firewalld-enabled
   /Content/embedded-cluster-install/overriding-installer-settings/install-with-selinux-enabled
