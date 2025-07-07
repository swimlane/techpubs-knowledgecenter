# Delete Email Authentication Method

**Description**: Removes a specified Email Authentication Method for a user in Microsoft Graph API using their email address and method ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/emailMethods/{{emailMethods-id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **emailMethods-id** (string) – Required: The ID of the email authentication method, referenced by {emailMethods-id}, is always 3ddfcfc8-9383-446f-83cc-3ab9be4be18f. Delete the email method from your own account. For a signed-in user to update their own authentication method, they must have satisfied a multi-factor authentication requirement during sign in.
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