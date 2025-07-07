# Get Identity Directory Device Groups List

**Description**: Retrieve groups associated with a specific device using its directory ID in Microsoft Graph API; requires 'id' path parameter.

## Endpoint

- **URL:** `/v1.0/devices/{{id}}/memberOf`
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
    - **file_name** (string) – Required
    - **file** (string) – Required
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