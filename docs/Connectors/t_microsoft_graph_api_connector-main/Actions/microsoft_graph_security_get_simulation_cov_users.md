# Get Simulation Coverage for Users

**Description**: Lists tenant users' training coverage for attack simulation and training campaigns via Microsoft Graph API.

## Endpoint

- **URL:** `/V1.0/reports/security/getAttackSimulationSimulationUserCoverage`
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
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.attackSimulationSimulationUserCoverage)",
      "@odata.nextLink": "https://graph.microsoft.com/v1.0/reports/security/getAttackSimulationSimulationUserCoverage?$skiptoken=rZDNasMwEIRfxei%2bRLFWtgRxwZKsYCil0J9rcCORGlI7yHLbvH3j0pQefCqew7LMsOzHbEL%2fkbRuVzvfxTaeC6ItMpVxBKpKBkh5CcIKhLVUSLUtdaYFSbr3%2fe4%2b9Ccf4vmuefMFuW2GaH3cv3pXO5K0v3HdOf9ZEEqmP1fzuTmOfju27hKgYJbmFSjGNGCuLKRZJYEKIxApo6WQZHWzWYz0sXk5%2bmmdp%2fx78I35EEPbHQryNPgwzJKgqGiKUoK%2boACmQoFMDQdmM56uc2O4qZbt7EcwM65alPS%2fnW1DP56m0r4A",
      "value": [
        {
          "simulationCount": 1063,
          "latestSimulationDateTime": "2022-02-10T10:45:50Z",
          "clickCount": 0,
          "compromisedCount": 0,
          "attackSimulationUser": {
            "userId": "9a00ce98-2c83-41be-89f7-6fdff7950aa9",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          }
        },
        {
          "simulationCount": null,
          "latestSimulationDateTime": null,
          "clickCount": null,
          "compromisedCount": null,
          "attackSimulationUser": {
            "userId": "e911a813-d360-4b1a-b3df-375dde934f2b",
            "displayName": "no role",
            "email": ""
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
  - **@odata.nextLink** (string)
  - **value** (array)
    - **simulationCount** (object)
    - **latestSimulationDateTime** (object)
    - **clickCount** (object)
    - **compromisedCount** (object)
    - **attackSimulationUser** (object)
      - **userId** (string)
      - **displayName** (string)
      - **email** (string)
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