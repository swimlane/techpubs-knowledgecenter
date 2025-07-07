# Create Table Row

**Description**: Creates a new entry in the specified ServiceNow table using provided path parameters and display values.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **tableName** (string) – Required: Table name.
- **parameters** (object) – Required: Structured object with nested properties.
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required: Structured object with nested properties.
  - **comments** (string): Text string.
## Output

### Output Parameters

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **json_body** (object): Structured object with nested properties.
  - **result** (object): Structured object with nested properties.
    - **parent** (string): Text string.
    - **made_sla** (string): Text string.
    - **caused_by** (string): Text string.
    - **watch_list** (string): Text string.
    - **upon_reject** (string): Text string.
    - **sys_updated_on** (string): Timestamp in ISO 8601 format.
    - **child_incidents** (string): Unique identifier.
    - **hold_reason** (string): Text string.
    - **origin_table** (string): Text string.
    - **task_effective_number** (string): Text string.
    - **approval_history** (string): Text string.
    - **number** (string): Text string.
    - **resolved_by** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **sys_updated_by** (string): Timestamp in ISO 8601 format.
    - **opened_by** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **user_input** (string): Text string.
    - **sys_created_on** (string): Text string.
    - **sys_domain** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **state** (string): Text string.
    - **route_reason** (string): Text string.
    - **sys_created_by** (string): Text string.
    - **knowledge** (string): Text string.
    - **order** (string): Text string.
    - **calendar_stc** (string): Text string.
    - **closed_at** (string): Text string.
    - **cmdb_ci** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **delivery_plan** (string): Text string.
    - **contract** (string): Text string.
    - **impact** (string): Text string.
    - **active** (string): Text string.
    - **work_notes_list** (string): Text string.
    - **business_service** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **business_impact** (string): Text string.
    - **priority** (string): Text string.
    - **sys_domain_path** (string): Text string.
    - **rfc** (string): Text string.
    - **time_worked** (string): Timestamp in ISO 8601 format.
    - **expected_start** (string): Text string.
    - **opened_at** (string): Text string.
    - **business_duration** (string): Text string.
    - **group_list** (string): Text string.
    - **work_end** (string): Text string.
    - **caller_id** (object): Unique identifier.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **reopened_time** (string): Timestamp in ISO 8601 format.
    - **resolved_at** (string): Text string.
    - **approval_set** (string): Text string.
    - **subcategory** (string): Text string.
    - **work_notes** (string): Text string.
    - **universal_request** (string): Text string.
    - **short_description** (string): Text string.
    - **close_code** (string): Text string.
    - **correlation_display** (string): Text string.
    - **delivery_task** (string): Text string.
    - **work_start** (string): Text string.
    - **assignment_group** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **additional_assignee_list** (string): Text string.
    - **business_stc** (string): Text string.
    - **cause** (string): Text string.
    - **description** (string): Text string.
    - **origin_id** (string): Unique identifier.
    - **calendar_duration** (string): Text string.
    - **close_notes** (string): Text string.
    - **notify** (string): Text string.
    - **service_offering** (string): Text string.
    - **sys_class_name** (string): Name or label.
    - **closed_by** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **follow_up** (string): Text string.
    - **parent_incident** (string): Unique identifier.
    - **sys_id** (string): Unique identifier.
    - **contact_type** (string): Type of the resource or value.
    - **reopened_by** (string): Text string.
    - **incident_state** (string): Unique identifier.
    - **urgency** (string): Text string.
    - **problem_id** (string): Unique identifier.
    - **company** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **reassignment_count** (string): Number of occurrences or items.
    - **activity_due** (string): Text string.
    - **assigned_to** (object): Structured object with nested properties.
      - **display_value** (string): Text string.
      - **link** (string): Text string.
    - **severity** (string): Text string.
    - **comments** (string): Text string.
    - **approval** (string): Text string.
    - **sla_due** (string): Text string.
    - **comments_and_work_notes** (string): Text string.
    - **due_date** (string): Timestamp in ISO 8601 format.
    - **sys_mod_count** (string): Number of occurrences or items.
    - **reopen_count** (string): Number of occurrences or items.
    - **sys_tags** (string): Text string.
    - **escalation** (string): Text string.
    - **upon_approval** (string): Text string.
    - **correlation_id** (string): Unique identifier.
    - **location** (string): Text string.
    - **category** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Text string. |
| Content-Encoding | string | Text string. |
| X-Is-Logged-In | string | Text string. |
| X-Transaction-ID | string | Unique identifier. |
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