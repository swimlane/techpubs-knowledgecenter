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
[
    {
        "status_code": 200,
        "response_headers": {
            "Server-Timing": "sem_wait;dur=0, sesh_wait;dur=0",
            "Content-Encoding": "gzip",
            "X-Is-Logged-In": "true",
            "X-Transaction-ID": "7d9414489707",
            "Link": "<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=0>;rel=\"first\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=-1>;rel=\"prev\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=1>;rel=\"next\",<https://dev130168.service-now.com/api/now/v2/table/incident?query=number%3DINC0000040&display_value=True&sysparm_limit=1&sysparm_offset=66>;rel=\"last\"",
            "X-Total-Count": "67",
            "X-Content-Type-Options": "nosniff",
            "Pragma": "no-store,no-cache",
            "Cache-Control": "no-cache,no-store,must-revalidate,max-age=-1",
            "Expires": "0",
            "Content-Type": "application/json;charset=UTF-8",
            "Transfer-Encoding": "chunked",
            "Date": "Thu, 03 Nov 2022 20:32:32 GMT",
            "Keep-Alive": "timeout=20",
            "Connection": "keep-alive",
            "Server": "ServiceNow",
            "Set-Cookie": "glide_user=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_session=; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:10 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_user_route=glide.f6d1c4085a807931391acf9b7192b09e; Max-Age=2147483647; Expires=Tue, 21-Nov-2090 23:46:39 GMT; Path=/; HttpOnly; SameSite=None; Secure, glide_session_store=6D941C849707111084D57E121153AFF6; Max-Age=1800; Expires=Thu, 03-Nov-2022 21:02:32 GMT; Path=/; HttpOnly; SameSite=None; Secure",
            "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
        },
        "reason": "OK",
        "json_body": {
            "result": [
                {
                    "parent": "",
                    "made_sla": "true",
                    "caused_by": "",
                    "watch_list": "",
                    "upon_reject": "cancel",
                    "sys_updated_on": "2016-12-14 02:46:44",
                    "child_incidents": "0",
                    "hold_reason": "",
                    "origin_table": "",
                    "task_effective_number": "INC0000060",
                    "approval_history": "",
                    "number": "INC0000060",
                    "resolved_by": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007",
                        "value": "5137153cc611227c000bbd1bd8cd2007"
                    },
                    "sys_updated_by": "employee",
                    "opened_by": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
                        "value": "681ccaf9c0a8016400b98a06818d57c7"
                    },
                    "user_input": "",
                    "sys_created_on": "2016-12-12 15:19:57",
                    "sys_domain": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/global",
                        "value": "global"
                    },
                    "state": "7",
                    "route_reason": "",
                    "sys_created_by": "employee",
                    "knowledge": "false",
                    "order": "",
                    "calendar_stc": "102197",
                    "closed_at": "2016-12-14 02:46:44",
                    "cmdb_ci": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci/109562a3c611227500a7b7ff98cc0dc7",
                        "value": "109562a3c611227500a7b7ff98cc0dc7"
                    },
                    "delivery_plan": "",
                    "contract": "",
                    "impact": "2",
                    "active": "false",
                    "work_notes_list": "",
                    "business_service": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/cmdb_ci_service/27d32778c0a8000b00db970eeaa60f16",
                        "value": "27d32778c0a8000b00db970eeaa60f16"
                    },
                    "business_impact": "",
                    "priority": "3",
                    "sys_domain_path": "/",
                    "rfc": "",
                    "time_worked": "",
                    "expected_start": "",
                    "opened_at": "2016-12-12 15:19:57",
                    "business_duration": "1970-01-01 08:00:00",
                    "group_list": "",
                    "work_end": "",
                    "caller_id": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
                        "value": "681ccaf9c0a8016400b98a06818d57c7"
                    },
                    "reopened_time": "",
                    "resolved_at": "2016-12-13 21:43:14",
                    "approval_set": "",
                    "subcategory": "email",
                    "work_notes": "",
                    "universal_request": "",
                    "short_description": "Unable to connect to email",
                    "close_code": "Solved (Permanently)",
                    "correlation_display": "",
                    "delivery_task": "",
                    "work_start": "",
                    "assignment_group": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user_group/287ebd7da9fe198100f92cc8d1d2154e",
                        "value": "287ebd7da9fe198100f92cc8d1d2154e"
                    },
                    "additional_assignee_list": "",
                    "business_stc": "28800",
                    "cause": "",
                    "description": "I am unable to connect to the email server. It appears to be down.",
                    "origin_id": "",
                    "calendar_duration": "1970-01-02 04:23:17",
                    "close_notes": "This incident is resolved.",
                    "notify": "1",
                    "service_offering": "",
                    "sys_class_name": "incident",
                    "closed_by": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/681ccaf9c0a8016400b98a06818d57c7",
                        "value": "681ccaf9c0a8016400b98a06818d57c7"
                    },
                    "follow_up": "",
                    "parent_incident": "",
                    "sys_id": "1c741bd70b2322007518478d83673af3",
                    "contact_type": "self-service",
                    "reopened_by": "",
                    "incident_state": "7",
                    "urgency": "2",
                    "problem_id": "",
                    "company": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/core_company/31bea3d53790200044e0bfc8bcbe5dec",
                        "value": "31bea3d53790200044e0bfc8bcbe5dec"
                    },
                    "reassignment_count": "2",
                    "activity_due": "2016-12-13 01:26:36",
                    "assigned_to": {
                        "link": "https://dev130168.service-now.com/api/now/v2/table/sys_user/5137153cc611227c000bbd1bd8cd2007",
                        "value": "5137153cc611227c000bbd1bd8cd2007"
                    },
                    "severity": "3",
                    "comments": "",
                    "approval": "not requested",
                    "sla_due": "",
                    "comments_and_work_notes": "",
                    "due_date": "",
                    "sys_mod_count": "15",
                    "reopen_count": "0",
                    "sys_tags": "",
                    "escalation": "0",
                    "upon_approval": "proceed",
                    "correlation_id": "",
                    "location": "",
                    "category": "inquiry"
                }
            ]
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