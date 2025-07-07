# Add User to Group

**Description**: Adds a user to a CyberArk Vault group by using the group's ID and the user's member ID.

## Endpoint

- **URL:** `/PasswordVault/API/UserGroups/{{id}}/Members/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The unique ID of the Vault group.
- **json_body** (object) – Required
  - **memberId** (string) – Required: The name of the Vault user or LDAP group to add to the Vault group.
  - **memberType** (string): The type of user being added to the Vault group. This differentiates members who are domain users from members who are Vault users.
  - **domainName** (string): The dns address of the domain.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {},
    "reason": "Created",
    "json_body": {
      "memberId": "string",
      "memberType": "Vault",
      "domainName": "string"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)
  - **memberId** (string)
  - **memberType** (string)
  - **domainName** (string)