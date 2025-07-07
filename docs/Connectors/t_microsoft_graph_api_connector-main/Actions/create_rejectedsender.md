# Create rejectedSender

**Description**: Adds a new user or group to the rejected sender list in Microsoft Graph API using the specified ID.

## Endpoint

- **URL:** `/v1.0/groups/{{id}}/rejectedSenders/$ref`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The unique identifier for the group.
- **json_body** (object) – Required
  - **@odata.id** (string) – Required: The ID of a user or group object.
## Output

### Example

```json
[
  {
    "status_code": 204,
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
    "reason": "No Content",
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