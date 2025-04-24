# Update Security Incident

**Description**: Updates a specified security incident in ServiceNow using the unique sys_id as an identifier.

## Endpoint

- **URL:** `api/now/table/{{security_incident}}/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

| Name | Type | Required |
|------|------|----------|
| path_parameters | object | Yes |
| json_body | object | No |
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Set-Cookie": "JSESSIONID=0ADFD22F053BCC78A9A82FAF40E83D50; Path=/; HttpOnly;Secure, BIGipServerpool_dev60827=999184138.46398.0000; path=/; Httponly; Secure",
      "Server-Timing": "wall;dur=0, sem_wait;dur=0, sesh_wait;dur=0, app_cpu;dur=0, db;dur=1, acl;dur=0, br;dur=null, ui_action;dur=0, cache_build;dur=0, scripting;dur=0",
      "Content-Security-Policy": "frame-ancestors 'self' teams.microsoft.com *.teams.microsoft.com",
      "Content-Length": "0",
      "Date": "Mon, 07 Aug 2023 11:18:32 GMT",
      "Keep-Alive": "timeout=70",
      "Connection": "close",
      "Server": "ServiceNow",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "response_text": ""
  }
]
```
### Output Parameters

| Name | Type |
|------|------|
| status_code | number |
| reason | string |
| response_text | string |
## Response Headers

| Header | Type |
|--------|------|
| Set-Cookie | string |
| Server-Timing | string |
| Content-Security-Policy | string |
| Content-Length | string |
| Date | string |
| Keep-Alive | string |
| Connection | string |
| Server | string |
| Strict-Transport-Security | string |