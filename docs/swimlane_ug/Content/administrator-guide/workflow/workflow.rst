Workflow
========

Every application in Swimlane has a workflow. Workflow is where you
define how your organization processes tasks. You build the workflow
like a tree, with one or more branches. Each branch is conditional, and
can consist of multiple conditions and actions. In addition, you can
also conditionalize repeat actions in workflow.

Activity on individual records catalyze workflow, for example:

-  You open a new record form.
-  A new record is saved for the first time.
-  An existing record is opened.
-  You modify an existing record.

In addition, workflow is also carried out when:

-  A new record is created by an integration task.
-  A new record is created by a remote client tool or script.
-  An existing record is modified by either of the previous two actions.

Swimlane workflow consists of:

-  Conditions - decision points in the workflow.
-  Repeats - iterative task items within the workflow.
-  Actions - singular tasks to be accomplished by workflow.

**Note:** Repeats iterate an integration action with a specific
condition for each item and work exclusively with Text, Numeric, Grid,
and Multi-select Reference fields.

For information on how applets handle workflow, and how workflow is
updated when applets are added to applications, see `Applets and
Workflow <../applications-and-applets/applet-builder/applets-and-workflow.htm>`__.

To view, create, or update workflow, click the workflow icon on the
Application or Applet Builder toolbar.

|image1|

Workflow processes conditionally and can become quite complex. To zoom
in to a flow, use the scroll wheel of your mouse, or use the zoom
buttons in the upper left corner of the page. From this menu you can
also collapse or expand all of the workflow..

|image2|

Left-click, hold, and drag your mouse to navigate the branches of the
workflow. You can also expand or collapse conditions within your
workflow so that you can focus on a specific section. To collapse or
expand a branch, click the **+** or **-** icon to the right of the
condition or action.

To search for a condition or action, place your cursor in the search
field and then enter a term from the name of the condition or action.
Swimlane locates each instance of the term, highlights it, and brings up
the editable window where you can review or make changes to the details.
If there is more than one instance of what you're searching for, click
the arrows to see the additional instances.

|image3|

Workflow Execution
------------------

There is no set order of how a workflow is executed. The processing
first evaluates all of the conditions in the workflow, and then
determines a list of actions that are dependent upon how the conditions
are met. The process then executes the defined actions.

.. |image1| image:: ../../Resources/Images/workflowicon.png
.. |image2| image:: ../../Resources/Images/zoomicons.png
.. |image3| image:: ../../Resources/Images/wf-search.png

.. toctree::
   :titlesonly:
   :caption: Children:

   /Content/administrator-guide/workflow/conditions
   /Content/administrator-guide/workflow/repeats
   /Content/administrator-guide/workflow/create-and-update-workflow
   /Content/administrator-guide/workflow/actions/actions
   /Content/administrator-guide/export-templates/create-export-templates-from-workflow
