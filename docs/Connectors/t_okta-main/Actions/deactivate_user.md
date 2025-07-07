# Deactivate User By ID

**Description**: Deactivates an Okta user account using the specified userId. A path parameter 'userId' is required.

## Endpoint

- **URL:** `/api/v1/users/{{userId}}/lifecycle/deactivate`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **userId** (string) – Required: User ID.
- **parameters** (object): Query Parameters
  - **sendEmail** (boolean): Sends a deactivation email to the admin if true.
- **headers** (object): Headers
  - **Prefer** (string): Request asynchronous processing.
## Output

### Example

```json
[
  {
    "status_code": 200,
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