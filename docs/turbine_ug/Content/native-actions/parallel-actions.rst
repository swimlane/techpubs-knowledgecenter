Parallel Actions
================

Parallel actions are another native action in Turbine.

|image1|

This feature adds Parallel action groups within a playbook and uses the
WAIT feature as a visual indicator to let you know that the node waits
for other actions in the Parallel block to execute before continuing
downstream.

**Note:** This includes all Parallel entry points and downstream On
Success, On Failure, and On Complete actions.

Parallel blocks and the WAIT construct enable an orchestrator to build a
playbook that executes Parallel branches, then waits for the branches to
execute in parallel.

You can use the Parallel native action and execute paths, wait for the
paths to complete execution, and then map the results to an application.

Important notes about the Parallel action and WAIT feature:

-  If any action in the group fails, then the On Failure action flow
   path executes.

-  If all the actions in the group succeed, then the On Success action
   flow path executes.

-  When a WAIT feature is complete, the next path continues downstream
   in the playbook.

-  You can use Loop native actions (or nested Loops) within a Parallel
   group.

-  You are not limited to the entry points. You can also chain actions
   in the Parallel group. You can have On Success, On Failure, and/or On
   Complete action flows for each action within the Parallel group.

Warning! If any action anywhere in the parallel groups fails, the entire
group is marked as a failure.

From an action within a Parallel group, there are two options for action
flow:

-  One On Success and/or one On Failure

-  One On Complete

You will receive an Action configuration error if you to add an Complete
with an On Success or On Failure. Also, you can only have one On Failure
within a Parallel group.

Parallel Native Action Set Up
-----------------------------

Time to start basic set-up for the Parallel native action.

You have already created a playbook, and you are ready to manipulate the
data from a property.

#. From your playbook, click Add an Action.

#. From the ACTION panel, click the **Action** drop-down menu.

#. Select **Parallel**.

#. Hover over or click the Parallel action to see the plus icon and add
   entry points.

#. Configure the On Success, On Failure, and On Complete actions for
   your needs and continue creating your playbook.

.. |image1| image:: ../Resources/Images/parallel-action-icon.png
