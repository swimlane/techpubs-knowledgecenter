# Get Incident

**Description**: Retrieve a specific Microsoft Defender incident by its unique ID, using the incident's ID as a path parameter.

## Endpoint

- **URL:** `api/incidents/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: Incident ID
## Output

### Example

```json
[
  {
    "@odata.context": "https://api.security.microsoft.com/api/$metadata#Incidents/$entity",
    "incidentId": 437,
    "incidentUri": "https://security.microsoft.com/incidents/437?tid=f5d73c4c-bb3d-421b-8bee-424916a4acca",
    "redirectIncidentId": null,
    "incidentName": "Unfamiliar sign-in properties involving one user",
    "createdTime": "2023-05-10T09:33:15.32Z",
    "lastUpdateTime": "2023-05-10T09:33:15.53Z",
    "assignedTo": null,
    "classification": "Unknown",
    "determination": "NotAvailable",
    "status": "Active",
    "severity": "High",
    "tags": [],
    "comments": [],
    "alerts": [
      {
        "alertId": "ad3ef58dc561c3234527be2d9ff82524a967a5fb1c",
        "providerAlertId": "039e0aead168175b4945b6eb116391f45e0701ea8777529e1b9bce5992760803",
        "incidentId": 437,
        "serviceSource": "AADIdentityProtection",
        "creationTime": "2023-05-10T09:33:14.6226578Z",
        "lastUpdatedTime": "2023-05-10T09:33:16.1033333Z",
        "resolvedTime": null,
        "firstActivity": "2023-05-10T09:29:24.2969531Z",
        "lastActivity": "2023-05-10T09:29:24.2969531Z",
        "title": "Unfamiliar sign-in properties",
        "description": "The following properties of this sign-in are unfamiliar for the given user: ASN, Browser, Device, IP, Location, EASId, TenantIPsubnet",
        "category": "InitialAccess",
        "status": "New",
        "severity": "High",
        "investigationId": null,
        "investigationState": "UnsupportedAlertType",
        "classification": null,
        "determination": null,
        "detectionSource": "AAD",
        "detectorId": "UnfamiliarLocation",
        "assignedTo": null,
        "actorName": null,
        "threatFamilyName": null,
        "mitreTechniques": [
          "T1078",
          "T1078.004"
        ],
        "devices": [],
        "entities": [
          {
            "entityType": "User",
            "evidenceCreationTime": "2023-05-10T09:33:14.89Z",
            "verdict": "Suspicious",
            "remediationStatus": "None",
            "accountName": "pov",
            "userSid": "S-1-12-1-1510799150-1340649529-3182594751-1539246002",
            "aadUserId": "5a0cf72e-b039-4fe8-bf8a-b2bdb207bf5b",
            "userPrincipalName": "pov@swimlaneintegrations.onmicrosoft.com"
          },
          {
            "entityType": "Ip",
            "evidenceCreationTime": "2023-05-10T09:33:14.89Z",
            "verdict": "Suspicious",
            "remediationStatus": "None",
            "ipAddress": "93.243.188.4"
          }
        ]
      }
    ]
  }
]
```
### Output Parameters

- **@odata.context** (string)
- **incidentId** (number)
- **incidentUri** (string)
- **redirectIncidentId** (object)
- **incidentName** (string)
- **createdTime** (string)
- **lastUpdateTime** (string)
- **assignedTo** (object)
- **classification** (string)
- **determination** (string)
- **status** (string)
- **severity** (string)
- **tags** (array)
  - **file_name** (string) – Required
  - **file** (string) – Required
- **comments** (array)
  - **file_name** (string) – Required
  - **file** (string) – Required
- **alerts** (array)
  - **alertId** (string)
  - **providerAlertId** (string)
  - **incidentId** (number)
  - **serviceSource** (string)
  - **creationTime** (string)
  - **lastUpdatedTime** (string)
  - **resolvedTime** (object)
  - **firstActivity** (string)
  - **lastActivity** (string)
  - **title** (string)
  - **description** (string)
  - **category** (string)
  - **status** (string)
  - **severity** (string)
  - **investigationId** (object)
  - **investigationState** (string)
  - **classification** (object)
  - **determination** (object)
  - **detectionSource** (string)
  - **detectorId** (string)
  - **assignedTo** (object)
  - **actorName** (object)
  - **threatFamilyName** (object)
  - **mitreTechniques** (array)
  - **devices** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **entities** (array)
    - **entityType** (string)
    - **evidenceCreationTime** (string)
    - **verdict** (string)
    - **remediationStatus** (string)
    - **accountName** (string)
    - **userSid** (string)
    - **aadUserId** (string)
    - **userPrincipalName** (string)
    - **ipAddress** (string)