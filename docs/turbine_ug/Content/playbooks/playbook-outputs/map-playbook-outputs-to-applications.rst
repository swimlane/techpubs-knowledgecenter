Map Playbook Outputs to Applications
====================================

When you map playbook outputs to an application, you allow the playbook
runs to update records for various things, such as performing manual
security actions, collecting information for charts and dashboards, and
increasing visibility for auditing.

.. _map-playbook-outputs-to-applications-1:

Map Playbook Outputs to Applications
------------------------------------

Create a new playbook or upload an existing playbook, then follow the
steps below:

#. Click **Playbook Outputs**.

#. On Playbook Outputs, click the **Application Mapping** tab.

3. To map the promoted playbook outputs to an application, click
   **Select Existing Application**.

4. | On Select an Application, click the application to which you want
     to map the playbook outputs and click **Confirm**.
   | |image1|

After mapping playbook outputs, you choose how to manage mapped outputs.
Options include:

Update or Create New records
----------------------------

Select how you want to handle distribution of the playbook outputs to
the application's records.

#. Click **Update or create new records**.

#. | If you want to create a new record with the playbook outputs, click
     **Create new records**.
   | or
   | If you want to create or update a record with the playbook outputs,
     click **Update or create new records**.

3. In the **Key Field** drop-down menu, select the field that uniquely
   identifies each record.

Set Up Error Handling
---------------------

Select how you want to handle errors encountered during the insertion
process.

#. Click **Set fields as empty on error**.

Select one of three options for handling errors: **Set fields as empty
on error**, **Skip record on error**, or **Stop record creation on
error**.

2. When finished, click **Apply**.

Record Linking
--------------

There are three possible scenarios that can occur with record linking
when mapping playbook outputs to an application.

See `Record Use
Cases <../../use-cases/record-use-cases/record-use-cases.rst>`__ for
details.

.. |image1| image:: ../../Resources/Images/select-an-application-record-linking.png
