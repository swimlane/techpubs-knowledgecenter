# List eDiscovery Case Operations

**Description**: Retrieve caseOperation objects with properties from Microsoft Graph API using the provided ediscoveryCaseId.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/operations`
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases('b0073e4e-4184-41c6-9eb7-8c8cc3e2288b')/operations",
      "value": [
        {
          "createdDateTime": "2022-05-23T01:09:36.834501Z",
          "completedDateTime": "2022-05-23T01:10:08.8710734Z",
          "percentProgress": 100,
          "status": "succeeded",
          "action": "holdUpdate",
          "id": "1ab699d7e53d46de944144c4a650d66f",
          "createdBy": {
            "application": null,
            "user": {
              "id": "0d38933a-0bbd-41ca-9ebd-28c4b5ba7cb7",
              "displayName": null,
              "userPrincipalName": null
            }
          }
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
  - **value** (array)
    - **createdDateTime** (string)
    - **completedDateTime** (string)
    - **percentProgress** (number)
    - **status** (string)
    - **action** (string)
    - **id** (string)
    - **createdBy** (object)
      - **application** (object)
      - **user** (object)
        - **id** (string)
        - **displayName** (object)
        - **userPrincipalName** (object)
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