# Get Domain Statistics

**Description**: Retrieve statistical data for a specified domain from Microsoft Defender, utilizing the 'domain' path parameter.

## Endpoint

- **URL:** `/api/domains/{{domain}}/stats`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **domain** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:35:52 GMT",
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
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#microsoft.windowsDefenderATP.api.InOrgDomainStats",
      "host": "google.com",
      "orgPrevalence": "1",
      "orgFirstSeen": "2023-04-20T13:07:59.6924183Z",
      "orgLastSeen": "2023-05-02T12:53:24.2750645Z",
      "organizationPrevalence": 1
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **host** (string)
  - **orgPrevalence** (string)
  - **orgFirstSeen** (string)
  - **orgLastSeen** (string)
  - **organizationPrevalence** (number)
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