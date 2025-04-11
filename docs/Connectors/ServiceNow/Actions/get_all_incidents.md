# Get all Incidents

**Description**: Retrieves all incident records from ServiceNow, with customization options for display values and result count limitation.

## Endpoint

- **URL:** `/api/now/v2/table/incident`
- **Method:** `GET`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| parameters | object |  | No |
## Output

### Example

```json
- json_body:
    result:
    - active: 'false'
      activity_due: '2016-12-13 01:26:36'
      additional_assignee_list: ''
      approval: not requested
      approval_history: ''
      approval_set: ''
      assigned_to:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007
        value: 5137153cc611227c000bbd1bd8cd2007
      assignment_group:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user_group/287ebd7da9fe198100f92cc8d1d2154e
        value: 287ebd7da9fe198100f92cc8d1d2154e
      business_duration: '1970-01-01 08:00:00'
      business_impact: ''
      business_service:
        link: https://dev130168.service-now.com/api/now/v2/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16
        value: 27d32778c0a8000b00db970eeaa60f16
      business_stc: '28800'
      calendar_duration: '1970-01-02 04:23:17'
      calendar_stc: '102197'
      caller_id:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
        value: 681ccaf9c0a8016400b98a06818d57c7
      category: inquiry
      cause: ''
      caused_by: ''
      child_incidents: '0'
      close_code: Solved (Permanently)
      close_notes: This incident is resolved.
      closed_at: '2016-12-14 02:46:44'
      closed_by:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
        value: 681ccaf9c0a8016400b98a06818d57c7
      cmdb_ci:
        link: https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/109562a3c611227500a7b7ff98cc0dc7
        value: 109562a3c611227500a7b7ff98cc0dc7
      comments: ''
      comments_and_work_notes: ''
      company:
        link: https://dev130168.service-now.com/api/now/v2/table/core_company/31bea3d53790200044e0bfc8bcbe5dec
        value: 31bea3d53790200044e0bfc8bcbe5dec
      contact_type: self-service
      contract: ''
      correlation_display: ''
      correlation_id: ''
      delivery_plan: ''
      delivery_task: ''
      description: I am unable to connect to the email server. It appears to be down.
      due_date: ''
      escalation: '0'
      expected_start: ''
      follow_up: ''
      group_list: ''
      hold_reason: ''
      impact: '2'
      incident_state: '7'
      knowledge: 'false'
      location: ''
      made_sla: 'true'
      notify: '1'
      number: INC0000060
      opened_at: '2016-12-12 15:19:57'
      opened_by:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
        value: 681ccaf9c0a8016400b98a06818d57c7
      order: ''
      origin_id: ''
      origin_table: ''
      parent: ''
      parent_incident: ''
      priority: '3'
      problem_id: ''
      reassignment_count: '2'
      reopen_count: '0'
      reopened_by: ''
      reopened_time: ''
      resolved_at: '2016-12-13 21:43:14'
      resolved_by:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007
        value: 5137153cc611227c000bbd1bd8cd2007
      rfc: ''
      route_reason: ''
      service_offering: ''
      severity: '3'
      short_description: Unable to connect to email
      sla_due: ''
      state: '7'
      subcategory: email
      sys_class_name: incident
      sys_created_by: employee
      sys_created_on: '2016-12-12 15:19:57'
      sys_domain:
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global
        value: global
      sys_domain_path: /
      sys_id: 1c741bd70b2322007518478d83673af3
      sys_mod_count: '15'
      sys_tags: ''
      sys_updated_by: employee
      sys_updated_on: '2016-12-14 02:46:44'
      task_effective_number: INC0000060
      time_worked: ''
      universal_request: ''
      upon_approval: proceed
      upon_reject: cancel
      urgency: '2'
      user_input: ''
      watch_list: ''
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
    Date: Thu, 03 Nov 2022 20:32:32 GMT
    Expires: '0'
    Keep-Alive: timeout=20
    Link: <https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=0>;rel="first",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=-1>;rel="prev",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=1>;rel="next",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=66>;rel="last"
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/;
      HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu,
      01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e;
      Max-Age=2147483647; Expires=Tue, 21-Nov-2090 23:46:39 GMT; Path=/; HttpOnly;
      SameSite=None; Secure, glide_session_store=6D941C849707111084D57E121153AFF6;
      Max-Age=1800; Expires=Thu, 03-Nov-2022 21:02:32 GMT; Path=/; HttpOnly; SameSite=None;
      Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Total-Count: '67'
    X-Transaction-ID: 7d9414489707
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
| Link | string |  |
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