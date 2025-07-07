# Delete FIDO2 Authentication Method

**Description**: Removes a user's FIDO2 Security Key Authentication Method in Microsoft Graph API by using the specified email address and method ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/fido2Methods/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **id** (string) – Required: The ID of the FIDO2 Security Key authentication method.
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