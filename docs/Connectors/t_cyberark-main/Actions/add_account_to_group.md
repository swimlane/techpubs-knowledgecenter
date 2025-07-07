# Add Account to Group

**Description**: Adds a specified account to an existing CyberArk group by utilizing the provided GroupID and AccountID.

## Endpoint

- **URL:** `/PasswordVault/API/AccountGroups/{{GroupID}}/Members/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **GroupID** (string) – Required: The unique ID of account group.
- **json_body** (object) – Required
  - **AccountID** (string) – Required: The ID of the account that will be added as a member to the group.
## Output

### Example

```json
[
  {
    "status_code": 201,
    "response_headers": {},
    "reason": "Created",
    "json_body": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (object)