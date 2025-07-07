# Get a User

**Description**: Retrieves a user account from Microsoft Graph API using the sign-in name to access user data seamlessly.

## Endpoint

- **URL:** `/v1.0/users`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **$select** (string): Select results.
  - **$filter** (string): Filters results (rows).
  - **$count** (boolean): Include count of items.
  - **$expand** (string): Expand related entities.
  - **$orderby** (string): Order items by property values.
  - **$search** (string): Search items by search phrases.
  - **$top** (integer): Show only the first n items.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
    - **businessPhones** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **displayName** (string)
    - **givenName** (object)
    - **jobTitle** (object)
    - **mail** (object)
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