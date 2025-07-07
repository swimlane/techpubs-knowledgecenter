# Verify Account Credentials

**Description**: Marks an account for verification in CyberArk using the provided AccountID as a path parameter.

## Endpoint

- **URL:** `/PasswordVault/API/Accounts/{{AccountID}}/Verify/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **AccountID** (string) – Required: The unique ID of the account.
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