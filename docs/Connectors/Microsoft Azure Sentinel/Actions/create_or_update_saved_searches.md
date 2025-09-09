# Create Or Update Saved Searches

**Description**: Create or update saved searches in Microsoft Azure Sentinel, including resource group, search ID, subscription, workspace, and properties.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourcegroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/savedSearches/{{savedSearchId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required
  - **resourceGroupName** (string) – Required: The name of the resource group. The name is case insensitive.
  - **savedSearchId** (string) – Required: The id of the saved search.
  - **subscriptionId** (string) – Required: The ID of the target subscription.
  - **workspaceName** (string) – Required: The name of the workspace. Regex pattern - ^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$
- **parameters** (object) – Required
  - **api-version** (string) – Required: The API version to use for this operation.
- **json_body** (object) – Required
  - **etag** (string): The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag.
  - **properties** (object) – Required
    - **category** (string) – Required: The category of the saved search. This helps the user to find a saved search faster.
    - **displayName** (string) – Required: Saved search display name.
    - **functionAlias** (string): The function alias if query serves as a function.
    - **functionParameters** (string): The optional function parameters if query serves as a function.
    - **query** (string) – Required: The query expression for the saved search.
    - **tags** (array): The tags attached to the saved search.
      - **name** (string)
      - **value** (string)
    - **version** (number): The version number of the query language. The current version is 2 and is the default.
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
      "x-ms-ratelimit-remaining-subscription-writes": "1199",
      "Request-Context": "appId=cid-v1:e6336c63-aab2-45f0-996a-e5dbab2a1508",
      "X-Content-Type-Options": "nosniff",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Access-Control-Allow-Origin": "*",
      "X-Powered-By": "ASP.NET",
      "x-ms-request-id": "23dc562b-c32f-4155-ae6a-81f1f7962b77",
      "x-ms-correlation-request-id": "23dc562b-c32f-4155-ae6a-81f1f7962b77",
      "x-ms-routing-request-id": "JIOINDIACENTRAL:20230810T104018Z:23dc562b-c32f-4155-ae6a-81f1f7962b77",
      "Date": "Thu, 10 Aug 2023 10:40:18 GMT"
    },
    "reason": "OK",
    "json_body": {
      "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/00000000-0000-0000-0000-00000000000",
      "etag": "W/\"datetime'2023-08-10T10%3A40%3A18.6215548Z'\"",
      "properties": {
        "category": "Saved Search Test Category",
        "displayName": "Create or Update Saved Search Test",
        "query": "Heartbeat | summarize Count() by Computer | take a",
        "version": 2
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
  - **etag** (string)
  - **properties** (object)
    - **category** (string)
    - **displayName** (string)
    - **query** (string)
    - **version** (number)
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
| x-ms-ratelimit-remaining-subscription-writes | string |
| Request-Context | string |
| X-Content-Type-Options | string |
| Strict-Transport-Security | string |
| Access-Control-Allow-Origin | string |
| X-Powered-By | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Date | string |