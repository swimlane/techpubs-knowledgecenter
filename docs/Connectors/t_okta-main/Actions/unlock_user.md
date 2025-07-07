# Unlock User By ID

**Description**: Unlocks an Okta user account with LOCKED_OUT status or allows sign-in from unknown devices for ACTIVE users.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/lifecycle/unlock`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **userId** (string) – Required: ID of an existing Okta user.
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
    "json": {}
  }
]
```
### Output Parameters

- **status_code** (number)
- **reason** (string)
- **json** (object)
## Response Headers

| Header | Type |
|--------|------|
| content-length | string |
| content-type | string |
| Date | string |