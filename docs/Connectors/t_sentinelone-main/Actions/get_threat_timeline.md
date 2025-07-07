# Get Threat Timeline

**Description**: Retrieve a detailed timeline for a specific threat in SentinelOne using the provided unique threat ID.

## Endpoint

- **URL:** `web/api/v2.1/threats/{{threat_id}}/timeline`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required
- **parameters** (object)
  - **sortOrder** (string)
  - **skipCount** (boolean)
  - **activityTypes** (number)
  - **sortBy** (string)
  - **countOnly** (boolean)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 14 Nov 2022 22:05:11 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "2a863e30-2f72-4519-9162-4e198dcb768d",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
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
          "accountId": "1286405255240245908",
          "activityType": 4003,
          "agentId": "1286438987267469377",
          "agentUpdatedVersion": null,
          "createdAt": "2022-09-07T02:38:56.730789Z",
          "data": {
            "accountName": "swimlane",
            "computerName": "localhost.localdomain",
            "confidenceLevel": "suspicious",
            "escapedMaliciousProcessArguments": null,
            "fileContentHash": "b691598c45658e76b2c328275db988baed3b8689",
            "fileDisplayName": "wildfire-test-pe-file(1).exe",
            "filePath": "/home/swimlane-host/wildfire-test-pe-file(1).exe",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "siteName": "Default site",
            "threatClassification": "Malware",
            "threatClassificationSource": "Engine",
            "username": null
          },
          "groupId": "1286405255265411734",
          "hash": null,
          "id": "1503989642143092180",
          "osFamily": null,
          "primaryDescription": "Threat with confidence level suspicious detected: wildfire-test-pe-file(1).exe.",
          "secondaryDescription": "b691598c45658e76b2c328275db988baed3b8689",
          "siteId": "1286405255257023125",
          "threatId": "1503989642042428880",
          "updatedAt": "2022-09-07T02:38:56.725244Z",
          "userId": null
        },
        {
          "accountId": "1286405255240245908",
          "activityType": 71,
          "agentId": "1286438987267469377",
          "agentUpdatedVersion": null,
          "createdAt": "2022-11-14T20:10:56.882863Z",
          "data": {
            "accountName": "swimlane",
            "computerName": "localhost.localdomain",
            "externalIp": "96.79.235.37",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "groupType": "Manual",
            "scopeLevel": "Group",
            "scopeName": "Default Group",
            "siteName": "Default site",
            "system": false,
            "username": "Travis Riley",
            "uuid": "33b3a892-d388-d3e6-6ead-a98acb5d054c"
          },
          "groupId": "1286405255265411734",
          "hash": null,
          "id": "1553803882072530508",
          "osFamily": null,
          "primaryDescription": "The management user Travis Riley initiated a full disk scan to the agent: localhost.localdomain (96.79.235.37).",
          "secondaryDescription": null,
          "siteId": "1286405255257023125",
          "threatId": null,
          "updatedAt": "2022-11-14T20:10:56.882868Z",
          "userId": "1286405906565325677"
        },
        {
          "accountId": "1286405255240245908",
          "activityType": 2030,
          "agentId": "1286438987267469377",
          "agentUpdatedVersion": null,
          "createdAt": "2022-11-14T22:01:32.904992Z",
          "data": {
            "accountName": "swimlane",
            "computerName": "localhost.localdomain",
            "escapedMaliciousProcessArguments": null,
            "fileDisplayName": "wildfire-test-pe-file(1).exe",
            "filePath": "/home/swimlane-host/wildfire-test-pe-file(1).exe",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "newAnalystVerdict": "true_positive",
            "newAnalystVerdictTitle": "True positive",
            "oldAnalystVerdict": "undefined",
            "oldAnalystVerdictTitle": "Undefined",
            "siteName": "Default site",
            "threatClassification": "Malware",
            "threatClassificationSource": "Engine",
            "username": "Travis Riley"
          },
          "groupId": "1286405255265411734",
          "hash": null,
          "id": "1553859549076555381",
          "osFamily": null,
          "primaryDescription": "The management user Travis Riley changed the analyst verdict for wildfire-test-pe-file(1).exe from Undefined to True positive.",
          "secondaryDescription": null,
          "siteId": "1286405255257023125",
          "threatId": "1503989642042428880",
          "updatedAt": "2022-11-14T22:01:32.904993Z",
          "userId": "1286405906565325677"
        },
        {
          "accountId": "1286405255240245908",
          "activityType": 3002,
          "agentId": null,
          "agentUpdatedVersion": null,
          "createdAt": "2022-11-14T22:01:32.962480Z",
          "data": {
            "accountName": "swimlane",
            "description": null,
            "fileContentHash": "b691598c45658e76b2c328275db988baed3b8689",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "osFamily": "linux",
            "scopeLevel": "Group",
            "scopeName": "Default Group",
            "siteName": "Default site",
            "username": "Travis Riley"
          },
          "groupId": "1286405255265411734",
          "hash": "b691598c45658e76b2c328275db988baed3b8689",
          "id": "1553859549537928826",
          "osFamily": "linux",
          "primaryDescription": "The management user Travis Riley added / modified Linux blacklist hash.",
          "secondaryDescription": "b691598c45658e76b2c328275db988baed3b8689",
          "siteId": "1286405255257023125",
          "threatId": null,
          "updatedAt": "2022-11-14T22:01:32.886298Z",
          "userId": "1286405906565325677"
        },
        {
          "accountId": "1286405255240245908",
          "activityType": 2028,
          "agentId": "1286438987267469377",
          "agentUpdatedVersion": null,
          "createdAt": "2022-11-14T22:03:17.939520Z",
          "data": {
            "accountName": "swimlane",
            "computerName": "localhost.localdomain",
            "escapedMaliciousProcessArguments": null,
            "fileDisplayName": "wildfire-test-pe-file(1).exe",
            "filePath": "/home/swimlane-host/wildfire-test-pe-file(1).exe",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "newIncidentStatus": "in_progress",
            "newIncidentStatusTitle": "In progress",
            "oldIncidentStatus": "unresolved",
            "oldIncidentStatusTitle": "Unresolved",
            "siteName": "Default site",
            "threatClassification": "Malware",
            "threatClassificationSource": "Engine",
            "username": "Travis Riley"
          },
          "groupId": "1286405255265411734",
          "hash": null,
          "id": "1553860430148830999",
          "osFamily": null,
          "primaryDescription": "The management user Travis Riley changed the incident status for wildfire-test-pe-file(1).exe from Unresolved to In progress",
          "secondaryDescription": null,
          "siteId": "1286405255257023125",
          "threatId": "1503989642042428880",
          "updatedAt": "2022-11-14T22:03:17.939526Z",
          "userId": "1286405906565325677"
        },
        {
          "accountId": "1286405255240245908",
          "activityType": 2014,
          "agentId": "1286438987267469377",
          "agentUpdatedVersion": null,
          "createdAt": "2022-11-14T22:03:29.996397Z",
          "data": {
            "accountName": "swimlane",
            "computerName": "localhost.localdomain",
            "fileContentHash": "b691598c45658e76b2c328275db988baed3b8689",
            "fileDisplayName": "wildfire-test-pe-file(1).exe",
            "filePath": "/home/swimlane-host/wildfire-test-pe-file(1).exe",
            "fullScopeDetails": "Group Default Group in Site Default site of Account swimlane",
            "fullScopeDetailsPath": "Global / swimlane / Default site / Default Group",
            "groupName": "Default Group",
            "newStatus": null,
            "originalStatus": "not_mitigated",
            "siteName": "Default site",
            "threatClassification": "Malware",
            "threatClassificationSource": "Engine",
            "username": "Travis Riley"
          },
          "groupId": "1286405255265411734",
          "hash": null,
          "id": "1553860531298666283",
          "osFamily": null,
          "primaryDescription": "The management user Travis Riley issued a quarantine command to threat wildfire-test-pe-file(1).exe on agent localhost.localdomain.",
          "secondaryDescription": "/home/swimlane-host/wildfire-test-pe-file(1).exe",
          "siteId": "1286405255257023125",
          "threatId": "1503989642042428880",
          "updatedAt": "2022-11-14T22:03:29.996398Z",
          "userId": "1286405906565325677"
        }
      ],
      "pagination": {
        "nextCursor": null,
        "totalItems": 6
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
    - **accountId** (string)
    - **activityType** (number)
    - **agentId** (string)
    - **agentUpdatedVersion** (object)
    - **createdAt** (string)
    - **data** (object)
      - **accountName** (string)
      - **computerName** (string)
      - **fileContentHash** (string)
      - **fileDisplayName** (string)
      - **filePath** (string)
      - **fullScopeDetails** (string)
      - **fullScopeDetailsPath** (string)
      - **groupName** (string)
      - **newStatus** (object)
      - **originalStatus** (string)
      - **siteName** (string)
      - **threatClassification** (string)
      - **threatClassificationSource** (string)
      - **username** (string)
    - **groupId** (string)
    - **hash** (object)
    - **id** (string)
    - **osFamily** (object)
    - **primaryDescription** (string)
    - **secondaryDescription** (string)
    - **siteId** (string)
    - **threatId** (string)
    - **updatedAt** (string)
    - **userId** (string)
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