Analyze a Swimlane Platform Installer Support Bundle
#############

A support bundle is a collection of logs and output from the underlying
Kubernetes cluster resources. This information is invaluable for
troubleshooting as it includes tons of information about node health,
Swimlane pod health and logs, KOTS pod health and logs, and more.

The support bundle is a gzip’d tarball (.tar.gz) that can be extracted
using the tar command:

tar zxvf supportbundle-XXXX-XX-XXTYY_YY_YY.tar.gz

The support bundle is comprised of logs divided into several
directories:

-  `ceph`

   -  Logs and outputs related to the status and configuration of the
      ceph storage system used by the KOTS related pods

-  `cluster-info`

   -  Information about the Kubernetes version

-  `cluster-resources`

   -  Definitions of all of the resources running in the clusters

   -  Each resource type is a different subdirectory (deployments,
      services, statefulsets, etc.)

   -  Each resource subdirectory has a json file for each namespace that
      has that resource type

   -  Swimlane resources are in the `default` namespace

-  `kots`

   -  Logs specific to the KOTS UI and process pods

      -  `goldpinger`

         -  Goldpinger checks the network connections between each
            unique pair of nodes.

         -  Results are stored as JSON in
            `default/kotsadm-###/goldpinger-statistics-stdout.txt`

         -  When working correctly, each ping should return a 200 status
            code

-  `swimlane`

   -  The custom support bundle collectors we have written for our
      Swimlane Platform resources

   -  Each pod type has a separate subdirectory for the logs collected
      for each pod of that type

   -  What we collect:

      -  `api`

         -  `logs` - API pod logs

         -  `pip-list` - List of python packages installed in the API
            pods

      -  `sw-mongo`

         -  `cert` - Expiration date of the MongoDB certificate

         -  `df` - Disk usage for the partitions of the MongoDB pods

         -  `free` - Memory usage of the MongoDB pods

         -  `logs` - MongoDB pod logs

         -  `mongo-version` - The version of MongoDB

         -  `stats` - MongoDB database stats

         -  `time-drift` - The current time of the MongoDB pods to use
            to compare against the support bundle date and time to check
            for time drift

         -  `top` - Top running processes in the MongoDB pods

      -  `tasks`

         -  `logs` - Tasks pod logs

         -  `pip-list` - List of python packages installed in the
            Tasks pods

      -  `tools`

         -  `environment-validator` - Output of the environment
            validator script being run from the Tools pod

         -  `logs` - Tools pod logs

         -  `ping` - A ping test done from the Tools pod to see if
            there is internet access

            -  Note: This only confirms if the node that the Tools pod
               is running on has internet access and not every node in
               the cluster

         -  `web`

            -  `logs` - Web pod logs

-  `velero`

   -  Logs for the Velero resources that handle snapshots
