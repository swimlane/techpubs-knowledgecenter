# Run Analytics Query

**Description**: Executes an Analytics query in Microsoft Azure Sentinel using a workspace ID and a specific query string, with an optional API version parameter.

## Endpoint

- **URL:** `/v1/workspaces/{{workspaceId}}/query`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **workspaceId** (string) – Required
- **parameters** (object) – Required: URL Query Parameters
  - **query** (string) – Required: The Analytics query.
  - **timespan** (string): The timespan over which to query data. This is an ISO8601 time period value. This timespan is applied in addition to any that are specified in the query expression.
  - **api-version** (string) – Required: The API version to use for this action.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Date": "Fri, 11 Aug 2023 03:08:43 GMT",
      "Content-Type": "application/json; charset=utf-8",
      "Transfer-Encoding": "chunked",
      "Connection": "keep-alive",
      "via": "1.1 draft-oms-74c8fb9684-6rv8g",
      "X-Content-Type-Options": "nosniff",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Expose-Headers": "Retry-After,Age,WWW-Authenticate,x-resource-identities,x-ms-status-location",
      "Vary": "Accept-Encoding",
      "Content-Encoding": "gzip",
      "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
    },
    "reason": "OK",
    "json_body": {
      "tables": [
        {
          "name": "PrimaryResult",
          "columns": [
            {
              "name": "TenantId",
              "type": "string"
            },
            {
              "name": "TimeGenerated",
              "type": "datetime"
            },
            {
              "name": "DisplayName",
              "type": "string"
            },
            {
              "name": "AlertName",
              "type": "string"
            },
            {
              "name": "AlertSeverity",
              "type": "string"
            },
            {
              "name": "Description",
              "type": "string"
            },
            {
              "name": "ProviderName",
              "type": "string"
            },
            {
              "name": "VendorName",
              "type": "string"
            },
            {
              "name": "VendorOriginalId",
              "type": "string"
            },
            {
              "name": "SystemAlertId",
              "type": "string"
            },
            {
              "name": "ResourceId",
              "type": "string"
            },
            {
              "name": "SourceComputerId",
              "type": "string"
            },
            {
              "name": "AlertType",
              "type": "string"
            },
            {
              "name": "ConfidenceLevel",
              "type": "string"
            },
            {
              "name": "ConfidenceScore",
              "type": "real"
            },
            {
              "name": "IsIncident",
              "type": "bool"
            },
            {
              "name": "StartTime",
              "type": "datetime"
            },
            {
              "name": "EndTime",
              "type": "datetime"
            },
            {
              "name": "ProcessingEndTime",
              "type": "datetime"
            },
            {
              "name": "RemediationSteps",
              "type": "string"
            },
            {
              "name": "ExtendedProperties",
              "type": "string"
            },
            {
              "name": "Entities",
              "type": "string"
            },
            {
              "name": "SourceSystem",
              "type": "string"
            },
            {
              "name": "WorkspaceSubscriptionId",
              "type": "string"
            },
            {
              "name": "WorkspaceResourceGroup",
              "type": "string"
            },
            {
              "name": "ExtendedLinks",
              "type": "string"
            },
            {
              "name": "ProductName",
              "type": "string"
            },
            {
              "name": "ProductComponentName",
              "type": "string"
            },
            {
              "name": "AlertLink",
              "type": "string"
            },
            {
              "name": "Status",
              "type": "string"
            },
            {
              "name": "CompromisedEntity",
              "type": "string"
            },
            {
              "name": "Tactics",
              "type": "string"
            },
            {
              "name": "Techniques",
              "type": "string"
            },
            {
              "name": "Type",
              "type": "string"
            }
          ],
          "rows": [
            [
              "7b3f088b-d55a-485c-b030-4cb167e8cffd",
              "2023-07-24T20:29:01.8010707Z",
              "Sentinel Test alert",
              "Sentinel Test alert",
              "Medium",
              "test alert",
              "ASI Scheduled Alerts",
              "Microsoft",
              "dff52d0f-17f9-4c6e-a212-bdecfdb67c11",
              "e9122c20-4ec9-483f-51ce-9039d3a40729",
              "",
              "",
              "7b3f088b-d55a-485c-b030-4cb167e8cffd_8a0d8e78-58a9-4d66-af3a-b054778b4aa2",
              "",
              null,
              false,
              "2023-07-24T19:45:43.1962911Z",
              "2023-07-24T19:50:01.0155241Z",
              "2023-07-24T20:29:01.761047Z",
              "",
              "{\"Query Period\":\"05:00:00\",\"Trigger Operator\":\"GreaterThan\",\"Trigger Threshold\":\"0\",\"Correlation Id\":\"5ebca6d9-f72d-45b5-b9e3-118c6a8d56c8\",\"Search Query Results Overall Count\":\"12\",\"Data Sources\":\"[\\\"swimlaneazuresentinel\\\"]\",\"Query\":\"// The query_now parameter represents the time (in UTC) at which the scheduled analytics rule ran to produce this alert.\\nset query_now = datetime(2023-07-24T20:23:59.1070000Z);\\nunion AzureActivity\",\"Query Start Time UTC\":\"2023-07-24 15:23:59Z\",\"Query End Time UTC\":\"2023-07-24 20:24:00Z\",\"Analytic Rule Ids\":\"[\\\"8a0d8e78-58a9-4d66-af3a-b054778b4aa2\\\"]\",\"Event Grouping\":\"SingleAlert\",\"Analytic Rule Name\":\"Sentinel Test alert\",\"ProcessedBySentinel\":\"True\",\"Alert generation status\":\"Full alert created\"}",
              "",
              "Detection",
              "38d4cde9-8ef2-4c61-bc61-7fa8658ab74b",
              "test",
              "",
              "Azure Sentinel",
              "Scheduled Alerts",
              "",
              "New",
              "",
              "Unknown",
              "",
              "SecurityAlert"
            ],
            [
              "7b3f088b-d55a-485c-b030-4cb167e8cffd",
              "2023-08-10T22:29:04.8630406Z",
              "Sentinel Test alert",
              "Sentinel Test alert",
              "Medium",
              "test alert",
              "ASI Scheduled Alerts",
              "Microsoft",
              "02c5e70c-dda1-4900-b609-a1c258deb4d0",
              "30085f40-d418-6b72-bf49-30fe7c3d9b73",
              "",
              "",
              "7b3f088b-d55a-485c-b030-4cb167e8cffd_8a0d8e78-58a9-4d66-af3a-b054778b4aa2",
              "",
              null,
              false,
              "2023-08-10T19:45:40.8560733Z",
              "2023-08-10T19:50:01.423544Z",
              "2023-08-10T22:29:04.8195353Z",
              "",
              "{\"Query Period\":\"05:00:00\",\"Trigger Operator\":\"GreaterThan\",\"Trigger Threshold\":\"0\",\"Correlation Id\":\"d2d2173a-ee82-4fa7-8b48-c76d745fe54e\",\"Search Query Results Overall Count\":\"12\",\"Data Sources\":\"[\\\"swimlaneazuresentinel\\\"]\",\"Query\":\"// The query_now parameter represents the time (in UTC) at which the scheduled analytics rule ran to produce this alert.\\nset query_now = datetime(2023-08-10T22:23:59.1070000Z);\\nunion AzureActivity\",\"Query Start Time UTC\":\"2023-08-10 17:23:59Z\",\"Query End Time UTC\":\"2023-08-10 22:24:00Z\",\"Analytic Rule Ids\":\"[\\\"8a0d8e78-58a9-4d66-af3a-b054778b4aa2\\\"]\",\"Event Grouping\":\"SingleAlert\",\"Analytic Rule Name\":\"Sentinel Test alert\",\"ProcessedBySentinel\":\"True\",\"Alert generation status\":\"Full alert created\"}",
              "",
              "Detection",
              "38d4cde9-8ef2-4c61-bc61-7fa8658ab74b",
              "test",
              "",
              "Azure Sentinel",
              "Scheduled Alerts",
              "",
              "New",
              "",
              "Unknown",
              "",
              "SecurityAlert"
            ]
          ]
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
  - **tables** (array)
    - **name** (string)
    - **columns** (array)
      - **name** (string)
      - **type** (string)
    - **rows** (array)
## Response Headers

| Header | Type |
|--------|------|
| Date | string |
| Content-Type | string |
| Transfer-Encoding | string |
| Connection | string |
| via | string |
| X-Content-Type-Options | string |
| Access-Control-Allow-Origin | string |
| Access-Control-Expose-Headers | string |
| Vary | string |
| Content-Encoding | string |
| Strict-Transport-Security | string |