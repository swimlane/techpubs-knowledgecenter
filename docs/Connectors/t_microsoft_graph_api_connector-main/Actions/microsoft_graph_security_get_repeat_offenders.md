# Get Repeat Offenders

**Description**: Lists tenant users who have been compromised multiple times in simulation and training campaigns via the Microsoft Graph API.

## Endpoint

- **URL:** `/V1.0/reports/security/getAttackSimulationRepeatOffenders`
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
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.attackSimulationRepeatOffender)",
      "@odata.nextLink": "https://graph.microsoft.com/v1.0/reports/security/getAttackSimulationRepeatOffenders?$skiptoken=+RID%3",
      "value": [
        {
          "repeatOffenceCount": 5,
          "attackSimulationUser": {
            "userId": "6fcdab00-385b-46f2-a329-b843b49e9147",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
          }
        },
        {
          "repeatOffenceCount": 638,
          "attackSimulationUser": {
            "userId": "478a22cd-aecc-41df-b995-88c8de17aaf5",
            "displayName": "Reed Flores",
            "email": "reed@contoso.com"
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
    - **repeatOffenceCount** (number)
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