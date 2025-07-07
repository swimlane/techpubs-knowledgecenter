# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **tableName** (string) – Required: Name of the table from which to retrieve the records.
- **parameters** (object)
  - **name_value_pairs** (object)
    - **active** (string)
    - **assigned_to** (string)
    - **state** (string)
  - **sysparm_display_value** (string)
  - **sysparm_exclude_reference_link** (boolean)
  - **sysparm_fields** (string)
  - **sysparm_limit** (number)
  - **sysparm_no_count** (boolean)
  - **sysparm_offset** (number)
  - **sysparm_query** (string)
  - **sysparm_query_category** (string)
  - **sysparm_query_no_domain** (boolean)
  - **sysparm_suppress_pagination_header** (boolean)
  - **sysparm_view** (string)
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

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (array)
    - **parent** (string)
    - **made_sla** (string)
    - **watch_list** (string)
    - **upon_reject** (string)
    - **sys_updated_on** (string)
    - **approval_history** (string)
    - **number** (string)
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
    - **sys_created_by** (string)
    - **knowledge** (string)
    - **order** (string)
    - **closed_at** (string)
    - **cmdb_ci** (object)
      - **link** (string)
      - **value** (string)
    - **delivery_plan** (string)
    - **impact** (string)
    - **active** (string)
    - **work_notes_list** (string)
    - **business_service** (string)
    - **priority** (string)
    - **sys_domain_path** (string)
    - **time_worked** (string)
    - **expected_start** (string)
    - **rejection_goto** (string)
    - **opened_at** (string)
    - **business_duration** (string)
    - **group_list** (string)
    - **work_end** (string)
    - **approval_set** (string)
    - **wf_activity** (string)
    - **work_notes** (string)
    - **short_description** (string)
    - **correlation_display** (string)
    - **delivery_task** (string)
    - **work_start** (string)
    - **assignment_group** (string)
    - **additional_assignee_list** (string)
    - **description** (string)
    - **calendar_duration** (string)
    - **close_notes** (string)
    - **sys_class_name** (string)
    - **closed_by** (string)
    - **follow_up** (string)
    - **sys_id** (string)
    - **contact_type** (string)
    - **urgency** (string)
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
    - **escalation** (string)
    - **upon_approval** (string)
    - **correlation_id** (string)
    - **location** (string)