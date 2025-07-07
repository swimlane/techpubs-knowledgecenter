# Get all Incidents

**Description**: Retrieves all incident records from ServiceNow, with customization options for display values and result count limitation.

## Endpoint

- **URL:** `/api/now/v2/table/incident`
- **Method:** `GET`
## Inputs

- **parameters** (object): Structured object with nested properties.
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

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **result** (array): List of items.
    - **parent** (string): Text string.
    - **made_sla** (string): Text string.
    - **caused_by** (string): Text string.
    - **watch_list** (string): Text string.
    - **upon_reject** (string): Text string.
    - **sys_updated_on** (string): Timestamp in ISO 8601 format.
    - **child_incidents** (string): Unique identifier.
    - **hold_reason** (string): Text string.
    - **origin_table** (string): Text string.
    - **task_effective_number** (string): Text string.
    - **approval_history** (string): Text string.
    - **number** (string): Text string.
    - **resolved_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **sys_updated_by** (string): Timestamp in ISO 8601 format.
    - **opened_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **user_input** (string): Text string.
    - **sys_created_on** (string): Text string.
    - **sys_domain** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **state** (string): Text string.
    - **route_reason** (string): Text string.
    - **sys_created_by** (string): Text string.
    - **knowledge** (string): Text string.
    - **order** (string): Text string.
    - **calendar_stc** (string): Text string.
    - **closed_at** (string): Text string.
    - **cmdb_ci** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **delivery_plan** (string): Text string.
    - **contract** (string): Text string.
    - **impact** (string): Text string.
    - **active** (string): Text string.
    - **work_notes_list** (string): Text string.
    - **business_service** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **business_impact** (string): Text string.
    - **priority** (string): Text string.
    - **sys_domain_path** (string): Text string.
    - **rfc** (string): Text string.
    - **time_worked** (string): Timestamp in ISO 8601 format.
    - **expected_start** (string): Text string.
    - **opened_at** (string): Text string.
    - **business_duration** (string): Text string.
    - **group_list** (string): Text string.
    - **work_end** (string): Text string.
    - **caller_id** (object): Unique identifier.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **reopened_time** (string): Timestamp in ISO 8601 format.
    - **resolved_at** (string): Text string.
    - **approval_set** (string): Text string.
    - **subcategory** (string): Text string.
    - **work_notes** (string): Text string.
    - **universal_request** (string): Text string.
    - **short_description** (string): Text string.
    - **close_code** (string): Text string.
    - **correlation_display** (string): Text string.
    - **delivery_task** (string): Text string.
    - **work_start** (string): Text string.
    - **assignment_group** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **additional_assignee_list** (string): Text string.
    - **business_stc** (string): Text string.
    - **cause** (string): Text string.
    - **description** (string): Text string.
    - **origin_id** (string): Unique identifier.
    - **calendar_duration** (string): Text string.
    - **close_notes** (string): Text string.
    - **notify** (string): Text string.
    - **service_offering** (string): Text string.
    - **sys_class_name** (string): Name or label.
    - **closed_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **follow_up** (string): Text string.
    - **parent_incident** (string): Unique identifier.
    - **sys_id** (string): Unique identifier.
    - **contact_type** (string): Type of the resource or value.
    - **reopened_by** (string): Text string.
    - **incident_state** (string): Unique identifier.
    - **urgency** (string): Text string.
    - **problem_id** (string): Unique identifier.
    - **company** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **reassignment_count** (string): Number of occurrences or items.
    - **activity_due** (string): Text string.
    - **assigned_to** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **severity** (string): Text string.
    - **comments** (string): Text string.
    - **approval** (string): Text string.
    - **sla_due** (string): Text string.
    - **comments_and_work_notes** (string): Text string.
    - **due_date** (string): Timestamp in ISO 8601 format.
    - **sys_mod_count** (string): Number of occurrences or items.
    - **reopen_count** (string): Number of occurrences or items.
    - **sys_tags** (string): Text string.
    - **escalation** (string): Text string.
    - **upon_approval** (string): Text string.
    - **correlation_id** (string): Unique identifier.
    - **location** (string): Text string.
    - **category** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Text string. |
| Content-Encoding | string | Text string. |
| X-Is-Logged-In | string | Text string. |
| X-Transaction-ID | string | Unique identifier. |
| Link | string | Text string. |
| X-Total-Count | string | Number of occurrences or items. |
| X-Content-Type-Options | string | Type of the resource or value. |
| Pragma | string | Text string. |
| Cache-Control | string | Text string. |
| Expires | string | Text string. |
| Content-Type | string | Type of the resource or value. |
| Transfer-Encoding | string | Text string. |
| Date | string | Timestamp in ISO 8601 format. |
| Keep-Alive | string | Text string. |
| Connection | string | Text string. |
| Server | string | Text string. |
| Set-Cookie | string | Text string. |
| Strict-Transport-Security | string | Text string. |