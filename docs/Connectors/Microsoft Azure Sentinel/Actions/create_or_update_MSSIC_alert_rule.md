# Create or Update MSSIC Alert Rule

**Description**: Create or update a Microsoft Security Incident Creation alert rule in Azure Sentinel, including subscription, resource group, workspace, and rule specifics.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/alertRules/{{ruleId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$.
  - **ruleId** (string) – Required: Alert rule ID.
- **parameters** (object) – Required
  - **api-version** (string) – Required: The API version to use for this operation.
- **json_body** (object) – Required
  - **etag** (string)
  - **kind** (string)
  - **properties** (object) – Required
    - **productFilter** (string) – Required
    - **displayName** (string) – Required: The display name for alerts created by this alert rule.
    - **enabled** (boolean) – Required: Determines whether this alert rule is enabled or disabled.
    - **alertRuleTemplateName** (string): The Name of the alert rule template used to create this rule.
    - **description** (string): The description of the alert rule.
    - **displayNamesExcludeFilter** (array): The alerts' displayNames on which the cases will not be generated.
    - **displayNamesFilter** (array): The alerts' displayNames on which the cases will be generated.
    - **severitiesFilter** (array): The alerts' severities on which the cases will be generated.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/microsoftSecurityIncidentCreationRuleExample",
      "name": "microsoftSecurityIncidentCreationRuleExample",
      "etag": "\"260097e0-0000-0d00-0000-5d6fa88f0000\"",
      "type": "Microsoft.SecurityInsights/alertRules",
      "kind": "MicrosoftSecurityIncidentCreation",
      "properties": {
        "productFilter": "Microsoft Cloud App Security",
        "severitiesFilter": null,
        "displayNamesFilter": null,
        "displayName": "testing displayname",
        "enabled": true,
        "description": null,
        "alertRuleTemplateName": null,
        "lastModifiedUtc": "2019-09-04T12:05:35.7296311Z"
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **name** (string)
  - **etag** (string)
  - **type** (string)
  - **kind** (string)
  - **properties** (object)
    - **productFilter** (string)
    - **severitiesFilter** (object)
    - **displayNamesFilter** (object)
    - **displayName** (string)
    - **enabled** (boolean)
    - **description** (object)
    - **alertRuleTemplateName** (object)
    - **lastModifiedUtc** (string)