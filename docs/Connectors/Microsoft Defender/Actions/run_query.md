# Run Query

**Description**: Executes a custom query in Microsoft Defender and returns the results, requiring a 'Query' specified in the JSON body.

## Endpoint

- **URL:** `/api/advancedqueries/run`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **Query** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 400,
    "response_headers": {
      "Date": "Thu, 04 May 2023 18:35:41 GMT",
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
        "code": "BadRequest",
        "message": "A recognition error occurred.. Fix syntax errors in your query.",
        "target": "|1d25001e-48e8e09dbddde4f4."
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