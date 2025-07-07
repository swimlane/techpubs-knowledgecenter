# Delete Software OATH Authentication Method

**Description**: Removes a user's Software OATH token authentication method in Microsoft Graph API using their email address and ID.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/softwareOathMethods/{{id}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **id** (string) – Required: The ID of the Software OATH token authentication method.
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