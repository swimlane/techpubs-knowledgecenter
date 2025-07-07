# Create Request

**Description**: Generates a new service request in ServiceNow, allowing for display value identification and input tracking.

## Endpoint

- **URL:** `/api/now/v2/table/sc_request`
- **Method:** `POST`
## Inputs

- **json_body** (object): Structured object with nested properties.
  - **active** (boolean): True or False value.
  - **activity_due** (string): Text string.
  - **additional_assignee_list** (string): Text string.
  - **approval** (string): Text string.
  - **approval_set** (string): Text string.
  - **assigned_to** (string): Text string.
  - **assignment_group** (string): Text string.
  - **business_duration** (string): Text string.
  - **business_service** (string): Text string.
  - **calendar_duration** (string): Text string.
  - **calendar_stc** (string): Text string.
  - **close_notes** (string): Text string.
  - **closed_at** (string): Text string.
  - **closed_by** (string): Text string.
  - **cmdb_ci** (object): Structured object with nested properties.
    - **link** (string): Text string.
    - **value** (string): Text string.
  - **company** (string): Text string.
  - **contact_type** (string): Type of the resource or value.
  - **contract** (string): Text string.
  - **correlation** (string): Text string.
  - **correlation_id** (string): Unique identifier.
  - **delivery_address** (string): Text string.
  - **delivery_plan** (string): Text string.
  - **delivery_task** (string): Text string.
  - **description** (string): Text string.
  - **due_date** (string): Timestamp in ISO 8601 format.
  - **escalation** (string): Text string.
  - **expected_start** (string): Text string.
  - **follow_up** (string): Text string.
  - **group_list** (string): Text string.
  - **impact** (string): Text string.
  - **knowledge** (boolean): True or False value.
  - **location** (string): Text string.
  - **made_sla** (boolean): True or False value.
  - **opened_at** (string): Text string.
  - **opened_by** (object): Structured object with nested properties.
    - **link** (string): Text string.
    - **value** (string): Text string.
  - **order** (string): Text string.
  - **parent** (string): Text string.
  - **parent_interaction** (string): Text string.
  - **price** (string): Text string.
  - **priority** (string): Text string.
  - **reassignment_count** (string): Number of occurrences or items.
  - **request_state** (string): Text string.
  - **requested_date** (string): Timestamp in ISO 8601 format.
  - **requested_for** (string): Text string.
  - **route_reason** (string): Text string.
  - **service_offering** (string): Text string.
  - **short_description** (string): Text string.
  - **skills** (string): Text string.
  - **sla_due** (string): Text string.
  - **special_instructions** (string): Text string.
  - **stage** (string): Text string.
  - **state** (string): Text string.
  - **time_worked** (string): Timestamp in ISO 8601 format.
  - **universal_request** (string): Text string.
  - **upon_approval** (string): Text string.
  - **upon_reject** (string): Text string.
  - **urgency** (string): Text string.
  - **user_input** (string): Text string.
  - **watch_list** (string): Text string.
  - **work_end** (string): Text string.
  - **work_notes** (string): Text string.
  - **work_notes_list** (string): Text string.
  - **work_start** (string): Text string.
- **parameters** (object): Structured object with nested properties.
  - **sysparm_display_value** (boolean): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "096cc61b9736",
      "Location": "https://dev130168.service-now.com/api/now/v2/table/sc_request/896c865f9736111084d57e121153af5f",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Tue, 01 Nov 2022 21:20:31 GMT",
      "Keep-Alive": "timeout=20",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Mon, 20-Nov-2090 00:34:38 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=016C8ED79736111084D57E121153AF34; Max-Age=1800; Expires=Tue, 01-Nov-2022 21:50:31 GMT; Path=/; HttpOnly; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "Created",
    "json_body": {
      "result": {
        "parent": "",
        "delivery_address": "",
        "made_sla": "true",
        "watch_list": "",
        "upon_reject": "cancel",
        "requested_for": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/no value",
          "value": "no value"
        },
        "sys_updated_on": "2022-11-01 21:20:31",
        "task_effective_number": "REQ0010003",
        "approval_history": "",
        "number": "REQ0010003",
        "sys_updated_by": "admin",
        "opened_by": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/{link=https://instance.serviceno",
          "value": "{link=https://instance.serviceno"
        },
        "user_input": "",
        "price": "0",
        "sys_created_on": "2022-11-01 21:20:31",
        "sys_domain": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global",
          "value": "global"
        },
        "state": "4",
        "route_reason": "",
        "sys_created_by": "admin",
        "knowledge": "false",
        "order": "",
        "calendar_stc": "",
        "special_instructions": "no value",
        "closed_at": "2016-01-19 04:52:04",
        "cmdb_ci": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/{link=https://instance.serviceno",
          "value": "{link=https://instance.serviceno"
        },
        "delivery_plan": "",
        "contract": "",
        "impact": "3",
        "active": "false",
        "work_notes_list": "",
        "business_service": "",
        "priority": "4",
        "sys_domain_path": "/",
        "time_worked": "",
        "expected_start": "",
        "opened_at": "2016-01-19 04:49:47",
        "business_duration": "1970-01-01 00:00:00",
        "group_list": "",
        "work_end": "",
        "approval_set": "2022-11-01 21:20:31",
        "work_notes": "",
        "universal_request": "",
        "short_description": "Switch occasionally drops connections",
        "correlation_display": "",
        "delivery_task": "",
        "work_start": "",
        "assignment_group": "",
        "parent_interaction": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/interaction/no value",
          "value": "no value"
        },
        "additional_assignee_list": "",
        "description": "Switch occasionally drops connections",
        "calendar_duration": "1970-01-01 00:02:17",
        "close_notes": "updated firmware",
        "service_offering": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/service_offering/no value",
          "value": "no value"
        },
        "sys_class_name": "sc_request",
        "closed_by": {
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/6816f79cc0a8016401c5a33be04be441",
          "value": "6816f79cc0a8016401c5a33be04be441"
        },
        "follow_up": "",
        "sys_id": "896c865f9736111084d57e121153af5f",
        "contact_type": "phone",
        "urgency": "3",
        "requested_date": "",
        "company": "",
        "reassignment_count": "0",
        "activity_due": "",
        "assigned_to": "",
        "comments": "",
        "approval": "approved",
        "sla_due": "",
        "comments_and_work_notes": "",
        "due_date": "",
        "sys_mod_count": "0",
        "sys_tags": "",
        "request_state": "in_process",
        "stage": "requested",
        "escalation": "0",
        "upon_approval": "proceed",
        "correlation_id": "",
        "location": ""
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
    - **delivery_address** (string): Text string.
    - **made_sla** (string): Text string.
    - **watch_list** (string): Text string.
    - **upon_reject** (string): Text string.
    - **requested_for** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **sys_updated_on** (string): Timestamp in ISO 8601 format.
    - **task_effective_number** (string): Text string.
    - **approval_history** (string): Text string.
    - **number** (string): Text string.
    - **sys_updated_by** (string): Timestamp in ISO 8601 format.
    - **opened_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **user_input** (string): Text string.
    - **price** (string): Text string.
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
    - **special_instructions** (string): Text string.
    - **closed_at** (string): Text string.
    - **cmdb_ci** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **delivery_plan** (string): Text string.
    - **contract** (string): Text string.
    - **impact** (string): Text string.
    - **active** (string): Text string.
    - **work_notes_list** (string): Text string.
    - **business_service** (string): Text string.
    - **priority** (string): Text string.
    - **sys_domain_path** (string): Text string.
    - **time_worked** (string): Timestamp in ISO 8601 format.
    - **expected_start** (string): Text string.
    - **opened_at** (string): Text string.
    - **business_duration** (string): Text string.
    - **group_list** (string): Text string.
    - **work_end** (string): Text string.
    - **approval_set** (string): Text string.
    - **work_notes** (string): Text string.
    - **universal_request** (string): Text string.
    - **short_description** (string): Text string.
    - **correlation_display** (string): Text string.
    - **delivery_task** (string): Text string.
    - **work_start** (string): Text string.
    - **assignment_group** (string): Text string.
    - **parent_interaction** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **additional_assignee_list** (string): Text string.
    - **description** (string): Text string.
    - **calendar_duration** (string): Text string.
    - **close_notes** (string): Text string.
    - **service_offering** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **sys_class_name** (string): Name or label.
    - **closed_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **follow_up** (string): Text string.
    - **sys_id** (string): Unique identifier.
    - **contact_type** (string): Type of the resource or value.
    - **urgency** (string): Text string.
    - **requested_date** (string): Timestamp in ISO 8601 format.
    - **company** (string): Text string.
    - **reassignment_count** (string): Number of occurrences or items.
    - **activity_due** (string): Text string.
    - **assigned_to** (string): Text string.
    - **comments** (string): Text string.
    - **approval** (string): Text string.
    - **sla_due** (string): Text string.
    - **comments_and_work_notes** (string): Text string.
    - **due_date** (string): Timestamp in ISO 8601 format.
    - **sys_mod_count** (string): Number of occurrences or items.
    - **sys_tags** (string): Text string.
    - **request_state** (string): Text string.
    - **stage** (string): Text string.
    - **escalation** (string): Text string.
    - **upon_approval** (string): Text string.
    - **correlation_id** (string): Unique identifier.
    - **location** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
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
| Set-Cookie | string | Text string. |
| Strict-Transport-Security | string | Text string. |