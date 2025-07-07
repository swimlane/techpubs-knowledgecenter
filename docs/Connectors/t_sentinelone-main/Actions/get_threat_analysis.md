# Get Threat Analysis

**Description**: Retrieve detailed information on a detected threat in SentinelOne using the specified threat ID.

## Endpoint

- **URL:** `web/api/v2.1/private/threats/{{threat_id}}/analysis`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **threat_id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 14 Nov 2022 21:44:11 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "fbaffde6-2d29-4834-946d-d3c77ee169f9",
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
      "data": {
        "agentDetectionInfo": {
          "accountId": "1286405255240245908",
          "accountName": "swimlane",
          "agentDetectionState": null,
          "agentDomain": "",
          "agentIpV4": "10.32.0.165,172.18.0.1,172.17.0.1",
          "agentIpV6": "fe80::7d:1cff:feeb:36b,fe80::70da:4eff:fe05:1e14,fe80::42:94ff:fe48:e0bf,fe80::4cca:b0ff:fec1:86e4,fe80::3013:22ff:fed7:6ba8,fe80::250:56ff:febd:78a0",
          "agentLastLoggedInUpn": null,
          "agentLastLoggedInUserMail": null,
          "agentLastLoggedInUserName": "",
          "agentMitigationMode": "protect",
          "agentOsName": "Linux",
          "agentOsRevision": "CentOS release 7.8.2003 (Core) 3.10.0-1127.el7.x86_64",
          "agentRegisteredAt": "2021-11-10T22:44:37.714973Z",
          "agentUuid": "33b3a892-d388-d3e6-6ead-a98acb5d054c",
          "agentVersion": "21.10.1.6",
          "cloudProviders": {},
          "externalIp": "96.79.235.37",
          "groupId": "1286405255265411734",
          "groupName": "Default Group",
          "siteId": "1286405255257023125",
          "siteName": "Default site"
        },
        "agentRealtimeInfo": {
          "accountId": "1286405255240245908",
          "accountName": "swimlane",
          "activeThreats": 0,
          "agentComputerName": "localhost.localdomain",
          "agentDecommissionedAt": null,
          "agentDomain": "",
          "agentId": "1286438987267469377",
          "agentInfected": false,
          "agentIsActive": true,
          "agentIsDecommissioned": false,
          "agentMachineType": "server",
          "agentMitigationMode": "protect",
          "agentNetworkStatus": "connected",
          "agentOsName": "Linux",
          "agentOsRevision": "CentOS release 7.8.2003 (Core) 3.10.0-1127.el7.x86_64",
          "agentOsType": "linux",
          "agentUuid": "33b3a892-d388-d3e6-6ead-a98acb5d054c",
          "agentVersion": "21.10.1.6",
          "groupId": "1286405255265411734",
          "groupName": "Default Group",
          "networkInterfaces": [
            {
              "id": "1543172592000726460",
              "inet": [],
              "inet6": [
                "fe80::40b2:6aff:fe95:383e"
              ],
              "name": "vethee3d644",
              "physical": "42:B2:6A:95:38:3E"
            },
            {
              "id": "1543172592000726459",
              "inet": [],
              "inet6": [
                "fe80::6015:78ff:fea9:c83f"
              ],
              "name": "vethe80c0de",
              "physical": "62:15:78:A9:C8:3F"
            },
            {
              "id": "1543172592000726458",
              "inet": [
                "172.18.0.1"
              ],
              "inet6": [
                "fe80::42:7aff:fe65:8d5d"
              ],
              "name": "br-fff54108db6c",
              "physical": "02:42:7A:65:8D:5D"
            },
            {
              "id": "1543172591992337849",
              "inet": [],
              "inet6": [
                "fe80::d49d:8eff:fe3e:7c96"
              ],
              "name": "veth4eead3a",
              "physical": "D6:9D:8E:3E:7C:96"
            },
            {
              "id": "1543172591992337848",
              "inet": [],
              "inet6": [
                "fe80::98cf:d7ff:feaa:df6d"
              ],
              "name": "veth9ec7d68",
              "physical": "9A:CF:D7:AA:DF:6D"
            },
            {
              "id": "1543147384250434231",
              "inet": [
                "172.17.0.1"
              ],
              "inet6": [],
              "name": "docker0",
              "physical": "02:42:C9:05:AD:AA"
            },
            {
              "id": "1286438987267469378",
              "inet": [
                "10.32.0.165"
              ],
              "inet6": [
                "fe80::250:56ff:febd:78a0"
              ],
              "name": "eth0",
              "physical": "00:50:56:BD:78:A0"
            }
          ],
          "operationalState": "na",
          "rebootRequired": false,
          "scanAbortedAt": null,
          "scanFinishedAt": "2022-09-07T02:40:59.261750Z",
          "scanStartedAt": "2022-11-14T20:11:25.369554Z",
          "scanStatus": "started",
          "siteId": "1286405255257023125",
          "siteName": "Default site",
          "storageName": null,
          "storageType": null,
          "userActionsNeeded": []
        },
        "containerInfo": {
          "id": null,
          "image": null,
          "isContainerQuarantine": null,
          "labels": null,
          "name": null
        },
        "customDetectionRules": [],
        "indicators": [],
        "kubernetesInfo": {
          "cluster": null,
          "controllerKind": null,
          "controllerLabels": null,
          "controllerName": null,
          "isContainerQuarantine": null,
          "namespace": null,
          "namespaceLabels": null,
          "node": null,
          "pod": null,
          "podLabels": null
        },
        "mitigationStatus": [
          {
            "action": "quarantine",
            "actionsCounters": {
              "failed": 0,
              "notFound": 0,
              "pendingReboot": 0,
              "success": 1,
              "total": 1
            },
            "agentSupportsReport": true,
            "groupNotFound": false,
            "lastUpdate": "2021-12-14T20:23:47.484537Z",
            "latestReport": "/threats/mitigation-report/1311010476397293060",
            "mitigationEndedAt": "2021-12-14T20:23:47.484543Z",
            "mitigationStartedAt": "2021-12-14T20:23:47.484548Z",
            "status": "success"
          }
        ],
        "threatInfo": {
          "analystVerdict": "undefined",
          "analystVerdictDescription": "Undefined",
          "automaticallyResolved": false,
          "browserType": null,
          "certificateId": null,
          "classification": "Malware",
          "classificationSource": "Static",
          "cloudFilesHashVerdict": "black",
          "collectionId": "433377870883088367",
          "confidenceLevel": "malicious",
          "createdAt": "2021-12-14T20:23:47.249133Z",
          "detectionEngines": [
            {
              "key": "pre_execution",
              "title": "On-Write Static AI"
            }
          ],
          "detectionType": "static",
          "engines": [
            "On-Write DFI"
          ],
          "externalTicketExists": false,
          "externalTicketId": null,
          "failedActions": false,
          "fileExtension": null,
          "fileExtensionType": null,
          "filePath": "/home/swimlane-host/eicar.com",
          "fileSize": 68,
          "fileVerificationType": null,
          "identifiedAt": "2021-12-14T20:23:47.143694Z",
          "incidentStatus": "unresolved",
          "incidentStatusDescription": "Unresolved",
          "initiatedBy": "agent_policy",
          "initiatedByDescription": "Agent Policy",
          "initiatingUserId": null,
          "initiatingUsername": null,
          "isFileless": false,
          "isValidCertificate": null,
          "maliciousProcessArguments": null,
          "md5": null,
          "mitigatedPreemptively": false,
          "mitigationStatus": "mitigated",
          "mitigationStatusDescription": "Mitigated",
          "originatorProcess": "scp",
          "pendingActions": false,
          "processUser": "swimlane-host",
          "publisherName": null,
          "reachedEventsLimit": null,
          "rebootRequired": false,
          "sha1": "3395856ce81f2b7382dee72602f798b642f14140",
          "sha256": null,
          "storyline": "9e6d373b-b7b7-c6fc-e703-6acca4842e53",
          "threatId": "1311010474425970168",
          "threatName": "eicar.com",
          "updatedAt": "2021-12-14T20:23:47.481644Z"
        },
        "whiteningOptions": [
          "path",
          "hash"
        ]
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **agentDetectionInfo** (object)
      - **accountId** (string)
      - **accountName** (string)
      - **agentDetectionState** (object)
      - **agentDomain** (string)
      - **agentIpV4** (string)
      - **agentIpV6** (string)
      - **agentLastLoggedInUpn** (object)
      - **agentLastLoggedInUserMail** (object)
      - **agentLastLoggedInUserName** (string)
      - **agentMitigationMode** (string)
      - **agentOsName** (string)
      - **agentOsRevision** (string)
      - **agentRegisteredAt** (string)
      - **agentUuid** (string)
      - **agentVersion** (string)
      - **cloudProviders** (object)
      - **externalIp** (string)
      - **groupId** (string)
      - **groupName** (string)
      - **siteId** (string)
      - **siteName** (string)
    - **agentRealtimeInfo** (object)
      - **accountId** (string)
      - **accountName** (string)
      - **activeThreats** (number)
      - **agentComputerName** (string)
      - **agentDecommissionedAt** (object)
      - **agentDomain** (string)
      - **agentId** (string)
      - **agentInfected** (boolean)
      - **agentIsActive** (boolean)
      - **agentIsDecommissioned** (boolean)
      - **agentMachineType** (string)
      - **agentMitigationMode** (string)
      - **agentNetworkStatus** (string)
      - **agentOsName** (string)
      - **agentOsRevision** (string)
      - **agentOsType** (string)
      - **agentUuid** (string)
      - **agentVersion** (string)
      - **groupId** (string)
      - **groupName** (string)
      - **networkInterfaces** (array)
        - **id** (string)
        - **inet** (array)
        - **inet6** (array)
        - **name** (string)
        - **physical** (string)
      - **operationalState** (string)
      - **rebootRequired** (boolean)
      - **scanAbortedAt** (object)
      - **scanFinishedAt** (string)
      - **scanStartedAt** (string)
      - **scanStatus** (string)
      - **siteId** (string)
      - **siteName** (string)
      - **storageName** (object)
      - **storageType** (object)
      - **userActionsNeeded** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
    - **containerInfo** (object)
      - **id** (object)
      - **image** (object)
      - **isContainerQuarantine** (object)
      - **labels** (object)
      - **name** (object)
    - **customDetectionRules** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **indicators** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **kubernetesInfo** (object)
      - **cluster** (object)
      - **controllerKind** (object)
      - **controllerLabels** (object)
      - **controllerName** (object)
      - **isContainerQuarantine** (object)
      - **namespace** (object)
      - **namespaceLabels** (object)
      - **node** (object)
      - **pod** (object)
      - **podLabels** (object)
    - **mitigationStatus** (array)
      - **action** (string)
      - **actionsCounters** (object)
        - **failed** (number)
        - **notFound** (number)
        - **pendingReboot** (number)
        - **success** (number)
        - **total** (number)
      - **agentSupportsReport** (boolean)
      - **groupNotFound** (boolean)
      - **lastUpdate** (string)
      - **latestReport** (string)
      - **mitigationEndedAt** (string)
      - **mitigationStartedAt** (string)
      - **status** (string)
    - **threatInfo** (object)
      - **analystVerdict** (string)
      - **analystVerdictDescription** (string)
      - **automaticallyResolved** (boolean)
      - **browserType** (object)
      - **certificateId** (object)
      - **classification** (string)
      - **classificationSource** (string)
      - **cloudFilesHashVerdict** (string)
      - **collectionId** (string)
      - **confidenceLevel** (string)
      - **createdAt** (string)
      - **detectionEngines** (array)
        - **key** (string)
        - **title** (string)
      - **detectionType** (string)
      - **engines** (array)
      - **externalTicketExists** (boolean)
      - **externalTicketId** (object)
      - **failedActions** (boolean)
      - **fileExtension** (object)
      - **fileExtensionType** (object)
      - **filePath** (string)
      - **fileSize** (number)
      - **fileVerificationType** (object)
      - **identifiedAt** (string)
      - **incidentStatus** (string)
      - **incidentStatusDescription** (string)
      - **initiatedBy** (string)
      - **initiatedByDescription** (string)
      - **initiatingUserId** (object)
      - **initiatingUsername** (object)
      - **isFileless** (boolean)
      - **isValidCertificate** (object)
      - **maliciousProcessArguments** (object)
      - **md5** (object)
      - **mitigatedPreemptively** (boolean)
      - **mitigationStatus** (string)
      - **mitigationStatusDescription** (string)
      - **originatorProcess** (string)
      - **pendingActions** (boolean)
      - **processUser** (string)
      - **publisherName** (object)
      - **reachedEventsLimit** (object)
      - **rebootRequired** (boolean)
      - **sha1** (string)
      - **sha256** (object)
      - **storyline** (string)
      - **threatId** (string)
      - **threatName** (string)
      - **updatedAt** (string)
    - **whiteningOptions** (array)
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