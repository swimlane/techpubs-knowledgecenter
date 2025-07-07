# Get Identity Directory Objects by IDs List

**Description**: Retrieve specific directory objects such as users or groups from Microsoft Graph API by supplying 'ids' and 'types'.

## Endpoint

- **URL:** `/v1.0/directoryObjects/getByIds`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required: JSON Body
  - **ids** (array) – Required: A collection of IDs for which to return objects. The IDs are GUIDs, represented as strings. You can specify up to 1000 IDs
  - **types** (array) – Required: A collection of resource types that specifies the set of resource collections to search, for example `user`, `group`, and device objects
## Output

### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **@odata.context** (string)
  - **value** (array)
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
| Location | string |
| Vary | string |
| Strict-Transport-Security | string |
| request-id | string |
| client-request-id | string |
| x-ms-ags-diagnostic | string |
| x-ms-resource-unit | string |
| OData-Version | string |
| Date | string |