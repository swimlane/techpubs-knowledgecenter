# Set Status Investigation

**Description**: Updates the status of a specified investigation in Rapid7 InsightIDR V2 by using its unique ID or RRN, requiring path parameters.

## Endpoint

- **URL:** `idr/v2/investigations/{{id}}/status/{{status}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
  - **status** (string) – Required
- **parameters** (object)
  - **multi-customer** (boolean)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
- **json_body** (object)
  - **disposition** (string)
  - **threat_command_close_reason** (string)
  - **threat_command_free_text** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **assignee** (object)
    - **email** (string)
    - **name** (string)
  - **created_time** (string)
  - **disposition** (string)
  - **first_alert_time** (string)
  - **last_accessed** (string)
  - **latest_alert_time** (string)
  - **organization_id** (string)
  - **priority** (string)
  - **responsibility** (string)
  - **rrn** (string)
  - **source** (string)
  - **status** (string)
  - **tags** (array)
  - **title** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Cache-Control | string |
| Expires | string |
| Pragma | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| X-XSS-Protection | string |
| vary | string |
| Access-Control-Allow-Credentials | string |