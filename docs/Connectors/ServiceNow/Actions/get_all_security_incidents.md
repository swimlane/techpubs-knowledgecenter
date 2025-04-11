# Get all Security Incidents

**Description**: Retrieves all security incident records from ServiceNow, offering display customization and pagination options.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
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
  response_headers:
    Cache-Control: no-cache,no-store,must-revalidate,max-age=-1
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json;charset=UTF-8
    Date: Mon, 23 Dec 2024 10:03:47 GMT
    Expires: '0'
    Keep-Alive: timeout=70
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: JSESSIONID=47A85A3A36C9AAE770C7A9D579538A40; Path=/; HttpOnly; SameSite=None;
      Secure, glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/;
      Secure; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu,
      01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_user_route=glide.dd365af53b877647bfe3ca23d2bda88c;
      Max-Age=2147483647; Expires=Sat, 10-Jan-2093 13:17:54 GMT; Path=/; Secure; HttpOnly;
      SameSite=None; Secure, glide_node_id_for_js=a4405af3dee08de0f8588f376b703f40b8fc9b61228796a63788e51f33976436;
      Path=/; Secure; SameSite=None; Secure, glide_session_store=C2568C93832252100D5E9D60CEAAD38D;
      Max-Age=1800; Expires=Mon, 23-Dec-2024 10:33:47 GMT; Path=/; Secure; HttpOnly;
      SameSite=None; Secure, BIGipServerpool_dev262724=2709626634.45630.0000; path=/;
      Httponly; Secure; SameSite=None; Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Total-Count: '1'
    X-Transaction-ID: 0a564c938322
  status_code: 200

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
| Server-Timing | string |  |
| Content-Encoding | string |  |
| X-Is-Logged-In | string |  |
| X-Transaction-ID | string |  |
| X-Total-Count | string |  |
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
| Set-Cookie | string |  |
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