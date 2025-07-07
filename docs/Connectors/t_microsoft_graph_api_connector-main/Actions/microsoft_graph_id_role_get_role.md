# Get Identity Directory Role

**Description**: Retrieve details for a specific directory role in Microsoft Graph API using the unique ID provided.

## Endpoint

- **URL:** `/v1.0/directoryRoles/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Directory Role ID
- **parameters** (object): URL Query Parameters
  - **count** (string): Include a count of the total number of items in a collection alongside the page of data values returned from Microsoft Graph
  - **filter** (string): Use the $filter query parameter to retrieve just a subset of a collection. For guidance on using $filter, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **orderby** (string): To sort the results in ascending or descending order, append either asc or desc to the field name, separated by a space.
  - **top** (number): Sets the page size of results
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **id** (string)
  - **deletedDateTime** (object)
  - **description** (string)
  - **displayName** (string)
  - **roleTemplateId** (string)
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