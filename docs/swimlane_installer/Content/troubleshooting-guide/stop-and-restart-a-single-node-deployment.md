Stop and Restart a Single-Node Deployment
##########=

On occasion, single-node SPI deployments must be stopped and restarted.
One example of this is when you need to perform scheduled maintenance.

To stop and restart a single-node SPI Deployment:

#. Login to the node as a user with administrator privileges.

#. Find the name of the node. In the example within this topic, the node
   is named `master3a`.

3. Drain the node.

4. Check that the node is in the “Ready,SchedulingDisabled” status.

5. Stop or restart the server or VM.

6. Next, uncordon the node (i.e. make the node schedulable).

7. Finally, ensure that the node is in the “Ready” status.
