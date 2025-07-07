# Get Directory Administrative Unit

**Description**: Retrieve details of a specified Directory Administrative Unit in Microsoft Graph API using its unique ID.

## Endpoint

- **URL:** `/v1.0/directory/administrativeUnits/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Unit ID
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
  - **id** (string)
  - **deletedDateTime** (object)
  - **displayName** (string)
  - **description** (object)
  - **isMemberManagementRestricted** (boolean)
  - **visibility** (object)
  - **membershipRule** (object)
  - **membershipType** (object)
  - **membershipRuleProcessingState** (object)
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