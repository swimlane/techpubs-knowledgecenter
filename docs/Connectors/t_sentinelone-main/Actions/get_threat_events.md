# Get Threat Events

**Description**: Retrieve all threat events associated with a given 'threat_id' in SentinelOne for focused incident analysis.

## Endpoint

- **URL:** `/web/api/v2.1/threats/{{threat_id}}/explore/events`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required
- **parameters** (object)
  - **eventId** (string)
  - **sortBy** (string)
  - **limit** (number)
  - **skip** (number)
  - **sortOrder** (string)
  - **skipCount** (boolean)
  - **countOnly** (boolean)
  - **cursor** (string)
  - **eventSubTypes** (array)
  - **processName__like** (string)
  - **eventTypes** (array)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Tue, 06 Dec 2022 20:12:03 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "19f65f98-24e9-42e2-b9bc-d1c075019219",
      "Access-Control-Allow-Origin": "https://usea1-attivo.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": [
        {
          "activeContentFileId": null,
          "activeContentHash": null,
          "activeContentPath": null,
          "agentDomain": "",
          "agentGroupId": "1286405255265411734",
          "agentId": "1286438987267469377",
          "agentInfected": true,
          "agentIp": "96.79.235.37",
          "agentIsActive": true,
          "agentIsDecommissioned": false,
          "agentMachineType": "server",
          "agentName": "localhost.localdomain",
          "agentNetworkStatus": "disconnected",
          "agentOs": "linux",
          "agentUuid": "33b3a892-d388-d3e6-6ead-a98acb5d054c",
          "agentVersion": "21.10.1.6",
          "connectionStatus": null,
          "createdAt": "2021-12-14T20:23:45.999000Z",
          "direction": null,
          "dnsRequest": null,
          "dnsResponse": null,
          "dstIp": null,
          "dstPort": null,
          "eventType": "Process Creation",
          "fileFullName": null,
          "fileId": null,
          "fileMd5": null,
          "fileSha1": "3395856ce81f2b7382dee72602f798b642f14140",
          "fileSha256": null,
          "fileSize": null,
          "fileType": null,
          "hasActiveContent": null,
          "id": "1569749506546751259",
          "indicatorCategory": null,
          "indicatorDescription": null,
          "indicatorMetadata": null,
          "indicatorName": null,
          "loginsBaseType": null,
          "loginsUserName": null,
          "md5": null,
          "networkMethod": null,
          "networkSource": null,
          "networkUrl": null,
          "objectType": "process",
          "oldFileMd5": null,
          "oldFileName": null,
          "oldFileSha1": null,
          "oldFileSha256": null,
          "parentPid": null,
          "parentProcessName": null,
          "parentProcessUniqueKey": null,
          "pid": "22566",
          "processCmd": null,
          "processDisplayName": "scp",
          "processGroupId": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "processImagePath": null,
          "processImageSha1Hash": "3395856ce81f2b7382dee72602f798b642f14140",
          "processIntegrityLevel": null,
          "processIsRedirectedCommandProcessor": null,
          "processIsWow64": null,
          "processName": "scp",
          "processRoot": "True",
          "processSessionId": null,
          "processStartTime": null,
          "processSubSystem": null,
          "processUniqueKey": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9_22566",
          "processUserName": null,
          "protocol": null,
          "publisher": null,
          "registryClassification": null,
          "registryId": null,
          "registryPath": null,
          "relatedToThreat": false,
          "rpid": null,
          "sha1": "3395856ce81f2b7382dee72602f798b642f14140",
          "sha256": null,
          "signatureSignedInvalidReason": null,
          "signedStatus": null,
          "siteName": "Default site",
          "srcIp": null,
          "srcPort": null,
          "storyline": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "taskName": null,
          "taskPath": null,
          "threatStatus": null,
          "tid": null,
          "trueContext": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "user": null,
          "verifiedStatus": null
        },
        {
          "activeContentFileId": null,
          "activeContentHash": null,
          "activeContentPath": null,
          "agentDomain": "",
          "agentGroupId": "1286405255265411734",
          "agentId": "1286438987267469377",
          "agentInfected": true,
          "agentIp": "96.79.235.37",
          "agentIsActive": true,
          "agentIsDecommissioned": false,
          "agentMachineType": "server",
          "agentName": "localhost.localdomain",
          "agentNetworkStatus": "disconnected",
          "agentOs": "linux",
          "agentUuid": "33b3a892-d388-d3e6-6ead-a98acb5d054c",
          "agentVersion": "21.10.1.6",
          "connectionStatus": null,
          "createdAt": "2021-12-14T20:23:46Z",
          "direction": null,
          "dnsRequest": null,
          "dnsResponse": null,
          "dstIp": null,
          "dstPort": null,
          "eventType": "File Creation",
          "fileFullName": "/home/swimlane-host/eicar.com",
          "fileId": "110885_fanotify",
          "fileMd5": null,
          "fileSha1": "3395856ce81f2b7382dee72602f798b642f14140",
          "fileSha256": null,
          "fileSize": null,
          "fileType": "",
          "hasActiveContent": null,
          "id": "1569749506538362650",
          "indicatorCategory": null,
          "indicatorDescription": null,
          "indicatorMetadata": null,
          "indicatorName": null,
          "loginsBaseType": null,
          "loginsUserName": null,
          "md5": null,
          "networkMethod": null,
          "networkSource": null,
          "networkUrl": null,
          "objectType": "file",
          "oldFileMd5": null,
          "oldFileName": null,
          "oldFileSha1": null,
          "oldFileSha256": null,
          "parentPid": null,
          "parentProcessName": null,
          "parentProcessUniqueKey": null,
          "pid": "22566",
          "processCmd": null,
          "processDisplayName": "scp",
          "processGroupId": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "processImagePath": null,
          "processImageSha1Hash": "3395856ce81f2b7382dee72602f798b642f14140",
          "processIntegrityLevel": null,
          "processIsRedirectedCommandProcessor": null,
          "processIsWow64": null,
          "processName": "scp",
          "processRoot": null,
          "processSessionId": null,
          "processStartTime": null,
          "processSubSystem": null,
          "processUniqueKey": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9_22566",
          "processUserName": null,
          "protocol": null,
          "publisher": null,
          "registryClassification": null,
          "registryId": null,
          "registryPath": null,
          "relatedToThreat": false,
          "rpid": null,
          "sha1": "3395856ce81f2b7382dee72602f798b642f14140",
          "sha256": null,
          "signatureSignedInvalidReason": null,
          "signedStatus": null,
          "siteName": "Default site",
          "srcIp": null,
          "srcPort": null,
          "storyline": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "taskName": null,
          "taskPath": null,
          "threatStatus": null,
          "tid": null,
          "trueContext": "da7e026e-d34d-87c7-e3fa-4f67b761e4c9",
          "user": null,
          "verifiedStatus": ""
        }
      ],
      "pagination": {
        "nextCursor": null,
        "totalItems": 2
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **activeContentFileId** (object)
    - **activeContentHash** (object)
    - **activeContentPath** (object)
    - **agentDomain** (string)
    - **agentGroupId** (string)
    - **agentId** (string)
    - **agentInfected** (boolean)
    - **agentIp** (string)
    - **agentIsActive** (boolean)
    - **agentIsDecommissioned** (boolean)
    - **agentMachineType** (string)
    - **agentName** (string)
    - **agentNetworkStatus** (string)
    - **agentOs** (string)
    - **agentUuid** (string)
    - **agentVersion** (string)
    - **connectionStatus** (object)
    - **createdAt** (string)
    - **direction** (object)
    - **dnsRequest** (object)
    - **dnsResponse** (object)
    - **dstIp** (object)
    - **dstPort** (object)
    - **eventType** (string)
    - **fileFullName** (string)
    - **fileId** (string)
    - **fileMd5** (object)
    - **fileSha1** (string)
    - **fileSha256** (object)
    - **fileSize** (object)
    - **fileType** (string)
    - **hasActiveContent** (object)
    - **id** (string)
    - **indicatorCategory** (object)
    - **indicatorDescription** (object)
    - **indicatorMetadata** (object)
    - **indicatorName** (object)
    - **loginsBaseType** (object)
    - **loginsUserName** (object)
    - **md5** (object)
    - **networkMethod** (object)
    - **networkSource** (object)
    - **networkUrl** (object)
    - **objectType** (string)
    - **oldFileMd5** (object)
    - **oldFileName** (object)
    - **oldFileSha1** (object)
    - **oldFileSha256** (object)
    - **parentPid** (object)
    - **parentProcessName** (object)
    - **parentProcessUniqueKey** (object)
    - **pid** (string)
    - **processCmd** (object)
    - **processDisplayName** (string)
    - **processGroupId** (string)
    - **processImagePath** (object)
    - **processImageSha1Hash** (string)
    - **processIntegrityLevel** (object)
    - **processIsRedirectedCommandProcessor** (object)
    - **processIsWow64** (object)
    - **processName** (string)
    - **processRoot** (object)
    - **processSessionId** (object)
    - **processStartTime** (object)
    - **processSubSystem** (object)
    - **processUniqueKey** (string)
    - **processUserName** (object)
    - **protocol** (object)
    - **publisher** (object)
    - **registryClassification** (object)
    - **registryId** (object)
    - **registryPath** (object)
    - **relatedToThreat** (boolean)
    - **rpid** (object)
    - **sha1** (string)
    - **sha256** (object)
    - **signatureSignedInvalidReason** (object)
    - **signedStatus** (object)
    - **siteName** (string)
    - **srcIp** (object)
    - **srcPort** (object)
    - **storyline** (string)
    - **taskName** (object)
    - **taskPath** (object)
    - **threatStatus** (object)
    - **tid** (object)
    - **trueContext** (string)
    - **user** (object)
    - **verifiedStatus** (string)
  - **pagination** (object)
    - **nextCursor** (object)
    - **totalItems** (number)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| X-RQID | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| Content-Encoding | string |