# Remove User from Group

**Description**: Removes a specified user from a CyberArk Vault user group by utilizing the provided groupID and member details.

## Endpoint

- **URL:** `/PasswordVault/API/UserGroups/{{groupID}}/Members/{{member}}/`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **groupID** (string) – Required: The unique ID of the group.
  - **member** (string) – Required: The name of the group member to be removed.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {},
    "reason": "No Content",
    "response_text": ""
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **response_text** (string)