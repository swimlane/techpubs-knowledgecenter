# Activate Application By ID

**Description**: Activates an inactive application in Okta Identity Management using the provided application ID.

## Endpoint

- **URL:** `/api/v1/apps/{{appId}}/lifecycle/activate`
- **Method:** `POST`
## Inputs

- **path_parameters** (object) – Required: Path Parameters
  - **appId** (string) – Required: Application ID
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