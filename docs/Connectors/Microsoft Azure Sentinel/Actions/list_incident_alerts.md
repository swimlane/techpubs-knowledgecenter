# List Incident Alerts

**Description**: Retrieve all alerts associated with a specific incident in Microsoft Azure Sentinel, including details like subscription ID, resource group, workspace name, and incident ID.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/providers/Microsoft.SecurityInsights/incidents/{{incidentId}}/alerts`
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
      "x-ms-request-id": "8745ade4-8c1e-4c0b-beec-2969c4a779e9",
      "x-ms-correlation-request-id": "8745ade4-8c1e-4c0b-beec-2969c4a779e9",
      "x-ms-routing-request-id": "SOUTHINDIA:20230729T111826Z:8745ade4-8c1e-4c0b-beec-2969c4a779e9",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "X-Content-Type-Options": "nosniff",
      "Date": "Sat, 29 Jul 2023 11:18:26 GMT"
    },
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/providers/Microsoft.SecurityInsights/Entities/fa4298e7-2a38-778b-b875-44509409d7fa",
          "name": "fa4298e7-2a38-778b-b875-44509409d7fa",
          "type": "Microsoft.SecurityInsights/Entities",
          "kind": "SecurityAlert",
          "properties": {
            "systemAlertId": "fa4298e7-2a38-778b-b875-44509409d7fa",
            "tactics": [],
            "alertDisplayName": "Azure Sentinel update alert",
            "description": "update alert",
            "confidenceLevel": "Unknown",
            "severity": "Medium",
            "vendorName": "Microsoft",
            "productName": "Azure Sentinel",
            "productComponentName": "Scheduled Alerts",
            "alertType": "7b3f088b-d55a-485c-b030-4cb167e8cffd_6134bf18-8d6a-46ff-a3f1-cdd43cafbf57",
            "processingEndTime": "2023-07-29T00:29:50.5444443Z",
            "status": "New",
            "endTimeUtc": "2023-07-28T19:50:00.684261Z",
            "startTimeUtc": "2023-07-28T19:45:39.4493887Z",
            "timeGenerated": "2023-07-29T00:29:50.5833611Z",
            "providerAlertId": "9028e8ae-c8ea-4d48-9ecd-551e8ac7c1b2",
            "resourceIdentifiers": [
              {
                "type": "LogAnalytics",
                "workspaceId": "7b3f088b-d55a-485c-b030-4cb167e8cffd",
                "subscriptionId": "38d4cde9-8ef2-4c61-bc61-7fa8658ab74b",
                "resourceGroup": "test"
              }
            ],
            "additionalData": {
              "AlertMessageEnqueueTime": "2023-07-29T00:29:50.586Z",
              "Search Query Results Overall Count": "12",
              "OriginalProductName": "Azure Sentinel",
              "OriginalProductComponentName": "Scheduled Alerts"
            },
            "friendlyName": "Azure Sentinel update alert"
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
      - **systemAlertId** (string)
      - **tactics** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **alertDisplayName** (string)
      - **description** (string)
      - **confidenceLevel** (string)
      - **severity** (string)
      - **vendorName** (string)
      - **productName** (string)
      - **productComponentName** (string)
      - **alertType** (string)
      - **processingEndTime** (string)
      - **status** (string)
      - **endTimeUtc** (string)
      - **startTimeUtc** (string)
      - **timeGenerated** (string)
      - **providerAlertId** (string)
      - **resourceIdentifiers** (array)
        - **type** (string)
        - **workspaceId** (string)
        - **subscriptionId** (string)
        - **resourceGroup** (string)
      - **additionalData** (object)
        - **AlertMessageEnqueueTime** (string)
        - **Search Query Results Overall Count** (string)
        - **OriginalProductName** (string)
        - **OriginalProductComponentName** (string)
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