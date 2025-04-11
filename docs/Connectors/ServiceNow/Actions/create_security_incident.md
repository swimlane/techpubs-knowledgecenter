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
[
    {
        "status_code": 201,
        "response_headers": {
            "Set-Cookie": "JSESSIONID=65CFEB1152B06972DD21833AFE556414; Path=/; HttpOnly;Secure, glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; Secure; HttpOnly, glide_user_route=glide.0523df0e933b3d0b61bd3203715792eb; Max-Age=2147483647; Expires=Sat, 25-Aug-2091 14:13:46 GMT; Path=/; Secure; HttpOnly, glide_session_store=2AD13C4147203110D737CD9BD36D43A3; Max-Age=1800; Expires=Mon, 07-Aug-2023 11:29:39 GMT; Path=/; Secure; HttpOnly, BIGipServerpool_dev60827=999184138.46398.0000; path=/; Httponly; Secure",
            "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
            "Content-Encoding": "gzip",
            "X-Is-Logged-In": "true",
            "X-Transaction-ID": "6ed13c41a300",
            "Location": "https://dev60827.service-now.com/api/now/v2/table/incident/26d1744d47603110d737cd9bd36d436b",
            "X-Content-Type-Options": "nosniff",
            "Pragma": "no-store,no-cache",
            "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
            "Expires": "0",
            "Content-Type": "application/json;charset=UTF-8",
            "Transfer-Encoding": "chunked",
            "Date": "Mon, 07 Aug 2023 10:59:39 GMT",
            "Keep-Alive": "timeout=70",
            "Connection": "keep-alive",
            "Server": "ServiceNow",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
        },
        "reason": "Created",
        "json_body": {
            "result": {
                "parent": "",
                "made_sla": "true",
                "caused_by": "",
                "watch_list": "",
                "upon_reject": "cancel",
                "sys_updated_on": "2023-08-07 10:59:39",
                "child_incidents": "0",
                "hold_reason": "",
                "origin_table": "",
                "task_effective_number": "INC0010006",
                "approval_history": "",
                "number": "INC0010006",
                "resolved_by": "",
                "sys_updated_by": "admin",
                "opened_by": {
                    "link": "https://dev60827.service-now.com/api/now/v2/table/sys_user/6816f79cc0a8016401c5a33be04be441",
                    "value": "6816f79cc0a8016401c5a33be04be441"
                },
                "user_input": "",
                "sys_created_on": "2023-08-07 10:59:39",
                "sys_domain": {
                    "link": "https://dev60827.service-now.com/api/now/v2/table/sys_user_group/global",
                    "value": "global"
                },
                "state": "1",
                "route_reason": "",
                "sys_created_by": "admin",
                "knowledge": "false",
                "order": "",
                "calendar_stc": "",
                "closed_at": "",
                "cmdb_ci": "",
                "delivery_plan": "",
                "contract": "",
                "impact": "3",
                "active": "true",
                "work_notes_list": "",
                "business_service": "",
                "business_impact": "",
                "priority": "5",
                "sys_domain_path": "/",
                "rfc": "",
                "time_worked": "",
                "expected_start": "",
                "opened_at": "2023-08-07 10:59:39",
                "business_duration": "",
                "group_list": "",
                "work_end": "",
                "caller_id": "",
                "reopened_time": "",
                "resolved_at": "",
                "approval_set": "",
                "subcategory": "",
                "work_notes": "",
                "universal_request": "",
                "short_description": "",
                "close_code": "",
                "correlation_display": "",
                "delivery_task": "",
                "work_start": "",
                "assignment_group": "",
                "additional_assignee_list": "",
                "business_stc": "",
                "cause": "",
                "description": "",
                "origin_id": "",
                "calendar_duration": "",
                "close_notes": "",
                "notify": "1",
                "service_offering": "",
                "sys_class_name": "incident",
                "closed_by": "",
                "follow_up": "",
                "parent_incident": "",
                "sys_id": "26d1744d47603110d737cd9bd36d436b",
                "contact_type": "",
                "reopened_by": "",
                "incident_state": "1",
                "urgency": "3",
                "problem_id": "",
                "company": "",
                "reassignment_count": "0",
                "activity_due": "",
                "assigned_to": "",
                "severity": "3",
                "comments": "",
                "approval": "not requested",
                "sla_due": "",
                "comments_and_work_notes": "",
                "due_date": "",
                "sys_mod_count": "0",
                "reopen_count": "0",
                "sys_tags": "",
                "escalation": "0",
                "upon_approval": "proceed",
                "correlation_id": "",
                "location": "",
                "category": "inquiry"
            }
        }
    }
]
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