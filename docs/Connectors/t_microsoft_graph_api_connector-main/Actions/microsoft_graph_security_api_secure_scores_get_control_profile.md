# Get Control Profile

**Description**: Retrieve a detailed security control profile by its unique ID from the Microsoft Graph Security API.

## Endpoint

- **URL:** `/v1.0/security/secureScoreControlProfiles/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Control Profile ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
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