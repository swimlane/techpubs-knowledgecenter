# Create Security Incident

**Description**: Creates a new security incident in ServiceNow based on the provided path parameters.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **security_incident** (string) – Required: Name of the Security Incident Table
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_exclude_reference_link** (boolean): Flag that indicates whether to exclude Table API links for reference fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_input_display_value** (boolean): Flag that indicates whether to set field values using the display value or the actual value.
  - **sysparm_view** (string): If you also specify the sysparm_fields parameter, it takes precedent.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **result** (object): Auto-generated description for `result`. Please update manually if needed.
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
    - **resolved_by** (string): Auto-generated description for `resolved_by`. Please update manually if needed.
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
    - **cmdb_ci** (string): Auto-generated description for `cmdb_ci`. Please update manually if needed.
    - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
    - **contract** (string): Auto-generated description for `contract`. Please update manually if needed.
    - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
    - **business_service** (string): Auto-generated description for `business_service`. Please update manually if needed.
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
    - **caller_id** (string): Auto-generated description for `caller_id`. Please update manually if needed.
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
    - **assignment_group** (string): Auto-generated description for `assignment_group`. Please update manually if needed.
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
    - **closed_by** (string): Auto-generated description for `closed_by`. Please update manually if needed.
    - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
    - **parent_incident** (string): Auto-generated description for `parent_incident`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
    - **reopened_by** (string): Auto-generated description for `reopened_by`. Please update manually if needed.
    - **incident_state** (string): Auto-generated description for `incident_state`. Please update manually if needed.
    - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
    - **problem_id** (string): Auto-generated description for `problem_id`. Please update manually if needed.
    - **company** (string): Auto-generated description for `company`. Please update manually if needed.
    - **reassignment_count** (string): Auto-generated description for `reassignment_count`. Please update manually if needed.
    - **activity_due** (string): Auto-generated description for `activity_due`. Please update manually if needed.
    - **assigned_to** (string): Auto-generated description for `assigned_to`. Please update manually if needed.
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
| Set-Cookie | string | Auto-generated description for `Set-Cookie`. Please update manually if needed. |
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| X-Is-Logged-In | string | Auto-generated description for `X-Is-Logged-In`. Please update manually if needed. |
| X-Transaction-ID | string | Auto-generated description for `X-Transaction-ID`. Please update manually if needed. |
| Location | string | Auto-generated description for `Location`. Please update manually if needed. |
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
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |