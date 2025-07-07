# List Incident Bookmarks

**Description**: Retrieve all bookmarks associated with an incident in Microsoft Azure Sentinel, requiring subscription, resource group, workspace, and incident IDs.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/bookmarks`
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
      "x-ms-request-id": "fa5a78c9-cc33-4e7e-9aa1-800086279fbd",
      "x-ms-correlation-request-id": "fa5a78c9-cc33-4e7e-9aa1-800086279fbd",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T112006Z:fa5a78c9-cc33-4e7e-9aa1-800086279fbd",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 11:20:05 GMT"
    },
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/afbd324f-6c48-459c-8710-8d1e1cd03812",
          "name": "afbd324f-6c48-459c-8710-8d1e1cd03812",
          "type": "Microsoft.SecurityInsights/Entities",
          "kind": "Bookmark",
          "properties": {
            "displayName": "SecurityEvent - 868f40f4698d",
            "created": "2020-06-17T15:34:01.4265524+00:00",
            "updated": "2020-06-17T15:34:01.4265524+00:00",
            "createdBy": {
              "objectId": "b03ca914-5eb6-45e5-9417-fe0797c372fd",
              "email": "user@microsoft.com",
              "name": "user"
            },
            "updatedBy": {
              "objectId": "b03ca914-5eb6-45e5-9417-fe0797c372fd",
              "email": "user@microsoft.com",
              "name": "user"
            },
            "eventTime": "2020-06-17T15:34:01.4265524+00:00",
            "labels": [],
            "query": "SecurityEvent\r\n| take 1\n",
            "queryResult": "{\"TimeGenerated\":\"2020-05-24T01:24:25.67Z\",\"Account\":\"\\\\ADMINISTRATOR\",\"AccountType\":\"User\",\"Computer\":\"SecurityEvents\",\"EventSourceName\":\"Microsoft-Windows-Security-Auditing\",\"Channel\":\"Security\",\"Task\":12544,\"Level\":\"16\",\"EventID\":4625,\"Activity\":\"4625 - An account failed to log on.\",\"AuthenticationPackageName\":\"NTLM\",\"FailureReason\":\"%%2313\",\"IpAddress\":\"176.113.115.73\",\"IpPort\":\"0\",\"LmPackageName\":\"-\",\"LogonProcessName\":\"NtLmSsp \",\"LogonType\":3,\"LogonTypeName\":\"3 - Network\",\"Process\":\"-\",\"ProcessId\":\"0x0\",\"__entityMapping\":{\"\\\\ADMINISTRATOR\":\"Account\",\"SecurityEvents\":\"Host\"}}",
            "additionalData": {
              "ETag": "\"3b00acab-0000-0d00-0000-5f15e4ed0000\"",
              "EntityId": "afbd324f-6c48-459c-8710-8d1e1cd03812"
            },
            "friendlyName": "SecurityEvent - 868f40f4698d"
          }
        },
        {
          "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/bbbd324f-6c48-459c-8710-8d1e1cd03812",
          "name": "bbbd324f-6c48-459c-8710-8d1e1cd03812",
          "type": "Microsoft.SecurityInsights/Entities",
          "kind": "Bookmark",
          "properties": {
            "displayName": "SecurityEvent - 868f40f4698d",
            "created": "2020-06-17T15:34:01.4265524+00:00",
            "updated": "2020-06-17T15:34:01.4265524+00:00",
            "createdBy": {
              "objectId": "303ca914-5eb6-45e5-9417-fe0797c372fd",
              "email": "user@microsoft.com",
              "name": "user"
            },
            "updatedBy": {
              "objectId": "b03ca914-5eb6-45e5-9417-fe0797c372fd",
              "email": "user@microsoft.com",
              "name": "user"
            },
            "eventTime": "2020-06-17T15:34:01.4265524+00:00",
            "labels": [],
            "query": "SecurityEvent\r\n| take 1\n",
            "queryResult": "{\"TimeGenerated\":\"2020-05-24T01:24:25.67Z\",\"Account\":\"\\\\ADMINISTRATOR\",\"AccountType\":\"User\",\"Computer\":\"SecurityEvents\",\"EventSourceName\":\"Microsoft-Windows-Security-Auditing\",\"Channel\":\"Security\",\"Task\":12544,\"Level\":\"16\",\"EventID\":4625,\"Activity\":\"4625 - An account failed to log on.\",\"AuthenticationPackageName\":\"NTLM\",\"FailureReason\":\"%%2313\",\"IpAddress\":\"176.113.115.73\",\"IpPort\":\"0\",\"LmPackageName\":\"-\",\"LogonProcessName\":\"NtLmSsp \",\"LogonType\":3,\"LogonTypeName\":\"3 - Network\",\"Process\":\"-\",\"ProcessId\":\"0x0\",\"__entityMapping\":{\"\\\\ADMINISTRATOR\":\"Account\",\"SecurityEvents\":\"Host\"}}",
            "additionalData": {
              "ETag": "\"3b00acab-0000-0d00-0000-5f15e4ed0000\"",
              "EntityId": "afbd324f-6c48-459c-8710-8d1e1cd03812"
            },
            "friendlyName": "SecurityEvent - 868f40f4698d"
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
    - **properties** (object)
      - **displayName** (string)
      - **created** (string)
      - **updated** (string)
      - **createdBy** (object)
        - **objectId** (string)
        - **email** (string)
        - **name** (string)
      - **updatedBy** (object)
        - **objectId** (string)
        - **email** (string)
        - **name** (string)
      - **eventTime** (string)
      - **labels** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **query** (string)
      - **queryResult** (string)
      - **additionalData** (object)
        - **ETag** (string)
        - **EntityId** (string)
      - **friendlyName** (string)
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