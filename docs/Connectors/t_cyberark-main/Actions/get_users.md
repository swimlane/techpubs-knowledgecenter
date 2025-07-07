# Get Users

**Description**: Retrieves a list of all users in the CyberArk Vault, excluding Master and Batch built-in users.

## Endpoint

- **URL:** `/PasswordVault/API/Users/`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **filter** (string): Filters according to the REST standard. Search for users using the following filters userType, componentUser and userName.
  - **sort** (string): Property or properties by which to sort returned users, followed by asc (default) or desc to control sort direction.
  - **search** (string): Search using the following values username, firstname and lastname.
  - **ExtendedDetails** (boolean): Returns additional user details as user groups and userDN for LDAP users.
  - **pageOffset** (number): Offsets the first user that is returned in the results.
  - **pageSize** (number): When used together with the Offset parameter, this value determines the maximum number of users to return.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "Users": [
        {
          "id": 2,
          "username": "Administrator",
          "source": "CyberArk",
          "userType": "Built-InAdmins",
          "componentUser": false,
          "groupsMembership": [
            {
              "groupID": 16,
              "groupName": "PVWAMonitor",
              "groupType": "Vault"
            },
            {
              "groupID": 17,
              "groupName": "PVWAUsers",
              "groupType": "Vault"
            },
            {
              "groupID": 11,
              "groupName": "Vault Admins",
              "groupType": "Vault"
            }
          ],
          "vaultAuthorization": [
            "AddUpdateUsers",
            "AddSafes",
            "AddNetworkAreas",
            "ManageDirectoryMapping",
            "ManageServerFileCategories",
            "AuditUsers",
            "BackupAllSafes",
            "RestoreAllSafes",
            "ResetUsersPasswords",
            "ActivateUsers"
          ],
          "location": "\\",
          "personalDetails": {
            "firstName": "Jen",
            "middleName": "R",
            "lastName": "Grey"
          }
        }
      ],
      "Total": 1
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **Users** (array)
    - **id** (number)
    - **username** (string)
    - **source** (string)
    - **userType** (string)
    - **componentUser** (boolean)
    - **groupsMembership** (array)
      - **groupID** (number)
      - **groupName** (string)
      - **groupType** (string)
    - **vaultAuthorization** (array)
    - **location** (string)
    - **personalDetails** (object)
      - **firstName** (string)
      - **middleName** (string)
      - **lastName** (string)
  - **Total** (number)