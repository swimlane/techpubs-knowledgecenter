# Create Incident

**Description**: Initiate incident response workflows by creating a new incident record in ServiceNow using the provided JSON body.

## Endpoint

- **URL:** `/api/now/table/incident`
- **Method:** `POST`
## Inputs

- **parameters** (object)
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_exclude_reference_link** (boolean): Flag that indicates whether to exclude Table API links for reference fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_input_display_value** (boolean): Flag that indicates whether to set field values using the display value or the actual value.
  - **sysparm_view** (string): UI view for which to render the data. Determines the fields returned in the response.
- **json_body** (object) – Required
  - **short_description** (string)
  - **assignment_group** (string)
  - **urgency** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **impact** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **description** (string)
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

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (object)
    - **parent** (string)
    - **made_sla** (string)
    - **caused_by** (string)
    - **watch_list** (string)
    - **upon_reject** (string)
    - **sys_updated_on** (string)
    - **child_incidents** (string)
    - **hold_reason** (string)
    - **origin_table** (string)
    - **task_effective_number** (string)
    - **approval_history** (string)
    - **number** (string)
    - **resolved_by** (string)
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
    - **route_reason** (string)
    - **sys_created_by** (string)
    - **knowledge** (string)
    - **order** (string)
    - **calendar_stc** (string)
    - **closed_at** (string)
    - **cmdb_ci** (string)
    - **delivery_plan** (string)
    - **contract** (string)
    - **impact** (string)
    - **active** (string)
    - **work_notes_list** (string)
    - **business_service** (string)
    - **business_impact** (string)
    - **priority** (string)
    - **sys_domain_path** (string)
    - **rfc** (string)
    - **time_worked** (string)
    - **expected_start** (string)
    - **opened_at** (string)
    - **business_duration** (string)
    - **group_list** (string)
    - **work_end** (string)
    - **caller_id** (string)
    - **reopened_time** (string)
    - **resolved_at** (string)
    - **approval_set** (string)
    - **subcategory** (string)
    - **work_notes** (string)
    - **universal_request** (string)
    - **short_description** (string)
    - **close_code** (string)
    - **correlation_display** (string)
    - **delivery_task** (string)
    - **work_start** (string)
    - **assignment_group** (string)
    - **additional_assignee_list** (string)
    - **business_stc** (string)
    - **cause** (string)
    - **description** (string)
    - **origin_id** (string)
    - **calendar_duration** (string)
    - **close_notes** (string)
    - **notify** (string)
    - **service_offering** (string)
    - **sys_class_name** (string)
    - **closed_by** (string)
    - **follow_up** (string)
    - **parent_incident** (string)
    - **sys_id** (string)
    - **contact_type** (string)
    - **reopened_by** (string)
    - **incident_state** (string)
    - **urgency** (string)
    - **problem_id** (string)
    - **company** (string)
    - **reassignment_count** (string)
    - **activity_due** (string)
    - **assigned_to** (string)
    - **severity** (string)
    - **comments** (string)
    - **approval** (string)
    - **sla_due** (string)
    - **comments_and_work_notes** (string)
    - **due_date** (string)
    - **sys_mod_count** (string)
    - **reopen_count** (string)
    - **sys_tags** (string)
    - **escalation** (string)
    - **upon_approval** (string)
    - **correlation_id** (string)
    - **location** (string)
    - **category** (string)
## Response Headers

| Header | Type |
|--------|------|
| Set-Cookie | string |
| Server-Timing | string |
| Content-Encoding | string |
| X-Is-Logged-In | string |
| X-Transaction-ID | string |
| Location | string |
| X-Content-Type-Options | string |
| Pragma | string |
| Cache-Control | string |
| Expires | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Date | string |
| Keep-Alive | string |
| Connection | string |
| Server | string |
| Strict-Transport-Security | string |