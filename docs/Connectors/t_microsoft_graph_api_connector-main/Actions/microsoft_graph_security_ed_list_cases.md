# List eDiscovery Cases

**Description**: Retrieve a comprehensive list of eDiscoveryCase objects with properties from the Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/security/cases/ediscoveryCases`
- **Method:** `GET`
## Inputs

- **parameters** (object): URL Query Parameters
  - **filter** (string): Use the `filter` query parameter to retrieve just a subset of a collection. For guidance on using `filter`, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderBy** (string): Use the `orderby` query parameter to specify the sort order of the items returned from Microsoft Graph.
  - **top** (number): Sets the page size of results.
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
      "@odata.context": "https://graph.microsoft.com/beta/$metadata#security/cases/ediscoveryCases",
      "@odata.count": 22,
      "value": [
        {
          "description": "",
          "lastModifiedDateTime": "2022-05-19T23:30:41.23Z",
          "status": "active",
          "closedDateTime": null,
          "externalId": "",
          "id": "60f86305-ac3e-408b-baa2-ea585dd8b0c0",
          "displayName": "My case 1",
          "createdDateTime": "2022-05-19T23:30:41.23Z",
          "lastModifiedBy": {
            "application": null,
            "user": {
              "id": null,
              "displayName": "MOD Administrator"
            }
          },
          "closedBy": {
            "application": null,
            "user": {
              "id": null,
              "displayName": ""
            }
          }
        },
        {
          "description": "",
          "lastModifiedDateTime": "2022-05-18T23:05:07.82Z",
          "status": "active",
          "closedDateTime": null,
          "externalId": "",
          "id": "7acdda75-3559-4f93-9827-cbd4c89db033",
          "displayName": "My case 2",
          "createdDateTime": "2022-05-18T23:05:07.82Z",
          "lastModifiedBy": {
            "application": null,
            "user": {
              "id": null,
              "displayName": "MOD Administrator"
            }
          },
          "closedBy": {
            "application": null,
            "user": {
              "id": null,
              "displayName": ""
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
    - **description** (string)
    - **lastModifiedDateTime** (string)
    - **status** (string)
    - **closedDateTime** (object)
    - **externalId** (string)
    - **id** (string)
    - **displayName** (string)
    - **createdDateTime** (string)
    - **lastModifiedBy** (object)
      - **application** (object)
      - **user** (object)
        - **id** (object)
        - **displayName** (string)
    - **closedBy** (object)
      - **application** (object)
      - **user** (object)
        - **id** (object)
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