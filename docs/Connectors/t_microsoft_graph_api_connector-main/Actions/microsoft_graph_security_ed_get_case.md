# Get eDiscovery Case

**Description**: Retrieve details and relationships of a specific eDiscovery case in Microsoft Graph API by providing the ediscoveryCaseId.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}`
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases/$entity",
      "description": "",
      "lastModifiedDateTime": "2022-05-22T18:36:46.597Z",
      "status": "active",
      "closedDateTime": null,
      "externalId": "324516",
      "id": "22aa2acd-7554-4330-9ba9-ce20014aaae4",
      "displayName": "CONTOSO LITIGATION-005",
      "createdDateTime": "2022-05-22T18:36:46.597Z",
      "lastModifiedBy": null,
      "closedBy": null
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **description** (string)
  - **lastModifiedDateTime** (string)
  - **status** (string)
  - **closedDateTime** (object)
  - **externalId** (string)
  - **id** (string)
  - **displayName** (string)
  - **createdDateTime** (string)
  - **lastModifiedBy** (object)
  - **closedBy** (object)
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