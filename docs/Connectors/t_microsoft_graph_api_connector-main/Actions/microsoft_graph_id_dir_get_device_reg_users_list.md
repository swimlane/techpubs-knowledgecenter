# Get Identity Directory Device Registered User List

**Description**: Retrieve a list of users registered to a specific device in Microsoft Graph API using the device's unique 'id'.

## Endpoint

- **URL:** `/v1.0/devices/{{id}}/registeredUsers`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Device ID
- **parameters** (object): URL Query Parameters
  - **filter** (string): Use the `filter` query parameter to retrieve just a subset of a collection. For guidance on using `filter`, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderBy** (string): Use the `orderby` query parameter to specify the sort order of the items returned from Microsoft Graph.
  - **top** (number): Sets the page size of results.
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
    - **displayName** (string)
    - **givenName** (string)
    - **jobTitle** (object)
    - **mail** (object)
    - **mobilePhone** (object)
    - **officeLocation** (object)
    - **preferredLanguage** (string)
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