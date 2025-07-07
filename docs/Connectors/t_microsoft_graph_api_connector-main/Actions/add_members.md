# Add Members

**Description**: Adds a new member to a group in Microsoft Graph API using the provided 'group-id' and member's '@odata.id'.

## Endpoint

- **URL:** `/v1.0/groups/{{group-id}}/members/$ref`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **group-id** (string) – Required: The ID of the group to which the member will be added.
- **json_body** (object) – Required
  - **@odata.id** (string) – Required: The ID of the directory object to add as a member.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json;odata.metadata=minimal;odata.streaming=true;IEEE754Compatible=false;charset=utf-8",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "f2584bdf-0295-424e-bdb1-2df08413c0c3",
      "client-request-id": "f2584bdf-0295-424e-bdb1-2df08413c0c3",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Central India\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"PN2PEPF00000273\"}}",
      "x-ms-resource-unit": "2",
      "OData-Version": "4.0",
      "Date": "Wed, 06 Nov 2024 15:54:59 GMT"
    },
    "reason": "OK"
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
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
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |