# Get Machine Action

**Description**: Retrieve details of a specific machine action in Microsoft Defender using the unique action ID provided in path parameters.

## Endpoint

- **URL:** `/api/machineactions/{{id}}`
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
      "Date": "Thu, 04 May 2023 17:56:32 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Bad Request",
    "json_body": {
      "error": {
        "code": "BadRequest",
        "message": "The key value (556b3952acb0bff29816d267822305781cc183ec) from request is not valid. The key value should be format of type 'Edm.Guid'.",
        "target": "|b1838e63-40a6640ddd2719ac."
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
| Strict-Transport-Security | string |