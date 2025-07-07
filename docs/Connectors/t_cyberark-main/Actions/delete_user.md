# Delete User

**Description**: Removes a specified user from the CyberArk Vault by utilizing the provided UserID.

## Endpoint

- **URL:** `/PasswordVault/API/Users/{{UserID}}/`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **UserID** (string) – Required: The user's unique ID.
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