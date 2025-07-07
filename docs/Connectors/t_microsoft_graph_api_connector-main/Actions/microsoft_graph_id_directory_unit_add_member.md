# Add Directory Administrative Unit Member

**Description**: Adds a member to a specified Directory Administrative Unit in Microsoft Graph API using the provided unit ID and member's @odata.id.

## Endpoint

- **URL:** `/v1.0/directory/administrativeUnits/{{id}}/members/$ref`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Unit ID
- **json_body** (object) – Required: JSON Body
  - **@odata.id** (string) – Required: The OData id of the user, group or DirectoryObject to add
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