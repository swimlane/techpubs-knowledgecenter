# Create or Update Scheduled Alert Rule

**Description**: Create or update a ScheduledAlertRule in Microsoft Azure Sentinel with subscription, resource group, workspace details, and rule ID.

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
  - **kind** (string): The alert rule kind.
  - **etag** (string): Etag of the azure resource.
  - **properties** (object) – Required
    - **alertRuleTemplateName** (string): The Name of the alert rule template used to create this rule.
    - **displayName** (string) – Required: The display name for alerts created by this alert rule.
    - **description** (string): The description of the alert rule.
    - **severity** (string) – Required: The severity for alerts created by this alert rule.
    - **enabled** (boolean) – Required: Determines whether this alert rule is enabled or disabled.
    - **tactics** (array): The tactics of the alert rule.
    - **techniques** (array): The techniques of the alert rule.
    - **templateVersion** (string): The version of the alert rule template used to create this rule - in format <a.b.c>, where all are numbers, for example 0 <1.0.2>.
    - **query** (string) – Required: The query that creates alerts for this rule.
    - **queryFrequency** (string) – Required: The frequency (in ISO 8601 duration format) for this alert rule to run.
    - **queryPeriod** (string) – Required: The period (in ISO 8601 duration format) that this alert rule looks at.
    - **triggerOperator** (string) – Required: The operation against the threshold that triggers alert rule.
    - **triggerThreshold** (number) – Required: The threshold triggers this alert rule.
    - **suppressionDuration** (string) – Required: The suppression (in ISO 8601 duration format) to wait since last time this alert rule been triggered.
    - **suppressionEnabled** (boolean) – Required: Determines whether the suppression for this alert rule is enabled or disabled.
    - **eventGroupingSettings** (object): The event grouping settings.
      - **aggregationKind** (string): The event grouping aggregation kinds.
    - **customDetails** (object): Dictionary of string key-value pairs of columns to be attached to the alert.
    - **entityMappings** (array): Array of the entity mappings of the alert rule.
      - **entityType** (string): The V3 type of the mapped entity.
      - **fieldMappings** (array): Array of field mappings for the given entity mapping.
        - **identifier** (string): The V3 identifier of the entity.
        - **columnName** (string): The column name to be mapped to the identifier.
    - **alertDetailsOverride** (object): The alert details override settings.
      - **alertDisplayNameFormat** (string): The format containing columns name(s) to override the alert description.
      - **alertDescriptionFormat** (string): The format containing columns name(s) to override the alert name.
      - **alertDynamicProperties** (array): List of additional dynamic properties to override.
        - **alertProperty** (string)
        - **value** (string)
      - **alertSeverityColumnName** (string): The column name to take the alert severity from.
      - **alertTacticsColumnName** (string): The column name to take the alert tactics from.
    - **incidentConfiguration** (object): The settings of the incidents that created from alerts triggered by this analytics rule.
      - **createIncident** (boolean): Create incidents from alerts triggered by this analytics rule.
      - **groupingConfiguration** (object): Set how the alerts that are triggered by this analytics rule, are grouped into incidents.
        - **enabled** (boolean): Grouping enabled.
        - **reopenClosedIncident** (boolean): Re-open closed matching incidents.
        - **lookbackDuration** (string): Limit the group to alerts created within the lookback duration (in ISO 8601 duration format).
        - **matchingMethod** (string): Grouping matching method. When method is Selected at least one of groupByEntities, groupByAlertDetails, groupByCustomDetails must be provided and not empty.
        - **groupByEntities** (array): A list of entity types to group by (when matchingMethod is Selected). Only entities defined in the current alert rule may be used.
        - **groupByAlertDetails** (array): A list of alert details to group by (when matchingMethod is Selected).
        - **groupByCustomDetails** (array): A list of custom details keys to group by (when matchingMethod is Selected). Only keys defined in the current alert rule may be used.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/alertRules",
      "kind": "Scheduled",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
      "properties": {
        "alertRuleTemplateName": null,
        "displayName": "My scheduled rule",
        "description": "An example for a scheduled rule",
        "severity": "High",
        "enabled": true,
        "tactics": [
          "Persistence"
        ],
        "query": "Heartbeat",
        "queryFrequency": "PT1H",
        "queryPeriod": "P2DT1H30M",
        "triggerOperator": "GreaterThan",
        "triggerThreshold": 0,
        "suppressionDuration": "PT1H",
        "suppressionEnabled": false,
        "lastModifiedUtc": "2021-03-01T13:17:30Z",
        "eventGroupingSettings": {
          "aggregationKind": "AlertPerResult"
        },
        "customDetails": {
          "OperatingSystemName": "OSName"
        },
        "entityMappings": [
          {
            "entityType": "IP",
            "fieldMappings": [
              {
                "identifier": "Address",
                "columnName": "ComputerIP"
              }
            ]
          }
        ],
        "alertDetailsOverride": {
          "alertDisplayNameFormat": "Alert from {{Computer}}",
          "alertDescriptionFormat": "Suspicious activity was made by {{ComputerIP}}",
          "alertDynamicProperties": [
            {
              "alertProperty": "AlertLink",
              "value": "Link"
            }
          ]
        },
        "incidentConfiguration": {
          "createIncident": true,
          "groupingConfiguration": {
            "enabled": true,
            "reopenClosedIncident": false,
            "lookbackDuration": "PT5H",
            "matchingMethod": "Selected",
            "groupByEntities": [
              "Host"
            ],
            "groupByAlertDetails": [
              "DisplayName"
            ]
          }
        }
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
  - **type** (string)
  - **kind** (string)
  - **etag** (string)
  - **properties** (object)
    - **alertRuleTemplateName** (object)
    - **displayName** (string)
    - **description** (string)
    - **severity** (string)
    - **enabled** (boolean)
    - **tactics** (array)
    - **query** (string)
    - **queryFrequency** (string)
    - **queryPeriod** (string)
    - **triggerOperator** (string)
    - **triggerThreshold** (number)
    - **suppressionDuration** (string)
    - **suppressionEnabled** (boolean)
    - **lastModifiedUtc** (string)
    - **eventGroupingSettings** (object)
      - **aggregationKind** (string)
    - **customDetails** (object)
      - **OperatingSystemName** (string)
    - **entityMappings** (array)
      - **entityType** (string)
      - **fieldMappings** (array)
        - **identifier** (string)
        - **columnName** (string)
    - **alertDetailsOverride** (object)
      - **alertDisplayNameFormat** (string)
      - **alertDescriptionFormat** (string)
      - **alertDynamicProperties** (array)
        - **alertProperty** (string)
        - **value** (string)
    - **incidentConfiguration** (object)
      - **createIncident** (boolean)
      - **groupingConfiguration** (object)
        - **enabled** (boolean)
        - **reopenClosedIncident** (boolean)
        - **lookbackDuration** (string)
        - **matchingMethod** (string)
        - **groupByEntities** (array)
        - **groupByAlertDetails** (array)