# Get Incident

**Description**: Retrieve detailed information and relationships for an incident by its ID from Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/security/incidents/{{incidentId}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **incidentId** (string) – Required: Incident ID
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "client-request-id": "8beed643-f868-4fd0-9e15-e0db4c50383e",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"CP1PEPF00003034\"}}",
      "Date": "Tue, 27 Dec 2022 21:12:51 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.type": "#microsoft.graph.incident",
      "id": "2972395",
      "incidentWebUrl": "https://security.microsoft.com/incidents/2972395?tid=12f988bf-16f1-11af-11ab-1d7cd011db47",
      "redirectIncidentId": null,
      "displayName": "Multi-stage incident involving Initial access & Command and control on multiple endpoints reported by multiple sources",
      "tenantId": "b3c1b5fc-828c-45fa-a1e1-10d74f6d6e9c",
      "createdDateTime": "2021-08-13T08:43:35.5533333Z",
      "lastUpdateDateTime": "2021-09-30T09:35:45.1133333Z",
      "assignedTo": "KaiC@contoso.onmicrosoft.com",
      "classification": "TruePositive",
      "determination": "MultiStagedAttack",
      "status": "Active",
      "severity": "Medium",
      "customTags": [
        "Demo"
      ],
      "comments": [
        {
          "comment": "Demo incident",
          "createdBy": "DavidS@contoso.onmicrosoft.com",
          "createdTime": "2021-09-30T12:07:37.2756993Z"
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
  - **@odata.type** (string)
  - **id** (string)
  - **incidentWebUrl** (string)
  - **redirectIncidentId** (object)
  - **displayName** (string)
  - **tenantId** (string)
  - **createdDateTime** (string)
  - **lastUpdateDateTime** (string)
  - **assignedTo** (string)
  - **classification** (string)
  - **determination** (string)
  - **status** (string)
  - **severity** (string)
  - **customTags** (array)
  - **comments** (array)
    - **comment** (string)
    - **createdBy** (string)
    - **createdTime** (string)
## Response Headers

| Header | Type |
|--------|------|
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| Date | string |