# Get IP Statistics

**Description**: Retrieve statistical data for a specified IP address from Microsoft Defender, with the IP required as a path parameter.

## Endpoint

- **URL:** `/api/ips/{{ip}}/stats`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **ip** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 17:49:46 GMT",
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
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#microsoft.windowsDefenderATP.api.InOrgIPStats",
      "ipAddress": "192.168.1.1",
      "orgPrevalence": "0",
      "organizationPrevalence": 0,
      "orgFirstSeen": null,
      "orgLastSeen": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **ipAddress** (string)
  - **orgPrevalence** (string)
  - **organizationPrevalence** (number)
  - **orgFirstSeen** (object)
  - **orgLastSeen** (object)
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