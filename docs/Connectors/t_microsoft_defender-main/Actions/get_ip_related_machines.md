# Get IP Related Machines

**Description**: Retrieve a list of machines associated with a specified IP address in Microsoft Defender, requiring the 'ip' path parameter.

## Endpoint

- **URL:** `/api/ips/{{ip}}/machines`
- **Method:** `get`
## Inputs

- **path_parameters** (object) – Required
  - **ip** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 404,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:50:09 GMT",
      "Content-Length": "0",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Not Found",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Length | string |
| Connection | string |
| Strict-Transport-Security | string |