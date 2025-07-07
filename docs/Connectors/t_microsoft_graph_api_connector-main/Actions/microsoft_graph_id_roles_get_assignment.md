# Get Identity Directory Role Assignment Member

**Description**: Retrieve directory role assignment details for a specified identity in Microsoft Graph API using the unique identifier.

## Endpoint

- **URL:** `/v1.0/roleManagement/directory/roleAssignments/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Role Assignment ID
## Output

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
| Date | string |