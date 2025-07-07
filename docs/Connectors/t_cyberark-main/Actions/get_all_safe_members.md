# Get All Safe Members

**Description**: Retrieve all members associated with a specified CyberArk Safe, identified by the SafeUrlId.

## Endpoint

- **URL:** `PasswordVault/API/Safes/{{SafeUrlId}}/Members/`
- **Method:** `GET`
## Inputs

- **path_parameters** (object) – Required
  - **SafeUrlId** (string) – Required: The unique ID of the Safe used when calling Safe APIs.
- **parameters** (object)
  - **filter** (string): Filters are according to the REST standard.
  - **search** (string): Searches according to the Safe name.
  - **offset** (number): Offset of the first member that is returned in the collection of results.
  - **limit** (number): The maximum number of members that are returned.
  - **sort** (string): Sorts according to the memberName property in ascending order (default) or descending order to control the sort direction.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": {
      "value": [
        {
          "safeUrlId": "BZ_I_87",
          "safeName": "BZ_I_87",
          "safeNumber": 37,
          "memberId": "84425267_6da7_4c2c_9ad6_26aef85c83be",
          "memberName": "Master",
          "memberType": "User",
          "membershipExpirationDate": null,
          "isExpiredMembershipEnable": false,
          "isPredefinedUser": true,
          "permissions": {
            "useAccounts": true,
            "retrieveAccounts": true,
            "listAccounts": true,
            "addAccounts": true,
            "updateAccountContent": true,
            "updateAccountProperties": true,
            "initiateCPMAccountManagementOperations": true,
            "specifyNextAccountContent": true,
            "renameAccounts": true,
            "deleteAccounts": true,
            "unlockAccounts": true,
            "manageSafe": true,
            "manageSafeMembers": true,
            "backupSafe": true,
            "viewAuditLog": true,
            "viewSafeMembers": true,
            "accessWithoutConfirmation": true,
            "createFolders": true,
            "deleteFolders": true,
            "moveAccountsAndFolders": true,
            "requestsAuthorizationLevel1": false,
            "requestsAuthorizationLevel2": false
          }
        }
      ],
      "count": 8
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **safeUrlId** (string)
    - **safeName** (string)
    - **safeNumber** (number)
    - **memberId** (string)
    - **memberName** (string)
    - **memberType** (string)
    - **membershipExpirationDate** (object)
    - **isExpiredMembershipEnable** (boolean)
    - **isPredefinedUser** (boolean)
    - **permissions** (object)
      - **useAccounts** (boolean)
      - **retrieveAccounts** (boolean)
      - **listAccounts** (boolean)
      - **addAccounts** (boolean)
      - **updateAccountContent** (boolean)
      - **updateAccountProperties** (boolean)
      - **initiateCPMAccountManagementOperations** (boolean)
      - **specifyNextAccountContent** (boolean)
      - **renameAccounts** (boolean)
      - **deleteAccounts** (boolean)
      - **unlockAccounts** (boolean)
      - **manageSafe** (boolean)
      - **manageSafeMembers** (boolean)
      - **backupSafe** (boolean)
      - **viewAuditLog** (boolean)
      - **viewSafeMembers** (boolean)
      - **accessWithoutConfirmation** (boolean)
      - **createFolders** (boolean)
      - **deleteFolders** (boolean)
      - **moveAccountsAndFolders** (boolean)
      - **requestsAuthorizationLevel1** (boolean)
      - **requestsAuthorizationLevel2** (boolean)
  - **count** (number)