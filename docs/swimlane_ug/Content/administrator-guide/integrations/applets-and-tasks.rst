Applets and Tasks
=================

When you create a task, you can choose to leave the task as a common
task or associate it with an applet or application. Applets and
applications can reference any common tasks or the associated tasks.
When adding an applet that contains a task or workflow to an
application, Swimlane notifies you that the applet workflow is being
added to the application and new application tasks will be created for
each of the applet tasks.

|image1|

Applet tasks differ from application task in a few ways, mainly in the
way applet task input and output parameters are configured. When
configuring parameters in an applet task, you will see the options to
map a parameter from or to a record. However, applets do not have
records to map to. When the applet is added to the application, the
applet tasks are duplicated as application tasks and any input or output
parameters mapped to the current record are updated accordingly.

Additionally, on the **Configuration** tab, in the **Debugger** subtab,
you can click **Run Task** to check your script. However, unlike
application tasks, applet tasks can not be tested against a record.

.. |image1| image:: ../../Resources/Images/workflow-and-tasks-added-dialog.png
