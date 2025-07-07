# Fetch Threat File

**Description**: Retrieves a file associated with a threat in SentinelOne using specified filters. 'Fetch Threat File' permissions required.

## Endpoint

- **URL:** `/web/api/v2.1/threats/fetch-file`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **data** (object) – Required
    - **password** (string) – Required: File encryption password.
  - **filter** (object) – Required: Use any of the filtering options to control the list of affected threats. You can use any combination of filters to narrow down the list (For example "apply to only active threats from Linux endpoints"). You can also leave this field empty to apply to all available threats. Note - Filter must match exactly one threat. Bulk operations are not supported.
    - **accountIds** (string): List of Account IDs to filter by.
    - **agentIds** (string): List of Agent IDs.
    - **agentIsActive** (boolean): Include Agents currently connected to the Management Console.
    - **agentMachineTypes** (string): Include Agent machine types.
    - **agentMachineTypesNin** (string): Excluded Agent machine types.
    - **agentTagsData** (string): Filter threats by assigned tags to the related agent. Given in form of a JSON where each key represents a tag key, and each value represents a list of string values to filter by. To filter by unassigned tag values, use __nin suffix in the tag key.
    - **agentVersions** (string): Include Agent versions.
    - **agentVersionsNin** (string): Excluded Agent versions.
    - **analystVerdicts** (string): Filter threats by a specific analyst verdict.
    - **analystVerdictsNin** (string): Exclude threats with specific analyst verdicts.
    - **awsRole__contains** (string): Free-text filter by aws role(supports multiple values).
    - **awsSecurityGroups__contains** (string): Free-text filter by aws securityGroups(supports multiple values).
    - **awsSubnetIds__contains** (string): Free-text filter by aws subnet ids (supports multiple values).
    - **azureResourceGroup__contains** (string): Free-text filter by azure resource group(supports multiple values).
    - **classifications** (string): List of threat classifications to search.
    - **classificationsNin** (string): List of threat classifications not to search.
    - **classificationSources** (string): Classification sources list.
    - **classificationSourcesNin** (string): Classification sources list to exclude.
    - **cloudAccount__contains** (string): Free-text filter by cloud account (supports multiple values).
    - **cloudImage__contains** (string): Free-text filter by cloud image (supports multiple values).
    - **cloudInstanceId__contains** (string): Free-text filter by cloud instance id(supports multiple values).
    - **cloudInstanceSize__contains** (string): Free-text filter by cloud instance size(supports multiple values).
    - **cloudLocation__contains** (string): Free-text filter by cloud location (supports multiple values).
    - **cloudNetwork__contains** (string): Free-text filter by cloud network (supports multiple values).
    - **cloudProvider** (string): Agents from which cloud provider.
    - **cloudProviderNin** (string): Exclude Agents from these cloud provider.
    - **collectionIds** (string): List of collection IDs to search.
    - **commandLineArguments__contains** (string): Free-text filter by threat command line arguments (supports multiple values).
    - **computerName__contains** (string): Free-text filter by computer name (supports multiple values).
    - **confidenceLevels** (string): Filter threats by a specific confidence level.
    - **confidenceLevelsNin** (string): Exclude threats with specific confidence level.
    - **containerImageName__contains** (string): Free-text filter by the endpoint container image name (supports multiple values).
    - **containerLabels__contains** (string): Free-text filter by the endpoint container labels (supports multiple values).
    - **containerName__contains** (string): Free-text filter by the endpoint container name (supports multiple values).
    - **contentHash__contains** (string): Free-text filter by file content hash (supports multiple values).
    - **contentHashes** (string): List of sha1 hashes to search for.
    - **countsFor** (string): comma-separated list of fields to be shown.
    - **createdAt__gt** (string): Created at greater than.
    - **createdAt__gte** (string): Created at greater or equal than.
    - **createdAt__lt** (string): Created at lesser than.
    - **createdAt__lte** (string): Created at lesser or equal than.
    - **detectionAgentDomain__contains** (string): Free-text filter by Agent domain at detection time (supports multiple values).
    - **detectionAgentVersion__contains** (string): Free-text filter by Agent version at detection time (supports multiple values).
    - **detectionEngines** (string): Included engines.
    - **detectionEnginesNin** (string): Excluded engines.
    - **displayName** (string): Display name.
    - **engines** (string): Included engines.
    - **enginesNin** (string): Excluded engines.
    - **externalTicketExists** (boolean): The threat contains ticket number.
    - **externalTicketId__contains** (string): Free-text filter by the threat external ticket ID (supports multiple values).
    - **externalTicketIds** (string): External ticket ID for the threat.
    - **failedActions** (string): At least one action failed on the threat.
    - **filePath__contains** (string): Free-text filter by file path (supports multiple values).
    - **gcpServiceAccount__contains** (string): Free-text filter by gcp service account (supports multiple values).
    - **groupIds** (string): List of Group IDs to filter by.
    - **hasAgentTags** (boolean): Include only Threats whose Agent is assigned any tags if True, or none if False.
    - **ids** (string): List of threat IDs.
    - **incidentStatuses** (string): Filter threats by a specific incident status.
    - **incidentStatusesNin** (string): Exclude threats with specific incident statuses.
    - **initiatedBy** (string): Only include threats from specific initiating sources.
    - **initiatedByNin** (string): Exclude threats with specific initiating sources.
    - **initiatedByUsername__contains** (string): Free-text filter by the username that initiated that threat (supports multiple values).
    - **k8sClusterName__contains** (string): Free-text filter by the endpoint Kubernetes cluster name (supports multiple values).
    - **k8sControllerLabels__contains** (string): Free-text filter by the endpoint Kubernetes controller labels (supports multiple values).
    - **k8sControllerName__contains** (string): Free-text filter by the endpoint Kubernetes controller name (supports multiple values).
    - **k8sNamespaceLabels__contains** (string): Free-text filter by the endpoint Kubernetes namespace labels (supports multiple values).
    - **k8sNamespaceName__contains** (string): Free-text filter by the endpoint Kubernetes namespace name (supports multiple values).
    - **k8sNodeLabels__contains** (string): Free-text filter by the endpoint Kubernetes node labels (supports multiple values).
    - **k8sNodeName__contains** (string): Free-text filter by the endpoint Kubernetes node name (supports multiple values).
    - **k8sPodLabels__contains** (string): Free-text filter by the endpoint Kubernetes pod labels (supports multiple values).
    - **k8sPodName__contains** (string): Free-text filter by the endpoint Kubernetes pod name (supports multiple values).
    - **mitigatedPreemptively** (boolean): If the threat was detected pre-execution or post-execution.
    - **mitigationStatuses** (string): Filter threats by a specific status.
    - **mitigationStatusesNin** (string): Filter threats not by a specific status.
    - **noteExists** (boolean): The threat contains at least one note.
    - **originatedProcess__contains** (string): Free-text filter by the originated process name of the threat (supports multiple values).
    - **osArchs** (string): Included OS Architectures.
    - **osNames** (string): OS Names.
    - **osNamesNin** (string): OS Names Nin.
    - **osTypes** (string): Included OS types.
    - **osTypesNin** (string): Excluded OS types.
    - **pendingActions** (boolean): At least one action is pending for the Agent for the threat.
    - **publisherName__contains** (string): Free-text filter by threat's publisher name (supports multiple values).
    - **query** (string): Full text search for fields like threat_details, content_hash, computer_name, file_path, uuid, detection_agent_version, realtime_agent_version, detection_agent_domain, command_line_arguments, initiated_by_username, storyline, originated_process, k8s_cluster_name, k8s_node_name, k8s_node_labels, k8s_namespace_name, k8s_namespace_labels, k8s_controller_name, k8s_controller_labels, k8s_pod_name, k8s_pod_labels, container_name, container_image_name, container_labels, external_ticket_id.
    - **realtimeAgentVersion__contains** (string): Free-text filter by Agent version at current time (supports multiple values).
    - **rebootRequired** (boolean): A reboot is required on any endpoint for at least one action on the threat.
    - **resolved** (boolean): This is used for backward-compatibility with API 2.0.
    - **siteIds** (string): List of Site IDs to filter by.
    - **storyline__contains** (string): Free-text filter by threat storyline (supports multiple values).
    - **storylines** (array): List of Agent context to search for.
    - **tenant** (boolean): Indicates a tenant scope request.
    - **threatDetails__contains** (string): Free-text filter by threat details(supports multiple values).
    - **updatedAt__gt** (string): Updated at greater than.
    - **updatedAt__gte** (string): Updated at greater or equal than.
    - **updatedAt__lt** (string): Updated at lesser than.
    - **updatedAt__lte** (string): Updated at lesser or equal than.
    - **uuid__contains** (string): Free-text filter by Agent UUID (supports multiple values).
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