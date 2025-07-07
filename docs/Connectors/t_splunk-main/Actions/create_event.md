# Create Event

**Description**: Creates a new event in Cisco Splunk for incident logging and tracking, allowing specification of the output mode.

## Endpoint

- **URL:** `services/receivers/simple`
- **Method:** `POST`
## Inputs

- **parameters** (object)
  - **output_mode** (string) – Required
- **data_body** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **index** (string)
  - **bytes** (number)
  - **host** (string)
  - **source** (string)
  - **sourcetype** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Expires | string |
| Cache-Control | string |
| Content-Type | string |
| X-Content-Type-Options | string |
| Content-Length | string |
| Vary | string |
| Connection | string |
| X-Frame-Options | string |
| Server | string |