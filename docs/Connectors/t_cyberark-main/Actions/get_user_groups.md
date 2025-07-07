# Get User Groups

**Description**: Retrieve a comprehensive list of user groups available within CyberArk for access management and control.

## Endpoint

- **URL:** `/PasswordVault/API/UserGroups/`
- **Method:** `GET`
## Inputs

- **parameters** (object)
  - **filter** (string): Filters according to the REST standard.
  - **sort** (string): Property or properties by which to sort returned users, followed by asc (default) or desc to control sort direction.
  - **search** (string): Searches according to the REST standard (searching with "contains"). Search matches when all search terms appear in the group name.
  - **includeMembers** (boolean): Whether or not to return members for each user group as part of the response.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "Success",
    "json_body": {
      "value": [
        {
          "id": 8,
          "groupType": "Vault",
          "members": [
            {
              "UserName": "Auditor",
              "id": 3
            }
          ],
          "groupName": "Auditors",
          "description": "Auditors group",
          "location": "\\"
        }
      ],
      "count": 1
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **value** (array)
    - **id** (number)
    - **groupType** (string)
    - **members** (array)
      - **UserName** (string)
      - **id** (number)
    - **groupName** (string)
    - **description** (string)
    - **location** (string)
  - **count** (number)