# Create Security Incident

**Description**: Creates a new security incident in ServiceNow based on the provided path parameters.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `POST`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| json_body | object |  | No |
## Output

### Example

```json
- json_body:
    result:
      active: 'true'
      activity_due: ''
      additional_assignee_list: ''
      approval: not requested
      approval_history: ''
      approval_set: ''
      assigned_to: ''
      assignment_group: ''
      business_duration: ''
      business_impact: ''
      business_service: ''
      business_stc: ''
      calendar_duration: ''
      calendar_stc: ''
      caller_id: ''
      category: inquiry
      cause: ''
      caused_by: ''
      child_incidents: '0'
      close_code: ''
      close_notes: ''
      closed_at: ''
      closed_by: ''
      cmdb_ci: ''
      comments: ''
      comments_and_work_notes: ''
      company: ''
      contact_type: ''
      contract: ''
      correlation_display: ''
      correlation_id: ''
      delivery_plan: ''
      delivery_task: ''
      description: ''
      due_date: ''
      escalation: '0'
      expected_start: ''
      follow_up: ''
      group_list: ''
      hold_reason: ''
      impact: '3'
      incident_state: '1'
      knowledge: 'false'
      location: ''
      made_sla: 'true'
      notify: '1'
      number: INC0010006
      opened_at: '2023-08-07 10:59:39'
      opened_by:
        link: https://dev60827.service-now.com/api/now/v2/table/sys_user/6816f79cc0a8016401c5a33be04be441
        value: 6816f79cc0a8016401c5a33be04be441
      order: ''
      origin_id: ''
      origin_table: ''
      parent: ''
      parent_incident: ''
      priority: '5'
      problem_id: ''
      reassignment_count: '0'
      reopen_count: '0'
      reopened_by: ''
      reopened_time: ''
      resolved_at: ''
      resolved_by: ''
      rfc: ''
      route_reason: ''
      service_offering: ''
      severity: '3'
      short_description: ''
      sla_due: ''
      state: '1'
      subcategory: ''
      sys_class_name: incident
      sys_created_by: admin
      sys_created_on: '2023-08-07 10:59:39'
      sys_domain:
        link: https://dev60827.service-now.com/api/now/v2/table/sys_user_group/global
        value: global
      sys_domain_path: /
      sys_id: 26d1744d47603110d737cd9bd36d436b
      sys_mod_count: '0'
      sys_tags: ''
      sys_updated_by: admin
      sys_updated_on: '2023-08-07 10:59:39'
      task_effective_number: INC0010006
      time_worked: ''
      universal_request: ''
      upon_approval: proceed
      upon_reject: cancel
      urgency: '3'
      user_input: ''
      watch_list: ''
      work_end: ''
      work_notes: ''
      work_notes_list: ''
      work_start: ''
  reason: Created
  response_headers:
    Cache-Control: no-cache,no-store,must-revalidate,max-age=-1
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json;charset=UTF-8
    Date: Mon, 07 Aug 2023 10:59:39 GMT
    Expires: '0'
    Keep-Alive: timeout=70
    Location: https://dev60827.service-now.com/api/now/v2/table/incident/26d1744d47603110d737cd9bd36d436b
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: JSESSIONID=65CFEB1152B06972DD21833AFE556414; Path=/; HttpOnly;Secure,
      glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure;
      HttpOnly, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10
      GMT; Path=/; Secure; HttpOnly, glide_user_route=glide.0523df0e933b3d0b61bd3203715792eb;
      Max-Age=2147483647; Expires=Sat, 25-Aug-2091 14:13:46 GMT; Path=/; Secure; HttpOnly,
      glide_session_store=2AD13C4147203110D737CD9BD36D43A3; Max-Age=1800; Expires=Mon,
      07-Aug-2023 11:29:39 GMT; Path=/; Secure; HttpOnly, BIGipServerpool_dev60827=999184138.46398.0000;
      path=/; Httponly; Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Transaction-ID: 6ed13c41a300
  status_code: 201

```
### Output Parameters

| Name | Type | Description |
|------|------|-------------|
| status_code | number |  |
| reason | string |  |
| json_body | object |  |
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string |  |
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| Location | string |  |
| X-Content-Type-Options | string |  |
| Pragma | string |  |
| Cache-Control | string |  |
| Expires | string |  |
| Content-Type | string |  |
| Transfer-Encoding | string |  |
| Date | string |  |
| Keep-Alive | string |  |
| Connection | string |  |
| Server | string |  |
| Strict-Transport-Security | string |  |
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