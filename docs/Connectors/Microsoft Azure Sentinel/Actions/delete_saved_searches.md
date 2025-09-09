# Delete Saved Searches

**Description**: Removes a specified saved search from an Azure Sentinel workspace using resource group, search ID, subscription ID, and workspace name.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourcegroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/savedSearches/{{savedSearchId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **resourceGroupName** (string) – Required
  - **savedSearchId** (string) – Required
  - **subscriptionId** (string) – Required
  - **workspaceName** (string) – Required
- **parameters** (object) – Required
  - **api-version** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Pragma": "no-cache",
      "Expires": "-1",
      "x-ms-ratelimit-remaining-subscription-deletes": "14999",
      "Request-Context": "appId=cid-v1:e6336c63-aab2-45f0-996a-e5dbab2a1508",
      "X-Content-Type-Options": "nosniff",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Access-Control-Allow-Origin": "*",
      "X-Powered-By": "ASP.NET",
      "x-ms-request-id": "1744d53b-b782-4116-9086-1ef0d39b76ba",
      "x-ms-correlation-request-id": "1744d53b-b782-4116-9086-1ef0d39b76ba",
      "x-ms-routing-request-id": "JIOINDIACENTRAL:20230810T104541Z:1744d53b-b782-4116-9086-1ef0d39b76ba",
      "Date": "Thu, 10 Aug 2023 10:45:40 GMT",
      "Content-Length": "0"
    },
    "reason": "OK",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Expires | string |
| x-ms-ratelimit-remaining-subscription-deletes | string |
| Request-Context | string |
| X-Content-Type-Options | string |
| Strict-Transport-Security | string |
| Access-Control-Allow-Origin | string |
| X-Powered-By | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Date | string |
| Content-Length | string |