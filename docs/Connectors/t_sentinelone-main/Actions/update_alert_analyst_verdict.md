# Update Alert Analyst Verdict

**Description**: Updates the analyst's verdict on an alert in SentinelOne using specific data and filter criteria.

## Endpoint

- **URL:** `/web/api/v2.1/cloud-detection/alerts/analyst-verdict`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **filter** (object) – Required
    - **containerImageName__contains** (string): Free-text filter by the endpoint container image name (supports multiple values).
    - **limit** (number): Limit.
    - **reportedAt__gte** (string): Reported at greater or equal than.
    - **tenant** (boolean): Indicates a tenant scope request.
    - **reportedAt__lte** (string): Reported at lesser or equal than.
    - **sourceProcessName__contains** (string): Free-text filter by source process name.
    - **incidentStatus** (string): Filter threats by a incident status.
    - **sourceProcessCommandline__contains** (string): Free-text filter by source commandline.
    - **createdAt__lte** (string): Created at lesser or equal than.
    - **k8sNamespaceLabels__contains** (string): Free-text filter by the endpoint Kubernetes namespace labels (supports multiple values).
    - **k8sPod__contains** (string): Free-text filter by the endpoint Kubernetes pod name (supports multiple values).
    - **reportedAt__gt** (string): Reported at greater than.
    - **sourceProcessFileHashSha1__contains** (string): Free-text filter by source SHA1.
    - **k8sNode__contains** (string): Free-text filter by the endpoint Kubernetes node name (supports multiple values).
    - **createdAt__gt** (string): Created at greater than.
    - **origAgentUuid__contains** (string): Free-text filter by agent UUID.
    - **sourceProcessFileHashMd5__contains** (string): Free-text filter by source MD5
    - **query** (string): Full text search for all fields.
    - **osType** (string): Included OS types.
    - **containerName__contains** (string): Free-text filter by the endpoint container name (supports multiple values).
    - **analystVerdict** (string): Filter threats by a analyst verdict.
    - **createdAt__lt** (string): Created at lesser than.
    - **origAgentName__contains** (string): Free-text filter by agent name.
    - **ruleName__contains** (string): Free-text filter by rule name.
    - **origAgentOsRevision__contains** (string): Free-text filter by agent OS revision.
    - **sourceProcessFilePath__contains** (string): Free-text filter by source file path.
    - **k8sControllerLabels__contains** (string): Free-text filter by the endpoint Kubernetes controller labels (supports multiple values).
    - **siteIds** (string): List of Site IDs to filter by.
    - **containerLabels__contains** (string): Free-text filter by the endpoint container labels (supports multiple values).
    - **k8sNamespaceName__contains** (string): Free-text filter by the endpoint Kubernetes namespace name (supports multiple values).
    - **groupIds** (string): A list of Alert IDs.
    - **accountIds** (string): List of Account IDs to filter by.
    - **machineType** (string): Agent machine type.
    - **k8sControllerName__contains** (string): Free-text filter by the endpoint Kubernetes controller name (supports multiple values).
    - **severity** (string): Severity.
    - **k8sCluster__contains** (string): Free-text filter by the endpoint Kubernetes cluster name (supports multiple values).
    - **ids** (string): A list of Alert IDs.
    - **scopes** (string): Filter results by scope.
    - **createdAt__gte** (string): Created at greater or equal than.
    - **sourceProcessStoryline__contains** (string): Free-text filter by source storyline.
    - **origAgentVersion__contains** (string): Free-text filter by agent OS version.
    - **reportedAt__lt** (string): Reported at lesser than.
    - **k8sPodLabels__contains** (string): Free-text filter by the endpoint Kubernetes pod labels (supports multiple values).
    - **sourceProcessFileHashSha256__contains** (string): Free-text filter by source SHA255.
  - **data** (object) – Required
    - **analystVerdict** (string) – Required: Analyst verdict.
## Output

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