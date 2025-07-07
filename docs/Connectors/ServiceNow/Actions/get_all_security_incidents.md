# Get all Security Incidents

**Description**: Retrieves all security incident records from ServiceNow, offering display customization and pagination options.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **security_incident** (string) – Required: Name of the Security Incident Table.
- **parameters** (object)
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

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (array)
    - **parent** (string)
    - **made_sla** (string)
    - **watch_list** (string)
    - **upon_reject** (string)
    - **sys_updated_on** (string)
    - **approval_history** (string)
    - **number** (string)
    - **sys_updated_by** (string)
    - **opened_by** (object)
      - **link** (string)
      - **value** (string)
    - **user_input** (string)
    - **sys_created_on** (string)
    - **sys_domain** (object)
      - **link** (string)
      - **value** (string)
    - **state** (string)
    - **sys_created_by** (string)
    - **knowledge** (string)
    - **order** (string)
    - **closed_at** (string)
    - **cmdb_ci** (object)
      - **link** (string)
      - **value** (string)
    - **delivery_plan** (string)
    - **impact** (string)
    - **active** (string)
    - **work_notes_list** (string)
    - **business_service** (string)
    - **priority** (string)
    - **sys_domain_path** (string)
    - **time_worked** (string)
    - **expected_start** (string)
    - **rejection_goto** (string)
    - **opened_at** (string)
    - **business_duration** (string)
    - **group_list** (string)
    - **work_end** (string)
    - **approval_set** (string)
    - **wf_activity** (string)
    - **work_notes** (string)
    - **short_description** (string)
    - **correlation_display** (string)
    - **delivery_task** (string)
    - **work_start** (string)
    - **assignment_group** (string)
    - **additional_assignee_list** (string)
    - **description** (string)
    - **calendar_duration** (string)
    - **close_notes** (string)
    - **sys_class_name** (string)
    - **closed_by** (string)
    - **follow_up** (string)
    - **sys_id** (string)
    - **contact_type** (string)
    - **urgency** (string)
    - **company** (string)
    - **reassignment_count** (string)
    - **activity_due** (string)
    - **assigned_to** (string)
    - **comments** (string)
    - **approval** (string)
    - **sla_due** (string)
    - **comments_and_work_notes** (string)
    - **due_date** (string)
    - **sys_mod_count** (string)
    - **sys_tags** (string)
    - **escalation** (string)
    - **upon_approval** (string)
    - **correlation_id** (string)
    - **location** (string)
## Response Headers

- **Server-Timing** (string)
- **Content-Encoding** (string)
- **X-Is-Logged-In** (string)
- **X-Transaction-ID** (string)
- **X-Total-Count** (string)
- **X-Content-Type-Options** (string)
- **Pragma** (string)
- **Cache-Control** (string)
- **Expires** (string)
- **Content-Type** (string)
- **Transfer-Encoding** (string)
- **Date** (string)
- **Keep-Alive** (string)
- **Connection** (string)
- **Server** (string)
- **Set-Cookie** (string)
- **Strict-Transport-Security** (string)