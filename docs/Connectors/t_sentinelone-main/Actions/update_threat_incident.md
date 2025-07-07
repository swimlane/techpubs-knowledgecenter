# Update Threat Incident

**Description**: Updates a threat incident's details in SentinelOne based on provided data and filter criteria.

## Endpoint

- **URL:** `/web/api/v2.1/threats/incident`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **data** (object) – Required
    - **incidentStatus** (string) – Required: Incident status to update for the threat.
    - **analystVerdict** (string): The analyst verdict to set for the threat.
  - **filter** (object) – Required
    - **createdAt__lt** (string): Created at lesser than.
    - **createdAt__gt** (string): Created at greater than.
    - **updatedAt__gt** (string): Updated at greater than.
    - **updatedAt__lt** (string): Updated at lesser than.
    - **ids** (array): List of threat IDs.
    - **groupIds** (array): List of Group IDs to filter by.
    - **siteIds** (array): List of Site IDs to filter by.
    - **accountIds** (array): List of Account IDs to filter by.
    - **incidentStatuses** (array): Filter threats by a specific incident status.
    - **classificationSources** (array): Classification sources list.
    - **classifications** (array): List of threat classifications to search.
    - **agentIds** (array): List of Agent IDs.
    - **osTypes** (array): Included OS types.
    - **enginesNin** (array): Excluded engines.
    - **osTypesNin** (array): Excluded OS types.
    - **containerImageName__contains** (array): Free-text filter by the endpoint container image name (supports multiple values).
    - **k8sNodeName__contains** (array): Free-text filter by the endpoint Kubernetes node name (supports multiple values).
    - **k8sNamespaceName__contains** (array): Free-text filter by the endpoint Kubernetes namespace name (supports multiple values).
    - **analystVerdicts** (array): Filter threats by a specific analyst verdict.
    - **agentIsActive** (boolean): Include Agents currently connected to the Management Console.
    - **agentMachineTypes** (array): Include Agent machine types.
    - **agentMachineTypesNin** (array): Excluded Agent machine types.
    - **agentTagsData** (string): Filter threats by assigned tags to the related agent. Given in form of a JSON where each key represents a tag key, and each value represents a list of string values to filter by. To filter by unassigned tag values, use __nin suffix in the tag key.
    - **agentVersions** (array): Include Agent versions.
    - **agentVersionsNin** (array): Excluded Agent versions.
    - **analystVerdictsNin** (array): Exclude threats with specific analyst verdicts.
    - **awsRole__contains** (array): Free-text filter by AWS role (supports multiple values).
    - **awsSecurityGroups__contains** (array): Free-text filter by AWS security groups (supports multiple values).
    - **awsSubnetIds__contains** (array): Free-text filter by AWS subnet IDs (supports multiple values).
    - **azureResourceGroup__contains** (array): Free-text filter by azure resource group (supports multiple values).
    - **classificationsNin** (array): List of threat classifications not to search.
    - **classificationSourcesNin** (array): Classification sources list to exclude.
    - **cloudAccount__contains** (array): Free-text filter by cloud account (supports multiple values).
    - **cloudImage__contains** (array): Free-text filter by cloud image (supports multiple values).
    - **cloudInstanceId__contains** (array): Free-text filter by cloud instance id (supports multiple values).
    - **cloudInstanceSize__contains** (array): Free-text filter by cloud instance size (supports multiple values).
    - **cloudLocation__contains** (array): Free-text filter by cloud location (supports multiple values).
    - **cloudNetwork__contains** (array): Free-text filter by cloud network (supports multiple values).
    - **cloudProvider** (array): Agents from which cloud provider.
    - **cloudProviderNin** (array): Exclude Agents from these cloud providers.
    - **collectionIds** (array): List of collection IDs to search.
    - **commandLineArguments__contains** (array): Free-text filter by threat command line arguments (supports multiple values).
    - **computerName__contains** (array): Free-text filter by computer name (supports multiple values).
    - **confidenceLevels** (array): Filter threats by a specific confidence level.
    - **confidenceLevelsNin** (array): Exclude threats with specific confidence levels.
    - **containerLabels__contains** (array): Free-text filter by the endpoint container labels (supports multiple values).
    - **containerName__contains** (array): Free-text filter by the endpoint container name (supports multiple values).
    - **contentHash__contains** (array): Free-text filter by file content hash (supports multiple values).
    - **contentHashes** (array): List of sha1 hashes to search for.
    - **countsFor** (string): Comma-separated list of fields to be shown.
    - **detectionAgentDomain__contains** (array): Free-text filter by Agent domain at detection time (supports multiple values).
    - **detectionAgentVersion__contains** (array): Free-text filter by Agent version at detection time (supports multiple values).
    - **detectionEngines** (array): Included engines.
    - **detectionEnginesNin** (array): Excluded engines.
    - **displayName** (string): Display name.
    - **engines** (array): Included engines.
    - **externalTicketExists** (boolean): The threat contains ticket number.
    - **externalTicketId__contains** (array): Free-text filter by the threat external ticket ID (supports multiple values).
    - **externalTicketIds** (array): External ticket ID for the threat.
    - **failedActions** (boolean): At least one action failed on the threat.
    - **filePath__contains** (array): Free-text filter by file path (supports multiple values).
    - **gcpServiceAccount__contains** (array): Free-text filter by GCP service account (supports multiple values).
    - **hasAgentTags** (boolean): Include only Threats whose Agent is assigned any tags if True, or none if False.
    - **initiatedBy** (array): Only include threats from specific initiating sources.
    - **initiatedByNin** (array): Exclude threats with specific initiating sources.
    - **initiatedByUsername__contains** (array): Free-text filter by the username that initiated that threat (supports multiple values).
    - **k8sClusterName__contains** (array): Free-text filter by the endpoint Kubernetes cluster name (supports multiple values).
    - **k8sControllerLabels__contains** (array): Free-text filter by the endpoint Kubernetes controller labels (supports multiple values).
    - **k8sControllerName__contains** (array): Free-text filter by the endpoint Kubernetes controller name (supports multiple values).
    - **k8sNamespaceLabels__contains** (array): Free-text filter by the endpoint Kubernetes namespace labels (supports multiple values).
    - **k8sNodeLabels__contains** (array): Free-text filter by the endpoint Kubernetes node labels (supports multiple values).
    - **k8sPodLabels__contains** (array): Free-text filter by the endpoint Kubernetes pod labels (supports multiple values).
    - **k8sPodName__contains** (array): Free-text filter by the endpoint Kubernetes pod name (supports multiple values).
    - **limit** (number): Limit.
    - **mitigatedPreemptively** (boolean): If the threat was detected pre-execution or post-execution.
    - **mitigationStatuses** (array): Filter threats by a specific status.
    - **mitigationStatusesNin** (array): Filter threats not by a specific status.
    - **noteExists** (boolean): The threat contains at least one note.
    - **originatedProcess__contains** (array): Free-text filter by the originated process name of the threat (supports multiple values).
    - **osArchs** (array): Included OS Architectures.
    - **osNames** (array): OS names.
    - **osNamesNin** (array): OS names to exclude.
    - **pendingActions** (boolean): At least one action is pending for the Agent for the threat.
    - **publisherName__contains** (array): Free-text filter by threat's publisher name (supports multiple values).
    - **query** (string): Full text search for fields- threat_details, content_hash, computer_name, file_path, uuid, detection_agent_version, realtime_agent_version, detection_agent_domain, command_line_arguments, initiated_by_username, storyline, originated_process, k8s_cluster_name, k8s_node_name, k8s_node_labels, k8s_namespace_name, k8s_namespace_labels, k8s_controller_name, k8s_controller_labels, k8s_pod_name, k8s_pod_labels, container_name, container_image_name, container_labels, external_ticket_id.
    - **realtimeAgentVersion__contains** (array): Free-text filter by Agent version at current time (supports multiple values).
    - **rebootRequired** (boolean): A reboot is required on any endpoint for at least one action on the threat.
    - **resolved** (boolean): Used for backward-compatibility with API 2.0.
    - **storyline__contains** (array): Free-text filter by threat storyline (supports multiple values).
    - **storylines** (array): List of Agent context to search for.
    - **tenant** (boolean): Indicates a tenant scope request.
    - **threatDetails__contains** (array): Free-text filter by threat details (supports multiple values).
    - **uuid__contains** (array): Free-text filter by Agent UUID (supports multiple values).
    - **createdAt__gte** (string): Created at greater or equal than.
    - **createdAt__lte** (string): Created at lesser or equal than.
    - **updatedAt__gte** (string): Updated at greater or equal than.
    - **updatedAt__lte** (string): Updated at lesser or equal than.
    - **incidentStatusesNin** (array): Exclude threats with specific incident statuses.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **data** (object)
    - **affected** (number)
    - **details** (array)
      - **result** (string)
      - **analystVerdict** (string)
      - **threatId** (string)
  - **errors** (object)
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