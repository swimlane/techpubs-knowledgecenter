# Get Table

**Description**: Retrieves records from a specified ServiceNow table using the 'tableName' path parameter.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| parameters | object |  | No |
## Output

### Example

```json
- json_body:
    result:
    - active: 'false'
      activity_due: ''
      additional_assignee_list: ''
      approval: not requested
      approval_history: ''
      approval_set: ''
      assigned_to: ''
      assignment_group: ''
      business_duration: '1970-01-01 00:00:00'
      business_service: ''
      calendar_duration: '1970-01-01 00:02:17'
      close_notes: updated firmware
      closed_at: '2016-01-19 04:52:04'
      closed_by: ''
      cmdb_ci:
        link: https://instance.servicenow.com/api/now/table/cmdb_ci/55b35562c0a8010e01cff22378e0aea9
        value: 55b35562c0a8010e01cff22378e0aea9
      comments: ''
      comments_and_work_notes: ''
      company: ''
      contact_type: phone
      correlation_display: ''
      correlation_id: ''
      delivery_plan: ''
      delivery_task: ''
      description: Switch occasionally drops connections
      due_date: ''
      escalation: '0'
      expected_start: ''
      follow_up: ''
      group_list: ''
      impact: '3'
      knowledge: 'false'
      location: ''
      made_sla: 'true'
      number: PRB0000050
      opened_at: '2016-01-19 04:49:47'
      opened_by:
        link: https://instance.servicenow.com/api/now/table/sys_user/glide.maint
        value: glide.maint
      order: ''
      parent: ''
      priority: '4'
      reassignment_count: ''
      rejection_goto: ''
      short_description: Switch occasionally drops connections
      sla_due: ''
      state: '4'
      sys_class_name: problem
      sys_created_by: glide.maint
      sys_created_on: '2016-01-19 04:51:19'
      sys_domain:
        link: https://instance.servicenow.com/api/now/table/sys_user_group/global
        value: global
      sys_domain_path: /
      sys_id: 04ce72c9c0a8016600b5b7f75ac67b5b
      sys_mod_count: '1'
      sys_tags: ''
      sys_updated_by: glide.maint
      sys_updated_on: '2016-01-19 04:52:04'
      time_worked: ''
      upon_approval: proceed
      upon_reject: cancel
      urgency: '3'
      user_input: ''
      watch_list: ''
      wf_activity: ''
      work_end: ''
      work_notes: ''
      work_notes_list: ''
      work_start: ''
  reason: OK
  response_headers: {}
  status_code: 200

```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Error Handling

### Common Error Responses

| Status Code | Message | Description | Example |
|-------------|---------|-------------|---------|
| 400 | Bad Request | The request was invalid or cannot be processed. | Invalid search ID or parameters. |
| 401 | Unauthorized | Missing or incorrect authentication. | Invalid API token. |
| 403 | Forbidden | Access to the resource is denied. | No permissions for search. |
| 404 | Not Found | The requested item does not exist. | Search ID not found. |
| 500 | Internal Server Error | A server error occurred. | Unexpected failure in Splunk. |

### Error Example

```json
{
  "messages": [
    {
      "type": "ERROR",
      "text": "Search ID not found."
    }
  ],
  "status_code": 404,
  "reason": "Not Found"
}
```