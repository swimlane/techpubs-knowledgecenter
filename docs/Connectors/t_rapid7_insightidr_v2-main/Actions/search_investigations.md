# Search Investigations

**Description**: Performs a search for investigations in Rapid7 InsightIDR V2 using specified criteria and returns matching results. Requires headers and path parameters.

## Endpoint

- **URL:** `idr/v2/investigations/{{_search}}`
- **Method:** `POST`
## Inputs

- **parameters** (object)
  - **index** (number)
  - **multi-customer** (boolean)
  - **size** (number)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
- **path_parameters** (object) – Required
  - **_search** (string) – Required
- **json_body** (object)
  - **end_time** (string)
  - **search** (array)
    - **field** (string)
    - **operator** (string)
    - **value** (object)
  - **sort** (array)
    - **field** (string)
    - **order** (string)
  - **start_time** (string)
  - **title** (string)
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