.. _records:

Application Records
===================

Records are the data from your Swimlane Turbine applications. They are
made up of various fields which are customizable, configurable, and
built within Turbine's Application Builder.

The fields and options available in the record vary based upon how the
application is configured. Turbine administrators control tasks related
to records for administrators and users, and can grant additional access
to users at the application, record, and field level. The listing of
records in Turbine are considered Reports.

Turbine now integrates with external storage solutions to store larger
fields efficiently. Records have a limit of up to 100 MB, and fields
have a limit of up to 30 MB. This means that data exceeding MongoDB's
document size limitation will no longer be an issue. You can select
which fields will need extra storage. This is available on new fields
only.

First, configure your workspace and dashboard to display records from
applications that you access frequently. You can then access them from
Turbine's navigation bar.

To access records click the APPLICATION RECORDS icon on the navigation
bar and then click the related application to see its records.

|image1|

Use the search filter on the APPLICATION RECORDS menu to find a specific
application, as needed. The search filter appears if you have more than
six applications associated to your workspace.

**Note:** If you don't see the application that you expect to be listed
in the navigation bar, verify that you have opened the correct workspace
and dashboard and have the proper permissions to view those records.
Additionally, you might need to load a different workspace.

When you select the name of the application, the Default Report view of
records opens. You can configure the columns in the Default Report by
clicking the vertical ellipsis Add/Remove Columns button and select the
desired fields.

If you have selected the **HyperLink** property for the URL, clicking
the URL takes you to the URL.

If you have multiple users accessing records of a specific application,
utilize the refresh button at the bottom left of the Default Report
view.

|image2|

Within records, you manage and interact with data contained within the
platform, and you can perform the following:

-  Add a New Record
-  Modify an Existing Record
-  Delete a Record
-  Restrict Access to a Record
-  Modify Bulk Records
-  Delete Bulk Records
-  View Record History
-  Share, Print, or Export Records

.. |image1| image:: ../Resources/Images/app-records-flyout.png
.. |image2| image:: ../Resources/Images/refresh-records.png

.. toctree::
   :titlesonly:
   :caption: Children:

   /Content/records/customize-the-list-of-records
   /Content/records/search-record-data
   /Content/records/modify-a-record/modify-a-record
   /Content/records/bulk-modify-records
   /Content/records/correlate-records
   /Content/records/view-record-history
   /Content/records/read-only-field-behavior
