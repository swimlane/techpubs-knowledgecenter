# Suspend User By ID

**Description**: Suspends an Okta user account based on the provided userId. This action is essential for quickly disabling access when needed.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/lifecycle/suspend`
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