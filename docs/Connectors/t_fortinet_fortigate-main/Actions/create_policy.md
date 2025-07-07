# Create Policy

**Description**: Establish a new network policy within Fortinet Fortigate to oversee and regulate security procedures.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/DoS-policy`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **policyid** (number)
  - **status** (string)
  - **name** (string)
  - **comments** (string)
  - **interface** (string)
  - **srcaddr** (array)
    - **name** (string)
  - **dstaddr** (array)
    - **name** (string)
  - **service** (array)
    - **name** (string)
  - **anomaly** (array)
    - **name** (string)
    - **status** (string)
    - **log** (string)
    - **action** (string)
    - **quarantine** (string)
    - **quarantine-expiry** (string)
    - **quarantine-log** (string)
    - **threshold** (number)
    - **threshold(default)** (number)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "date": "Mon, 08 May 2023 21:41:54 GMT",
      "x-frame-options": "SAMEORIGIN",
      "content-security-policy": "frame-ancestors 'self'",
      "x-xss-protection": "1; mode=block",
      "content-length": "354",
      "content-type": "text/html; charset=iso-8859-1",
      "Connection": "keep-alive"
    },
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
## Response Headers

| Header | Type |
|--------|------|
| date | string |
| x-frame-options | string |
| content-security-policy | string |
| x-xss-protection | string |
| content-length | string |
| content-type | string |
| Connection | string |