# Deactivate Application By ID

**Description**: Deactivates an active application within Okta Identity Management using the specified application ID.

## Endpoint

- **URL:** `/api/v1/apps/{{appId}}/lifecycle/deactivate`
- **Method:** `POST`
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