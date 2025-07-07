# Add Account

**Description**: Adds a new privileged account or SSH key to the CyberArk Vault with specified platformId and safeName.

## Endpoint

- **URL:** `/PasswordVault/api/Accounts`
- **Method:** `POST`
## Inputs

- **json_body** (object) – Required
  - **name** (string): The name of the account.
  - **address** (string): The name or address of the machine where the account will be used.
  - **userName** (string): Account user's name.
  - **platformId** (string) – Required: The platform assigned to this account.
  - **safeName** (string) – Required: The Safe where the account is created.
  - **secretType** (string): The type of password.
  - **secret** (string): The password value.
  - **platformAccountProperties** (object): The object containing key-value pairs to associate with the account, as defined by the account platform.
  - **secretManagement** (object)
    - **automaticManagementEnabled** (boolean): Whether the account secret is automatically managed by the CPM.
    - **manualManagementReason** (string): Reason for disabling automatic secret management.
    - **status** (string): Account management status.
    - **lastModifiedDateTime** (string): Last modified date of the account.
    - **lastReconciledDateTime** (string): Last reconciled date of the account.
    - **lastVerifiedDateTime** (string): Last verified date of the account.
  - **remoteMachinesAccess** (object)
    - **remoteMachines** (string): List of remote machines, separated by semicolons.
    - **accessRestrictedToRemoteMachines** (boolean): Whether or not to restrict access only to specified remote machines.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {},
    "reason": "Created",
    "json_body": {
      "name": "string",
      "address": "string",
      "userName": "string",
      "platformId": "string",
      "safeName": "string",
      "secretType": "key",
      "secret": "string",
      "platformAccountProperties": {},
      "secretManagement": {
        "automaticManagementEnabled": true,
        "manualManagementReason": "string"
      },
      "remoteMachinesAccess": {
        "remoteMachines": "string",
        "accessRestrictedToRemoteMachines": true
      }
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **name** (string)
  - **address** (string)
  - **userName** (string)
  - **platformId** (string)
  - **safeName** (string)
  - **secretType** (string)
  - **secret** (string)
  - **platformAccountProperties** (object)
  - **secretManagement** (object)
    - **automaticManagementEnabled** (boolean)
    - **manualManagementReason** (string)
  - **remoteMachinesAccess** (object)
    - **remoteMachines** (string)
    - **accessRestrictedToRemoteMachines** (boolean)