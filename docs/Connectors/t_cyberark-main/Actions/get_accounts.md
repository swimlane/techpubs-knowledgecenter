# Get Accounts

**Description**: Retrieve a comprehensive list of all accounts stored within the CyberArk Vault, providing an overview of credentials.

## Endpoint

- **URL:** `/PasswordVault/api/accounts`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **search** (string): A list of keywords to search for in accounts, separated by a space.
  - **searchType** (string): Get accounts that either contain or start with the value specified in the Search parameter.
  - **sort** (string): The property or properties that you want to sort returned accounts, followed by asc (default) or desc to control sort direction. Separate multiple properties with commas, up to a maximum of three properties.
  - **offset** (number): Offset of the first account that is returned in the collection of results.
  - **limit** (number): The maximum number of returned accounts. The maximum number that you can specify is 1000.
  - **filter** (string): Search for accounts using a filter.
  - **savedfilter** (string): Search for accounts using a saved filter(s).
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "id": "string",
      "name": "string",
      "address": "string",
      "userName": "string",
      "platformId": "string",
      "safeName": "string",
      "secretType": "key",
      "platformAccountProperties": {},
      "secretManagement": {
        "automaticManagementEnabled": true,
        "manualManagementReason": "string",
        "status": "inProcess",
        "lastModifiedTime": 0,
        "lastReconciledTime": 0,
        "lastVerifiedTime": 0
      },
      "remoteMachinesAccess": {
        "remoteMachines": "string",
        "accessRestrictedToRemoteMachines": true
      },
      "createdTime": 0,
      "categoryModificationTime": 111111111111111110000
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **id** (string)
  - **name** (string)
  - **address** (string)
  - **userName** (string)
  - **platformId** (string)
  - **safeName** (string)
  - **secretType** (string)
  - **platformAccountProperties** (object)
  - **secretManagement** (object)
    - **automaticManagementEnabled** (boolean)
    - **manualManagementReason** (string)
    - **status** (string)
    - **lastModifiedTime** (number)
    - **lastReconciledTime** (number)
    - **lastVerifiedTime** (number)
  - **remoteMachinesAccess** (object)
    - **remoteMachines** (string)
    - **accessRestrictedToRemoteMachines** (boolean)
  - **createdTime** (number)
  - **categoryModificationTime** (number)