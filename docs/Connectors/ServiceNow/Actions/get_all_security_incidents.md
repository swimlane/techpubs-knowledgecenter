# Get all Security Incidents

**Description**: Retrieves all security incident records from ServiceNow, offering display customization and pagination options.

## Endpoint

- **URL:** `/api/now/table/{{security_incident}}`
- **Method:** `GET`
## Inputs

| Name | Type | Required |
|------|------|----------|
| path_parameters | object | Yes |
| parameters | object | No |
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
      "X-Transaction-ID": "0a564c938322",
      "X-Total-Count": "1",
      "X-Content-Type-Options": "nosniff",
      "Pragma": "no-store,no-cache",
      "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
      "Expires": "0",
      "Content-Type": "application/json;charset=UTF-8",
      "Transfer-Encoding": "chunked",
      "Date": "Mon, 23 Dec 2024 10:03:47 GMT",
      "Keep-Alive": "timeout=70",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Set-Cookie": "JSESSIONID=47A85A3A36C9AAE770C7A9D579538A40; Path=/; HttpOnly; SameSite=None; Secure, glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_user_route=glide.dd365af53b877647bfe3ca23d2bda88c; Max-Age=2147483647; Expires=Sat, 10-Jan-2093 13:17:54 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, glide_node_id_for_js=a4405af3dee08de0f8588f376b703f40b8fc9b61228796a63788e51f33976436; Path=/; Secure; SameSite=None; Secure, glide_session_store=C2568C93832252100D5E9D60CEAAD38D; Max-Age=1800; Expires=Mon, 23-Dec-2024 10:33:47 GMT; Path=/; Secure; HttpOnly; SameSite=None; Secure, BIGipServerpool_dev262724=2709626634.45630.0000; path=/; Httponly; Secure; SameSite=None; Secure",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "result": [
        {
          "parent": "",
          "made_sla": "true",
          "watch_list": "",
          "upon_reject": "cancel",
          "sys_updated_on": "2016-01-19 04:52:04",
          "approval_history": "",
          "number": "PRB0000050",
          "sys_updated_by": "glide.maint",
          "opened_by": {
            "link": "https://instance.servicenow.com/api/now/table/sys_user/glide.maint",
            "value": "glide.maint"
          },
          "user_input": "",
          "sys_created_on": "2016-01-19 04:51:19",
          "sys_domain": {
            "link": "https://instance.servicenow.com/api/now/table/sys_user_group/global",
            "value": "global"
          },
          "state": "4",
          "sys_created_by": "glide.maint",
          "knowledge": "false",
          "order": "",
          "closed_at": "2016-01-19 04:52:04",
          "cmdb_ci": {
            "link": "https://instance.servicenow.com/api/now/table/cmdb_ci/55b35562c0a8010e01cff22378e0aea9",
            "value": "55b35562c0a8010e01cff22378e0aea9"
          },
          "delivery_plan": "",
          "impact": "3",
          "active": "false",
          "work_notes_list": "",
          "business_service": "",
          "priority": "4",
          "sys_domain_path": "/",
          "time_worked": "",
          "expected_start": "",
          "rejection_goto": "",
          "opened_at": "2016-01-19 04:49:47",
          "business_duration": "1970-01-01 00:00:00",
          "group_list": "",
          "work_end": "",
          "approval_set": "",
          "wf_activity": "",
          "work_notes": "",
          "short_description": "Switch occasionally drops connections",
          "correlation_display": "",
          "delivery_task": "",
          "work_start": "",
          "assignment_group": "",
          "additional_assignee_list": "",
          "description": "Switch occasionally drops connections",
          "calendar_duration": "1970-01-01 00:02:17",
          "close_notes": "updated firmware",
          "sys_class_name": "problem",
          "closed_by": "",
          "follow_up": "",
          "sys_id": "04ce72c9c0a8016600b5b7f75ac67b5b",
          "contact_type": "phone",
          "urgency": "3",
          "company": "",
          "reassignment_count": "",
          "activity_due": "",
          "assigned_to": "",
          "comments": "",
          "approval": "not requested",
          "sla_due": "",
          "comments_and_work_notes": "",
          "due_date": "",
          "sys_mod_count": "1",
          "sys_tags": "",
          "escalation": "0",
          "upon_approval": "proceed",
          "correlation_id": "",
          "location": ""
        }
      ]
    }
  }
]
```
### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| json_body | object |
## Response Headers

| Header | Type |
|--------|------|
| Server-Timing | string |
| Content-Encoding | string |
| X-Is-Logged-In | string |
| X-Transaction-ID | string |
| X-Total-Count | string |
| X-Content-Type-Options | string |
| Pragma | string |
| Cache-Control | string |
| Expires | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Date | string |
| Keep-Alive | string |
| Connection | string |
| Server | string |
| Set-Cookie | string |
| Strict-Transport-Security | string |