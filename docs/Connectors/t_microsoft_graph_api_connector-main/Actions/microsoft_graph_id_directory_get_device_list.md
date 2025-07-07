# Get Identity Directory Device List

**Description**: Retrieve registered devices from the Microsoft Graph Identity Directory with details like unique IDs and display names.

## Endpoint

- **URL:** `/v1.0/devices`
- **Method:** `GET`
## Inputs

- **parameters** (object): URL Query Parameters
  - **$filter** (string): Use the `filter` query parameter to retrieve just a subset of a collection. For guidance on using `filter`, see https://learn.microsoft.com/en-us/graph/filter-query-parameter
  - **$orderBy** (string): Use the `orderby` query parameter to specify the sort order of the items returned from Microsoft Graph.
  - **$top** (number): Sets the page size of results.
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.nextLink** (string)
  - **value** (array)
    - **id** (string)
    - **deletedDateTime** (object)
    - **accountEnabled** (boolean)
    - **approximateLastSignInDateTime** (string)
    - **complianceExpirationDateTime** (object)
    - **createdDateTime** (string)
    - **deviceCategory** (object)
    - **deviceId** (string)
    - **deviceMetadata** (object)
    - **deviceOwnership** (string)
    - **deviceVersion** (number)
    - **displayName** (string)
    - **domainName** (object)
    - **enrollmentProfileName** (object)
    - **enrollmentType** (string)
    - **externalSourceName** (object)
    - **isCompliant** (boolean)
    - **isManaged** (boolean)
    - **isRooted** (boolean)
    - **managementType** (string)
    - **manufacturer** (string)
    - **mdmAppId** (string)
    - **model** (string)
    - **onPremisesLastSyncDateTime** (object)
    - **onPremisesSyncEnabled** (object)
    - **operatingSystem** (string)
    - **operatingSystemVersion** (string)
    - **physicalIds** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **profileType** (string)
    - **registrationDateTime** (string)
    - **sourceType** (object)
    - **systemLabels** (array)
      - **file_name** (string) – Required
      - **file** (string) – Required
    - **trustType** (string)
    - **extensionAttributes** (object)
      - **extensionAttribute1** (object)
      - **extensionAttribute2** (object)
      - **extensionAttribute3** (object)
      - **extensionAttribute4** (object)
      - **extensionAttribute5** (object)
      - **extensionAttribute6** (object)
      - **extensionAttribute7** (object)
      - **extensionAttribute8** (object)
      - **extensionAttribute9** (object)
      - **extensionAttribute10** (object)
      - **extensionAttribute11** (object)
      - **extensionAttribute12** (object)
      - **extensionAttribute13** (object)
      - **extensionAttribute14** (object)
      - **extensionAttribute15** (object)
    - **alternativeSecurityIds** (array)
      - **type** (number)
      - **identityProvider** (object)
      - **key** (string)
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