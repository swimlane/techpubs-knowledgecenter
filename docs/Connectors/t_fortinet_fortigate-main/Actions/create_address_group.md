# Create Address Group

**Description**: Creates a new address group in Fortinet Fortigate for efficient management of multiple addresses.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/addrgrp`
- **Method:** `POST`
## Inputs

- **json_body** (object)
  - **name** (string)
  - **type** (string)
  - **category** (string)
  - **uuid** (string)
  - **member** (array)
    - **name** (string)
  - **comment** (string)
  - **exclude** (string)
  - **exclude-member** (array)
    - **name** (string)
  - **color** (number)
  - **tagging** (array)
    - **name** (string)
    - **category** (string)
    - **tags** (array)
  - **allow-routing** (string)
  - **fabric-object** (string)
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