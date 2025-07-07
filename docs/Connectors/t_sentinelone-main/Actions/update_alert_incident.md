# Update Alert Incident

**Description**: Updates an alert's incident details in SentinelOne using specified data and filter criteria.

## Endpoint

- **URL:** `/web/api/v2.1/cloud-detection/alerts/incident`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **filter** (object) – Required
    - **containerImageName__contains** (array): Free-text filter by the endpoint container image name (supports multiple values).
    - **limit** (number): Limit.
    - **reportedAt__gte** (string): Reported at greater or equal than.
    - **tenant** (boolean): Indicates a tenant scope request.
    - **reportedAt__lte** (string): Reported at lesser or equal than.
    - **sourceProcessName__contains** (array): Free-text filter by source process name.
    - **incidentStatus** (array): Filter threats by a incident status.
    - **sourceProcessCommandline__contains** (array): Free-text filter by source commandline.
    - **createdAt__lte** (string): Created at lesser or equal than.
    - **k8sNamespaceLabels__contains** (array): Free-text filter by the endpoint Kubernetes namespace labels (supports multiple values).
    - **k8sPod__contains** (array): Free-text filter by the endpoint Kubernetes pod name (supports multiple values).
    - **reportedAt__gt** (string): Reported at greater than.
    - **sourceProcessFileHashSha1__contains** (array): Free-text filter by source sha1.
    - **k8sNode__contains** (array): Free-text filter by the endpoint Kubernetes node name (supports multiple values).
    - **createdAt__gt** (string): Created at greater than.
    - **origAgentUuid__contains** (array): Free-text filter by agent UUID.
    - **sourceProcessFileHashMd5__contains** (array): Free-text filter by source MD5.
    - **query** (string): Full text search for all fields.
    - **osType** (array): Included OS types.
    - **containerName__contains** (array): Free-text filter by the endpoint container name (supports multiple values).
    - **analystVerdict** (array): Filter threats by a analyst verdict.
    - **createdAt__lt** (string): Created at lesser than.
    - **origAgentName__contains** (array): Free-text filter by agent name.
    - **ruleName__contains** (array): Free-text filter by rule name
    - **origAgentOsRevision__contains** (array): Free-text filter by agent OS revision.
    - **sourceProcessFilePath__contains** (array): Free-text filter by source file path.
    - **k8sControllerLabels__contains** (array): Free-text filter by the endpoint Kubernetes controller labels (supports multiple values).
    - **siteIds** (array): List of Site IDs to filter by.
    - **containerLabels__contains** (array): Free-text filter by the endpoint container labels (supports multiple values).
    - **k8sNamespaceName__contains** (array): Free-text filter by the endpoint Kubernetes namespace name (supports multiple values).
    - **groupIds** (array): List of Group IDs to filter by.
    - **accountIds** (array): List of Account IDs to filter by.
    - **machineType** (array): agent machine type
    - **k8sControllerName__contains** (array): Free-text filter by the endpoint Kubernetes controller name (supports multiple values).
    - **severity** (array): Severity.
    - **k8sCluster__contains** (array): Free-text filter by the endpoint Kubernetes cluster name (supports multiple values).
    - **ids** (array): A list of Alert IDs.
    - **scopes** (array): Filter results by scope.
    - **createdAt__gte** (string): Created at greater or equal than.
    - **sourceProcessStoryline__contains** (array): Free-text filter by source storyline.
    - **origAgentVersion__contains** (array): Free-text filter by agent OS version.
    - **reportedAt__lt** (string): Reported at lesser than.
    - **k8sPodLabels__contains** (array): Free-text filter by the endpoint Kubernetes pod labels (supports multiple values).
    - **sourceProcessFileHashSha256__contains** (array): Free-text filter by source sha255.
  - **data** (object) – Required
    - **incidentStatus** (string) – Required: Free-text filter by the endpoint container image name (supports multiple values).
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Server": "nginx",
      "Date": "Thu, 18 Apr 2024 00:12:38 GMT",
      "Content-Type": "application/json",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "X-RQID": "d281729a-04f6-40d4-aeef-5f0add7d40a3",
      "Access-Control-Allow-Origin": "https://cns-us-east-1-prod.sentinelone.net",
      "Access-Control-Allow-Credentials": "true",
      "Vary": "Origin",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Frame-Options": "SAMEORIGIN",
      "X-Content-Type-Options": "nosniff",
      "Content-Security-Policy": "default-src 'self' ; connect-src 'self' *.sentinelone.net cdn.pendo.io app.pendo.io *.pendo.io data.pendo.io *.scalyr.com *.storage.googleapis.com sentry.io *.sentry.io *.google-analytics.com *.gstatic.com unpkg.com cdn.auth0.com wss://*.sentinelone.net https://www.googletagmanager.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net data: ; script-src 'self' 'unsafe-inline' 'unsafe-eval' *.sentinelone.net cdn.pendo.io app.pendo.io pendo-io-static.storage.googleapis.com *.storage.googleapis.com data.pendo.io https://www.google-analytics.com https://www.googletagmanager.com https://unpkg.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; img-src 'self' *.sentinelone.net *.sentinelone.com dm64t97qsxvuz.cloudfront.net data: https://www.google-analytics.com cdn.pendo.io app.pendo.io *.storage.googleapis.com data.pendo.io ; style-src 'self' 'unsafe-inline' *.sentinelone.net app.pendo.io cdn.pendo.io *.storage.googleapis.com https://cdnjs.cloudflare.com https://dm64t97qsxvuz.cloudfront.net ; font-src 'self' data: *.sentinelone.net https://cdn.auth0.com https://dm64t97qsxvuz.cloudfront.net ; manifest-src 'self' https://dm64t97qsxvuz.cloudfront.net ; frame-src 'self' blob: https://receptive.io https://*.pendo.io https://pendo-io-extensions.storage.googleapis.com/ https://*.youtube.com *.sentinelone.net *.scalyr.com; frame-ancestors 'self' app.pendo.io *.sentinelone.net; object-src 'none'",
      "Cache-Control": "no-store",
      "Pragma": "no-cache",
      "Expires": "-1",
      "Content-Encoding": "gzip"
    },
    "reason": "OK",
    "json_body": {
      "data": {
        "affected": 3
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