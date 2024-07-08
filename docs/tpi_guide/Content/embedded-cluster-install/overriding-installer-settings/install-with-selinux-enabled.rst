Install with SELinux Enabled
============================

**Important!** Some integrations may require additional SELinux
configuration to be done by the system administrator in order to work.

By default, the installer requires that SELinux is disabled before
continuing. If you need to leave SELinux enabled you can add a flag
(under the selinuxConfig spec) to the installer-override.yaml patch file
``spec:`` section.

For example:

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: selinuxConfig: selinux: "enforcing" preserveConfig: false
disableSelinux: false

After the TPI completes, you can verify SELinux is still enabled by
running this command; the Current mode should be “enforcing:”

``sudo sestatus``

SELinux status: enabled SELinuxfs mount: /sys/fs/selinux SELinux root
directory: /etc/selinux Loaded policy name: targeted Current mode:
enforcing Mode from config file: enforcing Policy MLS status: enabled
Policy deny_unknown status: allowed Max kernel policy version: 31

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
