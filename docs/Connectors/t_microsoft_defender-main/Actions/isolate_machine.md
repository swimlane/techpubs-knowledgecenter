# Isolate Machine

**Description**: Initiates isolation of a specified machine in Microsoft Defender using its unique ID and requires a comment.

## Endpoint

- **URL:** `/api/machines/{{id}}/isolate`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **json_body** (object) – Required
  - **Comment** (string) – Required: Comment to associate with the action.
  - **IsolationType** (string): Type of the isolation. Allowed values are Full or Selective. IsolationType controls the type of isolation to perform and can be one of the following Full- Full isolation. Selective- Restrict only limited set of applications from accessing the network.
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