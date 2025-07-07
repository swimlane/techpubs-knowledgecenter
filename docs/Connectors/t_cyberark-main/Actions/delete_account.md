# Delete Account

**Description**: Permanently removes a specified account from the CyberArk Vault using the unique account ID provided in path parameters.

## Endpoint

- **URL:** `/PasswordVault/API/Accounts/{{id}}/`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **id** (string) – Required: The account's unique ID, composed of the SafeID and internal AccountID of the account to delete.
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