# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **tableName** (string) – Required: Name of the table from which to retrieve the records.
- **parameters** (object): Auto-generated description for `parameters`. Please update manually if needed.
  - **name_value_pairs** (object): Auto-generated description for `name_value_pairs`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **assigned_to** (string): Auto-generated description for `assigned_to`. Please update manually if needed.
    - **state** (string): Auto-generated description for `state`. Please update manually if needed.
  - **sysparm_display_value** (string): Auto-generated description for `sysparm_display_value`. Please update manually if needed.
  - **sysparm_exclude_reference_link** (boolean): Auto-generated description for `sysparm_exclude_reference_link`. Please update manually if needed.
  - **sysparm_fields** (string): Auto-generated description for `sysparm_fields`. Please update manually if needed.
  - **sysparm_limit** (number): Auto-generated description for `sysparm_limit`. Please update manually if needed.
  - **sysparm_no_count** (boolean): Auto-generated description for `sysparm_no_count`. Please update manually if needed.
  - **sysparm_offset** (number): Auto-generated description for `sysparm_offset`. Please update manually if needed.
  - **sysparm_query** (string): Auto-generated description for `sysparm_query`. Please update manually if needed.
  - **sysparm_query_category** (string): Auto-generated description for `sysparm_query_category`. Please update manually if needed.
  - **sysparm_query_no_domain** (boolean): Auto-generated description for `sysparm_query_no_domain`. Please update manually if needed.
  - **sysparm_suppress_pagination_header** (boolean): Auto-generated description for `sysparm_suppress_pagination_header`. Please update manually if needed.
  - **sysparm_view** (string): Auto-generated description for `sysparm_view`. Please update manually if needed.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
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