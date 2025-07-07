# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **tableName** (string) – Required: Name of the table from which to retrieve the records.
- **parameters** (object): Structured object with nested properties.
  - **name_value_pairs** (object): Name or label.
    - **active** (string): Text string.
    - **assigned_to** (string): Text string.
    - **state** (string): Text string.
  - **sysparm_display_value** (string): Text string.
  - **sysparm_exclude_reference_link** (boolean): True or False value.
  - **sysparm_fields** (string): Text string.
  - **sysparm_limit** (number): Numerical value.
  - **sysparm_no_count** (boolean): Number of occurrences or items.
  - **sysparm_offset** (number): Numerical value.
  - **sysparm_query** (string): Text string.
  - **sysparm_query_category** (string): Text string.
  - **sysparm_query_no_domain** (boolean): True or False value.
  - **sysparm_suppress_pagination_header** (boolean): True or False value.
  - **sysparm_view** (string): Text string.
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

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **result** (array): List of items.
    - **parent** (string): Text string.
    - **made_sla** (string): Text string.
    - **watch_list** (string): Text string.
    - **upon_reject** (string): Text string.
    - **sys_updated_on** (string): Timestamp in ISO 8601 format.
    - **approval_history** (string): Text string.
    - **number** (string): Text string.
    - **sys_updated_by** (string): Timestamp in ISO 8601 format.
    - **opened_by** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **user_input** (string): Text string.
    - **sys_created_on** (string): Text string.
    - **sys_domain** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **state** (string): Text string.
    - **sys_created_by** (string): Text string.
    - **knowledge** (string): Text string.
    - **order** (string): Text string.
    - **closed_at** (string): Text string.
    - **cmdb_ci** (object): Structured object with nested properties.
      - **link** (string): Text string.
      - **value** (string): Text string.
    - **delivery_plan** (string): Text string.
    - **impact** (string): Text string.
    - **active** (string): Text string.
    - **work_notes_list** (string): Text string.
    - **business_service** (string): Text string.
    - **priority** (string): Text string.
    - **sys_domain_path** (string): Text string.
    - **time_worked** (string): Timestamp in ISO 8601 format.
    - **expected_start** (string): Text string.
    - **rejection_goto** (string): Text string.
    - **opened_at** (string): Text string.
    - **business_duration** (string): Text string.
    - **group_list** (string): Text string.
    - **work_end** (string): Text string.
    - **approval_set** (string): Text string.
    - **wf_activity** (string): Text string.
    - **work_notes** (string): Text string.
    - **short_description** (string): Text string.
    - **correlation_display** (string): Text string.
    - **delivery_task** (string): Text string.
    - **work_start** (string): Text string.
    - **assignment_group** (string): Text string.
    - **additional_assignee_list** (string): Text string.
    - **description** (string): Text string.
    - **calendar_duration** (string): Text string.
    - **close_notes** (string): Text string.
    - **sys_class_name** (string): Name or label.
    - **closed_by** (string): Text string.
    - **follow_up** (string): Text string.
    - **sys_id** (string): Unique identifier.
    - **contact_type** (string): Type of the resource or value.
    - **urgency** (string): Text string.
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
    - **escalation** (string): Text string.
    - **upon_approval** (string): Text string.
    - **correlation_id** (string): Unique identifier.
    - **location** (string): Text string.