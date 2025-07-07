# List By Workspace Saved Searches

**Description**: Retrieve all saved searches within a Log Analytics Workspace in Microsoft Azure Sentinel, requiring resource group, subscription ID, and workspace name.

## Endpoint

- **URL:** `/subscriptions/{{subscriptionId}}/resourcegroups/{{resourceGroupName}}/providers/Microsoft.OperationalInsights/workspaces/{{workspaceName}}/savedSearches`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **resourceGroupName** (string) – Required
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
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json; charset=utf-8",
      "Content-Encoding": "gzip",
      "Expires": "-1",
      "Vary": "Accept-Encoding",
      "x-ms-ratelimit-remaining-subscription-reads": "11999",
      "Request-Context": "appId=cid-v1:e6336c63-aab2-45f0-996a-e5dbab2a1508",
      "X-Content-Type-Options": "nosniff",
      "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
      "Access-Control-Allow-Origin": "*",
      "X-Powered-By": "ASP.NET",
      "x-ms-request-id": "dee963e1-17f2-461b-83a1-321ca07cb530",
      "x-ms-correlation-request-id": "dee963e1-17f2-461b-83a1-321ca07cb530",
      "x-ms-routing-request-id": "JIOINDIACENTRAL:20230810T104321Z:dee963e1-17f2-461b-83a1-321ca07cb530",
      "Date": "Thu, 10 Aug 2023 10:43:20 GMT"
    },
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/00000000-0000-0000-0000-00000000000",
          "etag": "W/\"datetime'2023-08-10T10%3A40%3A18.6215548Z'\"",
          "properties": {
            "category": "Saved Search Test Category",
            "displayName": "Create or Update Saved Search Test",
            "query": "Heartbeat | summarize Count() by Computer | take a",
            "version": 2
          },
          "name": "00000000-0000-0000-0000-00000000000",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|AllEvents",
          "properties": {
            "displayName": "All Events",
            "category": "Log Management",
            "query": "Event | sort by TimeGenerated desc\r\n// Oql: Type=Event // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|AllEvents",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|ShowServersThrowingInternalServerError",
          "properties": {
            "displayName": "Shows servers that are throwing internal server error",
            "category": "Log Management",
            "query": "search scStatus == 500 | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by sComputerName\r\n// Oql: Type=W3CIISLog scStatus=500 | Measure count() by sComputerName // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|ShowServersThrowingInternalServerError",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesHTTPRequestMethod",
          "properties": {
            "displayName": "Count of IIS Log Entries by HTTP Request Method",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by csMethod\r\n// Oql: Type=W3CIISLog | Measure count() by csMethod // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesHTTPRequestMethod",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesHTTPUserAgent",
          "properties": {
            "displayName": "Count of IIS Log Entries by HTTP User Agent",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by csUserAgent\r\n// Oql: Type=W3CIISLog | Measure count() by csUserAgent // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesHTTPUserAgent",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesClientIPAddress",
          "properties": {
            "displayName": "Count of IIS Log Entries by Client IP Address",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by cIP\r\n// Oql: Type=W3CIISLog | Measure count() by cIP // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountIISLogEntriesClientIPAddress",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|IISLogEntriesForClientIP",
          "properties": {
            "displayName": "IIS Log Entries for a specific client IP Address (replace with your own)",
            "category": "Log Management",
            "query": "search cIP == \"192.168.0.1\" | extend Type = $table | where Type == W3CIISLog | sort by TimeGenerated desc | project csUriStem, scBytes, csBytes, TimeTaken, scStatus\r\n// Oql: Type=W3CIISLog cIP=\"192.168.0.1\" | Select csUriStem,scBytes,csBytes,TimeTaken,scStatus // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|IISLogEntriesForClientIP",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByURLRequestedByClient",
          "properties": {
            "displayName": "Count of IIS Log Entries by URL requested by client (without query strings)",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by csUriStem\r\n// Oql: Type=W3CIISLog | Measure count() by csUriStem // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByURLRequestedByClient",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByHostRequestedByClient",
          "properties": {
            "displayName": "Count of IIS Log Entries by Host requested by client",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by csHost\r\n// Oql: Type=W3CIISLog | Measure count() by csHost // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByHostRequestedByClient",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByURLForHost",
          "properties": {
            "displayName": "Count of IIS Log Entries by URL for the host \"www.contoso.com\" (replace with your own)",
            "category": "Log Management",
            "query": "search csHost == \"www.contoso.com\" | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = count() by csUriStem\r\n// Oql: Type=W3CIISLog csHost=\"www.contoso.com\" | Measure count() by csUriStem // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|CountOfIISLogEntriesByURLForHost",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesSentByClientIPAddress",
          "properties": {
            "displayName": "Total Bytes sent by Client IP Address",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = sum(csBytes) by cIP\r\n// Oql: Type=W3CIISLog | Measure Sum(csBytes) by cIP // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesSentByClientIPAddress",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesReceivedByEachAzureRoleInstance",
          "properties": {
            "displayName": "Total Bytes received by each Azure Role Instance",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = sum(csBytes) by RoleInstance\r\n// Oql: Type=W3CIISLog | Measure Sum(csBytes) by RoleInstance // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesReceivedByEachAzureRoleInstance",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesReceivedByEachIISComputer",
          "properties": {
            "displayName": "Total Bytes received by each IIS Computer",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = sum(csBytes) by Computer | limit 500000\r\n// Oql: Type=W3CIISLog | Measure Sum(csBytes) by Computer | top 500000 // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesReceivedByEachIISComputer",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesRespondedToClientsByEachIISServerIPAddress",
          "properties": {
            "displayName": "Total Bytes responded back to clients by each IIS ServerIP Address",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = sum(scBytes) by sIP\r\n// Oql: Type=W3CIISLog | Measure Sum(scBytes) by sIP // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesRespondedToClientsByEachIISServerIPAddress",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesRespondedToClientsByClientIPAddress",
          "properties": {
            "displayName": "Total Bytes responded back to clients by Client IP Address",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = sum(scBytes) by cIP\r\n// Oql: Type=W3CIISLog | Measure Sum(scBytes) by cIP // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|TotalBytesRespondedToClientsByClientIPAddress",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|AverageHTTPRequestTimeByClientIPAddress",
          "properties": {
            "displayName": "Average HTTP Request time by Client IP Address",
            "category": "Log Management",
            "query": "search * | extend Type = $table | where Type == W3CIISLog | summarize AggregatedValue = avg(TimeTaken) by cIP\r\n// Oql: Type=W3CIISLog | Measure Avg(TimeTaken) by cIP // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PEF: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|AverageHTTPRequestTimeByClientIPAddress",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslog",
          "properties": {
            "displayName": "All Syslogs",
            "category": "Log Management",
            "query": "Syslog | sort by TimeGenerated desc\r\n// Oql: Type=Syslog // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslog",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslogsWithErrors",
          "properties": {
            "displayName": "All Syslog Records with Errors",
            "category": "Log Management",
            "query": "Syslog | where SeverityLevel == \"error\" | sort by TimeGenerated desc\r\n// Oql: Type=Syslog SeverityLevel=error // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslogsWithErrors",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslogByFacility",
          "properties": {
            "displayName": "All Syslog Records grouped by Facility",
            "category": "Log Management",
            "query": "Syslog | summarize AggregatedValue = count() by Facility\r\n// Oql: Type=Syslog | Measure count() by Facility // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_LogManagement|AllSyslogByFacility",
          "type": "Microsoft.OperationalInsights/savedSearches"
        },
        {
          "id": "/subscriptions/38d4cde9-8ef2-4c61-bc61-7fa8658ab74b/resourceGroups/test/providers/Microsoft.OperationalInsights/workspaces/swimlaneazuresentinel/savedSearches/LogManagement(swimlaneazuresentinel)_General|StaleComputers",
          "properties": {
            "displayName": "Stale Computers (data older than 24 hours)",
            "category": "General Exploration",
            "query": "search not(ObjectName == \"Advisor Metrics\" or ObjectName == \"ManagedSpace\") | summarize lastdata = max(TimeGenerated) by Computer | limit 500000 | where lastdata < ago(24h)\r\n// Oql: NOT(ObjectName=\"Advisor Metrics\" OR ObjectName=ManagedSpace) | measure max(TimeGenerated) as lastdata by Computer | top 500000 | where lastdata < NOW-24HOURS // Args: {OQ: True; WorkspaceId: 00000000-0000-0000-0000-000000000000} // Settings: {PTT: True; SortI: True; SortF: True} // Version: 0.1.122",
            "version": 2
          },
          "name": "LogManagement(swimlaneazuresentinel)_General|StaleComputers",
          "type": "Microsoft.OperationalInsights/savedSearches"
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
    - **etag** (string)
    - **properties** (object)
      - **displayName** (string)
      - **category** (string)
      - **query** (string)
      - **version** (number)
    - **name** (string)
    - **type** (string)
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
| x-ms-ratelimit-remaining-subscription-reads | string |
| Request-Context | string |
| X-Content-Type-Options | string |
| Strict-Transport-Security | string |
| Access-Control-Allow-Origin | string |
| X-Powered-By | string |
| x-ms-request-id | string |
| x-ms-correlation-request-id | string |
| x-ms-routing-request-id | string |
| Date | string |