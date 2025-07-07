# Get Manager Root Level

**Description**: Retrieves the direct manager's root level details for a user or contact in Microsoft Graph API using their ID or userPrincipalName.

## Endpoint

- **URL:** `v1.0/users/{{id|userPrincipalName}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id|userPrincipalName** (string) – Required: The user's ID or UserPrincipalName
- **headers** (object)
  - **ConsistencyLevel** (string): Required when the request includes the $levels=n in the $expand query parameter.
- **parameters** (object)
  - **$levels** (string): The n value of $levels can be max (to return all managers) or a number between 1 and 1000.
  - **$select** (string): To select the individual Manager's properties.
  - **$expand** (string): To retrieve the Manager's Information for specified Levels, Selected ID and DisplayName.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **businessPhones** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **displayName** (string)
  - **givenName** (object)
  - **jobTitle** (object)
  - **mail** (string)
  - **mobilePhone** (object)
  - **officeLocation** (object)
  - **preferredLanguage** (object)
  - **surname** (object)
  - **userPrincipalName** (string)
  - **id** (string)
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