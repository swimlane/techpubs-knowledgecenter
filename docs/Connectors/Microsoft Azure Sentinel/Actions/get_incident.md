# Get Incident

**Description**: Retrieves detailed information for a specified incident in Microsoft Azure Sentinel using subscription ID, resource group, workspace name, and incident ID.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}`
- **Method:** `GET`
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
      "x-ms-ratelimit-remaining-subscription-reads": "11999",
      "x-ms-request-id": "80a0943c-0eaa-4a3d-bac9-1e4e4eae73db",
      "x-ms-correlation-request-id": "80a0943c-0eaa-4a3d-bac9-1e4e4eae73db",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T122616Z:80a0943c-0eaa-4a3d-bac9-1e4e4eae73db",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 12:26:16 GMT"
    },
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/incidents",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
      "properties": {
        "lastModifiedTimeUtc": "2019-01-01T13:15:30Z",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
        "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
        "description": "This is a demo incident",
        "title": "My incident",
        "owner": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "john.doe@contoso.com",
          "userPrincipalName": "john@contoso.com",
          "assignedTo": "john doe"
        },
        "severity": "High",
        "classification": "FalsePositive",
        "classificationComment": "Not a malicious activity",
        "classificationReason": "InaccurateData",
        "status": "Closed",
        "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        "incidentNumber": 3177,
        "labels": [],
        "providerName": "Azure Sentinel",
        "providerIncidentId": "3177",
        "relatedAnalyticRuleIds": [
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/fab3d2d4-747f-46a7-8ef0-9c0be8112bf7"
        ],
        "additionalData": {
          "alertsCount": 0,
          "bookmarksCount": 0,
          "commentsCount": 3,
          "alertProductNames": [],
          "tactics": [
            "InitialAccess",
            "Persistence"
          ]
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
  - **etag** (string)
  - **properties** (object)
    - **lastModifiedTimeUtc** (string)
    - **createdTimeUtc** (string)
    - **lastActivityTimeUtc** (string)
    - **firstActivityTimeUtc** (string)
    - **description** (string)
    - **title** (string)
    - **owner** (object)
      - **objectId** (string)
      - **email** (string)
      - **userPrincipalName** (string)
      - **assignedTo** (string)
    - **severity** (string)
    - **classification** (string)
    - **classificationComment** (string)
    - **classificationReason** (string)
    - **status** (string)
    - **incidentUrl** (string)
    - **incidentNumber** (number)
    - **labels** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **providerName** (string)
    - **providerIncidentId** (string)
    - **relatedAnalyticRuleIds** (array)
    - **additionalData** (object)
      - **alertsCount** (number)
      - **bookmarksCount** (number)
      - **commentsCount** (number)
      - **alertProductNames** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **tactics** (array)
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
| x-ms-ratelimit-remaining-subscription-reads | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| Date | string |