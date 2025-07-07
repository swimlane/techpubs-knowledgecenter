# Add Comment to Incident

**Description**: Add a comment to an existing incident in Microsoft Azure Sentinel, requiring subscription and workspace details, incident IDs, and comment properties.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/comments/{{incidentCommentId}}`
- **Method:** `PUT`
## Inputs

- **parameters** (object) – Required
  - **api-version** (string) – Required: API version for the operation.
- **path_parameters** (object) – Required
  - **subscriptionId** (string) – Required: Azure subscription ID. pattern is ^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$.
  - **resourceGroupName** (string) – Required: The name of the resource group within the user's subscription. The name is case insensitive. minLength is 1, maxLength is 90, pattern is ^[-\w\._\(\)]+$.
  - **workspaceName** (string) – Required: The name of the workspace. minLength is 1, maxLength is 90.
  - **incidentId** (string) – Required
  - **incidentCommentId** (string) – Required
- **json_body** (object) – Required
  - **properties** (object) – Required
    - **message** (string) – Required: The comment message.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "type": "Microsoft.SecurityInsights/incidents/comments",
      "properties": {
        "message": "Some message",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "author": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "john.doe@contoso.com",
          "userPrincipalName": "john@contoso.com",
          "name": "john doe"
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
  - **properties** (object)
    - **message** (string)
    - **createdTimeUtc** (string)
    - **author** (object)
      - **objectId** (string)
      - **email** (string)
      - **userPrincipalName** (string)
      - **name** (string)