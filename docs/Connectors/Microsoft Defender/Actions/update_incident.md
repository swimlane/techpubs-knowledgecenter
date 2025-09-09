# Update Incident by ID

**Description**: Updates an existing incident's details in Microsoft Defender, including status, determination, and classification, using the incident ID.

## Endpoint

- **URL:** `api/incidents/{{id}}`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **id** (number) – Required: Incident ID.
- **json_body** (object) – Required
  - **status** (string): Specifies the current status of the incident.
  - **assignedTo** (string): Owner of the incident.
  - **classification** (string): Specification of the incident.
  - **determination** (string): Specifies the determination of the incident.
  - **tags** (array): List of Incident tags.
  - **comment** (string): Comment to be added to the incident.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 05 Sep 2024 07:20:44 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Incidents/$entity",
      "incidentId": 552,
      "incidentUri": "https://security.microsoft.com/incidents/552?tid=f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "redirectIncidentId": null,
      "incidentName": "Email messages containing malicious file removed after delivery\u200b",
      "createdTime": "2024-08-30T08:55:32.21Z",
      "lastUpdateTime": "2024-09-05T07:20:44.9089383Z",
      "assignedTo": null,
      "classification": "Unknown",
      "determination": "NotAvailable",
      "status": "Resolved",
      "severity": "Informational",
      "tags": [],
      "comments": [],
      "alerts": [
        {
          "alertId": "fa54978fd8-0fca-bf7d-7200-08dcc8d0df02",
          "providerAlertId": "54978fd8-0fca-bf7d-7200-08dcc8d0df02",
          "incidentId": 552,
          "serviceSource": "MicrosoftDefenderForOffice365",
          "creationTime": "2024-08-30T08:55:31.9566667Z",
          "lastUpdatedTime": "2024-08-30T23:49:40.49Z",
          "resolvedTime": null,
          "firstActivity": "2024-08-30T08:50:19Z",
          "lastActivity": "2024-08-30T08:52:19Z",
          "title": "Email messages containing malicious file removed after delivery\u200b",
          "description": "Emails with malicious file that were delivered and later removed -V1.0.0.3",
          "category": "InitialAccess",
          "status": "InProgress",
          "severity": "Informational",
          "investigationId": null,
          "investigationState": "PendingApproval",
          "classification": null,
          "determination": null,
          "detectionSource": "OfficeATP",
          "detectorId": "4b1820ec-39dc-45f3-abf6-5ee80df51fd2",
          "assignedTo": null,
          "actorName": null,
          "threatFamilyName": null,
          "mitreTechniques": [
            "T1566.001"
          ],
          "devices": [],
          "entities": [
            {
              "entityType": "Mailbox",
              "evidenceCreationTime": "2024-08-30T08:55:32.2433333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "accountName": "pov",
              "userSid": "S-1-12-1-1510799150-1340649529-3182594751-1539246002",
              "aadUserId": "5a0cf72e-b039-4fe8-bf8a-b2bdb207bf5b",
              "userPrincipalName": "pov@swimlaneintegrations.onmicrosoft.com",
              "mailboxDisplayName": "SE  POV User",
              "mailboxAddress": "pov@swimlaneintegrations.onmicrosoft.com"
            },
            {
              "entityType": "File",
              "evidenceCreationTime": "2024-08-30T08:55:32.2433333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "sha256": "2a1a921bcd5bd4795f1204ce050bc7c1054273ffc87de9ec00c3949b8bdbce5c",
              "fileName": "2020-01-24-Ursnif-ma"
            },
            {
              "entityType": "MailMessage",
              "evidenceCreationTime": "2024-08-30T08:55:32.2433333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "userPrincipalName": "pov@swimlaneintegrations.onmicrosoft.com",
              "sender": "pov@swimlane.ai",
              "recipient": "pov@swimlaneintegrations.onmicrosoft.com",
              "subject": "WARNINGIs this a Phishing Email?",
              "internetMessageId": "<PH0PR19MB562398F6FB70809E1487FB7FB3972@PH0PR19MB5623.namprd19.prod.outlook.com>",
              "deliveryAction": "Blocked"
            },
            {
              "entityType": "User",
              "evidenceCreationTime": "2024-08-30T08:55:32.2433333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "accountName": "pov",
              "domainName": "",
              "userSid": "S-1-12-1-1510799150-1340649529-3182594751-1539246002",
              "aadUserId": "5a0cf72e-b039-4fe8-bf8a-b2bdb207bf5b",
              "userPrincipalName": "pov@swimlaneintegrations.onmicrosoft.com"
            },
            {
              "entityType": "File",
              "evidenceCreationTime": "2024-08-30T09:00:35.9533333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "sha256": "2a1a921bcd5bd4795f1204ce050bc7c1054273ffc87de9ec00c3949b8bdbce5c",
              "fileName": "2020-01-24-Ursnif-malspam-example-2-of-4-0750-UTC.eml"
            },
            {
              "entityType": "MailCluster",
              "evidenceCreationTime": "2024-08-30T09:05:50.2133333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "clusterBy": "Subject;SenderIp;AntispamDirection;ContentType",
              "clusterByValue": "WARNINGIs this a Phishing Email?;40.107.95.100;1;1",
              "emailCount": 1
            },
            {
              "entityType": "MailCluster",
              "evidenceCreationTime": "2024-08-30T09:05:50.2133333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "clusterBy": "Subject;P2SenderDomain;AntispamDirection;ContentType",
              "clusterByValue": "WARNINGIs this a Phishing Email?;swimlane.ai;1;1",
              "emailCount": 346
            },
            {
              "entityType": "MailCluster",
              "evidenceCreationTime": "2024-08-30T09:05:50.2133333Z",
              "verdict": "Suspicious",
              "remediationStatus": "None",
              "clusterBy": "FileHash;ContentType",
              "clusterByValue": "2A1A921BCD5BD4795F1204CE050BC7C1054273FFC87DE9EC00C3949B8BDBCE5C;1",
              "emailCount": 6
            }
          ]
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
      - **mailboxDisplayName** (string)
      - **mailboxAddress** (string)
      - **sha256** (string)
      - **fileName** (string)
      - **sender** (string)
      - **recipient** (string)
      - **subject** (string)
      - **internetMessageId** (string)
      - **deliveryAction** (string)
      - **domainName** (string)
      - **clusterBy** (string)
      - **clusterByValue** (string)
      - **emailCount** (number)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| Content-Encoding | string |
| Vary | string |
| OData-Version | string |
| Strict-Transport-Security | string |