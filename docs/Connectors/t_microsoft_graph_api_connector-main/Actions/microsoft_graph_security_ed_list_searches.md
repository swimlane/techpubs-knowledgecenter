# List eDiscovery Case Searches

**Description**: Retrieve eDiscovery search resources for a given case ID from Microsoft Graph API, requiring the ediscoveryCaseId as a path parameter.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/searches`
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases('b0073e4e-4184-41c6-9eb7-8c8cc3e2288b')/searches",
      "value": [
        {
          "dataSourceScopes": "none",
          "description": "My first search",
          "lastModifiedDateTime": "2022-05-23T04:38:07.5787454Z",
          "contentQuery": "(Author=\"edison\")",
          "id": "46867792-68e6-41db-9cd0-f651c2290d91",
          "displayName": "My search 2",
          "createdDateTime": "2022-05-23T04:38:07.5787454Z",
          "lastModifiedBy": null,
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            },
            "application": {
              "id": "de8bc8b5-d9f9-48b1-a8ad-b748da725064",
              "displayName": "Graph Explorer"
            }
          }
        },
        {
          "dataSourceScopes": "none",
          "description": "My first search",
          "lastModifiedDateTime": "2022-05-23T04:35:36.5424818Z",
          "contentQuery": "(Author=\"edison\")",
          "id": "80b9d59a-12a6-4273-a3d4-ab78f9a04ea5",
          "displayName": "My search 1",
          "createdDateTime": "2022-05-23T04:35:36.5424818Z",
          "lastModifiedBy": null,
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            },
            "application": {
              "id": "de8bc8b5-d9f9-48b1-a8ad-b748da725064",
              "displayName": "Graph Explorer"
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
    - **dataSourceScopes** (string)
    - **description** (string)
    - **lastModifiedDateTime** (string)
    - **contentQuery** (string)
    - **id** (string)
    - **displayName** (string)
    - **createdDateTime** (string)
    - **lastModifiedBy** (object)
    - **createdBy** (object)
      - **user** (object)
        - **id** (string)
        - **displayName** (string)
        - **userPrincipalName** (string)
      - **application** (object)
        - **id** (string)
        - **displayName** (string)
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