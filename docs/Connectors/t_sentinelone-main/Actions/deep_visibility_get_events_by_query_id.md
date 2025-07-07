# Deep Visibility Get Events By Query ID

**Description**: Retrieves all Deep Visibility events associated with a given queryId in SentinelOne after an 'init-query' operation.

## Endpoint

- **URL:** `web/api/v2.1/dv/events`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **queryId** (string) – Required
  - **limit** (number)
  - **sortOrder** (string)
  - **cursor** (string): Cursor position returned by the last request. Should be used instead of skip. cursor currently supports sort by with createdAt, pid, processStartTime.
  - **skip** (string): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **sortby** (string): Events sorted by field.
  - **subquery** (string): Create a sub query to run on the data that was already pulled.
## Output

### Example

```json
[
  {
    "status_code": 400,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 20:00:44 GMT",
      "Content-Type": "application/json",
      "Content-Length": "97",
      "Connection": "keep-alive",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'"
    },
    "reason": "BAD REQUEST",
    "json_body": {
      "data": [
        {
          "networkMethod": "string",
          "indicatorCategory": "string",
          "agentVersion": "string",
          "agentUuid": "string",
          "createdAt": "2018-02-27T04:49:26.257525Z",
          "agentMachineType": "string",
          "forensicUrl": "string",
          "fileSize": "string",
          "parentProcessUniqueKey": "string",
          "fileType": "string",
          "taskPath": "string",
          "oldFileMd5": "string",
          "fileMd5": "string",
          "trueContext": "string",
          "verifiedStatus": "string",
          "processIsRedirectedCommandProcessor": "string",
          "agentIsDecommissioned": true,
          "oldFileName": "string",
          "indicatorMetadata": "string",
          "dstIp": "string",
          "parentProcessName": "string",
          "processImagePath": "string",
          "sha1": "string",
          "srcProcDownloadToken": "string",
          "parentProcessIsMalicious": true,
          "registryId": "string",
          "processSubSystem": "string",
          "fileFullName": "string",
          "indicatorName": "string",
          "fileSha256": "string",
          "rpid": "string",
          "fileId": "string",
          "indicatorDescription": "string",
          "processName": "string",
          "agentInfected": true,
          "srcIp": "string",
          "direction": "string",
          "eventType": "string",
          "processUniqueKey": "string",
          "parentPid": "string",
          "agentDomain": "string",
          "processCmd": "string",
          "srcPort": 0,
          "agentName": "string",
          "registryPath": "string",
          "networkSource": "string",
          "connectionStatus": "string",
          "processIsWow64": "string",
          "agentIsActive": true,
          "agentGroupId": "string",
          "dnsRequest": "string",
          "processIntegrityLevel": "string",
          "agentIp": "string",
          "isAgentVersionFullySupportedForPg": true,
          "processUserName": "string",
          "parentProcessGroupId": "string",
          "oldFileSha256": "string",
          "isAgentVersionFullySupportedForPgMessage": "string",
          "threatStatus": "string",
          "siteName": "string",
          "loginsBaseType": "string",
          "processDisplayName": "string",
          "parentProcessStartTime": "string",
          "taskName": "string",
          "fileSha1": "string",
          "processStartTime": "string",
          "pid": "string",
          "md5": "string",
          "dnsResponse": "string",
          "sha256": "string",
          "objectType": "string",
          "dstPort": 0,
          "networkUrl": "string",
          "publisher": "string",
          "processImageSha1Hash": "string",
          "loginsUserName": "string",
          "processSessionId": "string",
          "signedStatus": "string",
          "processRoot": "string",
          "processGroupId": "string",
          "oldFileSha1": "string",
          "agentOs": "windows_legacy",
          "tid": "string",
          "user": "string",
          "agentNetworkStatus": "string",
          "id": "string",
          "relatedToThreat": "string",
          "processIsMalicious": true,
          "signatureSignedInvalidReason": "string",
          "agentId": "string"
        }
      ],
      "pagination": {
        "totalItems": 580,
        "nextCursor": "YWdlbnRfaWQ6NTgwMjkzODE="
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
    - **networkMethod** (string)
    - **indicatorCategory** (string)
    - **agentVersion** (string)
    - **agentUuid** (string)
    - **createdAt** (string)
    - **agentMachineType** (string)
    - **forensicUrl** (string)
    - **fileSize** (string)
    - **parentProcessUniqueKey** (string)
    - **fileType** (string)
    - **taskPath** (string)
    - **oldFileMd5** (string)
    - **fileMd5** (string)
    - **trueContext** (string)
    - **verifiedStatus** (string)
    - **processIsRedirectedCommandProcessor** (string)
    - **agentIsDecommissioned** (boolean)
    - **oldFileName** (string)
    - **indicatorMetadata** (string)
    - **dstIp** (string)
    - **parentProcessName** (string)
    - **processImagePath** (string)
    - **sha1** (string)
    - **srcProcDownloadToken** (string)
    - **parentProcessIsMalicious** (boolean)
    - **registryId** (string)
    - **processSubSystem** (string)
    - **fileFullName** (string)
    - **indicatorName** (string)
    - **fileSha256** (string)
    - **rpid** (string)
    - **fileId** (string)
    - **indicatorDescription** (string)
    - **processName** (string)
    - **agentInfected** (boolean)
    - **srcIp** (string)
    - **direction** (string)
    - **eventType** (string)
    - **processUniqueKey** (string)
    - **parentPid** (string)
    - **agentDomain** (string)
    - **processCmd** (string)
    - **srcPort** (number)
    - **agentName** (string)
    - **registryPath** (string)
    - **networkSource** (string)
    - **connectionStatus** (string)
    - **processIsWow64** (string)
    - **agentIsActive** (boolean)
    - **agentGroupId** (string)
    - **dnsRequest** (string)
    - **processIntegrityLevel** (string)
    - **agentIp** (string)
    - **isAgentVersionFullySupportedForPg** (boolean)
    - **processUserName** (string)
    - **parentProcessGroupId** (string)
    - **oldFileSha256** (string)
    - **isAgentVersionFullySupportedForPgMessage** (string)
    - **threatStatus** (string)
    - **siteName** (string)
    - **loginsBaseType** (string)
    - **processDisplayName** (string)
    - **parentProcessStartTime** (string)
    - **taskName** (string)
    - **fileSha1** (string)
    - **processStartTime** (string)
    - **pid** (string)
    - **md5** (string)
    - **dnsResponse** (string)
    - **sha256** (string)
    - **objectType** (string)
    - **dstPort** (number)
    - **networkUrl** (string)
    - **publisher** (string)
    - **processImageSha1Hash** (string)
    - **loginsUserName** (string)
    - **processSessionId** (string)
    - **signedStatus** (string)
    - **processRoot** (string)
    - **processGroupId** (string)
    - **oldFileSha1** (string)
    - **agentOs** (string)
    - **tid** (string)
    - **user** (string)
    - **agentNetworkStatus** (string)
    - **id** (string)
    - **relatedToThreat** (string)
    - **processIsMalicious** (boolean)
    - **signatureSignedInvalidReason** (string)
    - **agentId** (string)
  - **pagination** (object)
    - **totalItems** (number)
    - **nextCursor** (string)
## Response Headers

| Header | Type |
|--------|------|
| Server | string |
| Date | string |
| Content-Type | string |
| Content-Length | string |
| Connection | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |