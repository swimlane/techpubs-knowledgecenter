# Reset User Password

**Description**: Resets a CyberArk Vault user's password with a specified UserID and new password, ensuring secure access management.

## Endpoint

- **URL:** `/PasswordVault/API/Users/{{UserID}}/ResetPassword/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **UserID** (number) – Required: The user's unique ID.
- **json_body** (object) – Required
  - **newPassword** (string) – Required: The users new password.
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