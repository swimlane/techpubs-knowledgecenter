# Get User by ID

**Description**: Retrieve detailed information for a specific user by their unique ID in Microsoft Graph API.

## Endpoint

- **URL:** `v1.0/users/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required
- **parameters** (object)
  - **$select** (string)
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **businessPhones** (array)
  - **displayName** (string)
  - **givenName** (string)
  - **jobTitle** (string)
  - **mail** (string)
  - **mobilePhone** (string)
  - **officeLocation** (string)
  - **preferredLanguage** (string)
  - **surname** (string)
  - **userPrincipalName** (string)
  - **id** (string)