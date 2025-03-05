Add Additional Nodes to Create an HA Cluster
###########

__Important!__ This topic provides instructions on how to create a High
Availability (HA) cluster and assumes you have already run the Swimlane
Platform Installer on the first node. Please see `Install Into an
Embedded Kubernetes
Cluster <install-swimlane-on-an-embedded-kubernetes-cluster.htm>`__ if
you have not yet installed on the first node.

HA considerations
############~

-  HA clusters require at least 3 nodes and the total number of nodes
   must be an odd number.
-  Only one MongoDB pod can run on a node. For example, you need 3 nodes
   in a cluster if you want to go to 3 MongoDB pods to enable a replica
   set.
-  The first node that the initial install is running on should be in
   the target group to start. The additional nodes should only be added
   to the target groups after they’ve been joined to the cluster.

To add additional nodes to a cluster:

#. From the Swimlane Platform Installer UI, click the Cluster Management
   tab.

2. Click __Add a node__.

3. Under Add a Node, ensure that you have selected __Primary node__ and
   then click __Copy command__.

4. Go to your Command-Line Interface (CLI) and paste the copied command
   for your additional nodes.

5. Back in the Swimlane Platform Installer UI, click the Application
   tab, and then click __Config__.

6. Scroll down to the heading __HA Settings__. Select __HA Environment__
   and click __Save config__.

7. Once you save the new configuration, you are prompted to view the new
   version. Click __Go to new version__.

8. On Version History, click __Deploy__.

9.  Return to the Application tab. Once the Application Status is
    _Ready_ you have added the additional nodes to your HA Swimlane
    environment.

10. Add the new nodes to the load balancer target groups.
