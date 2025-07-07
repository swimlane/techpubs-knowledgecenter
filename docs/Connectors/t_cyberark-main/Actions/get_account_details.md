# Get Account Details

**Description**: Retrieve specific account details from CyberArk using the unique account identifier (ID) provided in path parameters.

## Endpoint

- **URL:** `PasswordVault/API/Accounts/{{id}}/`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The account's unique ID.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "CategoryModificationTime": 1588049324,
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
      "createdTime": 0
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **CategoryModificationTime** (number)
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