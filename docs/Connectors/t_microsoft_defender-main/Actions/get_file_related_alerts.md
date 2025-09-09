# Get File Related Alerts

**Description**: Retrieve alerts related to a specific file in Microsoft Defender by using the file's unique identifier.

## Endpoint

- **URL:** `/api/files/{{id}}/alerts`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:39:45 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts",
      "value": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| OData-Version | string |
| Strict-Transport-Security | string |