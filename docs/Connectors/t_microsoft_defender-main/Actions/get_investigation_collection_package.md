# Get Investigation Collection Package

**Description**: Retrieve a Microsoft Defender investigation package for an entity by using the unique ID.

## Endpoint

- **URL:** `/api/machineactions/{{id}}/getPackageUri`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 400,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:45:50 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Bad Request",
    "json_body": {
      "error": {
        "code": "InvalidInput",
        "message": "Provided Guid is not a valid id for a CollectInvestigationPackage action",
        "target": "|76dce355-471ae6d819782413."
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **error** (object)
    - **code** (string)
    - **message** (string)
    - **target** (string)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |