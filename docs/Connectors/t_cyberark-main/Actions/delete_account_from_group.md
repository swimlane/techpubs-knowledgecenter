# Delete Account from Group

**Description**: Removes a specified account from a CyberArk group using the provided GroupID and AccountID.

## Endpoint

- **URL:** `/PasswordVault/API/AccountGroups/{{GroupID}}/Members/{{AccountID}}/`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **GroupID** (string) – Required: The unique ID of the group.
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