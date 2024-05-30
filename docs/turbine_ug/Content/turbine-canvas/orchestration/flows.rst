Flows
=====

+------+------------------------------+------------------------------+
| Term | Definition                   | Characteristics              |
+======+==============================+==============================+
| Flow | A single execution path      | -  Each flow can only have   |
|      | within a playbook or         |    one trigger               |
|      | component that has one       |                              |
|      | trigger that initiates       | -  There can be multiple     |
|      | subsequent automation.       |    flows in one playbook     |
|      |                              |                              |
|      |                              | -  No cross-talk between     |
|      |                              |    flows                     |
+------+------------------------------+------------------------------+

The following image is a playbook canvas with three separate triggers.
Each has their own flow(s). Notice the flows do not communicate with one
another. They are individual execution paths.

|image1|

**How does information flow? **
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The playbook trigger receives data inputs from either an external
system/service or an application record, then applies that data
according to the actions needed for the required outcome in a single
execution flow. Then the data outputs are written to an external
system/service or a new/existing application record.

|image2|

A playbook canvas has a top-down flow visualization. The flows of
information are referred to as upstream and downstream.

|image3|

Flow Connectors
~~~~~~~~~~~~~~~

The flow between actions goes from the proceeding action to the
subsequent action. There are three types of flow connectors that signal
execution type from one action to the next.

-  On success

-  On failure

-  On complete

Visual indicators after you select a flow connector. Green flows are On
success flows, indicating that upon on success of the preceding action,
the next action in that flow executes. Red flows are On failure flows,
indicating that upon on failure of the preceding action, the next action
in that flow executes.

|image4|

 

 

 

.. |image1| image:: ../../Resources/Images/canvas-flows.png
.. |image2| image:: ../../Resources/Images/canvas-single-flow.png
.. |image3| image:: ../../Resources/Images/canvas-up-down-stream.png
.. |image4| image:: ../../Resources/Images/canvas-flow-connectors.png
