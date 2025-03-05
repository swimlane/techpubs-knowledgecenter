Update the Load Balancer Address
########

Use these instructions to change your existing load balancer address
following a prior installation.

Execute the main installer script again on one of your existing nodes
with the new load balancer address specified. The main installer script
will generate a new task script that can be executed on the remaining
cluster nodes.

To update the SPI load balancer address:

#. Connect to all the nodes that are part of your Swimlane cluster.

2. On node 1, run the main installer script with the new load balancer
   address.

3. The installer script you run on node 1 executes a curl command. Use
   this new command on the other remote nodes (node 2, node 3).

4. Run the tasks.sh script on node 2 and node 3.

5. Enter Y to resume the installer load balancer change process on node
   1.

6. Once the installer has finished running, the load balancer address
   will be updated. Next you update the Swimlane application to use the
   new load balancer address.
