# Get File Statistics

**Description**: Retrieve detailed statistics for a specific file in Microsoft Defender using the file's unique identifier.

## Endpoint

- **URL:** `/api/files/{{id}}/stats`
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
      "Date": "Thu, 04 May 2023 17:42:51 GMT",
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
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#microsoft.windowsDefenderATP.api.InOrgFileStats",
      "sha1": "6532ec91d513acc05f43ee0aa3002599729fd3e1",
      "orgPrevalence": "0",
      "organizationPrevalence": 0,
      "orgFirstSeen": null,
      "orgLastSeen": null,
      "globalPrevalence": "10",
      "globallyPrevalence": 10,
      "globalFirstObserved": "2018-05-07T14:05:18.4401316Z",
      "globalLastObserved": "2022-11-15T03:37:49.4593231Z",
      "topFileNames": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **sha1** (string)
  - **orgPrevalence** (string)
  - **organizationPrevalence** (number)
  - **orgFirstSeen** (object)
  - **orgLastSeen** (object)
  - **globalPrevalence** (string)
  - **globallyPrevalence** (number)
  - **globalFirstObserved** (string)
  - **globalLastObserved** (string)
  - **topFileNames** (array)
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