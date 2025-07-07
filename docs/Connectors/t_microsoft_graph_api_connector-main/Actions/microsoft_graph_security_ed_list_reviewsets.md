# List eDiscovery Case Review Sets

**Description**: Retrieve eDiscovery review sets associated with a specified case ID using the Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets`
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases('b0073e4e-4184-41c6-9eb7-8c8cc3e2288b')/reviewSets",
      "value": [
        {
          "displayName": "My review set",
          "id": "025852b3-5062-4169-9609-9861a6fe2fe5",
          "createdDateTime": "2022-05-23T16:26:08.7203883Z",
          "createdBy": {
            "application": null,
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
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
    - **displayName** (string)
    - **id** (string)
    - **createdDateTime** (string)
    - **createdBy** (object)
      - **application** (object)
      - **user** (object)
        - **id** (string)
        - **displayName** (string)
        - **userPrincipalName** (string)
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