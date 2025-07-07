# Delete Alert Rules

**Description**: Removes specified alert rules from Microsoft Azure Sentinel using subscription ID, resource group, workspace name, and rule ID.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/alertRules/{{ruleId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **ruleId** (string) – Required: Alert rule ID.
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$.
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