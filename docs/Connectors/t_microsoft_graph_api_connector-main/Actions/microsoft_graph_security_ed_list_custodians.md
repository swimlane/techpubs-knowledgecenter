# List eDiscovery Case Custodians

**Description**: Retrieve a list of custodian objects and their properties from Microsoft Graph API using the provided ediscoveryCaseId.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **ediscoveryCaseId** (string) – Required: eDiscovery Case ID
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "client-request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"CP1PEPF00003034\"}}",
      "Date": "Tue, 27 Dec 2022 21:12:51 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases('b0073e4e-4184-41c6-9eb7-8c8cc3e2288b')/custodians",
      "@odata.count": 1,
      "value": [
        {
          "status": "active",
          "holdStatus": "notApplied",
          "createdDateTime": "2022-05-23T00:58:19.0702426Z",
          "lastModifiedDateTime": "2022-05-23T00:58:19.0702436Z",
          "releasedDateTime": null,
          "id": "0053a61a3b6c42738f7606791716a22a",
          "displayName": "Alex Wilber",
          "email": "AlexW@M365x809305.OnMicrosoft.com",
          "acknowledgedDateTime": "0001-01-01T00:00:00Z"
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.count** (number)
  - **value** (array)
    - **status** (string)
    - **holdStatus** (string)
    - **createdDateTime** (string)
    - **lastModifiedDateTime** (string)
    - **releasedDateTime** (object)
    - **id** (string)
    - **displayName** (string)
    - **email** (string)
    - **acknowledgedDateTime** (string)
## Response Headers

| Header | Type |
|--------|------|
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |