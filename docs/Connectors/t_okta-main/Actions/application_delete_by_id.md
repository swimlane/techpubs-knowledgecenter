# Delete Application By ID

**Description**: Removes an inactive application from Okta Identity Management using the specified application ID.

## Endpoint

- **URL:** `/api/v1/apps/{{appId}}`
- **Method:** `DELETE`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **appId** (string) – Required: Application ID.
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