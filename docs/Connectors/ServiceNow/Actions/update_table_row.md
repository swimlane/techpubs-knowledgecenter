# Update Table Row

**Description**: Updates a specific row in a ServiceNow table using sys_id, with options for display value settings.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

| Name | Type | Description | Required |
|------|------|-------------|----------|
| path_parameters | object |  | Yes |
| parameters | object |  | No |
| json_body | object |  | Yes |
## Output

### Example

```json
- json_body:
    result:
      active: 'false'
      activity_due: '2016-12-12 17:26:36'
      additional_assignee_list: ''
      approval: Not Yet Requested
      approval_history: ''
      approval_set: ''
      assigned_to:
        display_value: David Loo
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007
      assignment_group:
        display_value: Network
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user_group/287ebd7da9fe198100f92cc8d1d2154e
      business_duration: 8 Hours
      business_impact: ''
      business_service:
        display_value: Email
        link: https://dev130168.service-now.com/api/now/v2/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16
      business_stc: 28,800
      calendar_duration: 1 Day 4 Hours 23 Minutes
      calendar_stc: 102,197
      caller_id:
        display_value: Joe Employee
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
      category: Inquiry / Help
      cause: ''
      caused_by: ''
      child_incidents: '0'
      close_code: Solved (Permanently)
      close_notes: This incident is resolved.
      closed_at: '2016-12-13 18:46:44'
      closed_by:
        display_value: Joe Employee
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
      cmdb_ci:
        display_value: Storage Area Network 001
        link: https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/109562a3c611227500a7b7ff98cc0dc7
      comments: "2022-11-04 15:29:20 - System Administrator (Additional comments)\n\
        test\n\n2022-11-04 15:28:12 - System Administrator (Additional comments)\n\
        test\n\n2022-11-04 15:21:53 - System Administrator (Additional comments)\n\
        test\n\n2022-11-04 15:21:03 - System Administrator (Additional comments)\n\
        test\n\n2016-12-13 12:30:14 - Joe Employee (Additional comments)\nHi David,\
        \ \nThat must be it. I was on phone calls at all three of those times and\
        \ must not have had any activity on my computer. Please close this incident.\n\
        \n2016-12-13 10:42:25 - David Loo (Additional comments)\nHi Joe,\nI've checked\
        \ in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and\
        \ 2:28PM. These three times coincide with entries in the exchange server logs\
        \ showing you lost connection at those same times. The VPN policy is to time\
        \ out a connection if it hasn't been active in 30 minutes. Please ensure the\
        \ next time you lose connectivity you are still\_connected to the VPN.\n\n\
        I'm going to update this incident to resolved. Please let me know if you need\
        \ any more assistance.\n\n2016-12-13 07:53:01 - Joe Employee (Additional comments)\n\
        Hi David,\nThank you! I use the corporate VPN and was also unable to connect\
        \ to the email server at 9:30AM and 10:45AM.\n\n2016-12-13 06:43:17 - David\
        \ Loo (Additional comments)\nHi Joe,\nMy name is David.\_I'll be assisting\
        \ you with this incident. Can you confirm which VPN you have been using today?\_\
        I also see you were having this issue at 2:30PM. Were there any other times\
        \ you can recall you had issues connecting to the email?\n\n2016-12-12 16:56:57\
        \ - Beth Anglin (Additional comments)\nHi Joe, \nAs per discussion on call,\
        \ Workaround has been provided and it has worked for you. I have verified\
        \ with the Exchange team we haven't had an issue with the email server today.\
        \ I'm going to assign this issue to the network team for further investigation.\n\
        \n2016-12-12 12:43:50 - Joe Employee (Additional comments)\nHi Beth,\nYes,\
        \ I'm connected to the VPN, although I've had to reconnect to it a couple\
        \ of times. The last time I was unable to connect was 2:30PM.\n\n2016-12-12\
        \ 10:52:42 - Beth Anglin (Additional comments)\nHi Joe, \nAre you connected\
        \ to the VPN when you're having this issue? Can you identify a specific time\
        \ you were unable to connect to email?\n\n2016-12-12 08:30:49 - Beth Anglin\
        \ (Additional comments)\nHi Joe, \nMy name is Beth and I'll be assisting you\
        \ with your issue.\n\n2016-12-12 07:19:57 - Joe Employee (Additional comments)\n\
        I am unable to connect to the email server. It appears to be down.\n\n"
      comments_and_work_notes: "2022-11-04 15:29:20 - System Administrator (Additional\
        \ comments)\ntest\n\n2022-11-04 15:28:12 - System Administrator (Additional\
        \ comments)\ntest\n\n2022-11-04 15:21:53 - System Administrator (Additional\
        \ comments)\ntest\n\n2022-11-04 15:21:03 - System Administrator (Additional\
        \ comments)\ntest\n\n2016-12-13 12:30:14 - Joe Employee (Additional comments)\n\
        Hi David, \nThat must be it. I was on phone calls at all three of those times\
        \ and must not have had any activity on my computer. Please close this incident.\n\
        \n2016-12-13 10:42:25 - David Loo (Additional comments)\nHi Joe,\nI've checked\
        \ in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and\
        \ 2:28PM. These three times coincide with entries in the exchange server logs\
        \ showing you lost connection at those same times. The VPN policy is to time\
        \ out a connection if it hasn't been active in 30 minutes. Please ensure the\
        \ next time you lose connectivity you are still\_connected to the VPN.\n\n\
        I'm going to update this incident to resolved. Please let me know if you need\
        \ any more assistance.\n\n2016-12-13 07:53:01 - Joe Employee (Additional comments)\n\
        Hi David,\nThank you! I use the corporate VPN and was also unable to connect\
        \ to the email server at 9:30AM and 10:45AM.\n\n2016-12-13 06:43:17 - David\
        \ Loo (Additional comments)\nHi Joe,\nMy name is David.\_I'll be assisting\
        \ you with this incident. Can you confirm which VPN you have been using today?\_\
        I also see you were having this issue at 2:30PM. Were there any other times\
        \ you can recall you had issues connecting to the email?\n\n2016-12-12 16:56:57\
        \ - Beth Anglin (Additional comments)\nHi Joe, \nAs per discussion on call,\
        \ Workaround has been provided and it has worked for you. I have verified\
        \ with the Exchange team we haven't had an issue with the email server today.\
        \ I'm going to assign this issue to the network team for further investigation.\n\
        \n2016-12-12 16:56:57 - Beth Anglin (Work notes)\nUpdating priority as workaround\
        \ for incident has been provided.\n\n2016-12-12 12:43:50 - Joe Employee (Additional\
        \ comments)\nHi Beth,\nYes, I'm connected to the VPN, although I've had to\
        \ reconnect to it a couple of times. The last time I was unable to connect\
        \ was 2:30PM.\n\n2016-12-12 10:52:42 - Beth Anglin (Additional comments)\n\
        Hi Joe, \nAre you connected to the VPN when you're having this issue? Can\
        \ you identify a specific time you were unable to connect to email?\n\n2016-12-12\
        \ 09:57:00 - Beth Anglin (Work notes)\nIncreasing priority as this incident\
        \ is affecting more number of users\n\n2016-12-12 09:01:24 - Beth Anglin (Work\
        \ notes)\nUpdating incident with correct Configuration item\n\n2016-12-12\
        \ 08:30:49 - Beth Anglin (Additional comments)\nHi Joe, \nMy name is Beth\
        \ and I'll be assisting you with your issue.\n\n2016-12-12 07:19:57 - Joe\
        \ Employee (Additional comments)\nI am unable to connect to the email server.\
        \ It appears to be down.\n\n"
      company:
        display_value: ACME North America
        link: https://dev130168.service-now.com/api/now/v2/table/core_company/31bea3d53790200044e0bfc8bcbe5dec
      contact_type: Self-service
      contract: ''
      correlation_display: ''
      correlation_id: ''
      delivery_plan: ''
      delivery_task: ''
      description: I am unable to connect to the email server. It appears to be down.
      due_date: ''
      escalation: Normal
      expected_start: ''
      follow_up: ''
      group_list: ''
      hold_reason: ''
      impact: 2 - Medium
      incident_state: Closed
      knowledge: 'false'
      location: ''
      made_sla: 'true'
      notify: Do Not Notify
      number: INC0000060
      opened_at: '2016-12-12 07:19:57'
      opened_by:
        display_value: Joe Employee
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7
      order: ''
      origin_id: ''
      origin_table: ''
      parent: ''
      parent_incident: ''
      priority: 3 - Moderate
      problem_id: ''
      reassignment_count: '2'
      reopen_count: '0'
      reopened_by: ''
      reopened_time: ''
      resolved_at: '2016-12-13 13:43:14'
      resolved_by:
        display_value: David Loo
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007
      rfc: ''
      route_reason: ''
      service_offering: ''
      severity: 3 - Low
      short_description: Unable to connect to email
      sla_due: UNKNOWN
      state: Closed
      subcategory: Email
      sys_class_name: Incident
      sys_created_by: employee
      sys_created_on: '2016-12-12 07:19:57'
      sys_domain:
        display_value: global
        link: https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global
      sys_domain_path: /
      sys_id: 1c741bd70b2322007518478d83673af3
      sys_mod_count: '19'
      sys_tags: ''
      sys_updated_by: admin
      sys_updated_on: '2022-11-04 15:29:20'
      task_effective_number: INC0000060
      time_worked: ''
      universal_request: ''
      upon_approval: Proceed to Next Task
      upon_reject: Cancel all future Tasks
      urgency: 2 - Medium
      user_input: ''
      watch_list: ''
      work_end: ''
      work_notes: '2016-12-12 16:56:57 - Beth Anglin (Work notes)

        Updating priority as workaround for incident has been provided.


        2016-12-12 09:57:00 - Beth Anglin (Work notes)

        Increasing priority as this incident is affecting more number of users


        2016-12-12 09:01:24 - Beth Anglin (Work notes)

        Updating incident with correct Configuration item


        '
      work_notes_list: ''
      work_start: ''
  reason: OK
  response_headers:
    Cache-Control: no-cache,no-store,must-revalidate,max-age=-1
    Connection: keep-alive
    Content-Encoding: gzip
    Content-Type: application/json;charset=UTF-8
    Date: Fri, 04 Nov 2022 22:29:20 GMT
    Expires: '0'
    Keep-Alive: timeout=20
    Pragma: no-store,no-cache
    Server: ServiceNow
    Server-Timing: sem_wait;dur=0, sesh_wait;dur=0
    Set-Cookie: glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/;
      HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu,
      01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e;
      Max-Age=2147483647; Expires=Thu, 23-Nov-2090 01:43:27 GMT; Path=/; HttpOnly;
      SameSite=None; Secure, glide_session_store=8EE8B5509703111084D57E121153AF4B;
      Max-Age=1800; Expires=Fri, 04-Nov-2022 22:59:20 GMT; Path=/; HttpOnly; SameSite=None;
      Secure
    Strict-Transport-Security: max-age=63072000; includeSubDomains
    Transfer-Encoding: chunked
    X-Content-Type-Options: nosniff
    X-Is-Logged-In: 'true'
    X-Transaction-ID: c2e8b1909703
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