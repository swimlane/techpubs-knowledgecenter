# Remove User to Group

**Description**: Removes a specified user from a group in Okta Identity Management by using the provided groupId and userId.

## Endpoint

- **URL:** `/api/v1/groups/{{groupId}}/users/{{userId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **groupId** (string) – Required: Group ID.
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