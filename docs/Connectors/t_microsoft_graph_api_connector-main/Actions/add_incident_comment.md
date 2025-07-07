# Add Incident Comment

**Description**: Appends a user-defined comment to an existing incident in Microsoft Graph API using the specified incidentId.

## Endpoint

- **URL:** `/v1.0/security/incidents/{{incidentId}}/comments`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **incidentId** (string) – Required: ID of the Incident.
- **json_body** (object) – Required
  - **@odata.type** (string)
  - **comment** (string) – Required: The comment to be added.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Location": "https://graph.microsoft.com",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "53216e5d-08e9-4dd7-82d1-bbf17db41756",
      "client-request-id": "53216e5d-08e9-4dd7-82d1-bbf17db41756",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"000\",\"RoleInstance\":\"PN1PEPF00007039\"}}",
      "OData-Version": "4.0",
      "Date": "Thu, 13 Jun 2024 06:54:26 GMT"
    },
    "reason": "OK",
    "json_body": {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#security/incidents('545')/comments",
      "value": [
        {
          "comment": "Demo for docs",
          "createdByDisplayName": "API-App:Defender - Test - JHYap",
          "createdDateTime": "2024-06-13T06:38:20.6536162Z"
        },
        {
          "comment": "Demo for docs",
          "createdByDisplayName": "API-App:Defender - Test - JHYap",
          "createdDateTime": "2024-06-13T06:51:40.9010261Z"
        },
        {
          "comment": "Demo for docs",
          "createdByDisplayName": "Defender - Test - JHYap",
          "createdDateTime": "2024-06-13T06:54:26.9428449Z"
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
  - **@odata.context** (string)
  - **value** (array)
    - **comment** (string)
    - **createdByDisplayName** (string)
    - **createdDateTime** (string)
## Response Headers

| Header | Type |
|--------|------|
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| OData-Version | string |
| Date | string |