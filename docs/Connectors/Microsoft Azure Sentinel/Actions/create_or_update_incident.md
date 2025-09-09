# Create or Update Incident

**Description**: Create or update an incident in Microsoft Azure Sentinel, specifying subscription ID, resource group, workspace name, incident ID, and incident properties.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$
  - **incidentId** (string) – Required: Incident ID
- **parameters** (object) – Required: URL Query Parameters
  - **api-version** (string) – Required: The API version to use for this action.
- **json_body** (object) – Required
  - **etag** (string)
  - **properties** (object) – Required
    - **lastActivityTimeUtc** (string): The time of the last activity in the incident.
    - **firstActivityTimeUtc** (string): The time of the first activity in the incident.
    - **description** (string): The description of the incident.
    - **title** (string) – Required: The title of the incident.
    - **owner** (object): Describes a user that the incident is assigned to.
      - **assignedTo** (string)
      - **email** (string)
      - **objectId** (string)
      - **ownerType** (string)
      - **userPrincipalName** (string)
    - **severity** (string) – Required: The severity of the incident.
    - **classification** (string): The reason the incident was closed.
    - **classificationComment** (string): Describes the reason the incident was closed.
    - **classificationReason** (string): The classification reason the incident was closed with.
    - **status** (string) – Required: The status of the incident.
    - **labels** (array): List of labels relevant to this incident.
      - **labelName** (string)
      - **labelType** (string)
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Content-Length": "1480",
      "Content-Type": "application/json; charset=utf-8",
      "Expires": "-1",
      "Server": "Kestrel",
      "x-ms-ratelimit-remaining-subscription-resource-requests": "499",
      "x-ms-request-id": "02b3f250-c3ec-47bc-9bf6-13c2233ea13d",
      "x-ms-correlation-request-id": "02b3f250-c3ec-47bc-9bf6-13c2233ea13d",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T120425Z:02b3f250-c3ec-47bc-9bf6-13c2233ea13d",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 12:04:25 GMT"
    },
    "reason": "Created",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/incidents",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0001\"",
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
          "assignedTo": "john doe",
          "ownerType": "User"
        },
        "severity": "High",
        "classification": "FalsePositive",
        "classificationComment": "Not a malicious activity",
        "classificationReason": "IncorrectAlertLogic",
        "status": "Closed",
        "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        "incidentNumber": 3177,
        "labels": [
          {
            "labelName": "example label",
            "labelType": "AutoAssigned"
          }
        ],
        "providerName": "Azure Sentinel",
        "providerIncidentId": "3177",
        "relatedAnalyticRuleIds": [],
        "additionalData": {
          "alertsCount": 0,
          "bookmarksCount": 0,
          "commentsCount": 3,
          "alertProductNames": [],
          "tactics": []
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
      - **ownerType** (string)
    - **severity** (string)
    - **classification** (string)
    - **classificationComment** (string)
    - **classificationReason** (string)
    - **status** (string)
    - **incidentUrl** (string)
    - **incidentNumber** (number)
    - **labels** (array)
      - **labelName** (string)
      - **labelType** (string)
    - **providerName** (string)
    - **providerIncidentId** (string)
    - **relatedAnalyticRuleIds** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **additionalData** (object)
      - **alertsCount** (number)
      - **bookmarksCount** (number)
      - **commentsCount** (number)
      - **alertProductNames** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **tactics** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Content-Length | string |
| Content-Type | string |
| Expires | string |
| Server | string |
| x-ms-ratelimit-remaining-subscription-resource-requests | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| Date | string |