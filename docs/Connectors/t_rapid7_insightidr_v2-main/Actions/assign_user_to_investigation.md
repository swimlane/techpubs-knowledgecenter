# Assign User to Investigation

**Description**: Assign a user to an investigation in Rapid7 InsightIDR V2 by specifying the investigation ID and user's email address.

## Endpoint

- **URL:** `idr/v2/investigations/{{id}}/assignee`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object)
  - **multi-customer** (boolean)
- **headers** (object) – Required
  - **Accept-version** (string) – Required
- **json_body** (object) – Required
  - **user_email_address** (string) – Required
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