# Change Account Credentials

**Description**: Initiates an immediate credential change for a specified account in CyberArk using the AccountID.

## Endpoint

- **URL:** `/PasswordVault/API/Accounts/{{AccountID}}/Change/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **AccountID** (string) – Required: The unique ID of the account.
- **json_body** (object)
  - **ChangeEntireGroup** (boolean): Whether or not the CPM will change the credentials in all the accounts that belong to the same group.
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