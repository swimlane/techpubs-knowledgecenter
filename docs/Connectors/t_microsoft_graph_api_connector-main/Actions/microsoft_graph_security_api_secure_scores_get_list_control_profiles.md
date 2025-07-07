# Get Secure Control Profiles

**Description**: Retrieve Secure Control Profiles to assess and improve your organization's security posture using Microsoft Graph Security API.

## Endpoint

- **URL:** `/v1.0/security/secureScoreControlProfiles`
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
    - **actionType** (string)
    - **actionUrl** (string)
    - **controlCategory** (string)
    - **title** (string)
    - **deprecated** (boolean)
    - **implementationCost** (string)
    - **lastModifiedDateTime** (object)
    - **maxScore** (number)
    - **rank** (number)
    - **remediation** (string)
    - **remediationImpact** (string)
    - **service** (string)
    - **threats** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **tier** (string)
    - **userImpact** (string)
    - **vendorInformation** (object)
      - **provider** (string)
      - **providerVersion** (object)
      - **subProvider** (object)
      - **vendor** (string)
    - **complianceInformation** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **controlStateUpdates** (array)
      - **assignedTo** (object)
      - **comment** (object)
      - **state** (string)
      - **updatedBy** (object)
      - **updatedDateTime** (object)
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