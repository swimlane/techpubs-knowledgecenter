# List Alert Rules

**Description**: Retrieve all alert rules from a specified Microsoft Azure Sentinel workspace, requiring subscription ID, resource group, and workspace name.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/alertRules`
- **Method:** `GET`
## Inputs

- **parameters** (object) – Required
  - **api-version** (string) – Required: The API version to use for this operation.
- **path_parameters** (object) – Required
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "no-store, no-cache",
      "Pragma": "no-cache",
      "Content-Type": "application/json; charset=utf-8",
      "Expires": "-1",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "P3P": "CP=\"DSP CUR OTPi IND OTRi ONL FIN\"",
      "x-ms-request-id": "f04749a8-b1d4-42ed-a64d-7c0cab024e00",
      "x-ms-ests-server": "2.1.18261.3 - EUS ProdSlices",
      "x-ms-srs": "1.P",
      "X-XSS-Protection": "0",
      "Set-Cookie": "fpc=AjlweEqE3N5AsDykcUumbB5D3sW4AQAAAK9y-90OAAAA; expires=Fri, 12-Jul-2024 10:42:55 GMT; path=/; secure; HttpOnly; SameSite=None, x-ms-gateway-slice=estsfd; path=/; secure; samesite=none; httponly, stsservicecookie=estsfd; path=/; secure; samesite=none; httponly",
      "Date": "Wed, 12 Jun 2024 10:42:55 GMT",
      "Content-Length": "695"
    },
    "reason": "Unauthorized",
    "json_body": {
      "value": [
        {
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
              "Persistence",
              "LateralMovement"
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
              "OperatingSystemName": "OSName",
              "OperatingSystemType": "OSType"
            },
            "entityMappings": [
              {
                "entityType": "Host",
                "fieldMappings": [
                  {
                    "identifier": "FullName",
                    "columnName": "Computer"
                  }
                ]
              },
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
              "alertTacticsColumnName": null,
              "alertSeverityColumnName": null
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
                ],
                "groupByCustomDetails": [
                  "OperatingSystemType",
                  "OperatingSystemName"
                ]
              }
            }
          }
        },
        {
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
        },
        {
          "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/myFirstFusionRule",
          "name": "myFirstFusionRule",
          "etag": "\"25005c11-0000-0d00-0000-5d6cc0e20000\"",
          "type": "Microsoft.SecurityInsights/alertRules",
          "kind": "Fusion",
          "properties": {
            "displayName": "Advanced Multi-Stage Attack Detection",
            "description": "In this mode, Sentinel combines low fidelity alerts, which themselves may not be actionable, and events across multiple products, into high fidelity security interesting incidents. The system looks at multiple products to produce actionable incidents. Custom tailored to each tenant, Fusion not only reduces false positive rates but also can detect attacks with limited or missing information. \nIncidents generated by Fusion system will encase two or more alerts. By design, Fusion incidents are low volume, high fidelity and will be high severity, which is why Fusion is turned ON by default in Azure Sentinel.\n\nFor Fusion to work, please configure the following data sources in Data Connectors tab:\nRequired - Azure Active Directory Identity Protection\nRequired - Microsoft Cloud App Security\nIf Available - Palo Alto Network\n\nFor full list of scenarios covered by Fusion, and detail instructions on how to configure the required data sources, go to aka.ms/SentinelFusion",
            "alertRuleTemplateName": "f71aba3d-28fb-450b-b192-4e76a83015c8",
            "tactics": [
              "Persistence",
              "LateralMovement",
              "Exfiltration",
              "CommandAndControl"
            ],
            "severity": "High",
            "enabled": false,
            "lastModifiedUtc": "2019-09-02T07:12:34.9065092Z"
          }
        }
      ]
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **id** (string)
    - **name** (string)
    - **type** (string)
    - **kind** (string)
    - **etag** (string)
    - **properties** (object)
      - **displayName** (string)
      - **description** (string)
      - **alertRuleTemplateName** (string)
      - **tactics** (array)
      - **severity** (string)
      - **enabled** (boolean)
      - **lastModifiedUtc** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Content-Type | string |
| Expires | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| P3P | string |
| x-ms-request-id | string |
| x-ms-ests-server | string |
| x-ms-srs | string |
| X-XSS-Protection | string |
| Set-Cookie | string |
| Date | string |
| Content-Length | string |