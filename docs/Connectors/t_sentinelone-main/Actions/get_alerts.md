# Get Alerts

**Description**: Retrieve a list of SentinelOne alerts to identify potential security threats within a specified scope.

## Endpoint

- **URL:** `/web/api/v2.1/cloud-detection/alerts`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **accountIds** (string): List of Account IDs to filter by.
  - **analystVerdict** (string): Filter threats by a analyst verdict.
  - **containerImageName__contains** (string): Free-text filter by the endpoint container image name (supports multiple values).
  - **containerLabels__contains** (string): Free-text filter by the endpoint container labels (supports multiple values).
  - **containerName__contains** (string): Free-text filter by the endpoint container name (supports multiple values).
  - **countOnly** (boolean): If true, only total number of items will be returned, without any of the actual objects.
  - **createdAt__gt** (string): Created at greater than.
  - **createdAt__gte** (string): Created at greater or equal than.
  - **createdAt__lt** (string): Created at lesser than.
  - **createdAt__lte** (string): Created at lesser or equal than.
  - **cursor** (string): Cursor position returned by the last request. Use to iterate over more than 1000 items.
  - **disablePagination** (boolean): If true, all rules for requested scope will be returned.
  - **groupIds** (string): List of Group IDs to filter by.
  - **ids** (array): A list of Alert IDs.
  - **incidentStatus** (string): Filter threats by a incident status.
  - **k8sCluster__contains** (string): Free-text filter by the endpoint Kubernetes cluster name (supports multiple values).
  - **k8sControllerLabels__contains** (string): Free-text filter by the endpoint Kubernetes controller labels (supports multiple values).
  - **k8sControllerName__contains** (string): Free-text filter by the endpoint Kubernetes controller name (supports multiple values).
  - **k8sNamespaceLabels__contains** (string): Free-text filter by the endpoint Kubernetes namespace labels (supports multiple values).
  - **k8sNamespaceName__contains** (string): Free-text filter by the endpoint Kubernetes namespace name (supports multiple values).
  - **k8sNode__contains** (string): Free-text filter by the endpoint Kubernetes node name (supports multiple values).
  - **k8sPod__contains** (string): Free-text filter by the endpoint Kubernetes pod name (supports multiple values).
  - **k8sPodLabels__contains** (string): Free-text filter by the endpoint Kubernetes pod labels (supports multiple values).
  - **limit** (number): Limit number of returned items (1-1000).
  - **machineType** (string): agent machine type.
  - **origAgentName__contains** (string): Free-text filter by agent name.
  - **origAgentOsRevision__contains** (string): Free-text filter by agent OS revision.
  - **origAgentUuid__contains** (string): Free-text filter by agent UUID.
  - **origAgentVersion__contains** (string): Free-text filter by agent OS version.
  - **osType** (string): Included OS types.
  - **query** (string): Full text search for all fields.
  - **reportedAt__gt** (string): Reported at greater than.
  - **reportedAt__gte** (string): Reported at greater or equal than.
  - **reportedAt__lt** (string): Reported at lesser than.
  - **reportedAt__lte** (string): Reported at lesser or equal than.
  - **ruleName__contains** (string): Free-text filter by rule name.
  - **scopes** (string): Filter results by scope.
  - **severity** (string): Severity
  - **siteIds** (string): List of Site IDs to filter by.
  - **skip** (number): Skip first number of items (0-1000). To iterate over more than 1000 items, use "cursor".
  - **skipCount** (boolean): If true, total number of items will not be calculated, which speeds up execution time.
  - **sortBy** (string): The column to sort the results by.
  - **sortOrder** (string): Sort direction.
  - **sourceProcessCommandline__contains** (string): Free-text filter by source commandline.
  - **sourceProcessFileHashMd5__contains** (string): Free-text filter by source MD5.
  - **sourceProcessFileHashSha1__contains** (string): Free-text filter by source SHA1.
  - **sourceProcessFileHashSha256__contains** (string): Free-text filter by source SHA255.
  - **sourceProcessFilePath__contains** (string): Free-text filter by source file path.
  - **sourceProcessName__contains** (string): Free-text filter by source process name.
  - **sourceProcessStoryline__contains** (string): Free-text filter by source storyline.
  - **tenant** (boolean): Indicates a tenant scope request.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (array)
    - **agentDetectionInfo** (object)
      - **accountId** (string)
      - **machineType** (object)
      - **name** (object)
      - **osFamily** (object)
      - **osName** (string)
      - **osRevision** (string)
      - **siteId** (object)
      - **uuid** (object)
      - **version** (object)
    - **alertInfo** (object)
      - **alertId** (string)
      - **analystVerdict** (string)
      - **createdAt** (string)
      - **dnsRequest** (object)
      - **dnsResponse** (object)
      - **dstIp** (object)
      - **dstPort** (object)
      - **dvEventId** (object)
      - **eventType** (object)
      - **hitType** (string)
      - **incidentStatus** (string)
      - **indicatorCategory** (object)
      - **indicatorDescription** (object)
      - **indicatorName** (object)
      - **isEdr** (boolean)
      - **loginAccountDomain** (object)
      - **loginAccountSid** (object)
      - **loginIsAdministratorEquivalent** (object)
      - **loginIsSuccessful** (object)
      - **loginType** (object)
      - **loginsUserName** (object)
      - **modulePath** (object)
      - **moduleSha1** (object)
      - **netEventDirection** (object)
      - **registryKeyPath** (object)
      - **registryOldValue** (object)
      - **registryOldValueType** (object)
      - **registryPath** (object)
      - **registryValue** (object)
      - **reportedAt** (string)
      - **source** (string)
      - **srcIp** (object)
      - **srcMachineIp** (object)
      - **srcPort** (object)
      - **tiIndicatorComparisonMethod** (object)
      - **tiIndicatorSource** (object)
      - **tiIndicatorType** (object)
      - **tiIndicatorValue** (object)
      - **updatedAt** (string)
    - **containerInfo** (object)
      - **id** (object)
      - **image** (object)
      - **labels** (object)
      - **name** (object)
    - **kubernetesInfo** (object)
      - **cluster** (object)
      - **controllerKind** (object)
      - **controllerLabels** (object)
      - **controllerName** (object)
      - **namespace** (object)
      - **namespaceLabels** (object)
      - **node** (object)
      - **pod** (object)
      - **podLabels** (object)
    - **ruleInfo** (object)
      - **description** (object)
      - **id** (string)
      - **name** (string)
      - **queryLang** (string)
      - **queryType** (string)
      - **s1ql** (string)
      - **scopeLevel** (string)
      - **severity** (string)
      - **treatAsThreat** (string)
    - **sourceParentProcessInfo** (object)
      - **commandline** (object)
      - **effectiveUser** (object)
      - **fileHashMd5** (object)
      - **fileHashSha1** (object)
      - **fileHashSha256** (object)
      - **filePath** (object)
      - **fileSignerIdentity** (object)
      - **integrityLevel** (string)
      - **loginUser** (object)
      - **name** (object)
      - **pid** (object)
      - **pidStarttime** (string)
      - **realUser** (object)
      - **storyline** (object)
      - **subsystem** (string)
      - **uniqueId** (object)
      - **user** (string)
    - **sourceProcessInfo** (object)
      - **commandline** (object)
      - **effectiveUser** (object)
      - **fileHashMd5** (object)
      - **fileHashSha1** (object)
      - **fileHashSha256** (object)
      - **filePath** (object)
      - **fileSignerIdentity** (object)
      - **integrityLevel** (string)
      - **loginUser** (object)
      - **name** (object)
      - **pid** (object)
      - **pidStarttime** (string)
      - **realUser** (object)
      - **storyline** (object)
      - **subsystem** (string)
      - **uniqueId** (object)
      - **user** (string)
    - **targetProcessInfo** (object)
      - **tgtFileCreatedAt** (string)
      - **tgtFileHashSha1** (object)
      - **tgtFileHashSha256** (object)
      - **tgtFileId** (object)
      - **tgtFileIsSigned** (object)
      - **tgtFileModifiedAt** (string)
      - **tgtFileOldPath** (object)
      - **tgtFilePath** (object)
      - **tgtProcCmdLine** (object)
      - **tgtProcImagePath** (object)
      - **tgtProcIntegrityLevel** (string)
      - **tgtProcName** (object)
      - **tgtProcPid** (object)
      - **tgtProcSignedStatus** (object)
      - **tgtProcStorylineId** (object)
      - **tgtProcUid** (object)
      - **tgtProcessStartTime** (string)
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