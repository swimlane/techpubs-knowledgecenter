Pod Requests and Limits
#####===

The following are the recommended requests and limits for each pod type
for the deployment sizes defined in the Cluster Resources section of
`System Requirements for an Existing Cluster
Install <system-requirements-for-an-existing-cluster-install/system-requirements-for-an-existing-cluster-install.htm#Cluster>`__.
Requests and limits can be raised based on your cluster's scheduling
needs and resource utilization. See `Managing Resources for
Containers <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`__
in the Kubernetes documentation for more information.

__Note:__ The MongoDB init containers stop running after their
initialization is complete and the primary MongoDB container starts.
Their resources are only used during pod start up.

Single node (Dev/Test) / Small
##############--

+######-+######-+######-+######-+######-+
| Pod Type    | CPU         | CPU Limits  | Memory      | Memory      |
|             | Requests    |             | Requests    | Limits      |
+###=+###=+###=+###=+###=+
| MongoDB     | 1000m (1    | 2000m (2    | 8G          | 18G         |
|             | CPU core)   | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| MongoDB     | 1000m (1    | 2000m (2    | 8G          | 18G         |
| Init        | CPU core)   | CPU cores)  |             |             |
| Containers  |             |             |             |             |
+######-+######-+######-+######-+######-+
| Tasks       | 4000m (4    | 4000m (4    | 4G          | 4G          |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| API         | 500m (.5    | 1000m (1    | 2G          | 4G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Web         | 200m (.2    | 400m (.4    | 1G          | 2G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Reports     | 200m (.2    | 400m (.4    | 500M        | 1G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Tools       | 100m (.1    | 200m (.2    | 500M        | 1G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Syslog      | 50m (.05    | 100m (.1    | 500M        | 1G          |
| Receiver    | CPU core)   | CPU core)   |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+
| Selenium    | 500m (.5    | 1000m (1    | 1G          | 2G          |
| C           | CPU core)   | CPU core)   |             |             |
| hromeDriver |             |             |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+

Medium
##--

+######-+######-+######-+######-+######-+
| Pod Type    | CPU         | CPU Limits  | Memory      | Memory      |
|             | Requests    |             | Requests    | Limits      |
+###=+###=+###=+###=+###=+
| MongoDB     | 4000m (4    | 8000m (8    | 16G         | 34G         |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| MongoDB     | 4000m (4    | 8000m (8    | 16G         | 34G         |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| Tasks       | 4000m (4    | 4000m (4    | 8G          | 8G          |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| API         | 1000m (1    | 2000m (2    | 6G          | 14G         |
|             | CPU core)   | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| Web         | 400m (.4    | 800m (.8    | 2G          | 4G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Reports     | 300m (.3    | 800m (.8    | 1G          | 2G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Tools       | 200m (.2    | 400m (.4    | 1G          | 2G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Syslog      | 200m (.2    | 400m (.4    | 500M        | 1G          |
| Receiver    | CPU core)   | CPU core)   |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+
| Selenium    | 700m (.7    | 1500m (1.5  | 1G          | 3G          |
| C           | CPU core)   | CPU cores)  |             |             |
| hromeDriver |             |             |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+

Large
##-

+######-+######-+######-+######-+######-+
| Pod Type    | CPU         | CPU Limits  | Memory      | Memory      |
|             | Requests    |             | Requests    | Limits      |
+###=+###=+###=+###=+###=+
| MongoDB     | 6000m (6    | 13000m (13  | 35G         | 72G         |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| MongoDB     | 6000m (6    | 13000m (13  | 35G         | 72G         |
| Init        | CPU cores)  | CPU cores)  |             |             |
| Containers  |             |             |             |             |
+######-+######-+######-+######-+######-+
| Tasks       | 4000m (4    | 4000m (4    | 8G          | 8G          |
|             | CPU cores)  | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| API         | 1000m (1    | 2000m (2    | 4G          | 8G          |
|             | CPU core)   | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| Web         | 500m (.5    | 1000m (1    | 4G          | 8G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Reports     | 600m (.6    | 1200m (1.2  | 2G          | 4G          |
|             | CPU core)   | CPU cores)  |             |             |
+######-+######-+######-+######-+######-+
| Tools       | 400m (.4    | 800m (.8    | 2G          | 4G          |
|             | CPU core)   | CPU core)   |             |             |
+######-+######-+######-+######-+######-+
| Syslog      | 200m (.2    | 500m (.5    | 1G          | 2G          |
| Receiver    | CPU core)   | CPU core)   |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+
| Selenium    | 1000m (1    | 3000M (3    | 2G          | 4G          |
| C           | CPU core)   | CPU cores)  |             |             |
| hromeDriver |             |             |             |             |
| (Optional)  |             |             |             |             |
+######-+######-+######-+######-+######-+
