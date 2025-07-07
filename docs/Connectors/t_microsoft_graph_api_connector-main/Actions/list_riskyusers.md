# List riskyUsers

**Description**: Retrieve a list of riskyUser objects along with their properties from Microsoft Graph API.

## Endpoint

- **URL:** `/v1.0/identityProtection/riskyUsers`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$filter** (string): Filters results (rows).
  - **$select** (string): Filters properties (columns).
  - **$top** (number): Sets the page size of results. The maximum page size with top is 500 objects.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "Cache-Control": "private",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "b15e85c5-d517-4e9e-a99e-d32ec5057dd7",
      "client-request-id": "b15e85c5-d517-4e9e-a99e-d32ec5057dd7",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"001\",\"RoleInstance\":\"PN3PEPF000002A8\"}}",
      "OData-Version": "4.0",
      "Date": "Thu, 05 Jun 2025 05:18:27 GMT"
    },
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "@odata.type": "#microsoft.graph.riskyUser",
          "id": "d1d4a5d4-a5d4-d1d4-d4a5-d4d1d4a5d4d1",
          "isDeleted": true,
          "isProcessing": true,
          "riskLastUpdatedDateTime": "2025-06-05T05:18:27Z",
          "riskLevel": "High",
          "riskState": "Active",
          "riskDetail": "Suspicious activity detected",
          "userDisplayName": "John Doe",
          "userPrincipalName": "johndoe@example.com"
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
    - **@odata.type** (string)
    - **id** (string)
    - **isDeleted** (boolean)
    - **isProcessing** (boolean)
    - **riskLastUpdatedDateTime** (string)
    - **riskLevel** (string)
    - **riskState** (string)
    - **riskDetail** (string)
    - **userDisplayName** (string)
    - **userPrincipalName** (string)
## Response Headers

| Header | Type |
|--------|------|
| Cache-Control | string |
| Transfer-Encoding | string |
| Content-Type | string |
| Content-Encoding | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| OData-Version | string |
| Date | string |