# Delete Identity Directory Domain

**Description**: Removes a specified domain from a Microsoft tenant using the unique domain ID.

## Endpoint

- **URL:** `v1.0/domains/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "Cache-Control": "no-cache",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "6519e78a-5079-483c-ab75-deb904ddda8b",
      "client-request-id": "6519e78a-5079-483c-ab75-deb904ddda8b",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"South Central US\",\"Slice\":\"E\",\"Ring\":\"5\",\"ScaleUnit\":\"000\",\"RoleInstance\":\"SN1PEPF00008F01\"}}",
      "x-ms-resource-unit": "1",
      "Date": "Tue, 20 Dec 2022 19:33:55 GMT"
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
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| Date | string |