# Get Incident History

**Description**: Retrieves the history and notes for a specified incident in Symantec DLP using the provided incident ID.

## Endpoint

- **URL:** `/ProtectManager/webservices/v2/incidents/{{id}}/history`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: The incident ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": [
      {
        "incidentHistoryDate": "2022-08-26T15:17:37.369",
        "dlpUserName": "Administrator",
        "incidentHistoryAction": "SET_STATUS",
        "incidentHistoryDetail": "New",
        "policyGroupId": 1,
        "detectionServerName": "Vontu Monitor One",
        "incidentId": 1,
        "messageSource": "NETWORK",
        "messageDate": "2017-07-27T16:08:09",
        "incidentHistoryActionString": "Status Changed"
      },
      {
        "incidentHistoryDate": "2022-08-26T15:17:23.19",
        "dlpUserName": "Administrator",
        "incidentHistoryAction": "MESSAGE_NOT_RETAINED",
        "policyGroupId": 1,
        "detectionServerName": "Vontu Monitor One",
        "incidentId": 1,
        "messageSource": "NETWORK",
        "messageDate": "2017-07-27T16:08:09",
        "incidentHistoryActionString": "The original message content was not retained due to default retention behavior or due to the Limit Incident Data Retention response rule action"
      },
      {
        "incidentHistoryDate": "2022-08-26T15:17:23.186",
        "dlpUserName": "Administrator",
        "incidentHistoryAction": "SET_SEVERITY",
        "incidentHistoryDetail": "High",
        "policyGroupId": 1,
        "detectionServerName": "Vontu Monitor One",
        "incidentId": 1,
        "messageSource": "NETWORK",
        "messageDate": "2017-07-27T16:08:09",
        "incidentHistoryActionString": "Severity Changed"
      },
      {
        "incidentHistoryDate": "2022-08-26T15:17:23.153",
        "dlpUserName": "Administrator",
        "incidentHistoryAction": "DETECTED",
        "policyGroupId": 1,
        "detectionServerName": "Vontu Monitor One",
        "incidentId": 1,
        "messageSource": "NETWORK",
        "messageDate": "2017-07-27T16:08:09",
        "incidentHistoryActionString": "Detected"
      }
    ]
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (array)
  - **incidentHistoryDate** (string)
  - **dlpUserName** (string)
  - **incidentHistoryAction** (string)
  - **incidentHistoryDetail** (string)
  - **policyGroupId** (number)
  - **detectionServerName** (string)
  - **incidentId** (number)
  - **messageSource** (string)
  - **messageDate** (string)
  - **incidentHistoryActionString** (string)