# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: TODO: Add description
  - **tableName** (string) – Required: Name of the table from which to retrieve the records.
- **parameters** (object): TODO: Add description
  - **name_value_pairs** (object): TODO: Add description
    - **active** (string): TODO: Add description
    - **assigned_to** (string): TODO: Add description
    - **state** (string): TODO: Add description
  - **sysparm_display_value** (string): TODO: Add description
  - **sysparm_exclude_reference_link** (boolean): TODO: Add description
  - **sysparm_fields** (string): TODO: Add description
  - **sysparm_limit** (number): TODO: Add description
  - **sysparm_no_count** (boolean): TODO: Add description
  - **sysparm_offset** (number): TODO: Add description
  - **sysparm_query** (string): TODO: Add description
  - **sysparm_query_category** (string): TODO: Add description
  - **sysparm_query_no_domain** (boolean): TODO: Add description
  - **sysparm_suppress_pagination_header** (boolean): TODO: Add description
  - **sysparm_view** (string): TODO: Add description
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

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
  - **result** (array): TODO: Add description
    - **parent** (string): TODO: Add description
    - **made_sla** (string): TODO: Add description
    - **watch_list** (string): TODO: Add description
    - **upon_reject** (string): TODO: Add description
    - **sys_updated_on** (string): TODO: Add description
    - **approval_history** (string): TODO: Add description
    - **number** (string): TODO: Add description
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
    - **sys_created_by** (string): TODO: Add description
    - **knowledge** (string): TODO: Add description
    - **order** (string): TODO: Add description
    - **closed_at** (string): TODO: Add description
    - **cmdb_ci** (object): TODO: Add description
      - **link** (string): TODO: Add description
      - **value** (string): TODO: Add description
    - **delivery_plan** (string): TODO: Add description
    - **impact** (string): TODO: Add description
    - **active** (string): TODO: Add description
    - **work_notes_list** (string): TODO: Add description
    - **business_service** (string): TODO: Add description
    - **priority** (string): TODO: Add description
    - **sys_domain_path** (string): TODO: Add description
    - **time_worked** (string): TODO: Add description
    - **expected_start** (string): TODO: Add description
    - **rejection_goto** (string): TODO: Add description
    - **opened_at** (string): TODO: Add description
    - **business_duration** (string): TODO: Add description
    - **group_list** (string): TODO: Add description
    - **work_end** (string): TODO: Add description
    - **approval_set** (string): TODO: Add description
    - **wf_activity** (string): TODO: Add description
    - **work_notes** (string): TODO: Add description
    - **short_description** (string): TODO: Add description
    - **correlation_display** (string): TODO: Add description
    - **delivery_task** (string): TODO: Add description
    - **work_start** (string): TODO: Add description
    - **assignment_group** (string): TODO: Add description
    - **additional_assignee_list** (string): TODO: Add description
    - **description** (string): TODO: Add description
    - **calendar_duration** (string): TODO: Add description
    - **close_notes** (string): TODO: Add description
    - **sys_class_name** (string): TODO: Add description
    - **closed_by** (string): TODO: Add description
    - **follow_up** (string): TODO: Add description
    - **sys_id** (string): TODO: Add description
    - **contact_type** (string): TODO: Add description
    - **urgency** (string): TODO: Add description
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
    - **escalation** (string): TODO: Add description
    - **upon_approval** (string): TODO: Add description
    - **correlation_id** (string): TODO: Add description
    - **location** (string): TODO: Add description