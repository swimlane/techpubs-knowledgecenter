System Requirements for an Existing Cluster Install
############===

Here are the system requirements for installing Swimlane on an existing
Kubernetes cluster:

-  A Kubernetes 1.19.x, 1.20.x, 1.21.x, 1.22.x, 1.23.x, 1.24.x, 1.25.x,
   or 1.26.x compliant cluster

   -  Swimlane has tested and verified compatibility with the following
      managed Kubernetes providers:

      -  Amazon EKS
      -  Azure AKS
      -  Google GKE
      -  K3OS v0.20.6-k3s1r0
      -  OpenShift 4.6.27

         -  Versions after this have a DNS resolution bug that prevents
            Swimlane from installing properly and can't be used until
            that is resolved. See this `Red Hat
            Bug <https://bugzilla.redhat.com/show_bug.cgi?id=1967766>`__
            for more information.

-  A persistent and reliable StorageClass to use for the MongoDB pods
   persistent volumes.

   -  The required filesystem for the MongoDB StorageClass is XFS.

   -  CPU architecture must be compatible with MongoDB, unless an
      external Mongo solution is used.

   -  See the MongoDB `Platform Support
      Matrix <https://www.mongodb.com/docs/v5.0/administration/production-notes/#platform-support-matrix>`__
      for more information.

-  3+ node cluster for production environments to provide redundancy and
   high availability (HA).

   -  Ensure all nodes are in the same cloud provider region or physical
      data center network. Nodes behind different WAN links in the same
      cluster are not supported.

-  Production environments should have snapshots set up and stored
   externally from the cluster to ensure that they can be retrieved in
   the event of a total cluster loss.

   -  See `Backup and Restore on an Existing Cluster with
      Snapshots <../backup-and-restore-on-an-existing-cluster-with-snapshots.htm>`__
      for more information on how to set up snapshots and compatible
      providers.

-  A load balancer or ingress controller to load balance to the Swimlane
   platform UI.

   -  Must be configured for TLS communication to the backend.
   -  If your load balancer or ingress controller requires explicit
      trust with the certificate presented by the backend service then
      you must upload a trusted certificate for the Swimlame Web
      backend.
   -  The Swimlane platform UI must be accessed externally via port 443.
      Accessing Swimlane over any other port is not supported.
   -  Must support websockets.

-  Velero 1.9.0 installed in the cluster to handle backup and restores
   with snapshots.

   -  See `Backup and Restore on an Existing Cluster with
      Snapshots <../backup-and-restore-on-an-existing-cluster-with-snapshots.htm#install-velero>`__
      for instructions to install Velero into your cluster.

Limitations
####---

-  Changing annotations, labels, resources, node selector, tolerations,
   or affinity settings for the Swimlane Platform Installer pods is not
   currently supported. These settings can, however, be set for the
   Swimlane platform pods on the config page.
-  The StorageClass for the Swimlane Platform Installer pods is required
   to be `default` and cannot currently be changed.
-  Multiple SPI installs into the same cluster is not currently
   supported.

Backup Requirements
############~~~

Taking a snapshot requires enough free disk space for a compressed
archive of the Swimlane database to be saved in ephemeral storage before
it is uploaded to the snapshot destination. Free disk space on the
cluster at `/var/lib/kubelet` should be greater than or equal to the
size of the uncompressed database to ensure there is no disk pressure
during the snapshot process.

Additional Offline Install Requirements
###########################~~~

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
   Swimlane Platform Installer.

Cluster Resources
############~

Your cluster needs the following resources available to meet the usage
thresholds for the given deployment sizes:

+######-+######-+######-+######-+######-+
| Components  | Single Node | Small       | Medium      | Large       |
|             | (Dev/Test)  |             |             |             |
+###=+###=+###=+###=+###=+
| __CPU__     | 8 CPU cores | 24 CPU      | 48 CPU      | 96 CPU      |
|             |             | cores       | cores       | cores       |
+######-+######-+######-+######-+######-+
| __MEMORY__  | 32 GB RAM   | 96 GB RAM   | 192 GB RAM  | 384 GB RAM  |
+######-+######-+######-+######-+######-+
| __STORAGE__ | 600 GB SSD  | 600 GB SSD  | 1 TB SSD /  | 1 TB SSD /  |
|             | / 3000 IOPS | / 3000 IOPS | 3000 IOPS   | 3000 IOPS   |
|             | per MongoDB | per MongoDB | per MongoDB | per MongoDB |
|             | pod         | pod         | pod         | pod         |
|             | persistent  | persistent  | persistent  | persistent  |
|             | volume      | volume      | volume      | volume      |
+######-+######-+######-+######-+######-+
| __Record    | Records     | Records     | Records     | Records     |
| Creation    | created in  | created in  | created in  | created in  |
| Boundaries  | a day:      | a day:      | a day: 1    | a day: 1    |
| + Active    | 250,000     | 500,000     | million     | million     |
| Users__     |             |             |             |             |
|             | Total       | Total       | Total       | Total       |
|             | records: 5  | records: 20 | records: 20 | records: 20 |
|             | million     | million     | million     | million     |
|             |             |             |             |             |
|             | Active      | Active      | Active      | Active      |
|             | users: 10   | users: 30   | users: 50   | users: 200  |
+######-+######-+######-+######-+######-+
| __          | I           | I           | I           | I           |
| Integration | ntegrations | ntegrations | ntegrations | ntegrations |
| Cal         | in use < 20 | in use < 20 | in use < 20 | in use > 20 |
| culations__ | average     | average     | average     | average     |
|             |             |             |             |             |
|             | Integration | Integration | Integration | Integration |
|             | actions/day | actions/day | actions/day | actions/day |
|             | < 250,000   | < 500,000   | < 1 million | < 1 million |
+######-+######-+######-+######-+######-+
| __Pods__    | API: 1      | API: 3      | API: 3      | API: 6      |
|             |             |             |             |             |
|             | Tasks: 1    | Tasks: 3    | Tasks: 3    | Tasks: 9    |
|             |             |             |             |             |
|             | Web: 1      | Web: 3      | Web: 3      | Web: 3      |
|             |             |             |             |             |
|             | Reports: 1  | Reports: 3  | Reports: 3  | Reports: 3  |
|             |             |             |             |             |
|             | MongoDB: 1  | MongoDB: 3  | MongoDB: 3  | MongoDB: 3  |
+######-+######-+######-+######-+######-+

External MongoDB Resource Recommendations
##############################~

The following table illustrates the resource recommendations (per node)
for a standalone mongo deployment. All of these values can be subtracted
from the Cluster Resources above when allocating resources for the
remainder of the Swimlane pods. For more information about deploying on
an External MongoDB cluster, see `Deploy Swimlane with an External
MongoDB Cluster <../deploy-with-an-external-mongodb-cluster.htm>`__.

+######-+######-+######-+######-+######-+
| Components  | Single Node | Small       | Medium      | Large       |
+###=+###=+###=+###=+###=+
| __CPU__     | 4 CPU Cores | 4 CPU Cores | 8 CPU Cores | 8 CPU Cores |
+######-+######-+######-+######-+######-+
| __Ram__     | 16 GB RAM   | 16 GB RAM   | 16 GB RAM   | 32 GB RAM   |
+######-+######-+######-+######-+######-+
| __Storage__ | 300 GB SSD  | 300 GB SSD  | 700 GB SSD  | 700 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per MongoDB | per MongoDB | per MongoDB | per MongoDB |
|             | pod         | pod         | pod         | pod         |
|             | persistent  | persistent  | persistent  | persistent  |
|             | volume      | volume      | volume      | volume      |
+######-+######-+######-+######-+######-+

Remaining Swimlane Cluster Resources
####################################

This table illustrates the resources necessary for the remainder of
Swimlane if you are using external MongoDB resources:

+######-+######-+######-+######-+######-+
| Components  | Single Node | Small       | Medium      | Large       |
+###=+###=+###=+###=+###=+
| __CPU__     | 4 CPU Cores | 12 CPU      | 24 CPU      | 72 CPU      |
|             |             | Cores       | Cores       | Cores       |
+######-+######-+######-+######-+######-+
| __Ram__     | 16 GB RAM   | 48 GB RAM   | 144 GB RAM  | 288 GB RAM  |
+######-+######-+######-+######-+######-+
| __Storage__ | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  | 300 GB SSD  |
|             | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS | / 3000 IOPS |
|             | per node    | per node    | per node    | per node    |
+######-+######-+######-+######-+######-+

Optional Pods
############^

If you require the use of these optional pods you will need the
following additional resources available:

+########+########+########+########+
| Pod            | Small          | Medium         | Large          |
+####+####+####+####+
| Selenium       | 1 CPU core2 GB | 1.5 CPU cores3 | 3 CPU core4 GB |
| ChromeDriver   | RAM            | GB RAM         | RAM            |
+########+########+########+########+
| Syslog         | .1 CPU core1   | .4 CPU core1   | .5 CPU core2   |
| Receiver       | GB RAM         | GB RAM         | GB RAM         |
+########+########+########+########+

See `Pod Requests and Limits <../pod-requests-and-limits.htm>`__ for a
breakdown of resources for each pod type including optional pods not
included in the table above.

External Monitoring Considerations
################--

Swimlane recommends that any SPI installation has some amount of
external monitoring set up and set to alert when any user-defined
thresholds are met as to possible cases of your production instances
going down. Different installation scenarios may call for different
metrics to monitor, so your implementation may vary. As a baseline the
following metrics are recommended for nodes that are running Swimlane
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
########################

There are several third-party monitoring solutions that you can use to
monitor resource usage for a node. Any tool that you put into use should
be installed externally to the cluster so as to not interfere with
cluster operations and to be able to alert if a metric enters into a
failing scenario. These products may require that their own agents or
exporters be installed on the nodes in order to facilitate monitoring.
Any agent or exporter should be tested against your cluster to validate
that they do not interfere with Swimlane operations.

- toctree::
   :titlesonly:
   :caption: Children:

   /Content/existing-cluster-install/system-requirements-for-an-existing-cluster-install/spi-existing-cluster-diagrams
