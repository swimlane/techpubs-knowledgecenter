# Delete Temporary Access Pass Auth Method

**Description**: Removes a user's Temporary Access Pass Authentication Method in Microsoft Graph API using their email address and ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/temporaryAccessPassMethods/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **id** (string) – Required: The ID of the Temporary Access Pass authentication method.
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