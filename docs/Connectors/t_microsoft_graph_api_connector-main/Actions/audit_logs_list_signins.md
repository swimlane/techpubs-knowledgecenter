# Audit Logs List SignIns

**Description**: Retrieve Microsoft Entra user sign-in logs to analyze access patterns and trends for a specified tenant.

## Endpoint

- **URL:** `/v1.0/auditLogs/signIns`
- **Method:** `GET`
## Inputs

- **parameters** (object): OData query parameters to help customize the response. Supports $top, $skiptoken and $filter.
  - **$top** (number): Sets the page size of results.
  - **$skiptoken** (string): Retrieves the next page of results from result sets that span multiple pages.
  - **$filter** (string): Filters results (rows).
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.nextLink** (string)
  - **value** (array)
    - **id** (string)
    - **createdDateTime** (string)
    - **userDisplayName** (string)
    - **userPrincipalName** (string)
    - **userId** (string)
    - **appId** (string)
    - **appDisplayName** (string)
    - **ipAddress** (string)
    - **clientAppUsed** (string)
    - **correlationId** (string)
    - **conditionalAccessStatus** (string)
    - **isInteractive** (boolean)
    - **riskDetail** (string)
    - **riskLevelAggregated** (string)
    - **riskLevelDuringSignIn** (string)
    - **riskState** (string)
    - **riskEventTypes** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **resourceDisplayName** (string)
    - **resourceId** (string)
    - **status** (object)
      - **errorCode** (number)
      - **failureReason** (object)
      - **additionalDetails** (object)
    - **deviceDetail** (object)
      - **deviceId** (string)
      - **displayName** (object)
      - **operatingSystem** (string)
      - **browser** (string)
      - **isCompliant** (object)
      - **isManaged** (object)
      - **trustType** (object)
    - **location** (object)
      - **city** (string)
      - **state** (string)
      - **countryOrRegion** (string)
      - **geoCoordinates** (object)
        - **altitude** (object)
        - **latitude** (number)
        - **longitude** (number)
    - **appliedConditionalAccessPolicies** (array)
      - **id** (string)
      - **displayName** (string)
      - **enforcedGrantControls** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **enforcedSessionControls** (array)
        - **file_name** (string) – Required
        - **file** (string) – Required
      - **result** (string)