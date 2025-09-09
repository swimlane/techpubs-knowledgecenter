# Get Alert User Information

**Description**: Retrieve detailed user information linked to a specific Microsoft Defender alert by using the unique alert ID.

## Endpoint

- **URL:** `/api/alerts/{{id}}/user`
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
      "Date": "Thu, 04 May 2023 13:19:32 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "Not Found",
    "json_body": {
      "error": {
        "code": "ResourceNotFound",
        "message": "There is no User related to alert ar638180599315648136_73827727",
        "target": "|f712eef2-447d37a1beaf6d2b."
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