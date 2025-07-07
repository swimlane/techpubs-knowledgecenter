# Create Request

**Description**: Generates a new service request in ServiceNow, allowing for display value identification and input tracking.

## Endpoint

- **URL:** `/api/now/v2/table/sc_request`
- **Method:** `POST`
## Inputs

- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **active** (boolean): Auto-generated description for `active`. Please update manually if needed.
  - **activity_due** (string): Auto-generated description for `activity_due`. Please update manually if needed.
  - **additional_assignee_list** (string): Auto-generated description for `additional_assignee_list`. Please update manually if needed.
  - **approval** (string): Auto-generated description for `approval`. Please update manually if needed.
  - **approval_set** (string): Auto-generated description for `approval_set`. Please update manually if needed.
  - **assigned_to** (string): Auto-generated description for `assigned_to`. Please update manually if needed.
  - **assignment_group** (string): Auto-generated description for `assignment_group`. Please update manually if needed.
  - **business_duration** (string): Auto-generated description for `business_duration`. Please update manually if needed.
  - **business_service** (string): Auto-generated description for `business_service`. Please update manually if needed.
  - **calendar_duration** (string): Auto-generated description for `calendar_duration`. Please update manually if needed.
  - **calendar_stc** (string): Auto-generated description for `calendar_stc`. Please update manually if needed.
  - **close_notes** (string): Auto-generated description for `close_notes`. Please update manually if needed.
  - **closed_at** (string): Auto-generated description for `closed_at`. Please update manually if needed.
  - **closed_by** (string): Auto-generated description for `closed_by`. Please update manually if needed.
  - **cmdb_ci** (object): Auto-generated description for `cmdb_ci`. Please update manually if needed.
    - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **value** (string): Auto-generated description for `value`. Please update manually if needed.
  - **company** (string): Auto-generated description for `company`. Please update manually if needed.
  - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
  - **contract** (string): Auto-generated description for `contract`. Please update manually if needed.
  - **correlation** (string): Auto-generated description for `correlation`. Please update manually if needed.
  - **correlation_id** (string): Auto-generated description for `correlation_id`. Please update manually if needed.
  - **delivery_address** (string): Auto-generated description for `delivery_address`. Please update manually if needed.
  - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
  - **delivery_task** (string): Auto-generated description for `delivery_task`. Please update manually if needed.
  - **description** (string): Auto-generated description for `description`. Please update manually if needed.
  - **due_date** (string): Auto-generated description for `due_date`. Please update manually if needed.
  - **escalation** (string): Auto-generated description for `escalation`. Please update manually if needed.
  - **expected_start** (string): Auto-generated description for `expected_start`. Please update manually if needed.
  - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
  - **group_list** (string): Auto-generated description for `group_list`. Please update manually if needed.
  - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
  - **knowledge** (boolean): Auto-generated description for `knowledge`. Please update manually if needed.
  - **location** (string): Auto-generated description for `location`. Please update manually if needed.
  - **made_sla** (boolean): Auto-generated description for `made_sla`. Please update manually if needed.
  - **opened_at** (string): Auto-generated description for `opened_at`. Please update manually if needed.
  - **opened_by** (object): Auto-generated description for `opened_by`. Please update manually if needed.
    - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **value** (string): Auto-generated description for `value`. Please update manually if needed.
  - **order** (string): Auto-generated description for `order`. Please update manually if needed.
  - **parent** (string): Auto-generated description for `parent`. Please update manually if needed.
  - **parent_interaction** (string): Auto-generated description for `parent_interaction`. Please update manually if needed.
  - **price** (string): Auto-generated description for `price`. Please update manually if needed.
  - **priority** (string): Auto-generated description for `priority`. Please update manually if needed.
  - **reassignment_count** (string): Auto-generated description for `reassignment_count`. Please update manually if needed.
  - **request_state** (string): Auto-generated description for `request_state`. Please update manually if needed.
  - **requested_date** (string): Auto-generated description for `requested_date`. Please update manually if needed.
  - **requested_for** (string): Auto-generated description for `requested_for`. Please update manually if needed.
  - **route_reason** (string): Auto-generated description for `route_reason`. Please update manually if needed.
  - **service_offering** (string): Auto-generated description for `service_offering`. Please update manually if needed.
  - **short_description** (string): Auto-generated description for `short_description`. Please update manually if needed.
  - **skills** (string): Auto-generated description for `skills`. Please update manually if needed.
  - **sla_due** (string): Auto-generated description for `sla_due`. Please update manually if needed.
  - **special_instructions** (string): Auto-generated description for `special_instructions`. Please update manually if needed.
  - **stage** (string): Auto-generated description for `stage`. Please update manually if needed.
  - **state** (string): Auto-generated description for `state`. Please update manually if needed.
  - **time_worked** (string): Auto-generated description for `time_worked`. Please update manually if needed.
  - **universal_request** (string): Auto-generated description for `universal_request`. Please update manually if needed.
  - **upon_approval** (string): Auto-generated description for `upon_approval`. Please update manually if needed.
  - **upon_reject** (string): Auto-generated description for `upon_reject`. Please update manually if needed.
  - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
  - **user_input** (string): Auto-generated description for `user_input`. Please update manually if needed.
  - **watch_list** (string): Auto-generated description for `watch_list`. Please update manually if needed.
  - **work_end** (string): Auto-generated description for `work_end`. Please update manually if needed.
  - **work_notes** (string): Auto-generated description for `work_notes`. Please update manually if needed.
  - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
  - **work_start** (string): Auto-generated description for `work_start`. Please update manually if needed.
- **parameters** (object): Auto-generated description for `parameters`. Please update manually if needed.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **result** (object): Auto-generated description for `result`. Please update manually if needed.
    - **parent** (string): Auto-generated description for `parent`. Please update manually if needed.
    - **delivery_address** (string): Auto-generated description for `delivery_address`. Please update manually if needed.
    - **made_sla** (string): Auto-generated description for `made_sla`. Please update manually if needed.
    - **watch_list** (string): Auto-generated description for `watch_list`. Please update manually if needed.
    - **upon_reject** (string): Auto-generated description for `upon_reject`. Please update manually if needed.
    - **requested_for** (object): Auto-generated description for `requested_for`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **sys_updated_on** (string): Auto-generated description for `sys_updated_on`. Please update manually if needed.
    - **task_effective_number** (string): Auto-generated description for `task_effective_number`. Please update manually if needed.
    - **approval_history** (string): Auto-generated description for `approval_history`. Please update manually if needed.
    - **number** (string): Auto-generated description for `number`. Please update manually if needed.
    - **sys_updated_by** (string): Auto-generated description for `sys_updated_by`. Please update manually if needed.
    - **opened_by** (object): Auto-generated description for `opened_by`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **user_input** (string): Auto-generated description for `user_input`. Please update manually if needed.
    - **price** (string): Auto-generated description for `price`. Please update manually if needed.
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
    - **special_instructions** (string): Auto-generated description for `special_instructions`. Please update manually if needed.
    - **closed_at** (string): Auto-generated description for `closed_at`. Please update manually if needed.
    - **cmdb_ci** (object): Auto-generated description for `cmdb_ci`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
    - **contract** (string): Auto-generated description for `contract`. Please update manually if needed.
    - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
    - **business_service** (string): Auto-generated description for `business_service`. Please update manually if needed.
    - **priority** (string): Auto-generated description for `priority`. Please update manually if needed.
    - **sys_domain_path** (string): Auto-generated description for `sys_domain_path`. Please update manually if needed.
    - **time_worked** (string): Auto-generated description for `time_worked`. Please update manually if needed.
    - **expected_start** (string): Auto-generated description for `expected_start`. Please update manually if needed.
    - **opened_at** (string): Auto-generated description for `opened_at`. Please update manually if needed.
    - **business_duration** (string): Auto-generated description for `business_duration`. Please update manually if needed.
    - **group_list** (string): Auto-generated description for `group_list`. Please update manually if needed.
    - **work_end** (string): Auto-generated description for `work_end`. Please update manually if needed.
    - **approval_set** (string): Auto-generated description for `approval_set`. Please update manually if needed.
    - **work_notes** (string): Auto-generated description for `work_notes`. Please update manually if needed.
    - **universal_request** (string): Auto-generated description for `universal_request`. Please update manually if needed.
    - **short_description** (string): Auto-generated description for `short_description`. Please update manually if needed.
    - **correlation_display** (string): Auto-generated description for `correlation_display`. Please update manually if needed.
    - **delivery_task** (string): Auto-generated description for `delivery_task`. Please update manually if needed.
    - **work_start** (string): Auto-generated description for `work_start`. Please update manually if needed.
    - **assignment_group** (string): Auto-generated description for `assignment_group`. Please update manually if needed.
    - **parent_interaction** (object): Auto-generated description for `parent_interaction`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **additional_assignee_list** (string): Auto-generated description for `additional_assignee_list`. Please update manually if needed.
    - **description** (string): Auto-generated description for `description`. Please update manually if needed.
    - **calendar_duration** (string): Auto-generated description for `calendar_duration`. Please update manually if needed.
    - **close_notes** (string): Auto-generated description for `close_notes`. Please update manually if needed.
    - **service_offering** (object): Auto-generated description for `service_offering`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **sys_class_name** (string): Auto-generated description for `sys_class_name`. Please update manually if needed.
    - **closed_by** (object): Auto-generated description for `closed_by`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
      - **value** (string): Auto-generated description for `value`. Please update manually if needed.
    - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
    - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
    - **requested_date** (string): Auto-generated description for `requested_date`. Please update manually if needed.
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
    - **request_state** (string): Auto-generated description for `request_state`. Please update manually if needed.
    - **stage** (string): Auto-generated description for `stage`. Please update manually if needed.
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
| Set-Cookie | string | Auto-generated description for `Set-Cookie`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |