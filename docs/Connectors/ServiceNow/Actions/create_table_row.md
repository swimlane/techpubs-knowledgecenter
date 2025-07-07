# Create Table Row

**Description**: Creates a new entry in the specified ServiceNow table using provided path parameters and display values.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: TODO: Add description
  - **tableName** (string) – Required: Table name.
- **parameters** (object) – Required: TODO: Add description
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required: TODO: Add description
  - **comments** (string): TODO: Add description
## Output

### Output Parameters

- **status_code** (number): TODO: Add description
- **reason** (string): TODO: Add description
- **json_body** (object): TODO: Add description
  - **result** (object): TODO: Add description
    - **parent** (string): TODO: Add description
    - **made_sla** (string): TODO: Add description
    - **caused_by** (string): TODO: Add description
    - **watch_list** (string): TODO: Add description
    - **upon_reject** (string): TODO: Add description
    - **sys_updated_on** (string): TODO: Add description
    - **child_incidents** (string): TODO: Add description
    - **hold_reason** (string): TODO: Add description
    - **origin_table** (string): TODO: Add description
    - **task_effective_number** (string): TODO: Add description
    - **approval_history** (string): TODO: Add description
    - **number** (string): TODO: Add description
    - **resolved_by** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **sys_updated_by** (string): TODO: Add description
    - **opened_by** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **user_input** (string): TODO: Add description
    - **sys_created_on** (string): TODO: Add description
    - **sys_domain** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **state** (string): TODO: Add description
    - **route_reason** (string): TODO: Add description
    - **sys_created_by** (string): TODO: Add description
    - **knowledge** (string): TODO: Add description
    - **order** (string): TODO: Add description
    - **calendar_stc** (string): TODO: Add description
    - **closed_at** (string): TODO: Add description
    - **cmdb_ci** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **delivery_plan** (string): TODO: Add description
    - **contract** (string): TODO: Add description
    - **impact** (string): TODO: Add description
    - **active** (string): TODO: Add description
    - **work_notes_list** (string): TODO: Add description
    - **business_service** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **business_impact** (string): TODO: Add description
    - **priority** (string): TODO: Add description
    - **sys_domain_path** (string): TODO: Add description
    - **rfc** (string): TODO: Add description
    - **time_worked** (string): TODO: Add description
    - **expected_start** (string): TODO: Add description
    - **opened_at** (string): TODO: Add description
    - **business_duration** (string): TODO: Add description
    - **group_list** (string): TODO: Add description
    - **work_end** (string): TODO: Add description
    - **caller_id** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **reopened_time** (string): TODO: Add description
    - **resolved_at** (string): TODO: Add description
    - **approval_set** (string): TODO: Add description
    - **subcategory** (string): TODO: Add description
    - **work_notes** (string): TODO: Add description
    - **universal_request** (string): TODO: Add description
    - **short_description** (string): TODO: Add description
    - **close_code** (string): TODO: Add description
    - **correlation_display** (string): TODO: Add description
    - **delivery_task** (string): TODO: Add description
    - **work_start** (string): TODO: Add description
    - **assignment_group** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **additional_assignee_list** (string): TODO: Add description
    - **business_stc** (string): TODO: Add description
    - **cause** (string): TODO: Add description
    - **description** (string): TODO: Add description
    - **origin_id** (string): TODO: Add description
    - **calendar_duration** (string): TODO: Add description
    - **close_notes** (string): TODO: Add description
    - **notify** (string): TODO: Add description
    - **service_offering** (string): TODO: Add description
    - **sys_class_name** (string): TODO: Add description
    - **closed_by** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **follow_up** (string): TODO: Add description
    - **parent_incident** (string): TODO: Add description
    - **sys_id** (string): TODO: Add description
    - **contact_type** (string): TODO: Add description
    - **reopened_by** (string): TODO: Add description
    - **incident_state** (string): TODO: Add description
    - **urgency** (string): TODO: Add description
    - **problem_id** (string): TODO: Add description
    - **company** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **reassignment_count** (string): TODO: Add description
    - **activity_due** (string): TODO: Add description
    - **assigned_to** (object): TODO: Add description
      - **display_value** (string): TODO: Add description
      - **link** (string): TODO: Add description
    - **severity** (string): TODO: Add description
    - **comments** (string): TODO: Add description
    - **approval** (string): TODO: Add description
    - **sla_due** (string): TODO: Add description
    - **comments_and_work_notes** (string): TODO: Add description
    - **due_date** (string): TODO: Add description
    - **sys_mod_count** (string): TODO: Add description
    - **reopen_count** (string): TODO: Add description
    - **sys_tags** (string): TODO: Add description
    - **escalation** (string): TODO: Add description
    - **upon_approval** (string): TODO: Add description
    - **correlation_id** (string): TODO: Add description
    - **location** (string): TODO: Add description
    - **category** (string): TODO: Add description
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | TODO: Add description |
| Content-Encoding | string | TODO: Add description |
| X-Is-Logged-In | string | TODO: Add description |
| X-Transaction-ID | string | TODO: Add description |
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