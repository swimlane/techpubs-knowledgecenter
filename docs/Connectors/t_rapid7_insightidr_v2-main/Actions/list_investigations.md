# List Investigations

**Description**: Retrieve a paginated list of investigations from Rapid7 InsightIDR using specified request headers.

## Endpoint

- **URL:** `idr/v2/investigations`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **assignee.email** (string)
  - **end_time** (string)
  - **index** (number)
  - **multi-customer** (boolean)
  - **priorities** (string)
  - **size** (number)
  - **sort** (string)
  - **sources** (string)
  - **start_time** (string)
  - **statuses** (string)
  - **tags** (string)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
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
  - **metadata** (object)
    - **index** (number)
    - **size** (number)
    - **total_data** (number)
    - **total_pages** (number)
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