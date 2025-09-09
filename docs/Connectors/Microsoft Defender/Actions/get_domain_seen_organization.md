# Get Domain Seen Organization

**Description**: Determines if a specific domain has been observed within the organization by Microsoft Defender, requiring the 'domain' as a path parameter.

## Endpoint

- **URL:** `/api/domains/{{domain}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **domain** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 404,
    "response_headers": {
      "Date": "Thu, 04 May 2023 18:12:16 GMT",
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