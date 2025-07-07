# Get Agents

**Description**: Obtain data for SentinelOne agents using specific filters to identify and utilize Agent IDs in further operations.

## Endpoint

- **URL:** `web/api/v2.1/agents`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **computerName** (string)
  - **infected** (boolean)
  - **isActive** (boolean)
  - **activeThreats** (array)
  - **domains** (array)
  - **networkStatuses** (array)
  - **externalIp__contains** (string)
  - **ids** (array)
  - **accountIds** (array)
  - **uuids** (array)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 17:35:13 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "bd078c0d-1020-461b-885a-0028c992ac70",
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
          "accountName": "swimlane",
          "activeDirectory": {
            "computerDistinguishedName": null,
            "computerMemberOf": [],
            "lastUserDistinguishedName": null,
            "lastUserMemberOf": []
          },
          "activeThreats": 0,
          "agentVersion": "21.10.1.6",
          "allowRemoteShell": false,
          "appsVulnerabilityStatus": "not_applicable",
          "cloudProviders": {
            "ESXI": {}
          },
          "computerName": "ubuntu",
          "consoleMigrationStatus": "N/A",
          "coreCount": 2,
          "cpuCount": 2,
          "cpuId": "Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz",
          "createdAt": "2022-11-10T20:04:42.684950Z",
          "detectionState": null,
          "domain": "unknown",
          "encryptedApplications": false,
          "externalId": "",
          "externalIp": "96.79.235.37",
          "firewallEnabled": true,
          "firstFullModeTime": null,
          "groupId": "1286405255265411734",
          "groupIp": "96.79.235.x",
          "groupName": "Default Group",
          "id": "1550901640146865256",
          "inRemoteShellSession": false,
          "infected": false,
          "installerType": ".deb",
          "isActive": false,
          "isDecommissioned": false,
          "isPendingUninstall": false,
          "isUninstalled": false,
          "isUpToDate": true,
          "lastActiveDate": "2022-11-10T20:10:21.624510Z",
          "lastIpToMgmt": "10.32.0.158",
          "lastLoggedInUserName": "",
          "licenseKey": "",
          "locationEnabled": false,
          "locationType": "not_applicable",
          "locations": null,
          "machineType": "server",
          "mitigationMode": "protect",
          "mitigationModeSuspicious": "detect",
          "modelName": "VMware, Inc. VMware Virtual Platform",
          "networkInterfaces": [
            {
              "gatewayIp": "10.32.0.1",
              "gatewayMacAddress": "24:6e:96:1d:46:28",
              "id": "1550901640155253865",
              "inet": [
                "10.32.0.158"
              ],
              "inet6": [
                "fe80::250:56ff:fe90:80e0"
              ],
              "name": "eth0",
              "physical": "00:50:56:90:80:E0"
            }
          ],
          "networkQuarantineEnabled": false,
          "networkStatus": "connected",
          "operationalState": "na",
          "operationalStateExpiration": null,
          "osArch": "64 bit",
          "osName": "Linux",
          "osRevision": "Ubuntu 14.04.6 LTS 4.4.0-142-generic",
          "osStartTime": "2022-11-10T20:04:19Z",
          "osType": "linux",
          "osUsername": "root",
          "rangerStatus": "NotApplicable",
          "rangerVersion": null,
          "registeredAt": "2022-11-10T20:04:42.680790Z",
          "remoteProfilingState": "disabled",
          "remoteProfilingStateExpiration": null,
          "scanAbortedAt": null,
          "scanFinishedAt": null,
          "scanStartedAt": "2022-11-10T20:05:39.778639Z",
          "scanStatus": "started",
          "serialNumber": null,
          "siteId": "1286405255257023125",
          "siteName": "Default site",
          "storageName": null,
          "storageType": null,
          "tags": {
            "sentinelone": []
          },
          "threatRebootRequired": false,
          "totalMemory": 3951,
          "updatedAt": "2022-11-16T03:20:46.218532Z",
          "userActionsNeeded": [],
          "uuid": "2e24b3bf-5769-e031-35af-7ebaf2f3dcf3"
        }
      ],
      "pagination": {
        "nextCursor": null,
        "totalItems": 1
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
    - **accountName** (string)
    - **activeDirectory** (object)
      - **computerDistinguishedName** (object)
      - **computerMemberOf** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **lastUserDistinguishedName** (object)
      - **lastUserMemberOf** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
    - **activeThreats** (number)
    - **agentVersion** (string)
    - **allowRemoteShell** (boolean)
    - **appsVulnerabilityStatus** (string)
    - **cloudProviders** (object)
      - **ESXI** (object)
    - **computerName** (string)
    - **consoleMigrationStatus** (string)
    - **coreCount** (number)
    - **cpuCount** (number)
    - **cpuId** (string)
    - **createdAt** (string)
    - **detectionState** (object)
    - **domain** (string)
    - **encryptedApplications** (boolean)
    - **externalId** (string)
    - **externalIp** (string)
    - **firewallEnabled** (boolean)
    - **firstFullModeTime** (object)
    - **groupId** (string)
    - **groupIp** (string)
    - **groupName** (string)
    - **id** (string)
    - **inRemoteShellSession** (boolean)
    - **infected** (boolean)
    - **installerType** (string)
    - **isActive** (boolean)
    - **isDecommissioned** (boolean)
    - **isPendingUninstall** (boolean)
    - **isUninstalled** (boolean)
    - **isUpToDate** (boolean)
    - **lastActiveDate** (string)
    - **lastIpToMgmt** (string)
    - **lastLoggedInUserName** (string)
    - **licenseKey** (string)
    - **locationEnabled** (boolean)
    - **locationType** (string)
    - **locations** (object)
    - **machineType** (string)
    - **mitigationMode** (string)
    - **mitigationModeSuspicious** (string)
    - **modelName** (string)
    - **networkInterfaces** (array)
      - **gatewayIp** (string)
      - **gatewayMacAddress** (string)
      - **id** (string)
      - **inet** (array)
      - **inet6** (array)
      - **name** (string)
      - **physical** (string)
    - **networkQuarantineEnabled** (boolean)
    - **networkStatus** (string)
    - **operationalState** (string)
    - **operationalStateExpiration** (object)
    - **osArch** (string)
    - **osName** (string)
    - **osRevision** (string)
    - **osStartTime** (string)
    - **osType** (string)
    - **osUsername** (string)
    - **rangerStatus** (string)
    - **rangerVersion** (object)
    - **registeredAt** (string)
    - **remoteProfilingState** (string)
    - **remoteProfilingStateExpiration** (object)
    - **scanAbortedAt** (object)
    - **scanFinishedAt** (object)
    - **scanStartedAt** (string)
    - **scanStatus** (string)
    - **serialNumber** (object)
    - **siteId** (string)
    - **siteName** (string)
    - **storageName** (object)
    - **storageType** (object)
    - **tags** (object)
      - **sentinelone** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
    - **threatRebootRequired** (boolean)
    - **totalMemory** (number)
    - **updatedAt** (string)
    - **userActionsNeeded** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **uuid** (string)
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