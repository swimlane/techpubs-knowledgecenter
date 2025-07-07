# Clear User Session

**Description**: Terminate a specific user's session in Okta Identity Management without affecting sessions for web or native apps.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/sessions`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **userId** (string) – Required: User ID.
- **parameters** (object): Query Parameters
  - **oauthTokens** (boolean): Revoke issued OpenID Connect and OAuth refresh and access tokens.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "reason": "Ok",
    "headers": null,
    "response": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **headers** (object)
- **response** (object)