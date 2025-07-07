# Get Password Value

**Description**: Retrieves a password or SSH key for a specified account in CyberArk using the Account ID, optionally including a reason and ticket ID.

## Endpoint

- **URL:** `PasswordVault/API/Accounts/{{accountId}}/Password/Retrieve/`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required
  - **accountId** (string) – Required: The unique ID of the account.
- **json_body** (object) – Required
  - **reason** (string): The reason that is required to retrieve the password/SSH key.
  - **TicketingSystemName** (string): The name of the Ticketing System.
  - **TicketId** (string): The ticket ID of the ticketing system.
  - **Version** (number): The version number of the required password. If there are no previous versions, the current password/key version is returned. Valid values are any positive numbers.
  - **ActionType** (string): The action this password will be used for.
  - **isUse** (boolean): Internal parameter (for PSM for SSH only).
  - **Machine** (string): The address of the remote machine to connect to.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {},
    "reason": "OK",
    "json_body": "<myPassword>"
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json_body** (string)