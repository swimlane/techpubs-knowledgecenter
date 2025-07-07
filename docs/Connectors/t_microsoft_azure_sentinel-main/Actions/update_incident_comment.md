# Update Incident Comment

**Description**: Create or update an incident comment in Microsoft Azure Sentinel, utilizing subscription, resource group, workspace, and incident identifiers.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/comments/{{incidentCommentId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **subscriptionId** (string) – Required
  - **resourceGroupName** (string) – Required
  - **workspaceName** (string) – Required
  - **incidentId** (string) – Required
  - **incidentCommentId** (string) – Required
- **parameters** (object) – Required
  - **api-version** (string) – Required
- **json_body** (object) – Required
  - **properties** (object) – Required
    - **message** (string) – Required
  - **etag** (string)
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
      "x-ms-request-id": "aa473e1f-78ce-4466-a0c6-f14359c755a2",
      "x-ms-correlation-request-id": "aa473e1f-78ce-4466-a0c6-f14359c755a2",
      "x-ms-routing-request-id": "CENTRALINDIA:20240118T092209Z:aa473e1f-78ce-4466-a0c6-f14359c755a2",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Thu, 18 Jan 2024 09:22:08 GMT"
    },
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5/comments/4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "name": "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014",
      "type": "Microsoft.SecurityInsights/incidents/comments",
      "etag": "0300bf09-0000-0000-0000-5c37296e0000",
      "properties": {
        "message": "Some message",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastModifiedTimeUtc": "2019-01-04T13:15:30Z",
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
  - **etag** (string)
  - **properties** (object)
    - **message** (string)
    - **createdTimeUtc** (string)
    - **lastModifiedTimeUtc** (string)
    - **author** (object)
      - **objectId** (string)
      - **email** (string)
      - **userPrincipalName** (string)
      - **name** (string)
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