# List Simulation Automations

**Description**: Retrieve an overview of attack simulation automations and security test settings within a Microsoft Graph tenant.

## Endpoint

- **URL:** `/V1.0/security/attackSimulation/simulationAutomations`
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
      "value": [
        {
          "@odata.type": "#microsoft.graph.simulationAutomation",
          "id": "fbad62b0-b32d-b6ac-9f48-d84bbea08f96",
          "displayName": "Reed Flores",
          "description": "Sample Simulation Automation Description",
          "status": "running",
          "createdDateTime": "2022-01-01T01:01:01.01Z",
          "createdBy": {
            "id": "99af58b9-ef1a-412b-a581-cb42fe8c8e21",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          },
          "lastModifiedDateTime": "2022-01-01T01:01:01.01Z",
          "lastModifiedBy": {
            "id": "99af58b9-ef1a-412b-a581-cb42fe8c8e21",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          },
          "lastRunDateTime": "2022-01-01T01:01:01.01Z",
          "nextRunDateTime": "2022-01-01T01:01:01.01Z"
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
  - **value** (array)
    - **@odata.type** (string)
    - **id** (string)
    - **displayName** (string)
    - **description** (string)
    - **status** (string)
    - **createdDateTime** (string)
    - **createdBy** (object)
      - **id** (string)
      - **displayName** (string)
      - **email** (string)
    - **lastModifiedDateTime** (string)
    - **lastModifiedBy** (object)
      - **id** (string)
      - **displayName** (string)
      - **email** (string)
    - **lastRunDateTime** (string)
    - **nextRunDateTime** (string)
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