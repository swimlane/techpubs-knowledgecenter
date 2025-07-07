# List eDiscovery Case Tags

**Description**: Retrieves a list of eDiscoveryReviewTag objects for a specified case in Microsoft Graph API, requiring the ediscoveryCaseId.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/tags`
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases('58399dff-cebe-478f-b1af-d3227f1fd645')/tags",
      "@odata.count": 5,
      "value": [
        {
          "displayName": "My tag",
          "lastModifiedDateTime": "2022-05-23T19:41:01.7432683Z",
          "childSelectability": "Many",
          "id": "062de822f17a4a2e9b833aa3f6c37108",
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            }
          }
        },
        {
          "displayName": "Responsive",
          "description": "",
          "lastModifiedDateTime": "2022-05-23T19:41:24.4237284Z",
          "childSelectability": "One",
          "id": "d3d99dc704a74801b792b3e1e722aa0d",
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            }
          }
        },
        {
          "displayName": "Not responsive",
          "lastModifiedDateTime": "2022-05-23T19:41:31.3381716Z",
          "childSelectability": "One",
          "id": "ced26633616a434abd83762d49a25a6c",
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            }
          }
        },
        {
          "displayName": "Processing",
          "description": "Determine whether to outsource processing",
          "lastModifiedDateTime": "2022-05-23T19:46:03.8746996Z",
          "childSelectability": "Many",
          "id": "d8580989505c4fb3a25b845013697cf7",
          "createdBy": {
            "user": {
              "id": "c25c3914-f9f7-43ee-9cba-a25377e0cec6",
              "displayName": "MOD Administrator",
              "userPrincipalName": "admin@M365x809305.onmicrosoft.com"
            }
          }
        },
        {
          "displayName": "External",
          "lastModifiedDateTime": "2022-05-23T19:46:10.5212362Z",
          "childSelectability": "One",
          "id": "d05c2ef9369d49c293b5a6a6d18a5fd9",
          "createdBy": {
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
  - **@odata.count** (number)
  - **value** (array)
    - **displayName** (string)
    - **lastModifiedDateTime** (string)
    - **childSelectability** (string)
    - **id** (string)
    - **createdBy** (object)
      - **user** (object)
        - **id** (string)
        - **displayName** (string)
        - **userPrincipalName** (string)
    - **description** (string)
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