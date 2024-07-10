Python Task API
===============

Swimlane has a rich API for interacting with Python scripts inside the
integration platform. On each script's initialization, Swimlane
automatically passes information about the task to each script through a
sw_context object.

Context objects contain the following:

-  **Inputs:** The input parameters defined in the task configuration.
   These parameters can be literal values, record values, or values from
   assets. Here's is an example: ``sw_context.inputs["ipAddress"]``

   **Note:** The TASK API passes data between the Swimlane platform and
   integration tasks as serialized JSON, which means all the data passed
   then is converted into character strings.

-  **Config:** System-level attributes and internal IDs, including:

   -  SwimlaneUrl - The base URL of the Swimlane install (i.e.
      http://swimlane.mycorp.com)

   -  RecordId - The ID of the record that executed the script, if
      applicable.

   -  ApplicationId - The application ID of the record that triggered
      the script, if applicable. For example:
      ``sw_context.config["SwimlaneUrl"]``

   -  **Asset information:** The parameters used to configure the asset,
      such as an access token or password, associated to the task when a
      script is executed as a packaged action.

      **Note:** The asset sw_context property is not available for
      standard ad-hoc Python integrations that are not associated
      directly with an asset.

      Retrieve properties defined on the asset that are associated with
      the integration task with: ``sw_context.asset["accessToken"]``

When the script has completed, developers can attach to a global array
of dictionaries as output variables. Messages that are printed to the
standard output can also be captured.

Considerations
--------------

There are a few scenarios to be aware of when developing Task scripts:

-  Attachments: Attachments from emails or record attachment fields that
   are mapped through the input parameters will be a byte array.
-  Dates: Dates that are passed will automatically be converted to UTC
   Python Date objects rather than a string representation.

**Note:** When entering dates for API GET calls, format the date as
follows: 2017-01-01T05:00:00Z

**Important!** Do not use ``sys.exit()`` in your Python script tasks. It
will terminate the integration process and will not return any results
to Swimlane.

More on setting up Inputs and Outputs, and setting up the asset
sw_context information

Debugger and the output mapping section.

.. toctree::
   :titlesonly:
   :caption: Children:

   /Content/developer-guide/python-task-api/introduction-to-the-python-task-api
   /Content/developer-guide/python-task-api/implementation-usage
   /Content/developer-guide/python-task-api/working-with-files-in-python-scripts
