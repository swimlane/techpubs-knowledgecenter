# Update Account

**Description**: Updates an existing CyberArk account's details using the specified AccountID. Required inputs include path parameters and JSON body.

## Endpoint

- **URL:** `/PasswordVault/API/Accounts/{{AccountID}}/`
- **Method:** `PATCH`
## Inputs

- **path_parameters** (object) – Required
  - **AccountID** (string) – Required: The unique ID of the account to update.
- **json_body** (array) – Required
  - **op** (string): The allowed operations to perform on the properties.
  - **path** (string): The path of the property name.
  - **value** (string): The updated property value.
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
      "createdTime": 0
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