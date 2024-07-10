Read-Only Field Behavior
========================

Enabling and disabling read-only fields is a flexible feature within
Swimlane. You set up read-only fields from within Application Builder or
within workflow. Within Application Builder, you set up a read-only
field by clicking a checkbox in the field properties. In workflow, you
can either enable a read-only field, or disable an existing read-only
field.

When you add integrations, Python Driver, and API, the read-only fields
can continue to be manipulated. Here are some scenarios that show you
how read-only fields behave:

Scenario 1
----------

In this scenario, the read-only field is built into the application in
Application Builder. The application has a field that is set to
Read-Only, for example, a Date & Time field. The table below describes
how that field behaves when encountered by a user or through workflow,
and also when updated via APIs, integration tasks, or Python Driver.

+-------------+-------------+-------------+-------------+----------+
| User        | Workflow    | Python      | RESTful API | Task API |
| (within a   |             | Driver      |             |          |
| record)     |             |             |             |          |
+=============+=============+=============+=============+==========+
| Unable to   | Field is    | Not         | Editable    | Editable |
| edit the    | editable    | editable    |             |          |
| field       |             | (You        |             |          |
|             |             | receive a   |             |          |
|             |             | read-only   |             |          |
|             |             | error       |             |          |
|             |             | message.)   |             |          |
+-------------+-------------+-------------+-------------+----------+

Scenario 2
----------

In the second scenario, the read-only field is created by workflow. In
this example, a condition is set up that if a record's Severity field is
set to *Critical,* then the Reported by field is set to *Read-Only* (the
field is not originally). Once the workflow executes, the field is
editable or not editable as seen in this table:

+-------------+-------------+-------------+-------------+----------+
| User        | Workflow    | Python      | RESTful API | Task API |
| (within a   |             | Driver      |             |          |
| record)     |             |             |             |          |
+=============+=============+=============+=============+==========+
| Unable to   | Editable    | Editable    | Editable    | Editable |
| edit the    | (if         |             |             |          |
| field       | workflow is |             |             |          |
|             | also set up |             |             |          |
|             | to set the  |             |             |          |
|             | field       |             |             |          |
|             | value)      |             |             |          |
+-------------+-------------+-------------+-------------+----------+
