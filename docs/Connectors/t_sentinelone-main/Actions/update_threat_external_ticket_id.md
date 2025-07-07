# Update Threat External Ticket ID

**Description**: Change the external ticket ID for a specified threat in SentinelOne with a JSON body input.

## Endpoint

- **URL:** `web/api/v2.1/threats/external-ticket-id`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **filter** (object)
    - **accountIds** (array)
    - **osArchs** (array)
    - **agentMachineTypes** (array)
    - **commandLineArguments__contains** (array)
    - **cloudImage__contains** (array)
    - **limit** (number)
    - **contentHashes** (string)
    - **tenant** (boolean)
    - **ids** (array)
    - **createdAt__lte** (string)
    - **noteExists** (boolean)
    - **k8sPodName__contains** (array)
    - **updatedAt__gte** (string)
    - **updatedAt__lt** (string)
    - **containerImageName__contains** (array)
    - **classificationSources** (array)
    - **confidenceLevels** (array)
    - **cloudAccount__contains** (array)
    - **classificationsNin** (array)
    - **k8sControllerLabels__contains** (array)
    - **osTypes** (array)
    - **osNamesNin** (array)
    - **realtimeAgentVersion__contains** (array)
    - **awsSecurityGroups__contains** (array)
    - **mitigatedPreemptively** (boolean)
    - **siteIds** (array)
    - **awsRole__contains** (array)
    - **detectionAgentDomain__contains** (array)
    - **agentIds** (array)
    - **storylines** (array)
    - **createdAt__lt** (string)
    - **gcpServiceAccount__contains** (array)
    - **failedActions** (boolean)
    - **collectionIds** (array)
    - **pendingActions** (boolean)
    - **query** (string)
    - **externalTicketId__contains** (array)
    - **storyline__contains** (array)
    - **initiatedByNin** (array)
    - **cloudNetwork__contains** (array)
    - **externalTicketIds** (array)
    - **cloudProviderNin** (array)
    - **displayName** (string)
    - **countsFor** (string)
    - **analystVerdicts** (array)
    - **detectionEnginesNin** (array)
    - **contentHash__contains** (array)
    - **confidenceLevelsNin** (array)
    - **computerName__contains** (array)
    - **threatDetails__contains** (array)
    - **initiatedBy** (array)
    - **containerName__contains** (array)
    - **osTypesNin** (array)
    - **azureResourceGroup__contains** (array)
    - **detectionAgentVersion__contains** (array)
    - **awsSubnetIds__contains** (array)
    - **cloudProvider** (array)
    - **agentIsActive** (boolean)
    - **groupIds** (array)
    - **cloudInstanceId__contains** (array)
    - **incidentStatuses** (array)
    - **updatedAt__gt** (string)
    - **containerLabels__contains** (array)
    - **agentVersionsNin** (array)
    - **rebootRequired** (boolean)
    - **createdAt__gte** (string)
    - **detectionEngines** (array)
    - **classifications** (array)
    - **k8sNamespaceLabels__contains** (array)
    - **filePath__contains** (array)
    - **agentVersions** (array)
    - **agentMachineTypesNin** (array)
    - **analystVerdictsNin** (array)
    - **mitigationStatuses** (array)
    - **k8sNodeName__contains** (array)
    - **k8sControllerName__contains** (array)
    - **initiatedByUsername__contains** (array)
    - **originatedProcess__contains** (array)
    - **k8sClusterName__contains** (array)
    - **k8sPodLabels__contains** (array)
    - **classificationSourcesNin** (array)
    - **mitigationStatusesNin** (array)
    - **engines** (array)
    - **k8sNamespaceName__contains** (array)
    - **uuid__contains** (array)
    - **cloudLocation__contains** (array)
    - **enginesNin** (array)
    - **incidentStatusesNin** (array)
    - **resolved** (boolean)
    - **externalTicketExists** (boolean)
    - **cloudInstanceSize__contains** (array)
    - **createdAt__gt** (string)
    - **publisherName__contains** (array)
    - **osNames** (array)
    - **updatedAt__lte** (string)
  - **data** (object)
    - **externalTicketId** (string)
## Output

### Example

```json
[
  {
    "status_code": 500,
    "response_headers": {
      "Server": "nginx",
      "Date": "Wed, 16 Nov 2022 20:32:59 GMT",
      "Content-Type": "application/json",
      "Content-Length": "111",
      "Connection": "keep-alive",
      "Access-Control-Allow-Origin": "https://attivo-us.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com cdn.pendo.io *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com ; img-src 'self' data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.sentinelone.com *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' app.pendo.io cdn.pendo.io *.storage.googleapis.com https://fonts.googleapis.com https://cdnjs.cloudflare.com ; font-src 'self' data: https://fonts.gstatic.com https://cdn.auth0.com ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com ; frame-ancestors 'self' app.pendo.io ; object-src 'none'"
    },
    "reason": "INTERNAL SERVER ERROR",
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
| Content-Length | string |
| Connection | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Allow-Credentials | string |
| Vary | string |
| Strict-Transport-Security | string |
| X-Frame-Options | string |
| X-Content-Type-Options | string |
| Content-Security-Policy | string |