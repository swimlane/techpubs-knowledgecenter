Parallels
=========

+--------------+--------------------------+--------------------------+
| Term         | Definition               | Characteristics          |
+==============+==========================+==========================+
|              |                          | -  Native action         |
|              |                          | -  Playbook building     |
| **Parallel** | Uses the WAIT feature as |    tool                  |
|              | a visual indicator to    | -  No connector needed   |
|              | let you know that the    |                          |
|              | node waits for other     |                          |
|              | actions in the Parallel  |                          |
|              | native action block to   |                          |
|              | execute before           |                          |
|              | continuing downstream.   |                          |
+--------------+--------------------------+--------------------------+

|image1|

As orchestrators, sometimes you need to build a playbook that executes
parallel branches, then waits for the branches to execute in parallel.

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

**Warning!** If any action anywhere in the parallel groups fails, the
entire group is marked as a failure.

From an action within a Parallel group, there are two options for action
flow:

-  One On Success and/or one On Failure

-  One On Complete

You will receive an Action configuration error if you to add an Complete
with an On Success or On Failure. Also, you can only have one On Failure
within a Parallel group.

Add and Configure Parallels
---------------------------

When you drag-and-drop a Parallel native action onto the playbook
canvas, the WAIT visual indicator automatically becomes available.

#. add entry points.

#. Configure the On Success, On Failure, and On Complete actions for
   your needs and continue creating your playbook.

.. |image1| image:: ../Resources/Images/canvas-na-parallel-action.png
