# Create Incident

**Description**: Initiate incident response workflows by creating a new incident record in ServiceNow using the provided JSON body.

## Endpoint

- **URL:** `/api/now/table/incident`
- **Method:** `POST`
## Inputs

- **parameters** (object): Structured object with nested properties.
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_exclude_reference_link** (boolean): Flag that indicates whether to exclude Table API links for reference fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_input_display_value** (boolean): Flag that indicates whether to set field values using the display value or the actual value.
  - **sysparm_view** (string): UI view for which to render the data. Determines the fields returned in the response.
- **json_body** (object) – Required: Structured object with nested properties.
  - **short_description** (string): Text string.
  - **assignment_group** (string): Text string.
  - **urgency** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **impact** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **description** (string): Text string.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Set-Cookie": "JSESSIONID=65CFEB1152B06972DD21833AFE556414; Path=/; HttpOnly;Secure, glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly, glide_user_route=glide.0523df0e933b3d0b61bd3203715792eb; Max-Age=2147483647; Expires=Sat, 25-Aug-2091 14:13:46 GMT; Path=/; Secure; HttpOnly, glide_session_store=2AD13C4147203110D737CD9BD36D43A3; Max-Age=1800; Expires=Mon, 07-Aug-2023 11:29:39 GMT; Path=/; Secure; HttpOnly, BIGipServerpool_dev60827=999184138.46398.0000; path=/; Httponly; Secure",
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "6ed13c41a300",
      "Location": "https://dev60827.service-now.com/api/now/v2/table/incident/26d1744d47603110d737cd9bd36d436b",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Mon, 07 Aug 2023 10:59:39 GMT",
      "Keep-Alive": "timeout=70",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "Created",
    "json_body": {
      "result": {
        "parent": "",
        "made_sla": "true",
        "caused_by": "",
        "watch_list": "",
        "upon_reject": "cancel",
        "sys_updated_on": "2023-08-07 10:59:39",
        "child_incidents": "0",
        "hold_reason": "",
        "origin_table": "",
        "task_effective_number": "INC0010006",
        "approval_history": "",
        "number": "INC0010006",
        "resolved_by": "",
        "sys_updated_by": "admin",
        "opened_by": {
          "link": "https://dev60827.service-now.com/api/now/v2/table/sys_user/6816f79cc0a8016401c5a33be04be441",
          "value": "6816f79cc0a8016401c5a33be04be441"
        },
        "user_input": "",
        "sys_created_on": "2023-08-07 10:59:39",
        "sys_domain": {
          "link": "https://dev60827.service-now.com/api/now/v2/table/sys_user_group/global",
          "value": "global"
        },
        "state": "1",
        "route_reason": "",
        "sys_created_by": "admin",
        "knowledge": "false",
        "order": "",
        "calendar_stc": "",
        "closed_at": "",
        "cmdb_ci": "",
        "delivery_plan": "",
        "contract": "",
        "impact": "3",
        "active": "true",
        "work_notes_list": "",
        "business_service": "",
        "business_impact": "",
        "priority": "5",
        "sys_domain_path": "/",
        "rfc": "",
        "time_worked": "",
        "expected_start": "",
        "opened_at": "2023-08-07 10:59:39",
        "business_duration": "",
        "group_list": "",
        "work_end": "",
        "caller_id": "",
        "reopened_time": "",
        "resolved_at": "",
        "approval_set": "",
        "subcategory": "",
        "work_notes": "",
        "universal_request": "",
        "short_description": "",
        "close_code": "",
        "correlation_display": "",
        "delivery_task": "",
        "work_start": "",
        "assignment_group": "",
        "additional_assignee_list": "",
        "business_stc": "",
        "cause": "",
        "description": "",
        "origin_id": "",
        "calendar_duration": "",
        "close_notes": "",
        "notify": "1",
        "service_offering": "",
        "sys_class_name": "incident",
        "closed_by": "",
        "follow_up": "",
        "parent_incident": "",
        "sys_id": "26d1744d47603110d737cd9bd36d436b",
        "contact_type": "",
        "reopened_by": "",
        "incident_state": "1",
        "urgency": "3",
        "problem_id": "",
        "company": "",
        "reassignment_count": "0",
        "activity_due": "",
        "assigned_to": "",
        "severity": "3",
        "comments": "",
        "approval": "not requested",
        "sla_due": "",
        "comments_and_work_notes": "",
        "due_date": "",
        "sys_mod_count": "0",
        "reopen_count": "0",
        "sys_tags": "",
        "escalation": "0",
        "upon_approval": "proceed",
        "correlation_id": "",
        "location": "",
        "category": "inquiry"
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **result** (object): Structured object with nested properties.
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
    - **resolved_by** (string): Text string.
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
    - **cmdb_ci** (string): Text string.
    - **delivery_plan** (string): Text string.
    - **contract** (string): Text string.
    - **impact** (string): Text string.
    - **active** (string): Text string.
    - **work_notes_list** (string): Text string.
    - **business_service** (string): Text string.
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
    - **caller_id** (string): Unique identifier.
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
    - **assignment_group** (string): Text string.
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
    - **closed_by** (string): Text string.
    - **follow_up** (string): Text string.
    - **parent_incident** (string): Unique identifier.
    - **sys_id** (string): Unique identifier.
    - **contact_type** (string): Type of the resource or value.
    - **reopened_by** (string): Text string.
    - **incident_state** (string): Unique identifier.
    - **urgency** (string): Text string.
    - **problem_id** (string): Unique identifier.
    - **company** (string): Text string.
    - **reassignment_count** (string): Number of occurrences or items.
    - **activity_due** (string): Text string.
    - **assigned_to** (string): Text string.
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
| Set-Cookie | string | Text string. |
| Server-Timing | string | Text string. |
| Content-Encoding | string | Text string. |
| X-Is-Logged-In | string | Text string. |
| X-Transaction-ID | string | Unique identifier. |
| Location | string | Text string. |
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
| Strict-Transport-Security | string | Text string. |