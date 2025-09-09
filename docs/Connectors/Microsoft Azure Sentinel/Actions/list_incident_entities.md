# List Incident Entities

**Description**: Retrieve all entities related to a specific incident in Microsoft Azure Sentinel, requiring subscriptionId, resourceGroupName, workspaceName, and incidentId.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/entities`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$
  - **incidentId** (string) – Required: Incident ID
- **parameters** (object) – Required: URL Query Parameters
  - **api-version** (string) – Required: The API version to use for this action.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Encoding": "gzip",
      "Expires": "-1",
      "Vary": "Accept-Encoding",
      "Server": "Kestrel",
      "x-ms-ratelimit-remaining-subscription-resource-requests": "499",
      "x-ms-request-id": "48c22610-cfa7-4ba0-9315-fd8bbd2aadba",
      "x-ms-correlation-request-id": "48c22610-cfa7-4ba0-9315-fd8bbd2aadba",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T122235Z:48c22610-cfa7-4ba0-9315-fd8bbd2aadba",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 12:22:34 GMT"
    },
    "reason": "OK",
    "json_body": {
      "entities": [
        {
          "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/Entities/e1d3d618-e11f-478b-98e3-bb381539a8e1",
          "name": "e1d3d618-e11f-478b-98e3-bb381539a8e1",
          "type": "Microsoft.SecurityInsights/Entities",
          "kind": "Account",
          "properties": {
            "friendlyName": "administrator",
            "accountName": "administrator",
            "ntDomain": "domain"
          }
        }
      ],
      "metaData": [
        {
          "entityKind": "Account",
          "count": 1
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
  - **entities** (array)
    - **id** (string)
    - **name** (string)
    - **type** (string)
    - **kind** (string)
    - **properties** (object)
      - **friendlyName** (string)
      - **accountName** (string)
      - **ntDomain** (string)
  - **metaData** (array)
    - **entityKind** (string)
    - **count** (number)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Expires | string |
| Vary | string |
| Server | string |
| x-ms-ratelimit-remaining-subscription-resource-requests | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| Date | string |