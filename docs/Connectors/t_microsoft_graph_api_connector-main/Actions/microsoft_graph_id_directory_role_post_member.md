# Create Identity Directory Role Member

**Description**: Adds a new member to a specified directory role in Microsoft Graph API using the role's unique ID and the member's resource identifier.

## Endpoint

- **URL:** `/v1.0/directoryRoles/{{id}}/members/$ref`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Directory Role ID
- **json_body** (object) – Required: JSON Body
  - **@odata.id** (string) – Required: OData ID Type User
## Output

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