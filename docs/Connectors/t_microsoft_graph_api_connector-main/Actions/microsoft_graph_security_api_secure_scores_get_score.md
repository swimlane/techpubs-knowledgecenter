# Get Secure Score

**Description**: Retrieves a specified secure score from the Microsoft Graph Security API using the provided 'id'.

## Endpoint

- **URL:** `/v1.0/security/secureScores/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Secure Score ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
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
    - **description** (string)
    - **score** (number)
    - **IsApplicable** (string)
    - **scoreInPercentage** (number)
    - **controlState** (string)
    - **total** (string)
    - **IsEnforced** (string)
    - **implementationStatus** (string)
    - **lastSynced** (string)
    - **count** (string)
    - **State** (string)
    - **on** (string)
    - **expiry** (string)
    - **source** (string)
    - **noPolicies** (string)
    - **mdoImplementationStatus** (string)
    - **state** (string)
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