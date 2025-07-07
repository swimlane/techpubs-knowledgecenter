# List Simulations

**Description**: Retrieve attack simulation campaigns from a Microsoft Graph tenant to evaluate security preparedness.

## Endpoint

- **URL:** `/v1.0/security/attackSimulation/simulations`
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
          "id": "f1b13829-3829-f1b1-2938-b1f12938b1f1",
          "displayName": "Sample Simulation",
          "description": "Sample Simulation Description",
          "attackType": "social",
          "attackTechnique": "credentialHarvesting",
          "status": "scheduled",
          "createdDateTime": "2021-01-01T01:01:01.01Z",
          "createdBy": {
            "id": "99af58b9-ef1a-412b-a581-cb42fe8c8e21",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          },
          "lastModifiedDateTime": "2021-01-01T01:01:01.01Z",
          "lastModifiedBy": {
            "id": "99af58b9-ef1a-412b-a581-cb42fe8c8e21",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          },
          "launchDateTime": "2021-01-01T02:01:01.01Z",
          "completionDateTime": "2021-01-07T01:01:01.01Z",
          "isAutomated": false,
          "automationId": "f1b13829-3829-f1b1-2938-b1f12938b1ab",
          "payloadDeliveryPlatform": "email"
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
    - **id** (string)
    - **displayName** (string)
    - **description** (string)
    - **attackType** (string)
    - **attackTechnique** (string)
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
    - **launchDateTime** (string)
    - **completionDateTime** (string)
    - **isAutomated** (boolean)
    - **automationId** (string)
    - **payloadDeliveryPlatform** (string)
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