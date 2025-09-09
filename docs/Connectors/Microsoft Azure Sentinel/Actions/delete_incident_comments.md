# Delete Incident Comments

**Description**: Removes a specific comment from an incident in Microsoft Azure Sentinel using unique identifiers like incidentCommentId and incidentId.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/comments/{{incidentCommentId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **incidentCommentId** (string) – Required: Incident comment ID.
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern is ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$.
  - **incidentId** (string) – Required: Incident ID.
- **parameters** (object) – Required
  - **api-version** (string) – Required: The API version to use for this operation.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)