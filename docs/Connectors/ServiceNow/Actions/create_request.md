# Create Request

**Description**: Generates a new service request in ServiceNow, allowing for display value identification and input tracking.

## Endpoint

- **URL:** `/api/now/v2/table/sc_request`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **active** (boolean)
  - **activity_due** (string)
  - **additional_assignee_list** (string)
  - **approval** (string)
  - **approval_set** (string)
  - **assigned_to** (string)
  - **assignment_group** (string)
  - **business_duration** (string)
  - **business_service** (string)
  - **calendar_duration** (string)
  - **calendar_stc** (string)
  - **close_notes** (string)
  - **closed_at** (string)
  - **closed_by** (string)
  - **cmdb_ci** (object)
    - **link** (string)
    - **value** (string)
  - **company** (string)
  - **contact_type** (string)
  - **contract** (string)
  - **correlation** (string)
  - **correlation_id** (string)
  - **delivery_address** (string)
  - **delivery_plan** (string)
  - **delivery_task** (string)
  - **description** (string)
  - **due_date** (string)
  - **escalation** (string)
  - **expected_start** (string)
  - **follow_up** (string)
  - **group_list** (string)
  - **impact** (string)
  - **knowledge** (boolean)
  - **location** (string)
  - **made_sla** (boolean)
  - **opened_at** (string)
  - **opened_by** (object)
    - **link** (string)
    - **value** (string)
  - **order** (string)
  - **parent** (string)
  - **parent_interaction** (string)
  - **price** (string)
  - **priority** (string)
  - **reassignment_count** (string)
  - **request_state** (string)
  - **requested_date** (string)
  - **requested_for** (string)
  - **route_reason** (string)
  - **service_offering** (string)
  - **short_description** (string)
  - **skills** (string)
  - **sla_due** (string)
  - **special_instructions** (string)
  - **stage** (string)
  - **state** (string)
  - **time_worked** (string)
  - **universal_request** (string)
  - **upon_approval** (string)
  - **upon_reject** (string)
  - **urgency** (string)
  - **user_input** (string)
  - **watch_list** (string)
  - **work_end** (string)
  - **work_notes** (string)
  - **work_notes_list** (string)
  - **work_start** (string)
- **parameters** (object)
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

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (object)
    - **parent** (string)
    - **delivery_address** (string)
    - **made_sla** (string)
    - **watch_list** (string)
    - **upon_reject** (string)
    - **requested_for** (object)
      - **link** (string)
      - **value** (string)
    - **sys_updated_on** (string)
    - **task_effective_number** (string)
    - **approval_history** (string)
    - **number** (string)
    - **sys_updated_by** (string)
    - **opened_by** (object)
      - **link** (string)
      - **value** (string)
    - **user_input** (string)
    - **price** (string)
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
    - **special_instructions** (string)
    - **closed_at** (string)
    - **cmdb_ci** (object)
      - **link** (string)
      - **value** (string)
    - **delivery_plan** (string)
    - **contract** (string)
    - **impact** (string)
    - **active** (string)
    - **work_notes_list** (string)
    - **business_service** (string)
    - **priority** (string)
    - **sys_domain_path** (string)
    - **time_worked** (string)
    - **expected_start** (string)
    - **opened_at** (string)
    - **business_duration** (string)
    - **group_list** (string)
    - **work_end** (string)
    - **approval_set** (string)
    - **work_notes** (string)
    - **universal_request** (string)
    - **short_description** (string)
    - **correlation_display** (string)
    - **delivery_task** (string)
    - **work_start** (string)
    - **assignment_group** (string)
    - **parent_interaction** (object)
      - **link** (string)
      - **value** (string)
    - **additional_assignee_list** (string)
    - **description** (string)
    - **calendar_duration** (string)
    - **close_notes** (string)
    - **service_offering** (object)
      - **link** (string)
      - **value** (string)
    - **sys_class_name** (string)
    - **closed_by** (object)
      - **link** (string)
      - **value** (string)
    - **follow_up** (string)
    - **sys_id** (string)
    - **contact_type** (string)
    - **urgency** (string)
    - **requested_date** (string)
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
    - **request_state** (string)
    - **stage** (string)
    - **escalation** (string)
    - **upon_approval** (string)
    - **correlation_id** (string)
    - **location** (string)
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| Location | string |  |
| X-Content-Type-Options | string |  |
| Pragma | string |  |
| Cache-Control | string |  |
| Expires | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Date | string |  |
| Keep-Alive | string |  |
| Connection | string |  |
| Server | string |  |
| Set-Cookie | string |  |
| Strict-Transport-Security | string |  |