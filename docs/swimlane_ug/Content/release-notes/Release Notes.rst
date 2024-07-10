Release Notes
=============

 

 

10.13.1
-------

*Swimlane 10.13.1, released June 30, 2023, includes:*

-  Users of Swimlane can now share dashboards, reports, and records with
   other Swimlane users based on role-based permissions within the
   platform. This means that you have control over data access with
   Swimlane’s robust permissions. Only those users who have permission
   to view a dashboard, report, or record are available to select as
   recipients of the shared information. But don’t worry, you can still
   send to others, including people outside of your Swimlane platform,
   by simply including their email addresses.

   Sharing reports, dashboards, and records with others can be done by
   email, by downloading a PDF, or by scheduling either an ongoing or
   one-time email. We hope this feature helps you ensure that your
   Swimlane data are shared with all the right people.

-  With this release, we have also added a new permission, Restrict
   History. When you enable this permission in role permissions for
   specific applications, then the users with that role designated are
   not able to see the history or workflow of that application’s
   records.

Fixes
~~~~~

-  We resolved an issue with copying field values. Some users had
   reported that they copied field data, received a “Text copied
   successfully” message, but the text hadn’t actually been copied. That
   has been resolved and you can again copy field data.

-  Swimlane now restricts user information that is passed through API
   endpoints.

Security
~~~~~~~~

-  You can now configure your own CORS and CSP headers. A new
   configuration options under the Ingress Settings section to enable
   and optionally override HTTP CORS and CSP headers for Swimlane Web.
   If left to their default values, no CORS or CSP headers will be set
   for Swimlane Web

Click
`here <https://support.swimlane.com/a/solutions/articles/8000101190>`__
to see a report on the Common Vulnerabilities and Exposures (CVEs)
addressed with this release of Swimlane.

.. _section-1:

10.13.0
-------

*Swimlane 10.13.0, released April 27, 2023, includes:*

Improvements
~~~~~~~~~~~~

-  You can now hover and copy read-only fields (with the exception of
   rich text and list fields).

-  Workflow runs now display in timestamps that include seconds.

-  If you inadvertently close your web browser with unsaved updates in
   application builder, you'll now receive a pop-up alert to remind you
   to go back to save or leave your changes.

.. _fixes-1:

Fixes
~~~~~

-  We resolved an issue that was causing duplicate records due to
   workflow and selection fields.

-  We've improved the coedit session sync for multiple users. You can
   now see unsaved changes during a session.

.. _section-2:

10.12.0
-------

*Swimlane 10.12.0, released March 2, 2023, includes:*

-  General security and quality improvements across the platform,
   including updates to the Swimlane Platform Installer. See the
   `Swimlane Platform Installer Release
   Notes <https://support.swimlane.com/support/solutions/articles/8000096991>`__
   for details.

-  You can now upload a certificate for Mongo DB. The configuration item
   is within the KOTS admin console and enables two items for uploading
   a cert/key pair.

.. _section-3:

10.11.3
-------

*Swimlane 10.11.3, released February 9, 2023, includes:*

-  A fix. The Google Chrome browser (when updated to the latest version,
   110) no longer redirects non-administrator users to an “Unauthorized”
   error page. If Swimlane support advised you to use the Edge browser,
   you should know that this fix applies to Edge, as well. Swimlane
   continues to full support the Chrome browser, however.

.. _section-4:

10.11.2
-------

*Swimlane 10.11.2, released February 8, 2023, includes:*

-  A fix that resolves a memory leak within the DotNet code.

.. _section-5:

10.11.1
-------

*Swimlane 10.11.1, released January 20, 2023, includes:*

API Improvements
~~~~~~~~~~~~~~~~

-  New Attachment API endpoints now require both an associated record ID
   and field ID as well as delete/read permission for the referenced
   record and field.

-  Previously removed Attachment API endpoints have been temporarily
   reintroduced to circumvent breaking changes introduced in Swimlane
   10.11.0. Due to a security vulnerability with these endpoints, they
   should be disabled as soon as possible via the Disable Obsolete
   Attachment Endpoints feature flag once you confirm that attachment
   APIs are not directly in use.

-  The /api/data-import/run endpoint now requires record create
   permissions for the applicationId sent in the payload.

See `Swimlane 10.11 API
Changes <https://support.swimlane.com/a/solutions/articles/8000107023>`__
for information about why we made these API changes, and how you can
mitigate the vulnerability if you use these API endpoints.

.. _section-6:

10.11.0
-------

*Swimlane 10.11.0, released January 11, 2023, includes:*

-  Security and quality improvements across the Swimlane platform.

-  Websocket connections no longer send the JWT in the querystring, but
   now sends with a cookie.

-  A change to how session timeouts work. Instead of timing out based on
   how long you have been logged in, timeouts are now based on how
   active you've been. So, as long as you're interacting with Swimlane,
   you won't be logged out. But, if you step away for a bit and don't do
   anything, the system will automatically log you out after a
   configured amount of inactivity.

-  The Workflow Run (time-to-live) TTL setting will now apply to the
   Swimlane.StageExecutions collection in the database. Previously, this
   collection was not properly managed by this setting, resulting in the
   collection growing to a large size and potentially causing a database
   crash. You should now see a reduction in size if the Workflow Run TTL
   setting is configured.

-  Corrected behavior when setting global record permissions.
   Field-level permissions now properly supersede changes to global
   permissions and remain set regardless of changes to global
   permissions.

.. _security-1:

Security
~~~~~~~~

Click
`here <https://support.swimlane.com/a/solutions/articles/8000101190>`__
to see a report on the Common Vulnerabilities and Exposures (CVEs)
addressed with this release of Swimlane.

.. _section-7:

10.10.1
-------

*Swimlane 10.10.1, released January 3, 2023, includes the following
fix:*

-  Imported tasks that are configured to trigger upon record save now
   perform as designed.

.. _section-8:

10.10.0
-------

*Swimlane 10.10.0, released November 16, 2022, includes:*

.. _improvements-1:

Improvements
~~~~~~~~~~~~

-  Record correlation, which was released in Swimlane 10.9.0, now also
   works with text list fields.

-  While importing an SSP package, if any of the entities already exist
   in the system, you can now choose to overwrite and replace them with
   the version from the SSP.

.. _security-2:

Security
~~~~~~~~

Click
`here <https://support.swimlane.com/a/solutions/articles/8000101190>`__
to see a report on the Common Vulnerabilities and Exposures (CVEs)
addressed with this release of Swimlane.

.. _section-9:

10.9.0
------

*Swimlane 10.9.0, released in October of 2022, includes:*

Important Highlights
~~~~~~~~~~~~~~~~~~~~

-  Users can now correlate fields across an application's records, then
   define the actions to take when the application detects a
   correlation.

-  You can now run a dynamic discovery of parameters within a newly
   added plugin that utilizes JSON schemas. You can also now select new
   output variables available in updated plugins.

.. _improvements-2:

Improvements
~~~~~~~~~~~~

-  We’ve redesigned and built a new version of the record page.

   -  We have removed:

      -  The print record dialog

      -  The share record dialog

      -  The record history timeline view

      -  The record time tracking

   -  Other notable differences:

      -  Performance improvements, particularly on applications with a
         larger amount of fields.

      -  Integration buttons are disabled for those with read-only
         permissions.

      -  Integration buttons are automatically disabled when not
         associated with a playbook.

      -  Widgets can no longer trigger record updates in read-only mode.

      -  Calculated record fields are now working more consistently with
         the API.

      -  The record-level hide empty fields option now applies to
         top-level fields and fields inside tabs.

-  We have updated Swimlane email settings to support OAuth2.0
   authentication methods. We continue to support Basic authentication.
   Users are also able to select “None” as an authentication method. See
   Email and PDF settings in Turbine documentation for more information.

-  We also added preview attachment support for the following file
   extensions: ODP, ODS, ODT, RTF, and XML.

.. _fixes-2:

Fixes
~~~~~

-  We resolved an issue where case sensitivity wasn’t active between
   SAML email and username values and their counterparts in Swimlane.

-  Records now properly display in charts in accordance with all the
   constraints of the group-by in the query dimension.

-  Removing a selection field value no longer disables a record.
   Instead, you are able to identify the records that had that selection
   field value by identifying it as *No value*, modifying it if
   necessary, and then save the record.

-  Updating a date field in a record now also updates the date in the
   default report.

-  You no longer have to refresh the browser to add a reference to a
   reference field.

.. _security-3:

Security
~~~~~~~~

Click
`here <https://support.swimlane.com/a/solutions/articles/8000101190>`__
to see a report on the Common Vulnerabilities and Exposures (CVEs)
addressed with this release of Swimlane.

.. _section-10:

10.8.3
------

*Swimlane 10.8.3, released March 6, 2023, includes these fixes:*

Editing a record no longer triggers an immediate save.

Setting a trigger to record save and initial save no longer returns a
400 error.

.. _section-11:

10.8.2
------

*Swimlane 10.8.2, released in February 2023, includes these fixes:*

-  The Google Chrome browser (when updated to the latest version, 110)
   no longer redirects non-administrator users to an "Unauthorized"
   error page. If Swimlane support advised you to use a different
   browser, you can now switch back to Chrome. Swimlane continues to
   fully support the Chrome browser.

-  You can now install Python packages that contain smbprotocol.

.. _section-12:

10.8.1
------

*Swimlane 10.8.1, released in June of 2022, includes:*

.. _improvements-3:

Improvements
~~~~~~~~~~~~

-  You can now configure "Max attempts" and "Interval" from Swimlane
   environment variables.

-  Log an error when a task is blocked after maxing out the retry
   attempts.

-  We introduced a feature flag around the concurrent task timeout
   feature and made the timeout configurable. The default timeout is 5
   minutes.

-  The release upgrade path has been tested from Swimlane platform
   releases 10.8.0 and 10.7.0.

Customer-Initiated Fixes
~~~~~~~~~~~~~~~~~~~~~~~~

This release addresses the following customer-initiated ticket:

SPT-13817 - Add "max attempts" & "interval" properties as environment
variables and read from the environment variables while checking for
concurrent tasks

.. _section-13:

10.7.1
------

*Swimlane 10.7.1, released in February 2023, includes these fixes:*

-  The Google Chrome browser (when updated to the latest version, 110)
   no longer redirects non-administrator users to an "Unauthorized"
   error page. If Swimlane support advised you to use a different
   browser, you can now switch back to Chrome. Swimlane continues to
   fully support the Chrome browser.

-  You can now install Python packages that contain smbprotocol.

.. _section-14:

10.7.0
------

*Swimlane 10.7.0, released in April 2022, includes:*

.. _important-highlights-1:

Important Highlights
~~~~~~~~~~~~~~~~~~~~

-  As of this release of the Swimlane platform, Swimlane no longer
   supports the Swimlane Linux Toolkit Installer. Contact your Swimlane
   support representative to discuss your migration path to Swimlane
   with the Swimlane Platform Installer (SPI).

-  You can now view workflow history from records, including Hangfire
   information that can help you in your troubleshooting efforts.

-  We added Python string interpolation functionality for formatting,
   adding/subtracting from datetimes, and converting datetimes to epoch
   and epoch_ms. We have also allowed setting utcNow as {{ now }}.

.. _improvements-4:

Improvements
~~~~~~~~~~~~

-  We have enhanced API endpoints that now allow you to specify a field
   by its name, in addition to its ID.

-  Workflow error logs now include more contextual information such as
   the action and record ID.

-  We made general performance improvements to record search
   functionality.

-  You can now filter by Tracking ID when searching reports.

.. _fixes-3:

Fixes
~~~~~

-  The Swimlane Python Driver now alerts you if you attempt to insert an
   attachment that is larger than a record field allows.

-  Integration actions configured after a condition of sw_task_status
   equals ‘failure’ now successfully execute.

-  Rich text field content that originated as sw_outputs now displays
   properly.

-  Filtering a records list with the "Previous X Days" filter now
   includes the current day.

-  Read-only users can no longer view the save button when another user
   with the appropriate permissions has staged changes on a dashboard.

-  API requests to change user properties are now successfully
   validated.

Breaking Changes
~~~~~~~~~~~~~~~~

-  GET api/search/keyword

-  The record count property has been removed from the results

-  The format of the returned data for the endpoint has been changed to:

   {"records": Record []}
