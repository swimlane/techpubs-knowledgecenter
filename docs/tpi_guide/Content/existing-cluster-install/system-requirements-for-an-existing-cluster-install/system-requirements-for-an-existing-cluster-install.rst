System Requirements for an Existing Cluster Install
===================================================

Here are the system requirements for installing Turbine on an existing
Kubernetes cluster:

-  A Kubernetes 1.19.x, 1.20.x, 1.21.x, 1.22.x, 1.23.x, 1.24.x, 1.25.x,
   or 1.26.x compliant cluster.

-  A persistent and reliable StorageClass to use for the MongoDB and
   RabbitMQ pods persistent volumes.

   -  The required filesystem for the MongoDB StorageClass is XFS.

-  3+ node cluster for production environments to provide redundancy and
   high availability (HA).

   -  Ensure all nodes are in the same cloud provider region or physical
      data center network. Nodes behind different WAN links in the same
      cluster are not supported.

-  CPU architecture must be compatible with MongoDB, unless an external
   Mongo solution is used.

   -  See the MongoDB `Platform Support
      Matrix <https://www.mongodb.com/docs/v5.0/administration/production-notes/#platform-support-matrix>`__
      for more information.

-  Production environments should have snapshots set up and stored
   externally from the cluster to ensure that they can be retrieved in
   the event of a total cluster loss.

   -  See `Backup and Restore on an Existing Cluster with
      Snapshots <../backup-and-restore-on-an-existing-cluster-with-snapshots.htm>`__
      for more information on how to set up snapshots and compatible
      providers.

-  A load balancer or ingress controller to load balance to the Turbine
   platform UI.

   -  Must be configured for TLS communication to the backend.
   -  If your load balancer or ingress controller requires explicit
      trust with the certificate presented by the backend service then
      you must upload a trusted certificate for the Swimlame Web
      backend.
   -  The Turbine platform UI must be accessed externally via port 443.
      Accessing Turbine over any other port is not supported.
   -  Must support websockets.

-  Velero 1.9.0 installed in the cluster to handle backup and restores
   with snapshots.

   -  See `Backup and Restore on an Existing Cluster with
      Snapshots <../backup-and-restore-on-an-existing-cluster-with-snapshots.htm#install-velero>`__
      for instructions to install Velero into your cluster.

Limitations
-----------

-  Changing annotations, labels, resources, node selector, tolerations,
   or affinity settings for the Turbine Platform Installer pods is not
   currently supported. These settings can, however, be set for the
   Turbine platform pods on the config page.
-  The StorageClass for the Turbine Platform Installer pods is required
   to be ``default`` and cannot currently be changed.
-  Multiple TPI installs into the same cluster is not currently
   supported.

Backup Requirements
~~~~~~~~~~~~~~~~~~~

Taking a snapshot requires enough free disk space for a compressed
archive of the Swimlane database to be saved in ephemeral storage before
it is uploaded to the snapshot destination. Free disk space on the
cluster at ``/var/lib/kubelet`` should be greater than or equal to the
size of the uncompressed database to ensure there is no disk pressure
during the snapshot process.

Additional Offline Install Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the requirements above, installs into an offline
(airgapped) Kubernetes cluster have the following additional
requirements:

-  A private docker image registry accessible by the Kubernetes cluster
   and jumpbox is required for installation and ongoing operation.

   -  The registry needs to be trusted by your Kubernetes cluster in
      order to be be able to pull images. See the `Kubernetes
      documentation <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>`__
      for more information.

-  A jumpbox that has access to the internet, access to the airgapped
   kubernetes cluster, and a browser from which you can access the
   Turbine Platform Installer.

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

Cluster Resources
~~~~~~~~~~~~~~~~~

Your cluster needs the following resources available to meet the usage
thresholds for the given deployment sizes:

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | Small       | Medium      | Large       |
|             | (Dev/Test)  |             |             |             |
+=============+=============+=============+=============+=============+
| **CPU**     | 8 CPU cores | 24 CPU      | 48 CPU      | 96 CPU      |
|             |             | cores       | cores       | cores       |
+-------------+-------------+-------------+-------------+-------------+
| **MEMORY**  | 32 GB RAM   | 96 GB RAM   | 192 GB RAM  | 384 GB RAM  |
+-------------+-------------+-------------+-------------+-------------+
| **STORAGE** | 600 GB SSD  | 600 GB SSD  | 1 TB SSD /  | 1 TB SSD /  |
|             | / 3000 IOPS | / 3000 IOPS | 3000 IOPS   | 3000 IOPS   |
|             | per MongoDB | per MongoDB | per MongoDB | per MongoDB |
|             | pod         | pod         | pod         | pod         |
|             | persistent  | persistent  | persistent  | persistent  |
|             | volume      | volume      | volume      | volume      |
+-------------+-------------+-------------+-------------+-------------+
| **Record    | Records     | Records     | Records     | Records     |
| Creation    | created in  | created in  | created in  | created in  |
| Boundaries  | a day:      | a day:      | a day: 1    | a day: 1    |
| + Active    | 2           | 5           | m           | m           |
| Users**     | 50,000Total | 00,000Total | illionTotal | illionTotal |
|             | records: 5  | records: 20 | records: 20 | records: 20 |
|             | mi          | mi          | mi          | mi          |
|             | llionActive | llionActive | llionActive | llionActive |
|             | users: 10   | users: 30   | users: 50   | users: 200  |
+-------------+-------------+-------------+-------------+-------------+
| **          | I           | I           | I           | I           |
| Integration | ntegrations | ntegrations | ntegrations | ntegrations |
| Cal         | in use < 20 | in use < 20 | in use < 20 | in use > 20 |
| culations** | average     | average     | average     | average     |
|             | Integration | Integration | Integration | Integration |
|             | actions/day | actions/day | actions/day | actions/day |
|             | < 250,000   | < 500,000   | < 1 million | < 1 million |
+-------------+-------------+-------------+-------------+-------------+
| **Pods**    | API:        | API:        | API:        | API:        |
|             | 1Tasks:     | 3Tasks:     | 3Tasks:     | 6Tasks:     |
|             | 1Web:       | 3Web:       | 3Web:       | 9Web:       |
|             | 1Reports:   | 3Reports:   | 3Reports:   | 3Reports:   |
|             | 1MongoDB: 1 | 3MongoDB: 3 | 3MongoDB: 3 | 3MongoDB: 3 |
+-------------+-------------+-------------+-------------+-------------+

External MongoDB Resource Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table illustrates the resource recommendations (per node)
for a standalone mongo deployment. All of these values can be subtracted
from the Cluster Resources above when allocating resources for the
remainder of the Turbine pods. For more information about deploying on
an External MongoDB cluster, see `Deploy Turbine with an External
MongoDB Cluster <../deploy-with-an-external-mongodb-cluster.htm>`__.

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | Small       | Medium      | Large       |
+=============+=============+=============+=============+=============+
| **CPU**     | 4 CPU Cores | 4 CPU Cores | 8 CPU Cores | 8 CPU Cores |
+-------------+-------------+-------------+-------------+-------------+
| **Ram**     | 16 GB RAM   | 16 GB RAM   | 16 GB RAM   | 32 GB RAM   |
+-------------+-------------+-------------+-------------+-------------+
| **Storage** | 300 GB SSD  | 300 GB SSD  | 700 GB SSD  | 700 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per MongoDB | per MongoDB | per MongoDB | per MongoDB |
|             | pod         | pod         | pod         | pod         |
|             | persistent  | persistent  | persistent  | persistent  |
|             | volume      | volume      | volume      | volume      |
+-------------+-------------+-------------+-------------+-------------+

Remaining Turbine Cluster Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This table illustrates the resources necessary for the remainder of
Turbine if you are using external MongoDB resources:

+-------------+-------------+-------------+-------------+-------------+
| Components  | Single Node | Small       | Medium      | Large       |
+=============+=============+=============+=============+=============+
| **CPU**     | 4 CPU Cores | 12 CPU      | 24 CPU      | 72 CPU      |
|             |             | Cores       | Cores       | Cores       |
+-------------+-------------+-------------+-------------+-------------+
| **Ram**     | 16 GB RAM   | 48 GB RAM   | 144 GB RAM  | 288 GB RAM  |
+-------------+-------------+-------------+-------------+-------------+
| **Storage** | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per node    | per node    | per node    | per node    |
+-------------+-------------+-------------+-------------+-------------+

Optional Pods
^^^^^^^^^^^^^

If you require the use of these optional pods you will need the
following additional resources available:

+----------------+---------------------+---------------------+---------------------+
| Pod            | Small               | Medium              | Large               |
+================+=====================+=====================+=====================+
| Turbine Logger | .1 CPU core1 GB RAM | .4 CPU core1 GB RAM | .5 CPU core2 GB RAM |
+----------------+---------------------+---------------------+---------------------+

See `Pod Requests and Limits <../pod-requests-and-limits.htm>`__ for a
breakdown of resources for each pod type including optional pods not
included in the table above.

Exceptions to Network Access Control Lists (ACL)
------------------------------------------------

Swimlane installations on servers with tight Network Access Control
(NAC) will need several exceptions made to properly install, license,
and stage a Swimlane deployment with the Swimlane Platform Installer.
See the tables below for the Outbound and Inbound exceptions.

Required Outbound URL ACL Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+----------------------------------+
| Exception                        | Purpose                          |
+==================================+==================================+
| get.swimlane.io                  | Swimlane platform installation   |
|                                  | script                           |
+----------------------------------+----------------------------------+
| k8s.kurl.sh                      | Swimlane platform installation   |
|                                  | script                           |
+----------------------------------+----------------------------------+
| kurl.sh                          | Swimlane platform installation   |
|                                  | script                           |
+----------------------------------+----------------------------------+
| kurl-sh.s3.amazonaws.com         | Swimlane platform installation   |
|                                  | script dependencies              |
+----------------------------------+----------------------------------+
| registry.replicated.com          | Swimlane platform container      |
|                                  | images                           |
+----------------------------------+----------------------------------+
| proxy.replicated.com             | Swimlane platform container      |
|                                  | images                           |
+----------------------------------+----------------------------------+
| k8s.gcr.io                       | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| ghcr.io                          | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| registry.k8s.io                  | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| storage.googleapis.com           | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| quay.io                          | Swimlane platform container      |
|                                  | dependency images                |
+----------------------------------+----------------------------------+
| replicated.app                   | Swimlane Platform Installer      |
|                                  | license verification             |
+----------------------------------+----------------------------------+
| auth.docker.io                   | Docker authentication            |
+----------------------------------+----------------------------------+
| registry-1.docker.io             | Docker registry                  |
+----------------------------------+----------------------------------+
| production.cloudflare.docker.com | Docker infrastructure            |
+----------------------------------+----------------------------------+
| files.pythonhosted.org           | Python packages for Swimlane     |
|                                  | integrations                     |
+----------------------------------+----------------------------------+
| pypi.org                         | Python packages for Swimlane     |
|                                  | integrations                     |
+----------------------------------+----------------------------------+
| <LoadBalancerIP\\>:6443          | Kubernetes API                   |
+----------------------------------+----------------------------------+

 

Port Requirements
~~~~~~~~~~~~~~~~~

+-------+----------+-----------------------+-----------------------+
| Ports | Protocol | Purpose               | Access From           |
+=======+==========+=======================+=======================+
| 443   | TCP      | Swimlane platform UI  | Clients that need to  |
|       |          |                       | access the Swimlane   |
|       |          |                       | platform UI           |
+-------+----------+-----------------------+-----------------------+
| 80    | TCP      | Swimlane platform UI  | Optional - HTTP to    |
|       |          |                       | HTTPS redirect for    |
|       |          |                       | the Swimlane platform |
|       |          |                       | UI                    |
+-------+----------+-----------------------+-----------------------+
| 8800  | TCP      | Swimlane              | Clients that need to  |
|       |          | Platform Installer UI | access the Swimlane   |
|       |          |                       | Platform Installer UI |
+-------+----------+-----------------------+-----------------------+
| 22    | TCP      | Shell access          | Management            |
|       |          |                       | workstations to       |
|       |          |                       | manage the cluster    |
|       |          |                       | nodes and install     |
|       |          |                       | Swimlane              |
+-------+----------+-----------------------+-----------------------+

External Monitoring Considerations
----------------------------------

Swimlane recommends that any TPI installation has some amount of
external monitoring set up and set to alert when any user-defined
thresholds are met as to possible cases of your production instances
going down. Different installation scenarios may call for different
metrics to monitor, so your implementation may vary. As a baseline the
following metrics are recommended for nodes that are running Turbine
pods:

-  Are all nodes healthy?
-  Does each node have sufficient free space in all partitions?
-  Are CPU and memory usage levels within acceptable levels?
-  Is disk latency within acceptable ranges?
-  Are any pods in an not ready state?
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
that they do not interfere with Turbine operations.

.. toctree::
   :titlesonly:
   :caption: Related Topics

   /Content/existing-cluster-install/system-requirements-for-an-existing-cluster-install/tpi-existing-cluster-architecture-diagrams
