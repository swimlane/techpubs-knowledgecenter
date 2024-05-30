Features Overview
=================

.. _how-to-use-this-site:

How to Use this Page
--------------------

This page provides overviews of Turbine features. Let's get started with
some basic Turbine knowledge. Use this page to better understand the
cradle-to-grave use of Turbine.

First, tailor your settings and permissions and gain an understanding of
security features.

Settings

With Turbine Cloud, there is an administrator who has access to tenant
provisioning and a user/group definition. Then, within each tenant you
have local tenants administrators and orchestrators. To request
additional tenants, reach out to your Swimlane support representative.

Each tenant has its own account administrator. This account
administrator can:

-  Set up users, groups, and roles.
-  Assign and restrict create, read, update, and delete permissions.
-  Create additional account administrators.

Click `Tenant Management in Turbine
Cloud <../cloud/turbine-cloud/tenant-management-in-turbine-cloud.rst>`__
for additional information.

You are now a Turbine Administrator! Now what? You have access to
Turbine Settings, which control other global Turbine settings and
contain error and troubleshooting tools.

#. In the navigation menu to access the settings dashboard, click the
   **SETTINGS** icon.

   You can also hover over the icon and select from the available
   options.

In SETTINGS, administrators can:

-  Manage sessions and security
-  Enable/disable directory syncing
-  Review/update system details, i.e., system time zone workflow run
   TTL unit, etc.
-  Add connector keys
-  View the number of agents and pools

Click `Settings <../settings/settings.rst>`__ for additional
information.

Permissions

Once you have your settings completed, it's best to set up permissions.

Since Turbine uses a role-based permissions model, we designed
permissions with flexibility in mind. Turbine has flexible
administration of roles, groups, users and their permissions, which also
allows synchronization between Turbine and customer systems like LDAP
and Active Directory.

Administrators can set permissions for:

-  **Roles:** Functional roles associated with users and groups that
   hold permissions to objects.
-  **Users:** Users defined in Turbine or imported to Turbine from
   Active Directory.
-  **Groups:** Collections of users and other groups.
-  **Turbine Objects:** Secured features of Turbine, such as records,
   applications, applets, records, reports, workspaces, and dashboards.

Additionally for Turbine objects, you set the level of access for users,
roles, and groups such as:

-  **Create**
-  **Read**
-  **Modify**
-  **Update**
-  **Delete**
-  **Export**
-  **Lock** (for records)
-  **Restrict** (for records)

Click `Permissions <../permissions/permissions.rst>`__ for additional
information.

Security Specifics

This section covers database and Turbine user accounts and helps you
configure the best security set up from the start.

Database Security
~~~~~~~~~~~~~~~~~

Turbine uses MongoDB for data storage. Take precautions to ensure
unauthorized access to data cannot be gained. In MongoDB authentication
should be enabled and a dedicated MongoDB user account should be used to
connect to Swimlane.

This is the default configuration if Swimlane is installed using the
Swimlane installer.

Turbine User Accounts
~~~~~~~~~~~~~~~~~~~~~

Passwords for Turbine user accounts are hashed before being stored using
the HMAC-SHA1 algorithm with a 128-bit salt.

Workflow

How does it work? 

Turbine makes automation approachable and integrates with any API, so
you can unify any workflow, telemetry source, or team.

Every application in Swimlane Turbine has a workflow. Workflow is a
series of conditional decision points and resulting actions that
automate the presentation of record fields and layout. You build the
workflow like a tree, with one or more branches. Each branch is
conditional, and can consist of multiple conditions and actions.

Activity on individual records catalyze workflow, for example:

-  You open a new record form.
-  A new record is saved for the first time.
-  An existing record is opened.
-  You modify an existing record.

In addition, workflow is also carried out when:

-  A new record is created by a playbook.
-  A new record is created by a remote client tool or script.
-  An existing record is modified by either of the previous two actions.

Turbine workflow consists of:

-  Conditions - decision points in the workflow.
-  Workflow Actions - singular items to be accomplished by workflow.

For information on how applets handle workflow, and how workflow is
updated when applets are added to applications, see `Applets and
Workflow <../applications-and-applets/applet-builder/applets-and-workflow.rst>`__.

To view, create, or update workflow, click the Workflow icon on the
Application or Applet Builder toolbar.

|image1|

To zoom in to a flow, use the scroll wheel of your mouse, or use the
zoom buttons in the upper-left corner of the page. From this menu you
can also collapse or expand all of the workflow.

|image2|

Left-click, hold, and drag your mouse to navigate the branches of the
workflow. You can also expand or collapse conditions within your
workflow so that you can focus on a specific section. To collapse or
expand a branch, click the **+** or **-** icon to the right of the
condition or action.

To search for a condition or action, place your cursor in the search
field and then enter a term from the name of the condition or action.
Turbine locates each instance of the term, highlights it, and brings up
the editable window where you can review or make changes to the details.
If there is more than one instance of what you're searching for, click
the arrows to see the additional instances.

Workflow Execution

There is no set order of how a workflow is executed. The processing
first evaluates all of the conditions in the workflow, and then
determines a list of actions that are dependent upon how the conditions
are met. The process then executes the defined actions.

Click `Workflow <../workflow/workflow.rst>`__ for additional
information.

Widgets

Widgets are JavaScript components that you can use to enrich the User
Interface (UI) on records and dashboards.

Want to enhance your use cases? Widgets allow you to easily create your
own UI components that interact with Turbine or third-party endpoints.

While not necessary for Turbine set-up, the growing set of widgets can
help you customize records and reports.

Click `Widgets <../widgets/widgets.rst>`__ for additional information.

.. |image1| image:: ../Resources/Images/workflowicon.png
.. |image2| image:: ../Resources/Images/zoomicons.png
