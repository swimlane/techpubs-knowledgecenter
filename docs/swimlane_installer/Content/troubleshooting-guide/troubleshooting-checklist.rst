Troubleshooting Checklist
=========================

Use this topic as a checklist for troubleshooting issues with the
Swimlane Platform Installer (SPI).

Check the Configuration
-----------------------

-  Ensure that Docker and Kubelet are running.

   -  Containerd

      -  | Run

         systemctl status containerd

      -  If the service is in a failed state, search the service log for
         errors with this command: journalctl -fu containerd

   -  Kubelet

      -  | Run

         systemctl status kubelet

         | If the service is in a failed state, search the service log
           for errors with this command:

         journalctl -fu kubelet

-  Check cluster node health:

   -  | Run

      kubectl get nodes

   -  All nodes should show ``Ready`` in the ``STATUS`` column.

      | If any nodes are not showing as ``Ready``, run the following and
        look for relevant issues/errors:

      kubectl describe node NODENAME

-  Check for any pods that are not running:

   -  Run
      kubectl get pods -A \| grep -v Running \| grep -v Completed

   -  If any pods are listed:

      -  | Check the pod logs for issues with this command:

         kubectl logs --all-containers PODNAME -n NAMESPACE

      -  Check the pod describe output for issues with this command:
         kubectl describe pod PODNAME -n NAMESPACE

-  Check for errors in the events.

   -  | Run

      kubectl get events --sort-by=.metadata.creationTimestamp

-  Ensure the infrastructure is configured according to the `System
   Requirements for an Embedded Cluster
   Install <../embedded-cluster-install/system-requirements-for-an-embedded-cluster-install/system-requirements-for-an-embedded-cluster-install.htm>`__
   or `System Requirements for an Existing Cluster
   Install <../existing-cluster-install/system-requirements-for-an-existing-cluster-install/system-requirements-for-an-existing-cluster-install.htm>`__.

Resources to Check; Logs/Info to Retrieve
-----------------------------------------

Ensure that there is a support bundle available. See `Generate a Support
Bundle <generate-a-support-bundle.htm>`__ for details.

In addition to the support bundle, get the status and logs of the
Containerd and Kubelet services. Use this code:

for SERVICES in containerd kubelet; do echo --- $SERVICES --- ;
systemctl is-active $SERVICES ; systemctl is-enabled $SERVICES ; echo
""; done \``\` \``\` for SERVICES in containerd kubelet; do echo ---
$SERVICES --- ; systemctl status $SERVICES ; systemctl status $SERVICES
; echo ""; done \``\` \``\` journalctl -u kubelet --since "3 hour ago" >
/tmp/kubelet-<node-name>-log.txt journalctl -u containerd --since "3
hour ago" > /tmp/containerd-<node-name>-log.txt \``\`

If you can't generate a support bundle, for example, if the issue is
occurring before the SPI is successfully installed and running, or the
support bundle generation fails, then run the following commands and
provide the output:

kubectl get pods -A \| grep -v Running \| grep -v Completed

If any pods are listed, include the pod logs with: 

kubectl logs --all-containers PODNAME -n NAMESPACE

Include the pod describe output with: 

kubectl describe pod PODNAME -n NAMESPACE

Then continue providing output with: 

kubectl get pods -A kubectl get deploy -A kubectl get sts -A kubectl get
pvc -A kubectl get pv -A kubectl get svc -A kubectl get nodes

If any nodes have a status other than *Ready*, then also include the
describe output of the node with: 

kubectl describe node NODENAME kubectl get events
--sort-by=.metadata.creationTimestamp

Next, get the status and logs of the Containerd and Kubelet services:

for SERVICES in containerd kubelet; do echo --- $SERVICES --- ;
systemctl is-active $SERVICES ; systemctl is-enabled $SERVICES ; echo
""; done for SERVICES in containerd kubelet; do echo --- $SERVICES --- ;
systemctl status $SERVICES ; systemctl status $SERVICES ; echo ""; done
journalctl -u kubelet --since "3 hour ago" >
/tmp/kubelet-<node-name>-log.txt journalctl -u containerd --since "3
hour ago" > /tmp/docker-<node-name>-log.txt

Finally, provide the following: 

-  OS and Version

-  Infrastructure setup:

   -  Instance provider, for example, Bare-metal, VM, AWS instance,
      Azure instance, GCP instance, etc.

   -  Instance sizes, including memory, cpu, disk/partitions

-  Load balancer type and setup
