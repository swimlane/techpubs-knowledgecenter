# Update Incident

**Description**: Updates an existing incident in ServiceNow using the unique sys_id and additional data provided in a JSON body.

## Endpoint

- **URL:** `/api/now/table/incident/{{sys_id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required: Structured object with nested properties.
  - **sys_id** (string) – Required: Sys_id of the record to be updated.
- **json_body** (object) – Required: Structured object with nested properties.
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
      "Set-Cookie": "JSESSIONID=CEA60557841F8F77A8AB86E60B05F18D; Path=/; HttpOnly;Secure, BIGipServerpool_dev60827=999184138.46398.0000; path=/; Httponly; Secure",
      "Server-Timing": "wall;dur=0, sem_wait;dur=0, sesh_wait;dur=0, app_cpu;dur=0, db;dur=1, acl;dur=0, br;dur=null, ui_action;dur=0, cache_build;dur=0, scripting;dur=0",
      "Content-Security-Policy": "frame-ancestors 'self' teams.microsoft.com *.teams.microsoft.com",
      "Content-Length": "0",
      "Date": "Mon, 07 Aug 2023 11:12:15 GMT",
      "Keep-Alive": "timeout=70",
      "Connection": "keep-alive",
      "Server": "ServiceNow",
      "Strict-Transport-Security": "max-age=63072000; includeSubDomains"
    },
    "reason": "OK",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number): Status value or code.
- **reason** (string): Text string.
- **response_text** (string): Text string.
## Response Headers

| Header | Type | Description |
|--------|------|-------------|
| Set-Cookie | string | Text string. |
| Server-Timing | string | Text string. |
| Content-Security-Policy | string | Text string. |
| Content-Length | string | Text string. |
| Date | string | Timestamp in ISO 8601 format. |
| Keep-Alive | string | Text string. |
| Connection | string | Text string. |
| Server | string | Text string. |
| Strict-Transport-Security | string | Text string. |