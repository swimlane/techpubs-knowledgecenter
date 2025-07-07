# Get Secure Scores List

**Description**: Retrieve a list of Secure Scores from the Microsoft Graph Security API to assess your organization's security posture.

## Endpoint

- **URL:** `/v1.0/security/secureScores`
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
  - **@odata.nextLink** (string)
  - **value** (array)
    - **id** (string)
    - **azureTenantId** (string)
    - **activeUserCount** (number)
    - **createdDateTime** (string)
    - **currentScore** (number)
    - **enabledServices** (array)
    - **licensedUserCount** (number)
    - **maxScore** (number)
    - **vendorInformation** (object)
      - **provider** (string)
      - **providerVersion** (object)
      - **subProvider** (object)
      - **vendor** (string)
    - **averageComparativeScores** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **controlScores** (array)
      - **controlCategory** (string)
      - **controlName** (string)
      - **description** (object)
      - **score** (number)
      - **lastSynced** (string)
      - **scoreInPercentage** (number)
      - **count** (string)
      - **total** (string)
      - **implementationStatus** (string)
      - **IsEnforced** (string)
      - **IsApplicable** (string)
      - **controlState** (string)
      - **State** (string)
      - **on** (string)
      - **expiry** (string)
      - **source** (string)
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