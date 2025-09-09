# Get Alert IPs

**Description**: Retrieves IP addresses associated with a specific Microsoft Defender alert by using the provided alert ID.

## Endpoint

- **URL:** `/api/{{id}}/ips`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 404,
    "response_headers": {
      "Date": "Thu, 04 May 2023 13:11:16 GMT",
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