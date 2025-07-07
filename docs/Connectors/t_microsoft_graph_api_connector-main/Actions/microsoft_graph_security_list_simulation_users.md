# List Simulation Users

**Description**: Retrieve a list of users and their actions from an attack simulation campaign using the 'simulationId'.

## Endpoint

- **URL:** `/V1.0/security/attackSimulation/simulations/{{simulationId}}/report/simulationUsers`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **simulationId** (string) – Required: Simulation ID
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
          "isCompromised": true,
          "compromisedDateTime": "2021-01-01T01:02:01.01Z",
          "simulationEvents": [
            {
              "eventName": "SuccessfullyDeliveredEmail",
              "eventDateTime": "2021-01-01T01:01:01.01Z",
              "ipAddress": "100.200.100.200",
              "osPlatformDeviceDetails": "Sample OS",
              "browser": "Sample Browser"
            },
            {
              "eventName": "EmailLinkClicked",
              "eventDateTime": "2021-01-01T01:02:01.01Z",
              "ipAddress": "100.200.100.200",
              "osPlatformDeviceDetails": "Sample OS",
              "browser": "Sample Browser"
            }
          ],
          "trainingEvents": [
            {
              "displayName": "Sample Training",
              "latestTrainingStatus": "assigned",
              "trainingAssignedProperties": {
                "contentDateTime": "2021-01-01T01:03:01.01Z",
                "ipAddress": "100.200.100.200",
                "osPlatformDeviceDetails": "Sample OS",
                "browser": "Sample Browser",
                "potentialScoreImpact": 5
              },
              "trainingUpdatedProperties": {
                "contentDateTime": "2021-01-01T01:04:01.01Z",
                "ipAddress": "100.200.100.201",
                "osPlatformDeviceDetails": "Sample OS-2",
                "browser": "Sample Browser",
                "potentialScoreImpact": 5
              },
              "trainingCompletedProperties": {
                "contentDateTime": "2021-01-01T01:05:01.01Z",
                "ipAddress": "100.200.100.202",
                "osPlatformDeviceDetails": "Sample OS",
                "browser": "Sample Browser-2",
                "potentialScoreImpact": 5
              }
            }
          ],
          "assignedTrainingsCount": 1,
          "completedTrainingsCount": 0,
          "inProgressTrainingsCount": 0,
          "reportedPhishDateTime": "2021-01-01T01:01:01.01Z",
          "simulationUser": {
            "userId": "99af58b9-ef1a-412b-a581-cb42fe8c8e21",
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
  - **value** (array)
    - **isCompromised** (boolean)
    - **compromisedDateTime** (string)
    - **simulationEvents** (array)
      - **eventName** (string)
      - **eventDateTime** (string)
      - **ipAddress** (string)
      - **osPlatformDeviceDetails** (string)
      - **browser** (string)
    - **trainingEvents** (array)
      - **displayName** (string)
      - **latestTrainingStatus** (string)
      - **trainingAssignedProperties** (object)
        - **contentDateTime** (string)
        - **ipAddress** (string)
        - **osPlatformDeviceDetails** (string)
        - **browser** (string)
        - **potentialScoreImpact** (number)
      - **trainingUpdatedProperties** (object)
        - **contentDateTime** (string)
        - **ipAddress** (string)
        - **osPlatformDeviceDetails** (string)
        - **browser** (string)
        - **potentialScoreImpact** (number)
      - **trainingCompletedProperties** (object)
        - **contentDateTime** (string)
        - **ipAddress** (string)
        - **osPlatformDeviceDetails** (string)
        - **browser** (string)
        - **potentialScoreImpact** (number)
    - **assignedTrainingsCount** (number)
    - **completedTrainingsCount** (number)
    - **inProgressTrainingsCount** (number)
    - **reportedPhishDateTime** (string)
    - **simulationUser** (object)
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