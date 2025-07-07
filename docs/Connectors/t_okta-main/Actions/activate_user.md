# Activate User By ID

**Description**: Activates an Okta user account using the specified userId. A path parameter 'userId' is required.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/lifecycle/activate`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **userId** (string) – Required: ID of an existing Okta user.
- **parameters** (object): Query Parameters
  - **sendEmail** (boolean): Sends an activation email to the user if true.
## Output

### Example

```json
[
  {
    "status_code": 200,
    "response_headers": {
      "content-length": "140",
      "content-type": "application/json",
      "Date": "Wed, 8 Jan 2025 20:37:23 GMT"
    },
    "reason": "OK",
    "json": {
      "activationToken": "XE6wE17zmphl3KqAPFxO",
      "activationUrl": "https://{yourOktaDomain}/welcome/XE6wE17zmphl3KqAPFxO"
    }
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json** (object)
  - **activationToken** (string)
  - **activationUrl** (string)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |