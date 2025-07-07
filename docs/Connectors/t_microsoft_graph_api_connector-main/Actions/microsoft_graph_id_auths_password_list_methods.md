# List Password Methods

**Description**: Retrieve registered password authentication methods for a user in Microsoft Graph API by their User ID.

## Endpoint

- **URL:** `/v1.0/users/{{id}}/authentication/passwordMethods`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: User ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **id** (string)
    - **password** (object)
    - **creationDateTime** (object)
    - **createdDateTime** (object)
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
| Link | string |
| Deprecation | string |
| Sunset | string |
| OData-Version | string |
| Date | string |