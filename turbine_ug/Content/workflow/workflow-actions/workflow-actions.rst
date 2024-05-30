Workflow Actions
================

If workflow is a tree, and conditions are branches, then workflow
actions are the leaves of the tree. Actions are the specific tasks that
occur. They cannot have child nodes, and are controlled by the defined
conditions and actions in the workflow. Each workflow action type has
specific options. See the table below for an introduction to each
option:

**Swimlane Turbine Workflow Action Options**

+---------------------------+-----------+---------------------------+
| **Workflow Action**       | **Icon**  | **Definition**            |
+===========================+===========+===========================+
| **Set Field Value**       | |image13| | Updates the value of a    |
|                           |           | field to a specified      |
|                           |           | value.                    |
+---------------------------+-----------+---------------------------+
| **Set Field Read/Write**  | |image14| | Sets a field to read-only |
|                           |           | or editable status.       |
+---------------------------+-----------+---------------------------+
| **Set Field               | |image15| | Makes a specified field   |
| Required/Optional**       |           | required or optional.     |
+---------------------------+-----------+---------------------------+
| **Filter Selection        | |image16| | Specifies the values to   |
| Options**                 |           | update on a field that    |
|                           |           | has multiple values       |
|                           |           | available.                |
+---------------------------+-----------+---------------------------+
| **Modify Layout**         | |image17| | Shows or hides fields in  |
|                           |           | a record.                 |
+---------------------------+-----------+---------------------------+
| **Toggle Time Tracking    | |image18| | When selected, tracks the |
| for Record**              |           | time for the record       |
+---------------------------+-----------+---------------------------+

For more detail on each of these workflow action types, see `Create and
Update Workflow <../create-and-update-workflow.rst>`__.

**Note:** Some fields are not available to be defined in workflow
actions, including variable fields like comments, HTML fields, and other
non-configurable data types.

.. |image1| image:: ../../Resources/Images/setfieldvalue.png
.. |image2| image:: ../../Resources/Images/makefieldseditable.png
.. |image3| image:: ../../Resources/Images/makefieldsrequired.png
.. |image4| image:: ../../Resources/Images/filtervalueslists.png
.. |image5| image:: ../../Resources/Images/modifylayout.png
.. |image6| image:: ../../Resources/Images/enabledisablerecordtimetrack.png
.. |image7| image:: ../../Resources/Images/setfieldvalue.png
.. |image8| image:: ../../Resources/Images/makefieldseditable.png
.. |image9| image:: ../../Resources/Images/makefieldsrequired.png
.. |image10| image:: ../../Resources/Images/filtervalueslists.png
.. |image11| image:: ../../Resources/Images/modifylayout.png
.. |image12| image:: ../../Resources/Images/enabledisablerecordtimetrack.png
.. |image13| image:: ../../Resources/Images/setfieldvalue.png
.. |image14| image:: ../../Resources/Images/makefieldseditable.png
.. |image15| image:: ../../Resources/Images/makefieldsrequired.png
.. |image16| image:: ../../Resources/Images/filtervalueslists.png
.. |image17| image:: ../../Resources/Images/modifylayout.png
.. |image18| image:: ../../Resources/Images/enabledisablerecordtimetrack.png

.. toctree::
   :titlesonly:
   

   /Content/workflow/workflow-actions/select-workflow-action-type

