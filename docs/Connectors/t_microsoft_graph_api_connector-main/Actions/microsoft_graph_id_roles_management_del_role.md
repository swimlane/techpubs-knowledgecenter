# Delete Identity Directory Role Management

**Description**: Removes a specified directory role in Microsoft Graph API using the provided unique identifier.

## Endpoint

- **URL:** `/v1.0/roleManagement/directory/roleDefinitions/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Role Management ID
## Output

### Example

```json
[
  {
    "status_code": 404,
    "response_headers": {
      "Transfer-Encoding": "chunked",
      "Content-Type": "application/json",
      "Content-Encoding": "gzip",
      "Vary": "Accept-Encoding",
      "Strict-Transport-Security": "max-age=31536000",
      "request-id": "14c4462e-7088-48de-adf6-d6283055090d",
      "client-request-id": "14c4462e-7088-48de-adf6-d6283055090d",
      "x-ms-ags-diagnostic": "{\"ServerInfo\":{\"DataCenter\":\"Brazil South\",\"Slice\":\"E\",\"Ring\":\"3\",\"ScaleUnit\":\"002\",\"RoleInstance\":\"CP1PEPF00002F0F\"}}",
      "Date": "Tue, 20 Dec 2022 20:37:28 GMT"
    },
    "reason": "Not Found",
    "json_body": {
      "error": {
        "code": "ResourceNotFound",
        "message": "Invalid version: rolemanagement",
        "innerError": {
          "date": "2022-12-20T20:37:28",
          "request-id": "14c4462e-7088-48de-adf6-d6283055090d",
          "client-request-id": "14c4462e-7088-48de-adf6-d6283055090d"
        }
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **error** (object)
    - **code** (string)
    - **message** (string)
    - **innerError** (object)
      - **date** (string)
      - **request-id** (string)
      - **client-request-id** (string)
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