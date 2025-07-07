# Get all Incidents

**Description**: Retrieves all incident records from ServiceNow, with customization options for display values and result count limitation.

## Endpoint

- **URL:** `/api/now/v2/table/incident`
- **Method:** `GET`
## Inputs

- **parameters** (object): Auto-generated description for `parameters`. Please update manually if needed.
  - **sysparm_query** (string): Encoded query used to filter the result set. You can use a UI filter to obtain a properly encoded query. Syntax - sysparm_query=<col_name><operator><value>. Example sysparm_query - number=INC0000040.
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields. Display values are manipulated based on the actual value in the database and user or system settings and preferences. Valid values are true - Returns the display values for all fields. false - Returns the actual values from the database. all - Returns both actual and display values.
  - **sysparm_exclude_reference_link** (boolean): Flag that indicates whether to exclude Table API links for reference fields. Valid values are true - Exclude Table API links for reference fields. false - Include Table API links for reference fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_limit** (number): Maximum number of records to return. For requests that exceed this number of records, use the sysparm_offset parameter to paginate record retrieval. This limit is applied before ACL evaluation. If no records return, including records you have access to, rearrange the record order so records you have access to return first.
  - **sysparm_no_count** (boolean): Flag that indicates whether to execute a select count(*) query on the table to return the number of rows in the associated table. Valid values are true - Do not execute a select count(*). false - Execute a select count(*).
  - **sysparm_offset** (number): Starting record index for which to begin retrieving records. Use this value to paginate record retrieval. This functionality enables the retrieval of all records, regardless of the number of records, in small manageable chunks. For example, the first time you call this endpoint, sysparm_offset is set to "0". To simply page through all available records, use sysparm_offset=sysparm_offset+sysparm_limit, until you reach the end of all records. Don't pass a negative number in the sysparm_offset parameter.
  - **sysparm_query_category** (string): Name of the category to use for queries.
  - **sysparm_query_no_domain** (boolean): Flag that indicates whether to restrict the record search to only the domains for which the logged in user is configured. Valid values are false - Exclude the record if it is in a domain that the currently logged in user is not configured to access. true - Include the record even if it is in a domain that the currently logged in user is not configured to access.
  - **sysparm_suppress_pagination_header** (boolean): Flag that indicates whether to remove the Link header from the response. The Link header provides various URLs to relative pages in the record set which you can use to paginate the returned record set. Valid values are true - Remove the Link header from the response. false - Do not remove the Link header from the response.
  - **sysparm_view** (string): UI view for which to render the data. Determines the fields returned in the response. Valid values are desktop, mobile, both. If you also specify the sysparm_fields parameter, it takes precedent.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "7d9414489707",
      "Link": "<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=0>;rel=\"first\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=-1>;rel=\"prev\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=1>;rel=\"next\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=66>;rel=\"last\"",
      "X-Total-Count": "67",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Thu, 03 Nov 2022 20:32:32 GMT",
      "Keep-Alive": "timeout=20",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Tue, 21-Nov-2090 23:46:39 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=6D941C849707111084D57E121153AFF6; Max-Age=1800; Expires=Thu, 03-Nov-2022 21:02:32 GMT; Path=/; HttpOnly; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "result": [
        {
          "parent": "",
          "made_sla": "true",
          "caused_by": "",
          "watch_list": "",
          "upon_reject": "cancel",
          "sys_updated_on": "2016-12-14 02:46:44",
          "child_incidents": "0",
          "hold_reason": "",
          "origin_table": "",
          "task_effective_number": "INC0000060",
          "approval_history": "",
          "number": "INC0000060",
          "resolved_by": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007",
            "value": "5137153cc611227c000bbd1bd8cd2007"
          },
          "sys_updated_by": "employee",
          "opened_by": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
            "value": "681ccaf9c0a8016400b98a06818d57c7"
          },
          "user_input": "",
          "sys_created_on": "2016-12-12 15:19:57",
          "sys_domain": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global",
            "value": "global"
          },
          "state": "7",
          "route_reason": "",
          "sys_created_by": "employee",
          "knowledge": "false",
          "order": "",
          "calendar_stc": "102197",
          "closed_at": "2016-12-14 02:46:44",
          "cmdb_ci": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/109562a3c611227500a7b7ff98cc0dc7",
            "value": "109562a3c611227500a7b7ff98cc0dc7"
          },
          "delivery_plan": "",
          "contract": "",
          "impact": "2",
          "active": "false",
          "work_notes_list": "",
          "business_service": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16",
            "value": "27d32778c0a8000b00db970eeaa60f16"
          },
          "business_impact": "",
          "priority": "3",
          "sys_domain_path": "/",
          "rfc": "",
          "time_worked": "",
          "expected_start": "",
          "opened_at": "2016-12-12 15:19:57",
          "business_duration": "1970-01-01 08:00:00",
          "group_list": "",
          "work_end": "",
          "caller_id": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
            "value": "681ccaf9c0a8016400b98a06818d57c7"
          },
          "reopened_time": "",
          "resolved_at": "2016-12-13 21:43:14",
          "approval_set": "",
          "subcategory": "email",
          "work_notes": "",
          "universal_request": "",
          "short_description": "Unable to connect to email",
          "close_code": "Solved (Permanently)",
          "correlation_display": "",
          "delivery_task": "",
          "work_start": "",
          "assignment_group": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/287ebd7da9fe198100f92cc8d1d2154e",
            "value": "287ebd7da9fe198100f92cc8d1d2154e"
          },
          "additional_assignee_list": "",
          "business_stc": "28800",
          "cause": "",
          "description": "I am unable to connect to the email server. It appears to be down.",
          "origin_id": "",
          "calendar_duration": "1970-01-02 04:23:17",
          "close_notes": "This incident is resolved.",
          "notify": "1",
          "service_offering": "",
          "sys_class_name": "incident",
          "closed_by": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
            "value": "681ccaf9c0a8016400b98a06818d57c7"
          },
          "follow_up": "",
          "parent_incident": "",
          "sys_id": "1c741bd70b2322007518478d83673af3",
          "contact_type": "self-service",
          "reopened_by": "",
          "incident_state": "7",
          "urgency": "2",
          "problem_id": "",
          "company": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/core_company/31bea3d53790200044e0bfc8bcbe5dec",
            "value": "31bea3d53790200044e0bfc8bcbe5dec"
          },
          "reassignment_count": "2",
          "activity_due": "2016-12-13 01:26:36",
          "assigned_to": {
            "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007",
            "value": "5137153cc611227c000bbd1bd8cd2007"
          },
          "severity": "3",
          "comments": "",
          "approval": "not requested",
          "sla_due": "",
          "comments_and_work_notes": "",
          "due_date": "",
          "sys_mod_count": "15",
          "reopen_count": "0",
          "sys_tags": "",
          "escalation": "0",
          "upon_approval": "proceed",
          "correlation_id": "",
          "location": "",
          "category": "inquiry"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **result** (array): Auto-generated description for `result`. Please update manually if needed.
    - **parent** (string): Auto-generated description for `parent`. Please update manually if needed.
    - **made_sla** (string): Auto-generated description for `made_sla`. Please update manually if needed.
    - **caused_by** (string): Auto-generated description for `caused_by`. Please update manually if needed.
    - **watch_list** (string): Auto-generated description for `watch_list`. Please update manually if needed.
    - **upon_reject** (string): Auto-generated description for `upon_reject`. Please update manually if needed.
    - **sys_updated_on** (string): Auto-generated description for `sys_updated_on`. Please update manually if needed.
    - **child_incidents** (string): Auto-generated description for `child_incidents`. Please update manually if needed.
    - **hold_reason** (string): Auto-generated description for `hold_reason`. Please update manually if needed.
    - **origin_table** (string): Auto-generated description for `origin_table`. Please update manually if needed.
    - **task_effective_number** (string): Auto-generated description for `task_effective_number`. Please update manually if needed.
    - **approval_history** (string): Auto-generated description for `approval_history`. Please update manually if needed.
    - **number** (string): Auto-generated description for `number`. Please update manually if needed.
    - **resolved_by** (object): Auto-generated description for `resolved_by`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **sys_updated_by** (string): Auto-generated description for `sys_updated_by`. Please update manually if needed.
    - **opened_by** (object): Auto-generated description for `opened_by`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **user_input** (string): Auto-generated description for `user_input`. Please update manually if needed.
    - **sys_created_on** (string): Auto-generated description for `sys_created_on`. Please update manually if needed.
    - **sys_domain** (object): Auto-generated description for `sys_domain`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **state** (string): Auto-generated description for `state`. Please update manually if needed.
    - **route_reason** (string): Auto-generated description for `route_reason`. Please update manually if needed.
    - **sys_created_by** (string): Auto-generated description for `sys_created_by`. Please update manually if needed.
    - **knowledge** (string): Auto-generated description for `knowledge`. Please update manually if needed.
    - **order** (string): Auto-generated description for `order`. Please update manually if needed.
    - **calendar_stc** (string): Auto-generated description for `calendar_stc`. Please update manually if needed.
    - **closed_at** (string): Auto-generated description for `closed_at`. Please update manually if needed.
    - **cmdb_ci** (object): Auto-generated description for `cmdb_ci`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
    - **contract** (string): Auto-generated description for `contract`. Please update manually if needed.
    - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
    - **business_service** (object): Auto-generated description for `business_service`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **business_impact** (string): Auto-generated description for `business_impact`. Please update manually if needed.
    - **priority** (string): Auto-generated description for `priority`. Please update manually if needed.
    - **sys_domain_path** (string): Auto-generated description for `sys_domain_path`. Please update manually if needed.
    - **rfc** (string): Auto-generated description for `rfc`. Please update manually if needed.
    - **time_worked** (string): Auto-generated description for `time_worked`. Please update manually if needed.
    - **expected_start** (string): Auto-generated description for `expected_start`. Please update manually if needed.
    - **opened_at** (string): Auto-generated description for `opened_at`. Please update manually if needed.
    - **business_duration** (string): Auto-generated description for `business_duration`. Please update manually if needed.
    - **group_list** (string): Auto-generated description for `group_list`. Please update manually if needed.
    - **work_end** (string): Auto-generated description for `work_end`. Please update manually if needed.
    - **caller_id** (object): Auto-generated description for `caller_id`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **reopened_time** (string): Auto-generated description for `reopened_time`. Please update manually if needed.
    - **resolved_at** (string): Auto-generated description for `resolved_at`. Please update manually if needed.
    - **approval_set** (string): Auto-generated description for `approval_set`. Please update manually if needed.
    - **subcategory** (string): Auto-generated description for `subcategory`. Please update manually if needed.
    - **work_notes** (string): Auto-generated description for `work_notes`. Please update manually if needed.
    - **universal_request** (string): Auto-generated description for `universal_request`. Please update manually if needed.
    - **short_description** (string): Auto-generated description for `short_description`. Please update manually if needed.
    - **close_code** (string): Auto-generated description for `close_code`. Please update manually if needed.
    - **correlation_display** (string): Auto-generated description for `correlation_display`. Please update manually if needed.
    - **delivery_task** (string): Auto-generated description for `delivery_task`. Please update manually if needed.
    - **work_start** (string): Auto-generated description for `work_start`. Please update manually if needed.
    - **assignment_group** (object): Auto-generated description for `assignment_group`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **additional_assignee_list** (string): Auto-generated description for `additional_assignee_list`. Please update manually if needed.
    - **business_stc** (string): Auto-generated description for `business_stc`. Please update manually if needed.
    - **cause** (string): Auto-generated description for `cause`. Please update manually if needed.
    - **description** (string): Auto-generated description for `description`. Please update manually if needed.
    - **origin_id** (string): Auto-generated description for `origin_id`. Please update manually if needed.
    - **calendar_duration** (string): Auto-generated description for `calendar_duration`. Please update manually if needed.
    - **close_notes** (string): Auto-generated description for `close_notes`. Please update manually if needed.
    - **notify** (string): Auto-generated description for `notify`. Please update manually if needed.
    - **service_offering** (string): Auto-generated description for `service_offering`. Please update manually if needed.
    - **sys_class_name** (string): Auto-generated description for `sys_class_name`. Please update manually if needed.
    - **closed_by** (object): Auto-generated description for `closed_by`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
    - **parent_incident** (string): Auto-generated description for `parent_incident`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
    - **reopened_by** (string): Auto-generated description for `reopened_by`. Please update manually if needed.
    - **incident_state** (string): Auto-generated description for `incident_state`. Please update manually if needed.
    - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
    - **problem_id** (string): Auto-generated description for `problem_id`. Please update manually if needed.
    - **company** (object): Auto-generated description for `company`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **reassignment_count** (string): Auto-generated description for `reassignment_count`. Please update manually if needed.
    - **activity_due** (string): Auto-generated description for `activity_due`. Please update manually if needed.
    - **assigned_to** (object): Auto-generated description for `assigned_to`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **severity** (string): Auto-generated description for `severity`. Please update manually if needed.
    - **comments** (string): Auto-generated description for `comments`. Please update manually if needed.
    - **approval** (string): Auto-generated description for `approval`. Please update manually if needed.
    - **sla_due** (string): Auto-generated description for `sla_due`. Please update manually if needed.
    - **comments_and_work_notes** (string): Auto-generated description for `comments_and_work_notes`. Please update manually if needed.
    - **due_date** (string): Auto-generated description for `due_date`. Please update manually if needed.
    - **sys_mod_count** (string): Auto-generated description for `sys_mod_count`. Please update manually if needed.
    - **reopen_count** (string): Auto-generated description for `reopen_count`. Please update manually if needed.
    - **sys_tags** (string): Auto-generated description for `sys_tags`. Please update manually if needed.
    - **escalation** (string): Auto-generated description for `escalation`. Please update manually if needed.
    - **upon_approval** (string): Auto-generated description for `upon_approval`. Please update manually if needed.
    - **correlation_id** (string): Auto-generated description for `correlation_id`. Please update manually if needed.
    - **location** (string): Auto-generated description for `location`. Please update manually if needed.
    - **category** (string): Auto-generated description for `category`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| X-Is-Logged-In | string | Auto-generated description for `X-Is-Logged-In`. Please update manually if needed. |
| X-Transaction-ID | string | Auto-generated description for `X-Transaction-ID`. Please update manually if needed. |
| Link | string | Auto-generated description for `Link`. Please update manually if needed. |
| X-Total-Count | string | Auto-generated description for `X-Total-Count`. Please update manually if needed. |
| X-Content-Type-Options | string | Auto-generated description for `X-Content-Type-Options`. Please update manually if needed. |
| Pragma | string | Auto-generated description for `Pragma`. Please update manually if needed. |
| Cache-Control | string | Auto-generated description for `Cache-Control`. Please update manually if needed. |
| Expires | string | Auto-generated description for `Expires`. Please update manually if needed. |
| Content-Type | string | Auto-generated description for `Content-Type`. Please update manually if needed. |
| Transfer-Encoding | string | Auto-generated description for `Transfer-Encoding`. Please update manually if needed. |
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Keep-Alive | string | Auto-generated description for `Keep-Alive`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| Server | string | Auto-generated description for `Server`. Please update manually if needed. |
| Set-Cookie | string | Auto-generated description for `Set-Cookie`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |