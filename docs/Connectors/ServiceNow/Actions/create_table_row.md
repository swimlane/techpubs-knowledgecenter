# Create Table Row

**Description**: Creates a new entry in the specified ServiceNow table using provided path parameters and display values.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **tableName** (string) – Required: Table name.
- **parameters** (object) – Required: Auto-generated description for `parameters`. Please update manually if needed.
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required: Auto-generated description for `json_body`. Please update manually if needed.
  - **comments** (string): Auto-generated description for `comments`. Please update manually if needed.
## Output

### Output Parameters

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **result** (object): Auto-generated description for `result`. Please update manually if needed.
    - **parent** (string): Auto-generated description for `parent`. Please update manually if needed.
    - **made_sla** (string): Auto-generated description for `made_sla`. Please update manually if needed.
    - **caused_by** (string): Auto-generated description for `caused_by`. Please update manually if needed.
    - **watch_list** (string): Auto-generated description for `watch_list`. Please update manually if needed.
    - **upon_reject** (string): Auto-generated description for `upon_reject`. Please update manually if needed.
    - **sys_updated_on** (string): Auto-generated description for `sys_updated_on`. Please update manually if needed.
    - **child_incidents** (string): Auto-generated description for `child_incidents`. Please update manually if needed.
    - **hold_reason** (string): Auto-generated description for `hold_reason`. Please update manually if needed.
    - **origin_table** (string): Auto-generated description for `origin_table`. Please update manually if needed.
    - **task_effective_number** (string): Auto-generated description for `task_effective_number`. Please update manually if needed.
    - **approval_history** (string): Auto-generated description for `approval_history`. Please update manually if needed.
    - **number** (string): Auto-generated description for `number`. Please update manually if needed.
    - **resolved_by** (object): Auto-generated description for `resolved_by`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **sys_updated_by** (string): Auto-generated description for `sys_updated_by`. Please update manually if needed.
    - **opened_by** (object): Auto-generated description for `opened_by`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **user_input** (string): Auto-generated description for `user_input`. Please update manually if needed.
    - **sys_created_on** (string): Auto-generated description for `sys_created_on`. Please update manually if needed.
    - **sys_domain** (object): Auto-generated description for `sys_domain`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **state** (string): Auto-generated description for `state`. Please update manually if needed.
    - **route_reason** (string): Auto-generated description for `route_reason`. Please update manually if needed.
    - **sys_created_by** (string): Auto-generated description for `sys_created_by`. Please update manually if needed.
    - **knowledge** (string): Auto-generated description for `knowledge`. Please update manually if needed.
    - **order** (string): Auto-generated description for `order`. Please update manually if needed.
    - **calendar_stc** (string): Auto-generated description for `calendar_stc`. Please update manually if needed.
    - **closed_at** (string): Auto-generated description for `closed_at`. Please update manually if needed.
    - **cmdb_ci** (object): Auto-generated description for `cmdb_ci`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **delivery_plan** (string): Auto-generated description for `delivery_plan`. Please update manually if needed.
    - **contract** (string): Auto-generated description for `contract`. Please update manually if needed.
    - **impact** (string): Auto-generated description for `impact`. Please update manually if needed.
    - **active** (string): Auto-generated description for `active`. Please update manually if needed.
    - **work_notes_list** (string): Auto-generated description for `work_notes_list`. Please update manually if needed.
    - **business_service** (object): Auto-generated description for `business_service`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **business_impact** (string): Auto-generated description for `business_impact`. Please update manually if needed.
    - **priority** (string): Auto-generated description for `priority`. Please update manually if needed.
    - **sys_domain_path** (string): Auto-generated description for `sys_domain_path`. Please update manually if needed.
    - **rfc** (string): Auto-generated description for `rfc`. Please update manually if needed.
    - **time_worked** (string): Auto-generated description for `time_worked`. Please update manually if needed.
    - **expected_start** (string): Auto-generated description for `expected_start`. Please update manually if needed.
    - **opened_at** (string): Auto-generated description for `opened_at`. Please update manually if needed.
    - **business_duration** (string): Auto-generated description for `business_duration`. Please update manually if needed.
    - **group_list** (string): Auto-generated description for `group_list`. Please update manually if needed.
    - **work_end** (string): Auto-generated description for `work_end`. Please update manually if needed.
    - **caller_id** (object): Auto-generated description for `caller_id`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **reopened_time** (string): Auto-generated description for `reopened_time`. Please update manually if needed.
    - **resolved_at** (string): Auto-generated description for `resolved_at`. Please update manually if needed.
    - **approval_set** (string): Auto-generated description for `approval_set`. Please update manually if needed.
    - **subcategory** (string): Auto-generated description for `subcategory`. Please update manually if needed.
    - **work_notes** (string): Auto-generated description for `work_notes`. Please update manually if needed.
    - **universal_request** (string): Auto-generated description for `universal_request`. Please update manually if needed.
    - **short_description** (string): Auto-generated description for `short_description`. Please update manually if needed.
    - **close_code** (string): Auto-generated description for `close_code`. Please update manually if needed.
    - **correlation_display** (string): Auto-generated description for `correlation_display`. Please update manually if needed.
    - **delivery_task** (string): Auto-generated description for `delivery_task`. Please update manually if needed.
    - **work_start** (string): Auto-generated description for `work_start`. Please update manually if needed.
    - **assignment_group** (object): Auto-generated description for `assignment_group`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **additional_assignee_list** (string): Auto-generated description for `additional_assignee_list`. Please update manually if needed.
    - **business_stc** (string): Auto-generated description for `business_stc`. Please update manually if needed.
    - **cause** (string): Auto-generated description for `cause`. Please update manually if needed.
    - **description** (string): Auto-generated description for `description`. Please update manually if needed.
    - **origin_id** (string): Auto-generated description for `origin_id`. Please update manually if needed.
    - **calendar_duration** (string): Auto-generated description for `calendar_duration`. Please update manually if needed.
    - **close_notes** (string): Auto-generated description for `close_notes`. Please update manually if needed.
    - **notify** (string): Auto-generated description for `notify`. Please update manually if needed.
    - **service_offering** (string): Auto-generated description for `service_offering`. Please update manually if needed.
    - **sys_class_name** (string): Auto-generated description for `sys_class_name`. Please update manually if needed.
    - **closed_by** (object): Auto-generated description for `closed_by`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **follow_up** (string): Auto-generated description for `follow_up`. Please update manually if needed.
    - **parent_incident** (string): Auto-generated description for `parent_incident`. Please update manually if needed.
    - **sys_id** (string): Auto-generated description for `sys_id`. Please update manually if needed.
    - **contact_type** (string): Auto-generated description for `contact_type`. Please update manually if needed.
    - **reopened_by** (string): Auto-generated description for `reopened_by`. Please update manually if needed.
    - **incident_state** (string): Auto-generated description for `incident_state`. Please update manually if needed.
    - **urgency** (string): Auto-generated description for `urgency`. Please update manually if needed.
    - **problem_id** (string): Auto-generated description for `problem_id`. Please update manually if needed.
    - **company** (object): Auto-generated description for `company`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **reassignment_count** (string): Auto-generated description for `reassignment_count`. Please update manually if needed.
    - **activity_due** (string): Auto-generated description for `activity_due`. Please update manually if needed.
    - **assigned_to** (object): Auto-generated description for `assigned_to`. Please update manually if needed.
      - **display_value** (string): Auto-generated description for `display_value`. Please update manually if needed.
      - **link** (string): Auto-generated description for `link`. Please update manually if needed.
    - **severity** (string): Auto-generated description for `severity`. Please update manually if needed.
    - **comments** (string): Auto-generated description for `comments`. Please update manually if needed.
    - **approval** (string): Auto-generated description for `approval`. Please update manually if needed.
    - **sla_due** (string): Auto-generated description for `sla_due`. Please update manually if needed.
    - **comments_and_work_notes** (string): Auto-generated description for `comments_and_work_notes`. Please update manually if needed.
    - **due_date** (string): Auto-generated description for `due_date`. Please update manually if needed.
    - **sys_mod_count** (string): Auto-generated description for `sys_mod_count`. Please update manually if needed.
    - **reopen_count** (string): Auto-generated description for `reopen_count`. Please update manually if needed.
    - **sys_tags** (string): Auto-generated description for `sys_tags`. Please update manually if needed.
    - **escalation** (string): Auto-generated description for `escalation`. Please update manually if needed.
    - **upon_approval** (string): Auto-generated description for `upon_approval`. Please update manually if needed.
    - **correlation_id** (string): Auto-generated description for `correlation_id`. Please update manually if needed.
    - **location** (string): Auto-generated description for `location`. Please update manually if needed.
    - **category** (string): Auto-generated description for `category`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Encoding | string | Auto-generated description for `Content-Encoding`. Please update manually if needed. |
| X-Is-Logged-In | string | Auto-generated description for `X-Is-Logged-In`. Please update manually if needed. |
| X-Transaction-ID | string | Auto-generated description for `X-Transaction-ID`. Please update manually if needed. |
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