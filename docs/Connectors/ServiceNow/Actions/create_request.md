# Create Request

**Description**: Generates a new service request in ServiceNow, allowing for display value identification and input tracking.

## Endpoint

- **URL:** `/api/now/v2/table/sc_request`
- **Method:** `POST`
## Inputs

- **json_body** (object): TODO: Add description
  - **active** (boolean): TODO: Add description
  - **activity_due** (string): TODO: Add description
  - **additional_assignee_list** (string): TODO: Add description
  - **approval** (string): TODO: Add description
  - **approval_set** (string): TODO: Add description
  - **assigned_to** (string): TODO: Add description
  - **assignment_group** (string): TODO: Add description
  - **business_duration** (string): TODO: Add description
  - **business_service** (string): TODO: Add description
  - **calendar_duration** (string): TODO: Add description
  - **calendar_stc** (string): TODO: Add description
  - **close_notes** (string): TODO: Add description
  - **closed_at** (string): TODO: Add description
  - **closed_by** (string): TODO: Add description
  - **cmdb_ci** (object): TODO: Add description
    - **link** (string): TODO: Add description
    - **value** (string): TODO: Add description
  - **company** (string): TODO: Add description
  - **contact_type** (string): TODO: Add description
  - **contract** (string): TODO: Add description
  - **correlation** (string): TODO: Add description
  - **correlation_id** (string): TODO: Add description
  - **delivery_address** (string): TODO: Add description
  - **delivery_plan** (string): TODO: Add description
  - **delivery_task** (string): TODO: Add description
  - **description** (string): TODO: Add description
  - **due_date** (string): TODO: Add description
  - **escalation** (string): TODO: Add description
  - **expected_start** (string): TODO: Add description
  - **follow_up** (string): TODO: Add description
  - **group_list** (string): TODO: Add description
  - **impact** (string): TODO: Add description
  - **knowledge** (boolean): TODO: Add description
  - **location** (string): TODO: Add description
  - **made_sla** (boolean): TODO: Add description
  - **opened_at** (string): TODO: Add description
  - **opened_by** (object): TODO: Add description
    - **link** (string): TODO: Add description
    - **value** (string): TODO: Add description
  - **order** (string): TODO: Add description
  - **parent** (string): TODO: Add description
  - **parent_interaction** (string): TODO: Add description
  - **price** (string): TODO: Add description
  - **priority** (string): TODO: Add description
  - **reassignment_count** (string): TODO: Add description
  - **request_state** (string): TODO: Add description
  - **requested_date** (string): TODO: Add description
  - **requested_for** (string): TODO: Add description
  - **route_reason** (string): TODO: Add description
  - **service_offering** (string): TODO: Add description
  - **short_description** (string): TODO: Add description
  - **skills** (string): TODO: Add description
  - **sla_due** (string): TODO: Add description
  - **special_instructions** (string): TODO: Add description
  - **stage** (string): TODO: Add description
  - **state** (string): TODO: Add description
  - **time_worked** (string): TODO: Add description
  - **universal_request** (string): TODO: Add description
  - **upon_approval** (string): TODO: Add description
  - **upon_reject** (string): TODO: Add description
  - **urgency** (string): TODO: Add description
  - **user_input** (string): TODO: Add description
  - **watch_list** (string): TODO: Add description
  - **work_end** (string): TODO: Add description
  - **work_notes** (string): TODO: Add description
  - **work_notes_list** (string): TODO: Add description
  - **work_start** (string): TODO: Add description
- **parameters** (object): TODO: Add description
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
  - **result** (object): TODO: Add description
    - **parent** (string): TODO: Add description
    - **delivery_address** (string): TODO: Add description
    - **made_sla** (string): TODO: Add description
    - **watch_list** (string): TODO: Add description
    - **upon_reject** (string): TODO: Add description
    - **requested_for** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **sys_updated_on** (string): TODO: Add description
    - **task_effective_number** (string): TODO: Add description
    - **approval_history** (string): TODO: Add description
    - **number** (string): TODO: Add description
    - **sys_updated_by** (string): TODO: Add description
    - **opened_by** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **user_input** (string): TODO: Add description
    - **price** (string): TODO: Add description
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
    - **special_instructions** (string): TODO: Add description
    - **closed_at** (string): TODO: Add description
    - **cmdb_ci** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **delivery_plan** (string): TODO: Add description
    - **contract** (string): TODO: Add description
    - **impact** (string): TODO: Add description
    - **active** (string): TODO: Add description
    - **work_notes_list** (string): TODO: Add description
    - **business_service** (string): TODO: Add description
    - **priority** (string): TODO: Add description
    - **sys_domain_path** (string): TODO: Add description
    - **time_worked** (string): TODO: Add description
    - **expected_start** (string): TODO: Add description
    - **opened_at** (string): TODO: Add description
    - **business_duration** (string): TODO: Add description
    - **group_list** (string): TODO: Add description
    - **work_end** (string): TODO: Add description
    - **approval_set** (string): TODO: Add description
    - **work_notes** (string): TODO: Add description
    - **universal_request** (string): TODO: Add description
    - **short_description** (string): TODO: Add description
    - **correlation_display** (string): TODO: Add description
    - **delivery_task** (string): TODO: Add description
    - **work_start** (string): TODO: Add description
    - **assignment_group** (string): TODO: Add description
    - **parent_interaction** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **additional_assignee_list** (string): TODO: Add description
    - **description** (string): TODO: Add description
    - **calendar_duration** (string): TODO: Add description
    - **close_notes** (string): TODO: Add description
    - **service_offering** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **sys_class_name** (string): TODO: Add description
    - **closed_by** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **follow_up** (string): TODO: Add description
    - **sys_id** (string): TODO: Add description
    - **contact_type** (string): TODO: Add description
    - **urgency** (string): TODO: Add description
    - **requested_date** (string): TODO: Add description
    - **company** (string): TODO: Add description
    - **reassignment_count** (string): TODO: Add description
    - **activity_due** (string): TODO: Add description
    - **assigned_to** (string): TODO: Add description
    - **comments** (string): TODO: Add description
    - **approval** (string): TODO: Add description
    - **sla_due** (string): TODO: Add description
    - **comments_and_work_notes** (string): TODO: Add description
    - **due_date** (string): TODO: Add description
    - **sys_mod_count** (string): TODO: Add description
    - **sys_tags** (string): TODO: Add description
    - **request_state** (string): TODO: Add description
    - **stage** (string): TODO: Add description
    - **escalation** (string): TODO: Add description
    - **upon_approval** (string): TODO: Add description
    - **correlation_id** (string): TODO: Add description
    - **location** (string): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
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
| Set-Cookie | string | TODO: Add description |
| Strict-Transport-Security | string | TODO: Add description |