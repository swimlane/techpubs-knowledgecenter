Define Proxy Settings
#####=

If your environment requires a proxy server, you can add proxy settings
(under the kurl spec) to the installer-override.yaml patch file
`spec:` section.

For example:

apiVersion: cluster.kurl.sh/v1beta1 kind: Installer metadata: name:
"patch" spec: kurl: proxyAddress: http://<Proxy Address>:<Proxy Port>
additionalNoProxyAddresses: - .corporate.internal - .other.domains

-  Set `proxyAddress:` to the address and port of the proxy server.
-  Set `additionalNoProxyAddresses:` to a yaml list of IP CIDR ranges
   or domains that should not be proxied.

   -  You must add the private IPs of every cluster node

      -  Swimlane recommends specifying an IP range in CIDR notation to
         encompass future node IPs in order to prevent re-running the
         install command when addition nodes are added to the cluster.

   -  All addresses specified here will be added to the default set of
      no-proxy addresses. The default set includes:

      -  The CIDR used for assigning IPs to Kubernetes services
      -  The CIDR used for assigning IPs to pods
      -  The private IP of the host where the script runs
      -  The load balancer address for the Kubernetes API servers (on HA
         installs)
      -  The .svc and .local search domains for cluster services
      -  Add-on namespaces
      -  Other service hostnames referenced by add-ons without fully
         qualified domain names

__Important!__ Prior to installing or joining additional nodes, include
the address of all nodes in the cluster in the
`additionalNoProxyAddresses` parameter. If you do not include the
addresses of all the nodes, then you will have to re-run the install
command on _every other node_ along with the new node IP address added
to the additionalNoProxyAddresses parameter. Because of this, Swimlane
recommends that you use a range of addresses, in CIDR notation, during
the initial install and join commands instead of individual node IPs.

See `Overriding Installer
Settings <overriding-installer-settings.htm>`__ for instructions on how
to specify the installer override file during the install and join node
commands.
