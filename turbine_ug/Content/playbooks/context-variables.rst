Context Variables
=================

Context variables are variables that hold a variety of contextual
information relating to the current playbook, its invocation parameters,
and executed actions.

Using context variables is especially helpful when creating `Playbook
Triggers <playbook-triggers/playbook-triggers.rst>`__ to help define
parameters and retrieve/store specific data.

This table lists some of the helpful context variables you can use.

+--------------------------+------------------------------------------+
| Context Variable         | Stored Contextual Information/Returned   |
|                          | Value of Variable                        |
+==========================+==========================================+
| $event                   | Data related to the sensor event that    |
|                          | triggered playbook                       |
+--------------------------+------------------------------------------+
| $event.data              | Data/inputs from the event               |
+--------------------------+------------------------------------------+
| $event.post              | Posted values from the trigger           |
+--------------------------+------------------------------------------+
| $event.type              | Type of event (events, sensors,          |
|                          | schedules)                               |
+--------------------------+------------------------------------------+
| $event.name              | Name of the event                        |
|                          | (http.webserver.request)                 |
+--------------------------+------------------------------------------+
| $event.timestamp         | Integer timestamp of the event in        |
|                          | milliseconds                             |
+--------------------------+------------------------------------------+
| $event.sensor.name       | Name of the sensor that received the     |
|                          | event                                    |
+--------------------------+------------------------------------------+
| $event.agent.name        | Name of the agent that was running the   |
|                          | sensor                                   |
+--------------------------+------------------------------------------+
| $actions                 | Object containing all preceding actions  |
|                          | that led to the current action           |
+--------------------------+------------------------------------------+
| $actions.<name>.result   | Result of the **Name** action            |
+--------------------------+------------------------------------------+
| $actions.<name>.post     | Object containing posted values from the |
|                          | **Name** action                          |
+--------------------------+------------------------------------------+
| $actions.$current.result | Result of the current action, not        |
|                          | populated until the action has ran       |
+--------------------------+------------------------------------------+
| $actions.$current.post   | Posted values from the current action,   |
|                          | not populated until the action has ran   |
+--------------------------+------------------------------------------+
| $actions.$parent.result  | Result of the previous action            |
+--------------------------+------------------------------------------+
| $actions.$parent.post    | Posted values from the previous action   |
+--------------------------+------------------------------------------+
| $assets                  | Object of asset names and their          |
|                          | respective parameters                    |
+--------------------------+------------------------------------------+
| $published               | Current publish object                   |
+--------------------------+------------------------------------------+
| $repeat.key              | Index or key of current repeat iteration |
|                          | for repeat actions                       |
+--------------------------+------------------------------------------+
| $repeat.value            | Value of current repeat iteration for    |
|                          | repeat actions                           |
+--------------------------+------------------------------------------+
| $utils                   | Collection of utilities to use           |
+--------------------------+------------------------------------------+

For a list of top-level properties that are defined on the $event.data
object when configuring webhook triggers, see event.data Properties in
the Webhook Triggers section.
