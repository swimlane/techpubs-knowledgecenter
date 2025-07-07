# Get Training Coverage for Users

**Description**: Lists tenant users' training coverage in attack simulation and training campaigns via Microsoft Graph API.

## Endpoint

- **URL:** `/V1.0/reports/security/getAttackSimulationTrainingUserCoverage`
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
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.attackSimulationTrainingUserCoverage)",
      "@odata.nextLink": "https://graph.microsoft.com/v1.0/reports/security/getAttackSimulationTrainingUserCoverage?$skiptoken=+RID%3",
      "value": [
        {
          "userTrainings": [
            {
              "assignedDateTime": "2021-07-28T07:33:47.493239Z",
              "completionDateTime": null,
              "trainingStatus": "assigned",
              "displayName": "Phishing"
            },
            {
              "assignedDateTime": "2021-07-28T07:33:47.493239Z",
              "completionDateTime": "2022-01-14T03:11:58Z",
              "trainingStatus": "completed",
              "displayName": ""
            }
          ],
          "attackSimulationUser": {
            "userId": "c5e40ca7-4c09-4801-a140-5ef733d1de0e",
            "displayName": null,
            "email": null
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
    - **userTrainings** (array)
      - **assignedDateTime** (string)
      - **completionDateTime** (string)
      - **trainingStatus** (string)
      - **displayName** (string)
    - **attackSimulationUser** (object)
      - **userId** (string)
      - **displayName** (object)
      - **email** (object)
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