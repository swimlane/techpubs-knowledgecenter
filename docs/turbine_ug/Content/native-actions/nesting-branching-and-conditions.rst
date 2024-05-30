Nesting, Branching, and Conditions
==================================

The forEach loop functionality has been enhanced to provide with nesting
capabilities, with multi-branching that enables on-success/error paths,
and If/Else conditions.

Review how to set up the `Loop <loops.rst>`__ native action before you
nest, branch, and create conditions within loops.

Nesting
-------

As an orchestrator working with loops, you can add loops into another
loop.

Note: You can only add four levels of *nested* loops (for a total of
five). A warning dialog shows when you have reached the limit and cannot
create more nested loops.

Inside the loops, you can:

-  Perform normal action functions, such as add, edit, and delete
   actions, inputs, and promote outputs
-  Configure on success, on failure, and on complete action flow logic
-  View and understand execution results from the branches of a loop and
   nested Loops
-  Support IF/ELSE conditions

Branching
---------

As an orchestrator working with loops you can:

-  Create one or more branches of actions and logic within a loop
-  Perform normal action functions, such as add, edit, and delete
   actions, inputs, and promote outputs
-  Configure on success, on failure, and on complete action flow logic
-  View and understand execution results from the branches of a loop and
   nested Loops

Conditions
----------

Just like actions, you can create action `Flows and
Conditions <../playbooks/actions/flows-and-conditions.rst>`__ for
forEach loops.

**Note:** Currently, in forEach loops, all conditions are **On
Complete**.

After adding an action, the action flow line displays.

#. Click the line to enable the condition functionality.
   |image1|

The condition icon displays. Click to open the FLOW window.

2. Click **Add Condition** to configure conditions for the action.

3. Click **CREATE YOUR FIRST CONDITION** and the playbook property
   drawer opens, where you can select the desired property from the
   current action and preceding actions.

Use Case
--------

See the `Nesting, Branching, and Conditions use
case <../use-cases/native-action-use-cases/nesting-branching-and-conditions-use-case.rst>`__
for example.

.. |image1| image:: ../Resources/Images/loop-condition-window.png
