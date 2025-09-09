# Get Alert

**Description**: Retrieves detailed information for a specified alert in Microsoft Defender using the unique alert ID.

## Endpoint

- **URL:** `/api/alerts/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Thu, 04 May 2023 13:05:30 GMT",
      "Content-Type": "application/json; odata.metadata=minimal; odata.streaming=true; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "Content-Encoding": "deflate",
      "Vary": "Accept-Encoding",
      "OData-Version": "4.0",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#Alerts/$entity",
      "id": "ar638180599315648136_73827727",
      "incidentId": 400,
      "investigationId": 6,
      "assignedTo": "API Action",
      "severity": "Informational",
      "status": "Resolved",
      "classification": null,
      "determination": null,
      "investigationState": "Benign",
      "detectionSource": "AutomatedInvestigation",
      "detectorId": "5c6b7d86-c91f-4f8c-8aec-9d2086f46527",
      "category": "SuspiciousActivity",
      "threatFamilyName": null,
      "title": "Automated investigation started manually",
      "description": "SE POV User(pov@swimlaneintegrations.onmicrosoft.com) initiated an Automated investigation on se-pov-desktop.\n    The investigation automatically identifies and reviews threat artifacts for possible remediation.",
      "alertCreationTime": "2023-04-25T22:52:11.5648315Z",
      "firstEventTime": "2023-04-25T22:52:11Z",
      "lastEventTime": "2023-04-25T22:52:11Z",
      "lastUpdateTime": "2023-04-25T22:58:00.55Z",
      "resolvedTime": "2023-04-25T22:58:00.4108067Z",
      "machineId": "556b3952acb0bff29816d267822305781cc183ec",
      "computerDnsName": "se-pov-desktop",
      "rbacGroupName": null,
      "aadTenantId": "f5d73c4c-bb3d-421b-8bee-424916a4acca",
      "threatName": null,
      "mitreTechniques": [],
      "relatedUser": null,
      "loggedOnUsers": [
        {
          "accountName": "Chris Phillips",
          "domainName": "SE-POV-DESKTOP"
        }
      ],
      "comments": [],
      "evidence": [
        {
          "entityType": "Ip",
          "evidenceCreationTime": "2023-04-25T22:52:11.7733333Z",
          "sha1": null,
          "sha256": null,
          "fileName": null,
          "filePath": null,
          "processId": null,
          "processCommandLine": null,
          "processCreationTime": null,
          "parentProcessId": null,
          "parentProcessCreationTime": null,
          "parentProcessFileName": null,
          "parentProcessFilePath": null,
          "ipAddress": null,
          "url": null,
          "registryKey": null,
          "registryHive": null,
          "registryValueType": null,
          "registryValue": null,
          "registryValueName": null,
          "accountName": null,
          "domainName": null,
          "userSid": null,
          "aadUserId": null,
          "userPrincipalName": null,
          "detectionStatus": null
        }
      ],
      "domains": []
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **id** (string)
  - **incidentId** (number)
  - **investigationId** (number)
  - **assignedTo** (string)
  - **severity** (string)
  - **status** (string)
  - **classification** (object)
  - **determination** (object)
  - **investigationState** (string)
  - **detectionSource** (string)
  - **detectorId** (string)
  - **category** (string)
  - **threatFamilyName** (object)
  - **title** (string)
  - **description** (string)
  - **alertCreationTime** (string)
  - **firstEventTime** (string)
  - **lastEventTime** (string)
  - **lastUpdateTime** (string)
  - **resolvedTime** (string)
  - **machineId** (string)
  - **computerDnsName** (string)
  - **rbacGroupName** (object)
  - **aadTenantId** (string)
  - **threatName** (object)
  - **mitreTechniques** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **relatedUser** (object)
  - **loggedOnUsers** (array)
    - **accountName** (string)
    - **domainName** (string)
  - **comments** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **evidence** (array)
    - **entityType** (string)
    - **evidenceCreationTime** (string)
    - **sha1** (object)
    - **sha256** (object)
    - **fileName** (object)
    - **filePath** (object)
    - **processId** (object)
    - **processCommandLine** (object)
    - **processCreationTime** (object)
    - **parentProcessId** (object)
    - **parentProcessCreationTime** (object)
    - **parentProcessFileName** (object)
    - **parentProcessFilePath** (object)
    - **ipAddress** (object)
    - **url** (object)
    - **registryKey** (object)
    - **registryHive** (object)
    - **registryValueType** (object)
    - **registryValue** (object)
    - **registryValueName** (object)
    - **accountName** (object)
    - **domainName** (object)
    - **userSid** (object)
    - **aadUserId** (object)
    - **userPrincipalName** (object)
    - **detectionStatus** (object)
  - **domains** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
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