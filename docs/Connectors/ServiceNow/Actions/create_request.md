# Create Request

**Description**: Generates a new service request in ServiceNow, allowing for display value identification and input tracking.

## Endpoint

- **URL:** `/api/now/v2/table/sc_request`
- **Method:** `POST`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| json_body | object |  | No |
| parameters | object |  | No |
## Output

### Example

```json
- json_body:
    result:
      active: 'false'
      activity_due: ''
      additional_assignee_list: ''
      approval: approved
      approval_history: ''
      approval_set: '2022-11-01 21:20:31'
      assigned_to: ''
      assignment_group: ''
      business_duration: '1970-01-01 00:00:00'
      business_service: ''
      calendar_duration: '1970-01-01 00:02:17'
      calendar_stc: ''
      close_notes: updated firmware
      closed_at: '2016-01-19 04:52:04'
      closed_by:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/6816f79cc0a8016401c5a33be04be441
        value: 6816f79cc0a8016401c5a33be04be441
      cmdb_ci:
        link: https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/{link=https://instance.serviceno
        value: '{link=https://instance.serviceno'
      comments: ''
      comments_and_work_notes: ''
      company: ''
      contact_type: phone
      contract: ''
      correlation_display: ''
      correlation_id: ''
      delivery_address: ''
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
      number: REQ0010003
      opened_at: '2016-01-19 04:49:47'
      opened_by:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/{link=https://instance.serviceno
        value: '{link=https://instance.serviceno'
      order: ''
      parent: ''
      parent_interaction:
        link: https://dev130168.service-now.com/api/now/v2/table/interaction/no value
        value: no value
      price: '0'
      priority: '4'
      reassignment_count: '0'
      request_state: in_process
      requested_date: ''
      requested_for:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/no value
        value: no value
      route_reason: ''
      service_offering:
        link: https://dev130168.service-now.com/api/now/v2/table/service_offering/no
          value
        value: no value
      short_description: Switch occasionally drops connections
      sla_due: ''
      special_instructions: no value
      stage: requested
      state: '4'
      sys_class_name: sc_request
      sys_created_by: admin
      sys_created_on: '2022-11-01 21:20:31'
      sys_domain:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global
        value: global
      sys_domain_path: /
      sys_id: 896c865f9736111084d57e121153af5f
      sys_mod_count: '0'
      sys_tags: ''
      sys_updated_by: admin
      sys_updated_on: '2022-11-01 21:20:31'
      task_effective_number: REQ0010003
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
    Date: Tue, 01 Nov 2022 21:20:31 GMT
    Expires: '0'
    Keep-Alive: timeout=20
    Location: https://dev130168.service-now.com/api/now/v2/table/sc_request/896c865f9736111084d57e121153af5f
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/;
      HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu,
      01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e;
      Max-Age=2147483647; Expires=Mon, 20-Nov-2090 00:34:38 GMT; Path=/; HttpOnly;
      SameSite=None; Secure, glide_session_store=016C8ED79736111084D57E121153AF34;
      Max-Age=1800; Expires=Tue, 01-Nov-2022 21:50:31 GMT; Path=/; HttpOnly; SameSite=None;
      Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Transaction-ID: 096cc61b9736
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