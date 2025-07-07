# Get Threat Assessment List

**Description**: Retrieve and analyze threat assessments to enhance security posture using the Microsoft Graph Security API.

## Endpoint

- **URL:** `/v1.0/informationProtection/threatAssessmentRequests`
- **Method:** `GET`
## Inputs

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
    - **createdDateTime** (string)
    - **contentType** (string)
    - **expectedAssessment** (string)
    - **category** (string)
    - **status** (string)
    - **requestSource** (string)
    - **recipientEmail** (string)
    - **destinationRoutingReason** (string)
    - **contentData** (string)
    - **createdBy** (object)
      - **user** (object)
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
| OData-Version | string |
| Date | string |