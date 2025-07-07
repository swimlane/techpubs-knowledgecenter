# Create Investigation

**Description**: Initiate a manual investigation in Rapid7 InsightIDR V2 with custom headers and JSON body data.

## Endpoint

- **URL:** `idr/v2/investigations`
- **Method:** `POST`
## Inputs

- **headers** (object) – Required
  - **Accept-version** (string) – Required
- **json_body** (object) – Required
  - **assignee** (object)
    - **email** (string)
  - **disposition** (string)
  - **priority** (string)
  - **status** (string)
  - **title** (string)
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
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Expires | string |
| Pragma | string |
| X-Content-Type-Options | string |
| X-Frame-Options | string |
| X-XSS-Protection | string |
| vary | string |
| Access-Control-Allow-Credentials | string |