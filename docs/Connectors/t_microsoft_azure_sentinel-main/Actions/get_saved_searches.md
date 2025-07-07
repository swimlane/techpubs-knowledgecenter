# Get Saved Searches

**Description**: Retrieves a specific saved search from a Microsoft Azure Sentinel workspace using resource group, search ID, subscription, and workspace name.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourcegroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/savedSearches/{{savedSearchId}}`
- **Method:** `GET`
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
      "Content-Type": "application/json; charset=utf-8",
      "Expires": "-1",
      "x-ms-failure-cause": "gateway",
      "x-ms-request-id": "54b36bb1-0d41-45b8-a8ba-6f4552f3c8fe",
      "x-ms-correlation-request-id": "54b36bb1-0d41-45b8-a8ba-6f4552f3c8fe",
      "x-ms-routing-request-id": "JIOINDIACENTRAL:20230810T090934Z:54b36bb1-0d41-45b8-a8ba-6f4552f3c8fe",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Thu, 10 Aug 2023 09:09:34 GMT",
      "Content-Length": "139"
    },
    "reason": "OK",
    "json_body": {
      "id": "subscriptions/00000000-0000-0000-0000-000000000005/resourceGroups/mms-eus/providers/Microsoft.OperationalInsights/workspaces/AtlantisDemo/savedSearches/test-new-saved-search-id-2015",
      "etag": "W/\"datetime'2017-10-02T23%3A15%3A41.0709875Z'\"",
      "properties": {
        "category": " Saved Search Test Category",
        "displayName": "Create or Update Saved Search Test",
        "functionAlias": "heartbeat_func",
        "functionParameters": "a:int=1",
        "query": "* | measure Count() by Computer | take a",
        "version": 1
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
    - **functionAlias** (string)
    - **functionParameters** (string)
    - **query** (string)
    - **version** (number)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Pragma | string |
| Content-Type | string |
| Expires | string |
| x-ms-failure-cause | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Strict-Transport-Security | string |
| X-Content-Type-Options | string |
| Date | string |
| Content-Length | string |