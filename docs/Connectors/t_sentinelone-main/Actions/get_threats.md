# Get Threats

**Description**: Retrieve a comprehensive list of all identified threats from SentinelOne.

## Endpoint

- **URL:** `web/api/v2.1/threats`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountIds** (array)
  - **agentIds** (array)
  - **agentIsActive** (boolean)
  - **agentMachineTypes** (array)
  - **agentMachineTypesNin** (array)
  - **agentVersions** (array)
  - **agentVersionsNin** (array)
  - **analystVerdicts** (array)
  - **analystVerdictsNin** (array)
  - **awsRole__contains** (array)
  - **awsSecurityGroups__contains** (array)
  - **awsSubnetIds__contains** (array)
  - **azureResourceGroup__contains** (array)
  - **classifications** (array)
  - **classificationsNin** (array)
  - **classificationSources** (array)
  - **classificationSourcesNin** (array)
  - **cloudAccount__contains** (array)
  - **cloudImage__contains** (array)
  - **cloudInstanceId__contains** (array)
  - **cloudInstanceSize__contains** (array)
  - **cloudLocation__contains** (array)
  - **cloudNetwork__contains** (array)
  - **cloudProvider** (array)
  - **cloudProviderNin** (array)
  - **collectionIds** (array)
  - **commandLineArguments__contains** (array)
  - **computerName__contains** (array)
  - **confidenceLevels** (array)
  - **confidenceLevelsNin** (array)
  - **containerImageName__contains** (array)
  - **containerLabels__contains** (array)
  - **containerName__contains** (array)
  - **contentHash__contains** (array)
  - **contentHashes** (array)
  - **countOnly** (boolean)
  - **countsFor** (string)
  - **createdAt__gt** (string)
  - **createdAt__gte** (string)
  - **createdAt__lt** (string)
  - **createdAt__lte** (string)
  - **cursor** (string)
  - **detectionAgentDomain__contains** (array)
  - **detectionAgentVersion__contains** (array)
  - **detectionEngines** (array)
  - **detectionEnginesNin** (array)
  - **displayName** (string)
  - **engines** (array)
  - **enginesNin** (array)
  - **externalTicketExists** (boolean)
  - **externalTicketId__contains** (array)
  - **externalTicketIds** (array)
  - **failedActions** (boolean)
  - **filePath__contains** (array)
  - **gcpServiceAccount__contains** (array)
  - **groupIds** (array)
  - **ids** (array)
  - **incidentStatuses** (array)
  - **incidentStatusesNin** (array)
  - **initiatedBy** (array)
  - **initiatedByNin** (array)
  - **initiatedByUsername__contains** (array)
  - **k8sClusterName__contains** (array)
  - **k8sControllerLabels__contains** (array)
  - **k8sControllerName__contains** (array)
  - **k8sNamespaceLabels__contains** (array)
  - **k8sNamespaceName__contains** (array)
  - **k8sNodeLabels__contains** (array)
  - **k8sNodeName__contains** (array)
  - **k8sPodLabels__contains** (array)
  - **k8sPodName__contains** (array)
  - **limit** (number)
  - **mitigatedPreemptively** (boolean)
  - **mitigationStatuses** (array)
  - **mitigationStatusesNin** (array)
  - **noteExists** (boolean)
  - **originatedProcess__contains** (array)
  - **osArchs** (array)
  - **osNames** (array)
  - **osNamesNin** (array)
  - **osTypes** (array)
  - **osTypesNin** (array)
  - **pendingActions** (boolean)
  - **publisherName__contains** (array)
  - **query** (string)
  - **realtimeAgentVersion__contains** (array)
  - **rebootRequired** (boolean)
  - **resolved** (boolean)
  - **siteIds** (array)
  - **skip** (number)
  - **skipCount** (boolean)
  - **sortBy** (string)
  - **sortOrder** (string)
  - **storyline__contains** (array)
  - **storylines** (array)
  - **tenant** (boolean)
  - **threatDetails__contains** (array)
  - **updatedAt__gt** (string)
  - **updatedAt__gte** (string)
  - **updatedAt__lt** (string)
  - **updatedAt__lte** (string)
  - **uuid__contains** (array)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 03 Jul 2023 03:42:11 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "96f7b37b-0e6b-4cb7-ba52-1c6bffa6d0fe",
      "Access-Control-Allow-Origin": "https://usea1-identity.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.pendo.io *.storage.googleapis.com cdn.auth0.com *.sentinelone.net wss://*.sentinelone.net https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-eval' *.sentinelone.net cdn.pendo.io app.pendo.io data.pendo.io pendo-io-static.storage.googleapis.com *.storage.googleapis.com https://cdnjs.cloudflare.com ; img-src 'self' data: *.pendo.io *.sentinelone.com *.sentinelone.net *.storage.googleapis.com; style-src 'self' 'unsafe-inline' *.sentinelone.net app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: *.sentinelone.net; frame-src 'self' blob: https://*.sentinelone.net https://*.scalyr.com https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://www.youtube.com/; object-src 'none'; frame-ancestors 'self' app.pendo.io *.sentinelone.net",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "errors": [
        {
          "type": "object"
        }
      ],
      "pagination": {
        "totalItems": 580,
        "nextCursor": "YWdlbnRfaWQ6NTgwMjkzODE="
      },
      "data": [
        {
          "mitigationStatus": [
            {
              "lastUpdate": "2018-02-27T04:49:26.257525Z",
              "agentSupportsReport": "boolean",
              "latestReport": "string",
              "groupNotFound": "boolean",
              "mitigationEndedAt": "2018-02-27T04:49:26.257525Z",
              "action": "kill",
              "actionsCounters": {
                "pendingReboot": "integer",
                "failed": "integer",
                "total": "integer",
                "notFound": "integer",
                "success": "integer"
              },
              "status": "success",
              "mitigationStartedAt": "2018-02-27T04:49:26.257525Z"
            }
          ],
          "kubernetesInfo": {
            "controllerKind": "string",
            "namespace": "string",
            "isContainerQuarantine": "boolean",
            "controllerLabels": [
              {
                "type": "string"
              }
            ],
            "nodeLabels": [
              {
                "type": "string"
              }
            ],
            "namespaceLabels": [
              {
                "type": "string"
              }
            ],
            "controllerName": "string",
            "pod": "string",
            "podLabels": [
              {
                "type": "string"
              }
            ],
            "node": "string",
            "cluster": "string"
          },
          "whiteningOptions": [
            {
              "type": "string"
            }
          ],
          "agentDetectionInfo": {
            "accountId": "225494730938493804",
            "siteName": "string",
            "groupId": "225494730938493804",
            "agentVersion": "3.6.1.14",
            "accountName": "string",
            "agentIpV4": "string",
            "siteId": "225494730938493804",
            "agentLastLoggedInUserMail": "string",
            "agentOsName": "string",
            "agentRegisteredAt": "2018-02-27T04:49:26.257525Z",
            "cloudProviders": "object",
            "agentMitigationMode": "detect",
            "externalIp": "string",
            "agentOsRevision": "string",
            "agentUuid": "string",
            "groupName": "string",
            "agentIpV6": "string",
            "agentLastLoggedInUserName": "janedoe3",
            "agentDomain": "mybusiness.net",
            "agentDetectionState": "string",
            "agentLastLoggedInUpn": "string"
          },
          "agentRealtimeInfo": {
            "siteId": "225494730938493804",
            "groupName": "string",
            "agentVersion": "3.6.1.14",
            "agentDecommissionedAt": "boolean",
            "agentComputerName": "string",
            "scanStartedAt": "2018-02-27T04:49:26.257525Z",
            "agentDomain": "string",
            "agentMitigationMode": "detect",
            "agentId": "225494730938493804",
            "operationalState": "string",
            "userActionsNeeded": [
              {
                "type": "string",
                "example": "none",
                "enum": [
                  "none",
                  "reboot_needed",
                  "upgrade_needed",
                  "incompatible_os",
                  "unprotected",
                  "rebootless_without_dynamic_detection",
                  "extended_exclusions_partially_accepted",
                  "reboot_required",
                  "pending_deprecation",
                  "user_action_needed",
                  "user_action_needed_fda",
                  "user_action_needed_rs_fda",
                  "user_action_needed_fda_helper",
                  "user_action_needed_bluetooth_per",
                  "user_action_needed_network",
                  "user_action_needed_notifications",
                  "user_action_needed_login_items"
                ]
              }
            ],
            "agentOsType": "linux",
            "networkInterfaces": [
              {
                "inet6": [
                  {
                    "type": "string"
                  }
                ],
                "id": "225494730938493804",
                "inet": [
                  {
                    "type": "string"
                  }
                ],
                "name": "string",
                "physical": "00:25:96:FF:FE:12:34:56"
              }
            ],
            "rebootRequired": "boolean",
            "siteName": "string",
            "groupId": "225494730938493804",
            "agentInfected": "boolean",
            "agentOsName": "string",
            "scanStatus": "none",
            "agentNetworkStatus": "connected",
            "activeThreats": "integer",
            "agentUuid": "string",
            "agentMachineType": "unknown",
            "agentIsActive": "boolean",
            "accountId": "225494730938493804",
            "storageType": "string",
            "agentOsRevision": "string",
            "storageName": "string",
            "agentIsDecommissioned": "boolean",
            "scanFinishedAt": "2018-02-27T04:49:26.257525Z",
            "scanAbortedAt": "2018-02-27T04:49:26.257525Z",
            "accountName": "string"
          },
          "id": "225494730938493804",
          "containerInfo": {
            "isContainerQuarantine": "boolean",
            "id": "string",
            "image": "string",
            "labels": [
              {
                "type": "string"
              }
            ],
            "name": "string"
          },
          "indicators": [
            {
              "ids": [
                {
                  "type": "integer",
                  "format": "int32"
                }
              ],
              "categoryId": "integer",
              "category": "string",
              "tactics": [
                {
                  "name": "string",
                  "techniques": [
                    {
                      "link": "string",
                      "name": "string"
                    }
                  ],
                  "source": "string"
                }
              ],
              "description": "string"
            }
          ],
          "threatInfo": {
            "publisherName": "string",
            "updatedAt": "2018-02-27T04:49:26.257525Z",
            "threatId": "225494730938493804",
            "initiatedBy": "agent_policy",
            "fileExtensionType": "string",
            "classification": "string",
            "confidenceLevel": "malicious",
            "filePath": {
              "readOnly": true,
              "description": "File path"
            },
            "maliciousProcessArguments": "string",
            "threatName": "string",
            "failedActions": "boolean",
            "initiatingUsername": "string",
            "sha1": "ddd5030a3d029f3845fc1052419829f08f312240",
            "storyline": "a00637fa-e18d-9b80-e803-f370524f8085",
            "isFileless": {
              "readOnly": true,
              "description": "Is fileless"
            },
            "isValidCertificate": "boolean",
            "certificateId": "string",
            "classificationSource": "Cloud",
            "incidentStatusDescription": {
              "readOnly": true,
              "description": "Incident status description"
            },
            "identifiedAt": "2018-02-27T04:49:26.257525Z",
            "browserType": "string",
            "automaticallyResolved": "boolean",
            "fileSize": "integer",
            "mitigationStatus": "not_mitigated",
            "engines": [
              "reputation",
              "pre_execution"
            ],
            "rebootRequired": "boolean",
            "processUser": "string",
            "detectionEngines": [
              "reputation",
              "pre_execution"
            ],
            "analystVerdictDescription": {
              "readOnly": true,
              "description": "Analyst verdict description"
            },
            "initiatingUserId": "225494730938493804",
            "analystVerdict": "undefined",
            "initiatedByDescription": {
              "readOnly": true,
              "description": "Initiated by description"
            },
            "mitigatedPreemptively": "boolean",
            "incidentStatus": "unresolved",
            "detectionType": "static",
            "mitigationStatusDescription": {
              "readOnly": true,
              "description": "Mitigation status description"
            },
            "collectionId": "225494730938493804",
            "fileVerificationType": "string",
            "externalTicketId": "string",
            "reachedEventsLimit": "boolean",
            "originatorProcess": "string",
            "externalTicketExists": {
              "readOnly": true,
              "description": "External ticket exists"
            },
            "fileExtension": "string",
            "md5": "string",
            "pendingActions": "boolean",
            "cloudFilesHashVerdict": "string",
            "sha256": "50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccacd0f6545c",
            "createdAt": "2018-02-27T04:49:26.257525Z"
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
  - **errors** (array)
    - **type** (string)
  - **pagination** (object)
    - **totalItems** (number)
    - **nextCursor** (string)
  - **data** (array)
    - **mitigationStatus** (array)
      - **lastUpdate** (string)
      - **agentSupportsReport** (string)
      - **latestReport** (string)
      - **groupNotFound** (string)
      - **mitigationEndedAt** (string)
      - **action** (string)
      - **actionsCounters** (object)
        - **pendingReboot** (string)
        - **failed** (string)
        - **total** (string)
        - **notFound** (string)
        - **success** (string)
      - **status** (string)
      - **mitigationStartedAt** (string)
    - **kubernetesInfo** (object)
      - **controllerKind** (string)
      - **namespace** (string)
      - **isContainerQuarantine** (string)
      - **controllerLabels** (array)
        - **type** (string)
      - **nodeLabels** (array)
        - **type** (string)
      - **namespaceLabels** (array)
        - **type** (string)
      - **controllerName** (string)
      - **pod** (string)
      - **podLabels** (array)
        - **type** (string)
      - **node** (string)
      - **cluster** (string)
    - **whiteningOptions** (array)
      - **type** (string)
    - **agentDetectionInfo** (object)
      - **accountId** (string)
      - **siteName** (string)
      - **groupId** (string)
      - **agentVersion** (string)
      - **accountName** (string)
      - **agentIpV4** (string)
      - **siteId** (string)
      - **agentLastLoggedInUserMail** (string)
      - **agentOsName** (string)
      - **agentRegisteredAt** (string)
      - **cloudProviders** (string)
      - **agentMitigationMode** (string)
      - **externalIp** (string)
      - **agentOsRevision** (string)
      - **agentUuid** (string)
      - **groupName** (string)
      - **agentIpV6** (string)
      - **agentLastLoggedInUserName** (string)
      - **agentDomain** (string)
      - **agentDetectionState** (string)
      - **agentLastLoggedInUpn** (string)
    - **agentRealtimeInfo** (object)
      - **siteId** (string)
      - **groupName** (string)
      - **agentVersion** (string)
      - **agentDecommissionedAt** (string)
      - **agentComputerName** (string)
      - **scanStartedAt** (string)
      - **agentDomain** (string)
      - **agentMitigationMode** (string)
      - **agentId** (string)
      - **operationalState** (string)
      - **userActionsNeeded** (array)
        - **type** (string)
        - **example** (string)
        - **enum** (array)
      - **agentOsType** (string)
      - **networkInterfaces** (array)
        - **inet6** (array)
          - **type** (string)
        - **id** (string)
        - **inet** (array)
          - **type** (string)
        - **name** (string)
        - **physical** (string)
      - **rebootRequired** (string)
      - **siteName** (string)
      - **groupId** (string)
      - **agentInfected** (string)
      - **agentOsName** (string)
      - **scanStatus** (string)
      - **agentNetworkStatus** (string)
      - **activeThreats** (string)
      - **agentUuid** (string)
      - **agentMachineType** (string)
      - **agentIsActive** (string)
      - **accountId** (string)
      - **storageType** (string)
      - **agentOsRevision** (string)
      - **storageName** (string)
      - **agentIsDecommissioned** (string)
      - **scanFinishedAt** (string)
      - **scanAbortedAt** (string)
      - **accountName** (string)
    - **id** (string)
    - **containerInfo** (object)
      - **isContainerQuarantine** (string)
      - **id** (string)
      - **image** (string)
      - **labels** (array)
        - **type** (string)
      - **name** (string)
    - **indicators** (array)
      - **ids** (array)
        - **type** (string)
        - **format** (string)
      - **categoryId** (string)
      - **category** (string)
      - **tactics** (array)
        - **name** (string)
        - **techniques** (array)
          - **link** (string)
          - **name** (string)
        - **source** (string)
      - **description** (string)
    - **threatInfo** (object)
      - **publisherName** (string)
      - **updatedAt** (string)
      - **threatId** (string)
      - **initiatedBy** (string)
      - **fileExtensionType** (string)
      - **classification** (string)
      - **confidenceLevel** (string)
      - **filePath** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **maliciousProcessArguments** (string)
      - **threatName** (string)
      - **failedActions** (string)
      - **initiatingUsername** (string)
      - **sha1** (string)
      - **storyline** (string)
      - **isFileless** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **isValidCertificate** (string)
      - **certificateId** (string)
      - **classificationSource** (string)
      - **incidentStatusDescription** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **identifiedAt** (string)
      - **browserType** (string)
      - **automaticallyResolved** (string)
      - **fileSize** (string)
      - **mitigationStatus** (string)
      - **engines** (array)
      - **rebootRequired** (string)
      - **processUser** (string)
      - **detectionEngines** (array)
      - **analystVerdictDescription** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **initiatingUserId** (string)
      - **analystVerdict** (string)
      - **initiatedByDescription** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **mitigatedPreemptively** (string)
      - **incidentStatus** (string)
      - **detectionType** (string)
      - **mitigationStatusDescription** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **collectionId** (string)
      - **fileVerificationType** (string)
      - **externalTicketId** (string)
      - **reachedEventsLimit** (string)
      - **originatorProcess** (string)
      - **externalTicketExists** (object)
        - **readOnly** (boolean)
        - **description** (string)
      - **fileExtension** (string)
      - **md5** (string)
      - **pendingActions** (string)
      - **cloudFilesHashVerdict** (string)
      - **sha256** (string)
      - **createdAt** (string)
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