# Get Identity Directory Object

**Description**: Retrieves a specific directory object from Microsoft Graph API using a unique identifier.

## Endpoint

- **URL:** `/v1.0/directoryObjects/{{id}}`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **id** (string) – Required: Directory Object ID
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **@odata.type** (string)
  - **id** (string)
  - **deletedDateTime** (object)
  - **classification** (object)
  - **createdDateTime** (string)
  - **creationOptions** (array)
  - **description** (string)
  - **displayName** (string)
  - **expirationDateTime** (object)
  - **groupTypes** (array)
  - **isAssignableToRole** (object)
  - **mail** (string)
  - **mailEnabled** (boolean)
  - **mailNickname** (string)
  - **membershipRule** (object)
  - **membershipRuleProcessingState** (object)
  - **onPremisesDomainName** (object)
  - **onPremisesLastSyncDateTime** (object)
  - **onPremisesNetBiosName** (object)
  - **onPremisesSamAccountName** (object)
  - **onPremisesSecurityIdentifier** (object)
  - **onPremisesSyncEnabled** (object)
  - **preferredDataLocation** (object)
  - **preferredLanguage** (object)
  - **proxyAddresses** (array)
  - **renewedDateTime** (string)
  - **resourceBehaviorOptions** (array)
  - **resourceProvisioningOptions** (array)
    - **file_name** (string) – Required
    - **file** (string) – Required
  - **securityEnabled** (boolean)
  - **securityIdentifier** (string)
  - **theme** (object)
  - **visibility** (string)
  - **onPremisesProvisioningErrors** (array)
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