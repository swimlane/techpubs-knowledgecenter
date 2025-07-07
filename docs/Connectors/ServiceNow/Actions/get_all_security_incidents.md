# Get all Security Incidents

**Description**: Retrieves all security incident records from ServiceNow, offering display customization and pagination options.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **security_incident** (string) – Required: Name of the Security Incident Table.
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
      "X-Transaction-ID": "0a564c938322",
      "X-Total-Count": "1",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Mon, 23 Dec 2024 10:03:47 GMT",
      "Keep-Alive": "timeout=70",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "JSESSIONID=47A85A3A36C9AAE770C7A9D579538A40; Path=/; HttpOnly; SameSite=None; Secure, glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_user_route=glide.dd365af53b877647bfe3ca23d2bda88c; Max-Age=2147483647; Expires=Sat, 10-Jan-2093 13:17:54 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_node_id_for_js=a4405af3dee08de0f8588f376b703f40b8fc9b61228796a63788e51f33976436; Path=/; Secure; SameSite=None; Secure, glide_session_store=C2568C93832252100D5E9D60CEAAD38D; Max-Age=1800; Expires=Mon, 23-Dec-2024 10:33:47 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, BIGipServerpool_dev262724=2709626634.45630.0000; path=/; Httponly; Secure; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "result": [
        {
          "parent": "",
          "made_sla": "true",
          "watch_list": "",
          "upon_reject": "cancel",
          "sys_updated_on": "2016-01-19 04:52:04",
          "approval_history": "",
          "number": "PRB0000050",
          "sys_updated_by": "glide.maint",
          "opened_by": {
            "link": "https://instance.servicenow.com/api/now/table/sys_user/glide.maint",
            "value": "glide.maint"
          },
          "user_input": "",
          "sys_created_on": "2016-01-19 04:51:19",
          "sys_domain": {
            "link": "https://instance.servicenow.com/api/now/table/sys_user_group/global",
            "value": "global"
          },
          "state": "4",
          "sys_created_by": "glide.maint",
          "knowledge": "false",
          "order": "",
          "closed_at": "2016-01-19 04:52:04",
          "cmdb_ci": {
            "link": "https://instance.servicenow.com/api/now/table/cmdb_ci/55b35562c0a8010e01cff22378e0aea9",
            "value": "55b35562c0a8010e01cff22378e0aea9"
          },
          "delivery_plan": "",
          "impact": "3",
          "active": "false",
          "work_notes_list": "",
          "business_service": "",
          "priority": "4",
          "sys_domain_path": "/",
          "time_worked": "",
          "expected_start": "",
          "rejection_goto": "",
          "opened_at": "2016-01-19 04:49:47",
          "business_duration": "1970-01-01 00:00:00",
          "group_list": "",
          "work_end": "",
          "approval_set": "",
          "wf_activity": "",
          "work_notes": "",
          "short_description": "Switch occasionally drops connections",
          "correlation_display": "",
          "delivery_task": "",
          "work_start": "",
          "assignment_group": "",
          "additional_assignee_list": "",
          "description": "Switch occasionally drops connections",
          "calendar_duration": "1970-01-01 00:02:17",
          "close_notes": "updated firmware",
          "sys_class_name": "problem",
          "closed_by": "",
          "follow_up": "",
          "sys_id": "04ce72c9c0a8016600b5b7f75ac67b5b",
          "contact_type": "phone",
          "urgency": "3",
          "company": "",
          "reassignment_count": "",
          "activity_due": "",
          "assigned_to": "",
          "comments": "",
          "approval": "not requested",
          "sla_due": "",
          "comments_and_work_notes": "",
          "due_date": "",
          "sys_mod_count": "1",
          "sys_tags": "",
          "escalation": "0",
          "upon_approval": "proceed",
          "correlation_id": "",
          "location": ""
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
    - **watch_list** (string): Auto-generated description for `watch_list`. Please update manually if needed.
    - **upon_reject** (string): Auto-generated description for `upon_reject`. Please update manually if needed.
    - **sys_updated_on** (string): Auto-generated description for `sys_updated_on`. Please update manually if needed.
    - **approval_history** (string): Auto-generated description for `approval_history`. Please update manually if needed.
    - **number** (string): Auto-generated description for `number`. Please update manually if needed.
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
    - **sys_created_by** (string): Auto-generated description for `sys_created_by`. Please update manually if needed.
    - **knowledge** (string): Auto-generated description for `knowledge`. Please update manually if needed.
    - **order** (string): Auto-generated description for `order`. Please update manually if needed.
    - **closed_at** (string): Auto-generated description for `closed_at`. Please update manually if needed.
    - **cmdb_ci** (object): Auto-generated description for `cmdb_ci`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
    - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
    - **business_service** (string): Auto-generated description for `business_service`. Please update manually if needed.
    - **priority** (string): Auto-generated description for `priority`. Please update manually if needed.
    - **sys_domain_path** (string): Auto-generated description for `sys_domain_path`. Please update manually if needed.
    - **time_worked** (string): Auto-generated description for `time_worked`. Please update manually if needed.
    - **expected_start** (string): Auto-generated description for `expected_start`. Please update manually if needed.
    - **rejection_goto** (string): Auto-generated description for `rejection_goto`. Please update manually if needed.
    - **opened_at** (string): Auto-generated description for `opened_at`. Please update manually if needed.
    - **business_duration** (string): Auto-generated description for `business_duration`. Please update manually if needed.
    - **group_list** (string): Auto-generated description for `group_list`. Please update manually if needed.
    - **work_end** (string): Auto-generated description for `work_end`. Please update manually if needed.
    - **approval_set** (string): Auto-generated description for `approval_set`. Please update manually if needed.
    - **wf_activity** (string): Auto-generated description for `wf_activity`. Please update manually if needed.
    - **work_notes** (string): Auto-generated description for `work_notes`. Please update manually if needed.
    - **short_description** (string): Auto-generated description for `short_description`. Please update manually if needed.
    - **correlation_display** (string): Auto-generated description for `correlation_display`. Please update manually if needed.
    - **delivery_task** (string): Auto-generated description for `delivery_task`. Please update manually if needed.
    - **work_start** (string): Auto-generated description for `work_start`. Please update manually if needed.
    - **assignment_group** (string): Auto-generated description for `assignment_group`. Please update manually if needed.
    - **additional_assignee_list** (string): Auto-generated description for `additional_assignee_list`. Please update manually if needed.
    - **description** (string): Auto-generated description for `description`. Please update manually if needed.
    - **calendar_duration** (string): Auto-generated description for `calendar_duration`. Please update manually if needed.
    - **close_notes** (string): Auto-generated description for `close_notes`. Please update manually if needed.
    - **sys_class_name** (string): Auto-generated description for `sys_class_name`. Please update manually if needed.
    - **closed_by** (string): Auto-generated description for `closed_by`. Please update manually if needed.
    - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
    - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
    - **company** (string): Auto-generated description for `company`. Please update manually if needed.
    - **reassignment_count** (string): Auto-generated description for `reassignment_count`. Please update manually if needed.
    - **activity_due** (string): Auto-generated description for `activity_due`. Please update manually if needed.
    - **assigned_to** (string): Auto-generated description for `assigned_to`. Please update manually if needed.
    - **comments** (string): Auto-generated description for `comments`. Please update manually if needed.
    - **approval** (string): Auto-generated description for `approval`. Please update manually if needed.
    - **sla_due** (string): Auto-generated description for `sla_due`. Please update manually if needed.
    - **comments_and_work_notes** (string): Auto-generated description for `comments_and_work_notes`. Please update manually if needed.
    - **due_date** (string): Auto-generated description for `due_date`. Please update manually if needed.
    - **sys_mod_count** (string): Auto-generated description for `sys_mod_count`. Please update manually if needed.
    - **sys_tags** (string): Auto-generated description for `sys_tags`. Please update manually if needed.
    - **escalation** (string): Auto-generated description for `escalation`. Please update manually if needed.
    - **upon_approval** (string): Auto-generated description for `upon_approval`. Please update manually if needed.
    - **correlation_id** (string): Auto-generated description for `correlation_id`. Please update manually if needed.
    - **location** (string): Auto-generated description for `location`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| X-Is-Logged-In | string | Auto-generated description for `X-Is-Logged-In`. Please update manually if needed. |
| X-Transaction-ID | string | Auto-generated description for `X-Transaction-ID`. Please update manually if needed. |
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