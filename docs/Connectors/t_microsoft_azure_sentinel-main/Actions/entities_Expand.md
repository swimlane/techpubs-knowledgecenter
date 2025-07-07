# Entities Expand

**Description**: Expands a specific entity in Microsoft Azure Sentinel by utilizing entityId, subscriptionId, resourceGroupName, and workspaceName.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/entities/{{entityId}}/expand`
- **Method:** `POST`
## Inputs

- **parameters** (object) – Required
  - **api-version** (string) – Required: The API version to use for this operation.
- **path_parameters** (object) – Required
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$.
  - **entityId** (string) – Required: entity ID.
- **json_body** (object) – Required
  - **expansionId** (string): The end date filter, so the only expansion results returned are before this date.
  - **startTime** (string): The Id of the expansion to perform.
  - **endTime** (string): The start date filter, so the only expansion results returned are after this date.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "value": {
        "entities": [
          {
            "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/entities/e1d3d618-e11f-478b-98e3-bb381539a8e1",
            "name": "e1d3d618-e11f-478b-98e3-bb381539a8e1",
            "type": "Microsoft.SecurityInsights/entities",
            "kind": "Ip",
            "properties": {
              "address": "13.89.108.248",
              "friendlyName": "13.89.108.248"
            }
          }
        ],
        "edges": [
          {
            "targetEntityId": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/entities/c1d60d86-5988-11eb-ae93-0242ac130002",
            "additionalData": {
              "EpochTimestamp": "1608289949",
              "FirstSeen": "2021-09-01T11:12:29.597Z",
              "Source": "Heartbeat"
            }
          }
        ]
      },
      "metaData": {
        "aggregations": [
          {
            "entityKind": "Account",
            "count": 1
          }
        ]
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (object)
    - **entities** (array)
      - **id** (string)
      - **name** (string)
      - **type** (string)
      - **kind** (string)
      - **properties** (object)
        - **address** (string)
        - **friendlyName** (string)
    - **edges** (array)
      - **targetEntityId** (string)
      - **additionalData** (object)
        - **EpochTimestamp** (string)
        - **FirstSeen** (string)
        - **Source** (string)
  - **metaData** (object)
    - **aggregations** (array)
      - **entityKind** (string)
      - **count** (number)