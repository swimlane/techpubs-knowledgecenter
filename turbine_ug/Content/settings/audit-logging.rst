.. _logging:

Audit Logging
=============

Audit logs report events in the Swimlane Turbine system. Turbine uses a
common log schema to report log events. The goal of a common log schema
is to provide uniformity in how log entries are recorded, allowing for
easier integration and analysis of log data.

Understand the API Log Retrieval Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a reference for users who intend to interact with the log
retrieval endpoint of the API via a URL for retrieving logs from the
API. The API is designed to provide log information for a specific
account and tenant within a specified date range:

https://swimlane.app/api/account/{account_id}/tenant/{tenant_id}/logs?fromdate=2024-01-04T13:01:36.3373Z&todate=2024-01-07T23:01:36.3373Z&pageNumber=2&pageSize=10

 

Use this table to further understand the log endpoints and parameters:

+-----------------------+---------------------------------------------+
| Endpoint / Parameter  | Definition                                  |
+=======================+=============================================+
| {account_id}          | The unique identifier for the account.      |
+-----------------------+---------------------------------------------+
| {tenant_id}           | The unique identifier for the tenant.       |
+-----------------------+---------------------------------------------+
| fromdate (Optional)   | Indicates the start date and time for the   |
|                       | log retrieval, in ISO 8601 format           |
|                       | (2024-01-04T23:01:36.3373Z).                |
+-----------------------+---------------------------------------------+
| todate (Optional)     | Indicates the end date and time for the log |
|                       | retrieval, also in ISO 8601                 |
|                       | format.(2024-01-010T14:01:26.1273Z).        |
+-----------------------+---------------------------------------------+
| pageNumber (Optional) | Page number for paginated results. If no    |
|                       | pagination parameters are provided, the API |
|                       | returns page number one.                    |
+-----------------------+---------------------------------------------+
| pageSize (Optional)   | Number of log entries to include in each    |
|                       | page(Maximum 100 ).                         |
+-----------------------+---------------------------------------------+

Important! If no date range is provided, you will receive logs for the
last 7 days.

 

Use this table to further understand the event types logged in audit
logs:

Note: Depending on the event type, some fields may not be present.

+--------------+------------------------------------------------------+
| Audit Logs   | Definition                                           |
+==============+======================================================+
| EventTime    | The date and time when the event occurred in ISO     |
|              | 8601 format. The timestamp indicates when the log    |
|              | entry was generated. It helps in understanding the   |
|              | chronological order of events and is crucial for     |
|              | time-based analysis and debugging.                   |
+--------------+------------------------------------------------------+
| User         | The user’s email is the unique identifier of the     |
|              | authenticated user. You can anticipate a report of   |
|              | the user’s email if an event is triggered by user    |
|              | action, otherwise expect “Null” if an event is       |
|              | triggered by the system or automation.               |
+--------------+------------------------------------------------------+
| UserId       | The user GUID                                        |
+--------------+------------------------------------------------------+
| Category     | | Defines the functional areas. Areas include:       |
|              |                                                      |
|              | -  Login                                             |
|              |                                                      |
|              |    Playbook                                          |
|              |                                                      |
|              | -  Record                                            |
|              |                                                      |
|              | -  Solutions                                         |
|              |                                                      |
|              | -  Asset Management                                  |
|              |                                                      |
|              | -  User Management                                   |
|              |                                                      |
|              | -  Settings                                          |
|              |                                                      |
|              | -  Tenant Management                                 |
|              |                                                      |
|              | -  Account Management                                |
|              |                                                      |
|              | -  Applications                                      |
+--------------+------------------------------------------------------+
| Description  | A short description of the event, including what     |
|              | action was taken and what data was accessed or       |
|              | modified.                                            |
|              |                                                      |
|              | Read - “[User Display Name] read [entity]            |
|              | [ID/Name]”. For example “Frank read record           |
|              | a334ff323”                                           |
|              |                                                      |
|              | Create - “[User Display Name] created a new          |
|              | [Entity]”                                            |
|              |                                                      |
|              | Update - “[User Display Name] updated [Entity]       |
|              | [ID/Name]”. For example, “Frank Smith updated        |
|              | playbook Fetch threat intel”                         |
|              |                                                      |
|              | Delete - “[User Display Name] deleted [Entity]       |
|              | [Id/Name]”                                           |
+--------------+------------------------------------------------------+
| TenantId     | Any action performed under a specific tenant.        |
+--------------+------------------------------------------------------+
| AccountId    | For account-level operations (user management) the   |
|              | AccountId is required. AccountId is not required     |
|              | when TenantId is provided.                           |
+--------------+------------------------------------------------------+
| SourceIp     | The IP address of the client/user.                   |
+--------------+------------------------------------------------------+
| UserAgent    | User-agent header responsible for making the request |
|              | for non-system access.                               |
+--------------+------------------------------------------------------+
| ActionType   | Typically refers to the specific action or event     |
|              | that occurred. The type of action describes what     |
|              | happened in the system or application being audited. |
|              | Here are the high-level action types for a log:      |
|              |                                                      |
|              | Create                                               |
|              |                                                      |
|              | Update                                               |
|              |                                                      |
|              | Delete                                               |
|              |                                                      |
|              | Read                                                 |
|              |                                                      |
|              | UserAction                                           |
+--------------+------------------------------------------------------+
| Id           | ID of value being created/updated/deleted/read when  |
|              | an ID is available                                   |
+--------------+------------------------------------------------------+
| NewValue     | Individual new field value if change or addition is  |
|              | an atomic operation. For model updates, the new      |
|              | updated model in JSON format. Use for non-sensitive  |
|              | information only. Not available for Delete and Read  |
|              | operations.                                          |
+--------------+------------------------------------------------------+
| EventOutcome | Either "Success" or "Failure"                        |
+--------------+------------------------------------------------------+

.. _example-api-payload:

Example of a Read Audit Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{ "eventTime": "2024-01-15T18:10:19.4501967Z", "category": "Settings",
"description": " read security parameter settings", "actionType":
"Read", "tenantId": "...", "accountId": "...", "eventOutcome":
"Success", "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }
