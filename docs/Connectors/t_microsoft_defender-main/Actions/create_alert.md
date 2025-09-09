# Create Alert

**Description**: Creates a new alert in Microsoft Defender with details such as machine ID, severity, and event time to identify potential threats.

## Endpoint

- **URL:** `/api/alerts/CreateAlertByReference`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **machineId** (string) – Required: Id of the device on which the event was identified.
  - **severity** (string) – Required: Severity of the alert.
  - **title** (string) – Required: Title for the alert.
  - **description** (string) – Required: Description of the alert.
  - **recommendedAction** (string) – Required: Security officer needs to take this action when analyzing the alert.
  - **eventTime** (string) – Required: The precise time of the event as string, as obtained from advanced hunting.
  - **reportId** (string) – Required: The reportId of the event, as obtained from advanced hunting.
  - **category** (string) – Required: Category of the alert.
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
      "Date": "Tue, 30 Apr 2024 10:36:47 GMT"
    },
    "reason": "OK",
    "json_body": {
      "id": "da637472900382838869_1364969609",
      "incidentId": 1126093,
      "investigationId": null,
      "assignedTo": null,
      "severity": "Low",
      "status": "New",
      "classification": null,
      "determination": null,
      "investigationState": "Queued",
      "detectionSource": "WindowsDefenderAtp",
      "detectorId": "17e10bbc-3a68-474a-8aad-faef14d43952",
      "category": "Execution",
      "threatFamilyName": null,
      "title": "Low-reputation arbitrary code executed by signed executable",
      "description": "Binaries signed by Microsoft can be used to run low-reputation arbitrary code. This technique hides the execution of malicious code within a trusted process. As a result, the trusted process might exhibit suspicious behaviors, such as opening a listening port or connecting to a command-and-control (C&C) server.",
      "alertCreationTime": "2021-01-26T20:33:57.7220239Z",
      "firstEventTime": "2021-01-26T20:31:32.9562661Z",
      "lastEventTime": "2021-01-26T20:31:33.0577322Z",
      "lastUpdateTime": "2021-01-26T20:33:59.2Z",
      "resolvedTime": null,
      "machineId": "111e6dd8c833c8a052ea231ec1b19adaf497b625",
      "computerDnsName": "temp123.middleeast.corp.microsoft.com",
      "rbacGroupName": "A",
      "aadTenantId": "a839b112-1253-6432-9bf6-94542403f21c",
      "threatName": null,
      "mitreTechniques": [
        "T1064",
        "T1085",
        "T1220"
      ],
      "relatedUser": {
        "userName": "temp123",
        "domainName": "DOMAIN"
      },
      "comments": [
        {
          "comment": "test comment for docs",
          "createdBy": "secop123@contoso.com",
          "createdTime": "2021-01-26T01:00:37.8404534Z"
        }
      ],
      "evidence": [
        {
          "entityType": "User",
          "evidenceCreationTime": "2021-01-26T20:33:58.42Z",
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
          "accountName": "name",
          "domainName": "DOMAIN",
          "userSid": "S-1-5-21-11111607-1111760036-109187956-75141",
          "aadUserId": "11118379-2a59-1111-ac3c-a51eb4a3c627",
          "userPrincipalName": "temp123@microsoft.com",
          "detectionStatus": null
        },
        {
          "entityType": "Process",
          "evidenceCreationTime": "2021-01-26T20:33:58.6133333Z",
          "sha1": "ff836cfb1af40252bd2a2ea843032e99a5b262ed",
          "sha256": "a4752c71d81afd3d5865d24ddb11a6b0c615062fcc448d24050c2172d2cbccd6",
          "fileName": "rundll32.exe",
          "filePath": "C:\\Windows\\SysWOW64",
          "processId": 3276,
          "processCommandLine": "rundll32.exe  c:\\temp\\suspicious.dll,RepeatAfterMe",
          "processCreationTime": "2021-01-26T20:31:32.9581596Z",
          "parentProcessId": 8420,
          "parentProcessCreationTime": "2021-01-26T20:31:32.9004163Z",
          "parentProcessFileName": "rundll32.exe",
          "parentProcessFilePath": "C:\\Windows\\System32",
          "ipAddress": null,
          "url": null,
          "registryKey": null,
          "registryHive": null,
          "registryValueType": null,
          "registryValue": null,
          "accountName": null,
          "domainName": null,
          "userSid": null,
          "aadUserId": null,
          "userPrincipalName": null,
          "detectionStatus": "Detected"
        },
        {
          "entityType": "File",
          "evidenceCreationTime": "2021-01-26T20:33:58.42Z",
          "sha1": "8563f95b2f8a284fc99da44500cd51a77c1ff36c",
          "sha256": "dc0ade0c95d6db98882bc8fa6707e64353cd6f7767ff48d6a81a6c2aef21c608",
          "fileName": "suspicious.dll",
          "filePath": "c:\\temp",
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
          "accountName": null,
          "domainName": null,
          "userSid": null,
          "aadUserId": null,
          "userPrincipalName": null,
          "detectionStatus": "Detected"
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
  - **id** (string)
  - **incidentId** (number)
  - **investigationId** (object)
  - **assignedTo** (object)
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
  - **resolvedTime** (object)
  - **machineId** (string)
  - **computerDnsName** (string)
  - **rbacGroupName** (string)
  - **aadTenantId** (string)
  - **threatName** (object)
  - **mitreTechniques** (array)
  - **relatedUser** (object)
    - **userName** (string)
    - **domainName** (string)
  - **comments** (array)
    - **comment** (string)
    - **createdBy** (string)
    - **createdTime** (string)
  - **evidence** (array)
    - **entityType** (string)
    - **evidenceCreationTime** (string)
    - **sha1** (string)
    - **sha256** (string)
    - **fileName** (string)
    - **filePath** (string)
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
    - **accountName** (object)
    - **domainName** (object)
    - **userSid** (object)
    - **aadUserId** (object)
    - **userPrincipalName** (object)
    - **detectionStatus** (string)
## Response Headers

| Header | Type |
|--------|------|
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| Date | string |