# Delete Phone Authentication Method

**Description**: Removes a user's phone authentication method in Microsoft Graph API using their email address and the specific phoneMethodId.

## Endpoint

- **URL:** `/v1.0/users/{{email_address}}/authentication/phoneMethods/{{phoneMethodId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required
  - **email_address** (string) – Required: The account associated with the email.
  - **phoneMethodId** (string) – Required: The ID of the phone authentication method. The Phone Method ID values correspond to deleting specific phone types are b6332ec1-7057-4abe-9331-3d72feddfe41 for alternateMobile, e37fc753-ff3b-4958-9484-eaa9425c82bc for office, and 3179e48a-750b-4051-897c-87b9720928f7 for mobile.
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