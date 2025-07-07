# Delete Windows Hello For Business Auth Method

**Description**: Removes a specified Windows Hello For Business authentication method for a user using their email address and method ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/windowsHelloForBusinessMethods/{{windowsHelloForBusinessAuthenticationMethodId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **windowsHelloForBusinessAuthenticationMethodId** (string) – Required: The ID of the Windows Hello For Business authentication method.
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