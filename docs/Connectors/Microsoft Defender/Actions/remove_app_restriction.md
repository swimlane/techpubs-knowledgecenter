# Remove APP Restriction

**Description**: Removes an existing application restriction in Microsoft Defender using the specified unique identifier (ID).

## Endpoint

- **URL:** `/api/machines/{{id}}/unrestrictCodeExecution`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **json_body** (object)
  - **Comment** (string)
  - **Isolationtype** (string)
## Output

### Example

```json
[
  {
    "status_code": 405,
    "response_headers": {
      "Date": "Thu, 04 May 2023 18:07:32 GMT",
      "Content-Length": "0",
      "Connection": "keep-alive",
      "Allow": "POST",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Method Not Allowed",
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
| Allow | string |
| Strict-Transport-Security | string |