# Create Incident

**Description**: Initiate incident response workflows by creating a new incident record in ServiceNow using the provided JSON body.

## Endpoint

- **URL:** `/api/now/table/incident`
- **Method:** `POST`
## Inputs

- **parameters** (object): TODO: Add description
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_exclude_reference_link** (boolean): Flag that indicates whether to exclude Table API links for reference fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_input_display_value** (boolean): Flag that indicates whether to set field values using the display value or the actual value.
  - **sysparm_view** (string): UI view for which to render the data. Determines the fields returned in the response.
- **json_body** (object) – Required: TODO: Add description
  - **short_description** (string): TODO: Add description
  - **assignment_group** (string): TODO: Add description
  - **urgency** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **impact** (string): Possible values are 1-High, 2-Medium, 3-Low.
  - **description** (string): TODO: Add description
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
  - **result** (object): TODO: Add description
    - **parent** (string): TODO: Add description
    - **made_sla** (string): TODO: Add description
    - **caused_by** (string): TODO: Add description
    - **watch_list** (string): TODO: Add description
    - **upon_reject** (string): TODO: Add description
    - **sys_updated_on** (string): TODO: Add description
    - **child_incidents** (string): TODO: Add description
    - **hold_reason** (string): TODO: Add description
    - **origin_table** (string): TODO: Add description
    - **task_effective_number** (string): TODO: Add description
    - **approval_history** (string): TODO: Add description
    - **number** (string): TODO: Add description
    - **resolved_by** (string): TODO: Add description
    - **sys_updated_by** (string): TODO: Add description
    - **opened_by** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **user_input** (string): TODO: Add description
    - **sys_created_on** (string): TODO: Add description
    - **sys_domain** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **state** (string): TODO: Add description
    - **route_reason** (string): TODO: Add description
    - **sys_created_by** (string): TODO: Add description
    - **knowledge** (string): TODO: Add description
    - **order** (string): TODO: Add description
    - **calendar_stc** (string): TODO: Add description
    - **closed_at** (string): TODO: Add description
    - **cmdb_ci** (string): TODO: Add description
    - **delivery_plan** (string): TODO: Add description
    - **contract** (string): TODO: Add description
    - **impact** (string): TODO: Add description
    - **active** (string): TODO: Add description
    - **work_notes_list** (string): TODO: Add description
    - **business_service** (string): TODO: Add description
    - **business_impact** (string): TODO: Add description
    - **priority** (string): TODO: Add description
    - **sys_domain_path** (string): TODO: Add description
    - **rfc** (string): TODO: Add description
    - **time_worked** (string): TODO: Add description
    - **expected_start** (string): TODO: Add description
    - **opened_at** (string): TODO: Add description
    - **business_duration** (string): TODO: Add description
    - **group_list** (string): TODO: Add description
    - **work_end** (string): TODO: Add description
    - **caller_id** (string): TODO: Add description
    - **reopened_time** (string): TODO: Add description
    - **resolved_at** (string): TODO: Add description
    - **approval_set** (string): TODO: Add description
    - **subcategory** (string): TODO: Add description
    - **work_notes** (string): TODO: Add description
    - **universal_request** (string): TODO: Add description
    - **short_description** (string): TODO: Add description
    - **close_code** (string): TODO: Add description
    - **correlation_display** (string): TODO: Add description
    - **delivery_task** (string): TODO: Add description
    - **work_start** (string): TODO: Add description
    - **assignment_group** (string): TODO: Add description
    - **additional_assignee_list** (string): TODO: Add description
    - **business_stc** (string): TODO: Add description
    - **cause** (string): TODO: Add description
    - **description** (string): TODO: Add description
    - **origin_id** (string): TODO: Add description
    - **calendar_duration** (string): TODO: Add description
    - **close_notes** (string): TODO: Add description
    - **notify** (string): TODO: Add description
    - **service_offering** (string): TODO: Add description
    - **sys_class_name** (string): TODO: Add description
    - **closed_by** (string): TODO: Add description
    - **follow_up** (string): TODO: Add description
    - **parent_incident** (string): TODO: Add description
    - **sys_id** (string): TODO: Add description
    - **contact_type** (string): TODO: Add description
    - **reopened_by** (string): TODO: Add description
    - **incident_state** (string): TODO: Add description
    - **urgency** (string): TODO: Add description
    - **problem_id** (string): TODO: Add description
    - **company** (string): TODO: Add description
    - **reassignment_count** (string): TODO: Add description
    - **activity_due** (string): TODO: Add description
    - **assigned_to** (string): TODO: Add description
    - **severity** (string): TODO: Add description
    - **comments** (string): TODO: Add description
    - **approval** (string): TODO: Add description
    - **sla_due** (string): TODO: Add description
    - **comments_and_work_notes** (string): TODO: Add description
    - **due_date** (string): TODO: Add description
    - **sys_mod_count** (string): TODO: Add description
    - **reopen_count** (string): TODO: Add description
    - **sys_tags** (string): TODO: Add description
    - **escalation** (string): TODO: Add description
    - **upon_approval** (string): TODO: Add description
    - **correlation_id** (string): TODO: Add description
    - **location** (string): TODO: Add description
    - **category** (string): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string | TODO: Add description |
| Server-Timing | string | TODO: Add description |
| Content-Encoding | string | TODO: Add description |
| X-Is-Logged-In | string | TODO: Add description |
| X-Transaction-ID | string | TODO: Add description |
| Location | string | TODO: Add description |
| X-Content-Type-Options | string | TODO: Add description |
| Pragma | string | TODO: Add description |
| Cache-Control | string | TODO: Add description |
| Expires | string | TODO: Add description |
| Content-Type | string | TODO: Add description |
| Transfer-Encoding | string | TODO: Add description |
| Date | string | TODO: Add description |
| Keep-Alive | string | TODO: Add description |
| Connection | string | TODO: Add description |
| Server | string | TODO: Add description |
| Strict-Transport-Security | string | TODO: Add description |