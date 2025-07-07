# Add user to Group

**Description**: Adds a specified user to a group in Okta Identity Management using the provided groupId and userId.

## Endpoint

- **URL:** `/api/v1/groups/{{groupId}}/users/{{userId}}`
- **Method:** `PUT`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **groupId** (string) – Required: Group ID.
  - **userId** (string) – Required: User ID.
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