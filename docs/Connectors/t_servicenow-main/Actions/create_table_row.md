# Create Table Row

**Description**: Creates a new entry in the specified ServiceNow table using provided path parameters and display values.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **tableName** (string) – Required: Table name.
- **parameters** (object) – Required
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required
  - **comments** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **result** (object)
    - **parent** (string)
    - **made_sla** (string)
    - **caused_by** (string)
    - **watch_list** (string)
    - **upon_reject** (string)
    - **sys_updated_on** (string)
    - **child_incidents** (string)
    - **hold_reason** (string)
    - **origin_table** (string)
    - **task_effective_number** (string)
    - **approval_history** (string)
    - **number** (string)
    - **resolved_by** (object)
      - **display_value** (string)
      - **link** (string)
    - **sys_updated_by** (string)
    - **opened_by** (object)
      - **display_value** (string)
      - **link** (string)
    - **user_input** (string)
    - **sys_created_on** (string)
    - **sys_domain** (object)
      - **display_value** (string)
      - **link** (string)
    - **state** (string)
    - **route_reason** (string)
    - **sys_created_by** (string)
    - **knowledge** (string)
    - **order** (string)
    - **calendar_stc** (string)
    - **closed_at** (string)
    - **cmdb_ci** (object)
      - **display_value** (string)
      - **link** (string)
    - **delivery_plan** (string)
    - **contract** (string)
    - **impact** (string)
    - **active** (string)
    - **work_notes_list** (string)
    - **business_service** (object)
      - **display_value** (string)
      - **link** (string)
    - **business_impact** (string)
    - **priority** (string)
    - **sys_domain_path** (string)
    - **rfc** (string)
    - **time_worked** (string)
    - **expected_start** (string)
    - **opened_at** (string)
    - **business_duration** (string)
    - **group_list** (string)
    - **work_end** (string)
    - **caller_id** (object)
      - **display_value** (string)
      - **link** (string)
    - **reopened_time** (string)
    - **resolved_at** (string)
    - **approval_set** (string)
    - **subcategory** (string)
    - **work_notes** (string)
    - **universal_request** (string)
    - **short_description** (string)
    - **close_code** (string)
    - **correlation_display** (string)
    - **delivery_task** (string)
    - **work_start** (string)
    - **assignment_group** (object)
      - **display_value** (string)
      - **link** (string)
    - **additional_assignee_list** (string)
    - **business_stc** (string)
    - **cause** (string)
    - **description** (string)
    - **origin_id** (string)
    - **calendar_duration** (string)
    - **close_notes** (string)
    - **notify** (string)
    - **service_offering** (string)
    - **sys_class_name** (string)
    - **closed_by** (object)
      - **display_value** (string)
      - **link** (string)
    - **follow_up** (string)
    - **parent_incident** (string)
    - **sys_id** (string)
    - **contact_type** (string)
    - **reopened_by** (string)
    - **incident_state** (string)
    - **urgency** (string)
    - **problem_id** (string)
    - **company** (object)
      - **display_value** (string)
      - **link** (string)
    - **reassignment_count** (string)
    - **activity_due** (string)
    - **assigned_to** (object)
      - **display_value** (string)
      - **link** (string)
    - **severity** (string)
    - **comments** (string)
    - **approval** (string)
    - **sla_due** (string)
    - **comments_and_work_notes** (string)
    - **due_date** (string)
    - **sys_mod_count** (string)
    - **reopen_count** (string)
    - **sys_tags** (string)
    - **escalation** (string)
    - **upon_approval** (string)
    - **correlation_id** (string)
    - **location** (string)
    - **category** (string)
## Response Headers

| Header | Type |
|--------|------|
| Server-Timing | string |
| Content-Encoding | string |
| X-Is-Logged-In | string |
| X-Transaction-ID | string |
| X-Content-Type-Options | string |
| Pragma | string |
| Cache-Control | string |
| Expires | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Date | string |
| Keep-Alive | string |
| Connection | string |
| Server | string |
| Set-Cookie | string |
| Strict-Transport-Security | string |