System Requirements for an Embedded Cluster Install
===================================================

While the Turbine platform can be installed on a single node for
testing, a 3+ node cluster is recommended for production environments to
provide redundancy and high availability (HA). Any multiple node cluster
must have an odd number of total nodes.

This table details the recommended sizing and data per node:

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | 3 Node      | 3 Node      | 3 Node      |
|             |             | Cluster -   | Cluster -   | Cluster -   |
|             |             | Small       | Medium      | Large       |
+=============+=============+=============+=============+=============+
| **CPU**     | 8 CPU cores | 8 CPU cores | 16 CPU      | 32 CPU      |
|             |             |             | cores       | cores       |
+-------------+-------------+-------------+-------------+-------------+
| **MEMORY**  | 32 GB RAM   | 32 GB RAM   | 64 GB RAM   | 128 GB RAM  |
+-------------+-------------+-------------+-------------+-------------+
| **STORAGE** | 600 GB SSD  | 600 GB SSD  | 1 TB SSD /  | 1 TB SSD /  |
|             | / 3000 IOPS | / 3000 IOPS | 3000 IOPS   | 3000 IOPS   |
|             | per node    | per node    | per node    | per node    |
+-------------+-------------+-------------+-------------+-------------+
| **Record    | Records     | Records     | Records     | Records     |
| Creation    | created in  | created in  | created in  | created in  |
| Boundaries  | a day:      | a day:      | a day: 1    | a day: 1    |
| + Active    | 250,000     | 500,000     | million     | million     |
| Users**     |             |             |             |             |
|             | Total       | Total       | Total       | Total       |
|             | records: 5  | records: 20 | records: 20 | records: 20 |
|             | million     | million     | million     | million     |
|             |             |             |             |             |
|             | Active      | Active      | Active      | Active      |
|             | users: 10   | users: 30   | users: 50   | users: 200  |
+-------------+-------------+-------------+-------------+-------------+
| **          | I           | I           | I           | I           |
| Integration | ntegrations | ntegrations | ntegrations | ntegrations |
| Cal         | in use < 20 | in use < 20 | in use < 20 | in use > 20 |
| culations** | average     | average     | average     | average     |
|             |             |             |             |             |
|             | Integration | Integration | Integration | Integration |
|             | actions/day | actions/day | actions/day | actions/day |
|             | < 250,000   | < 500,000   | < 1 million | < 1 million |
+-------------+-------------+-------------+-------------+-------------+
| **Pods**    | API: 1      | API: 3      | API: 3      | API: 6      |
|             |             |             |             |             |
|             | Tasks: 1    | Tasks: 3    | Tasks: 3    | Tasks: 9    |
|             |             |             |             |             |
|             | Web: 1      | Web: 3      | Web: 3      | Web: 3      |
|             |             |             |             |             |
|             | MongoDB: 1  | MongoDB: 3  | MongoDB: 3  | MongoDB: 3  |
+-------------+-------------+-------------+-------------+-------------+

External MongoDB Resource Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table illustrates the resource recommendations (per node) for a
standalone mongo deployment. All of these values can be subtracted from
the system requirements above when allocating resources for the
remainder of the Turbine pods. For more information about deploying on
an External MongoDB cluster, see `Deploy Turbine with an External
MongoDB Cluster <../deploy-with-an-external-mongodb-cluster.htm>`__.

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | 3 Node      | 3 Node      | 3 Node      |
|             |             | Cluster -   | Cluster -   | Cluster -   |
|             |             | Sm          | Med         | Lg          |
+=============+=============+=============+=============+=============+
| **CPU**     | 4 CPU Cores | 4 CPU Cores | 8 CPU Cores | 8 CPU Cores |
+-------------+-------------+-------------+-------------+-------------+
| **Ram**     | 16 GB RAM   | 16 GB RAM   | 16 GB RAM   | 32 GB RAM   |
+-------------+-------------+-------------+-------------+-------------+
| **Storage** | 300 GB SSD  | 300 GB SSD  | 700 GB SSD  | 700 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per node    | per node    | per node    | per node    |
+-------------+-------------+-------------+-------------+-------------+

Remaining Turbine Cluster Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table illustrates the resources necessary for the remainder of
Turbine if you are using external MongoDB resources:

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | 3 Node      | 3 Node      | 3 Node      |
|             |             | Cluster -   | Cluster -   | Cluster -   |
|             |             | Sm          | Med         | Lg          |
+=============+=============+=============+=============+=============+
| **CPU**     | 4 CPU Cores | 4 CPU Cores | 8 CPU Cores | 24 CPU      |
|             |             |             |             | Cores       |
+-------------+-------------+-------------+-------------+-------------+
| **Ram**     | 16 GB RAM   | 16 GB RAM   | 48 GB RAM   | 96 GB RAM   |
+-------------+-------------+-------------+-------------+-------------+
| **Storage** | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per node    | per node    | per node    | per node    |
+-------------+-------------+-------------+-------------+-------------+

Resource Utilization Thresholds
-------------------------------

All nodes need to stay below certain resource utilization thresholds to
ensure that pods always have available resources to operate in. If any
of the following thresholds are exceeded on a node, all pods on that
node will be removed until the resource utilization is addressed:

+----------------------------------+----------------------------------+
| Resource                         | Threshold                        |
+==================================+==================================+
| Memory                           | Less than 100                    |
|                                  | `Mebibytes <https://simple       |
|                                  | .wikipedia.org/wiki/Mebibyte>`__ |
|                                  | (MiB) Available                  |
+----------------------------------+----------------------------------+
| Disk Space (/var/lib/containerd  | Less than 15% Available          |
| partition)                       |                                  |
+----------------------------------+----------------------------------+
| Disk Space (/var/lib/kubelet     | Less than 10% Available          |
| partition)                       |                                  |
+----------------------------------+----------------------------------+
| Disk Inodes (/var/lib/kubelet    | Less than 5% Available           |
| partition)                       |                                  |
+----------------------------------+----------------------------------+

Backup Requirements
-------------------

Taking a snapshot requires enough free disk space for a compressed
archive of the Swimlane database to be saved in ephemeral storage before
it is uploaded to the snapshot destination. Free disk space on the
cluster at ``/var/lib/kubelet`` should be greater than or equal to the
size of the uncompressed database to ensure there is no disk pressure
during the snapshot process.

Cloud Service Sizing Tools
--------------------------

+----------------------------------+----------------------------------+
| Sizing Calculators               | Sizing Guides                    |
+==================================+==================================+
| Instance Sizing Calculators AWS  | `Instance Sizing                 |
|                                  | AWS <https://aws.am              |
|                                  | azon.com/ec2/instance-types/>`__ |
+----------------------------------+----------------------------------+
| Instance Sizing Calculators      | `Instance Sizing                 |
| Azure                            | Azur                             |
|                                  | e <https://docs.microsoft.com/en |
|                                  | -us/azure/virtual-machines/windo |
|                                  | ws/sizes-general#dsv2-series>`__ |
+----------------------------------+----------------------------------+
| Instance Sizing Calculators GCP  | `Instance Sizing                 |
|                                  | GCP <https://cloud.google.co     |
|                                  | m/compute/docs/machine-types>`__ |
+----------------------------------+----------------------------------+

**Important!** Most cloud providers limit IOPS for disks and for
instances/virtual machines. Consult your provider's documentation to
ensure the effective IOPS for the cluster nodes meet the requirements in
the sizing table above.

+----------+----------------------------------------------------------+
| Provider | Documentation                                            |
+==========+==========================================================+
| AWS      | `Disk Performance                                        |
|          | Limits <https://docs.aws.amaz                            |
|          | on.com/AWSEC2/latest/UserGuide/ebs-volume-types.html>`__ |
+----------+----------------------------------------------------------+
| AWS      | `Instance Performance                                    |
|          | Limits <https://docs.aws.a                               |
|          | mazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html>`__ |
+----------+----------------------------------------------------------+
| Azure    | `Disk Performance                                        |
|          | Limits <https://docs.microsoft.com/en                    |
|          | -us/azure/virtual-machines/disks-scalability-targets>`__ |
+----------+----------------------------------------------------------+
| Azure    | `VM Performance                                          |
|          | Limits <https://docs.micr                                |
|          | osoft.com/en-us/azure/virtual-machines/sizes-general>`__ |
+----------+----------------------------------------------------------+
| GCP      | `Disk Performance                                        |
|          | Limits <htt                                              |
|          | ps://cloud.google.com/compute/docs/disks/performance>`__ |
+----------+----------------------------------------------------------+
| GCP      | `VM Performance                                          |
|          | Limits <https://cloud.google.com/com                     |
|          | pute/docs/disks/performance#machine-type-disk-limits>`__ |
+----------+----------------------------------------------------------+

Critical Prerequisites
----------------------

The following operating systems have been tested by Swimlane for your
node setup: 

-  **CentOS 7:** 7.7, 7.8, 7.9

-  **CentOS 8:** Stream Release 8

-  **RHEL 7:** 7.9

-  **RHEL 8:** 8.6, 8.9

-  **RHEL 9:** 9.2, 9.3

-  **Rocky Linux 9:** 9.2

-  **Ubuntu:** 20.04.6 LTS, 22.04.2 LTS

-  **Amazon Linux:** Amazon Linux 2

Prerequisites for Airgap Installation on Rocky Linux or RHEL 9.x
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before installation Arigap, make sure to install the following:

-  nfs-utils

-  conntrack-tools

-  socat

-  git

-  fio

Use the following command to install:

sudo dnf -y install nfs-utils conntrack-tools socat git fio
container-selinux tar zip unzip

For Rocky Linux 9.2, run the following command to change the file
permissions:

sudo chmod 755 /etc/rc.d/rc.local

For each node, ensure that you have: 

-  Sudo/Root access

-  NUMA (non-uniform memory access) disabled.

-  Accurate system time.

**Important!** To maintain accurate system time you must have Network
Time Protocol (NTP) or a similar time-sync service.

-  Static IPs (dynamic IPs are **not** supported).

-  Static node hostnames (node hostnames cannot change).

-  No previous installs of Kubernetes, Docker, or Containerd.

   -  Disable any automatic updates for Kubernetes and Docker-related
      packages. Updating these will be handled through the Turbine
      Platform Installer.

-  IPv6 and dual stack networks are not supported.

-  IP forwarding enabled.

   -  The installer can handle enabling IPv4 forwarding but you must
      ensure it remains enabled on all cluster nodes going forward, even
      after reboot.

Critical CPU Architecture Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  CPU architecture must be compatible with MongoDB, unless an external
   Mongo solution is used. See the MongoDB `Platform Support
   Matrix <https://www.mongodb.com/docs/v5.0/administration/production-notes/#platform-support-matrix>`__
   for more information.

Critical Network Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The IP ranges ``10.32.0.0/20``\ and ``10.96.0.0/22`` are the default
   IP ranges used internally in the cluster for Kubernetes service and
   pod networking. If these are in use in your network and routable by
   the cluster nodes, the internal cluster IP ranges will need to be
   overridden. See `Define Custom Pod and Service
   Subnets <../overriding-installer-settings/define-custom-pod-and-service-subnets.htm>`__
   for instructions on overriding the internal cluster IP ranges.

-  Ensure all nodes are in the same cloud provider region or physical
   data center network. Nodes behind different WAN links in the same
   cluster are not supported.

Critical Prerequisites for Airgapped Network Installations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For access to these optional services, ensure you have these things
within the airgapped network:

-  LDAP login functionality requires an LDAP server inside of the
   airgapped subnet, or access to outside subnets or the IP or Domain
   where the LDAP server resides. In order to open these ports,
   non-secure LDAP uses port 389, but LDAPS (Secure LDAP) uses port 636
   and is preferred.

-  SSO login functionality requires the service to be able to reach
   inside the airgapped network (where the Turbine instance resides).

-  Email functionality requires the Turbine instance to use a
   functioning mail proxy that resides within the airgapped subnet,
   access to outside subnets where an email server resides, or to your
   chosen email server on the internet. In order to open these ports,
   non-secure SMTP uses port 25, but the Secure SMTP uses port 587 and
   is preferred.

-  In order to provide threat intelligence enrichment, the SOC Solution
   requires access to the following Threat Intelligence URLs:

   -  VirusTotal - `https://virustotal.com <https://virustotal.com/>`__
      and subdomains

   -  URL Haus - `URLhaus - Malware URL
      exchange <https://urlhaus.abuse.ch/>`__ - and subdomains

   -  Recorded Future - `Recorded Future: Securing Our World With
      Intelligence <http://recordedfuture.com/>`__ and subdomains

   -  IPQualityScore - `Fraud Prevention \| Bot Detection \| Bot
      Protection \| Prevent Fraud with
      IPQS <http://ipqualityscore.com/>`__ and subdomains

   -  Each of these requires TCP port 443 access and TCP port 80 access.

Critical Load Balancer Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A load balancer that supports hairpinning is **REQUIRED** for HA
installations.

Here are some suggested load balancers and configurations that you can
use:

-  Layer 7 Load Balancers:

   -  `AWS Application Load
      Balancer <../infrastructure-examples/aws-application-load-balancer.htm>`__
   -  `Azure Standard Application
      Gateway <../infrastructure-examples/azure-standard-applicatin-gateway.htm>`__
   -  `Azure Standard_v2 Application
      Gateway <../infrastructure-examples/Azure%20Standard_v2%20Application.htm>`__
   -  `GCP HTTPS Load
      Balancer <../infrastructure-examples/gcp-https-load-balancer.htm>`__
   -  `HA
      Proxy <../infrastructure-examples/haproxy-load-balancer.htm#http-mode-layer-7-haproxy>`__

-  TCP Forwarding Layer 4 Load Balancers:

   -  `AWS Network Load
      Balancer <../infrastructure-examples/aws-network-load-balancer.htm>`__
   -  `Azure Standard Load
      Balancer <../infrastructure-examples/azure-load-balancer.htm>`__
   -  `GCP TCP Load
      Balancer <../infrastructure-examples/gcp-tcp-load-balancer.htm>`__
   -  `HA
      Proxy <../infrastructure-examples/haproxy-load-balancer.htm#tcp-mode-layer-4-haproxy>`__

   More detailed information about specific load balancer configurations
   can be found in the `Infrastructure
   Examples <../infrastructure-examples/infrastructure-examples.htm>`__
   topic.

Extra Considerations for Load Balancer Set Up on Nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each node in the cluster needs to be reachable by the load balancer on
these ports:

-  TCP 443 (Turbine Platform UI)
-  TCP 8800 (Turbine Platform Installer UI)
-  TCP 6443 (Kubernetes API)
-  TCP 80 (Optional - HTTP to HTTPS redirect for the Turbine Platform
   UI)

A load balancer is required for the Kubernetes API and the Turbine
Platform Installer.

**Note:** If you are using a Layer 4 load balancer for the Turbine
Platform Installer and the Turbine platform, it can be combined with the
Kubernetes API load balancer so that only one is required.

The **Kubernetes API load balancer** must be a Layer 4 load balancer.

-  The front-end port on the load balancer should be 6443 (Kubernetes
   Control Plane).
-  The back-end port on the load balancer to the nodes should be 6443.

The **Turbine Platform Installer** and the **Turbine platform** load
balancer can be either a Layer 4 or Layer 7 load balancer.

-  Front-end ports on the load balancer should be 443 (Turbine platform)
   and 8800 (Turbine Platform Installer).
-  Backend ports on the load balancer map different based on load
   balancer type
-  For Layer 7 load balancers:

   -  443 should map to 4443
   -  8800 should map to 8800

-  For Layer 4 load balancers:

   -  443 should map to 443
   -  8800 should map to 8800

Other Critical Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  For production environments use an Amazon S3 bucket or S3-compatible
   storage solution to store snapshots externally so that a total
   cluster outage does not result in a loss of snapshots.

   -  If Amazon S3 is unavailable for use then an S3-compatible solution
      like `min.io <https://min.io/>`__ can be used but should be
      installed external to the cluster.

-  In order to maximize disk space, Swimlane recommends that you set up
   partitions. Here are the minimum recommended partition sizes:

+------------------+--------+------------------+------------------+---+
| Partition        | Size   | Description of   | Storage concerns |   |
|                  |        | highest storage  | and what to look |   |
|                  |        | consumers by     | out for:         |   |
|                  |        | function:        |                  |   |
+==================+========+==================+==================+===+
| /                | 50 GB  | Base OS,         | Local logs       |   |
|                  |        | installation     | storage and log  |   |
|                  |        | files, logs, and | rotation         |   |
|                  |        | other smaller    | policies         |   |
|                  |        | cluster          |                  |   |
|                  |        | dependencies     |                  |   |
+------------------+--------+------------------+------------------+---+
| /va              | 100 GB | Container        | Image growth     |   |
| r/lib/containerd |        | images, logs,    | (unused images   |   |
|                  |        | and runtime      | get pruned when  |   |
|                  |        | volumes          | the default      |   |
|                  |        |                  | images threshold |   |
|                  |        |                  | of 15% is        |   |
|                  |        |                  | reached) and     |   |
|                  |        |                  | container log    |   |
|                  |        |                  | growth           |   |
+------------------+--------+------------------+------------------+---+
| /var/lib/kubelet | 100 GB | Kubernetes       | Snapshot size    |   |
|                  |        | runtime,         | and pod          |   |
|                  |        | ephemeral        | temporary        |   |
|                  |        | storage, and in  | storage          |   |
|                  |        | flight snapshot  | increasing       |   |
|                  |        | temporary        |                  |   |
|                  |        | storage          |                  |   |
+------------------+--------+------------------+------------------+---+
| /var/openebs     | 300 GB | Persistent       | Amount of        |   |
|                  |        | storage          | Turbine data and |   |
|                  |        | subsystem - used | integrations     |   |
|                  |        | for database     |                  |   |
|                  |        | volumes          | Local storage of |   |
|                  |        | Swimlane         | snapshots (see   |   |
|                  |        | Platform         | note below)      |   |
|                  |        | Installer        |                  |   |
|                  |        | database, and    |                  |   |
|                  |        | completed local  |                  |   |
|                  |        | snapshots        |                  |   |
+------------------+--------+------------------+------------------+---+
| /var/log         | 5 GB   | Storage for the  | 100% usage of    |   |
|                  |        | Kubernetes API   | /v               |   |
|                  |        | server logs      | ar/log/apiserver |   |
|                  |        |                  | will cause a     |   |
|                  |        |                  | Swimlane outage  |   |
|                  |        |                  | until space is   |   |
|                  |        |                  | retrieved        |   |
+------------------+--------+------------------+------------------+---+

The directory ``/var/lib/kurl/`` is the default location for installer
temporary files but the path can be overridden at install time. The
partition that path is on needs to have 20GB available during the
install to ensure successful installation and can be removed after the
installation has completed.

**Note:** Production environments should be using external storage
locations for snapshots. If you plan to store snapshots locally in a
test/lab environment, you will need to make the /opt partition larger to
accommodate them.

**Note:** If you plan to use a separate disk or volume for
``/var/openebs`` ensure it meets the minimum IOPS defined in the table
with recommended data and sizing at the beginning of this topic.

**Note:** The partition /var/log needs at least 5GB available to avoid
degrading a Turbine cluster or outage.

Domain Name System (DNS)
~~~~~~~~~~~~~~~~~~~~~~~~

Use the IP or DNS record for the Kubernetes API load balancer to specify
the load balancer address during the initial installation.

A DNS record should be created that points to the Turbine Platform
Installer and Turbine platform load balancer. This will be the DNS
address specified when you configure Turbine after the installation.
Append that address with ``:8800`` in order to access the Turbine
Platform Installer UI.

If only one Layer 4 load balancer is used then a single DNS record can
be created and used for both purposes.

**Important!** You must use DNS-compliant records. A DNS record can be
up to 63-characters long and can only contain letters, numbers, and
hyphens. The record cannot start or end with a hyphen, nor have
consecutive hyphens.

Exceptions to Network Access Control Lists (ACL)
------------------------------------------------

Turbine installations on servers with tight Network Access Control (NAC)
will need several exceptions made to properly install, license, and
stage a Turbine deployment with the Turbine Platform Installer. See the
tables below for the Outbound and Inbound exceptions.

Required Outbound URL ACL Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+----------------------------------+
| Exception                        | Purpose                          |
+==================================+==================================+
| get.swimlane.io                  | Turbine platform installation    |
|                                  | script                           |
+----------------------------------+----------------------------------+
| k8s.kurl.sh                      | Turbine platform installation    |
|                                  | script                           |
+----------------------------------+----------------------------------+
| kurl.sh                          | Turbine platform installation    |
|                                  | script                           |
+----------------------------------+----------------------------------+
| kurl-sh.s3.amazonaws.com         | Turbine platform installation    |
|                                  | script dependencies              |
+----------------------------------+----------------------------------+
| registry.replicated.com          | Turbine platform container       |
|                                  | images                           |
+----------------------------------+----------------------------------+
| proxy.replicated.com             | Turbine platform container       |
|                                  | images                           |
+----------------------------------+----------------------------------+
| ghcr.io                          | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| registry.k8s.io                  | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| k8s.gcr.io                       | Turbine platform container       |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| storage.googleapis.com           | Turbine platform container       |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| quay.io                          | Turbine platform container       |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| replicated.app                   | Turbine Platform Installer       |
|                                  | license verification             |
+----------------------------------+----------------------------------+
| auth.docker.io                   | Docker authentication            |
+----------------------------------+----------------------------------+
| registry-1.docker.io             | Docker registry                  |
+----------------------------------+----------------------------------+
| production.cloudflare.docker.com | Docker infrastructure            |
+----------------------------------+----------------------------------+
| files.pythonhosted.org           | Python packages for Turbine      |
|                                  | integrations                     |
+----------------------------------+----------------------------------+
| pypi.org                         | Python packages for Turbine      |
|                                  | integrations                     |
+----------------------------------+----------------------------------+
| <LoadBalancerIP>:6443            | Kubernetes API                   |
+----------------------------------+----------------------------------+

Port Requirements
~~~~~~~~~~~~~~~~~

External Access
^^^^^^^^^^^^^^^

The following ports are required externally to allow access to the
Turbine platform components:

+-------+----------+-----------------------+-----------------------+
| Ports | Protocol | Purpose               | Access From           |
+=======+==========+=======================+=======================+
| 443   | TCP      | Turbine platform UI   | Clients that need to  |
|       |          |                       | access the Turbine    |
|       |          |                       | platform UI           |
+-------+----------+-----------------------+-----------------------+
| 80    | TCP      | Turbine platform UI   | Optional - HTTP to    |
|       |          |                       | HTTPS redirect for    |
|       |          |                       | the Turbine platform  |
|       |          |                       | UI                    |
+-------+----------+-----------------------+-----------------------+
| 8800  | TCP      | Turbine Platform      | Clients that need to  |
|       |          | Installer UI          | access the Turbine    |
|       |          |                       | Platform Installer UI |
+-------+----------+-----------------------+-----------------------+
| 22    | TCP      | Shell access          | Management            |
|       |          |                       | workstations to       |
|       |          |                       | manage the cluster    |
|       |          |                       | nodes and install     |
|       |          |                       | Turbine               |
+-------+----------+-----------------------+-----------------------+

Between Cluster Nodes
^^^^^^^^^^^^^^^^^^^^^

The following ports are required between the clusters nodes to allow
cluster operation:

+-------------+----------+-------------------------------------------+
| Ports       | Protocol | Purpose                                   |
+=============+==========+===========================================+
| 2379-2380   | TCP      | Kubernetes etcd                           |
+-------------+----------+-------------------------------------------+
| 6443        | TCP      | Kubernetes API                            |
+-------------+----------+-------------------------------------------+
| 8472        | UDP      | Kubernetes CNI                            |
+-------------+----------+-------------------------------------------+
| 10250-10252 | TCP      | Kubernetes components (kubelet,           |
|             |          | kube-scheduler, kube-controller)          |
+-------------+----------+-------------------------------------------+

From Load Balancers
^^^^^^^^^^^^^^^^^^^

The following ports are required between the cluster nodes and the load
balancer(s):

+-------+----------+-------------------------------------------------+
| Ports | Protocol | Purpose                                         |
+=======+==========+=================================================+
| 443   | TCP      | Turbine platform UI                             |
+-------+----------+-------------------------------------------------+
| 80    | TCP      | Optional - HTTP to HTTPS redirect for the       |
|       |          | Turbine platform UI                             |
+-------+----------+-------------------------------------------------+
| 8800  | TCP      | Turbine Platform Installer UI                   |
+-------+----------+-------------------------------------------------+
| 6443  | TCP      | Kubernetes API                                  |
+-------+----------+-------------------------------------------------+

Available Ports
^^^^^^^^^^^^^^^

In addition to all ports listed above in the ``Between Cluster Nodes``
table, the following ports are required to be available and unused by
other processes on each cluster node in order to install:

===== ================================================
Ports Purpose
===== ================================================
2381  Kubernetes etcd
8472  Kubernetes CNI
10248 Kubernetes kubelet health server
10249 Kubernetes kube-proxy metrics server
10257 Kubernetes kube-controller-manager health server
10259 Kubernetes kube-scheduler health server
===== ================================================

External Monitoring Considerations
----------------------------------

Swimlane recommends that any TPI installation has some amount of
external monitoring set up and set to alert when any user-defined
thresholds are met as to possible instances of your production instances
going down. Different installation scenarios may call for different
metrics to monitor for, so your implementation may vary. As a baseline,
the following metrics are recommended:

-  Are all nodes healthy?
-  Does each node have sufficient free space in all partitions?
-  Are CPU and memory usage levels within acceptable levels?
-  Is disk latency within acceptable ranges?
-  Are any pods in a not-ready state?
-  Are any deployments or StatefulSets not reporting the correct number
   of ready replicas?
-  Do any load balancers have health checks in place? Are they healthy?

Third Party Monitoring Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several third-party monitoring solutions that you can use to
monitor resource usage for a node. Any tool that you put into use should
be installed externally to the cluster so as to not interfere with
cluster operations and to be able to alert if a metric enters into a
failing scenario. These products may require that their own agents or
exporters be installed on the nodes in order to facilitate monitoring.
Any agent or exporter should be tested against your cluster to validate
that they do not interfere with Turbine operations or `port
requirements <#Port>`__.

.. toctree::
   :titlesonly:
   :caption: Related Topics

   /Content/embedded-cluster-install/infrastructure-examples/infrastructure-examples
