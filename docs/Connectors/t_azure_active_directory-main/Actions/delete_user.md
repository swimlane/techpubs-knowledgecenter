# Delete User

**Description**: Removes a user from Azure Active Directory using their unique identifier (ID). Requires the user's ID as a path parameter.

## Endpoint

- **URL:** `/v1.0/users/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: The ID of the user.
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Wed, 23 Aug 2023 14:02:55 GMT",
      "Content-Type": "text/html; charset=UTF-8",
      "Content-Length": "999",
      "Connection": "keep-alive",
      "Cache-Control": "private",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "x-content-type-options": "nosniff",
      "X-XSS-Protection": "1; mode=block",
      "x-ms-version": "12.43.4.1 (v12.42.0.1#162d343f82.230814-2250) Signed",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-UA-Compatible": "IE=edge",
      "X-Frame-Options": "SAMEORIGIN",
      "x-azure-ref": "20230823T140255Z-bg05mztcd56310tsaceruzncb400000003h0000000002692",
      "X-Cache": "CONFIG_NOCACHE",
      "Accept-Ranges": "bytes"
    },
    "reason": "OK",
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
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Cache-Control | string |
| Content-Encoding | string |
| Vary | string |
| x-content-type-options | string |
| X-XSS-Protection | string |
| x-ms-version | string |
| Strict-Transport-Security | string |
| X-UA-Compatible | string |
| X-Frame-Options | string |
| x-azure-ref | string |
| X-Cache | string |
| Accept-Ranges | string |