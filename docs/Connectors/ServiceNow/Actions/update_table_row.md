# Update Table Row

**Description**: Updates a specific row in a ServiceNow table using sys_id, with options for display value settings.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **tableName** (string) – Required: Table name
  - **sys_id** (string) – Required: Sys_id of the record to be updated.
- **parameters** (object)
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required
  - **comments** (string)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
      "Content-Encoding": "gzip",
      "X-Is-Logged-In": "true",
      "X-Transaction-ID": "c2e8b1909703",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Fri, 04 Nov 2022 22:29:20 GMT",
      "Keep-Alive": "timeout=20",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Thu, 23-Nov-2090 01:43:27 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=8EE8B5509703111084D57E121153AF4B; Max-Age=1800; Expires=Fri, 04-Nov-2022 22:59:20 GMT; Path=/; HttpOnly; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "result": {
        "parent": "",
        "made_sla": "true",
        "caused_by": "",
        "watch_list": "",
        "upon_reject": "Cancel all future Tasks",
        "sys_updated_on": "2022-11-04 15:29:20",
        "child_incidents": "0",
        "hold_reason": "",
        "origin_table": "",
        "task_effective_number": "INC0000060",
        "approval_history": "",
        "number": "INC0000060",
        "resolved_by": {
          "display_value": "David Loo",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007"
        },
        "sys_updated_by": "admin",
        "opened_by": {
          "display_value": "Joe Employee",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7"
        },
        "user_input": "",
        "sys_created_on": "2016-12-12 07:19:57",
        "sys_domain": {
          "display_value": "global",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global"
        },
        "state": "Closed",
        "route_reason": "",
        "sys_created_by": "employee",
        "knowledge": "false",
        "order": "",
        "calendar_stc": "102,197",
        "closed_at": "2016-12-13 18:46:44",
        "cmdb_ci": {
          "display_value": "Storage Area Network 001",
          "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/109562a3c611227500a7b7ff98cc0dc7"
        },
        "delivery_plan": "",
        "contract": "",
        "impact": "2 - Medium",
        "active": "false",
        "work_notes_list": "",
        "business_service": {
          "display_value": "Email",
          "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16"
        },
        "business_impact": "",
        "priority": "3 - Moderate",
        "sys_domain_path": "/",
        "rfc": "",
        "time_worked": "",
        "expected_start": "",
        "opened_at": "2016-12-12 07:19:57",
        "business_duration": "8 Hours",
        "group_list": "",
        "work_end": "",
        "caller_id": {
          "display_value": "Joe Employee",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7"
        },
        "reopened_time": "",
        "resolved_at": "2016-12-13 13:43:14",
        "approval_set": "",
        "subcategory": "Email",
        "work_notes": "2016-12-12 16:56:57 - Beth Anglin (Work notes)\nUpdating priority as workaround for incident has been provided.\n\n2016-12-12 09:57:00 - Beth Anglin (Work notes)\nIncreasing priority as this incident is affecting more number of users\n\n2016-12-12 09:01:24 - Beth Anglin (Work notes)\nUpdating incident with correct Configuration item\n\n",
        "universal_request": "",
        "short_description": "Unable to connect to email",
        "close_code": "Solved (Permanently)",
        "correlation_display": "",
        "delivery_task": "",
        "work_start": "",
        "assignment_group": {
          "display_value": "Network",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/287ebd7da9fe198100f92cc8d1d2154e"
        },
        "additional_assignee_list": "",
        "business_stc": "28,800",
        "cause": "",
        "description": "I am unable to connect to the email server. It appears to be down.",
        "origin_id": "",
        "calendar_duration": "1 Day 4 Hours 23 Minutes",
        "close_notes": "This incident is resolved.",
        "notify": "Do Not Notify",
        "service_offering": "",
        "sys_class_name": "Incident",
        "closed_by": {
          "display_value": "Joe Employee",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7"
        },
        "follow_up": "",
        "parent_incident": "",
        "sys_id": "1c741bd70b2322007518478d83673af3",
        "contact_type": "Self-service",
        "reopened_by": "",
        "incident_state": "Closed",
        "urgency": "2 - Medium",
        "problem_id": "",
        "company": {
          "display_value": "ACME North America",
          "link": "https://dev130168.service-now.com/api/now/v2/table/core_company/31bea3d53790200044e0bfc8bcbe5dec"
        },
        "reassignment_count": "2",
        "activity_due": "2016-12-12 17:26:36",
        "assigned_to": {
          "display_value": "David Loo",
          "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007"
        },
        "severity": "3 - Low",
        "comments": "2022-11-04 15:29:20 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:28:12 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:21:53 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:21:03 - System Administrator (Additional comments)\ntest\n\n2016-12-13 12:30:14 - Joe Employee (Additional comments)\nHi David, \nThat must be it. I was on phone calls at all three of those times and must not have had any activity on my computer. Please close this incident.\n\n2016-12-13 10:42:25 - David Loo (Additional comments)\nHi Joe,\nI've checked in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and 2:28PM. These three times coincide with entries in the exchange server logs showing you lost connection at those same times. The VPN policy is to time out a connection if it hasn't been active in 30 minutes. Please ensure the next time you lose connectivity you are still\u00a0connected to the VPN.\n\nI'm going to update this incident to resolved. Please let me know if you need any more assistance.\n\n2016-12-13 07:53:01 - Joe Employee (Additional comments)\nHi David,\nThank you! I use the corporate VPN and was also unable to connect to the email server at 9:30AM and 10:45AM.\n\n2016-12-13 06:43:17 - David Loo (Additional comments)\nHi Joe,\nMy name is David.\u00a0I'll be assisting you with this incident. Can you confirm which VPN you have been using today?\u00a0I also see you were having this issue at 2:30PM. Were there any other times you can recall you had issues connecting to the email?\n\n2016-12-12 16:56:57 - Beth Anglin (Additional comments)\nHi Joe, \nAs per discussion on call, Workaround has been provided and it has worked for you. I have verified with the Exchange team we haven't had an issue with the email server today. I'm going to assign this issue to the network team for further investigation.\n\n2016-12-12 12:43:50 - Joe Employee (Additional comments)\nHi Beth,\nYes, I'm connected to the VPN, although I've had to reconnect to it a couple of times. The last time I was unable to connect was 2:30PM.\n\n2016-12-12 10:52:42 - Beth Anglin (Additional comments)\nHi Joe, \nAre you connected to the VPN when you're having this issue? Can you identify a specific time you were unable to connect to email?\n\n2016-12-12 08:30:49 - Beth Anglin (Additional comments)\nHi Joe, \nMy name is Beth and I'll be assisting you with your issue.\n\n2016-12-12 07:19:57 - Joe Employee (Additional comments)\nI am unable to connect to the email server. It appears to be down.\n\n",
        "approval": "Not Yet Requested",
        "sla_due": "UNKNOWN",
        "comments_and_work_notes": "2022-11-04 15:29:20 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:28:12 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:21:53 - System Administrator (Additional comments)\ntest\n\n2022-11-04 15:21:03 - System Administrator (Additional comments)\ntest\n\n2016-12-13 12:30:14 - Joe Employee (Additional comments)\nHi David, \nThat must be it. I was on phone calls at all three of those times and must not have had any activity on my computer. Please close this incident.\n\n2016-12-13 10:42:25 - David Loo (Additional comments)\nHi Joe,\nI've checked in network logs and you were timed out from the VPN at 9:25AM, 10:42AM and 2:28PM. These three times coincide with entries in the exchange server logs showing you lost connection at those same times. The VPN policy is to time out a connection if it hasn't been active in 30 minutes. Please ensure the next time you lose connectivity you are still\u00a0connected to the VPN.\n\nI'm going to update this incident to resolved. Please let me know if you need any more assistance.\n\n2016-12-13 07:53:01 - Joe Employee (Additional comments)\nHi David,\nThank you! I use the corporate VPN and was also unable to connect to the email server at 9:30AM and 10:45AM.\n\n2016-12-13 06:43:17 - David Loo (Additional comments)\nHi Joe,\nMy name is David.\u00a0I'll be assisting you with this incident. Can you confirm which VPN you have been using today?\u00a0I also see you were having this issue at 2:30PM. Were there any other times you can recall you had issues connecting to the email?\n\n2016-12-12 16:56:57 - Beth Anglin (Additional comments)\nHi Joe, \nAs per discussion on call, Workaround has been provided and it has worked for you. I have verified with the Exchange team we haven't had an issue with the email server today. I'm going to assign this issue to the network team for further investigation.\n\n2016-12-12 16:56:57 - Beth Anglin (Work notes)\nUpdating priority as workaround for incident has been provided.\n\n2016-12-12 12:43:50 - Joe Employee (Additional comments)\nHi Beth,\nYes, I'm connected to the VPN, although I've had to reconnect to it a couple of times. The last time I was unable to connect was 2:30PM.\n\n2016-12-12 10:52:42 - Beth Anglin (Additional comments)\nHi Joe, \nAre you connected to the VPN when you're having this issue? Can you identify a specific time you were unable to connect to email?\n\n2016-12-12 09:57:00 - Beth Anglin (Work notes)\nIncreasing priority as this incident is affecting more number of users\n\n2016-12-12 09:01:24 - Beth Anglin (Work notes)\nUpdating incident with correct Configuration item\n\n2016-12-12 08:30:49 - Beth Anglin (Additional comments)\nHi Joe, \nMy name is Beth and I'll be assisting you with your issue.\n\n2016-12-12 07:19:57 - Joe Employee (Additional comments)\nI am unable to connect to the email server. It appears to be down.\n\n",
        "due_date": "",
        "sys_mod_count": "19",
        "reopen_count": "0",
        "sys_tags": "",
        "escalation": "Normal",
        "upon_approval": "Proceed to Next Task",
        "correlation_id": "",
        "location": "",
        "category": "Inquiry / Help"
      }
    }
  }
]
```
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

| Header | Type | Description |
|--------|------|-------------|
| Server-Timing | string | - |
| Content-Encoding | string | - |
| X-Is-Logged-In | string | - |
| X-Transaction-ID | string | - |
| X-Content-Type-Options | string | - |
| Pragma | string | - |
| Cache-Control | string | - |
| Expires | string | - |
| Content-Type | string | - |
| Transfer-Encoding | string | - |
| Date | string | - |
| Keep-Alive | string | - |
| Connection | string | - |
| Server | string | - |
| Set-Cookie | string | - |
| Strict-Transport-Security | string | - |