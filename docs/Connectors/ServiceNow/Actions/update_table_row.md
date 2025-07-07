# Update Table Row

**Description**: Updates a specific row in a ServiceNow table using sys_id, with options for display value settings.

## Endpoint

- **URL:** `api/now/v2/table/{{tableName}}/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **tableName** (string) – Required: Table name
  - **sys_id** (string) – Required: Sys_id of the record to be updated.
- **parameters** (object): Structured object with nested properties.
  - **sysparm_display_value** (boolean) – Required: Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_input_display_value** (boolean) – Required: Flag that indicates whether to set field values using the display value or the actual value.
- **json_body** (object) – Required: Structured object with nested properties.
  - **comments** (string): Text string.
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