# Get Identity Directory Role Members List

**Description**: Retrieve a list of members assigned to a specific directory role in Microsoft Graph API using the provided 'role-id'.

## Endpoint

- **URL:** `v1.0/directoryRoles/{{role-id}}/members`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **role-id** (string) – Required
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **@odata.type** (string)
    - **id** (string)
    - **businessPhones** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **displayName** (string)
    - **givenName** (string)
    - **jobTitle** (object)
    - **mail** (string)
    - **mobilePhone** (object)
    - **officeLocation** (object)
    - **preferredLanguage** (object)
    - **surname** (string)
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
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |