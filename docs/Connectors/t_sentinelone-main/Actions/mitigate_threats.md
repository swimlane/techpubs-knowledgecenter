# Mitigate Threats

**Description**: Apply a specified mitigation action to identified threats in SentinelOne using 'action' and 'filter' parameters.

## Endpoint

- **URL:** `/web/api/v2.1/threats/mitigate/{{action}}`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **action** (string) – Required
- **json_body** (object) – Required
  - **filter** (object) – Required
    - **k8sPodLabels__contains** (array)
    - **updatedAt__gte** (string)
    - **awsSubnetIds__contains** (array)
    - **agentMachineTypes** (array)
    - **cloudAccount__contains** (array)
    - **agentVersions** (array)
    - **siteIds** (array)
    - **classificationSourcesNin** (array)
    - **storylines** (array)
    - **detectionAgentVersion__contains** (array)
    - **createdAt__lt** (string)
    - **resolved** (boolean)
    - **mitigatedPreemptively** (boolean)
    - **detectionEngines** (array)
    - **threatDetails__contains** (array)
    - **storyline__contains** (array)
    - **agentVersionsNin** (array)
    - **originatedProcess__contains** (array)
    - **tenant** (boolean)
    - **cloudProvider** (array)
    - **pendingActions** (boolean)
    - **agentIds** (array)
    - **detectionAgentDomain__contains** (array)
    - **incidentStatusesNin** (array)
    - **updatedAt__gt** (string)
    - **gcpServiceAccount__contains** (array)
    - **k8sNodeName__contains** (array)
    - **classifications** (array)
    - **ids** (array)
    - **classificationsNin** (array)
    - **confidenceLevels** (array)
    - **classificationSources** (array)
    - **osArchs** (array)
    - **limit** (number)
    - **k8sClusterName__contains** (array)
    - **publisherName__contains** (array)
    - **k8sControllerLabels__contains** (array)
    - **externalTicketId__contains** (array)
    - **cloudInstanceSize__contains** (array)
    - **cloudInstanceId__contains** (array)
    - **k8sNamespaceLabels__contains** (array)
    - **noteExists** (boolean)
    - **k8sNodeLabels__contains** (array)
    - **uuid__contains** (array)
    - **updatedAt__lt** (string)
    - **osNames** (array)
    - **azureResourceGroup__contains** (array)
    - **confidenceLevelsNin** (array)
    - **createdAt__gt** (string)
    - **enginesNin** (array)
    - **groupIds** (array)
    - **collectionIds** (array)
    - **k8sPodName__contains** (array)
    - **accountIds** (array)
    - **analystVerdicts** (array)
    - **k8sControllerName__contains** (array)
    - **cloudProviderNin** (array)
    - **mitigationStatusesNin** (array)
    - **osTypes** (array)
    - **detectionEnginesNin** (array)
    - **initiatedByNin** (array)
    - **k8sNamespaceName__contains** (array)
    - **cloudImage__contains** (array)
    - **query** (string)
    - **containerImageName__contains** (array)
    - **osTypesNin** (array)
    - **contentHash__contains** (array)
    - **agentMachineTypesNin** (array)
    - **rebootRequired** (boolean)
    - **commandLineArguments__contains** (array)
    - **realtimeAgentVersion__contains** (array)
    - **createdAt__lte** (string)
    - **initiatedByUsername__contains** (array)
    - **failedActions** (boolean)
    - **containerLabels__contains** (array)
    - **cloudLocation__contains** (array)
    - **mitigationStatuses** (array)
    - **createdAt__gte** (string)
    - **awsSecurityGroups__contains** (array)
    - **agentIsActive** (boolean)
    - **engines** (array)
    - **awsRole__contains** (array)
    - **updatedAt__lte** (string)
    - **containerName__contains** (array)
    - **cloudNetwork__contains** (array)
    - **displayName** (string)
    - **filePath__contains** (array)
    - **osNamesNin** (array)
    - **analystVerdictsNin** (array)
    - **incidentStatuses** (array)
    - **countsFor** (string)
    - **externalTicketIds** (array)
    - **contentHashes** (array)
    - **initiatedBy** (array)
    - **computerName__contains** (array)
    - **externalTicketExists** (boolean)
  - **data** (object)
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Mon, 11 Sep 2023 08:58:22 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "ca215f22-b23f-4683-a984-d5283635fed4",
      "Access-Control-Allow-Origin": "https://usea1-identity.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "affected": 0
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
    - **affected** (number)
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