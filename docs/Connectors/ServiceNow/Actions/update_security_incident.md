# Update Security Incident

**Description**: Updates a specified security incident in ServiceNow using the unique sys_id as an identifier.

## Endpoint

- **URL:** `api/now/table/{{security_incident}}/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Auto-generated description for `path_parameters`. Please update manually if needed.
  - **security_incident** (string) – Required: Name of the Security Incident Table
  - **sys_id** (string) – Required: ID of the security incident to update.
- **json_body** (object): Auto-generated description for `json_body`. Please update manually if needed.
  - **sysparm_display_value** (string): Determines the type of data returned, either the actual values from the database or the display values of the fields.
  - **sysparm_fields** (string): Comma-separated list of fields to return in the response.
  - **sysparm_input_display_value** (boolean): Flag that indicates whether to set field values using the display value or the actual value.
  - **sysparm_query_no_domain** (boolean): Flag that indicates whether to restrict the record search to only the domains for which the logged in user is configured.
  - **sysparm_view** (string): If you also specify the sysparm_fields parameter, it takes precedent.
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

- **status_code** (number): Auto-generated description for `status_code`. Please update manually if needed.
- **reason** (string): Auto-generated description for `reason`. Please update manually if needed.
- **response_text** (string): Auto-generated description for `response_text`. Please update manually if needed.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string | Auto-generated description for `Set-Cookie`. Please update manually if needed. |
| Server-Timing | string | Auto-generated description for `Server-Timing`. Please update manually if needed. |
| Content-Security-Policy | string | Auto-generated description for `Content-Security-Policy`. Please update manually if needed. |
| Content-Length | string | Auto-generated description for `Content-Length`. Please update manually if needed. |
| Date | string | Auto-generated description for `Date`. Please update manually if needed. |
| Keep-Alive | string | Auto-generated description for `Keep-Alive`. Please update manually if needed. |
| Connection | string | Auto-generated description for `Connection`. Please update manually if needed. |
| Server | string | Auto-generated description for `Server`. Please update manually if needed. |
| Strict-Transport-Security | string | Auto-generated description for `Strict-Transport-Security`. Please update manually if needed. |