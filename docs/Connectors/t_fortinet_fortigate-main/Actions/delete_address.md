# Delete Address

**Description**: Removes a specified address object from Fortinet Fortigate configurations using the provided name.

## Endpoint

- **URL:** `/api/v2/cmdb/firewall/address/{{name}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **name** (string) – Required
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