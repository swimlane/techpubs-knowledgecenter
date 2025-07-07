# Force Password Reset

**Description**: Initiates a forced password reset for a specified user in Okta Identity Management, with an option to send a notification email.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/lifecycle/reset_password`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **userId** (string) – Required: User ID
- **parameters** (object) – Required: URL Query Parameters
  - **sendEmail** (boolean) – Required: When this is True, sends the reset link directly to the User's email, otherwise, the Url will be returned here
  - **revokeSessions** (boolean): Revokes all User sessions, except for the current session, if set to true.
## Output

### Example

```json
[
  {
    "status_code": 204,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Wed, 8 Jan 2025 20:37:23 GMT"
    },
    "reason": "OK",
    "json": {
      "summary": "Reset password without sending email",
      "resetPasswordUrl": "https://{yourOktaDomain}/reset_password/XE6wE17zmphl3KqAPFxO"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json** (object)
  - **summary** (string)
  - **resetPasswordUrl** (string)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |