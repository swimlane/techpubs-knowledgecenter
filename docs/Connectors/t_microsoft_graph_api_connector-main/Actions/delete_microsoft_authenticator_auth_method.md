# Delete Microsoft Authenticator Auth Method

**Description**: Removes a specific Microsoft Authenticator method for a user, identified by email address and authenticator ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/microsoftAuthenticatorMethods/{{microsoftAuthenticatorAuthenticationMethodId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **microsoftAuthenticatorAuthenticationMethodId** (string) – Required: The ID of the Microsoft Authenticator authentication method.
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